"""Private, effect-free TOML CST materialization; no source or permission choices."""

from __future__ import annotations

import copy
from collections.abc import Mapping

from connector_toml_parse import (
    TomlFailure, _selected, _validate_edit, _value, apply_edits, equal_values,
    parse_source,
)


def _parent(document, path):
    parent = document
    for name in path[:-1]:
        parent = parent[name]
    return parent


def _item(parent, key):
    # Container.item retains Boolean nodes rather than returning native bools.
    return parent.item(key)


def _value_span(document, path, text, tomlkit):
    """Use the selected CST node, not a textual key search, to locate its bytes."""
    marker = "__caprmedio_selected_toml_occurrence__"
    while marker in text:
        marker += "_"
    probe = copy.deepcopy(document)
    parent = _parent(probe, path)
    parent[path[-1]] = tomlkit.string(marker)
    token = tomlkit.string(marker).as_string()
    rendered = probe.as_string()
    if rendered.count(token) != 1:
        raise TomlFailure("schema_invalid", "Selected CST occurrence is ambiguous.", "delta")
    prefix, suffix = rendered.split(token)
    original = _item(_parent(document, path), path[-1]).as_string()
    if prefix + original + suffix != text:
        raise TomlFailure("schema_invalid", "Selected layout cannot be changed losslessly.", "delta")
    return prefix, suffix


def _only_deletion(before, after, selected_start, selected_end):
    start = 0
    while start < len(after) and before[start] == after[start]:
        start += 1
    removed = len(before) - len(after)
    return (removed > 0 and before[:start] + before[start + removed:] == after
            and start <= selected_start and selected_end <= start + removed)


def _edit_cst(document, native, edit, keys, tomlkit):
    proposed, changes = apply_edits(native, {"edits": [edit]}, keys)
    if not changes:
        return native
    change = changes[0]
    path = keys[edit["field"]]
    parent, key = _parent(document, path), path[-1]
    before_text = document.as_string()
    present = change["before_present"]
    span = _value_span(document, path, before_text, tomlkit) if present else None
    action, mode = edit["action"], edit["mode"]
    if mode == "item":
        if not present:
            parent[key] = tomlkit.array()
        array = _item(parent, key)
        from tomlkit.items import Array
        if not isinstance(array, Array):
            raise TomlFailure("schema_invalid", "Selected collection layout is unsupported.", "delta")
        retained = []
        retained_indents = []
        index = None if action == "add" else _selected(change["before"], edit["current"])
        last_group = array._value[array._index_map[len(array) - 1]] if len(array) else None
        trailing_comma = last_group.comma.as_string() if last_group and last_group.comma else ""
        for position in range(len(array)):
            if position != index:
                retained.append(array.item(position).as_string())
                group = array._value[array._index_map[position]]
                retained_indents.append((position, copy.deepcopy(group.indent)))
                if group.comment is not None:
                    retained.append(group.comment.as_string())
        if action == "add":
            array.append(edit["value"])
        elif action == "replace":
            array[index] = edit["value"]
        else:
            del array[index]
        for position, indent in retained_indents:
            after_position = position - 1 if action == "remove" and position > index else position
            array._value[array._index_map[after_position]].indent = indent
        if action == "remove" and index < len(change["before"]) - 1 and trailing_comma:
            last = array._value[array._index_map[len(array) - 1]]
            if last.comma is None or last.comma.as_string() != trailing_comma:
                raise TomlFailure("schema_invalid", "Removal changed an unrelated trailing delimiter.", "delta")
        # Reject any dependency behavior that rewrites another entry's lexeme.
        remaining = array.as_string()
        offset = 0
        for token in retained:
            found = remaining.find(token, offset)
            if found < 0:
                raise TomlFailure("schema_invalid", "Collection edit changed an unrelated entry.", "delta")
            offset = found + len(token)
    elif not change["after_present"]:
        del parent[key]
    else:
        parent[key] = tomlkit.item(change["after"])
    if not present and "\r\n" in before_text:
        # Only newly created entry trivia is adapted; existing bytes are checked below.
        _item(parent, key).trivia.trail = "\r\n"
    after_text = document.as_string()
    if present and change["after_present"]:
        prefix, suffix = span
        selected = _item(parent, key).as_string()
        if after_text != prefix + selected + suffix:
            raise TomlFailure("schema_invalid", "Edit changed bytes outside its occurrence.", "delta")
    elif present:
        prefix, suffix = span
        if not _only_deletion(before_text, after_text, len(prefix), len(before_text) - len(suffix)):
            raise TomlFailure("schema_invalid", "Removal changed unrelated bytes.", "delta")
    else:
        probe = copy.deepcopy(document)
        del _parent(probe, path)[key]
        if probe.as_string() != before_text:
            raise TomlFailure("schema_invalid", "Addition changed unrelated bytes.", "delta")
    # New CST trivia must not silently introduce another line-ending convention.
    if "\r\n" in before_text and "\n" not in before_text.replace("\r\n", ""):
        if "\n" in after_text.replace("\r\n", ""):
            raise TomlFailure("schema_invalid", "Changed layout cannot retain CRLF exactly.", "delta")
    return proposed


def materialize_toml(source: bytes, delta: object,
                     keys: Mapping[str, tuple[str, ...]]) -> tuple[bytes, dict, list]:
    """Return proposed bytes, complete native values and the effective semantic diff.

    Bindings and source admission belong to the receiver. This function never
    selects, reads or publishes a carrier and does not encode public values.
    """
    try:
        if type(source) is not bytes:
            raise TomlFailure("input_invalid", "Source must be supplied bytes.", "target")
        if not isinstance(keys, Mapping) or any(
            type(name) is not str or not name or type(path) is not tuple or not path
            or any(type(part) is not str or not part for part in path)
            for name, path in keys.items()
        ):
            raise TomlFailure("schema_invalid", "Private key bindings are invalid.", "context")
        paths = list(keys.values())
        if len(set(paths)) != len(paths):
            raise TomlFailure("schema_invalid", "Private key bindings select duplicate occurrences.", "context")
        text, native = parse_source(source)
        proposed, changes = apply_edits(native, delta, keys)
        for edit in delta["edits"]:
            _validate_edit(edit, keys)
            for name in ("value", "current"):
                if name in edit:
                    _value(edit[name])
        _value(proposed)
        if not changes:
            return source, proposed, []
        import tomlkit

        document = tomlkit.parse(text)
        if tomlkit.dumps(document).encode("utf-8") != source:
            raise TomlFailure("schema_invalid", "CST baseline round-trip is not byte-exact.", "target")
        current = native
        for edit in delta["edits"]:
            current = _edit_cst(document, current, edit, keys, tomlkit)
        payload = tomlkit.dumps(document).encode("utf-8")
        if payload != document.as_string().encode("utf-8"):
            raise TomlFailure("schema_invalid", "CST serializer changed the proposed bytes.", "delta")
        if not equal_values(parse_source(payload)[1], proposed):
            raise TomlFailure("schema_invalid", "Complete proposed TOML values or types differ.", "delta")
        return payload, proposed, changes
    except TomlFailure:
        raise
    except Exception as error:
        raise TomlFailure("schema_invalid", f"TOML materialization refused: {error}", "delta") from error
