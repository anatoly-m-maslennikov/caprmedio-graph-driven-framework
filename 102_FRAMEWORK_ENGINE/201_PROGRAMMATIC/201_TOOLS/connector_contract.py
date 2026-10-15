"""Private, pure structural checks for CA-D-625's logical connector contract.

These helpers neither resolve bindings nor authorize or execute an operation.
Receiving adapters must validate their admitted identity/filter/delta/state schemas,
resolve permission/context references, check exact absence/currentness and preview
evidence before effects, and independently observe the declared postconditions.
Physical selectors and lifecycle decisions must be excluded by those bound schemas.
No existing connector or outer service envelope is changed by this module.
"""

from __future__ import annotations

import math
from collections.abc import Collection


OPERATIONS = frozenset({"query", "read", "create", "modify"})
REQUEST_FIELDS = frozenset({
    "operation", "target", "query", "delta", "expected_state", "authorization", "context",
})
RESULT_FIELDS = frozenset({"data", "current_state", "effects", "errors"})
ERROR_CODES = frozenset({
    "input_invalid", "unsupported_operation", "target_not_found", "target_ambiguous",
    "stale_state", "permission_denied", "schema_invalid", "backend_failure", "effect_uncertain",
})


def _json_value(value: object) -> bool:
    if value is None or type(value) in (str, bool, int):
        return True
    if type(value) is float:
        return math.isfinite(value)
    if type(value) is list:
        return all(_json_value(item) for item in value)
    if type(value) is dict:
        return all(type(key) is str and _json_value(item) for key, item in value.items())
    return False


def _error(code: str, message: str, field: str | None) -> dict:
    return {"code": code, "message": message, "field": field}


def _json_object(value: object) -> bool:
    try:
        return type(value) is dict and _json_value(value)
    except RecursionError:
        return False


def _reference(value: object) -> bool:
    return (isinstance(value, str) and bool(value.strip())) or (
        isinstance(value, dict) and bool(value)
    )


def validate_request(
    request: object, *, supported_operations: Collection[str], supported_kinds: Collection[str],
) -> list[dict]:
    """Return structural errors; an empty list is never binding or effect permission.

    Declarations come from the receiving adapter, not from the caller's request.
    Operation-specific schemas still govern the opaque content and references.
    """
    if not _json_object(request):
        return [_error("input_invalid", "Request must be a JSON object.", None)]
    if request.keys() != REQUEST_FIELDS:
        return [_error("input_invalid", "Request must contain exactly the seven logical fields.", None)]
    errors = []
    operation = request["operation"]
    if not isinstance(operation, str) or operation not in OPERATIONS:
        return [_error("unsupported_operation", "Unknown connector operation.", "operation")]
    if operation not in supported_operations:
        errors.append(_error("unsupported_operation", "Operation is not admitted by this connector.", "operation"))

    selector = "query" if operation == "query" else "target"
    other = "target" if operation == "query" else "query"
    value_field = "filters" if operation == "query" else "identity"
    value = request[selector]
    if request[other] is not None:
        errors.append(_error("input_invalid", f"{other} must be null for {operation}.", other))
    if not isinstance(value, dict) or value.keys() != {"kind", value_field}:
        errors.append(_error("input_invalid", f"{selector} requires exactly kind and {value_field}.", selector))
    else:
        if not isinstance(value["kind"], str) or value["kind"] not in supported_kinds:
            errors.append(_error("input_invalid", "Logical kind is not admitted by this connector.", selector))
        if value[value_field] is None:
            errors.append(_error("input_invalid", f"Explicit {value_field} is required.", selector))

    if operation in {"query", "read"} and request["delta"] is not None:
        errors.append(_error("input_invalid", "Query and Read require null delta.", "delta"))
    if operation in {"create", "modify"}:
        if request["delta"] is None:
            errors.append(_error("input_invalid", "Create and Modify require explicit delta.", "delta"))
        if request["expected_state"] is None:
            errors.append(_error("input_invalid", "Create requires expected absence; Modify requires exact current state.", "expected_state"))
    for field in ("authorization", "context"):
        if not _reference(request[field]):
            errors.append(_error("input_invalid", "A nonempty bound reference is required, not an approval flag.", field))
    return errors


def _result_errors(value: object) -> list[dict]:
    if not isinstance(value, list):
        return [_error("input_invalid", "Result errors must be an array.", None)]
    errors = []
    for item in value:
        if not isinstance(item, dict) or item.keys() != {"code", "message", "field"}:
            errors.append(_error("input_invalid", "An error requires exactly code, message and field.", None))
        elif (
            not isinstance(item["code"], str) or item["code"] not in ERROR_CODES
            or not isinstance(item["message"], str) or not item["message"].strip()
            or not (item["field"] is None or (
                isinstance(item["field"], str) and item["field"] in REQUEST_FIELDS
            ))
        ):
            errors.append(_error("input_invalid", "Invalid structured error code, message or request field.", None))
        else:
            errors.append(dict(item))
    return errors


def _effect_errors(effects: object, request: dict, errors: list[dict]) -> list[dict]:
    violations = []
    if not isinstance(effects, list):
        return [_error("input_invalid", "Result effects must be an array.", None)]
    if effects and request["operation"] in {"query", "read"}:
        violations.append(_error("input_invalid", "Query and Read cannot report mutation effects.", None))
    for effect in effects:
        if not isinstance(effect, dict) or effect.keys() != {"operation", "target", "state", "evidence"}:
            violations.append(_error("input_invalid", "An effect requires exactly operation, target, state and evidence.", None))
            continue
        if effect["operation"] != request["operation"] or effect["target"] != request["target"]:
            violations.append(_error("input_invalid", "Effect must be attributable to the requested operation and target.", None))
        if effect["state"] not in ("known", "unknown") or effect["evidence"] is None:
            violations.append(_error("input_invalid", "Effect requires known/unknown state and non-null evidence.", None))
        if effect["state"] == "unknown" and not any(item["code"] == "effect_uncertain" for item in errors):
            violations.append(_error("effect_uncertain", "An unknown effect requires an effect_uncertain error.", None))
    return violations


def validate_result(
    result: object, *, request: dict, postconditions_verified: bool = False,
    unchanged_verified: bool = False,
) -> list[dict]:
    """Return operation errors plus contract violations without changing any evidence.

    `request` must have passed request AND receiving-adapter binding/schema checks.
    Verification arguments are private attestations from the adapter's independent
    observations, never logical request fields or permission. The helper cannot
    establish their truth. A successful write with no effects is a no-op and also
    requires observed unchanged state. Nonempty returned errors always mean failure.
    """
    if not _json_object(result):
        return [_error("input_invalid", "Result must be a JSON object.", None)]
    if result.keys() != RESULT_FIELDS:
        return [_error("input_invalid", "Result must contain exactly the four logical fields.", None)]
    errors = _result_errors(result["errors"])
    errors.extend(_effect_errors(result["effects"], request, errors))
    if not errors:
        if postconditions_verified is not True:
            errors.append(_error("backend_failure", "Declared postconditions have not been independently verified.", None))
        if request["operation"] in {"create", "modify"} and not result["effects"]:
            if unchanged_verified is not True:
                errors.append(_error("backend_failure", "No-op requires verification that requested state is satisfied and unchanged.", None))
    return errors
