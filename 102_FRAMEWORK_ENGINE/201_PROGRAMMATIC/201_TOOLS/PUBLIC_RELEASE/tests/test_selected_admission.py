"""Current D613 admission and stale-source refusal, without release effects."""
from __future__ import annotations

import copy
from contextlib import contextmanager
import hashlib
from pathlib import Path
import shutil
import sys
import tempfile
from types import SimpleNamespace
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
        temporary = tempfile.TemporaryDirectory(prefix="public-release-admission-")
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name).resolve()
        self.authority = self.root / AUTHORITY_REF
        self.authority_text = (REPOSITORY / AUTHORITY_REF).read_text(encoding="utf-8")
        control = Path(".caprmedio_caprmedio")
        for name in ("caprmedio_project_settings.toml", "project_structure.toml"):
            self.copy(control / name)
        project_tools = Path(AUTHORITY_REF).parents[1]
        for source_root in (REPOSITORY / project_tools, REPOSITORY / control / "09_operations"):
            for source in source_root.rglob("*.md"):
                if not {"archive", "archived", "draft", "drafts", "done", "canceled"}.intersection(source.relative_to(source_root).parts):
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
        self.assertEqual(["CA-O-189", "CA-O-191", "CA-O-195", "CA-O-197"],
                         [pin["atom_id"] for pin in record["ordered_steps"]])
        self.assertEqual(["CA-O-190", "CA-O-192", "CA-O-196", "CA-O-198"],
                         [pin["atom_id"] for pin in record["ordered_actions"]])
        self.assertEqual({"requirements": 7, "methods": 3, "evaluations": 8, "deliveries": 6},
                         {key: len(pins) for key, pins in record["rmed_frontier"].items()})
        self.assertEqual(24, sum(map(len, record["rmed_frontier"].values())))
        expected_members = {
            "requirements": ["CA-R-1920", "CA-R-1921", "CA-R-1923", "CA-R-1925", "CA-R-1926", "CA-R-1927", "CA-R-1928"],
            "methods": ["CA-M-365", "CA-M-366", "CA-M-368"],
            "evaluations": ["CA-E-610", "CA-E-611", "CA-E-612", "CA-E-613", "CA-E-615", "CA-E-616", "CA-E-617", "CA-E-618"],
            "deliveries": ["CA-D-610", "CA-D-611", "CA-D-612", "CA-D-616", "CA-D-617", "CA-D-618"],
        }
        self.assertEqual(expected_members,
                         {key: [pin["atom_id"] for pin in pins] for key, pins in record["rmed_frontier"].items()})
        self.assertNotIn("CA-D-613", [pin["atom_id"] for pins in record["rmed_frontier"].values() for pin in pins])
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
            self.authority_text.replace(first, "| 1 | CA-O-191 | CA-O-192 |", 1).replace(second, "| 2 | CA-O-189 | CA-O-190 |", 1),
            self.authority_text.replace("| 4 | CA-O-197 | CA-O-198 |\n", "", 1),
            self.authority_text.replace("| deliveries | 6 | CA-D-618 |\n", "", 1),
            self.authority_text.replace("| requirements | 1 | CA-R-1920 |", "| requirements | 1 | CA-R-1920 |\n| requirements | 1 | CA-R-1920 |", 1),
            self.authority_text.replace("| requirements | 2 | CA-R-1921 |", "| requirements | 2 | CA-R-1920 |", 1),
            self.authority_text.replace("| requirements | 2 | CA-R-1921 |", "| requirements | 2 | CA-R-999999 |", 1),
            self.authority_text.replace("| requirements | 2 | CA-R-1921 |", "| requirements | 2 | CA-M-365 |", 1),
            self.authority_text.replace("| deliveries | 6 | CA-D-618 |", "| deliveries | 6 | CA-D-613 |", 1),
        )
        for text in mutations:
            self.assertNotEqual(self.authority_text, text, "mutation must actually alter the current fixture")
            with self.subTest(text=text[-100:]):
                self.authority.write_text(text, encoding="utf-8")
                with self.trusted_fixture_authority(), self.assertRaises(PublicReleaseSourceAdmissionError):
                    derive_public_release_source_admission(self.root)
        self.authority.write_text(self.authority_text, encoding="utf-8")

    def test_authority_drift_and_reordered_record_refuse_without_writes(self):
        record = derive_public_release_source_admission(self.root)
        reordered = copy.deepcopy(record)
        reordered["rmed_frontier"]["requirements"].reverse()
        with self.assertRaises(PublicReleaseSourceAdmissionError):
            validate_public_release_source_admission(self.root, reordered)
        self.authority.write_bytes(self.authority.read_bytes() + b"\nchanged authority\n")
        before = self.snapshot()
        with self.assertRaisesRegex(PublicReleaseSourceAdmissionError, "source pin is stale"):
            derive_public_release_source_admission(self.root)
        self.assertEqual(before, self.snapshot())

    def test_obsolete_acceptance_caller_pass_or_shadow_field_refuses(self):
        record = derive_public_release_source_admission(self.root)
        for field, value in (("acceptance_frontier", record["workflow"]), ("caller_pass", True),
                             ("authority_pin", copy.deepcopy(AUTHORITY_PIN)), ("canonical_manifest_sha256", "f" * 64)):
            with self.subTest(field=field):
                forged = copy.deepcopy(record)
                forged[field] = value
                with self.assertRaises(PublicReleaseSourceAdmissionError):
                    validate_public_release_source_admission(self.root, forged)


