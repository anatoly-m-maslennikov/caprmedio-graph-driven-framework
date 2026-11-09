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

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "FEATURE_TOOLS"))
from health_observations import HealthObservations  # noqa: E402
from operation_error_boundary import (  # noqa: E402
    ExplicitBlockingRuntimeFailure, FailureRecord, operation_error_boundary,
)
from project_selection import (  # noqa: E402
    ProjectSelection, bind_selection, resolve_project, rebind_selection,
)
from project_tool_blacklist import project_tool_blacklist  # noqa: E402
from project_tool_context import native_arguments  # noqa: E402
from runtime_failure_diagnostics import report_failure  # noqa: E402
from shared_tool_contract import public_tool  # noqa: E402
from workbench_links import (  # noqa: E402
    context_project_root, public_saved, public_workspace, validate_reference,
)
from workbench_tools import (  # noqa: E402
    NATIVE_TOOLS, WORKSPACE_GET, WORKSPACE_OPEN, WorkbenchTools, mcp_app_probe,
    native_tools,
)


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
        self.ready = False
        self.server = None
        self.workbench = WorkbenchTools(self.root)
        self.health_observations = HealthObservations()

    async def initialize(self):
        if self.ready:
            return
        with bind_selection(self.selection) if self.selection is not None else nullcontext():
            self.tool_blacklist = project_tool_blacklist(self.root)
        self.tools = tuple(tool for tool in native_tools() if tool.name not in self.tool_blacklist)
        self.ready = True

    async def close(self):
        self.ready = False
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
            if params.name in self.tool_blacklist or params.name not in NATIVE_TOOLS:
                return result({"outcome": "rejected", "diagnostics": ["Unknown Tool"]}, True)
            with bind_selection(self.selection) if self.selection is not None else nullcontext():
                return await self._call(context, params.name, arguments)

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
        request = getattr(context, "request", None)
        if (name == "query_load" and isinstance(arguments, dict)
                and isinstance(arguments.get("reference"), str)):
            try:
                reference = validate_reference(
                    arguments["reference"], request, self.selection, context_project_root(context),
                )
            except ValueError as error:
                raise ExplicitBlockingRuntimeFailure("query_error", str(error)) from error
            arguments = {**arguments, "reference": reference}
        value = await self.workbench.call(name, arguments)
        if request is not None:
            value = public_saved(value, request, self.selection, context_project_root(context))
            if name in {WORKSPACE_OPEN, WORKSPACE_GET}:
                value = public_workspace(value, request, self.selection, context_project_root(context))
        return result(value)

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
        await self.initialize()
        try:
            async with stdio_server() as streams:
                with redirect_stdout(sys.stderr):
                    await self.build_server().run(*streams, self.server.create_initialization_options())
        finally:
            await self.close()
