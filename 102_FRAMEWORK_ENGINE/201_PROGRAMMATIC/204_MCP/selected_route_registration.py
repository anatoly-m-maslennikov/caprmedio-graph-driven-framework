"""MCP registration for selected routes."""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Any, Callable, Protocol, cast

from selected_route_spec import DirectLocalReleaseRequest, DirectPublicReleaseRequest


class ToolServer(Protocol):
    def tool(
        self, *, name: str, structured_output: bool, annotations: Any
    ) -> Callable[[Callable[..., Any]], Callable[..., Any]]: ...


def _public_module() -> Any:
    return sys.modules.get("selected_routes")


def register_selected_routes(
    server: ToolServer, root: str | Path, *, tool_blacklist: frozenset[str] = frozenset()
) -> Any:
    """Register direct Release commands and fully admitted ordinary routes."""
    from mcp.types import ToolAnnotations

    public = _public_module()
    adapter = public.SelectedRouteAdapter(root, strict_manifest=False)
    try:
        adapter.manifest = public.load_selected_manifest(adapter.root)
        adapter.routes = {
            entry["route"]: entry
            for entry in adapter.manifest["routes"]
            if entry["route"] in public.ADMITTED_SELECTED_ROUTE_NAMES
        }
    except OSError, ValueError:
        pass
    selected_annotations = ToolAnnotations(
        read_only_hint=False, destructive_hint=False, idempotent_hint=True, open_world_hint=False
    )
    query_annotations = ToolAnnotations(
        read_only_hint=True, destructive_hint=False, idempotent_hint=True, open_world_hint=False
    )
    observation_annotations = ToolAnnotations(
        read_only_hint=True, destructive_hint=False, idempotent_hint=True, open_world_hint=False
    )
    release_annotations = ToolAnnotations(
        read_only_hint=False, destructive_hint=True, idempotent_hint=False, open_world_hint=False
    )
    public_route_names = (
        *adapter.routes,
        public._OPTIONAL_RELEASE_ROUTE_NAME,
        public._OPTIONAL_PUBLIC_RELEASE_ROUTE_NAME,
    )
    adapter.public_route_names = frozenset(public_route_names) - tool_blacklist

    for route_name in sorted(adapter.routes.keys() - tool_blacklist):

        def add_route(route: str) -> None:
            @server.tool(
                name=route,
                structured_output=True,
                annotations=(
                    query_annotations if route in public.QUERY_ROUTE_NAMES else selected_annotations
                ),
            )
            def selected_route(request: dict[str, Any]) -> dict[str, Any]:
                """Preview ordinary routes before their explicit authorized execute."""
                return cast(
                    dict[str, Any],
                    public._guard_public_call(
                        adapter, route, request, lambda: adapter.invoke(route, request)
                    ),
                )

        add_route(route_name)

    def release_version(request: DirectLocalReleaseRequest) -> dict[str, Any]:
        return cast(
            dict[str, Any],
            public._guard_public_call(
                adapter,
                public._OPTIONAL_RELEASE_ROUTE_NAME,
                request,
                lambda: adapter.invoke(public._OPTIONAL_RELEASE_ROUTE_NAME, request),
            ),
        )

    def public_release(request: DirectPublicReleaseRequest) -> dict[str, Any]:
        return cast(
            dict[str, Any],
            public._guard_public_call(
                adapter,
                public._OPTIONAL_PUBLIC_RELEASE_ROUTE_NAME,
                request,
                lambda: adapter.invoke(public._OPTIONAL_PUBLIC_RELEASE_ROUTE_NAME, request),
            ),
        )

    def get_selected_workflow_run(request: dict[str, Any]) -> dict[str, Any]:
        return cast(
            dict[str, Any],
            public._guard_public_call(
                adapter,
                "get_selected_workflow_run",
                request,
                lambda: adapter.get_workflow_run(request),
            ),
        )

    def get_selected_action_run(request: dict[str, Any]) -> dict[str, Any]:
        return cast(
            dict[str, Any],
            public._guard_public_call(
                adapter,
                "get_selected_action_run",
                request,
                lambda: adapter.get_action_run(request),
            ),
        )

    controls = {
        public._OPTIONAL_RELEASE_ROUTE_NAME: (release_version, release_annotations),
        public._OPTIONAL_PUBLIC_RELEASE_ROUTE_NAME: (public_release, release_annotations),
        "get_selected_workflow_run": (get_selected_workflow_run, observation_annotations),
        "get_selected_action_run": (get_selected_action_run, observation_annotations),
    }
    for name in sorted(controls.keys() - tool_blacklist):
        handler, annotations = controls[name]
        server.tool(name=name, structured_output=True, annotations=annotations)(
            cast(Callable[..., Any], handler)
        )
    return adapter
