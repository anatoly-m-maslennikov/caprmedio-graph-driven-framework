"""Apply the pinned Property packet using the existing manual adoption boundary."""
import importlib.util
import json
from pathlib import Path
import re
import sys
from datetime import datetime
from zoneinfo import ZoneInfo

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
HELPER = ROOT / '.caprmedio_caprmedio/03_plan/CA-P-2694-EPIC--entity-graph-refactor-stage-4-polishing/model-header-content-20261103/integration/adopt.py'
spec = importlib.util.spec_from_file_location('property_packet_adopt', HELPER)
native = importlib.util.module_from_spec(spec)
spec.loader.exec_module(native)
native.ROOT = ROOT
native.HERE = HERE / 'application'


def prepare():
    destination = native.HERE / 'adoption-plan.json'
    if destination.exists():
        raise ValueError('Review the existing plan before preparing again')
    rows = json.loads((HERE / 'rules/manifest.json').read_text())
    extra = json.loads((HERE / 'inheritance-extra/manifest.json').read_text())
    by_id = {row['id']: row for row in rows}
    for row in extra['candidates']:
        if row['id'] in by_id:
            assert row['source_sha256'] == by_id[row['id']]['source_sha256']
        by_id[row['id']] = row
    now = datetime.now(ZoneInfo('Asia/Tbilisi')).strftime('%Y-%m-%d %H:%M:%S %z')
    operations, outputs = [], []
    with native.atom_identity_lock(ROOT):
        versions = {}
        for path in native.control_root(ROOT).rglob('CA-R-*.md'):
            identity = re.match(r'(CA-R-\d+)(?!\d)', path.name)
            version = re.search(rb'(?m)^version:\s*(\d+)\s*$', path.read_bytes())
            if identity and version:
                versions[identity[1]] = max(versions.get(identity[1], 0), int(version[1]))
        for row in by_id.values():
            source = native.checked_path(row['source_path'])
            before = source.read_bytes()
            candidate = (ROOT / row['candidate_path']).read_bytes()
            assert native.sha(before) == row['source_sha256'], row['id']
            assert native.sha(candidate) == row['candidate_sha256'], row['id']
            old_meta, old_body = native.read(before)
            meta, body = native.read(candidate)
            assert meta == old_meta and native.summary(body) == native.summary(old_body), row['id']
            if candidate == before:
                continue
            archive = source.parent / 'archive' / f'{source.stem}@{old_meta["version"]}.md'
            assert not archive.exists(), archive
            meta.update(version=versions[row['id']] + 1, updated_at=now)
            after = native.render(meta, body)
            for path, prior, result in ((archive, None, before), (source, before, after)):
                operations.append({'path': path.relative_to(ROOT).as_posix(),
                                   'before': prior.decode() if prior is not None else None,
                                   'before_sha256': native.sha(prior) if prior is not None else None,
                                   'after': result.decode(), 'after_sha256': native.sha(result)})
            outputs.append({'atom_id': row['id'], 'version': meta['version'],
                            'before_version': old_meta['version'], 'target_path': row['source_path'],
                            'archive_path': archive.relative_to(ROOT).as_posix(),
                            'sha256': native.sha(after), 'summary': native.summary(body)})
        native.HERE.mkdir(exist_ok=True)
        with destination.open('x') as stream:
            json.dump({'status': 'PREPARED_NOT_ADOPTED', 'prepared_at': now,
                       'route': 'explicit user-authorized manual application',
                       'native_workflow_admission': False, 'journal_append': False,
                       'outputs': outputs, 'operations': operations}, stream, indent=2)
            stream.write('\n')
    print(f'Prepared {len(outputs)} same-ID revisions and exact archives')


if __name__ == '__main__':
    {'prepare': prepare, 'apply': native.apply}[sys.argv[1]]()
