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
from subject_batch_stage import stage_subject_batch
from subject_batch_drafts import require_reviewed_draft_candidate, subject_batch_draft_path
from lifecycle_intents import carrier_descriptor

EFFECT_TIME = "2026-10-15 19:20:21 +0400"


def draft_marker(project, value):
    canonical_id = value.split("@", 1)[0]
    _, role_letter, _ = canonical_id.split("-", 2)
    return operations.parse_draft_marker(
        value,
        project_prefix=operations.project_identity_prefix(project.root),
        role_letter=role_letter,
    )


def edit_drafts(project):
    drafts = []
    for path in (project.root / ".caprmedio_caprmedio").rglob("*.md"):
        frontmatter, _ = operations.split_frontmatter(path.read_text())
        identity = operations.frontmatter_scalar(frontmatter, "atom_id")
        if identity is None:
            continue
        try:
            marker = draft_marker(project, identity)
        except (TypeError, ValueError):
            continue
        if marker is not None and marker.canonical_id is not None:
            drafts.append(path)
    return drafts


def is_draft_marker(project, value):
    try:
        return draft_marker(project, value) is not None
    except (TypeError, ValueError):
        return False


def _id_free_draft_path(project, item):
    target = item["target"]
    current = project.root / target["path"]
    _, role_letter, _ = target["atom_id"].split("-", 2)
    role = next(parent for parent in current.parents if operations.ROLE_DIRECTORY.fullmatch(parent.name))
    identity = f"{operations.project_identity_prefix(project.root)}-{role_letter}"
    name = current.name.replace(target["atom_id"], identity, 1)
    return role / "draft" / name


def _without_frontmatter_line(raw, key):
    lines = raw.decode().splitlines(keepends=True)
    result = []
    removed = False
    for line in lines:
        if not removed and line.startswith(f"{key}:"):
            removed = True
            continue
        result.append(line)
    if not removed:
        raise AssertionError(f"missing frontmatter field: {key}")
    return "".join(result).encode()


