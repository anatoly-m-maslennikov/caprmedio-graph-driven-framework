# implementation of:
# Method: CA-M-405, CA-M-409, CA-M-410, CA-M-422
"""Closed state schema and bounded carrier I/O for Integrated frontiers."""

from __future__ import annotations

from collections.abc import Mapping
import copy
import json
from pathlib import Path
from typing import Any

from selected_evidence_io import atomic_write, bounded_bytes
from selected_execution_contracts import SelectedExecutionError
from selected_integrated_frontier_records import (
    MAX_RECORD_BYTES,
    MAX_RECORDS,
    IntegratedFrontierError,
    canonical,
    digest,
    validate_frontier,
    validate_submission,
)
from selected_integrated_frontier_response import read_response, response_ref, write_response


STATE_FIELDS = frozenset(
    {"schema_version", "project_root_digest", "run_id", "current_continuation_id", "records"}
)
RECORD_FIELDS = {
    "pending": frozenset({"frontier", "state"}),
    "admitted": frozenset({"frontier", "state", "submission", "submission_digest"}),
}
_V1_COMPLETED = frozenset(
    {"frontier", "state", "submission", "submission_digest", "response", "response_digest"}
)
_V2_COMPLETED = frozenset(
    {"frontier", "state", "submission", "submission_digest", "response_ref", "response_digest"}
)


def hydrate_record(record: Mapping[str, Any], state_path: Path) -> dict[str, Any]:
    """Restore the original response shape without exposing its private reference."""
    value = copy.deepcopy(dict(record))
    if "response_ref" in value:
        value["response"] = read_response(
            state_path,
            value["frontier"]["continuation_id"],
            value.pop("response_ref"),
            value["response_digest"],
        )
    return value


def receipt_view(record: Mapping[str, Any], state_path: Path) -> dict[str, Any]:
    """Return the retained submission and, when present, its original response."""
    retained = hydrate_record(record, state_path)
    value = {
        "continuation_id": retained["frontier"]["continuation_id"],
        "submission": retained["submission"],
    }
    if "response" in retained:
        value["response"] = retained["response"]
    return value


def pending_view(state: Mapping[str, Any], state_path: Path) -> dict[str, Any]:
    """Expose the one pending pointer without losing consumed receipts."""
    current = state["records"].get(state["current_continuation_id"])
    frontier = current["frontier"] if current and current["state"] == "pending" else None
    receipts = {
        key: receipt_view(record, state_path)
        for key, record in state["records"].items()
        if "submission" in record
    }
    return {"frontier": copy.deepcopy(frontier), "receipts": receipts}


def empty_state(root: Path, run_id: str) -> dict[str, Any]:
    return {
        "schema_version": 2,
        "project_root_digest": digest(root.as_posix()),
        "run_id": run_id,
        "current_continuation_id": None,
        "records": {},
    }


def _validate_completed(record: Mapping[str, Any], key: str, version: int) -> None:
    if version == 1 and record["response_digest"] != digest(record["response"]):
        raise IntegratedFrontierError("completed frontier response digest is stale")
    if version == 2 and record["response_ref"] != response_ref(key, record["response_digest"]):
        raise IntegratedFrontierError("completed frontier response reference is stale")


def _validate_record(record: object, key: str, root: Path, run_id: str, version: int) -> None:
    if not isinstance(record, dict) or record.get("state") not in {*RECORD_FIELDS, "completed"}:
        raise IntegratedFrontierError("Integrated frontier record is invalid")
    state = record["state"]
    if state == "completed":
        fields = _V1_COMPLETED if version == 1 else _V2_COMPLETED
    else:
        fields = RECORD_FIELDS[state]
    if set(record) != fields:
        raise IntegratedFrontierError("Integrated frontier record fields are not closed")
    frontier = record["frontier"]
    if not isinstance(frontier, Mapping):
        raise IntegratedFrontierError("Integrated frontier record has no frontier")
    checked_frontier = validate_frontier(frontier, run_id, root)
    if key != checked_frontier["continuation_id"]:
        raise IntegratedFrontierError("Integrated frontier record key is not its continuation")
    if state == "pending":
        return
    submission = record["submission"]
    if not isinstance(submission, Mapping) or validate_submission(submission) != submission:
        raise IntegratedFrontierError("Integrated frontier submission is invalid")
    if submission["continuation_id"] != key or record["submission_digest"] != digest(submission):
        raise IntegratedFrontierError("Integrated frontier submission binding is stale")
    if state == "completed":
        _validate_completed(record, key, version)


def _validate_state(value: object, root: Path, run_id: str) -> dict[str, Any]:
    if not isinstance(value, dict) or set(value) != STATE_FIELDS:
        raise IntegratedFrontierError("Integrated frontier state fields are not closed")
    version = value["schema_version"]
    if type(version) is not int or version not in {1, 2}:
        raise IntegratedFrontierError("Integrated frontier state schema is unsupported")
    if value["project_root_digest"] != digest(root.as_posix()) or value["run_id"] != run_id:
        raise IntegratedFrontierError("Integrated frontier state binding is stale")
    records = value["records"]
    if not isinstance(records, dict) or len(records) > MAX_RECORDS:
        raise IntegratedFrontierError("Integrated frontier record history is invalid or unbounded")
    current = value["current_continuation_id"]
    if current is not None and (not isinstance(current, str) or current not in records):
        raise IntegratedFrontierError("Integrated frontier current pointer is invalid")
    pending = []
    for key, record in records.items():
        if not isinstance(key, str):
            raise IntegratedFrontierError("Integrated frontier record key is invalid")
        _validate_record(record, key, root, run_id, version)
        if record["state"] == "pending":
            pending.append(key)
    if len(pending) > 1 or (pending and current != pending[0]):
        raise IntegratedFrontierError("Integrated frontier pending pointer is inconsistent")
    return value


def _read_carrier(path: Path) -> bytes | None:
    try:
        return bounded_bytes(path, MAX_RECORD_BYTES)
    except SelectedExecutionError as error:
        if isinstance(error.__cause__, FileNotFoundError):
            return None
        raise IntegratedFrontierError(
            "Integrated frontier carrier is unsafe or unreadable"
        ) from error


def read_state(path: Path, root: Path, run_id: str) -> dict[str, Any]:
    payload = _read_carrier(path)
    if payload is None:
        return empty_state(root, run_id)
    try:
        value = json.loads(payload.decode("utf-8"))
    except (UnicodeDecodeError, ValueError) as error:
        raise IntegratedFrontierError("Integrated frontier carrier is invalid") from error
    return _validate_state(value, root, run_id)


def upgrade_legacy_responses(value: dict[str, Any], path: Path) -> None:
    """Write all legacy responses before atomically changing to state v2."""
    if value["schema_version"] == 2:
        return
    for continuation_id, record in value["records"].items():
        if record["state"] == "completed":
            reference, response_digest = write_response(
                path, continuation_id, record.pop("response")
            )
            record["response_ref"] = reference
            record["response_digest"] = response_digest
    value["schema_version"] = 2


def write_state(path: Path, root: Path, run_id: str, value: Mapping[str, Any]) -> None:
    payload = canonical(value)
    if len(payload) > MAX_RECORD_BYTES:
        raise IntegratedFrontierError("Integrated frontier state exceeds its bounded carrier size")
    _validate_state(value, root, run_id)
    if path.is_symlink() or (path.exists() and not path.is_file()):
        raise IntegratedFrontierError("Integrated frontier destination is unsafe")
    try:
        atomic_write(path, value)
    except (OSError, RuntimeError, ValueError) as error:
        raise IntegratedFrontierError("Integrated frontier state could not be persisted") from error
