"""Observe retained business state without a scheduler or Action replay."""

# implementation of:
# Requirement: CA-R-1524, CA-R-2117
# Method: CA-M-405, CA-M-410, CA-M-431

from __future__ import annotations

from collections.abc import Mapping
import json
from pathlib import Path
from typing import Any

from selected_evidence_io import run_directory
from selected_execution_contracts import SelectedExecutionError
from selected_integrated_entry import load_request, owns
from selected_integrated_frontier import IntegratedFrontierStore
from selected_integrated_frontier_records import project_root
from selected_integrated_dispatch import _admitted_methods
from selected_integrated_dispatch_admission import validate
from selected_integrated_dispatch_capture import load_capture
from selected_integrated_dispatch_pending import revalidate_pending
from selected_integrated_dispatch_profile import profile_from_frozen
from selected_integrated_resume_pending import pending_response
from selected_integrated_session_record import CHECKPOINT_NAME, CheckpointRecord
from selected_integrated_checkpoint_read import load_bound_checkpoint
from selected_run_session import shared_tracker


def _terminal_response(
    root: Path,
    frozen: Mapping[str, Any],
    record: CheckpointRecord,
    receipt: Mapping[str, Any],
    evidence: Mapping[str, bytes],
) -> dict[str, Any] | None:
    reference = receipt.get("result_ref")
    if reference is None and receipt.get("disposition") == "interrupted":
        return None
    expected = (
        (run_directory(root, record.run_id) / "graph_result.json").relative_to(root).as_posix()
    )
    if reference != expected or expected not in evidence:
        raise SelectedExecutionError(
            "retained Workflow result does not bind its canonical graph evidence"
        )
    result = json.loads(evidence[expected])
    actual = record.actual.get(record.run_id)
    if (
        not isinstance(actual, Mapping)
        or not isinstance(result, dict)
        or receipt.get("run_id") != actual.get("run_id")
        or result.get("workflow_run_id") != actual.get("run_id")
        or result.get("workflow_definition_id") != frozen["graph"]["workflow"]["atom_id"]
        or result.get("outcome") != receipt.get("outcome")
    ):
        raise SelectedExecutionError("retained Workflow graph result identity or outcome differs")
    return {
        "disposition": "terminal",
        "status": receipt["outcome"],
        "outcome": receipt["outcome"],
        "run_disposition": receipt["disposition"],
        "workflow_run_id": actual["run_id"],
        "graph_result": result,
    }


def _retained_status(
    root: Path,
    frozen: Mapping[str, Any],
    record: CheckpointRecord,
    evidence: Mapping[str, bytes],
) -> dict[str, Any] | None:
    receipt = record.terminal.get(record.run_id) or record.interrupted.get(record.run_id)
    if isinstance(receipt, Mapping):
        terminal = _terminal_response(root, frozen, record, receipt, evidence)
        if terminal is not None:
            return terminal
    if record.interrupted:
        actual = record.actual.get(record.run_id)
        if not isinstance(actual, Mapping):
            raise SelectedExecutionError("retained interruption has no actual Workflow Run")
        return {
            "disposition": "interrupted",
            "status": "interrupted_pending",
            "outcome": "interrupted_pending",
            "workflow_run_id": actual["run_id"],
            "diagnostics": [
                "Retained interruption requires explicit inspection; status does not recover or resume it."
            ],
        }
    return None


def _pending_status(
    root: Path,
    run_id: str,
    frozen: Mapping[str, Any],
    store: IntegratedFrontierStore,
) -> dict[str, Any]:
    frontier = store.load()["frontier"]
    if not isinstance(frontier, Mapping):
        raise SelectedExecutionError("retained Integrated Run has no pending or terminal state")
    tracker = shared_tracker(root, {}, frozen)
    validate(tracker, frozen["request"]["execution"])
    profile = profile_from_frozen(root, frozen)
    methods = _admitted_methods(root, frozen, profile, None)
    capture = load_capture(root, run_id, frontier)
    revalidate_pending(root, frozen, profile, None, methods, frontier, capture)
    return pending_response(root, run_id, frozen, tracker, frontier)


def observe(root: Path, run_id: str) -> dict[str, Any] | None:
    folder = run_directory(root, run_id)
    if not (folder / "selected_request.json").exists():
        return None
    frozen = load_request(root, run_id)
    if not owns(frozen):
        return None
    root = project_root(root)
    if not (folder / CHECKPOINT_NAME).exists():
        return {
            "status": "not_observed",
            "requested_workflow_run_id": run_id,
            "diagnostics": [
                "Frozen request retained without an execution checkpoint; Run start or completion is not established."
            ],
        }
    with IntegratedFrontierStore(root, run_id) as store:
        record, evidence = load_bound_checkpoint(root, frozen)
        result = _retained_status(root, frozen, record, evidence)
        if result is None:
            result = _pending_status(root, run_id, frozen, store)
        if record.recording_errors:
            result["recording_errors"] = list(record.recording_errors)
        return result
