# CA-M-504@2
"""Admission-ordered dispatch for frozen selected Workflow requests."""


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
    execution = request.get("execution")
    if isinstance(execution, Mapping) and execution.get("operation_route") == "run_implementation_workflow":
        raise SelectedExecutionError("Unsupported: AI Agent implementation execution has been removed")
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
