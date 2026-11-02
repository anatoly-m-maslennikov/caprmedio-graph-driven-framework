"""Native capability adapters for selected graph-projection Actions."""

from __future__ import annotations

from collections.abc import Callable, Mapping
from pathlib import Path
from typing import Any

from selected_execution_contracts import SelectedExecutionError


ActionHandler = Callable[[dict[str, Any]], Mapping[str, Any]]


def graph_projection_handlers(root: Path) -> dict[str, ActionHandler]:
    """Return the existing graph-construction adapters for the selected Project."""
    import generate_entity_graph  # type: ignore[import-not-found]  # Runtime source adapter.

    return {
        action_id: _graph_projection_handler(handler)
        for action_id, handler in generate_entity_graph.queue_action_handlers(root).items()
    }


def _graph_projection_handler(
    handler: Callable[[dict[str, Any]], Mapping[str, Any]],
) -> ActionHandler:
    def graph_projection(context: dict[str, Any]) -> dict[str, Any]:
        from graph_completion import construction_outcome

        result = handler(context)
        if not isinstance(result, Mapping) or not isinstance(result.get("result"), str):
            raise SelectedExecutionError(
                "graph projection Action returned an invalid queue envelope"
            )
        native_result = result.get("graph_result", result)
        output = {**result, "native_result": native_result}
        output["terminal_outcome"] = construction_outcome(native_result)
        return output

    return graph_projection
