# CA-E-826@1
"""Opt-in live lifecycle exercise. Review before running: this writes a temporary Scope Unit."""
import asyncio
from datetime import datetime
from statistics import median
import hashlib
import json
import os
from pathlib import Path
import random
import sys
import time
import tomllib
import unittest
from unittest.mock import AsyncMock
from types import SimpleNamespace
from urllib.parse import urlparse
from uuid import uuid4

from mcp.client.session import ClientSession
from mcp.client.streamable_http import streamable_http_client

ROOT = Path(__file__).resolve().parents[5]
PROGRAM = ROOT / 'LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC'
sys.path[:0] = [str(PROGRAM / 'FEATURE_TOOLS'), str(PROGRAM / 'FEATURE_APPS/APP_WORKBENCH/tests')]
from workbench_live_canary_support import (CanaryScope, atomic_publish, authority_path,  # noqa: E402
    declaration_target, new_atom_id, new_scope_unit_id, remove_owned_file,
    scope_authority, scope_carrier, stage_carrier, write_scope_declaration)
from project_settings_values import control_root  # noqa: E402
from scope_unit_declarations import read_scope_unit_declarations  # noqa: E402
from VALIDATE_ATOMS.validate_atoms_workers.parsing import parse_carrier  # noqa: E402
from carrier_aliases import carrier_read_view  # noqa: E402

OUT = ROOT / '.caprmedio_tmp/workbench/lifecycle-live-canary'
ENDPOINT = os.environ.get('CAPRMEDIO_LIVE_LIFECYCLE_URL', '')
SEED = int(os.environ.get('CAPRMEDIO_RANDOM_SEED', '3005'))
CALL_TIMEOUT = int(os.environ.get('CAPRMEDIO_LIVE_CALL_TIMEOUT', '15'))
PARENT = 'WORKBENCH_BACKEND'

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def snapshot(path):
    if not path.exists():
        return {}
    if path.is_symlink() or any(p.is_symlink() for p in path.rglob('*')):
        raise RuntimeError('symlink in test Scope Unit')
    return {p.relative_to(path).as_posix(): digest(p) for p in path.rglob('*') if p.is_file()}

def read(path):
    parsed = parse_carrier(path.read_bytes(), path)
    return carrier_read_view(parsed.metadata), parsed.body

def case_matrix(rng):
    """Balance both update variants and both direct-update/status orders."""
    choices = [{'priority': rng.choice(('Low', 'Medium', 'High')),
                'draft_direct_update': bool(i & 1),
                'status_first': bool(i & 2),
                'replacement': i < 10} for i in range(20)]
    rng.shuffle(choices)
    return choices


def record_timing(report, tool, seconds, arguments):
    def add(timing, name):
        samples = timing.setdefault(name, {}).setdefault('samples', [])
        samples.append(seconds)
        timing[name].update(count=len(samples), p50=median(samples), max=max(samples))

    timing = report.setdefault('timing_seconds', {})
    add(timing, tool)
    if tool == 'update':
        variant = 'summary_replacement' if 'summary' in arguments['changes'] else 'body_revision'
        add(report.setdefault('update_variant_timing_seconds', {}), variant)
    elif tool == 'direct_update':
        variant = 'draft' if '@' in arguments['target']['ref_id'] else 'current'
        add(report.setdefault('direct_update_variant_timing_seconds', {}), variant)


async def load_archive_scope(client, scope_name):
    expected = {'scope_unit': scope_name, 'role': 'Concern'}
    result = await asyncio.wait_for(client.call_tool('workbench_archive_load', {
        'project_root': str(ROOT), 'scopes': [expected],
    }), CALL_TIMEOUT)
    if (result.is_error or not isinstance(result.structured_content, dict)
            or expected not in result.structured_content.get('loaded_archive_scopes', [])):
        raise RuntimeError(f'Could not load the canary Archive: {result}')
    return result.structured_content['loaded_archive_scopes']


