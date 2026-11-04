# CA-E-673@3

from __future__ import annotations

from pathlib import Path
import re
import sys
import tempfile
import unittest
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


class FakeWorkbench:
    async def call(self, name, arguments):
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

    def _selection(self, root):
        if root != "/project":
            raise ValueError("invalid_project_root")
        return object()

    async def call(self, _context, params):
        self.roots.append(params.arguments["project_root"])
        try:
            value = await self.workbench.call(params.name, params.arguments)
            return types.CallToolResult(content=[], structured_content=value)
        except ExplicitBlockingRuntimeFailure as error:
            return types.CallToolResult(content=[], structured_content={"diagnostics": [str(error)]}, is_error=True)


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

    def test_frontend_preserves_submit_and_nested_result_contracts(self):
        app = (FRONTEND_ROOT / "src" / "App.svelte").read_text()
        results = (FRONTEND_ROOT / "src" / "lib" / "ResultsTable.svelte").read_text()
        self.assertIn('<Button type="submit" disabled={loading}>Run</Button>', app)
        self.assertIn("JSON.stringify(value)", results)
        self.assertNotIn("String(value)}</td>", results)

    def test_page_and_project_bound_run_check_routes(self):
        gateway = FakeGateway()
        app = Starlette(routes=routes(gateway))
        with TestClient(app) as client:
            page = client.get(WORKBENCH_PATH)
            self.assertEqual(200, page.status_code)
            self.assertIn('id="app"', page.text)
            self.assertIn(f"{WORKBENCH_PATH}/assets/", page.text)
            self.assertEqual(1, client.post(f"{WORKBENCH_PATH}/check", json={"sql": "SELECT 1"}).json()["row_count"])
            result = client.post(f"{WORKBENCH_PATH}/run", json={"sql": "SELECT 1"})
            self.assertEqual(1, result.json()["row_count"])
            large = client.post(f"{WORKBENCH_PATH}/run", json={"sql": "large"})
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
                f"{WORKBENCH_PATH}/page",
                json={"query_id": "query-1", "offset": 100, "page_size": 20},
            )
            self.assertEqual(200, paged.status_code)
            self.assertEqual(100, paged.json()["offset"])
            self.assertEqual(20, paged.json()["page_size"])
            for operation in ("run", "check"):
                failure = client.post(f"{WORKBENCH_PATH}/{operation}", json={"sql": "bad"})
                self.assertEqual(400, failure.status_code)
                self.assertEqual({"error": "bad query"}, failure.json())
            failure = client.post(f"{WORKBENCH_PATH}/run", json={"sql": "crash"})
            self.assertEqual(400, failure.status_code)
            self.assertEqual({"error": "operation failure"}, failure.json())
            failure = client.post(f"{WORKBENCH_PATH}/check", json={"sql": 1})
            self.assertEqual({"error": "sql must be a string"}, failure.json())
            failure = client.post(f"{WORKBENCH_PATH}/page", json={"query_id": "query-1", "offset": -1})
            self.assertEqual({"error": "offset must be a non-negative integer"}, failure.json())

    def test_missing_frontend_does_not_block_query_routes(self):
        missing = Path(self._temporary.name) / "missing"
        with patch.object(workbench_web, "_FRONTEND", missing):
            app = Starlette(routes=routes(FakeGateway()))
            with TestClient(app) as client:
                response = client.get(WORKBENCH_PATH)
                self.assertEqual(503, response.status_code)
                self.assertEqual(
                    {"error": "Workbench frontend is unavailable; build required"}, response.json()
                )
                self.assertEqual(
                    1,
                    client.post(f"{WORKBENCH_PATH}/check", json={"sql": "SELECT 1"}).json()["row_count"],
                )

    def test_built_assets_follow_the_workbench_route_when_available(self):
        frontend = FRONTEND_ROOT / "dist"
        index = frontend / "index.html"
        if not index.is_file():
            self.skipTest("frontend build is not present")
        with patch.object(workbench_web, "_FRONTEND", frontend):
            app = Starlette(routes=routes(FakeGateway()))
            with TestClient(app) as client:
                self.assertEqual(200, client.get(WORKBENCH_PATH).status_code)
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
            self.assertEqual(400, client.get(WORKBENCH_PATH).status_code)
            self.assertEqual(200, client.get(f"{WORKBENCH_PATH}?project_root=/project").status_code)
            self.assertEqual(1, client.post(f"{WORKBENCH_PATH}/run", json={"project_root": "/project", "sql": "SELECT 1"}).json()["row_count"])
        self.assertEqual(["/project"], gateway.roots)


if __name__ == "__main__":
    unittest.main()
