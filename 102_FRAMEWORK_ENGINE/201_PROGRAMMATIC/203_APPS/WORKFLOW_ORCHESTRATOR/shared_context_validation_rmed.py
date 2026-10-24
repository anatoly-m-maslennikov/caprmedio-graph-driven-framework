"""Current R/M/E/D source and trusted Method-inventory validation."""

from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass
import hashlib
from pathlib import Path
import re
import sys
from typing import Any

from selected_evidence_io import bounded_bytes
from selected_execution_contracts import SelectedExecutionError
from selected_graph_sources import safe_definition_path
from selected_integrated_frontier_records import MAX_RECORD_BYTES
from shared_context_validation_sources import (
    ProjectSourceScope,
    SharedContextPacketError,
    project_source_scope,
)


TOOLS = Path(__file__).resolve().parents[2] / "201_TOOLS"
if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))

from atom_operations import ToolError, frontmatter_scalar, split_frontmatter  # noqa: E402


_DIGEST = re.compile(r"[0-9a-f]{64}")
_ARCHIVED = frozenset({"archive", "archived", "draft", "drafts"})
_ROLES = {"R": "Requirement", "M": "Method", "E": "Evaluation", "D": "Delivery"}


@dataclass(frozen=True)
class SourceRow:
    atom_id: str
    version: int
    path: str
    sha256: str
    content: str

    @property
    def pin(self) -> tuple[str, int, str, str]:
        return self.atom_id, self.version, self.path, self.sha256


def _source_row(
    root: Path,
    scope: ProjectSourceScope,
    row: object,
    prefix: str,
    *,
    require_content: bool,
) -> SourceRow:
    if not isinstance(row, Mapping):
        raise SharedContextPacketError("rmed", f"{prefix} source row is invalid")
    atom_id, version, path, digest, content = (
        row.get("atom_id"),
        row.get("version"),
        row.get("path"),
        row.get("sha256"),
        row.get("content"),
    )
    relative = Path(path) if isinstance(path, str) else None
    if (
        not isinstance(atom_id, str)
        or not atom_id.startswith(f"{scope.prefix}-{prefix}-")
        or isinstance(version, bool)
        or not isinstance(version, int)
        or version < 1
        or not isinstance(path, str)
        or relative is None
        or relative.is_absolute()
        or ".." in relative.parts
        or not relative.is_relative_to(Path(scope.root))
        or any(part.casefold() in _ARCHIVED for part in relative.parts)
        or not isinstance(digest, str)
        or _DIGEST.fullmatch(digest) is None
        or (require_content and not isinstance(content, str))
    ):
        raise SharedContextPacketError("rmed", f"{prefix} source row is incomplete")
    if require_content and isinstance(content, str) and len(content) > MAX_RECORD_BYTES:
        raise SharedContextPacketError("rmed", f"{prefix} source content is oversized")
    try:
        raw = bounded_bytes(safe_definition_path(root, path), MAX_RECORD_BYTES)
    except (OSError, SelectedExecutionError) as error:
        raise SharedContextPacketError("rmed", f"{prefix} source is unavailable") from error
    if hashlib.sha256(raw).hexdigest() != digest:
        raise SharedContextPacketError("rmed", f"{prefix} source content is stale")
    try:
        actual_content = raw.decode("utf-8")
        frontmatter, _ = split_frontmatter(actual_content)
        actual = {
            name: frontmatter_scalar(frontmatter, name)
            for name in ("atom_id", "version", "content_role", "status")
        }
    except (ToolError, UnicodeError, ValueError) as error:
        raise SharedContextPacketError("rmed", f"{prefix} source frontmatter is invalid") from error
    if require_content and content != actual_content:
        raise SharedContextPacketError("rmed", f"{prefix} source content is stale")
    if (
        actual["atom_id"] != atom_id
        or actual["version"] != str(version)
        or actual["content_role"] != _ROLES[prefix]
        or actual["status"] != "Active"
    ):
        raise SharedContextPacketError("rmed", f"{prefix} source identity is stale")
    return SourceRow(atom_id, version, path, digest, actual_content)


def load_current_source_row(
    root: Path,
    scope: ProjectSourceScope,
    row: object,
    prefix: str,
    *,
    require_content: bool = True,
) -> SourceRow:
    """Public current-authority wrapper for one independently pinned source row."""
    return _source_row(root, scope, row, prefix, require_content=require_content)


def _rows(
    root: Path,
    scope: ProjectSourceScope,
    value: object,
    prefix: str,
    *,
    require_content: bool = True,
) -> list[SourceRow]:
    if not isinstance(value, list) or not value:
        raise SharedContextPacketError("rmed", f"{prefix} sources are missing")
    rows = [_source_row(root, scope, row, prefix, require_content=require_content) for row in value]
    if len({row.atom_id for row in rows}) != len(rows):
        raise SharedContextPacketError("rmed", f"{prefix} sources are duplicated")
    return rows


def validate_rmed_inputs(
    root: Path,
    packet: Mapping[str, Any],
    trusted_method_projection: object | None = None,
    *,
    trusted_methods: object | None = None,
) -> set[str]:
    """Check R/M/E/D bytes against an independently trusted Method frontier."""
    scope = project_source_scope(root)
    identifiers: set[str] = set()
    for field, prefix in (("requirements", "R"), ("delivery", "D"), ("evaluations", "E")):
        identifiers.update(row.atom_id for row in _rows(root, scope, packet.get(field), prefix))
    from shared_context_validation_methods import validate_method_inputs

    identifiers.update(
        validate_method_inputs(
            root,
            scope,
            packet,
            trusted_method_projection,
            trusted_methods,
        )
    )
    return identifiers
