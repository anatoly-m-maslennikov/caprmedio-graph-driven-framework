"""Focused MCP admission checks for reviewed O016 Workflow revisions."""

# implementation of:
# Requirement: CA-R-2117
# Method: CA-M-431

from __future__ import annotations

from pathlib import Path
import sys
from typing import cast
import unittest
from unittest.mock import patch


MCP = Path(__file__).resolve().parents[1]
APP = MCP.parent / "203_APPS" / "WORKFLOW_ORCHESTRATOR"
TOOLS = MCP.parent / "201_TOOLS"
for location in (MCP, APP, TOOLS):
    if str(location) not in sys.path:
        sys.path.insert(0, str(location))

from selected_route_adapter import SelectedRouteAdapter  # noqa: E402
import selected_route_interactive  # noqa: E402
import selected_routes  # noqa: E402


class _QueueProbe:
    def __init__(self) -> None:
        self.calls = 0

    def run_selected_operation(self, _request: dict[str, object]) -> dict[str, object]:
        self.calls += 1
        raise AssertionError("unknown O016 revisions must not fall back to the queue")


class _Adapter:
    def __init__(self, version: int, queue: _QueueProbe) -> None:
        self.routes = {
            "run_implementation_workflow": {
                "entry_step": "CA-O-231",
                "workflow": {"atom_id": "CA-O-016", "version": version},
            }
        }
        self.queue = queue

    def _support(self) -> _QueueProbe:
        return self.queue

    @staticmethod
    def _result(
        _request: object, disposition: str, outcome: str, diagnostic: str
    ) -> dict[str, object]:
        return {"disposition": disposition, "outcome": outcome, "diagnostics": [diagnostic]}


class SelectedRouteVersionAdmissionTests(unittest.TestCase):
    def test_direct_version_20_is_current_but_legacy_17_is_not(self) -> None:
        request = {"mode": "execute", "operation_route": "run_implementation_workflow"}
        for version in (18, 20):
            with self.subTest(version=version):
                route = {
                    "entry_step": "CA-O-231",
                    "workflow": {"atom_id": "CA-O-016", "version": version},
                }
                self.assertTrue(selected_route_interactive.is_current_integrated_execute(route, request))
        legacy = {
            "entry_step": "CA-O-231",
            "workflow": {"atom_id": "CA-O-016", "version": 17},
        }
        self.assertFalse(selected_route_interactive.is_current_integrated_execute(legacy, request))

    def test_unknown_versions_are_refused_before_queue_fallback(self) -> None:
        request = {"mode": "execute", "operation_route": "run_implementation_workflow"}
        for version in (19, 21):
            with self.subTest(version=version):
                queue = _QueueProbe()
                adapter = _Adapter(version, queue)
                result = SelectedRouteAdapter._invoke_validated(
                    cast(SelectedRouteAdapter, adapter), "run_implementation_workflow", request
                )
                self.assertEqual("rejected", result["disposition"])
                self.assertEqual("rejected", result["outcome"])
                self.assertIn(f"O016@{version}", result["diagnostics"][0])
                self.assertEqual(0, queue.calls)

    def test_public_execute_refuses_unknown_versions_before_queue_fallback(self) -> None:
        request = {"mode": "execute", "operation_route": "run_implementation_workflow"}
        for version in (19, 21):
            with self.subTest(version=version):
                queue = _QueueProbe()
                manifest = {
                    "routes": [
                        {
                            "route": "run_implementation_workflow",
                            "entry_step": "CA-O-231",
                            "workflow": {"atom_id": "CA-O-016", "version": version},
                        }
                    ]
                }
                adapter = SelectedRouteAdapter(Path.cwd(), service=queue, strict_manifest=False)
                with (
                    patch.object(selected_routes, "load_selected_manifest", return_value=manifest),
                    patch.object(adapter, "_validate_request", return_value=request),
                    patch.object(adapter, "_validate_execute", return_value=None),
                    patch.object(adapter, "_preflight_lifecycle", return_value=None),
                    patch.object(selected_routes, "_log_structured_failure", return_value=None),
                ):
                    result = adapter.invoke("run_implementation_workflow", request)
                self.assertEqual("rejected", result["disposition"])
                self.assertEqual("rejected", result["outcome"])
                self.assertIn(f"O016@{version}", result["diagnostics"][0])
                self.assertEqual(0, queue.calls)


if __name__ == "__main__":
    unittest.main()
