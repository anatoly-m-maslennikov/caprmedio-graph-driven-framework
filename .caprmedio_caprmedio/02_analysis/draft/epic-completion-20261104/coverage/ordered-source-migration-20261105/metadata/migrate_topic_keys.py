"""Rename native Atom topic keys without reserializing YAML or Markdown."""
from pathlib import Path
import hashlib
import json
import re
import sys
import yaml
from yaml.nodes import MappingNode

ROOT = Path.cwd()
CONTROL = ROOT / '.caprmedio_caprmedio'
HERE = Path(__file__).resolve().parent
ROLES = {'01_concern': ('C', 'Concern'), '02_analysis': ('A', 'Analysis'),
         '03_plan': ('P', 'Plan'), '04_requirement': ('R', 'Requirement'),
         '05_method': ('M', 'Method'), '06_evaluation': ('E', 'Evaluation'),
         '07_delivery': ('D', 'Delivery'), '09_operations': ('O', 'Operations'),
         '09_ops': ('O', 'Operations')}
STATUSES = {'draft', 'backlog', 'done', 'canceled', 'cancelled', 'active'}
KEYS = {'active': 'main_subject', 'governs': 'main_subject',
        'passive': 'dependencies', 'depend_on': 'dependencies', 'depends_on': 'dependencies'}


def sha(data):
    return hashlib.sha256(data).hexdigest()


def parts(raw):
    text = raw.decode('utf-8')
    match = re.match(r'\A---\r?\n(.*?)^---[ \t]*(?:\r?\n|$)', text, re.M | re.S)
    if not match:
        raise ValueError('missing frontmatter')
    return text, match, match.group(1)


def unique_mapping(node):
    if not isinstance(node, MappingNode):
        raise ValueError('expected mapping')
    names = [key.value for key, _ in node.value]
    if len(names) != len(set(names)):
        raise ValueError('duplicate YAML keys')
    return dict((key.value, (key, value)) for key, value in node.value)


def rename(raw):
    text, match, header = parts(raw)
    tree = unique_mapping(yaml.compose(header))
    before = yaml.safe_load(header)
    if 'subjects' not in tree:
        return raw
    if 'topics' in tree:
        raise ValueError('both subjects and topics present')
    subject_key, subject_value = tree['subjects']
    children = unique_mapping(subject_value)
    unknown = set(children) - set(KEYS)
    if unknown:
        raise ValueError('unmapped subject keys: ' + repr(sorted(unknown)))
    mapped = [KEYS[key] for key in children]
    if len(mapped) != len(set(mapped)):
        raise ValueError('multiple old keys map to the same Topic key')
    edits = [(subject_key, 'topics')]
    edits.extend((children[key][0], KEYS[key]) for key in children)
    result = header
    for node, replacement in sorted(edits, key=lambda pair: pair[0].start_mark.index, reverse=True):
        token = header[node.start_mark.index:node.end_mark.index]
        quote = token[0] if token and token[0] in "\"'" else ''
        result = result[:node.start_mark.index] + quote + replacement + quote + result[node.end_mark.index:]
    expected = dict(before)
    expected['topics'] = {KEYS[key]: value for key, value in expected.pop('subjects').items()}
    assert yaml.safe_load(result) == expected, 'metadata values changed'
    updated = (text[:match.start(1)] + result + text[match.end(1):]).encode('utf-8')
    assert parts(updated)[0][parts(updated)[1].end():] == text[match.end():], 'body changed'
    return updated


def native_role(path):
    components = path.relative_to(CONTROL).parts
    if len(components) == 1:
        match = re.match(r'CA-([CAPRMEDO])-\d+(?:[-@.]|$)', path.name)
        return next((name for name, value in ROLES.items() if match and value[0] == match[1]), None)
    role_positions = [index for index, name in enumerate(components[:-1]) if name in ROLES]
    if not role_positions:
        return None
    index = role_positions[0]
    if not all(re.fullmatch(r'CA-SU-\d+_.+', name) for name in components[:index]):
        return None
    role = components[index]
    tail = components[index + 1:-1]
    if not all(name.lower() in STATUSES or re.match(r'(?:\d+-)?CA-' + ROLES[role][0] + r'-\d+[-@]', name) for name in tail):
        return None
    if not re.match(r'(?:\d+-)?CA-' + ROLES[role][0] + r'-(?:\d+|draft)?(?:[-@.]|$)', path.name):
        return None
    return role


def self_check():
    examples = [
        "---\nsubjects:\n  active: X\n  passive:\n  - A\n  - B\n  - C\nrole: Requirement\n---\n## Claim\ntext\n",
        "---\r\nsubjects: {active: X, passive: [A, B]} # comment\r\n---\r\nbody\r\n",
        "---\n'subjects':\n  \"governs\": X\n  depend_on: []\n---\nbody\n",
        "---\nsubjects:\n  active: >-\n    X Y\n  passive: A\n---\nbody\n",
    ]
    for text in examples:
        result = rename(text.encode())
        assert rename(result) == result
        assert 'subjects' not in yaml.safe_load(parts(result)[2])
    try:
        rename(b'---\nsubjects: {active: A, governs: B}\n---\n')
    except ValueError:
        pass
    else:
        raise AssertionError('ambiguous mapping accepted')


def prepare():
    if (HERE / 'adoption-receipt.json').exists():
        raise ValueError('applied plan is retained; prepare a separate delta rather than overwrite it')
    operations, holds, inventory = [], [], []
    for path in sorted(CONTROL.rglob('*.md')):
        role = native_role(path)
        if not role:
            continue
        raw = path.read_bytes()
        relative = path.relative_to(ROOT).as_posix()
        row = {'path': relative, 'before_sha256': sha(raw)}
        try:
            _, _, header = parts(raw)
            metadata = yaml.safe_load(header)
            if not isinstance(metadata, dict):
                raise ValueError('frontmatter is not a mapping')
            declared_role = re.sub(r'[^a-z]', '', str(metadata.get('role', '')).lower())
            if declared_role not in {'', ROLES[role][1].lower(), 'analysisadvisory' if role == '02_analysis' else ''}:
                raise ValueError('role disagrees with native directory')
            if str(metadata.get('status')).lower() == 'archived':
                continue
            row.update(atom_id=metadata.get('atom_id'), status=metadata.get('status'),
                       foreign_owner=any(p.startswith(('CA-SU-43_', 'CA-SU-47_', 'CA-SU-48_')) for p in path.parts))
            inventory.append(row)
            after = rename(raw)
            if after != raw:
                operations.append(dict(row, before=raw.decode(), after=after.decode(), after_sha256=sha(after)))
        except (ValueError, yaml.YAMLError) as error:
            holds.append(dict(row, reason=str(error)))
    plan = {'status': 'PREPARED', 'scope': 'native modern Current and Draft Atom metadata only; no archives, source copies, Journals or projections',
            'native_workflow_admission': False, 'journal_append': False,
            'inventory': inventory, 'holds': holds, 'operations': operations}
    (HERE / 'safe-topic-key-plan.json').write_text(json.dumps(plan, indent=2, ensure_ascii=False) + '\n')
    from collections import Counter
    print(json.dumps({'inventory': len(inventory), 'operations': len(operations), 'holds': len(holds), 'hold_reasons': dict(Counter(row['reason'] for row in holds))}, ensure_ascii=False))


if __name__ == '__main__':
    self_check()
    prepare()
