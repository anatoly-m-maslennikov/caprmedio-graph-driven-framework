"""Bounded model/CFEL view preserves legacy graph behavior and evidence."""

from __future__ import annotations

import json
from pathlib import Path
import sys
import tempfile
import unittest


TOOL = Path(__file__).resolve().parents[1]
sys.path[:0] = [str(TOOL.parent), str(TOOL)]

from cfel_claim_constraints import extract_claim_constraints, preview_constraints_from_paths  # noqa: E402
from current_entity_sources import (  # noqa: E402
    build_current_model_graph,
)
from current_subject_graph import compose_current_graph, compose_enhanced_current_graph, subject_facts  # noqa: E402
from generate_entity_graph import AtomCarrier, EntityGraphError, discover_atoms, parse_subject_relations  # noqa: E402
from readable_entity_tree import render_model  # noqa: E402
import subject_notation  # noqa: E402


def source(atom_id: str) -> dict[str, object]:
    return {"atom_id": atom_id, "version": 1, "path": f"sources/{atom_id}.md", "sha256": "a" * 64}


def carrier(
    atom_id: str, subjects: dict, body: str = "", *, declaration: bool = False,
    role: str = "Requirement", form: str = "Declaration",
) -> dict[str, object]:
    row = {"source": source(atom_id), "subjects": subjects, "body": body}
    if declaration:
        row["read_view"] = {"content_role": role, "type": form}
    return row


