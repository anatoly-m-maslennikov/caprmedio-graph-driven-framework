"""Reconcile derived Header data/order on fresh successors of concurrent edits."""
from pathlib import Path
import contextlib
import importlib.util
import json
import re
import yaml

ROOT = Path.cwd()
HERE = Path(__file__).resolve().parent


def module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result


n = module('concurrent_order_adoption', ROOT / '.caprmedio_caprmedio/03_plan/CA-P-2694-EPIC--entity-graph-refactor-stage-4-polishing/model-header-content-20261103/integration/adopt.py')
n.ROOT = ROOT
order = module('concurrent_order_transform', HERE / 'migration/prepare_order.py')
ref = module('concurrent_ref_transform', HERE / 'ref-id-data/prepare_ref_id.py')


def main():
    batch = HERE / 'concurrent-reconciliation'
    batch.mkdir(exist_ok=True)
    assert not (batch / 'adoption-plan.json').exists()
    prior = json.loads((HERE / 'migration/stable-application/adoption-plan.json').read_text())
    paths = set()
    consumed = []
    for row in prior['held']:
        path = ROOT / row['path']
        if path.exists():
            paths.add(path)
        else:
            consumed.append(row['path'])
            identity = re.search(r'CA-[CAPRMEDO]-\d+', path.name)
            if identity and path.parent.name == 'draft':
                paths.update(path.parent.parent.glob(identity[0] + '-*.md'))
    operations, held, corrected = [], [], []
    with n.atom_identity_lock(ROOT):
        for path in sorted(paths):
            before = path.read_bytes()
            text = before.decode()
            match = re.match(r'\A---\r?\n(.*?)^---[ \t]*(?:\r?\n|$)', text, re.M | re.S)
            assert match
            header = match[1]
            assert not re.search(r'(?m)^\s*#', header), 'preserve commented Header using a reviewed span edit'
            meta = yaml.safe_load(header)
            expected = dict(meta)
            try:
                value = ref.reference(meta.get('atom_id'), meta.get('version'), meta.get('status'))
                if expected.get('ref_id') != value:
                    corrected.append({'path': str(path.relative_to(ROOT)), 'old': expected.get('ref_id'), 'new': value})
                    expected['ref_id'] = value
            except ValueError as error:
                held.append({'path': str(path.relative_to(ROOT)), 'reason': str(error)})
            if expected.get('relations') == {}:
                expected.pop('relations')
            topics = expected.get('topics')
            if isinstance(topics, dict) and topics.get('dependencies') == []:
                expected['topics'] = {key: value for key, value in topics.items() if key != 'dependencies'}
                assert expected['topics']
            ranked = {key: expected[key] for key in order.HEADER_ORDER if key in expected}
            ranked.update({key: value for key, value in expected.items() if key not in ranked})
            body, hold, _, _, check = order.reorder_content(text[match.end():])
            assert not hold and check['preservation_check'] == 'PASS'
            after = '---\n' + yaml.safe_dump(ranked, sort_keys=False, allow_unicode=True, width=1000) + '---\n' + body
            actual = re.match(r'\A---\r?\n(.*?)^---[ \t]*(?:\r?\n|$)', after, re.M | re.S)
            assert actual and yaml.safe_load(actual[1]) == expected and after[actual.end():] == body
            if after != text:
                operations.append({'path': str(path.relative_to(ROOT)), 'before': text, 'after': after, 'before_sha256': n.sha(before), 'after_sha256': n.sha(after.encode())})
        plan = {'scope': 'Fresh derived Ref ID and serialization repairs; all business values, Version and Updated At preserved.',
                'consumed_draft_paths': consumed, 'ref_id_corrections': corrected, 'holds': held,
                'outputs': [row['path'] for row in operations], 'operations': operations,
                'native_workflow_admission': False, 'journal_append': False}
        (batch / 'adoption-plan.json').write_text(json.dumps(plan, indent=2) + '\n')
        n.HERE = batch
        outer = n.atom_identity_lock
        n.atom_identity_lock = lambda _: contextlib.nullcontext()
        try:
            n.apply()
        finally:
            n.atom_identity_lock = outer
    print(json.dumps({'sources': len(paths), 'consumed_drafts': len(consumed), 'ref_id_corrections': len(corrected), 'holds': held}))


if __name__ == '__main__':
    main()
