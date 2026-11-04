# CA-E-676@9

from __future__ import annotations

from pathlib import Path
import re
import sys
import tempfile
from types import MappingProxyType
import unittest
import uuid
from unittest.mock import patch

from mcp import types
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
    async def call(self, name, arguments):  # noqa: C901
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
        if name == "query_saved_list":
            return {"items": []}
        if name == "query_load":
            return {"saved_query_id": arguments["reference"], "kind": "query", "sql": "SELECT 1"}
        if name in ("query_save", "worksheet_save"):
            value = {"saved_query_id": "q_1", "kind": "query", "sql": arguments["sql"]}
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
        if name == "query_check":
            return {"valid": True, "row_count": 1, "column_count": 1}
        return {
            "query_id": "query-1",
            "columns": [{"name": "value", "type": "VARCHAR"}],
            "rows": [["<script>x</script>"]],
            "row_count": 1,
            "column_count": 1,
            "offset": 0,
            "page_size": arguments.get("page_size", 100),
            "has_more": False,
        }


class FakeGateway:
    def __init__(self):
        self.workbench = FakeWorkbench()
        self.roots = []
        settings = MappingProxyType({"project": MappingProxyType({"name": PROJECT_NAME})})
        self.selection = type("Selection", (), {"settings": settings})()

    def _selection(self, root):
        if root != "/project":
            raise ValueError("invalid_project_root")
        return self.selection

    async def call(self, _context, params):
        self.roots.append(params.arguments["project_root"])
        try:
            value = await self.workbench.call(params.name, params.arguments)
            return types.CallToolResult(content=[], structured_content=value)
        except ExplicitBlockingRuntimeFailure as error:
            return types.CallToolResult(
                content=[], structured_content={"error": error.message}, is_error=True,
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

    def test_saved_values_have_request_derived_urls_and_query_errors_do_not(self):
        with TestClient(Starlette(routes=routes(FakeGateway())), base_url="http://workbench.test") as client:
            saved = client.post(f"{PROJECT_PATH}/save", json={"sql": "SELECT 1"}).json()
            self.assertEqual(
                "http://workbench.test/caprmedio/workbench/caprmedio?query=q_1", saved["saved_query_url"],
            )
            named = client.post(f"{PROJECT_PATH}/save", json={"sql": "SELECT 1", "name": "named"}).json()
            self.assertEqual("named", named["name"])
            unnamed = client.post(f"{PROJECT_PATH}/save", json={"sql": "SELECT 1", "name": "   "}).json()
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
            named = client.post(f"{PROJECT_PATH}/save", json={"project_root": "/project", "sql": "SELECT 1", "name": "shared"}).json()
            self.assertEqual("shared", named["name"])
            failure = client.post(f"{PROJECT_PATH}/run", json={"project_root": "/project", "sql": "bad"})
            self.assertEqual(400, failure.status_code)
            self.assertEqual({"error": "bad query"}, failure.json())
        self.assertEqual(["/project", "/project", "/project"], gateway.roots)


if __name__ == "__main__":
    unittest.main()
