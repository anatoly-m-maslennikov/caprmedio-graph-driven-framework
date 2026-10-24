# implementation of: CA-M-405

from collections.abc import Mapping
import hashlib
from pathlib import Path
from typing import Any, cast

from selected_action_context import build_action_context
from selected_evidence_io import atomic_write, run_directory
from selected_execution_contracts import ActionHandler, SelectedExecutionError, canonical_json
from selected_graph_terminal import add_progress_fields, finish_action


def _effect_refs(value: object) -> list[str]:
    if not isinstance(value, list) or any(not isinstance(item, str) for item in value):
        raise SelectedExecutionError("native Action handler returned invalid effect references")
    return list(value)


def _result_map(action: Mapping[str, Any], result: str) -> str:
    mapping = action.get("result_map", {})
    final = mapping.get(result, result) if isinstance(mapping, Mapping) else None
    if not isinstance(final, str):
        raise SelectedExecutionError("selected Action result map is invalid")
    return final


def _graph_output(
    output: dict[str, Any],
    progress: dict[str, Any],
    route: object,
) -> object | None:
    if route not in {"build_entities_graph", "build_terms_graph"}:
        return None
    observation = cast(Mapping[str, Any], output.get("native_result"))
    from graph_completion import construction_outcome

    output["terminal_outcome"] = construction_outcome(observation)
    if output.get("action_terminal_recorded") is True:
        raise SelectedExecutionError("graph Action cannot supply its own terminal recording")
    progress["graph_construction_observation"] = observation
    progress["graph_construction_digest"] = hashlib.sha256(canonical_json(observation)).hexdigest()
    return observation


def _record_graph_result(
    output: dict[str, Any],
    observation: object,
    terminal_receipt: Mapping[str, Any] | None,
    *,
    action_run_id: str,
    result_ref: str,
    effect_refs: list[str],
) -> str:
    from graph_completion import finalize_graph_result

    finalized = finalize_graph_result(
        cast(Mapping[str, Any], observation),
        terminal_receipt,
        action_run_id=action_run_id,
        result_ref=result_ref,
        effect_refs=effect_refs,
    )
    output["native_result"] = finalized
    return str(finalized["outcome"])


def retain_implementation_result(
    workflow_id: object,
    step: Mapping[str, Any],
    action: Mapping[str, Any],
    final_result: str,
    output: Mapping[str, Any],
    target: list[dict[str, Any]],
) -> None:
    if workflow_id != "CA-O-016":
        return
    values = native if isinstance(native := output.get("native_result"), Mapping) else {}
    target.append(
        {
            "step_definition_id": step["atom_id"],
            "action_definition_id": action["atom_id"],
            "result": final_result,
            "outputs": values.get("outputs", {}),
            "evidence": values.get("evidence", []),
            "retained_state": values.get("retained_state", {}),
            **{key: values.get(key) for key in ("candidate", "binding_digest")},
        }
    )


def execute_action(
    root: Path,
    handlers: Mapping[str, ActionHandler],
    frozen: Mapping[str, Any],
    session: Any,
    graph: Mapping[str, Any],
    step: Mapping[str, Any],
    action: Mapping[str, Any],
    *,
    workflow_run_id: str,
    step_run_id: str,
    action_run_id: str,
    requested_action_id: str,
    implementation_prior_results: list[dict[str, Any]],
    structural_prior_results: list[dict[str, Any]],
    lifecycle_prior_results: list[dict[str, Any]],
    journal_preparation: Any | None,
    recovery: bool,
    restored_action_ids: frozenset[str],
) -> dict[str, Any]:
    handler, context = build_action_context(
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
        requested_action_id=requested_action_id,
        implementation_prior_results=implementation_prior_results,
        structural_prior_results=structural_prior_results,
        lifecycle_prior_results=lifecycle_prior_results,
        journal_preparation=journal_preparation,
        restored_action_ids=restored_action_ids,
    )
    output = handler(context)
    if not isinstance(output, Mapping) or not isinstance(output.get("result"), str):
        raise SelectedExecutionError("native Action handler returned no declared result")
    output = dict(output)
    final_result = _result_map(action, output["result"])
    effect_refs = _effect_refs(output.get("effect_refs", []))
    run_id = frozen["request"]["run_id"]
    progress_path = run_directory(root, run_id) / f"{requested_action_id}.json"
    result_ref = progress_path.relative_to(root).as_posix()
    progress: dict[str, Any] = {
        "result": final_result,
        "action_run_id": action_run_id,
        "effect_refs": effect_refs,
        "native_result": output.get("native_result"),
        "compiler_publication_recording": output.get("compiler_publication_recording"),
    }
    observation = _graph_output(output, progress, graph.get("route"))
    add_progress_fields(progress, output)
    if observation is not None and effect_refs:
        session.note_effects(action_run_id, result_ref=result_ref, effect_refs=effect_refs)
    atomic_write(progress_path, progress)
    terminal_receipt = finish_action(
        session,
        requested_action_id,
        action_run_id,
        output,
        result_ref,
        effect_refs,
        recovery=recovery,
    )
    if observation is not None:
        final_result = _result_map(
            action,
            _record_graph_result(
                output,
                observation,
                terminal_receipt,
                action_run_id=action_run_id,
                result_ref=result_ref,
                effect_refs=effect_refs,
            ),
        )
        progress["native_result"] = output["native_result"]
        progress["result"] = final_result
        atomic_write(progress_path, progress)
    recording = output.get("compiler_publication_recording")
    if recording is not None:
        if not isinstance(recording, Mapping):
            raise SelectedExecutionError("compiler publication recording handoff is invalid")
        if (
            terminal_receipt is not None
            and terminal_receipt.get("disposition") == "terminal"
            and terminal_receipt.get("outcome") == "completed"
        ):
            completed = recording.get("on_recorded_result")
            if not isinstance(completed, str):
                raise SelectedExecutionError("compiler publication recording handoff is incomplete")
            final_result = _result_map(action, completed)
            progress["result"] = final_result
            atomic_write(progress_path, progress)
        else:
            output["terminal_outcome"] = "interrupted_pending"
    return dict(
        output=output,
        final_result=final_result,
        effect_refs=effect_refs,
        terminal_receipt=terminal_receipt,
        progress=progress,
        progress_path=progress_path,
    )
