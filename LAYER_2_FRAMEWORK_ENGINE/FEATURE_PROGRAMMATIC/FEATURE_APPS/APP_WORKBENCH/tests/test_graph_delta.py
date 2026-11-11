# CA-E-677@14
"""Incremental Workbench graph/public projection checks against real DuckPGQ."""

from __future__ import annotations

import copy
from dataclasses import replace
from pathlib import Path
import sys
import unittest
from unittest.mock import patch


APP_ROOT = Path(__file__).resolve().parents[2]
sys.path[:0] = [str(APP_ROOT), str(Path(__file__).parent)]

from APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.index_delta import MaterializationDelta  # noqa: E402
from APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.projection_delta import apply, snapshot  # noqa: E402
from APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.graph_store import graph_relations  # noqa: E402
from APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.query_store import QueryStore  # noqa: E402
from APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.content_schema import (  # noqa: E402
    ContentSchema,
    DeclarationSource,
)
from smalltest_support import extension_directory  # noqa: E402


class GraphDeltaTest(unittest.TestCase):
    relation_types = {"CONTAINS", "IS_CONTAINED_BY"}

    def setUp(self) -> None:
        self.store = QueryStore(extension_directory=extension_directory(APP_ROOT.parents[2]))
        self.addCleanup(self.store.close)

    @staticmethod
    def edge(source: str, relation: str, target: str, *, derived: bool = False) -> dict:
        return {
            "source_kind": "Atom", "source_ref": source,
            "target_kind": "Atom", "target_ref": target,
            "relation_type": relation, "derived": derived,
        }

    @staticmethod
    def atom(
        reference: str, *, edges: list[dict] | None = None, version: int = 1, path: str | None = None,
    ) -> dict:
        return {
            "source_path": path or f"{reference}.md", "status_group": "Current", "id": reference,
            "ref": reference, "version": version, "status": "Active",
            "current_scope_unit": None, "claim_target_scope_unit": None,
            "role": "Requirement", "form": "Declaration", "tier": 1,
            "updated_at": None, "header_json": {}, "content_markdown": "",
            "content_properties_json": [], "relation_edges_json": edges or [], "hash": reference,
        }

    def replace(self, atoms: list[dict]) -> None:
        self.store.replace(atoms, [], relation_types=self.relation_types)

    def apply_delta(
        self, atoms: list[dict], delta: MaterializationDelta,
    ) -> tuple[object, object]:
        previous = self.store._projection
        assert previous is not None
        connection = self.store._connection
        connection.execute("BEGIN TRANSACTION")
        try:
            current, change = apply(
                connection, previous, atoms, [], self.relation_types,
                self.store._header_schema, self.store._content_schema, delta=delta,
            )
            connection.execute("COMMIT")
        except BaseException:
            connection.execute("ROLLBACK")
            raise
        self.store._projection = current
        return current, change

    def test_delta_has_full_projection_parity_without_graph_state_scan(self) -> None:
        old_a = self.atom("A", edges=[self.edge("A", "CONTAINS", "B")])
        old_b = self.atom("B", edges=[self.edge("B", "IS_CONTAINED_BY", "A", derived=True)])
        self.replace([old_a, old_b, self.atom("UNRELATED")])
        previous = self.store._projection
        assert previous is not None
        new_a = self.atom("A", edges=[self.edge("A", "CONTAINS", "C")], version=2)
        new_b = self.atom("B")
        new_c = self.atom("C", edges=[self.edge("C", "IS_CONTAINED_BY", "A", derived=True)])
        updated = [new_a, new_b, new_c, self.atom("UNRELATED")]
        expected = snapshot(
            updated, [], self.relation_types, self.store._header_schema, self.store._content_schema,
        )
        delta = MaterializationDelta(
            {"A.md": old_a, "B.md": old_b},
            {"A.md": new_a, "B.md": new_b, "C.md": new_c}, {}, {},
        )
        with (
            patch(
                "APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.projection_delta.graph_state",
                side_effect=AssertionError("ordinary delta must not scan full graph state"),
            ),
            patch(
                "APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.projection_delta._changed_keys",
                side_effect=AssertionError("ordinary delta must not scan all public rows"),
            ),
        ):
            current, _ = self.apply_delta(updated, delta)

        self.assertEqual(expected.atoms, current.atoms)
        self.assertEqual(expected.scopes, current.scopes)
        self.assertEqual(expected.graph.references, current.graph.references)
        self.assertEqual(expected.graph.edges, current.graph.edges)
        self.assertEqual(
            {("Atom", "A"): {"CONTAINS": [{"kind": "Atom", "reference": "C", "derived": False}]},
             ("Atom", "C"): {"IS_CONTAINED_BY": [{"kind": "Atom", "reference": "A", "derived": True}]}},
            graph_relations(self.store._connection, has_edges=True),
        )

    def test_delta_keeps_dangling_target_and_accepts_its_reappearance(self) -> None:
        source = self.atom("A", edges=[self.edge("A", "CONTAINS", "B")])
        target = self.atom("B")
        self.replace([source, target])

        self.apply_delta([source], MaterializationDelta({"B.md": target}, {}, {}, {}))
        self.assertEqual(
            [("Atom", "B")],
            self.store._connection.execute(
                "SELECT kind, ref FROM internal.reference WHERE ref = 'B'"
            ).fetchall(),
        )
        self.assertEqual(
            [], self.store._connection.execute("SELECT * FROM atoms WHERE reference = 'B'").fetchall(),
        )

        reappeared = self.atom("B", version=2)
        self.apply_delta([source, reappeared], MaterializationDelta({}, {"B.md": reappeared}, {}, {}))
        self.assertEqual(
            [("B",)], self.store._connection.execute("SELECT reference FROM atoms WHERE reference = 'B'").fetchall(),
        )
        self.assertEqual(
            [("Atom", "B")],
            self.store._connection.execute(
                "SELECT kind, ref FROM internal.reference WHERE ref = 'B'"
            ).fetchall(),
        )

    def test_delta_replaces_direct_and_inverse_only_rows(self) -> None:
        old_a = self.atom("A", edges=[self.edge("A", "CONTAINS", "B")])
        old_b = self.atom("B", edges=[self.edge("B", "IS_CONTAINED_BY", "A", derived=True)])
        self.replace([old_a, old_b, self.atom("UNRELATED")])
        new_a = self.atom("A", edges=[self.edge("A", "CONTAINS", "C")], version=2)
        new_b = self.atom("B")
        new_c = self.atom("C", edges=[self.edge("C", "IS_CONTAINED_BY", "A", derived=True)])

        self.apply_delta(
            [new_a, new_b, new_c, self.atom("UNRELATED")],
            MaterializationDelta(
                {"A.md": old_a, "B.md": old_b},
                {"A.md": new_a, "B.md": new_b, "C.md": new_c}, {}, {},
            ),
        )
        self.assertEqual(
            {
                ("Atom", "A"): {"CONTAINS": [{"kind": "Atom", "reference": "C", "derived": False}]},
                ("Atom", "C"): {"IS_CONTAINED_BY": [{"kind": "Atom", "reference": "A", "derived": True}]},
            },
            graph_relations(self.store._connection, has_edges=True),
        )
        self.assertEqual(
            [("UNRELATED",)],
            self.store._connection.execute("SELECT reference FROM atoms WHERE reference = 'UNRELATED'").fetchall(),
        )

    def test_delta_preserves_and_removes_self_loop_reference_counts(self) -> None:
        old = self.atom("A", edges=[self.edge("A", "CONTAINS", "A")])
        self.replace([old])
        previous = self.store._projection
        assert previous is not None
        revised = self.atom("A", version=2)

        current, _ = self.apply_delta(
            [revised], MaterializationDelta({"A.md": old}, {"A.md": revised}, {}, {}),
        )
        self.assertIs(previous.graph.edges["IS_CONTAINED_BY"], current.graph.edges["IS_CONTAINED_BY"])
        self.assertEqual(
            [("Atom", "A")],
            self.store._connection.execute("SELECT kind, ref FROM internal.reference").fetchall(),
        )
        self.apply_delta([], MaterializationDelta({"A.md": revised}, {}, {}, {}))
        self.assertEqual([], self.store._connection.execute("SELECT kind, ref FROM internal.reference").fetchall())

    def test_delta_moves_public_atom_without_reinserting_its_reference(self) -> None:
        old = self.atom("A", path="old/A.md")
        self.replace([old])
        moved = self.atom("A", version=2, path="new/A.md")

        self.apply_delta(
            [moved], MaterializationDelta({"old/A.md": old}, {"new/A.md": moved}, {}, {}),
        )

        self.assertEqual(
            [("new", "A.md", "A")],
            self.store._connection.execute(
                'SELECT "relative_path", filename, reference FROM atoms'
            ).fetchall(),
        )
        self.assertEqual(
            [("Atom", "A")], self.store._connection.execute("SELECT kind, ref FROM internal.reference").fetchall(),
        )

    def test_delta_accepts_content_schema_provenance_only_change(self) -> None:
        atom = self.atom("A")
        self.replace([atom])
        previous = self.store._projection
        assert previous is not None
        previous_schema = ContentSchema((), (), (DeclarationSource("A", 1, "A.md"),))
        current_schema = ContentSchema((), (), (DeclarationSource("A", 2, "A.md"),))
        previous = replace(previous, content_schema=previous_schema)
        connection = self.store._connection
        connection.execute("BEGIN TRANSACTION")
        current, change = apply(
            connection, previous, [atom], [], self.relation_types,
            self.store._header_schema, current_schema, delta=MaterializationDelta({}, {}, {}, {}),
        )
        connection.execute("COMMIT")

        self.assertEqual(0, change.inserted_atoms)
        self.assertEqual(current_schema, current.content_schema)

    def test_rollback_does_not_mutate_previous_snapshot(self) -> None:
        old = self.atom("A")
        self.replace([old])
        previous = self.store._projection
        assert previous is not None
        before = copy.deepcopy(previous)
        new = self.atom("A", edges=[self.edge("A", "CONTAINS", "B")], version=2)
        connection = self.store._connection
        connection.execute("BEGIN TRANSACTION")
        current, _ = apply(
            connection, previous, [new], [], self.relation_types,
            self.store._header_schema, self.store._content_schema,
            delta=MaterializationDelta({"A.md": old}, {"A.md": new}, {}, {}),
        )
        connection.execute("ROLLBACK")

        self.assertEqual(before, previous)
        self.assertIn((".", "A.md"), current.atoms)
        self.assertEqual({}, graph_relations(connection, has_edges=True))


if __name__ == "__main__":
    unittest.main()
