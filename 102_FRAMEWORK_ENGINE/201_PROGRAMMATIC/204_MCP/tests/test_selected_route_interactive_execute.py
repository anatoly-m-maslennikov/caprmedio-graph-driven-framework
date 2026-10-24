"""Focused exact-preview admission checks for the Integrated APP route."""

from __future__ import annotations

from pathlib import Path
import sys
import unittest
from unittest.mock import patch


MCP = Path(__file__).resolve().parents[1]
APP = MCP.parent / "203_APPS" / "WORKFLOW_ORCHESTRATOR"
for location in (MCP, APP):
    if str(location) not in sys.path:
        sys.path.insert(0, str(location))

import selected_route_interactive  # noqa: E402


class _Adapter:
    root = Path("/selected-project")

    @staticmethod
    def _result(_request, disposition, outcome, diagnostic):
        return {"disposition": disposition, "outcome": outcome, "diagnostics": [diagnostic]}


class SelectedRouteInteractiveExecuteTests(unittest.TestCase):
    def test_current_integrated_execute_requires_exact_preview_then_enters_app(self) -> None:
        request = {
            "request_id": "request",
            "proposal_receipt": {"sealed": True},
            "proposal_receipt_digest": "digest",
            "requested_runs": [{"kind": "workflow", "requested_run_id": "workflow-run"}],
            "assigned_action_id": "action",
            "operator_authorization": {"authorization_ref": "sealed"},
        }
        captured: dict[str, object] = {}

        class Support:
            @staticmethod
            def run_selected_operation(preview):
                captured["preview"] = preview
                return {
                    "disposition": "preview",
                    "proposal_receipt": {"sealed": True},
                    "proposal_receipt_digest": "digest",
                }

        class Orchestrator:
            @staticmethod
            def run(root, value):
                captured.update(root=root, value=value)
                return {"disposition": "started", "status": "pending_action"}

        with patch.object(selected_route_interactive, "_orchestrator", return_value=Orchestrator):
            result = selected_route_interactive.invoke_integrated_execute(
                _Adapter(), request, Support()
            )

        self.assertEqual({"disposition": "started", "status": "pending_action"}, result)
        self.assertEqual("preview", captured["preview"]["mode"])
        self.assertNotIn("operator_authorization", captured["preview"])
        self.assertEqual(
            {"operation": "enqueue_selected", "run_id": "workflow-run", "execution": request},
            captured["value"],
        )

    def test_current_integrated_execute_refuses_stale_preview(self) -> None:
        request = {
            "request_id": "request",
            "proposal_receipt": {"sealed": True},
            "proposal_receipt_digest": "digest",
        }

        class Support:
            @staticmethod
            def run_selected_operation(_preview):
                return {"disposition": "preview", "proposal_receipt": {"sealed": False}}

        result = selected_route_interactive.invoke_integrated_execute(
            _Adapter(), request, Support()
        )
        self.assertEqual("blocked", result["disposition"])
        self.assertIn("exact current preview", result["diagnostics"][0])


if __name__ == "__main__":
    unittest.main()
