"""Omit empty optional Header Properties; preserve populated values and content."""
from pathlib import Path
import importlib.util
import json
import re
import yaml

ROOT = Path.cwd()
HERE = Path(__file__).resolve().parent
SNAPSHOT = ROOT / '.caprmedio_caprmedio/02_analysis/draft/epic-completion-20261104/coverage/ordered-source-migration-20261105/property-audit/snapshot.json'


def main():
    helper = ROOT / '.caprmedio_caprmedio/03_plan/CA-P-2694-EPIC--entity-graph-refactor-stage-4-polishing/model-header-content-20261103/integration/adopt.py'
    spec = importlib.util.spec_from_file_location('empty_property_adoption', helper)
    n = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(n)
    n.ROOT = ROOT
    target = HERE / 'empty-properties-application'
    target.mkdir(exist_ok=True)
    assert not (target / 'adoption-plan.json').exists()
    operations, holds = [], []
    counts = {'relations': 0, 'topics.dependencies': 0}
    for row in json.loads(SNAPSHOT.read_text())['carriers']:
        path = ROOT / row['path']
        if not path.is_file():
            continue
        before = path.read_bytes()
        text = before.decode()
        match = re.match(r'\A---\r?\n(.*?)^---[ \t]*(?:\r?\n|$)', text, re.M | re.S)
        assert match
        header = match[1]
        metadata = yaml.safe_load(header)
        expected = dict(metadata)
        tree = yaml.compose(header)
        edits = []

        def remove(mapping, key):
            entry = next((k, v) for k, v in mapping.value if k.value == key)
            k, v = entry
            if mapping.flow_style:
                raise ValueError('flow mapping needs an exact reviewed edit')
            start = header.rfind('\n', 0, k.start_mark.index) + 1
            end = v.end_mark.index
            if v.end_mark.column:
                end = header.find('\n', end)
                end = len(header) if end == -1 else end + 1
            edits.append((start, end))

        try:
            if metadata.get('relations') == {}:
                remove(tree, 'relations')
                expected.pop('relations')
                counts['relations'] += 1
            topics = metadata.get('topics')
            if isinstance(topics, dict) and topics.get('dependencies') == []:
                assert len(topics) > 1, 'empty Topics needs a separate missing-subject disposition'
                topics_node = next(v for k, v in tree.value if k.value == 'topics')
                remove(topics_node, 'dependencies')
                expected['topics'] = {k: v for k, v in topics.items() if k != 'dependencies'}
                counts['topics.dependencies'] += 1
        except ValueError as error:
            holds.append({'path': row['path'], 'reason': str(error)})
            continue
        if not edits:
            continue
        result = header
        for start, end in sorted(edits, reverse=True):
            result = result[:start] + result[end:]
        assert yaml.safe_load(result) == expected, row['path']
        after = (text[:match.start(1)] + result + text[match.end(1):]).encode()
        assert after.split(b'---', 2)[2] == before.split(b'---', 2)[2]
        operations.append({'path': row['path'], 'before': text, 'after': after.decode(), 'before_sha256': n.sha(before), 'after_sha256': n.sha(after)})
    assert not holds, holds
    plan = {'scope': 'Remove only empty optional Relations mappings and empty optional Topics.Dependencies lists.',
            'counts': counts, 'holds': holds, 'outputs': [r['path'] for r in operations], 'operations': operations,
            'native_workflow_admission': False, 'journal_append': False}
    (target / 'adoption-plan.json').write_text(json.dumps(plan, indent=2) + '\n')
    n.HERE = target
    n.apply()
    print(json.dumps(counts))


if __name__ == '__main__':
    main()
