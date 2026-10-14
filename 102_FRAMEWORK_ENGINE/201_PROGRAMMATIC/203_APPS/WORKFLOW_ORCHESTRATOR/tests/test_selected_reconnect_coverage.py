"""Representative transport repetition never removes per-route execution coverage."""

from __future__ import annotations

from contextlib import asynccontextmanager
from pathlib import Path
import sys
import tempfile
from types import SimpleNamespace
from typing import Any, AsyncIterator, Callable, cast
import unittest
from unittest.mock import AsyncMock, patch

from mcp import Client
from mcp.server import MCPServer

TESTS = Path(__file__).resolve().parent
APP = TESTS.parent
for location in (TESTS, APP.parents[1] / "204_MCP"):
    if str(location) not in sys.path:
        sys.path.insert(0, str(location))

import test_selected_workflows_docker_e2e as harness  # noqa: E402
import selected_workflows_docker_fixture as corpus  # noqa: E402
from implementation_server import create_server as _create_server  # noqa: E402

create_server = cast(Callable[[Path], MCPServer[object]], _create_server)


class SelectedReconnectCoverageTests(unittest.IsolatedAsyncioTestCase):
    def _fixture(self, case_id: str) -> corpus.GoldenProject:
        parent = harness.ROOT / ".caprmedio_tmp/tests/selected-reconnect-coverage"
        parent.mkdir(parents=True, exist_ok=True)
        temporary = tempfile.TemporaryDirectory(dir=parent)
        self.addCleanup(temporary.cleanup)
        route = dict(corpus.ROUTE_CASES)[case_id]
        fixture = corpus.GoldenProject(
            harness.ROOT, Path(temporary.name), corpus.GoldenCase(case_id, route)
        )
        fixture.prepare()
        return fixture

    async def _assert_preview_connections(self, case_id: str, expected: int) -> None:
        fixture = self._fixture(case_id)
        connections: list[Client] = []

        @asynccontextmanager
        async def actual_client(_parameters: Any) -> AsyncIterator[Client]:
            async with Client(
                create_server(fixture.root), cache=None, mode="legacy", read_timeout_seconds=60
            ) as client:
                connections.append(client)
                yield client

        case = harness.SelectedWorkflowsDockerEndToEnd("runTest")
        runtime: Any = SimpleNamespace(root=fixture.root.resolve())
        context = SimpleNamespace(candidate_image_digest="sha256:" + "a" * 64)
        with (
            patch.object(harness, "_stdio_client", actual_client),
            patch.object(harness, "E2E_CONTEXT", context),
        ):
            try:
                preview = await case._preview_for_execution(
                    runtime, fixture.root, fixture, f"{case_id}-preview"
                )
                self.assertEqual("preview", preview["disposition"], preview)
                self.assertEqual(expected, len(connections))
            finally:
                await case._disconnect()

    async def test_real_sdk_repeats_only_mutation_and_query_representatives(self) -> None:
        self.assertEqual({"W01", "W15"}, harness._RECONNECT_CASES)
        for case_id, connections in (("W01", 2), ("W02", 1), ("W15", 2)):
            with self.subTest(case=case_id):
                await self._assert_preview_connections(case_id, connections)

    async def test_terminal_polling_keeps_default_and_optional_reconnect(self) -> None:
        for reconnect in (None, True, False):
            with self.subTest(reconnect=reconnect):
                case = harness.SelectedWorkflowsDockerEndToEnd("runTest")
                runtime: Any = SimpleNamespace()
                call = AsyncMock(side_effect=[{"outcome": "running"}, {"outcome": "completed"}])
                with (
                    patch.object(case, "_call", call),
                    patch.object(case, "_disconnect", new_callable=AsyncMock) as disconnect,
                    patch("asyncio.sleep", new_callable=AsyncMock),
                ):
                    kwargs = {} if reconnect is None else {"reconnect": reconnect}
                    result = await case._terminal_status(
                        runtime, harness.ROOT, "terminal-probe", **kwargs
                    )
                    self.assertEqual("completed", result["outcome"])
                    self.assertEqual(2, call.await_count)
                    self.assertEqual(int(reconnect is not False), disconnect.await_count)


if __name__ == "__main__":
    unittest.main()
