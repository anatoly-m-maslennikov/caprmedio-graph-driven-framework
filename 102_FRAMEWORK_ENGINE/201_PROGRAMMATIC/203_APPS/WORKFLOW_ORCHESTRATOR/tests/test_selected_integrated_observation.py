"""Focused read-only status guards for retained Integrated Workflow state."""

# implementation of:
# Requirement: CA-R-1524
# Method: CA-M-405, CA-M-410

from __future__ import annotations

import json
from pathlib import Path
import sys
import tempfile
import unittest
from typing import Any, cast
from unittest.mock import MagicMock, patch


APP = Path(__file__).resolve().parents[1]
APP_STR = str(APP)
sys.path[:] = [path for path in sys.path if path != APP_STR]
sys.path.insert(0, APP_STR)

from selected_execution_contracts import SelectedExecutionError  # noqa: E402
from selected_integrated_frontier_records import IntegratedFrontierError  # noqa: E402
from selected_integrated_observation import _retained_status  # noqa: E402
import selected_integrated_observation as observation  # noqa: E402
from selected_integrated_session_record import CHECKPOINT_NAME, CheckpointRecord  # noqa: E402
from selected_evidence_io import run_directory  # noqa: E402


class SelectedIntegratedObservationTests(unittest.TestCase):
    run_id = "observation-run"
    actual_run_id = "workflow-actual"
    workflow_id = "CA-O-016"
    result_ref = f".caprmedio_install/workflow_orchestrator/runs/{run_id}/graph_result.json"

    def setUp(self) -> None:
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        (self.root / ".git").mkdir()
        (self.root / ".caprmedio_tmp").mkdir()
    def _frozen(self) -> dict[str, Any]:
        return {
            "request": {"run_id": self.run_id, "execution": {"mode": "execute"}},
            "graph": {
                "route": "run_implementation_workflow",
                "workflow": {"atom_id": self.workflow_id, "version": 18},
                "entry_step": "CA-O-231",
            },
        }
    def _receipt(self, **overrides: Any) -> dict[str, Any]:
        receipt: dict[str, Any] = {
            "event_id": "event-1",
            "run_id": self.actual_run_id,
            "disposition": "interrupted",
            "outcome": "interrupted_pending",
            "result_ref": self.result_ref,
            "effect_refs": [],
            "report_ref": None,
        }
        receipt.update(overrides)
        return receipt

    def _record(
        self, *, terminal: dict[str, dict[str, Any]] | None = None,
        interrupted: dict[str, dict[str, Any]] | None = None,
        recording_errors: list[str] | None = None,
    ) -> CheckpointRecord:
        return CheckpointRecord(
            schema_version=1,
            project_root_digest="a" * 64,
            run_id=self.run_id,
            frozen_digest="b" * 64,
            request={"mode": "execute"},
            actual={self.run_id: {"run_id": self.actual_run_id}},
            terminal=terminal or {},
            interrupted=interrupted or {},
            observed_effects={},
            start_event_ids={},
            recording_errors=recording_errors or [],
            evidence_digests={},
        )

    def _evidence(self, **overrides: Any) -> dict[str, bytes]:
        result: dict[str, Any] = {
            "workflow_run_id": self.actual_run_id,
            "workflow_definition_id": self.workflow_id,
            "outcome": "interrupted_pending",
            "step_results": [],
        }
        result.update(overrides)
        return {self.result_ref: json.dumps(result).encode()}

    def _observe(self, record: CheckpointRecord, evidence: dict[str, bytes]) -> dict[str, Any]:
        folder = run_directory(self.root, self.run_id)
        folder.mkdir(parents=True, exist_ok=True)
        (folder / "selected_request.json").write_text("{}", encoding="utf-8")
        (folder / CHECKPOINT_NAME).write_text("{}", encoding="utf-8")
        store = MagicMock()
        store.__enter__.return_value = store
        with (
            patch.object(observation, "load_request", return_value=self._frozen()),
            patch.object(observation, "owns", return_value=True),
            patch.object(observation, "IntegratedFrontierStore", return_value=store) as store_factory,
            patch.object(observation, "load_bound_checkpoint", return_value=(record, evidence)),
            patch.object(
                observation,
                "_pending_status",
                side_effect=AssertionError("status must not publish a prompt"),
            ) as pending,
            patch.object(observation, "shared_tracker") as tracker,
        ):
            result = observation.observe(self.root, self.run_id)
        pending.assert_not_called()
        tracker.assert_not_called()
        store.load.assert_not_called()
        store_factory.assert_called_once_with(self.root, self.run_id)
        return cast(dict[str, Any], result)

    def test_canonical_interrupted_graph_is_publicly_terminal_pending(self) -> None:
        record = self._record(interrupted={self.run_id: self._receipt()})
        result = self._observe(record, self._evidence())
        self.assertEqual("terminal", result["disposition"])
        self.assertEqual("interrupted_pending", result["status"])
        self.assertEqual("interrupted_pending", result["outcome"])
        self.assertEqual("interrupted", result["run_disposition"])
        self.assertEqual(self.actual_run_id, result["workflow_run_id"])
        self.assertEqual(self._evidence(), {self.result_ref: json.dumps(result["graph_result"]).encode()})

    def test_graph_reference_run_definition_and_outcome_mismatches_are_refused(self) -> None:
        cases: tuple[tuple[str, dict[str, Any], dict[str, Any]], ...] = (
            ("reference", {"result_ref": "other.json"}, {}),
            ("run", {}, {"workflow_run_id": "other-run"}), ("receipt-run", {"run_id": "other-run"}, {}),
            ("definition", {}, {"workflow_definition_id": "CA-O-999"}),
            ("outcome", {}, {"outcome": "completed"}),
        )
        for name, receipt_overrides, evidence_overrides in cases:
            with self.subTest(name=name):
                record = self._record(
                    terminal={self.run_id: self._receipt(**receipt_overrides)}
                )
                with self.assertRaises(SelectedExecutionError):
                    _retained_status(
                        self.root,
                        self._frozen(),
                        record,
                        self._evidence(**evidence_overrides),
                    )

    def test_unknown_root_or_child_interruption_stays_pending_without_prompt(self) -> None:
        for requested_id in (self.run_id, "child-run"):
            with self.subTest(requested_id=requested_id):
                record = self._record(
                    interrupted={requested_id: self._receipt(result_ref=None)}
                )
                result = self._observe(record, {})
                self.assertEqual("interrupted", result["disposition"])
                self.assertEqual("interrupted_pending", result["status"])
                self.assertEqual("interrupted_pending", result["outcome"])

    def test_recording_errors_are_retained_on_public_status(self) -> None:
        record = self._record(
            terminal={self.run_id: self._receipt()}, recording_errors=["journal unavailable"]
        )
        result = self._observe(record, self._evidence())
        self.assertEqual(["journal unavailable"], result["recording_errors"])

    def test_valid_project_without_checkpoint_is_not_observed(self) -> None:
        folder = run_directory(self.root, self.run_id)
        folder.mkdir(parents=True, exist_ok=True)
        (folder / "selected_request.json").write_text(json.dumps(self._frozen()), encoding="utf-8")
        with (
            patch.object(observation, "IntegratedFrontierStore") as store,
            patch.object(observation, "load_bound_checkpoint") as reader,
            patch.object(observation, "_pending_status") as pending,
        ):
            result = cast(dict[str, Any], observation.observe(self.root, self.run_id))
        self.assertEqual("not_observed", result["status"])
        self.assertEqual(self.run_id, result["requested_workflow_run_id"])
        self.assertNotIn("workflow_run_id", result)
        store.assert_not_called()
        reader.assert_not_called()
        pending.assert_not_called()

    def test_arbitrary_non_project_root_cannot_return_not_observed(self) -> None:
        arbitrary = self.root / "arbitrary"
        folder = run_directory(arbitrary, self.run_id)
        folder.mkdir(parents=True, exist_ok=True)
        (folder / "selected_request.json").write_text("{}", encoding="utf-8")
        with (
            patch.object(observation, "load_request", return_value=self._frozen()),
            patch.object(observation, "owns", return_value=True),
            self.assertRaises(IntegratedFrontierError),
        ):
            observation.observe(arbitrary, self.run_id)


if __name__ == "__main__":
    unittest.main()
