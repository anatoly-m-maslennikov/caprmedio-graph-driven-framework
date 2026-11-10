# CA-E-814@1
"""Real MCP transport and standalone hook caller-context checks."""

from __future__ import annotations

import asyncio
import json
from pathlib import Path
import subprocess
import sys
import unittest
from unittest.mock import patch

from mcp import types
from mcp.client._memory import InMemoryTransport
from mcp.client.session import ClientSession

MCP = Path(__file__).resolve().parents[1]
PROGRAMMATIC = MCP.parent
sys.path[:0] = [str(PROGRAMMATIC), str(MCP), str(PROGRAMMATIC / "FEATURE_TOOLS")]

from host_runtime_config import load_host_runtime_config  # noqa: E402
from runtime_request_context import (  # noqa: E402
    RuntimeRequestContext,
    bind_request_context,
    current_request_context,
)
from shared_gateway import SharedGateway  # noqa: E402
import test_shared_gateway as shared_fixture  # noqa: E402


class _ContextGateway(shared_fixture._Gateway):
    barrier = None

    async def call(self, _context, params):
        if self.barrier is not None:
            await self.barrier.wait()
        else:
            await asyncio.sleep(0)
        context = current_request_context()
        return types.CallToolResult(
            content=[],
            structuredContent={
                "root": str(self.root),
                "arguments": params.arguments,
                "context_session": context.session_id if context else None,
            },
        )


class _CancelledGateway(_ContextGateway):
    async def call(self, _context, params):
        assert current_request_context().session_id == "cancelled-session"
        raise asyncio.CancelledError


class CallerContextE2ETests(unittest.IsolatedAsyncioTestCase):
    setUp = shared_fixture.SharedGatewayTests.setUp
    _project = shared_fixture.SharedGatewayTests._project
    _config = shared_fixture.SharedGatewayTests._config

    def _gateway(self):
        return SharedGateway(
            load_host_runtime_config(self.config_path), gateway_factory=_ContextGateway
        )

    def _event(self, root, session, native_session="native-session"):
        return {
            "tool_name": "mcp__caprmedio__echo",
            "session_id": session,
            "tool_input": {"project_root": str(root), "session_id": native_session},
        }

    def _run_hook(self, event):
        hook = PROGRAMMATIC / "FEATURE_CODEX_HOOK" / "codex_hook.py"
        result = subprocess.run(
            [sys.executable, str(hook)],
            input=json.dumps(event),
            capture_output=True,
            text=True,
            check=True,
        )
        return json.loads(result.stdout)

    async def test_hook_context_reaches_native_tool_for_two_concurrent_projects(self):
        tool = types.Tool(
            name="echo",
            inputSchema={
                "type": "object",
                "properties": {
                    "session_id": {"type": "string"},
                },
                "required": ["session_id"],
                "additionalProperties": False,
            },
            outputSchema={"type": "object"},
        )
        _ContextGateway.tools_by_root = {str(root): [tool] for root in (*self.roots, self.nested)}
        gateway = self._gateway()
        await gateway.initialize()
        self.addAsyncCleanup(gateway.close)
        self.assertEqual({}, self._run_hook({"tool_name": "unrelated"}))

        async with InMemoryTransport(gateway.build_server(), raise_exceptions=True) as streams:
            async with ClientSession(*streams) as client:
                await client.initialize()
                listed = (await client.list_tools()).tools[0]
                self.assertIn("caller_context", listed.input_schema["properties"])
                inputs = [
                    self._run_hook(self._event(root, f"codex-{index}"))["hookSpecificOutput"][
                        "updatedInput"
                    ]
                    for index, root in enumerate(self.roots)
                ]
                _ContextGateway.barrier = asyncio.Barrier(2)
                first, second = await asyncio.wait_for(
                    asyncio.gather(*(client.call_tool("echo", arguments) for arguments in inputs)),
                    timeout=3,
                )
                _ContextGateway.barrier = None
                for index, response in enumerate((first, second)):
                    self.assertFalse(response.is_error, response.structured_content)
                    self.assertEqual(str(self.roots[index]), response.structured_content["root"])
                    self.assertEqual(
                        {"session_id": "native-session"}, response.structured_content["arguments"]
                    )
                    self.assertEqual(
                        f"codex-{index}", response.structured_content["context_session"]
                    )
                stateless = await client.call_tool(
                    "echo", {"project_root": str(self.roots[0]), "session_id": "native"}
                )
                self.assertIsNone(stateless.structured_content["context_session"])

    async def test_invalid_or_conflicting_context_does_not_invoke_a_tool(self):
        tool = types.Tool(
            name="echo",
            inputSchema={"type": "object", "properties": {}, "additionalProperties": False},
        )
        _ContextGateway.tools_by_root = {str(root): [tool] for root in (*self.roots, self.nested)}
        gateway = self._gateway()
        await gateway.initialize()
        self.addAsyncCleanup(gateway.close)
        root = str(self.roots[0])
        with patch.object(_ContextGateway, "call", side_effect=AssertionError("must not invoke")):
            for invalid in (
                None,
                {},
                {"session_id": ""},
                {"session_id": "  "},
                {"session_id": 3},
                {"session_id": "x", "extra": 1},
            ):
                result = await gateway.call(
                    None,
                    types.CallToolRequestParams(
                        name="echo", arguments={"project_root": root, "caller_context": invalid}
                    ),
                )
                self.assertTrue(result.is_error, repr(invalid))
            with bind_request_context(RuntimeRequestContext("already-bound")):
                result = await gateway.call(
                    None,
                    types.CallToolRequestParams(
                        name="echo",
                        arguments={
                            "project_root": root,
                            "caller_context": {"session_id": "different"},
                        },
                    ),
                )
                self.assertTrue(result.is_error)
            result = await gateway.call(
                None,
                types.CallToolRequestParams(
                    name="echo",
                    arguments={
                        "project_root": str(self.base),
                        "caller_context": {"session_id": "session"},
                    },
                ),
            )
            self.assertTrue(result.is_error)
        self.assertIsNone(current_request_context())

    async def test_context_is_reset_after_cancellation(self):
        tool = types.Tool(
            name="echo",
            inputSchema={"type": "object", "properties": {}, "additionalProperties": False},
        )
        _ContextGateway.tools_by_root = {str(root): [tool] for root in (*self.roots, self.nested)}
        gateway = SharedGateway(
            load_host_runtime_config(self.config_path), gateway_factory=_CancelledGateway
        )
        await gateway.initialize()
        self.addAsyncCleanup(gateway.close)
        params = types.CallToolRequestParams(
            name="echo",
            arguments={
                "project_root": str(self.roots[0]),
                "caller_context": {"session_id": "cancelled-session"},
            },
        )
        with self.assertRaises(asyncio.CancelledError):
            await gateway.call(None, params)
        self.assertIsNone(current_request_context())
