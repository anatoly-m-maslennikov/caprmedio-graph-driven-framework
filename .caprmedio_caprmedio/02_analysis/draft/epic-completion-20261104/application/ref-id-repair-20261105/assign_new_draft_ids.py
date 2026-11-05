"""Assign identities to reviewed Drafts without promoting their content."""
from pathlib import Path
import contextlib
import importlib.util
import json
import re

ROOT = Path.cwd()
HERE = Path(__file__).resolve().parent
CONTROL = ROOT / '.caprmedio_caprmedio'


def module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result


n = module('identity_only_adoption', CONTROL / '03_plan/CA-P-2694-EPIC--entity-graph-refactor-stage-4-polishing/model-header-content-20261103/integration/adopt.py')
n.ROOT = ROOT
order = module('identity_only_order', HERE.parent / 'property-order-20261105/migration/prepare_order.py')


def main(review_name='new-v1-rename-skeleton.json', batch_name='new-draft-application'):
    target = HERE / batch_name
    target.mkdir(exist_ok=True)
    assert not (target / 'adoption-plan.json').exists()
    review_path = HERE / 'identity' / review_name
    review = json.loads(review_path.read_text())
    operations, outputs = {}, []

    def operation(path, after):
        rel = path.relative_to(ROOT).as_posix()
        assert rel not in operations
        before = path.read_bytes() if path.exists() else None
        operations[rel] = {'path': rel, 'before': before.decode() if before is not None else None,
                           'before_sha256': n.sha(before) if before is not None else None,
                           'after': after.decode() if after is not None else None,
                           'after_sha256': n.sha(after) if after is not None else None}

    with n.atom_identity_lock(ROOT):
        maximum = {}
        for path in CONTROL.rglob('CA-[CAPRMEDO]-*.md'):
            match = re.match(r'CA-([CAPRMEDO])-(\d+)', path.name)
            if match:
                maximum[match[1]] = max(maximum.get(match[1], 0), int(match[2]))
        for row in review['candidates']:
            source = ROOT / row['source']
            before = source.read_bytes()
            assert n.sha(before) == row['source_sha256'], source
            meta, body = n.read(before)
            version = row.get('version', 1)
            assert type(version) is int and version >= 1
            assert version == 1 or review.get('preserve_existing_versions') is True
            assert meta['status'] == 'Draft' and meta['version'] == version
            for predecessor in row.get('predecessor_files', []):
                assert n.sha((ROOT / predecessor['path']).read_bytes()) == predecessor['sha256']
            letter = row['letter']
            while True:
                maximum[letter] = maximum.get(letter, 0) + 1
                identity = f'CA-{letter}-{maximum[letter]}'
                if not n.atom_id_has_preserved_history_evidence(ROOT, identity):
                    break
            destination = ROOT / row['destination_template'].replace('{ID}', identity)
            assert not destination.exists(), destination
            assert f'@{version}-draft-' in destination.name
            expected = dict(meta, atom_id=identity, ref_id=f'{identity}@{version}-draft')
            cd = expected.get('carrier_destination')
            if isinstance(cd, dict) and isinstance(cd.get('file'), dict):
                cd = dict(cd, file=dict(cd['file'], name=destination.name))
                expected['carrier_destination'] = cd
            ranked = {key: expected[key] for key in order.HEADER_ORDER if key in expected}
            ranked.update({key: value for key, value in expected.items() if key not in ranked})
            after = n.render(ranked, body)
            assert n.read(after) == (expected, body)
            operation(destination, after)
            operation(source, None)
            outputs.append({'source': row['source'], 'path': destination.relative_to(ROOT).as_posix(),
                            'atom_id': identity, 'version': version, 'status': 'Draft', 'sha256': n.sha(after)})
        plan = {'status': 'REVIEWED_IDENTITY_REPAIR', 'source_review_sha256': n.sha(review_path.read_bytes()),
                'scope': 'Reviewed Draft identities, preserving Versions; no Form admission, Claim change or promotion.',
                'outputs': outputs, 'operations': list(operations.values()),
                'native_workflow_admission': False, 'journal_append': False}
        (target / 'adoption-plan.json').write_text(json.dumps(plan, indent=2) + '\n')
        n.HERE = target
        outer = n.atom_identity_lock
        n.atom_identity_lock = lambda _: contextlib.nullcontext()
        try:
            n.apply()
        finally:
            n.atom_identity_lock = outer
    print(json.dumps({'allocated_drafts': len(outputs), 'batch': batch_name}))


if __name__ == '__main__':
    main()
