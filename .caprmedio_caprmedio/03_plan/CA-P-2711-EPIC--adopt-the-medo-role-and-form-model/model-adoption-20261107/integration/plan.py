"""Seal exact manual source-promotion preimages and outputs for review."""
import copy
from datetime import datetime
import importlib.util
import json
from pathlib import Path
import stat
from types import SimpleNamespace
from zoneinfo import ZoneInfo

import prepare as p
from atom_operations import archive_revision_destination

ROOT, PACKET = p.ROOT, p.PACKET
spec = importlib.util.spec_from_file_location('source_apply', PACKET / 'lifecycle/apply_source_plan.py')
a = importlib.util.module_from_spec(spec)
spec.loader.exec_module(a)


def main():
    target = PACKET / 'adoption-plan.json'
    assert not target.exists(), 'review existing sealed plan'
    selected = json.loads((PACKET / 'selected-drafts.json').read_text())['drafts']
    retirement_rows = json.loads((PACKET / 'conflicts/ready-candidates.json').read_text())['planned_retirements']
    retired = {row['id'] for row in retirement_rows}
    assert not retired.intersection(row['atom_id'] for row in selected)
    now = datetime.now(ZoneInfo('Asia/Tbilisi')).strftime('%Y-%m-%d %H:%M:%S %z')
    archives, publications, deletions, outputs = [], [], [], []
    paths = set()

    def operation(path, after, collection, mode=None):
        relative = path.relative_to(ROOT).as_posix()
        assert relative not in paths, relative
        paths.add(relative)
        before = path.read_bytes() if path.exists() else None
        collection.append(dict(path=relative, before=before.decode() if before is not None else None,
                               before_sha256=p.sha(before) if before is not None else None,
                               after=after.decode() if after is not None else None,
                               after_sha256=p.sha(after) if after is not None else None,
                               before_mode=stat.S_IMODE(path.stat().st_mode) if path.exists() else None,
                               after_mode=mode or (stat.S_IMODE(path.stat().st_mode) if path.exists() else 0o644)))

    def archive(source):
        raw = source.read_bytes()
        meta, _ = p.read(raw)
        assert meta['role'] in {'Requirement', 'Method', 'Evaluation', 'Delivery'}
        # This pure resolver needs path/role only; legacy Draft admission is unrelated.
        address = SimpleNamespace(path=source, frontmatter=raw.decode().split('---', 2)[1])
        destination = archive_revision_destination(ROOT, address, meta['version'])
        assert not destination.exists(), destination
        operation(destination, raw, archives, stat.S_IMODE(source.stat().st_mode))
        return destination

    with p.atom_identity_lock(ROOT):
        footprint = a.versions(ROOT)
        versions = {r['atom_id']: max(x[2] for x in footprint[r['atom_id']]) + 1 for r in selected}
        for row in selected:
            draft = ROOT / row['path']
            raw = draft.read_bytes()
            assert p.sha(raw) == row['sha256'], draft
            meta, body = p.read(raw)
            assert meta['status'] == 'Draft' and meta['atom_id'] == row['atom_id']
            assert p.summary(body) == row['summary']
            current = None
            if not row['new_identity']:
                if row.get('source_path'):
                    current = ROOT / row['source_path']
                else:
                    found = list(draft.parent.parent.glob(f'{row["atom_id"]}-*.md'))
                    assert len(found) == 1, (row['atom_id'], found)
                    current = found[0]
                before = current.read_bytes()
                if row.get('source_sha256'):
                    assert p.sha(before) == row['source_sha256'], current
                old_meta, old_body = p.read(before)
                assert old_meta['atom_id'] == row['atom_id']
                assert old_meta['status'] not in ('Draft', 'Archived')
                assert p.summary(old_body) == p.summary(body), row['atom_id']
                archive_path = archive(current)
            else:
                archive_path = None
            name = draft.name.replace(meta['ref_id'], row['atom_id'], 1)
            destination = draft.parent.parent / name
            assert destination == current or not destination.exists(), destination
            meta = copy.deepcopy(meta)
            meta.update(ref_id=row['atom_id'], status='Active', version=versions[row['atom_id']], updated_at=now)
            meta['carrier_destination'] = {'file': {'name': destination.name, 'path': str(destination.parent.relative_to(ROOT))}}
            final = p.render(meta, body)
            operation(destination, final, publications)
            if current and current != destination:
                operation(current, None, deletions)
            operation(draft, None, deletions)
            outputs.append(dict(atom_id=row['atom_id'], version=meta['version'], draft_path=row['path'],
                                target_path=str(destination.relative_to(ROOT)), sha256=p.sha(final),
                                predecessor_path=str(current.relative_to(ROOT)) if current else None,
                                archive_path=str(archive_path.relative_to(ROOT)) if archive_path else None,
                                summary=row['summary'], key=row['key']))
        retirements = []
        for row in retirement_rows:
            source = ROOT / row['source_path']
            assert p.sha(source.read_bytes()) == row['source_sha256'], source
            retired_archive = archive(source)
            operation(source, None, deletions)
            retirements.append(dict(atom_id=row['id'], source_path=row['source_path'], archive_path=str(retired_archive.relative_to(ROOT))))
        for identity in ('CA-R-2688', 'CA-M-461'):
            for draft in p.CORE.glob(f'*/draft/{identity}@3-draft-*.md'):
                retired_archive = archive(draft)
                operation(draft, None, deletions)
                retirements.append(dict(atom_id=identity, source_path=str(draft.relative_to(ROOT)), archive_path=str(retired_archive.relative_to(ROOT)), kind='obsolete Draft'))
        pins = [dict(path=path, sha256=digest, atom_id=identity, version=version)
                for identity in set(versions) | retired for path, digest, version in footprint.get(identity, [])]
        plan = dict(status='SEALED_FOR_REVIEW_NOT_APPLIED', route='user-authorized manual source promotion',
                    native_workflow_admission=False, journal_append=False, prepared_at=now,
                    selected_versions=versions, version_pins=pins, outputs=outputs, retirements=retirements,
                    operations=archives + publications + deletions)
        target.write_text(json.dumps(plan, indent=2) + '\n')
    print(f'sealed {len(outputs)} promotions, {len(retirements)} retirements, {len(plan["operations"])} operations, {len(pins)} version pins')


if __name__ == '__main__':
    main()
