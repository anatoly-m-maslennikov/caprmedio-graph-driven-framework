"""Materialize the reviewed source proposals; no native Workflow execution."""
import copy
from datetime import datetime
import hashlib
import json
from pathlib import Path
import re
import sys
from zoneinfo import ZoneInfo

import yaml

ROOT = Path(__file__).resolve().parents[5]
PACKET = Path(__file__).resolve().parent.parent
CONTROL = ROOT / '.caprmedio_caprmedio'
CORE = CONTROL / 'CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL'
sys.path.insert(0, str(ROOT / 'LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_TOOLS'))
from atom_operations import atom_identity_lock


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def read(raw):
    _, front, body = raw.decode().split('---', 2)
    return yaml.safe_load(front), body


def summary(body):
    return re.search(r'(?ms)^## Summary\s*\n(.*?)(?=^## |\Z)', body)[1].strip()


class Dumper(yaml.SafeDumper):
    pass


class Quoted(str):
    pass


Dumper.add_representer(Quoted, lambda d, s: d.represent_scalar('tag:yaml.org,2002:str', s, style='"'))


def render(meta, body):
    meta = copy.deepcopy(meta)
    meta['updated_at'] = Quoted(str(meta['updated_at']))
    return ('---\n' + yaml.dump(meta, Dumper=Dumper, sort_keys=False, allow_unicode=True, width=1000)
            + '---\n\n' + body.strip() + '\n').encode()


def census():
    versions, ordinary, ids = {}, {}, set()
    for path in CONTROL.rglob('CA-*.md'):
        match = re.match(r'(CA-([CAPRMEDO])-(\d+))(?!\d)', path.name)
        if not match:
            continue
        identity, role, number = match[1], match[2], int(match[3])
        ids.add(identity)
        if 'workbench_burst_500' not in str(path).lower() and 'temporary-throughput-probe' not in path.name:
            ordinary[role] = max(ordinary.get(role, 0), number)
        found = re.search(rb'(?m)^\s*version:\s*(\d+)\s*$', path.read_bytes())
        if found:
            versions[identity] = max(versions.get(identity, 0), int(found[1]))
    return versions, ordinary, ids


def main():
    target = PACKET / 'selected-drafts.json'
    assert not target.exists(), 'review existing selected Draft manifest'
    candidates = []
    for lane in ('forms', 'scope', 'conflicts'):
        data = json.loads((PACKET / lane / 'ready-candidates.json').read_text())
        candidates.extend(dict(row, lane=lane) for row in data['candidates'])
    initial = json.loads((PACKET / 'native-drafts.json').read_text())['drafts']
    selected = []
    for row in initial:
        path = ROOT / row['path']
        assert sha(path.read_bytes()) == row['sha256'], path
        selected.append(dict(row))
    for identity in ('CA-R-2512', 'CA-R-2513', 'CA-R-2514', 'CA-R-2515', 'CA-R-2463'):
        paths = list(CORE.glob(f'04_requirement/draft/{identity}@3-draft-*.md'))
        assert len(paths) == 1, identity
        meta, body = read(paths[0].read_bytes())
        selected.append(dict(key=identity, atom_id=identity, ref_id=meta['ref_id'], version=3,
                             path=str(paths[0].relative_to(ROOT)), new_identity=False,
                             summary=summary(body), sha256=sha(paths[0].read_bytes())))
    now = datetime.now(ZoneInfo('Asia/Tbilisi')).strftime('%Y-%m-%d %H:%M:%S %z')
    writes = []
    with atom_identity_lock(ROOT):
        versions, maximum, ids = census()
        for row in candidates:
            source = ROOT / row['source_path'] if row.get('source_path') else None
            before = source.read_bytes() if source else None
            if source:
                assert sha(before) == row['source_sha256'], source
                meta, old_body = read(before)
                assert summary(old_body) == row['summary'], source
                identity = meta['atom_id']
            else:
                role = row['role'][0]
                while True:
                    maximum[role] = maximum.get(role, 0) + 1
                    identity = f'CA-{role}-{maximum[role]:03d}'
                    if identity not in ids:
                        break
                ids.add(identity)
                meta = dict(atom_id=identity, container={'scope_unit': 'CA-SU-11'},
                            role=row['role'], form=row['form'], topics={}, tier=3)
            assert identity not in {r['atom_id'] for r in selected}, identity
            meta = copy.deepcopy(meta)
            meta.setdefault('container', {'scope_unit': 'CA-SU-13' if source and 'CA-SU-13_' in str(source) else 'CA-SU-11'})
            for name, value in row.get('header_overrides', {}).items():
                if value is None:
                    meta.pop(name, None)
                else:
                    meta[name] = copy.deepcopy(value)
            meta.update(role=row['role'], form=row['form'])
            meta.setdefault('topics', {})['main_subject'] = row['main_subject']
            if row.get('reuse_draft_path'):
                path = ROOT / row['reuse_draft_path']
                raw = path.read_bytes()
                reused, reused_body = read(raw)
                assert reused['atom_id'] == identity and summary(reused_body) == row['summary']
                assert reused_body.strip() == row['body'].strip(), path
                meta = reused
                version = meta['version']
            else:
                version = versions.get(identity, 0) + 1
                ref_id = f'{identity}@{version}-draft'
                unit = 'PROJECT_CONFIGURATION' if source and 'CA-SU-13_' in str(source) else 'CORE_META_MODEL'
                parent = source.parent if source else CORE / {'Requirement':'04_requirement', 'Method':'05_method'}[row['role']]
                slug = re.sub(r'[^a-z0-9]+', '-', row['summary'].lower()).strip('-')
                token = (meta.get('label') or row['form']).upper().replace(' ', '_')
                path = parent / 'draft' / f'{ref_id}-{unit}-{token}--{slug}.md'
                assert not path.exists(), path
            meta.update(ref_id=f'{identity}@{version}-draft', status='Draft', version=version, updated_at=now)
            meta['carrier_destination'] = {'file': {'name': path.name, 'path': str(path.parent.relative_to(ROOT))}}
            raw = render(meta, row['body'])
            assert summary(read(raw)[1]) == row['summary']
            writes.append((path, raw, path.read_bytes() if path.exists() else None))
            selected.append(dict(key=row['key'], atom_id=identity, ref_id=meta['ref_id'], version=version,
                                 path=str(path.relative_to(ROOT)), new_identity=source is None,
                                 source_path=row.get('source_path'), source_sha256=row.get('source_sha256'),
                                 summary=row['summary'], sha256=sha(raw), retires=row.get('retires', []), lane=row['lane']))
        # All hashes, identities and destinations pass before the first Draft write.
        for path, raw, before in writes:
            path.parent.mkdir(exist_ok=True)
            if before is None:
                with path.open('xb') as stream:
                    stream.write(raw)
            else:
                assert path.read_bytes() == before
                path.write_bytes(raw)
        for row in selected:
            assert sha((ROOT / row['path']).read_bytes()) == row['sha256']
        target.write_text(json.dumps({'status':'DRAFTS_READY_FOR_REVIEW', 'drafts':selected,
                                     'current_sources_changed':False, 'promotion_performed':False}, indent=2) + '\n')
    print(f'{len(selected)} selected Drafts; {len(writes)} materialized/reused; Current unchanged')


if __name__ == '__main__':
    main()
