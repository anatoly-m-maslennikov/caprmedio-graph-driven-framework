"""The direct lookup reader verifies sources without Runs or source repairs."""
from __future__ import annotations

from pathlib import Path
import shutil
import unittest
from unittest.mock import patch

import test_subject_lookup as fixtures
import atom_subject_lookup as lookup
from atom_operations import ToolError
from subject_notation import get_profile


class DirectSubjectReaderTests(unittest.TestCase):
    def setUp(self):
        self.fixture = fixtures.SubjectLookupTest(methodName="runTest")
        self.fixture.setUp()
        self.addCleanup(self.fixture.tearDown)
        self.root = self.fixture.root
        self.source = self.fixture.role / "CA-R-1-CORE-REQUIREMENT--fixture.md"
        repository = Path(__file__).resolve().parents[5]
        for profile in ("legacy", "approved"):
            for pin in get_profile(profile).grammar_pins:
                target = self.root / pin.path
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(repository / pin.path, target)

    def search(self, **kwargs):
        args = self.fixture._args(content_role=["Requirement"], scope_unit="CORE", **kwargs)
        return lookup.run_subject_search(self.root, args, direct_subject_only=True)

    def snapshot(self):
        return {p.relative_to(self.root).as_posix(): p.read_bytes()
                for p in self.root.rglob("*") if p.is_file()}

    def excluded(self, header):
        path = self.root / ".caprmedio_caprmedio/core/02_analysis/CA-A-9--excluded.md"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("---\n" + header + "\n---\nUnrelated legacy body\n")
        return path

    def test_absent_type_and_unrelated_malformed_headers_remain_readonly(self):
        for header in ("atom_id: [invalid", '"atom_id" : [invalid', "atom_id: CA-A-9\nbroken: ["):
            with self.subTest(header=header):
                self.excluded(header)
                before = self.snapshot()
                result = self.search()
                self.assertEqual("full", result["coverage"])
                self.assertEqual(1, result["count"])
                self.assertEqual(before, self.snapshot())

    def test_malformed_excluded_selected_id_claim_is_not_hidden(self):
        self.excluded("atom_id: CA-R-1\nbroken: [")
        with self.assertRaises(ToolError) as caught:
            self.search()
        self.assertEqual("subject-identity-inventory-unavailable", caught.exception.code)

    def test_decoded_excluded_selected_identity_claim_is_not_hidden(self):
        self.excluded('atom_id: "CA-R-\\x31"\nstatus: Active\nbroken: [')
        with self.assertRaises(ToolError) as caught:
            self.search()
        self.assertEqual("subject-identity-inventory-unavailable", caught.exception.code)

    def test_competing_current_identity_outside_selected_owner_refuses(self):
        foreign = self.root / ".caprmedio_caprmedio/foreign/04_requirement/CA-R-1--competing.md"
        foreign.parent.mkdir(parents=True)
        foreign.write_bytes(self.source.read_bytes().replace(b"current_scope_unit: CORE", b"current_scope_unit: FOREIGN"))
        structure = self.root / ".caprmedio_caprmedio/project_structure.toml"
        structure.write_text(structure.read_text() + '\n[[scope_units]]\nscope_unit_name = "FOREIGN"\nauthority_path = ".caprmedio_caprmedio/foreign"\n')
        with self.assertRaises(ToolError) as caught:
            self.search()
        self.assertEqual("subject-identity-duplicate", caught.exception.code)

    def test_unrelated_malformed_selected_role_in_other_owner_is_not_selected_content(self):
        foreign = self.root / ".caprmedio_caprmedio/foreign/04_requirement/CA-R-71--unrelated.md"
        foreign.parent.mkdir(parents=True)
        foreign.write_text("---\natom_id: CA-R-71\nbroken: [\n---\n")
        structure = self.root / ".caprmedio_caprmedio/project_structure.toml"
        structure.write_text(structure.read_text() + '\n[[scope_units]]\nscope_unit_name = "FOREIGN"\nauthority_path = ".caprmedio_caprmedio/foreign"\n')
        self.assertEqual("full", self.search()["coverage"])

    def test_literal_suffix_contains_reuse_complete_source_validation(self):
        self.fixture._write("CA-R-3", "Core/Atom.Status", [])
        suffix = self.search(subject=".Status", subject_match="suffix")
        contains = self.search(subject="/Atom", subject_match="contains")
        self.assertEqual(["Core/Atom.Status"], [row["value"] for row in suffix["occurrences"]])
        # Literal contains intentionally includes the Atomology lexical near-miss.
        self.assertEqual(4, contains["count"])
        self.assertEqual(0, self.search(subject=".status", subject_match="suffix")["count"])

    def test_grammar_pin_changed_before_observation_refuses(self):
        pin = get_profile("legacy").grammar_pins[0]
        path = self.root / pin.path
        path.write_bytes(path.read_bytes() + b"changed\n")
        with self.assertRaises(ToolError) as caught:
            self.search()
        self.assertEqual("subject-grammar-pin-stale", caught.exception.code)

    def test_selected_role_directory_symlink_cannot_be_complete_empty(self):
        hidden = self.root / "hidden_sources"
        self.fixture.role.rename(hidden)
        self.fixture.role.symlink_to(hidden, target_is_directory=True)
        for target_exists in (True, False):
            with self.subTest(target_exists=target_exists):
                if not target_exists:
                    hidden.rename(self.root / "removed_source_target")
                with self.assertRaises(ToolError) as caught:
                    self.search()
                self.assertEqual("subject-source-verification-unavailable", caught.exception.code)

    def test_excluded_role_directory_symlink_is_not_a_selected_frontier_gate(self):
        hidden = self.root / "unrelated_analysis"
        hidden.mkdir()
        analysis = self.root / ".caprmedio_caprmedio/core/02_analysis"
        analysis.symlink_to(hidden, target_is_directory=True)
        self.assertEqual("full", self.search()["coverage"])
        hidden.rmdir()
        self.assertEqual("full", self.search()["coverage"])

    def test_source_structure_and_frontier_drift_refuse(self):
        original = lookup.ReadContext.currentness
        structure = self.root / ".caprmedio_caprmedio/project_structure.toml"
        settings = self.root / ".caprmedio_caprmedio/caprmedio_project_settings.toml"
        for target in (self.source, structure, settings, self.fixture.role / "CA-R-19--added.md"):
            with self.subTest(target=target):
                before = target.read_bytes() if target.exists() else None
                mutated = False

                def drift(reader):
                    nonlocal mutated
                    if not mutated:
                        mutated = True
                        target.write_bytes((before or b"") + b"# external drift\n")
                    return original(reader)

                try:
                    with patch.object(lookup.ReadContext, "currentness", drift), self.assertRaises(ToolError) as caught:
                        self.search()
                    self.assertEqual("subject-source-changed", caught.exception.code)
                finally:
                    if before is None:
                        target.unlink(missing_ok=True)
                    else:
                        target.write_bytes(before)

    def test_archived_only_result_does_not_require_a_current_original(self):
        self.fixture._write("CA-R-19", "Core/Atom", [], directory=self.fixture.role / "archive", status="Archived")
        result = self.search(lifecycle="archived")
        self.assertEqual(1, result["count"])
        self.assertEqual("CA-R-19", result["occurrences"][0]["atom_id"])

    def test_exhausted_read_budget_is_not_successful_empty_coverage(self):
        with patch.object(lookup, "CEILINGS", {**lookup.CEILINGS, "max_total_read_bytes": 1}):
            with self.assertRaises(ToolError) as caught:
                self.search()
        self.assertEqual("subject-source-verification-unavailable", caught.exception.code)


if __name__ == "__main__":
    unittest.main()
