# CA-M-504@2
"""Explicit built-in native Action handlers for selected Workflow execution."""

from __future__ import annotations

from pathlib import Path
import sys
from typing import Any

from selected_execution_contracts import ActionHandler, SelectedExecutionError


def source_bound_native_handlers(
    root: Path,
) -> dict[str, ActionHandler]:
    """Load the fixed built-in domains; manifests still select every Action."""
    _add_domain_import_paths()
    available: dict[str, ActionHandler] = {}
    _add_lifecycle_handlers(available, root)
    _add_graph_projection_handlers(available, root)
    available["CA-O-131"] = _revert_not_configured
    return available


def _add_domain_import_paths() -> None:
    tools_root = Path(__file__).resolve().parents[2] / "FEATURE_TOOLS"
    paths = (
        tools_root,
        tools_root / "GENERATE_ENTITY_GRAPH",
        tools_root / "COMPILE_APPLICABLE_METHODOLOGY",
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
