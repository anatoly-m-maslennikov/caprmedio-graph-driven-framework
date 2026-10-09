"""Step-1 acceptance tests for literal, non-admitting Subject notation output."""

from __future__ import annotations

import sys
import tempfile
import unittest
import hashlib
from pathlib import Path


TEST_TEMP_ROOT = Path.cwd() / ".caprmedio_tmp" / "tests" / Path(__file__).stem
TEST_TEMP_ROOT.mkdir(parents=True, exist_ok=True)
TOOL_DIRECTORY = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOL_DIRECTORY))
import mechanical_subject_graph as mechanical  # type: ignore[import-not-found]  # noqa: E402


def atom(atom_id: str, governs: str, depends_on: tuple[str, ...] = ()) -> str:
    values = ", ".join(repr(item) for item in depends_on)
    return (
        "---\n"
        f"atom_id: {atom_id}\nversion: 1\ncontent_role: Requirement\ntype: Demand\nstatus: Active\n"
        "current_scope_unit: CORE_META_MODEL\nclaim_target_scope_unit: CORE_META_MODEL\nsubjects:\n"
        f"  governs: {governs!r}\n  depends_on: [{values}]\n---\n"
        "# Summary\n\nMechanical fixture.\n\n## Scope\n\nCORE_META_MODEL.\n\n"
        "## Claim\n\nNo semantic admission is asserted.\n\n## Details\n\nNo metadata becomes a model node.\n"
    )


class MechanicalSubjectGraphAcceptanceTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory(dir=TEST_TEMP_ROOT, ignore_cleanup_errors=True)
        self.addCleanup(self.temporary.cleanup)
        self.repository = Path(self.temporary.name) / "first"
        self.other_repository = Path(self.temporary.name) / "second"
        self._seed(self.repository, (
            ("CA-R-9201", "Atom/Status: Active", ("Atom/Status",)),
            ("CA-R-9202", "Workflow/Status: Active", ()),
        ))
        self._seed(self.other_repository, (("CA-R-9301", "Atom/Status: Active", ()),))

    @staticmethod
    def _seed(repository: Path, carriers: tuple[tuple[str, str, tuple[str, ...]], ...]) -> None:
        control = repository / ".caprmedio_caprmedio"
        core = control / "core"
        core.mkdir(parents=True)
        (control / "caprmedio_project_settings.toml").write_text(
            "[paths]\ncontrol_root = '.caprmedio_caprmedio'\nprojection_root = '.caprmedio_caprmedio/_projection'\n",
            encoding="utf-8",
        )
        (control / "project_structure.toml").write_text(
            "[[scope_units]]\nscope_unit_name = 'CORE_META_MODEL'\nauthority_path = '.caprmedio_caprmedio/core'\nauthority_mode = 'strict'\n",
            encoding="utf-8",
        )
        for atom_id, governs, depends_on in carriers:
            (core / f"{atom_id}.md").write_text(atom(atom_id, governs, depends_on), encoding="utf-8", newline="\n")

    @staticmethod
    def _nodes(graph: dict) -> set[str]:
        return {row["identity"] for row in graph["nodes"]}

    @staticmethod
    def _edges(graph: dict) -> set[tuple[str, str, str]]:
        return {(row["kind"], row["source_identity"], row["target_identity"]) for row in graph["edges"]}

    def _source_bytes(self, repository: Path) -> dict[str, bytes]:
        return {
            path.relative_to(repository).as_posix(): path.read_bytes()
            for path in sorted((repository / ".caprmedio_caprmedio" / "core").glob("*.md"))
        }

    def test_projection_keeps_contextual_full_identities_and_never_admits_native_facts(self) -> None:
        before = self._source_bytes(self.repository)
        data = mechanical.build_mechanical_subject_graph(self.repository)
        entities = data["entities_graph"]
        terms = data["terms_graph"]

        self.assertEqual(before, self._source_bytes(self.repository))
        self.assertEqual("not_performed", data["native_admission"])
        self.assertEqual("not_performed", data["source_migration"])
        self.assertEqual("not_performed", data["content_classification"])
        self.assertEqual({"Atom", "Status", "Active", "Workflow"}, self._nodes(terms))
        self.assertEqual(set(), self._edges(terms))
        self.assertEqual(
            {"Atom", "Atom/Status", "Atom/Status: Active", "Workflow", "Workflow/Status", "Workflow/Status: Active"},
            self._nodes(entities),
        )
        self.assertIn(("IS_ALLOWED_VALUE_OF", "Atom/Status: Active", "Atom/Status"), self._edges(entities))
        self.assertIn(("IS_ALLOWED_VALUE_OF", "Workflow/Status: Active", "Workflow/Status"), self._edges(entities))
        self.assertNotIn("CA-R-9201", self._nodes(entities) | self._nodes(terms))
        self.assertTrue(all(row["kind"] == "UNCLASSIFIED" for row in entities["edges"] if row["source_separator"] == "/"))
        occurrence_ids = {row["occurrence_id"] for row in data["occurrences"]}
        self.assertTrue(all(set(row["occurrence_ids"]) <= occurrence_ids for row in entities["edges"]))
        self.assertTrue(all(row["source_ref"]["carrier_sha256"] for row in data["occurrences"]))

    def test_parser_preserves_literal_prefixes_and_leaves_slash_unclassified(self) -> None:
        parsed = mechanical.parse_subject_expression("Atom/Status: Active")

        self.assertEqual("Atom/Status: Active", parsed["source_expression"])
        self.assertEqual(["Atom", "Atom/Status", "Atom/Status: Active"], parsed["literal_prefixes"])
        self.assertEqual(["/", ":"], parsed["separators"])
        self.assertEqual("UNCLASSIFIED", parsed["slash_steps"][0]["classification"])
        self.assertEqual({"source": "Atom/Status: Active", "target": "Atom/Status"}, parsed["value_link"])

    def test_source_binding_dot_and_create_only_publication_are_explicit(self) -> None:
        first = mechanical.build_mechanical_subject_graph(self.repository)
        second = mechanical.build_mechanical_subject_graph(self.other_repository)

        self.assertNotEqual(first["source_binding"]["source_frontier_sha256"], second["source_binding"]["source_frontier_sha256"])
        self.assertNotEqual(first["graph_sha256"], second["graph_sha256"])
        entities_dot = mechanical.graph_dot(first, graph_kind="entities")
        self.assertIn("IS_ALLOWED_VALUE_OF", entities_dot)
        self.assertIn("UNCLASSIFIED", entities_dot)
        terms_dot = mechanical.graph_dot(first, graph_kind="terms")
        self.assertNotIn("NARROWER_THAN", terms_dot)
        output_directory = self.repository / ".caprmedio_caprmedio" / "_projection" / "core-subject-notation"
        self.assertFalse((output_directory / "step1.graph.json").exists())
        self.assertFalse((output_directory / "step1.entities.graph.dot").exists())
        self.assertFalse((output_directory / "step1.terms.graph.dot").exists())

    def test_create_only_publication_has_exact_source_provenance_and_never_overwrites(self) -> None:
        before = self._source_bytes(self.repository)
        data = mechanical.build_mechanical_subject_graph(self.repository)
        receipt = mechanical.persist_mechanical_subject_graph(self.repository, data)
        output_directory = self.repository / ".caprmedio_caprmedio" / "_projection" / "core-subject-notation"

        self.assertEqual("declared_syntax_projection_created", receipt["outcome"])
        self.assertEqual("not_performed", receipt["run_recording"])
        self.assertEqual(before, self._source_bytes(self.repository))
        self.assertEqual(
            {"step1.graph.json", "step1.entities.graph.dot", "step1.terms.graph.dot"},
            {Path(row["path"]).name for row in receipt["outputs"]},
        )
        for row in receipt["outputs"]:
            self.assertEqual(hashlib.sha256((self.repository / row["path"]).read_bytes()).hexdigest(), row["sha256"])
        with self.assertRaises(ValueError):
            mechanical.persist_mechanical_subject_graph(self.repository, data)
        self.assertTrue((output_directory / "step1.graph.json").is_file())

    def test_malformed_subject_is_diagnosed_without_source_mutation_or_implicit_publication(self) -> None:
        before = self._source_bytes(self.repository)
        source = self.repository / ".caprmedio_caprmedio" / "core" / "CA-R-9203.md"
        source.write_text(atom("CA-R-9203", "Atom//Status", ()), encoding="utf-8", newline="\n")

        with self.assertRaises(ValueError):
            mechanical.build_mechanical_subject_graph(self.repository)

        self.assertEqual(before, {path: value for path, value in self._source_bytes(self.repository).items()
                                  if path != source.relative_to(self.repository).as_posix()})
        self.assertFalse((self.repository / ".caprmedio_caprmedio" / "_projection" / "core-subject-notation" / "step1.graph.json").exists())


if __name__ == "__main__":
    unittest.main()
