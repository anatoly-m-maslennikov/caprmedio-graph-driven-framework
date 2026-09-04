from __future__ import annotations

import contextlib
import importlib.util
import io
import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path


TOOL = Path(__file__).resolve().parents[1] / "retrieve_applicable_methodology.py"
SPEC = importlib.util.spec_from_file_location("retrieve_applicable_methodology", TOOL)
assert SPEC and SPEC.loader
module = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = module
SPEC.loader.exec_module(module)


def source_carrier(atom_id: str, governs: tuple[str, str], depends_on: tuple[str, str] | None = None) -> bytes:
    dependency = ""
    if depends_on:
        dependency = f"  depends_on:\n    {depends_on[0]}:\n      - {depends_on[1]}\n"
    return (
        "---\n"
        f"atom_id: {atom_id}\n"
        "cce_version: cce_1\n"
        "cce_form: obligation\n"
        "subjects:\n"
        "  governs:\n"
        f"    {governs[0]}:\n"
        f"      - {governs[1]}\n"
        f"{dependency}"
        "version: 1\n"
        "updated_at: 2026-08-27 00:00:00 +0400\n"
        "relations: {}\n"
        "---\n"
        f"# {atom_id}\n\nclaim\n"
    ).encode()


def projected(source: bytes, relative_source: str) -> bytes:
    boundary = source.find(b"\n---\n", 4)
    addition = f"\nprojection:\n  source_carrier_path: {relative_source}".encode()
    return source[:boundary] + addition + source[boundary:]


