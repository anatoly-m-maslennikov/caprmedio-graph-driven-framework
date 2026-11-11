# CA-O-10002@2

"""Compile finite Content constraints from Current formal declarations."""
from __future__ import annotations

from dataclasses import dataclass
import re

from carrier_aliases import matches_named_value
from FEATURE_WORKBENCH_BACKEND.content_schema import declaration_statements
from FEATURE_WORKBENCH_BACKEND.declaration_ancestry import compile_ancestry
from FEATURE_WORKBENCH_BACKEND.declaration_cfel import filters, intersect_selectors, segments
from FEATURE_WORKBENCH_BACKEND.markdown_content import content_key, parse_content, source_markdown

_CARD = r'\{\s*::\s*(\d+)(?:\s*\.\.\s*(\d+))?\s*\}'
_PROPERTY = re.compile(rf'^\s*{_CARD}\s*::')
_CHILDREN = re.compile(rf'^\s*\[\s*(?:string\s*,\s*)?in\s*\(([^()]*)\)\s*\]\s*{_CARD}\s*$')
_VALUE = re.compile(rf'^\s*(?:\[\s*(?:markdown|string)?\s*\]\s*)?{_CARD}\s*$')


def compile_content_constraints(rows):  # noqa: C901
    statements = (statement for row in rows for statement in declaration_statements(row))
    records = set()
    for projected in compile_ancestry(statements):
        statement = projected.statement
        if not statement.startswith('Atom') or '.Content.' not in statement:
            continue
        prefix, tail = statement.split('.Content', 1)
        path, remainder = segments(tail)
        if not path or '**' in path or '*' in path[:-1]:
            continue
        roles = intersect_selectors(filters(prefix, 'Role'), projected.roles)
        forms = intersect_selectors(filters(prefix, 'Form'), projected.forms)
        children = ()
        if path[-1] == '*':
            match = _CHILDREN.fullmatch(remainder)
            if not match:
                continue
            raw_names, lower, upper = match.groups()
            names = [name.strip() for name in raw_names.split(',')]
            if not names or any(not re.fullmatch(r'[A-Za-z][A-Za-z0-9 _-]*', name) for name in names):
                continue
            children = tuple(sorted(content_key(name) for name in names))
            path = path[:-1]
            bounds = [('children', lower, upper)]
        else:
            bounds = []
            if match := _PROPERTY.match(remainder):
                bounds.append(('heading', *match.groups()))
                value = _VALUE.fullmatch(remainder[match.end():])
                if value:
                    bounds.append(('heading_value', *value.groups()))
            elif remainder.strip().startswith('::') and (value := _VALUE.fullmatch(remainder.strip()[2:])):
                bounds.append(('value', *value.groups()))
        for kind, lower, upper in bounds:
            low, high = int(lower), int(upper or lower)
            if low > high:
                raise ValueError(f'{projected.source.reference}: invalid Content cardinality')
            records.add((kind, tuple(path), None if roles is None else tuple(sorted(roles)),
                         None if forms is None else tuple(sorted(forms)), low, high,
                         children, projected.source.reference))
    return [dict(zip(('kind', 'path', 'roles', 'forms', 'min', 'max', 'children', 'source'),
                     (kind, list(path), list(roles) if roles is not None else None,
                      list(forms) if forms is not None else None, low, high, list(children), source)))
            for kind, path, roles, forms, low, high, children, source in sorted(records, key=repr)]


@dataclass(frozen=True)
class ContentConstraints:
    records: tuple

    def validate(self, row):  # noqa: C901
        body = source_markdown(row)
        parsed = parse_content(body, tolerate_duplicate_siblings=True) if isinstance(body, str) else []
        paths = [tuple(item['property_path']) for item in parsed]
        for kind, path, roles, forms, low, high, children, source in self.records:
            if roles is not None and not any(matches_named_value(row.get('role'), role) for role in roles):
                continue
            if forms is not None and not any(matches_named_value(row.get('form'), form) for form in forms):
                continue
            if kind == 'children':
                if path not in paths:
                    continue
                actual = [item[-1] for item in paths if item[:-1] == path]
                if any(name not in children for name in actual) or not low <= len(actual) <= high or len(actual) != len(set(actual)):
                    raise ValueError(f'Content {".".join(path)} requires {low}..{high} unique children from {", ".join(children)} ({source})')
            elif kind == 'heading' and not low <= paths.count(path) <= high:
                raise ValueError(f'Content {".".join(path)} requires {low}..{high} occurrences ({source})')
            elif kind in {'value', 'heading_value'}:
                if kind == 'heading_value' and path not in paths:
                    continue
                count = sum(bool(item['direct_markdown']) for item, address in zip(parsed, paths) if address == path)
                if not low <= count <= high:
                    raise ValueError(f'Content {".".join(path)} requires {low}..{high} direct Markdown values ({source})')


def load_content_constraints(records, source_ids):
    if not isinstance(records, list):
        raise ValueError('invalid Content constraints')
    result, seen = [], set()
    for item in records:
        if not isinstance(item, dict) or set(item) != {'kind', 'path', 'roles', 'forms', 'min', 'max', 'children', 'source'}:
            raise ValueError('invalid Content constraint')
        kind, path, roles, forms, low, high, children, source = (item[k] for k in ('kind', 'path', 'roles', 'forms', 'min', 'max', 'children', 'source'))
        def valid_names(value, nullable=False):
            return (value is None and nullable) or (isinstance(value, list) and all(isinstance(x, str) and x for x in value) and len(value) == len(set(value)))
        if (kind not in ('heading', 'value', 'heading_value', 'children')
                or not valid_names(path) or not path or not valid_names(roles, True) or not valid_names(forms, True)
                or not valid_names(children) or type(low) is not int or type(high) is not int
                or bool(children) != (kind == 'children') or low < 0 or high < low
                or not isinstance(source, str) or source not in source_ids):
            raise ValueError('invalid Content constraint')
        key = (kind, tuple(path), None if roles is None else tuple(roles), None if forms is None else tuple(forms), low, high, tuple(children), source)
        if key in seen:
            raise ValueError('duplicate Content constraint')
        seen.add(key)
        result.append(key)
    return ContentConstraints(tuple(result))
