"""Selected-route adapter API."""

from __future__ import annotations

import sys
from typing import Any, Callable, Mapping, cast

from selected_route_request import (
    expected_revisions,
    preflight_lifecycle,
    validate_execute,
    validate_request,
)
from selected_route_spec import (
    _OPTIONAL_PUBLIC_RELEASE_ROUTE_NAME,
    _OPTIONAL_RELEASE_ROUTE_NAME,
    SelectedRouteError,
)
from selected_route_support import _SelectedRouteAdapterBase, _log_structured_failure
from selected_route_interactive import (
    _public_pending,
    invoke_integrated_execute,
    invoke_submit_result,
    is_current_integrated_execute,
    is_submit_result,
)


def _public_module() -> Any:
    return sys.modules.get("selected_routes")


class SelectedRouteAdapter(_SelectedRouteAdapterBase):
    def _preflight_lifecycle(self, request: Mapping[str, Any]) -> dict[str, Any] | None:
        return preflight_lifecycle(self, request)

    def _validate_request(self, route: str, request: Any) -> dict[str, Any]:
        return validate_request(self, route, request)

    def _expected_revisions(self, route: str) -> list[dict[str, Any]]:
        return expected_revisions(self, route)

    def _validate_execute(self, request: Mapping[str, Any]) -> str | None:
        return validate_execute(request)

    def invoke(self, route: str, request: Any) -> dict[str, Any]:
        if route in {_OPTIONAL_RELEASE_ROUTE_NAME, _OPTIONAL_PUBLIC_RELEASE_ROUTE_NAME}:
            public = _public_module()
            return cast(
                dict[str, Any],
                getattr(public, "_invoke_direct_release")(self.root, route, request),
            )
        if route == "run_implementation_workflow" and is_submit_result(request):
            return invoke_submit_result(self, request)
        try:
            public = _public_module()
            self.manifest = public.load_selected_manifest(self.root)
            self.routes = {entry["route"]: entry for entry in self.manifest["routes"]}
            normalized = self._validate_request(route, request)
        except SelectedRouteError as error:
            return self._result(request, "rejected", "rejected", str(error))
        if normalized["mode"] == "execute":
            blocked = self._validate_execute(normalized)
            if blocked:
                return self._result(normalized, "blocked", "blocked", blocked)
        refusal = self._preflight_lifecycle(normalized)
        if refusal is not None:
            return refusal
        return self._invoke_validated(route, normalized)

    def _invoke_validated(self, route: str, normalized: dict[str, Any]) -> dict[str, Any]:
        support = self._support()
        if support is None:
            value = {
                "request_id": normalized["request_id"],
                "disposition": "blocked",
                "outcome": "implementation_gap",
                "source_freshness": normalized["source_freshness"],
                "diagnostics": ["shared implement_run_support is unavailable"],
            }
            public = _public_module()
            logger = (
                getattr(public, "_log_structured_failure", _log_structured_failure)
                if public
                else _log_structured_failure
            )
            diagnostic_error = logger(self.root, route, normalized, disposition="blocked")
            if diagnostic_error:
                value["diagnostics"].append("technical diagnostic unavailable")
            return value
        if is_current_integrated_execute(self.routes.get(route), normalized):
            return invoke_integrated_execute(self, normalized, support)
        try:
            handler: Callable[[dict[str, Any]], dict[str, Any]] = getattr(
                support, "run_selected_operation"
            )
            return handler(normalized)
        except (AttributeError, TypeError, ValueError, RuntimeError) as error:
            return self._result(
                normalized, "blocked", "blocked", f"shared support rejected request: {error}"
            )

    def _observe(self, method: str, request: Any, required_key: str) -> dict[str, Any]:
        if (
            not isinstance(request, Mapping)
            or set(request) != {required_key}
            or not isinstance(request[required_key], str)
            or not request[required_key]
        ):
            return self._result(
                request, "rejected", "rejected", f"{method} requires one exact {required_key}"
            )
        support = self._support()
        if support is None or not hasattr(support, method):
            return self._result(
                request,
                "blocked",
                "implementation_gap",
                "shared implement_run_support observation is unavailable",
            )
        try:
            observed = getattr(support, method)(dict(request))
            if method == "get_selected_workflow_run" and isinstance(observed, Mapping):
                return _public_pending(observed)
            return cast(dict[str, Any], observed)
        except (TypeError, ValueError, RuntimeError) as error:
            return self._result(
                request, "blocked", "blocked", f"shared support rejected observation: {error}"
            )

    def get_workflow_run(self, request: Any) -> dict[str, Any]:
        return self._observe("get_selected_workflow_run", request, "run_id")

    def get_action_run(self, request: Any) -> dict[str, Any]:
        return self._observe("get_selected_action_run", request, "action_run_id")
