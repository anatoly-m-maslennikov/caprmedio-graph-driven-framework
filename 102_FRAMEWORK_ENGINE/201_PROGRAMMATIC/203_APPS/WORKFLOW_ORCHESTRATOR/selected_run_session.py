"""Shared selected-Run session capabilities."""

from __future__ import annotations

from collections.abc import Callable, Mapping
from pathlib import Path
import sys
from typing import Any

import selected_freeze_state
from selected_execution_contracts import (
    ActionHandler,
    SelectedExecutionError,
    canonical_json,
)
from selected_graph_admission import _lifecycle_preflight
from selected_graph_executor import execute_graph


SessionExecutor = Callable[[Any], Mapping[str, Any]]
RunSupport = Callable[[Path, dict[str, Any], SessionExecutor], Mapping[str, Any]]


def execute_admitted_session(
    root: Path,
    handlers: Mapping[str, ActionHandler],
    frozen: Mapping[str, Any],
    session: Any,
) -> dict[str, Any]:
    """Execute one already-admitted selected graph through its Run session."""
    execution = frozen["request"]["execution"]
    parameters = execution.get("parameters")
    if (
        execution.get("operation_route") == "update_atom"
        and isinstance(parameters, Mapping)
        and "subject_batch" in parameters
    ):
        from subject_batch_execution import execute_subject_batch

        return execute_subject_batch(root, frozen, session)
    return execute_graph(root, handlers, frozen, session)


def shared_tracker(
    root: Path,
    handlers: Mapping[str, ActionHandler],
    frozen: Mapping[str, Any],
) -> Any:
    """Construct the shared Run tracker with source-bound currentness."""
    tools_root = str(Path(__file__).resolve().parents[2] / "201_TOOLS")
    if tools_root not in sys.path:
        sys.path.insert(0, tools_root)
    from workflow_run_support import RunTracker

    def observe(request: dict[str, Any]) -> dict[str, Any]:
        graph = selected_freeze_state.revalidate(root, frozen)
        lifecycle_admission = (
            _lifecycle_preflight(root, {"parameters": request.get("parameters")})
            if graph.get("route") == "change_atom_status"
            else None
        )
        lifecycle_current = lifecycle_admission is None or canonical_json(
            lifecycle_admission
        ) == canonical_json(frozen.get("lifecycle_admission"))
        observed: dict[str, Any] = {
            "manifest_ref": graph["manifest_ref"],
            "manifest_digest": graph["manifest_digest"],
        }
        if lifecycle_admission is not None:
            observed["lifecycle_admission"] = lifecycle_admission
        return {
            "selected": request.get("operation_route") == graph["route"],
            "current": lifecycle_current,
            "observed": observed,
        }

    return RunTracker(
        root,
        source_observer=observe,
        executor=lambda _request, session: execute_admitted_session(
            root, handlers, frozen, session
        ),
    )


def shared_dispatch(
    root: Path,
    handlers: Mapping[str, ActionHandler],
    frozen: Mapping[str, Any],
    *,
    run_support: RunSupport | None = None,
) -> dict[str, Any]:
    """Dispatch through shared Run support or an explicitly injected support."""
    if run_support is None:
        result = shared_tracker(root, handlers, frozen).run_selected_operation(
            dict(frozen["request"]["execution"])
        )
    else:
        result = run_support(
            root,
            dict(frozen["request"]["execution"]),
            lambda session: execute_admitted_session(root, handlers, frozen, session),
        )
    if not isinstance(result, Mapping):
        raise SelectedExecutionError("shared selected Run support returned an invalid result")
    return dict(result)
