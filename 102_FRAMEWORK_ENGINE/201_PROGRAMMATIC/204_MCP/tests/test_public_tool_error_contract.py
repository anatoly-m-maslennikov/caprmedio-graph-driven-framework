"""Focused public MCP failure-boundary contracts."""

from __future__ import annotations

import asyncio
from dataclasses import dataclass, field
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

from pydantic import BaseModel

MCP_ROOT = Path(__file__).resolve().parents[1]
TOOLS_ROOT = MCP_ROOT.parent / "201_TOOLS"
TEST_TEMP_ROOT = MCP_ROOT.parents[2] / ".caprmedio_tmp" / "tests" / Path(__file__).stem
TEST_TEMP_ROOT.mkdir(parents=True, exist_ok=True)
for directory in (MCP_ROOT, TOOLS_ROOT):
    if str(directory) not in sys.path:
        sys.path.insert(0, str(directory))

import registered_tool_registry as registry  # noqa: E402
import selected_routes  # noqa: E402
from mcp.server.mcpserver.exceptions import ToolError  # noqa: E402
from operation_error_boundary import ExplicitBlockingRuntimeFailure  # noqa: E402


class _Request(BaseModel):
    value: str


class _Result(BaseModel):
    completed: list[str]
    errors: list[str]


@dataclass(frozen=True)
class _Logger:
    project_prefix: str = "TEST"
    root: Path = Path(".")
    version: str = "test"
    stream: object = None
    environment: str = "test"
    component: str = "TEST"
    records: list[dict[str, object]] = field(default_factory=list)

    def emit(self, **record: object) -> None:
        self.records.append(record)
        return None


class _Adapter:
    def __init__(self, error: Exception | None = None) -> None:
        self.error = error
        self.calls = 0

    def invoke(self, _request: _Request) -> _Result:
        self.calls += 1
        if self.error is not None:
            raise self.error
        return _Result(completed=["one"], errors=[])


class PublicToolErrorContractTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory(
            dir=TEST_TEMP_ROOT, ignore_cleanup_errors=True,
        )
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.logger = _Logger()
        self.fresh_binding = patch.object(registry, "_binding_is_fresh", return_value=True)
        self.fresh_binding.start()
        self.addCleanup(self.fresh_binding.stop)

    def _wrapper(self, adapter: _Adapter):
        binding = {"source_atom": "CA-D-1", "action_ids": ["CA-O-1"]}
        return registry._invoke_wrapper(
            adapter=adapter, input_model=_Request, output_model=_Result,
            mcp_name="example_tool", root=self.root, catalog_binding=binding,
        )

    def _registry_logger(self):
        return patch.object(
            registry, "active_selection",
            return_value=type("Selection", (), {"settings": {}})(),
        ), patch.object(registry, "make_technical_logger", return_value=(self.logger, None))

    def test_request_failure_is_safe_warning_and_invokes_once(self) -> None:
        adapter = _Adapter(ValueError("token=do-not-leak"))
        function = self._wrapper(adapter)
        with self._registry_logger()[0], self._registry_logger()[1]:
            with self.assertRaises(ToolError) as raised:
                asyncio.run(function(_Request(value="bad")))

        self.assertEqual(1, adapter.calls)
        self.assertIn("internal_failure", str(raised.exception))
        self.assertNotIn("do-not-leak", str(raised.exception))
        self.assertEqual("WARNING", self.logger.records[0]["severity"])

    def test_explicit_runtime_failure_is_error_and_blocks(self) -> None:
        adapter = _Adapter(ExplicitBlockingRuntimeFailure("runtime_down", "runtime unavailable"))
        function = self._wrapper(adapter)
        with self._registry_logger()[0], self._registry_logger()[1]:
            with self.assertRaises(ToolError) as raised:
                asyncio.run(function(_Request(value="run")))

        self.assertEqual("ERROR", self.logger.records[0]["severity"])
        self.assertIn("runtime_down", str(raised.exception))

    def test_known_tool_refusal_has_stable_warning_code(self) -> None:
        adapter = _Adapter(ToolError("secret provider detail"))
        function = self._wrapper(adapter)
        with self._registry_logger()[0], self._registry_logger()[1]:
            with self.assertRaises(ToolError) as raised:
                asyncio.run(function(_Request(value="rejected")))

        self.assertIn("request_rejected", str(raised.exception))
        self.assertNotIn("secret provider detail", str(raised.exception))
        self.assertEqual("request_rejected", self.logger.records[0]["code"])
        self.assertEqual("WARNING", self.logger.records[0]["severity"])

    def test_verified_partial_result_is_preserved(self) -> None:
        class PartialAdapter(_Adapter):
            def invoke(self, _request: _Request) -> _Result:
                self.calls += 1
                return _Result(completed=["one"], errors=["two failed"])

        function = self._wrapper(PartialAdapter())
        result = asyncio.run(function(_Request(value="partial")))
        self.assertEqual(["one"], result.completed)
        self.assertEqual(["two failed"], result.errors)

    def test_async_cancellation_is_not_converted_to_tool_error(self) -> None:
        class CancelAdapter(_Adapter):
            async def invoke(self, _request: _Request) -> _Result:
                raise asyncio.CancelledError

        function = self._wrapper(CancelAdapter())
        with self.assertRaises(asyncio.CancelledError):
            asyncio.run(function(_Request(value="cancel")))

    def test_selected_structured_refusal_emits_warning_without_journal(self) -> None:
        adapter = object.__new__(selected_routes.SelectedRouteAdapter)
        adapter.root = self.root
        request = {"request_id": "request-1", "operation_route": "create_atom"}
        with patch.object(selected_routes, "_public_logger", return_value=self.logger):
            result = adapter._result(request, "rejected", "rejected", "input is invalid")

        self.assertEqual("rejected", result["disposition"])
        self.assertEqual(["input is invalid"], result["diagnostics"])
        self.assertEqual("WARNING", self.logger.records[0]["severity"])
        self.assertNotIn("journal", {str(key).lower() for key in self.logger.records[0]})

    def test_logger_absence_is_visible_in_structured_refusal(self) -> None:
        adapter = object.__new__(selected_routes.SelectedRouteAdapter)
        adapter.root = self.root
        request = {"request_id": "request-logger-missing", "operation_route": "create_atom"}
        with patch.object(selected_routes, "_public_logger", return_value=None):
            result = adapter._result(request, "rejected", "rejected", "input is invalid")

        self.assertEqual("rejected", result["disposition"])
        self.assertEqual("rejected", result["outcome"])
        self.assertEqual("request-logger-missing", result["request_id"])
        self.assertEqual("input is invalid", result["diagnostics"][0])
        self.assertEqual("technical diagnostic unavailable", result["diagnostics"][1])

    def test_missing_shared_support_logs_warning_and_preserves_gap_result(self) -> None:
        adapter = object.__new__(selected_routes.SelectedRouteAdapter)
        adapter.root = self.root
        adapter.manifest = {"source_freshness": {"binding": "current"}}
        adapter.routes = {"create_atom": {}}
        request = {
            "operation_route": "create_atom", "request_id": "request-gap",
            "mode": "preview", "source_freshness": {"binding": "current"},
        }
        with (
            patch.object(selected_routes, "load_selected_manifest",
                         return_value={"routes": [], "source_freshness": {"binding": "current"}}),
            patch.object(adapter, "_validate_request", return_value=request),
            patch.object(adapter, "_support", return_value=None),
            patch.object(selected_routes, "_public_logger", return_value=self.logger),
        ):
            result = adapter.invoke("create_atom", request)

        self.assertEqual("blocked", result["disposition"])
        self.assertEqual("implementation_gap", result["outcome"])
        self.assertEqual({"binding": "current"}, result["source_freshness"])
        self.assertEqual("shared implement_run_support is unavailable", result["diagnostics"][0])
        self.assertEqual("WARNING", self.logger.records[0]["severity"])


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
