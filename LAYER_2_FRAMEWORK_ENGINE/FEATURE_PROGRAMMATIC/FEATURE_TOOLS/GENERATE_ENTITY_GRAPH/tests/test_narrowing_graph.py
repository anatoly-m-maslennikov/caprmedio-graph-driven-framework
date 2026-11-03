"""Declared-only Current NARROWER_THAN tree projection."""

from pathlib import Path
import sys
import unittest


TOOL = Path(__file__).resolve().parents[1]
sys.path[:0] = [str(TOOL.parent), str(TOOL)]

from current_subject_graph import compose_narrowing_graph  # noqa: E402
from readable_entity_tree import render_inherency  # noqa: E402


def carrier(atom_id, active, *, form="Declaration", body=""):
    return {
        "source": {"atom_id": atom_id, "version": 1, "path": f"sources/{atom_id}.md"},
        "subjects": {"active": active, "passive": []}, "body": body,
        "read_view": {"content_role": "Requirement", "type": form},
    }


def claim(expression):
    return f"## Claim\n\n```CFEL\n{expression}\n```\n"


class NarrowingGraphTests(unittest.TestCase):
    def test_instance_group_cannot_create_a_narrowing_edge(self):
        graph, _ = compose_narrowing_graph([
            carrier("CA-R-1", "Node"), carrier("CA-R-2", "Node/Continuant"),
            carrier("CA-R-3", "Node/Actor", body=claim("# instances\nActor ((NARROWER_THAN)) @Continuant")),
        ])
        names = {row["id"]: row["identity"] for row in graph["nodes"]}
        edges = {(names[row["relation_source"]], names[row["relation_target"]]) for row in graph["edges"]}
        self.assertNotIn(("Node/Actor", "Node/Continuant"), edges)

    def test_declared_paths_and_explicit_reference_claims_form_the_only_tree_edges(self):
        graph, provenance = compose_narrowing_graph([
            carrier("CA-R-0", "Node"),
            carrier("CA-R-1", "Node/Continuant"),
            carrier("CA-R-2", "Node/Atom"),
            carrier("CA-R-3", "Node/Atom/(.Role := Method)"),
            carrier("CA-R-4", "Node/Actor", body=claim("Actor ((NARROWER_THAN)) @Continuant")),
            carrier("CA-R-5", "Event Record"),
            carrier("CA-R-5A", "Node/Continuant//CAPRMEDIO Framework"),
            carrier("CA-R-6", "Node/Atom.Status"),
            carrier("CA-R-7", "Node/Node", body=claim("Node {:0+}((NARROWER_THAN)) Node")),
            carrier("CA-R-8", "CFEL", form="Entity Definition"),
            carrier("CA-R-9", "Carrier", form="Entity Definition"),
            carrier("CA-R-10", "Carrier/File", form="Entity Definition"),
            carrier("CA-R-11", "Carrier/File/Markdown", form="Entity Definition"),
            carrier("CA-R-12", "Term", form="Entity Definition"),
            carrier("CA-R-13", "CFEL ((NARROWER_THAN)) @Carrier", form="Entity Definition"),
            carrier("CA-R-14", "CFEL > Format/bool", form="Entity Definition"),
            carrier("CA-R-15", "Entity/Legacy", form="Entity Definition"),
            carrier("CA-R-16", "Node/Atom", form="Relation Definition", body=claim("Atom ((NARROWER_THAN)) @Continuant")),
        ])

        nodes = {row["identity"]: row for row in graph["nodes"]}
        self.assertTrue({"Node/Continuant", "Node/Atom", "Node/Atom/(.Role:=Method)", "Node/Actor", "CFEL", "Carrier", "Carrier/File/Markdown", "Term"} <= set(nodes))
        self.assertNotIn("Node/Atom.Status", nodes)
        self.assertNotIn("Node/Continuant//CAPRMEDIO Framework", nodes)
        self.assertNotIn("Format/bool", nodes)
        self.assertEqual("(.Role:=Method)", nodes["Node/Atom/(.Role:=Method)"]["display_name"])
        names = {row["id"]: row["identity"] for row in graph["nodes"]}
        edges = {(names[row["relation_source"]], names[row["relation_target"]]) for row in graph["edges"]}
        self.assertTrue({("Node/Atom/(.Role:=Method)", "Node/Atom"), ("Node/Actor", "Node/Continuant"),
                         ("Carrier/File/Markdown", "Carrier/File"), ("CFEL", "Carrier")} <= edges)
        self.assertNotIn(("Node/Node", "Node/Node"), edges)
        self.assertTrue(any("CFEL > Format/bool" in row for row in graph["diagnostics"]))
        self.assertTrue(any("Entity/Legacy" in row for row in graph["diagnostics"]))
        self.assertFalse(any("CAPRMEDIO Framework" in row for row in graph["diagnostics"]))
        self.assertIn("Event Record: no explicit NARROWER_THAN parent; rendered as a root.", graph["diagnostics"])
        document = render_inherency(
            graph, provenance, updated_at="2026-11-02 00:00:00 +0400",
            source_selection="controlled Current fixture",
            projection_identity={"projection_id": "CA-PROJ-918", "named_selection": "Current Nodes"},
        )
        self.assertIn("/ (.Role:=Method)", document)
        self.assertIn("Node/Atom/(.Role:=Method)", "\n".join(row["identity"] for row in graph["nodes"]))

    def test_missing_and_ambiguous_reference_parents_are_diagnostics(self):
        graph, _ = compose_narrowing_graph([
            carrier("CA-R-0", "Node"),
            carrier("CA-R-1", "Node/Continuant"), carrier("CA-R-2", "Node/Continuant"),
            carrier("CA-R-3", "Node/Actor", body=claim("Actor ((NARROWER_THAN)) @Continuant")),
            carrier("CA-R-4", "Node/Aspect", body=claim("Aspect ((NARROWER_THAN)) @Missing")),
        ])
        names = {row["id"]: row["identity"] for row in graph["nodes"]}
        edges = {(names[row["relation_source"]], names[row["relation_target"]]) for row in graph["edges"]}
        self.assertNotIn(("Node/Actor", "Node/Continuant"), edges)
        self.assertTrue(any("reference `Continuant` is ambiguous" in row for row in graph["diagnostics"]))
        self.assertTrue(any("Aspect` -> `Missing` has an undeclared endpoint" in row for row in graph["diagnostics"]))

    def test_declared_cfel_components_form_their_own_narrowing_branch_not_a_composition_edge(self):
        graph, _ = compose_narrowing_graph([
            carrier("CA-R-1", "CFEL", form="Entity Definition"),
            carrier("CA-R-2", "CFEL <+ Format"),
            carrier("CA-R-3", "CFEL <+ Format/bool"),
            carrier("CA-R-4", "CFEL <+ Operator//not-a-primary-component"),
            carrier("CA-R-5", "CFEL <+ Relation//RUN"),
        ])

        nodes = {row["identity"]: row for row in graph["nodes"]}
        self.assertEqual({"CFEL", "Format", "Format/bool"}, set(nodes))
        names = {row["id"]: row["identity"] for row in graph["nodes"]}
        edges = {(names[row["relation_source"]], names[row["relation_target"]]) for row in graph["edges"]}
        self.assertEqual({("Format/bool", "Format")}, edges)
        self.assertFalse(any("Format" in row and "undeclared endpoint" in row for row in graph["diagnostics"]))
        self.assertFalse(any("Operator//not-a-primary-component" in row for row in graph["diagnostics"]))
        self.assertFalse(any("Relation//RUN" in row for row in graph["diagnostics"]))

    def test_namespace_prefix_admits_only_the_local_narrowing_tree(self):
        graph, _ = compose_narrowing_graph([
            carrier("CA-R-1", "CAPRMEDIO <+ MODEL <+ Node"),
            carrier("CA-R-2", "CAPRMEDIO <+ MODEL <+ Node/Atom"),
            carrier("CA-R-3", "CAPRMEDIO <+ MODEL <+ CFEL <+ Format"),
            carrier("CA-R-4", "CAPRMEDIO <+ MODEL <+ CFEL <+ Format/bool"),
        ])

        names = {row["id"]: row["identity"] for row in graph["nodes"]}
        edges = {(names[row["relation_source"]], names[row["relation_target"]]) for row in graph["edges"]}
        self.assertTrue({"Node", "Node/Atom", "Format", "Format/bool"} <= set(names.values()))
        self.assertIn(("Node/Atom", "Node"), edges)
        self.assertIn(("Format/bool", "Format"), edges)
        self.assertFalse(any("CAPRMEDIO" in edge for edge in edges))

    def test_explicit_namespace_roots_do_not_create_primary_nodes(self):
        graph, _ = compose_narrowing_graph([
            carrier("CA-R-1", "CAPRMEDIO_MODEL"),
            carrier("CA-R-2", "CAPRMEDIO_STRUCTURE"),
            carrier("CA-R-3", "CAPRMEDIO_MODEL <+ Node"),
        ])
        self.assertEqual({"Node"}, {row["identity"] for row in graph["nodes"]})
