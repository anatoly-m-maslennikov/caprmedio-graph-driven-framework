"""Read-only reconstruction of selected-Run Journal evidence.

This module deliberately has no append, pending-event recovery, executor, or
dispatch function.  It can only prove what an already accepted selected Run
recorded, then hand that evidence to :class:`RunExecutionSession` for state
reconstruction.
"""

from __future__ import annotations

import hashlib
import json
from collections.abc import Iterable, Mapping
from pathlib import Path
from typing import Any

import work_journal
from workflow_run_support import SelectedRunError, _validate_common


def canonical_dispatch_bytes(request: Mapping[str, Any]) -> bytes:
    """Return the exact immutable request bytes recorded before dispatch."""
    parsed = _validate_common(request)
    if parsed["mode"] != "execute":
        raise SelectedRunError("invalid-recovery", "only an execute request has dispatch recovery evidence")
    return work_journal.canonical_json_bytes({key: parsed[key] for key in sorted(parsed) if key != "mode"})


def inspect_selected_run_dispatch(root: str | Path, request: Mapping[str, Any]) -> dict[str, Any]:
    """Read and bind one accepted dispatch carrier without changing it."""
    root_path = _root(root)
    expected_bytes = canonical_dispatch_bytes(request)
    parsed = _validate_common(request)
    try:
        runtime_root = work_journal.configured_runtime_root(root_path)
        work_journal.configured_journal_root(root_path)
    except (OSError, RuntimeError) as error:
        raise SelectedRunError("invalid-recovery", f"configured recovery roots are unavailable: {error}") from error
    path = (
        root_path
        / runtime_root
        / "state"
        / "work_journal"
        / "selected_runs"
        / "requests"
        / f"{_sha256(parsed['request_id'].encode('utf-8'))}.json"
    )
    _require_regular_file(path, root_path / runtime_root)
    try:
        raw = path.read_bytes()
        value = json.loads(raw)
    except FileNotFoundError as error:
        raise SelectedRunError("dispatch-not-found", "accepted dispatch evidence does not exist") from error
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as error:
        raise SelectedRunError("invalid-dispatch-evidence", "cannot read accepted dispatch evidence") from error
    expected_fields = {
        "schema_version", "request_id", "canonical_request_bytes",
        "canonical_request_bytes_digest", "state",
    }
    if (
        not isinstance(value, dict)
        or set(value) != expected_fields
        or value.get("schema_version") != 1
        or value.get("request_id") != parsed["request_id"]
        or value.get("state") != "accepted"
        or not isinstance(value.get("canonical_request_bytes"), str)
    ):
        raise SelectedRunError("invalid-dispatch-evidence", "accepted dispatch evidence has invalid fields")
    encoded = value["canonical_request_bytes"].encode("utf-8")
    if (
        value.get("canonical_request_bytes_digest") != _sha256(encoded)
        or encoded != expected_bytes
    ):
        raise SelectedRunError("dispatch-mismatch", "accepted dispatch evidence does not bind this exact execute request")
    try:
        decoded = json.loads(encoded)
    except json.JSONDecodeError as error:
        raise SelectedRunError("invalid-dispatch-evidence", "accepted dispatch bytes are not JSON") from error
    if work_journal.canonical_json_bytes(decoded) != encoded:
        raise SelectedRunError("invalid-dispatch-evidence", "accepted dispatch bytes are not canonical")
    return {**value, "carrier": path.relative_to(root_path).as_posix()}


def validate_selected_run_events(
    request: Mapping[str, Any],
    events: Iterable[Mapping[str, Any]],
) -> list[dict[str, Any]]:
    """Return Journal rows as supplied; Run authorization is independent."""
    return [dict(event) for event in events]


def read_selected_run_evidence(root: str | Path, request: Mapping[str, Any]) -> dict[str, Any]:
    """Read bounded canonical Journal evidence for one accepted dispatch.

    The function reads only configured runtime dispatch evidence and canonical
    Journal part carriers.  It does not inspect pending evidence, append a
    recovery event, or execute an Action.
    """
    root_path = _root(root)
    dispatch = inspect_selected_run_dispatch(root_path, request)
    parsed = _validate_common(request)
    records = work_journal.read_records(root_path)
    return {
        "dispatch": dispatch,
        "events": [
            dict(event)
            for event in records
            if isinstance(event, Mapping) and _possibly_selected_event(event, parsed)
        ],
    }


def _root(root: str | Path) -> Path:
    path = Path(root)
    try:
        resolved = path.resolve(strict=True)
    except OSError as error:
        raise SelectedRunError("invalid-recovery", "recovery root does not exist") from error
    if not resolved.is_dir():
        raise SelectedRunError("invalid-recovery", "recovery root must be a directory")
    return resolved


def _possibly_selected_event(event: Mapping[str, Any], request: Mapping[str, Any]) -> bool:
    session = event.get("llm_session")
    request_matches = isinstance(session, Mapping) and session.get("uuid") == request["request_id"]
    action_matches = event.get("action_id") == request["assigned_action_id"]
    return request_matches and action_matches


def _require_regular_file(path: Path, boundary: Path) -> None:
    if path.is_symlink() or not path.is_file():
        raise SelectedRunError("dispatch-not-found", "required recovery evidence is not a regular file")
    try:
        path.resolve(strict=True).relative_to(boundary.resolve(strict=True))
    except (OSError, ValueError) as error:
        raise SelectedRunError("invalid-recovery", "recovery evidence escapes its configured root") from error


def _sha256(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()
