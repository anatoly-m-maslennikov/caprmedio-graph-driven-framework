"""Actual native batch bytes, exact predecessors and no uncertain replay."""

import copy
import json
from pathlib import Path
import sys
import unittest
from unittest.mock import patch

APP = Path(__file__).resolve().parents[1]
TOOLS = APP.parent.parent / "201_TOOLS"
for location in (APP, TOOLS, TOOLS / "tests"):
    sys.path.insert(0, str(location))

import atom_operations as operations  # noqa: E402
import atom_subject_apply as native  # noqa: E402
import backend  # noqa: E402
import subject_batch_execution as batch  # noqa: E402
from selected_execution import SelectedExecution, SelectedExecutionError  # noqa: E402
from subject_batch_stage import stage_subject_batch  # noqa: E402
from subject_batch_fixture import SubjectBatchProject  # noqa: E402

EFFECT_TIME = "2026-10-15 19:20:21 +0400"


class SubjectBatchExecutionTests(unittest.TestCase):
    def setUp(self):
        self.project = SubjectBatchProject(self, count=3)
        self.archives = self.project.archives()
        self.runner, self.frozen = self.project.execution()

    def progress(self):
        path = (
            self.runner.run_directory(self.frozen["request"]["run_id"])
            / "subject_batch_progress.json"
        )
        return json.loads(path.read_bytes())

    def assert_changed(self, ordinal):
        project, path = self.project, self.project.paths[ordinal]
        before = operations.parse_carrier(project.before[path], path)
        after = operations.parse_carrier(path.read_bytes(), path)
        expected = copy.deepcopy(before.metadata)
        expected["subjects"]["governs"] = "Atom.State"
        expected.update(version=before.metadata["version"] + 1, updated_at=EFFECT_TIME)
        self.assertEqual(expected, after.metadata)
        self.assertEqual(before.body, after.body)
        self.assertEqual(project.before[path], self.archives[ordinal].read_bytes())

    def assert_untouched(self, ordinal):
        path = self.project.paths[ordinal]
        self.assertEqual(self.project.before[path], path.read_bytes())
        self.assertFalse(self.archives[ordinal].exists())

    def test_fresh_runner_executes_without_extra_confirmation_and_native_effects_are_exact(self):
        reports = set(self.project.root.rglob("*update-assessment*"))
        self.assertEqual(set(), reports)
        reconnect = SelectedExecution(self.project.root)
        frozen = reconnect.load(self.frozen["request"]["run_id"])
        with patch.object(native, "current_timestamp", return_value=EFFECT_TIME):
            result = reconnect.dispatch(frozen)
        self.assertEqual("terminal", result["disposition"])
        for ordinal in range(3):
            self.assert_changed(ordinal)
        self.assertEqual(reports, set(self.project.root.rglob("*update-assessment*")))
        self.assertEqual("completed", self.progress()["state"])
        with patch.object(
            batch, "subject_update_action", side_effect=AssertionError("replayed")
        ) as publisher:
            self.assertEqual(result, reconnect.dispatch(frozen))
        publisher.assert_not_called()

    def test_first_failure_preserves_completed_atom_and_skips_later(self):
        staged = stage_subject_batch(self.project.root, self.project.parameters, limit=3)
        self.project.use_reviewed_packet(staged["reviewed_packet"])
        drafts = [
            self.project.root / item["draft"]["path"] for item in self.project.packet["atoms"]
        ]
        draft_bytes = [path.read_bytes() for path in drafts]
        self.project.commit_drafts()
        self.archives = self.project.archives()
        self.runner, self.frozen = self.project.execution("draft-backed-first-failure")
        original = native.subject_update_action
        observed = []

        def fail_second(root, parameters, **kwargs):
            observed.append(parameters["target"]["atom_id"])
            if parameters["target"] == self.project.targets[1]:
                return {
                    "operation": "update",
                    "outcome": "failed",
                    "effects": [],
                    "observed": parameters["target"],
                }
            return original(root, parameters, **kwargs)

        with (
            patch.object(batch, "subject_update_action", side_effect=fail_second),
            patch.object(native, "current_timestamp", return_value=EFFECT_TIME),
        ):
            result = self.runner.dispatch(self.frozen)
        self.assert_changed(0)
        self.assert_untouched(1)
        self.assert_untouched(2)
        self.assertFalse(drafts[0].exists())
        self.assertEqual(draft_bytes[1], drafts[1].read_bytes())
        self.assertEqual(draft_bytes[2], drafts[2].read_bytes())
        self.assertNotIn(self.project.targets[2]["atom_id"], observed)
        self.assertEqual("stopped", self.progress()["state"])
        self.assertEqual("failed", self.progress()["atoms"][-1]["outcome"])
        with patch.object(
            batch, "subject_update_action", side_effect=AssertionError("replayed")
        ) as publisher:
            self.assertEqual(result, self.runner.dispatch(self.frozen))
        publisher.assert_not_called()

    def test_unknown_native_outcome_stops_without_replay(self):
        original = native.subject_update_action

        def uncertain_second(root, parameters, **kwargs):
            if parameters["target"] == self.project.targets[1]:
                raise OSError("fixture connection disappeared")
            return original(root, parameters, **kwargs)

        with (
            patch.object(batch, "subject_update_action", side_effect=uncertain_second),
            patch.object(native, "current_timestamp", return_value=EFFECT_TIME),
        ):
            self.runner.dispatch(self.frozen)
        self.assert_changed(0)
        self.assert_untouched(1)
        self.assert_untouched(2)
        self.assertEqual("stopped", self.progress()["state"])
        self.assertEqual("unknown", self.progress()["atoms"][-1]["outcome"])
        with patch.object(
            batch, "subject_update_action", side_effect=AssertionError("replayed")
        ) as publisher:
            self.runner.dispatch(self.frozen)
        publisher.assert_not_called()

    def test_partial_native_result_keeps_written_atoms_and_skips_later(self):
        original = native.subject_update_action

        def partial_second(root, parameters, **kwargs):
            result = original(root, parameters, **kwargs)
            if parameters["target"] == self.project.targets[1]:
                result["outcome"] = "partial"
                for effect in result["effects"]:
                    effect["state"] = "unknown"
            return result

        with (
            patch.object(batch, "subject_update_action", side_effect=partial_second),
            patch.object(native, "current_timestamp", return_value=EFFECT_TIME),
        ):
            self.runner.dispatch(self.frozen)
        self.assert_changed(0)
        self.assert_changed(1)
        self.assert_untouched(2)
        progress = self.progress()
        self.assertEqual("stopped", progress["state"])
        self.assertEqual(1, progress["completed"])
        self.assertEqual("partial", progress["atoms"][-1]["outcome"])
        self.assertEqual(2, len(progress["atoms"][-1]["effect_refs"]))
        with patch.object(batch, "subject_update_action") as publisher:
            self.runner.dispatch(self.frozen)
        publisher.assert_not_called()

    def test_changed_packet_cannot_publish(self):
        self.project.packet_path.write_bytes(self.project.packet_path.read_bytes() + b"\n")
        with patch.object(
            batch, "subject_update_action", side_effect=AssertionError("changed packet")
        ) as publisher:
            try:
                result = self.runner.dispatch(self.frozen)
            except (ValueError, SelectedExecutionError):
                pass
            else:
                outcome, _, _ = backend._selected_public_outcome(
                    self.frozen, result, self.frozen["request"]["run_id"]
                )
                self.assertNotEqual("completed", outcome)
        publisher.assert_not_called()
        for ordinal in range(3):
            self.assert_untouched(ordinal)


if __name__ == "__main__":
    unittest.main()
