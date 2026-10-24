"""Public selected-executor registrations and isolated native adapters."""

from __future__ import annotations

from collections.abc import Callable, Mapping
from pathlib import Path
import sys
from typing import Any, cast

from selected_execution_contracts import (
    ActionHandler,
    LifecycleAdmissionError,
    SelectedExecutionError,
)


_ACTION_HANDLERS: dict[str, ActionHandler] = {}
_IMPLEMENTATION_AGENT: Callable[[str, Mapping[str, Any]], Mapping[str, Any]] | None = None


def preflight_selected_lifecycle(
    root: Path, route: object, parameters: object
) -> dict[str, Any] | None:
    """Observe source-derived status admission before a selected Run exists."""
    if route != "change_atom_status":
        return None
    tools_root = str(Path(__file__).resolve().parents[2] / "201_TOOLS")
    if tools_root not in sys.path:
        sys.path.insert(0, tools_root)
    try:
        import lifecycle_intents

        preflight = lifecycle_intents.preflight_atom_lifecycle(
            root, "change_status", cast(Mapping[str, Any], parameters)
        )
    except ImportError as error:
        raise SelectedExecutionError("source-derived lifecycle admission is unavailable") from error
    except lifecycle_intents.LifecycleError as error:
        raise LifecycleAdmissionError(error.code, str(error)) from error
    return {
        "operation": preflight["operation"],
        "prior": dict(preflight["prior"]),
        "requested_status": preflight["requested_status"],
        "current_status": preflight["current_status"],
        "status_model": dict(preflight["status_model"]),
        "archive": preflight["archive"],
    }


def register_action_handler(action_definition_id: str, handler: ActionHandler) -> None:
    """Register one native Action adapter without adding graph policy."""
    if not isinstance(action_definition_id, str) or not action_definition_id:
        raise ValueError("Action definition ID is required")
    if not callable(handler):
        raise TypeError("Action handler must be callable")
    previous = _ACTION_HANDLERS.get(action_definition_id)
    if previous is not None and previous is not handler:
        raise ValueError(f"Action handler already registered for {action_definition_id}")
    _ACTION_HANDLERS[action_definition_id] = handler


def register_implementation_agent(
    agent: Callable[[str, Mapping[str, Any]], Mapping[str, Any]],
) -> None:
    """Install the explicit Agent bridge for future selected queues."""
    if not callable(agent):
        raise TypeError("implementation agent must be callable")
    global _IMPLEMENTATION_AGENT
    if _IMPLEMENTATION_AGENT is not None and _IMPLEMENTATION_AGENT is not agent:
        raise ValueError("implementation agent is already registered")
    _IMPLEMENTATION_AGENT = agent


def implementation_agent() -> Callable[[str, Mapping[str, Any]], Mapping[str, Any]] | None:
    return _IMPLEMENTATION_AGENT


def action_handlers() -> Mapping[str, ActionHandler]:
    return _ACTION_HANDLERS


def make_revert_action_handler(service: Any) -> ActionHandler:
    """Adapt an injected CA-O-131 service to the shared selected Run session."""
    execute = getattr(service, "execute_with_session", None)
    if not callable(execute):
        raise TypeError("revert service must expose execute_with_session")

    def handler(context: dict[str, Any]) -> dict[str, Any]:
        parameters = context.get("parameters")
        if not isinstance(parameters, Mapping):
            raise SelectedExecutionError("CA-O-131 requires a reversal parameter mapping")
        manifest = parameters.get("approved_reversal_manifest", parameters.get("reversal_manifest"))
        if not isinstance(manifest, Mapping):
            raise SelectedExecutionError("CA-O-131 requires an approved reversal manifest")
        result = execute(
            manifest,
            context["session"],
            context["requested_action_run_id"],
            parameters.get("cancel_after_effect_id"),
        )
        if not isinstance(result, Mapping) or not isinstance(result.get("outcome"), str):
            raise SelectedExecutionError("CA-O-131 returned an invalid reversal result")
        account = result.get("effect_account", {})
        effects = account.get("effects", []) if isinstance(account, Mapping) else []
        manifest_id = result.get("manifest_id")
        effect_refs = [
            f".caprmedio_runtime/revert_changes/{manifest_id}:terminal/{item['effect_id']}"
            for item in effects
            if isinstance(item, Mapping)
            and item.get("status") == "completed"
            and isinstance(item.get("effect_id"), str)
            and isinstance(manifest_id, str)
        ]
        terminal = {
            "reverted": "completed",
            "no_op": "no_op",
            "failed": "failed",
            "partial_failure": "partial",
            "blocked": "interrupted_pending",
            "canceled": "cancelled",
            "recording_blocked": "interrupted_pending",
        }.get(result["outcome"], "interrupted_pending")
        return {
            "result": result["outcome"],
            "terminal_outcome": terminal,
            "effect_refs": effect_refs,
            "native_result": dict(result),
            "action_terminal_recorded": bool(result.get("run_receipt_refs"))
            and "run_error" not in result,
        }

    return handler
