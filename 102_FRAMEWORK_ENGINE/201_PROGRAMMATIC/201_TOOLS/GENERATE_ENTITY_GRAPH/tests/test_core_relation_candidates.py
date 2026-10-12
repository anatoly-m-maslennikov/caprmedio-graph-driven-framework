"""Raw current Core relation candidates are never native facts."""

from __future__ import annotations

import hashlib
import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


TOOL_DIRECTORY = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOL_DIRECTORY))
import core_relation_candidates as candidates  # noqa: E402
import core_relation_registry as registry  # noqa: E402
import generate_entity_graph as graph  # noqa: E402
import graph_fact_context as facts  # noqa: E402

WORKSPACE = TOOL_DIRECTORY.parents[3]
CORE_PATH = registry._CORE_AUTHORITY_PATH
ACTUAL_CORE = WORKSPACE / CORE_PATH
TEST_TEMP_ROOT = Path.cwd() / ".caprmedio_tmp/tests/test_core_relation_candidates"
TEST_TEMP_ROOT.mkdir(parents=True, exist_ok=True)
R1251_SUFFIX = "04_requirement/CA-R-1251-CORE_META_MODEL-CORE-REQUIREMENT--classify-property-as-a-dependent-entity.md"
D258_SUFFIX = "07_delivery/CA-D-258-CORE_META_MODEL-CORE-DELIVERY--classify-file-carrier.md"


class CoreRelationCandidateTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory(dir=TEST_TEMP_ROOT, ignore_cleanup_errors=True)
        self.addCleanup(self.temporary.cleanup)
        self.repository = Path(self.temporary.name) / "repository"
        self.authority = self.repository / CORE_PATH
        self.authority.mkdir(parents=True)
        self.control = self.repository / ".caprmedio_caprmedio"
        (self.control / "caprmedio_project_settings.toml").write_text(
            "[paths]\ncontrol_root = '.caprmedio_caprmedio'\nprojection_root = '.caprmedio_caprmedio/_projection'\n", encoding="utf-8")
        (self.control / "project_structure.toml").write_text(
            "[[scope_units]]\nscope_unit_name = 'CORE_META_MODEL'\nauthority_path = '" + CORE_PATH + "'\nauthority_mode = 'strict'\n", encoding="utf-8")
        for _, _, _, suffix in registry._REQUIRED_AUTHORITIES.values():
            self.copy_source(suffix)
        self.r1251 = self.copy_source(R1251_SUFFIX)
        self.d258 = self.copy_source(D258_SUFFIX)
        self.original = self.r1251.read_text(encoding="utf-8")

    def copy_source(self, suffix: str) -> Path:
        destination = self.authority / suffix
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_bytes((ACTUAL_CORE / suffix).read_bytes())
        return destination

    def inputs(self, ids=None):
        carriers, diagnostics = graph.discover_atoms(self.repository, self.authority)
        self.assertEqual([], diagnostics)
        frontier = graph.source_frontier_for(self.repository, self.authority)
        selection = {"atom_ids": ["CA-D-258", "CA-R-1251"] if ids is None else ids,
                     "scope_unit_names": ["CORE_META_MODEL"]}
        compiled = registry.prepare_core_relation_registry(self.repository, carriers, frontier, selection)
        self.assertEqual((), compiled.diagnostics)
        records = [record for record in compiled.records if record["kind"]["graph_kind"] == "terms"]
        return carriers, selection, records

    def recognize(self, ids=None):
        carriers, selection, records = self.inputs(ids)
        return candidates.recognize_core_term_relations(self.repository, carriers, selection, records)

    def test_actual_primary_plain_and_normative_claims_remain_unresolved_candidates(self) -> None:
        result = self.recognize()
        self.assertEqual({"provider", "candidates", "admission_decisions", "admitted_facts", "diagnostics"}, set(result))
        self.assertEqual({"id", "version", "profile_sha256"}, set(result["provider"]))
        self.assertEqual([], result["admitted_facts"])
        self.assertEqual(2, len(result["candidates"]))
        by_id = {row["source_ref"]["atom_id"]: row for row in result["candidates"]}
        self.assertEqual({"CA-D-258", "CA-R-1251"}, set(by_id))
        self.assertTrue(by_id["CA-D-258"]["recognizer"]["id"].endswith(".plain-assertion"))
        self.assertTrue(by_id["CA-R-1251"]["recognizer"]["id"].endswith(".normative-obligation"))
        self.assertEqual(("Property", "Dependent Entity"),
                         (by_id["CA-R-1251"]["payload"]["source"]["identity"], by_id["CA-R-1251"]["payload"]["target"]["identity"]))
        for row in result["candidates"]:
            self.assertEqual("relation", row["fact_class"])
            payload = row["payload"]
            self.assertEqual({"graph_kind": "terms", "canonical_name": "NARROWER_THAN"}, payload["kind"])
            self.assertEqual("external_reference", payload["representation"])
            self.assertTrue(all(payload[key]["graph_kind"] == "terms" and payload[key]["node_class"] == "Term" for key in ("source", "target")))
            self.assertEqual("primary_content", row["source_ref"]["contribution"]["kind"])
            self.assertEqual("Claim", row["source_ref"]["contribution"]["section"])
            raw = (self.repository / row["source_ref"]["carrier_path"]).read_bytes()
            self.assertEqual(hashlib.sha256(raw).hexdigest(), row["source_ref"]["carrier_sha256"])
            locator = row["source_ref"]["contribution"]
            span = b"".join(raw.splitlines(keepends=True)[locator["start_line"] - 1:locator["end_line"]])
            self.assertEqual(hashlib.sha256(span).hexdigest(), locator["text_sha256"])
            if row["source_ref"]["atom_id"] == "CA-R-1251":
                self.assertIn(b"the Term Property **must** be NARROWER_THAN Dependent Entity.", span)
        by_candidate = {row["candidate_id"]: row for row in result["candidates"]}
        for decision in result["admission_decisions"]:
            self.assertEqual("unresolved", decision["disposition"])
            checks = {row["code"]: row for row in decision["checks"]}
            for code in ("semantic-definition-implication", "endpoint-admission", "acyclicity"):
                self.assertEqual("unresolved", checks[code]["disposition"])
            if by_candidate[decision["candidate_id"]]["recognizer"]["id"].endswith(".normative-obligation"):
                self.assertEqual("unresolved", checks["normative-declaration-implies-model-relation"]["disposition"])
            self.assertIn("CA-R-1435", {ref["atom_id"] for ref in decision["authority_inputs"]})
            self.assertTrue(any(ref["atom_id"] == "CA-R-1435" and ref["contribution"].get("section") == "Details" for ref in decision["authority_inputs"]))
            body = dict(decision)
            digest = body.pop("decision_sha256")
            self.assertEqual(hashlib.sha256(facts.canonical_bytes(body)).hexdigest(), digest)

    def test_case_alias_unsupported_obligation_and_fenced_forms_do_not_recognize(self) -> None:
        original_claim = "the Term Property **must** be NARROWER_THAN Dependent Entity."
        variants = (
            "The Term Property NARROWER_THAN Dependent Entity.",
            "the term Property NARROWER_THAN Dependent Entity.",
            "the Term Property narrower_than Dependent Entity.",
            "the Term Property must be NARROWER_THAN Dependent Entity.",
            "the Term Property **must** be **NARROWER_THAN** Dependent Entity.",
            "the Term Property **must not** be NARROWER_THAN Dependent Entity.",
            "the Term Property SUBKIND_OF Dependent Entity.",
            "```markdown\nthe Term Property NARROWER_THAN Dependent Entity.\n```",
            "> the Term Property NARROWER_THAN Dependent Entity.",
            "the Term Property NARROWER_THAN Dependent Entity.\n\nAnother contribution.",
        )
        for claim in variants:
            with self.subTest(claim=claim):
                self.r1251.write_text(self.original.replace(original_claim, claim), encoding="utf-8")
                result = self.recognize(["CA-R-1251"])
                self.assertEqual([], result["candidates"])
                self.assertEqual([], result["admitted_facts"])

    def test_exact_raw_subject_matches_required_without_legacy_aliases(self) -> None:
        variants = (
            self.original.replace('governs: "Property"', 'governs: "Other Property"'),
            self.original.replace('- "Dependent Entity"', '- "Primary Entity"'),
            self.original.replace('governs: "Property"', 'governed_entity: "Property"'),
            self.original.replace('depends_on:', 'dependent_entities:'),
            self.original.replace('- "Dependent Entity"', '- "First/Dependent Entity"\n    - "Second/Dependent Entity"'),
        )
        for raw in variants:
            with self.subTest(raw=raw):
                self.r1251.write_text(raw, encoding="utf-8")
                result = self.recognize(["CA-R-1251"])
                self.assertEqual([], result["candidates"])
                self.assertEqual([], result["admitted_facts"])

    def test_qualified_subject_terminal_matching_is_source_only(self) -> None:
        self.r1251.write_text(self.original.replace('governs: "Property"', 'governs: "Atom/Property"')
                             .replace('- "Dependent Entity"', '- "Entity/Type: Dependent Entity"'), encoding="utf-8")
        result = self.recognize(["CA-R-1251"])
        self.assertEqual(1, len(result["candidates"]))
        self.assertEqual([], result["admitted_facts"])
        decision = result["admission_decisions"][0]
        check = next(row for row in decision["checks"] if row["code"] == "source-subject-terminal-matches")
        self.assertEqual("pass", check["disposition"])
        self.assertEqual({"subjects.governs", "subjects.depends_on"}, {ref["contribution"]["property_path"] for ref in check["source_refs"]})
        self.assertEqual("unresolved", next(row for row in decision["checks"] if row["code"] == "endpoint-admission")["disposition"])

    def test_one_ambiguous_source_does_not_erase_another_candidate(self) -> None:
        for raw in (
            self.original.replace("## Details", "## Claim\n\nA second primary contribution.\n\n## Details"),
            self.original.replace('governs: "Property"', 'governs: "Property"\n  governs: "Other Property"'),
        ):
            with self.subTest(raw=raw):
                self.r1251.write_text(raw, encoding="utf-8")
                result = self.recognize()
                self.assertEqual(["CA-D-258"], [row["source_ref"]["atom_id"] for row in result["candidates"]])
                self.assertEqual([], result["admitted_facts"])
                self.assertTrue(any(row["code"].endswith("unresolved") for row in result["diagnostics"]))

    def test_no_subject_slash_inverse_property_or_other_relation_inference(self) -> None:
        original_claim = "the Term Property **must** be NARROWER_THAN Dependent Entity."
        for claim in (
            "Property is independently described here.",
            "the Term Property BEARS Dependent Entity.",
            "the Term Property IS_BORNE_BY Dependent Entity.",
            "the Term Property IS_ALLOWED_VALUE_OF Dependent Entity.",
            "the Term Property GOVERNS Dependent Entity.",
        ):
            with self.subTest(claim=claim):
                self.r1251.write_text(self.original.replace(original_claim, claim).replace('governs: "Property"', 'governs: "Atom/Property"'), encoding="utf-8")
                result = self.recognize(["CA-R-1251"])
                self.assertEqual([], result["candidates"])
                self.assertEqual([], result["admitted_facts"])
        result = self.recognize(["CA-D-258"])
        self.assertEqual(1, len(result["candidates"]))
        self.assertEqual({"NARROWER_THAN"}, {row["payload"]["kind"]["canonical_name"] for row in result["candidates"]})
        self.assertEqual([], result["admitted_facts"])

    def test_registry_currentness_and_forged_records_fail_closed(self) -> None:
        carriers, selection, records = self.inputs()
        for wrong in ({"pass": True}, [], [records[0], records[0]], [{**records[0], "passed": True}]):
            with self.subTest(record=wrong):
                with self.assertRaises(ValueError):
                    candidates.recognize_core_term_relations(self.repository, carriers, selection, wrong)
        forged = {**records[0], "metadata": {**records[0]["metadata"], "direction": "broader_to_narrower"}}
        unsigned = dict(forged)
        unsigned.pop("registry_record_sha256")
        forged["registry_record_sha256"] = hashlib.sha256(facts.canonical_bytes(unsigned)).hexdigest()
        with self.assertRaises(candidates.CoreRelationCandidateError):
            candidates.recognize_core_term_relations(self.repository, carriers, selection, [forged])
        self.r1251.write_bytes(self.r1251.read_bytes() + b"\nchanged after binding\n")
        with self.assertRaises(ValueError):
            candidates.recognize_core_term_relations(self.repository, carriers, selection, records)

    def test_loaded_code_drift_does_not_claim_a_fresh_execution_profile(self) -> None:
        carriers, selection, records = self.inputs()
        original_read = Path.read_bytes
        for source_path in (candidates._IMPLEMENTATION_PATH, candidates._HIERARCHY_PATH):
            changed = source_path.read_bytes() + b"\n# changed after load\n"
            with self.subTest(path=source_path), patch.object(Path, "read_bytes", autospec=True,
                    side_effect=lambda path: changed if path == source_path else original_read(path)):
                with self.assertRaises(candidates.CoreRelationCandidateError) as failure:
                    candidates.recognize_core_term_relations(self.repository, carriers, selection, records)
                self.assertEqual("profile-stale", failure.exception.code)

    def test_registry_reconstruction_once_and_deterministic_detached_bundle(self) -> None:
        carriers, selection, records = self.inputs()
        with patch.object(registry, "prepare_core_relation_registry", wraps=registry.prepare_core_relation_registry) as prepare:
            first = candidates.recognize_core_term_relations(self.repository, carriers, selection, records)
            self.assertEqual(1, prepare.call_count)
        second = candidates.recognize_core_term_relations(self.repository, carriers, selection, records)
        self.assertEqual(first, second)
        first["candidates"][0]["payload"]["source"]["identity"] = "caller mutation"
        self.assertNotEqual(first, second)
        self.assertEqual(second, candidates.recognize_core_term_relations(self.repository, carriers, selection, records))

    def test_unselected_source_unknown_selection_and_descriptor_carriers(self) -> None:
        carriers, selection, records = self.inputs(["CA-R-1251"])
        result = candidates.recognize_core_term_relations(self.repository, carriers, selection, records)
        self.assertEqual(["CA-R-1251"], [row["source_ref"]["atom_id"] for row in result["candidates"]])
        with self.assertRaises(ValueError):
            candidates.recognize_core_term_relations(self.repository, carriers, {"atom_ids": ["CA-R-999999"], "scope_unit_names": ["CORE_META_MODEL"]}, records)
        with self.assertRaises(ValueError):
            candidates.recognize_core_term_relations(self.repository, [carrier.evidence() for carrier in carriers], selection, records)

    def test_alias_loaded_atom_carriers_use_checked_bytes_not_class_identity(self) -> None:
        carriers, selection, records = self.inputs()
        module_name = "_alias_graph_for_core_relation_candidates"
        spec = importlib.util.spec_from_file_location(module_name, TOOL_DIRECTORY / "generate_entity_graph.py")
        self.assertIsNotNone(spec)
        self.assertIsNotNone(spec.loader)
        alias_graph = importlib.util.module_from_spec(spec)
        sys.modules[module_name] = alias_graph
        self.addCleanup(sys.modules.pop, module_name, None)
        spec.loader.exec_module(alias_graph)
        alias_carriers, diagnostics = alias_graph.discover_atoms(self.repository, self.authority)
        self.assertEqual([], diagnostics)
        self.assertIsNot(type(alias_carriers[0]), graph.AtomCarrier)
        expected = candidates.recognize_core_term_relations(self.repository, carriers, selection, records)
        actual = candidates.recognize_core_term_relations(self.repository, alias_carriers, selection, records)
        self.assertEqual(expected, actual)
        self.assertEqual(2, len(actual["candidates"]))
        self.assertEqual([], actual["admitted_facts"])
        with self.assertRaises(ValueError):
            candidates.recognize_core_term_relations(self.repository, [row.evidence() for row in alias_carriers], selection, records)


if __name__ == "__main__":
    unittest.main()
