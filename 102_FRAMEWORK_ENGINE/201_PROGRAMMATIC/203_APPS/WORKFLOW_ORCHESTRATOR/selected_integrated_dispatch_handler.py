"""Action handler and Run lineage helpers for Integrated dispatch."""

from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path
from typing import Any

from selected_execution_contracts import ActionHandler, SelectedExecutionError
from selected_integrated_action import IntegratedActionPending
from selected_integrated_action_provider import invoke_integrated_action_from_context
from selected_integrated_session import load_completed_output


# implementation of:
# Method: CA-M-405
def action_handler(
    root: Path,
    run_id: str,
    session: Any,
    profile: Mapping[str, Any],
    method_projection: object | None,
    methods: object | None,
    action: Any,
) -> ActionHandler:
    """Return one bridge handler which prefers a checkpointed native output."""

    def invoke(context: dict[str, Any]) -> Mapping[str, Any]:
        requested = context.get("requested_action_run_id")
        if not isinstance(requested, str):
            raise SelectedExecutionError("Integrated Action has no requested Run identity")
        retained = load_completed_output(root, run_id, requested, session)
        if retained is not None:
            return dict(retained)
        try:
            return invoke_integrated_action_from_context(
                {**context, "trusted_workflow_binding": profile},
                trusted_method_projection=method_projection,
                trusted_methods=methods,
                action=action,
            )
        except IntegratedActionPending as pending:
            capture = dict(pending.capture)
            capture["run_binding"] = {
                "workflow_run_id": context["workflow_run_id"],
                "step_run_id": context["step_run_id"],
                "action_run_id": context["action_run_id"],
                "requested_action_id": requested,
            }
            raise IntegratedActionPending(capture) from pending

    return invoke


def actual_run_ids(session: Any, run_id: str, capture: Mapping[str, Any]) -> dict[str, str]:
    """Return the started Workflow, Step, and Action Run identities."""
    actual, binding = getattr(session, "actual", {}), capture.get("run_binding")
    if not isinstance(actual, Mapping) or not isinstance(binding, Mapping):
        raise SelectedExecutionError("Integrated checkpoint has no actual Run facts")
    requested = binding.get("requested_action_id")
    action_row = actual.get(requested) if isinstance(requested, str) else None
    if not isinstance(action_row, Mapping) or action_row.get("run_id") != binding.get(
        "action_run_id"
    ):
        raise SelectedExecutionError("Integrated Action Run binding is incomplete")
    if not isinstance(action_row.get("definition"), Mapping) or action_row["definition"].get(
        "atom_id"
    ) != capture.get("action_id"):
        raise SelectedExecutionError("Integrated Action Run binding is stale")
    expected = {"workflow_run_id": run_id, "step_run_id": action_row.get("parent_run_id")}
    by_run = {row.get("run_id"): row for row in actual.values() if isinstance(row, Mapping)}
    step = by_run.get(expected["step_run_id"])
    if not isinstance(step, Mapping) or step.get("run_id") != binding.get("step_run_id"):
        raise SelectedExecutionError("Integrated Step Run binding is incomplete")
    workflow = by_run.get(step.get("parent_run_id"))
    if not isinstance(workflow, Mapping) or workflow.get("run_id") != binding.get(
        "workflow_run_id"
    ):
        raise SelectedExecutionError("Integrated Workflow Run binding is incomplete")
    if actual.get(run_id) is not workflow:
        raise SelectedExecutionError("Integrated Workflow Run binding is stale")
    return {key: binding[key] for key in ("workflow_run_id", "step_run_id", "action_run_id")}
