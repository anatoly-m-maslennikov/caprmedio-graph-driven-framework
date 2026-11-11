# CA-D-657@11

"""Private mechanical serialization of lifecycle Atom Carriers.

Editing a Header reserializes its YAML, so comments and presentation styles are
not retained. The Markdown body is preserved byte-for-byte unless supplied.
"""
from __future__ import annotations

from copy import deepcopy
from pathlib import Path
import re
from typing import Any

import yaml

from carrier_aliases import carrier_read_view
from header_groups import GROUP_ORDER, GROUP_FIELDS, ROLE_FIELDS, equal_values, header_field_paths, header_path, header_value, path_value
from VALIDATE_ATOMS.validate_atoms_workers.parsing import parse_carrier


def _set(metadata: dict[str, Any], path: tuple[str, ...], value: Any) -> None:
    parent = metadata
    for part in path[:-1]:
        if part not in parent:
            parent[part] = {}
        if not isinstance(parent[part], dict):
            raise ValueError(f"Header {'.'.join(path[:-1])} must be a mapping.")
        parent = parent[part]
    parent[path[-1]] = deepcopy(value)


def _source_parts(raw: bytes) -> tuple[dict[str, Any], str, str, str]:
    parsed = parse_carrier(raw, Path("<carrier>"))
    match = re.match(r"\A---\r?\n.*?\r?\n---\r?\n", parsed.text, re.DOTALL)
    if not match:
        raise ValueError("Carrier frontmatter boundary is unsupported.")
    newline = "\r\n" if parsed.text.startswith("---\r\n") else "\n"
    return deepcopy(parsed.metadata), match.group(), parsed.text[match.end():], newline


def _apply_fields(metadata: dict[str, Any], fields: dict[str, Any]) -> None:
    # Role determines where role-specific properties belong in a new Header.
    names = sorted(fields, key=lambda name: name not in ("role", "content_role", "context.role"))
    touched: set[tuple[str, ...]] = set()
    for name in names:
        paths = header_field_paths(name, metadata)
        present = [path for path in paths if path_value(metadata, path)[0]]
        for path in present or [header_path(name, metadata)]:
            if any(path[:len(other)] == other or other[:len(path)] == path for other in touched):
                raise ValueError("Overlapping Header field updates are ambiguous.")
            _set(metadata, path, fields[name])
            touched.add(path)


def logical_view(metadata, model):
    view = carrier_read_view(metadata)
    schema = getattr(model, 'candidate_schema', None)
    if schema is not None:
        for field, alias in (('role', 'content_role'), ('form', 'type')):
            if field in view:
                view[field] = view[alias] = schema.role_form.decode(field, view[field])
    return view


def _remove_header_path(metadata, path):
    current = metadata
    parents = []
    for part in path[:-1]:
        if not isinstance(current, dict) or part not in current:
            return
        parents.append((current, part))
        current = current[part]
    if not isinstance(current, dict) or path[-1] not in current:
        return
    del current[path[-1]]
    for parent, part in reversed(parents):
        if parent[part] != {}:
            break
        del parent[part]


def same_authored_carrier(left_raw, right_raw, model):
    """Compare authored properties and body, excluding revision-generated fields."""
    def normalized(raw):  # noqa: C901
        parsed = parse_carrier(raw, Path('<carrier>'))
        metadata = deepcopy(parsed.metadata)
        logical = {}
        names = (*GROUP_FIELDS['identity'], *GROUP_FIELDS['context'], *GROUP_FIELDS['state'],
                 *ROLE_FIELDS['concern'], *ROLE_FIELDS['plan'], 'destination')
        excluded = {'ref_id', 'version', 'updated_at', 'destination', 'status'}
        for name in names:
            present, value = header_value(metadata, name)
            if not present:
                continue
            if name not in excluded:
                if name in {'role', 'form'}:
                    schema = getattr(model, 'candidate_schema', None)
                    if schema is not None:
                        value = schema.role_form.decode(name, value)
                    elif isinstance(value, str):
                        value = value.casefold()
                logical[name] = value
            for path in header_field_paths(name, metadata):
                _remove_header_path(metadata, path)
        return logical, metadata, parsed.body

    left = normalized(left_raw)
    right = normalized(right_raw)
    return equal_values(left[0], right[0]) and equal_values(left[1], right[1]) and left[2] == right[2]


def render_carrier(raw: bytes | None, fields: dict[str, Any], *, body: str | None = None, model=None) -> bytes:
    """Apply supplied logical fields; an omitted body keeps the original bytes.

    Field keys use Header names or dotted paths. Existing equivalent aliases are
    updated together; absent aliases are never added. New Carriers use grouped
    Header paths. Header YAML is reserialized when fields are supplied.
    """
    if not isinstance(fields, dict) or any(not isinstance(k, str) or not k or any(not p for p in k.split('.')) for k in fields):
        raise ValueError("Header fields must have nonempty string paths.")
    if body is not None and not isinstance(body, str):
        raise ValueError("Body must be a string.")
    schema = getattr(model, 'candidate_schema', None)
    if schema is not None:
        fields = {field: schema.role_form.encode(field, value) if field in {'role', 'form'} else value
                  for field, value in fields.items()}
    if raw is None:
        metadata: dict[str, Any] = {"identity": {}}
        newline = "\n"
        original_body = ""
        prefix = None
    else:
        metadata, prefix, original_body, newline = _source_parts(raw)
    if fields or raw is None:
        _apply_fields(metadata, fields)
        if raw is None:
            if not metadata['identity']:
                del metadata['identity']
            metadata = {key: metadata[key] for key in GROUP_ORDER if key in metadata} | {
                key: value for key, value in metadata.items() if key not in GROUP_ORDER
            }
        carrier_read_view(metadata)
        try:
            header = yaml.safe_dump(metadata, allow_unicode=True, sort_keys=False, default_flow_style=False)
        except yaml.YAMLError as error:
            raise ValueError("Header values cannot be serialized safely.") from error
        prefix = "---" + newline + header.replace("\n", newline) + "---" + newline
    assert prefix is not None
    result = (prefix + (original_body if body is None else body)).encode("utf-8")
    parse_carrier(result, Path("<carrier>"))
    return result