async def main():  # noqa: C901 -- ordered live workflow and ownership checks
    if os.environ.get('CAPRMEDIO_LIVE_LIFECYCLE') != '1':
        raise RuntimeError('Explicit CAPRMEDIO_LIVE_LIFECYCLE=1 required')
    configured_root = os.environ.get('CAPRMEDIO_LIVE_LIFECYCLE_ROOT', '')
    url = urlparse(ENDPOINT)
    if not configured_root or Path(configured_root).resolve() != ROOT.resolve():
        raise RuntimeError('Explicit current Project root required')
    if url.scheme != 'http' or url.hostname not in ('127.0.0.1', 'localhost') or not url.port:
        raise RuntimeError('Explicit loopback MCP endpoint required')
    OUT.mkdir(parents=True, exist_ok=True)
    rng = random.Random(SEED)
    control = control_root(ROOT)
    declarations = read_scope_unit_declarations(ROOT, control)
    parent = authority_path(declarations, ROOT, PARENT)
    token = uuid4().hex[:10].upper()
    scope = CanaryScope('RANDOM_' + token, new_scope_unit_id({x.scope_unit_id for x in declarations.units}),
                        new_atom_id(ROOT, set()), PARENT)
    target = declaration_target(parent, scope)
    authority = scope_authority(parent, scope)
    if authority.exists() or scope.name in declarations.by_name or target.exists():
        raise RuntimeError('Scope collision')
    report = {'seed': SEED, 'scope': scope.__dict__, 'endpoint': ENDPOINT,
              'operations': [], 'outcome': 'starting', 'call_timeout_seconds': CALL_TIMEOUT,
              'started': datetime.now().astimezone().isoformat()}
    report_path = OUT / ('report-' + token + '.json')
    owned_decl = None
    expected_files = {}
    successful = False
    def save():
        report_path.write_text(json.dumps(report, indent=2, default=str) + '\n')
    save()
    async def reject_elicitation(_context, _params):
        raise AssertionError('Lifecycle must return input errors through MCP')

    try:
        async with streamable_http_client(ENDPOINT) as streams:
            async with ClientSession(*streams[:2], read_timeout_seconds=600, elicitation_callback=reject_elicitation) as client:
                await client.initialize()
                required = {'atom_lifecycle_' + s for s in ('create_draft', 'promote_draft', 'direct_update', 'change_status', 'update', 'archive')}
                names = {t.name for t in (await client.list_tools()).tools}
                if not (required | {'query_run', 'workbench_archive_load'}) <= names:
                    raise RuntimeError('Live server lacks required tools')
                async def query(sql):
                    result = await asyncio.wait_for(client.call_tool('query_run', {'project_root': str(ROOT), 'sql': sql, 'save': False, 'result_delivery': 'inline'}), 120)
                    if result.is_error or not isinstance(result.structured_content, dict):
                        raise RuntimeError(f'Query failed: {result}')
                    return result.structured_content['rows']
                async def wait_rows(sql, predicate, phase):
                    start = time.monotonic()
                    last = None
                    while time.monotonic() - start < 90:
                        last = await query(sql)
                        if predicate(last):
                            report.setdefault('visibility_seconds', {})[phase] = time.monotonic() - start
                            save()
                            return
                        await asyncio.sleep(.5)
                    raise TimeoutError(f'{phase}: last rows {last!r}')
                async def invoke(name, args, status='completed'):
                    nonlocal expected_files
                    entry = {'tool': name, 'arguments': args}
                    report['operations'].append(entry)
                    save()
                    start = time.monotonic()
                    try:
                        result = await asyncio.wait_for(client.call_tool('atom_lifecycle_' + name, args), CALL_TIMEOUT)
                    except TimeoutError:
                        entry['seconds'] = time.monotonic() - start
                        save()
                        raise
                    entry.update(seconds=time.monotonic()-start, result=result.model_dump(mode='json'))
                    if status == 'completed' and not result.is_error and isinstance(result.structured_content, dict) and result.structured_content.get('status') == status:
                        record_timing(report, name, entry['seconds'], args)
                    save()
                    if result.is_error or not isinstance(result.structured_content, dict) or result.structured_content.get('status') != status:
                        raise RuntimeError(f'{name}: unexpected result {result}')
                    expected_files = snapshot(authority)
                    print(f"{name}: {status} ({entry['seconds']:.2f}s)", flush=True)
                    return result.structured_content
                scope_sql = f"SELECT name FROM scope_units WHERE scope_unit_id = '{scope.scope_unit_id}'"
                project_name = tomllib.loads((control / 'caprmedio_project_settings.toml').read_text())['project']['name']
                staged = stage_carrier(OUT, scope.atom_id, scope_carrier(scope, project_name, '2026-11-06 00:00:00 +0000'))
                try:
                    write_scope_declaration(staged, scope, project_name)
                    owned_decl = atomic_publish(staged, target)
                finally:
                    staged.unlink(missing_ok=True)
                report['declaration'] = str(target)
                save()
                await wait_rows(scope_sql, lambda rows: rows == [[scope.name]], 'scope_created')
                report['loaded_archive_scopes'] = await load_archive_scope(client, scope.name)
                save()
                before = snapshot(authority)
                pending = await invoke('create_draft', {'newAtom': {'role': 'Concern', 'scope_unit': scope.name}},
                                       'needs_input')
                assert pending['requested_input'] and pending['errors']
                await invoke('create_draft', {'cancel': True}, 'cancelled')
                if snapshot(authority) != before:
                    raise AssertionError('Cancellation did not leave Scope Unit unchanged')

                choices = case_matrix(rng)
                report['choices'] = choices
                save()
                print(f"{scope.name} seed={SEED}; {len(choices)} Atoms", flush=True)
                for index, choice in enumerate(choices):
                    summary = f'Random lifecycle {token} case {index:02}'
                    body = f'## Summary\n\n{summary}\n\n## Concern\n\nInitial {token}.\n'
                    inputs = {'role': 'Concern', 'form': 'Problem', 'scope_unit': scope.name,
                              'body': body, 'tier': 3, 'priority': choice['priority'],
                              'topics': {'main_subject': 'Atom'}}
                    if index == 0:
                        missing_form = {key: value for key, value in inputs.items() if key not in {'form', 'priority'}}
                        pending = await invoke('create_draft', {'newAtom': missing_form}, 'needs_input')
                        assert 'form' in pending['requested_input']
                        await invoke('create_draft', {'form': inputs['form'], 'priority': inputs['priority']})
                    else:
                        await invoke('create_draft', {'newAtom': inputs})
                    drafts = list(authority.rglob('CA-C-*@1-draft-*.md'))
                    if len(drafts) != 1:
                        raise AssertionError(f'Expected one draft: {drafts}')
                    draft = drafts[0]
                    view, _ = read(draft)
                    atom_id = view['atom_id']
                    assert view['status'].lower() == 'draft' and view['version'] == 1
                    assert view['priority'].casefold() == choice['priority'].casefold()
                    assert datetime.fromisoformat(str(view['updated_at'])).utcoffset() is not None
                    assert view['destination']['file'] == {'name': draft.name, 'path': draft.parent.relative_to(ROOT).as_posix()}
                    draft_time = view['updated_at']
                    atom_sql = f"SELECT reference, status_group FROM atoms WHERE filename LIKE '{atom_id}-%' OR filename LIKE '{atom_id}@%'"
                    await wait_rows(atom_sql, lambda rows: any(row[1] == 'Draft' for row in rows), f'draft_{index}')
                    draft_ref = {'ref_id': atom_id + '@1-draft', 'version': 1}
                    if choice['draft_direct_update']:
                        await invoke('direct_update', {'target': draft_ref, 'changes': {'body': body.replace('Initial', 'Edited')}})
                        after, content = read(draft)
                        assert after['version'] == 1 and after['updated_at'] == draft_time and 'Edited' in content
                    await invoke('promote_draft', {'target': draft_ref, 'targetStatus': 'Active'})
                    assert not draft.exists()
                    current, = list((authority / '01_concern').glob(atom_id + '-*.md'))
                    view, _ = read(current)
                    assert view['atom_id'] == atom_id and view['status'].lower() == 'active' and view['version'] == 1
                    assert view['updated_at'] == draft_time
                    assert view['destination']['file'] == {'name': current.name, 'path': current.parent.relative_to(ROOT).as_posix()}
                    await wait_rows(atom_sql, lambda rows: any(row[1] == 'Current' for row in rows) and not any(row[1] == 'Draft' for row in rows), f'current_{index}')
                    selector = {'ref_id': atom_id, 'version': 1}
                    if index == 0:
                        unchanged = snapshot(authority)
                        rejected = await invoke('change_status', {'target': {'ref_id': atom_id, 'version': 2}, 'targetStatus': 'Resolved'}, 'failed')
                        assert any(error['code'] == 'source_selection_failed' for error in rejected['errors']), rejected
                        assert snapshot(authority) == unchanged
                    if not choice['draft_direct_update']:
                        oldtime = view['updated_at']
                        await invoke('direct_update', {'target': selector, 'changes': {'body': body.replace('Initial', 'Edited')}})
                        view, content = read(current)
                        assert view['version'] == 1 and view['updated_at'] == oldtime and 'Edited' in content
                    if choice['status_first']:
                        await invoke('change_status', {'target': selector, 'targetStatus': 'Resolved'})
                    predecessor, = list(authority.rglob(atom_id + '-*.md'))
                    old, _ = read(predecessor)
                    changes = {'summary': summary + ' replacement'} if choice['replacement'] else {'body': body.replace('Initial', 'Version two')}
                    await invoke('update', {'sourceCurrent': selector, 'changes': changes})
                    archived, = list(authority.rglob(atom_id + '@1-*.md'))
                    historical, _ = read(archived)
                    assert historical['status'].lower() == 'archived' and historical['version'] == 1 and historical['updated_at'] == old['updated_at']
                    candidates = [p for p in (authority / '01_concern').rglob('CA-C-*.md') if '@' not in p.name]
                    matches = [(p, *read(p)) for p in candidates if summary in read(p)[1]]
                    current, view, content = next(x for x in matches if (x[1]['atom_id'] != atom_id) == choice['replacement'])
                    assert current == predecessor or not predecessor.exists()
                    new_id = view['atom_id']
                    assert view['version'] == (1 if choice['replacement'] else 2)
                    assert view['status'].lower() == ('resolved' if choice['status_first'] else 'active')
                    assert view['destination']['file'] == {'name': current.name, 'path': current.parent.relative_to(ROOT).as_posix()}
                    assert datetime.fromisoformat(str(view['updated_at'])).utcoffset() is not None
                    if choice['replacement']:
                        assert atom_id in view['relations']['is_replacement_for'] and summary + ' replacement' in content
                    else:
                        assert new_id == atom_id and 'Version two' in content
                    selector = {'ref_id': new_id, 'version': view['version']}
                    if not choice['status_first']:
                        await invoke('change_status', {'target': selector, 'targetStatus': 'Resolved'})
                    resolved, = list(authority.rglob(new_id + '-*.md'))
                    view, resolved_body = read(resolved)
                    assert view['status'].lower() == 'resolved' and view['version'] == selector['version']
                    assert view['destination']['file'] == {'name': resolved.name, 'path': resolved.parent.relative_to(ROOT).as_posix()}
                    await invoke('archive', {'target': selector})
                    assert not resolved.exists()
                    final, = list(authority.rglob(new_id + '@' + str(selector['version']) + '-*.md'))
                    final_view, final_body = read(final)
                    assert final_view['status'].lower() == 'archived' and final_view['version'] == selector['version']
                    assert final_view['updated_at'] == view['updated_at']
                    assert final_body == resolved_body
                    assert final_view['destination']['file'] == {'name': final.name, 'path': final.parent.relative_to(ROOT).as_posix()}
                    archived_ref = f"{new_id}@{selector['version']}"
                    await wait_rows(
                        f"SELECT reference FROM atoms WHERE reference = '{archived_ref}' AND status_group = 'Archived'",
                        lambda rows: rows == [[archived_ref]], f'archived_{index}',
                    )
                    report.setdefault('cases', []).append({'index': index, 'source_id': atom_id, 'final_id': new_id, 'final_path': str(final)})
                    save()
                if any(report['timing_seconds'].get(tool, {}).get('count') != 20 for tool in
                       ('create_draft', 'promote_draft', 'direct_update', 'change_status', 'update', 'archive')):
                    raise AssertionError('Expected 20 successful timings for each lifecycle tool')
                for key, variants in (('update_variant_timing_seconds', ('summary_replacement', 'body_revision')),
                                      ('direct_update_variant_timing_seconds', ('draft', 'current'))):
                    if any(report.get(key, {}).get(variant, {}).get('count') != 10 for variant in variants):
                        raise AssertionError(f'Expected 10 timings for each {key} variant')
                # Only successful, fully observed runs are eligible for deletion.
                if snapshot(authority) != expected_files or digest(target) != owned_decl:
                    raise RuntimeError('Owned files changed before cleanup')
                known_ids = {value for case in report['cases'] for value in (case['source_id'], case['final_id'])}
                for path in authority.rglob('*'):
                    if path.is_file():
                        carrier, content = read(path)
                        if carrier.get('atom_id') not in known_ids or token not in content:
                            raise RuntimeError(f'Unexpected file in Scope Unit; preserving all: {path}')
                for path in sorted(authority.rglob('*'), reverse=True):
                    if path.is_file():
                        rel = path.relative_to(authority).as_posix()
                        remove_owned_file(path, expected_files[rel])
                    elif path.is_dir():
                        path.rmdir()
                authority.rmdir()
                remove_owned_file(target, owned_decl)
                owned_decl = None
                await wait_rows(scope_sql, lambda rows: rows == [], 'scope_removed')
                for case in report['cases']:
                    for atom_id in {case['source_id'], case['final_id']}:
                        sql = f"SELECT reference FROM atoms WHERE filename LIKE '{atom_id}-%' OR filename LIKE '{atom_id}@%'"
                        await wait_rows(sql, lambda rows: rows == [], f'removed_{atom_id}')
                successful = True
    except BaseException as error:
        report['error'] = repr(error)
        raise
    finally:
        report['outcome'] = 'passed' if successful else 'failed_preserve_remaining_scope_and_evidence'
        report['scope_path'] = str(authority)
        report['finished'] = datetime.now().astimezone().isoformat()
        save()
    print(report_path)


