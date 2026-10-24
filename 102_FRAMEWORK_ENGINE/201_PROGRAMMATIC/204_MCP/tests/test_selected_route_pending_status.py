"""Public workflow observation must not expose retained Integrated definitions."""

from __future__ import annotations

from pathlib import Path
import sys
import unittest
from unittest.mock import patch


MCP = Path(__file__).resolve().parents[1]
APP = MCP.parent / "203_APPS" / "WORKFLOW_ORCHESTRATOR"
TOOLS = MCP.parent / "201_TOOLS"
for location in (MCP, APP, TOOLS):
    if str(location) not in sys.path:
        sys.path.insert(0, str(location))

from selected_route_adapter import SelectedRouteAdapter  # noqa: E402
from selected_route_queue import _QueueBackedSelectedSupport  # noqa: E402


class SelectedRoutePendingStatusTests(unittest.TestCase):
    def test_workflow_observation_sanitizes_pending_capture_without_replay(self) -> None:
        response = {
            "status": "pending_action",
            "workflow_run_id": "workflow-run",
            "action_run_id": "action-run",
            "continuation_id": "a" * 64,
            "capture": {
                "prompt": "Perform the captured Action.",
                "packet": {"bound": True},
                "output_schema": {"type": "object"},
                "definitions": {"trusted_methods": ["private"]},
            },
        }

        class Support:
            calls = 0

            @classmethod
            def get_selected_workflow_run(cls, request):
                cls.calls += 1
                self.assertEqual({"run_id": "workflow-run"}, request)
                return response

        class Adapter:
            @staticmethod
            def _support():
                return Support()

            @staticmethod
            def _result(*_args, **_kwargs):
                raise AssertionError("status response must not use an error result")

        result = SelectedRouteAdapter._observe(
            Adapter(), "get_selected_workflow_run", {"run_id": "workflow-run"}, "run_id"
        )

        self.assertEqual(1, Support.calls)
        self.assertNotIn("definitions", result["capture"])
        self.assertEqual("submit_result", result["next_call"]["request"]["operation"])
        self.assertEqual("a" * 64, result["next_call"]["request"]["continuation_id"])

    def test_queue_observation_sanitizes_the_raw_orchestrator_status(self) -> None:
        response = {
            "status": "pending_action",
            "workflow_run_id": "workflow-run",
            "action_run_id": "action-run",
            "continuation_id": "a" * 64,
            "capture": {
                "prompt": "Perform the captured Action.",
                "packet": {"bound": True},
                "output_schema": {"type": "object"},
                "definitions": {"trusted_methods": ["private"]},
            },
        }
        calls: list[object] = []

        class Orchestrator:
            @staticmethod
            def run(root, request):
                calls.append((root, request))
                return response

        support = _QueueBackedSelectedSupport(Path("/selected-project"), object())
        with patch("selected_route_queue.importlib.import_module", return_value=Orchestrator):
            result = support.get_selected_workflow_run({"run_id": "workflow-run"})

        self.assertEqual(
            [(Path("/selected-project"), {"operation": "status", "run_id": "workflow-run"})],
            calls,
        )
        self.assertNotIn("definitions", result["capture"])
        self.assertEqual("submit_result", result["next_call"]["request"]["operation"])


if __name__ == "__main__":
    unittest.main()
