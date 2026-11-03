#!/usr/bin/env python3
"""Normalize reviewed packets into the existing guarded manual-adoption operations."""
import argparse
from contextlib import contextmanager
import importlib.util
import json
from pathlib import Path
import re
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[5]
PACKETS = HERE.parent
OLD = ROOT / '.caprmedio_caprmedio/03_plan/CA-P-2694-EPIC--entity-graph-refactor-stage-4-polishing/model-header-content-20261103'
sys.path.insert(0, str(OLD / 'migration'))
spec = importlib.util.spec_from_file_location('existing_adoption', OLD / 'integration/adopt.py')
native = importlib.util.module_from_spec(spec)
spec.loader.exec_module(native)
native.ROOT = ROOT
native.HERE = HERE


def relative(path):
    path = Path(path)
    return path.relative_to(ROOT).as_posix() if path.is_absolute() else path.as_posix()


def normalize(manifests):
    rows, seen = [], set()
    for manifest in manifests:
        manifest = Path(manifest)
        packet = json.loads(manifest.read_text())
        if isinstance(packet, list): items = packet
        else:
            if packet.get('withheld'): raise ValueError(f'withheld items: {manifest}')
            items = packet.get('items', packet.get('sources', packet.get('candidates')))
        if not isinstance(items, list): raise ValueError(f'unsupported packet: {manifest}')
        for item in items:
            source = item.get('source_path', item.get('source', item.get('path')))
            before_sha = item.get('source_sha256', item.get('sha256'))
            candidate = item.get('candidate_path', item.get('candidate'))
            retire = item.get('action') == 'retire'
            if not source or not before_sha or (not retire and not candidate):
                raise ValueError(f'incomplete source/candidate packet: {manifest}: {source}')
            source = relative(source)
            if source in seen: raise ValueError(f'overlapping source: {source}')
            seen.add(source)
            path = native.checked_path(source)
            raw = path.read_bytes()
            if native.sha(raw) != before_sha: raise ValueError(f'source pin drift: {source}')
            meta, _ = native.read(raw)
            if meta['atom_id'] != item.get('source_atom_id', item.get('id', item.get('atom_id', meta['atom_id']))):
                raise ValueError(f'source ID mismatch: {source}')
            row = {'source_path': source, 'source_id': meta['atom_id'], 'source_sha256': before_sha,
                   'lane': manifest.parent.name, 'retire': retire}
            if not retire:
                proposed = Path(candidate)
                if not proposed.is_absolute():
                    proposed = ROOT / proposed if proposed.parts[0] == '.caprmedio_caprmedio' else manifest.parent / proposed
                proposed = proposed.resolve()
                if not proposed.is_relative_to(PACKETS.resolve()): raise ValueError('candidate outside packet directory')
                payload = proposed.read_bytes()
                if native.sha(payload) != item.get('candidate_sha256'): raise ValueError(f'candidate pin drift: {proposed}')
                row.update(candidate_path=relative(proposed), candidate_sha256=native.sha(payload))
            rows.append(row)
    return rows


