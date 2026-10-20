"""Current-source ``//`` instance paths remain typed and non-authoritative."""

from __future__ import annotations

from pathlib import Path
import sys
import unittest


TOOL = Path(__file__).resolve().parents[1]
sys.path[:0] = [str(TOOL.parent), str(TOOL)]

from current_subject_graph import compose_current_graph, path_steps  # noqa: E402


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
        subject = "Entity/Workflow//Daily.Status: Active"
        self.assertEqual(
            [
                ("Entity", None, None),
                ("Entity/Workflow", "Entity", "NARROWER_THAN"),
                ("Entity/Workflow//Daily", "Entity/Workflow", "INSTANCE_OF"),
                ("Entity/Workflow//Daily.Status", "Entity/Workflow//Daily", "IS_BORNE_BY"),
                (
                    "Entity/Workflow//Daily.Status: Active",
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
            ("IS_BORNE_BY", "Entity/Workflow//Daily.Status", "Entity/Workflow//Daily"),
            edges,
        )
        self.assertEqual("not_performed", graph["native_admission"])
        self.assertEqual("Entity/Workflow//Daily.Status: Active", provenance["occurrences"][0]["subject"])

    def test_classifier_folding_stops_before_instance_separator(self) -> None:
        self.assertEqual(
            [
                ("Entity", None, None),
                ("Entity/Type: Workflow", "Entity", "NARROWER_THAN"),
                ("Entity/Type: Workflow//Daily", "Entity/Type: Workflow", "INSTANCE_OF"),
            ],
            path_steps("Entity/Type: Workflow//Daily"),
        )

    def test_old_operators_keep_their_existing_kinds(self) -> None:
        self.assertEqual(
            [
                ("Entity", None, None),
                ("Entity/Property", "Entity", "NARROWER_THAN"),
                ("Entity/Property.Status", "Entity/Property", "IS_BORNE_BY"),
                (
                    "Entity/Property.Status: Active",
                    "Entity/Property.Status",
                    "IS_ALLOWED_VALUE_OF",
                ),
            ],
            path_steps("Entity/Property.Status: Active"),
        )


if __name__ == "__main__":
    unittest.main()
