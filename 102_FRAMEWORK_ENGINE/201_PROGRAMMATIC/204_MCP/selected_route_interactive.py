"""Strict public entry for a retained Integrated O016 Action response."""

# implementation of:
# Requirement: CA-R-2117
# Method: CA-M-431, CA-M-413

from __future__ import annotations

import importlib
import sys
from collections.abc import Mapping
from pathlib import Path
from typing import Any, cast

from pydantic import ValidationError
from selected_route_workflow_profiles import (
    is_current_integrated_execute as _is_current_integrated_execute,
    is_direct_integrated_version,
    workflow_version,
)

is_current_integrated_execute = _is_current_integrated_execute


def is_submit_result(request: object) -> bool:
    """Recognize only the continuation operation on the existing O016 route."""
    return isinstance(request, Mapping) and request.get("operation") == "submit_result"


def _orchestrator() -> Any:
    app = Path(__file__).resolve().parents[1] / "203_APPS/WORKFLOW_ORCHESTRATOR"
    if str(app) not in sys.path:
        sys.path.insert(0, str(app))
    return importlib.import_module("orchestrator")


def _public_pending(value: Mapping[str, Any]) -> dict[str, Any]:
    """Expose the pending Action contract without retained trusted definitions."""
    capture = value.get("capture")
    if (
        value.get("status") != "pending_action"
        or not isinstance(capture, Mapping)
        or not isinstance(capture.get("output_schema"), Mapping)
        or not all(
            isinstance(value.get(name), str) and value[name]
            for name in ("workflow_run_id", "action_run_id", "continuation_id")
        )
    ):
        return dict(value)
    public_capture = {key: item for key, item in capture.items() if key != "definitions"}
    return {
        **value,
        "capture": public_capture,
        "next_call": {
            "tool": "run_implementation_workflow",
            "request": {
                "operation": "submit_result",
                "run_id": value["workflow_run_id"],
                "action_run_id": value["action_run_id"],
                "continuation_id": value["continuation_id"],
            },
            "result_schema": dict(capture["output_schema"]),
        },
    }


# implementation of:
# Requirement: CA-R-2117
# Method: CA-M-431, CA-M-413
def invoke_submit_result(adapter: Any, request: object) -> dict[str, Any]:
    """Validate a response before handing its selected Project root to the APP."""
    try:
        parsed = _orchestrator().SubmitResult.model_validate(request)
    except (ImportError, AttributeError, ValidationError) as error:
        return cast(
            dict[str, Any],
            adapter._result(request, "rejected", "rejected", f"submit_result is invalid: {error}"),
        )
    try:
        value = _orchestrator().run(adapter.root, parsed.model_dump())
    except (ImportError, AttributeError, OSError, RuntimeError, TypeError, ValueError) as error:
        return cast(
            dict[str, Any],
            adapter._result(
                request, "blocked", "blocked", f"submit_result continuation is unavailable: {error}"
            ),
        )
    if not isinstance(value, Mapping):
        return cast(
            dict[str, Any],
            adapter._result(
                request,
                "blocked",
                "blocked",
                "submit_result continuation returned an invalid result",
            ),
        )
    return _public_pending(value)


def _workflow_run_id(request: Mapping[str, Any]) -> str:
    rows = request.get("requested_runs")
    if not isinstance(rows, list):
        raise ValueError("execute has no requested Workflow Run identity")
    workflow = [row for row in rows if isinstance(row, Mapping) and row.get("kind") == "workflow"]
    if len(workflow) != 1 or not isinstance(workflow[0].get("requested_run_id"), str):
        raise ValueError("execute must carry one requested Workflow Run identity")
    return str(workflow[0]["requested_run_id"])


def _preview_request(request: Mapping[str, Any]) -> dict[str, Any]:
    preview = {
        key: value
        for key, value in request.items()
        if key
        not in {
            "proposal_receipt",
            "proposal_receipt_digest",
            "assigned_action_id",
            "operator_authorization",
            "requested_runs",
        }
    }
    preview["mode"] = "preview"
    return preview


# implementation of:
# Requirement: CA-R-2117
# Method: CA-M-431, CA-M-413
def invoke_integrated_execute(
    adapter: Any, request: Mapping[str, Any], support: Any
) -> dict[str, Any]:
    """Admit only the exact preview before the current Integrated APP entry."""
    routes = getattr(adapter, "routes", None)
    if isinstance(routes, Mapping):
        version = workflow_version(routes.get(request.get("operation_route")))
        if not is_direct_integrated_version(version):
            return cast(
                dict[str, Any],
                adapter._result(
                    request,
                    "rejected",
                    "rejected",
                    f"O016@{version} is not an admitted direct Integrated Workflow",
                ),
            )
    try:
        prepared = support.run_selected_operation(_preview_request(request))
        if (
            prepared.get("disposition") != "preview"
            or request.get("proposal_receipt") != prepared.get("proposal_receipt")
            or request.get("proposal_receipt_digest") != prepared.get("proposal_receipt_digest")
        ):
            return cast(
                dict[str, Any],
                adapter._result(
                    request,
                    "blocked",
                    "blocked",
                    "exact current preview receipt is required before Integrated dispatch",
                ),
            )
        value = _orchestrator().run(
            adapter.root,
            {
                "operation": "enqueue_selected",
                "run_id": _workflow_run_id(request),
                "execution": dict(request),
            },
        )
    except (ImportError, AttributeError, OSError, RuntimeError, TypeError, ValueError) as error:
        return cast(
            dict[str, Any],
            adapter._result(
                request,
                "blocked",
                "blocked",
                f"Integrated dispatch is unavailable: {error}",
            ),
        )
    if not isinstance(value, Mapping):
        return cast(
            dict[str, Any],
            adapter._result(
                request,
                "blocked",
                "blocked",
                "Integrated dispatch returned an invalid result",
            ),
        )
    return _public_pending(value)
