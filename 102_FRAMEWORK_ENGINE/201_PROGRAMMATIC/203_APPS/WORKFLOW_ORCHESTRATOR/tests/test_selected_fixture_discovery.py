"""Real source-derived helper discovery in a disposable selected fixture."""

from __future__ import annotations

import json
from pathlib import Path
import sys
import tempfile
from typing import Callable, cast
import unittest

from mcp.server import MCPServer
from mcp.server.mcpserver.exceptions import ToolError
from mcp.types import CallToolResult, TextContent

APP = Path(__file__).resolve().parents[1]
ROOT = APP.parents[3]
MCP = APP.parents[1] / "204_MCP"
for location in (APP, MCP):
    if str(location) not in sys.path:
        sys.path.insert(0, str(location))

from implementation_server import create_server as _create_server  # noqa: E402
from selected_workflows_docker_fixture import (  # noqa: E402
    GoldenCase,
    GoldenProject,
    _CONTEXT_DECLARATION_DIGEST,
    _CONTEXT_DECLARATION_PATH,
    file_digest,
)

# The existing server factory has no annotations; retain its actual SDK boundary.
create_server = cast(Callable[[Path], MCPServer[object]], _create_server)


class SelectedFixtureDiscoveryTests(unittest.IsolatedAsyncioTestCase):
    def setUp(self) -> None:
        parent = ROOT / ".caprmedio_tmp/tests/selected-fixture-discovery"
        parent.mkdir(parents=True, exist_ok=True)
        self.temporary = tempfile.TemporaryDirectory(dir=parent)
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name).resolve()
        self.fixture = GoldenProject(ROOT, self.root, GoldenCase("W01", "create_atom"))
        self.manifest = self.fixture.prepare()
        self.declaration = self.root / _CONTEXT_DECLARATION_PATH

    async def test_actual_server_exposes_source_bound_create_atom_context(self) -> None:
        self.assertEqual(_CONTEXT_DECLARATION_DIGEST, file_digest(self.declaration))
        server = create_server(self.root)
        names = {tool.name for tool in await server.list_tools()}
        self.assertIn("get_execution_context", names)
        before = self.fixture.snapshot()
        response = await server.call_tool(
            "get_execution_context", {"request": {"id": "create_atom"}}
        )
        assert isinstance(response, CallToolResult)
        assert isinstance(response.content[0], TextContent)
        result = json.loads(response.content[0].text)
        self.assertTrue(result["context_complete"], result)
        self.assertEqual("create_atom", result["definition"]["name"])
        self.assertEqual(
            self.manifest["canonical_manifest_sha256"],
            result["definition"]["definition_manifest"]["manifest_digest"],
        )
        self.assertEqual(before, self.fixture.snapshot())
        with self.assertRaises(ToolError):
            await server.call_tool(
                "get_execution_context", {"request": {"id": "create_atom", "extra": True}}
            )

    async def test_omitted_declaration_is_not_silently_registered(self) -> None:
        self.declaration.unlink()
        server = create_server(self.root)
        self.assertNotIn("get_execution_context", {tool.name for tool in await server.list_tools()})
        with self.assertRaises(ToolError):
            await server.call_tool("get_execution_context", {"request": {"id": "create_atom"}})

    async def test_malformed_or_conflicting_declaration_is_not_silently_registered(self) -> None:
        raw = self.declaration.read_text()
        self.assertIn('action_ids = ["CA-O-114"]', raw)
        for replacement in ('action_ids = ["CA-O-999"]', "action_ids = ["):
            with self.subTest(declaration=replacement):
                self.declaration.write_text(raw.replace('action_ids = ["CA-O-114"]', replacement))
                server = create_server(self.root)
                self.assertNotIn(
                    "get_execution_context", {tool.name for tool in await server.list_tools()}
                )
                with self.assertRaises(ToolError):
                    await server.call_tool(
                        "get_execution_context", {"request": {"id": "create_atom"}}
                    )


if __name__ == "__main__":
    unittest.main()
