"""Prepare and manually apply the reviewed, pinned MODEL packet; no workflow admission."""
import hashlib
import json
import os
from pathlib import Path
import re
import sys
from datetime import datetime
from zoneinfo import ZoneInfo

import yaml

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
TOOLS = ROOT / 'LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_TOOLS'
sys.path.insert(0, str(TOOLS))
sys.path.insert(0, str(HERE.parent / 'migration'))
from atom_operations import atom_identity_lock, atom_id_has_preserved_history_evidence, control_root
from migrate import atomic_replace


def sha(data):
    return hashlib.sha256(data).hexdigest()


def read(raw):
    _, fm, body = raw.decode().split('---', 2)
    return yaml.safe_load(fm), body


def summary(body):
    return re.search(r'(?ms)^## Summary\s*\n(.*?)(?=^## |\Z)', body)[1].strip()


def render(meta, body):
    return ('---\n' + yaml.safe_dump(meta, sort_keys=False, allow_unicode=True, width=1000)
            + '---' + body).encode()


def checked_path(relative):
    supplied = Path(relative)
    if supplied.is_absolute() or '..' in supplied.parts or supplied.suffix != '.md':
        raise ValueError(f'invalid adoption path: {relative}')
    path = ROOT / supplied
    if not path.resolve().is_relative_to(control_root(ROOT).resolve()):
        raise ValueError(f'path outside Project control root: {relative}')
    if any(item.is_symlink() for item in (path, *path.parents) if item.is_relative_to(ROOT)):
        raise ValueError(f'symlink in adoption path: {relative}')
    return path


def prepare():
    destination = HERE / 'adoption-plan.json'
    if destination.exists():
        raise ValueError('adoption plan already exists; review it rather than reallocating IDs')
    inventory = json.loads((HERE.parent / 'reviews/adoption-inventory.json').read_text())
    rows = inventory['source_to_candidate_map']
    core = Path(rows[0]['source_path']).parent
    for row in [*rows, *inventory['retirements']]:
        assert sha(Path(row['source_path']).read_bytes()) == row['source_sha256_actual']
    for row in [*rows, *inventory['new_candidates']]:
        assert sha(Path(row['candidate_path']).read_bytes()) == row['candidate_sha256_actual']
    now = datetime.now(ZoneInfo('Asia/Tbilisi')).strftime('%Y-%m-%d %H:%M:%S %z')
    operations, outputs, ids = {}, [], {}
    with atom_identity_lock(ROOT):
        # Retained filenames and native evidence checks share the existing ID boundary.
        retained = list(control_root(ROOT).rglob('CA-[RMED]-*.md'))
        maximum = max(int(m[1]) for p in retained if (m := re.match(r'CA-R-(\d+)', p.name)))
        versions = {}
        for path in retained:
            m = re.match(r'(CA-[RMED]-\d+)(?!\d)', path.name)
            if not m:
                continue
            match = re.search(rb'(?m)^version:\s*(\d+)\s*$', path.read_bytes())
            if match:
                versions[m[1]] = max(versions.get(m[1], 0), int(match[1]))

        def allocate():
            nonlocal maximum
            while True:
                maximum += 1
                identity = f'CA-R-{maximum}'
                if not atom_id_has_preserved_history_evidence(ROOT, identity):
                    return identity

        def operation(path, after):
            relative = path.relative_to(ROOT).as_posix()
            before = path.read_bytes() if path.exists() else None
            if relative in operations:
                raise ValueError(f'duplicate operation: {relative}')
            operations[relative] = {
                'path': relative, 'before_sha256': sha(before) if before is not None else None,
                'before': before.decode() if before is not None else None,
                'after_sha256': sha(after) if after is not None else None,
                'after': after.decode() if after is not None else None,
            }

        def preserve(path):
            meta, _ = read(path.read_bytes())
            archive = path.parent / 'archive' / f'{path.stem}@{meta["version"]}.md'
            if archive.exists():
                raise ValueError(f'archive collision: {archive}')
            # Native history preserves predecessor bytes, including its original timestamp.
            operation(archive, path.read_bytes())
            return archive

        for row in [*rows, *inventory['new_candidates']]:
            meta, body = read(Path(row['candidate_path']).read_bytes())
            prior = Path(row['source_path']) if 'source_path' in row else None
            changed = prior is None or row['summary_changed']
            identity = allocate() if changed else row['source_id']
            version = 1 if changed else versions[identity] + 1
            if prior is not None:
                preserve(prior)
                if changed:
                    ids[row['source_id']] = identity
                    operation(prior, None)
            if changed:
                slug = re.sub(r'[^a-z0-9]+', '-', summary(body).lower()).strip('-')
                form = str(meta.get('form', 'Declaration')).upper().replace(' ', '_')
                target = core / f'{identity}-CORE_META_MODEL-{form}--{slug}.md'
                if target.exists():
                    raise ValueError(f'new destination exists: {target}')
            else:
                target = prior
            meta.update(atom_id=identity, version=version, status='Active', updated_at=now)
            meta['carrier_destination'] = {'file': {'name': target.name, 'path': target.parent.relative_to(ROOT).as_posix()}}
            raw = render(meta, body)
            operation(target, raw)
            staged = HERE / 'prospective' / target.name
            staged.parent.mkdir(exist_ok=True)
            with staged.open('xb') as stream:
                stream.write(raw)
            outputs.append({'source_id': row.get('source_id'), 'atom_id': identity, 'version': version,
                            'source_path': prior.relative_to(ROOT).as_posix() if prior else None,
                            'target_path': target.relative_to(ROOT).as_posix(), 'candidate_path': str(staged.relative_to(ROOT)),
                            'sha256': sha(raw), 'summary': summary(body), 'lane': row['lane']})
        for row in inventory['retirements']:
            source = Path(row['source_path'])
            preserve(source)
            operation(source, None)
        result = {'status': 'PREPARED_NOT_ADOPTED', 'route': 'explicit user-authorized manual application',
                  'native_workflow_admission': False, 'journal_append': False,
                  'prepared_at': now, 'outputs': outputs, 'base_id_replacements': ids,
                  'retirements': inventory['retirements'], 'operations': list(operations.values())}
        destination.write_text(json.dumps(result, indent=2) + '\n')
    print(f'prepared {len(outputs)} outputs, {len(ids)} identity replacements, {len(operations)} operations')


