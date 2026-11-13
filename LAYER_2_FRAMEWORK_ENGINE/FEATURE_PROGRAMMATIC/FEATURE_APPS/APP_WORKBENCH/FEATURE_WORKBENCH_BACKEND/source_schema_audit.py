# CA-M-549@2
# CA-R-3066@2
"""Check parsed Atom rows against the installed, current declaration schema."""
from __future__ import annotations

from collections import defaultdict
from collections.abc import Mapping

from ATOM_LIFECYCLE.status_model import StatusModelError, canonical_status
from carrier_aliases import carrier_read_view, matches_named_value
from header_groups import header_value, path_value
from project_root_container import is_logical_container

from .header_columns import _matches_format
from .markdown_content import content_lines, direct_markdown, source_markdown


class SourceSchemaAudit:
    """The caller loads the model once and supplies each parsed source row."""

    def __init__(self, candidate_schema, status_model):
        self.schema = candidate_schema
        self.status_model = status_model
        self.header = candidate_schema.header(1)
        self._columns = {}

    def issues(self, row: Mapping) -> list[dict[str, str]]:
        issues = []

        def add(field, message):
            issues.append({'field': field, 'message': str(message)})

        projected = self._header(row, add)
        if projected is not None:
            self._content(row, projected, add)
        return issues

    def _header(self, row, add):
        root_header = row.get('_project_root_header')
        metadata = row.get('header_json') if root_header is None else root_header
        if not isinstance(metadata, dict):
            add('header', 'Header must be a mapping.')
            return None
        try:
            view = carrier_read_view(metadata)
        except ValueError as error:
            add('header', error)
            return None
        self._decode_roles(view, add)
        role, form = view.get('role'), view.get('form')
        projected = dict(row, role=role, form=form, header_json=metadata)
        self._check_role_status(view, add)
        self._check_formats(metadata, projected, add)
        constraints = self.schema.header_constraints.validate(view, metadata=metadata)
        for field, message, _allowed in constraints:
            add(field, message)
        if root_header is not None and not is_logical_container(view.get('container')) and not any(
            field == 'container' or field.startswith('container.') for field, _, _ in constraints
        ):
            add('container', 'Supply one Scope Unit or containing Atom.')
        return projected

    def _decode_roles(self, view, add):
        for field, alias in (('role', 'content_role'), ('form', 'type')):
            if isinstance(view.get(field), str):
                try:
                    view[field] = view[alias] = self.schema.role_form.decode(field, view[field])
                except ValueError as error:
                    add(field, error)

    def _check_role_status(self, view, add):
        role, form = view.get('role'), view.get('form')
        try:
            self.schema.validate_role_form(role, form)
        except ValueError as error:
            add('role' if role not in self.schema.role_form.roles else 'form', error)
        forms = self.schema.role_form.names('form')
        if isinstance(form, str) and forms and form not in forms:
            add('form', f'Form is not declared: {form}')

        if isinstance(role, str) and isinstance(form, str) and isinstance(view.get('status'), str):
            try:
                canonical_status(self.status_model, role, form, view['status'])
            except StatusModelError as error:
                add('status', error)

    def _check_formats(self, metadata, projected, add):
        role, form = projected.get('role'), projected.get('form')
        key = (role if isinstance(role, str) else None, form if isinstance(form, str) else None)
        columns = self._columns.get(key)
        if columns is None:
            columns = self._columns[key] = tuple(c for c in self.header.columns if c.applies(projected))
        for column in columns:
            try:
                present = (header_value(metadata, column.reader)[0] if column.reader is not None else
                           path_value(metadata, column.path)[0])
                value = self.header.value(projected, column)
                if present and not _matches_format(value, column.format):
                    add(column.name, f'Header {column.name} requires {column.format}')
            except (TypeError, ValueError, OverflowError) as error:
                add(column.name, error)

    def _content(self, row, projected, add):
        records = row.get('content_properties_json')
        if not isinstance(records, list):
            add('content', 'Parsed Content properties are unavailable.')
            return
        indexed = self._content_records(records, add)
        if indexed is None:
            return
        paths, children = indexed
        _, declared = self.schema.content._layout(projected)
        for path in sorted(declared & paths.keys()):
            if len(paths[path]) > 1:
                add('content.' + '.'.join(path), f'duplicate declared content property: {".".join(path)}')

        lines = None
        for rule in self.schema.content_constraints.records:
            kind, path, roles, forms, *_ = rule
            role, form = projected.get('role'), projected.get('form')
            if roles is not None and not any(matches_named_value(role, item) for item in roles):
                continue
            if forms is not None and not any(matches_named_value(form, item) for item in forms):
                continue
            if kind in {'value', 'heading_value'} and lines is None and (kind == 'value' or paths.get(path)):
                body = source_markdown(row)
                lines = content_lines(body) if isinstance(body, str) else []
            self._content_rule(rule, paths, children, lines, add)

    @staticmethod
    def _content_records(records, add):
        paths = defaultdict(list)
        children = defaultdict(list)
        for record in records:
            if not isinstance(record, Mapping) or not isinstance(record.get('property_path'), list):
                add('content', 'Parsed Content property is invalid.')
                return None
            path = tuple(record['property_path'])
            if not path or any(not isinstance(part, str) for part in path):
                add('content', 'Parsed Content property path is invalid.')
                return None
            paths[path].append(record)
            children[path[:-1]].append(record)
        return paths, children

    @staticmethod
    def _content_rule(rule, paths, children, lines, add):
        kind, path, _roles, _forms, low, high, allowed, source = rule
        present = paths.get(path, ())
        label = '.'.join(path)
        if kind == 'children':
            if not present:
                return
            names = [item['property_path'][-1] for item in children.get(path, ())]
            if any(name not in allowed for name in names) or not low <= len(names) <= high or len(names) != len(set(names)):
                add('content.' + label, f'Content {label} requires {low}..{high} unique children from {", ".join(allowed)} ({source})')
        elif kind == 'heading' and not low <= len(present) <= high:
            add('content.' + label, f'Content {label} requires {low}..{high} occurrences ({source})')
        elif kind in {'value', 'heading_value'}:
            if kind == 'heading_value' and not present:
                return
            count = sum(bool(direct_markdown(item, children.get(path, ()), lines)) for item in present)
            if not low <= count <= high:
                add('content.' + label, f'Content {label} requires {low}..{high} direct Markdown values ({source})')
