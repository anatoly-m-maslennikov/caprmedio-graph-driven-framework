# CA-E-525@10
# CA-E-681@1

"""Protocol checks for the generated MCP discovery catalog."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

import httpx2
from mcp import types
from mcp.client._memory import InMemoryTransport
from mcp.client.session import ClientSession
from mcp.server import MCPServer
from mcp.server.lowlevel import Server


MCP_ROOT = Path(__file__).resolve().parents[1]
TOOLS_ROOT = MCP_ROOT.parent / "FEATURE_TOOLS"
sys.path[:0] = [str(MCP_ROOT), str(TOOLS_ROOT), str(TOOLS_ROOT / "VALIDATE_ATOMS")]

import registered_tool_registry as registry  # noqa: E402
from capability_discovery import service as discovery_service  # noqa: E402
from capability_discovery.tool_catalog import ToolCatalogError, build_catalog, read_catalog  # noqa: E402
from generate_tools_catalog import generate_catalog  # noqa: E402


def _tool(name: str, *, schema: dict[str, object] | None = None) -> types.Tool:
    return types.Tool(
        name=name,
        title=f"{name} title",
        description=f"{name} description",
        inputSchema=schema or {"type": "object", "properties": {}},
        outputSchema={"type": "object"},
        annotations=types.ToolAnnotations(readOnlyHint=True, idempotentHint=True),
    )


class _CatalogServer:
    def __init__(self, tools: list[types.Tool]) -> None:
        self.tools = tools
        self.calls = 0
        self.server = Server("catalog-fixture", on_list_tools=self.list_tools, on_call_tool=self.call_tool)

    def create_app(self):
        return self.server.streamable_http_app()

    async def list_tools(self, _context, params):
        cursor = getattr(params, "cursor", None)
        if cursor is None:
            return types.ListToolsResult(tools=self.tools[:2], nextCursor="next" if len(self.tools) > 2 else None)
        if cursor == "next":
            return types.ListToolsResult(tools=self.tools[2:])
        raise AssertionError("unexpected cursor")

    async def call_tool(self, _context, _params):
        self.calls += 1
        raise AssertionError("catalog generation must not invoke a tool")


class GeneratedCatalogTests(unittest.IsolatedAsyncioTestCase):
    async def _generate(self, fixture: _CatalogServer, root: Path) -> dict[str, object]:
        app = fixture.create_app()
        async with app.router.lifespan_context(app):
            async with httpx2.AsyncClient(
                transport=httpx2.ASGITransport(app=app),
                base_url="http://127.0.0.1:8091",
            ) as client:
                return await generate_catalog(root, "http://127.0.0.1:8091/mcp", client)

    async def test_generation_reads_all_sdk_pages_preserves_metadata_and_replaces_changes(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            fixture = _CatalogServer([
                _tool("query_run", schema={"type": "object", "properties": {"sql": {"type": "string"}}}),
                _tool("discover_tools"),
                _tool("workspace_open"),
                _tool("view_save"),
                _tool("reload_mcp_implementation"),
                _tool("other_tool"),
            ])
            result = await self._generate(fixture, root)
            self.assertEqual(6, result["tool_count"])
            self.assertEqual(0, fixture.calls)
            catalog = read_catalog(root)
            self.assertEqual(["discover_tools", "other_tool"], [item["name"] for item in catalog["root"]])
            self.assertEqual(["query_run"], [item["name"] for item in catalog["groups"]["Queries"]])
            self.assertEqual(["workspace_open"], [item["name"] for item in catalog["groups"]["Workspaces"]])
            self.assertEqual(["view_save"], [item["name"] for item in catalog["groups"]["Views"]])
            self.assertEqual(["reload_mcp_implementation"], [item["name"] for item in catalog["groups"]["Service"]])
            query = catalog["groups"]["Queries"][0]
            self.assertEqual({"type": "string"}, query["inputSchema"]["properties"]["sql"])
            self.assertTrue(query["annotations"]["readOnlyHint"])

            fixture.tools = [
                _tool("discover_tools"),
                _tool("query_run", schema={"type": "object", "properties": {"query": {"type": "string"}}}),
                _tool("query_check"),
                _tool("workbench_restart"),
            ]
            await self._generate(fixture, root)
            regenerated = read_catalog(root)
            self.assertEqual(["discover_tools"], [item["name"] for item in regenerated["root"]])
            self.assertEqual(["query_check", "query_run"], [item["name"] for item in regenerated["groups"]["Queries"]])
            self.assertEqual(["workbench_restart"], [item["name"] for item in regenerated["groups"]["Service"]])
            self.assertNotIn("view_save", json.dumps(regenerated))
            self.assertIn("query", regenerated["groups"]["Queries"][1]["inputSchema"]["properties"])
            self.assertEqual(0, fixture.calls)

    def test_catalog_read_fails_explicitly_when_missing_or_corrupt(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            with self.assertRaisesRegex(ToolCatalogError, "missing"):
                read_catalog(root)
            path = root / ".caprmedio_runtime/mcp"
            path.mkdir(parents=True)
            (path / "tools_catalog.json").write_text("{not json", encoding="utf-8")
            with self.assertRaisesRegex(ToolCatalogError, "invalid"):
                read_catalog(root)

    def test_catalog_requires_the_one_root_discovery_tool(self) -> None:
        with self.assertRaisesRegex(ToolCatalogError, "exactly one discover_tools"):
            build_catalog([])
        with self.assertRaisesRegex(ToolCatalogError, "exactly one discover_tools"):
            build_catalog([_tool("query_run")])

    def test_workbench_reread_is_an_explicit_service_tool(self) -> None:
        catalog = build_catalog([_tool("discover_tools"), _tool("workbench_reread")])
        self.assertEqual(["workbench_reread"], [item["name"] for item in catalog["groups"]["Service"]])

    def test_catalog_read_rejects_a_symlinked_runtime_path(self) -> None:
        with tempfile.TemporaryDirectory() as temporary, tempfile.TemporaryDirectory() as outside:
            root = Path(temporary)
            (root / ".caprmedio_runtime").symlink_to(outside, target_is_directory=True)
            with self.assertRaisesRegex(ToolCatalogError, "unsafe"):
                read_catalog(root)

    async def test_real_mcp_wrapper_keeps_empty_request_distinct_from_selector_search(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            catalog_path = root / ".caprmedio_runtime/mcp"
            catalog_path.mkdir(parents=True)
            (catalog_path / "tools_catalog.json").write_text(json.dumps({
                "updated_at": "2026-11-05T00:00:00Z",
                "root": [{"name": "discover_tools", "inputSchema": {"type": "object"}}],
                "groups": {"Workspaces": [], "Queries": [], "Views": [], "Service": []},
            }), encoding="utf-8")
            binding = {
                "name": "DISCOVER_TOOLS",
                "mcp_name": "discover_tools",
                "entrypoint": "LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_TOOLS/TOOL_DISCOVER_TOOLS/discover_tools.py",
                "source_atom": "CA-D-512",
                "source_path": "fixture/discover_tools.md",
                "sha256": hashlib.sha256(b"fixture").hexdigest(),
                "action_ids": ["CA-O-112"],
            }
            with (
                patch.object(registry, "_binding_is_fresh", return_value=True),
                patch.object(discovery_service.Service, "discover", return_value={"matches": ["selected"]}) as discover,
            ):
                server = MCPServer("catalog-discovery")
                registered = registry.register_catalog_tools(server, root, [binding])
                self.assertEqual(frozenset({"discover_tools"}), registered.registered_names)
                async with InMemoryTransport(server, raise_exceptions=True) as streams:
                    async with ClientSession(*streams) as session:
                        await session.initialize()
                        root_response = await session.call_tool("discover_tools", {"request": {}})
                        selected_response = await session.call_tool(
                            "discover_tools", {"request": {"query": "selected"}},
                        )
            self.assertFalse(root_response.is_error, str(root_response))
            self.assertEqual("discover_tools", root_response.structured_content["root"][0]["name"])
            self.assertFalse(selected_response.is_error, str(selected_response))
            self.assertEqual({"matches": ["selected"]}, selected_response.structured_content)
            discover.assert_called_once()
            request = discover.call_args.args[0]
            self.assertEqual({"query"}, request.model_fields_set)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
