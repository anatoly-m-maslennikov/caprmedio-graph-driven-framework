from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path
from typing import Any

import selected_freeze_state
import selected_execution_run_plan
from graph_completion import finalize_graph_result
from selected_evidence_io import atomic_write, bounded_read, run_directory
from selected_execution_contracts import ActionHandler, SelectedExecutionError, canonical_json
from selected_graph_terminal import confirmed as confirmed_graph_terminal
from selected_graph_readback import (
    read_aggregate as _read_aggregate_impl,
    read_progress as _read_progress_impl,
    reconcile_outputs,
)
from selected_run_recovery import read_selected_run_evidence
from selected_run_session import shared_tracker
from workflow_run_support import LazyRunTracker, RunExecutionSession, _proposal, _validate_common


def _request_and_graph(
    root: Path, frozen: Mapping[str, Any]
) -> tuple[dict[str, Any], dict[str, Any]]:
    request = frozen.get("request")
    if not isinstance(request, Mapping) or not isinstance(request.get("run_id"), str):
        raise SelectedExecutionError("saved graph request is invalid")
    run_id = request["run_id"]
    if canonical_json(selected_freeze_state.load(root, run_id)) != canonical_json(frozen):
        raise SelectedExecutionError(
            "graph recording observation differs from its saved frozen request"
        )
    graph = selected_freeze_state.revalidate(root, frozen)
    if graph.get("route") not in {"build_entities_graph", "build_terms_graph"}:
        raise SelectedExecutionError("graph reconciliation is outside its selected routes")
    steps = graph.get("steps")
    if (
        not isinstance(steps, list)
        or len(steps) != 1
        or not isinstance(steps[0], Mapping)
        or not isinstance(steps[0].get("actions"), list)
        or len(steps[0]["actions"]) != 1
    ):
        raise SelectedExecutionError(
            "graph reconciliation requires its exact single Action frontier"
        )
    return dict(request), graph


def _read_progress(
    root: Path,
    folder: Path,
    requested_action: str,
    session: Any,
) -> tuple[dict[str, Any], Path, str, list[str], str]:
    return _read_progress_impl(root, folder, requested_action, session)


def _read_aggregate(
    root: Path,
    folder: Path,
    graph: Mapping[str, Any],
    session: Any,
    run_id: str,
    requested_step: str,
    requested_action: str,
    effect_refs: list[str],
) -> tuple[dict[str, Any], Path, str, Mapping[str, Any]]:
    return _read_aggregate_impl(
        root, folder, graph, session, run_id, requested_step, requested_action, effect_refs
    )


def _restore_session(
    root: Path,
    handlers: Mapping[str, ActionHandler],
    frozen: Mapping[str, Any],
    request: Mapping[str, Any],
) -> tuple[dict[str, Any], Any, Any, str, str]:
    execution = _validate_common(request["execution"])
    tracker = shared_tracker(root, handlers, frozen)
    evidence = read_selected_run_evidence(root, execution)
    session = RunExecutionSession.restore(tracker, execution, evidence["events"])
    run_id = request["run_id"]
    requested_step = selected_execution_run_plan.requested_step_id(run_id, 1, 1)
    requested_action = f"{requested_step}:action:1"
    if any(
        identity not in session.actual for identity in (run_id, requested_step, requested_action)
    ):
        raise SelectedExecutionError(
            "graph reconciliation lacks its actual construction Run frontier"
        )
    return execution, tracker, session, requested_step, requested_action


def reconcile_graph_recording(
    root: Path,
    handlers: Mapping[str, ActionHandler],
    frozen: Mapping[str, Any],
    *,
    persist: bool = True,
) -> dict[str, Any]:
    root = Path(root).resolve(strict=True)
    request, graph = _request_and_graph(root, frozen)
    run_id = request["run_id"]
    execution, tracker, session, requested_step, requested_action = _restore_session(
        root, handlers, frozen, request
    )
    folder = run_directory(root, run_id)
    progress, progress_path, progress_ref, effect_refs, expected_outcome = _read_progress(
        root, folder, requested_action, session
    )
    aggregate, aggregate_path, aggregate_ref, row = _read_aggregate(
        root, folder, graph, session, run_id, requested_step, requested_action, effect_refs
    )
    accepted_path = folder / "accepted.json"
    previous = bounded_read(accepted_path).get("result") if accepted_path.exists() else {}
    if not isinstance(previous, Mapping):
        raise SelectedExecutionError("saved graph dispatch result is invalid")
    if not isinstance(progress.get("native_result"), Mapping) or not isinstance(
        progress["native_result"].get("completion"), Mapping
    ):
        raise SelectedExecutionError("saved graph completion evidence is invalid")
    terminal = session.terminal.get(requested_action) or session.interrupted.get(requested_action)
    finalized = finalize_graph_result(
        progress["graph_construction_observation"],
        terminal,
        action_run_id=progress["action_run_id"],
        result_ref=progress_ref,
        effect_refs=effect_refs,
    )
    action = graph["steps"][0]["actions"][0]
    result_map = action.get("result_map", {})
    result_label = result_map.get(finalized["outcome"], finalized["outcome"])
    updated_progress, updated_aggregate = reconcile_outputs(
        progress,
        aggregate,
        row,
        finalized,
        result_label,
        session,
        requested_step,
        run_id,
        aggregate_ref,
        effect_refs,
        expected_outcome,
        confirmed_graph_terminal,
    )
    if persist and canonical_json(updated_progress) != canonical_json(progress):
        atomic_write(progress_path, updated_progress)
    if persist and canonical_json(updated_aggregate) != canonical_json(aggregate):
        atomic_write(aggregate_path, updated_aggregate)
    proposal = _proposal(request["execution"], tracker._observe(request["execution"]))
    result = LazyRunTracker._session_result(tracker, request["execution"], proposal, session)
    if run_id not in session.terminal and result["disposition"] == "terminal":
        result["disposition"] = "started"
        result["retry_disposition"] = "inspect-or-recover-only"
    if persist and accepted_path.exists() and canonical_json(previous) != canonical_json(result):
        atomic_write(accepted_path, {"result": result})
    return result
