"""Ordinary MCP transport checks, intentionally outside sealed Docker E2E discovery."""

from __future__ import annotations

import asyncio
import sys
from contextlib import asynccontextmanager
from pathlib import Path
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import AsyncMock, patch

from mcp import types

import test_selected_workflows_docker_e2e as harness
from test_selected_workflows_docker_e2e import (
    _stdio_client,
    _stdio_tool_call,
    _stdio_tool_names,
    _structured_tool_result,
)


ECHO_SERVER = (
    "from mcp.server import MCPServer\nfrom typing import Any\nfrom uuid import uuid4\n"
    "connection_id = str(uuid4())\nserver = MCPServer('selected-harness-transport-check')\n"
    "@server.tool(name='readonly_echo', structured_output=True)\n"
    "def echo(request: dict[str, Any]) -> dict[str, Any]: return {'request': request, 'connection_id': connection_id}\n"
    "server.run(transport='stdio')\n"
)


class SelectedDockerHarnessTransportTests(unittest.IsolatedAsyncioTestCase):
    async def test_actual_declared_stdio_client_reconnects_and_unwraps_structured_output(
        self,
    ) -> None:
        from mcp import StdioServerParameters

        parameters = StdioServerParameters(command=sys.executable, args=["-B", "-c", ECHO_SERVER])
        first = await _stdio_tool_call(parameters, "readonly_echo", {"sequence": 1})
        second = await _stdio_tool_call(parameters, "readonly_echo", {"sequence": 2})
        self.assertEqual({"sequence": 1}, first["request"])
        self.assertEqual({"sequence": 2}, second["request"])
        self.assertNotEqual(first["connection_id"], second["connection_id"])

    async def test_actual_client_reuses_connection_until_explicit_reconnect(self) -> None:
        from mcp import StdioServerParameters

        parameters = StdioServerParameters(command=sys.executable, args=["-B", "-c", ECHO_SERVER])
        async with _stdio_client(parameters) as client:
            async with asyncio.timeout(20):
                self.assertIsInstance(await client.list_tools(), types.ListToolsResult)
            self.assertEqual({"readonly_echo"}, await _stdio_tool_names(client))
            first = _structured_tool_result(
                await client.call_tool(
                    "readonly_echo", {"request": {"sequence": 1}}, read_timeout_seconds=20
                )
            )
            second = _structured_tool_result(
                await client.call_tool(
                    "readonly_echo", {"request": {"sequence": 2}}, read_timeout_seconds=20
                )
            )
        reconnected = await _stdio_tool_call(parameters, "readonly_echo", {"sequence": 3})
        self.assertEqual({"sequence": 1}, first["request"])
        self.assertEqual({"sequence": 2}, second["request"])
        self.assertEqual(first["connection_id"], second["connection_id"])
        self.assertNotEqual(first["connection_id"], reconnected["connection_id"])

    async def test_shared_call_and_listing_keep_twenty_second_budgets(self) -> None:
        client = SimpleNamespace(
            call_tool=AsyncMock(
                return_value=types.CallToolResult(content=[], structured_content={})
            ),
            list_tools=AsyncMock(return_value=types.ListToolsResult(tools=[])),
        )
        context = AsyncMock()
        context.__aenter__.return_value = client
        with patch.object(harness, "_stdio_client", return_value=context):
            self.assertEqual({}, await _stdio_tool_call("fixture", "echo", {}))
        client.call_tool.assert_awaited_once_with("echo", {"request": {}}, read_timeout_seconds=20)
        with patch.object(asyncio, "timeout", wraps=asyncio.timeout) as timeout:
            self.assertEqual(set(), await _stdio_tool_names(client))
        timeout.assert_called_once_with(20)
        client.list_tools.assert_awaited_once_with()

    async def test_harness_reconnects_once_before_polling_and_refuses_cross_fixture_client(
        self,
    ) -> None:
        connections, closed, calls = [], [], []

        @asynccontextmanager
        async def fake_client(parameters):
            identity = len(connections)
            connections.append(parameters)

            async def call_tool(tool, arguments, *, read_timeout_seconds):
                self.assertEqual(20, read_timeout_seconds)
                calls.append((identity, tool, arguments))
                statuses = [call for call in calls if call[1] == "workflow_orchestrator"]
                outcome = "running" if len(statuses) == 1 else "completed"
                return types.CallToolResult(content=[], structured_content={"outcome": outcome})

            try:
                yield SimpleNamespace(call_tool=call_tool)
            finally:
                closed.append(identity)

        temporary_root = (
            harness.ROOT / ".caprmedio_tmp/tests/test_selected_workflows_docker_transport"
        )
        temporary_root.mkdir(parents=True, exist_ok=True)
        with tempfile.TemporaryDirectory(dir=temporary_root) as directory:
            root = Path(directory)
            runtime = SimpleNamespace(root=root.resolve())
            case = harness.SelectedWorkflowsDockerEndToEnd()
            context = SimpleNamespace(candidate_image_digest="sha256:" + "a" * 64)
            with (
                patch.object(harness, "E2E_CONTEXT", context),
                patch.object(harness, "_stdio_client", fake_client),
                patch.object(
                    harness.asyncio,
                    "sleep",
                    new=AsyncMock(),
                ),
            ):
                try:
                    await case._call(runtime, root, "preview", {})
                    await case._call(runtime, root, "enqueue", {})
                    terminal = await case._terminal_status(runtime, root, "fixture-run")
                    self.assertEqual("completed", terminal["outcome"])
                    self.assertEqual([0, 0, 1, 1], [call[0] for call in calls])
                    self.assertEqual([0], closed)
                    other = root / "other"
                    other.mkdir()
                    with self.assertRaisesRegex(AssertionError, "must not cross fixture roots"):
                        await case._call(
                            SimpleNamespace(root=other.resolve()), other, "preview", {}
                        )
                finally:
                    await case._disconnect()
            self.assertEqual([0, 1], closed)

    async def test_result_unwrap_never_counts_tool_error_or_text_marker_as_success(self) -> None:
        successful = types.CallToolResult(content=[], structured_content={"actual": "structured"})
        self.assertEqual({"actual": "structured"}, _structured_tool_result(successful))
        for response in (
            types.CallToolResult(
                content=[], structured_content={"actual": "structured"}, is_error=True
            ),
            types.CallToolResult(
                content=[types.TextContent(type="text", text='{"actual":"marker"}')]
            ),
        ):
            with self.assertRaises(AssertionError):
                _structured_tool_result(response)


