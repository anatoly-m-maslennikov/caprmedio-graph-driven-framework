# CA-E-684@1
# CA-D-681@1

"""Real MCP and HTTP boundary proof for Workspace Views."""

from __future__ import annotations

from contextlib import asynccontextmanager
from pathlib import Path
import sys
import tempfile
import unittest

import httpx2
from mcp.client.session import ClientSession
from mcp.client.streamable_http import streamable_http_client


REPOSITORY = Path(__file__).resolve().parents[4]
PROGRAMMATIC = REPOSITORY / "LAYER_2_FRAMEWORK_ENGINE" / "FEATURE_PROGRAMMATIC"
MCP = PROGRAMMATIC / "FEATURE_MCP"
APP = PROGRAMMATIC / "FEATURE_APPS" / "APP_WORKBENCH"
for location in (MCP, PROGRAMMATIC / "FEATURE_TOOLS", APP.parent, APP / "tests"):
    if str(location) not in sys.path:
        sys.path.insert(0, str(location))

from APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.service import WorkbenchService  # noqa: E402
from http_paths import MCP_PATH, WORKBENCH_PATH  # noqa: E402
from http_server import create_app  # noqa: E402
from hot_reload import startup_selection  # noqa: E402
from scope_declaration_test_support import write_scope_unit_declarations  # noqa: E402
from smalltest_support import extension_directory, source_path, write_atom, write_settings  # noqa: E402
from workbench_tools import WorkbenchTools  # noqa: E402


class _ConfiguredWorkbenchTools(WorkbenchTools):
    def __init__(self, root: Path, extensions: Path) -> None:
        super().__init__(root)
        self.extensions = extensions

    def _owner(self):
        if self._service is None:
            self._service = WorkbenchService(self.root, extension_directory=self.extensions)
        return self._service


