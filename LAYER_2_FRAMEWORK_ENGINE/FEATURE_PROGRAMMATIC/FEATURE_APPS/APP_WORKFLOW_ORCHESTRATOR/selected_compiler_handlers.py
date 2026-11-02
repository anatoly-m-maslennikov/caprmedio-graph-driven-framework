"""Native compiler Action adaptation for selected Workflow execution."""

from __future__ import annotations

from collections.abc import Callable, Mapping
from pathlib import Path
from typing import Any

from selected_compiler_inputs import compiler_parameters_for_executor, publication_output_paths
from selected_execution_contracts import ActionHandler, SelectedExecutionError


CompilerAction = Callable[[dict[str, Any]], object]


def compiler_handler(
    root_provider: Callable[[], Path],
    action: CompilerAction,
    structural_handler: ActionHandler | None,
) -> ActionHandler:
    """Adapt one compiler Action while preserving source-selected successors."""

    def execute(context: dict[str, Any]) -> dict[str, Any]:
        if context["workflow_definition_id"] != "CA-O-011":
            if structural_handler is not None:
                return dict(structural_handler(context))
            return {
                "result": "blocked",
                "terminal_outcome": "interrupted_pending",
                "effect_refs": [],
            }
        result = action(dict(compiler_parameters_for_executor(root_provider(), context)))
        if not isinstance(result, Mapping) or not isinstance(result.get("outcome"), str):
            raise SelectedExecutionError("compiler Action returned an invalid result")
        return _compiler_result(context, result)

    return execute


def _compiler_result(context: Mapping[str, Any], result: Mapping[str, Any]) -> dict[str, Any]:
    outcome = result["outcome"]
    step_id = context["step_definition_id"]
    output: dict[str, Any] = {"result": outcome, "effect_refs": [], "native_result": result}
    if step_id == "CA-O-157" and context["action_definition_id"] == "CA-O-009":
        return _publication_result(output, result, outcome)
    if step_id == "CA-O-152" and outcome == "assessed":
        output["result"] = "complete exact selection"
    elif step_id == "CA-O-153" and outcome == "assessed" and _checks_complete(result):
        output["result"] = (
            "required checks complete, no unresolved conflict, required approvals valid"
        )
    elif outcome in {"blocked", "pending_recording"}:
        output["terminal_outcome"] = "interrupted_pending"
    else:
        output["terminal_outcome"] = "interrupted_pending"
    return output


def _publication_result(
    output: dict[str, Any], result: Mapping[str, Any], outcome: str
) -> dict[str, Any]:
    if outcome == "pending_recording" and result.get("apply_status") == "APPLIED":
        return _pending_publication(output, result)
    if (
        outcome == "publication_recovery_required"
        and result.get("apply_status") == "EFFECT_APPLIED_STALE"
    ):
        return _stale_publication(output, result)
    if outcome == "published":
        publication = result.get("publication")
        planned = publication.get("output_plan", []) if isinstance(publication, Mapping) else []
        output["result"] = "completed publication from the still-valid final frontier"
        output["effect_refs"] = sorted(
            {
                item["output_path"]
                for item in planned
                if isinstance(item, Mapping) and isinstance(item.get("output_path"), str)
            }
        )
        return output
    output["terminal_outcome"] = "interrupted_pending"
    return output


def _pending_publication(output: dict[str, Any], result: Mapping[str, Any]) -> dict[str, Any]:
    publication = result.get("publication")
    frontier = result.get("source_frontier_digest")
    planned = publication.get("output_plan") if isinstance(publication, Mapping) else None
    output_digest = publication.get("output_digest") if isinstance(publication, Mapping) else None
    if (
        not isinstance(frontier, str)
        or not frontier
        or not isinstance(output_digest, str)
        or not output_digest
    ):
        output.update(result="blocked", terminal_outcome="interrupted_pending")
        return output
    if not isinstance(planned, list):
        output.update(result="blocked", terminal_outcome="interrupted_pending")
        return output
    paths = sorted(
        {
            item["output_path"]
            for item in planned
            if isinstance(item, Mapping) and isinstance(item.get("output_path"), str)
        }
    )
    if len(paths) != len(planned):
        output.update(result="blocked", terminal_outcome="interrupted_pending")
        return output
    output.update(
        result="publication recording required",
        terminal_outcome="completed",
        effect_refs=paths,
        compiler_publication_recording={
            "on_recorded_result": "completed publication from the still-valid final frontier",
            "source_frontier_digest": frontier,
            "output_digest": output_digest,
            "output_paths": paths,
        },
    )
    return output


def _stale_publication(output: dict[str, Any], result: Mapping[str, Any]) -> dict[str, Any]:
    publication = result.get("publication")
    planned = publication.get("output_plan") if isinstance(publication, Mapping) else None
    effect_state = publication.get("effect_state") if isinstance(publication, Mapping) else None
    refs = publication_output_paths(planned)
    if (
        effect_state != "output_replacement_completed"
        or result.get("output_plan") != planned
        or refs is None
    ):
        output["terminal_outcome"] = "interrupted_pending"
        return output
    output.update(terminal_outcome="partial", effect_refs=refs)
    return output


def _checks_complete(result: Mapping[str, Any]) -> bool:
    return result.get("unresolved_conflict_count") == 0 and result.get("can_apply") is True
