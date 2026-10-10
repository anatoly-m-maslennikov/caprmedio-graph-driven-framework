from __future__ import annotations

import argparse
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

    def _write(self, atom_id: str, governs: str, depends: list[str], *, directory: Path | None = None, role: str = "Requirement") -> Path:
        path = (directory or self.role) / f"{atom_id}-CORE-REQUIREMENT--fixture.md"
        path.parent.mkdir(parents=True, exist_ok=True)
        dependencies = "\n".join(f"    - {value}" for value in depends)
        path.write_text(
            f"---\natom_id: {atom_id}\nversion: 1\nstatus: Active\ncontent_role: {role}\ncurrent_scope_unit: CORE\nupdated_at: now\nsubjects:\n  governs: {governs}\n"
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
        prefix = run_subject_search(self.root, self._args(subject_match="prefix"))
        self.assertEqual(prefix["count"], 2)
        self.assertEqual([item["index"] for item in prefix["occurrences"]], [None, 1])

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
        analysis.write_text(analysis.read_text(encoding="utf-8").replace("  governs: Core/Atom\n", ""), encoding="utf-8")
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
