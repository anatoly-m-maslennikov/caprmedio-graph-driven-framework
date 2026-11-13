"""Explicit Aspect membership in CFEL retains the complete written identity."""

from pathlib import Path
import sys
import unittest

TOOL = Path(__file__).resolve().parents[1]
sys.path[:0] = [str(TOOL.parent), str(TOOL)]

from current_subject_graph import compose_enhanced_current_graph  # noqa: E402
from readable_entity_tree import render_model  # noqa: E402
from cfel_claim_constraints import extract_claim_constraints  # noqa: E402


def carrier(atom_id, subject, expression):
    return {
        "source": {"atom_id": atom_id, "version": 1, "path": f"{atom_id}.md", "sha256": "a" * 64},
        "subjects": {} if subject is None else {"active": subject, "passive": []},
        "body": f"## Claim\n### Formal Claim\n```CFEL\n{expression};\n```\n",
        "read_view": {"content_role": "Requirement", "type": "Declaration"},
    }


def instance_edges(graph):
    identities = {node["id"]: node["identity"] for node in graph["nodes"]}
    return {
        (identities[edge["relation_source"]], identities[edge["relation_target"]])
        for edge in graph["edges"] if edge["kind"] == "INSTANCE_OF"
    }


class AspectClaimProjectionTests(unittest.TestCase):
    def test_grouped_formal_claim_preserves_full_identity_without_subject_fallback(self):
        first = "PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation <+ Data Handling <+ Query Processing"
        second = "PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Other <+ Query Processing"
        graph, provenance = compose_enhanced_current_graph([
            carrier("CA-R-1", "Unrelated Main Subject", f"({first}) ((INSTANCE_OF)) Aspect"),
            carrier("CA-R-2", None, f"({second}) ((INSTANCE_OF)) Aspect"),
        ])
        edges = instance_edges(graph)
        self.assertIn((first, "Aspect"), edges)
        self.assertIn((second, "Aspect"), edges)
        self.assertNotIn(("Query Processing", "Aspect"), edges)
        self.assertNotIn(("Unrelated Main Subject", "Aspect"), edges)
        self.assertTrue(any(row.get("role") == "formal_claim" for row in provenance["occurrences"]))
        rendered = render_model(
            graph, provenance, updated_at="2026-11-11 00:00:00 +0000", source_selection="Fixture",
            projection_identity={"projection_id": "CA-PROJ-901", "named_selection": "Current Atoms"},
        )
        self.assertIn(f"`INSTANCE_OF` `{first}` → `Aspect`", rendered)
        self.assertIn(f"`INSTANCE_OF` `{second}` → `Aspect`", rendered)

    def test_typed_aspect_preserves_full_identity_and_provenance(self):
        path = "PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Query Processing"
        old = carrier("CA-R-1", path, f"# project_structure\n{path};\n({path}) ((INSTANCE_OF)) Aspect")
        new = carrier("CA-R-1", path, "")
        new["body"] = ("## Claim\n### Formal Claim\n```python\n"
                       "from caprmedio.formal_claims import declare_entity\n"
                       "from caprmedio.model import Aspect\n"
                       f"declare_entity(entity_name='Query Processing', instance=Aspect(address={path!r}))\n```\n")
        old_constraints, old_errors = extract_claim_constraints(old)
        new_constraints, new_errors = extract_claim_constraints(new)
        self.assertEqual(old_errors, [])
        self.assertEqual(new_errors, [])
        self.assertEqual(old_constraints, new_constraints)
        old_graph, _ = compose_enhanced_current_graph([old])
        new_graph, provenance = compose_enhanced_current_graph([new])
        self.assertEqual(instance_edges(old_graph), instance_edges(new_graph))
        self.assertIn((path, "Aspect"), instance_edges(new_graph))
        self.assertTrue(any(row.get("role") == "formal_claim" for row in provenance["occurrences"]))

    def test_typed_aspects_with_same_name_keep_distinct_paths(self):
        paths = ["PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ " + parent + " <+ Example"
                 for parent in ("Engineering", "Product")]
        rows = []
        for index, path in enumerate(paths):
            row = carrier(f"CA-R-{index}", path, "")
            row["body"] = ("## Claim\n### Formal Claim\n```python\n"
                           "from caprmedio.formal_claims import declare_entity\n"
                           "from caprmedio.model import Aspect\n"
                           f"declare_entity(entity_name='Example', instance=Aspect(address={path!r}))\n```\n")
            rows.append(row)
        graph, _ = compose_enhanced_current_graph(rows)
        self.assertTrue({(path, "Aspect") for path in paths} <= instance_edges(graph))

    def test_ordinary_claim_does_not_declare_aspect_membership(self):
        path = "PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Example"
        row = carrier("CA-R-3", None, f"({path}) ((INSTANCE_OF)) Aspect")
        row["read_view"]["type"] = "Requirement"
        graph, _ = compose_enhanced_current_graph([row])
        self.assertNotIn((path, "Aspect"), instance_edges(graph))


if __name__ == "__main__":
    unittest.main()
