"""Focused checks for the shared host HTTP boundary."""

from __future__ import annotations

import json
from concurrent.futures import CancelledError as FutureCancelledError
from pathlib import Path
import sys
from types import SimpleNamespace
import unittest
from unittest.mock import patch

import httpx2
from mcp import types
from mcp.client.session import ClientSession
from mcp.client.streamable_http import streamable_http_client
from mcp.server.lowlevel import Server

MCP_ROOT = Path(__file__).resolve().parents[1]
TOOLS_ROOT = MCP_ROOT.parent / "201_TOOLS"
sys.path[:0] = [str(MCP_ROOT), str(TOOLS_ROOT)]

from shared_http_server import create_app  # noqa: E402


class FakeGateway:
    instances: list["FakeGateway"] = []

    def __init__(self, config):
        self.config = config
        self.initialized = False
        self.initialize_calls = 0
        self.close_calls = 0
        self.status_calls = 0
        self.status_error = None
        self.fail_initialize = False
        self.snapshot = {"initialized": False, "advertised_tools": [],
                         "calls": [], "workflows": []}
        self.__class__.instances.append(self)

    def build_server(self):
        async def list_tools(_context, _params):
            return types.ListToolsResult(tools=[types.Tool(
                name="echo_project", description="test", inputSchema={
                    "type": "object", "properties": {"project_root": {"type": "string"}},
                    "required": ["project_root"], "additionalProperties": False,
                })])

        async def call_tool(_context, params):
            root = params.arguments.get("project_root")
            value = {"project_root": root, "instance": str(id(self))}
            return types.CallToolResult(
                content=[types.TextContent(type="text", text=json.dumps(value))],
                structuredContent=value,
            )

        return Server("shared-test", on_list_tools=list_tools, on_call_tool=call_tool)

    async def initialize(self):
        self.initialize_calls += 1
        if self.fail_initialize:
            raise RuntimeError("private initialization detail")
        self.initialized = True
        self.snapshot.update(initialized=True, advertised_tools=["echo_project"])

    async def close(self):
        self.close_calls += 1
        self.initialized = False
        self.snapshot.update(initialized=False, advertised_tools=[])

    def status(self):
        self.status_calls += 1
        if self.status_error is not None:
            raise self.status_error
        return dict(self.snapshot)


class SharedHTTPTests(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        FakeGateway.instances.clear()
        self.config = SimpleNamespace(http_port=8092)
        self.app = create_app(self.config, gateway_factory=FakeGateway)
        self.gateway = FakeGateway.instances[-1]

    async def request(self, method="GET", path="/health", **kwargs):
        async with httpx2.AsyncClient(
            transport=httpx2.ASGITransport(app=self.app),
            base_url="http://127.0.0.1:8092",
        ) as client:
            return await client.request(method, path, **kwargs)

    async def test_health_is_preinit_snapshot_and_accept_negotiation_is_explicit(self):
        response = await self.request()
        self.assertEqual(503, response.status_code)
        self.assertEqual({"ready": False}, response.json())
        self.assertEqual(0, self.gateway.initialize_calls)
        self.assertGreaterEqual(self.gateway.status_calls, 1)

        response = await self.request(headers={"accept": "text/html;q=1,application/json;q=.5"})
        self.assertEqual(503, response.status_code)
        self.assertTrue(response.headers["content-type"].startswith("text/html"))
        self.assertIn("not ready", response.text)

        response = await self.request(headers={"accept": "text/html;q=0,application/json;q=1"})
        self.assertEqual({"ready": False}, response.json())

    async def test_loopback_host_and_origin_guard_are_shared(self):
        self.assertEqual(421, (await self.request(headers={"host": "attacker.invalid"})).status_code)
        self.assertEqual(403, (await self.request(
            headers={"origin": "https://attacker.invalid"})).status_code)
        self.assertEqual(0, self.gateway.initialize_calls)

    async def test_health_snapshot_failure_is_safe_and_reported_unbound(self):
        self.gateway.status_error = RuntimeError("secret status detail")
        with patch("shared_http_server.report_failure", return_value=(None, None)) as report:
            response = await self.request()
        self.assertEqual(503, response.status_code)
        self.assertEqual({"ready": False}, response.json())
        report.assert_called_once()
        self.assertIsNone(report.call_args.args[0])
        failure = report.call_args.args[1]
        self.assertEqual("shared_health_snapshot_unavailable", failure.code)
        self.assertNotIn("secret status detail", response.text)

    async def test_health_snapshot_cancellation_is_not_converted_to_503(self):
        self.gateway.status_error = FutureCancelledError()
        with self.assertRaises(FutureCancelledError):
            await self.request()

    async def test_lifespan_closes_after_partial_initialize_failure(self):
        self.gateway.fail_initialize = True
        with self.assertRaises(BaseException):
            async with self.app.starlette_app.router.lifespan_context(self.app.starlette_app):
                pass
        self.assertEqual(1, self.gateway.close_calls)

    async def test_lifespan_initializes_host_and_routes_two_project_calls(self):
        async with self.app.starlette_app.router.lifespan_context(self.app.starlette_app):
            async with httpx2.AsyncClient(
                transport=httpx2.ASGITransport(app=self.app),
                base_url="http://127.0.0.1:8092",
            ) as client:
                transport = streamable_http_client("http://127.0.0.1:8092/mcp", http_client=client)
                streams = await transport.__aenter__()
                session = ClientSession(*streams)
                await session.__aenter__()
                try:
                    await session.initialize()
                    first = await session.call_tool("echo_project", {"project_root": "/repos/alpha"})
                    second = await session.call_tool("echo_project", {"project_root": "/repos/beta"})
                    self.assertEqual("/repos/alpha", first.structured_content["project_root"])
                    self.assertEqual("/repos/beta", second.structured_content["project_root"])
                    health = await client.get("/health")
                    self.assertEqual({"ready": True}, health.json())
                finally:
                    await session.__aexit__(None, None, None)
                    await transport.__aexit__(None, None, None)
        self.assertEqual(1, self.gateway.initialize_calls)
        self.assertEqual(1, self.gateway.close_calls)


if __name__ == "__main__":
    unittest.main()
