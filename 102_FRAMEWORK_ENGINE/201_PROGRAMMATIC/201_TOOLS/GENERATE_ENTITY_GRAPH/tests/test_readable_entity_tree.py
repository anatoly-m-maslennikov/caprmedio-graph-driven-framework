"""Controlled Inherency view acceptance under R1456, M385, E449 and D634."""

import copy
from pathlib import Path
import re
import sys
import unittest

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import readable_entity_tree as readable  # noqa: E402


STAMP = "2026-10-15 19:00:00 +0400"


def edge(child, parent, kind="NARROWER_THAN", **fields):
    return dict(relation_source=child, relation_target=parent, kind=kind, **fields)


def fixture():
    names = {
        "a": "Alpha",
        "b": "Beta",
        "s": "Shared",
        "z": "Zebra",
        "p": "Shared.Status",
        "v": "Shared.Status: Active",
        "d": "Shared.Status/Special",
        "bp": "Beta.Label",
    }
    graph = {
        "nodes": [dict(id=key, identity=value) for key, value in names.items()],
        "edges": [
            edge("s", "a"),
            edge("s", "b"),
            edge("z", "a"),
            edge("p", "s", "IS_BORNE_BY"),
            edge("v", "p", "IS_ALLOWED_VALUE_OF"),
            edge("d", "p"),
            edge("bp", "b", "IS_BORNE_BY"),
        ],
        "native_admission": "not_performed",
    }
    owners = [
        {
            "source": {
                "atom_id": atom_id,
                "version": version,
                "path": f"sources/{atom_id}.md",
                "sha256": "a" * 64,
            }
        }
        for atom_id, version in (("CA-R-9002", 3), ("CA-M-9001", 2), ("CA-R-9002", 3))
    ]
    return graph, {"owners": owners}


def render(graph=None, provenance=None, **overrides):
    default_graph, default_provenance = fixture()
    return readable.render_inherency(
        default_graph if graph is None else graph,
        default_provenance if provenance is None else provenance,
        updated_at=overrides.get("updated_at", STAMP),
        source_selection="controlled Core fixture",
    )


def primary(document):
    return document.split("### Primary entities\n", 1)[1].split("\n### ", 1)[0]


def text_blocks(document):
    return re.findall(r"```text\n(.*?)\n```", document, re.DOTALL)


class ReadableEntityTreeTests(unittest.TestCase):
    def test_frontmatter_sources_timestamp_selection_and_provisional_warning(self):
        document = render()
        self.assertTrue(document.startswith("---\n"))
        frontmatter = document.split("---\n", 2)[1]
        metadata = yaml.safe_load(frontmatter)
        self.assertEqual("Projection", metadata["artifact_form"])
        self.assertEqual("Entities Graph", metadata["type"])
        self.assertEqual(STAMP, metadata["updated_at"])
        self.assertEqual(["CA-M-9001@2", "CA-R-9002@3"], metadata["sources"])
        self.assertNotIn("\t", frontmatter)
        self.assertIn("controlled Core fixture", document)
        self.assertRegex(document.lower(), r"provisional|admission.*not|not.*admission")
        self.assertIn("## Inherency tree", document)
        self.assertNotIn("## Construction", document)
        graph, provenance = fixture()
        provenance["owners"][0]["source"]["atom_id"] = "OTHER-R-9002"
        self.assertIn("OTHER-R-9002@3", render(graph, provenance))

    def test_shared_primary_placements_and_single_ordered_details(self):
        document = render()
        main = primary(document)
        self.assertEqual(2, main.count("Shared"))
        self.assertLess(main.index("Alpha"), main.index("Beta"))
        self.assertLess(main.index("Shared"), main.index("Zebra"))
        self.assertNotIn("Status", main)
        self.assertNotIn("Label", main)
        sections = re.findall(r"^### (.+)$", document, re.MULTILINE)
        self.assertEqual(["Primary entities", "Shared", "Beta"], sections)

    def test_qualified_dependents_values_and_relation_meanings_use_tabs(self):
        document = render()
        details = document.split("### Shared\n", 1)[1].split("\n### ", 1)[0]
        for name in ("Shared.Status", "Shared.Status: Active", "Shared.Status/Special"):
            self.assertIn(name, details)
        for relation in ("NARROWER_THAN", "IS_BORNE_BY", "IS_ALLOWED_VALUE_OF"):
            self.assertIn(relation, document)
        blocks = text_blocks(document)
        self.assertTrue(blocks)
        self.assertTrue(
            any(line.startswith("\t\t") for block in blocks for line in block.splitlines())
        )
        self.assertFalse(
            any(line.startswith(" ") for block in blocks for line in block.splitlines())
        )

    def test_generation_is_deterministic_and_does_not_mutate_inputs(self):
        graph, provenance = fixture()
        before = copy.deepcopy((graph, provenance))
        expected = render(graph, provenance)
        self.assertEqual(before, (graph, provenance))
        graph["nodes"].reverse()
        graph["edges"].reverse()
        provenance["owners"].reverse()
        self.assertEqual(expected, render(graph, provenance))
        later = render(graph, provenance, updated_at="2026-10-15 19:01:00 +0400")
        self.assertEqual(expected.split("---\n", 2)[2], later.split("---\n", 2)[2])

    def test_declared_root_and_sibling_order_precedes_alphabetical_fallback(self):
        graph, provenance = fixture()
        graph["nodes"][1]["ordinal_position"] = 1
        graph["edges"][2]["ordinal_position"] = 1
        main = primary(render(graph, provenance))
        self.assertLess(main.index("Beta"), main.index("Alpha"))
        alpha = main.split("Alpha", 1)[1]
        self.assertLess(alpha.index("Zebra"), alpha.index("Shared"))

    def test_cycle_without_roots_is_reported_and_expansion_is_finite(self):
        graph = {
            "nodes": [{"id": name, "identity": name} for name in ("A", "B")],
            "edges": [edge("A", "B"), edge("B", "A")],
        }
        document = render(graph)
        self.assertIn("[cycle]", document)
        self.assertIn("A", primary(document))
        self.assertIn("B", primary(document))
        self.assertLess(len(document.splitlines()), 100)

    def test_unclassified_and_non_inherency_edges_are_not_guessed(self):
        graph = {
            "nodes": [{"id": name, "identity": name} for name in ("A", "B", "C")],
            "edges": [edge("B", "A", "UNCLASSIFIED"), edge("C", "A", "DEPENDS_ON")],
        }
        document = render(graph)
        self.assertIn("UNCLASSIFIED", document)
        self.assertIn("DEPENDS_ON", document)
        self.assertFalse(
            any(
                line.startswith("\t")
                for block in text_blocks(primary(document))
                for line in block.splitlines()
            )
        )
        self.assertNotIn("## Construction", document)

    def test_malformed_endpoints_and_duplicate_node_ids_are_refused(self):
        for change in ("missing endpoint", "duplicate node"):
            graph, provenance = fixture()
            if change == "missing endpoint":
                graph["edges"][0]["relation_target"] = "missing"
            else:
                graph["nodes"].append(dict(graph["nodes"][0]))
            with self.subTest(change=change), self.assertRaises(ValueError):
                render(graph, provenance)

    def test_missing_or_invalid_source_versions_are_refused(self):
        for version in (None, 0, -1, True, "2", 2.5):
            graph, provenance = fixture()
            source = provenance["owners"][0]["source"]
            if version is None:
                source.pop("version")
            else:
                source["version"] = version
            with self.subTest(version=version), self.assertRaises(ValueError):
                render(graph, provenance)


if __name__ == "__main__":
    unittest.main()