def prepare(manifests, new_relation_id, timestamp, frontier):
    if not re.fullmatch(r'CA-R-[1-9]\d*', new_relation_id): raise ValueError('root must provide a numeric new Relation ID')
    operations, outputs, replacements = {}, [], {}
    def operation(path, after):
        name = relative(path)
        native.checked_path(name)
        if name in operations: raise ValueError(f'overlapping output: {name}')
        before = path.read_bytes() if path.exists() else None
        operations[name] = {'path': name, 'before_sha256': native.sha(before) if before is not None else None,
                            'before': before.decode() if before is not None else None,
                            'after_sha256': native.sha(after) if after is not None else None,
                            'after': after.decode() if after is not None else None}
    with native.atom_identity_lock(ROOT):
        frontier_pins = {}
        for row in frontier['operations']:
            path = native.checked_path(row['destination_path'])
            if row['destination_path'] in frontier_pins: raise ValueError('duplicate frontier source')
            if native.sha(path.read_bytes()) != row['sha256']: raise ValueError('frontier source drift: ' + str(path))
            frontier_pins[row['destination_path']] = row['sha256']
        rows = normalize(manifests)
        if sum(row['source_id'] == 'CA-R-2279' and not row['retire'] for row in rows) != 1:
            raise ValueError('expected exactly one fresh Relation replacement')
        if native.atom_id_has_preserved_history_evidence(ROOT, new_relation_id):
            raise ValueError('supplied new ID has preserved identity evidence')
        version_index = {}
        for retained in native.control_root(ROOT).rglob('CA-[RMED]-*.md'):
            identity = re.match(r'(CA-[RMED]-\d+)(?!\d)', retained.name)
            version = re.search(rb'(?m)^version:\s*(\d+)\s*$', retained.read_bytes()) if identity else None
            if version:
                version_index[identity[1]] = max(version_index.get(identity[1], 0), int(version[1]))
        for row in rows:
            source = native.checked_path(row['source_path'])
            before = source.read_bytes(); prior, prior_body = native.read(before)
            archive = source.parent / 'archive' / f'{source.stem}@{prior["version"]}.md'
            if archive.exists(): raise ValueError(f'archive collision: {archive}')
            operation(archive, before)
            if row['retire']:
                operation(source, None)
                outputs.append(dict(row, target_path=None))
                continue
            candidate = ROOT / row['candidate_path']
            meta, body = native.read(candidate.read_bytes())
            changed = native.summary(body) != native.summary(prior_body)
            fresh = row['source_id'] == 'CA-R-2279'
            if changed != fresh: raise ValueError(f'unexpected Summary identity change: {source}')
            if not fresh and meta['atom_id'] != prior['atom_id']: raise ValueError('candidate changes retained identity')
            identity = new_relation_id if fresh else prior['atom_id']
            if fresh:
                slug = re.sub(r'[^a-z0-9]+', '-', native.summary(body).lower()).strip('-')
                target = source.parent / f'{identity}-CORE_META_MODEL-DECLARATION--{slug}.md'
                if target.exists(): raise ValueError('fresh destination exists')
                version = 1; replacements[prior['atom_id']] = identity; operation(source, None)
            else:
                target = source
                version = max(int(prior['version']), version_index.get(identity, 0)) + 1
            meta.update(atom_id=identity, version=version, status=prior['status'], updated_at=timestamp)
            if 'carrier_destination' in meta or fresh:
                meta['carrier_destination'] = {'file': {'name': target.name, 'path': relative(target.parent)}}
            after = native.render(meta, body)
            operation(target, after)
            outputs.append(dict(row, target_path=relative(target), atom_id=identity, version=version, sha256=native.sha(after)))
    return {'status': 'PREPARED_NOT_ADOPTED', 'native_workflow_admission': False, 'journal_append': False,
            'prepared_at': timestamp, 'source_frontier_pins': frontier_pins, 'base_id_replacements': replacements, 'outputs': outputs,
            'operations': list(operations.values()),
            'reference_policy': 'Bare current references remap after semantic adoption; frozen oldId@N and exact predecessor archive bytes remain unchanged.'}


def check(plan):
    states = []
    seen = set()
    for row in plan['operations']:
        if row['path'] in seen: raise ValueError('duplicate operation path')
        seen.add(row['path'])
        path = native.checked_path(row['path'])
        for key in ('before', 'after'):
            payload = row[key]
            if (native.sha(payload.encode()) if payload is not None else None) != row[key + '_sha256']:
                raise ValueError('corrupt plan payload')
        actual = native.sha(path.read_bytes()) if path.exists() else None
        if actual == row['before_sha256']: states.append('before')
        elif actual == row['after_sha256']: states.append('after')
        else: raise ValueError(f'preflight drift: {path}')
    if len(set(states)) > 1: raise ValueError('mixed partial adoption state')
    for name, expected in plan.get('source_frontier_pins', {}).items():
        if name in seen: continue
        path = native.checked_path(name)
        if native.sha(path.read_bytes()) != expected: raise ValueError('unchanged frontier source drift: ' + name)
    return states[0] if states else 'before'


