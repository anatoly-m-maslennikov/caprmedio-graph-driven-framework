# CA-E-533@13
# CA-E-534@10

"""Default MCP startup keeps Workbench and selected tools in one process."""

from __future__ import annotations

from contextlib import nullcontext
from pathlib import Path
import sys
import tempfile
import unittest
from types import SimpleNamespace
from unittest.mock import AsyncMock, patch

from mcp import types
from mcp.client._memory import InMemoryTransport
from mcp.client.session import ClientSession
from mcp.server import MCPServer
from mcp.server.mcpserver import Context

MCP = Path(__file__).resolve().parents[1]
TOOLS = MCP.parent / "FEATURE_TOOLS"
sys.path[:0] = [str(MCP), str(TOOLS), str(TOOLS / "VALIDATE_ATOMS")]

from direct_gateway import DirectGateway  # noqa: E402
from http_server import create_app  # noqa: E402
import server as mcp_server  # noqa: E402


class _Server:
    async def list_tools(self):
        return [types.Tool(name="selected_tool", input_schema={"type": "object"})]

    async def _handle_call_tool(self, context, params):
        if params.name != "selected_tool" or params.arguments != {}:
            raise AssertionError("unexpected direct call")
        return types.CallToolResult(content=[], structured_content={"source": "direct"})


class DefaultMCPRuntimeTests(unittest.IsolatedAsyncioTestCase):
    async def test_default_gateway_has_no_child_and_registers_selected_and_workbench_tools(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            gateway = DirectGateway(root)
            with (
                patch("capability_discovery.service.Service.tool_blacklist", return_value=frozenset()),
                patch("implementation_server.create_server", return_value=_Server()) as create_server,
                patch("hot_reload.Generation", side_effect=AssertionError("unexpected reload child")),
            ):
                await gateway.initialize()
                try:
                    async with InMemoryTransport(gateway.build_server(), raise_exceptions=True) as streams:
                        async with ClientSession(*streams) as client:
                            await client.initialize()
                            names = {tool.name for tool in (await client.list_tools()).tools}
                            self.assertTrue({"selected_tool", "workbench_status"} <= names)
                            response = await client.call_tool("selected_tool", {})
                            self.assertEqual({"source": "direct"}, response.structured_content)
                finally:
                    await gateway.close()
            create_server.assert_called_once_with(root.resolve())
            self.assertTrue(gateway.active.task.done())

    async def test_direct_gateway_passes_the_outer_request_context_to_real_tools(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            implementation = MCPServer("context")

            @implementation.tool(name="context_tool", structured_output=True)
            async def context_tool(value: str, ctx: Context) -> dict[str, bool]:
                return {
                    "has_request_context": ctx.request_context is not None,
                    "has_session": ctx.request_context is not None and ctx.request_context.session is not None,
                }

            gateway = DirectGateway(root)
            with (
                patch("capability_discovery.service.Service.tool_blacklist", return_value=frozenset()),
                patch("implementation_server.create_server", return_value=implementation),
            ):
                await gateway.initialize()
                try:
                    async with InMemoryTransport(gateway.build_server(), raise_exceptions=True) as streams:
                        async with ClientSession(*streams) as client:
                            await client.initialize()
                            response = await client.call_tool("context_tool", {"value": "ok"})
                            invalid = await client.call_tool("context_tool", {})
                    self.assertEqual({"has_request_context": True, "has_session": True},
                                     response.structured_content)
                    self.assertTrue(invalid.is_error)
                finally:
                    await gateway.close()

    async def test_direct_gateway_keeps_the_subject_confirmation_guard(self):
        with tempfile.TemporaryDirectory() as directory:
            gateway = DirectGateway(Path(directory))
            confirmed = types.CallToolResult(content=[], structured_content={"status": "unconfirmed"})
            server = SimpleNamespace(call_tool=AsyncMock())
            request = {"mode": "execute", "parameters": {"subject_patches": []}}
            params = SimpleNamespace(name="update_atom", arguments={"request": request})
            with patch.object(gateway, "_confirm_subject", new=AsyncMock(return_value=confirmed)) as guard:
                response = await gateway._implementation_call(object(), params, SimpleNamespace(server=server))
            self.assertIs(confirmed, response)
            guard.assert_awaited_once()
            server.call_tool.assert_not_awaited()

    def test_http_app_uses_the_direct_gateway_without_an_opt_in(self):
        with tempfile.TemporaryDirectory() as directory:
            app = create_app(Path(directory))
        self.assertIsInstance(app.gateway, DirectGateway)


class StartupModeTests(unittest.TestCase):
    def _gateway_class_for(self, enabled):
        made = []

        class _DirectGateway:
            def __init__(self, *args, **kwargs):
                made.append(("direct", args, kwargs))

            async def serve(self):
                return None

        class _ReloadGateway:
            def __init__(self, *args, **kwargs):
                made.append(("reload", args, kwargs))

            async def serve(self):
                return None

        args = type("Args", (), {
            "project_root": Path("/project"), "control_root": None,
            "instance_id": None, "host_project_root": None,
        })()
        with (
            patch.object(mcp_server, "DirectGateway", _DirectGateway),
            patch.object(mcp_server, "Gateway", _ReloadGateway),
            patch.object(mcp_server, "hot_reload_enabled", return_value=enabled),
            patch.object(mcp_server, "startup_selection", return_value=object()),
            patch.object(mcp_server, "bind_selection", return_value=nullcontext()),
            patch.object(mcp_server.asyncio, "run", side_effect=lambda coro: coro.close()),
        ):
            mcp_server._serve_stdio(args)
        return made

    def test_stdio_uses_single_process_by_default(self):
        self.assertEqual("direct", self._gateway_class_for(False)[0][0])

    def test_stdio_uses_reload_only_after_explicit_opt_in(self):
        self.assertEqual("reload", self._gateway_class_for(True)[0][0])


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
