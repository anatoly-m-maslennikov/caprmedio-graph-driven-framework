"""Public stateful facade for source-bound selected Workflow execution."""

from __future__ import annotations

from collections.abc import Callable, Mapping
from pathlib import Path
from typing import Any

from selected_evidence_io import atomic_write, bounded_read, run_directory, safe_path
from selected_execution_contracts import (
    ActionHandler,
    LifecycleAdmissionError,
    RUN_ID,
    SelectedExecutionError,
    canonical_json,
)
from selected_execution_registration import (
    action_handlers,
    implementation_agent as configured_implementation_agent,
    make_revert_action_handler,
    preflight_selected_lifecycle,
    register_action_handler,
    register_implementation_agent,
)
from selected_execution_run_plan import build_requested_runs as _plan_runs
from selected_freeze_state import (
    _validated_freeze,
    freeze as freeze_state,
    load as load_state,
    revalidate,
    validate_requested_runs,
)
from selected_graph_admission import validate_lifecycle_admission, validate_query_admission
from selected_graph_executor import execute_graph
from selected_graph_sources import manifest_relative_path
from selected_graph_validation import validate_graph


RunSupport = Callable[[Path, dict[str, Any], Callable[[Any], Mapping[str, Any]]], Mapping[str, Any]]


__all__ = [
    "ActionHandler",
    "LifecycleAdmissionError",
    "RUN_ID",
    "SelectedExecution",
    "SelectedExecutionError",
    "build_requested_runs",
    "canonical_json",
    "make_revert_action_handler",
    "manifest_relative_path",
    "preflight_selected_lifecycle",
    "register_action_handler",
    "register_implementation_agent",
]


class SelectedExecution:
    """Bind explicit executor state to canonical selected-Workflow capabilities."""

    def __init__(
        self,
        root: str | Path,
        *,
        handlers: Mapping[str, ActionHandler] | None = None,
        implementation_agent: Callable[[str, Mapping[str, Any]], Mapping[str, Any]] | None = None,
    ) -> None:
        self.root = Path(root).resolve(strict=True)
        self.implementation_agent = implementation_agent or configured_implementation_agent()
        self.handlers = {**self._native_handlers(), **action_handlers()}
        if handlers:
            self.handlers.update(handlers)

    def _native_handlers(self) -> dict[str, ActionHandler]:
        from selected_native_domain_handlers import source_bound_native_handlers

        available = source_bound_native_handlers(self.root, self.implementation_agent)
        try:
            # E540: optional compiler entrypoint sits outside the bounded import path.
            import compile_applicable_methodology  # type: ignore[import-not-found]
            from selected_compiler_handlers import compiler_handler

            for action_id, handler in compile_applicable_methodology.ACTION_ADAPTERS.items():
                available[action_id] = compiler_handler(
                    lambda: self.root, handler, available.get(action_id)
                )
        except ImportError:
            pass
        try:
            import query_actions

            available.update(query_actions.ACTION_HANDLERS)
        except ImportError:
            pass
        return available

    def run_directory(self, run_id: str) -> Path:
        return run_directory(self.root, run_id)

    def _safe_path(self, relative: str) -> Path:
        return safe_path(self.root, relative)

    @staticmethod
    def _write(path: Path, value: object) -> None:
        atomic_write(path, value)

    @staticmethod
    def _read(path: Path) -> dict[str, Any]:
        return bounded_read(path)

    def _validate_graph(self, execution: Mapping[str, Any]) -> dict[str, Any]:
        return validate_graph(self.root, execution)

    @staticmethod
    def _validate_query_admission(graph: Mapping[str, Any], execution: Mapping[str, Any]) -> None:
        validate_query_admission(graph, execution)

    def _validate_lifecycle_admission(
        self,
        graph: Mapping[str, Any],
        execution: Mapping[str, Any],
        *,
        expected_admission: Mapping[str, Any] | None = None,
    ) -> dict[str, Any] | None:
        return validate_lifecycle_admission(
            self.root, graph, execution, expected_admission=expected_admission
        )

    @classmethod
    def build_requested_runs(
        cls,
        graph: Mapping[str, Any],
        run_id: str,
        run_visit_limits: Mapping[str, int] | None = None,
    ) -> list[dict[str, Any]]:
        return _plan_runs(graph, run_id, run_visit_limits)

    def _validate_requested_runs(
        self, execution: Mapping[str, Any], graph: Mapping[str, Any], run_id: str
    ) -> None:
        validate_requested_runs(self.root, execution, graph, run_id)

    def _validated_freeze(self, request: Mapping[str, Any]) -> dict[str, Any]:
        return _validated_freeze(self.root, request)

    def freeze(self, request: Mapping[str, Any]) -> dict[str, Any]:
        return freeze_state(self.root, request)

    def load(self, run_id: str) -> dict[str, Any]:
        return load_state(self.root, run_id)

    def _revalidate(self, frozen: Mapping[str, Any]) -> dict[str, Any]:
        return revalidate(self.root, frozen)

    def _execute_graph(
        self, frozen: Mapping[str, Any], session: Any, *, recovery: bool = False
    ) -> dict[str, Any]:
        return execute_graph(self.root, self.handlers, frozen, session, recovery=recovery)

    def _shared_tracker(self, frozen: Mapping[str, Any]) -> Any:
        from selected_run_session import shared_tracker

        return shared_tracker(self.root, self.handlers, frozen)

    def _shared_dispatch(self, frozen: Mapping[str, Any]) -> dict[str, Any]:
        from selected_run_session import shared_dispatch

        return shared_dispatch(self.root, self.handlers, frozen)

    def reconcile_graph_recording(
        self, frozen: Mapping[str, Any], *, persist: bool = True
    ) -> dict[str, Any]:
        from selected_graph_reconciliation import reconcile_graph_recording

        return reconcile_graph_recording(self.root, self.handlers, frozen, persist=persist)

    def _dispatch_confirmed_subject(
        self, frozen: Mapping[str, Any], confirmation: object
    ) -> dict[str, Any]:
        from selected_dispatch import dispatch_confirmed_subject

        return dispatch_confirmed_subject(self.root, self.handlers, frozen, confirmation)

    def dispatch(
        self, frozen: Mapping[str, Any], *, run_support: RunSupport | None = None
    ) -> dict[str, Any]:
        from selected_dispatch import dispatch

        return dispatch(self.root, self.handlers, frozen, run_support=run_support)


def build_requested_runs(
    graph: Mapping[str, Any],
    run_id: str,
    run_visit_limits: Mapping[str, int] | None = None,
) -> list[dict[str, Any]]:
    return SelectedExecution.build_requested_runs(graph, run_id, run_visit_limits)
