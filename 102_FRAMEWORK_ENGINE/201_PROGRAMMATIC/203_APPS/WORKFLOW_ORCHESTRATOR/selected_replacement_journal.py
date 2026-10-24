"""Append an observed replacement after reading back its source carrier."""

from __future__ import annotations

import hashlib
from collections.abc import Mapping
from pathlib import Path
import re
import sys
from typing import Any

from selected_execution_contracts import SelectedExecutionError


TOOLS = Path(__file__).resolve().parents[2] / "201_TOOLS"
if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))

from work_journal import append_sealed_events  # noqa: E402


class ReplacementJournalError(RuntimeError):
    """The observed source carrier does not match the supplied result."""


def canonical_event(
    *,
    parameters: object,
    native_result: Mapping[str, Any],
    replacement_binding: Mapping[str, Any],
    replacement_action_run_id: str,
    execution_request_id: object,
    author: str,
    occurred_at: str,
    structural_scope: str,
) -> dict[str, Any]:
    """Build only the observed O051 replacement provenance event."""
    if (
        not isinstance(parameters, Mapping)
        or not isinstance(execution_request_id, str)
        or not execution_request_id
    ):
        raise SelectedExecutionError("replacement request identity is invalid")
    requested_predecessor = parameters.get("predecessor")
    history = native_result.get("history")
    observed = native_result.get("predecessor")
    successors = native_result.get("successors")
    if (
        not isinstance(requested_predecessor, Mapping)
        or not isinstance(history, Mapping)
        or not isinstance(history.get("predecessor"), Mapping)
        or not isinstance(observed, Mapping)
        or not isinstance(successors, list)
        or not successors
    ):
        raise SelectedExecutionError("replacement did not return complete observed provenance")
    original = history["predecessor"]
    for field in ("path", "version", "digest"):
        if original.get(field) != requested_predecessor.get(field):
            raise SelectedExecutionError(
                "replacement observed predecessor differs from its admitted input"
            )
    predecessor_id = original.get("atom_id")
    successor_ids = [
        item.get("atom_id") if isinstance(item, Mapping) else None for item in successors
    ]
    if (
        not isinstance(predecessor_id, str)
        or not predecessor_id
        or any(not isinstance(item, str) or not item for item in successor_ids)
        or len(successor_ids) != len(set(successor_ids))
    ):
        raise SelectedExecutionError("replacement returned invalid successor identities")
    result_path = observed.get("path")
    result_filename = observed.get("filename")
    result_version = observed.get("version")
    result_digest = observed.get("digest")
    if (
        not isinstance(result_path, str)
        or not result_path
        or Path(result_path).is_absolute()
        or ".." in Path(result_path).parts
        or not isinstance(result_filename, str)
        or not result_filename
        or type(result_version) is not int
        or result_version < 1
        or not isinstance(result_digest, str)
        or re.fullmatch(r"[0-9a-f]{64}", result_digest) is None
        or not isinstance(replacement_action_run_id, str)
        or not replacement_action_run_id
    ):
        raise SelectedExecutionError("replacement returned an invalid archived predecessor")
    return {
        "schema_version": 3,
        "event_id": f"selected-replacement:{replacement_action_run_id}",
        "action_id": replacement_binding["atom_id"],
        "event": "completed",
        "kind": "governed_project_change",
        "subject_kind": "file",
        "author": author,
        "occurred_at": occurred_at,
        "llm_session": {"app": "run-support", "uuid": execution_request_id},
        "structural_scope": structural_scope,
        "action_type": "MOVE+UPDATE",
        "sources": [],
        "predecessor_atom_id": predecessor_id,
        "successor_atom_ids": successor_ids,
        "result": {
            "state": "present",
            "filename": result_filename,
            "version": result_version,
            "path": result_path,
            "sha256": result_digest,
        },
    }


def _read_verified_result(root: Path, result: Mapping[str, Any]) -> None:
    path = result.get("path")
    digest = result.get("sha256")
    if not isinstance(path, str) or not isinstance(digest, str):
        raise ReplacementJournalError("replacement result must identify a path and sha256")
    relative = Path(path)
    if relative.is_absolute() or ".." in relative.parts or not relative.parts:
        raise ReplacementJournalError("replacement readback path is unsafe")

    canonical_root = root.resolve()
    candidate = root / relative
    current = root
    for component in relative.parts:
        current = current / component
        if current.is_symlink():
            raise ReplacementJournalError("replacement readback path is unsafe")
    try:
        resolved = candidate.resolve(strict=True)
        resolved.relative_to(canonical_root)
    except (OSError, RuntimeError, ValueError) as error:
        raise ReplacementJournalError("replacement readback path is unsafe") from error
    if not resolved.is_file() or resolved.is_symlink():
        raise ReplacementJournalError("replacement readback path is unsafe")
    if hashlib.sha256(resolved.read_bytes()).hexdigest() != digest:
        raise ReplacementJournalError("replacement readback differs from supplied result")


def record_selected_replacement(
    root: Path,
    *,
    canonical_event: Mapping[str, Any],
    author: object,
    local_date: object,
    timezone: object,
    append_context: Mapping[str, Any] | None = None,
) -> Mapping[str, Any]:
    """Append one already-authorized, observed replacement event."""
    result = canonical_event.get("result")
    if not isinstance(result, Mapping):
        raise ReplacementJournalError("replacement event has no source result")
    project_root = Path(root)
    _read_verified_result(project_root, result)
    locations = append_sealed_events(
        project_root,
        [canonical_event],
        author=author,
        local_date=local_date,
        timezone=timezone,
        append_context=append_context,
    )
    return {"state": "completed", "event": canonical_event, "locations": locations}
