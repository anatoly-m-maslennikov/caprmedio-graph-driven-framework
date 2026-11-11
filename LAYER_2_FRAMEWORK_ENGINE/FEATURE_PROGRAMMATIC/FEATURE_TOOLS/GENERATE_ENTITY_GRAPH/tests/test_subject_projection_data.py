"""Subject projection data is declaration-only for detail evidence."""

from pathlib import Path
import sys
import unittest


TOOL = Path(__file__).resolve().parents[1]
sys.path[:0] = [str(TOOL.parent), str(TOOL)]

from subject_projection_data import build_subject_projection_data  # noqa: E402
from subject_projection_views import render_primary_projection  # noqa: E402


def carrier(atom_id, subject, body, *, role="Requirement", form="Declaration"):
    return {
        "source": {"atom_id": atom_id, "version": 1, "path": f"sources/{atom_id}.md"},
        "subjects": {"active": subject, "passive": []}, "body": body,
        "read_view": {"content_role": role, "type": form},
    }


def claim(*lines):
    return "## Claim\n\n" + "\n".join(lines) + "\n"


class SubjectProjectionDataTests(unittest.TestCase):
    def test_encoded_roles_and_forms_keep_declaration_evidence(self):
        body = claim("```CFEL", "Node.Name: [string]{:1};", "```")
        canonical = [carrier("CA-R-1", "Node", claim("Node.")),
                     carrier("CA-R-2", "Node.Name", body)]
        encoded = [carrier("CA-R-1", "Node", claim("Node."), role="requirement", form="declaration"),
                   carrier("CA-R-2", "Node.Name", body, role="requirement", form="declaration")]
        self.assertEqual(build_subject_projection_data(canonical), build_subject_projection_data(encoded))

    def test_inherited_model_format_and_instance_constraints_stay_separate(self):
        data = build_subject_projection_data([
            carrier("CA-R-1", "Node", claim("Node declaration.")),
            carrier("CA-R-2", "Node/Child", claim("Child declaration.")),
            carrier("CA-R-3", "Node.Name", claim("```CFEL", "# model", "Node.Name: [string]{:1};", "# instances", "Node//$n;", "$n.Name: [string]{:1};", "```")),
            carrier("CA-R-4", "Node.Name", claim("```CFEL", "# model", "Node.Name: [integer]{:1};", "```"), form="Rule"),
        ])
        child = next(row for row in data["entities"] if row["identity"] == "Node/Child")
        prop = child["inherited_properties"][0]
        self.assertEqual(["string"], [row["value_format"] for row in prop["contracts"]])
        self.assertEqual(["instance_binding", "property_constraint"], [row["kind"] for row in prop["instance_constraints"]])
        self.assertIn("# model", prop["formal_claims"][0]["block"])
        self.assertIn("# instances", prop["formal_claims"][0]["block"])
        self.assertFalse(any("$n" in row["identity"] for row in data["entities"]))
        inspector = render_primary_projection(data, 4)
        self.assertIn("# model\nNode.Name: [string]{:1};\n# instances\nNode//$n;\n$n.Name: [string]{:1};", inspector)

    def test_keeps_explicit_new_namespace_roots(self):
        data = build_subject_projection_data([
            carrier("CA-R-1", "CAPRMEDIO_MODEL", claim("Model root.")),
            carrier("CA-R-2", "CAPRMEDIO_MODEL <+ Node", claim("Node.")),
            carrier("CA-R-3", "CAPRMEDIO_STRUCTURE <+ Project", claim("Project.")),
        ])
        self.assertEqual(
            [("CAPRMEDIO_MODEL", "CA-R-1"), ("CAPRMEDIO_STRUCTURE", "CA-R-3")],
            [(row["subject"], row["source"]["atom_id"]) for row in data["namespaces"]],
        )

    def test_keeps_one_explicit_root_namespace_context_and_uses_prefix_only_as_fallback(self):
        data = build_subject_projection_data([
            carrier("CA-R-1", "CAPRMEDIO <+ MODEL", claim("Model root.")),
            carrier("CA-R-2", "CAPRMEDIO <+ MODEL <+ Node", claim("Node declaration.")),
            carrier("CA-R-3", "CAPRMEDIO <+ STRUCTURE <+ Project", claim("Project declaration.")),
            carrier("CA-R-4", "CAPRMEDIO <+ OTHER <+ Ignored", claim("Other declaration.")),
        ])

        self.assertEqual(
            [("CAPRMEDIO <+ MODEL", "CA-R-1"), ("CAPRMEDIO <+ STRUCTURE", "CA-R-3")],
            [(row["subject"], row["source"]["atom_id"]) for row in data["namespaces"]],
        )

    def test_does_not_invent_namespace_context_without_an_explicit_prefix(self):
        data = build_subject_projection_data([
            carrier("CA-R-1", "Node", claim("Node declaration.")),
            carrier("CA-R-2", "Project", claim("Project declaration.")),
        ])

        self.assertEqual([], data["namespaces"])

    def test_keeps_exact_component_declaration_for_a_retained_tree_entity_only(self):
        data = build_subject_projection_data([
            carrier("CA-R-1", "CFEL", claim("```CFEL", "CFEL: [string]{:1};", "```"), form="Entity Definition"),
            carrier("CA-R-2", "CFEL <+ Operator", claim("```CFEL", "Operator: [string]{:1};", "```")),
        ])

        entities = {row["identity"]: row for row in data["entities"]}
        self.assertEqual(["CA-R-2@1"], entities["Operator"]["declaration_refs"])
        self.assertEqual(["CA-R-2"], [row["source"]["atom_id"] for row in entities["Operator"]["formal_claims"]])
        self.assertEqual([], entities["CFEL"]["formal_claims"])
        self.assertIn("Operator", data["declarations"]["primary_nodes"])

    def test_catalog_keeps_exact_instances_relations_and_components_only(self):
        data = build_subject_projection_data([
            carrier("CA-R-1", "Node", claim("Node declaration.")),
            carrier("CA-R-2", "Node//Example", claim("Instance declaration.")),
            carrier("CA-R-3", "CFEL <+ Relation//RUN", claim("Relation declaration.")),
            carrier("CA-R-4", "CFEL <+ Format", claim("Component declaration.")),
            carrier("CA-R-5", "Node//Poison", claim("Rule."), form="Rule"),
        ])

        declarations = data["declarations"]
        self.assertEqual(["Node//Example"], list(declarations["instances"]))
        self.assertEqual(["RUN"], list(declarations["relations"]))
        self.assertEqual(["Format"], list(declarations["components"]))
        self.assertNotIn("Node//Poison", declarations["instances"])

    def test_surfaces_duplicate_exact_property_declarations_without_merging_them(self):
        data = build_subject_projection_data([
            carrier("CA-R-1", "Node", claim("Node declaration.")),
            carrier("CA-R-2", "Node.Status", claim("```CFEL", "Node.Status: Draft;", "```")),
            carrier("CA-R-3", "Node.Status", claim("```CFEL", "Node.Status: Review;", "```")),
        ])

        property = next(row for row in data["entities"] if row["identity"] == "Node")["direct_properties"][0]
        self.assertTrue(property["multiple_applicable"])
        self.assertEqual(["CA-R-2@1", "CA-R-3@1"], property["declaration_refs"])
        self.assertEqual(["Draft", "Review"], [row["literal"] for row in property["contracts"]])
        self.assertEqual(
            ["Node.Status"],
            [row["target"] for row in data["diagnostics"] if row.get("code") == "duplicate_exact_declaration"],
        )

    def test_keeps_inherited_original_property_and_all_constraint_channels_without_merging(self):
        data = build_subject_projection_data([
            carrier("CA-R-1", "Node", claim("```CFEL", "Node.Status[status]{:1}: [string]{:1+};", "```")),
            carrier("CA-R-2", "Node/Child", claim("Child declaration.")),
            carrier("CA-R-3", "Node.Status", claim("```CFEL", "Node.Status[status]{:1}: [string]{:1+};", "```")),
            carrier("CA-R-4", "Node/Child.Status", claim("```CFEL", "Node/Child.Status[child]{:0..1}: [integer]{:2};", "```")),
        ])

        child = next(row for row in data["entities"] if row["identity"] == "Node/Child")
        self.assertEqual(["Node"], child["ancestors"])
        self.assertEqual("Node/Child.Status", child["direct_properties"][0]["identity"])
        self.assertEqual("Node.Status", child["inherited_properties"][0]["identity"])
        self.assertTrue(child["direct_properties"][0]["multiple_applicable"])
        contract = child["direct_properties"][0]["contracts"][0]
        self.assertEqual("child", contract["name_format"])
        self.assertEqual({"minimum": 0, "maximum": 1}, contract["occurrence_cardinality"])
        self.assertEqual("integer", contract["value_format"])
        self.assertEqual({"minimum": 2, "maximum": 2}, contract["value_cardinality"])
        self.assertEqual("CA-R-3@1", child["inherited_properties"][0]["declaration_refs"][0])

    def test_excludes_non_declaration_claims_before_formal_extraction(self):
        carriers = [
            carrier("CA-R-1", "Node", claim("Node declaration.")),
            carrier("CA-R-2", "Node.Status", claim("```CFEL", "Node.Status: Draft;", "```")),
            carrier("CA-M-3", "Node.Status", claim("```CFEL", "Node.Status: Poison;", "```"), role="Method", form="Policy"),
            carrier("CA-R-4", "Node.Status", claim("```CFEL", "Node.Status: Poison;", "```"), form="Rule"),
            carrier("CA-R-5", "Node.Status", claim("```CFEL", "Node.Status: Poison;", "```"), form="Entity Definition"),
        ]
        for carrier_row in carriers:
            carrier_row["raw"] = repr(carrier_row).encode()
        source_bytes = [carrier_row["raw"] for carrier_row in carriers]
        data = build_subject_projection_data(carriers)

        property = next(row for row in data["entities"] if row["identity"] == "Node")["direct_properties"][0]
        self.assertEqual(["Draft"], [row["literal"] for row in property["contracts"]])
        self.assertEqual(["CA-R-2"], [row["source"]["atom_id"] for row in property["formal_claims"]])
        self.assertEqual(2, data["coverage"]["detail_declaration_sources"])
        self.assertEqual(source_bytes, [carrier_row["raw"] for carrier_row in carriers])


if __name__ == "__main__":
    unittest.main()
