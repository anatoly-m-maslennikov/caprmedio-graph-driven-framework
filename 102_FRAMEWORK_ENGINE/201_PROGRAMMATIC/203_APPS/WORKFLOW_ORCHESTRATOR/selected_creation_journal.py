"""Append an observed creation after reading back its source carrier."""

from __future__ import annotations

import hashlib
from collections.abc import Mapping
from pathlib import Path
import re
import sys
from typing import Any

from selected_execution_contracts import SelectedExecutionError, canonical_json


TOOLS = Path(__file__).resolve().parents[2] / "201_TOOLS"
if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))

from work_journal import append_sealed_events  # noqa: E402


class CreationJournalError(RuntimeError):
    """The observed source carrier does not match the supplied result."""


def canonical_event(
    *,
    parameters: object,
    native_result: Mapping[str, Any],
    creation_binding: Mapping[str, Any],
    creation_action_run_id: str,
    execution_request_id: object,
    author: str,
    occurred_at: str,
    structural_scope: str,
) -> dict[str, Any]:
    """Build W01's schema-3 ADD event from its observed source result."""
    if (
        not isinstance(parameters, Mapping)
        or not isinstance(execution_request_id, str)
        or not execution_request_id
    ):
        raise SelectedExecutionError("creation request identity is invalid")
    requested = parameters.get("carrier")
    observed = native_result.get("observed")
    native_requested = native_result.get("requested")
    if (
        not isinstance(requested, Mapping)
        or not isinstance(native_requested, Mapping)
        or not isinstance(observed, Mapping)
    ):
        raise SelectedExecutionError("creation did not return complete observed provenance")
    requested_path = requested.get("path")
    if (
        canonical_json(dict(native_requested)) != canonical_json(dict(requested))
        or observed.get("path") != requested_path
    ):
        raise SelectedExecutionError("creation observed carrier differs from its admitted input")
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
        or not isinstance(creation_action_run_id, str)
        or not creation_action_run_id
    ):
        raise SelectedExecutionError("creation returned an invalid observed carrier")
    try:
        import work_journal
    except ImportError as error:
        raise SelectedExecutionError("canonical Work Journal support is unavailable") from error
    event = {
        "schema_version": 3,
        "event_id": f"selected-creation:{creation_action_run_id}",
        "action_id": creation_binding["atom_id"],
        "event": "completed",
        "kind": "governed_project_change",
        "subject_kind": "file",
        "author": author,
        "occurred_at": occurred_at,
        "llm_session": {"app": "run-support", "uuid": execution_request_id},
        "structural_scope": structural_scope,
        "action_type": "ADD",
        "sources": [],
        "result": {
            "state": "present",
            "filename": result_filename,
            "version": result_version,
            "path": result_path,
            "sha256": result_digest,
        },
    }
    return work_journal.with_event_digest(event)


def _read_observed_result(root: Path, result: Mapping[str, Any]) -> None:
    path = result.get("path")
    digest = result.get("sha256")
    if not isinstance(path, str) or not isinstance(digest, str):
        raise CreationJournalError("creation result must identify a path and sha256")
    relative = Path(path)
    if relative.is_absolute() or ".." in relative.parts or not relative.parts:
        raise CreationJournalError("created carrier readback path is unsafe")

    canonical_root = root.resolve()
    candidate = root / relative
    current = root
    for component in relative.parts:
        current = current / component
        if current.is_symlink():
            raise CreationJournalError("created carrier readback path is unsafe")
    try:
        resolved = candidate.resolve(strict=True)
        resolved.relative_to(canonical_root)
    except (OSError, RuntimeError, ValueError) as error:
        raise CreationJournalError("created carrier readback path is unsafe") from error
    if not resolved.is_file() or resolved.is_symlink():
        raise CreationJournalError("created carrier readback path is unsafe")
    if hashlib.sha256(resolved.read_bytes()).hexdigest() != digest:
        raise CreationJournalError("created carrier readback differs from supplied result")


def record_selected_creation(
    root: Path,
    *,
    canonical_event: Mapping[str, Any],
    author: object,
    local_date: object,
    timezone: object,
    append_context: Mapping[str, Any] | None = None,
) -> Mapping[str, Any]:
    """Append one already-authorized, observed creation event."""
    result = canonical_event.get("result")
    if not isinstance(result, Mapping):
        raise CreationJournalError("creation event has no source result")
    project_root = Path(root)
    _read_observed_result(project_root, result)
    locations = append_sealed_events(
        project_root,
        [canonical_event],
        author=author,
        local_date=local_date,
        timezone=timezone,
        append_context=append_context,
    )
    return {"state": "completed", "event": canonical_event, "locations": locations}
