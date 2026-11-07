# CA-M-322@13
# CA-R-1820@9

"""Single-process MCP gateway used while reload is disabled."""

import asyncio
import sys
from pathlib import Path

from mcp import types
from mcp.server.lowlevel import Server

from hot_reload import Gateway, result
from shared_tool_contract import public_tool
from workbench_tools import (
    NATIVE_TOOLS as WORKBENCH_TOOLS,
    mcp_app_probe,
    native_tools as workbench_native_tools,
)


class DirectGeneration:
    """The direct implementation has no child process or reload lifecycle."""

    def __init__(self, server, tools):
        self.server, self.tools = server, list(tools)
        self.fingerprint = "single_process"
        self.in_flight, self.retired_at = 0, None
        self.task = asyncio.get_running_loop().create_future()

    async def close(self):
        if not self.task.done():
            self.task.set_result(None)


class DirectGateway(Gateway):
    """Keep Gateway's public boundaries while serving its tools in-process."""

    async def initialize(self):
        if self.active is not None:
            return
        if self.selection is None:
            sys.path.insert(
                0, str(Path(__file__).resolve().parents[1] / "FEATURE_TOOLS/VALIDATE_ATOMS")
            )
            from capability_discovery.service import Service

            self.tool_blacklist = Service(self.root).tool_blacklist()
        default = Path(__file__).with_name("implementation_server.py").resolve()
        if self.implementation.resolve() != default:
            raise ValueError("Custom MCP implementations require CAPRMEDIO_HOT_RELOAD=1")
        from implementation_server import create_server

        server = create_server(self.root)
        tools = await server.list_tools()
        names = [tool.name for tool in tools]
        if len(names) != len(set(names)) or set(WORKBENCH_TOOLS).intersection(names):
            raise ValueError("Duplicate or reserved Tool name")
        self.active = DirectGeneration(server, tools)
        self.generations = [self.active]
        self._initialized = True

    def status(self):
        return {
            "runtime": "single_process",
            "reload_enabled": False,
            "active_generation": self.active.fingerprint if self.active else None,
        }

    async def control(self, context, arguments):
        return result({"outcome": "rejected", "diagnostics": ["MCP hot reload is disabled"]}, True)

    async def refresh_generation(self, context, *, request_id, force=False):
        return {
            "request_id": request_id,
            "active_generation": self.active.fingerprint if self.active else None,
            "outcome": "restart_required",
            "diagnostics": ["Restart MCP to load implementation changes"],
        }

    async def _implementation_call(self, context, params, generation):
        request = params.arguments.get("request") if isinstance(params.arguments, dict) else None
        if (
            params.name == "update_atom"
            and isinstance(request, dict)
            and request.get("mode") == "execute"
            and isinstance(request.get("parameters"), dict)
            and "subject_patches" in request["parameters"]
        ):
            confirmed = await self._confirm_subject(context, params.arguments)
            if confirmed is not None:
                return confirmed
        response = await generation.server._handle_call_tool(context, params)
        if (
            params.name == "atom_update"
            and isinstance(request, dict)
            and request.get("operation") in ("stage_subjects", "stage_subject_batch")
        ):
            self._retain_subject_stage(context, response)
        return response

    async def close(self):
        try:
            if self.active is not None:
                await self.active.close()
        finally:
            await self.workbench.close()

    def build_server(self):
        async def list_tools(context, params):
            return types.ListToolsResult(
                tools=[
                    public_tool(tool, required=False)
                    for tool in (*workbench_native_tools(), *self.active.tools)
                    if tool.name not in self.tool_blacklist
                ]
            )

        self.server = Server(
            "CAPRMEDIO",
            version="0.2.0",
            on_list_tools=list_tools,
            on_call_tool=self.call,
            on_list_resources=mcp_app_probe.list_resources,
            on_read_resource=mcp_app_probe.read_resource,
        )
        return self.server
