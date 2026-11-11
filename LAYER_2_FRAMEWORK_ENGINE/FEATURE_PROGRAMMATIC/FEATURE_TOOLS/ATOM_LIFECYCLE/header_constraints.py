# CA-O-10002@2

"""Compile a bounded subset of explicit Header property declarations.

Compile explicit property and finite child cardinality and literal value domains.
"""
from dataclasses import dataclass
import re

from FEATURE_WORKBENCH_BACKEND.declaration_cfel import formal_claim_blocks, model_statements
from carrier_aliases import matches_named_value
from header_groups import GROUP_FIELDS, ROLE_FIELDS, header_value, path_value

_PATH = r'[A-Za-z][A-Za-z0-9_ ]*(?:\.[A-Za-z][A-Za-z0-9_ ]*)*'
_SELECTED = r'(?:"[^"\r\n]+"|[A-Za-z][A-Za-z0-9 &_-]*)'
_SELECTOR = (rf'(?:/\(\s*\.Header\.(?:Context\.)?(Role|Form)\s*'
             rf'((?::=|:)\s*{_SELECTED}|in\s*\(\s*{_SELECTED}\s*\))\s*\))?')
_PROPERTY = re.compile(rf'^Atom{_SELECTOR}\.Header\.({_PATH})\s*\{{::\s*([01])\s*\}}\s*::')
_DOMAIN = re.compile(rf'^Atom{_SELECTOR}\.Header\.({_PATH})(?:\s*\{{::\s*[01]\s*\}})?\s*::\s*\[\s*in\s*\(([^()]*)\)\s*\]')
_NAME = re.compile(r'^(?:"[^"\r\n]+"|[A-Za-z][A-Za-z0-9 &_-]*)$')
_LITERAL = re.compile(rf'^Atom{_SELECTOR}\.Header\.({_PATH})\s*::?\s*({_NAME.pattern[1:-1]})$')
_CHILDREN = re.compile(rf'^Atom{_SELECTOR}\.Header\.({_PATH})\.\*\s*\[\s*in\s*\(([^()]*)\)\s*\]'
                       r'\s*\{::\s*(\d+)(?:\.\.(\d+))?\s*\}$')


def _path(value):
    parts = [re.sub(r'\s+', '_', p.strip()).lower() for p in value.split('.')]
    if len(parts) > 1 and parts[0] in GROUP_FIELDS:
        group, leaf = parts[:2]
        if group == 'identity' and leaf == 'id':
            parts[:2] = ['atom_id']
        elif leaf in GROUP_FIELDS[group]:
            parts.pop(0)
        elif group == 'context' and len(parts) > 2 and parts[2] in ROLE_FIELDS.get(leaf, ()):
            parts = parts[2:]
    parts[0] = {'id': 'atom_id', 'carrier_destination': 'destination'}.get(parts[0], parts[0])
    return '.'.join(parts)


def _value(view, path):
    return header_value(view, _path(path))


def _group(metadata, name, fields):
    _, stored = path_value(metadata, tuple(name.split('.')))
    values = {_path(key): value for key, value in stored.items()} if isinstance(stored, dict) else {}
    for field in fields:
        address = f'{name}.{field}' if '.' in name else field
        present, value = header_value(metadata, address)
        if present:
            values[field] = value
    return values


def _logical_groups(metadata, role):
    projection = dict(metadata)
    for group, fields in GROUP_FIELDS.items():
        values = _group(metadata, group, fields)
        if values:
            projection[group] = values
    for group, fields in ROLE_FIELDS.items():
        if matches_named_value(role, group.capitalize()):
            values = _group(metadata, f'context.{group}', fields)
            if values:
                projection.setdefault('context', {})[group] = values
    return projection


def _selected(value):
    if value is None:
        return ''
    text = value.partition('(')[2][:-1] if value.startswith('in') else value.lstrip(':=')
    return text.strip().strip('"')


def compile_header_constraints(rows):  # noqa: C901
    records = set()
    for row in rows:
        for block in formal_claim_blocks(row['_content_bytes'].decode('utf-8')):
            for statement in model_statements(block):
                if match := _PROPERTY.match(statement):
                    selector, selected, path, count = match.groups()
                    records.add(('property', _path(path), selector.lower() if selector else '',
                                 _selected(selected), count, row['id']))
                if match := _DOMAIN.match(statement):
                    selector, selected, path, values = match.groups()
                    literals = [v.strip() for v in values.split(',')]
                    if literals and all(_NAME.fullmatch(v) for v in literals):
                        for literal in literals:
                            records.add(('domain', _path(path), selector.lower() if selector else '',
                                         _selected(selected), literal.strip('"'), row['id']))
                elif match := _LITERAL.fullmatch(statement):
                    selector, selected, path, literal = match.groups()
                    logical = _path(path)
                    if logical not in {'role', 'form', 'status'}:
                        records.add(('domain', logical, selector.lower() if selector else '',
                                     _selected(selected), literal.strip('"'), row['id']))
                elif match := _CHILDREN.fullmatch(statement):
                    selector, selected, path, names, low, high = match.groups()
                    values = [name.strip() for name in names.split(',')]
                    if values and all(_NAME.fullmatch(name) for name in values):
                        bounds = (int(low), int(high or low), *(sorted(_path(name.strip('"')) for name in values)))
                        records.add(('children', _path(path), selector.lower() if selector else '',
                                     _selected(selected), bounds, row['id']))
    keys = ('kind', 'path', 'selector', 'selected', 'value', 'source')
    return [dict(zip(keys, item)) for item in sorted(records)]


