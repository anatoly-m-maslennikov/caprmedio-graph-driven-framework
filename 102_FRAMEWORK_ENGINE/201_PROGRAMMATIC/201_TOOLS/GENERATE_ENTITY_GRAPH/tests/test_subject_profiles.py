"""Profile-aware Subject parsing stays internal to graph/source helpers."""

from __future__ import annotations

import hashlib
import json
import sys
import tempfile
import unittest
from dataclasses import FrozenInstanceError
from pathlib import Path


TOOL_DIRECTORY = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOL_DIRECTORY.parent))
sys.path.insert(0, str(TOOL_DIRECTORY))

import generate_entity_graph as graph  # noqa: E402
import subject_model_sources as sources  # noqa: E402
import subject_notation  # noqa: E402


TEST_TEMP_ROOT = Path.cwd() / ".caprmedio_tmp" / "tests" / Path(__file__).stem
TEST_TEMP_ROOT.mkdir(parents=True, exist_ok=True)


def atom_text(atom_id: str, subject: str, *, depends_on: tuple[str, ...] = ()) -> str:
    dependencies = "\n".join(f"    - {json.dumps(value)}" for value in depends_on)
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
            f"  governs: {json.dumps(subject)}",
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

    def write_subject_block(self, atom_id: str, block: str) -> Path:
        path = self.selected / f"{atom_id}.md"
        text = atom_text(atom_id, "Placeholder").replace(
            'subjects:\n  governs: "Placeholder"\n  depends_on: []', block
        )
        path.write_text(text, encoding="utf-8")
        return path

    def copy_current_approved_pins(self) -> None:
        for pin in subject_notation.get_profile("approved").grammar_pins:
            destination = self.repository / pin.path
            destination.parent.mkdir(parents=True, exist_ok=True)
            raw = (Path(__file__).resolve().parents[5] / pin.path).read_bytes()
            destination.write_bytes(raw)
            self.assertEqual(raw, destination.read_bytes())

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

    def test_bare_selectors_name_only_existing_atom_term_and_preserve_owner_identities(self) -> None:
        selectors = (
            'atom(atom_id="CA-O-135")',
            'atom(content_role="Plan")',
            'atom(content_role="Plan",type="Plan")',
            'atom( content_role = "Owner/Plan.Kind: Value, O\'Brien" , type = "Plan/Kind" )',
        )
        for index, selector in enumerate(selectors):
            with self.subTest(selector=selector):
                self.assertEqual([(selector, None)], graph._subject_parts(selector, subject_profile="approved"))
                self.assertEqual("Atom", graph.terminal_term(selector, subject_profile="approved"))
                self.assertEqual("Status", graph.terminal_term(selector + ".Status", subject_profile="approved"))
            self.write(f"CA-R-{2080 + index}", selector)

        projection = graph.generate_projection(self.repository, self.selected, subject_profile="approved")
        self.assertEqual(["Atom"], projection["declared_terms"])
        self.assertEqual([], projection["term_system"]["edges"])
        self.assertEqual(sorted(selectors), projection["governed_subjects"])
        self.assertEqual(sorted(selectors), sorted(row["subject_path"] for row in projection["claim_subject_relations"]))
        roots = projection["sets"]["declared_term_tree"]
        self.assertEqual(sorted(selectors), [node["subject_path"] for node in roots])
        self.assertTrue(all(node["declared_term"] == "Atom" for node in roots))

    def test_selected_owner_edges_tree_and_incidence_do_not_flatten_patterns(self) -> None:
        owners = ('atom(atom_id="CA-O-135")', 'atom(content_role="Plan")', 'atom(content_role="Plan",type="Plan")')
        for index, owner in enumerate(owners):
            self.write(f"CA-R-{2090 + index}", owner + ".Status: Active", depends_on=(owner,))
        projection = graph.generate_projection(self.repository, self.selected, subject_profile="approved")
        self.assertEqual(["Active"], projection["declared_terms"])
        edges = projection["term_system"]["edges"]
        self.assertEqual(6, len(edges))
        for owner in owners:
            bearer = next(row for row in edges if row["source_subject"] == owner + ".Status")
            self.assertEqual(("IS_BORNE_BY", "Status", owner, "Atom"),
                             (bearer["relation"], bearer["source_term"], bearer["target_subject"], bearer["target_term"]))
            self.assertEqual(owner + ".Status: Active", bearer["evidence"][0]["subject_path"])
            value = next(row for row in edges if row["source_subject"] == owner + ".Status: Active")
            self.assertEqual(("IS_ALLOWED_VALUE_OF", owner + ".Status", "Status"),
                             (value["relation"], value["target_subject"], value["target_term"]))
        self.assertEqual(sorted(owners), [node["subject_path"] for node in projection["sets"]["declared_term_tree"]])
        self.assertEqual({owner + ".Status: Active" for owner in owners},
                         {row["subject_path"] for row in projection["claim_subject_relations"] if row["kind"] == "GOVERNS"})
        self.assertFalse(any(row["relation"] == "NARROWER_THAN" for row in edges))

    def test_selector_first_separator_retains_slash_dot_and_colon_semantics(self) -> None:
        owner = 'atom(content_role="Plan",type="Plan")'
        for separator, dependent in (("/", "Child"), (".", "Status"), (":", "Plan")):
            with self.subTest(separator=separator):
                subject = owner + separator + (" " if separator == ":" else "") + dependent
                self.assertEqual([(owner, None), (dependent, separator)], graph._subject_parts(subject, subject_profile="approved"))
                self.write("CA-R-2100", subject)
                projection = graph.generate_projection(self.repository, self.selected, subject_profile="approved")
                edges = projection["term_system"]["edges"]
                if separator == "/":
                    self.assertEqual([], edges)
                    self.assertIsNone(projection["sets"]["declared_term_tree"][0]["children"][0]["relation_from_parent"])
                else:
                    self.assertEqual(1, len(edges))
                    self.assertEqual(owner, edges[0]["target_subject"])
                    self.assertEqual("Atom", edges[0]["target_term"])
                    self.assertEqual("IS_BORNE_BY" if separator == "." else "IS_ALLOWED_VALUE_OF", edges[0]["relation"])
                self.assertEqual(subject, graph.parse_subject_relations(self.carriers()[0], subject_profile="approved")[0][0].subject_path)

    def test_approved_yaml_quotes_flow_and_block_lists_preserve_decoded_selectors_and_source_spans(self) -> None:
        self.copy_current_approved_pins()
        owner = 'atom( content_role = "Owner/Plan.Kind: Value, O\'Brien" , type = "Plan" )'
        governs = owner + ".Status: Active"
        dependencies = ('atom(atom_id="CA-O-135").Status', 'atom(content_role="Plan",type="Plan")/Child')
        for quotes in ("double", "single"):
            quote = json.dumps if quotes == "double" else lambda value: "'" + value.replace("'", "''") + "'"
            for collection in ("flow", "block"):
                with self.subTest(quotes=quotes, collection=collection):
                    dependency_yaml = "[" + ", ".join(quote(value) for value in dependencies) + "]" if collection == "flow" else "\n" + "\n".join("    - " + quote(value) for value in dependencies)
                    self.write_subject_block("CA-R-2101", "subjects:\n  governs: " + quote(governs) + "\n  depends_on: " + dependency_yaml)
                    carriers = self.carriers()
                    rows, diagnostics = graph.parse_subject_relations(carriers[0], subject_profile="approved")
                    self.assertEqual([], diagnostics)
                    self.assertEqual({governs, *dependencies}, {row.subject_path for row in rows})
                    result = sources.collect_subject_model_sources(self.repository, carriers, subject_profile="approved").as_dict()
                    self.assertEqual("complete", result["coverage"]["disposition"])
                    self.assertEqual([], result["diagnostics"])
                    self.assertEqual({governs, *dependencies}, {row["subject_path"] for row in result["occurrences"]})
                    raw = (self.repository / carriers[0].carrier_path).read_bytes()
                    for row in result["occurrences"]:
                        ref = row["source_ref"]["contribution"]
                        span = b"".join(raw.splitlines(keepends=True)[ref["start_line"] - 1:ref["end_line"]])
                        self.assertEqual(hashlib.sha256(span).hexdigest(), ref["text_sha256"])
                        self.assertIn(quote(row["subject_path"]).encode(), span)

    def test_approved_yaml_requires_text_and_rejects_malformed_selectors_without_legacy_drift(self) -> None:
        self.copy_current_approved_pins()
        for encoded in ("true", "12", "null", "{owner: Atom}", '"unterminated', "&owner Atom", "!!str Atom", '["Atom", 12]'):
            with self.subTest(encoded=encoded):
                self.write_subject_block("CA-R-2102", "subjects:\n  governs: Atom\n  depends_on: " + encoded)
                with self.assertRaises(graph.EntityGraphError) as failure:
                    graph.parse_subject_relations(self.carriers()[0], subject_profile="approved")
                self.assertEqual("subjects-yaml-invalid", failure.exception.code)
                result = sources.collect_subject_model_sources(
                    self.repository, self.carriers(), subject_profile="approved"
                ).as_dict()
                self.assertEqual("incomplete", result["coverage"]["disposition"])
                self.assertEqual([], result["occurrences"])
        for malformed in (
            'atom(type="Plan").Status',
            'atom(atom_id="CA-O-135",content_role="Plan").Status',
            'Atom(content_role="Plan").Status',
            'Artifact/atom(atom_id="CA-O-135")',
            'atom(content_role="Plan").Status@current',
            'atom(content_role="Plan")/',
        ):
            with self.subTest(malformed=malformed):
                with self.assertRaises(graph.EntityGraphError):
                    graph._subject_parts(malformed, subject_profile="approved")
        for ordinary in ("atom", 'Ordinary "quoted" Term', "Core.Atom"):
            self.assertEqual(ordinary, graph.terminal_term(ordinary))
            self.assertEqual([(ordinary, None)], graph._subject_parts(ordinary))
        self.assertEqual('a\\"b', graph.scalar_value('"a\\"b"'))
        with self.assertRaises(graph.EntityGraphError):
            graph.terminal_term("atom", subject_profile="approved")
        with self.assertRaises(graph.EntityGraphError):
            graph.terminal_term('atom(content_role="Plan").Status')

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

        self.copy_current_approved_pins()
        first = sources._check_current_approved_grammar_pins(self.repository, profile)
        first["grammar_pins"][0]["atom_id"] = "CA-R-FORGED"  # type: ignore[index]
        second = sources._check_current_approved_grammar_pins(self.repository, profile)
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
        first_path.write_bytes(first_path.read_bytes().replace(first.atom_id.encode(), b"CA-R-99999", 1))
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

    def test_new_request_observes_changed_current_grammar_but_same_request_rejects_drift(self) -> None:
        self.copy_current_approved_pins()
        profile = subject_notation.get_profile("approved")
        first = sources._check_current_approved_grammar_pins(self.repository, profile)
        source = profile.grammar_pins[0]
        path = self.repository / source.path
        raw = path.read_bytes()
        version = first["grammar_pins"][0]["version"]
        path.write_bytes(raw.replace(f"version: {version}".encode(), f"version: {version + 1}".encode(), 1))
        second = sources._check_current_approved_grammar_pins(self.repository, profile)
        self.assertEqual(version + 1, second["grammar_pins"][0]["version"])
        self.assertEqual(hashlib.sha256(path.read_bytes()).hexdigest(), second["grammar_pins"][0]["sha256"])
        with self.assertRaises(sources.SubjectModelSourceError):
            sources._check_current_approved_grammar_pins(self.repository, profile, expected=first)


if __name__ == "__main__":
    unittest.main()
