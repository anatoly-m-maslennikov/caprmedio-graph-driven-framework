"""Preview recording boundaries begin after Project-scoped transport startup."""

from contextlib import asynccontextmanager
from pathlib import Path
import tempfile
from types import SimpleNamespace
from typing import Any, AsyncIterator, Awaitable, Callable
import unittest
from unittest.mock import patch

from mcp import types

import test_selected_query_mcp_e2e as query_harness
import test_selected_workflows_docker_e2e as harness


class SelectedWorkflowsPreviewBoundaryTests(unittest.IsolatedAsyncioTestCase):
    async def test_preview_observes_handshake_lock_but_still_refuses_tool_record_writes(
        self,
    ) -> None:
        temporary_root = (
            harness.ROOT / ".caprmedio_tmp/tests/test_selected_workflows_docker_transport"
        )
        temporary_root.mkdir(parents=True, exist_ok=True)
        for kind in ("route", "query"):
            with (
                self.subTest(kind=kind),
                tempfile.TemporaryDirectory(dir=temporary_root) as directory,
            ):
                root = Path(directory)
                journal = root / ".caprmedio_caprmedio/_journal"
                journal.mkdir(parents=True)
                lock = root / ".caprmedio_runtime/runtime/mcp_hot_reload/fixture/gateway.lock"
                mutate = [False]

                @asynccontextmanager
                async def client_with_startup_lock(parameters: Any) -> AsyncIterator[Any]:
                    lock.parent.mkdir(parents=True)
                    lock.write_bytes(b"")

                    async def call_tool(
                        tool: str, arguments: dict[str, Any], *, read_timeout_seconds: float
                    ) -> types.CallToolResult:
                        self.assertEqual(20, read_timeout_seconds)
                        if mutate[0]:
                            (journal / "unrequested.ndjson").write_text('{"event":"unrequested"}\n')
                        return types.CallToolResult(
                            content=[],
                            structured_content={
                                "disposition": "preview",
                                "proposal_receipt": {},
                                "proposal_receipt_digest": "sealed",
                            },
                        )

                    yield SimpleNamespace(call_tool=call_tool)

                case = harness.SelectedWorkflowsDockerEndToEnd()
                runtime: Any = SimpleNamespace(root=root.resolve())
                fixture: Any = SimpleNamespace(
                    root=root,
                    case=SimpleNamespace(route="fixture"),
                    request=lambda **_: {},
                    snapshot=lambda: {},
                )
                query = query_harness.SelectedQueryMcpEndToEnd()
                query.harness, query.runtime, query.fixture = case, runtime, fixture
                preview: Callable[[], Awaitable[Any]] = (
                    (lambda: case._preview(runtime, root, fixture, "fixture-preview"))
                    if kind == "route"
                    else (lambda: query._preview("fixture-preview"))
                )
                context = SimpleNamespace(candidate_image_digest="sha256:" + "a" * 64)
                with (
                    patch.object(harness, "E2E_CONTEXT", context),
                    patch.object(
                        harness,
                        "_stdio_client",
                        client_with_startup_lock,
                    ),
                ):
                    try:
                        self.assertFalse(lock.exists())
                        await preview()
                        self.assertIn(
                            lock.relative_to(root).as_posix(), case._recording_snapshot(root)
                        )
                        mutate[0] = True
                        with self.assertRaisesRegex(
                            AssertionError, "preview must not write|must not create or change"
                        ):
                            await preview()
                    finally:
                        await case._disconnect()
