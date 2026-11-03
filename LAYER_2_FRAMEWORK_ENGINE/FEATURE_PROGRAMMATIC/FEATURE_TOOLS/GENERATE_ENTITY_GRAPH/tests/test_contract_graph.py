"""Formal-contract graph preserves complete, source-bound Claim evidence."""

from pathlib import Path
import sys
import unittest


TOOL = Path(__file__).resolve().parents[1]
sys.path[:0] = [str(TOOL.parent), str(TOOL)]

from contract_graph import compose_contract_graph, render_contract_graph  # noqa: E402
from cfel_claim_constraints import extract_claim_constraints  # noqa: E402


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
    def test_qualified_declared_by_derivation_is_not_an_unconditional_inverse(self):
        graph = compose_contract_graph([carrier("CA-R-1", "CFEL <+ Relation//IS_DECLARED_BY", body(
            "### Formal Claim", "```CFEL", "# model",
            "Relation//IS_DECLARED_BY ((IS_DERIVED_RELATION_OF)) Relation//GOVERNS;", "```",
            "### Prose Claim", "Only governing links satisfying the Declaration ownership rule."))])
        relation = graph["relations"][0]
        self.assertEqual(["GOVERNS"], [row["name"] for row in relation["derivation_links"]])
        self.assertEqual([], relation["inverses"])
        self.assertNotIn("derived_view", relation)
        self.assertIn("not structurally interpreted", relation["derivation_scope"])

    def test_instance_group_does_not_supply_relation_classification_or_alias(self):
        graph = compose_contract_graph([carrier("CA-R-1", "CFEL <+ Relation//TEST", body(
            "### Formal Claim", "```CFEL", "# instances",
            "Relation//TEST ((HAS_CLASSIFICATION)) Derivation == Direct;",
            'alias(Relation//TEST) == "/";', "```"))])
        relation = graph["relations"][0]
        self.assertEqual([], relation["metadata"])
        self.assertEqual(2, len(relation["own"][0]["instance_clauses"]))

    def test_grouped_formal_claims_keep_instance_variables_out_of_model_contracts(self):
        graph = compose_contract_graph([
            carrier("CA-R-1", "Atom", body("Atom.")),
            carrier("CA-R-2", "Atom.Header.Name", body(
                "### Formal Claim", "```CFEL", "# model",
                "Atom.Header.Name: [string]{:1};", 'alias(Relation//CONTAINS) == "# instances";',
                "# a full-line comment", "# instances", "Atom//$atom;", "$atom.Header.Name: [string]{:1};", "```")),
        ])
        row = next(row for row in graph["entities"] if row["target"] == "Atom.Header.Name")
        entry = row["own"][0]
        self.assertEqual(["model", "model"], [x["group"] for x in entry["clauses"]])
        self.assertEqual(["instance_binding", "property_constraint"], [x["kind"] for x in entry["instance_clauses"]])
        self.assertEqual("$atom.Header.Name", entry["instance_clauses"][1]["property_selector"])
        self.assertEqual("# instances", entry["clauses"][1]["glyph"])
        self.assertEqual([], entry["diagnostics"])
        self.assertIn("# instances", entry["cfel_blocks"][0]["block"])
        self.assertFalse(any("$atom" in x["target"] for x in graph["entities"]))
        self.assertIn("Instance constraints:", render_contract_graph(graph))

    def test_minimal_inverse_uses_corroborated_direct_meaning_and_reversed_endpoint_view(self):
        direct = carrier("CA-R-1", "CFEL <+ Relation//DIRECT", body(
            "### Formal Claim", "```CFEL", "$left ((DIRECT)) $right;",
            "Relation//DIRECT ((HAS_INVERSE)) Relation//INVERSE;",
            "Relation//DIRECT ((HAS_CLASSIFICATION)) Derivation == Direct", "```",
            "### Prose Claim", "Direct meaning."))
        inverse = carrier("CA-R-2", "CFEL <+ Relation//INVERSE", body(
            "### Formal Claim", "```CFEL", "Relation//INVERSE <((HAS_INVERSE)) Relation//DIRECT", "```"))
        graph = compose_contract_graph([direct, inverse])
        row = next(row for row in graph["relations"] if row["target"] == "INVERSE")
        self.assertEqual("Derived", row["derived_view"]["classification"])
        self.assertEqual("Direct meaning.", row["derived_view"]["meaning"])
        self.assertEqual([{"host": "$right", "target": "$left"}], row["derived_view"]["endpoints"])
        self.assertEqual([], row["host_target"])
        self.assertEqual(0, graph["coverage"]["missing_relation_semantics"])
        self.assertIn("not new permissions", render_contract_graph(graph))

        missing = compose_contract_graph([inverse])
        self.assertEqual(1, missing["coverage"]["missing_relation_semantics"])
        self.assertNotIn("derived_view", missing["relations"][0])
        conflicting = carrier("CA-R-3", "CFEL <+ Relation//OTHER", body(
            "### Formal Claim", "```CFEL", "Relation//OTHER ((HAS_INVERSE)) Relation//INVERSE;",
            "Relation//OTHER ((HAS_CLASSIFICATION)) Derivation == Direct", "```",
            "### Prose Claim", "Other meaning."))
        ambiguous = compose_contract_graph([direct, inverse, conflicting])
        inverse_row = next(row for row in ambiguous["relations"] if row["target"] == "INVERSE")
        self.assertNotIn("derived_view", inverse_row)

    def test_relation_bounds_and_quoted_counterpart_alias_remain_distinct(self):
        clauses, diagnostics = extract_claim_constraints(carrier("CA-R-1", "Node", body(
            "```CFEL", 'alias(HAS_INVERSE) == "<-->";',
            "Node{:1}((REL)){:2}Node;", "Node:{:1}((REL)){:2}Node;", "```")))
        alias = next(row for row in clauses if row["kind"] == "relation_alias")
        relation = next(row for row in clauses if row["kind"] == "relation_cardinality")
        self.assertEqual("<-->", alias["glyph"])
        self.assertEqual({"minimum": 2, "maximum": 2}, relation["target_cardinality"])
        self.assertEqual(1, len(diagnostics))

    def test_explicit_namespace_header_qualifications_bind_declared_properties(self):
        graph = compose_contract_graph([
            carrier("CA-R-1", "CAPRMEDIO_MODEL <+ Atom", body("Atom.")),
            carrier("CA-R-2", "CAPRMEDIO_MODEL <+ Atom.Header", body("Header.")),
            carrier("CA-R-3", "CAPRMEDIO_MODEL <+ Atom.Header.Role", body("Role.")),
            carrier("CA-R-4", "CAPRMEDIO_MODEL <+ Atom.Header.Form", body("Form.")),
            carrier("CA-R-5", "CAPRMEDIO_MODEL <+ Atom/(.Header.Role:=Requirement)", body("Role rule."), form="Rule"),
            carrier("CA-R-6", "CAPRMEDIO_MODEL <+ Atom/(.Header.Form:=Declaration)", body("Form rule."), form="Rule"),
            carrier("CA-R-7", "CAPRMEDIO_MODEL <+ (Node, Node.**)", body("Scope."), form="Rule"),
            carrier("CA-R-8", "CAPRMEDIO_MODEL <+ Node", body("Node.")),
            carrier("CA-R-9", "CAPRMEDIO_MODEL <+ Atom/(.Header.Role:=Requirement)/(.Header.Form:=Declaration)", body("Combined rule."), form="Rule"),
            carrier("CA-R-10", "CAPRMEDIO_MODEL <+ Atom/(.Header.Role: Method)/(.Header.Form: Declaration)", body("Combined colon rule."), form="Rule"),
            carrier("CA-R-11", "CAPRMEDIO_MODEL <+ Atom.Content.Claim", body("Claim.")),
            carrier("CA-R-12", "CAPRMEDIO_MODEL <+ Atom/(.Header.Role: Delivery).Content.Claim", body("Claim rule."), form="Rule"),
        ])
        rows = {row["target"]: row for row in graph["entities"]}
        self.assertEqual({"Atom", "Atom.Header", "Atom.Header.Role", "Atom.Header.Form", "Atom.Content.Claim", "Node"}, set(rows))
        self.assertEqual({"Atom.Header.Role", "Atom.Header.Form"},
                         {row["binding_context"]["property"] for row in rows["Atom"]["shared"] if "property" in row["binding_context"]})
        combined = next(row for row in rows["Atom"]["shared"] if row["source"]["atom_id"] == "CA-R-9")
        self.assertEqual(["Atom.Header.Role", "Atom.Header.Form"], combined["binding_context"]["properties"])
        self.assertEqual("CA-R-12", rows["Atom.Content.Claim"]["shared"][0]["source"]["atom_id"])
        self.assertEqual([], rows["Node"]["shared"])
        self.assertIn("complex selection scope", graph["coverage_gaps"][0]["message"])

    def test_named_claim_children_keep_prose_markdown_and_only_extract_formal_cfel(self):
        graph = compose_contract_graph([
            carrier("CA-R-1", "Atom", """## Claim

### Formal Claim

```CFEL
Atom.Header: [YAML]{:1};
```

### Prose Claim

#### Context

Prose with an example:

```CFEL
Atom.Example: [wrong]{:1};
```
"""),
        ])
        entry = graph["entities"][0]["own"][0]
        self.assertEqual(["Atom.Header"], [row["property_selector"] for row in entry["clauses"]])
        self.assertIn("#### Context", entry["prose"])
        self.assertIn("Atom.Example", entry["prose"])
        self.assertEqual(1, len(entry["cfel_blocks"]))

    def test_prose_only_claim_does_not_interpret_cfel_examples(self):
        graph = compose_contract_graph([
            carrier("CA-R-1", "Atom", """## Claim

### Prose Claim

```CFEL
Atom.Example: [wrong]{:1};
```
"""),
        ])
        entry = graph["entities"][0]["own"][0]
        self.assertEqual([], entry["clauses"])
        self.assertEqual([], entry["cfel_blocks"])
        self.assertEqual([], entry["diagnostics"])
        self.assertIn("Atom.Example", entry["prose"])

    def test_prose_claim_keeps_unrecognized_headings_at_any_level(self):
        graph = compose_contract_graph([carrier("CA-R-1", "Atom", """## Claim
### Prose Claim
Opening.
### Sibling Title
Sibling text.
## Dependent Selection
More text.
```CFEL
Atom.Example: [wrong]{:1};
```
## Expression Lists
Last text.
## Details
Actual root detail.
""")])
        entry = graph["entities"][0]["own"][0]
        self.assertIn("### Sibling Title\nSibling text.", entry["prose"])
        self.assertIn("## Dependent Selection\nMore text.", entry["prose"])
        self.assertIn("Atom.Example", entry["prose"])
        self.assertIn("## Expression Lists\nLast text.", entry["prose"])
        self.assertNotIn("Actual root detail", entry["prose"])
        self.assertEqual([], entry["diagnostics"])
        self.assertEqual([], entry["clauses"])

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
            carrier("CA-R-11", "CAPRMEDIO <+ MODEL <+ PROJECT STRUCTURE", body("Structure kind declaration.")),
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
            carrier("CA-R-14", "CAPRMEDIO <+ STRUCTURE", body("Structure context."),
                    form="Rule"),
            carrier("CA-R-15", "Named Selection//Unknown", body("Unknown selection context."),
                    form="Rule"),
            carrier("CA-R-16", "PROJECT STRUCTURE//CAPRMEDIO", body("Historical structure context."),
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
        self.assertEqual(2, graph["coverage"]["outside_model_scope_sources"])
        self.assertEqual(
            {"CA-R-7", "CA-R-15"},
            {row["source"]["atom_id"] for row in graph["coverage_gaps"]},
        )
        self.assertEqual(
            {"CA-R-8", "CA-R-14"},
            {row["source"]["atom_id"] for row in graph["outside_model_scope"]},
        )

    def test_binds_prefixed_namespaces_to_local_targets_without_losing_subject_provenance(self):
        graph = compose_contract_graph([
            carrier("CA-R-1", "CAPRMEDIO <+ MODEL <+ Node", body("Node declaration.")),
            carrier("CA-R-2", "CAPRMEDIO <+ MODEL <+ Node.Status", body("Status declaration.")),
            carrier("CA-R-3", "CAPRMEDIO <+ MODEL <+ Node//Example", body("Example declaration.")),
            carrier("CA-R-4", "CAPRMEDIO <+ MODEL <+ CFEL <+ Format", body("Format declaration.")),
            carrier("CA-R-5", "CAPRMEDIO <+ MODEL <+ CFEL <+ Relation//depends_on",
                    body("Relation declaration."), form="Relation Definition"),
            carrier("CA-R-6", "CAPRMEDIO <+ STRUCTURE <+ Project", body("Project declaration.")),
            carrier("CA-R-7", "CAPRMEDIO <+ STRUCTURE <+ Project//caprmedio",
                    body("Project declaration context."), form="Scope Unit Declaration"),
            carrier("CA-R-8", "CAPRMEDIO <+ MODEL <+ Node", body("Node rule."), form="Rule"),
            carrier("CA-R-9", "CAPRMEDIO <+ MODEL <+ CFEL <+ Relation//depends_on",
                    body("Relation rule."), form="Rule"),
            carrier("CA-R-10", "CAPRMEDIO <+ STRUCTURE <+ Project//caprmedio",
                    body("Project rule."), form="Rule"),
            carrier("CA-R-11", "CAPRMEDIO <+ MODEL <+ Projection", body("Projection declaration.")),
            carrier("CA-R-12", "CAPRMEDIO <+ MODEL <+ Named Selection", body("Selection declaration.")),
            carrier("CA-R-13", "CAPRMEDIO <+ MODEL <+ (Node, Node.**)", body("Node scope."), form="Rule"),
            carrier("CA-R-14", "CAPRMEDIO <+ MODEL <+ (Node, Node.**)", body("Node scope."), form="Rule"),
            carrier("CA-R-15", "CAPRMEDIO <+ STRUCTURE <+ Projection//PROJECT_SCOPE_UNIT_GRAPH",
                    body("Projection context."), form="Rule"),
            carrier("CA-R-16", "CAPRMEDIO <+ STRUCTURE <+ Projection//PROJECT_SCOPE_UNIT_GRAPH",
                    body("Projection context."), form="Rule"),
            carrier("CA-R-17", "CAPRMEDIO <+ STRUCTURE <+ Named Selection//Extension Sources",
                    body("Selection context."), form="Rule"),
        ])

        entities = {row["target"]: row for row in graph["entities"]}
        components = {row["target"]: row for row in graph["components"]}
        relations = {row["target"]: row for row in graph["relations"]}
        self.assertEqual("exact", entities["Node"]["shared"][0]["binding"])
        self.assertEqual("CAPRMEDIO <+ MODEL <+ Node", entities["Node"]["shared"][0]["subject"])
        self.assertEqual("property", entities["Node.Status"]["kind"])
        self.assertEqual("instance", entities["Node//Example"]["kind"])
        self.assertEqual("component", components["Format"]["kind"])
        self.assertEqual("Project", entities["Project"]["shared"][0]["target"])
        self.assertEqual("scope_unit_declaration_context", entities["Project"]["shared"][0]["binding"])
        self.assertEqual("depends_on", relations["depends_on"]["target"])
        self.assertEqual("CAPRMEDIO <+ MODEL <+ CFEL <+ Relation//depends_on",
                         relations["depends_on"]["shared"][0]["subject"])
        self.assertEqual(1, len(entities["Node"]["shared"]))
        self.assertEqual(2, len(entities["Projection"]["shared"]))
        self.assertEqual("known_instance_context", entities["Projection"]["shared"][0]["binding"])
        self.assertEqual("known_instance_context", entities["Named Selection"]["shared"][0]["binding"])
        self.assertEqual(2, graph["coverage"]["coverage_gaps"])

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
        self.assertIn("Derivation interpretation gap", rendered)
        self.assertNotIn("((is_depended_on)) — declared Relation", rendered)

    def test_typed_relation_alias_and_inverse_are_source_bound_in_either_direction(self):
        def read(binding):
            return compose_contract_graph([
                carrier("CA-R-1", "CFEL <+ Relation//NARROWER_THAN", body(
                    "### Formal Claim", "```CFEL",
                    'alias(Relation//NARROWER_THAN) == "/";',
                    binding,
                    "Node ((NARROWER_THAN)) Node;", "```")),
            ])["relations"][0]

        forward = read("Relation//NARROWER_THAN ((HAS_INVERSE)) Relation//BROADER_THAN;")
        reverse = read("Relation//BROADER_THAN <((HAS_INVERSE)) Relation//NARROWER_THAN;")
        glyph = read("Relation//NARROWER_THAN <--> Relation//BROADER_THAN;")
        self.assertEqual(["BROADER_THAN"], [row["name"] for row in forward["inverses"]])
        self.assertEqual(forward["inverses"], reverse["inverses"])
        self.assertEqual(forward["inverses"], glyph["inverses"])
        self.assertEqual(["/"], [row["value"] for row in forward["metadata"]])
        self.assertEqual(["Node"], [row["source_selector"] for row in forward["host_target"]])
        self.assertEqual(1, len(forward["host_target"]))

        graph = compose_contract_graph([carrier("CA-R-2", "CFEL <+ Relation//CONTAINS", body(
            "### Formal Claim", "```CFEL", 'alias(Relation//CONTAINS) == "<+";', "```"))])
        self.assertEqual([], graph["entities"])
        self.assertEqual([], graph["relations"][0]["host_target"])
        self.assertEqual("<+", graph["relations"][0]["metadata"][0]["value"])

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

    def test_renders_blank_outside_scope_prose_lines_without_trailing_whitespace(self):
        graph = compose_contract_graph([
            carrier("CA-R-1", "Node", body("Node declaration.")),
            carrier("CA-R-2", "Unknown", body("First outside line.", "", "Second outside line."), form="Rule"),
        ])

        rendered = render_contract_graph(graph)
        self.assertIn("    First outside line.\n\n    Second outside line.", rendered)
        self.assertFalse(any(line.endswith(" ") for line in rendered.splitlines()))

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

