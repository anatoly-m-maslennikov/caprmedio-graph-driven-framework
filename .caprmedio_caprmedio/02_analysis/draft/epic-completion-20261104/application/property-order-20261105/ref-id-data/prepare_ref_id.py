"""Prepare Ref IDs from explicit identity/state; never assign missing identity."""
from pathlib import Path
import hashlib
import json
import re
import yaml

ROOT = Path.cwd()
HERE = Path(__file__).resolve().parent
SNAPSHOT = ROOT / '.caprmedio_caprmedio/02_analysis/draft/epic-completion-20261104/coverage/ordered-source-migration-20261105/property-audit/snapshot.json'


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def reference(identity, version, status):
    if not isinstance(identity, str) or not isinstance(status, str) or not status.strip():
        raise ValueError('missing explicit Atom ID or Status')
    match = re.fullmatch(r'(CA-[CAPRMEDO]-\d+)(?:@(\d+)?(-draft|draft)?)?', identity)
    if not match:
        raise ValueError('unallocated or invalid Atom ID')
    base = match[1]
    group = status.casefold()
    if group not in ('draft', 'archived'):
        if identity != base:
            raise ValueError('qualified identity outside Draft/Archived')
        return base
    if not isinstance(version, int) or isinstance(version, bool) or version < 1:
        raise ValueError('missing or invalid Version')
    if match[2] and int(match[2]) != version:
        raise ValueError('identity marker conflicts with Version')
    if identity != base and group == 'draft' and not identity.endswith('draft'):
        raise ValueError('Draft identity marker lacks draft suffix')
    return f'{base}@{version}' + ('-draft' if group == 'draft' else '')


def prepare():
    assert reference('CA-P-123', 2, 'Draft') == 'CA-P-123@2-draft'
    assert reference('CA-P-123', 1, 'Archived') == 'CA-P-123@1'
    for state in ('Active', 'Done', 'Backlog', 'Canceled'):
        assert reference('CA-P-123', 1, state) == 'CA-P-123'
    assert reference('CA-P-123@2-draft', 2, 'Draft') == 'CA-P-123@2-draft'
    assert reference('CA-P-123@draft', 2, 'Draft') == 'CA-P-123@2-draft'
    for args in [('CA-P-123', True, 'Draft'), ('CA-P-draft', 1, 'Draft'), ('CA-P-123@2-draft', 3, 'Draft'), ('CA-P-123', 1, None)]:
        try:
            reference(*args)
        except ValueError:
            pass
        else:
            raise AssertionError(args)
    operations, holds, unchanged = [], [], []
    for row in json.loads(SNAPSHOT.read_text())['carriers']:
        path = ROOT / row['path']
        if not path.is_file() or path.is_symlink():
            holds.append({'path': row['path'], 'reason': 'snapshot path missing or symlink'})
            continue
        before = path.read_bytes()
        text = before.decode()
        match = re.match(r'\A---\r?\n(.*?)^---[ \t]*(?:\r?\n|$)', text, re.M | re.S)
        if not match:
            holds.append({'path': row['path'], 'reason': 'frontmatter missing'})
            continue
        header = match[1]
        metadata = yaml.safe_load(header)
        if str(metadata.get('status')).casefold() == 'archived':
            continue
        try:
            ref = reference(metadata.get('atom_id'), metadata.get('version'), metadata.get('status'))
        except ValueError as error:
            holds.append({'path': row['path'], 'reason': str(error)})
            continue
        if 'ref_id' in metadata:
            if metadata['ref_id'] == ref:
                unchanged.append(row['path'])
            else:
                holds.append({'path': row['path'], 'reason': 'stored Ref ID conflicts with explicit identity/state', 'expected': ref})
            continue
        tree = yaml.compose(header)
        keys = [key.value for key, _ in tree.value]
        assert len(keys) == len(set(keys)), row['path']
        key, value = next((key, value) for key, value in tree.value if key.value == 'atom_id')
        if tree.flow_style or key.start_mark.line != value.end_mark.line:
            holds.append({'path': row['path'], 'reason': 'Atom ID is not a scalar block entry'})
            continue
        end = header.find('\n', value.end_mark.index)
        newline = '\r\n' if '\r\n' in header else '\n'
        if end == -1:
            updated = header + newline + 'ref_id: ' + ref + newline
        else:
            updated = header[:end + 1] + 'ref_id: ' + ref + newline + header[end + 1:]
        assert yaml.safe_load(updated) == dict(metadata, ref_id=ref)
        after = (text[:match.start(1)] + updated + text[match.end(1):]).encode()
        assert after.split(b'---', 2)[2] == before.split(b'---', 2)[2]
        operations.append({'path': row['path'], 'before': text, 'after': after.decode(), 'before_sha256': digest(before), 'after_sha256': digest(after), 'ref_id': ref})
    result = {'status': 'PREPARED_NOT_APPLIED', 'operations': operations, 'holds': holds, 'unchanged': unchanged}
    (HERE / 'planned-operations.json').write_text(json.dumps(result, indent=2) + '\n')
    from collections import Counter
    print(json.dumps({'operations': len(operations), 'holds': dict(Counter(item['reason'] for item in holds)), 'unchanged': len(unchanged)}))


if __name__ == '__main__':
    prepare()