def reference_payload(raw, replacements):
    """Rewrite current reference tokens, preserving identity, Summary and literal operands."""
    def rewrite(value):
        quoted = []
        def hide(match):
            quoted.append(match.group()); return '\x00QUOTE' + str(len(quoted) - 1) + '\x00'
        value = re.sub(r'"(?:\\.|[^"\\\r\n])*"|\'(?:\\.|[^\'\\\r\n])*\'', hide, value)
        lookup = dict(replacements, IS_DEFINED_BY='IS_DECLARED_BY')
        pattern = r'(?<![\w-])(?:' + '|'.join(re.escape(k) for k in sorted(lookup, key=len, reverse=True)) + r')(?![\w-]|@\d)'
        value = re.sub(pattern, lambda m: lookup[m.group()], value)
        return re.sub(r'\x00QUOTE(\d+)\x00', lambda m: quoted[int(m.group(1))], value)
    text = raw.decode()
    delimiters = list(re.finditer(r'(?m)^---[ \t]*(?:\r?\n|$)', text))
    if len(delimiters) < 2 or delimiters[0].start(): raise ValueError('missing reference source frontmatter')
    a, b, end = delimiters[0].end(), delimiters[1].start(), delimiters[1].end()
    fm = text[a:b]; root = native.yaml.compose(fm); edits = []
    def scalar(node):
        if isinstance(node, native.yaml.nodes.MappingNode):
            for _, value in node.value: scalar(value)
        elif isinstance(node, native.yaml.nodes.SequenceNode):
            for value in node.value: scalar(value)
        elif isinstance(node, native.yaml.nodes.ScalarNode) and node.tag == 'tag:yaml.org,2002:str':
            changed = rewrite(node.value)
            if changed == node.value: return
            if '\n' in node.value: raise ValueError('multiline Subject reference needs explicit review')
            if node.style == "'": rendered = "'" + changed.replace("'", "''") + "'"
            elif node.style == '"': rendered = json.dumps(changed, ensure_ascii=False)
            elif node.style is None: rendered = changed
            else: raise ValueError('unsupported Subject scalar style')
            edits.append((node.start_mark.index, node.end_mark.index, rendered))
    for key, value in root.value:
        if key.value == 'subjects': scalar(value)
    for start, stop, value in sorted(edits, reverse=True): fm = fm[:start] + value + fm[stop:]
    body = text[end:]
    from claim import sections
    lines, found = sections(body)
    roots = [(index, name) for index, level, name in found if level == 2]
    protected = None
    for index, (position, name) in enumerate(roots):
        if name == 'summary':
            stop = roots[index + 1][0] if index + 1 < len(roots) else len(lines)
            protected = ''.join(lines[position + 1:stop])
            body = ''.join(lines[:position + 1]) + '\x00SUMMARY\x00' + ''.join(lines[stop:])
            break
    body = rewrite(body)
    if protected is not None: body = body.replace('\x00SUMMARY\x00', protected)
    result = (text[:a] + fm + text[b:end] + body).encode()
    before_meta, _ = native.read(raw); after_meta, _ = native.read(result)
    if {k: v for k, v in before_meta.items() if k != 'subjects'} != {k: v for k, v in after_meta.items() if k != 'subjects'}:
        raise ValueError('reference rewrite would alter non-Subject metadata')
    return result


