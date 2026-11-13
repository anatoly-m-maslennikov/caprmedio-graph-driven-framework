"""Convert the supported literal CFEL statements to Python model declarations."""

from __future__ import annotations

import argparse
import ast
import hashlib
import json
import re
import sys
from pathlib import Path


_WORKBENCH_APP = str(Path(__file__).resolve().parents[1] / "FEATURE_APPS" / "APP_WORKBENCH")
if _WORKBENCH_APP not in sys.path:
    sys.path.insert(0, _WORKBENCH_APP)


_COUNT = r"(?:\d+\+?|\d+\.\.\d+)"
_NAME = r"(?:[A-Za-z_][A-Za-z_0-9 -]*|\"(?:\\.|[^\"\\])*\"|'(?:\\.|[^'\\])*')"
_ADDRESS = re.compile(r"""^[A-Za-z_$(][A-Za-z_0-9.$/* ()"'<>|[\],:=+\-]*$""")
_CHILDREN = re.compile(
    rf"^(?P<address>.+?)\.\*\[\s*(?:(?P<format>string)\s*,\s*)?"
    rf"in\s*\((?P<names>.*?)\)\s*\]\s*\{{\s*::\s*(?P<count>{_COUNT})\s*\}}$"
)
_DOMAIN = re.compile(
    rf"^(?P<address>.+?)\s*::\s*\[\s*in\s*\((?P<values>.*?)\)\s*\]"
    rf"\s*\{{\s*::\s*(?P<count>{_COUNT})\s*\}}$"
)
_PROPERTY = re.compile(
    rf"^(?P<address>.+?)(?:\s*\{{\s*::\s*(?P<occurrences>{_COUNT})\s*\}})?"
    rf"\s*::\s*(?:\[\s*(?P<format>[^\[\]{{}};]*)\s*\])?"
    rf"\s*(?:\{{\s*::\s*(?P<values>{_COUNT})\s*\}})?$"
)
_LITERAL = re.compile(rf"^(?P<address>.+?)\s*::\s*(?P<value>{_NAME})$")
_CHILD_COUNT = re.compile(
    rf'^(?P<address>.+?)\.(?P<stars>\*{{1,2}})\[(?P<format>string|[A-Za-z_][A-Za-z_ 0-9/$]*//[A-Za-z_$0-9_]*|)\]'
    rf'\{{::(?P<count>{_COUNT})\}}$'
)
_CLASSIFY = re.compile(
    rf'^(?P<address>.+?)\s*(?P<operator>>\||\(\(HAS_CLASSIFICATION\)\))'
    rf'\s*(?P<group>\()?(?P<axis>[A-Za-z][A-Za-z_0-9 ]*?)\s*(?P<comparison>==|:)'
    rf'\s*(?P<value>{_NAME}|-?\d+)\)?$'
)
_PATH_TEMPLATE = re.compile(r'^(?P<address>.+?)\s*==\s*PATH_TEMPLATE\((?P<template>"(?:\\.|[^"\\])*")\)$')
_COPY_VALUE = re.compile(r'^(?P<address>.+?)\s*==\s*(?P<source>\$[A-Za-z_]\w*\.[A-Za-z_][A-Za-z_0-9. ]*)$')
_MINIMUM = re.compile(r'^(?P<address>.+?)\s*>=\s*(?P<minimum>-?\d+)$')
_OCCURRENCES = re.compile(rf'^(?P<address>.+?)\s*\{{::(?P<count>{_COUNT})\}}$')
_UNIQUE = re.compile(r'^UNIQUE\(\s*(?P<population>.+?)\s*,\s*\((?P<keys>[^()]+)\)\s*\)$')
_QUALIFIED_PATH = re.compile(r'^([A-Za-z_][A-Za-z_ 0-9.]*)(?:/\(\.[A-Za-z_][A-Za-z_0-9. ]* in \([^()]+\)\))+(?:[/.][A-Za-z_$][A-Za-z_$ 0-9./]*)?$')
_INSTANCE_BINDING = re.compile(r'^\$[a-zA-Z_]\w*\[<[A-Za-z_][A-Za-z_0-9 /]*>\]$')
_FORM_ROLES = re.compile(
    r'^FOR EACH \$(?P<participant>[A-Za-z_]\w*)\[<Atom>,\s*\(\.Header\.Context\.Form\s*=\s*'
    r'(?P<form>[A-Za-z_][A-Za-z_0-9 ]*?)\)\]\s*:\s*\(\s*'
    r'\$(?P=participant)\.Header\.Context\.Role\s*::\s*\[in\s*\((?P<roles>[^()]*)\)\]\{::1\}\s*\)$'
)
_RELATION = re.compile(
    rf"^(?P<source>.+?)\s*(?:\{{\s*::\s*(?P<source_count>{_COUNT})\s*\}}\s*)?"
    rf"(?P<reverse><)?\(\((?P<name>[A-Za-z_][A-Za-z_0-9]*|\*)\)\)"
    rf"\s*(?:\{{\s*::\s*(?P<target_count>{_COUNT})\s*\}}\s*)?(?P<target>.*?)$"
)
_SET_VALUE = re.compile(rf'^(?P<address>.+?)\s*==\s*(?P<value>{_NAME}|-?\d+)$')
_LEXEMES = re.compile(
    r'''"(?:\\.|[^"\\])*"|'(?:\\.|[^'\\])*'|[A-Za-z_$][A-Za-z_0-9$]*|'''
    r'''\d+|::|\.\.|;>|:=|==|\(\(|\)\)|[^\s]'''
)
_ADDRESS_TOKENS = re.compile(r"""\"(?:\\.|[^"\\])*\"|'(?:\\.|[^'\\])*'|[()[\]"']""")


