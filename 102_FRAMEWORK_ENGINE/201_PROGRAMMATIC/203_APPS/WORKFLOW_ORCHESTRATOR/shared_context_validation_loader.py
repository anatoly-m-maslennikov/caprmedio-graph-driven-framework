"""Reload the explicitly frozen Method selection from current Project sources."""

from __future__ import annotations

from collections.abc import Iterable, Mapping
from pathlib import Path
import sys
from typing import Any

from shared_context_validation_rmed import (
    SourceRow,
    load_current_source_row,
)
from shared_context_validation_sources import (
    ProjectSourceScope,
    SharedContextPacketError,
    project_source_scope,
)
from selected_integrated_frontier_records import MAX_RECORD_BYTES


PARSER = (
    Path(__file__).resolve().parents[2] / "201_TOOLS" / "VALIDATE_ATOMS" / "validate_atoms_workers"
)
if str(PARSER) not in sys.path:
    sys.path.insert(0, str(PARSER))

from parsing import CarrierError, parse_carrier  # type: ignore[import-not-found]  # noqa: E402


class FrozenMethodLoaderError(ValueError):
    """A frozen Method selection is incomplete, stale, or structurally invalid."""

    def __init__(self, code: str, message: str, *, needed_ids: Iterable[str] = ()) -> None:
        super().__init__(message)
        self.code = code
        self.needed_ids = tuple(sorted(set(needed_ids)))

    def warning(self) -> dict[str, object]:
        """Return the bounded diagnostic shape used by Workflow callers."""
        result: dict[str, object] = {"code": self.code, "message": str(self)}
        if self.needed_ids:
            result["needed_ids"] = list(self.needed_ids)
        return result


def _frozen_rows(frozen: Mapping[str, Any]) -> list[object]:
    request = frozen.get("request")
    if not isinstance(request, Mapping) or request.get("operation") != "enqueue_selected":
        raise FrozenMethodLoaderError(
            "frozen_request_invalid", "frozen selected enqueue request is required"
        )
    execution = request.get("execution")
    parameters = execution.get("parameters") if isinstance(execution, Mapping) else None
    base_packet = parameters.get("base_packet") if isinstance(parameters, Mapping) else None
    rows = base_packet.get("methods") if isinstance(base_packet, Mapping) else None
    if not isinstance(rows, list) or not rows:
        raise FrozenMethodLoaderError(
            "methods_missing", "frozen request does not declare direct Methods"
        )
    return rows


def _row_id(row: object) -> str | None:
    return (
        row.get("atom_id")
        if isinstance(row, Mapping) and isinstance(row.get("atom_id"), str)
        else None
    )


def _frozen_parent_ids(rows: Iterable[object]) -> set[str]:
    result: set[str] = set()
    for row in rows:
        if not isinstance(row, Mapping) or not isinstance(row.get("content"), str):
            continue
        if len(row["content"]) > MAX_RECORD_BYTES:
            continue
        try:
            metadata = parse_carrier(
                row["content"].encode("utf-8"), Path(str(row.get("path", "<frozen>")))
            ).metadata
        except CarrierError, UnicodeError:
            continue
        relations = metadata.get("relations")
        if not isinstance(relations, Mapping):
            continue
        parents = relations.get("child_of")
        if isinstance(parents, list):
            result.update(parent for parent in parents if isinstance(parent, str))
    return result


def _load_row(
    root: Path,
    scope: ProjectSourceScope,
    row: object,
    parent_ids: set[str],
) -> SourceRow:
    atom_id = _row_id(row)
    try:
        return load_current_source_row(root, scope, row, "M", require_content=True)
    except SharedContextPacketError as error:
        message = str(error)
        if atom_id in parent_ids:
            code = "unresolved_parent"
        elif "stale" in message:
            code = "stale_source"
        else:
            code = "unresolved_method"
        raise FrozenMethodLoaderError(code, message) from error


def _canonical(row: SourceRow) -> dict[str, Any]:
    return {
        "atom_id": row.atom_id,
        "version": row.version,
        "path": row.path,
        "sha256": row.sha256,
        "content": row.content,
    }


def _method_parents(
    row: SourceRow,
    scope: ProjectSourceScope,
) -> tuple[str, ...]:
    try:
        metadata = parse_carrier(row.content.encode("utf-8"), Path(row.path)).metadata
    except (CarrierError, UnicodeError) as error:
        raise FrozenMethodLoaderError(
            "structural_invalid", f"Method {row.atom_id} frontmatter is invalid"
        ) from error
    if (
        metadata.get("atom_id") != row.atom_id
        or metadata.get("version") != row.version
        or metadata.get("content_role") != "Method"
        or metadata.get("status") != "Active"
    ):
        raise FrozenMethodLoaderError(
            "structural_invalid", f"Method {row.atom_id} identity is invalid"
        )
    if "type" in metadata and (
        not isinstance(metadata["type"], str) or not metadata["type"].strip()
    ):
        raise FrozenMethodLoaderError("structural_invalid", f"Method {row.atom_id} type is invalid")
    relations = metadata.get("relations", {})
    if not isinstance(relations, Mapping):
        raise FrozenMethodLoaderError(
            "structural_invalid", f"Method {row.atom_id} relations are invalid"
        )
    if "parent_of" in relations:
        raise FrozenMethodLoaderError(
            "unsupported_condition",
            f"Method {row.atom_id} uses unsupported authored parent_of",
        )
    parents = relations.get("child_of", [])
    if not isinstance(parents, list):
        raise FrozenMethodLoaderError(
            "structural_invalid", f"Method {row.atom_id} child_of is invalid"
        )
    if any(
        not isinstance(parent, str)
        or not parent.startswith(f"{scope.prefix}-M-")
        or parent == row.atom_id
        for parent in parents
    ) or len(set(parents)) != len(parents):
        raise FrozenMethodLoaderError(
            "structural_invalid", f"Method {row.atom_id} child_of is invalid"
        )
    return tuple(parents)


def load_frozen_methods(root: Path, frozen: Mapping[str, Any]) -> tuple[dict[str, Any], ...]:
    """Reload only the frozen request's direct Methods and verify parent closure."""
    rows = _frozen_rows(frozen)
    atom_ids = [_row_id(row) for row in rows]
    if any(atom_id is None for atom_id in atom_ids):
        raise FrozenMethodLoaderError("method_authority", "frozen Method row is invalid")
    if len(set(atom_ids)) != len(atom_ids):
        raise FrozenMethodLoaderError("duplicate_methods", "frozen Method rows are duplicated")
    scope = project_source_scope(root)
    parent_ids = _frozen_parent_ids(rows)
    current = tuple(_load_row(root, scope, row, parent_ids) for row in rows)
    parents = {row.atom_id: _method_parents(row, scope) for row in current}
    selected = set(parents)
    missing = {parent for values in parents.values() for parent in values if parent not in selected}
    if missing:
        raise FrozenMethodLoaderError(
            "missing_parent",
            "frozen Method selection omits declared governing parents",
            needed_ids=missing,
        )
    return tuple(
        _canonical(row)
        for row in sorted(current, key=lambda item: (item.atom_id, item.version, item.path))
    )
