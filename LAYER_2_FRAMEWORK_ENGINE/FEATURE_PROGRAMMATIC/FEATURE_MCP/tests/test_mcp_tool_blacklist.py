"""Project exclusions filter the native Workbench gateway without discovery."""

from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import AsyncMock

from mcp.client._memory import InMemoryTransport
from mcp.client.session import ClientSession

MCP_ROOT = Path(__file__).resolve().parents[1]
sys.path[:0] = [str(MCP_ROOT), str(MCP_ROOT.parent / "FEATURE_TOOLS")]
from direct_gateway import DirectGateway  # noqa: E402
from project_tool_blacklist import project_tool_blacklist  # noqa: E402
from project_selection import ProjectSelection, bind_selection  # noqa: E402
from workbench_tools import NATIVE_TOOLS  # noqa: E402


class MCPToolBlacklistTests(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name).resolve()
        self.control = self.root / ".caprmedio_fixture"
        self.control.mkdir()
        self.settings = self.control / "caprmedio_project_settings.toml"

    def write_settings(self, blacklist):
        self.settings.write_text(
            '[paths]\ncontrol_root = ".caprmedio_fixture"\n'
            f'[project_mcp]\ntool_blacklist = {blacklist}\n', encoding="utf-8",
        )

    def test_no_settings_disables_no_tools(self):
        self.assertEqual(frozenset(), project_tool_blacklist(self.root))

    def test_local_settings_and_invalid_blacklist(self):
        self.write_settings('["query_run"]')
        self.assertEqual(frozenset({"query_run"}), project_tool_blacklist(self.root))
        self.write_settings('"query_run"')
        with self.assertRaises(ValueError):
            project_tool_blacklist(self.root)

    def test_ambiguous_and_symlink_settings_are_rejected(self):
        self.write_settings('[]')
        second = self.root / ".caprmedio_second"
        second.mkdir()
        (second / self.settings.name).write_text("[paths]\n", encoding="utf-8")
        with self.assertRaises(ValueError):
            project_tool_blacklist(self.root)
        (second / self.settings.name).unlink()
        self.settings.rename(self.control / "actual.toml")
        self.settings.symlink_to(self.control / "actual.toml")
        with self.assertRaises(ValueError):
            project_tool_blacklist(self.root)

    async def test_gateway_lists_and_refuses_blacklisted_workbench_names(self):
        self.write_settings('["workbench_ui_ping", "query_run"]')
        gateway = DirectGateway(self.root)
        await gateway.initialize()
        try:
            async with InMemoryTransport(gateway.build_server(), raise_exceptions=True) as streams:
                async with ClientSession(*streams) as client:
                    await client.initialize()
                    names = {tool.name for tool in (await client.list_tools()).tools}
                    self.assertEqual(set(NATIVE_TOOLS) - {"workbench_ui_ping", "query_run"}, names)
                    response = await client.call_tool("workbench_ui_ping", {})
                    self.assertTrue(response.is_error)
                    self.assertEqual(["Unknown Tool"], response.structured_content["diagnostics"])
        finally:
            await gateway.close()

    async def test_startup_bound_settings_override_disk_and_block_forwarding(self):
        self.write_settings('[]')
        selection = ProjectSelection(
            self.root, self.control, Path(self.control.name), "a" * 64,
            {"project_mcp": {"tool_blacklist": ["echo"]}}, {}, (), {}, "",
        )
        with bind_selection(selection):
            self.assertEqual(frozenset({"echo"}), project_tool_blacklist(self.root))
        gateway = DirectGateway(self.root, selection=selection)
        await gateway.initialize()
        gateway.workbench.call = AsyncMock()
        from mcp import types
        response = await gateway.call(None, types.CallToolRequestParams(name="echo", arguments={}))
        self.assertTrue(response.is_error)
        gateway.workbench.call.assert_not_awaited()
        await gateway.close()


if __name__ == "__main__":
    unittest.main()