def _address(value: str) -> bool:
    """Accept literal paths and balanced qualified selectors only."""
    if not _ADDRESS.fullmatch(value) or '::' in value or '==' in value:
        return False
    stack = []
    for token in _ADDRESS_TOKENS.findall(value):
        if token in ('(', '['):
            stack.append(token)
        elif token in (')', ']'):
            if not stack or stack.pop() != {')': '(', ']': '['}[token]:
                return False
        elif token in ('"', "'"):
            return False
    return not stack


def _names(value: str) -> tuple[str, ...] | None:
    """Keep written quotes and escapes on each literal name."""
    items = []
    position = 0
    while position < len(value):
        match = re.match(rf"\s*({_NAME})\s*(,|$)", value[position:])
        if match is None:
            return None
        items.append(match.group(1).strip())
        position += match.end()
        if match.group(2) == ',' and position == len(value):
            return None
    return tuple(items) if items else None


def _literal_names(items: tuple[str, ...]) -> tuple[str, ...] | None:
    values = []
    for item in items:
        if item.startswith('"'):
            try:
                value = json.loads(item)
            except json.JSONDecodeError:
                return None
            if not isinstance(value, str):
                return None
            values.append(value)
        elif item.startswith("'"):
            return None
        else:
            values.append(item)
    return tuple(values)


def _call(function: str, **keywords: object) -> str:
    args = [ast.keyword(arg=key, value=ast.Constant(value=value) if not isinstance(value, tuple)
                        else ast.Tuple(elts=[ast.Constant(value=item) for item in value], ctx=ast.Load()))
            for key, value in keywords.items() if value is not None]
    expression = ast.Expression(body=ast.Call(func=ast.Name(id=function, ctx=ast.Load()), args=[], keywords=args))
    return ast.unparse(ast.fix_missing_locations(expression))


def _accepted(source: str, python: str) -> str | None:
    """Require the shared reader to reproduce every CFEL lexeme."""
    from python_model_claim import PythonModelClaimError, parse_python_model_claim

    try:
        restored = parse_python_model_claim(python)
    except PythonModelClaimError:
        return None
    if len(restored) != 1 or _LEXEMES.findall(restored[0]) != _LEXEMES.findall(source):
        return None
    return python


