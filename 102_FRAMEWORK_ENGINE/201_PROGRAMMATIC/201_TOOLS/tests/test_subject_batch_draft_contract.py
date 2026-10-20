"""Closed draft-backed packets and bounded staging collision behavior."""

import unittest

from subject_batch_fixture import SubjectBatchProject
from subject_batch import load_subject_batch
from subject_batch_drafts import subject_batch_draft_path
from subject_batch_stage import stage_subject_batch
from ATOM_UPDATE.atom_update import create_adapter


class SubjectBatchDraftContractTests(unittest.TestCase):
    def test_existing_preparation_adapter_exposes_bounded_batch_staging(self):
        project = SubjectBatchProject(self)
        result = (
            create_adapter(project.root)
            .invoke(
                {
                    "operation": "stage_subject_batch",
                    **project.parameters,
                    "limit": 1,
                }
            )
            .model_dump(mode="json")
        )
        self.assertEqual([], result["errors"])
        self.assertEqual("stage_subject_batch", result["operation"])
        self.assertEqual(1, result["batch"]["completed"])
        self.assertEqual(1, result["batch"]["remaining"])

    def test_invalid_limits_do_not_create_drafts_or_change_sources(self):
        project = SubjectBatchProject(self, count=1)
        draft = subject_batch_draft_path(
            project.root, project.targets[0], project.targets[0]["version"] + 1
        )
        for limit in (0, 11, True, "1"):
            with self.subTest(limit=limit), self.assertRaises(ValueError):
                stage_subject_batch(project.root, project.parameters, limit=limit)
        self.assertFalse(draft.exists())
        self.assertEqual(project.before[project.paths[0]], project.paths[0].read_bytes())

    def test_existing_draft_collision_stops_without_overwrite_or_source_effect(self):
        project = SubjectBatchProject(self, count=1)
        draft = subject_batch_draft_path(
            project.root, project.targets[0], project.targets[0]["version"] + 1
        )
        draft.parent.mkdir(parents=True, exist_ok=True)
        draft.write_bytes(b"fixture-owned existing draft\n")
        progress = stage_subject_batch(project.root, project.parameters, limit=1)
        self.assertEqual("stopped", progress["state"])
        self.assertEqual(0, progress["completed"])
        self.assertEqual(b"fixture-owned existing draft\n", draft.read_bytes())
        self.assertEqual(project.before[project.paths[0]], project.paths[0].read_bytes())
        repeated = stage_subject_batch(project.root, project.parameters, limit=1)
        self.assertEqual("stopped", repeated["state"])
        self.assertTrue(repeated["inspection_required"])

    def test_partial_draft_backing_is_rejected_as_ambiguous(self):
        project = SubjectBatchProject(self)
        staged = stage_subject_batch(project.root, project.parameters, limit=2)
        project.use_reviewed_packet(staged["reviewed_packet"])
        project.packet["atoms"][1].pop("draft")
        project.save_packet()
        with self.assertRaises(ValueError):
            load_subject_batch(project.root, project.parameters)


if __name__ == "__main__":
    unittest.main()
