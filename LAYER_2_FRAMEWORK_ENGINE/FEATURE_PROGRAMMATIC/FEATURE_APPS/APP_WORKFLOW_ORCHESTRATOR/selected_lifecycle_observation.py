"""Source observations shared by selected lifecycle Journal recording."""

from __future__ import annotations

from collections.abc import Mapping
import datetime as dt
from pathlib import Path
import re
from typing import Any
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError

from selected_execution_contracts import SelectedExecutionError, _sha256
from selected_evidence_io import safe_path
from selected_graph_sources import _frontmatter


def journal_context(session: Any) -> tuple[str, str, str, str]:
    """Take observed author and clock settings from the selected session."""
    tracker = getattr(session, "tracker", None)
    context = getattr(tracker, "journal_context", None)
    if not isinstance(context, Mapping):
        raise SelectedExecutionError("replacement requires the current tracker Journal context")
    author = context.get("author")
    timezone = context.get("timezone")
    if not isinstance(author, str) or not isinstance(timezone, str):
        raise SelectedExecutionError("replacement tracker Journal context is invalid")
    try:
        now = dt.datetime.now(ZoneInfo(timezone))
        local_date = now.date().isoformat()
    except (ValueError, ZoneInfoNotFoundError) as error:
        raise SelectedExecutionError("replacement tracker Journal context is invalid") from error
    return author, local_date, timezone, now.isoformat(timespec="seconds")


def _read_scope(
    root: Path,
    path: str,
    digest: str,
    changed_message: str,
    missing_message: str,
) -> str:
    source = safe_path(root, path)
    if _sha256(source.read_bytes()) != digest:
        raise SelectedExecutionError(changed_message)
    scope = _frontmatter(source).get("current_scope_unit")
    if not isinstance(scope, str) or not scope:
        raise SelectedExecutionError(missing_message)
    return scope


def creation_structural_scope(root: Path, binding: Mapping[str, Any]) -> str:
    """Read scope from the exact admitted O032 Action carrier."""
    path = binding.get("path")
    digest = binding.get("sha256")
    if not isinstance(path, str) or not isinstance(digest, str):
        raise SelectedExecutionError("creation CA-O-032 Action binding is invalid")
    return _read_scope(
        root,
        path,
        digest,
        "creation CA-O-032 Action definition changed after admission",
        "creation CA-O-032 Action has no current scope",
    )


def lifecycle_structural_scope(root: Path, binding: Mapping[str, Any]) -> str:
    """Read W02/W04 scope from the source-bound native Action carrier."""
    if binding.get("atom_id") not in {"CA-O-029", "CA-O-030"}:
        raise SelectedExecutionError("lifecycle native Action binding is invalid")
    return bound_action_structural_scope(root, binding)


def bound_action_structural_scope(root: Path, binding: Mapping[str, Any]) -> str:
    """Read a current Action scope after rechecking its admitted bytes."""
    action_id = binding.get("atom_id")
    path = binding.get("path")
    digest = binding.get("sha256")
    if (
        not isinstance(action_id, str)
        or not action_id
        or not isinstance(path, str)
        or not isinstance(digest, str)
    ):
        raise SelectedExecutionError("bound Action binding is invalid")
    return _read_scope(
        root,
        path,
        digest,
        "bound Action definition changed after admission",
        "bound Action has no current scope",
    )


def replacement_structural_scope(root: Path, binding: Mapping[str, Any]) -> str:
    """Read scope from the exact admitted O051 carrier."""
    path = binding.get("path")
    digest = binding.get("sha256")
    if not isinstance(path, str) or not isinstance(digest, str):
        raise SelectedExecutionError("replacement CA-O-051 Action binding is invalid")
    return _read_scope(
        root,
        path,
        digest,
        "replacement CA-O-051 Action definition changed after admission",
        "replacement CA-O-051 Action has no current scope",
    )


def result_facts(root: Path, observed: object) -> tuple[dict[str, Any], bytes]:
    """Bind a native descriptor to current regular-file bytes exactly once."""
    if not isinstance(observed, Mapping):
        raise SelectedExecutionError("lifecycle Action did not return an observed carrier")
    path = observed.get("path")
    filename = observed.get("filename")
    version = observed.get("version")
    digest = observed.get("digest")
    if (
        not isinstance(path, str)
        or not path
        or Path(path).is_absolute()
        or ".." in Path(path).parts
        or not isinstance(filename, str)
        or not filename
        or Path(filename).name != filename
        or type(version) is not int
        or version < 1
        or not isinstance(digest, str)
        or re.fullmatch(r"[0-9a-f]{64}", digest) is None
    ):
        raise SelectedExecutionError("lifecycle Action observed carrier is invalid")
    candidate = safe_path(root, path)
    if candidate.is_symlink() or not candidate.is_file():
        raise SelectedExecutionError("lifecycle Action observed carrier is unsafe")
    current = candidate.read_bytes()
    if _sha256(current) != digest:
        raise SelectedExecutionError("lifecycle Action observed carrier differs from current bytes")
    return {"filename": filename, "version": version, "path": path, "sha256": digest}, current


def lifecycle_action_type(before: Mapping[str, Any], after: Mapping[str, Any]) -> str:
    """Represent current-state differences without treating every change as ADD."""
    if before.get("path") != after.get("path"):
        return "MOVE+UPDATE"
    return "UPDATE"