def convert_statement(statement: str) -> str | None:
    """Return one Python call, or None when a statement is outside this cohort."""
    text = statement.strip()
    if not text:
        return None
    # Normalize line wrapping only when every token remains the same.
    flattened = ' '.join(text.splitlines())
    if _LEXEMES.findall(text) != _LEXEMES.findall(flattened):
        return None
    text = flattened
    if match := _FORM_ROLES.fullmatch(text):
        roles = _names(match['roles'])
        if roles is not None:
            return _accepted(text, _call('allow_roles_for_form', form=match['form'], roles=roles,
                                        participant=match['participant'] if match['participant'] != 'a' else None))
    if re.match(r'^(?:IF|THEN|ELSE|FOR EACH|AND|OR)\b', text):
        return None

    if '<+' in text:
        container, *parts = tuple(part.strip() for part in text.split('<+'))
        if all(_address(side) for side in (container, *parts)):
            return _accepted(text, _call('composition', container=container, parts=tuple(parts)))

    if '>>' in text:
        source, separator, carrier = text.partition('>>')
        if separator and _address(source.strip()) and _address(carrier.strip()) and '>>' not in carrier:
            return _accepted(text, _call('deliver', source=source.strip(), carrier=carrier.strip()))

    if match := _CLASSIFY.fullmatch(text):
        address, value = match['address'].strip(), match['value']
        if _address(address):
            if re.fullmatch(r'-?\d+', value):
                value = int(value)
            notation = ('relation' if match['operator'].startswith('((')
                        else 'allowed' if match['comparison'] == ':' else None)
            return _accepted(text, _call('classify', address=address, axis=match['axis'], value=value,
                                        grouped=True if match['group'] else None, notation=notation))
        return None

    if match := _PATH_TEMPLATE.fullmatch(text):
        address = match['address'].strip()
        try:
            template = json.loads(match['template'])
        except ValueError:
            return None
        if _address(address):
            return _accepted(text, _call('path_template', address=address, template=template))
        return None

    if match := _COPY_VALUE.fullmatch(text):
        address, source = match['address'].strip(), match['source'].strip()
        if _address(address) and _address(source):
            return _accepted(text, _call('copy_value', address=address, source=source))
        return None

    if match := _MINIMUM.fullmatch(text):
        address = match['address'].strip()
        if _address(address):
            return _accepted(text, _call('minimum_value', address=address, minimum=int(match['minimum'])))
        return None

    if match := _UNIQUE.fullmatch(text):
        population = match['population'].strip()
        keys = tuple(key.strip() for key in match['keys'].split(','))
        if _address(population) and all(re.fullmatch(r'\.[A-Za-z_][A-Za-z_0-9 .]*', key) for key in keys):
            return _accepted(text, _call('unique', population=population, keys=keys))
        return None

    if match := _CHILD_COUNT.fullmatch(text):
        address = match['address'].strip()
        if _address(address):
            return _accepted(text, _call('children', address=address, occurrences=match['count'],
                                        name_format=match['format'] or None,
                                        recursive=True if match['stars'] == '**' else None))
        return None

    if ';>' in text:
        parts = text.split(';>')
        if len(parts) == 2 and all(_address(part.strip()) for part in parts):
            return _accepted(text, _call('order_before', first=parts[0].strip(), second=parts[1].strip()))

    if match := _CHILDREN.fullmatch(text):
        address = match['address'].strip()
        names = _names(match['names'])
        if _address(address) and names is not None:
            return _accepted(text, _call('allowed_children', address=address, names=names,
                                        occurrences=match['count'], name_format=match['format']))
        return None

    if match := _OCCURRENCES.fullmatch(text):
        address = match['address'].strip()
        if _address(address):
            if '//' in address:
                return _accepted(text, _call('population', address=address, count=match['count']))
            return _accepted(text, _call('property_rule', address=address, occurrences=match['count']))

    if match := _DOMAIN.fullmatch(text):
        address = match['address'].strip()
        raw_values = _names(match['values'])
        values = _literal_names(raw_values) if raw_values is not None else None
        if _address(address) and values is not None:
            return _accepted(text, _call('allowed_values', address=address, values=values,
                                        occurrences=match['count'],
                                        quoted=True if all(item.startswith('"') for item in raw_values) else None))
        return None

    if match := _PROPERTY.fullmatch(text):
        address = match['address'].strip()
        format_name = match['format'].strip() if match['format'] is not None else None
        if (_address(address)
                and (format_name is not None or match['values'] is not None)
                and (format_name is None or re.fullmatch(r'[A-Za-z_0-9 ,.+/$-]*', format_name))):
            return _accepted(text, _call('property_rule', address=address, value_format=format_name,
                                        occurrences=match['occurrences'], values=match['values']))
        return None

    if match := _LITERAL.fullmatch(text):
        address = match['address'].strip()
        values = _literal_names((match['value'],))
        if _address(address) and values is not None:
            return _accepted(text, _call('allowed_values', address=address, values=values,
                                        quoted=True if match['value'].startswith('"') else None))
        return None

    if match := _SET_VALUE.fullmatch(text):
        address, value = match['address'].strip(), match['value']
        if _address(address):
            if value in ('true', 'false'):
                value = value == 'true'
            elif re.fullmatch(r'-?\d+', value):
                value = int(value)
            return _accepted(text, _call('set_value', address=address, value=value))
        return None

    if match := _RELATION.fullmatch(text):
        source = match['source'].strip()
        target = match['target'].strip()
        if _address(source) and (not target or _address(target)):
            return _accepted(text, _call('relation', source=source, name=match['name'], target=target or None,
                                        source_count=match['source_count'], target_count=match['target_count'],
                                        reverse=True if match['reverse'] else None))
        return None

    if _address(text) and text not in {'IF', 'THEN', 'ELSE', 'AND', 'OR'}:
        from subject_notation import SubjectNotationError, parse_subject_expression

        try:
            parse_subject_expression(text, subject_profile='approved')
        except (SubjectNotationError, ValueError):
            if not (_QUALIFIED_PATH.fullmatch(text) or _INSTANCE_BINDING.fullmatch(text)):
                return None
        return _accepted(text, _call('subject_path', address=text))
    return None


