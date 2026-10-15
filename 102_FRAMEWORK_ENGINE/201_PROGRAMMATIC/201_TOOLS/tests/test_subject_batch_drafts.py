"""Bounded full edit-draft staging and exact native promotion."""

import copy
import hashlib
import unittest
from unittest.mock import patch

from subject_batch_fixture import SubjectBatchProject
import atom_operations as operations
import atom_subject_apply as native
from atom_subject_patch import prepare_subject_intent, materialize_subject_intent
from subject_batch import load_subject_batch
from subject_batch_authorization import capture_batch_review, persist_subject_batch_confirmation
from subject_batch_stage import stage_subject_batch
from subject_batch_drafts import require_reviewed_draft_candidate
from lifecycle_intents import carrier_descriptor

EFFECT_TIME = "2026-10-15 19:20:21 +0400"


def edit_drafts(project):
    drafts = []
    for path in (project.root / ".caprmedio_caprmedio").rglob("*.md"):
        frontmatter, _ = operations.split_frontmatter(path.read_text())
        identity = operations.frontmatter_scalar(frontmatter, "atom_id")
        if identity is not None and identity.endswith("@draft"):
            drafts.append(path)
    return drafts


class SubjectBatchDraftTests(unittest.TestCase):
    def test_noop_draft_promotion_keeps_original_bytes_version_and_time(self):
        project = SubjectBatchProject(self, count=1)
        path = project.paths[0]
        before = path.read_bytes().replace(b"governs: Atom/Test", b'governs: "Atom.State"')
        path.write_bytes(before)
        project.git("add", project.targets[0]["path"])
        project.git(
            "-c",
            "user.name=Fixture",
            "-c",
            "user.email=fixture@example.invalid",
            "commit",
            "--quiet",
            "-m",
            "Fixture no-op state",
        )
        target = carrier_descriptor(project.root, path.relative_to(project.root).as_posix())
        project.packet["git_checkpoint"] = project.git("rev-parse", "HEAD").strip()
        project.packet["atoms"] = [
            {
                "target": target,
                "subject_patches": [{"field": "governs", "old": "Atom.State", "new": "Atom.State"}],
            }
        ]
        project.save_packet()
        staged = stage_subject_batch(project.root, project.parameters, limit=1)
        project.use_reviewed_packet(staged["reviewed_packet"])
        runner, frozen = project.execution("noop-subject-edit-draft")
        review = capture_batch_review(runner, frozen)
        persist_subject_batch_confirmation(runner, frozen, review, operator_name="golden-operator")
        with patch.object(
            native, "current_timestamp", side_effect=AssertionError("no-op edit time")
        ):
            result = runner.dispatch(frozen)
        self.assertEqual("terminal", result["disposition"])
        self.assertEqual(before, path.read_bytes())
        self.assertEqual([], list((path.parent / "archive").glob("*")))

    def test_staging_is_bounded_resumable_and_keeps_canonical_sources_untouched(self):
        project = SubjectBatchProject(self)
        archives = project.archives()
        first = stage_subject_batch(project.root, project.parameters, limit=1)
        self.assertEqual(1, len(edit_drafts(project)))
        self.assertIsNone(first.get("reviewed_packet"))
        completed = stage_subject_batch(project.root, project.parameters, limit=1)
        project.use_reviewed_packet(completed["reviewed_packet"])
        packet = load_subject_batch(project.root, project.parameters)
        self.assertEqual(2, len(edit_drafts(project)))
        self.assertTrue(all("draft" in item for item in packet["atoms"]))
        for path, archive in zip(project.paths, archives):
            self.assertEqual(project.before[path], path.read_bytes())
            self.assertFalse(archive.exists())
        for item in packet["atoms"]:
            draft = project.root / item["draft"]["path"]
            self.assertIn("draft", draft.parts)
            self.assertEqual(
                item["draft"]["digest"], hashlib.sha256(draft.read_bytes()).hexdigest()
            )
            metadata = operations.parse_carrier(draft.read_bytes(), draft).metadata
            self.assertEqual(item["target"]["atom_id"] + "@draft", metadata["atom_id"])
            self.assertEqual("Draft", metadata["status"])
        canonical = operations.scan_atoms(project.root)
        for target in project.targets:
            self.assertEqual(
                1,
                sum(
                    atom.atom_id == target["atom_id"] and atom.lifecycle != "archived"
                    for atom in canonical
                ),
            )
        self.assertFalse(
            any(atom.atom_id and atom.atom_id.endswith("@draft") for atom in canonical)
        )

    def test_changed_edit_draft_is_rejected_before_any_publication(self):
        project = SubjectBatchProject(self)
        completed = stage_subject_batch(project.root, project.parameters, limit=2)
        project.use_reviewed_packet(completed["reviewed_packet"])
        runner, frozen = project.execution("tampered-subject-edit-draft")
        draft = project.root / project.packet["atoms"][0]["draft"]["path"]
        draft.write_bytes(draft.read_bytes() + b"\nunreviewed body edit\n")
        with self.assertRaises(ValueError):
            capture_batch_review(runner, frozen)
        for path in project.paths:
            self.assertEqual(project.before[path], path.read_bytes())

    def test_promotion_restores_canonical_identity_and_done_status_with_exact_history(self):
        project = SubjectBatchProject(self, count=1, role="Plan", status="Done")
        path, archive = project.paths[0], project.archives()[0]
        completed = stage_subject_batch(project.root, project.parameters, limit=1)
        project.use_reviewed_packet(completed["reviewed_packet"])
        runner, frozen = project.execution("promote-subject-edit-draft")
        review = capture_batch_review(runner, frozen)
        persist_subject_batch_confirmation(runner, frozen, review, operator_name="golden-operator")
        with patch.object(native, "current_timestamp", return_value=EFFECT_TIME):
            result = runner.dispatch(frozen)
        self.assertEqual("terminal", result["disposition"])
        before = operations.parse_carrier(project.before[path], path)
        after = operations.parse_carrier(path.read_bytes(), path)
        expected = copy.deepcopy(before.metadata)
        expected["subjects"]["governs"] = "Atom.State"
        expected.update(version=before.metadata["version"] + 1, updated_at=EFFECT_TIME)
        self.assertEqual(expected, after.metadata)
        self.assertEqual("Done", after.metadata["status"])
        self.assertEqual(before.body, after.body)
        self.assertEqual(project.before[path], archive.read_bytes())
        self.assertEqual(project.fixture.before_mode, path.stat().st_mode & 0o777)
        self.assertEqual(
            1,
            sum(
                atom.atom_id == after.metadata["atom_id"] and atom.lifecycle != "archived"
                for atom in operations.scan_atoms(project.root)
            ),
        )

    def test_repinning_a_body_change_cannot_expand_the_subjects_only_patch(self):
        project = SubjectBatchProject(self, count=1)
        archive = project.archives()[0]
        completed = stage_subject_batch(project.root, project.parameters, limit=1)
        project.use_reviewed_packet(completed["reviewed_packet"])
        pin = project.packet["atoms"][0]["draft"]
        draft = project.root / pin["path"]
        changed = draft.read_bytes() + b"\nunapproved body text\n"
        draft.write_bytes(changed)
        pin["digest"] = hashlib.sha256(changed).hexdigest()
        project.save_packet()
        item = project.packet["atoms"][0]
        prepared = prepare_subject_intent(
            project.root, item["target"], item["subject_patches"], subject_profile="approved"
        )
        candidate = materialize_subject_intent(project.root, prepared, EFFECT_TIME)
        with self.assertRaises(ValueError):
            require_reviewed_draft_candidate(project.root, item, candidate["carrier_bytes"])
        self.assertEqual(project.before[project.paths[0]], project.paths[0].read_bytes())
        self.assertFalse(archive.exists())


if __name__ == "__main__":
    unittest.main()
