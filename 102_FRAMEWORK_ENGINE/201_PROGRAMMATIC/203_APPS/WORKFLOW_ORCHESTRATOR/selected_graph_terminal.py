from collections.abc import Callable, Mapping
from pathlib import Path
from typing import Any, cast

from selected_evidence_io import atomic_write, run_directory
from selected_execution_contracts import SelectedExecutionError
from selected_run_completion import finish_selected_run

VALID_TERMINAL_OUTCOMES = frozenset(
    {"completed", "no_op", "failed", "cancelled", "partial", "interrupted_pending"}
)


def result_writer(root: Path, path: Path, owner: str) -> Callable[[Mapping[str, Any]], str]:
    def write(payload: Mapping[str, Any]) -> str:
        if not isinstance(payload, Mapping):
            raise SelectedExecutionError(f"{owner} result writer requires an evidence mapping")
        atomic_write(path, dict(payload))
        return path.relative_to(root).as_posix()

    return write


def add_progress_fields(progress: dict[str, Any], output: Mapping[str, Any]) -> None:
    for key in ("recording_error", "lifecycle_prior", "lifecycle_recording"):
        if output.get(key) is not None:
            progress[key] = output[key]


def transition(step: Mapping[str, Any], result: str) -> Mapping[str, Any]:
    for candidate in step["on_result"]:
        condition = candidate.get("result", candidate.get("when"))
        if condition in (result, "*") and ("next" in candidate or "terminal" in candidate):
            return cast(Mapping[str, Any], candidate)
    raise SelectedExecutionError("no declared On Result transition admits Action result")


def terminal_transition(value: object) -> str:
    if not isinstance(value, str):
        raise SelectedExecutionError("selected terminal result is invalid")
    if value not in VALID_TERMINAL_OUTCOMES:
        raise SelectedExecutionError("selected terminal result is not a truthful Run outcome")
    return value


def confirmed(
    terminal: object,
    run_id: str,
    outcome: str,
    result_ref: str,
    effect_refs: list[str],
) -> bool:
    if not isinstance(terminal, Mapping):
        return False
    return (
        terminal.get("disposition") == "terminal"
        and terminal.get("run_id") == run_id
        and terminal.get("outcome") == outcome
        and terminal.get("result_ref") == result_ref
        and terminal.get("effect_refs") == effect_refs
    )


def completed_receipt(
    receipt: object,
    *,
    result_ref: str,
    effect_refs: list[str],
) -> bool:
    return (
        isinstance(receipt, Mapping)
        and receipt.get("disposition") == "terminal"
        and receipt.get("outcome") == "completed"
        and receipt.get("result_ref") == result_ref
        and receipt.get("effect_refs") == effect_refs
    )


def finish_graph_terminal(
    root: Path,
    session: Any,
    graph: Mapping[str, Any],
    request: Mapping[str, Any],
    results: list[dict[str, Any]],
    requested_step: str,
    step_run_id: str,
    workflow_run_id: str,
    step_effect_refs: list[str],
    terminal: str,
    *,
    recovery: bool,
) -> dict[str, Any]:
    run_id = request["run_id"]
    result_path = run_directory(root, run_id) / "graph_result.json"
    projection = graph.get("route") in {"build_entities_graph", "build_terms_graph"}
    output: dict[str, Any] = {
        "outcome": "interrupted_pending" if projection else terminal,
        "workflow_run_id": workflow_run_id,
        "workflow_definition_id": graph["workflow"]["atom_id"],
        "step_results": results,
    }
    atomic_write(result_path, output)
    result_ref = result_path.relative_to(root).as_posix()
    effect_refs = sorted({reference for row in results for reference in row["effect_refs"]})
    step_terminal = finish_selected_run(
        session,
        requested_step,
        step_run_id,
        recovery=recovery,
        outcome=terminal,
        result_ref=result_ref,
        effect_refs=step_effect_refs,
    )
    workflow_outcome = terminal
    if projection and not confirmed(
        step_terminal, step_run_id, terminal, result_ref, step_effect_refs
    ):
        workflow_outcome = "interrupted_pending"
    workflow_terminal = finish_selected_run(
        session,
        run_id,
        workflow_run_id,
        recovery=recovery,
        outcome=workflow_outcome,
        result_ref=result_ref,
        effect_refs=effect_refs,
    )
    if projection and all(
        confirmed(receipt, actual_id, terminal, result_ref, actual_effects)
        for receipt, actual_id, actual_effects in (
            (step_terminal, step_run_id, step_effect_refs),
            (workflow_terminal, workflow_run_id, effect_refs),
        )
    ):
        output["outcome"] = terminal
    if projection:
        atomic_write(result_path, output)
    return {**output, "result_ref": result_ref, "effect_refs": effect_refs}


def finish_action(
    session: Any,
    requested_action: str,
    action_run_id: str,
    output: Mapping[str, Any],
    result_ref: str,
    effect_refs: list[str],
    *,
    recovery: bool,
) -> Mapping[str, Any] | None:
    if output.get("action_terminal_recorded") is True:
        return None
    outcome = output.get("terminal_outcome", "completed")
    if outcome not in VALID_TERMINAL_OUTCOMES:
        raise SelectedExecutionError("native Action handler returned an invalid terminal outcome")
    return finish_selected_run(
        session,
        requested_action,
        action_run_id,
        recovery=recovery,
        outcome=outcome,
        result_ref=result_ref,
        effect_refs=effect_refs,
    )