def _parts(text: str) -> list[tuple[str, str]] | None:
    """Split statements at semicolons and retain whole-line comments."""
    parts = []
    pending = ''
    quote = None
    escaped = False
    for line in text.splitlines():
        if line.lstrip().startswith('#') and quote is None:
            if pending.strip():
                return None
            parts.append(('comment', line.strip()))
            continue
        for index, char in enumerate(line):
            if escaped:
                escaped = False
            elif quote and char == '\\':
                escaped = True
            elif char in {'"', "'"}:
                if quote == char:
                    quote = None
                elif quote is None:
                    quote = char
            elif char == '#' and quote is None:
                return None
            if char == ';' and quote is None and line[index:index + 2] != ';>':
                if pending.strip():
                    parts.append(('statement', pending.strip()))
                pending = ''
            else:
                pending += char
        pending += '\n'
    if quote is not None:
        return None
    if pending.strip():
        parts.append(('statement', pending.strip()))
    return parts


def convert_claim(text: str) -> str | None:
    """Convert a complete Claim only when every statement is supported."""
    parts = _parts(text)
    if parts is None:
        return None
    output = []
    count = 0
    for kind, value in parts:
        if kind == 'comment':
            output.append(value)
        else:
            converted = convert_statement(value)
            if converted is None:
                return None
            count += 1
            output.append(converted)
    return '\n'.join(output) if count else None


