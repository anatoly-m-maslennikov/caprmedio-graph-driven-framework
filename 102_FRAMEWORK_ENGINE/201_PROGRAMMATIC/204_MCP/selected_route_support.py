"""Public error boundary and common adapter support."""

from __future__ import annotations

import sys
from dataclasses import replace
from pathlib import Path
from typing import Any, Callable, Mapping, TYPE_CHECKING

from operation_error_boundary import (
    FailureRecord,
    classify_failure,
    emit_failure_diagnostic,
    operation_error_boundary,
)
from technical_diagnostics import make_technical_logger
from project_selection import active_selection

if TYPE_CHECKING:
    from selected_routes import SelectedRouteAdapter


def _public_module() -> Any:
    return sys.modules.get("selected_routes")


def _public_logger(root: Path) -> Any:
    try:
        selection = active_selection(root)
        logger, _error = make_technical_logger(selection.settings, root)
        return replace(logger, component="MCP_SELECTED_ROUTES") if logger is not None else None
    except Exception:
        return None


def _log_structured_failure(
    root: Path, operation: str, request: Any, *, disposition: str
) -> str | None:
    public = _public_module()
    logger = (
        getattr(public, "_public_logger", _public_logger)(root) if public else _public_logger(root)
    )
    code = {
        "rejected": "input_invalid",
        "blocked": "operation_blocked",
        "failed": "operation_failed",
    }.get(disposition, "operation_failed")
    failure = FailureRecord("WARNING", code, "public operation did not complete")
    return emit_failure_diagnostic(
        logger,
        failure,
        operation=operation,
        correlation_id=(
            request.get("request_id")
            if isinstance(request, Mapping) and isinstance(request.get("request_id"), str)
            else None
        ),
    )


def _public_boundary_result(
    adapter: "SelectedRouteAdapter", route: str, request: Any, error: Exception
) -> dict[str, Any]:
    public = _public_module()
    logger_factory = getattr(public, "_public_logger", _public_logger) if public else _public_logger
    failure = classify_failure(error)
    diagnostic_error = emit_failure_diagnostic(
        logger_factory(adapter.root),
        failure,
        operation=route,
        correlation_id=(
            request.get("request_id")
            if isinstance(request, Mapping) and isinstance(request.get("request_id"), str)
            else None
        ),
    )
    disposition = "blocked" if failure.severity == "ERROR" else "failed"
    result = adapter._result(
        request, disposition, disposition, f"{failure.code}: {failure.message}", log=False
    )
    if diagnostic_error:
        result["diagnostics"].append("technical diagnostic unavailable")
    return result


def _guard_public_call(
    adapter: "SelectedRouteAdapter", route: str, request: Any, call: Callable[[], Any]
) -> Any:
    return operation_error_boundary(
        on_error=lambda error: _public_boundary_result(adapter, route, request, error)
    )(call)()


class _SelectedRouteAdapterBase:
    """Validate the closed projection, then call shared run support once."""

    def __init__(
        self, root: str | Path, service: Any | None = None, *, strict_manifest: bool = True
    ) -> None:
        self.root = Path(root).resolve(strict=True)
        self.manifest: dict[str, Any] | None = None
        self.routes: dict[str, dict[str, Any]] = {}
        public = _public_module()
        if strict_manifest:
            loader = getattr(public, "load_selected_manifest")
            self.manifest = loader(self.root)
            self.routes = {entry["route"]: entry for entry in self.manifest["routes"]}
        self.service = service

    def _result(
        self, request: Any, disposition: str, outcome: str, diagnostic: str, *, log: bool = True
    ) -> dict[str, Any]:
        value: dict[str, Any] = {
            "disposition": disposition,
            "outcome": outcome,
            "diagnostics": [diagnostic],
        }
        if isinstance(request, Mapping) and isinstance(request.get("request_id"), str):
            value["request_id"] = request["request_id"]
        if log:
            public = _public_module()
            logger = (
                getattr(public, "_log_structured_failure", _log_structured_failure)
                if public
                else _log_structured_failure
            )
            error = logger(
                self.root,
                str(request.get("operation_route", "selected_route"))
                if isinstance(request, Mapping)
                else "selected_route",
                request,
                disposition=disposition,
            )
            if error:
                value["diagnostics"].append("technical diagnostic unavailable")
        return value

    def _support(self) -> Any | None:
        if self.service is not None:
            return self.service
        from selected_route_queue import _QueueBackedSelectedSupport

        return _QueueBackedSelectedSupport(self.root, self)
