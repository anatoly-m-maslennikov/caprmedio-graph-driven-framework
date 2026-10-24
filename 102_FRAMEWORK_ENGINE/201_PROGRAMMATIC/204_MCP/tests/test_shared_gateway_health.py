"""Focused health and failure-boundary checks for the shared gateway."""

from __future__ import annotations

import asyncio
from concurrent.futures import CancelledError as FutureCancelledError
from pathlib import Path
import sys
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import patch

MCP = Path(__file__).resolve().parents[1]
TOOLS = MCP.parent / "201_TOOLS"
sys.path[:0] = [str(MCP), str(TOOLS), str(TOOLS / "VALIDATE_ATOMS")]

from health_page import render_health_page  # noqa: E402
from health_observations import MAX_OBSERVATIONS  # noqa: E402
from host_runtime_config import load_host_runtime_config  # noqa: E402
from mcp import types  # noqa: E402
from operation_error_boundary import FailureRecord  # noqa: E402
from shared_gateway import SharedGateway  # noqa: E402
from shared_gateway_support import refusal  # noqa: E402


def _tool():
    return types.Tool(name="echo", inputSchema={"type": "object"}, outputSchema={"type": "object"})


class _Gateway:
    hold = None

    def __init__(self, _root, *, selection):
        self.selection = selection
        self.active = SimpleNamespace(tools=[_tool()])
        self.tool_blacklist = frozenset()

    async def initialize(self):
        return None

    async def close(self):
        return None

    async def call(self, _context, _params):
        if self.hold is not None:
            await self.hold.wait()
        return types.CallToolResult(
            content=[],
            structuredContent={
                "kind": "workflow",
                "actual_run_id": "run-1",
                "outcome": "completed",
            },
        )


class SharedGatewayHealthTests(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.base = Path(self.temporary.name).resolve()
        self.projects = self.base / "My_Repos"
        self.root = self._project("alpha")
        self.other = self._project("beta")

    def _project(self, name):
        root = self.projects / name
        control = root / f".caprmedio_{name}"
        control.mkdir(parents=True)
        (control / "caprmedio_project_settings.toml").write_text(
            f'[project]\nname="{name}"\n[paths]\ncontrol_root=".caprmedio_{name}"\n'
            f'[artifacts.identity]\nproject_prefix="{name.upper()}"\n'
        )
        (control / "project_structure.toml").write_text("schema_version=1\nscope_units=[]\n")
        return root

    def _config(self, max_loaded=2):
        self.config_path = self.base / "runtime.toml"
        self.config_path.write_text(
            "schema_version=1\n[shared_mcp]\n"
            f'projects_root="{self.projects}"\nhttp_port=8092\nmax_loaded_projects={max_loaded}\n'
        )
        _Gateway.hold = None

    async def _gateway(self):
        gateway = SharedGateway(
            load_host_runtime_config(self.config_path), gateway_factory=_Gateway
        )
        await gateway.initialize()
        self.addAsyncCleanup(gateway.close)
        return gateway

    def _params(self, root=None):
        return types.CallToolRequestParams(
            name="echo", arguments={"project_root": str(self.root if root is None else root)}
        )

    async def test_status_and_html_contain_attributable_observations(self):
        self._config()
        gateway = await self._gateway()
        await gateway.call(None, self._params())
        status = gateway.status()
        self.assertEqual(1, len(status["calls"]))
        self.assertEqual(1, len(status["workflows"]))
        self.assertEqual("ALPHA", status["calls"][0]["project_prefix"])
        self.assertEqual(1, len(status["known_project_contexts"]))
        html = render_health_page(status, ready=True, gateway=gateway)
        self.assertIn("Known Project contexts", html)
        self.assertIn(status["calls"][0]["project_instance_id"], html)
        projects = html.split('<section aria-labelledby="projects">')[1].split("</section>")[0]
        self.assertIn("ALPHA / " + status["calls"][0]["project_instance_id"], projects)

    async def test_observer_failure_warns_without_replacing_native_success(self):
        class BrokenObserver:
            def record(self, *_args, **_kwargs):
                raise RuntimeError("SECRET_OBSERVER_FAILURE")

        self._config()
        gateway = await self._gateway()
        gateway.health_observations = BrokenObserver()
        with patch(
            "shared_gateway_support.report_failure",
            return_value=(
                FailureRecord("WARNING", "health_observation_failed", "safe"),
                None,
            ),
        ) as reported:
            response = await gateway.call(None, self._params())
        self.assertFalse(response.is_error)
        self.assertEqual("health_observation_failed", reported.call_args.args[1].code)

    async def test_async_and_future_cancellation_are_not_adapted_to_success(self):
        self._config()
        gateway = await self._gateway()
        wait = asyncio.Event()
        _Gateway.hold = wait
        pending = asyncio.create_task(gateway.call(None, self._params()))
        while not gateway.pool.status()["loaded_projects"]:
            await asyncio.sleep(0)
        pending.cancel()
        with self.assertRaises(asyncio.CancelledError):
            await pending
        with patch(
            "shared_gateway_support.report_failure",
            return_value=(FailureRecord("WARNING", "missing_project_root", "safe"), "SECRET_SINK"),
        ):
            refusal_result = refusal("missing_project_root")
        self.assertEqual(
            ["missing_project_root", "technical_diagnostics_unavailable"],
            refusal_result.structured_content["diagnostics"],
        )
        with patch("shared_gateway_support.report_failure", side_effect=FutureCancelledError()):
            with self.assertRaises(FutureCancelledError):
                refusal("missing_project_root")

    async def test_observer_future_cancellation_propagates(self):
        class CancelledObserver:
            def record(self, *_args, **_kwargs):
                raise FutureCancelledError()

        self._config()
        gateway = await self._gateway()
        gateway.health_observations = CancelledObserver()
        with self.assertRaises(FutureCancelledError):
            await gateway.call(None, self._params())

    async def test_busy_capacity_refuses_another_project(self):
        self._config(max_loaded=1)
        gateway = await self._gateway()
        _Gateway.hold = asyncio.Event()
        first = asyncio.create_task(gateway.call(None, self._params()))
        while not gateway.pool.status()["loaded_projects"]:
            await asyncio.sleep(0)
        refused = await gateway.call(
            None,
            types.CallToolRequestParams(name="echo", arguments={"project_root": str(self.other)}),
        )
        self.assertTrue(refused.is_error)
        _Gateway.hold.set()
        self.assertFalse((await first).is_error)

    async def test_known_project_contexts_are_bounded(self):
        roots = [
            self.root,
            *[self._project(f"project{index}") for index in range(MAX_OBSERVATIONS)],
        ]
        self._config()
        gateway = await self._gateway()
        for root in roots:
            await gateway.call(None, self._params(root))
        contexts = gateway.status()["known_project_contexts"]
        self.assertEqual(MAX_OBSERVATIONS, len(contexts))
        self.assertNotIn("ALPHA", [context["prefix"] for context in contexts])


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