def convert_markdown_claim(body: str) -> str | None:
    """Replace one complete Claim/Formal Claim fence, preserving other Markdown."""
    from markdown_it import MarkdownIt
    from FEATURE_WORKBENCH_BACKEND.markdown_content import content_key

    headings: list[tuple[int, str]] = []
    fences = []
    tokens = MarkdownIt('commonmark').parse(body)
    for index, token in enumerate(tokens):
        if token.type == 'heading_open':
            level = int(token.tag[1:])
            while headings and headings[-1][0] >= level:
                headings.pop()
            headings.append((level, content_key(tokens[index + 1].content)))
        elif token.type == 'fence' and tuple(name for _, name in headings) == ('claim', 'formal_claim'):
            fences.append(token)
    if len(fences) != 1 or fences[0].info.strip().casefold() != 'cfel' or fences[0].map is None:
        return None

    lines = body.splitlines(keepends=True)
    start, end = fences[0].map
    if end - start < 2:
        return None
    opening = re.fullmatch(r'(?P<indent> {0,3})(?P<marks>`{3,}|~{3,})[ \t]*[Cc][Ff][Ee][Ll][ \t]*(?P<ending>\r?\n)', lines[start])
    if opening is None:
        return None
    marks = opening['marks']
    if not re.fullmatch(rf" {{0,3}}{re.escape(marks[0])}{{{len(marks)},}}[ \t]*(?:\r?\n)?", lines[end - 1]):
        return None

    converted = convert_claim(fences[0].content)
    if converted is None:
        return None
    ending = opening['ending']
    rendered = ending.join(converted.split('\n')) + ending
    return ''.join(lines[:start]) + opening['indent'] + marks + 'python' + ending + rendered + ''.join(lines[end - 1:])


def convert_carrier(raw: bytes, path: Path) -> bytes | None:
    """Convert one carrier while preserving its exact Header and line endings."""
    from VALIDATE_ATOMS.validate_atoms_workers.parsing import parse_carrier

    parsed = parse_carrier(raw, path)
    match = re.search(rb"\r?\n---\r?\n", raw)
    if match is None:
        return None
    start = match.end()
    body = raw[start:].decode('utf-8')
    if body.replace('\r\n', '\n') != parsed.body:
        return None
    converted = convert_markdown_claim(body)
    return None if converted is None else raw[:start] + converted.encode('utf-8')


def audit(frontier: Path, *, stage: Path | None = None) -> dict[str, object]:
    """Check the pinned frontier and optionally write a separate converted cohort."""
    from FEATURE_WORKBENCH_BACKEND.declaration_cfel import formal_claim_blocks
    from VALIDATE_ATOMS.validate_atoms_workers.parsing import parse_carrier

    manifest = json.loads(frontier.read_text())
    counts: dict[str, dict[str, int]] = {}
    conversions: dict[Path, bytes] = {}
    unsupported: list[dict[str, object]] = []
    for record in manifest['records']:
        group = record['status_group']
        if group == 'Current':
            candidate = record.get('source_path_check', {}).get('candidate')
            entries = [row for row in record['candidates'] if row['path'] == candidate and row['contains_cfel']]
        else:
            entries = [row for row in record['candidates'] if row['contains_cfel']]
        if len(entries) != 1:
            continue
        entry = entries[0]
        path = Path(entry['path'])
        raw = path.read_bytes()
        if hashlib.sha256(raw).hexdigest() != entry['sha256']:
            raise ValueError(f'Pinned source changed: {path}')
        body = parse_carrier(raw, path).body
        blocks = formal_claim_blocks(body)
        if not blocks:
            continue
        group_counts = counts.setdefault(group, {'claims': 0, 'convertible': 0})
        group_counts['claims'] += 1
        converted = convert_carrier(raw, path)
        if converted is not None:
            group_counts['convertible'] += 1
            conversions[path] = converted
        else:
            unsupported.append({'reference': record['reference'], 'version': entry.get('version'),
                                'status_group': group, 'path': str(path)})
    if stage is not None:
        for path in conversions:
            if path.is_absolute() or '..' in path.parts:
                raise ValueError(f'Stage requires repository-relative source paths: {path}')
        stage.mkdir(parents=True, exist_ok=False)
        for path, payload in conversions.items():
            output = stage / path
            output.parent.mkdir(parents=True, exist_ok=True)
            output.write_bytes(payload)
    return {'frontier': str(frontier), 'groups': counts, 'unsupported': unsupported}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--audit', required=True, type=Path, help='Pinned CFEL source frontier JSON')
    parser.add_argument('--stage', type=Path, help='New directory for converted carrier copies')
    args = parser.parse_args()
    print(json.dumps(audit(args.audit, stage=args.stage), indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
