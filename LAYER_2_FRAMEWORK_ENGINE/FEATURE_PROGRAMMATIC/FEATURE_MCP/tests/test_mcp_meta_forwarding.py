"""Keep MCP request metadata across the two gateway boundaries."""

from __future__ import annotations

from pathlib import Path
import sys
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import AsyncMock

MCP = Path(__file__).resolve().parents[1]
TOOLS = MCP.parent / "FEATURE_TOOLS"
sys.path[:0] = [str(MCP), str(TOOLS)]

from health_observations import HealthObservations  # noqa: E402
from hot_reload import Gateway  # noqa: E402
from mcp import types  # noqa: E402
from project_selection import ProjectSelection  # noqa: E402
from shared_gateway import SharedGateway  # noqa: E402


def _params() -> types.CallToolRequestParams:
    return types.CallToolRequestParams(
        name="echo", arguments={"project_root": "/project", "request": "value"},
        meta={"progressToken": "progress"},
    )


class MetaForwardingTests(unittest.IsolatedAsyncioTestCase):
    async def test_single_gateway_forwards_meta_to_implementation_client(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            client = AsyncMock(return_value=types.CallToolResult(content=[]))
            gateway = Gateway(Path(directory))
            params = _params().model_copy(update={"arguments": {"request": "value"}})
            await gateway._implementation_call(None, params, SimpleNamespace(client=client))
            self.assertEqual(params.meta, client.call_tool.await_args.kwargs["meta"])

    async def test_shared_gateway_preserves_meta_when_stripping_project_root(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            selection = ProjectSelection(
                root, root / ".caprmedio_fixture", Path(".caprmedio_fixture"), "a" * 64,
                {"artifacts": {"identity": {"project_prefix": "TEST"}}}, {}, (), {}, "",
            )
            inner = SimpleNamespace(call=AsyncMock(return_value=types.CallToolResult(content=[])))
            entry = SimpleNamespace(selection=selection, gateway=inner)
            gateway = object.__new__(SharedGateway)
            gateway.frontier = object()
            gateway.pool = SimpleNamespace(
                acquire=AsyncMock(return_value=entry), release=AsyncMock(),
            )
            gateway.health_observations = HealthObservations()
            gateway._arguments = lambda _params: (selection, {"request": "value"})
            gateway._current_config = lambda: None
            gateway._selection = lambda _root: selection
            gateway._current_tool = lambda *_args: None
            gateway._remember_project = lambda *_args: None
            params = _params()
            await gateway.call(None, params)
            forwarded = inner.call.await_args.args[1]
            self.assertEqual(params.meta, forwarded.meta)
            self.assertEqual({"request": "value"}, forwarded.arguments)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
