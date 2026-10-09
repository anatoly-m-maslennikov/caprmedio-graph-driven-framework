"""Step 1 wrapper tests: literal syntax only, no later classification/migration."""

from __future__ import annotations

import hashlib
import io
import json
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from unittest.mock import patch


TOOL_DIRECTORY = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOL_DIRECTORY))
import graph_fact_context as facts  # noqa: E402
import mechanical_subject_graph as mechanical  # noqa: E402

TEST_TEMP_ROOT = Path.cwd() / ".caprmedio_tmp/tests/test_mechanical_subject_graph"
TEST_TEMP_ROOT.mkdir(parents=True, exist_ok=True)


def atom(atom_id, target, dependencies=(), *, body="Source content not interpreted."):
    values = ", ".join(json.dumps(value) for value in dependencies)
    return (f"---\natom_id: {atom_id}\nversion: 1\ncontent_role: Requirement\ntype: Demand\nstatus: Active\n"
            "current_scope_unit: CORE_META_MODEL\nclaim_target_scope_unit: CORE_META_MODEL\nsubjects:\n"
            f"  governs: {json.dumps(target)}\n  depends_on: [{values}]\n---\n# Summary\n\nSource summary\n"
            f"\n## Scope\n\nCore.\n\n## Claim\n\n{body}\n\n## Details\n")


class MechanicalSubjectGraphTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory(dir=TEST_TEMP_ROOT, ignore_cleanup_errors=True)
        self.addCleanup(self.temporary.cleanup)
        self.repository = Path(self.temporary.name)
        control = self.repository / ".caprmedio_caprmedio"
        self.core = control / "core"
        self.core.mkdir(parents=True)
        (control / "caprmedio_project_settings.toml").write_text(
            "[paths]\ncontrol_root = '.caprmedio_caprmedio'\nprojection_root = '.caprmedio_caprmedio/_projection'\n", encoding="utf-8")
        self.structure = control / "project_structure.toml"
        self.structure.write_text("[[scope_units]]\nscope_unit_name = 'CORE_META_MODEL'\nauthority_path = '.caprmedio_caprmedio/core'\nauthority_mode = 'strict'\n", encoding="utf-8")
        self.first = self.core / "CA-R-9401.md"
        self.second = self.core / "CA-R-9402.md"
        self.first.write_text(atom("CA-R-9401", "Atom/Status: Active", ("Atom/Status",)), encoding="utf-8")
        self.second.write_text(atom("CA-R-9402", "Workflow/Status: Active", ()), encoding="utf-8")
        self.outputs = [self.repository / mechanical._OUTPUT_DIRECTORY / name for name in mechanical._OUTPUT_NAMES]

    def build(self):
        return mechanical.build_mechanical_subject_graph(self.repository)

    def source_bytes(self):
        return {path.name: path.read_bytes() for path in self.core.glob("*.md")}

    def test_literal_parser_handles_context_combinations_without_dot_interpretation(self) -> None:
        parsed = mechanical.parse_subject_expression("Atom/Status: Active")
        self.assertEqual(["Atom", "Atom/Status", "Atom/Status: Active"], parsed["literal_prefixes"])
        self.assertEqual(["/", ":"], parsed["separators"])
        self.assertEqual({"source": "Atom/Status: Active", "target": "Atom/Status"}, parsed["value_link"])
        nested = mechanical.parse_subject_expression("Atom/Content Role: Requirement/Type: Demand")
        self.assertEqual(["/", ":", "/", ":"], nested["separators"])
        self.assertEqual("Atom/Content Role: Requirement/Type", nested["value_link"]["target"])
        self.assertTrue(all(step["classification"] == "UNCLASSIFIED" for step in nested["slash_steps"]))
        dotted = mechanical.parse_subject_expression("Artifact/Atom.Status: Active")
        self.assertEqual(["Artifact", "Artifact/Atom.Status", "Artifact/Atom.Status: Active"], dotted["literal_prefixes"])
        self.assertNotIn("Atom.Status", dotted["literal_prefixes"])
        self.assertEqual(["Thing.with.dot"], mechanical.parse_subject_expression("Thing.with.dot")["literal_prefixes"])
        self.assertEqual(["Atom ", "Atom / Status", "Atom / Status: Active"],
                         mechanical.parse_subject_expression("Atom / Status: Active")["literal_prefixes"])
        for invalid in ("", "Atom//Status", "Atom/", "Atom:", None):
            with self.subTest(path=invalid), self.assertRaises((ValueError, mechanical.graph.EntityGraphError)):
                mechanical.parse_subject_expression(invalid)

    def test_nodes_and_edges_are_literal_deduplicated_and_possible_values_only(self) -> None:
        before = self.source_bytes()
        data = self.build()
        self.assertEqual(before, self.source_bytes())
        self.assertEqual({"Atom", "Atom/Status", "Atom/Status: Active", "Workflow", "Workflow/Status", "Workflow/Status: Active"},
                         {node["identity"] for node in data["entities_graph"]["nodes"]})
        self.assertEqual({"Atom", "Status", "Active", "Workflow"}, {node["identity"] for node in data["terms_graph"]["nodes"]})
        self.assertEqual([], data["terms_graph"]["edges"])
        self.assertEqual(2, data["counts"]["unclassified_slash_edges"])
        self.assertEqual(2, data["counts"]["allowed_value_edges"])
        edges = {(edge["kind"], edge["source_identity"], edge["target_identity"]) for edge in data["entities_graph"]["edges"]}
        self.assertIn(("IS_ALLOWED_VALUE_OF", "Atom/Status: Active", "Atom/Status"), edges)
        self.assertIn(("UNCLASSIFIED", "Atom", "Atom/Status"), edges)
        self.assertNotIn("CA-R-9401", {node["identity"] for node in data["entities_graph"]["nodes"]})
        self.assertEqual([], data["native_facts"])
        self.assertEqual("not_performed", data["semantic_admission"])
        self.assertEqual("not_performed", data["content_classification"])
        self.assertEqual("not_performed", data["source_migration"])
        self.assertNotIn("value_assignment", json.dumps(data))
        self.assertNotIn("NARROWER_THAN", json.dumps(data["terms_graph"]))
        self.assertNotIn("IS_BORNE_BY", json.dumps(data["entities_graph"]))

    def test_full_provenance_occurs_once_and_model_references_use_indices(self) -> None:
        data = self.build()
        self.assertEqual(list(range(len(data["occurrences"]))), [row["occurrence_id"] for row in data["occurrences"]])
        ids = {row["occurrence_id"] for row in data["occurrences"]}
        for model in (data["entities_graph"], data["terms_graph"]):
            self.assertNotIn("source_ref", json.dumps(model))
            for record in model["nodes"] + model["edges"]:
                self.assertTrue(set(record["occurrence_ids"]) <= ids)
        for occurrence in data["occurrences"]:
            ref = occurrence["source_ref"]
            raw = (self.repository / ref["carrier_path"]).read_bytes()
            location = ref["contribution"]
            span = b"".join(raw.splitlines(keepends=True)[location["start_line"] - 1:location["end_line"]])
            self.assertEqual(hashlib.sha256(span).hexdigest(), location["text_sha256"])
        self.assertNotIn("source_ref", json.dumps(data["source_links"]))

    def test_producer_profile_payload_and_graph_digest_are_readable_and_verifiable(self) -> None:
        data = self.build()
        profile = data["producer"]["profile_payload"]
        self.assertEqual(hashlib.sha256(facts.canonical_bytes(profile)).hexdigest(), data["producer"]["profile_sha256"])
        for key in ("implementation", "snapshot", "source_reader", "subject_parser", "fact_context"):
            self.assertEqual(hashlib.sha256(Path(profile[key]["loaded_path"]).read_bytes()).hexdigest(), profile[key]["sha256"])
        body = dict(data)
        digest = body.pop("graph_sha256")
        self.assertEqual(hashlib.sha256(facts.canonical_bytes(body)).hexdigest(), digest)
        self.assertEqual(data, self.build())

    def test_main_content_never_classifies_slash_or_creates_model_edges(self) -> None:
        first = self.build()
        self.first.write_text(atom("CA-R-9401", "Atom/Status: Active", ("Atom/Status",),
                                   body="Atom is a Property. Status NARROWER_THAN Atom. This content is not interpreted."), encoding="utf-8")
        second = self.build()
        self.assertEqual(first["entities_graph"], second["entities_graph"])
        self.assertEqual(first["terms_graph"], second["terms_graph"])
        self.assertNotEqual(first["source_frontier_evidence"], second["source_frontier_evidence"])

    def test_default_cli_dry_and_model_dot_never_inserts_source_atom_nodes(self) -> None:
        output = io.StringIO()
        with redirect_stdout(output):
            status = mechanical.main(["--repository", str(self.repository)])
        self.assertEqual(0, status)
        self.assertEqual("dry_run", json.loads(output.getvalue())["outcome"])
        self.assertFalse(any(path.exists() for path in self.outputs))
        data = self.build()
        self.assertIn("IS_ALLOWED_VALUE_OF", mechanical.graph_dot(data, "entities"))
        self.assertIn("UNCLASSIFIED", mechanical.graph_dot(data, "entities"))
        self.assertNotIn("CA-R-9401", mechanical.graph_dot(data, "entities"))
        self.assertNotIn("NARROWER_THAN", mechanical.graph_dot(data, "terms"))

    def test_incomplete_source_extraction_fails_without_implicit_publication(self) -> None:
        self.first.write_text(atom("CA-R-9401", "Atom//Status"), encoding="utf-8")
        with self.assertRaises(mechanical.MechanicalSubjectGraphError) as failure:
            self.build()
        self.assertEqual("mechanical-source-extraction-incomplete", failure.exception.code)
        self.assertFalse(any(path.exists() for path in self.outputs))

    def test_create_only_publication_preserves_before_files_and_all_source_bytes(self) -> None:
        before = self.source_bytes()
        data = self.build()
        self.outputs[0].parent.mkdir(parents=True)
        preserved = self.outputs[0].parent / "before.graph.json"
        preserved.write_bytes(b"existing before snapshot\n")
        receipt = mechanical.persist_mechanical_subject_graph(self.repository, data)
        self.assertEqual("declared_syntax_projection_created", receipt["outcome"])
        self.assertEqual(3, len(receipt["outputs"]))
        for record in receipt["outputs"]:
            self.assertEqual(hashlib.sha256((self.repository / record["path"]).read_bytes()).hexdigest(), record["sha256"])
        with self.assertRaises(mechanical.MechanicalSubjectGraphError) as failure:
            mechanical.persist_mechanical_subject_graph(self.repository, data)
        self.assertEqual("mechanical-output-exists", failure.exception.code)
        self.assertEqual(before, self.source_bytes())
        self.assertEqual(b"existing before snapshot\n", preserved.read_bytes())

    def test_stale_caller_data_and_changed_source_fail_before_output(self) -> None:
        data = self.build()
        forged = json.loads(json.dumps(data))
        forged["native_facts"] = [{"passed": True}]
        with self.assertRaises(mechanical.MechanicalSubjectGraphError):
            mechanical.persist_mechanical_subject_graph(self.repository, forged)
        self.first.write_bytes(self.first.read_bytes() + b"\nchanged after build\n")
        with self.assertRaises(mechanical.MechanicalSubjectGraphError):
            mechanical.persist_mechanical_subject_graph(self.repository, data)
        self.assertFalse(any(path.exists() for path in self.outputs))

    def test_current_code_drift_is_not_claimed_as_the_loaded_producer(self) -> None:
        original = Path.read_bytes
        changed = mechanical._IMPLEMENTATION_PATH.read_bytes() + b"\n# drift\n"
        with patch.object(Path, "read_bytes", autospec=True, side_effect=lambda path: changed if path == mechanical._IMPLEMENTATION_PATH else original(path)):
            with self.assertRaises(mechanical.MechanicalSubjectGraphError) as failure:
                self.build()
            self.assertEqual("profile-stale", failure.exception.code)


if __name__ == "__main__":
    unittest.main()
