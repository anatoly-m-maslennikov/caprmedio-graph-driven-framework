"""Executor-bound graph and Journal query inputs for selected Workflows."""

from __future__ import annotations

from collections.abc import Mapping
import importlib
from pathlib import Path
from typing import TYPE_CHECKING, Callable, Protocol, cast

from selected_execution_contracts import SelectedExecutionError

if TYPE_CHECKING:
    from query_actions import JournalPreparation


class GraphSession(Protocol):
    """Minimum executor-owned Session state needed by graph binding."""

    actual: Mapping[object, object]


def _actual_run_index(session: GraphSession) -> dict[str, Mapping[str, object]]:
    actual = getattr(session, "actual", {})
    if not isinstance(actual, Mapping):
        return {}
    by_id: dict[str, Mapping[str, object]] = {}
    for run in actual.values():
        if not isinstance(run, Mapping):
            continue
        run_id = run.get("run_id")
        if isinstance(run_id, str):
            by_id[run_id] = run
    return by_id


def _graph_recording_context(
    session: GraphSession,
    workflow_run_id: str,
    step_run_id: str,
    action_run_id: str,
    action: Mapping[str, object],
) -> object | None:
    try:
        graph_module = importlib.import_module("generate_entity_graph")
    except ImportError:
        return None
    session_request = getattr(session, "request", None)
    execution_authorization = (
        session_request.get("operator_authorization")
        if isinstance(session_request, Mapping)
        else None
    )
    if not isinstance(execution_authorization, Mapping):
        execution_authorization = None
    recording_factory = cast(
        Callable[..., object],
        getattr(graph_module, "actual_run_recording_context", None),
    )
    graph_error = cast(type[Exception], getattr(graph_module, "EntityGraphError", None))
    if not callable(recording_factory) or not isinstance(graph_error, type):
        return None
    try:
        return recording_factory(
            workflow_run_id,
            step_run_id,
            action_run_id,
            action,
            execution_authorization=execution_authorization,
        )
    except graph_error:
        return None


def graph_parameters_with_actual_recording(
    parameters: object,
    session: GraphSession,
    *,
    workflow_run_id: str,
    step_run_id: str,
    action_run_id: str,
) -> object:
    """Bind graph publication to the Session's actual Action and parents.

    The context is executor-owned; caller JSON cannot claim an actual Run.
    """
    if not isinstance(parameters, Mapping):
        return parameters
    by_id = _actual_run_index(session)
    action = by_id.get(action_run_id)
    step = by_id.get(step_run_id)
    workflow = by_id.get(workflow_run_id)
    if (
        not isinstance(action, Mapping)
        or not isinstance(step, Mapping)
        or not isinstance(workflow, Mapping)
        or action.get("parent_run_id") != step_run_id
        or step.get("parent_run_id") != workflow_run_id
    ):
        return parameters
    recording = _graph_recording_context(
        session,
        workflow_run_id,
        step_run_id,
        action_run_id,
        action,
    )
    if recording is None:
        # Leave the caller shape intact; the graph Tool reports the stable
        # recording-context blocker without an effect.
        return parameters
    return {**parameters, "run_recording_context": recording}


def prepare_journal_query_before_run(
    root: Path,
    graph: Mapping[str, object],
    execution: Mapping[str, object],
) -> JournalPreparation | None:
    """Seal CA-O-163's Journal source before any Run evidence exists."""
    if graph.get("route") != "find_and_fetch_journal_events":
        return None
    try:
        import query_actions
    except ImportError as error:
        raise SelectedExecutionError("Journal query adapter is unavailable") from error
    steps = graph.get("steps")
    if not isinstance(steps, list) or len(steps) != 1 or not isinstance(steps[0], Mapping):
        raise SelectedExecutionError("Journal query route must retain exactly one source Step")
    step = steps[0]
    actions = step.get("actions")
    if step.get("atom_id") != "CA-O-163" or not isinstance(actions, list) or len(actions) != 1:
        raise SelectedExecutionError("Journal query route must retain CA-O-163 and one Action")
    action = actions[0]
    if not isinstance(action, Mapping) or action.get("atom_id") != "CA-O-162":
        raise SelectedExecutionError("Journal query route must retain CA-O-162")
    workflow = cast(Mapping[str, object], graph["workflow"])
    context = {
        "route": graph["route"],
        "workflow_definition_id": workflow["atom_id"],
        "step_definition_id": step["atom_id"],
        "action_definition_id": action["atom_id"],
        "parameters": execution.get("parameters"),
    }
    try:
        return query_actions.prepare_journal_query(root, context)
    except query_actions.QueryActionError as error:
        raise SelectedExecutionError(str(error)) from error


__all__ = [
    "GraphSession",
    "graph_parameters_with_actual_recording",
    "prepare_journal_query_before_run",
]
