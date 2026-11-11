"""Restore missing Status from the user-confirmed ordinary-folder placement."""
from pathlib import Path
import json
import importlib.util

ROOT = Path.cwd()
HERE = Path(__file__).resolve().parent


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main():
    helper = load('folder_status_identity', HERE / 'assign_new_draft_ids.py')
    formula = load('folder_status_ref', HERE.parent / 'property-order-20261105/ref-id-data/prepare_ref_id.py')
    target = HERE / 'folder-status-application-20261106'
    target.mkdir(exist_ok=True)
    assert not (target / 'adoption-plan.json').exists(), 'batch already prepared'
    rows = [row for row in json.loads((HERE / 'progress-readback.json').read_text())['rows'] if not row['status']]
    assert len(rows) == 159
    operations, outputs, identity_holds = [], [], []
    for row in rows:
        path = ROOT / row['path']
        assert path.parent.name in ('01_concern', '02_analysis', '07_delivery'), path
        assert not path.is_symlink()
        before = path.read_bytes()
        meta, body = helper.n.read(before)
        assert 'status' not in meta, path
        expected = dict(meta, status='Active')
        if meta.get('atom_id'):
            ref_id = formula.reference(meta['atom_id'], meta.get('version'), 'Active')
            assert 'ref_id' not in meta or meta['ref_id'] == ref_id
            expected['ref_id'] = ref_id
        else:
            identity_holds.append(row['path'])
        ordered = {key: expected[key] for key in helper.order.HEADER_ORDER if key in expected}
        ordered.update({key: value for key, value in expected.items() if key not in ordered})
        after = helper.n.render(ordered, body)
        assert helper.n.read(after) == (expected, body)
        assert {key for key in set(meta) | set(expected) if meta.get(key) != expected.get(key)} <= {'status', 'ref_id'}
        operations.append(dict(path=row['path'], before=before.decode(), before_sha256=helper.n.sha(before),
                               after=after.decode(), after_sha256=helper.n.sha(after)))
        outputs.append(dict(path=row['path'], atom_id=meta.get('atom_id'), status='Active',
                            ref_id=expected.get('ref_id'), sha256=helper.n.sha(after)))
    assert len(identity_holds) == 8
    plan = dict(scope='159 missing Status values: ordinary Role folder means Active; other lifecycle states have separate folders.',
                operations=operations, outputs=outputs, identity_holds=identity_holds,
                native_workflow_admission=False, journal_append=False)
    (target / 'adoption-plan.json').write_text(json.dumps(plan, indent=2) + '\n')
    helper.n.HERE = target
    helper.n.apply()
    print(dict(status_restored=len(outputs), ref_ids_restored=len(outputs) - len(identity_holds), missing_ids=len(identity_holds)))


if __name__ == '__main__':
    main()
