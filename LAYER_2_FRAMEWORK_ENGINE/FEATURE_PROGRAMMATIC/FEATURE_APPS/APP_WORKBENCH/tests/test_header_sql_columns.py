# CA-E-675@6
# CA-E-677@19
"""Source-faithful dynamic Header columns in the Workbench SQL projection."""

from __future__ import annotations

import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch


APP_ROOT = Path(__file__).resolve().parents[2]
sys.path[:0] = [str(APP_ROOT), str(Path(__file__).parent)]

from APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.header_columns import infer_header_schema  # noqa: E402
from APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.errors import WorkbenchUnavailableError  # noqa: E402
from APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.index_delta import MaterializationDelta  # noqa: E402
from APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.markdown_content import parse_content  # noqa: E402
from APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.public_rows import atom_fields  # noqa: E402
from APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.query_store import QueryStore  # noqa: E402
from smalltest_support import extension_directory  # noqa: E402


class HeaderSqlColumnsTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.database = Path(self.temporary.name) / "workbench" / "projection.duckdb"
        self.store = QueryStore(
            extension_directory=extension_directory(APP_ROOT.parents[2]), database_path=self.database,
        )
        self.addCleanup(self.store.close)

    @staticmethod
    def atom(
        reference: str, header: dict, *, body: str = "## Summary\n\nSummary.\n", edges: list[dict] | None = None,
        form: str = "Definition", version: int = 1,
    ) -> dict:
        return {
            "source_path": f"source/{reference}.md", "status_group": "Current", "id": reference,
            "ref": reference, "version": version, "status": "Active", "current_scope_unit": None,
            "claim_target_scope_unit": None, "role": "Requirement", "form": form, "tier": 1,
            "updated_at": None, "header_json": header, "content_markdown": body,
            "content_properties_json": parse_content(body, tolerate_duplicate_siblings=True),
            "relation_edges_json": edges or [], "hash": reference,
        }

    @staticmethod
    def edge(source: str, target: str) -> dict:
        return {
            "source_kind": "Atom", "source_ref": source, "target_kind": "Atom", "target_ref": target,
            "relation_type": "CONTAINS", "derived": False,
        }

    def test_raw_flat_and_nested_paths_build_typed_columns_and_schema_asset(self) -> None:
        flat = self.atom("FLAT", {
            "atom_id": "CA-R-1", "status": "Active", "enabled": False, "zero": 0,
            "tags": ["one"], "metadata": {"answer": 42}, "unknown residue": "kept", "relations": {},
        })
        nested = self.atom("NESTED", {
            "identity": {"atom_id": "CA-R-2"}, "state": {"status": "Done"},
            "items": [{"answer": 1}], "relations": {},
        })

        self.store.replace([flat, nested], [])

        fields = atom_fields(self.store._header_schema, self.store._content_schema)
        self.assertTrue({
            "header.atom_id", "header.identity.atom_id", "header.status", "header.state.status",
            "header.enabled", "header.zero", "header.tags", "header.metadata.answer",
            "header.unknown_residue", "header.items", "header.relations",
        } <= set(fields))
        self.assertNotIn("id", fields)
        self.assertNotIn("status", fields)
        values = self.store._connection.execute(
            'SELECT "header.enabled", "header.zero", "header.tags", "header.metadata.answer", '
            '"header.items", "header.identity.atom_id", "header.atom_id" FROM atoms ORDER BY reference'
        ).fetchall()
        self.assertEqual((False, 0, '["one"]', 42, None, None, "CA-R-1"), values[0])
        self.assertEqual((None, None, None, None, '[{"answer":1}]', "CA-R-2", None), values[1])
        asset = json.loads((self.database.parent / "projection-schema.json").read_text(encoding="utf-8"))
        self.assertIn(
            {
                "path": ["identity", "atom_id"], "name": "header.identity.atom_id", "format": "VARCHAR",
                "populated": True, "reader": None,
            },
            asset["header_columns"],
        )

    def test_nested_identity_id_keeps_its_observed_header_column(self) -> None:
        self.store.replace([self.atom("CA-R-3", {"identity": {"id": "CA-R-3"}})], [])

        fields = atom_fields(self.store._header_schema, self.store._content_schema)
        self.assertIn("header.identity.id", fields)
        self.assertNotIn("header.identity.atom_id", fields)
        self.assertEqual(("CA-R-3",), self.store._connection.execute(
            'SELECT "header.identity.id" FROM atoms WHERE reference = \'CA-R-3\''
        ).fetchone())

    def test_nested_container_is_queryable_as_json_and_as_leaf_columns(self) -> None:
        rows = [
            self.atom("A", {"context": {"container": {"scope_unit": "CA-SU-00"}}}),
            self.atom("B", {"context": {"container": {"atom": "CA-P-1"}}}),
            self.atom("C", {}),
        ]
        self.store.replace(rows, [])
        self.assertEqual([
            ('{"scope_unit":"CA-SU-00"}', "CA-SU-00", None),
            ('{"atom":"CA-P-1"}', None, "CA-P-1"),
            (None, None, None),
        ], self.store._connection.execute(
            'SELECT "header.context.container", "header.context.container.scope_unit", '
            '"header.context.container.atom" FROM atoms ORDER BY reference'
        ).fetchall())
        self.assertEqual("CA-SU-00", self.store._connection.execute(
            'SELECT "header.context.container"->>\'scope_unit\' FROM atoms WHERE reference = \'A\''
        ).fetchone()[0])

        changed = self.atom("A", {"context": {"container": {"scope_unit": "CA-SU-14"}}})
        self.assertTrue(self.store.apply([changed, *rows[1:]], [], relation_types=set()))
        self.assertFalse(self.store.schema_changed)
        self.assertEqual("CA-SU-14", self.store._connection.execute(
            'SELECT "header.context.container"->>\'scope_unit\' FROM atoms WHERE reference = \'A\''
        ).fetchone()[0])

    def test_schema_change_defers_rebuild_but_same_schema_preserves_unaffected_row(self) -> None:
        initial = [
            self.atom("A", {"atom_id": "A", "volatile": "value", "stable": "first", "zero": 0, "enabled": False}),
            self.atom("B", {"atom_id": "B", "volatile": "value", "stable": "first", "zero": 0, "enabled": False}),
        ]
        self.store.replace(initial, [])
        retained_row = self.store._connection.execute(
            "SELECT rowid FROM atoms WHERE reference = 'A'"
        ).fetchone()[0]
        normal = [
            self.atom("A", {"atom_id": "A", "volatile": "value", "stable": "first", "zero": 0, "enabled": False}),
            self.atom("B", {"atom_id": "B", "volatile": "value", "stable": "edited", "zero": 0, "enabled": False}),
        ]
        self.assertTrue(self.store.apply(normal, [], relation_types=set()))
        self.assertFalse(self.store.schema_changed)
        self.assertEqual(retained_row, self.store._connection.execute(
            "SELECT rowid FROM atoms WHERE reference = 'A'"
        ).fetchone()[0])
        empty = [
            self.atom("A", {"atom_id": "A", "volatile": "", "stable": "first", "zero": 0, "enabled": False}),
            self.atom("B", {"atom_id": "B", "volatile": None, "stable": "edited", "zero": 0, "enabled": False}),
        ]
        self.assertTrue(self.store.apply(empty, [], relation_types=set()))
        self.assertTrue(self.store.schema_changed)
        self.assertIn("header.volatile", atom_fields(self.store._header_schema, self.store._content_schema))
        self.store.replace(empty, [])
        fields = atom_fields(self.store._header_schema, self.store._content_schema)
        self.assertIn("header.volatile", fields)
        self.assertIn("header.zero", fields)
        self.assertIn("header.enabled", fields)
        self.assertFalse(next(
            column.populated for column in self.store._header_schema.columns if column.name == "header.volatile"
        ))
        asset = json.loads((self.database.parent / "projection-schema.json").read_text(encoding="utf-8"))
        self.assertFalse(next(
            column["populated"] for column in asset["header_columns"] if column["name"] == "header.volatile"
        ))

        with_empty_path = [
            self.atom("A", {"atom_id": "A", "volatile": "", "stable": "first", "zero": 0, "enabled": False}),
            self.atom("B", {
                "atom_id": "B", "volatile": None, "stable": "edited", "zero": 0, "enabled": False,
                "optional": None,
            }),
        ]
        self.assertTrue(self.store.apply(with_empty_path, [], relation_types=set()))
        self.assertTrue(self.store.schema_changed)
        self.store.replace(with_empty_path, [])
        self.assertIn("header.optional", atom_fields(self.store._header_schema, self.store._content_schema))

        self.assertTrue(self.store.apply(empty, [], relation_types=set()))
        self.assertTrue(self.store.schema_changed)
        self.store.replace(empty, [])
        self.assertNotIn("header.optional", atom_fields(self.store._header_schema, self.store._content_schema))

        changed_type = [
            self.atom("A", {"atom_id": "A", "volatile": "", "stable": 1, "zero": 0, "enabled": False}),
            self.atom("B", {"atom_id": "B", "volatile": None, "stable": 2, "zero": 0, "enabled": False}),
        ]
        self.assertTrue(self.store.apply(changed_type, [], relation_types=set()))
        self.assertTrue(self.store.schema_changed)

    def test_mixed_empty_values_keep_their_native_values_without_conversion_failure(self) -> None:
        rows = [
            self.atom("number", {"mixed": 1, "all_empty": ""}),
            self.atom("text", {"mixed": "", "all_empty": []}),
            self.atom("list", {"mixed": [], "all_empty": {}}),
            self.atom("map", {"mixed": {}, "all_empty": None}),
            self.atom("group", {"mixed": {"child": 2}, "group_only": {"child": 2}, "empty_map": {}}),
        ]

        self.store.replace(rows, [])

        fields = atom_fields(self.store._header_schema, self.store._content_schema)
        self.assertIn("header.mixed", fields)
        self.assertIn("header.mixed.child", fields)
        self.assertIn("header.all_empty", fields)
        self.assertIn("header.empty_map", fields)
        self.assertIn("header.group_only.child", fields)
        self.assertNotIn("header.group_only", fields)
        values = self.store._connection.execute(
            'SELECT "header.mixed" FROM atoms ORDER BY reference'
        ).fetchall()
        self.assertEqual([{"child": 2}, [], {}, 1, ""], [json.loads(value[0]) for value in values])
        self.assertEqual(
            [(2,)], self.store._connection.execute(
                'SELECT "header.mixed.child" FROM atoms WHERE reference = \'group\''
            ).fetchall(),
        )
        self.assertEqual(
            [(None,), ('{}',), (None,), ('""',), ('[]',)], self.store._connection.execute(
                'SELECT "header.all_empty" FROM atoms ORDER BY reference'
            ).fetchall(),
        )

    def test_declaration_provenance_delta_keeps_the_table_and_updates_the_schema_asset(self) -> None:
        declaration_body = "## Claim\n\n```CFEL\n# model\nAtom.Content.Summary{::1}:: {::1};\n```\n"
        first = self.atom(
            "CA-R-DECL", {"atom_id": "CA-R-DECL", "version": 1},
            body=declaration_body, form="Declaration", version=1,
        )
        ordinary = self.atom("CA-R-ORDINARY", {"atom_id": "CA-R-ORDINARY"})
        self.store.replace([first, ordinary], [])
        retained_row = self.store._connection.execute(
            "SELECT rowid FROM atoms WHERE reference = 'CA-R-ORDINARY'"
        ).fetchone()[0]
        later = {**first, "version": 2, "header_json": {"atom_id": "CA-R-DECL", "version": 2}}

        self.assertTrue(self.store.apply([later, ordinary], [], relation_types=set()))

        self.assertFalse(self.store.schema_changed)
        self.assertEqual(retained_row, self.store._connection.execute(
            "SELECT rowid FROM atoms WHERE reference = 'CA-R-ORDINARY'"
        ).fetchone()[0])
        self.assertEqual(("Summary.",), self.store._connection.execute(
            'SELECT "content.summary" FROM atoms WHERE reference = \'CA-R-ORDINARY\''
        ).fetchone())
        content_asset = json.loads((self.database.parent / "content-schema.json").read_text(encoding="utf-8"))
        self.assertEqual(2, content_asset["content_declaration_sources"][0]["version"])

    def test_materialized_relations_and_normalized_name_collisions_are_explicit(self) -> None:
        self.store.replace([
            self.atom("A", {"atom_id": "A", "relations": {}}, edges=[self.edge("A", "B")]),
            self.atom("B", {"atom_id": "B", "relations": {}}),
        ], [])
        relations = self.store._connection.execute(
            'SELECT "header.relations" FROM atoms WHERE reference = \'A\''
        ).fetchone()[0]
        self.assertEqual(
            {"CONTAINS": [{"kind": "Atom", "reference": "B", "derived": False}]}, json.loads(relations),
        )
        with self.assertRaisesRegex(ValueError, "collision"):
            infer_header_schema([{"header_json": {"same-name": "a", "same_name": "b"}}])

    def test_failed_delta_write_does_not_publish_candidate_header_state(self) -> None:
        original = self.atom("A", {"atom_id": "A", "stable": "before"})
        unchanged = self.atom("B", {"atom_id": "B", "stable": "unchanged"})
        self.store.replace([original, unchanged], [])
        previous_state = self.store._header_state
        previous_schema = self.store._header_schema
        updated = self.atom("A", {"atom_id": "A", "stable": "after"}, version=2)
        delta = MaterializationDelta(
            old_atoms={"source/A.md": original}, new_atoms={"source/A.md": updated},
            old_scopes={}, new_scopes={},
        )

        with patch(
            "APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.query_store.apply_projection_delta",
            side_effect=RuntimeError("write failed"),
        ), self.assertRaises(WorkbenchUnavailableError):
            self.store.apply([updated, unchanged], [], relation_types=set(), delta=delta)

        self.assertIs(previous_state, self.store._header_state)
        self.assertIs(previous_schema, self.store._header_schema)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
