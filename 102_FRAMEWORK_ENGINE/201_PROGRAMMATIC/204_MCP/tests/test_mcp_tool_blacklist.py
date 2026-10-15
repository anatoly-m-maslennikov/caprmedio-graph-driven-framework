"""One Project blacklist filters selected, catalog and gateway MCP boundaries."""

from pathlib import Path
import sys
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import AsyncMock, patch

MCP = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(MCP))
import implementation_server  # noqa: E402
from capability_discovery.service import Service  # noqa: E402
from DISCOVER_TOOLS import discover_tools as provider  # noqa: E402
from hot_reload import CONTROL, STATUS, Gateway  # noqa: E402
from mcp.server.mcpserver.exceptions import ToolError  # noqa: E402
from mcp import Client  # noqa: E402
from project_selection import ProjectSelection, bind_selection  # noqa: E402
import test_hot_reload as hot_fixture  # noqa: E402


class MCPToolBlacklistTests(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        parent = MCP.parents[2] / ".caprmedio_tmp/tests/mcp-tool-blacklist"
        parent.mkdir(parents=True, exist_ok=True)
        temporary = tempfile.TemporaryDirectory(dir=parent)
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        self.control = self.root / ".caprmedio_fixture"
        self.control.mkdir()
        self.settings = self.control / "caprmedio_project_settings.toml"
        self.write_settings('["release_version", "public.release"]')

    def write_settings(self, blacklist):
        self.settings.write_text(
            '[paths]\ncontrol_root = ".caprmedio_fixture"\n'
            f"[project_mcp]\ntool_blacklist = {blacklist}\n"
        )

    def create_server(self):
        binding = {
            "name": provider.TOOL_NAME,
            "mcp_name": provider.MCP_NAME,
            "entrypoint": provider.ENTRYPOINT,
            "source_atom": provider.DELIVERY_ID,
            "action_ids": [provider.ACTION_ID],
            "source_path": "binding.md",
            "sha256": "a" * 64,
        }
        manifest = {"routes": [{"route": "create_atom"}]}
        self.frontiers = []
        original = Service.bind_server_frontier

        def bind(service, **frontier):
            original(service, **frontier)
            self.frontiers.append(service.exposed)

        with (
            patch("selected_routes.load_selected_manifest", return_value=manifest),
            patch.object(Service, "catalog", return_value=({}, [binding], [])),
            patch.object(Service, "bind_server_frontier", bind),
        ):
            return implementation_server.create_server(self.root)

    async def test_release_exclusions_preserve_other_routes_and_discovery(self):
        server = self.create_server()
        names = {tool.name for tool in await server.list_tools()}
        self.assertEqual(
            {
                "workflow_orchestrator",
                "create_atom",
                "get_selected_workflow_run",
                "get_selected_action_run",
                "discover_tools",
            },
            names,
        )
        self.assertEqual(
            [names - {"get_selected_workflow_run", "get_selected_action_run"}], self.frontiers
        )
        for name in ("release_version", "public.release"):
            with self.subTest(name=name), self.assertRaises(ToolError):
                await server.call_tool(name, {"request": {}})
        service = Service(self.root, exposed=names)
        with patch("selected_routes.load_selected_manifest", side_effect=ValueError("fixture")):
            self.assertEqual([], service._admitted_selected_route_tools([]))

    async def test_any_registered_name_can_be_excluded_without_constructing_provider(self):
        self.write_settings(
            '["workflow_orchestrator", "create_atom", "get_selected_action_run", "discover_tools"]'
        )
        with patch.object(provider, "create_adapter", side_effect=AssertionError("constructed")):
            server = self.create_server()
        names = {tool.name for tool in await server.list_tools()}
        self.assertEqual({"release_version", "public.release", "get_selected_workflow_run"}, names)
        for name in (
            "workflow_orchestrator",
            "create_atom",
            "get_selected_action_run",
            "discover_tools",
        ):
            with self.subTest(name=name), self.assertRaises(ToolError):
                await server.call_tool(name, {"request": {}})

    async def test_absent_list_and_unknown_exact_names_do_not_disable_tools(self):
        self.write_settings('["Release_Version", "unknown_tool"]')
        names = {tool.name for tool in await self.create_server().list_tools()}
        self.assertIn("release_version", names)
        self.settings.write_text('[paths]\ncontrol_root = ".caprmedio_fixture"\n')
        self.assertEqual(frozenset(), Service(self.root).tool_blacklist())
        self.assertEqual(names, {tool.name for tool in await self.create_server().list_tools()})

    async def test_invalid_blacklist_refuses_startup(self):
        for value in ('"release_version"', "[true]", '[""]'):
            self.write_settings(value)
            with self.subTest(value=value), self.assertRaises(ValueError):
                self.create_server()

    async def test_bound_settings_override_unselected_carrier_values(self):
        selection = ProjectSelection(
            self.root,
            self.control,
            Path(self.control.name),
            "a" * 64,
            {"project_mcp": {"tool_blacklist": ["create_atom"]}},
            {},
        )
        with bind_selection(selection):
            self.assertEqual(frozenset({"create_atom"}), Service(self.root).tool_blacklist())


class GatewayBlacklistTests(unittest.IsolatedAsyncioTestCase):
    setUp = hot_fixture.HotReload.setUp
    write = hot_fixture.HotReload.write
    params = hot_fixture.HotReload.params

    async def test_gateway_blocks_builtin_and_child_advertised_tools(self):
        control = self.root / ".caprmedio_fixture"
        control.mkdir()
        (control / "caprmedio_project_settings.toml").write_text(
            '[paths]\ncontrol_root = ".caprmedio_fixture"\n'
            '[project_mcp]\ntool_blacklist = ["echo", "reload_mcp_implementation", "get_mcp_reload_status"]\n'
        )
        async with Client(self.params(), cache=None) as client:
            self.assertEqual([], (await client.list_tools()).tools)
            for name in ("echo", CONTROL.name, STATUS.name):
                response = await client.call_tool(name, {"request": {}})
                self.assertTrue(response.is_error)
                self.assertEqual(["Unknown Tool"], response.structured_content["diagnostics"])

    async def test_gateway_does_not_forward_blacklisted_name_to_old_child(self):
        selection = ProjectSelection(
            self.root,
            self.root / ".caprmedio_fixture",
            Path(".caprmedio_fixture"),
            "a" * 64,
            {"project_mcp": {"tool_blacklist": ["echo"]}},
            {},
        )
        gateway = Gateway(self.root, self.source, selection=selection)
        client = SimpleNamespace(call_tool=AsyncMock())
        gateway.active = SimpleNamespace(
            client=client,
            tools=[SimpleNamespace(name="echo")],
            in_flight=0,
        )
        response = await gateway.call(None, SimpleNamespace(name="echo", arguments={}))
        self.assertTrue(response.is_error)
        client.call_tool.assert_not_awaited()


if __name__ == "__main__":
    unittest.main()
