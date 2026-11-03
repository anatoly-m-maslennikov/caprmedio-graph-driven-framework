#!/usr/bin/env python3
"""Guarded model/instance CFEL migration; no writes unless apply is explicit."""
import argparse
import importlib.util
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[6]
OLD = ROOT / '.caprmedio_caprmedio/03_plan/CA-P-2694-EPIC--entity-graph-refactor-stage-4-polishing/model-header-content-20261103/migration'
sys.path.insert(0, str(OLD))
spec = importlib.util.spec_from_file_location('guarded_header_migration', OLD / 'migrate.py')
guards = importlib.util.module_from_spec(spec)
spec.loader.exec_module(guards)
Ambiguous = guards.Ambiguous
FENCE = re.compile(r'(?im)^([ \t]*)(`{3,}|~{3,})[ \t]*CFEL[ \t]*\r?\n')
KINDS = r'(?:Atom(?:/\([^()\n]*\))*|Scope Unit(?:/Project)?|Package(?:/Implementation)?|Event Record|Carrier(?:/Markdown_file)?|Projection|Workflow|Substep|Journal|Relation|Actor|Plan|Step|Action|Node|Project)'
BARE = re.compile(r'(?<![\w/$])(' + KINDS + r')//(?![\w$])')
TYPED = re.compile(r'//\$[A-Za-z_]\w*')
LITERAL = re.compile(r'"(?:\\.|[^"\\\r\n])*"|\'(?:\\.|[^\'\\\r\n])*\'')


def protect(text):
    values = []
    def save(match):
        values.append(match.group())
        return '\x00Q' + str(len(values) - 1) + '\x00'
    return re.sub(r'(?m)^[ \t]*#[^\r\n]*|' + LITERAL.pattern, save, text), values


def restore(text, values):
    return re.sub(r'\x00Q(\d+)\x00', lambda m: values[int(m.group(1))], text)


def statements(text):
    """Retain IF/THEN and parenthesized clauses as one semantic statement."""
    visible, quoted = protect(text)
    depth, start, result = 0, 0, []
    for index, char in enumerate(visible):
        if char == '(': depth += 1
        elif char == ')':
            depth -= 1
            if depth < 0: raise Ambiguous('unbalanced CFEL parentheses')
        elif char == ';' and depth == 0:
            result.append(restore(visible[start:index + 1].strip(), quoted)); start = index + 1
    if depth: raise Ambiguous('unbalanced CFEL parentheses')
    if visible[start:].strip(): result.append(restore(visible[start:].strip(), quoted))
    return result


def group_block(text):
    # Existing group comments are regenerated; all other comments remain with their statement.
    text = re.sub(r'(?im)^[ \t]*#\s*(?:model|instances)[ \t]*\r?\n', '', text)
    clauses = statements(text)
    used = set(re.findall(r'\$[A-Za-z_]\w*', text))
    instance_vars = set(re.findall(r'(?<!Relation)//(\$[A-Za-z_]\w*)', text))
    model, instances = [], []
    def fresh(kind):
        stem = re.sub(r'[^a-z0-9]+', '_', kind.split('/')[0].lower()).strip('_')
        number, variable = 1, '$' + stem
        while variable in used:
            number += 1; variable = '$' + stem + '_' + str(number)
        used.add(variable)
        return variable
    shared = {}
    for clause in clauses:
        visible, _ = protect(clause)
        matches = list(BARE.finditer(visible))
        repeated = {m.group(1) for m in matches if sum(n.group(1) == m.group(1) for n in matches) > 1}
        if re.search(r'\b(?:IF|THEN)\b', visible):
            for kind in sorted(repeated): shared.setdefault(kind, None)
        if re.search(r'Node//\s*\)\.\*\*|Node//\s*,', visible): shared.setdefault('Node', None)
    for kind in shared:
        shared[kind] = fresh(kind)
        instances.append(kind + '//' + shared[kind] + ';')
    for clause in clauses:
        visible, quoted = protect(clause)
        leading_comments = ''
        while True:
            prefix = re.match(r'\s*\x00Q(\d+)\x00\s*', visible)
            if not prefix or not quoted[int(prefix.group(1))].lstrip().startswith('#'): break
            leading_comments += prefix.group()
            visible = visible[prefix.end():]
        anonymous = list(BARE.finditer(visible))
        # Existing union Kind selections and post-instance filters retain their exact range.
        union = re.compile(r'(\(in\s*\([^()\n]+\)\))//(?![\w$])')
        had_union = bool(union.search(visible))
        visible = union.sub(lambda m: m.group(1) + '//' + fresh('selected'), visible)
        membership = re.search(r'\bIF\s+(\$[A-Za-z_]\w*)\s+in\s*\(', visible)
        model_membership = bool(membership and membership.group(1) not in instance_vars) and not TYPED.search(visible)
        # Repeated model selections keep one binding across the complete conclusion.
        if re.match(r'\s*IF\b', visible) and '(Node, Node.**)' in visible and membership is None:
            variable = fresh('model_node')
            rewritten = visible.replace('(Node, Node.**)', variable).rstrip().rstrip(';')
            visible = 'IF ' + variable + ' in (Node, Node.**) THEN (\n' + rewritten + ';\n);'
            model_membership = True
        data_atom = bool(re.match(r'\s*(?:IF\b|COUNT\s*\()', visible) and re.search(r'\bAtom(?:/\([^()\n]*\))*\.', visible))
        if data_atom:
            receivers = list(dict.fromkeys(re.findall(r'\bAtom(?:/\([^()\n]*\))*(?=\.)', visible)))
            prefixes = []
            for receiver in sorted(receivers, key=len, reverse=True):
                number, variable = 1, '$atom'
                while variable in used:
                    number += 1; variable = '$atom_' + str(number)
                used.add(variable)
                prefixes.append(receiver + '//' + variable + ';')
                visible = re.sub(r'(?<![\w/])' + re.escape(receiver) + r'(?=\.)', lambda _: variable, visible)
            visible = '\n\n'.join(prefixes + [visible])
        # A named Relation/Operator address describes the model, regardless of //.
        model_relation = model_membership or bool(re.match(r'\s*(?:Relation|Operator)//', visible)) or bool(re.match(r'\s*\$(?:property|classified|part)\b', visible) and re.search(r'\(\((?:IS_PROPERTY_OF|HAS_CLASSIFICATION|IS_CONTAINED_BY)\)\)', visible))
        instance = bool(anonymous or TYPED.search(visible) or data_atom or had_union) and not model_relation
        if re.match(r'\s*\$[A-Za-z_]\w*\s+\(\(NARROWER_THAN\)\)', visible):
            model_relation = True
        if not instance and re.search(r'\$[A-Za-z_]\w*', visible):
            instance = not model_relation
        def bind(match):
            kind = match.group(1)
            return shared[kind] if kind in shared else kind + '//' + fresh(kind)
        visible = BARE.sub(bind, visible)
        for variable in shared.values():
            visible = visible.replace('(' + variable + ').**', variable + '.**')
        # Detect unknown anonymous address shapes rather than leaving them silently unresolved.
        if re.search(r'//(?=[\s.{}();,]|$)', visible):
            raise Ambiguous('unrecognized anonymous instance receiver')
        (instances if instance else model).append(restore(leading_comments + visible, quoted))
    groups = []
    if model:
        if instances and not model[-1].rstrip().endswith(';'): model[-1] += ';'
        groups.append('# model\n' + '\n\n'.join(model))
    if instances: groups.append('# instances\n' + '\n\n'.join(instances))
    return '\n\n'.join(groups) + ('\n' if groups else '')


