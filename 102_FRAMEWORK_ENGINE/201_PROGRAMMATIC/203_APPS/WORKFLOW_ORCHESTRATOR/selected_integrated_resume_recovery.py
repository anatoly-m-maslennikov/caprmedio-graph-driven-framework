"""Checkpoint recovery for a sealed Integrated result submission."""

# implementation of:
# Requirement: CA-R-1524
# Method: CA-M-405

from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path
from typing import Any

from selected_execution_contracts import SelectedExecutionError
from selected_integrated_action import submit_integrated_action
from selected_integrated_action_provider import current_integrated_action_provider
from selected_integrated_session import load_completed_output, restore_checkpoint


def _checkpointed(
    root: Path, frozen: Mapping[str, Any], tracker: Any, capture: Mapping[str, Any]
) -> Mapping[str, Any]:
    binding = capture.get("run_binding")
    requested = binding.get("requested_action_id") if isinstance(binding, Mapping) else None
    if not isinstance(requested, str):
        raise SelectedExecutionError("admitted Integrated result has no Action Run binding")
    request = frozen.get("request")
    run_id = request.get("run_id") if isinstance(request, Mapping) else None
    if not isinstance(run_id, str):
        raise SelectedExecutionError("admitted Integrated result has no Run identity")
    retained = load_completed_output(
        root, run_id, requested, restore_checkpoint(root, frozen, tracker)
    )
    native = retained.get("native_result") if isinstance(retained, Mapping) else None
    if not isinstance(native, Mapping):
        raise SelectedExecutionError("admitted Integrated result has no checkpointed Action output")
    return dict(native)


def accepted_result(
    root: Path,
    frozen: Mapping[str, Any],
    tracker: Any,
    capture: Mapping[str, Any],
    sealed: Mapping[str, Any],
    record: Mapping[str, Any],
    action: Any,
) -> Mapping[str, Any]:
    """Never replay a provider for an already-admitted continuation."""
    if record.get("state") == "admitted":
        return _checkpointed(root, frozen, tracker, capture)
    provider = current_integrated_action_provider if action is None else action
    return submit_integrated_action(provider, capture, sealed["result"], selected_project_root=root)
