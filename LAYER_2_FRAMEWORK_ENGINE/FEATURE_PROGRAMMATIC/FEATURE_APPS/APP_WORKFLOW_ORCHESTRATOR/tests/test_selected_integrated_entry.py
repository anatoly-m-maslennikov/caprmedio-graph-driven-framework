"""Focused ownership and observation guards for the Integrated APP entry."""

# implementation of:
# Requirement: CA-R-1522, CA-R-1524, CA-R-2117
# Method: CA-M-405, CA-M-410, CA-M-431

from __future__ import annotations

from pathlib import Path
from types import SimpleNamespace
import sys
import tempfile
import unittest
from unittest.mock import MagicMock, patch


APP = Path(__file__).resolve().parents[1]
PROJECT_ROOT = APP.parents[3]
APP_STR = str(APP)
sys.path[:] = [path for path in sys.path if path != APP_STR]
sys.path.insert(0, APP_STR)

from contracts import Enqueue, EnqueueSelected  # noqa: E402
from selected_evidence_io import run_directory  # noqa: E402
from selected_execution_contracts import SelectedExecutionError  # noqa: E402
from selected_integrated_session_record import CHECKPOINT_NAME  # noqa: E402
import selected_integrated_entry as entry  # noqa: E402
import selected_integrated_observation as observation  # noqa: E402


# implementation of:
# Requirement: CA-R-1522, CA-R-1524, CA-R-2117
# Method: CA-M-405, CA-M-410, CA-M-431
class SelectedIntegratedEntryTests(unittest.TestCase):
    # implementation of:
    # Requirement: CA-R-2117
    # Method: CA-M-431
    def setUp(self) -> None:
        parent = PROJECT_ROOT / ".caprmedio_tmp/tests/selected-integrated-entry"
        parent.mkdir(parents=True, exist_ok=True)
        temporary = tempfile.TemporaryDirectory(dir=parent)
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        (self.root / ".git").mkdir()
        (self.root / ".caprmedio_tmp").mkdir()

    # implementation of:
    # Requirement: CA-R-1522, CA-R-2117
    # Method: CA-M-405, CA-M-431
    def test_plain_legacy_request_does_not_require_integrated_project_admission(self) -> None:
        request = Enqueue(
            run_id="legacy-run",
            selection=[],
            criteria_paths=["criteria.md"],
            author="fixture",
            scope="fixture",
        )

        self.assertEqual((False, None), entry.run(self.root, request))

    # implementation of:
    # Requirement: CA-R-1522, CA-R-2117
    # Method: CA-M-405, CA-M-431
    def test_legacy_selected_workflow_falls_back_before_strict_project_admission(self) -> None:
        request = EnqueueSelected(
            run_id="legacy-selected",
            execution={"mode": "execute", "operation_route": "run_implementation_workflow"},
        )
        frozen = {
            "request": request.model_dump(),
            "graph": {
                "route": "run_implementation_workflow",
                "workflow": {"atom_id": "CA-O-016", "version": 17},
                "entry_step": "CA-O-231",
            },
        }

        with (
            patch.object(entry, "_validated_freeze", return_value=frozen),
            patch.object(entry, "project_root") as strict_root,
        ):
            self.assertEqual((False, None), entry.run(self.root, request))

        strict_root.assert_not_called()

    # implementation of:
    # Requirement: CA-R-1522, CA-R-2117
    # Method: CA-M-405, CA-M-431
    def test_malformed_current_workflow_cannot_fall_back(self) -> None:
        request = EnqueueSelected(
            run_id="malformed-current",
            execution={"mode": "execute", "operation_route": "run_implementation_workflow"},
        )
        frozen = {
            "request": request.model_dump(),
            "graph": {
                "route": "run_implementation_workflow",
                "workflow": {"atom_id": "CA-O-016", "version": 18},
                "entry_step": "CA-O-232",
            },
        }

        with (
            patch.object(entry, "_validated_freeze", return_value=frozen),
            patch.object(entry, "project_root") as strict_root,
            self.assertRaisesRegex(SelectedExecutionError, "entry must be CA-O-231"),
        ):
            entry.run(self.root, request)

        strict_root.assert_not_called()

    # implementation of:
    # Requirement: CA-R-1524, CA-R-2117
    # Method: CA-M-405, CA-M-410, CA-M-431
    def test_stale_pending_status_is_refused_before_prompt_publication(self) -> None:
        run_id = "stale-pending"
        folder = run_directory(self.root, run_id)
        folder.mkdir(parents=True)
        (folder / "selected_request.json").write_text("{}", encoding="utf-8")
        (folder / CHECKPOINT_NAME).write_text("{}", encoding="utf-8")
        frozen = {
            "request": {"run_id": run_id, "execution": {"mode": "execute"}},
            "graph": {
                "route": "run_implementation_workflow",
                "workflow": {"atom_id": "CA-O-016", "version": 18},
                "entry_step": "CA-O-231",
            },
        }
        frontier = {"continuation_id": "a" * 64}
        capture = {"prompt": "retained prompt"}
        profile = {"workflow": {"version": 18}}
        methods = [{"atom_id": "CA-M-431"}]
        store = MagicMock()
        store.__enter__.return_value = store
        store.load.return_value = {"frontier": frontier}

        with (
            patch.object(observation, "load_request", return_value=frozen),
            patch.object(observation, "owns", return_value=True),
            patch.object(observation, "shared_tracker", return_value=object()),
            patch.object(observation, "IntegratedFrontierStore", return_value=store),
            patch.object(
                observation,
                "load_bound_checkpoint",
                return_value=(
                    SimpleNamespace(
                        run_id=run_id,
                        actual={},
                        terminal={},
                        interrupted={},
                        recording_errors=[],
                    ),
                    {},
                ),
            ),
            patch.object(observation, "validate") as validate,
            patch.object(observation, "profile_from_frozen", return_value=profile),
            patch.object(observation, "_admitted_methods", return_value=methods),
            patch.object(observation, "load_capture", return_value=capture),
            patch.object(
                observation,
                "revalidate_pending",
                side_effect=SelectedExecutionError("retained Integrated authority is stale"),
            ) as revalidate,
            patch.object(observation, "pending_response") as publish,
            self.assertRaisesRegex(SelectedExecutionError, "authority is stale"),
        ):
            observation.observe(self.root, run_id)

        validate.assert_called_once()
        revalidate.assert_called_once_with(
            self.root, frozen, profile, None, methods, frontier, capture
        )
        publish.assert_not_called()


if __name__ == "__main__":
    unittest.main()
