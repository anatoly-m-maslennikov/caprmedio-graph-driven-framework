"""Initial, source-bound dispatch for the current Integrated O016 graph."""

from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path
from typing import Any

from selected_evidence_io import run_directory
from selected_execution_contracts import SelectedExecutionError
from selected_graph_executor import execute_graph
from selected_integrated_action import IntegratedActionInputError, IntegratedActionPending
from selected_integrated_dispatch_capture import load_capture, save_capture
from selected_integrated_dispatch_admission import register, validate
from selected_integrated_dispatch_handler import action_handler, actual_run_ids
from selected_integrated_dispatch_pending import revalidate_pending
from selected_integrated_dispatch_profile import profile_from_frozen
from selected_integrated_frontier import IntegratedFrontierStore
from selected_integrated_frontier_records import digest
from selected_integrated_session_record import CHECKPOINT_NAME
from selected_integrated_session import (
    create_checkpoint,
    restore_checkpoint,
)
from selected_freeze_state import revalidate, validate_requested_runs
from shared_context_validation_loader import FrozenMethodLoaderError, load_frozen_methods
from shared_context_validation_sources import CURRENT_ACTIONS, is_direct_integrated_version


def _request(frozen: Mapping[str, Any]) -> tuple[str, Mapping[str, Any], str]:
    request = frozen.get("request")
    if not isinstance(request, Mapping):
        raise SelectedExecutionError("frozen Integrated request is invalid")
    run_id, execution = request.get("run_id"), request.get("execution")
    request_id = execution.get("request_id") if isinstance(execution, Mapping) else None
    if (
        not isinstance(run_id, str)
        or not isinstance(execution, Mapping)
        or not isinstance(request_id, str)
        or not request_id
    ):
        raise SelectedExecutionError("Integrated dispatch requires a sealed request identity")
    return run_id, execution, request_id


def _admitted_methods(
    root: Path,
    frozen: Mapping[str, Any],
    profile: Mapping[str, Any],
    methods: object | None,
) -> object | None:
    workflow = profile.get("workflow")
    if not isinstance(workflow, Mapping) or not is_direct_integrated_version(workflow.get("version")):
        return methods
    try:
        frozen_methods = list(load_frozen_methods(root, frozen))
    except FrozenMethodLoaderError as error:
        raise SelectedExecutionError(str(error)) from error
    if methods is not None and digest(frozen_methods) != digest(methods):
        raise SelectedExecutionError("trusted direct Methods differ from the frozen request")
    return frozen_methods


def frontier_for_capture(
    root: Path,
    run_id: str,
    frozen: Mapping[str, Any],
    profile: Mapping[str, Any],
    capture: Mapping[str, Any],
) -> dict[str, Any]:
    definitions = capture["definitions"]
    packet = capture["packet"]
    step_id, action_id = str(capture["step_id"]), str(capture["action_id"])
    row = profile["steps"][step_id]
    sources = {
        "profile": definitions["trusted_workflow_binding"],
        "method_projection": definitions.get("trusted_method_projection"),
        "methods": definitions.get("trusted_methods"),
    }
    authorization = definitions.get("trusted_execution_authorization")
    digests = {
        "request": digest(frozen["request"]),
        "source": digest(sources),
        "packet": digest(packet),
        "candidate": digest(packet.get("candidate")),
        "authorization": digest(authorization),
    }
    continuation = digest(
        {
            "run": run_id,
            "step": step_id,
            "action": action_id,
            "visit": digest(capture["run_binding"]),
            **digests,
        }
    )
    return {
        "continuation_id": continuation,
        "project": {"root": root.as_posix(), "digest": digest(root.as_posix())},
        "run": {"id": run_id, "digest": digest(run_id)},
        "step": {"id": step_id, "digest": row["step"]["sha256"]},
        "action": {"id": action_id, "digest": row["action"]["sha256"]},
        "request_digest": digests["request"],
        "source_digest": digests["source"],
        "packet_digest": digests["packet"],
        "candidate_digest": digests["candidate"],
        "authorization_digest": digests["authorization"],
    }


_frontier = frontier_for_capture


def _pending_response(
    session: Any, run_id: str, capture: Mapping[str, Any], frontier: Mapping[str, Any]
) -> dict[str, Any]:
    continuation = frontier.get("continuation_id")
    if not isinstance(continuation, str):
        raise SelectedExecutionError("retained Integrated frontier has no continuation identity")
    return {
        "disposition": "started",
        "status": "pending_action",
        "capture": capture,
        "continuation_id": continuation,
        **actual_run_ids(session, run_id, capture),
    }


def dispatch_integrated(
    root: Path,
    frozen: Mapping[str, Any],
    *,
    tracker: Any,
    trusted_method_projection: object | None = None,
    trusted_methods: object | None = None,
    action: Any = None,
) -> dict[str, Any]:
    """Start one current Integrated Action or return its retained pending frontier."""
    run_id, execution, _request_id = _request(frozen)
    with IntegratedFrontierStore(root, run_id) as store:
        graph = revalidate(store.root, frozen)
        validate_requested_runs(store.root, execution, graph, run_id)
        parsed = validate(tracker, execution)
        profile = profile_from_frozen(store.root, frozen)
        admitted_methods = _admitted_methods(store.root, frozen, profile, trusted_methods)
        retained = store.load()["frontier"]
        if isinstance(retained, Mapping):
            capture = load_capture(store.root, run_id, retained)
            revalidate_pending(
                store.root,
                frozen,
                profile,
                trusted_method_projection,
                admitted_methods,
                retained,
                capture,
            )
            return _pending_response(
                restore_checkpoint(store.root, frozen, tracker), run_id, capture, retained
            )
        register(store.root, tracker, parsed)
        checkpoint = run_directory(store.root, run_id) / CHECKPOINT_NAME
        session = (
            restore_checkpoint(store.root, frozen, tracker)
            if checkpoint.exists()
            else create_checkpoint(store.root, frozen, tracker)
        )
        handlers = {
            action_id: action_handler(
                store.root,
                run_id,
                session,
                profile,
                trusted_method_projection,
                admitted_methods,
                action,
            )
            for action_id in CURRENT_ACTIONS.values()
        }
        try:
            execute_graph(store.root, handlers, frozen, session)
        except IntegratedActionPending as pending:
            session.save()
            capture = pending.capture
            frontier = frontier_for_capture(store.root, run_id, frozen, profile, capture)
            save_capture(store.root, run_id, frontier, capture)
            store.save(frontier)
            return _pending_response(session, run_id, capture, frontier)
        except IntegratedActionInputError as error:
            validation = error.validation
            result = (
                validation.as_result()
                if hasattr(validation, "as_result")
                else {"status": "invalid_packet"}
            )
            return {"disposition": "blocked", **result}
    raise SelectedExecutionError("Integrated dispatch completed without a pending Action")
