"""Subjects extraction preserves current raw paths, not admitted model facts."""

from __future__ import annotations

import hashlib
import importlib.util
import sys
import tempfile
import unittest
from dataclasses import replace
from pathlib import Path
from unittest.mock import patch


TOOL_DIRECTORY = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOL_DIRECTORY))
import generate_entity_graph as graph  # noqa: E402
import graph_fact_context as facts  # noqa: E402
import subject_model_sources as subjects  # noqa: E402

TEST_TEMP_ROOT = Path.cwd() / ".caprmedio_tmp/tests/test_subject_model_sources"
TEST_TEMP_ROOT.mkdir(parents=True, exist_ok=True)


def atom_text(atom_id: str, subject_block: str) -> str:
    return "\n".join(("---", f"atom_id: {atom_id}", "version: 1", "content_role: Requirement",
                      "type: Demand", "status: Active", "current_scope_unit: CORE_META_MODEL",
                      "claim_target_scope_unit: CORE_META_MODEL", subject_block, "---", "# Summary", "",
                      "Source summary", "", "## Scope", "", "Selected source.", "", "## Claim", "",
                      "The Main Content is not semantically assessed by this reader.", "", "## Details", ""))


class SubjectModelSourceTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory(dir=TEST_TEMP_ROOT, ignore_cleanup_errors=True)
        self.addCleanup(self.temporary.cleanup)
        self.repository = Path(self.temporary.name)
        self.folder = self.repository / "sources"
        self.folder.mkdir()
        self.first = self.folder / "CA-R-9001.md"
        self.second = self.folder / "CA-R-9002.md"
        self.first.write_text(atom_text("CA-R-9001", 'subjects:\n  governs: "Atom/Claim"\n  depends_on:\n    - "Atom/Status: Active"\n    - "Artifact"'), encoding="utf-8")
        self.second.write_text(atom_text("CA-R-9002", 'subjects:\n  governs: "Artifact"\n  depends_on: []'), encoding="utf-8")
        self.carriers, diagnostics = graph.discover_atoms(self.repository, self.folder)
        self.assertEqual([], diagnostics)
        self.by_id = {carrier.atom_id: carrier for carrier in self.carriers}

    def changed_carrier(self, atom_id: str, raw: str | bytes):
        carrier = self.by_id[atom_id]
        data = raw.encode("utf-8") if isinstance(raw, str) else raw
        (self.repository / carrier.carrier_path).write_bytes(data)
        return replace(carrier, sha256=hashlib.sha256(data).hexdigest())

    def collect(self, carriers=None):
        return subjects.collect_subject_model_sources(self.repository, self.carriers if carriers is None else carriers)

    def test_full_paths_roles_and_exact_property_byte_spans(self) -> None:
        collection = self.collect()
        result = collection.as_dict()
        self.assertEqual([("Artifact", "DEPENDS_ON"), ("Artifact", "GOVERNS"), ("Atom/Claim", "GOVERNS"),
                          ("Atom/Status: Active", "DEPENDS_ON")],
                         [(row["subject_path"], row["role"]) for row in result["occurrences"]])
        self.assertEqual("complete", result["coverage"]["disposition"])
        self.assertEqual((2, 2, 0, 4), tuple(result["coverage"][key] for key in
                                          ("source_count", "resolved_source_count", "unresolved_source_count", "occurrence_count")))
        self.assertEqual([], result["diagnostics"])
        self.assertNotIn("admitted_facts", result)
        self.assertNotIn("native_membership", result)
        self.assertIn("main_content_conformance", result["unperformed"])
        self.assertIn("target_resolution", result["unperformed"])
        for row in result["occurrences"]:
            ref = row["source_ref"]
            location = ref["contribution"]
            raw = (self.repository / ref["carrier_path"]).read_bytes()
            self.assertEqual(hashlib.sha256(raw).hexdigest(), ref["carrier_sha256"])
            self.assertEqual("canonical_atom_property", location["kind"])
            self.assertEqual("subjects.governs" if row["role"] == "GOVERNS" else "subjects.depends_on", location["property_path"])
            span = b"".join(raw.splitlines(keepends=True)[location["start_line"] - 1:location["end_line"]])
            self.assertEqual(hashlib.sha256(span).hexdigest(), location["text_sha256"])
            self.assertIn(row["subject_path"].encode("utf-8"), span)
        body = dict(result)
        digest = body.pop("collection_sha256")
        self.assertEqual(hashlib.sha256(facts.canonical_bytes(body)).hexdigest(), digest)

    def test_absent_dependencies_are_zero_and_empty_selection_has_extraction_coverage(self) -> None:
        carrier = self.changed_carrier("CA-R-9001", atom_text("CA-R-9001", 'subjects:\n  governs: "Object"'))
        result = self.collect([carrier]).as_dict()
        self.assertEqual([("Object", "GOVERNS")], [(row["subject_path"], row["role"]) for row in result["occurrences"]])
        self.assertEqual("complete", result["coverage"]["disposition"])
        self.assertTrue(all(row["source_ref"]["contribution"]["property_path"] != "subjects.depends_on" for row in result["occurrences"]))
        empty = self.collect([]).as_dict()
        self.assertEqual([], empty["source_pins"])
        self.assertEqual([], empty["occurrences"])
        self.assertEqual({"scope": "subject_occurrence_extraction", "disposition": "complete", "source_count": 0,
                          "resolved_source_count": 0, "unresolved_source_count": 0, "occurrence_count": 0}, empty["coverage"])

    def test_inline_and_block_lists_and_explicit_atom_id_target(self) -> None:
        carrier = self.changed_carrier("CA-R-9001", atom_text("CA-R-9001", 'subjects:\n  governs: "Model Object"\n  depends_on: ["CA-R-9001", "Other/Status: Active"]'))
        result = self.collect([carrier]).as_dict()
        self.assertEqual({"Model Object", "CA-R-9001", "Other/Status: Active"}, {row["subject_path"] for row in result["occurrences"]})
        for row in result["occurrences"]:
            ref = row["source_ref"]["contribution"]
            self.assertEqual(ref["start_line"], ref["end_line"])
        self.assertEqual([], result["diagnostics"])

    def test_crlf_property_hashes_retain_original_eol_bytes(self) -> None:
        raw = self.first.read_bytes().replace(b"\n", b"\r\n")
        carrier = self.changed_carrier("CA-R-9001", raw)
        result = self.collect([carrier]).as_dict()
        for row in result["occurrences"]:
            location = row["source_ref"]["contribution"]
            span = b"".join(raw.splitlines(keepends=True)[location["start_line"] - 1:location["end_line"]])
            self.assertTrue(span.endswith(b"\r\n"))
            self.assertEqual(hashlib.sha256(span).hexdigest(), location["text_sha256"])

    def test_malformed_duplicate_and_unassigned_forms_are_isolated(self) -> None:
        blocks = (
            'subjects:\n  governs: "Object"\n  governs: "Other Object"\n  depends_on: []',
            'subjects:\n  governs: "Object"\n  depends_on: []\n  depends_on: []',
            'subjects:\n  governs: "Object"\n  depends_on: ["Parent", "Parent"]',
            'subjects:\n  governs: "Object"\n  depends_on:\n    - "Parent"\n    - "Parent"',
            'subjects:\n  governs: ["Object"]\n  depends_on: []',
            'subjects:\n  governs:\n    - "Object"\n  depends_on: []',
            'subjects:\n  governs: "Object"\n  depends_on: "Parent"',
            'subjects:\n  governs: "Object"\n  depends_on:',
            'subjects:\n  governs: "Object"\n  depends_on: ["Comma, Parent"]',
            'subjects:\n  governs: "Object"\n  depends_on: ["Parent", ]',
            'subjects:\n  governs:\n    continuant: "Object"\n  depends_on: []',
            'subjects:\n  governed_entity: "Object"\n  depends_on: []',
            'subjects:\n  governs: "Object"\n  depends_on:\n    target: "Parent"',
            'subjects:\n  governs: "Object"\n  depends_on: []\n  target_kind: Entity',
            'subjects:\n  governs: {entity: "Object"}\n  depends_on: []',
            'subjects:\n  governs: *alias\n  depends_on: []',
            'subjects:\n  governs: "Escaped \\"Name\\""\n  depends_on: []',
            'subjects:\n  governs: "Object/"\n  depends_on: []',
            'subjects:\n  governs: "Artifact//Atom"\n  depends_on: []',
            'subjects:\n  depends_on: []',
        )
        for block in blocks:
            with self.subTest(block=block):
                bad = self.changed_carrier("CA-R-9001", atom_text("CA-R-9001", block))
                result = self.collect([bad, self.by_id["CA-R-9002"]]).as_dict()
                self.assertEqual(["Artifact"], [row["subject_path"] for row in result["occurrences"]])
                self.assertEqual("incomplete", result["coverage"]["disposition"])
                self.assertEqual((2, 1, 1, 1), tuple(result["coverage"][key] for key in
                                                  ("source_count", "resolved_source_count", "unresolved_source_count", "occurrence_count")))
                self.assertEqual(1, len(result["diagnostics"]))
                self.assertNotIn("Main Content", str(result["diagnostics"]))

    def test_duplicate_top_level_key_is_safe_diagnostic_not_occurrence(self) -> None:
        raw = atom_text("CA-R-9001", 'subjects:\n  governs: "Object"\nsubjects:\n  governs: "Other Object"')
        bad = self.changed_carrier("CA-R-9001", raw)
        result = self.collect([bad, self.by_id["CA-R-9002"]]).as_dict()
        self.assertEqual(1, len(result["occurrences"]))
        self.assertEqual(1, result["coverage"]["unresolved_source_count"])
        self.assertEqual("context-carrier-duplicate", result["diagnostics"][0]["code"])
        self.assertEqual([], result["diagnostics"][0]["source_refs"])
        self.assertEqual(["CA-R-9002"], [pin["atom_id"] for pin in result["source_pins"]])

    def test_malformed_current_carrier_bytes_are_diagnosed_without_forged_pin(self) -> None:
        for raw in (b"not Atom frontmatter\n", b"---\nsubjects:\n  governs: Object\n", b"---\n\xff\n---\n"):
            with self.subTest(raw=raw):
                bad = self.changed_carrier("CA-R-9001", raw)
                result = self.collect([bad, self.by_id["CA-R-9002"]]).as_dict()
                self.assertEqual(["Artifact"], [row["subject_path"] for row in result["occurrences"]])
                self.assertEqual("incomplete", result["coverage"]["disposition"])
                diagnostic = result["diagnostics"][0]
                self.assertEqual("context-carrier-invalid", diagnostic["code"])
                self.assertEqual([], diagnostic["source_refs"])
                self.assertNotIn("atom_id", diagnostic["details"])
                self.assertEqual(hashlib.sha256(raw).hexdigest(), diagnostic["details"]["carrier_sha256"])

    def test_stale_and_forged_pins_descriptors_and_duplicate_inputs_fail_closed(self) -> None:
        with self.assertRaises(ValueError):
            self.collect([row.evidence() for row in self.carriers])
        with self.assertRaises(ValueError):
            self.collect([self.carriers[0], self.carriers[0]])
        with self.assertRaises(subjects.SubjectModelSourceError):
            self.collect([replace(self.by_id["CA-R-9001"], atom_id=[])])
        with self.assertRaises(facts.FactContextError) as failure:
            self.collect([replace(self.by_id["CA-R-9001"], atom_id="CA-R-9999")])
        self.assertEqual("context-carrier-identity", failure.exception.code)
        self.first.write_bytes(self.first.read_bytes() + b"\nchanged after source binding\n")
        with self.assertRaises(facts.FactContextError) as failure:
            self.collect()
        self.assertEqual("context-source-stale", failure.exception.code)

    def test_occurrence_data_is_immutable_detached_and_not_caller_minted(self) -> None:
        collection = self.collect()
        expected = collection.as_dict()
        detached = collection.as_dict()
        detached["occurrences"][0]["source_ref"]["atom_id"] = "caller invented"
        detached["admitted_facts"] = [{"passed": True}]
        self.assertEqual(expected, collection.as_dict())
        with self.assertRaises(TypeError):
            collection.occurrences[0]["source_ref"]["atom_id"] = "caller invented"
        with self.assertRaises(TypeError):
            collection.coverage["disposition"] = "caller invented"
        with self.assertRaises(AttributeError):
            collection.collection_sha256 = "f" * 64
        with self.assertRaises(subjects.SubjectModelSourceError):
            subjects.SubjectModelSources(b"{}")

    def test_carrier_and_dependency_permutation_preserves_roles_and_paths(self) -> None:
        first = self.collect().as_dict()
        self.assertEqual(first, self.collect(list(reversed(self.carriers))).as_dict())
        raw = atom_text("CA-R-9001", 'subjects:\n  governs: "Atom/Claim"\n  depends_on:\n    - "Artifact"\n    - "Atom/Status: Active"')
        changed = self.changed_carrier("CA-R-9001", raw)
        second = self.collect([changed, self.by_id["CA-R-9002"]]).as_dict()
        self.assertEqual([(row["subject_path"], row["role"]) for row in first["occurrences"]],
                         [(row["subject_path"], row["role"]) for row in second["occurrences"]])
        self.assertNotEqual(first["collection_sha256"], second["collection_sha256"])
        self.assertEqual(first["provider"], second["provider"])

    def test_alias_loaded_carrier_class_reads_only_checked_current_bytes(self) -> None:
        module_name = "_alias_graph_for_subject_model_sources"
        spec = importlib.util.spec_from_file_location(module_name, TOOL_DIRECTORY / "generate_entity_graph.py")
        alias = importlib.util.module_from_spec(spec)
        sys.modules[module_name] = alias
        self.addCleanup(sys.modules.pop, module_name, None)
        spec.loader.exec_module(alias)
        alias_carriers, diagnostics = alias.discover_atoms(self.repository, self.folder)
        self.assertEqual([], diagnostics)
        self.assertIsNot(type(alias_carriers[0]), graph.AtomCarrier)
        self.assertEqual(self.collect().as_dict(), self.collect(alias_carriers).as_dict())
        # Caller-provided parsed frontmatter is irrelevant after raw pin checks.
        forged_body = [replace(row, frontmatter='subjects:\n  governs: "Invented"') for row in alias_carriers]
        self.assertEqual(self.collect().as_dict(), self.collect(forged_body).as_dict())

    def test_loaded_implementation_or_parser_drift_is_not_a_new_profile(self) -> None:
        original = Path.read_bytes
        for module_path in (subjects._IMPLEMENTATION_PATH, subjects._PARSER_PATH):
            changed = module_path.read_bytes() + b"\n# changed after load\n"
            with self.subTest(path=module_path), patch.object(Path, "read_bytes", autospec=True,
                    side_effect=lambda path: changed if path == module_path else original(path)):
                with self.assertRaises(subjects.SubjectModelSourceError) as failure:
                    self.collect()
                self.assertEqual("profile-stale", failure.exception.code)


if __name__ == "__main__":
    unittest.main()
