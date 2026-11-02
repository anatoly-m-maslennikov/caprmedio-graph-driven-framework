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
from scope_declaration_render import render_scope_declaration


class DirectSubjectReaderTests(unittest.TestCase):
    def setUp(self):
        self.fixture = fixtures.SubjectLookupTest(methodName="runTest")
        self.fixture.setUp()
        self.addCleanup(self.fixture.tearDown)
        self.root = self.fixture.root
        self.source = self.fixture.role / "CA-R-1-CORE-REQUIREMENT--fixture.md"
        self.declaration = next(self.root.glob(
            ".caprmedio_caprmedio/04_requirement/CA-R-*-SCOPE_UNIT_DECLARATION--declare-core.md"
        ))
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
        path = self.fixture.role.parent / "02_analysis/CA-A-9--excluded.md"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("---\n" + header + "\n---\nUnrelated legacy body\n")
        return path

    def foreign_owner(self):
        declaration = self.declaration.with_name(
            "CA-R-990002-foreign-scope-unit-declaration--declare-foreign.md"
        )
        declaration.write_text(render_scope_declaration(
            name="FOREIGN", project_name="fixture", atom_id="CA-R-990002",
            updated_at="2026-11-02 00:00:00 +0000", scope_id="TEST-SU-2",
            parent="PROJECT",
        ), encoding="utf-8")
        return self.root / ".caprmedio_caprmedio/TEST-SU-2_FOREIGN/04_requirement"

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
        foreign_owner = self.foreign_owner()
        foreign = foreign_owner / "CA-R-1--competing.md"
        foreign.parent.mkdir(parents=True, exist_ok=True)
        foreign.write_bytes(self.source.read_bytes().replace(b"current_scope_unit: CORE", b"current_scope_unit: FOREIGN"))
        with self.assertRaises(ToolError) as caught:
            self.search()
        self.assertEqual("subject-identity-duplicate", caught.exception.code)

    def test_unrelated_malformed_selected_role_in_other_owner_is_not_selected_content(self):
        foreign = self.foreign_owner().parent / "02_analysis/CA-R-71--unrelated.md"
        foreign.parent.mkdir(parents=True, exist_ok=True)
        foreign.write_text("---\natom_id: CA-R-71\nbroken: [\n---\n")
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
        analysis = self.fixture.role.parent / "02_analysis"
        analysis.symlink_to(hidden, target_is_directory=True)
        self.assertEqual("full", self.search()["coverage"])
        hidden.rmdir()
        self.assertEqual("full", self.search()["coverage"])

    def test_source_structure_and_frontier_drift_follow_current_contract(self):
        original = lookup.ReadContext.currentness
        settings = self.root / ".caprmedio_caprmedio/caprmedio_project_settings.toml"
        for target in (self.source, self.declaration, settings, self.fixture.role / "CA-R-19--added.md"):
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
                    with patch.object(lookup.ReadContext, "currentness", drift):
                        try:
                            result = self.search()
                        except ToolError as caught:
                            self.assertIn(target, (self.declaration, settings))
                            self.assertEqual("scope-unit-declarations-unavailable", caught.code)
                        else:
                            # A source/frontier mutation made before that input is
                            # observed is accepted by the current reader contract;
                            # declarations and Settings fail closed during discovery.
                            self.assertNotIn(target, (self.declaration, settings))
                            self.assertTrue(mutated)
                            self.assertEqual(1, result["count"])
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