def references(frontier, plan):
    """Pin reviewed overrides against prospective semantic outputs without applying them."""
    paths = {row['source_path']: row['target_path'] for row in plan['outputs']}
    after = {row['path']: row['after'] for row in plan['operations'] if row['after'] is not None}
    overrides = []
    for row in frontier['operations']:
        source = native.checked_path(row['destination_path']); current = source.read_bytes()
        if native.sha(current) != row['sha256']: raise ValueError('reference frontier drift: ' + str(source))
        target = paths.get(row['destination_path'], row['destination_path'])
        if target is None: continue
        raw = after[target].encode() if target in after else current
        candidate = reference_payload(raw, plan['base_id_replacements'])
        if candidate == raw: continue
        meta, _ = native.read(raw)
        overrides.append({'source_id': meta['atom_id'], 'path': target,
                          'before_sha256': native.sha(raw), 'candidate_sha256': native.sha(candidate), 'candidate': candidate.decode()})
    return {'reviewed_source_overrides': overrides,
            'reference_policy': 'Current bare ID and IS_DEFINED_BY tokens only; frozen @N, identity metadata, Summary and quoted literals preserved.'}


def apply_plan(plan):
    if check(plan) == 'after': return 0
    original_lock = native.atom_identity_lock
    @contextmanager
    def locked_with_identity_check(root):
        with original_lock(root):
            for name, expected in plan['source_frontier_pins'].items():
                if native.sha(native.checked_path(name).read_bytes()) != expected:
                    raise ValueError('frontier drift before adoption: ' + name)
            for identity in plan['base_id_replacements'].values():
                if native.atom_id_has_preserved_history_evidence(root, identity):
                    raise ValueError('fresh ID acquired preserved identity evidence after prepare: ' + identity)
            yield
    native.atom_identity_lock = locked_with_identity_check
    try:
        native.apply()
    finally:
        native.atom_identity_lock = original_lock
    return len(plan['operations'])


def refresh(frontier, plan):
    if check(plan) != 'after': raise ValueError('semantic adoption not applied completely')
    mapping = {row['source_path']: row['target_path'] for row in plan['outputs']}
    result = dict(frontier); rows = []
    for row in frontier['operations']:
        target = mapping.get(row['destination_path'], row['destination_path'])
        if target is None: continue
        path = native.checked_path(target); raw = path.read_bytes(); meta, _ = native.read(raw)
        rows.append(dict(row, destination_path=target, base_id=meta['atom_id'], version=meta['version'],
                         sha256=native.sha(raw), status=meta['status'], role=meta['role'], form=meta['form'], subjects=meta.get('subjects', {})))
    result.update(status='POST_SEMANTIC_ADOPTION_CURRENT_FRONTIER', operations=rows)
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command', required=True)
    p = sub.add_parser('prepare'); p.add_argument('--manifest', type=Path, action='append', required=True); p.add_argument('--new-relation-id', required=True); p.add_argument('--timestamp', required=True); p.add_argument('--frontier', type=Path, required=True)
    sub.add_parser('check'); sub.add_parser('apply')
    p = sub.add_parser('references'); p.add_argument('--frontier', type=Path, required=True); p.add_argument('--output', type=Path, required=True)
    p = sub.add_parser('refresh'); p.add_argument('--frontier', type=Path, required=True); p.add_argument('--output', type=Path, required=True)
    args = parser.parse_args(); destination = HERE / 'adoption-plan.json'
    if args.command == 'prepare':
        if (HERE / 'adoption-receipt.json').exists(): raise ValueError('existing receipt; retain the reviewed applied plan')
        plan = prepare(args.manifest, args.new_relation_id, args.timestamp, json.loads(args.frontier.read_text()))
        destination.write_text(json.dumps(plan, ensure_ascii=False, indent=2) + '\n'); print(f"prepared {len(plan['outputs'])} sources; {len(plan['operations'])} operations")
    else:
        plan = json.loads(destination.read_text())
        if args.command == 'check': print(check(plan))
        elif args.command == 'apply':
            if check(plan) == 'after': print('already applied; no writes')
            else: apply_plan(plan)
        elif args.command == 'references':
            args.output.write_text(json.dumps(references(json.loads(args.frontier.read_text()), plan), ensure_ascii=False, indent=2) + '\n')
        else:
            args.output.write_text(json.dumps(refresh(json.loads(args.frontier.read_text()), plan), ensure_ascii=False, indent=2) + '\n')


if __name__ == '__main__': main()
