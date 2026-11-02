"""Pure TOML parsing, semantic edits and rendering; no source selection or effects."""

from __future__ import annotations

import copy
import datetime
import json
import math
import tomllib
from collections.abc import Mapping

from connector_contract import _json_value


class TomlFailure(ValueError):
    def __init__(self, code: str, message: str, field: str | None = None):
        super().__init__(message)
        self.code = code
        self.field = field


def parse_source(payload: bytes) -> tuple[str, dict]:
    text = payload.decode("utf-8")
    return text, tomllib.loads(text)


def equal_values(left: object, right: object) -> bool:
    """TOML equality retains types and handles TOML's NaN values."""
    if type(left) is not type(right):
        return False
    if isinstance(left, dict):
        return left.keys() == right.keys() and all(equal_values(v, right[k]) for k, v in left.items())
    if isinstance(left, list):
        return len(left) == len(right) and all(equal_values(a, b) for a, b in zip(left, right))
    if isinstance(left, float) and math.isnan(left):
        return math.isnan(right) and math.copysign(1, left) == math.copysign(1, right)
    return left == right


def represent_document(document: dict) -> dict:
    """Reject native TOML values whose public JSON representation is unresolved."""
    if not _json_value(document):
        raise ValueError("The TOML value types have no admitted lossless JSON representation.")
    return document


def _value(value: object) -> str:
    if type(value) is str:
        return json.dumps(value, ensure_ascii=False)
    if type(value) is bool:
        return "true" if value else "false"
    if type(value) is int:
        if not -(2**63) <= value < 2**63:
            raise ValueError("TOML integer is outside its supported range.")
        return str(value)
    if type(value) is float:
        if math.isnan(value):
            return "-nan" if math.copysign(1, value) < 0 else "nan"
        return repr(value)
    if type(value) in (datetime.datetime, datetime.date, datetime.time):
        return value.isoformat()
    if type(value) is list:
        return "[" + ", ".join(_value(item) for item in value) + "]"
    if type(value) is dict and all(type(key) is str for key in value):
        return "{" + ", ".join(f"{_value(key)} = {_value(item)}" for key, item in value.items()) + "}"
    raise ValueError("Value is not representable in TOML.")


def render_document(document: dict) -> bytes:
    rendered = "".join(f"{_value(key)} = {_value(value)}\n" for key, value in document.items()).encode("utf-8")
    if not equal_values(parse_source(rendered)[1], document):
        raise ValueError("TOML serialization lost a value or type.")
    return rendered


def _selected(items: list, value: object) -> int:
    matches = [index for index, item in enumerate(items) if equal_values(item, value)]
    if not matches:
        raise TomlFailure("target_not_found", "Selected current value is absent.", "delta")
    if len(matches) != 1:
        raise TomlFailure("target_ambiguous", "Selected current value is not unique.", "delta")
    return matches[0]


def _list_edit(items: list, edit: dict) -> list:
    action, mode = edit["action"], edit["mode"]
    if mode == "set" and action == "replace":
        return copy.deepcopy(edit["value"])
    selected = edit["value"] if action == "add" or mode == "set" else edit["current"]
    values = selected if mode == "set" else [selected]
    result = copy.deepcopy(items)
    for value in values:
        if action == "add":
            matches = [item for item in result if equal_values(item, value)]
            if len(matches) > 1:
                raise TomlFailure("target_ambiguous", "Added current value is not unique.", "delta")
            if not matches:
                result.append(copy.deepcopy(value))
        else:
            index = _selected(result, value)
            if action == "remove":
                result.pop(index)
            else:
                result[index] = copy.deepcopy(edit["value"])
    return result


def _validate_edit(edit: object, keys: Mapping[str, tuple[str, ...]]) -> None:
    if type(edit) is not dict:
        raise TomlFailure("input_invalid", "An edit must be an object.", "delta")
    action, mode, field = edit.get("action"), edit.get("mode"), edit.get("field")
    if action not in ("add", "replace", "remove") or mode not in ("value", "item", "set"):
        raise TomlFailure("input_invalid", "Unknown edit action or mode.", "delta")
    if not isinstance(field, str) or field not in keys:
        raise TomlFailure("schema_invalid", "The logical field is not admitted for editing.", "delta")
    required = {"action", "mode", "field"}
    if action != "remove" or mode == "set":
        required.add("value")
    if mode == "item" and action != "add":
        required.add("current")
    if edit.keys() != required or (mode == "set" and type(edit.get("value")) is not list):
        raise TomlFailure("input_invalid", "The edit has an invalid closed shape.", "delta")


def apply_edits(document: dict, delta: object, keys: Mapping[str, tuple[str, ...]]) -> tuple[dict, list]:
    """Keys are private receiver bindings; logical requests never supply TOML paths."""
    if type(delta) is not dict or delta.keys() != {"edits"} or type(delta["edits"]) is not list:
        raise TomlFailure("input_invalid", "Delta requires only an explicit edits array.", "delta")
    result, changed = copy.deepcopy(document), []
    for edit in delta["edits"]:
        _validate_edit(edit, keys)
        path = keys[edit["field"]]
        if not path or any(type(key) is not str or not key for key in path):
            raise TomlFailure("schema_invalid", "The logical field binding is invalid.", "context")
        container = result
        for key in path[:-1]:
            if type(container.get(key)) is not dict:
                raise TomlFailure("target_not_found", "The bound field parent is absent.", "delta")
            container = container[key]
        key, action, mode = path[-1], edit["action"], edit["mode"]
        present, old = key in container, copy.deepcopy(container.get(key))
        if mode in ("item", "set"):
            if not present and action == "add":
                container[key] = []
            if type(container.get(key)) is not list:
                raise TomlFailure("schema_invalid", "List edit requires a list field.", "delta")
            container[key] = _list_edit(container[key], edit)
        elif action == "remove":
            container.pop(key, None)
        elif action == "replace" and not present:
            raise TomlFailure("target_not_found", "The replaced field is absent.", "delta")
        elif action == "add" and present and not equal_values(old, edit["value"]):
            raise TomlFailure("input_invalid", "Add cannot replace an existing field.", "delta")
        else:
            container[key] = copy.deepcopy(edit["value"])
        if present != (key in container) or not equal_values(old, container.get(key)):
            changed.append({"field": edit["field"], "action": action, "mode": mode,
                            "before_present": present, "after_present": key in container,
                            "before": old, "after": copy.deepcopy(container.get(key))})
    effective = {}
    for change in changed:
        field = change["field"]
        if field in effective:
            effective[field]["after_present"] = change["after_present"]
            effective[field]["after"] = change["after"]
        else:
            effective[field] = change
    return result, [change for change in effective.values()
                    if change["before_present"] != change["after_present"]
                    or not equal_values(change["before"], change["after"])]
