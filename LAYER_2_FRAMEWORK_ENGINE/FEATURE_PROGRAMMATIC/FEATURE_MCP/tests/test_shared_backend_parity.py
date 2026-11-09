# CA-M-506@2
# CA-D-673@14
# CA-E-798@1

"""Shared Workbench transports use one selected native backend lease."""

from __future__ import annotations

import asyncio
from pathlib import Path
import sys
import tempfile
import unittest

MCP = Path(__file__).resolve().parents[1]
TOOLS = MCP.parent / "FEATURE_TOOLS"
sys.path[:0] = [str(MCP), str(TOOLS), str(TOOLS / "VALIDATE_ATOMS")]

from host_runtime_config import load_host_runtime_config  # noqa: E402
from mcp import types  # noqa: E402
from operation_error_boundary import ExplicitBlockingRuntimeFailure  # noqa: E402
from scope_declaration_test_support import write_scope_unit_declarations  # noqa: E402
from shared_gateway import SharedGateway, SharedGatewayRefusal  # noqa: E402


class _Workbench:
    hold: asyncio.Event | None = None
    started: asyncio.Event | None = None

    def __init__(self) -> None:
        self.calls: list[tuple[str, dict[str, object]]] = []

    async def call(self, name: str, arguments: dict[str, object]) -> dict[str, object]:
        self.calls.append((name, arguments))
        if self.started is not None:
            self.started.set()
        if self.hold is not None:
            await self.hold.wait()
        if arguments.get("sql") == "bad":
            raise ExplicitBlockingRuntimeFailure("query_error", "bad query")
        return {"outcome": "completed", "name": name, "arguments": arguments}


class _Gateway:
    blacklists: dict[str, frozenset[str]] = {}
    workbenches: list[_Workbench] = []
    mcp_calls = 0

    def __init__(self, root: Path, *, selection: object) -> None:
        self.root = Path(root)
        self.selection = selection
        self.tool_blacklist = self.blacklists.get(str(root), frozenset())
        self.ready = True
        from workbench_tools import native_tools
        self.tools = native_tools()
        self.workbench = _Workbench()
        self.workbenches.append(self.workbench)

    async def initialize(self) -> None:
        return None

    async def close(self) -> None:
        return None

    async def call(self, _context: object, params: types.CallToolRequestParams) -> types.CallToolResult:
        type(self).mcp_calls += 1
        return types.CallToolResult(
            content=[],
            structured_content=await self.workbench.call(params.name, params.arguments),
        )


class SharedBackendParityTests(unittest.IsolatedAsyncioTestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.base = Path(self.temporary.name).resolve()
        self.projects = self.base / "My_Repos"
        self.roots = [self._project(name) for name in ("alpha", "beta")]
        self.config_path = self.base / "runtime.toml"
        _Gateway.blacklists = {}
        _Gateway.workbenches = []
        _Gateway.mcp_calls = 0
        _Workbench.hold = None
        _Workbench.started = None

    def _project(self, name: str) -> Path:
        root = self.projects / name
        control = root / f".caprmedio_{name}"
        control.mkdir(parents=True)
        (control / "caprmedio_project_settings.toml").write_text(
            f'[project]\nname="{name}"\n[paths]\ncontrol_root="{control.name}"\n'
            f'[artifacts.identity]\nproject_prefix="{name.upper()}"\n'
        )
        write_scope_unit_declarations(root, control_root=control)
        return root

    async def _gateway(self, max_loaded: int = 2) -> SharedGateway:
        self.config_path.write_text(
            "schema_version=1\n[shared_mcp]\n"
            f'projects_root="{self.projects}"\nhttp_port=8092\nmax_loaded_projects={max_loaded}\n'
        )
        gateway = SharedGateway(
            load_host_runtime_config(self.config_path), gateway_factory=_Gateway
        )
        await gateway.initialize()
        self.addAsyncCleanup(gateway.close)
        return gateway

    async def test_mcp_and_native_workbench_return_the_same_result(self) -> None:
        gateway = await self._gateway()
        arguments = {"project_root": str(self.roots[0]), "sql": "SELECT 1"}

        native = await gateway.workbench_call("query_run", arguments)
        mcp = await gateway.call(
            None, types.CallToolRequestParams(name="query_run", arguments=arguments)
        )

        self.assertEqual(native, mcp.structured_content)
        self.assertEqual(1, _Gateway.mcp_calls)
        self.assertEqual({"sql": "SELECT 1"}, native["arguments"])
        rows = gateway.status()["calls"]
        self.assertEqual(["completed", "completed"], [row["outcome"] for row in rows])

    async def test_cancellation_releases_the_shared_project_lease(self) -> None:
        gateway = await self._gateway(max_loaded=1)
        _Workbench.hold = asyncio.Event()
        _Workbench.started = asyncio.Event()
        pending = asyncio.create_task(gateway.workbench_call(
            "query_run", {"project_root": str(self.roots[0]), "sql": "SELECT 1"}
        ))
        await _Workbench.started.wait()
        pending.cancel()
        with self.assertRaises(asyncio.CancelledError):
            await pending

        _Workbench.hold = None
        value = await gateway.workbench_call(
            "query_run", {"project_root": str(self.roots[1]), "sql": "SELECT 2"}
        )
        self.assertEqual("completed", value["outcome"])

    async def test_native_query_error_keeps_a_returned_error_observation(self) -> None:
        gateway = await self._gateway()

        with self.assertRaisesRegex(ExplicitBlockingRuntimeFailure, "bad query"):
            await gateway.workbench_call(
                "query_run", {"project_root": str(self.roots[0]), "sql": "bad"}
            )

        row = gateway.status()["calls"][-1]
        self.assertEqual("failed", row["outcome"])
        self.assertEqual("returned-error", row["error_category"])

    async def test_foreign_and_disabled_project_bindings_refuse(self) -> None:
        _Gateway.blacklists = {str(self.roots[0]): frozenset({"query_run"})}
        gateway = await self._gateway()

        with self.assertRaises(SharedGatewayRefusal) as outside:
            await gateway.workbench_call(
                "query_run", {"project_root": str(self.base), "sql": "SELECT 1"}
            )
        with self.assertRaises(SharedGatewayRefusal) as disabled:
            await gateway.workbench_call(
                "query_run", {"project_root": str(self.roots[0]), "sql": "SELECT 1"}
            )

        self.assertEqual("outside_project_root", outside.exception.code)
        self.assertEqual("project_tool_frontier_stale", disabled.exception.code)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