class LifecycleLivePerformanceCanary(unittest.TestCase):
    def test_twenty_atoms(self):
        if os.environ.get('CAPRMEDIO_LIVE_LIFECYCLE') != '1':
            self.skipTest('set CAPRMEDIO_LIVE_LIFECYCLE=1 for the live Project canary')
        asyncio.run(main())


class LifecycleCanarySetupTest(unittest.TestCase):
    def test_matrix_covers_both_update_variants(self):
        choices = case_matrix(random.Random(3005))
        self.assertEqual(len(choices), 20)
        self.assertEqual(sum(choice['replacement'] for choice in choices), 10)
        self.assertEqual(sum(choice['draft_direct_update'] for choice in choices), 10)
        self.assertEqual(choices, case_matrix(random.Random(3005)))

    def test_report_keeps_samples_median_max_and_variants(self):
        report = {}
        record_timing(report, 'update', 3.0, {'changes': {'summary': 'new'}})
        record_timing(report, 'update', 1.0, {'changes': {'body': 'new'}})
        self.assertEqual(report['timing_seconds']['update'], {
            'samples': [3.0, 1.0], 'count': 2, 'p50': 2.0, 'max': 3.0,
        })
        self.assertEqual(report['update_variant_timing_seconds']['summary_replacement']['samples'], [3.0])
        self.assertEqual(report['update_variant_timing_seconds']['body_revision']['samples'], [1.0])

    def test_archive_load_uses_only_the_temporary_scope_and_concern_role(self):
        expected = {'scope_unit': 'RANDOM_TEST', 'role': 'Concern'}
        response = SimpleNamespace(is_error=False, structured_content={'loaded_archive_scopes': [expected]})
        client = SimpleNamespace(call_tool=AsyncMock(return_value=response))
        self.assertEqual([expected], asyncio.run(load_archive_scope(client, 'RANDOM_TEST')))
        client.call_tool.assert_awaited_once_with('workbench_archive_load', {
            'project_root': str(ROOT), 'scopes': [expected],
        })

    def test_archive_load_rejects_missing_or_failed_coverage(self):
        for response in (SimpleNamespace(is_error=True, structured_content={}),
                         SimpleNamespace(is_error=False, structured_content={'loaded_archive_scopes': []})):
            with self.assertRaises(RuntimeError):
                asyncio.run(load_archive_scope(SimpleNamespace(call_tool=AsyncMock(return_value=response)), 'RANDOM_TEST'))


if __name__ == '__main__':
    unittest.main()