class WorkspaceEndToEndTests(unittest.IsolatedAsyncioTestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = (Path(self.temporary.name) / "project").resolve()
        self.root.mkdir()
        control = write_settings(self.root)
        declarations = write_scope_unit_declarations(
            self.root,
            ({"scope_unit_name": "ENGINE", "scope_unit_type": "Ordered", "scope_unit_label": "LAYER", "local_order": 1},),
            control_root=control,
        )
        write_atom(source_path(declarations, "ENGINE", "04_requirement", "fixture.md"), "CA-R-684")
        self.provider = Path(self.temporary.name) / "provider.py"
        self.provider.write_text(
            "from mcp.server import MCPServer\nMCPServer('workspace-e2e-fixture').run(transport='stdio')\n",
            encoding="utf-8",
        )
        self.app = create_app(self.root, implementation=self.provider, selection=startup_selection(self.root))
        self.app.gateway.workbench = _ConfiguredWorkbenchTools(
            self.root, extension_directory(REPOSITORY),
        )
        self.interface = f"{WORKBENCH_PATH}/fixture/interface"

    @asynccontextmanager
    async def session(self):
        async with self.app.starlette_app.router.lifespan_context(self.app.starlette_app):
            async with httpx2.AsyncClient(
                transport=httpx2.ASGITransport(app=self.app), base_url="http://127.0.0.1:18093",
            ) as client:
                transport = streamable_http_client(
                    "http://127.0.0.1:18093" + MCP_PATH, http_client=client,
                )
                streams = await transport.__aenter__()
                session = ClientSession(*streams)
                await session.__aenter__()
                try:
                    await session.initialize()
                    yield session, client
                finally:
                    await session.__aexit__(None, None, None)
                    await transport.__aexit__(None, None, None)

    async def tool(self, session: ClientSession, name: str, arguments: dict) -> dict:
        response = await session.call_tool(name, arguments)
        self.assertFalse(response.is_error, response.structured_content)
        return response.structured_content

    async def interface_call(self, client: httpx2.AsyncClient, operation: str, arguments: dict):
        return await client.post(self.interface, json={"operation": operation, "arguments": arguments})

    async def test_native_mcp_workspace_flow_matches_http_state(self) -> None:
        async with self.session() as (session, client):
            opened = await self.tool(session, "workspace_open", {"session_id": "native-session"})
            self.assertEqual("native-session", opened["workspace_id"])
            self.assertIn("?workspace=native-session", opened["workspace_url"])
            first = opened["active_view_id"]
            created = await self.tool(session, "view_create", {
                "workspace_id": opened["workspace_id"], "position": "last",
            })
            view = created["view_id"]
            updated = await self.tool(session, "view_update", {
                "workspace_id": opened["workspace_id"], "view_id": view,
                "sql": "SELECT id FROM atoms WHERE id = 'CA-R-684'", "expected_revision": 0,
            })
            self.assertEqual(1, updated["revision"])
            run = await self.tool(session, "view_run", {
                "workspace_id": opened["workspace_id"], "view_id": view,
            })
            self.assertNotIn("rows", run)
            self.assertEqual("success", run["status"])
            fetched = await self.tool(session, "view_fetch", {
                "workspace_id": opened["workspace_id"], "view_id": view, "offset": 0, "page_size": 1,
            })
            self.assertEqual([["CA-R-684"]], fetched["rows"])
            focused = await self.tool(session, "view_focus", {
                "workspace_id": opened["workspace_id"], "view_id": first,
            })
            self.assertEqual(first, focused["active_view_id"])
            http = await self.interface_call(client, "workspace_get", {"workspace_id": opened["workspace_id"]})
            self.assertEqual(200, http.status_code, http.text)
            state = http.json()
            self.assertEqual(first, state["active_view_id"])
            self.assertEqual({item["id"] for item in created["views"]}, {item["id"] for item in state["views"]})

    async def test_workspaces_are_isolated_and_guarded_by_ids_and_revisions(self) -> None:
        async with self.session() as (session, client):
            one = await self.tool(session, "workspace_open", {"session_id": "one"})
            two = await self.tool(session, "workspace_open", {"session_id": "two"})
            one_view, two_view = one["active_view_id"], two["active_view_id"]
            await self.tool(session, "view_update", {
                "workspace_id": "one", "view_id": one_view, "sql": "SELECT 1", "expected_revision": 0,
            })
            for name, arguments, message in (
                ("workspace_get", {"workspace_id": "missing"}, "unknown workspace_id"),
                ("view_get", {"workspace_id": "one", "view_id": two_view}, "unknown view_id"),
                ("view_update", {"workspace_id": "one", "view_id": one_view, "sql": "SELECT 2", "expected_revision": 0}, "expected_revision does not match"),
                ("view_remove", {"workspace_id": "two", "view_id": two_view}, "cannot remove the last view"),
            ):
                with self.subTest(name=name):
                    response = await session.call_tool(name, arguments)
                    self.assertTrue(response.is_error)
                    self.assertIn(message, str(response.structured_content))
            unknown = await self.interface_call(client, "workspace_get", {"workspace_id": "missing"})
            self.assertEqual(400, unknown.status_code)
            self.assertEqual({"error": "unknown workspace_id"}, unknown.json())
            untouched = await self.tool(session, "view_get", {"workspace_id": "two", "view_id": two_view})
            self.assertEqual("", untouched["sql"])

    async def test_runs_log_success_and_failure_and_saved_views_stay_loadable(self) -> None:
        async with self.session() as (session, _client):
            opened = await self.tool(session, "workspace_open", {"session_id": "logs"})
            view = opened["active_view_id"]
            await self.tool(session, "view_update", {
                "workspace_id": "logs", "view_id": view, "sql": "SELECT 1", "expected_revision": 0,
            })
            succeeded = await self.tool(session, "view_run", {"workspace_id": "logs", "view_id": view})
            self.assertEqual("success", succeeded["status"])
            saved = await self.tool(session, "view_save", {"workspace_id": "logs", "view_id": view})
            self.assertEqual("SELECT 1", (await self.tool(session, "query_load", {"reference": saved["saved_query_id"]}))["sql"])
            revision = (await self.tool(session, "view_get", {"workspace_id": "logs", "view_id": view}))["revision"]
            await self.tool(session, "view_update", {
                "workspace_id": "logs", "view_id": view, "sql": "SELECT FROM", "expected_revision": revision,
            })
            failed = await self.tool(session, "view_run", {"workspace_id": "logs", "view_id": view})
            self.assertEqual("failed", failed["status"])
            logs = await self.tool(session, "query_log_list", {})
            self.assertEqual(["failed", "success"], [item["outcome"] for item in logs["items"][:2]])
            for item in logs["items"][:2]:
                self.assertEqual({"log_id", "at", "sql", "outcome", "error", "row_count", "column_count"}, set(item))
                self.assertNotIn("rows", item)
                self.assertEqual(item, await self.tool(session, "query_log_get", {"log_id": item["log_id"]}))
            preview = await self.tool(session, "query_run", {
                "sql": "SELECT 1", "preview": 0, "save": False,
            })
            self.assertEqual([], preview["rows"])
            self.assertEqual(0, preview["row_count"])
            self.assertEqual(1, preview["column_count"])
            self.assertNotIn("saved_query_id", preview)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
