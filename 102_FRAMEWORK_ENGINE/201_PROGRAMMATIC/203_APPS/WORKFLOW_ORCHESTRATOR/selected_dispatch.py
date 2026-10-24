"""Admission-ordered dispatch for frozen selected Workflow requests."""

# implementation of:
# Requirement: CA-R-2117
# Method: CA-M-431, CA-M-405

from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path
from typing import Any, cast

import selected_freeze_state
from selected_dispatch_state import (
    dispatch_admitted_with_failure_boundary,
)
from selected_evidence_io import atomic_write, bounded_read, run_directory
from selected_execution_contracts import (
    ActionHandler,
    LifecycleAdmissionError,
    SelectedExecutionError,
    canonical_json,
)
from selected_graph_admission import validate_lifecycle_admission, validate_query_admission
from selected_run_session import RunSupport
from shared_context_validation_sources import is_direct_integrated_version


def dispatch_confirmed_subject(
    root: Path,
    handlers: Mapping[str, ActionHandler],
    frozen: Mapping[str, Any],
    confirmation: object,
) -> dict[str, Any]:
    """Dispatch only under the trusted host's exact Subject confirmation."""
    from subject_publication_authorization import bind_subject_publication_confirmation

    execution = frozen.get("request", {}).get("execution", {})
    if execution.get("operation_route") != "update_atom" or "subject_patches" not in execution.get(
        "parameters", {}
    ):
        raise SelectedExecutionError("confirmed Subject dispatch requires the exact Subject route")
    with bind_subject_publication_confirmation(confirmation):
        return dispatch(root, handlers, frozen)


def _retained_graph_result(
    root: Path,
    handlers: Mapping[str, ActionHandler],
    frozen: Mapping[str, Any],
    retained: Mapping[str, Any],
    run_id: str,
) -> dict[str, Any]:
    if (
        retained.get("disposition") in {"recording_pending", "started"}
        and isinstance(frozen.get("graph"), Mapping)
        and frozen["graph"].get("route") in {"build_entities_graph", "build_terms_graph"}
    ):
        if canonical_json(selected_freeze_state.load(root, run_id)) != canonical_json(frozen):
            raise SelectedExecutionError(
                "accepted graph inspection differs from its frozen request"
            )
        from selected_graph_reconciliation import reconcile_graph_recording

        return reconcile_graph_recording(root, handlers, frozen)
    return dict(retained)


def _is_current_integrated(frozen: Mapping[str, Any]) -> bool:
    request = frozen.get("request")
    graph = frozen.get("graph")
    if not isinstance(request, Mapping) or not isinstance(graph, Mapping):
        return False
    execution = request.get("execution")
    workflow = graph.get("workflow")
    return (
        isinstance(execution, Mapping)
        and execution.get("operation_route") == "run_implementation_workflow"
        and execution.get("mode") == "execute"
        and isinstance(workflow, Mapping)
        and workflow.get("atom_id") == "CA-O-016"
        and is_direct_integrated_version(workflow.get("version"))
    )


# implementation of:
# Requirement: CA-R-2117
# Method: CA-M-431, CA-M-405
def dispatch_current_integrated(
    root: Path, handlers: Mapping[str, ActionHandler], frozen: Mapping[str, Any]
) -> dict[str, Any]:
    """Use the retained Integrated frontier before legacy dispatch interruption."""
    graph = frozen.get("graph")
    if not isinstance(graph, Mapping) or graph.get("entry_step") != "CA-O-231":
        raise SelectedExecutionError("current Integrated O016 graph must enter at CA-O-231")
    from selected_integrated_dispatch_admission import validate
    from selected_integrated_dispatch import dispatch_integrated
    from selected_run_session import shared_tracker
    from shared_context_validation_loader import load_frozen_methods

    tracker = shared_tracker(root, handlers, frozen)
    request = frozen.get("request")
    execution = request.get("execution") if isinstance(request, Mapping) else None
    if not isinstance(execution, Mapping):
        raise SelectedExecutionError("frozen Integrated request has no execution")
    validate(tracker, execution)
    return dispatch_integrated(
        root,
        frozen,
        tracker=tracker,
        trusted_methods=load_frozen_methods(root, frozen),
    )


def dispatch(
    root: Path,
    handlers: Mapping[str, ActionHandler],
    frozen: Mapping[str, Any],
    *,
    run_support: RunSupport | None = None,
) -> dict[str, Any]:
    """Revalidate, intent-record, and dispatch one frozen selected request."""
    request = frozen.get("request") if isinstance(frozen, Mapping) else None
    if not isinstance(request, Mapping) or not isinstance(request.get("run_id"), str):
        raise SelectedExecutionError("saved selected request is invalid")
    run_id = request["run_id"]
    if _is_current_integrated(frozen):
        return dispatch_current_integrated(root, handlers, frozen)
    folder = run_directory(root, run_id)
    accepted = folder / "accepted.json"
    if accepted.exists():
        retained = bounded_read(accepted)["result"]
        if isinstance(retained, Mapping):
            return _retained_graph_result(root, handlers, frozen, retained, run_id)
        return cast(dict[str, Any], retained)
    intent = folder / "dispatch-intent.json"
    if intent.exists():
        return {
            "disposition": "recording_pending",
            "outcome": "interrupted_pending",
            "workflow_run_id": run_id,
            "reason": "uncertain selected dispatch intent retained; no replay",
        }
    graph = selected_freeze_state.revalidate(root, frozen)
    execution = request["execution"]
    if not isinstance(execution, Mapping):
        raise SelectedExecutionError("saved selected execution is invalid")
    validate_query_admission(graph, execution)
    try:
        validate_lifecycle_admission(
            root,
            graph,
            execution,
            expected_admission=frozen.get("lifecycle_admission"),
        )
    except LifecycleAdmissionError as error:
        return {
            "disposition": "blocked",
            "outcome": "blocked",
            "workflow_run_id": run_id,
            "effect_refs": [],
            "lifecycle_error": error.record(),
            "diagnostics": [str(error)],
        }
    atomic_write(
        intent,
        {"run_id": run_id, "state": "dispatching", "graph": frozen["graph"]},
    )
    return dispatch_admitted_with_failure_boundary(
        root,
        handlers,
        frozen,
        request,
        run_id,
        folder,
        accepted,
        intent,
        run_support,
    )
