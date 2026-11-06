# CA-E-679@1
# CA-E-680@1
# CA-E-676@10
"""Public MCP proof for explicit Workbench restart."""

from __future__ import annotations

import asyncio
from contextlib import asynccontextmanager
from pathlib import Path
import re
import sys
import tempfile
import threading
import time
import unittest
from unittest.mock import patch

import httpx2
from mcp.client.session import ClientSession
from mcp.client.streamable_http import streamable_http_client


REPOSITORY = Path(__file__).resolve().parents[5]
PROGRAMMATIC = REPOSITORY / "LAYER_2_FRAMEWORK_ENGINE" / "FEATURE_PROGRAMMATIC"
MCP = PROGRAMMATIC / "FEATURE_MCP"
TOOLS = PROGRAMMATIC / "FEATURE_TOOLS"
APP = PROGRAMMATIC / "FEATURE_APPS" / "APP_WORKBENCH"
for location in (MCP, TOOLS, APP.parent, APP / "tests"):
    if str(location) not in sys.path:
        sys.path.insert(0, str(location))

from APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.service import WorkbenchService  # noqa: E402
from http_paths import HEALTH_PATH, MCP_PATH  # noqa: E402
from http_server import create_app  # noqa: E402
from hot_reload import startup_selection  # noqa: E402
from scope_declaration_test_support import write_scope_unit_declarations  # noqa: E402
from workbench_tools import WorkbenchTools  # noqa: E402
from smalltest_support import write_atom, write_settings  # noqa: E402


class _ConfiguredWorkbenchTools(WorkbenchTools):
    """Use the suite's DuckPGQ cache without replacing real Workbench work."""

    def __init__(self, root: Path, extension_directory: Path) -> None:
        super().__init__(root)
        self.extension_directory = extension_directory

    def _owner(self):
        if self._service is None:
            self._service = WorkbenchService(self.root, extension_directory=self.extension_directory)
        return self._service


class _BlockingService:
    """Small lifecycle double: cancellation must not release the adapter lock."""

    def __init__(self) -> None:
        self.started = threading.Event()
        self.release = threading.Event()
        self.closed = False

    def run(self, _sql: str, **_arguments):
        self.started.set()
        self.release.wait(timeout=5)
        return {"rows": []}

    def schema(self):
        return {}

    def close(self) -> None:
        self.closed = True


class _SequencedWorkbenchTools(WorkbenchTools):
    """Exercise adapter lifecycle serialization without replacing production code."""

    def __init__(self, old: _BlockingService, fresh: _BlockingService) -> None:
        super().__init__(Path("/workbench-restart-test"))
        self._service = old
        self._fresh = fresh

    def _owner(self):
        if self._service is None:
            self._service = self._fresh
        return self._service