@dataclass(frozen=True)
class HeaderConstraints:
    properties: tuple
    domains: tuple
    children: tuple = ()

    def validate(self, view, *, metadata=None):
        metadata = _logical_groups(view if metadata is None else metadata, view.get('role'))
        errors = []
        for path, selector, selected, count, source in self.properties:
            if selector and not matches_named_value(view.get(selector), selected):
                continue
            logical = _path(path)
            parent_path = logical.rpartition('.')[0]
            if parent_path and not isinstance(_value(metadata, parent_path)[1], dict):
                continue
            present, _ = _value(metadata, logical)
            if (count == '1' and not present) or (count == '0' and present):
                field = self._missing_field(view, logical) if not present else path
                errors.append((field, f'Header {path} requires property cardinality {count} ({source}).', None))
        for path, selector, selected, values, source in self.domains:
            if selector and not matches_named_value(view.get(selector), selected):
                continue
            present, current = _value(metadata, path)
            named = _path(path) in {'role', 'form', 'status'}
            if present and (not isinstance(current, str) or not any(
                matches_named_value(current, value) if named else current == value for value in values
            )):
                errors.append((path, f'Header {path} must use a declared value ({source}).', values))
        errors.extend(self._validate_children(view, metadata))
        return errors

    def _missing_field(self, view, path):
        for group, selector, selected, bounds, _ in self.children:
            if (_path(group) == path and bounds[:2] == (1, 1) and len(bounds) == 3
                    and (not selector or matches_named_value(view.get(selector), selected))):
                return _path(f'{path}.{bounds[2]}')
        return path

    def _validate_children(self, view, metadata):
        for path, selector, selected, value, source in self.children:
            if selector and not matches_named_value(view.get(selector), selected):
                continue
            present, group = _value(metadata, path)
            if not present:
                continue
            low, high, *names = value
            keys = set(group) if isinstance(group, dict) else set()
            if not low <= len(keys) <= high or keys - set(names):
                yield path, f'Header {path} requires {low}..{high} children from {", ".join(names)} ({source}).', None


def load_header_constraints(records, source_ids):  # noqa: C901
    if not isinstance(records, list):
        raise ValueError('invalid Header constraint records')
    seen, properties, domains, children = set(), [], {}, []
    for row in records:
        if not isinstance(row, dict) or set(row) != {'kind', 'path', 'selector', 'selected', 'value', 'source'}:
            raise ValueError('invalid Header constraint record')
        kind, path, selector, selected, value, source = (row[k] for k in ('kind', 'path', 'selector', 'selected', 'value', 'source'))
        if (any(not isinstance(v, str) for v in (kind, path, selector, selected, source))
                or kind not in {'property', 'domain', 'children'} or not re.fullmatch(r'[a-z0-9_]+(?:\.[a-z0-9_]+)*', path)
                or selector not in {'', 'role', 'form'} or bool(selector) != bool(selected)
                or source not in source_ids):
            raise ValueError('invalid Header constraint record')
        if kind == 'children':
            if (not isinstance(value, (list, tuple)) or len(value) < 3
                    or any(type(bound) is not int for bound in value[:2]) or not 0 <= value[0] <= value[1]
                    or any(not isinstance(name, str) or not re.fullmatch(r'[a-z0-9_]+', name) for name in value[2:])):
                raise ValueError('invalid Header child constraint')
            value = tuple(value)
        elif not isinstance(value, str) or not value or (kind == 'property' and value not in {'0', '1'}):
            raise ValueError('invalid Header constraint value')
        key = (kind, path, selector, selected, value, source)
        if key in seen:
            raise ValueError('duplicate Header constraint record')
        seen.add(key)
        if kind == 'property':
            properties.append((path, selector, selected, value, source))
        elif kind == 'children':
            children.append((path, selector, selected, value, source))
        else:
            domains.setdefault((path, selector, selected, source), set()).add(value)
    return HeaderConstraints(tuple(properties), tuple((*key[:3], frozenset(values), key[3]) for key, values in sorted(domains.items())), tuple(children))
