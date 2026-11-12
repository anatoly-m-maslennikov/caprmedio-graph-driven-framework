# CA-M-1008@1
# CA-R-1115@24
# CA-M-512@2
# CA-M-517@1
from __future__ import annotations

# CA-M-322@13
# CA-R-1820@9
# CA-M-506@2
# CA-D-673@14

import asyncio
from collections.abc import Awaitable
from contextlib import nullcontext
from typing import Any, Callable

from mcp import types
from mcp.server.lowlevel import Server

from health_observations import MAX_OBSERVATIONS, HealthObservations
from direct_gateway import DirectGateway
from caller_context import CallerContextError, take_caller_context
from workbench_tools import mcp_app_probe
from host_runtime_config import (
    HostRuntimeConfig,
    HostRuntimeConfigError,
    _canonical_directory,
    load_host_runtime_config,
    resolve_host_project,
)
from project_selection import ProjectSelection, ProjectSelectionError, bind_selection
from shared_project_catalog import contract_digest, discover_frontier, native_tools
from shared_project_pool import ProjectCapacityError, SharedProjectPool
from shared_gateway_support import record_observation, refusal
from runtime_request_context import bind_request_context
from tool_registry_runtime import ToolRegistryStaleError


class SharedGatewayRefusal(ValueError):
    """A caller-visible refusal which never picks a different Project."""

    def __init__(self, code: str) -> None:
        self.code = code
        super().__init__(code)


def _project_context(selection: ProjectSelection) -> tuple[str, str]:
    try:
        prefix = selection.settings["artifacts"]["identity"]["project_prefix"]
    except (KeyError, TypeError) as error:
        raise SharedGatewayRefusal("invalid_project_root") from error
    if not isinstance(prefix, str):
        raise SharedGatewayRefusal("invalid_project_root")
    return prefix, selection.instance_id


