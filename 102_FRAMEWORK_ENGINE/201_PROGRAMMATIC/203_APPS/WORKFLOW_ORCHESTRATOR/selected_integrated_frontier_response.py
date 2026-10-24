# implementation of:
# Method: CA-M-405, CA-M-409, CA-M-410, CA-M-422
"""Immutable bounded response carriers for Integrated continuation receipts."""

from __future__ import annotations

import copy
import json
from pathlib import Path

from selected_evidence_io import atomic_write, bounded_bytes
from selected_execution_contracts import SelectedExecutionError
from selected_integrated_frontier_records import (
    MAX_RECORD_BYTES,
    IntegratedFrontierError,
    canonical,
    digest,
    sha,
    text,
)


_PREFIX = "integrated_frontier_response_"


def response_ref(continuation_id: str, response_digest: str) -> str:
    """Return a filesystem-safe immutable response reference."""
    continuation = text(continuation_id, "continuation_id")
    response_hash = sha(response_digest, "response_digest")
    identity = digest({"continuation_id": continuation, "response_digest": response_hash})
    return f"{_PREFIX}{identity}.json"


def _path(state_path: Path, continuation_id: str, response_digest: str, reference: str) -> Path:
    if reference != response_ref(continuation_id, response_digest):
        raise IntegratedFrontierError("Integrated frontier response reference is invalid")
    return state_path.with_name(reference)


def write_response(state_path: Path, continuation_id: str, response: object) -> tuple[str, str]:
    """Persist one response before its state reference becomes visible."""
    payload = canonical(response)
    if len(payload) > MAX_RECORD_BYTES:
        raise IntegratedFrontierError(
            "Integrated frontier response exceeds its bounded carrier size"
        )
    response_digest = digest(response)
    reference = response_ref(continuation_id, response_digest)
    path = _path(state_path, continuation_id, response_digest, reference)
    if path.is_symlink() or (path.exists() and not path.is_file()):
        raise IntegratedFrontierError("Integrated frontier response destination is unsafe")
    if path.exists():
        try:
            if bounded_bytes(path, MAX_RECORD_BYTES) != payload:
                raise IntegratedFrontierError("conflicting retained Integrated response")
        except SelectedExecutionError as error:
            raise IntegratedFrontierError(
                "Integrated frontier response is unsafe or unreadable"
            ) from error
        return reference, response_digest
    try:
        atomic_write(path, response)
    except (OSError, RuntimeError, ValueError) as error:
        raise IntegratedFrontierError(
            "Integrated frontier response could not be persisted"
        ) from error
    return reference, response_digest


def read_response(
    state_path: Path, continuation_id: str, reference: str, response_digest: str
) -> object:
    """Return a verified deep copy of a retained response."""
    path = _path(state_path, continuation_id, response_digest, reference)
    try:
        payload = bounded_bytes(path, MAX_RECORD_BYTES)
        response = json.loads(payload.decode("utf-8"))
    except (SelectedExecutionError, UnicodeDecodeError, ValueError) as error:
        raise IntegratedFrontierError(
            "Integrated frontier response is unsafe or unreadable"
        ) from error
    if payload != canonical(response) or digest(response) != response_digest:
        raise IntegratedFrontierError("retained Integrated response is stale")
    return copy.deepcopy(response)
