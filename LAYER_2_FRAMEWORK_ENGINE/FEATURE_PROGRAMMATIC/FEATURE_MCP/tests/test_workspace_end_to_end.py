# CA-E-684@7
# CA-D-681@9
# CA-E-781@1
# CA-D-696@1

"""Real MCP and HTTP boundary proof for Workspace Views."""

from __future__ import annotations

from contextlib import asynccontextmanager
import asyncio
import datetime as dt
from pathlib import Path
import sys
import tempfile
import threading
import unittest
from unittest.mock import patch

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
from APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.source_reader import SourceReader  # noqa: E402
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

    async def test_ui_probe_uses_existing_mcp_without_starting_workbench(self) -> None:
        from mcp import MCPError

        async with self.session() as (session, _client):
            descriptors = {tool.name: tool for tool in (await session.list_tools()).tools}
            uri = descriptors["workbench_ui_probe"].meta["ui"]["resourceUri"]
            self.assertEqual(
                {"ui": {"resourceUri": "ui://caprmedio/workbench.html"}},
                descriptors["workspace_open"].meta,
            )
            self.assertIsNone(descriptors["workbench_ui_ping"].meta)
            resources = (await session.list_resources()).resources
            resource_uris = [resource.uri for resource in resources]
            self.assertIn(uri, resource_uris)
            self.assertIn("ui://caprmedio/workbench.html", resource_uris)
            contents = (await session.read_resource(uri)).contents
            self.assertEqual("text/html;profile=mcp-app", contents[0].mime_type)
            self.assertIn("ui/initialize", contents[0].text)
            self.assertIn("ui/notifications/tool-result", contents[0].text)
            self.assertEqual({"message": "CAPRMEDIO MCP App resource loaded"},
                             await self.tool(session, "workbench_ui_probe", {}))
            self.assertEqual({"message": "Tool bridge passed"},
                             await self.tool(session, "workbench_ui_ping", {}))
            invalid = await session.call_tool("workbench_ui_ping", {"sql": "SELECT 1"})
            self.assertTrue(invalid.is_error)
            self.assertIsNone(self.app.gateway.workbench._service)
            with self.assertRaises(MCPError):
                await session.read_resource("ui://caprmedio/not-a-resource")

    async def test_sync_status_is_shared_and_readable_during_initial_capture(self) -> None:
        async with self.session() as (session, client):
            initial = {"syncing": False, "last_synced_at": None}
            self.assertEqual(initial, await self.tool(session, "workbench_status", {}))
            self.assertIsNone(self.app.gateway.workbench._service)
            endpoint = f"{WORKBENCH_PATH}/fixture/status"
            response = await client.post(endpoint, json={})
            self.assertEqual(200, response.status_code)
            self.assertEqual(initial, response.json())
            self.assertIsNone(self.app.gateway.workbench._service)

            entered, release = threading.Event(), threading.Event()
            capture = SourceReader.capture

            def paused(reader):
                entered.set()
                if not release.wait(10):
                    raise RuntimeError("capture release timed out")
                return capture(reader)

            with patch.object(SourceReader, "capture", paused):
                query = asyncio.create_task(self.tool(session, "query_run", {"sql": "SELECT 1"}))
                try:
                    self.assertTrue(await asyncio.to_thread(entered.wait, 5))
                    running = {"syncing": True, "last_synced_at": None}
                    self.assertEqual(running, await asyncio.wait_for(self.tool(session, "workbench_status", {}), 2))
                    response = await asyncio.wait_for(client.post(endpoint, json={}), 2)
                    self.assertEqual(running, response.json())
                finally:
                    release.set()
                    await query

            finished = await self.tool(session, "workbench_status", {})
            self.assertEqual({"syncing", "last_synced_at"}, set(finished))
            self.assertFalse(finished["syncing"])
            self.assertIsNotNone(dt.datetime.fromisoformat(finished["last_synced_at"]).tzinfo)
            self.assertEqual(finished, (await client.post(endpoint, json={})).json())
            self.assertEqual(400, (await client.post(endpoint, json={"unexpected": True})).status_code)

    async def test_native_mcp_workspace_flow_matches_http_state(self) -> None:
        async with self.session() as (session, client):
            opened = await self.tool(session, "workspace_open", {"session_id": "native-session"})
            self.assertEqual("native-session", opened["workspace_id"])
            self.assertEqual("fixture", opened["project_name"])
            self.assertNotEqual(self.root.name, opened["project_name"])
            self.assertIn("?workspace=native-session", opened["workspace_url"])
            native_state = await self.tool(session, "workspace_get", {"workspace_id": opened["workspace_id"]})
            self.assertEqual("fixture", native_state["project_name"])
            http_open = await self.interface_call(client, "workspace_open", {"session_id": "native-session"})
            self.assertEqual(200, http_open.status_code, http_open.text)
            self.assertEqual("fixture", http_open.json()["project_name"])
            first = opened["active_view_id"]
            created = await self.tool(session, "view_create", {
                "workspace_id": opened["workspace_id"], "position": "last",
            })
            view = created["view_id"]
            updated = await self.tool(session, "view_update", {
                "workspace_id": opened["workspace_id"], "view_id": view,
                "sql": "SELECT reference FROM atoms WHERE reference = 'CA-R-684'", "expected_revision": 0,
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
            self.assertEqual("fixture", state["project_name"])
            self.assertNotEqual(self.root.name, state["project_name"])
            self.assertEqual(first, state["active_view_id"])
            self.assertEqual({item["id"] for item in created["views"]}, {item["id"] for item in state["views"]})
            workspace_files = list((self.root / ".caprmedio_runtime" / "workbench" / "workspaces").glob("*.json"))
            self.assertEqual(1, len(workspace_files))
            self.assertNotIn("project_name", workspace_files[0].read_text(encoding="utf-8"))

    async def test_view_duplicate_has_strict_mcp_http_parity_without_execution(self) -> None:
        async with self.session() as (session, client):
            opened = await self.tool(session, "workspace_open", {"session_id": "duplicate"})
            workspace_id, source_id = opened["workspace_id"], opened["active_view_id"]
            await self.tool(session, "view_update", {
                "workspace_id": workspace_id, "view_id": source_id,
                "sql": "SELECT 42", "cursor_position": 7, "expected_revision": 0,
            })
            await self.tool(session, "view_rename", {
                "workspace_id": workspace_id, "view_id": source_id, "name": "Report",
            })
            await self.tool(session, "view_create", {
                "workspace_id": workspace_id, "position": "last", "name": "Report(1)",
            })
            await self.tool(session, "view_create", {
                "workspace_id": workspace_id, "position": "last", "name": "Report(3)",
            })
            logs_before = await self.tool(session, "query_log_list", {"limit": 1000})

            duplicate = await self.tool(session, "view_duplicate", {
                "workspace_id": workspace_id, "view_id": source_id,
            })
            duplicate_id = duplicate["view_id"]
            self.assertEqual(duplicate_id, duplicate["active_view_id"])
            self.assertEqual(
                [source_id, duplicate_id],
                [item["id"] for item in duplicate["views"][:2]],
            )
            duplicate_view = await self.tool(session, "view_get", {
                "workspace_id": workspace_id, "view_id": duplicate_id,
            })
            self.assertEqual("SELECT 42", duplicate_view["sql"])
            self.assertEqual(7, duplicate_view["cursor_position"])
            self.assertEqual(0, duplicate_view["revision"])
            self.assertNotIn("result", duplicate_view)
            self.assertEqual("Report(2)", duplicate_view["name"])
            self.assertEqual(logs_before, await self.tool(session, "query_log_list", {"limit": 1000}))

            http_duplicate = await self.interface_call(client, "view_duplicate", {
                "workspace_id": workspace_id, "view_id": source_id,
            })
            self.assertEqual(200, http_duplicate.status_code, http_duplicate.text)
            http_state_response = await self.interface_call(client, "workspace_get", {
                "workspace_id": workspace_id,
            })
            self.assertEqual(200, http_state_response.status_code, http_state_response.text)
            http_state = http_state_response.json()
            self.assertEqual(http_duplicate.json()["view_id"], http_state["active_view_id"])
            self.assertEqual(
                http_state,
                await self.tool(session, "workspace_get", {"workspace_id": workspace_id}),
            )

            invalid_mcp = await session.call_tool("view_duplicate", {
                "workspace_id": workspace_id, "view_id": source_id, "unexpected": True,
            })
            self.assertTrue(invalid_mcp.is_error)
            invalid_http = await self.interface_call(client, "view_duplicate", {
                "workspace_id": workspace_id, "view_id": source_id, "unexpected": True,
            })
            self.assertEqual(400, invalid_http.status_code)
            self.assertEqual(
                http_state,
                await self.tool(session, "workspace_get", {"workspace_id": workspace_id}),
            )

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
                "workspace_id": "logs", "view_id": view, "sql": 'SELECT * FROM "restart required"', "expected_revision": revision,
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


    async def test_view_run_preserves_workbench_unavailable_boundary(self) -> None:
        async with self.session() as (session, client):
            opened = await self.tool(session, "workspace_open", {"session_id": "invalid-settings"})
            identity = {"workspace_id": opened["workspace_id"], "view_id": opened["active_view_id"]}
            await self.tool(session, "view_update", identity | {"sql": "SELECT 1", "expected_revision": 0})
            settings = self.root / ".caprmedio_runtime" / "caprmedio_runtime_settings.toml"
            settings.parent.mkdir(parents=True, exist_ok=True)
            settings.write_text("[workbench]\nresult_ttl_seconds = 0\n", encoding="utf-8")
            failed = await session.call_tool("view_run", identity)
            self.assertTrue(failed.is_error)
            self.assertIn("workbench_unavailable", str(failed.structured_content))
            response = await self.interface_call(client, "view_run", identity)
            self.assertEqual(400, response.status_code)
            self.assertIn("Workbench unavailable", response.json()["error"])

    async def test_grid_page_contract_matches_http_and_rejects_invalid_indices(self) -> None:
        async with self.session() as (session, client):
            opened = await self.tool(session, "workspace_open", {"session_id": "grid-session"})
            identity = {"workspace_id": opened["workspace_id"], "view_id": opened["active_view_id"]}
            await self.tool(session, "view_update", identity | {
                "sql": "SELECT i % 3 AS bucket, i AS rowid, 'DRAFT%' AS label FROM range(12) AS t(i)",
                "expected_revision": 0,
            })
            run = await self.tool(session, "view_run", identity)
            grid = {"sort": [{"column": 1, "direction": "desc"}],
                    "filters": [{"column": 2, "operator": "contains", "value": "draft%"}],
                    "group_by": {"column": 0, "direction": "asc"}}
            args = {"query_id": run["query_id"], "offset": 0, "page_size": 2, "grid": grid}
            native = await self.tool(session, "query_page", args)
            response = await client.post(f"{WORKBENCH_PATH}/fixture/page", json=args)
            self.assertEqual(200, response.status_code, response.text)
            self.assertEqual(native, response.json())
            self.assertEqual([[0, 9, "DRAFT%"], [0, 6, "DRAFT%"]], native["rows"])
            self.assertEqual(12, native["source_row_count"])
            self.assertEqual(12, native["row_count"])
            self.assertEqual([{"value": 0, "count": 4}], native["groups"])
            fetched = await self.tool(session, "view_fetch", identity | {
                "offset": 0, "page_size": 2, "grid": grid,
            })
            self.assertEqual(native["rows"], fetched["rows"])
            self.assertEqual(native["groups"], fetched["groups"])
            for bad in ({"sort": [{"column": 99, "direction": "asc"}]}, {"unknown": True}, None, []):
                rejected = await session.call_tool("query_page", args | {"grid": bad})
                self.assertTrue(rejected.is_error)
                response = await client.post(f"{WORKBENCH_PATH}/fixture/page", json=args | {"grid": bad})
                self.assertEqual(400, response.status_code)
            invalid_fetch = await self.interface_call(client, "view_fetch", identity | {"grid": None})
            self.assertEqual(400, invalid_fetch.status_code)
            self.assertEqual(native, await self.tool(session, "query_page", args))



if __name__ == "__main__":  # pragma: no cover
    unittest.main()
