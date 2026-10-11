"""Profile-aware Subject parsing stays internal to graph/source helpers."""

from __future__ import annotations

import hashlib
import shutil
import sys
import tempfile
import unittest
from dataclasses import FrozenInstanceError
from pathlib import Path


REPOSITORY = Path(__file__).resolve().parents[5]
TOOL_DIRECTORY = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOL_DIRECTORY.parent))
sys.path.insert(0, str(TOOL_DIRECTORY))

import generate_entity_graph as graph  # noqa: E402
import subject_model_sources as sources  # noqa: E402
import subject_notation  # noqa: E402


TEST_TEMP_ROOT = Path.cwd() / ".caprmedio_tmp" / "tests" / Path(__file__).stem
TEST_TEMP_ROOT.mkdir(parents=True, exist_ok=True)


def atom_text(atom_id: str, subject: str, *, depends_on: tuple[str, ...] = ()) -> str:
    dependencies = "\n".join(f"    - {value!r}" for value in depends_on)
    dependency_block = "  depends_on: []" if not dependencies else f"  depends_on:\n{dependencies}"
    return "\n".join(
        (
            "---",
            f"atom_id: {atom_id}",
            "version: 1",
            "content_role: Definition",
            "type: Definition",
            "status: Active",
            "current_scope_unit: CORE_META_MODEL",
            "claim_target_scope_unit: CORE_META_MODEL",
            "subjects:",
            f"  governs: {subject!r}",
            dependency_block,
            "---",
            "# Summary",
            "",
            "Source summary",
            "",
            "## Claim",
            "",
            "No native relation is admitted by this graph parser.",
        )
    )


class SubjectProfileGraphTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory(dir=TEST_TEMP_ROOT, ignore_cleanup_errors=True)
        self.addCleanup(self.temporary.cleanup)
        self.repository = Path(self.temporary.name)
        self.selected = self.repository / "sources"
        self.selected.mkdir()

    def write(self, atom_id: str, subject: str, *, depends_on: tuple[str, ...] = ()) -> Path:
        path = self.selected / f"{atom_id}.md"
        path.write_text(atom_text(atom_id, subject, depends_on=depends_on), encoding="utf-8")
        return path

    def carriers(self) -> list[graph.AtomCarrier]:
        rows, diagnostics = graph.discover_atoms(self.repository, self.selected)
        self.assertEqual([], diagnostics)
        return rows

    def copy_current_approved_pins(self) -> None:
        for pin in subject_notation.get_profile("approved").grammar_pins:
            source = REPOSITORY / pin.path
            destination = self.repository / pin.path
            self.assertTrue(source.is_file(), source)
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(source, destination)
            self.assertEqual(pin.sha256, hashlib.sha256(destination.read_bytes()).hexdigest())

    def test_approved_mixed_path_retains_full_prefixes_and_only_emits_dot_and_colon_edges(self) -> None:
        subject = "Core/Atom.Dependent: Value"
        self.write("CA-R-2070", subject, depends_on=("Core/Claim.Dependent",))

        projection = graph.generate_projection(self.repository, self.selected, subject_profile="approved")

        edges = [
            (row["relation"], row["source_subject"], row["source_term"], row["target_subject"], row["target_term"])
            for row in projection["term_system"]["edges"]
        ]
        self.assertEqual(
            [
                ("IS_ALLOWED_VALUE_OF", "Core/Atom.Dependent: Value", "Value", "Core/Atom.Dependent", "Dependent"),
                ("IS_BORNE_BY", "Core/Atom.Dependent", "Dependent", "Core/Atom", "Atom"),
                ("IS_BORNE_BY", "Core/Claim.Dependent", "Dependent", "Core/Claim", "Claim"),
            ],
            edges,
        )
        self.assertNotIn(
            ("IS_BORNE_BY", "Core/Atom", "Atom", "Core", "Core"),
            edges,
        )
        self.assertFalse(any(row[0] == "NARROWER_THAN" for row in edges))
        self.assertEqual(
            subject,
            projection["claim_subject_relations"][1]["subject_path"],
        )
        relations, diagnostics = graph.parse_subject_relations(
            self.carriers()[0], subject_profile="approved"
        )
        self.assertEqual([], diagnostics)
        dependency_graph, dependency_evidence, cycles = graph._term_dependencies(
            relations, {"Value", "Dependent"}, subject_profile="approved"
        )
        self.assertEqual({"Dependent": [], "Value": ["Dependent"]}, dependency_graph)
        self.assertEqual([], cycles)
        self.assertEqual("Value", dependency_evidence[0]["source"])
        self.assertEqual("Dependent", dependency_evidence[0]["target"])
        tree = projection["sets"]["declared_term_tree"]
        self.assertIsNone(tree[0]["children"][0]["relation_from_parent"])
        self.assertEqual("IS_BORNE_BY", tree[0]["children"][0]["children"][0]["relation_from_parent"])
        self.assertEqual("IS_ALLOWED_VALUE_OF", tree[0]["children"][0]["children"][0]["children"][0]["relation_from_parent"])

    def test_legacy_dot_is_literal_and_default_stays_legacy(self) -> None:
        subject = "Core.Atom/Property: Value"
        self.write("CA-R-2071", subject)

        default = graph.generate_projection(self.repository, self.selected)
        explicit = graph.generate_projection(self.repository, self.selected, subject_profile="legacy")

        self.assertEqual("Value", graph.terminal_term(subject))
        self.assertEqual(
            [("Core.Atom", None), ("Property", "/"), ("Value", ":")],
            graph._subject_parts(subject),
        )
        self.assertEqual(default["term_system"], explicit["term_system"])
        self.assertIn(
            ("IS_BORNE_BY", "Core.Atom/Property", "Property", "Core.Atom", "Core.Atom"),
            [
                (row["relation"], row["source_subject"], row["source_term"], row["target_subject"], row["target_term"])
                for row in default["term_system"]["edges"]
            ],
        )

    def test_profile_failures_and_at_rejection_keep_graph_error_codes(self) -> None:
        with self.assertRaises(graph.EntityGraphError) as unknown:
            graph.terminal_term("Atom", subject_profile="unapproved")
        self.assertEqual("profile-unknown", unknown.exception.code)

        self.write("CA-R-2072", "Atom@12")
        with self.assertRaises(graph.EntityGraphError) as unsupported:
            graph.generate_projection(self.repository, self.selected, subject_profile="approved")
        self.assertEqual("subject-at-unsupported", unsupported.exception.code)

    def test_profile_pins_are_immutable_and_evidence_is_fresh(self) -> None:
        profile = subject_notation.get_profile("approved")
        with self.assertRaises(FrozenInstanceError):
            profile.name = "legacy"  # type: ignore[misc]
        with self.assertRaises(FrozenInstanceError):
            profile.grammar_pins[0].sha256 = "0" * 64  # type: ignore[misc]

        first = subject_notation.profile_evidence("approved")
        first["grammar_pins"][0]["atom_id"] = "CA-R-FORGED"  # type: ignore[index]
        second = subject_notation.profile_evidence("approved")
        self.assertEqual("CA-R-1931", second["grammar_pins"][0]["atom_id"])  # type: ignore[index]
        self.assertEqual("not_performed", second["native_admission"])

    def test_approved_source_provider_binds_current_pins_and_keeps_old_extractor_evidence(self) -> None:
        self.copy_current_approved_pins()
        self.write("CA-R-2073", "Core/Atom.Dependent: Value")

        result = sources.collect_subject_model_sources(
            self.repository, self.carriers(), subject_profile="approved"
        ).as_dict()

        self.assertEqual("approved", result["subject_profile"])
        self.assertEqual("not_performed", result["subject_profile_evidence"]["native_admission"])
        self.assertEqual(
            ["CA-D-269", "CA-R-1194"],
            [pin["atom_id"] for pin in result["grammar_pins"]],
        )
        self.assertEqual(
            ["CA-R-1931", "CA-R-1321", "CA-R-1324", "CA-M-228", "CA-E-383"],
            [pin["atom_id"] for pin in result["subject_profile_evidence"]["grammar_pins"]],
        )

    def test_approved_source_provider_rejects_stale_and_symlinked_current_pins(self) -> None:
        self.copy_current_approved_pins()
        self.write("CA-R-2074", "Core/Atom.Dependent")
        first = subject_notation.get_profile("approved").grammar_pins[0]
        first_path = self.repository / first.path
        first_path.write_bytes(first_path.read_bytes() + b"\nchanged after grammar pin\n")
        with self.assertRaises(sources.SubjectModelSourceError) as stale:
            sources.collect_subject_model_sources(self.repository, self.carriers(), subject_profile="approved")
        self.assertEqual("approved-grammar-pin-stale", stale.exception.code)

        self.copy_current_approved_pins()
        linked = self.repository / first.path
        replacement = linked.with_name("replacement.md")
        replacement.write_bytes(linked.read_bytes())
        try:
            linked.unlink()
            linked.symlink_to(replacement)
        except (OSError, NotImplementedError):
            self.skipTest("symlinks are unavailable")
        with self.assertRaises(sources.SubjectModelSourceError) as symlink:
            sources.collect_subject_model_sources(self.repository, self.carriers(), subject_profile="approved")
        self.assertEqual("approved-grammar-pin-symlink", symlink.exception.code)


if __name__ == "__main__":
    unittest.main()
