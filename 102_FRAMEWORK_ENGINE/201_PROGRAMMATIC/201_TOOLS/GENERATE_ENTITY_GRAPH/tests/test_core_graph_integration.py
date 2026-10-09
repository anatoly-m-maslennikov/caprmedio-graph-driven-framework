"""Core declaration admission through the strict builder, not live MCP proof."""
from __future__ import annotations

import hashlib
import sys
import unittest
from pathlib import Path

TEST_DIRECTORY = Path(__file__).resolve().parent
if str(TEST_DIRECTORY) not in sys.path:
    sys.path.insert(0, str(TEST_DIRECTORY))
import test_core_term_admission as term_fixture
import test_core_relation_candidates as relation_fixture
import graph_fact_context
graph = term_fixture.graph
requirement = term_fixture.requirement


class CoreGraphIntegrationTests(unittest.TestCase):
    def setUp(self) -> None:
        self.fixture = term_fixture.CoreTermAdmissionTests()
        self.fixture.setUp()
        self.addCleanup(self.fixture.tearDown)

    def request(self, **extra):
        _, frontier, selection = self.fixture.inputs()
        return {"graph_kind": "terms", "source_frontier": frontier, "selection": selection,
                "representation_configuration": {"format": "canonical-json"},
                "capability_permission_evidence": {"authorized": True}, **extra}

    def test_native_definition_keeps_declared_context_and_scope_lineage(self) -> None:
        result = graph.build_graph(self.fixture.repository, self.request())
        self.assertEqual("incomplete", result["outcome"])
        namespace = result["terms_graph"]
        self.assertEqual({"kind": "declared_core_model", "scope_unit": "CORE_META_MODEL"},
                         namespace["declaration_context"])
        self.assertEqual(["Entity"], [row["payload"]["term_identity"] for row in namespace["terms"]])
        self.assertEqual([], namespace["root_terms"])
        decision = next(row for row in result["lineage"]["admission_decisions"]
                        if row["disposition"] == "admitted")
        self.assertIn("Scope", {ref["contribution"].get("section") for ref in decision["authority_inputs"]})
        self.assertEqual("construction_only", result["completion"]["state"])
        self.assertEqual("none", result["output_effects"]["state"])

    def test_project_extension_is_not_part_of_declared_core_cardinality(self) -> None:
        outsider = self.fixture.repository / ".caprmedio_caprmedio/extensions/CA-R-901.md"
        outsider.parent.mkdir(parents=True)
        outsider.write_text(requirement("CA-R-901"), encoding="utf-8")
        result = graph.build_graph(self.fixture.repository, self.request())
        self.assertEqual(["Entity"], [row["payload"]["term_identity"] for row in result["terms_graph"]["terms"]])
        self.assertNotIn("CA-R-901", {row["source"]["atom_id"] for row in result["terms_graph"]["source_atoms"]})

    def test_context_digest_and_native_fact_links_are_deterministic(self) -> None:
        carriers, frontier, selection = self.fixture.inputs()
        first = graph_fact_context.prepare_fact_context(self.fixture.repository, "terms", carriers,
                                                       selection, frontier, carriers).as_dict()
        second = graph_fact_context.prepare_fact_context(self.fixture.repository, "terms", carriers,
                                                        selection, frontier, carriers).as_dict()
        self.assertEqual(first, second)
        digest = first.pop("context_sha256")
        self.assertEqual(digest, hashlib.sha256(graph_fact_context.canonical_bytes(first)).hexdigest())
        decisions = {row["candidate_id"]: row for row in first["admission_decisions"]}
        for fact in first["admitted_facts"]:
            self.assertEqual("admitted", decisions[fact["candidate_id"]]["disposition"])
            self.assertEqual(decisions[fact["candidate_id"]]["decision_sha256"], fact["decision_sha256"])

    def test_display_cannot_admit_a_new_native_identity(self) -> None:
        result = graph.build_graph(self.fixture.repository, self.request(
            display_selection={"mode": "explicit_native_identity_set", "native_identities": ["Not admitted"]}))
        self.assertEqual("failed", result["outcome"])
        self.assertEqual("display-selection-outside-source", result["diagnostics"][0]["code"])

    def relation_inputs(self, graph_kind="terms", atom_ids=None):
        fixture = relation_fixture.CoreRelationCandidateTests()
        fixture.setUp()
        self.addCleanup(fixture.doCleanups)
        carriers, selection, _ = fixture.inputs(atom_ids)
        frontier = graph.source_frontier_for(fixture.repository, fixture.authority)
        context = graph_fact_context.prepare_fact_context(fixture.repository, graph_kind, carriers,
                                                         selection, frontier, carriers).as_dict()
        return fixture, selection, frontier, context

    def test_relation_candidates_do_not_become_native_edges_or_roots(self) -> None:
        fixture, selection, frontier, context = self.relation_inputs()
        attempts = [row for row in context["candidates"] if row["fact_class"] == "relation"]
        self.assertEqual(2, len(attempts))
        self.assertEqual({"CA-D-258", "CA-R-1251"}, {row["source_ref"]["atom_id"] for row in attempts})
        self.assertEqual([], context["admitted_facts"])
        self.assertEqual([], context["derivations"])
        coverage = next(row for row in context["coverage"] if row["fact_class"] == "relation")
        self.assertEqual(("unknown", "unknown", 2, 0),
                         tuple(coverage[key] for key in ("disposition", "selected_result", "candidate_count", "admitted_count")))
        request = {"graph_kind": "terms", "source_frontier": frontier, "selection": selection,
                   "representation_configuration": {"format": "canonical-json"},
                   "capability_permission_evidence": {"authorized": True}}
        result = graph.build_graph(fixture.repository, request)
        self.assertEqual("incomplete", result["outcome"])
        self.assertEqual([], result["terms_graph"]["native_relations"])
        self.assertEqual([], result["terms_graph"]["root_terms"])
        self.assertEqual("none", result["output_effects"]["state"])

    def test_registry_alone_does_not_materialize_terms_or_transitive_relations(self) -> None:
        _, _, _, context = self.relation_inputs(atom_ids=[])
        self.assertEqual(["NARROWER_THAN"], [row["kind"]["canonical_name"] for row in context["relation_registry"]])
        self.assertEqual([], context["candidates"])
        self.assertEqual([], context["admitted_facts"])
        self.assertEqual([], context["derivations"])
        self.assertTrue(all(row["disposition"] == "unknown" for row in context["coverage"]))

    def test_entity_registry_does_not_assign_properties_or_materialize_bears(self) -> None:
        _, _, _, context = self.relation_inputs(graph_kind="entities")
        self.assertEqual({"IS_BORNE_BY", "IS_ALLOWED_VALUE_OF"},
                         {row["kind"]["canonical_name"] for row in context["relation_registry"]})
        self.assertEqual([], context["admitted_facts"])
        self.assertEqual([], context["derivations"])
        self.assertFalse(any(row["fact_class"] == "entity_property" for row in context["candidates"]))
        self.assertTrue(all(row["admitted_count"] == 0 for row in context["coverage"]))


if __name__ == "__main__":
    unittest.main()
