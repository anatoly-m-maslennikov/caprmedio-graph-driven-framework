"""Pure mechanics for explicitly schema-bound Atom Property edits.

The receiving Workflow supplies the field mapping, list declarations and complete
validator. These are private bindings, never permission or request fields.
"""

from __future__ import annotations

from collections.abc import Callable, Mapping, Set
from copy import deepcopy

from connector_contract import _json_object


class PropertyEditError(ValueError):
    def __init__(self, code: str, message: str):
        self.code = code
        super().__init__(message)


def _same(left: object, right: object) -> bool:
    if type(left) is not type(right):
        return False
    if isinstance(left, list):
        return len(left) == len(right) and all(_same(a, b) for a, b in zip(left, right))
    if isinstance(left, dict):
        return left.keys() == right.keys() and all(_same(left[key], right[key]) for key in left)
    return left == right


def _parent(document: dict, path: tuple[str, ...]) -> tuple[dict, str]:
    if not path or any(type(part) is not str or not part for part in path):
        raise PropertyEditError("schema_invalid", "Property has no unambiguous bound field path.")
    current = document
    for part in path[:-1]:
        if part not in current or type(current[part]) is not dict:
            raise PropertyEditError("schema_invalid", "Property parent is missing or not a mapping.")
        current = current[part]
    return current, path[-1]


def _entry_index(values: list, selected: object) -> int:
    matches = [index for index, value in enumerate(values) if _same(value, selected)]
    if len(matches) != 1:
        code = "target_ambiguous" if matches else "stale_state"
        raise PropertyEditError(code, "Current value must identify exactly one list entry.")
    return matches[0]


def _edit(parent: dict, key: str, edit: dict, is_list: bool, is_entry: bool) -> None:
    operation = edit["operation"]
    present = key in parent
    current = parent.get(key)
    if operation == "replace_set":
        if not is_list or type(edit["old"]) is not list or type(edit["new"]) is not list:
            raise PropertyEditError("schema_invalid", "replace_set requires a bound list and complete lists.")
        if not present or not _same(current, edit["old"]):
            raise PropertyEditError("stale_state", "Complete current list differs from expected old collection.")
        parent[key] = deepcopy(edit["new"])
    elif is_entry:
        if not is_list:
            raise PropertyEditError("schema_invalid", "Entry edit requires a schema-bound list Property.")
        if not present or type(current) is not list:
            raise PropertyEditError("schema_invalid", "List entry edit requires an existing list Property.")
        if operation == "add":
            matches = [value for value in current if _same(value, edit["value"])]
            if len(matches) > 1:
                raise PropertyEditError("target_ambiguous", "Added value is already ambiguous.")
            if not matches:
                current.append(deepcopy(edit["value"]))
        else:
            index = _entry_index(current, edit["old"] if operation == "replace" else edit["value"])
            if operation == "replace":
                current[index] = deepcopy(edit["new"])
            else:
                del current[index]
    elif operation == "add":
        if present and not _same(current, edit["value"]):
            raise PropertyEditError("stale_state", "Property addition requires absence or an exact no-op.")
        parent[key] = deepcopy(edit["value"])
    else:
        if not present or not _same(current, edit["old"]):
            raise PropertyEditError("stale_state", "Property differs from its expected current value.")
        if operation == "replace":
            parent[key] = deepcopy(edit["new"])
        else:
            del parent[key]


def apply_property_edits(
    complete_atom: dict, edits: list, *, field_paths: Mapping[str, tuple[str, ...]],
    list_fields: Set[str], list_entry_edit: Callable[[dict], bool],
    validate_final: Callable[[dict], None],
) -> dict:
    """Return a validated copy; never read, write, choose schema or bump metadata.

    This private edit representation follows D623's explicit operations. Public
    request syntax and binding admission belong to the receiving adapter.
    Validation raises on an invalid complete result, including required fields,
    membership and uniqueness. Summary, Type and identity remain same-ID guards.
    """
    if not _json_object(complete_atom) or not _json_object({"edits": edits}) or type(edits) is not list:
        raise PropertyEditError("input_invalid", "Complete Atom and edits must contain JSON values.")
    proposed = deepcopy(complete_atom)
    for edit in edits:
        if type(edit) is not dict or type(edit.get("field")) is not str:
            raise PropertyEditError("input_invalid", "Each edit must name one explicit Property.")
        field = edit["field"]
        if field not in field_paths:
            raise PropertyEditError("schema_invalid", "Property is not declared by the bound schema.")
        operation = edit.get("operation")
        is_list = field in list_fields
        is_entry = list_entry_edit(deepcopy(edit))
        if type(is_entry) is not bool:
            raise PropertyEditError("schema_invalid", "Bound edit granularity must be Property or list entry.")
        shapes = {
            "add": {"field", "operation", "value"},
            "replace": {"field", "operation", "old", "new"},
            "remove": {"field", "operation", "value" if is_entry else "old"},
            "replace_set": {"field", "operation", "old", "new"},
        }
        if type(operation) is not str or operation not in shapes or edit.keys() != shapes[operation]:
            raise PropertyEditError("input_invalid", "Edit has unsupported operation or fields; indexes are not selectors.")
        parent, key = _parent(proposed, field_paths[field])
        original_present, original = key in parent, deepcopy(parent.get(key))
        _edit(parent, key, edit, is_list, is_entry)
        if key in parent and is_list and type(parent[key]) is not list:
            raise PropertyEditError("schema_invalid", "Bound list Property must contain a list.")
        if key.casefold() in {"summary", "type", "atom_id"} and (
            original_present != (key in parent) or not _same(original, parent.get(key))
        ):
            raise PropertyEditError("schema_invalid", "Summary, Type or identity change requires the replacement Workflow.")
        if field_paths[field][-2:] == ("subjects", "depends_on") and type(parent.get(key)) is list:
            values = parent[key]
            if any(_same(value, previous) for index, value in enumerate(values) for previous in values[:index]):
                raise PropertyEditError("schema_invalid", "Subject dependencies must be unique.")
    if validate_final(deepcopy(proposed)) is not None:
        raise PropertyEditError("schema_invalid", "Complete validator must raise on refusal or return None.")
    return proposed
