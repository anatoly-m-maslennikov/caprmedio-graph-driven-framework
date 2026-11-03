#!/usr/bin/env python3
"""Plan or apply a hash-pinned, explicit ordinary RMED carrier migration."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import stat
import sys
import tempfile
import yaml

from claim import Ambiguous, migrate_claim

ROOT = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(ROOT / 'LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_TOOLS'))
from atom_operations import atom_identity_lock


def digest(data):
    return hashlib.sha256(data).hexdigest()


def remove_cfel_references(text):
    """Remove entity-reference markers inside CFEL, leaving quoted literals intact."""
    result = []
    marker = None
    for line in text.splitlines(keepends=True):
        opening = re.match(r'^\s*(`{3,}|~{3,})\s*CFEL\s*$', line, re.I)
        if marker is None and opening:
            marker = opening.group(1); result.append(line); continue
        if marker is not None and re.match(r'^\s*' + re.escape(marker[0]) + r'{' + str(len(marker)) + r',}\s*$', line):
            marker = None; result.append(line); continue
        if marker is None:
            result.append(line); continue
        out, quote, escaped = [], None, False
        for i, char in enumerate(line):
            if quote:
                out.append(char)
                if escaped: escaped = False
                elif char == '\\': escaped = True
                elif char == quote: quote = None
            elif char in ('"', "'"):
                quote = char; out.append(char)
            elif char == '@' and (i == 0 or not (line[i-1].isalnum() or line[i-1] in '_.@-')) and i + 1 < len(line) and (line[i+1].isalpha() or line[i+1] in '(_'):
                continue
            else:
                out.append(char)
        if quote:
            raise Ambiguous('unterminated quoted literal in CFEL')
        result.append(''.join(out))
    return ''.join(result)


def remove_subject_references(frontmatter):
    root = yaml.compose(frontmatter, Loader=yaml.SafeLoader)
    if not isinstance(root, yaml.nodes.MappingNode):
        raise Ambiguous('line 1: expected frontmatter mapping')
    subjects = [v for k, v in root.value if isinstance(k, yaml.nodes.ScalarNode) and k.value == 'subjects']
    if len(subjects) > 1: raise Ambiguous('line 1: duplicate subjects')
    if not subjects: return frontmatter
    edits = []
    def visit(node):
        if isinstance(node, yaml.nodes.MappingNode):
            for _, value in node.value: visit(value)
        elif isinstance(node, yaml.nodes.SequenceNode):
            for value in node.value: visit(value)
        elif isinstance(node, yaml.nodes.ScalarNode) and node.tag == 'tag:yaml.org,2002:str':
            a, b = node.start_mark.index, node.end_mark.index
            original = frontmatter[a:b]
            # Complex YAML quoting or multiline values need human review.
            value = original[1:-1] if original.startswith(('"', "'")) and original.endswith(original[0]) else original
            if any(c in value for c in ("'", '"', '\\', '\n', '\r')):
                if '@' in value: raise Ambiguous(f'line {node.start_mark.line + 2}: complex quoted Subject')
                return
            changed = re.sub(r'(?<![\w.@-])@(?=[A-Za-z_(])', '', value)
            replacement = original[0] + changed + original[-1] if value != original else changed
            if replacement != original: edits.append((a, b, replacement))
        else:
            raise Ambiguous('line 1: unsupported Subject structure')
    visit(subjects[0])
    for a, b, replacement in sorted(edits, reverse=True):
        frontmatter = frontmatter[:a] + replacement + frontmatter[b:]
    return frontmatter


def expose_subject_quotes(frontmatter):
    """Hide YAML serialization quotes, leaving Subject-expression literals visible."""
    root = yaml.compose(frontmatter, Loader=yaml.SafeLoader)
    edits, quotes = [], []
    def visit(node):
        if isinstance(node, yaml.nodes.MappingNode):
            for _, value in node.value: visit(value)
        elif isinstance(node, yaml.nodes.SequenceNode):
            for value in node.value: visit(value)
        elif isinstance(node, yaml.nodes.ScalarNode) and node.style in ("'", '"'):
            a, b = node.start_mark.index, node.end_mark.index
            for position in (a, b - 1):
                quotes.append(frontmatter[position])
                edits.append((position, position + 1, '\x00SUBJECTQUOTE' + str(len(quotes) - 1) + '\x00'))
            # YAML escapes semantic quote delimiters inside its own quoted scalar.
            pattern = r"''.*?''" if node.style == "'" else r'\\".*?\\"'
            for match in re.finditer(pattern, frontmatter[a + 1:b - 1]):
                quotes.append(match.group())
                edits.append((a + 1 + match.start(), a + 1 + match.end(), '\x00SUBJECTQUOTE' + str(len(quotes) - 1) + '\x00'))
    for key, value in root.value:
        if key.value == 'subjects': visit(value)
    for start, stop, replacement in sorted(edits, reverse=True):
        frontmatter = frontmatter[:start] + replacement + frontmatter[stop:]
    return frontmatter, quotes


def transform(raw, mapping):
    overrides = [row for row in mapping.get('reviewed_source_overrides', [])
                 if row['before_sha256'] == digest(raw)]
    if len(overrides) > 1:
        raise Ambiguous('duplicate reviewed override preimage')
    if overrides:
        row = overrides[0]
        candidate = row['candidate'].encode('utf-8')
        if digest(candidate) != row['candidate_sha256']:
            raise Ambiguous('reviewed override candidate hash mismatch')
        raw = candidate
    text = raw.decode('utf-8')
    delimiters = list(re.finditer(r'(?m)^---[ \t]*(?:\r?\n|$)', text))
    if len(delimiters) < 2 or delimiters[0].start():
        raise Ambiguous('line 1: expected frontmatter')
    # Keep frontmatter physical layout unchanged. Field values may contain references.
    end = delimiters[1].end()
    try:
        body = migrate_claim(text[end:])
    except Ambiguous as error:
        message = str(error)
        match = re.match(r'line (\d+):', message)
        if match:
            message = f'line {int(match.group(1)) + text[:end].count(chr(10))}:' + message[match.end():]
        raise Ambiguous(message) from error
    original_metadata = yaml.safe_load(text[delimiters[0].end():delimiters[1].start()])
    mapped_ids = dict(mapping.get('base_atom_id_replacements', {}), **mapping.get('atom_id_replacements', {}))
    if original_metadata.get('status') == 'Draft' and original_metadata.get('atom_id') in mapped_ids:
        raise Ambiguous('Draft identity is a mapped old authority ID; resolve identity before migration')
    frontmatter = remove_subject_references(text[delimiters[0].end():delimiters[1].start()])
    frontmatter, subject_quotes = expose_subject_quotes(frontmatter)
    text = remove_cfel_references(text[:delimiters[0].end()] + frontmatter + text[delimiters[1].start():end] + body)
    literals = []
    def hide_literal(match):
        literals.append(match.group())
        return '\x00LITERAL' + str(len(literals) - 1) + '\x00'
    text = re.sub(r'(?m)^atom_id:[^\r\n]*', hide_literal, text)
    text = re.sub(r'"(?:\\.|[^"\\\r\n])*"|\'(?:\\.|[^\'\\\r\n])*\'', hide_literal, text)
    # These obsolete addresses are model aliases, not generic English synonyms.
    text = re.sub(r'(?<![\w/])Entity/Object/Continuant/Governing Objects/Atom(?=[/.(\s]|$)', 'Atom', text)
    roles = r'(?:Requirement|Operations|Evaluation|Delivery|Concern|Method|Plan)'
    forms = r'(?:Term Definition|Project Goal|Eng Decision|Constraint|Workflow|Action|Demand|Goal|Step|Plan)'
    role_prefix = r'(?<![\w./])Atom/Content Role: (' + roles + r')(?![\w])'
    text = re.sub(role_prefix + r'/Type: (' + forms + r')(?![\w])',
                  lambda m: 'Atom/(.Header.Role := ' + m.group(1) + ')/(.Header.Form := ' + m.group(2) + ')', text)
    text = re.sub(role_prefix + r'/Type(?![\w:])',
                  lambda m: 'Atom/(.Header.Role := ' + m.group(1) + ').Header.Form', text)
    text = re.sub(role_prefix, lambda m: 'Atom/(.Header.Role := ' + m.group(1) + ')', text)
    text = re.sub(r'(?<![\w./])Atom/Content Role(?![\w:])', 'Atom.Header.Role', text)
    text = re.sub(r'(?<![\w./])Atom/Type(?![\w:])', 'Atom.Header.Form', text)
    text = re.sub(r'(?<![\w.])Projection\.Type(?![\w])', 'Projection.Form', text)
    text = re.sub(r'(?<![\w.])(Projection/\(\.)Type(?=\s*(?::=|:|=|in\b))', r'\1Form', text)
    text = re.sub(r'(?<![\w.])Atom\.Content\.Claim Scope(?![\w])', 'Atom.Content.Claim.Prose Claim', text)
    paths = sorted(mapping['full_property_paths'], key=lambda row: len(row['old']), reverse=True)
    # A single substitution pass prevents one mapping from changing the output of another.
    lookup = {row['old']: row['new'] for row in paths}
    pattern = re.compile(r'(?<![\w.])(?:' + '|'.join(re.escape(k) for k in lookup) + r')(?![\w])')
    text = pattern.sub(lambda m: lookup[m.group()], text)
    ids = dict(mapping.get('base_atom_id_replacements', {}))
    for old, new in mapping.get('atom_id_replacements', {}).items():
        if old in ids and ids[old] != new:
            raise ValueError(f'conflicting ID mapping: {old}')
        ids[old] = new
    if ids:
        id_pattern = re.compile(r'(?<![\w-])(?:' + '|'.join(re.escape(k) for k in sorted(ids, key=len, reverse=True)) + r')(?![\w-]|@\d)')
        text = id_pattern.sub(lambda m: ids[m.group()], text)
    fields = sorted(set(mapping.get('atom_header_fields', [])) | {'Type', 'Content Role', 'Version Number'}, key=len, reverse=True)
    if fields:
        field_pattern = '|'.join(re.escape(field) for field in fields)
        renamed = {'Type': 'Form', 'Content Role': 'Role', 'Version Number': 'Version'}
        # A binding supplies the receiver type for subsequent variable field paths.
        bound = set(re.findall(r'Atom//(\$[A-Za-z_]\w*)', text))
        other = set(re.findall(r'(?:Scope Unit|Projection|Event Record)//(\$[A-Za-z_]\w*)', text))
        if bound & other:
            raise Ambiguous('variable has conflicting Atom and other receiver bindings')
        def qualify(match):
            return match.group(1) + 'Header.' + renamed.get(match.group(2), match.group(2))
        text = re.sub(r'(Atom//\$[A-Za-z_]\w*\.)(' + field_pattern + r')(?![\w])', qualify, text)
        for variable in bound:
            text = re.sub(r'(?<![\w/])(' + re.escape(variable) + r'\.)(' + field_pattern + r')(?![\w])', qualify, text)
        text = re.sub(r'(Atom/\(\.)(' + field_pattern + r')(?=\s*(?::=|in\b|=|\)))', qualify, text)
        text = re.sub(r'(Atom/\([^\n]*?\)\.)(' + field_pattern + r')(?![\w])', qualify, text)
        def qualify_filters(match):
            return re.sub(r'(?<![\w.])(\.)(' + field_pattern + r')(?![\w])', qualify, match.group())
        text = re.sub(r'\bAtom(?:/\([^()\n]*\))+', qualify_filters, text)

    known_other_receivers = set(re.findall(r'(?:Scope Unit|Projection|Event Record)//(\$[A-Za-z_]\w*)', text))
    relation_token = r'(?:\(\([A-Za-z_]\w*\)\)|\+>|<\+)'
    old_bound = r'\{(\d+(?:\+|\.\.\d+)?)\}'
    text = re.sub(old_bound + r'(?=\s*' + relation_token + r')', lambda m: '{:' + m.group(1) + '}', text)
    text = re.sub('(' + relation_token + r'\s*)' + old_bound,
                  lambda m: m.group(1) + '{:' + m.group(2) + '}', text)
    # Cardinalities are optional. Only the obsolete colon outside braces is invalid.
    fence = False
    for number, line in enumerate(text.splitlines(), 1):
        if re.match(r'^\s*```\s*CFEL\s*$', line, re.I): fence = True; continue
        if fence and re.match(r'^\s*```\s*$', line): fence = False; continue
        visible = re.sub(r'"(?:\\.|[^"\\])*"|\'(?:\\.|[^\'\\])*\'', '', line)
        if any(match.group(1) not in known_other_receivers for match in re.finditer(r'(\$[A-Za-z_]\w*)\.(?:ID|Version)\b', visible)):
            raise Ambiguous(f'line {number}: unbound variable field receiver')
        if fence and re.search(r'\)\)\s*:', visible):
            raise Ambiguous(f'line {number}: relation colon outside cardinality braces')
    text = re.sub(r'\x00SUBJECTQUOTE(\d+)\x00', lambda m: subject_quotes[int(m.group(1))], text)
    text = re.sub(r'\x00LITERAL(\d+)\x00', lambda m: literals[int(m.group(1))], text)
    return text.encode('utf-8')


def atomic_replace(path, data):
    mode = stat.S_IMODE(path.stat().st_mode)
    fd, name = tempfile.mkstemp(dir=path.parent, prefix=f'.{path.name}.')
    try:
        with os.fdopen(fd, 'wb') as stream:
            stream.write(data); stream.flush(); os.fsync(stream.fileno())
        os.chmod(name, mode); os.replace(name, path)
    finally:
        if os.path.exists(name): os.unlink(name)


def plan(paths, mapping, root=ROOT):
    records, held, seen = [], [], set()
    root = root.resolve()
    for name in paths:
        path = Path(name)
        path = (root / path).resolve() if not path.is_absolute() else path.resolve()
        if not path.is_relative_to(root) or path in seen or path.suffix.lower() != '.md':
            raise ValueError(f'invalid or duplicate source: {name}')
        seen.add(path)
        raw = path.read_bytes()
        try:
            candidate = transform(raw, mapping)
        except (Ambiguous, UnicodeDecodeError, yaml.YAMLError) as error:
            held.append({'path': str(path), 'reason': str(error)})
            continue
        records.append({'path': str(path), 'before_sha256': digest(raw), 'after_sha256': digest(candidate), 'candidate': candidate.decode('utf-8')})
    return {'mapping': mapping, 'records': records, 'held': held}


def apply_records(manifest, root=ROOT):
    if manifest['held']:
        raise ValueError('plan has held files; resolve them before applying')
    root = root.resolve()
    with atom_identity_lock(root):
        pending = []
        seen = set()
        for row in manifest['records']:
            path = Path(row['path']).resolve()
            if not path.is_relative_to(root) or path in seen or path.suffix.lower() != '.md':
                raise ValueError(f'invalid source: {path}')
            seen.add(path)
            raw = path.read_bytes()
            if digest(raw) == row['after_sha256']: continue
            candidate = row['candidate'].encode('utf-8')
            if digest(raw) != row['before_sha256'] or digest(candidate) != row['after_sha256'] or transform(raw, manifest['mapping']) != candidate:
                raise ValueError(f'concurrent drift or invalid candidate: {path}')
            pending.append((path, raw, candidate))
        written = []
        try:
            for path, before, candidate in pending:
                if digest(path.read_bytes()) != digest(before): raise ValueError(f'concurrent drift: {path}')
                atomic_replace(path, candidate)
                written.append((path, before, digest(candidate)))
        except BaseException as error:
            failures = []
            for path, before, after in reversed(written):
                try:
                    if digest(path.read_bytes()) != after: raise ValueError('changed after write')
                    atomic_replace(path, before)
                except (OSError, ValueError) as rollback_error:
                    failures.append(f'{path}: {rollback_error}')
            if failures: raise RuntimeError(f'{error}; rollback failed: {failures}') from error
            raise
        return len(written)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest='command', required=True)
    p = commands.add_parser('plan')
    p.add_argument('--sources', type=Path, required=True)
    p.add_argument('--map', type=Path, required=True)
    p.add_argument('--output', type=Path, required=True)
    p = commands.add_parser('apply')
    p.add_argument('manifest', type=Path)
    args = parser.parse_args()
    if args.command == 'plan':
        mapping = json.loads(args.map.read_text())
        paths = [line.strip() for line in args.sources.read_text().splitlines() if line.strip() and not line.lstrip().startswith('#')]
        result = plan(paths, mapping)
        args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
        print(f"planned {len(result['records'])}; held {len(result['held'])}")
    else:
        print(f"applied {apply_records(json.loads(args.manifest.read_text()))}")


if __name__ == '__main__': main()
