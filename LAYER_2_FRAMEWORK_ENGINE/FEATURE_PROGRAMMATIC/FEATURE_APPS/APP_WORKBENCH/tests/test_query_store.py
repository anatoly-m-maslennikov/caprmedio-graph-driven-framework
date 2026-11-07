# CA-E-751@1
# CA-E-780@4
# CA-E-676@11
# CA-E-677@20
# CA-M-472@1
from __future__ import annotations

from contextlib import redirect_stderr
import datetime as dt
import hashlib
from io import StringIO
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


APP_ROOT = Path(__file__).resolve().parents[2]
sys.path[:0] = [str(APP_ROOT), str(Path(__file__).parent)]

from APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.query_store import QueryStore  # noqa: E402
from APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.errors import (  # noqa: E402
    QueryExecutionError,
    WorkbenchUnavailableError,
)
from APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.relations import canonical  # noqa: E402
from APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.markdown_content import parse_content  # noqa: E402
from APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND import public_rows as public_rows_module  # noqa: E402
from APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.public_rows import SCOPE_FIELDS  # noqa: E402
from smalltest_support import extension_directory  # noqa: E402


class QueryStoreTest(unittest.TestCase):
    def setUp(self) -> None:
        self.store = QueryStore(extension_directory=extension_directory(APP_ROOT.parents[2]))

    def tearDown(self) -> None:
        self.store.close()

    @staticmethod
    def atom(
        ref: str | None,
        edges: list[dict] | None = None,
        *,
        source_path: str | None = None,
        body: str = "# Claim\n",
    ) -> dict:
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
            "header_json": {
                "atom_id": base_id,
                "version": 2 if ref and "@" in ref else 1,
                "status": "Active",
                "role": "Requirement",
                "form": "Declaration",
                "tier": 4,
                "present": True,
                "nested": {"zero": 0, "empty": None},
            },
            "content_markdown": body,
            "content_properties_json": parse_content(body, tolerate_duplicate_siblings=True),
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
        atom_fields = tuple(column for table, column in schema if table == "atoms")
        self.assertTrue({
            "relative path", "filename", "status_group", "reference", "header_atom_id",
            "header_version", "header_status", "header_relations", "hash",
        } <= set(atom_fields))
        self.assertFalse(any(field.startswith("content.") for field in atom_fields))
        self.assertEqual(
            [["atoms", field] for field in atom_fields]
            + [["change_log", field] for field in ("observed_at", "operation", "old_path", "new_path")]
            + [["scope_units", field] for field in SCOPE_FIELDS],
            schema,
        )
        self.assertEqual(
            [[2]],
            self.store.run("WITH source AS (SELECT * FROM atoms) SELECT count(*) FROM source")["rows"],
        )
        connection = self.store._connection
        self.store.replace([], [])
        self.assertIs(connection, self.store._connection)
        empty_atom_fields = self.store.schema()["tables"]["atoms"]
        self.assertEqual(
            {
                "valid": True,
                "row_count": 0,
                "column_count": len(empty_atom_fields),
                "sql": "SELECT * FROM atoms",
            },
            self.store.check("SELECT * FROM atoms"),
        )

    def test_schema_exposes_actual_status_literals_without_running_a_query(self) -> None:
        done = self.atom("B")
        done["status"] = "Done"
        done["header_json"]["status"] = "Done"
        self.store.replace([self.atom("A"), done], [])

        schema = self.store.schema()["tables"]

        status = next(column for column in schema["atoms"] if column["name"] == "header_status")
        self.assertEqual(["Active", "Done"], status["values"])

    def test_normal_source_edit_uses_delta_not_projection_replacement(self) -> None:
        unchanged = self.atom("B")
        self.store.replace([self.atom("A"), unchanged], [])
        edited = self.atom("A")
        edited["version"] = 2
        edited["header_json"]["version"] = 2

        with patch(
            "APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.query_store.insert_rows"
        ) as full_replace:
            changed = self.store.apply([edited, unchanged], [], relation_types=set())

        self.assertTrue(changed)
        full_replace.assert_not_called()
        self.assertEqual([["A", 2], ["B", 1]], self.store.run(
            "SELECT reference, header_version FROM atoms ORDER BY reference"
        )["rows"])

    def test_full_replace_projects_once_and_sql_matches_retained_snapshot(self) -> None:
        atoms = [
            self.atom("A", [self.edge("Atom", "A", "Scope Unit", "S")]),
            self.atom("B"),
        ]
        scopes = [self.scope("S")]
        with patch.object(
            public_rows_module, "projected_rows", wraps=public_rows_module.projected_rows,
        ) as project:
            self.store.replace(atoms, scopes, relation_types={"CONTAINS"})

        self.assertEqual(1, project.call_count)
        snapshot = self.store._projection
        assert snapshot is not None
        atom_fields = [column[0] for column in self.store._connection.execute(
            "SELECT * FROM atoms LIMIT 0"
        ).description]
        scope_fields = [column[0] for column in self.store._connection.execute(
            "SELECT * FROM scope_units LIMIT 0"
        ).description]
        atom_json = snapshot.header_schema.json_names | {"header_relations"}
        sql_atoms = [
            {
                name: json.loads(value) if name in atom_json and value is not None else value
                for name, value in zip(atom_fields, values, strict=True)
            }
            for values in self.store._connection.execute(
                'SELECT * FROM atoms ORDER BY "relative path", filename'
            ).fetchall()
        ]
        sql_scopes = [
            {
                name: json.loads(value) if name == "relations" and value is not None else value
                for name, value in zip(scope_fields, values, strict=True)
            }
            for values in self.store._connection.execute("SELECT * FROM scope_units ORDER BY name").fetchall()
        ]
        snapshot_atoms = sorted(
            snapshot.atoms.values(), key=lambda row: (row["relative path"], row["filename"]),
        )
        snapshot_scopes = sorted(snapshot.scopes.values(), key=lambda row: row["name"])
        self.assertEqual(snapshot_atoms, sql_atoms)
        self.assertEqual(snapshot_scopes, sql_scopes)
        self.assertEqual(
            [row["hash"] for row in snapshot_atoms], [row["hash"] for row in sql_atoms],
        )

    def test_failed_full_replace_keeps_the_published_snapshot(self) -> None:
        self.store.replace([self.atom("A")], [])
        previous_projection = self.store._projection
        previous_header_state = self.store._header_state

        with patch(
            "APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.query_store.insert_rows",
            side_effect=RuntimeError("write failed"),
        ), self.assertRaises(WorkbenchUnavailableError):
            self.store.replace([self.atom("B")], [])

        self.assertIs(previous_projection, self.store._projection)
        self.assertIs(previous_header_state, self.store._header_state)

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
            self.store.run("WITH attempted AS (DELETE FROM atoms RETURNING filename) SELECT * FROM attempted")
        self.assertEqual([[0]], self.store.run("SELECT count(*) FROM atoms")["rows"])
        with self.assertRaises(RuntimeError):
            self.store.run("SELECT * FROM read_csv_auto('/private/tmp/workbench-does-not-exist.csv')")
        with self.assertRaises(RuntimeError):
            self.store.run("SELECT missing FROM atoms")
        self.assertEqual([[1]], self.store.run("SELECT 1")["rows"])

    def test_native_ctas_conversion_failure_keeps_the_owner_available(self) -> None:
        with self.assertRaisesRegex(QueryExecutionError, "Could not convert"):
            self.store.run("SELECT CAST('not-an-integer' AS INTEGER)")
        self.assertEqual([[1]], self.store.run("SELECT 1")["rows"])

    def test_file_backed_materialized_pages_preserve_duplicate_metadata(self) -> None:
        with tempfile.TemporaryDirectory() as runtime:
            database_path = Path(runtime) / "workbench" / "projection.duckdb"
            store = QueryStore(
                extension_directory=extension_directory(APP_ROOT.parents[2]), database_path=database_path,
            )
            try:
                result = store.run(
                    "SELECT value FROM (VALUES (1), (2), (3)) AS source(value)", page_size=2,
                )
                self.assertTrue(database_path.is_file())
                self.assertEqual([[1], [2]], result["rows"])
                self.assertEqual(3, result["row_count"])
                self.assertEqual(1, result["column_count"])
                self.assertEqual(0, result["offset"])
                self.assertEqual(2, result["page_size"])
                self.assertTrue(result["has_more"])
                self.assertEqual(
                    [[3]], store.page(result["query_id"], offset=2, page_size=2)["rows"],
                )
                self.assertFalse(store.page(result["query_id"], offset=2, page_size=2)["has_more"])
                boundary = store.run("SELECT range AS value FROM range(101)", page_size=100)
                self.assertEqual(100, len(boundary["rows"]))
                self.assertEqual([[100]], store.page(boundary["query_id"], offset=100)["rows"])
                duplicate = store.run("SELECT 1 AS duplicate, 2 AS duplicate")
                self.assertEqual(
                    [
                        {"name": "duplicate", "type": "INTEGER", "has_values": True},
                        {"name": "duplicate", "type": "INTEGER", "has_values": True},
                    ],
                    duplicate["columns"],
                )
                self.assertEqual([[1, 2]], duplicate["rows"])
                visibility = store.run("SELECT NULL AS empty, 1 AS present")
                self.assertEqual(
                    [
                        {"name": "empty", "type": '"NULL"', "has_values": False},
                        {"name": "present", "type": "INTEGER", "has_values": True},
                    ],
                    visibility["columns"],
                )
                store.replace([self.atom("refreshed")], [])
                self.assertEqual(
                    [[1], [2]], store.page(result["query_id"], offset=0, page_size=2)["rows"],
                )
                self.assertEqual(
                    {
                        "valid": True,
                        "row_count": 3,
                        "column_count": 1,
                        "sql": "SELECT value FROM (VALUES (1), (2), (3)) AS source(value)",
                    },
                    store.check("SELECT value FROM (VALUES (1), (2), (3)) AS source(value)"),
                )
                with self.assertRaisesRegex(ValueError, "page_size"):
                    store.run("SELECT 1", page_size=0)
                with self.assertRaisesRegex(ValueError, "page_size"):
                    store.page(result["query_id"], offset=0, page_size=1001)
                with self.assertRaisesRegex(ValueError, "offset"):
                    store.page(result["query_id"], offset=-1)
            finally:
                store.close()
            restarted = QueryStore(
                extension_directory=extension_directory(APP_ROOT.parents[2]), database_path=database_path,
            )
            try:
                with self.assertRaisesRegex(ValueError, "unknown query_id"):
                    restarted.page(result["query_id"], offset=0)
                self.assertEqual(
                    [[0]],
                    restarted.run(
                        "SELECT count(*) FROM information_schema.tables "
                        "WHERE table_schema = 'workbench_results' "
                        f"AND table_name = 'query_{result['query_id']}'"
                    )["rows"],
                )
            finally:
                restarted.close()

    def test_timezone_aware_values_are_delivered_as_iso_strings(self) -> None:
        result = self.store.run("SELECT TIMESTAMPTZ '2026-11-04 12:00:00+00' AS observed_at")
        self.assertEqual(
            dt.datetime(2026, 11, 4, 12, tzinfo=dt.UTC),
            dt.datetime.fromisoformat(result["rows"][0][0]),
        )
        self.assertEqual("TIMESTAMP WITH TIME ZONE", result["columns"][0]["type"])

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
        public_rows = self.store.run(
            'SELECT "relative path", filename, reference, header_relations FROM atoms '
            "WHERE reference IN ('A', 'B') ORDER BY reference"
        )["rows"]
        self.assertEqual(
            [
                [".", "A.md", "A", {"CONTAINS": [{"kind": "Atom", "reference": "B", "derived": False}]}],
                [
                    ".", "B.md", "B",
                    {
                        "CONTAINS": [
                            {"kind": "Atom", "reference": "A", "derived": True},
                            {"kind": "Atom", "reference": "C", "derived": False},
                        ],
                        "DRAFT_LINK": [{"kind": "Atom", "reference": "A@2-draft", "derived": False}],
                    },
                ],
            ],
            [[path, filename, reference, json.loads(relations)]
             for path, filename, reference, relations in public_rows],
        )
        self.assertEqual(
            {},
            json.loads(self.store.run("SELECT header_relations FROM atoms WHERE reference = 'A@2-draft'")["rows"][0][0]),
        )
        self.assertEqual(
            {"OWNS": [{"kind": "Atom", "reference": "A", "derived": False}]},
            json.loads(self.store.run("SELECT relations FROM scope_units WHERE name = 'A'")["rows"][0][0]),
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
            "JOIN atoms ON atoms.reference = graph_edges.source_ref "
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
        tables_before = self.store._connection.execute(
            "SELECT table_name FROM information_schema.tables WHERE table_schema = 'workbench_results'"
        ).fetchall()
        with self.assertRaisesRegex(ValueError, "NaN or infinity"):
            self.store.run("SELECT 'NaN'::DOUBLE")
        self.assertEqual(tables_before, self.store._connection.execute(
            "SELECT table_name FROM information_schema.tables WHERE table_schema = 'workbench_results'"
        ).fetchall())
        self.assertEqual([[1]], self.store.run("SELECT 1")["rows"])
        with self.assertRaises(RuntimeError):
            self.store.replace([{"source_path": "invalid.md"}], [])
        with self.assertRaisesRegex(RuntimeError, "restart required"):
            self.store.run("SELECT 1")

    def test_internal_management_failure_requires_restart(self) -> None:
        stderr = StringIO()
        with redirect_stderr(stderr), self.assertRaisesRegex(WorkbenchUnavailableError, "restart required"):
            self.store.run("SELECT * FROM drop_property_graph()")
        self.assertIn("query store unavailable", stderr.getvalue())
        with self.assertRaisesRegex(WorkbenchUnavailableError, "restart required"):
            self.store.run("SELECT 1")


if __name__ == "__main__":
    unittest.main()
