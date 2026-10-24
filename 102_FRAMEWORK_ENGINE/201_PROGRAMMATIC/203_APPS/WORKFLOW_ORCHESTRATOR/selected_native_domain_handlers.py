"""Explicit built-in native Action handlers for selected Workflow execution."""

from __future__ import annotations

from collections.abc import Callable, Mapping
from pathlib import Path
import sys
from typing import Any, cast

from selected_execution_contracts import ActionHandler, SelectedExecutionError


ImplementationAgent = Callable[[str, Mapping[str, Any]], Mapping[str, Any]]


def source_bound_native_handlers(
    root: Path,
    implementation_agent: ImplementationAgent | None,
) -> dict[str, ActionHandler]:
    """Load the fixed built-in domains; manifests still select every Action."""
    _add_domain_import_paths()
    available: dict[str, ActionHandler] = {}
    _add_lifecycle_handlers(available, root)
    _add_project_structure_handlers(available, root)
    _add_graph_projection_handlers(available, root)
    available["CA-O-131"] = _revert_not_configured
    _add_implementation_handlers(available, root, implementation_agent)
    return available


def _add_domain_import_paths() -> None:
    tools_root = Path(__file__).resolve().parents[2] / "201_TOOLS"
    paths = (
        tools_root,
        tools_root / "WORKFLOW_OPERATIONS" / "PROJECT_STRUCTURE",
        tools_root / "GENERATE_ENTITY_GRAPH",
        tools_root / "COMPILE_APPLICABLE_METHODOLOGY",
        Path(__file__).resolve().parents[3]
        / "202_AGENTIC"
        / "202_PROMPTS"
        / "ACTION_PROMPTS"
        / "IMPLEMENTATION_WORKFLOW",
    )
    for path in paths:
        value = str(path)
        if value not in sys.path:
            sys.path.insert(0, value)


def _add_lifecycle_handlers(available: dict[str, ActionHandler], root: Path) -> None:
    try:
        from selected_lifecycle_dispatch import lifecycle_handlers

        available.update(lifecycle_handlers(root))
    except ImportError:
        pass


def _add_project_structure_handlers(available: dict[str, ActionHandler], root: Path) -> None:
    try:
        from selected_project_structure_handlers import project_structure_handlers

        available.update(project_structure_handlers(root))
    except ImportError:
        pass


def _add_graph_projection_handlers(available: dict[str, ActionHandler], root: Path) -> None:
    try:
        from selected_graph_projection_handlers import graph_projection_handlers

        available.update(graph_projection_handlers(root))
    except ImportError:
        pass


def _revert_not_configured(_context: dict[str, Any]) -> dict[str, Any]:
    raise SelectedExecutionError(
        "CA-O-131 requires register_action_handler('CA-O-131', make_revert_action_handler(service))"
    )


def _add_implementation_handlers(
    available: dict[str, ActionHandler],
    root: Path,
    implementation_agent: ImplementationAgent | None,
) -> None:
    try:
        from selected_implementation_handlers import implementation_handlers

        available.update(
            implementation_handlers(root, cast(ImplementationAgent, implementation_agent))
        )
    except ImportError:
        pass
