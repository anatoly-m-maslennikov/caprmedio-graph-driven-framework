"""Read back the original identity/state hold set without inferring missing data."""
from pathlib import Path
from collections import Counter
import importlib.util
import json

HERE = Path(__file__).resolve().parent
ROOT = Path.cwd()


def module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result


def main():
    helper = module('readback_identity', HERE / 'assign_new_draft_ids.py')
    formula = module('readback_formula', HERE.parent / 'property-order-20261105/ref-id-data/prepare_ref_id.py')
    mapping = {}
    for batch in ('new-draft-application', 'graph-draft-application', 'historical-draft-application',
                  'versioned-draft-application'):
        for row in json.loads((HERE / batch / 'adoption-plan.json').read_text())['outputs']:
            mapping[row['source']] = row['path']
    for row in json.loads((HERE / 'recovery-application/adoption-plan.json').read_text())['operations']:
        mapping[row['before_path']] = row['after_path']
    rows = []
    for row in json.loads((HERE / 'census/census.json').read_text())['carriers']:
        path = mapping.get(row['path'], row['path'])
        source = ROOT / path
        assert source.is_file(), path
        raw = source.read_bytes()
        meta, _ = helper.n.read(raw)
        try:
            expected = formula.reference(meta.get('atom_id'), meta.get('version'), meta.get('status'))
            state = 'repaired' if meta.get('ref_id') == expected else 'mismatch'
        except ValueError as error:
            state, expected = 'held', str(error)
        rows.append(dict(original_path=row['path'], path=path, atom_id=meta.get('atom_id'),
                         status=meta.get('status'), version=meta.get('version'), ref_id=meta.get('ref_id'),
                         result=state, expected_or_reason=expected, sha256=helper.n.sha(raw)))
    counts = dict(Counter(row['result'] for row in rows))
    assert len(rows) == 206 and not counts.get('mismatch'), counts
    result = dict(scope='Original 206 holds; no admission or runtime claim', counts=counts,
                  missing_status=sum(not row['status'] for row in rows),
                  draft_lineage_identity_holds=sum(row['result'] == 'held' and row['status'] == 'Draft' for row in rows),
                  missing_current_ids=sum(not row['atom_id'] for row in rows), rows=rows)
    (HERE / 'progress-readback.json').write_text(json.dumps(result, indent=2) + '\n')
    print({key: value for key, value in result.items() if key != 'rows'})


if __name__ == '__main__':
    main()
