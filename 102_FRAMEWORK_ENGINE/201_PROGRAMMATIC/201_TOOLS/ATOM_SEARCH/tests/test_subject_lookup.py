from __future__ import annotations

import argparse
import json
import sys
import tempfile
import unittest
from pathlib import Path


TOOLS = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(TOOLS))

from atom_operations import ToolError  # noqa: E402
from atom_subject_lookup import run_subject_search  # noqa: E402

TEST_TEMP_ROOT = Path.cwd() / ".caprmedio_tmp" / "tests" / Path(__file__).stem
TEST_TEMP_ROOT.mkdir(parents=True, exist_ok=True)

LEGACY_PROFILE_EVIDENCE = {
    "grammar_pins": [
        {"atom_id": "CA-R-1204", "version": 14,
         "path": ".caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/archive/CA-R-1204-CORE_META_MODEL--use-subject-path-slash-only-for-bearer-qualification@14.md",
         "sha256": "f57d56dab2cff12ea38a94900a1f146e40ead39f0af9e26e3130e9867f290dda"},
        {"atom_id": "CA-R-1321", "version": 12,
         "path": ".caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/archive/CA-R-1321-CORE_META_MODEL-CORE--define-subject-expression@12.md",
         "sha256": "6baf3f4179591dcc89c458dcb6503a55f24b70f9f1bd93203f4b748a9bcb1b8c"},
        {"atom_id": "CA-R-1324", "version": 10,
         "path": ".caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/archive/CA-R-1324-CORE_META_MODEL-REQUIREMENT--reserve-subject-expression-separators@10.md",
         "sha256": "f38d4cc446b04cde6958f1fe011679ff95048bdfe30f360d11a7366a572bc0b1"},
        {"atom_id": "CA-M-228", "version": 14,
         "path": ".caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/05_method/archive/CA-M-228-CORE_META_MODEL-METHOD--write-subject-expressions-with-bearer-and-value-qualification@14.md",
         "sha256": "f5a2152648b95c04af56c49118f43ac64ee46dd8183b23913cb64f335d6f26df"},
        {"atom_id": "CA-E-383", "version": 13,
         "path": ".caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/06_evaluation/archive/CA-E-383-CORE_META_MODEL-EVALUATION_APPROACH--reject-invalid-subject-expressions@13.md",
         "sha256": "00c3e901fbd18cdb584387386f6b04cd43905f651c4369e16a97d20b469b3274"},
    ],
    "native_admission": "not_performed",
}

APPROVED_PROFILE_EVIDENCE = {
    "grammar_pins": [
        {"atom_id": "CA-R-1931", "version": 1,
         "path": ".caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/CA-R-1931-CORE_META_MODEL--use-subject-path-separators-for-broader-to-narrower-and-bearer-to-dependent.md",
         "sha256": "f11bc913a0f7b31abc746a86599eaeaa76db8be412568ef4c34f68c7d01525c8"},
        {"atom_id": "CA-R-1321", "version": 14,
         "path": ".caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/CA-R-1321-CORE_META_MODEL-CORE--define-subject-expression.md",
         "sha256": "d883f1bd53ac3ea83aeff2d3d1fdfb5498641a0e5f2db5e8e79d8dfd5c5a84df"},
        {"atom_id": "CA-R-1324", "version": 12,
         "path": ".caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/CA-R-1324-CORE_META_MODEL-REQUIREMENT--reserve-subject-expression-separators.md",
         "sha256": "33cbfee9844ba4dd895ae6745121fd5db5793a20aab27eb8b8d7b4591e7fb9a3"},
        {"atom_id": "CA-M-228", "version": 16,
         "path": ".caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/05_method/CA-M-228-CORE_META_MODEL-METHOD--write-subject-expressions-with-bearer-and-value-qualification.md",
         "sha256": "0f398721d7d15aaf8e0b0f69a20b1b541e8d306839073c98eea4b80f9580b40d"},
        {"atom_id": "CA-E-383", "version": 15,
         "path": ".caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/06_evaluation/CA-E-383-CORE_META_MODEL-EVALUATION_APPROACH--reject-invalid-subject-expressions.md",
         "sha256": "6baca162365f248e08fc8d8a29b27e350149ff478290553b3cd6ee0441b4a6a6"},
    ],
    "native_admission": "not_performed",
}