def _rewrite_as_id_free(project, item, *, filename=None, suffix=b""):
    preferred = project.root / item["draft"]["path"]
    path = _id_free_draft_path(project, item)
    if filename is not None:
        path = path.with_name(filename)
    raw = _without_frontmatter_line(preferred.read_bytes(), "atom_id") + suffix
    preferred.rename(path)
    path.write_bytes(raw)
    item["draft"] = {
        "path": path.relative_to(project.root).as_posix(),
        "digest": hashlib.sha256(raw).hexdigest(),
    }
    project.save_packet()
    return path


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
        draft_path = project.root / project.packet["atoms"][0]["draft"]["path"]
        self.assertTrue(draft_path.exists())
        metadata = operations.parse_carrier(draft_path.read_bytes(), draft_path).metadata
        marker = draft_marker(project, metadata["atom_id"])
        self.assertEqual(project.packet["atoms"][0]["target"]["version"], marker.proposed_version)
        self.assertEqual(
            subject_batch_draft_path(
                project.root,
                project.packet["atoms"][0]["target"],
                project.packet["atoms"][0]["target"]["version"],
            ),
            draft_path,
        )
        runner, frozen = project.execution("noop-subject-edit-draft")
        with patch.object(
            native, "current_timestamp", side_effect=AssertionError("no-op edit time")
        ):
            result = runner.dispatch(frozen)
        self.assertEqual("terminal", result["disposition"])
        self.assertEqual(before, path.read_bytes())
        self.assertEqual([], list((path.parent / "archive").glob("*")))
        self.assertFalse(draft_path.exists())

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
            marker = draft_marker(project, metadata["atom_id"])
            self.assertEqual(item["target"]["atom_id"], marker.canonical_id)
            self.assertEqual(metadata["version"], marker.proposed_version)
            self.assertEqual(
                subject_batch_draft_path(project.root, item["target"], metadata["version"]),
                draft,
            )
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
            any(atom.atom_id and is_draft_marker(project, atom.atom_id) for atom in canonical)
        )

    def test_legacy_draft_marker_remains_accepted(self):
        project = SubjectBatchProject(self, count=1)
        staged = stage_subject_batch(project.root, project.parameters, limit=1)
        project.use_reviewed_packet(staged["reviewed_packet"])
        item = project.packet["atoms"][0]
        preferred = project.root / item["draft"]["path"]
        metadata = operations.parse_carrier(preferred.read_bytes(), preferred).metadata
        canonical_id = item["target"]["atom_id"]
        legacy = subject_batch_draft_path(project.root, item["target"])
        preferred.rename(legacy)
        raw = legacy.read_bytes().replace(
            f'{canonical_id}@{metadata["version"]}-draft'.encode(),
            f"{canonical_id}@draft".encode(),
        )
        legacy.write_bytes(raw)
        item["draft"] = {
            "path": legacy.relative_to(project.root).as_posix(),
            "digest": hashlib.sha256(raw).hexdigest(),
        }
        project.save_packet()
        loaded = load_subject_batch(project.root, project.parameters)
        self.assertEqual(item["draft"], loaded["atoms"][0]["draft"])

    def test_legacy_draft_version_must_match_materialized_candidate(self):
        project = SubjectBatchProject(self, count=1)
        staged = stage_subject_batch(project.root, project.parameters, limit=1)
        project.use_reviewed_packet(staged["reviewed_packet"])
        item = project.packet["atoms"][0]
        preferred = project.root / item["draft"]["path"]
        metadata = operations.parse_carrier(preferred.read_bytes(), preferred).metadata
        canonical_id = item["target"]["atom_id"]
        legacy = subject_batch_draft_path(project.root, item["target"])
        preferred.rename(legacy)
        raw = legacy.read_bytes().replace(
            f'{canonical_id}@{metadata["version"]}-draft'.encode(),
            f"{canonical_id}@draft".encode(),
        )
        wrong_version = metadata["version"] + 1
        raw = raw.replace(
            f"version: {metadata['version']}".encode(), f"version: {wrong_version}".encode(), 1
        )
        legacy.write_bytes(raw)
        item["draft"] = {
            "path": legacy.relative_to(project.root).as_posix(),
            "digest": hashlib.sha256(raw).hexdigest(),
        }
        project.save_packet()
        prepared = prepare_subject_intent(
            project.root, item["target"], item["subject_patches"], subject_profile="approved"
        )
        candidate = materialize_subject_intent(project.root, prepared, EFFECT_TIME)
        with self.assertRaises(ValueError):
            require_reviewed_draft_candidate(project.root, item, candidate["carrier_bytes"])
        self.assertEqual(project.before[project.paths[0]], project.paths[0].read_bytes())

    def test_id_free_reviewed_draft_roundtrip_preserves_candidate_and_archive(self):
        project = SubjectBatchProject(self, count=1)
        staged = stage_subject_batch(project.root, project.parameters, limit=1)
        project.use_reviewed_packet(staged["reviewed_packet"])
        item = project.packet["atoms"][0]
        draft_path = _rewrite_as_id_free(project, item)
        loaded = load_subject_batch(project.root, project.parameters)
        self.assertEqual(item["draft"], loaded["atoms"][0]["draft"])
        prepared = prepare_subject_intent(
            project.root, item["target"], item["subject_patches"], subject_profile="approved"
        )
        candidate = materialize_subject_intent(project.root, prepared, EFFECT_TIME)
        require_reviewed_draft_candidate(project.root, item, candidate["carrier_bytes"])
        path, archive = project.paths[0], project.archives()[0]
        before = operations.parse_carrier(project.before[path], path)
        runner, frozen = project.execution("id-free-subject-edit")
        with patch.object(native, "current_timestamp", return_value=EFFECT_TIME):
            result = runner.dispatch(frozen)
        self.assertEqual("terminal", result["disposition"])
        after = operations.parse_carrier(path.read_bytes(), path)
        expected = copy.deepcopy(before.metadata)
        expected["subjects"]["governs"] = "Atom.State"
        expected.update(version=before.metadata["version"] + 1, updated_at=EFFECT_TIME)
        self.assertEqual(expected, after.metadata)
        self.assertEqual(before.body, after.body)
        self.assertEqual(project.before[path], archive.read_bytes())
        self.assertFalse(draft_path.exists())

    def test_id_free_reviewed_draft_rejects_wrong_filename_and_tampering(self):
        for case in ("wrong-filename", "tampered"):
            with self.subTest(case=case):
                project = SubjectBatchProject(self, count=1)
                staged = stage_subject_batch(project.root, project.parameters, limit=1)
                project.use_reviewed_packet(staged["reviewed_packet"])
                item = project.packet["atoms"][0]
                if case == "wrong-filename":
                    valid = _id_free_draft_path(project, item)
                    _rewrite_as_id_free(project, item, filename=f"{valid.stem}-wrong.md")
                    with self.assertRaises(ValueError):
                        load_subject_batch(project.root, project.parameters)
                else:
                    _rewrite_as_id_free(project, item, suffix=b"\nunreviewed body edit\n")
                    prepared = prepare_subject_intent(
                        project.root, item["target"], item["subject_patches"], subject_profile="approved"
                    )
                    candidate = materialize_subject_intent(project.root, prepared, EFFECT_TIME)
                    with self.assertRaises(ValueError):
                        require_reviewed_draft_candidate(project.root, item, candidate["carrier_bytes"])
                self.assertEqual(project.before[project.paths[0]], project.paths[0].read_bytes())

    def test_id_free_draft_version_must_match_materialized_candidate(self):
        project = SubjectBatchProject(self, count=1)
        staged = stage_subject_batch(project.root, project.parameters, limit=1)
        project.use_reviewed_packet(staged["reviewed_packet"])
        item = project.packet["atoms"][0]
        draft = _rewrite_as_id_free(project, item)
        metadata = operations.parse_carrier(draft.read_bytes(), draft).metadata
        wrong_version = metadata["version"] + 1
        raw = draft.read_bytes().replace(
            f"version: {metadata['version']}".encode(), f"version: {wrong_version}".encode(), 1
        )
        draft.write_bytes(raw)
        item["draft"]["digest"] = hashlib.sha256(raw).hexdigest()
        project.save_packet()
        prepared = prepare_subject_intent(
            project.root, item["target"], item["subject_patches"], subject_profile="approved"
        )
        candidate = materialize_subject_intent(project.root, prepared, EFFECT_TIME)
        with self.assertRaises(ValueError):
            require_reviewed_draft_candidate(project.root, item, candidate["carrier_bytes"])
        self.assertEqual(project.before[project.paths[0]], project.paths[0].read_bytes())

    def test_versioned_draft_marker_must_match_candidate_version(self):
        project = SubjectBatchProject(self, count=1)
        staged = stage_subject_batch(project.root, project.parameters, limit=1)
        project.use_reviewed_packet(staged["reviewed_packet"])
        item = project.packet["atoms"][0]
        preferred = project.root / item["draft"]["path"]
        metadata = operations.parse_carrier(preferred.read_bytes(), preferred).metadata
        wrong_version = metadata["version"] + 1
        wrong_path = subject_batch_draft_path(project.root, item["target"], wrong_version)
        raw = preferred.read_bytes().replace(
            f'{item["target"]["atom_id"]}@{metadata["version"]}-draft'.encode(),
            f'{item["target"]["atom_id"]}@{wrong_version}-draft'.encode(),
        )
        preferred.rename(wrong_path)
        wrong_path.write_bytes(raw)
        item["draft"] = {
            "path": wrong_path.relative_to(project.root).as_posix(),
            "digest": hashlib.sha256(raw).hexdigest(),
        }
        project.save_packet()
        prepared = prepare_subject_intent(
            project.root, item["target"], item["subject_patches"], subject_profile="approved"
        )
        candidate = materialize_subject_intent(project.root, prepared, EFFECT_TIME)
        with self.assertRaises(ValueError):
            require_reviewed_draft_candidate(project.root, item, candidate["carrier_bytes"])
        self.assertEqual(project.before[project.paths[0]], project.paths[0].read_bytes())

    def test_versioned_draft_marker_must_match_carried_yaml_version(self):
        project = SubjectBatchProject(self, count=1)
        staged = stage_subject_batch(project.root, project.parameters, limit=1)
        project.use_reviewed_packet(staged["reviewed_packet"])
        item = project.packet["atoms"][0]
        draft = project.root / item["draft"]["path"]
        metadata = operations.parse_carrier(draft.read_bytes(), draft).metadata
        wrong_version = metadata["version"] + 1
        raw = draft.read_bytes().replace(
            f"version: {metadata['version']}".encode(),
            f"version: {wrong_version}".encode(),
            1,
        )
        draft.write_bytes(raw)
        item["draft"]["digest"] = hashlib.sha256(raw).hexdigest()
        project.save_packet()
        with self.assertRaises(ValueError):
            load_subject_batch(project.root, project.parameters)
        self.assertEqual(project.before[project.paths[0]], project.paths[0].read_bytes())

    def test_changed_edit_draft_is_rejected_before_any_publication(self):
        project = SubjectBatchProject(self)
        completed = stage_subject_batch(project.root, project.parameters, limit=2)
        project.use_reviewed_packet(completed["reviewed_packet"])
        runner, frozen = project.execution("tampered-subject-edit-draft")
        draft = project.root / project.packet["atoms"][0]["draft"]["path"]
        draft.write_bytes(draft.read_bytes() + b"\nunreviewed body edit\n")
        with self.assertRaises(ValueError):
            load_subject_batch(project.root, project.parameters)
        with patch("subject_batch_execution.subject_update_action") as native_publisher:
            result = runner.dispatch(frozen)
        self.assertEqual("terminal", result["disposition"])
        self.assertNotEqual("completed", result.get("outcome"))
        native_publisher.assert_not_called()
        for path in project.paths:
            self.assertEqual(project.before[path], path.read_bytes())

    def test_promotion_restores_canonical_identity_and_done_status_with_exact_history(self):
        project = SubjectBatchProject(self, count=1, role="Plan", status="Done")
        path, archive = project.paths[0], project.archives()[0]
        self.assertEqual("archived", archive.parent.name)
        self.assertEqual("03_plan", archive.parent.parent.name)
        self.assertEqual(f"{path.stem}@{project.targets[0]['version']}.md", archive.name)
        with patch.object(
            operations,
            "_validate_complete_carrier",
            side_effect=AssertionError("full-carrier validation"),
        ) as complete_validation:
            completed = stage_subject_batch(project.root, project.parameters, limit=1)
            project.use_reviewed_packet(completed["reviewed_packet"])
            draft_path = project.root / project.packet["atoms"][0]["draft"]["path"]
            self.assertTrue(draft_path.exists())
            runner, frozen = project.execution("promote-subject-edit-draft")
            with patch.object(native, "current_timestamp", return_value=EFFECT_TIME):
                result = runner.dispatch(frozen)
        complete_validation.assert_not_called()
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
        self.assertFalse(draft_path.exists())
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
