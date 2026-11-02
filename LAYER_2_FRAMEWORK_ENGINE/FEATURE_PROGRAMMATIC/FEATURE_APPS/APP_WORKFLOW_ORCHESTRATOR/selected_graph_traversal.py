from collections.abc import Mapping
from pathlib import Path
from typing import Any

from selected_action_execution import execute_action, retain_implementation_result
from selected_execution_contracts import ActionHandler
from selected_graph_terminal import completed_receipt


def prior_result(
    workflow_run_id: str,
    graph: Mapping[str, Any],
    step_run_id: str,
    step: Mapping[str, Any],
    action_run_id: str,
    action: Mapping[str, Any],
    final_result: str,
    progress: Mapping[str, Any],
    terminal_receipt: Mapping[str, Any],
) -> dict[str, Any]:
    return {
        "workflow_run_id": workflow_run_id,
        "workflow_definition_id": graph["workflow"]["atom_id"],
        "step_run_id": step_run_id,
        "step_definition_id": step["atom_id"],
        "action_run_id": action_run_id,
        "action_definition_id": action["atom_id"],
        "result": final_result,
        "result_ref": progress["_result_ref"],
        "native_result": progress.get("native_result"),
        "completed_receipt": dict(terminal_receipt),
    }


def retain_prior_result(
    workflow_id: object,
    expected_id: str,
    target: list[dict[str, Any]],
    completed: bool,
    *,
    workflow_run_id: str,
    graph: Mapping[str, Any],
    step_run_id: str,
    step: Mapping[str, Any],
    action_run_id: str,
    action: Mapping[str, Any],
    final_result: str,
    progress: Mapping[str, Any],
    terminal_receipt: Mapping[str, Any],
) -> None:
    if completed and workflow_id == expected_id:
        target.append(
            prior_result(
                workflow_run_id,
                graph,
                step_run_id,
                step,
                action_run_id,
                action,
                final_result,
                progress,
                terminal_receipt,
            )
        )


def _retain_prior_results(
    graph: Mapping[str, Any],
    workflow_run_id: str,
    step_run_id: str,
    step: Mapping[str, Any],
    action_run_id: str,
    action: Mapping[str, Any],
    final_result: str,
    progress: Mapping[str, Any],
    terminal_receipt: Mapping[str, Any],
    completed: bool,
    structural_prior_results: list[dict[str, Any]],
    lifecycle_prior_results: list[dict[str, Any]],
) -> None:
    for expected_id, target in (
        ("CA-O-015", structural_prior_results),
        ("CA-O-127", lifecycle_prior_results),
    ):
        retain_prior_result(
            graph["workflow"]["atom_id"],
            expected_id,
            target,
            completed,
            workflow_run_id=workflow_run_id,
            graph=graph,
            step_run_id=step_run_id,
            step=step,
            action_run_id=action_run_id,
            action=action,
            final_result=final_result,
            progress=progress,
            terminal_receipt=terminal_receipt,
        )


def dispatch_step_actions(
    root: Path,
    handlers: Mapping[str, ActionHandler],
    frozen: Mapping[str, Any],
    session: Any,
    graph: Mapping[str, Any],
    step: Mapping[str, Any],
    requested_step: str,
    step_run_id: str,
    workflow_run_id: str,
    implementation_prior_results: list[dict[str, Any]],
    structural_prior_results: list[dict[str, Any]],
    lifecycle_prior_results: list[dict[str, Any]],
    journal: Any | None,
    recovery: bool,
    restored_action_ids: frozenset[str],
    results: list[dict[str, Any]],
) -> dict[str, Any]:
    final_result = None
    output: dict[str, Any] = {}
    step_effect_refs: list[str] = []
    for action_ordinal, action in enumerate(step["actions"], 1):
        requested_action = f"{requested_step}:action:{action_ordinal}"
        action_actual = session.start_run(requested_action)
        action_run_id = action_actual["run_id"]
        action_result = execute_action(
            root,
            handlers,
            frozen,
            session,
            graph,
            step,
            action,
            workflow_run_id=workflow_run_id,
            step_run_id=step_run_id,
            action_run_id=action_run_id,
            requested_action_id=requested_action,
            implementation_prior_results=implementation_prior_results,
            structural_prior_results=structural_prior_results,
            lifecycle_prior_results=lifecycle_prior_results,
            journal_preparation=journal,
            recovery=recovery,
            restored_action_ids=restored_action_ids,
        )
        output = action_result["output"]
        final_result = action_result["final_result"]
        effect_refs = action_result["effect_refs"]
        terminal_receipt = action_result["terminal_receipt"]
        progress = dict(action_result["progress"])
        progress_path = action_result["progress_path"]
        result_ref = progress_path.relative_to(root).as_posix()
        progress["_result_ref"] = result_ref
        completed = completed_receipt(
            terminal_receipt,
            result_ref=result_ref,
            effect_refs=effect_refs,
        )
        _retain_prior_results(
            graph,
            workflow_run_id,
            step_run_id,
            step,
            action_run_id,
            action,
            final_result,
            progress,
            terminal_receipt,
            completed,
            structural_prior_results,
            lifecycle_prior_results,
        )
        step_effect_refs.extend(effect_refs)
        result_row = {
            "step_run_id": step_run_id,
            "action_run_id": action_run_id,
            "step_definition_id": step["atom_id"],
            "action_definition_id": action["atom_id"],
            "result": final_result,
            "effect_refs": effect_refs,
        }
        if output.get("recording_error") is not None:
            result_row["recording_error"] = output["recording_error"]
        results.append(result_row)
        retain_implementation_result(
            graph["workflow"]["atom_id"],
            step,
            action,
            final_result,
            output,
            implementation_prior_results,
        )
    return {
        "final_result": final_result,
        "output": output,
        "step_effect_refs": step_effect_refs,
    }
