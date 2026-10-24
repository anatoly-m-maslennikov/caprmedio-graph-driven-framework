"""Source-bound lifecycle dispatch for the selected Workflow executor."""

from __future__ import annotations

from collections.abc import Callable, Mapping
from pathlib import Path
from typing import Any, cast

from selected_creation_handler import creation_atom as execute_creation_atom
from selected_execution_contracts import ActionHandler
from selected_lifecycle_handler import lifecycle_change_atom as execute_lifecycle_change_atom
from selected_lifecycle_status_handler import (
    lifecycle_status_change_atom as execute_lifecycle_status_change_atom,
)
from selected_replacement_handler import replacement_atom as execute_replacement_atom
from selected_update_assessment import (
    LifecycleIntents,
    admitted_update_assessment,
    assess_update_identity,
)


Action = Callable[..., Mapping[str, Any]]


def _effect_path(item: object) -> object:
    if not isinstance(item, Mapping):
        return None
    path = item.get("path")
    carrier = item.get("carrier")
    if not isinstance(path, str) and isinstance(carrier, Mapping):
        path = carrier.get("path")
    return path


def _effect_paths(value: object) -> list[str]:
    candidates = value.get("paths", []) if isinstance(value, Mapping) else value
    if not isinstance(candidates, list):
        return []
    paths = [
        _effect_path(item)
        for item in candidates
        if isinstance(item, Mapping) and item.get("state") == "changed"
    ]
    return sorted({path for path in paths if isinstance(path, str)})


def ordinary_lifecycle_result(
    root: Path,
    context: Mapping[str, Any],
    action: Action,
    call: Mapping[str, Any],
) -> dict[str, Any]:
    """Preserve the generic lifecycle result for routes without nested recording."""
    result = action(root, context["parameters"], **dict(call))
    outcome = cast(str, result.get("outcome"))
    effects = _effect_paths(result.get("effects"))
    history = result.get("history")
    prior = history.get("prior_revision") if isinstance(history, Mapping) else None
    if isinstance(prior, Mapping) and isinstance(prior.get("path"), str):
        effects = sorted({*effects, prior["path"]})
    terminal = {
        "applied": "completed",
        "no-op": "no_op",
        "duplicate": "no_op",
        "failed": "failed",
        "partial": "partial",
        "canceled": "cancelled",
        "recording-blocked": "interrupted_pending",
        "blocked": "interrupted_pending",
    }.get(outcome, "interrupted_pending")
    return {
        "result": {"duplicate": "no-op", "no-op": "no-op"}.get(outcome, outcome),
        "terminal_outcome": terminal,
        "effect_refs": effects,
        "native_result": result,
    }


def _action_for_route(lifecycle_intents: LifecycleIntents, route: str) -> Action | None:
    if route == "create_atom":
        return lifecycle_intents.create_atom_action
    if route == "update_atom":
        return lifecycle_intents.update_atom_action
    if route == "replace_atom":
        return lifecycle_intents.replace_atom_action
    if route == "change_atom_status":
        return lifecycle_intents.change_status_atom_action
    if route == "move_atom":
        return lifecycle_intents.move_atom_action
    return None


def atom_lifecycle(
    root: Path, lifecycle_intents: LifecycleIntents, context: dict[str, Any]
) -> dict[str, Any]:
    """Dispatch one of the five source-declared atom lifecycle routes."""
    route = context.get("route")
    if not isinstance(route, str):
        return {"result": "blocked", "effect_refs": []}
    action = _action_for_route(lifecycle_intents, route)
    if action is None:
        return {"result": "blocked", "effect_refs": []}
    call: dict[str, Any] = {"execute": True, "authorized": True}
    if route == "update_atom":
        assessment = admitted_update_assessment(lifecycle_intents, context)
        if assessment is None:
            return {
                "result": "reassessment-required",
                "terminal_outcome": "interrupted_pending",
                "effect_refs": [],
            }
        call["assessment"] = assessment
    return dispatch_lifecycle_action(root, context, action, call)


def dispatch_lifecycle_action(
    root: Path,
    context: dict[str, Any],
    action: Action,
    call: Mapping[str, Any],
) -> dict[str, Any]:
    """Select the canonical nested handler while retaining generic fallback."""
    route = context["route"]
    if route == "create_atom" and "creation_requested_run_id" in context:
        return execute_creation_atom(root, context, action, call)
    if route == "replace_atom":
        return execute_replacement_atom(root, context, action, call)
    if route == "update_atom" and "lifecycle_requested_run_id" in context:
        return execute_lifecycle_change_atom(root, context, action, call)
    if route == "change_atom_status" and context.get("lifecycle_current_state") is True:
        return execute_lifecycle_status_change_atom(root, context, action, call)
    return ordinary_lifecycle_result(root, context, action, call)


def lifecycle_handlers(root: Path) -> dict[str, ActionHandler]:
    """Bind source-declared lifecycle Actions to this Project root."""
    import lifecycle_intents

    intents = cast(LifecycleIntents, lifecycle_intents)

    def atom_handler(context: dict[str, Any]) -> dict[str, Any]:
        return atom_lifecycle(root, intents, context)

    def assessment_handler(context: dict[str, Any]) -> dict[str, Any]:
        return assess_update_identity(intents, context)

    return {"CA-O-128": atom_handler, "CA-O-067": assessment_handler}
