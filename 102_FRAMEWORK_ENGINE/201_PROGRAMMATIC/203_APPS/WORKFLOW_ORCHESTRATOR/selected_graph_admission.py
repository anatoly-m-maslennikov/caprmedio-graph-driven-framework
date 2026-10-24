"""Query and source-derived lifecycle admission for selected graphs."""

from __future__ import annotations

from collections.abc import Mapping
import json
from pathlib import Path
import sys
from typing import Any, cast

from selected_execution_contracts import LifecycleAdmissionError, SelectedExecutionError


def _canonical_json(value: object) -> bytes:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode()


def validate_query_admission(graph: Mapping[str, Any], execution: Mapping[str, Any]) -> None:
    if graph.get("route") not in {
        "find_and_fetch_artifacts",
        "find_and_fetch_journal_events",
    }:
        return
    steps = graph.get("steps")
    if not isinstance(steps, list) or len(steps) != 1 or not isinstance(steps[0], Mapping):
        raise SelectedExecutionError("query Workflow must bind exactly one Step")
    actions = steps[0].get("actions")
    if not isinstance(actions, list) or len(actions) != 1 or not isinstance(actions[0], Mapping):
        raise SelectedExecutionError("query Step must bind exactly one Action")
    try:
        import query_actions

        query_actions.validate_query_parameters(
            {
                "route": graph["route"],
                "workflow_definition_id": graph["workflow"]["atom_id"],
                "step_definition_id": steps[0]["atom_id"],
                "action_definition_id": actions[0]["atom_id"],
                "parameters": execution.get("parameters"),
            }
        )
    except ImportError as error:
        raise SelectedExecutionError("query request adapter is unavailable") from error
    except query_actions.QueryActionError as error:
        raise SelectedExecutionError("query request is not admitted") from error


def _lifecycle_preflight(root: Path, execution: Mapping[str, Any]) -> dict[str, Any] | None:
    tools_root = str(Path(__file__).resolve().parents[2] / "201_TOOLS")
    if tools_root not in sys.path:
        sys.path.insert(0, tools_root)
    try:
        import lifecycle_intents

        preflight = lifecycle_intents.preflight_atom_lifecycle(
            root,
            "change_status",
            cast(Mapping[str, Any], execution.get("parameters")),
        )
    except ImportError as error:
        raise SelectedExecutionError("source-derived lifecycle admission is unavailable") from error
    except lifecycle_intents.LifecycleError as error:
        raise LifecycleAdmissionError(error.code, str(error)) from error
    if preflight is None:
        return None
    return {
        "operation": preflight["operation"],
        "prior": dict(preflight["prior"]),
        "requested_status": preflight["requested_status"],
        "current_status": preflight["current_status"],
        "status_model": dict(preflight["status_model"]),
        "archive": preflight["archive"],
    }


def validate_lifecycle_admission(
    root: Path,
    graph: Mapping[str, Any],
    execution: Mapping[str, Any],
    *,
    expected_admission: Mapping[str, Any] | None = None,
) -> dict[str, Any] | None:
    if graph.get("route") != "change_atom_status":
        return None
    current = _lifecycle_preflight(root, execution)
    if current is None:
        return None
    expected = expected_admission
    if expected is None:
        receipt = execution.get("proposal_receipt")
        freshness = receipt.get("source_freshness") if isinstance(receipt, Mapping) else None
        observed = freshness.get("observed") if isinstance(freshness, Mapping) else None
        expected = observed.get("lifecycle_admission") if isinstance(observed, Mapping) else None
    if not isinstance(expected, Mapping):
        raise LifecycleAdmissionError(
            "status-preview-admission-missing",
            "status execution requires the source-derived preview admission",
        )
    if _canonical_json(dict(expected)) != _canonical_json(current):
        raise LifecycleAdmissionError(
            "status-model-stale",
            "authoritative status-model source changed after lifecycle admission",
        )
    return current
