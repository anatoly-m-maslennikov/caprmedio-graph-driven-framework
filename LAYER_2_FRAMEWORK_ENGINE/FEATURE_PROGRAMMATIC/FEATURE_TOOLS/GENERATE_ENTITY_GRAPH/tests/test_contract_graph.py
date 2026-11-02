"""Formal-contract graph preserves complete, source-bound Claim evidence."""

from pathlib import Path
import sys
import unittest


TOOL = Path(__file__).resolve().parents[1]
sys.path[:0] = [str(TOOL.parent), str(TOOL)]

from contract_graph import compose_contract_graph, render_contract_graph  # noqa: E402


def carrier(atom_id, active, body, *, role="Requirement", form="Declaration"):
    return {
        "source": {"atom_id": atom_id, "version": 1, "path": f"sources/{atom_id}.md"},
        "subjects": {"active": active, "passive": []}, "body": body,
        "read_view": {"content_role": role, "type": form},
    }


def body(*claim_lines, semantics=None):
    result = "## Claim\n\n" + "\n".join(claim_lines) + "\n"
    if semantics is not None:
        result += "\n## Semantics\n\n" + semantics + "\n"
    return result


class ContractGraphTests(unittest.TestCase):
    def test_attaches_exact_shared_rmed_evidence_and_links_transitive_properties_without_copies(self):
        graph = compose_contract_graph([
            carrier("CA-R-1", "Node", body("Node declaration.")),
            carrier("CA-R-2", "Node/Parent", body("Parent declaration.")),
            carrier("CA-R-3", "Node/Parent/Child", body("Child declaration.")),
            carrier("CA-R-4", "Node/Parent.Status", body("```CFEL", "Node/Parent.Status: [string]{:1};", "```")),
            carrier("CA-R-5", "Node/Parent/Child", body("Rule for Child."), form="Rule"),
            carrier("CA-D-6", "Node/Parent/Child", body("Delivery for Child."), role="Delivery", form="Markdown"),
            carrier("CA-R-7", "Node/Unknown", body("```CFEL", "Node/Unknown.Status: [string]{:1};", "```"), form="Rule"),
        ])

        rows = {row["target"]: row for row in graph["entities"]}
        child = rows["Node/Parent/Child"]
        self.assertEqual(["CA-D-6@1", "CA-R-5@1"], child["shared_sources"])
        self.assertEqual(["Node/Parent", "Node"], [row["target"] for row in child["transitive_ancestors"]])
        self.assertEqual(["Node/Parent.Status"], [row["target"] for row in child["inherited_property_declarations"]])
        self.assertNotIn("Node/Parent/Child.Status", rows)
        self.assertEqual(1, graph["coverage"]["coverage_gaps"])
        self.assertIn("Node/Unknown.Status", graph["coverage_gaps"][0]["blocks"][0]["block"])
        rendered = render_contract_graph(graph)
        self.assertLess(rendered.index("## Declared Narrowing Tree"), rendered.index("## Entity and Property Contracts"))
        self.assertIn("Transitive ancestor Declarations", rendered)
        self.assertIn("Inherited Property Declaration refs", rendered)

    def test_keeps_cfel_component_and_semantics_without_inventing_a_node(self):
        graph = compose_contract_graph([
            carrier("CA-R-1", "CFEL <+ Format", body("Format declaration.", semantics="A CFEL component.")),
            carrier("CA-R-2", "CFEL", body("CFEL root declaration.")),
            carrier("CA-R-3", "Operator", body("Operator kind declaration.")),
            carrier("CA-R-4", "Operator//Anatoly", body("Operator instance declaration.")),
        ])

        self.assertEqual(["CFEL", "Format"], [row["target"] for row in graph["components"]])
        self.assertEqual({("Operator", "primary_node"), ("Operator//Anatoly", "instance")},
                         {(row["target"], row["kind"]) for row in graph["entities"]})
        instance = next(row for row in graph["entities"] if row["kind"] == "instance")
        self.assertEqual(["CA-R-3@1"], instance["instance_of"]["effective_source_refs"])
        rendered = render_contract_graph(graph)
        self.assertIn("CFEL, Carrier, and Term Component Contracts", rendered)
        self.assertIn("A CFEL component.", rendered)

    def test_keeps_explicit_cfel_component_properties_and_instances_out_of_narrowing_tree(self):
        graph = compose_contract_graph([
            carrier("CA-R-1", "CFEL", body("CFEL root declaration.")),
            carrier("CA-R-2", "CFEL <+ Format", body("Format declaration.")),
            carrier("CA-R-3", "CFEL <+ Format.Data Type", body("Format Property declaration.")),
            carrier("CA-R-4", "CFEL <+ Format//markdown", body("Markdown format declaration.")),
            carrier("CA-R-5", "CFEL <+ Operator", body("Operator declaration.")),
            carrier("CA-R-6", "CFEL <+ Operator//Addition", body("Addition declaration.")),
        ])

        rows = {row["target"]: row for row in graph["entities"]}
        self.assertEqual("property", rows["Format.Data Type"]["kind"])
        self.assertEqual("instance", rows["Format//markdown"]["kind"])
        self.assertEqual("instance", rows["Operator//Addition"]["kind"])
        self.assertEqual(["CA-R-2@1"], rows["Format//markdown"]["instance_of"]["effective_source_refs"])
        self.assertEqual(
            {"CFEL", "Format", "Operator"},
            {row["identity"] for row in graph["narrowing_tree"]["nodes"]},
        )
        self.assertEqual([], graph["narrowing_tree"]["edges"])
        self.assertFalse(graph["inheritance_diagnostics"])
        self.assertEqual(0, graph["coverage"]["coverage_gaps"])
        self.assertEqual(0, graph["coverage"]["instance_kind_gaps"])

    def test_binds_only_declared_value_and_qualifier_conditions_and_keeps_other_evidence_scoped(self):
        graph = compose_contract_graph([
            carrier("CA-R-1", "Atom", body("Atom declaration.")),
            carrier("CA-R-2", "Atom.Status", body("Status declaration.")),
            carrier("CA-R-3", "Projection", body("Projection declaration.")),
            carrier("CA-R-4", "Projection.Form", body("Form declaration.")),
            carrier("CA-R-5", "Atom.Status:Draft", body("Draft status rule."), form="Rule"),
            carrier("CA-R-6", "Projection/(.Form:=ApplicableMethodology)", body("Projection form rule."), form="Rule"),
            carrier("CA-R-7", "Atom.Kind:Unknown", body("Unknown property rule."), form="Rule"),
            carrier("CA-M-8", "Method/PlanProcess", body("Method evidence."), role="Method", form="Policy"),
        ])

        rows = {row["target"]: row for row in graph["entities"]}
        self.assertEqual("allowed_value_condition", rows["Atom.Status"]["shared"][0]["binding"])
        self.assertEqual("Atom.Status:Draft", rows["Atom.Status"]["shared"][0]["subject"])
        self.assertEqual("property_qualification", rows["Projection"]["shared"][0]["binding"])
        self.assertNotIn("Projection/(.Form:=ApplicableMethodology)", rows)
        self.assertEqual(1, graph["coverage"]["coverage_gaps"])
        self.assertEqual(1, graph["coverage"]["outside_model_scope_sources"])
        self.assertEqual("outside_model_scope", graph["outside_model_scope"][0]["selection_disposition"])

    def test_binds_only_source_proven_scope_unit_declaration_instance_contexts(self):
        graph = compose_contract_graph([
            carrier("CA-R-1", "Scope Unit", body("Scope Unit kind declaration.")),
            carrier("CA-R-2", "Project", body("Project kind declaration.")),
            carrier("CA-R-9", "Projection", body("Projection kind declaration.")),
            carrier("CA-R-10", "Named Selection", body("Selection kind declaration.")),
            carrier("CA-R-11", "PROJECT STRUCTURE", body("Structure kind declaration.")),
            carrier("CA-R-3", "Scope Unit//CORE_META_MODEL", body("Core scope declaration."),
                    form="Scope Unit Declaration"),
            carrier("CA-R-4", "Project//caprmedio", body("Project declaration."),
                    form="Scope Unit Declaration"),
            carrier("CA-R-5", "Scope Unit//CORE_META_MODEL", body("Core scope evidence."),
                    form="Rule"),
            carrier("CA-R-6", "Project//caprmedio", body("Project evidence."), form="Rule"),
            carrier("CA-R-7", "Scope Unit//MISSING", body("Missing scope evidence."), form="Rule"),
            carrier("CA-R-8", "Actor//ANATOLY", body("Unknown kind declaration."),
                    form="Scope Unit Declaration"),
            carrier("CA-R-12", "Projection//PROJECT_SCOPE_UNIT_GRAPH", body("Projection context."),
                    form="Rule"),
            carrier("CA-R-13", "Named Selection//ExtensionSources", body("Selection context."),
                    form="Rule"),
            carrier("CA-R-14", "PROJECT STRUCTURE//CAPRMEDIO", body("Structure context."),
                    form="Rule"),
            carrier("CA-R-15", "Named Selection//Unknown", body("Unknown selection context."),
                    form="Rule"),
        ])

        entities = {row["target"]: row for row in graph["entities"]}
        scope_shared = entities["Scope Unit"]["shared"]
        project_shared = entities["Project"]["shared"]
        projection_shared = entities["Projection"]["shared"]
        selection_shared = entities["Named Selection"]["shared"]
        structure_shared = entities["PROJECT STRUCTURE"]["shared"]
        self.assertEqual(["CA-R-3@1", "CA-R-5@1"], entities["Scope Unit"]["shared_sources"])
        self.assertEqual("scope_unit_declaration_context", scope_shared[0]["binding"])
        self.assertEqual("scope_unit_declaration_context", project_shared[0]["binding"])
        self.assertEqual(
            "current_scope_unit_declaration",
            scope_shared[0]["binding_context"]["existence_provenance"],
        )
        self.assertEqual(
            {"atom_id": "CA-R-3", "version": 1, "path": "sources/CA-R-3.md"},
            scope_shared[1]["binding_context"]["declaration_source"],
        )
        self.assertEqual(
            "CA-R-4", project_shared[1]["binding_context"]["declaration_source"]["atom_id"],
        )
        self.assertEqual("known_instance_context", projection_shared[0]["binding"])
        self.assertEqual("known_instance_context", selection_shared[0]["binding"])
        self.assertEqual("known_instance_context", structure_shared[0]["binding"])
        self.assertEqual(
            "bounded_named_contract_context",
            selection_shared[0]["binding_context"]["existence_provenance"],
        )
        self.assertEqual(
            ["CA-R-1"], [row["source"]["atom_id"] for row in entities["Scope Unit"]["own"]],
        )
        self.assertNotIn("Scope Unit//CORE_META_MODEL", entities)
        self.assertNotIn("Actor//ANATOLY", entities)
        self.assertEqual(2, graph["coverage"]["coverage_gaps"])
        self.assertEqual(1, graph["coverage"]["outside_model_scope_sources"])
        self.assertEqual(
            {"CA-R-7", "CA-R-15"},
            {row["source"]["atom_id"] for row in graph["coverage_gaps"]},
        )
        self.assertEqual("CA-R-8", graph["outside_model_scope"][0]["source"]["atom_id"])

    def test_claim_scope_and_details_are_source_bound_context_before_claim(self):
        graph = compose_contract_graph([
            carrier("CA-R-1", "Atom.Status", body("Status declaration.")),
            carrier("CA-R-2", "Atom.Status:Draft", """## Claim Scope

Only Draft Atom instances.

## Claim

Draft status rule.

## Details

Carrier-specific constraint.
""", form="Rule"),
        ])

        rendered = render_contract_graph(graph)
        rule = rendered[rendered.index("CA-R-2@1"):]
        self.assertLess(rule.index("Claim Scope:"), rule.index("Remaining Claim prose:"))
        self.assertIn("Only Draft Atom instances.", rendered)
        self.assertIn("Details (source-bound):", rendered)
        self.assertIn("Carrier-specific constraint.", rendered)

    def test_preserved_unsupported_cfel_is_partial_extraction_not_a_display_gap(self):
        graph = compose_contract_graph([
            carrier("CA-R-1", "Node", body("```CFEL", "IF Node THEN Property", "```")),
        ])

        self.assertEqual("complete", graph["display_coverage"])
        self.assertEqual("partial", graph["structured_cfel"])
        self.assertEqual("complete", graph["outcome"])
        self.assertIn("IF Node THEN Property", render_contract_graph(graph))

    def test_relation_metadata_is_case_preserving_and_inverse_is_not_another_declaration(self):
        graph = compose_contract_graph([
            carrier(
                "CA-R-1", "CFEL <+ Relation//depends_on",
                body(
                    "```CFEL", "Step// {:1}((depends_on)){:1} Action//;",
                    "((depends_on)) ((HAS_INVERSE)) ((is_depended_on));",
                    "((depends_on)) ((IS_DERIVED_RELATION_OF)) ((is_depended_on));",
                    "((depends_on)) == <<;", "((depends_on)) >| Derivation == Direct;", "```",
                    semantics="Dependency direction.",
                ),
            ),
        ])

        relation = graph["relations"][0]
        self.assertEqual("depends_on", relation["target"])
        self.assertEqual(["is_depended_on"], [row["name"] for row in relation["inverses"]])
        self.assertEqual(["is_depended_on"], [row["name"] for row in relation["derivation_links"]])
        self.assertEqual({"notation", "derivation"}, {row["kind"] for row in relation["metadata"]})
        self.assertEqual(0, graph["coverage"]["missing_relation_semantics"])
        rendered = render_contract_graph(graph)
        self.assertIn("does not certify an undeclared inverse Relation", rendered)
        self.assertNotIn("((is_depended_on)) — declared Relation", rendered)

    def test_preserves_unlabelled_claim_blocks_and_reports_unbound_source(self):
        graph = compose_contract_graph([
            carrier("CA-R-1", "Node", body("Node declaration.")),
            carrier("CA-R-2", "Node/Missing", body("Legacy formal evidence:", "```", "Node/Missing: [string]{:1}", "```"), form="Rule"),
        ])

        gap = graph["coverage_gaps"][0]
        self.assertEqual("", gap["blocks"][0]["label"])
        self.assertIn("Node/Missing", gap["blocks"][0]["block"])
        rendered = render_contract_graph(graph)
        self.assertIn("Unbound source evidence", rendered)
        self.assertIn("```\nNode/Missing", rendered)

    def test_declared_derived_relation_keeps_its_own_metadata(self):
        graph = compose_contract_graph([
            carrier(
                "CA-R-1", "CFEL <+ Relation//is_depended_on",
                body("```CFEL", "((is_depended_on)) >| Derivation == Derived;", "```", semantics="Reverse dependency."),
            ),
        ])

        relation = graph["relations"][0]
        self.assertEqual("is_depended_on", relation["target"])
        self.assertEqual(["Derived"], [row["value"] for row in relation["metadata"]])
        self.assertIn("`((is_depended_on))` — declared Relation", render_contract_graph(graph))

    def test_duplicate_declaration_and_missing_relation_semantics_are_coverage_failures(self):
        graph = compose_contract_graph([
            carrier("CA-R-1", "Node", body("One.")),
            carrier("CA-R-2", "Node", body("Two.")),
            carrier("CA-R-3", "CFEL <+ Relation//RUN", body("```CFEL", "((RUN)) == >>;", "```")),
        ])

        self.assertEqual(1, graph["coverage"]["duplicate_declarations"])
        self.assertEqual(1, graph["coverage"]["missing_relation_semantics"])
        self.assertEqual("incomplete", graph["outcome"])

