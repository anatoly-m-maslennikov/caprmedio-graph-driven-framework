"""Public APP boundary for the current, session-controlled implementation loop."""

# implementation of:
# Requirement: CA-R-1522, CA-R-2117
# Method: CA-M-405, CA-M-410, CA-M-431

from __future__ import annotations

from collections.abc import Mapping
import json
from pathlib import Path
from typing import Any

from contracts import EnqueueSelected, Status, SubmitResult
from selected_evidence_io import bounded_bytes, run_directory, safe_path
from selected_execution_contracts import SelectedExecutionError
from selected_freeze_state import _validated_freeze, freeze
from selected_integrated_dispatch import dispatch_integrated
from selected_integrated_dispatch_admission import validate
from selected_integrated_frontier_records import project_root
from selected_integrated_resume import resume_integrated
from selected_run_session import shared_tracker
from shared_context_validation_loader import load_frozen_methods
from shared_context_validation_sources import is_direct_integrated_version


def owns(frozen: Mapping[str, Any]) -> bool:
    graph = frozen.get("graph")
    if not isinstance(graph, Mapping):
        return False
    workflow = graph.get("workflow")
    current = (
        graph.get("route") == "run_implementation_workflow"
        and isinstance(workflow, Mapping)
        and workflow.get("atom_id") == "CA-O-016"
        and is_direct_integrated_version(workflow.get("version"))
    )
    if current and graph.get("entry_step") != "CA-O-231":
        raise SelectedExecutionError("current Integrated Workflow entry must be CA-O-231")
    return current


def load_request(root: Path, run_id: str) -> dict[str, Any]:
    path = run_directory(root, run_id) / "selected_request.json"
    value = json.loads(
        bounded_bytes(safe_path(root, path.relative_to(root).as_posix()), 8 * 1024 * 1024)
    )
    request = value.get("request") if isinstance(value, dict) else None
    if (
        not isinstance(value, dict)
        or not isinstance(request, Mapping)
        or request.get("run_id") != run_id
    ):
        raise SelectedExecutionError("retained Integrated request identity differs")
    return value


def _execute(root: Path, request: EnqueueSelected) -> dict[str, Any] | None:
    if request.execution.get("operation_route") != "run_implementation_workflow":
        return None
    if request.execution.get("mode") != "execute":
        return None
    candidate = _validated_freeze(root, request.model_dump())
    if not owns(candidate):
        return None
    root = project_root(root)
    tracker = shared_tracker(root, {}, candidate)
    validate(tracker, candidate["request"]["execution"])
    methods = load_frozen_methods(root, candidate)
    frozen = freeze(root, request.model_dump())
    return dispatch_integrated(root, frozen, tracker=tracker, trusted_methods=methods)


def _resume(root: Path, request: SubmitResult) -> dict[str, Any]:
    root = project_root(root)
    frozen = load_request(root, request.run_id)
    if not owns(frozen):
        raise SelectedExecutionError("submit_result requires the current Integrated Workflow")
    tracker = shared_tracker(root, {}, frozen)
    validate(tracker, frozen["request"]["execution"])
    methods = load_frozen_methods(root, frozen)
    return resume_integrated(
        root,
        frozen,
        request.model_dump(exclude={"operation", "run_id"}),
        tracker=tracker,
        trusted_methods=methods,
    )


def run(root: Path, request: object) -> tuple[bool, Any]:
    root = Path(root).resolve(strict=True)
    if isinstance(request, SubmitResult):
        return True, _resume(root, request)
    if isinstance(request, EnqueueSelected):
        result = _execute(root, request)
        return result is not None, result
    if isinstance(request, Status):
        from selected_integrated_observation import observe

        result = observe(root, request.run_id)
        return result is not None, result
    return False, None
