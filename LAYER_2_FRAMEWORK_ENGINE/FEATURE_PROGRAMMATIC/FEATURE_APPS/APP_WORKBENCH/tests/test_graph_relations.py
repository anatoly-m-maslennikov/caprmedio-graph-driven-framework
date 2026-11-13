# CA-E-676@15
# CA-E-677@30
"""Native graph relation projection tests."""

from __future__ import annotations

import json
from pathlib import Path
import sys
import unittest


APP_ROOT = Path(__file__).resolve().parents[2]
sys.path[:0] = [str(APP_ROOT), str(Path(__file__).parent)]

from APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.graph_store import graph_relations  # noqa: E402
from APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.query_store import QueryStore  # noqa: E402
from smalltest_support import extension_directory  # noqa: E402


class GraphRelationsTests(unittest.TestCase):
    def setUp(self) -> None:
        self.store = QueryStore(extension_directory=extension_directory(APP_ROOT.parents[2]))
        self.addCleanup(self.store.close)

    @staticmethod
    def atom(ref: str, edges: list[dict], *, version: int = 1) -> dict:
        return {
            "source_path": f"{ref}.md", "status_group": "Current", "id": ref,
            "ref": ref, "version": version, "status": "Active",
            "current_scope_unit": None, "claim_target_scope_unit": None,
            "role": "Requirement", "form": "Declaration", "tier": 1,
            "updated_at": None, "header_json": {}, "content_markdown": "",
            "content_properties_json": [], "relation_edges_json": edges,
            "hash": ref,
        }

    @staticmethod
    def scope(name: str, edges: list[dict]) -> dict:
        return {
            "name": name, "scope_unit_id": None, "parent_name": None,
            "declared_label": None, "ordered": False, "order_number": None,
            "declaration_source_path": f"{name}.md", "declaration_version": 1,
            "relation_edges_json": edges, "hash": name,
        }

    @staticmethod
    def edge(source_kind: str, source_ref: str, target_kind: str, target_ref: str,
             relation_type: str, derived: bool = False) -> dict:
        return {
            "source_kind": source_kind, "source_ref": source_ref,
            "target_kind": target_kind, "target_ref": target_ref,
            "relation_type": relation_type, "derived": derived,
        }

    def test_reads_outgoing_native_edges_with_typed_references(self) -> None:
        self.store.replace(
            [
                self.atom("A", [self.edge("Atom", "A", "Atom", "B", "CONTAINS")]),
                self.atom("B", [self.edge("Atom", "B", "Scope Unit", "A", "CONTAINS", True)]),
            ],
            [self.scope("A", [self.edge("Scope Unit", "A", "Atom", "A", "DEPENDS_ON")])],
        )

        self.assertEqual(
            {
                ("Atom", "A"): {"CONTAINS": [{"kind": "Atom", "reference": "B", "derived": False}]},
                ("Atom", "B"): {"CONTAINS": [{"kind": "Scope Unit", "reference": "A", "derived": True}]},
                ("Scope Unit", "A"): {"DEPENDS_ON": [{"kind": "Atom", "reference": "A", "derived": False}]},
            },
            graph_relations(self.store._connection, has_edges=True),
        )

    def test_returns_empty_when_the_native_graph_has_no_edges(self) -> None:
        self.store.replace([self.atom("A", [])], [self.scope("A", [])])
        self.assertEqual({}, graph_relations(self.store._connection, has_edges=True))
        self.assertEqual({}, graph_relations(self.store._connection, has_edges=False))
        self.assertEqual([], self.store._connection.execute("SELECT * FROM relations").fetchall())
        self.assertEqual(
            ["VARCHAR"] * 5 + ["BOOLEAN"],
            [row[1] for row in self.store._connection.execute("DESCRIBE relations").fetchall()],
        )

    def test_flat_relations_follow_rebuild_and_incremental_updates(self) -> None:
        connection = self.store._connection
        query = "SELECT * FROM relations ORDER BY source_ref, target_ref"
        self.assertEqual([], connection.execute(query).fetchall())
        initial = [self.atom("A", [self.edge("Atom", "A", "Atom", "B", "LINKS")])]
        self.store.replace(initial, [], relation_types={"LINKS"})
        self.assertEqual([("Atom", "A", "Atom", "B", "LINKS", False)], connection.execute(query).fetchall())
        updated = [self.atom("A", [self.edge("Atom", "A", "Atom", "C", "LINKS", True)], version=2)]
        self.assertTrue(self.store.apply(updated, [], relation_types={"LINKS"}))
        self.assertEqual([("Atom", "A", "Atom", "C", "LINKS", True)], connection.execute(query).fetchall())
        result = self.store.run(query)
        self.assertEqual([["Atom", "A", "Atom", "C", "LINKS", True]], result["rows"])
        changed_type = [self.atom("A", [self.edge("Atom", "A", "Atom", "D", "CONTAINS")], version=3)]
        self.assertTrue(self.store.apply(changed_type, [], relation_types={"CONTAINS"}))
        self.assertEqual([("Atom", "A", "Atom", "D", "CONTAINS", False)], connection.execute(query).fetchall())
        self.store.replace([], [], relation_types=set())
        self.assertEqual([], connection.execute(query).fetchall())

    def test_incremental_apply_updates_graph_without_reinserting_unrelated_atom(self) -> None:
        relation_types = {"CONTAINS", "IS_CONTAINED_BY", "LINKS"}
        initial = [
            self.atom("A", [self.edge("Atom", "A", "Atom", "B", "CONTAINS")]),
            self.atom("B", [self.edge("Atom", "B", "Atom", "A", "IS_CONTAINED_BY", True)]),
            self.atom("C", []),
            self.atom("UNRELATED", []),
        ]
        self.store.replace(initial, [], relation_types=relation_types)
        unrelated_before = self.store._connection.execute(
            "SELECT rowid, hash FROM atoms WHERE reference = 'UNRELATED'"
        ).fetchone()

        retargeted = [
            self.atom("A", [
                self.edge("Atom", "A", "Atom", "B", "LINKS"),
                self.edge("Atom", "A", "Atom", "C", "CONTAINS"),
            ], version=2),
            self.atom("B", []),
            self.atom("C", [self.edge("Atom", "C", "Atom", "A", "IS_CONTAINED_BY", True)]),
            self.atom("UNRELATED", []),
        ]
        self.assertTrue(self.store.apply(retargeted, [], relation_types=relation_types))

        self.assertEqual(
            [("A", "C", False)],
            self.store._connection.execute(
                'FROM GRAPH_TABLE (caprmedio MATCH '
                '(source:Reference)-[edge:"CONTAINS"]->(target:Reference) '
                'COLUMNS (source.ref, target.ref, edge.derived))'
            ).fetchall(),
        )
        self.assertEqual(
            [("A", "B", False)],
            self.store._connection.execute(
                'FROM GRAPH_TABLE (caprmedio MATCH '
                '(source:Reference)-[edge:"LINKS"]->(target:Reference) '
                'COLUMNS (source.ref, target.ref, edge.derived))'
            ).fetchall(),
        )
        relations = dict(self.store._connection.execute(
            'SELECT reference, "header.relations" FROM atoms WHERE reference IN (\'A\', \'B\', \'C\')'
        ).fetchall())
        self.assertEqual(
            {"CONTAINS": [{"kind": "Atom", "reference": "C", "derived": False}],
             "LINKS": [{"kind": "Atom", "reference": "B", "derived": False}]},
            json.loads(relations["A"]),
        )
        self.assertEqual({}, json.loads(relations["B"]))
        self.assertEqual(
            {"IS_CONTAINED_BY": [{"kind": "Atom", "reference": "A", "derived": True}]},
            json.loads(relations["C"]),
        )
        self.assertEqual(
            {
                ("Atom", "A"): {
                    "CONTAINS": [{"kind": "Atom", "reference": "C", "derived": False}],
                    "LINKS": [{"kind": "Atom", "reference": "B", "derived": False}],
                },
                ("Atom", "C"): {
                    "IS_CONTAINED_BY": [{"kind": "Atom", "reference": "A", "derived": True}],
                },
            },
            graph_relations(self.store._connection, has_edges=True),
        )
        self.assertEqual(
            unrelated_before,
            self.store._connection.execute(
                "SELECT rowid, hash FROM atoms WHERE reference = 'UNRELATED'"
            ).fetchone(),
        )

        links_removed = [
            self.atom("A", [self.edge("Atom", "A", "Atom", "C", "CONTAINS")], version=3),
            self.atom("B", []),
            self.atom("C", [self.edge("Atom", "C", "Atom", "A", "IS_CONTAINED_BY", True)]),
            self.atom("UNRELATED", []),
        ]
        self.assertTrue(self.store.apply(links_removed, [], relation_types=relation_types))
        self.assertEqual(
            [],
            self.store._connection.execute(
                'FROM GRAPH_TABLE (caprmedio MATCH '
                '(source:Reference)-[edge:"LINKS"]->(target:Reference) '
                'COLUMNS (source.ref, target.ref))'
            ).fetchall(),
        )


if __name__ == "__main__":
    unittest.main()
