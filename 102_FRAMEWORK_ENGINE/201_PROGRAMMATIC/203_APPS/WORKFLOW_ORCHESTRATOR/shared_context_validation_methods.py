"""Independent Method-inventory validation for the shared Workflow packet."""

from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path
from typing import Any

from shared_context_validation_rmed import SourceRow, _rows
from shared_context_validation_sources import (
    ProjectSourceScope,
    SharedContextPacketError,
)


def _trusted_methods(
    root: Path,
    scope: ProjectSourceScope,
    value: object,
    *,
    require_content: bool,
) -> list[SourceRow]:
    sources = value.get("sources") if isinstance(value, Mapping) else value
    if not isinstance(sources, (list, tuple)):
        raise SharedContextPacketError(
            "method_authority", "trusted Method inventory is unavailable"
        )
    normalized_sources: list[object] = [
        {
            "atom_id": row.atom_id,
            "version": row.version,
            "path": row.path,
            "sha256": row.sha256,
            "content": row.content,
        }
        if isinstance(row, SourceRow)
        else row
        for row in sources
    ]
    content_flags = [isinstance(row, Mapping) and "content" in row for row in normalized_sources]
    if (require_content and not all(content_flags)) or (any(content_flags) and not all(content_flags)):
        raise SharedContextPacketError(
            "method_authority", "trusted Method inventory requires full SourceRows"
        )
    try:
        return _rows(
            root,
            scope,
            normalized_sources,
            "M",
            require_content=require_content or all(content_flags),
        )
    except SharedContextPacketError as error:
        if error.code == "rmed":
            raise SharedContextPacketError("method_authority", str(error)) from error
        raise


def _projection_methods(
    root: Path, scope: ProjectSourceScope, projection: object
) -> tuple[list[SourceRow], str]:
    if not isinstance(projection, Mapping) or set(projection) != {"content", "sources"}:
        raise SharedContextPacketError("methods", "full Method projection is missing")
    methods = _rows(root, scope, projection.get("sources"), "M", require_content=False)
    content = projection.get("content")
    if not isinstance(content, str):
        raise SharedContextPacketError("methods", "full Method projection content is stale")
    return methods, content


def _same_method_inventory(left: list[SourceRow], right: list[SourceRow]) -> bool:
    return {row.pin for row in left} == {row.pin for row in right}


def validate_method_inputs(
    root: Path,
    scope: ProjectSourceScope,
    packet: Mapping[str, Any],
    trusted_method_projection: object | None,
    trusted_methods: object | None,
) -> set[str]:
    """Validate direct or legacy Method inputs against independent sources."""
    direct_value = packet.get("methods")
    projection = packet.get("method_projection")
    if direct_value is None and projection is None:
        raise SharedContextPacketError("methods", "direct Methods or legacy projection is missing")
    trusted_value = trusted_methods if trusted_methods is not None else trusted_method_projection
    if direct_value is not None and trusted_methods is None:
        raise SharedContextPacketError(
            "method_authority", "independent trusted Method inventory is unavailable"
        )
    trusted = _trusted_methods(
        root,
        scope,
        trusted_value,
        require_content=direct_value is not None,
    )
    direct = _rows(root, scope, direct_value, "M") if direct_value is not None else []
    if direct and not _same_method_inventory(direct, trusted):
        raise SharedContextPacketError(
            "method_authority", "direct Methods differ from trusted inventory"
        )
    identifiers = {row.atom_id for row in direct}
    if projection is not None:
        projected, content = _projection_methods(root, scope, projection)
        if not _same_method_inventory(projected, trusted):
            raise SharedContextPacketError(
                "method_authority", "Method projection differs from trusted inventory"
            )
        expected = "\n\n".join(
            row.content for row in sorted(trusted, key=lambda row: (row.atom_id, row.version))
        )
        if content != expected:
            raise SharedContextPacketError("methods", "full Method projection content is stale")
        identifiers.update(row.atom_id for row in projected)
    return identifiers
