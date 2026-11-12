# CA-R-3013@2
# CA-M-506@6
# CA-M-512@2
# CA-M-517@1

"""In-process MCP gateway for the Project-owned Workbench."""

import asyncio
from concurrent.futures import CancelledError as FutureCancelledError
from contextlib import nullcontext, redirect_stdout
import json
from pathlib import Path
import sys

from mcp import types
from mcp.server.lowlevel import Server
from mcp.server.stdio import stdio_server

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "FEATURE_TOOLS"))
from caller_context import CallerContextError, take_caller_context  # noqa: E402
from health_observations import HealthObservations  # noqa: E402
from operation_error_boundary import (  # noqa: E402
    FailureRecord, operation_error_boundary,
)
from project_selection import (  # noqa: E402
    ProjectSelection, bind_selection, resolve_project, rebind_selection,
)
from project_tool_blacklist import project_tool_blacklist  # noqa: E402
from project_tool_context import native_arguments  # noqa: E402
from runtime_failure_diagnostics import report_failure  # noqa: E402
from runtime_request_context import bind_request_context  # noqa: E402
from shared_tool_contract import public_tool  # noqa: E402
from tool_registry_runtime import (  # noqa: E402
    ToolInputValidationError, ToolOutputValidationError, ToolRegistryRuntimeError,
    ToolRegistryStaleError,
    load_active_registry,
)
from workbench_tools import WorkbenchTools, mcp_app_probe  # noqa: E402


def startup_selection(root, control_root=None, instance_id=None, host_root=None):
    selection = resolve_project(root, control_root)
    if host_root is not None and instance_id is None:
        raise ValueError("Host Project binding requires an explicit instance identity")
    return rebind_selection(selection, instance_id, host_root=host_root) if instance_id is not None else selection


def result(value, error=False):
    return types.CallToolResult(
        content=[types.TextContent(type="text", text=json.dumps(value))],
        structured_content=value, is_error=error,
    )


class DirectGateway:
    """Keep native Workbench calls within their selected Project and request."""

    def __init__(self, root, *, selection=None):
        self.root = Path(root).resolve(strict=True)
        if selection is not None and (not isinstance(selection, ProjectSelection) or selection.root != self.root):
            raise ValueError("Gateway selection belongs to another Project")
        self.selection = selection
        self.tool_blacklist = frozenset()
        self.tools = ()
        self.registry = None
        self.ready = False
        self.server = None
        self.workbench = WorkbenchTools(self.root)
        self.health_observations = HealthObservations()

    async def initialize(self):
        if self.ready:
            return
        with bind_selection(self.selection) if self.selection is not None else nullcontext():
            project_blacklist = project_tool_blacklist(self.root)
        try:
            self.registry = load_active_registry(Path(__file__).parent, self.root, self)
        except ToolRegistryRuntimeError as error:
            report_failure(
                self.root,
                FailureRecord("ERROR", "tool_registry_unavailable", "MCP tool registry is unavailable"),
                component="MCP_GATEWAY", operation="initialize",
            )
            raise error
        self.tool_blacklist = self.registry.global_blacklist | project_blacklist
        self.tools = tuple(tool for tool in self.registry.tools if tool.name not in self.tool_blacklist)
        if self.selection is not None:
            try:
                consistency = await asyncio.to_thread(self.workbench.project_consistency)
            except Exception:
                await self.close()
                raise
            print(json.dumps({"event": "project_consistency",
                              "severity": "WARNING" if consistency.get("audit_error") or any(
                                  type(value) is int and value for value in consistency.values()
                              ) else "INFO",
                              **consistency}), flush=True)
        self.ready = True

    async def close(self):
        self.ready = False
        if self.registry is not None:
            await self.registry.close()
            self.registry = None
        await self.workbench.close()

    def status(self):
        return {"runtime": "single_process", "ready": self.ready,
                "advertised_tools": [tool.name for tool in self.tools]}

    def _failure(self, error, operation):
        failure, secondary = report_failure(
            self.root, error, component="MCP_GATEWAY", operation=operation,
        )
        diagnostics = [f"{failure.code}: {failure.message}"]
        if secondary:
            diagnostics.append("technical diagnostic unavailable")
        return result({"outcome": "failed", "diagnostics": diagnostics}, True)

    def _input_rejection(self, operation):
        report_failure(
            self.root,
            FailureRecord("WARNING", "tool_input_invalid", "Tool input does not match its schema"),
            component="MCP_GATEWAY", operation=operation,
        )
        return result({"outcome": "rejected", "diagnostics": ["tool_input_invalid"]}, True)

    def _runtime_failure(self, code, message, operation):
        return self._failure(FailureRecord("ERROR", code, message), operation)

    def _registry_failure(self, error, operation):
        if isinstance(error, ToolRegistryStaleError):
            return result({"outcome": "rejected", "diagnostics": ["tool_registry_stale"]}, True)
        return self._runtime_failure(
            "tool_runtime_failure", "MCP tool runtime is unavailable", operation
        )

    async def _invoke_bound(self, context, params, arguments):
        try:
            arguments, request_context = take_caller_context(arguments)
        except CallerContextError as error:
            return result({"outcome": "rejected", "diagnostics": [str(error)]}, True)
        if self.registry is None or params.name in self.tool_blacklist or not self.registry.permits(params.name):
            return result({"outcome": "rejected", "diagnostics": ["Unknown Tool"]}, True)
        with (bind_request_context(request_context) if request_context else nullcontext(),
              bind_selection(self.selection) if self.selection is not None else nullcontext()):
            try:
                return await self._call(context, params.name, arguments)
            except ToolInputValidationError:
                return self._input_rejection(params.name)
            except ToolOutputValidationError:
                return self._runtime_failure(
                    "tool_output_invalid", "Tool output does not match its schema", params.name,
                )
            except ToolRegistryRuntimeError as error:
                return self._registry_failure(error, params.name)

    async def call(self, context, params):
        response = None
        error = None

        def on_error(caught):
            nonlocal error
            error = caught
            return self._failure(caught, params.name)

        @operation_error_boundary(on_error=on_error)
        async def guarded_call():
            arguments = native_arguments(params.arguments, self.selection, self.root)
            return await self._invoke_bound(context, params, arguments)

        try:
            response = await guarded_call()
            return response
        except (asyncio.CancelledError, FutureCancelledError) as caught:
            error = caught
            raise
        finally:
            try:
                self.health_observations.record(
                    params.name, getattr(params, "arguments", None), response, error=error,
                )
            except FutureCancelledError:
                raise
            except Exception:
                report_failure(
                    self.root,
                    FailureRecord("WARNING", "health_observation_failed", "health observations unavailable"),
                    component="MCP_GATEWAY", operation="health_observations",
                )

    async def _call(self, context, name, arguments):
        if self.registry is None:
            raise ToolRegistryRuntimeError("tool-registry-unavailable")
        return result(await self.registry.call(name, arguments, context=context))

    def build_server(self):
        async def list_tools(context, params):
            return types.ListToolsResult(tools=[public_tool(tool, required=False) for tool in self.tools])

        self.server = Server(
            "CAPRMEDIO", version="0.2.0", on_list_tools=list_tools, on_call_tool=self.call,
            on_list_resources=mcp_app_probe.list_resources,
            on_read_resource=mcp_app_probe.read_resource,
        )
        return self.server

    async def serve(self):
        with redirect_stdout(sys.stderr):
            await self.initialize()
            try:
                async with stdio_server() as streams:
                    await self.build_server().run(*streams, self.server.create_initialization_options())
            finally:
                await self.close()
