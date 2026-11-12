# CA-E-676@11
# CA-E-673@3
# CA-E-683@5
# CA-E-684@7
# CA-D-673@14

from __future__ import annotations

from pathlib import Path
import re
import sys
import tempfile
from types import MappingProxyType
import unittest
import uuid
from unittest.mock import patch

from starlette.applications import Starlette
from starlette.testclient import TestClient

MCP_ROOT = Path(__file__).resolve().parents[1]
FRONTEND_ROOT = MCP_ROOT.parent / "FEATURE_APPS" / "APP_WORKBENCH" / "FEATURE_WORKBENCH_FRONTEND"
sys.path.insert(0, str(MCP_ROOT))

from http_paths import WORKBENCH_PATH  # noqa: E402
import workbench_web  # noqa: E402
from workbench_web import routes  # noqa: E402
from operation_error_boundary import ExplicitBlockingRuntimeFailure  # noqa: E402


PROJECT_NAME = "caprmedio"
PROJECT_PATH = f"{WORKBENCH_PATH}/{PROJECT_NAME}"


class FakeWorkbench:
    def __init__(self):
        self.calls = []

    async def call(self, name, arguments):  # noqa: C901
        self.calls.append((name, arguments))
        if name == "query_page" and (
            not isinstance(arguments.get("query_id"), str)
            or type(arguments.get("offset")) is not int
            or arguments["offset"] < 0
        ):
            raise ExplicitBlockingRuntimeFailure("query_error", "offset must be a non-negative integer")
        if name == "query_load" and not isinstance(arguments.get("reference"), str):
            raise ExplicitBlockingRuntimeFailure("query_error", "reference must be a string")
        if name == "query_saved_list":
            limit = arguments.get("limit", 20)
            if type(limit) is not int or not 1 <= limit <= 1000:
                raise ExplicitBlockingRuntimeFailure("query_error", "limit must be an integer from 1 to 1000")
        if (
            name in {"query_run", "query_check"}
            or name == "view_save" and "workspace_id" not in arguments
        ) and not isinstance(arguments.get("sql"), str):
            raise ExplicitBlockingRuntimeFailure("query_error", "sql must be a string")
        if name == "workspace_open":
            return {"workspace_id": arguments["session_id"], "views": []}
        if name == "workspace_get":
            return {"workspace_id": arguments["workspace_id"], "views": []}
        if name == "view_create":
            return {"workspace_id": arguments["workspace_id"], "view_id": "view-1"}
        if name == "view_save" and "workspace_id" in arguments:
            return {"workspace_id": arguments["workspace_id"], "view_id": arguments["view_id"]}
        if name == "query_page":
            if arguments["query_id"] != "query-1":
                raise ExplicitBlockingRuntimeFailure("query_error", "unknown query_id")
            return {
                "query_id": "query-1",
                "columns": [{"name": "value", "type": "VARCHAR"}],
                "rows": [["page two"]],
                "row_count": 2,
                "column_count": 1,
                "offset": arguments["offset"],
                "page_size": arguments.get("page_size", 100),
                "has_more": False,
            }
        if name == "query_schema":
            return {"atoms": []}
        if name == "workbench_archive_load":
            return {"loaded_archive_scopes": arguments["scopes"]}
        if name == "query_saved_list":
            return {"items": []}
        if name == "query_load":
            return {"saved_query_id": arguments["reference"], "kind": "query", "sql": "SELECT 1"}
        if name == "view_save":
            value = {"saved_query_id": "w_1", "kind": "view", "sql": arguments["sql"]}
            if arguments.get("name", "").strip():
                value["name"] = arguments["name"]
            return value
        if arguments["sql"] == "bad":
            raise ExplicitBlockingRuntimeFailure("query_error", "bad query")
        if arguments["sql"] == "crash":
            raise RuntimeError("private unexpected connector detail")
        if arguments["sql"] == "large":
            return {
                "query_id": "query-1",
                "columns": [{"name": "item", "type": "VARCHAR"}, {"name": "item", "type": "VARCHAR"}],
                "rows": [[f"λ-{index}", f"value-{index}"] for index in range(100)],
                "row_count": 1024,
                "column_count": 2,
                "offset": 0,
                "page_size": arguments.get("page_size", 100),
                "has_more": True,
            }
        if arguments["sql"] == "partial":
            return {
                "query_id": "query-1",
                "rows": [["saved result"]],
                "outcome": "partial",
                "save_error": "journal unavailable",
            }
        if name == "query_check":
            return {"valid": True, "row_count": 1, "column_count": 1}
        value = {
            "query_id": "query-1",
            "columns": [{"name": "value", "type": "VARCHAR"}],
            "rows": [["<script>x</script>"]],
            "row_count": 1,
            "column_count": 1,
            "offset": 0,
            "page_size": arguments.get("page_size", 100),
            "has_more": False,
        }
        if arguments.get("save"):
            value.update({"saved_query_id": "q_1", "kind": "query", "sql": arguments["sql"]})
            if arguments.get("name", "").strip():
                value["name"] = arguments["name"]
        return value


