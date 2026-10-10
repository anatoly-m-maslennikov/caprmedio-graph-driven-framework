"""Current D613 admission and stale-source refusal, without release effects."""
from __future__ import annotations

import copy
from contextlib import contextmanager
import hashlib
from pathlib import Path
import shutil
import sys
import tempfile
import unittest
from unittest.mock import patch

TOOLS = Path(__file__).resolve().parents[2]
PUBLIC_RELEASE = TOOLS / "PUBLIC_RELEASE"
REPOSITORY = TOOLS.parents[2]
for item in (str(TOOLS), str(PUBLIC_RELEASE)):
    if item not in sys.path:
        sys.path.insert(0, item)

import selected_admission
from selected_admission import (AUTHORITY_PIN, AUTHORITY_REF, PublicReleaseSourceAdmissionError,
                                derive_public_release_source_admission, validate_public_release_source_admission)


class SelectedPublicReleaseAdmissionTests(unittest.TestCase):
    def setUp(self):
        self.root = Path(tempfile.mkdtemp(prefix="public-release-admission-", dir="/private/tmp"))
        self.authority = self.root / AUTHORITY_REF
        self.authority_text = (REPOSITORY / AUTHORITY_REF).read_text(encoding="utf-8")
        control = Path(".caprmedio_caprmedio")
        for name in ("caprmedio_project_settings.toml", "project_structure.toml"):
            self.copy(control / name)
        project_tools = Path(AUTHORITY_REF).parents[1]
        for source_root in (REPOSITORY / project_tools, REPOSITORY / control / "09_operations"):
            for source in source_root.rglob("*.md"):
                if not {"archive", "draft", "drafts", "done", "canceled"}.intersection(source.relative_to(source_root).parts):
                    self.copy(source.relative_to(REPOSITORY))
        self.projection = REPOSITORY / control / "_projection/selected_workflow_bindings.json"
        self.projection_before = self.projection.read_bytes()

    def copy(self, relative):
        destination = self.root / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(REPOSITORY / relative, destination)

    def snapshot(self):
        return {path.relative_to(self.root).as_posix(): path.read_bytes()
                for path in self.root.rglob("*") if path.is_file()}

    @contextmanager
    def trusted_fixture_authority(self):
        pin = {**AUTHORITY_PIN, "digest": hashlib.sha256(self.authority.read_bytes()).hexdigest()}
        with patch.object(selected_admission, "AUTHORITY_PIN", pin):
            yield

    def test_current_project_source_derives_without_task_done_and_without_writes(self):
        before = self.snapshot()
        record = derive_public_release_source_admission(self.root)
        self.assertEqual(record, validate_public_release_source_admission(self.root, record))
        self.assertEqual({"route", "workflow", "ordered_steps", "ordered_actions", "rmed_frontier",
                          "mutation_capable", "native_action_calls"}, set(record))
        self.assertEqual("public.release", record["route"])
        self.assertTrue(record["workflow"]["source_path"].startswith(".caprmedio_caprmedio/09_operations/"))
        self.assertEqual(5, len(record["ordered_steps"]))
        self.assertEqual(5, len(record["ordered_actions"]))
        self.assertEqual(34, sum(map(len, record["rmed_frontier"].values())))
        self.assertEqual(before, self.snapshot())
        self.assertEqual(self.projection_before, self.projection.read_bytes())

    def test_actual_project_current_admission_has_no_task_or_acceptance_gate(self):
        record = derive_public_release_source_admission(REPOSITORY)
        self.assertNotIn("acceptance_frontier", record)
        self.assertEqual(self.projection_before, self.projection.read_bytes())

    def test_changed_source_derives_current_pin_but_refuses_old_record(self):
        original = derive_public_release_source_admission(self.root)
        workflow = self.root / original["workflow"]["source_path"]
        workflow.write_bytes(workflow.read_bytes() + b"\ncurrent source changed\n")
        current = derive_public_release_source_admission(self.root)
        self.assertNotEqual(original["workflow"]["digest"], current["workflow"]["digest"])
        with self.assertRaises(PublicReleaseSourceAdmissionError):
            validate_public_release_source_admission(self.root, original)

    def test_inactive_duplicate_wrong_role_or_unregistered_source_refuses(self):
        record = derive_public_release_source_admission(self.root)
        requirement = self.root / record["rmed_frontier"]["requirements"][0]["source_path"]
        original = requirement.read_bytes()
        for mutation in (b'status: "Inactive"', b'content_role: "Method"'):
            with self.subTest(mutation=mutation):
                old = b'status: "Active"' if mutation.startswith(b"status") else b'content_role: "Requirement"'
                self.assertIn(old, original)
                requirement.write_bytes(original.replace(old, mutation, 1))
                with self.assertRaises(PublicReleaseSourceAdmissionError):
                    derive_public_release_source_admission(self.root)
                requirement.write_bytes(original)
        duplicate = requirement.with_name("CA-R-1920-duplicate.md")
        duplicate.write_bytes(original)
        with self.assertRaises(PublicReleaseSourceAdmissionError):
            derive_public_release_source_admission(self.root)
        duplicate.unlink()
        structure = self.root / ".caprmedio_caprmedio/project_structure.toml"
        payload = structure.read_text(encoding="utf-8")
        structure.write_text(payload.replace('scope_unit_name = "PROJECT_TOOLS"', 'scope_unit_name = "UNREGISTERED"', 1), encoding="utf-8")
        with self.assertRaises(PublicReleaseSourceAdmissionError):
            derive_public_release_source_admission(self.root)

    def test_ambiguous_reordered_incomplete_or_extra_membership_refuses(self):
        first = "| 1 | CA-O-189 | CA-O-190 |"
        second = "| 2 | CA-O-191 | CA-O-192 |"
        mutations = (
            self.authority_text.replace(second, "| 2 | CA-O-189 | CA-O-190 |", 1),
            self.authority_text.replace(first, "TEMP_ROW", 1).replace(second, first, 1).replace("TEMP_ROW", second, 1),
            self.authority_text.replace("| 5 | CA-O-197 | CA-O-198 |\n", "", 1),
            self.authority_text.replace("| deliveries | 9 | CA-D-619 |\n", "", 1),
            self.authority_text.replace("| requirements | 1 | CA-R-1920 |", "| requirements | 1 | CA-R-1920 |\n| requirements | 1 | CA-R-1920 |", 1),
        )
        for text in mutations:
            with self.subTest(text=text[-100:]):
                self.authority.write_text(text, encoding="utf-8")
                with self.trusted_fixture_authority(), self.assertRaises(PublicReleaseSourceAdmissionError):
                    derive_public_release_source_admission(self.root)
        self.authority.write_text(self.authority_text, encoding="utf-8")

    def test_obsolete_acceptance_caller_pass_or_shadow_field_refuses(self):
        record = derive_public_release_source_admission(self.root)
        for field, value in (("acceptance_frontier", record["workflow"]), ("caller_pass", True),
                             ("authority_pin", copy.deepcopy(AUTHORITY_PIN)), ("canonical_manifest_sha256", "f" * 64)):
            with self.subTest(field=field):
                forged = copy.deepcopy(record)
                forged[field] = value
                with self.assertRaises(PublicReleaseSourceAdmissionError):
                    validate_public_release_source_admission(self.root, forged)


if __name__ == "__main__":
    unittest.main()
