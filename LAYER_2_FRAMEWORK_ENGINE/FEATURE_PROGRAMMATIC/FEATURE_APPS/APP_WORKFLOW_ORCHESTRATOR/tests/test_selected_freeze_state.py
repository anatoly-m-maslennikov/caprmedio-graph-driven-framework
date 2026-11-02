"""Focused parity checks for the extracted selected-Run freeze state."""

from __future__ import annotations

from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch


APP = Path(__file__).resolve().parents[1]
if str(APP) not in sys.path:
    sys.path.insert(0, str(APP))

from selected_execution import SelectedExecution  # noqa: E402
from selected_execution_contracts import SelectedExecutionError, canonical_json  # noqa: E402
from selected_freeze_state import freeze, load, revalidate  # noqa: E402


class SelectedFreezeStateTests(unittest.TestCase):
    def _root(self) -> Path:
        parent = Path(__file__).resolve().parents[3] / ".caprmedio_tmp"
        parent.mkdir(parents=True, exist_ok=True)
        temporary = tempfile.TemporaryDirectory(dir=parent)
        self.addCleanup(temporary.cleanup)
        return Path(temporary.name)

    @staticmethod
    def _request(run_id: str) -> dict[str, object]:
        return {
            "operation": "enqueue_selected",
            "run_id": run_id,
            "execution": {"workflow_run_id": run_id, "requested_runs": []},
        }

    @staticmethod
    def _graph() -> dict[str, object]:
        return {"route": "create_atom", "steps": [], "entry_step": "CA-O-1"}

    def test_extracted_freeze_matches_legacy_state(self) -> None:
        root = self._root()
        request = self._request("freeze-state-parity")
        graph = self._graph()
        old = SelectedExecution.__new__(SelectedExecution)
        old.root = root
        with (
            patch.object(SelectedExecution, "_validate_graph", return_value=graph),
            patch.object(SelectedExecution, "_validate_requested_runs"),
            patch.object(SelectedExecution, "_validate_query_admission"),
            patch.object(SelectedExecution, "_validate_lifecycle_admission", return_value=None),
        ):
            legacy = old.freeze(request)
        state_path = (
            root
            / ".caprmedio_install/workflow_orchestrator/runs/freeze-state-parity/selected_request.json"
        )
        state_path.unlink()
        with (
            patch("selected_freeze_state.validate_graph", return_value=graph),
            patch("selected_freeze_state.validate_requested_runs"),
            patch("selected_freeze_state.validate_query_admission"),
            patch("selected_freeze_state.validate_lifecycle_admission", return_value=None),
        ):
            extracted = freeze(root, request)
        self.assertEqual(canonical_json(legacy), canonical_json(extracted))
        self.assertEqual(extracted, load(root, "freeze-state-parity"))
        with patch("selected_freeze_state.validate_graph", return_value=graph):
            self.assertEqual(extracted["graph"], revalidate(root, extracted))

    def test_revalidate_rejects_a_changed_source_graph(self) -> None:
        root = self._root()
        request = self._request("freeze-state-stale")
        graph = self._graph()
        with (
            patch("selected_freeze_state.validate_graph", return_value=graph),
            patch("selected_freeze_state.validate_requested_runs"),
            patch("selected_freeze_state.validate_query_admission"),
            patch("selected_freeze_state.validate_lifecycle_admission", return_value=None),
        ):
            extracted = freeze(root, request)
        with self.assertRaisesRegex(SelectedExecutionError, "Workflow graph changed"):
            with patch("selected_freeze_state.validate_graph", return_value={"route": "changed"}):
                revalidate(root, extracted)


if __name__ == "__main__":
    unittest.main()
