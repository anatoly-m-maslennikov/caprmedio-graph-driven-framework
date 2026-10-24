"""One locked, source-bound continuation advance for an Integrated Action."""

# implementation of:
# Requirement: CA-R-1522, CA-R-1524
# Method: CA-M-405, CA-M-410

from __future__ import annotations

from collections.abc import Mapping
from copy import deepcopy
from pathlib import Path
from typing import Any

from selected_execution_contracts import ActionHandler, SelectedExecutionError
from selected_graph_executor import execute_graph
from selected_integrated_action import IntegratedActionPending
from selected_integrated_dispatch import _admitted_methods
from selected_integrated_dispatch_admission import validate
from selected_integrated_dispatch_capture import load_capture
from selected_integrated_dispatch_handler import action_handler
from selected_integrated_dispatch_pending import revalidate_pending
from selected_integrated_dispatch_profile import profile_from_frozen
from selected_integrated_frontier import IntegratedFrontierStore
from selected_integrated_resume_handler import replace_handler
from selected_integrated_resume_pending import pending_response, publish_pending
from selected_integrated_resume_recovery import accepted_result
from selected_integrated_resume_submission import continuation_id, sealed_submission
from selected_integrated_session import restore_checkpoint
from selected_freeze_state import revalidate, validate_requested_runs
from shared_context_validation_sources import CURRENT_ACTIONS


def _request(frozen: Mapping[str, Any]) -> tuple[str, Mapping[str, Any]]:
    request = frozen.get("request")
    execution = request.get("execution") if isinstance(request, Mapping) else None
    run_id = request.get("run_id") if isinstance(request, Mapping) else None
    if not isinstance(run_id, str) or not isinstance(execution, Mapping):
        raise SelectedExecutionError("frozen Integrated request is invalid")
    return run_id, execution


def _admission(
    root: Path, frozen: Mapping[str, Any], tracker: Any
) -> tuple[Mapping[str, Any], Mapping[str, Any], str]:
    run_id, execution = _request(frozen)
    graph = revalidate(root, frozen)
    validate_requested_runs(root, execution, graph, run_id)
    validate(tracker, execution)
    return execution, profile_from_frozen(root, frozen), run_id


def _handlers(
    root: Path,
    run_id: str,
    session: Any,
    profile: Mapping[str, Any],
    method_projection: object | None,
    methods: object | None,
    action: Any,
) -> dict[str, ActionHandler]:
    return {
        action_id: action_handler(
            root, run_id, session, profile, method_projection, methods, action
        )
        for action_id in CURRENT_ACTIONS.values()
    }


def _advance(
    store: IntegratedFrontierStore,
    frozen: Mapping[str, Any],
    tracker: Any,
    profile: Mapping[str, Any],
    capture: Mapping[str, Any],
    accepted: Mapping[str, Any],
    method_projection: object | None,
    methods: object | None,
    action: Any,
) -> dict[str, Any]:
    run_id, _execution = _request(frozen)
    session = restore_checkpoint(store.root, frozen, tracker)
    handlers = _handlers(store.root, run_id, session, profile, method_projection, methods, action)
    resumed = replace_handler(str(capture["action_id"]), handlers, capture, accepted)
    try:
        result = execute_graph(store.root, resumed, frozen, session, recovery=True)
    except IntegratedActionPending as pending:
        return publish_pending(
            store,
            frozen,
            tracker,
            session,
            profile,
            method_projection,
            methods,
            pending.capture,
        )
    session.save()
    return {"disposition": "terminal", "status": result["outcome"], "graph_result": result}


def _resume_locked(
    store: IntegratedFrontierStore,
    frozen: Mapping[str, Any],
    submission: object,
    tracker: Any,
    method_projection: object | None,
    methods: object | None,
    action: Any,
) -> dict[str, Any]:
    _execution, profile, run_id = _admission(store.root, frozen, tracker)
    admitted_methods = _admitted_methods(store.root, frozen, profile, methods)
    continuation = continuation_id(submission)
    record = store.record(continuation)
    frontier = record.get("frontier")
    if not isinstance(frontier, Mapping):
        raise SelectedExecutionError("retained Integrated continuation has no frontier")
    capture = load_capture(store.root, run_id, frontier)
    revalidate_pending(
        store.root, frozen, profile, method_projection, admitted_methods, frontier, capture
    )
    sealed = sealed_submission(submission, capture)
    receipt = store.admit(sealed)
    response = receipt.get("response")
    if isinstance(response, Mapping):
        return deepcopy(dict(response))
    successor = store.load()["frontier"]
    if isinstance(successor, Mapping) and successor != frontier:
        capture = load_capture(store.root, run_id, successor)
        revalidate_pending(
            store.root, frozen, profile, method_projection, admitted_methods, successor, capture
        )
        response = pending_response(store.root, run_id, frozen, tracker, successor)
    else:
        accepted = accepted_result(store.root, frozen, tracker, capture, sealed, record, action)
        response = _advance(
            store,
            frozen,
            tracker,
            profile,
            capture,
            accepted,
            method_projection,
            admitted_methods,
            action,
        )
    store.complete_receipt(continuation, response)
    return response


def resume_integrated(
    root: Path,
    frozen: Mapping[str, Any],
    submission: object,
    *,
    tracker: Any,
    trusted_method_projection: object | None = None,
    trusted_methods: object | None = None,
    action: Any = None,
) -> dict[str, Any]:
    """Submit one retained result and advance to the next frontier or terminal."""
    run_id, _execution = _request(frozen)
    with IntegratedFrontierStore(root, run_id) as store:
        return _resume_locked(
            store,
            frozen,
            submission,
            tracker,
            trusted_method_projection,
            trusted_methods,
            action,
        )


__all__ = ["resume_integrated"]
