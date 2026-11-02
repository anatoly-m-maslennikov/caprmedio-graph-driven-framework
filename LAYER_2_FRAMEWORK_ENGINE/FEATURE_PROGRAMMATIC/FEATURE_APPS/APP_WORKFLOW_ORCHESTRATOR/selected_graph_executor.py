from collections.abc import Mapping
from pathlib import Path
from typing import Any

from selected_evidence_io import atomic_write, run_directory
from selected_execution_contracts import ActionHandler, SelectedExecutionError
from selected_execution_run_plan import (
    declared_run_visit_limits,
    requested_step_id,
    run_visit_limits_for,
)
from selected_graph_inputs import prepare_journal_query_before_run
from selected_graph_terminal import (
    finish_graph_terminal,
    terminal_transition,
    transition,
)
from selected_graph_traversal import dispatch_step_actions
from selected_run_completion import finish_selected_run


def _finish_nonterminal_step(
    root: Path,
    session: Any,
    run_id: str,
    requested_step: str,
    step_run_id: str,
    final_result: str | None,
    results: list[dict[str, Any]],
    step_effect_refs: list[str],
    edge: Mapping[str, Any],
    *,
    recovery: bool,
) -> str:
    step_result_path = run_directory(root, run_id) / f"{requested_step}.json"
    atomic_write(
        step_result_path,
        {"result": final_result, "step_run_id": step_run_id, "action_results": results},
    )
    finish_selected_run(
        session,
        requested_step,
        step_run_id,
        recovery=recovery,
        outcome="completed",
        result_ref=step_result_path.relative_to(root).as_posix(),
        effect_refs=step_effect_refs,
    )
    next_step = edge.get("next")
    if not isinstance(next_step, str):
        raise SelectedExecutionError("selected transition target is invalid")
    return next_step


def _step_transition(
    step: Mapping[str, Any], final_result: object, output: Mapping[str, Any]
) -> Mapping[str, Any]:
    try:
        return transition(step, final_result if isinstance(final_result, str) else "")
    except SelectedExecutionError:
        fallback = output.get("terminal_outcome")
        if not isinstance(fallback, str):
            raise
        return {"terminal": fallback}


def _traverse_graph(
    root: Path,
    handlers: Mapping[str, ActionHandler],
    frozen: Mapping[str, Any],
    session: Any,
    *,
    recovery: bool,
) -> dict[str, Any]:
    graph = frozen["graph"]
    request = frozen["request"]
    run_id = request["run_id"]
    actual = getattr(session, "actual", {})
    restored_action_ids = (
        frozenset(actual) if recovery and isinstance(actual, Mapping) else frozenset()
    )
    steps = {row["atom_id"]: row for row in graph["steps"]}
    ordinals = {row["atom_id"]: ordinal for ordinal, row in enumerate(graph["steps"], 1)}
    visit_limits = run_visit_limits_for(graph, declared_run_visit_limits(request["execution"]))
    visit_counts: dict[str, int] = {}
    next_step = graph["entry_step"]
    journal = prepare_journal_query_before_run(root, graph, request["execution"])
    workflow_actual = session.start_run(run_id)
    workflow_run_id = workflow_actual["run_id"]
    results: list[dict[str, Any]] = []
    implementation_prior_results: list[dict[str, Any]] = []
    structural_prior_results: list[dict[str, Any]] = []
    lifecycle_prior_results: list[dict[str, Any]] = []
    while next_step:
        step = steps.get(next_step)
        if step is None:
            raise SelectedExecutionError("On Result transition references an unbound Step")
        visit = visit_counts.get(next_step, 0) + 1
        if visit > visit_limits[next_step]:
            raise SelectedExecutionError(
                "selected Workflow exhausted the caller-declared Step visit limit before Action dispatch"
            )
        visit_counts[next_step] = visit
        requested_step = requested_step_id(run_id, ordinals[next_step], visit)
        step_actual = session.start_run(requested_step)
        step_run_id = step_actual["run_id"]
        dispatched = dispatch_step_actions(
            root,
            handlers,
            frozen,
            session,
            graph,
            step,
            requested_step,
            step_run_id,
            workflow_run_id,
            implementation_prior_results,
            structural_prior_results,
            lifecycle_prior_results,
            journal,
            recovery,
            restored_action_ids,
            results,
        )
        final_result = dispatched["final_result"]
        output = dispatched["output"]
        step_effect_refs = dispatched["step_effect_refs"]
        edge = _step_transition(step, final_result, output)
        if "terminal" in edge:
            terminal = terminal_transition(edge["terminal"])
            return finish_graph_terminal(
                root,
                session,
                graph,
                request,
                results,
                requested_step,
                step_run_id,
                workflow_run_id,
                step_effect_refs,
                terminal,
                recovery=recovery,
            )
        next_step = _finish_nonterminal_step(
            root,
            session,
            run_id,
            requested_step,
            step_run_id,
            final_result,
            results,
            step_effect_refs,
            edge,
            recovery=recovery,
        )
    raise SelectedExecutionError("selected Workflow has no terminal result")


def execute_graph(
    root: Path,
    handlers: Mapping[str, ActionHandler],
    frozen: Mapping[str, Any],
    session: Any,
    *,
    recovery: bool = False,
) -> dict[str, Any]:
    """Execute a frozen selected graph through traversal and action helpers."""
    return _traverse_graph(root, handlers, frozen, session, recovery=recovery)