class SubjectLookupTest(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory(dir=TEST_TEMP_ROOT, ignore_cleanup_errors=True)
        self.root = Path(self.temp.name)
        (self.root / ".git").mkdir()
        control = self.root / ".caprmedio_caprmedio"
        control.mkdir()
        (control / "caprmedio_project_settings.toml").write_text("[paths]\ncontrol_root = \".caprmedio_caprmedio\"\n")
        (control / "project_structure.toml").write_text(
            "schema_version = 1\n[[scope_units]]\nscope_unit_name = \"CORE\"\nauthority_path = \".caprmedio_caprmedio/core\"\n"
        )
        self.role = control / "core" / "04_requirement"
        self.role.mkdir(parents=True)
        self._write("CA-R-1", "Core/Atom", ["Core/Dependency", "Core/Atom/child"])
        self._write("CA-R-2", "Artifact/Atomology", [])

    def tearDown(self) -> None:
        self.temp.cleanup()

    def _write(self, atom_id: str, governs: str, depends: list[str], *, directory: Path | None = None,
               role: str = "Requirement", status: str = "Active") -> Path:
        path = (directory or self.role) / f"{atom_id}-CORE-REQUIREMENT--fixture.md"
        path.parent.mkdir(parents=True, exist_ok=True)
        dependencies = "\n".join(f"    - {json.dumps(value)}" for value in depends)
        path.write_text(
            f"---\natom_id: {atom_id}\nversion: 1\nstatus: {status}\ncontent_role: {role}\ncurrent_scope_unit: CORE\nupdated_at: now\nsubjects:\n  governs: {json.dumps(governs)}\n"
            + (f"  depends_on:\n{dependencies}\n" if dependencies else "") + "---\nCore/Atom in body only\n",
            encoding="utf-8",
        )
        return path

    def _args(self, **overrides: object) -> argparse.Namespace:
        values = dict(subject="Core/Atom", subject_field="both", subject_match="exact", content_role=None,
                      scope_unit=None, under=None, lifecycle="active", atom=None, query=None, limit=None)
        values.update(overrides)
        return argparse.Namespace(**values)

    def test_structured_exact_prefix_and_ordered_pins(self) -> None:
        exact = run_subject_search(self.root, self._args())
        self.assertEqual(exact["count"], 1)
        self.assertEqual(exact["occurrences"][0]["field"], "governs")
        self.assertIn("sha256", exact["occurrences"][0])
        self.assertEqual(exact["subject_profile"], "legacy")
        self.assertEqual(exact["subject_profile_evidence"], LEGACY_PROFILE_EVIDENCE)
        prefix = run_subject_search(self.root, self._args(subject_match="prefix"))
        self.assertEqual(prefix["count"], 2)
        self.assertEqual([item["index"] for item in prefix["occurrences"]], [None, 1])

    def test_profiles_select_lexical_boundaries_and_exact_evidence(self) -> None:
        self._write("CA-R-3", "Core.Atom.child", [])
        legacy = run_subject_search(self.root, self._args(subject="Core.Atom", subject_match="prefix"))
        self.assertEqual(legacy["count"], 0)
        self.assertEqual(legacy["subject_profile"], "legacy")
        self.assertEqual(legacy["subject_profile_evidence"], LEGACY_PROFILE_EVIDENCE)
        approved = run_subject_search(
            self.root, self._args(subject="Core.Atom", subject_match="prefix", subject_profile="approved")
        )
        self.assertEqual(approved["count"], 1)
        self.assertEqual(approved["occurrences"][0]["value"], "Core.Atom.child")
        self.assertEqual(approved["subject_profile"], "approved")
        self.assertEqual(approved["subject_profile_evidence"], APPROVED_PROFILE_EVIDENCE)

    def test_approved_selectors_are_case_sensitive_literal_subject_components(self) -> None:
        """Selectors qualify text syntax; they do not select fixture Atom rows."""

        named_status = 'atom(content_role="Plan").Status'
        quoted_status = 'atom(content_role="Plan/Type: Exact").Status'
        self._write("CA-R-3", f"{named_status}: Accepted", [])
        self._write("CA-R-4", f"{quoted_status}: Active", [])
        self._write("CA-R-5", 'atom(content_role="plan").Status: Rejected', [])
        self._write("CA-R-6", "Atom.Status", [])

        named = run_subject_search(
            self.root,
            self._args(subject=named_status, subject_match="prefix", subject_profile="approved"),
        )
        self.assertEqual(
            [("CA-R-3", "governs", None, f"{named_status}: Accepted")],
            [(row["atom_id"], row["field"], row["index"], row["value"])
             for row in named["occurrences"]],
        )
        # The slash and colon inside the quoted selector value are one literal
        # selector token, not prefix boundaries.
        quoted = run_subject_search(
            self.root,
            self._args(subject=quoted_status, subject_match="prefix", subject_profile="approved"),
        )
        self.assertEqual(
            [("CA-R-4", "governs", None, f"{quoted_status}: Active")],
            [(row["atom_id"], row["field"], row["index"], row["value"])
             for row in quoted["occurrences"]],
        )
        # ``Atom`` remains a literal ordinary component and is never the
        # lowercase selector keyword by case-folding or aliasing.
        ordinary = run_subject_search(
            self.root,
            self._args(subject="Atom.Status", subject_match="exact", subject_profile="approved"),
        )
        self.assertEqual(
            [("CA-R-6", "governs", None, "Atom.Status")],
            [(row["atom_id"], row["field"], row["index"], row["value"])
             for row in ordinary["occurrences"]],
        )

    def test_legacy_and_malformed_selector_queries_fail_before_source_search(self) -> None:
        with self.assertRaises(ToolError):
            run_subject_search(
                self.root,
                self._args(
                    subject='atom(content_role="Plan").Status',
                    subject_profile="legacy",
                ),
            )
        for subject in (
            'atom(type="Plan").Status',
            'atom(type="Plan",content_role="Plan").Status',
            'atom(content_role=Plan).Status',
            'atom(content_role="Plan",type="Plan",type="Plan").Status',
        ):
            with self.subTest(subject=subject), self.assertRaises(ToolError):
                run_subject_search(
                    self.root,
                    self._args(subject=subject, subject_profile="approved"),
                )

    def test_profile_and_subject_syntax_fail_before_search_and_sources_are_diagnostic(self) -> None:
        with self.assertRaises(ToolError) as context:
            run_subject_search(self.root, self._args(subject_profile="unknown"))
        self.assertEqual(context.exception.code, "profile-unknown")
        with self.assertRaises(ToolError) as context:
            run_subject_search(self.root, self._args(subject="Core@Atom"))
        self.assertEqual(context.exception.code, "subject-at-unsupported")
        source = self._write("CA-R-4", "Core@Atom", [])
        before = source.read_bytes()
        result = run_subject_search(self.root, self._args())
        self.assertEqual(source.read_bytes(), before)
        diagnostic = next(item for item in result["diagnostics"] if item["path"] == source.as_posix())
        self.assertEqual(diagnostic["code"], "subject-at-unsupported")

    def test_body_false_positive_is_not_subject_hit_and_limit_is_truthful(self) -> None:
        result = run_subject_search(self.root, self._args(subject="Core/Atom", subject_field="depends_on"))
        self.assertEqual(result["count"], 0)
        limited = run_subject_search(self.root, self._args(subject_match="prefix", limit=1))
        self.assertEqual(limited["coverage"], "limited")
        self.assertEqual(limited["count"], 1)

    def test_unknown_request_is_rejected_before_traversal(self) -> None:
        with self.assertRaises(ToolError) as context:
            run_subject_search(self.root, self._args(scope_unit="MISSING"))
        self.assertEqual(context.exception.code, "scope-unit-unknown")
        with self.assertRaises(ToolError) as context:
            run_subject_search(self.root, self._args(content_role=["Invented"]))
        self.assertEqual(context.exception.code, "content-role-unknown")

    def test_invalid_and_duplicate_sources_are_diagnostic(self) -> None:
        duplicate = self.role / "CA-R-1-CORE-REQUIREMENT--duplicate.md"
        duplicate.write_text((self.role / "CA-R-1-CORE-REQUIREMENT--fixture.md").read_text(encoding="utf-8"), encoding="utf-8")
        (self.role / "CA-R-3-CORE-REQUIREMENT--invalid.md").write_text("---\natom_id: CA-R-3\natom_id: CA-R-3\n---\n", encoding="utf-8")
        result = run_subject_search(self.root, self._args())
        self.assertEqual(result["count"], 0)
        self.assertEqual(result["coverage"], "limited")
        self.assertIn("duplicate-original-id", {item["code"] for item in result["diagnostics"]})
        self.assertIn("source-invalid", {item["code"] for item in result["diagnostics"]})

    def test_archived_history_is_not_an_original_duplicate_but_current_duplicate_is(self) -> None:
        self._write("CA-R-1", "Core/Atom", [], directory=self.role / "archive")
        archived = run_subject_search(self.root, self._args())
        self.assertEqual(archived["count"], 1)
        duplicate = self.role / "CA-R-1-CORE-REQUIREMENT--duplicate.md"
        duplicate.write_text((self.role / "CA-R-1-CORE-REQUIREMENT--fixture.md").read_text(encoding="utf-8"), encoding="utf-8")
        current = run_subject_search(self.root, self._args())
        self.assertEqual(current["count"], 0)
        self.assertIn("duplicate-original-id", {item["code"] for item in current["diagnostics"]})

    def test_analysis_and_complete_subject_validation(self) -> None:
        analysis = self._write("CA-A-9", "Core/Atom", [], role="Analysis")
        result = run_subject_search(self.root, self._args(content_role=["Analysis"]))
        self.assertEqual(result["count"], 1)
        original = analysis.read_text(encoding="utf-8")
        governs_line = '  governs: "Core/Atom"\n'
        self.assertIn(governs_line, original)
        analysis.write_text(original.replace(governs_line, "", 1), encoding="utf-8")
        invalid = run_subject_search(self.root, self._args(subject_field="depends_on"))
        self.assertIn("subject-invalid", {item["code"] for item in invalid["diagnostics"]})

    def test_filename_mismatch_and_symlink_frontier_are_rejected(self) -> None:
        bad = self._write("CA-R-8", "Core/Atom", [])
        bad.rename(self.role / "CA-R-7-CORE-REQUIREMENT--wrong-id.md")
        invalid = run_subject_search(self.root, self._args())
        self.assertIn("source-invalid", {item["code"] for item in invalid["diagnostics"]})
        linked = self.role.parent / "linked"
        linked.symlink_to(self.role, target_is_directory=True)
        with self.assertRaises(ToolError) as context:
            run_subject_search(self.root, self._args(under=linked.relative_to(self.root).as_posix()))
        self.assertEqual(context.exception.code, "path-symlink")
        with self.assertRaises(ToolError) as context:
            run_subject_search(self.root, self._args(under=str(linked)))
        self.assertEqual(context.exception.code, "path-symlink")

    def test_filename_id_kind_must_match_content_role(self) -> None:
        self._write("CA-M-8", "Core/Atom", [], role="Requirement")
        result = run_subject_search(self.root, self._args())
        self.assertIn("source-invalid", {item["code"] for item in result["diagnostics"]})

    def test_active_default_excludes_backlog_plan_outside_lifecycle_folder(self) -> None:
        planning = self.role.parent / "031_planning"
        self._write("CA-P-9", "Core/Atom", [], directory=planning, role="Plan", status="Backlog")
        active = run_subject_search(self.root, self._args(content_role=["Plan"]))
        self.assertEqual(active["count"], 0)
        all_lifecycles = run_subject_search(self.root, self._args(content_role=["Plan"], lifecycle="all"))
        self.assertEqual(all_lifecycles["count"], 1)