class QueryClientLifetimeTests(unittest.TestCase):
    def test_all_query_bodies_close_live_client_before_separate_teardown_task(self) -> None:
        from mcp import StdioServerParameters
        from test_selected_query_mcp_e2e import SelectedQueryMcpEndToEnd

        class BodyFailureCase(SelectedQueryMcpEndToEnd):
            __unittest_skip__ = False

            async def asyncSetUp(self) -> None:
                self.harness = harness.SelectedWorkflowsDockerEndToEnd()
                self.runtime, self.lease, self.launched = None, None, False

            async def _start_fixture(self, case_id, route):
                parameters = StdioServerParameters(
                    command=sys.executable, args=["-B", "-c", ECHO_SERVER]
                )
                self.harness._mcp_context = _stdio_client(parameters)
                self.harness._mcp_client = await self.harness._mcp_context.__aenter__()
                self.opening_task = asyncio.current_task()
                await self.harness._mcp_client.call_tool(
                    "readonly_echo", {"request": {"route": route}}, read_timeout_seconds=20
                )
                raise RuntimeError("fixture body failure after live MCP open")

            async def asyncTearDown(self) -> None:
                self.assertIsNone(
                    self.harness._mcp_client, "test body must close its own MCP context"
                )
                self.assertIsNot(self.opening_task, asyncio.current_task())
                await super().asyncTearDown()

        suite = unittest.defaultTestLoader.loadTestsFromTestCase(BodyFailureCase)
        result = unittest.TestResult()
        suite.run(result)
        self.assertEqual(4, result.testsRun)
        self.assertEqual([], result.skipped)
        self.assertEqual([], result.failures)
        self.assertEqual(4, len(result.errors))
        for _case, error in result.errors:
            self.assertIn("fixture body failure after live MCP open", error)
            self.assertNotIn("cancel scope", error)