def transform(raw, mapping):
    text = raw.decode('utf-8')
    overrides = [row for row in mapping.get('reviewed_source_overrides', []) if row['before_sha256'] == guards.digest(raw)]
    if len(overrides) > 1: raise Ambiguous('duplicate reviewed override preimage')
    if overrides:
        candidate = overrides[0]['candidate'].encode()
        if guards.digest(candidate) != overrides[0]['candidate_sha256']: raise Ambiguous('override payload hash mismatch')
        text = candidate.decode()
    out, cursor = [], 0
    for opening in FENCE.finditer(text):
        if opening.start() < cursor: continue
        closing = re.search(r'(?m)^' + re.escape(opening[1]) + re.escape(opening[2][0]) + '{' + str(len(opening[2])) + r',}[ \t]*(?:\r?\n|$)', text[opening.end():])
        if not closing: raise Ambiguous('unclosed CFEL fence')
        start, stop = opening.end(), opening.end() + closing.start()
        body = group_block(text[start:stop])
        if mapping.get('rename_is_defined_by'):
            visible, quoted = protect(body)
            visible = re.sub(r'(?<![\w])IS_DEFINED_BY(?![\w])', 'IS_DECLARED_BY', visible)
            body = restore(visible, quoted)
        if '\r\n' in opening.group(): body = body.replace('\n', '\r\n')
        out.extend([text[cursor:start], body, text[stop:opening.end() + closing.end()]])
        cursor = opening.end() + closing.end()
    out.append(text[cursor:])
    text = ''.join(out)
    # Overrides may repair formal clauses, never mechanical carrier identity.
    before_header = re.split(r'(?m)^---[ \t]*\r?$', raw.decode('utf-8'), maxsplit=2)
    after_header = re.split(r'(?m)^---[ \t]*\r?$', text, maxsplit=2)
    if len(before_header) < 3 or len(after_header) < 3 or before_header[1] != after_header[1]:
        raise Ambiguous('carrier frontmatter changed or missing')
    def summary(body):
        lines, found = guards.sections(body)
        roots = [(i, name) for i, level, name in found if level == 2]
        for index, (position, name) in enumerate(roots):
            if name == 'summary':
                stop = roots[index + 1][0] if index + 1 < len(roots) else len(lines)
                return ''.join(lines[position + 1:stop])
        return None
    if summary(before_header[2]) != summary(after_header[2]):
        raise Ambiguous('carrier Summary changed')
    return text.encode('utf-8')


# Reuse the existing native lock, full SHA preflight, atomic writes and owned rollback.
guards.transform = transform
plan = guards.plan
apply_records = guards.apply_records


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command', required=True)
    p = sub.add_parser('plan'); p.add_argument('--frontier', type=Path, required=True); p.add_argument('--map', type=Path); p.add_argument('--output', type=Path, required=True)
    p = sub.add_parser('apply'); p.add_argument('manifest', type=Path)
    args = parser.parse_args()
    if args.command == 'plan':
        rows = json.loads(args.frontier.read_text())['operations']
        mapping = json.loads(args.map.read_text()) if args.map else {}
        for row in rows:
            source = (ROOT / row['destination_path']).resolve()
            if not source.is_relative_to(ROOT): raise ValueError('frontier path outside repository')
            if guards.digest(source.read_bytes()) != row['sha256']:
                raise ValueError('frontier snapshot drift: ' + row['destination_path'])
        result = plan([r['destination_path'] for r in rows], mapping)
        args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
        print(f"planned {len(result['records'])}; held {len(result['held'])}")
    else: print(f"applied {apply_records(json.loads(args.manifest.read_text()))}")


if __name__ == '__main__': main()
