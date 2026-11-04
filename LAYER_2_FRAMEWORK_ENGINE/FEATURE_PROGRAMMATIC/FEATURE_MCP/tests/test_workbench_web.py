# CA-E-673@2

from __future__ import annotations

from pathlib import Path
import sys
import unittest

from mcp import types
from starlette.applications import Starlette
from starlette.testclient import TestClient

MCP_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(MCP_ROOT))

from workbench_web import routes  # noqa: E402
from operation_error_boundary import ExplicitBlockingRuntimeFailure  # noqa: E402


class FakeWorkbench:
    async def call(self, name, arguments):
        if arguments["sql"] == "bad":
            raise ExplicitBlockingRuntimeFailure("query_error", "bad query")
        if arguments["sql"] == "crash":
            raise RuntimeError("private unexpected connector detail")
        if name == "query_check":
            return {"valid": True, "row_count": 1, "column_count": 1}
        return {"columns": [{"name": "value", "type": "VARCHAR"}], "rows": [["<script>x</script>"]], "row_count": 1, "column_count": 1}


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
    def test_page_and_project_bound_run_check_routes(self):
        gateway = FakeGateway()
        app = Starlette(routes=routes(gateway))
        with TestClient(app) as client:
            page = client.get("/workbench")
            self.assertEqual(200, page.status_code)
            self.assertIn('for="sql"', page.text)
            self.assertIn("textContent", page.text)
            self.assertIn("JSON.stringify(value,null,2)", page.text)
            self.assertNotIn("value.rows===undefined?value:value.rows", page.text)
            self.assertEqual(1, client.post("/workbench/check", json={"sql": "SELECT 1"}).json()["row_count"])
            result = client.post("/workbench/run", json={"sql": "SELECT 1"})
            self.assertEqual(1, result.json()["row_count"])
            for operation in ("run", "check"):
                failure = client.post(f"/workbench/{operation}", json={"sql": "bad"})
                self.assertEqual(400, failure.status_code)
                self.assertEqual({"error": "bad query"}, failure.json())
            failure = client.post("/workbench/run", json={"sql": "crash"})
            self.assertEqual(400, failure.status_code)
            self.assertEqual({"error": "operation failure"}, failure.json())
            failure = client.post("/workbench/check", json={"sql": 1})
            self.assertEqual({"error": "sql must be a string"}, failure.json())

    def test_shared_routes_require_and_forward_the_explicit_project_root(self):
        gateway = FakeGateway()
        app = Starlette(routes=routes(gateway, shared=True))
        with TestClient(app) as client:
            self.assertEqual(400, client.get("/workbench").status_code)
            self.assertEqual(200, client.get("/workbench?project_root=/project").status_code)
            self.assertEqual(1, client.post("/workbench/run", json={"project_root": "/project", "sql": "SELECT 1"}).json()["row_count"])
        self.assertEqual(["/project"], gateway.roots)


if __name__ == "__main__":
    unittest.main()
