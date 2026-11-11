"""Exercise the retained native frontier over the real MCP transport."""

from pathlib import Path
import sys
import tempfile
import unittest

from mcp.client._memory import InMemoryTransport
from mcp.client.session import ClientSession

MCP_ROOT = Path(__file__).resolve().parents[1]
sys.path[:0] = [str(MCP_ROOT), str(MCP_ROOT.parent / "FEATURE_TOOLS")]
from direct_gateway import DirectGateway  # noqa: E402
from shared_project_catalog import native_tools as shared_native_tools  # noqa: E402


WORKBENCH_NAMES = frozenset("""
workbench_ui_probe workbench_ui_ping query_run query_page query_check query_schema
view_save query_load query_saved_list workspace_open workspace_list workspace_get
view_create view_duplicate view_list view_get view_update view_run view_check
view_fetch view_focus view_rename view_remove query_log_list query_log_get
workbench_restart workbench_reread workbench_status
""".split())
LIFECYCLE_NAMES = frozenset("""
atom_lifecycle_create_draft atom_lifecycle_archive atom_lifecycle_change_status
atom_lifecycle_direct_update atom_lifecycle_promote_draft atom_lifecycle_update
""".split())
RETIRED_NAMES = """
atom_search find_and_fetch_artifacts find_and_fetch_journal_events
append_change_records atom_update rmed_atoms_base_revise discover_tools
discover_operations get_execution_context get_execution_status
resume_execution_context watch_execution workflow_orchestrator create_atom
update_atom replace_atom change_atom_status move_atom run_implementation_workflow
revert_changes build_entities_graph build_terms_graph build_applicable_methodology
generate_entity_graph get_selected_workflow_run get_selected_action_run
release_version public.release reload_mcp_implementation get_mcp_reload_status
""".split()


class RetainedFrontierTests(unittest.IsolatedAsyncioTestCase):
    async def test_listing_healthy_bridge_and_retired_call_refusals(self):
        with tempfile.TemporaryDirectory() as directory:
            gateway = DirectGateway(Path(directory))
            await gateway.initialize()
            self.assertEqual(WORKBENCH_NAMES | LIFECYCLE_NAMES, {tool.name for tool in shared_native_tools(gateway)})
            try:
                async with InMemoryTransport(gateway.build_server(), raise_exceptions=True) as streams:
                    async with ClientSession(*streams) as client:
                        await client.initialize()
                        names = {tool.name for tool in (await client.list_tools()).tools}
                        self.assertEqual(28, len(WORKBENCH_NAMES))
                        self.assertEqual(WORKBENCH_NAMES | LIFECYCLE_NAMES, names)
                        response = await client.call_tool("workbench_ui_ping", {})
                        self.assertFalse(response.is_error)
                        self.assertEqual({"message": "Tool bridge passed"}, response.structured_content)
                        for name in RETIRED_NAMES:
                            with self.subTest(name=name):
                                response = await client.call_tool(name, {"request": {}})
                                self.assertTrue(response.is_error)
            finally:
                await gateway.close()



if __name__ == "__main__":
    unittest.main()