class CurrentPublicReleaseSourceHistoryTests(unittest.TestCase):
    """Exercise current discovery without obsolete live D613 graph fixtures."""

    def setUp(self):
        temporary = tempfile.TemporaryDirectory(prefix="public-release-source-history-")
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name).resolve()
        control = self.root / ".caprmedio_caprmedio"
        self.authority = control / "project_tools"
        self.source = self.authority / "07_delivery/CA-D-999--source.md"
        self.source.parent.mkdir(parents=True)
        (control / "09_operations").mkdir()
        self.original = (b"---\natom_id: CA-D-999\nversion: 2\ncontent_role: Delivery\n"
                         b"current_scope_unit: PROJECT_TOOLS\nstatus: Active\n---\n"
                         b"# Summary\n\nCurrent source fixture\n")
        self.source.write_bytes(self.original)
        selection = SimpleNamespace(
            control_root=control,
            structure={"scope_units": [{"scope_unit_name": "PROJECT_TOOLS",
                                        "authority_path": ".caprmedio_caprmedio/project_tools"}]},
            settings={"project": {"name": "fixture"}},
        )
        selector = patch("project_selection.resolve_project", return_value=selection)
        selector.start()
        self.addCleanup(selector.stop)

    def resolve(self):
        return selected_admission._current_source_resolver(self.root)("CA-D-999", "Delivery", None)

    def test_exact_active_history_never_becomes_current(self):
        current_bytes = self.original.replace(b"version: 2", b"version: 3", 1)
        self.source.write_bytes(current_bytes)
        expected = self.resolve()
        for relative in ("archive/prior@2.md", "archived/prior@2.md", "prior@2.md", "archived/prior.md"):
            with self.subTest(relative=relative):
                historical = self.source.parent / relative
                historical.parent.mkdir(exist_ok=True)
                historical.write_bytes(self.original)
                self.assertEqual(expected, self.resolve())
                self.assertEqual(self.original, historical.read_bytes())
                self.source.unlink()
                with self.assertRaisesRegex(PublicReleaseSourceAdmissionError, "resolve exactly once"):
                    self.resolve()
                self.source.write_bytes(current_bytes)
                historical.unlink()

    def test_history_does_not_hide_actual_current_duplicates(self):
        self.source.with_name("prior@2.md").write_bytes(self.original)
        for name in ("duplicate.md", "duplicate@preview.md", "duplicate@0.md", "duplicate@01.md"):
            with self.subTest(name=name):
                duplicate = self.source.with_name(name)
                duplicate.write_bytes(self.original)
                with self.assertRaisesRegex(PublicReleaseSourceAdmissionError, "resolve exactly once"):
                    self.resolve()
                duplicate.unlink()


if __name__ == "__main__":
    unittest.main()