class FakeGateway:
    def __init__(self):
        self.workbench = FakeWorkbench()
        self.roots = []
        settings = MappingProxyType({"project": MappingProxyType({"name": PROJECT_NAME})})
        self.root = Path.cwd()
        self.tool_blacklist = frozenset()
        self.selection = type("Selection", (), {"settings": settings, "root": self.root, "host_root": None})()

    def _selection(self, root):
        if root != "/project":
            raise ValueError("invalid_project_root")
        return self.selection

    async def workbench_call(self, name, arguments):
        self.roots.append(arguments["project_root"])
        return await self.workbench.call(
            name, {key: value for key, value in arguments.items() if key != "project_root"}
        )


class WorkbenchWebTests(unittest.TestCase):
    def setUp(self):
        self._temporary = tempfile.TemporaryDirectory()
        frontend = Path(self._temporary.name)
        (frontend / "assets").mkdir()
        (frontend / "assets" / "app.js").write_text("// fixture")
        (frontend / "index.html").write_text(
            f'<div id="app"></div><script src="{WORKBENCH_PATH}/assets/app.js"></script>'
        )
        self._frontend = patch.object(workbench_web, "_FRONTEND", frontend)
        self._frontend.start()
        self.addCleanup(self._frontend.stop)
        self.addCleanup(self._temporary.cleanup)

    def test_project_named_assets_is_not_shadowed_by_static_files(self):
        gateway = FakeGateway()
        gateway.selection.settings = MappingProxyType({"project": MappingProxyType({"name": "assets"})})
        with TestClient(Starlette(routes=routes(gateway))) as client:
            self.assertEqual(200, client.get(f"{WORKBENCH_PATH}/assets").status_code)
            self.assertEqual(200, client.post(f"{WORKBENCH_PATH}/assets/check", json={"sql": "SELECT 1"}).status_code)
            self.assertEqual(200, client.get(f"{WORKBENCH_PATH}/assets/app.js").status_code)

    def test_archive_load_route_and_blacklist(self):
        gateway = FakeGateway()
        scopes = [{'scope_unit': 'PROJECT', 'role': 'Plan'}]
        with TestClient(Starlette(routes=routes(gateway))) as client:
            response = client.post(f'{PROJECT_PATH}/archive-load', json={'scopes': scopes})
            self.assertEqual(200, response.status_code)
            self.assertEqual({'loaded_archive_scopes': scopes}, response.json())
            self.assertEqual(('workbench_archive_load', {'scopes': scopes}), gateway.workbench.calls[-1])
            self.assertEqual(404, client.post(f'{WORKBENCH_PATH}/other/archive-load', json={'scopes': scopes}).status_code)
            gateway.tool_blacklist = frozenset({'workbench_archive_load'})
            self.assertEqual(400, client.post(f'{PROJECT_PATH}/archive-load', json={'scopes': scopes}).status_code)
            self.assertEqual(1, len(gateway.workbench.calls))

    def test_archive_load_route_selects_shared_project(self):
        gateway = FakeGateway()
        scopes = [{'scope_unit': 'PROJECT', 'role': 'Plan'}]
        with TestClient(Starlette(routes=routes(gateway, shared=True))) as client:
            response = client.post(f'{PROJECT_PATH}/archive-load', json={'project_root': '/project', 'scopes': scopes})
        self.assertEqual(200, response.status_code)
        self.assertEqual({'loaded_archive_scopes': scopes}, response.json())
        self.assertEqual(['/project'], gateway.roots)

    def test_page_and_project_bound_run_check_routes(self):
        gateway = FakeGateway()
        app = Starlette(routes=routes(gateway))
        with TestClient(app) as client:
            self.assertEqual(404, client.get(WORKBENCH_PATH).status_code)
            page = client.get(PROJECT_PATH)
            self.assertEqual(200, page.status_code)
            self.assertIn('id="app"', page.text)
            self.assertIn(f"{WORKBENCH_PATH}/assets/", page.text)
            self.assertEqual(1, client.post(f"{PROJECT_PATH}/check", json={"sql": "SELECT 1"}).json()["row_count"])
            result = client.post(f"{PROJECT_PATH}/run", json={"sql": "SELECT 1"})
            self.assertEqual(1, result.json()["row_count"])
            self.assertEqual({"atoms": []}, client.post(f"{PROJECT_PATH}/schema", json={}).json())
            saved_id = "q_" + "0" * 32
            self.assertEqual(saved_id, client.post(f"{PROJECT_PATH}/load", json={"reference": saved_id}).json()["saved_query_id"])
            current_id = str(uuid.uuid7())
            self.assertEqual(current_id, client.post(f"{PROJECT_PATH}/load", json={"reference": current_id}).json()["saved_query_id"])
            self.assertEqual(
                {"error": "saved query reference must be an ID or absolute URL"},
                client.post(f"{PROJECT_PATH}/load", json={"reference": "?query=" + saved_id}).json(),
            )
            large = client.post(f"{PROJECT_PATH}/run", json={"sql": "large"})
            self.assertEqual("application/json", large.headers["content-type"])
            self.assertEqual(
                {
                    "query_id": "query-1",
                    "columns": [{"name": "item", "type": "VARCHAR"}, {"name": "item", "type": "VARCHAR"}],
                    "rows": [[f"λ-{index}", f"value-{index}"] for index in range(100)],
                    "row_count": 1024,
                    "column_count": 2,
                    "offset": 0,
                    "page_size": 100,
                    "has_more": True,
                },
                large.json(),
            )
            paged = client.post(
                f"{PROJECT_PATH}/page",
                json={"query_id": "query-1", "offset": 100, "page_size": 20},
            )
            self.assertEqual(200, paged.status_code)
            self.assertEqual(100, paged.json()["offset"])
            self.assertEqual(20, paged.json()["page_size"])
            for operation in ("run", "check"):
                failure = client.post(f"{PROJECT_PATH}/{operation}", json={"sql": "bad"})
                self.assertEqual(400, failure.status_code)
                self.assertEqual({"error": "bad query"}, failure.json())
            failure = client.post(f"{PROJECT_PATH}/run", json={"sql": "crash"})
            self.assertEqual(400, failure.status_code)
            self.assertEqual({"error": "operation failure"}, failure.json())
            failure = client.post(f"{PROJECT_PATH}/check", json={"sql": 1})
            self.assertEqual({"error": "sql must be a string"}, failure.json())
            failure = client.post(f"{PROJECT_PATH}/page", json={"query_id": "query-1", "offset": -1})
            self.assertEqual({"error": "offset must be a non-negative integer"}, failure.json())
            self.assertEqual(404, client.post(f"{WORKBENCH_PATH}/wrong/run", json={"sql": "SELECT 1"}).status_code)

    def test_missing_frontend_does_not_block_query_routes(self):
        missing = Path(self._temporary.name) / "missing"
        with patch.object(workbench_web, "_FRONTEND", missing):
            app = Starlette(routes=routes(FakeGateway()))
            with TestClient(app) as client:
                response = client.get(PROJECT_PATH)
                self.assertEqual(503, response.status_code)
                self.assertEqual(
                    {"error": "Workbench frontend is unavailable; build required"}, response.json()
                )
                self.assertEqual(
                    1,
                    client.post(f"{PROJECT_PATH}/check", json={"sql": "SELECT 1"}).json()["row_count"],
                )

    def test_standalone_codex_chat_route_is_disabled(self):
        with TestClient(Starlette(routes=routes(FakeGateway()))) as client:
            self.assertEqual(404, client.get(f"{PROJECT_PATH}/codex").status_code)

    def test_workspace_interface_uses_the_shared_native_operation_and_public_url(self):
        with TestClient(Starlette(routes=routes(FakeGateway())), base_url="http://workbench.test") as client:
            opened = client.post(f"{PROJECT_PATH}/interface", json={
                "operation": "workspace_open", "arguments": {"session_id": "session-1"},
            })
            self.assertEqual(200, opened.status_code)
            self.assertEqual(
                "http://workbench.test/caprmedio/workbench/caprmedio?workspace=session-1",
                opened.json()["workspace_url"],
            )
            self.assertEqual(PROJECT_NAME, opened.json()["project_name"])
            created = client.post(f"{PROJECT_PATH}/interface", json={
                "operation": "view_create", "arguments": {"workspace_id": "session-1"},
            })
            self.assertEqual("view-1", created.json()["view_id"])
            invalid = client.post(f"{PROJECT_PATH}/interface", json={
                "operation": "unknown", "arguments": {},
            })
            self.assertEqual(400, invalid.status_code)

    def test_interface_rejects_blacklisted_bound_view_save_and_validates_single_root(self):
        gateway = FakeGateway()
        gateway.tool_blacklist = frozenset({"view_save"})
        with TestClient(Starlette(routes=routes(gateway))) as client:
            blocked = client.post(f"{PROJECT_PATH}/interface", json={
                "operation": "view_save", "arguments": {"workspace_id": "session-1", "view_id": "view-1"},
            })
            self.assertEqual(400, blocked.status_code)
            self.assertEqual([], gateway.workbench.calls)

        gateway = FakeGateway()
        with TestClient(Starlette(routes=routes(gateway))) as client:
            wrong = client.post(f"{PROJECT_PATH}/interface", json={
                "operation": "workspace_open", "project_root": "/other",
                "arguments": {"session_id": "session-1"},
            })
            self.assertEqual(400, wrong.status_code)
            self.assertEqual([], gateway.workbench.calls)
            correct = client.post(f"{PROJECT_PATH}/interface", json={
                "operation": "workspace_open", "project_root": str(gateway.root),
                "arguments": {"session_id": "session-1"},
            })
            self.assertEqual(200, correct.status_code)
            self.assertEqual([("workspace_open", {"session_id": "session-1"})], gateway.workbench.calls)

    def test_run_and_save_values_have_request_derived_urls_and_query_errors_do_not(self):
        with TestClient(Starlette(routes=routes(FakeGateway())), base_url="http://workbench.test") as client:
            self.assertEqual(404, client.post(f"{PROJECT_PATH}/save", json={"sql": "SELECT 1"}).status_code)
            self.assertEqual(404, client.post(f"{PROJECT_PATH}/worksheet-save", json={"sql": "SELECT 1"}).status_code)
            view = client.post(f"{PROJECT_PATH}/view-save", json={"sql": "SELECT 1", "name": "view"}).json()
            self.assertEqual("view", view["kind"])
            self.assertEqual("view", view["name"])
            saved = client.post(f"{PROJECT_PATH}/run", json={"sql": "SELECT 1", "save": True}).json()
            self.assertEqual(
                "http://workbench.test/caprmedio/workbench/caprmedio?query=q_1", saved["saved_query_url"],
            )
            named = client.post(f"{PROJECT_PATH}/run", json={"sql": "SELECT 1", "save": True, "name": "named"}).json()
            self.assertEqual("named", named["name"])
            unnamed = client.post(f"{PROJECT_PATH}/run", json={"sql": "SELECT 1", "save": True, "name": "   "}).json()
            self.assertNotIn("name", unnamed)
            failed = client.post(f"{PROJECT_PATH}/run", json={"sql": "bad"})
            self.assertEqual(400, failed.status_code)
            self.assertEqual({"error": "bad query"}, failed.json())

    def test_built_assets_follow_the_workbench_route_when_available(self):
        frontend = FRONTEND_ROOT / "dist"
        index = frontend / "index.html"
        if not index.is_file():
            self.skipTest("frontend build is not present")
        with patch.object(workbench_web, "_FRONTEND", frontend):
            app = Starlette(routes=routes(FakeGateway()))
            with TestClient(app) as client:
                self.assertEqual(200, client.get(PROJECT_PATH).status_code)
                assets = re.findall(r'(?:src|href)="([^"?#]+)', index.read_text())
                self.assertTrue(assets)
                for asset in assets:
                    self.assertTrue(asset.startswith(f"{WORKBENCH_PATH}/assets/"))
                    self.assertNotIn("/assets/assets/", asset)
                    self.assertEqual(200, client.get(asset).status_code, asset)

    def test_shared_routes_require_and_forward_the_explicit_project_root(self):
        gateway = FakeGateway()
        app = Starlette(routes=routes(gateway, shared=True))
        with TestClient(app) as client:
            self.assertEqual(404, client.get(WORKBENCH_PATH).status_code)
            self.assertEqual(400, client.get(PROJECT_PATH).status_code)
            self.assertEqual(200, client.get(f"{PROJECT_PATH}?project_root=/project").status_code)
            self.assertEqual(404, client.get(f"{WORKBENCH_PATH}/wrong?project_root=/project").status_code)
            self.assertEqual(1, client.post(f"{PROJECT_PATH}/run", json={"project_root": "/project", "sql": "SELECT 1"}).json()["row_count"])
            named = client.post(f"{PROJECT_PATH}/run", json={"project_root": "/project", "sql": "SELECT 1", "save": True, "name": "shared"}).json()
            self.assertEqual("shared", named["name"])
            partial = client.post(f"{PROJECT_PATH}/run", json={"project_root": "/project", "sql": "partial"})
            self.assertEqual(200, partial.status_code)
            self.assertEqual("partial", partial.json()["outcome"])
            self.assertEqual("journal unavailable", partial.json()["save_error"])
            failure = client.post(f"{PROJECT_PATH}/run", json={"project_root": "/project", "sql": "bad"})
            self.assertEqual(400, failure.status_code)
            self.assertEqual({"error": "bad query"}, failure.json())
        self.assertEqual(["/project", "/project", "/project", "/project"], gateway.roots)


if __name__ == "__main__":
    unittest.main()
