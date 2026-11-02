"""Current-source ``//`` instance paths remain typed and non-authoritative."""

from __future__ import annotations

from pathlib import Path
import sys
import unittest


TOOL = Path(__file__).resolve().parents[1]
sys.path[:0] = [str(TOOL.parent), str(TOOL)]

from current_subject_graph import compose_current_graph, path_steps  # noqa: E402
import subject_notation  # noqa: E402


def source(atom_id: str = "CA-R-2002", version: int = 1) -> dict[str, object]:
    return {
        "atom_id": atom_id,
        "version": version,
        "path": f"sources/{atom_id}.md",
        "sha256": "a" * 64,
    }


def graph_for(subject: str) -> tuple[dict, dict]:
    return compose_current_graph(
        [{"source": source(), "subjects": {"governs": subject, "depends_on": []}}]
    )


class CurrentInstanceGraphTests(unittest.TestCase):
    def test_instance_path_preserves_full_prefix_and_direction(self) -> None:
        subject = "Entity/Workflow//Daily.Status:Active"
        self.assertEqual(
            [
                ("Entity", None, None),
                ("Entity/Workflow", "Entity", "NARROWER_THAN"),
                ("Entity/Workflow//Daily", "Entity/Workflow", "INSTANCE_OF"),
                ("Entity/Workflow//Daily.Status", "Entity/Workflow//Daily", "IS_PROPERTY_OF"),
                (
                    "Entity/Workflow//Daily.Status:Active",
                    "Entity/Workflow//Daily.Status",
                    "IS_ALLOWED_VALUE_OF",
                ),
            ],
            path_steps(subject),
        )

        graph, provenance = graph_for(subject)
        names = {row["id"]: row["identity"] for row in graph["nodes"]}
        edges = {
            (row["kind"], names[row["relation_source"]], names[row["relation_target"]])
            for row in graph["edges"]
        }
        self.assertIn(
            ("INSTANCE_OF", "Entity/Workflow//Daily", "Entity/Workflow"),
            edges,
        )
        self.assertIn(
            ("IS_PROPERTY_OF", "Entity/Workflow//Daily.Status", "Entity/Workflow//Daily"),
            edges,
        )
        self.assertEqual("not_performed", graph["native_admission"])
        self.assertEqual("Entity/Workflow//Daily.Status:Active", provenance["occurrences"][0]["subject"])

    def test_value_and_instance_steps_remain_distinct(self) -> None:
        self.assertEqual(
            [
                ("Entity", None, None),
                ("Entity/Type", "Entity", "NARROWER_THAN"),
                ("Entity/Type:Workflow", "Entity/Type", "IS_ALLOWED_VALUE_OF"),
                ("Entity/Type:Workflow//Daily", "Entity/Type:Workflow", "INSTANCE_OF"),
            ],
            path_steps("Entity/Type:Workflow//Daily"),
        )

    def test_old_operators_keep_their_existing_kinds(self) -> None:
        self.assertEqual(
            [
                ("Entity", None, None),
                ("Entity/Property", "Entity", "NARROWER_THAN"),
                ("Entity/Property.Status", "Entity/Property", "IS_PROPERTY_OF"),
                (
                    "Entity/Property.Status:Active",
                    "Entity/Property.Status",
                    "IS_ALLOWED_VALUE_OF",
                ),
            ],
            path_steps("Entity/Property.Status:Active"),
        )

    def test_containment_directions_and_counts_normalize_to_one_fact(self) -> None:
        first, _ = graph_for("Part {1+}+>{2} Whole")
        second, _ = graph_for("Whole {2}<+{1+} Part")
        self.assertEqual(first["edges"], second["edges"])
        edge = first["edges"][0]
        names = {row["id"]: row["identity"] for row in first["nodes"]}
        self.assertEqual(("IS_CONTAINED_BY", "Part", "Whole"),
                         (edge["kind"], names[edge["relation_source"]], names[edge["relation_target"]]))
        self.assertEqual({"minimum": 1, "maximum": None}, edge["forward_cardinality"])
        self.assertEqual({"minimum": 2, "maximum": 2}, edge["reverse_cardinality"])

    def test_classification_is_one_direct_fact_with_ordinary_endpoints(self) -> None:
        first, _ = graph_for("Entity >| Classification")
        second, _ = graph_for("Classification |< Entity")
        self.assertEqual(first["edges"], second["edges"])
        self.assertEqual("HAS_CLASSIFICATION", first["edges"][0]["kind"])
        self.assertTrue(all("kind" not in row for row in first["nodes"]))

    def test_relative_qualification_is_whole_entity_and_resolves_property_context(self) -> None:
        graph, _ = graph_for("Root/X/(.Property:Value)")
        names = {row["id"]: row["identity"] for row in graph["nodes"]}
        edges = {(row["kind"], names[row["relation_source"]], names[row["relation_target"]])
                 for row in graph["edges"]}
        self.assertIn(("NARROWER_THAN", "Root/X/(.Property:Value)", "Root/X"), edges)
        self.assertIn(("IS_PROPERTY_OF", "Root/X.Property", "Root/X"), edges)
        self.assertIn(("IS_ALLOWED_VALUE_OF", "Root/X.Property:Value", "Root/X.Property"), edges)
        self.assertNotIn("Property:Value", names.values())

    def test_formats_counts_and_declared_reference_do_not_create_terms(self) -> None:
        graph, _ = graph_for("X:Value[Text]{1+}")
        self.assertEqual({"X", "X:Value"}, {row["identity"] for row in graph["nodes"]})
        value = next(row for row in graph["nodes"] if row["identity"] == "X:Value")
        self.assertEqual("Text", value["value_format"])
        self.assertEqual({"minimum": 1, "maximum": None}, value["value_cardinality"])
        reference, _ = graph_for("@(Root/X.Property)")
        self.assertEqual(["Root/X.Property"], [row["identity"] for row in reference["nodes"]])
        self.assertEqual([], reference["edges"])

    def test_named_relation_retains_canonical_direct_direction_and_counts(self) -> None:
        graph, _ = graph_for("Left {0+}((USES)){1} Right")
        self.assertEqual("USES", graph["edges"][0]["kind"])
        self.assertEqual({"minimum": 0, "maximum": None}, graph["edges"][0]["forward_cardinality"])

    def test_reverse_named_relation_normalizes_one_canonical_fact_and_preserves_written_form(self) -> None:
        forward, _ = graph_for("Step {1}((IS_CONTAINED_BY)){2} Workflow")
        reverse, _ = graph_for("Workflow {2}<((IS_CONTAINED_BY)){1} Step")
        self.assertEqual(forward["edges"], reverse["edges"])
        names = {row["id"]: row["identity"] for row in reverse["nodes"]}
        edge = reverse["edges"][0]
        self.assertEqual(("IS_CONTAINED_BY", "Step", "Workflow"),
                         (edge["kind"], names[edge["relation_source"]], names[edge["relation_target"]]))
        self.assertEqual({"minimum": 1, "maximum": 1}, edge["forward_cardinality"])
        self.assertEqual({"minimum": 2, "maximum": 2}, edge["reverse_cardinality"])
        parsed = subject_notation.parse_subject_expression("Workflow {2}<((IS_CONTAINED_BY)){1} Step")
        self.assertEqual("Workflow {2}<((IS_CONTAINED_BY)){1} Step", subject_notation.render_subject(parsed))

    def test_named_relation_chains_and_groups_keep_each_written_direction(self) -> None:
        graph, _ = graph_for("(Step) ((RUN)) Workflow <((IS_CONTAINED_BY)) Part")
        names = {row["id"]: row["identity"] for row in graph["nodes"]}
        edges = {(row["kind"], names[row["relation_source"]], names[row["relation_target"]]) for row in graph["edges"]}
        self.assertEqual({("RUN", "Step", "Workflow"), ("IS_CONTAINED_BY", "Part", "Workflow")}, edges)
        for invalid in ("Step <((IS_CONTAINED_BY) Workflow", "Step ((IS_CONTAINED_BY))> Workflow"):
            with self.subTest(invalid=invalid), self.assertRaises(subject_notation.SubjectNotationError):
                subject_notation.parse_subject_expression(invalid)

    def test_logical_head_grouping_does_not_create_another_entity(self) -> None:
        direct, _ = graph_for("Root/X.Property")
        grouped, _ = graph_for("(Root/X).Property")
        self.assertEqual(direct["nodes"], grouped["nodes"])
        self.assertEqual(direct["edges"], grouped["edges"])

    def test_conflicting_value_annotations_fail_instead_of_discarding_a_constraint(self) -> None:
        with self.assertRaisesRegex(ValueError, "conflicting Subject projection metadata"):
            compose_current_graph([{
                "source": source(),
                "subjects": {"governs": "X:Value[Text]", "depends_on": ["X:Value[Number]"]},
            }])

    def test_invalid_expression_fails_without_a_literal_node(self) -> None:
        with self.assertRaisesRegex(ValueError, "Subject projection failed"):
            graph_for("X///Broken")


if __name__ == "__main__":
    unittest.main()
