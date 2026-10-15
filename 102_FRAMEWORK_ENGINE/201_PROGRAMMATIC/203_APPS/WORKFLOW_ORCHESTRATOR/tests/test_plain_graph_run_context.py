"""Native context binds actual Run state rather than Journal append locations."""

from pathlib import Path
from types import SimpleNamespace
import sys
import unittest

APP = Path(__file__).resolve().parents[1]
TOOLS = APP.parents[1] / "201_TOOLS"
for location in (APP, TOOLS, TOOLS / "GENERATE_ENTITY_GRAPH"):
    sys.path.insert(0, str(location))

from selected_execution import SelectedExecution  # noqa: E402
import generate_entity_graph as graph  # noqa: E402


class PlainGraphRunContextTests(unittest.TestCase):
    def session(self):
        return SimpleNamespace(
            actual={
                "workflow": {
                    "run_id": "workflow",
                    "kind": "workflow",
                    "definition": {"atom_id": "workflow-definition"},
                },
                "step": {
                    "run_id": "step",
                    "kind": "step",
                    "parent_run_id": "workflow",
                    "definition": {"atom_id": "step-definition"},
                },
                "action": {
                    "run_id": "action",
                    "kind": "action",
                    "parent_run_id": "step",
                    "definition": {"atom_id": "CA-O-134"},
                },
            },
            request={},
        )

    def test_actual_action_context_needs_no_journal_receipt(self):
        session = self.session()
        bound = SelectedExecution._graph_parameters_with_actual_recording(
            {"graph_kind": "entities"},
            session,
            workflow_run_id="workflow",
            step_run_id="step",
            action_run_id="action",
        )
        context = bound["run_recording_context"]
        self.assertTrue(graph.is_actual_recording_context(context))
        self.assertEqual(session.actual["action"], context.action_run)
        self.assertIsNone(context.authorization_evidence())

    def test_wrong_source_run_lineage_does_not_mint_context(self):
        session = self.session()
        session.actual["action"]["parent_run_id"] = "other-step"
        parameters = {"graph_kind": "entities"}
        self.assertIs(
            parameters,
            SelectedExecution._graph_parameters_with_actual_recording(
                parameters,
                session,
                workflow_run_id="workflow",
                step_run_id="step",
                action_run_id="action",
            ),
        )


if __name__ == "__main__":
    unittest.main()
