"""Closed parent-gateway activation markers returned by admitted tools."""
from __future__ import annotations

import re
from collections.abc import Mapping


_REQUEST_ID = re.compile(r"[A-Za-z0-9_-]{1,128}\Z")
_KINDS = frozenset(("metadata", "image_recreation"))


def completion_marker(value):
    """Return one declared completion marker, or ``None`` when absent.

    The marker is part of an admitted tool's structured output, never inferred
    from its name or normal business fields.  Invalid claimed markers fail the
    parent call rather than creating a best-effort activation.
    """
    if not isinstance(value, Mapping) or "mcp_activation" not in value:
        return None
    marker = value["mcp_activation"]
    if not isinstance(marker, Mapping) or set(marker) != {"schema_version", "kind", "request_id"}:
        raise ValueError("MCP activation marker is invalid")
    if marker.get("schema_version") != 1 or marker.get("kind") not in _KINDS:
        raise ValueError("MCP activation marker is unsupported")
    request_id = marker.get("request_id")
    if not isinstance(request_id, str) or _REQUEST_ID.fullmatch(request_id) is None:
        raise ValueError("MCP activation request_id is invalid")
    return dict(marker)


def activation_succeeded(value) -> bool:
    """Refuse post-command activation for a reported business failure."""
    if not isinstance(value, Mapping):
        return False
    return value.get("effect_outcome") == "completed" and value.get("recording_state") == "recorded"


def attach_receipt(response, value):
    """Attach activation evidence without changing the Tool business result."""
    meta = dict(response.meta or {})
    meta["caprmedio_mcp_activation"] = value
    response.meta = meta
    return response