def apply():
    plan = json.loads((HERE / 'adoption-plan.json').read_text())
    receipt = HERE / 'adoption-receipt.json'
    if receipt.exists():
        raise ValueError('application receipt already exists')
    written = []
    with atom_identity_lock(ROOT):
        names = [row['path'] for row in plan['operations']]
        if len(names) != len(set(names)):
            raise ValueError('duplicate adoption paths')
        for row in plan['operations']:
            path = checked_path(row['path'])
            before = path.read_bytes() if path.exists() else None
            if (sha(before) if before is not None else None) != row['before_sha256']:
                raise ValueError(f'preflight drift: {path}')
            if row['after'] is not None and sha(row['after'].encode()) != row['after_sha256']:
                raise ValueError(f'corrupt prepared output: {path}')
        try:
            for row in plan['operations']:
                path = checked_path(row['path'])
                actual = path.read_bytes() if path.exists() else None
                if (sha(actual) if actual is not None else None) != row['before_sha256']:
                    raise ValueError(f'concurrent drift: {path}')
                if row['after'] is None:
                    path.unlink()
                elif path.exists():
                    atomic_replace(path, row['after'].encode())
                else:
                    path.parent.mkdir(exist_ok=True)
                    with path.open('xb') as stream:
                        stream.write(row['after'].encode()); stream.flush(); os.fsync(stream.fileno())
                written.append(row)
        except BaseException:
            for row in reversed(written):
                path = checked_path(row['path'])
                actual = path.read_bytes() if path.exists() else None
                if (sha(actual) if actual is not None else None) != row['after_sha256']:
                    raise RuntimeError(f'rollback blocked by external drift: {path}')
                if row['before'] is None:
                    path.unlink()
                elif path.exists():
                    atomic_replace(path, row['before'].encode())
                else:
                    path.write_text(row['before'])
            raise
    for row in plan['operations']:
        path = checked_path(row['path'])
        actual = path.read_bytes() if path.exists() else None
        assert (sha(actual) if actual is not None else None) == row['after_sha256']
    receipt.write_text(json.dumps({'status': 'APPLIED_VERIFIED', 'native_workflow_admission': False,
                                 'journal_append': False, 'plan_sha256': sha((HERE / 'adoption-plan.json').read_bytes()),
                                 'output_count': len(plan['outputs']), 'operation_count': len(written)}, indent=2) + '\n')
    print(f'applied and verified {len(written)} operations')


if __name__ == '__main__':
    {'prepare': prepare, 'apply': apply}[sys.argv[1]]()