class SharedGateway:
    """Project selection adapter; native Gateways retain all domain behavior."""

    def __init__(
        self, config: HostRuntimeConfig, gateway_factory: Callable[..., Any] = DirectGateway
    ) -> None:
        self.config = config
        self.gateway_factory = gateway_factory
        self.pool = SharedProjectPool(config.max_loaded_projects, gateway_factory)
        self.frontier = None
        self.ready = False
        self.tools = []
        self.server = None
        self._known_projects: dict[str, dict[str, str]] = {}
        self.health_observations = HealthObservations()

    async def initialize(self) -> None:
        if self.ready:
            return
        self.frontier = await discover_frontier(self.config, self.gateway_factory)
        self.tools = [contract.tool for contract in self.frontier.tools.values()]
        self.ready = True

    async def close(self) -> None:
        self.ready = False
        await self.pool.close()

    def status(self) -> dict[str, object]:
        frontier = self.frontier
        return {
            "shared_runtime_id": self.config.shared_runtime_id,
            "initialized": self.ready,
            "advertised_tools": sorted(frontier.tools) if frontier is not None else [],
            "warnings": list(frontier.warnings) if frontier is not None else [],
            "known_project_contexts": list(self._known_projects.values()),
            **self.pool.status(),
            **self.health_observations.snapshot(),
        }

    def _current_config(self) -> None:
        try:
            current = load_host_runtime_config(self.config.source_path)
        except HostRuntimeConfigError as error:
            raise SharedGatewayRefusal("host_configuration_invalid") from error
        if current != self.config:
            raise SharedGatewayRefusal("host_configuration_stale")

    def _selection(self, value: object) -> ProjectSelection:
        if not isinstance(value, str):
            raise SharedGatewayRefusal("invalid_project_root")
        try:
            return resolve_host_project(self.config, value)
        except HostRuntimeConfigError as error:
            code = "outside_project_root" if "outside" in str(error) else "invalid_project_root"
            raise SharedGatewayRefusal(code) from error
        except ProjectSelectionError as error:
            raise SharedGatewayRefusal("invalid_project_root") from error

    def _project_arguments(self, arguments: Any) -> tuple[ProjectSelection, dict[str, Any]]:
        if not isinstance(arguments, dict) or "project_root" not in arguments:
            raise SharedGatewayRefusal("missing_project_root")
        selection = self._selection(arguments["project_root"])
        return selection, {key: value for key, value in arguments.items() if key != "project_root"}

    def _current_tool(self, entry: Any, selection: ProjectSelection, name: str) -> None:
        if (
            entry.selection.provenance != selection.provenance
            or entry.selection.instance_id != selection.instance_id
        ):
            raise SharedGatewayRefusal("project_declarations_stale")
        registry = getattr(entry.gateway, "registry", None)
        if registry is not None:
            try:
                registry.ensure_current()
            except ToolRegistryStaleError as error:
                raise SharedGatewayRefusal("tool_registry_stale") from error
        advertised = self.frontier.tools.get(name)
        if advertised is None:
            raise SharedGatewayRefusal("tool_unavailable")
        tools = {tool.name: tool for tool in native_tools(entry.gateway)}
        native = tools.get(name)
        if native is None or contract_digest(native) != advertised.digest:
            raise SharedGatewayRefusal("project_tool_frontier_stale")

    def _remember_project(self, prefix: str, instance_id: str) -> None:
        self._known_projects.pop(instance_id, None)
        self._known_projects[instance_id] = {"prefix": prefix, "instance_id": instance_id}
        if len(self._known_projects) > MAX_OBSERVATIONS:
            self._known_projects.pop(next(iter(self._known_projects)))

    @staticmethod
    def _failure_code(error: Exception) -> str:
        if isinstance(error, SharedGatewayRefusal):
            return error.code
        if isinstance(error, ProjectCapacityError):
            return "project_gateway_busy"
        return "shared_gateway_failure"

    async def _lifecycle_selection(self, arguments: Any) -> tuple[Any, ProjectSelection, dict[str, Any]]:
        if not isinstance(arguments, dict) or "project_root" not in arguments:
            raise SharedGatewayRefusal("missing_project_root")
        value = arguments["project_root"]
        if not isinstance(value, str):
            raise SharedGatewayRefusal("invalid_project_root")
        try:
            root = _canonical_directory(value)
        except HostRuntimeConfigError as caught:
            raise SharedGatewayRefusal("invalid_project_root") from caught
        if root == self.config.projects_root or not root.is_relative_to(self.config.projects_root):
            raise SharedGatewayRefusal("outside_project_root")
        self._current_config()
        entry = await self.pool.acquire_cached(root)
        if entry is None:
            selection = self._selection(value)
            entry = await self.pool.acquire(selection)
        else:
            selection = entry.selection
        native = {key: item for key, item in arguments.items() if key != "project_root"}
        return entry, selection, native

    async def _backend_call(
        self,
        name: str,
        arguments: Any,
        selection_for: Callable[[], tuple[ProjectSelection, dict[str, Any]]],
        invoke: Callable[[Any, dict[str, Any]], Awaitable[Any]],
    ) -> tuple[Any, str | None, ProjectSelection | None]:
        """Run either transport through one selected native Project lease."""
        response = None
        error = None
        entry = None
        selection = None
        try:
            if self.frontier is None:
                raise SharedGatewayRefusal("shared_gateway_unavailable")
            if name.startswith("atom_lifecycle_"):
                entry, selection, native_arguments = await self._lifecycle_selection(arguments)
                refreshed = selection
            else:
                selection, native_arguments = selection_for()
                self._current_config()
                entry = await self.pool.acquire(selection)
                refreshed = self._selection(str(selection.root))
            self._current_config()
            self._current_tool(entry, refreshed, name)
            prefix, identity = _project_context(refreshed)
            self._remember_project(prefix, identity)
            with bind_selection(refreshed):
                response = await invoke(entry.gateway, native_arguments)
            return response, None, selection
        except asyncio.CancelledError as caught:
            error = caught
            raise
        except (OSError, RuntimeError, TypeError, ValueError, ProjectCapacityError) as caught:
            error = caught
            code = self._failure_code(caught)
            response = {"outcome": "rejected", "diagnostics": [code]}
            return response, code, selection
        except Exception:
            response = {"outcome": "failed", "is_error": True}
            raise
        finally:
            if entry is not None:
                await self.pool.release(entry)
            prefix, identity = (
                _project_context(selection) if selection is not None else (None, None)
            )
            record_observation(
                self.health_observations,
                name,
                arguments,
                response,
                error,
                root=selection.root if selection is not None else None,
                project_prefix=prefix,
                project_instance_id=identity,
            )

    async def workbench_call(self, name: str, arguments: dict[str, Any]) -> dict[str, Any]:
        """Call the native Workbench API without an MCP request/result envelope."""
        async def invoke(gateway: Any, native_arguments: dict[str, Any]) -> dict[str, Any]:
            value = await gateway.workbench.call(name, native_arguments)
            if not isinstance(value, dict):
                raise RuntimeError("Workbench returned an invalid result")
            return value

        response, code, _selection = await self._backend_call(
            name, arguments, lambda: self._project_arguments(arguments), invoke
        )
        if code is not None:
            raise SharedGatewayRefusal(code)
        return response

    async def call(self, context: Any, params: Any) -> types.CallToolResult:
        try:
            arguments, request_context = take_caller_context(getattr(params, "arguments", None))
        except CallerContextError as error:
            return refusal(str(error), None)
        with bind_request_context(request_context) if request_context else nullcontext():
            response, code, selection = await self._backend_call(
                params.name,
                arguments,
                lambda: self._project_arguments(arguments),
                lambda gateway, native_arguments: gateway.call(
                    context, params.model_copy(update={"arguments": native_arguments})
                ),
            )
        if code is not None:
            return refusal(code, selection.root if selection is not None else None)
        return response

    def build_server(self) -> Server:
        async def list_tools(_context: Any, _params: Any) -> types.ListToolsResult:
            tools = (
                []
                if self.frontier is None
                else [item.tool for item in self.frontier.tools.values()]
            )
            return types.ListToolsResult(tools=tools)

        self.server = Server(
            "CAPRMEDIO", version="0.2.0", on_list_tools=list_tools, on_call_tool=self.call,
            on_list_resources=mcp_app_probe.list_resources,
            on_read_resource=mcp_app_probe.read_resource,
        )
        return self.server


__all__ = ["SharedGateway", "SharedGatewayRefusal"]
