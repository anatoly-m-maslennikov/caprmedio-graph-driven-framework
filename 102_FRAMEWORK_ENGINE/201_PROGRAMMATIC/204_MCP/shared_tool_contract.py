"""Native Tool contract validation and the shared public schema adapter."""

from __future__ import annotations

from dataclasses import dataclass
import copy
import hashlib
import json

from jsonschema import Draft202012Validator, SchemaError
from mcp import types


_UNADAPTABLE_ROOT_KEYS = frozenset(
    {
        "$ref",
        "$dynamicRef",
        "allOf",
        "anyOf",
        "oneOf",
        "not",
        "if",
        "then",
        "else",
        "dependentRequired",
        "dependentSchemas",
        "enum",
        "const",
        "maxProperties",
        "patternProperties",
        "propertyNames",
        "unevaluatedProperties",
    }
)


@dataclass(frozen=True)
class ToolContract:
    tool: types.Tool
    digest: str


def contract_digest(tool: types.Tool) -> str:
    value = {"input_schema": tool.input_schema, "output_schema": tool.output_schema}
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def public_tool(tool: types.Tool) -> types.Tool:
    """Add only the explicit host selector to a native root-object schema."""
    schema = copy.deepcopy(tool.input_schema)
    if not isinstance(schema, dict):
        raise ValueError("Native Tool input schema is invalid")
    try:
        Draft202012Validator.check_schema(schema)
    except SchemaError as error:
        raise ValueError("Native Tool input schema is invalid") from error
    if _UNADAPTABLE_ROOT_KEYS.intersection(schema):
        raise ValueError("Native Tool input schema cannot safely add project_root at its root")
    if "project_root" in schema.get("properties", {}):
        raise ValueError("Native Tool cannot be given an unambiguous project_root")
    if schema.get("type") not in (None, "object"):
        raise ValueError("Native Tool input is not a root object")
    properties = dict(schema.get("properties", {}))
    properties["project_root"] = {"type": "string", "minLength": 1}
    required = list(schema.get("required", []))
    if "project_root" not in required:
        required.append("project_root")
    schema["type"], schema["properties"], schema["required"] = "object", properties, required
    try:
        Draft202012Validator.check_schema(schema)
    except SchemaError as error:
        raise ValueError("Public Tool input schema is invalid") from error
    return tool.model_copy(update={"input_schema": schema})


__all__ = ["ToolContract", "contract_digest", "public_tool"]
