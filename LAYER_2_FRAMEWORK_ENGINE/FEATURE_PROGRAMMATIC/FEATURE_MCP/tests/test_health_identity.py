"""Identity gates for bounded MCP Tool and Workflow observations."""
from pathlib import Path
import sys
import unittest


APP = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(APP))
from health_observations import HealthObservations  # noqa: E402


class HealthIdentityTests(unittest.TestCase):
    def setUp(self):
        self.observations = HealthObservations()

    def test_action_response_with_parent_workflow_id_is_only_a_tool_observation(self):
        self.observations.record(
            "get_selected_action_run",
            {},
            {
                "action_run_id": "workflow-parent:step:1:action:1",
                "workflow_run_id": "workflow-parent",
                "disposition": "terminal",
                "outcome": "completed",
            },
        )

        snapshot = self.observations.snapshot()
        self.assertEqual(1, len(snapshot["calls"]))
        self.assertEqual("completed", snapshot["calls"][0]["outcome"])
        self.assertEqual([], snapshot["workflows"])

    def test_technical_coordinator_identity_is_not_a_workflow(self):
        self.observations.record(
            "workflow_orchestrator",
            {},
            {
                "coordinator_id": "technical-coordinator-actual",
                "identity_kind": "technical_coordinator",
                "workflow_run_id": "claimed-workflow",
                "disposition": "terminal",
                "outcome": "completed",
            },
        )

        snapshot = self.observations.snapshot()
        self.assertEqual(1, len(snapshot["calls"]))
        self.assertEqual([], snapshot["workflows"])

    def test_genuine_workflow_records_both_rows_and_prefers_explicit_actual_id(self):
        self.observations.record(
            "workflow_orchestrator",
            {"request": {"run_id": "requested-workflow"}},
            {
                "kind": "workflow",
                "requested_run_id": "requested-workflow",
                "workflow_run_id": "workflow-parent",
                "actual_run_id": "workflow-actual",
                "scheduler_status": "SUCCESS",
                "disposition": "terminal",
                "outcome": "completed",
            },
        )

        snapshot = self.observations.snapshot()
        self.assertEqual(1, len(snapshot["calls"]))
        self.assertEqual(1, len(snapshot["workflows"]))
        self.assertEqual("completed", snapshot["calls"][0]["outcome"])
        self.assertEqual("workflow-actual", snapshot["workflows"][0]["run_id"])
        self.assertNotEqual("requested-workflow", snapshot["workflows"][0]["run_id"])
        self.assertNotEqual("workflow-parent", snapshot["workflows"][0]["run_id"])

    def test_invalid_or_nested_workflow_identities_do_not_create_workflow_rows(self):
        cases = (
            {
                "kind": "workflow",
                "workflow_run_id": "../invalid-workflow",
                "outcome": "completed",
            },
            {
                "kind": "workflow",
                "requested_run_id": "requested-workflow",
                "workflow_run_id": "requested-workflow",
                "actual_run_id": "../invalid-actual",
                "outcome": "completed",
            },
            {
                "kind": "workflow",
                "requested_run_id": "requested-workflow",
                "workflow_run_id": "requested-workflow",
                "actual_run_id": None,
                "outcome": "completed",
            },
            {
                "kind": "step",
                "step_run_id": "workflow-parent:step:1",
                "workflow_run_id": "workflow-parent",
                "outcome": "completed",
            },
        )
        for payload in cases:
            with self.subTest(payload=payload):
                self.observations = HealthObservations()
                self.observations.record("workflow_orchestrator", {}, payload)
                snapshot = self.observations.snapshot()
                self.assertEqual(1, len(snapshot["calls"]))
                self.assertEqual([], snapshot["workflows"])


if __name__ == "__main__":
    unittest.main()
