"""Strict on-disk boundary for a durable selected Run session."""

# implementation of:
# Requirement: CA-R-1524
# Method: CA-M-405, CA-M-410

from __future__ import annotations

from collections.abc import Mapping
from copy import deepcopy
import hashlib
from pathlib import Path
from typing import Any, Literal

from pydantic import BaseModel, ConfigDict

from selected_evidence_io import bounded_bytes, run_directory, safe_path
from selected_execution_contracts import RUN_ID, SelectedExecutionError, canonical_json


CHECKPOINT_NAME = "integrated_session.json"
MAX_CHECKPOINT_BYTES = 256 * 1024
MAX_EVIDENCE_BYTES = 8 * 1024 * 1024


class CheckpointRecord(BaseModel):
    """The closed JSON shape persisted beside one selected Run."""

    model_config = ConfigDict(extra="forbid", strict=True)

    schema_version: Literal[1]
    project_root_digest: str
    run_id: str
    frozen_digest: str
    request: dict[str, Any]
    actual: dict[str, dict[str, Any]]
    terminal: dict[str, dict[str, Any]]
    interrupted: dict[str, dict[str, Any]]
    observed_effects: dict[str, dict[str, Any]]
    start_event_ids: dict[str, str]
    recording_errors: list[str]
    evidence_digests: dict[str, str]


def digest(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def context(frozen: Mapping[str, Any]) -> tuple[str, dict[str, Any], str]:
    request = frozen.get("request")
    if not isinstance(request, Mapping) or not isinstance(request.get("run_id"), str):
        raise SelectedExecutionError("selected checkpoint frozen request is invalid")
    run_id, execution = request["run_id"], request.get("execution")
    if not RUN_ID.fullmatch(run_id) or not isinstance(execution, Mapping):
        raise SelectedExecutionError("selected checkpoint frozen request is invalid")
    try:
        return run_id, deepcopy(dict(execution)), digest(canonical_json(frozen))
    except (TypeError, ValueError) as error:
        raise SelectedExecutionError("selected checkpoint frozen request is not JSON") from error


def evidence_bytes(root: Path, reference: str) -> bytes:
    try:
        return bounded_bytes(safe_path(root, reference), MAX_EVIDENCE_BYTES)
    except SelectedExecutionError as error:
        raise SelectedExecutionError("selected checkpoint evidence is unavailable") from error


def load(root: Path, run_id: str) -> CheckpointRecord:
    path = run_directory(root, run_id) / CHECKPOINT_NAME
    try:
        payload = bounded_bytes(
            safe_path(root, path.relative_to(root).as_posix()), MAX_CHECKPOINT_BYTES
        )
        return CheckpointRecord.model_validate_json(payload)
    except (SelectedExecutionError, ValueError) as error:
        raise SelectedExecutionError("selected checkpoint is unsafe or invalid") from error
