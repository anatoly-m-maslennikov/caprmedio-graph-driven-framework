"""A failed exact-draft cleanup stops a batch without undoing its publication."""

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
import subject_batch_drafts as drafts_module  # noqa: E402
import subject_batch_execution as batch  # noqa: E402
from subject_batch_fixture import SubjectBatchProject  # noqa: E402
from subject_batch_stage import stage_subject_batch  # noqa: E402

EFFECT_TIME = "2026-10-15 19:20:21 +0400"


class SubjectBatchDraftCleanupTests(unittest.TestCase):
    def _staged_project(self, failure):
        project = SubjectBatchProject(self, count=2)
        staged = stage_subject_batch(project.root, project.parameters, limit=2)
        project.use_reviewed_packet(staged["reviewed_packet"])
        drafts = [project.root / item["draft"]["path"] for item in project.packet["atoms"]]
        draft_bytes = [path.read_bytes() for path in drafts]
        project.commit_drafts()
        return project, drafts, draft_bytes, project.archives(), *project.execution(
            f"draft-cleanup-{failure}"
        )

    def _assert_published_prefix(self, project, archives, drafts, draft_bytes, failure):
        path = project.paths[0]
        before = operations.parse_carrier(project.before[path], path)
        after = operations.parse_carrier(path.read_bytes(), path)
        expected = copy.deepcopy(before.metadata)
        expected["subjects"]["governs"] = "Atom.State"
        expected.update(version=before.metadata["version"] + 1, updated_at=EFFECT_TIME)
        self.assertEqual(expected, after.metadata)
        self.assertEqual(project.before[path], archives[0].read_bytes())
        self.assertEqual(project.before[project.paths[1]], project.paths[1].read_bytes())
        self.assertFalse(archives[1].exists())
        self.assertEqual(draft_bytes[1], drafts[1].read_bytes())
        self.assertEqual(failure == "symlink", drafts[0].is_symlink())
        self.assertTrue(drafts[0].exists())

    def _assert_stopped_without_replay(self, runner, frozen, result):
        progress = json.loads(
            (runner.run_directory(frozen["request"]["run_id"]) / "subject_batch_progress.json").read_bytes()
        )
        self.assertEqual("stopped", progress["state"])
        self.assertEqual(0, progress["completed"])
        self.assertEqual(1, len(progress["atoms"]))
        self.assertEqual("partial", progress["atoms"][0]["outcome"])
        self.assertEqual("unknown", progress["atoms"][0]["draft_promotion"]["state"])
        with patch.object(
            batch, "subject_update_action", side_effect=AssertionError("replayed")
        ) as publisher:
            self.assertEqual(result, runner.dispatch(frozen))
        publisher.assert_not_called()

    def test_failed_cleanup_preserves_the_published_prefix_and_stops(self):
        for failure in ("oserror", "changed", "symlink"):
            with self.subTest(failure=failure):
                project, drafts, draft_bytes, archives, runner, frozen = self._staged_project(failure)
                original = drafts_module.remove_promoted_subject_draft

                def fail_cleanup(root, item, native_result, failure=failure):
                    if item["target"] != project.targets[0]:
                        return original(root, item, native_result)
                    if failure == "oserror":
                        raise OSError("fixture cleanup unavailable")
                    if failure == "changed":
                        drafts[0].write_bytes(draft_bytes[0] + b"\nunreviewed cleanup change\n")
                    else:
                        saved = project.root / ".caprmedio_tmp/saved-draft.md"
                        saved.write_bytes(draft_bytes[0])
                        drafts[0].unlink()
                        drafts[0].symlink_to(saved)
                    return original(root, item, native_result)

                with (
                    patch.object(drafts_module, "remove_promoted_subject_draft", side_effect=fail_cleanup),
                    patch.object(native, "current_timestamp", return_value=EFFECT_TIME),
                ):
                    result = runner.dispatch(frozen)
                self._assert_published_prefix(project, archives, drafts, draft_bytes, failure)
                self._assert_stopped_without_replay(runner, frozen, result)


if __name__ == "__main__":
    unittest.main()
