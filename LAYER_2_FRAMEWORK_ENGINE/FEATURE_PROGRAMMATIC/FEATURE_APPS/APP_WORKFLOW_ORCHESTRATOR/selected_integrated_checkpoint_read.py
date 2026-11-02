"""Read-only validation of one durable Integrated Run checkpoint."""

# implementation of:
# Requirement: CA-R-1524
# Method: CA-M-405, CA-M-410

from __future__ import annotations

from collections.abc import Mapping
from copy import deepcopy
from pathlib import Path
from typing import Any

from selected_execution_contracts import SelectedExecutionError, canonical_json
from selected_integrated_frontier_records import IntegratedFrontierError, project_root
from selected_integrated_session_record import (
    CheckpointRecord,
    context,
    digest,
    evidence_bytes,
    load,
)
from selected_integrated_session_validation import validate_checkpoint_state


def _root(root: Path) -> Path:
    try:
        return project_root(root)
    except IntegratedFrontierError as error:
        raise SelectedExecutionError("selected checkpoint Project root is unavailable") from error


def load_bound_checkpoint(
    root: Path, frozen: Mapping[str, Any]
) -> tuple[CheckpointRecord, dict[str, bytes]]:
    """Load checkpoint data and its exact verified evidence without resuming."""
    safe_root = _root(Path(root))
    run_id, request, frozen_digest = context(frozen)
    record = load(safe_root, run_id)
    if (
        record.run_id != run_id
        or record.frozen_digest != frozen_digest
        or record.project_root_digest != digest(safe_root.as_posix().encode())
        or canonical_json(record.request) != canonical_json(request)
    ):
        raise SelectedExecutionError(
            "selected checkpoint binding differs from the current frozen Run"
        )
    validate_checkpoint_state(
        request,
        actual=record.actual,
        terminal=record.terminal,
        interrupted=record.interrupted,
        observed_effects=record.observed_effects,
        start_event_ids=record.start_event_ids,
        recording_errors=record.recording_errors,
        evidence_digests=record.evidence_digests,
    )
    evidence: dict[str, bytes] = {}
    for reference, stored_digest in record.evidence_digests.items():
        payload = evidence_bytes(safe_root, reference)
        if digest(payload) != stored_digest:
            raise SelectedExecutionError("selected checkpoint evidence changed after recording")
        evidence[reference] = payload
    return deepcopy(record), evidence
