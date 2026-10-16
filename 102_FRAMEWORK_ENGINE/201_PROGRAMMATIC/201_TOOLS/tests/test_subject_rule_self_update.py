"""Real selected publication must keep its approved edit to an updater rule."""

import copy
import hashlib
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

TOOLS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOLS))
sys.path.insert(0, str(TOOLS / "ATOM_UPDATE/tests"))

import atom_operations as operations  # noqa: E402
import atom_subject_apply as native  # noqa: E402
import atom_subject_patch as subjects  # noqa: E402
from lifecycle_intents import carrier_descriptor  # noqa: E402
from test_subject_apply_portfolio import SubjectApplyProject  # noqa: E402
from VALIDATE_ATOMS.validate_atoms_workers import proposed_carrier as admission  # noqa: E402


class SubjectRuleSelfUpdateTests(unittest.TestCase):
    def setUp(self):
        scratch = Path.cwd() / ".caprmedio_tmp/tests/subject-rule-self-update"
        scratch.mkdir(parents=True, exist_ok=True)
        directory = tempfile.TemporaryDirectory(dir=scratch)
        self.addCleanup(directory.cleanup)
        self.fixture = SubjectApplyProject(Path(directory.name).resolve())
        self.root = self.fixture.root
        self.next_path = self.fixture.path
        operators = self.root / ".caprmedio_caprmedio/operators_registry.toml"
        operators.write_text(
            operators.read_text()
            + '\n[[operators]]\nname = "Anatoly Maslennikov"\nrole = "project owner"\n'
        )
        structure = self.root / ".caprmedio_caprmedio/project_structure.toml"
        structure.write_text(
            structure.read_text()
            + (
                '\n[[scope_units]]\nscope_unit_name = "CORE_META_MODEL"\nparent = "PROJECT"\n'
                'scope_unit_type = "Unordered"\nscope_unit_label = "FEATURE"\nstructural_level = 1\n'
                "navigational_order_number = 2\n"
                'authority_path = ".caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL"\n'
                'delivery_path = "delivery/CORE_META_MODEL"\n'
            )
        )
        context = admission.source_context_from_project(self.root)
        row = next(
            row for row in context.inputs["sources"] if row["binding"]["atom_id"] == "CA-D-276"
        )
        self.rule = Path(row["binding"]["path"])
        self.report_number = 400

    def select_target(self, path, new_subject):
        fixture = self.fixture
        fixture.path, fixture.before = path, path.read_bytes()
        fixture.before_mode = path.stat().st_mode & 0o777
        fixture.target = carrier_descriptor(self.root, path.relative_to(self.root).as_posix())
        metadata = operations.parse_carrier(fixture.before, path).metadata
        self.assertNotEqual(metadata["subjects"]["governs"], new_subject)
        fixture.patches = [
            {"field": "governs", "old": metadata["subjects"]["governs"], "new": new_subject}
        ]
        fixture.prepared = subjects.prepare_subject_intent(
            self.root, fixture.target, fixture.patches, subject_profile="approved"
        )
        fixture.parameters = {
            "target": fixture.target,
            "subject_patches": fixture.patches,
            "subject_profile": "approved",
            "subject_intent_sha256": fixture.prepared["subject_intent_sha256"],
        }
        fixture.parameters["semantic_assessment_report"] = self.assessment()
        fixture.golden._semantic_update_parameters = fixture.parameters
        archive = fixture.prepared["subject_intent"]["predecessorArchive"]
        self.assertIsNotNone(archive)
        fixture.archive = self.root / archive["path"]

    def assessment(self):
        fixture = self.fixture
        original = (
            self.root
            / ".caprmedio_caprmedio/fixture/02_analysis/done/CA-A-400--update-assessment.md"
        )
        before = original.read_bytes()
        pin = fixture.golden._semantic_assessment_report(
            fixture.target, fixture.prepared["proposed"]
        )
        self.report_number += 1
        report = original.with_name(f"CA-A-{self.report_number}--update-assessment.md")
        raw = (
            (self.root / pin["path"])
            .read_bytes()
            .replace(b"atom_id: CA-A-400", f"atom_id: CA-A-{self.report_number}".encode())
        )
        report.write_bytes(raw)
        original.write_bytes(before)
        return {
            "path": report.relative_to(self.root).as_posix(),
            "digest": hashlib.sha256(raw).hexdigest(),
        }

    def publish(self, run_id):
        fixture = self.fixture
        runner, frozen = fixture.execution(run_id)
        confirmation = fixture.confirmation(frozen)
        actual_at = native.current_timestamp(self.root)
        expected_raw = subjects.materialize_subject_intent(self.root, fixture.prepared, actual_at)[
            "carrier_bytes"
        ]
        with patch.object(native, "current_timestamp", return_value=actual_at):
            result = runner._dispatch_confirmed_subject(frozen, confirmation)
        self.assertEqual(expected_raw, fixture.path.read_bytes())
        after = operations.parse_carrier(fixture.path.read_bytes(), fixture.path)
        before = operations.parse_carrier(fixture.before, fixture.path)
        expected = copy.deepcopy(before.metadata)
        expected["subjects"]["governs"] = fixture.patches[0]["new"]
        expected.update(
            version=fixture.target["version"] + 1, updated_at=after.metadata["updated_at"]
        )
        self.assertEqual(expected, after.metadata)
        self.assertEqual(before.body, after.body)
        self.assertEqual(fixture.before, fixture.archive.read_bytes())
        self.assertEqual(fixture.before_mode, fixture.path.stat().st_mode & 0o777)
        effects = sorted(
            [fixture.target["path"], fixture.archive.relative_to(self.root).as_posix()]
        )
        self.assertTrue(
            any(
                row["outcome"] == "completed" and row["effect_refs"] == effects
                for row in result["terminal_runs"]
            )
        )
        return after

    def test_approved_rule_change_persists_and_next_publication_uses_current_rule(self):
        self.select_target(self.rule, "Atom.State")
        after = self.publish("updater-rule-subject-change")
        rule_bytes = self.rule.read_bytes()
        rule_archive = self.fixture.archive
        archived_bytes = rule_archive.read_bytes()
        captures = []
        real_context = admission.source_context_from_project

        def observe(root):
            context = real_context(root)
            captures.append(
                next(
                    row["binding"]
                    for row in context.inputs["sources"]
                    if row["binding"]["atom_id"] == "CA-D-276"
                )
            )
            return context

        with patch.object(admission, "source_context_from_project", side_effect=observe):
            self.select_target(self.next_path, "Atom.State")
            self.publish("next-subject-change-after-rule-update")
        self.assertEqual(rule_bytes, self.rule.read_bytes())
        self.assertEqual(archived_bytes, rule_archive.read_bytes())
        self.assertTrue(captures)
        self.assertTrue(
            all(
                row["version"] == after.metadata["version"]
                and row["sha256"] == hashlib.sha256(rule_bytes).hexdigest()
                for row in captures
            )
        )


if __name__ == "__main__":
    unittest.main()
