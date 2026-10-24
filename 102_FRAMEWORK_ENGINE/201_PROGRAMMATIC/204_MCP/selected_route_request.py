"""Request and lifecycle validation for selected route adapters."""

from __future__ import annotations

import importlib
import sys
from pathlib import Path
from typing import Any, Mapping, cast

from selected_route_spec import _DIGEST
import selected_route_request_checks as _request_checks

validate_request = _request_checks.validate_request


def _public_module() -> Any:
    return sys.modules.get("selected_routes")


def _digest(value: Any) -> str:
    public = _public_module()
    if public is None:
        raise RuntimeError("selected_routes public module is unavailable")
    return cast(str, getattr(public, "canonical_digest")(value))


def preflight_lifecycle(adapter: Any, request: Mapping[str, Any]) -> dict[str, Any] | None:
    if request.get("operation_route") != "change_atom_status":
        return None
    app = Path(__file__).resolve().parents[1] / "203_APPS/WORKFLOW_ORCHESTRATOR"
    if str(app) not in sys.path:
        sys.path.insert(0, str(app))
    try:
        selected_execution = importlib.import_module("selected_execution")
    except (ImportError, AttributeError, TypeError, ValueError, RuntimeError) as error:
        return cast(
            dict[str, Any],
            adapter._result(
                request,
                "blocked",
                "blocked",
                f"source-derived lifecycle admission unavailable: {error}",
            ),
        )
    try:
        current = selected_execution.preflight_selected_lifecycle(
            adapter.root, "change_atom_status", request.get("parameters")
        )
        if request.get("mode") == "execute":
            receipt = request.get("proposal_receipt")
            freshness = receipt.get("source_freshness") if isinstance(receipt, Mapping) else None
            observed = freshness.get("observed") if isinstance(freshness, Mapping) else None
            expected = (
                observed.get("lifecycle_admission") if isinstance(observed, Mapping) else None
            )
            if not isinstance(expected, Mapping):
                raise selected_execution.LifecycleAdmissionError(
                    "status-preview-admission-missing",
                    "status execution requires the source-derived preview admission",
                )
            if _digest(dict(expected)) != _digest(current):
                raise selected_execution.LifecycleAdmissionError(
                    "status-model-stale",
                    "authoritative status-model source changed after lifecycle admission",
                )
    except selected_execution.LifecycleAdmissionError as error:
        result = cast(dict[str, Any], adapter._result(request, "blocked", "blocked", str(error)))
        result["effect_refs"] = []
        result["lifecycle_error"] = error.record()
        return result
    except (AttributeError, TypeError, ValueError, RuntimeError) as error:
        return cast(
            dict[str, Any],
            adapter._result(
                request,
                "blocked",
                "blocked",
                f"source-derived lifecycle admission unavailable: {error}",
            ),
        )
    return None


def expected_revisions(adapter: Any, route: str) -> list[dict[str, Any]]:
    entry = adapter.routes[route]
    rows: list[dict[str, Any]] = []
    for kind, pin in [
        ("workflow", entry["workflow"]),
        *[("step", item["step"]) for item in entry["ordered_steps"]],
        *[("action", item) for item in entry["ordered_actions"]],
    ]:
        row = {
            "kind": kind,
            "atom_id": pin["atom_id"],
            "version": pin["version"],
            "path": pin["source_path"],
            "digest": pin["digest"],
        }
        if row not in rows:
            rows.append(row)
    return sorted(
        rows, key=lambda item: (item["kind"], item["atom_id"], item["version"], item["path"])
    )


def validate_execute(request: Mapping[str, Any]) -> str | None:
    required = {
        "proposal_receipt",
        "proposal_receipt_digest",
        "assigned_action_id",
        "requested_runs",
        "operator_authorization",
    }
    missing = [name for name in sorted(required) if name not in request]
    if missing:
        return "execute requires exact preview receipt and Operator authorization"
    receipt = request["proposal_receipt"]
    public = _public_module()
    digest = getattr(public, "canonical_digest")
    if (
        not isinstance(receipt, Mapping)
        or not receipt
        or not _DIGEST.fullmatch(str(request["proposal_receipt_digest"]))
    ):
        return "execute proposal receipt is invalid"
    if digest(receipt) != request["proposal_receipt_digest"]:
        return "execute proposal receipt digest differs"
    if not isinstance(request["assigned_action_id"], str) or not request["assigned_action_id"]:
        return "execute assigned_action_id is invalid"
    if not isinstance(request["requested_runs"], list) or not request["requested_runs"]:
        return "execute requested Run identities are invalid"
    authorization = request["operator_authorization"]
    if (
        not isinstance(authorization, Mapping)
        or not isinstance(authorization.get("authorization_ref"), str)
        or not authorization["authorization_ref"]
    ):
        return "execute lacks explicit sealed Operator authorization"
    required_bindings = {
        key: request[key]
        for key in (
            "request_id",
            "operation_route",
            "proposal_receipt_digest",
            "parameters_digest",
            "target_frontier_digest",
            "effects_digest",
            "definition_manifest",
            "source_freshness",
        )
    }
    if any(authorization.get(key) != value for key, value in required_bindings.items()):
        return (
            "Operator authorization is not bound to the exact preview and current source frontier"
        )
    freshness = authorization.get("authorization_freshness")
    if (
        not isinstance(freshness, Mapping)
        or set(freshness) != {"state", "digest"}
        or freshness.get("state") != "current"
        or not isinstance(freshness.get("digest"), str)
        or not _DIGEST.fullmatch(freshness["digest"])
    ):
        return "Operator authorization freshness is invalid"
    if set(authorization) != {"authorization_ref", "authorization_freshness", *required_bindings}:
        return "Operator authorization contains unknown or incomplete bindings"
    return None
