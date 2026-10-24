# implementation of:
# Method: CA-M-405, CA-M-409, CA-M-410, CA-M-422
"""Durable one-use state for the source-bound Integrated continuation loop."""

from __future__ import annotations

from collections.abc import Mapping
import fcntl
import os
from pathlib import Path
from typing import Any

from selected_integrated_frontier_records import (
    MAX_RECORD_BYTES,
    MAX_RECORDS,
    IntegratedFrontierError,
    digest,
    project_root,
    state_path,
    text,
    validate_frontier,
    validate_submission,
)
from selected_integrated_frontier_state import (
    hydrate_record,
    pending_view,
    read_state,
    receipt_view,
    upgrade_legacy_responses,
    write_state,
)
from selected_integrated_frontier_response import write_response


class IntegratedFrontierStore:
    """Own one Project/Run lock across admission, resume, and next publication."""

    def __init__(self, root: str | Path, run_id: str) -> None:
        self.root = project_root(root)
        self.run_id = run_id
        self._lock: Any = None
        self._state: Path | None = None

    def __enter__(self) -> "IntegratedFrontierStore":
        self._state = state_path(self.root, self.run_id)
        lock_path = self._state.with_name(".integrated_frontier.lock")
        if lock_path.is_symlink() or (lock_path.exists() and not lock_path.is_file()):
            raise IntegratedFrontierError("Integrated frontier lock is unsafe")
        flags = os.O_CREAT | os.O_RDWR
        if hasattr(os, "O_NOFOLLOW"):
            flags |= os.O_NOFOLLOW
        descriptor = -1
        handle: Any = None
        try:
            descriptor = os.open(lock_path, flags, 0o600)
            handle = os.fdopen(descriptor, "a+")
            descriptor = -1
            fcntl.flock(handle.fileno(), fcntl.LOCK_EX)
        except (OSError, ValueError) as error:
            if handle is not None:
                handle.close()
            elif descriptor >= 0:
                os.close(descriptor)
            raise IntegratedFrontierError(
                "Integrated frontier lock could not be acquired"
            ) from error
        self._lock = handle
        return self

    def __exit__(self, *_: object) -> None:
        handle = self._lock
        self._lock = None
        if handle is None:
            return
        try:
            fcntl.flock(handle.fileno(), fcntl.LOCK_UN)
        except OSError as error:
            raise IntegratedFrontierError(
                "Integrated frontier lock could not be released"
            ) from error
        finally:
            handle.close()

    def _path(self) -> Path:
        if self._lock is None or self._state is None:
            raise IntegratedFrontierError("Integrated frontier store is not open")
        return self._state

    def _state_value(self) -> dict[str, Any]:
        return read_state(self._path(), self.root, self.run_id)

    def load(self) -> dict[str, Any]:
        return pending_view(self._state_value(), self._path())

    # implementation of:
    # Method: CA-M-405
    def record(self, continuation_id: str) -> dict[str, Any]:
        """Read a verified historical frontier under the existing Run lock."""
        records = self._state_value()["records"]
        retained = records.get(text(continuation_id, "continuation_id"))
        if retained is None:
            raise IntegratedFrontierError("no retained Integrated continuation exists")
        return hydrate_record(retained, self._path())

    def save(self, frontier: Mapping[str, Any]) -> None:
        checked = validate_frontier(frontier, self.run_id, self.root)
        state = self._state_value()
        continuation = checked["continuation_id"]
        records = state["records"]
        existing = records.get(continuation)
        if existing is not None:
            if existing["frontier"] != checked:
                raise IntegratedFrontierError("continuation frontier conflicts with retained state")
            return
        current_id = state["current_continuation_id"]
        current = records.get(current_id) if current_id is not None else None
        if isinstance(current, Mapping) and current["state"] == "pending":
            raise IntegratedFrontierError("a different Integrated frontier is already pending")
        if len(records) >= MAX_RECORDS:
            raise IntegratedFrontierError("Integrated frontier history reached its bounded limit")
        records[continuation] = {"frontier": checked, "state": "pending"}
        state["current_continuation_id"] = continuation
        write_state(self._path(), self.root, self.run_id, state)

    def admit(self, submission: Mapping[str, Any]) -> dict[str, Any]:
        checked = validate_submission(submission)
        state = self._state_value()
        record = state["records"].get(checked["continuation_id"])
        if not isinstance(record, dict):
            raise IntegratedFrontierError("submission does not bind a retained frontier")
        if "submission" in record:
            if record["submission"] != checked:
                raise IntegratedFrontierError("conflicting repeat submission")
            return receipt_view(record, self._path())
        if record["state"] != "pending":
            raise IntegratedFrontierError("frontier is not pending")
        record["submission"] = checked
        record["submission_digest"] = digest(checked)
        record["state"] = "admitted"
        write_state(self._path(), self.root, self.run_id, state)
        return receipt_view(record, self._path())

    def complete_receipt(self, continuation_id: str, response: object) -> dict[str, Any]:
        state = self._state_value()
        record = state["records"].get(continuation_id)
        if not isinstance(record, dict) or "submission" not in record:
            raise IntegratedFrontierError("completion does not bind an admitted submission")
        if record["state"] == "completed":
            if hydrate_record(record, self._path())["response"] != response:
                raise IntegratedFrontierError("conflicting retained Integrated response")
            return receipt_view(record, self._path())
        upgrade_legacy_responses(state, self._path())
        reference, response_digest = write_response(self._path(), continuation_id, response)
        record["response_ref"] = reference
        record["response_digest"] = response_digest
        record["state"] = "completed"
        write_state(self._path(), self.root, self.run_id, state)
        return receipt_view(record, self._path())


def save_pending(root: str | Path, run_id: str, frontier: Mapping[str, Any]) -> None:
    with IntegratedFrontierStore(root, run_id) as store:
        store.save(frontier)


def load_pending(root: str | Path, run_id: str) -> dict[str, Any]:
    with IntegratedFrontierStore(root, run_id) as store:
        loaded = store.load()
    if loaded["frontier"] is None and not loaded["receipts"]:
        raise IntegratedFrontierError("no retained Integrated frontier exists")
    return loaded


def admit_submission(
    root: str | Path, run_id: str, submission: Mapping[str, Any]
) -> dict[str, Any]:
    with IntegratedFrontierStore(root, run_id) as store:
        return store.admit(submission)


def complete_receipt(
    root: str | Path, run_id: str, continuation_id: str, response: object
) -> dict[str, Any]:
    with IntegratedFrontierStore(root, run_id) as store:
        return store.complete_receipt(continuation_id, response)


__all__ = [
    "IntegratedFrontierError",
    "IntegratedFrontierStore",
    "MAX_RECORD_BYTES",
    "MAX_RECORDS",
    "admit_submission",
    "complete_receipt",
    "load_pending",
    "save_pending",
]
