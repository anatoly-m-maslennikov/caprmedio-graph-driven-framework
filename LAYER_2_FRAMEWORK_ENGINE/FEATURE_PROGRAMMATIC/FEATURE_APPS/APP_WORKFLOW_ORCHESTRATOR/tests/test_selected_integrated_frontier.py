"""Focused contract cases for durable Integrated continuation frontiers."""

from __future__ import annotations

from copy import deepcopy
import os
from pathlib import Path
import shutil
import sys
import tempfile
import unittest
from unittest.mock import patch


APP = Path(__file__).resolve().parents[1]
PROJECT_ROOT = APP.parents[3]
if str(APP) not in sys.path:
    sys.path.insert(0, str(APP))

import selected_integrated_frontier as frontier  # noqa: E402
from selected_integrated_frontier import (  # noqa: E402
    IntegratedFrontierError,
    admit_submission,
    load_pending,
    save_pending,
)
from selected_integrated_frontier_records import digest  # noqa: E402


class SelectedIntegratedFrontierTests(unittest.TestCase):
    """Keep one-use persistence and continuation history independently observable."""

    def setUp(self) -> None:
        temp_parent = PROJECT_ROOT / ".caprmedio_tmp" / "integrated-frontier-tests"
        temp_parent.mkdir(parents=True, exist_ok=True)
        self.temporary = tempfile.TemporaryDirectory(dir=temp_parent)
        self.project = Path(self.temporary.name) / "project"
        self.run_id = "integrated-run-1"
        (self.project / ".git").mkdir(parents=True)
        (self.project / ".caprmedio_tmp").mkdir(parents=True)
        (self.project / ".caprmedio_install/workflow_orchestrator/runs" / self.run_id).mkdir(
            parents=True
        )

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def _frontier(
        self, continuation_id: str, *, candidate: str = "candidate-a"
    ) -> dict[str, object]:
        project_root = self.project.resolve().as_posix()
        return {
            "continuation_id": continuation_id,
            "project": {"root": project_root, "digest": digest(project_root)},
            "run": {"id": self.run_id, "digest": "b" * 64},
            "step": {"id": "CA-O-231", "digest": "c" * 64},
            "action": {"id": "CA-O-017", "digest": "d" * 64},
            "request_digest": "e" * 64,
            "source_digest": "f" * 64,
            "packet_digest": "0" * 64,
            "candidate_digest": candidate,
            "authorization_digest": "1" * 64,
        }

    def _submission(self, continuation_id: str, result: str = "completed") -> dict[str, object]:
        result_digest = digest(result)
        return {
            "continuation_id": continuation_id,
            "result": result,
            "result_digest": result_digest,
        }

    def test_save_and_load_are_idempotent_for_the_same_pending_frontier(self) -> None:
        first = self._frontier("frontier-a")
        save_pending(self.project, self.run_id, first)
        before = load_pending(self.project, self.run_id)
        save_pending(self.project, self.run_id, deepcopy(first))
        after = load_pending(self.project, self.run_id)
        self.assertEqual(before, after)
        self.assertEqual(first, after["frontier"])

    def test_conflicting_frontier_cannot_replace_the_current_cas_record(self) -> None:
        save_pending(self.project, self.run_id, self._frontier("frontier-a"))
        changed = self._frontier("frontier-a", candidate="candidate-changed")
        with self.assertRaises(IntegratedFrontierError):
            save_pending(self.project, self.run_id, changed)
        self.assertEqual(
            "candidate-a", load_pending(self.project, self.run_id)["frontier"]["candidate_digest"]
        )

    def test_consumed_frontier_keeps_receipt_when_next_frontier_is_published(self) -> None:
        first = self._frontier("frontier-a")
        save_pending(self.project, self.run_id, first)
        first_result = admit_submission(self.project, self.run_id, self._submission("frontier-a"))

        second = self._frontier("frontier-b", candidate="candidate-b")
        save_pending(self.project, self.run_id, second)
        self.assertEqual(
            "frontier-b", load_pending(self.project, self.run_id)["frontier"]["continuation_id"]
        )

        duplicate_first = admit_submission(
            self.project, self.run_id, self._submission("frontier-a")
        )
        self.assertEqual(first_result, duplicate_first)
        self.assertEqual(
            "frontier-b", load_pending(self.project, self.run_id)["frontier"]["continuation_id"]
        )

    def test_different_repeat_submission_is_rejected_without_advancing_next_frontier(self) -> None:
        save_pending(self.project, self.run_id, self._frontier("frontier-a"))
        admit_submission(self.project, self.run_id, self._submission("frontier-a"))
        save_pending(
            self.project, self.run_id, self._frontier("frontier-b", candidate="candidate-b")
        )
        conflicting = self._submission("frontier-a", result="different")
        with self.assertRaises(IntegratedFrontierError):
            admit_submission(self.project, self.run_id, conflicting)
        self.assertEqual(
            "frontier-b", load_pending(self.project, self.run_id)["frontier"]["continuation_id"]
        )

    def test_submission_digest_must_match_the_result(self) -> None:
        save_pending(self.project, self.run_id, self._frontier("frontier-a"))
        invalid = self._submission("frontier-a")
        invalid["result_digest"] = "2" * 64
        with self.assertRaises(IntegratedFrontierError):
            admit_submission(self.project, self.run_id, invalid)

    def test_project_root_binding_keeps_same_run_id_isolated(self) -> None:
        save_pending(self.project, self.run_id, self._frontier("frontier-a"))
        state = (
            self.project
            / ".caprmedio_install/workflow_orchestrator/runs"
            / self.run_id
            / "integrated_frontier.json"
        )
        other_project = self.project.parent / "other-project"
        (other_project / ".git").mkdir(parents=True)
        (other_project / ".caprmedio_tmp").mkdir(parents=True)
        destination = (
            other_project
            / ".caprmedio_install/workflow_orchestrator/runs"
            / self.run_id
            / "integrated_frontier.json"
        )
        destination.parent.mkdir(parents=True)
        shutil.copy2(state, destination)
        with self.assertRaises(IntegratedFrontierError):
            load_pending(other_project, self.run_id)

    def test_false_project_metadata_is_rejected(self) -> None:
        false_metadata = self._frontier("frontier-a")
        false_metadata["project"] = {
            "root": self.project.parent.as_posix(),
            "digest": digest(self.project.parent.as_posix()),
        }
        with self.assertRaises(IntegratedFrontierError):
            save_pending(self.project, self.run_id, false_metadata)

    def test_symlinked_and_oversized_carriers_are_rejected_before_read_effects(self) -> None:
        save_pending(self.project, self.run_id, self._frontier("frontier-a"))
        state = (
            self.project
            / ".caprmedio_install/workflow_orchestrator/runs"
            / self.run_id
            / "integrated_frontier.json"
        )
        external = self.project.parent / "external-frontier.json"
        external.write_text(state.read_text(encoding="utf-8"), encoding="utf-8")
        state.unlink()
        state.symlink_to(external)
        with self.assertRaises(IntegratedFrontierError):
            load_pending(self.project, self.run_id)

        state.unlink()
        state.write_bytes(b"x" * (frontier.MAX_RECORD_BYTES + 1))
        with self.assertRaises(IntegratedFrontierError):
            load_pending(self.project, self.run_id)

    def test_state_replacement_stages_under_project_temp(self) -> None:
        replacement_sources: list[Path] = []
        real_replace = os.replace

        def observe(source: str | bytes | Path, destination: str | bytes | Path) -> None:
            replacement_sources.append(Path(os.fsdecode(source)))
            real_replace(source, destination)

        with patch.object(os, "replace", side_effect=observe):
            save_pending(self.project, self.run_id, self._frontier("frontier-a"))
        self.assertTrue(replacement_sources)
        self.assertTrue(replacement_sources[0].is_relative_to(self.project / ".caprmedio_tmp"))


if __name__ == "__main__":
    unittest.main()