class RetrieverTest(unittest.TestCase):
    def setUp(self) -> None:
        runtime = Path.cwd() / ".caprmedio_runtime/retriever-tests"
        runtime.mkdir(parents=True, exist_ok=True)
        self.root = Path(tempfile.mkdtemp(prefix="case-", dir=runtime))
        self.applicable = self.root / module.APPLICABLE_RELATIVE
        self.source_root = self.root / module.SOURCES_RELATIVE / "001_CORE_META_MODEL"
        for role in module.ROLES:
            (self.applicable / role).mkdir(parents=True)
            (self.source_root / role).mkdir(parents=True)

    def tearDown(self) -> None:
        shutil.rmtree(self.root, ignore_errors=True)

    def add(self, role: str, name: str, data: bytes) -> None:
        source = self.source_root / role / name
        source.write_bytes(data)
        target = self.applicable / role / name
        relative = Path("../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL") / role / name
        target.write_bytes(projected(data, relative.as_posix()))

    def add_project_scope_graph(self, project_name: str = "caprmedio") -> None:
        graph = self.root / module.PROJECT_SCOPE_GRAPH_RELATIVE
        graph.parent.mkdir(parents=True, exist_ok=True)
        graph.write_text(f"[project]\nname = {project_name!r}\n", encoding="utf-8")

    def invoke(self, *arguments: str) -> tuple[int, dict[str, object]]:
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            code = module.run(["--root", str(self.root), *arguments])
        return code, json.loads(output.getvalue())

    def test_subject_seed_closes_prerequisites_and_preserves_compilation_order(self) -> None:
        self.add("04_requirement", "CA-R-001--base.md", source_carrier("CA-R-001", ("continuant", "Base")))
        self.add(
            "05_method",
            "CA-M-001--consumer.md",
            source_carrier("CA-M-001", ("continuant", "Consumer"), ("continuant", "Base")),
        )
        code, report = self.invoke("--subject", "Consumer")
        self.assertEqual(code, 0)
        self.assertTrue(report["complete"])
        self.assertEqual([item["atom_id"] for item in report["selected_atoms"]], ["CA-R-001", "CA-M-001"])
        self.assertEqual(report["selected_atom_count"], 2)
        self.assertFalse(report["persistent_subject_index_created"])

    def test_process_query_matches_only_occurrent_governors(self) -> None:
        self.add("04_requirement", "CA-R-001--continuant.md", source_carrier("CA-R-001", ("continuant", "Build")))
        self.add("05_method", "CA-M-001--occurrent.md", source_carrier("CA-M-001", ("occurrent", "Build")))
        code, report = self.invoke("--process", "Build")
        self.assertEqual(code, 0)
        self.assertEqual([item["atom_id"] for item in report["selected_atoms"]], ["CA-M-001"])

    def test_unknown_uppercase_subject_fails_closed(self) -> None:
        self.add("04_requirement", "CA-R-001--base.md", source_carrier("CA-R-001", ("continuant", "Base")))
        code, report = self.invoke("--subject", "Missing")
        self.assertEqual(code, 2)
        self.assertEqual(report["selected_atom_count"], 0)
        self.assertFalse(report["complete"])
        self.assertEqual(report["diagnostics"][0]["subject_path"], "Missing")

    def test_scope_unit_query_returns_structural_frontier_without_atom_selection(self) -> None:
        code, report = self.invoke("--subject", "CORE_META_MODEL")
        self.assertEqual(code, 0)
        self.assertTrue(report["complete"])
        self.assertEqual(report["selected_atom_count"], 0)
        outcomes = report["resolution_outcomes"]
        self.assertTrue(all(item["category"] == "scope_unit" for item in outcomes))
        self.assertTrue(all(item["scope_unit"] == "CORE_META_MODEL" for item in outcomes))
        self.assertTrue(all(item["current_scope"] == "METHODOLOGY_SOURCES" for item in outcomes))

    def test_project_scope_unit_query_uses_project_structural_graph(self) -> None:
        self.add_project_scope_graph()
        code, report = self.invoke("--subject", "Project")
        self.assertEqual(code, 0)
        self.assertTrue(report["complete"])
        outcomes = report["resolution_outcomes"]
        self.assertTrue(all(item["category"] == "scope_unit" for item in outcomes))
        self.assertTrue(all(item["scope_unit"] == "caprmedio" for item in outcomes))
        self.assertTrue(all(item["source"] == "project_scope_unit_graph" for item in outcomes))

    def test_lowercase_general_subject_is_successful_terminal(self) -> None:
        code, report = self.invoke("--subject", "methodology")
        self.assertEqual(code, 0)
        self.assertTrue(report["complete"])
        self.assertEqual(report["selected_atom_count"], 0)
        outcomes = report["resolution_outcomes"]
        self.assertTrue(all(item["category"] == "general_subject" for item in outcomes))
        self.assertTrue(all(item["terminal"] == "true" for item in outcomes))

    def test_unresolved_prerequisite_is_explicit_and_fails_closed(self) -> None:
        self.add(
            "05_method",
            "CA-M-001--consumer.md",
            source_carrier("CA-M-001", ("continuant", "Consumer"), ("continuant", "Missing")),
        )
        code, report = self.invoke("--subject", "Consumer")
        self.assertEqual(code, 2)
        self.assertFalse(report["complete"])
        self.assertEqual(report["diagnostics"][0]["subject_path"], "Missing")

    def test_source_drift_fails_before_retrieval(self) -> None:
        self.add("04_requirement", "CA-R-001--base.md", source_carrier("CA-R-001", ("continuant", "Base")))
        source = self.source_root / "04_requirement/CA-R-001--base.md"
        source.write_bytes(source.read_bytes() + b"drift")
        code, report = self.invoke("--subject", "Base")
        self.assertEqual(code, 2)
        self.assertEqual(report["diagnostics"][0]["code"], "projection-source-mismatch")

    def test_same_frontier_produces_same_selection_digest(self) -> None:
        self.add("04_requirement", "CA-R-001--base.md", source_carrier("CA-R-001", ("continuant", "Base")))
        first_code, first = self.invoke("--subject", "Base")
        second_code, second = self.invoke("--subject", "Base")
        self.assertEqual((first_code, second_code), (0, 0))
        self.assertEqual(first["selected_frontier_digest"], second["selected_frontier_digest"])


if __name__ == "__main__":
    unittest.main()
