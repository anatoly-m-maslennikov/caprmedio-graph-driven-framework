# CA-E-673@2
# CA-E-674@4
# CA-E-676@3
# CA-E-677@6

from __future__ import annotations

from contextlib import redirect_stderr
import hashlib
from io import StringIO
import sys
import unittest
from pathlib import Path


APP_ROOT = Path(__file__).resolve().parents[2]
sys.path[:0] = [str(APP_ROOT), str(Path(__file__).parent)]

from APP_WORKBENCH.query_store import QueryStore  # noqa: E402
from APP_WORKBENCH.relations import canonical  # noqa: E402
from smalltest_support import extension_directory  # noqa: E402


class QueryStoreTest(unittest.TestCase):
    def setUp(self) -> None:
        self.store = QueryStore(extension_directory=extension_directory(APP_ROOT.parents[2]))

    def tearDown(self) -> None:
        self.store.close()

    @staticmethod
    def atom(ref: str | None, edges: list[dict] | None = None, *, source_path: str | None = None) -> dict:
        base_id = ref.split("@", 1)[0] if ref else None
        return {
            "source_path": source_path or f"{ref or 'anonymous'}.md",
            "status_group": "Draft" if ref and "@" in ref else "Current",
            "id": base_id,
            "ref": ref,
            "version": 2 if ref and "@" in ref else 1,
            "status": "Active",
            "current_scope_unit": None,
            "claim_target_scope_unit": None,
            "role": "Requirement",
            "form": "Declaration",
            "tier": 4,
            "updated_at": None,
            "header_json": {"present": True, "nested": {"zero": 0, "empty": None}},
            "content_markdown": "# Claim\n",
            "content_properties_json": [],
            "relation_edges_json": edges or [],
            "hash": f"atom-{ref or 'anonymous'}",
        }

    @staticmethod
    def scope(name: str, edges: list[dict] | None = None) -> dict:
        return {
            "name": name,
            "scope_unit_id": None,
            "parent_name": None,
            "declared_label": None,
            "ordered": False,
            "order_number": None,
            "declaration_source_path": f"{name}.declaration.md",
            "declaration_version": 1,
            "relation_edges_json": edges or [],
            "hash": f"scope-{name}",
        }

    @staticmethod
    def edge(source_kind: str, source_ref: str, target_kind: str, target_ref: str,
             relation_type: str = "CONTAINS", derived: bool = False) -> dict:
        return {
            "source_kind": source_kind,
            "source_ref": source_ref,
            "target_kind": target_kind,
            "target_ref": target_ref,
            "relation_type": relation_type,
            "derived": derived,
        }

    @staticmethod
    def mapping_hash(value: dict) -> str:
        return hashlib.sha256(canonical(value).encode("utf-8")).hexdigest()

    def test_exact_public_schema_cte_and_direct_replacement(self) -> None:
        self.store.replace([self.atom("A"), self.atom(None)], [self.scope("S")])
        schema = self.store.run(
            "SELECT table_name, column_name FROM information_schema.columns "
            "WHERE table_schema = 'main' AND table_name NOT LIKE '__duckpgq_%' "
            "ORDER BY table_name, ordinal_position"
        )["rows"]
        self.assertEqual(
            [
                ["atoms", "source_path"], ["atoms", "status_group"], ["atoms", "id"],
                ["atoms", "ref"], ["atoms", "version"], ["atoms", "status"],
                ["atoms", "current_scope_unit"], ["atoms", "claim_target_scope_unit"],
                ["atoms", "role"], ["atoms", "form"], ["atoms", "tier"],
                ["atoms", "updated_at"], ["atoms", "header_json"],
                ["atoms", "content_markdown"], ["atoms", "content_properties_json"],
                ["atoms", "relation_edges_json"], ["atoms", "hash"],
                ["scope_units", "name"], ["scope_units", "scope_unit_id"],
                ["scope_units", "parent_name"], ["scope_units", "declared_label"],
                ["scope_units", "ordered"], ["scope_units", "order_number"],
                ["scope_units", "declaration_source_path"], ["scope_units", "declaration_version"],
                ["scope_units", "relation_edges_json"], ["scope_units", "hash"],
            ],
            schema,
        )
        self.assertEqual(
            [[2]],
            self.store.run("WITH source AS (SELECT * FROM atoms) SELECT count(*) FROM source")["rows"],
        )
        connection = self.store._connection
        self.store.replace([], [])
        self.assertIs(connection, self.store._connection)
        self.assertEqual({"valid": True, "row_count": 0, "column_count": 17}, self.store.check("SELECT * FROM atoms"))

    def test_native_admission_errors_leave_a_valid_connection(self) -> None:
        self.assertEqual([[1]], self.store.run("-- comment ;\nSELECT 1; /* comment ; */")["rows"])
        self.assertEqual(
            [[""]],
            self.store.run("SELECT value FROM duckdb_settings() WHERE name = 'temp_directory'")["rows"],
        )
        with self.assertRaises(ValueError):
            self.store.run("SELECT 1; SELECT 2")
        with self.assertRaises(ValueError):
            self.store.run("INSERT INTO atoms VALUES ('bad')")
        with self.assertRaises(ValueError):
            self.store.run("ATTACH 'outside.duckdb' AS outside")
        with self.assertRaises(RuntimeError):
            self.store.run("WITH attempted AS (DELETE FROM atoms RETURNING source_path) SELECT * FROM attempted")
        self.assertEqual([[0]], self.store.run("SELECT count(*) FROM atoms")["rows"])
        with self.assertRaises(RuntimeError):
            self.store.run("SELECT * FROM read_csv_auto('/private/tmp/workbench-does-not-exist.csv')")
        with self.assertRaises(RuntimeError):
            self.store.run("SELECT missing FROM atoms")
        self.assertEqual([[1]], self.store.run("SELECT 1")["rows"])

    def test_public_graph_table_direct_inverse_cycles_and_typed_identity(self) -> None:
        atoms = [
                self.atom("A", [self.edge("Atom", "A", "Atom", "B")]),
                self.atom("B", [
                    self.edge("Atom", "B", "Atom", "A", derived=True),
                    self.edge("Atom", "B", "Atom", "C"),
                    self.edge("Atom", "B", "Atom", "A@2-draft", "DRAFT_LINK"),
                ]),
                self.atom("C", [self.edge("Atom", "C", "Atom", "A")]),
                self.atom("A@2-draft"),
            ]
        scopes = [self.scope("A", [self.edge("Scope Unit", "A", "Atom", "A", "OWNS")])]
        self.store.replace(atoms, scopes)
        direct = self.store.run(
            "FROM GRAPH_TABLE (caprmedio "
            "MATCH (a:Reference)-[e:CONTAINS]->(b:Reference) "
            "COLUMNS (a.kind AS source_kind, a.ref AS source_ref, "
            "b.kind AS target_kind, b.ref AS target_ref, "
            "e.relation_type AS relation_type, e.derived AS derived)) "
            "ORDER BY source_ref, target_ref, derived"
        )["rows"]
        self.assertEqual(
            [
                ["Atom", "A", "Atom", "B", "CONTAINS", False],
                ["Atom", "B", "Atom", "A", "CONTAINS", True],
                ["Atom", "B", "Atom", "C", "CONTAINS", False],
                ["Atom", "C", "Atom", "A", "CONTAINS", False],
            ],
            direct,
        )
        mapping_hashes = self.store.run(
            "SELECT * FROM GRAPH_TABLE (caprmedio "
            "MATCH (a:Reference)-[e:CONTAINS]->(b:Reference) "
            "COLUMNS (a.hash AS source_hash, b.hash AS target_hash, e.hash AS edge_hash, "
            "a.ref AS source_ref, b.ref AS target_ref)) "
            "WHERE source_ref = 'A' AND target_ref = 'B'"
        )["rows"]
        self.assertEqual(
            [[
                self.mapping_hash({"kind": "Atom", "ref": "A"}),
                self.mapping_hash({"kind": "Atom", "ref": "B"}),
                self.mapping_hash(self.edge("Atom", "A", "Atom", "B")),
                "A",
                "B",
            ]],
            mapping_hashes,
        )
        self.store.replace(atoms, scopes)
        self.assertEqual(
            mapping_hashes,
            self.store.run(
                "SELECT * FROM GRAPH_TABLE (caprmedio "
                "MATCH (a:Reference)-[e:CONTAINS]->(b:Reference) "
                "COLUMNS (a.hash AS source_hash, b.hash AS target_hash, e.hash AS edge_hash, "
                "a.ref AS source_ref, b.ref AS target_ref)) "
                "WHERE source_ref = 'A' AND target_ref = 'B'"
            )["rows"],
        )
        inverse = self.store.run(
            "SELECT * FROM GRAPH_TABLE (caprmedio "
            "MATCH (target:Reference)<-[e:CONTAINS]-(source:Reference) "
            "COLUMNS (target.ref AS target_ref, source.ref AS source_ref, e.derived AS derived)) "
            "WHERE target_ref = 'B'"
        )["rows"]
        self.assertEqual([["B", "A", False]], inverse)
        draft = self.store.run(
            "FROM GRAPH_TABLE (caprmedio "
            "MATCH (a:Reference)-[e:DRAFT_LINK]->(b:Reference) "
            "COLUMNS (a.kind AS source_kind, a.ref AS source_ref, b.kind AS target_kind, b.ref AS target_ref))"
        )["rows"]
        self.assertEqual([["Atom", "B", "Atom", "A@2-draft"]], draft)
        owned = self.store.run(
            "FROM GRAPH_TABLE (caprmedio "
            "MATCH (a:Reference)-[e:OWNS]->(b:Reference) "
            "COLUMNS (a.kind AS source_kind, a.ref AS source_ref, b.kind AS target_kind, b.ref AS target_ref))"
        )["rows"]
        self.assertEqual([["Scope Unit", "A", "Atom", "A"]], owned)
        reachable = self.store.run(
            "WITH RECURSIVE edges AS (FROM GRAPH_TABLE (caprmedio "
            "MATCH (a:Reference)-[e:CONTAINS]->(b:Reference) "
            "COLUMNS (a.kind AS source_kind, a.ref AS source_ref, b.kind AS target_kind, b.ref AS target_ref))), "
            "reach(kind, ref) AS (SELECT 'Atom', 'A' UNION "
            "SELECT target_kind, target_ref FROM reach JOIN edges "
            "ON reach.kind = source_kind AND reach.ref = source_ref) "
            "SELECT kind, ref FROM reach ORDER BY ref"
        )["rows"]
        self.assertEqual([["Atom", "A"], ["Atom", "B"], ["Atom", "C"]], reachable)

    def test_native_graph_ctes_select_labels_directions_and_isolated_seed(self) -> None:
        atoms = [
            self.atom("A", [self.edge("Atom", "A", "Atom", "B")]),
            self.atom("B", [
                self.edge("Atom", "B", "Atom", "C"),
                self.edge("Atom", "B", "Atom", "A@2-draft", "DRAFT_LINK"),
            ]),
            self.atom("C", [self.edge("Atom", "C", "Atom", "A")]),
            self.atom("A@2-draft"),
            self.atom("ISOLATED"),
        ]
        self.store.replace(atoms, [])
        multi_label_direction = self.store.run(
            "WITH selected AS (FROM GRAPH_TABLE (caprmedio "
            "MATCH (seed:Reference)<-[draft:DRAFT_LINK]-(middle:Reference)-[contains:CONTAINS]->(target:Reference) "
            "WHERE seed.ref = 'A@2-draft' "
            "COLUMNS (seed.kind AS seed_kind, seed.ref AS seed_ref, "
            "middle.kind AS middle_kind, middle.ref AS middle_ref, "
            "target.kind AS target_kind, target.ref AS target_ref))) "
            "SELECT * FROM selected"
        )["rows"]
        self.assertEqual(
            [["Atom", "A@2-draft", "Atom", "B", "Atom", "C"]],
            multi_label_direction,
        )
        isolated = self.store.run(
            "WITH RECURSIVE edges AS (FROM GRAPH_TABLE (caprmedio "
            "MATCH (source:Reference)-[e:CONTAINS]->(target:Reference) "
            "COLUMNS (source.kind AS source_kind, source.ref AS source_ref, "
            "target.kind AS target_kind, target.ref AS target_ref))), "
            "reach(kind, ref) AS (SELECT 'Atom', 'ISOLATED' UNION "
            "SELECT target_kind, target_ref FROM reach JOIN edges "
            "ON reach.kind = source_kind AND reach.ref = source_ref) "
            "SELECT kind, ref FROM reach"
        )["rows"]
        self.assertEqual([["Atom", "ISOLATED"]], isolated)
        aggregate = self.store.run(
            "WITH graph_edges AS (FROM GRAPH_TABLE (caprmedio "
            "MATCH (source:Reference)-[e:CONTAINS]->(target:Reference) "
            "COLUMNS (source.ref AS source_ref, target.ref AS target_ref))) "
            "SELECT graph_edges.source_ref, count(*) AS edge_count FROM graph_edges "
            "JOIN atoms ON atoms.ref = graph_edges.source_ref "
            "WHERE atoms.status_group = 'Current' GROUP BY graph_edges.source_ref "
            "ORDER BY graph_edges.source_ref"
        )["rows"]
        self.assertEqual([["A", 1], ["B", 1], ["C", 1]], aggregate)

    def test_result_delivery_is_lossless_and_refresh_failure_stops_service(self) -> None:
        result = self.store.run(
            "SELECT 9007199254740992::HUGEINT AS wide, 1.20::DECIMAL(4,2) AS decimal, "
            "DATE '2026-11-04' AS day, TIME '01:02:03' AS moment, "
            "TIMESTAMP '2026-11-04 01:02:03' AS stamped, CAST('bin' AS BLOB) AS binary, "
            "[9007199254740992::HUGEINT, 9007199254740993::HUGEINT] AS nested_wide, "
            "[CAST('x' AS BLOB)] AS nested_binary, "
            "{'wide': 9007199254740992::HUGEINT, 'binary': CAST('x' AS BLOB)} AS mapped"
        )["rows"][0]
        self.assertEqual("9007199254740992", result[0])
        self.assertEqual("1.20", result[1])
        self.assertEqual("2026-11-04", result[2])
        self.assertEqual("01:02:03", result[3])
        self.assertEqual("2026-11-04T01:02:03", result[4])
        self.assertEqual("base64:Ymlu", result[5])
        self.assertEqual(["9007199254740992", "9007199254740993"], result[6])
        self.assertEqual(["base64:eA=="], result[7])
        self.assertEqual({"wide": "9007199254740992", "binary": "base64:eA=="}, result[8])
        with self.assertRaisesRegex(ValueError, "NaN or infinity"):
            self.store.run("SELECT 'NaN'::DOUBLE")
        self.assertEqual([[1]], self.store.run("SELECT 1")["rows"])
        with self.assertRaises(RuntimeError):
            self.store.replace([{"source_path": "invalid.md"}], [])
        with self.assertRaisesRegex(RuntimeError, "restart required"):
            self.store.run("SELECT 1")

    def test_internal_management_failure_requires_restart(self) -> None:
        stderr = StringIO()
        with redirect_stderr(stderr), self.assertRaisesRegex(RuntimeError, "query failed"):
            self.store.run("SELECT * FROM drop_property_graph()")
        self.assertIn("query store unavailable", stderr.getvalue())
        with self.assertRaisesRegex(RuntimeError, "restart required"):
            self.store.run("SELECT 1")


if __name__ == "__main__":
    unittest.main()