class WorkbenchRestartTests(unittest.IsolatedAsyncioTestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name).resolve()
        control = write_settings(self.root)
        self.declarations = write_scope_unit_declarations(
            self.root,
            ({"scope_unit_name": "ENGINE", "scope_unit_type": "Ordered", "scope_unit_label": "LAYER", "local_order": 1},),
            control_root=control,
        )
        self.declaration = Path(self.declarations["ENGINE"]["declaration_path"])
        self.declaration_bytes = self.declaration.read_bytes()
        authority = Path(self.declarations["ENGINE"]["authority_path"])
        write_atom(authority / "04_requirement" / "source.md", "CA-R-501")
        self.provider = self.root / "provider.py"
        self.provider.write_text(
            "from mcp.server import MCPServer\n"
            "server = MCPServer('restart-fixture')\n"
            "@server.tool(structured_output=True)\n"
            "def echo() -> dict[str, str]: return {'value': 'ok'}\n"
            "server.run(transport='stdio')\n",
            encoding="utf-8",
        )
        self.app = create_app(
            self.root,
            implementation=self.provider,
            selection=startup_selection(self.root),
        )
        extension_directory = REPOSITORY / ".caprmedio_tmp" / "workbench" / "extensions"
        self.app.gateway.workbench = _ConfiguredWorkbenchTools(self.root, extension_directory)

    @asynccontextmanager
    async def session(self):
        async with self.app.starlette_app.router.lifespan_context(self.app.starlette_app):
            async with httpx2.AsyncClient(
                transport=httpx2.ASGITransport(app=self.app),
                base_url="http://127.0.0.1:18092",
            ) as client:
                transport = streamable_http_client(
                    "http://127.0.0.1:18092" + MCP_PATH,
                    http_client=client,
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

    async def _wait_unavailable(self, session: ClientSession) -> None:
        deadline = time.monotonic() + 10
        while time.monotonic() < deadline:
            response = await session.call_tool("query_schema", {})
            if response.is_error:
                self.assertIn("restart required", str(response.structured_content).lower())
                return
            await asyncio.sleep(0.05)
        self.fail("invalid Scope Unit Declaration did not stop Workbench")

    def _restart_action(self, page: str) -> str:
        action = re.search(
            r'<form method="post" action="([^\"]+)">\s*<button type="submit">Restart Workbench</button>',
            page,
        )
        self.assertIsNotNone(action)
        return action.group(1)

    async def test_restart_recovers_only_workbench_and_requires_an_explicit_retry(self) -> None:
        async with self.session() as (session, client):
            tools = {tool.name for tool in (await session.list_tools()).tools}
            self.assertIn("workbench_restart", tools)

            malformed = await session.call_tool("workbench_restart", {"unexpected": True})
            self.assertTrue(malformed.is_error)

            ran = await session.call_tool("query_run", {"sql": "SELECT 41"})
            self.assertFalse(ran.is_error, ran.structured_content)
            query_id = ran.structured_content["query_id"]
            saved_sql = "WITH source AS (SELECT range AS value FROM range(10)) SELECT value FROM source LIMIT 7"
            saved = await session.call_tool("query_run", {
                "sql": saved_sql, "save": True, "preview": 5, "name": "restart",
            })
            self.assertFalse(saved.is_error, saved.structured_content)
            saved_id = saved.structured_content["saved_query_id"]
            self.assertEqual(saved_sql, saved.structured_content["sql"])
            self.assertEqual([[0], [1], [2], [3], [4]], saved.structured_content["rows"])
            self.assertEqual(5, saved.structured_content["row_count"])
            saved_url = saved.structured_content["saved_query_url"]

            with patch(
                "APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.saved_queries.append_sealed_events",
                side_effect=OSError("disk full"),
            ):
                partial = await session.call_tool("query_run", {"sql": "SELECT 43", "save": True})
            self.assertFalse(partial.is_error, partial.structured_content)
            self.assertEqual([[43]], partial.structured_content["rows"])
            self.assertEqual("partial", partial.structured_content["outcome"])
            self.assertIn("disk full", partial.structured_content["save_error"])
            self.assertFalse((await session.call_tool(
                "query_page", {"query_id": partial.structured_content["query_id"], "offset": 0},
            )).is_error)

            with patch(
                "APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.saved_queries.append_sealed_events",
                side_effect=OSError("disk full"),
            ):
                partial_http = await client.post(
                    "/caprmedio/workbench/fixture/run",
                    json={"sql": "SELECT 44", "save": True},
                )
            self.assertEqual(200, partial_http.status_code)
            self.assertEqual([[44]], partial_http.json()["rows"])
            self.assertEqual("partial", partial_http.json()["outcome"])

            invalid_form = await client.post(
                f"{HEALTH_PATH}/workbench-restart", content='{"unexpected": true}',
                headers={"accept": "text/html", "content-type": "application/json"},
            )
            self.assertEqual(200, invalid_form.status_code)
            self.assertIn("Workbench restart does not accept a request body.", invalid_form.text)
            self.assertFalse((await session.call_tool(
                "query_page", {"query_id": query_id, "offset": 0},
            )).is_error)

            health_page = await client.get(HEALTH_PATH, headers={"accept": "text/html"})
            restart_form = await client.post(
                self._restart_action(health_page.text), data={}, headers={"accept": "text/html"},
            )
            self.assertEqual(200, restart_form.status_code)
            self.assertIn("Workbench is ready.", restart_form.text)
            echo = await session.call_tool("echo", {})
            self.assertFalse(echo.is_error, echo.structured_content)
            self.assertEqual("ok", echo.structured_content["value"])

            invalid = self.declaration.with_suffix(".invalid")
            invalid.write_bytes(
                self.declaration_bytes.replace(
                    b"role: Requirement",
                    b'role: Requirement\natom_id: "CA-R-990099"',
                )
            )
            invalid.replace(self.declaration)
            await self._wait_unavailable(session)
            failed_form = await client.post(
                self._restart_action((await client.get(HEALTH_PATH, headers={"accept": "text/html"})).text),
                data={}, headers={"accept": "text/html"},
            )
            self.assertEqual(200, failed_form.status_code)
            self.assertIn("Workbench restart failed.", failed_form.text)
            failed_restart = await session.call_tool("workbench_restart", {})
            self.assertTrue(failed_restart.is_error)
            self.assertIn("restart required", str(failed_restart.structured_content).lower())

            self.declaration.write_bytes(self.declaration_bytes)
            still_unavailable = await session.call_tool("query_schema", {})
            self.assertTrue(still_unavailable.is_error)

            restarted = await session.call_tool("workbench_restart", {})
            self.assertFalse(restarted.is_error, restarted.structured_content)
            self.assertEqual({"service": "workbench", "status": "ready"}, restarted.structured_content)

            old_page = await session.call_tool("query_page", {"query_id": query_id, "offset": 0})
            self.assertTrue(old_page.is_error)
            restored = await session.call_tool("query_load", {"reference": saved_url})
            self.assertFalse(restored.is_error, restored.structured_content)
            self.assertEqual(saved_id, restored.structured_content["saved_query_id"])
            self.assertEqual(saved_sql, restored.structured_content["sql"])
            fresh = await session.call_tool("query_run", {"sql": "SELECT 42"})
            self.assertFalse(fresh.is_error, fresh.structured_content)
            self.assertEqual([[42]], fresh.structured_content["rows"])
            echo = await session.call_tool("echo", {})
            self.assertFalse(echo.is_error, echo.structured_content)
            self.assertEqual("ok", echo.structured_content["value"])

    async def test_restart_waits_for_a_cancelled_inflight_call(self) -> None:
        old = _BlockingService()
        fresh = _BlockingService()
        tools = _SequencedWorkbenchTools(old, fresh)
        running = asyncio.create_task(tools.call("query_run", {"sql": "SELECT 1"}))
        self.assertTrue(await asyncio.to_thread(old.started.wait, 1))
        running.cancel()
        with self.assertRaises(asyncio.CancelledError):
            await running

        restarting = asyncio.create_task(tools.call("workbench_restart", {}))
        await asyncio.sleep(0.05)
        self.assertFalse(old.closed)
        old.release.set()
        self.assertEqual({"service": "workbench", "status": "ready"}, await restarting)
        self.assertTrue(old.closed)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