class EnhancedCurrentGraphTests(unittest.TestCase):
    def test_model_binder_is_opaque_and_population_count_applies_to_selection(self) -> None:
        block = '''# model
IF $model_node in (Node, Node.**) THEN (
  $model_node.Name: [string]{:1};
  IF $model_node >| Category == "A; B" THEN ($model_node.X: [string]{:1})
);
Relation//$relation ((HAS_INVERSE)) Relation//$relation_2;
# instances
Node//$n{:1..3};
$n.Name: [string]{:1}
'''
        graph, _ = compose_enhanced_current_graph([
            carrier("CA-R-1", {"active": "Node", "passive": []}, declaration=True),
            carrier("CA-R-2", {"active": "Node.Name", "passive": []}, "## Claim\n### Formal Claim\n```CFEL\n" + block + "```\n", declaration=True),
        ])
        binder = next(row for row in graph["constraints"] if row["kind"] == "model_binding")
        self.assertEqual("model_node", binder["variable"])
        self.assertEqual("Node, Node.**", binder["selection"])
        self.assertIn('"A; B"', binder["expression"])
        self.assertEqual("opaque", binder["interpretation"])
        self.assertEqual([], graph["model_contracts"])
        population = next(row for row in graph["instance_constraints"] if row["kind"] == "instance_population_constraint")
        self.assertEqual({"minimum": 1, "maximum": 3}, population["population_cardinality"])
        self.assertEqual("Node", population["kind_selector"])
        self.assertTrue(any(row.get("relation") == "HAS_INVERSE" for row in graph["constraints"]))
        self.assertFalse(any("$" in row["identity"] for row in graph["model"]["primary_nodes"]))
        self.assertIn(block, [row["block"] for row in graph["formal_claim_blocks"]])

    def test_grouped_constraints_keep_declaration_model_and_instance_evidence_separate(self) -> None:
        block = """# model
Node.Name: [string]{:1};
Node ((CONTAINS)) Node;
# instances
Node//$n;
$n.Name: [integer]{:1};
$n ((CONTAINS)) Node//$child
"""
        graph, _ = compose_enhanced_current_graph([
            carrier("CA-R-1", {"active": "Node", "passive": []}, declaration=True),
            carrier("CA-R-2", {"active": "Node.Name", "passive": []}, "## Claim\n### Formal Claim\n```CFEL\n" + block + "```\n", declaration=True),
            carrier("CA-R-3", {"active": "Node.Name", "passive": []}, "## Claim\n```CFEL\n# model\nNode.Name: [integer]{:1};\n```\n", declaration=True, form="Rule"),
        ])
        self.assertEqual(["string"], [row["value_format"] for row in graph["model_contracts"]])
        self.assertEqual(["integer"], [row["value_format"] for row in graph["source_constraints"]])
        self.assertEqual({"instance_binding", "property_constraint", "relation_cardinality"},
                         {row["kind"] for row in graph["instance_constraints"]})
        self.assertTrue(any(row.get("relation") == "CONTAINS" for row in graph["constraints"]))
        self.assertIn(block, [row["block"] for row in graph["formal_claim_blocks"]])
        self.assertFalse(any("$n" in row["identity"] for row in graph["model"]["primary_nodes"]))

    def test_migrated_subject_keys_keep_the_legacy_graph_shape(self) -> None:
        legacy, _ = compose_current_graph([
            carrier("CA-R-1001", {"governs": "Node.Property", "depends_on": []}),
        ])
        migrated, _ = compose_current_graph([
            carrier("CA-R-1001", {"active": "Node.Property", "passive": []}),
        ])
        self.assertEqual(legacy, migrated)

    def test_conflicting_subject_aliases_fail_before_graph_projection(self) -> None:
        with self.assertRaisesRegex(ValueError, "Conflicting carrier aliases"):
            compose_current_graph([
                carrier("CA-R-1001", {"active": "Node", "governs": "Other", "passive": []}),
            ])

    def test_enhanced_view_separates_nodes_instances_relations_classifications_and_constraints(self) -> None:
        graph, _ = compose_enhanced_current_graph([
            carrier("CA-R-1001", {"active": "Node >| Independence", "passive": []}, declaration=True),
            carrier("CA-R-1002", {"active": "Node.Property: literal", "passive": []}, """## Claim
```CFEL
Node.Property{:0..1}: [string]{:1};
Node.Content.**[string]{:0+}: [markdown]{:1};
Journal// {:0+}((CONTAINS)) Event Record//;
Node >| Independence == Primary Node;
IF Node THEN Property
```
""", declaration=True),
            carrier("CA-R-1003", {"active": "Workflow//Daily", "passive": []}, declaration=True),
            carrier("CA-R-1004", {"active": "Node", "passive": []}, declaration=True),
            carrier("CA-R-1005", {"active": "Node.Property", "passive": []}, declaration=True),
        ])
        self.assertEqual("current_atom_model_graph", graph["kind"])
        self.assertEqual(
            {"Node"},
            {row["identity"] for row in graph["model"]["primary_nodes"]},
        )
        self.assertEqual(["Node.Property"], [row["identity"] for row in graph["model"]["properties"]])
        self.assertEqual(["Workflow//Daily"], [row["identity"] for row in graph["model"]["instances"]])
        self.assertEqual([], graph["model"]["relations"])
        self.assertEqual([], graph["model"]["classifications"])
        self.assertEqual([], graph["model"]["allowed_literals"])
        self.assertIn("Node >| Independence", [
            row["expression"] for row in graph["model"]["selected_subject_expressions"]
        ])
        self.assertEqual(
            {"property_constraint", "relation_cardinality", "classification_condition"},
            {row["kind"] for row in graph["constraints"]},
        )
        self.assertEqual(["cfel-expression-unsupported"], [row["code"] for row in graph["cfel_diagnostics"]])

    def test_enhanced_view_keeps_unparseable_current_subjects_as_diagnostics(self) -> None:
        graph, _ = compose_enhanced_current_graph([
            carrier(
                "CA-R-1016",
                {"active": "CFEL > Relation//rationale_for", "passive": []},
                declaration=True,
                form="Relation Definition",
            ),
        ])
        self.assertEqual([], graph["model"]["relations"])
        self.assertEqual(
            ["CFEL > Relation//rationale_for"],
            [row["expression"] for row in graph["model"]["selected_subject_expressions"]],
        )
        self.assertTrue(any("CA-R-1016" in row and "Subject projection failed" in row for row in graph["diagnostics"]))
        self.assertTrue(any("CA-R-1016" in row and "Model target unavailable" in row for row in graph["diagnostics"]))

    def test_property_value_count_is_per_property_and_recursive_name_count_stays_separate(self) -> None:
        records, diagnostics = extract_claim_constraints(carrier("CA-R-1001", {}, """## Claim
```CFEL
Property: [string]{:1};
Property.**[string]{:0+}: [markdown]{:1}
```
"""))
        self.assertEqual([], diagnostics)
        values = next(row for row in records if row["selection"] == "values")
        recursive = next(row for row in records if row["selection"] == "recursive_dependents")
        self.assertEqual("Property", values["property_selector"])
        self.assertIsNone(values["occurrence_cardinality"])
        self.assertEqual({"minimum": 1, "maximum": 1}, values["value_cardinality"])
        self.assertEqual({"minimum": 0, "maximum": None}, recursive["occurrence_cardinality"])
        self.assertEqual({"minimum": 1, "maximum": 1}, recursive["value_cardinality"])

    def test_bounded_extractor_preserves_structural_and_reverse_classification_notation(self) -> None:
        records, diagnostics = extract_claim_constraints(carrier("CA-R-1001", {}, """## Claim
```CFEL
Workflow// {:1+}<+{:1} Step//;
Independence |< Node == Primary Node
```
"""))
        self.assertEqual([], diagnostics)
        relation = next(row for row in records if row["kind"] == "relation_cardinality")
        self.assertEqual("<+", relation["relation_notation"])
        self.assertIsNone(relation["relation"])
        classification = next(row for row in records if row["kind"] == "classification_condition")
        self.assertEqual(("Node", "Independence", "Primary Node"),
                         (classification["subject_selector"], classification["axis"], classification["value"]))

    def test_role_form_and_subject_aliases_are_read_without_changing_carrier_evidence(self) -> None:
        atom = AtomCarrier(
            atom_id="CA-R-1001", version=1, cce_form="", content_role="Requirement",
            atom_type="Declaration", status="Active", carrier_path="sources/CA-R-1001.md",
            sha256="a" * 64,
            frontmatter="subjects:\n  active: Node\n  passive: []\n",
            body="",
        )
        relations, diagnostics = parse_subject_relations(atom, subject_profile="approved")
        self.assertEqual([], diagnostics)
        self.assertEqual([("GOVERNS", "active")], [(row.kind, row.source_schema_key) for row in relations])
        parsed = subject_notation.parse_subject_expression("Atom/(.Role:= Method)")
        self.assertEqual("Atom/(.Role:=Method)", subject_notation.render_subject(parsed))

    def test_conflicting_mixed_aliases_are_rejected_by_canonical_reader(self) -> None:
        atom = AtomCarrier(
            atom_id="CA-R-1001", version=1, cce_form="", content_role="Requirement",
            atom_type="Declaration", status="Active", carrier_path="sources/CA-R-1001.md",
            sha256="a" * 64,
            frontmatter="subjects:\n  active: Node\n  governs: Other\n",
            body="",
        )
        with self.assertRaises(EntityGraphError) as error:
            parse_subject_relations(atom, subject_profile="approved")
        self.assertEqual("subject-schema-conflict", error.exception.code)

    def test_canonical_discovery_reads_role_form_and_rejects_a_conflict(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            source_root = root / "SUPERLAYER_1_METHODOLOGY_SOURCES"
            source_root.mkdir()
            path = source_root / "CA-R-1001.md"
            path.write_text(
                "---\natom_id: CA-R-1001\nversion: 1\nstatus: Active\n"
                "role: Requirement\nform: Declaration\nsubjects:\n  active: Node\n  passive: []\n"
                "---\n# Source\n",
                encoding="utf-8",
            )
            carriers, diagnostics = discover_atoms(root, source_root)
            self.assertEqual([], diagnostics)
            self.assertEqual(("Requirement", "Declaration"), (carriers[0].content_role, carriers[0].atom_type))
            path.write_text(path.read_text(encoding="utf-8").replace("role: Requirement", "role: Method\ncontent_role: Requirement"), encoding="utf-8")
            with self.assertRaises(EntityGraphError) as error:
                discover_atoms(root, source_root)
            self.assertEqual("atom-metadata-conflict", error.exception.code)

    def test_model_renderer_keeps_constraints_and_unsupported_cfel_visible(self) -> None:
        graph, provenance = compose_enhanced_current_graph([
            carrier("CA-R-1001", {"active": "Node.Property: literal", "passive": []}, """## Claim
```CFEL
Node.Property: [string]{:1};
IF Node THEN Property
```
""", declaration=True),
        ])
        document = render_model(
            graph, provenance, updated_at="2026-11-01 00:00:00 +0000",
            source_selection="Current Atoms in sources",
            projection_identity={"projection_id": "CA-PROJ-901", "named_selection": "Current Atoms"},
        )
        for heading in ("## Model graph", "## Primary Nodes", "## Properties", "## Allowed literals", "## Constraints", "## Unsupported CFEL"):
            self.assertIn(heading, document)
        self.assertIn("Node.Property: [string]{:1}", document)
        self.assertIn("IF Node THEN Property", document)

    def test_model_renderer_keeps_nonexpression_cfel_diagnostic_visible(self) -> None:
        graph, provenance = compose_enhanced_current_graph([
            carrier("CA-R-1001", {"active": "Node", "passive": []}, """## Claim
```CFEL
Node: [string]{:1}
""", declaration=True),
        ])
        document = render_model(
            graph, provenance, updated_at="2026-11-01 00:00:00 +0000",
            source_selection="Current Atoms in sources",
            projection_identity={"projection_id": "CA-PROJ-901", "named_selection": "Current Atoms"},
        )
        self.assertIn("CFEL fence has no closing fence", document)

    def test_explicit_draft_paths_are_read_only_preview_inputs(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            path = root / "draft" / "CA-R-1001@1-draft.md"
            path.parent.mkdir()
            path.write_text(
                "---\natom_id: CA-R-1001\nversion: 1\nstatus: Draft\nsubjects:\n  active: Node\n"
                "---\n## Claim\n```CFEL\nNode.Property: [string]{:1};\nIF Node THEN Property\n```\n",
                encoding="utf-8",
            )
            before = path.read_bytes()
            records, diagnostics = preview_constraints_from_paths([path], repository=root)
            self.assertEqual("property_constraint", records[0]["kind"])
            self.assertEqual("draft/CA-R-1001@1-draft.md", records[0]["source"]["path"])
            self.assertEqual("cfel-expression-unsupported", diagnostics[0]["code"])
            self.assertEqual(before, path.read_bytes())

    def test_fail_closed_claim_scope_controls_selectors_and_markdown_fences(self) -> None:
        records, diagnostics = extract_claim_constraints(carrier("CA-R-1001", {}, """## Claim
````markdown
```CFEL
Outside: [string]{:1}
```
````
```CFEL
A{:1}: [int]{:1};
Atom/(.Role := Requirement)/(.Form := Rule);
IF(A) THEN(B ((RUN)) C);
Journal >| (Container == yes);
Node >| Container: yes;
Node {:0}((*));
Label: 'a;b';
FENCED_LABELS(Atom.Content.Claim): [in (CFEL)]{:0..1};
A + B{:1}
```
## Details
```CFEL
Details: [string]{:1}
```
"""))
        property_constraint = next(row for row in records if row["kind"] == "property_constraint")
        self.assertEqual("A", property_constraint["property_selector"])
        self.assertEqual({"minimum": 1, "maximum": 1}, property_constraint["occurrence_cardinality"])
        self.assertEqual({"minimum": 1, "maximum": 1}, property_constraint["value_cardinality"])
        default_relation = next(row for row in records if row["kind"] == "relation_cardinality")
        self.assertEqual(("Node", "*", None, "all_relations"), (
            default_relation["source_selector"], default_relation["relation"],
            default_relation["target_selector"], default_relation["selection"],
        ))
        grouped = next(row for row in records if row["kind"] == "classification_condition")
        self.assertEqual(("Journal", "Container", "yes"),
                         (grouped["subject_selector"], grouped["axis"], grouped["value"]))
        self.assertFalse(any(row.get("property_selector") == "Node >| Container" for row in records))
        self.assertFalse(any(row.get("relation") == "RUN" for row in records))
        unsupported = [row["expression"] for row in diagnostics if row["code"] == "cfel-expression-unsupported"]
        self.assertIn("Atom/(.Role := Requirement)/(.Form := Rule)", unsupported)
        self.assertIn("IF(A) THEN(B ((RUN)) C)", unsupported)
        self.assertIn("Node >| Container: yes", unsupported)
        self.assertIn("Label: 'a;b'", unsupported)
        self.assertIn("FENCED_LABELS(Atom.Content.Claim): [in (CFEL)]{:0..1}", unsupported)
        self.assertIn("A + B{:1}", unsupported)
        self.assertEqual(1, sum(row["code"] == "cfel-fence-outside-claim" for row in diagnostics))

    def test_reverse_named_relation_clause_normalizes_endpoints_and_written_counts(self) -> None:
        records, diagnostics = extract_claim_constraints(carrier("CA-R-1001", {}, """## Claim
```CFEL
Step {:1}((IS_CONTAINED_BY)){:2} Workflow;
Workflow {:2}<((IS_CONTAINED_BY)){:1} Step;
```
"""))
        self.assertEqual([], diagnostics)
        forward, reverse = records
        self.assertEqual(
            (forward["relation"], forward["source_selector"], forward["target_selector"],
             forward["source_cardinality"], forward["target_cardinality"]),
            (reverse["relation"], reverse["source_selector"], reverse["target_selector"],
             reverse["source_cardinality"], reverse["target_cardinality"]),
        )
        self.assertEqual("forward", forward["written_direction"])
        self.assertEqual("reverse", reverse["written_direction"])
        self.assertEqual(("Workflow", "Step"),
                         (reverse["written_source_selector"], reverse["written_target_selector"]))

    def test_qualified_declaration_admits_its_node_but_other_roles_do_not(self) -> None:
        graph, _ = compose_enhanced_current_graph([
            carrier(
                "CA-R-1001", {"active": "Atom/(.Role := Requirement)/(.Form := Rule)", "passive": []},
                declaration=True,
            ),
            carrier(
                "CA-C-1002", {"active": "Atom/(.Role := Concern)", "passive": []},
            ),
        ])
        self.assertTrue(graph["nodes"], "legacy syntax graph remains available")
        self.assertEqual(
            ["Atom/(.Role:=Requirement)/(.Form:=Rule)"],
            [row["identity"] for row in graph["model"]["primary_nodes"]],
        )
        self.assertEqual([], graph["model"]["properties"])
        self.assertEqual(
            ["Atom/(.Role := Concern)", "Atom/(.Role := Requirement)/(.Form := Rule)"],
            [row["expression"] for row in graph["model"]["selected_subject_expressions"]],
        )

    def test_namespace_prefixes_add_containment_without_changing_local_targets(self) -> None:
        graph, _ = compose_enhanced_current_graph([
            carrier("CA-R-1001", {"active": "CAPRMEDIO <+ MODEL <+ Node", "passive": []}, declaration=True),
            carrier("CA-R-1002", {"active": "CAPRMEDIO <+ MODEL <+ Node.Property", "passive": []}, declaration=True),
            carrier("CA-R-1003", {"active": "CAPRMEDIO <+ MODEL <+ Workflow//Daily", "passive": []}, declaration=True),
            carrier("CA-R-1004", {"active": "CAPRMEDIO <+ MODEL <+ CFEL <+ Relation//RUN", "passive": []}, declaration=True, form="Relation Definition"),
        ])

        self.assertEqual({"Node"}, {
            row["identity"] for row in graph["model"]["primary_nodes"]
        })
        self.assertEqual(["Node.Property"], [row["identity"] for row in graph["model"]["properties"]])
        self.assertEqual(["Workflow//Daily"], [row["identity"] for row in graph["model"]["instances"]])
        self.assertEqual(["Relation//RUN"], [row["identity"] for row in graph["model"]["relations"]])
        nodes = {row["id"]: row["identity"] for row in graph["nodes"]}
        containment = {
            (nodes[row["relation_source"]], nodes[row["relation_target"]])
            for row in graph["edges"] if row["kind"] == "IS_CONTAINED_BY"
        }
        self.assertIn(("MODEL", "CAPRMEDIO"), containment)

    def test_inverse_glyph_projects_distinct_relation_endpoints(self) -> None:
        nodes, facts, _ = subject_facts("Relation//NARROWER_THAN <--> Relation//BROADER_THAN")
        self.assertTrue({"Relation//NARROWER_THAN", "Relation//BROADER_THAN"} <=
                        {row["identity"] for row in nodes})
        inverse = [row for row in facts if row["kind"] == "HAS_INVERSE"]
        self.assertEqual(1, len(inverse))
        self.assertEqual(("Relation//NARROWER_THAN", "Relation//BROADER_THAN"),
                         (inverse[0]["source"], inverse[0]["target"]))

    def test_bare_legacy_namespace_subjects_remain_literal_without_containment(self) -> None:
        for subject in ("MODEL", "PROJECT STRUCTURE"):
            nodes, facts, target = subject_facts(subject)
            self.assertEqual([subject], [row["identity"] for row in nodes])
            self.assertEqual([], facts)
            self.assertEqual(subject, target)

    def test_explicit_roots_are_not_model_nodes_and_grouped_selectors_project(self) -> None:
        graph, _ = compose_enhanced_current_graph([
            carrier("CA-R-1001", {"active": "CAPRMEDIO_MODEL", "passive": []}, declaration=True),
            carrier("CA-R-1002", {"active": "CAPRMEDIO_STRUCTURE", "passive": []}, declaration=True),
            carrier("CA-R-1003", {"active": "CAPRMEDIO_MODEL <+ (Atom/(.Header.Role := Method))", "passive": []}, declaration=True),
            carrier("CA-R-1004", {"active": "(CAPRMEDIO_MODEL <+ Atom)/(.Header.Form := Rule)", "passive": []}, declaration=True),
        ])
        self.assertEqual({"Atom/(.Header.Role:=Method)", "Atom/(.Header.Form:=Rule)"},
                         {row["identity"] for row in graph["model"]["primary_nodes"]})
        self.assertEqual([], graph["diagnostics"])

    def test_post_cutover_role_form_frontier_keeps_catalogue_and_constraints_separate(self) -> None:
        temporary_root = Path.cwd() / ".caprmedio_tmp/tests/test_enhanced_current_graph"
        temporary_root.mkdir(parents=True, exist_ok=True)
        with tempfile.TemporaryDirectory(dir=temporary_root) as temporary:
            root = Path(temporary)
            source_root = root / "current-model"
            source_root.mkdir()

            def write(atom_id: str, role: str, form: str, active: str, claim: str = "") -> None:
                (source_root / f"{atom_id}.md").write_text(
                    "---\n"
                    f"atom_id: {atom_id}\nversion: 1\nstatus: Active\nrole: {role}\nform: {form}\n"
                    f"subjects:\n  active: {active}\n  passive: []\n---\n" + claim,
                    encoding="utf-8",
                )

            write("CA-R-9001", "Requirement", "Declaration", "Node")
            write(
                "CA-R-9002", "Requirement", "Declaration", "Projection.Form",
                "## Claim\n```CFEL\nProjection.Form{:1}: [string]{:1};\nProjection.Form: Catalog;\nProjection.Form: Map\n```\n",
            )
            write("CA-R-9003", "Requirement", "Relation Definition", "Entity/CFEL <+ Relation//RUN")
            write("CA-R-9004", "Requirement", "Declaration", "Node/Continuant")
            write("CA-R-9005", "Requirement", "Declaration", "Node/Occurrent")
            write("CA-R-9006", "Requirement", "Rule", "(Node, Node/**, .**)")

            graph, _ = build_current_model_graph(source_root, root)

        self.assertEqual(
            ["Node", "Node/Continuant", "Node/Occurrent"],
            [row["identity"] for row in graph["model"]["primary_nodes"]],
        )
        self.assertEqual(["Projection.Form"], [row["identity"] for row in graph["model"]["properties"]])
        self.assertEqual(["Relation//RUN"], [row["identity"] for row in graph["model"]["relations"]])
        self.assertEqual(
            {"Projection.Form: Catalog", "Projection.Form: Map"},
            {row["expression"] for row in graph["constraints"] if row["kind"] == "allowed_literal"},
        )
        self.assertNotIn("CA-R-9006", [row["source"]["atom_id"] for row in graph["model"]["selected_subject_expressions"]])

    def test_promoted_draft_register_preserves_the_historical_90_declaration_target(self) -> None:
        repository = Path(__file__).resolve().parents[5]
        register = repository / (
            ".caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/"
            "CA-SU-11_LAYER_1_CORE_META_MODEL/02_analysis/draft/node-declaration-20261031/"
            "migration-20261101/promoted-draft-register.json"
        )
        snapshot = json.loads(register.read_text(encoding="utf-8"))
        declarations = [row for row in snapshot["drafts"] if row.get("classification")]

        self.assertEqual(
            "139 identified Drafts; 90 Node Declarations including retained Continuant and Occurrent",
            snapshot["status"],
        )
        self.assertEqual(90, len(declarations))
        self.assertEqual(30, sum(row["classification"] == "Primary Node" for row in declarations))
        self.assertEqual(60, sum(row["classification"] == "Property" for row in declarations))
        self.assertTrue(all(row["id"].endswith("@1-draft") for row in declarations))
        self.assertTrue(all("@1-draft" in row["path"] for row in declarations))
        self.assertTrue(all(len(row["sha256"]) == 64 for row in declarations))


if __name__ == "__main__":
    unittest.main()
