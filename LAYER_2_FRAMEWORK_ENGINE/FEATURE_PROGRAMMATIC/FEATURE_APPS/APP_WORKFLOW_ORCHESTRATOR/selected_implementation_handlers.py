"""Native capability adapters for the established implementation Actions."""

from __future__ import annotations

from collections.abc import Callable, Mapping
from pathlib import Path
from typing import Any

from selected_execution_contracts import SelectedExecutionError


ActionHandler = Callable[[dict[str, Any]], Mapping[str, Any]]
ImplementationAgent = Callable[[str, Mapping[str, Any]], Mapping[str, Any]]
PENDING_RESULTS = frozenset(
    {
        "blocked",
        "retry_blocked",
        "unresolved",
        "authority_change_required",
        "environment_blocker",
    }
)


def implementation_handlers(root: Path, agent: ImplementationAgent) -> dict[str, ActionHandler]:
    """Return the fixed Action adapters without selecting successor Steps."""
    import implementation_actions  # type: ignore[import-not-found]  # Runtime source adapter.

    return {
        action_id: _implementation_handler(root, agent, action)
        for action_id, action in implementation_actions.ACTION_HANDLERS.items()
    }


def _implementation_handler(
    root: Path,
    agent: ImplementationAgent,
    action: Callable[..., Mapping[str, Any]],
) -> ActionHandler:
    def implementation(context: dict[str, Any]) -> dict[str, Any]:
        result = action(
            context["parameters"],
            agent=agent,
            selected_project_root=root,
            trusted_execution_authorization=context.get("trusted_execution_authorization"),
        )
        if not isinstance(result, Mapping) or not isinstance(result.get("result"), str):
            raise SelectedExecutionError("implementation Action returned an invalid queue envelope")
        label = result["result"]
        output: dict[str, Any] = {"result": label, "effect_refs": [], "native_result": result}
        if label in PENDING_RESULTS:
            output["terminal_outcome"] = "interrupted_pending"
        return output

    return implementation
