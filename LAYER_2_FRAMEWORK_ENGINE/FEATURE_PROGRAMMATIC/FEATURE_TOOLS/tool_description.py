"""Uniform, transport-neutral Tool self-description primitives.

Providers retain ownership of their canonical models and adapters.  This file
only makes the governed descriptor shape mechanical and keeps admission checks
aligned with the catalog binding that the MCP registry has already verified.
"""
from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import Any


def _identifier(value: object, field: str) -> str:
    if not isinstance(value, str) or not value:
        raise ValueError(f"{field} must be a non-empty string")
    return value


def _action_ids(value: Sequence[str]) -> list[str]:
    action_ids = list(value)
    if (
        not action_ids
        or not all(isinstance(action_id, str) and action_id for action_id in action_ids)
        or len(action_ids) != len(set(action_ids))
    ):
        raise ValueError("action_ids must be unique non-empty strings")
    return action_ids


def make_tool_description(
    *,
    entrypoint: str,
    name: str,
    delivery_atom_id: str,
    action_ids: Sequence[str],
    input_symbol: str,
    output_symbol: str,
    title: str,
    description: str,
    purpose: str,
    read_only: bool,
    destructive: bool = False,
    idempotent: bool = False,
    open_world: bool = False,
    tool_version: int = 1,
    refresh_after_success: bool = False,
) -> dict[str, Any]:
    """Construct the exact D621 Tool descriptor from canonical symbols.

    The descriptor intentionally carries no JSON Schema: callers derive that
    solely from the input/output model symbols at transport registration.
    """

    entrypoint = _identifier(entrypoint, "entrypoint")
    name = _identifier(name, "name")
    delivery_atom_id = _identifier(delivery_atom_id, "delivery_atom_id")
    input_symbol = _identifier(input_symbol, "input_symbol")
    output_symbol = _identifier(output_symbol, "output_symbol")
    title = _identifier(title, "title")
    description = _identifier(description, "description")
    purpose = _identifier(purpose, "purpose")
    if type(tool_version) is not int or tool_version < 1:
        raise ValueError("tool_version must be a positive integer")
    if not all(type(value) is bool for value in (
        read_only, destructive, idempotent, open_world, refresh_after_success,
    )):
        raise ValueError("effect and refresh hints must be booleans")
    action_ids = _action_ids(action_ids)
    return {
        "schema_version": 1,
        "identity": {
            "name": name,
            "tool_version": tool_version,
            "title": title,
            "description": description,
            "purpose": purpose,
        },
        "binding": {
            "delivery_atom_id": delivery_atom_id,
            "action_ids": action_ids,
            "implementation_entrypoint": entrypoint,
        },
        "models": {
            "input": {"module": entrypoint, "symbol": input_symbol},
            "output": {"module": entrypoint, "symbol": output_symbol},
        },
        "callable": {"module": entrypoint, "symbol": "create_adapter"},
        "effect_hints": {
            "read_only_hint": read_only,
            "destructive_hint": destructive,
            "idempotent_hint": idempotent,
            "open_world_hint": open_world,
        },
        "permissions": {
            "execution": "operator_authorized",
            "enforcement": "canonical_action_boundary",
            "metadata_grants_permission": False,
        },
        "source_pins": {
            "delivery_atom_id": delivery_atom_id,
            "action_ids": action_ids,
        },
        "admission": {
            "module": entrypoint,
            "symbol": "binding_is_admitted",
            "refresh_after_success": refresh_after_success,
        },
        "diagnostics": {"discovery_is_effect_free": True},
        "failure_contract": {"invokes_on_discovery": False},
    }


def binding_matches(
    binding: Mapping[str, object] | None,
    *,
    entrypoint: str,
    name: str,
    delivery_atom_id: str,
    action_ids: Sequence[str],
) -> bool:
    """Whether one already-verified catalog binding is this Tool's binding."""

    if not isinstance(binding, Mapping):
        return False
    try:
        return (
            binding.get("entrypoint") == _identifier(entrypoint, "entrypoint")
            and binding.get("name") == _identifier(name, "name")
            and binding.get("source_atom") == _identifier(delivery_atom_id, "delivery_atom_id")
            and binding.get("action_ids") == _action_ids(action_ids)
        )
    except ValueError:
        return False


__all__ = ["binding_matches", "make_tool_description"]
