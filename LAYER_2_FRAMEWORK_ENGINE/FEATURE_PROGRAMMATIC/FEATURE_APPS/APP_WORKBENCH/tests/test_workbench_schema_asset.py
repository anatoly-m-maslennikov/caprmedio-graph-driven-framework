# CA-E-677@23
"""Both Workbench schema modes and their deterministic generated asset."""

from __future__ import annotations

import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import Mock, patch


APP_ROOT = Path(__file__).resolve().parents[2]
sys.path[:0] = [str(APP_ROOT), str(Path(__file__).parent)]

from APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.content_schema import compile_content_schema  # noqa: E402
from APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.declared_header_rules import compile_header_rules  # noqa: E402
from APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.errors import WorkbenchUnavailableError  # noqa: E402
from APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.generate_workbench_schema import (  # noqa: E402
    compile_project_schema,
    write_schema,
)
from APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.header_columns import (  # noqa: E402
    declared_header_schema,
)
from APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.query_store import QueryStore  # noqa: E402
from APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.service import WorkbenchService  # noqa: E402
from APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.source_header_schema import SourceHeaderSchema  # noqa: E402
from APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.workbench_schema_asset import (  # noqa: E402
    compile_schema,
    load_schema_asset,
    schema_asset,
)
from smalltest_support import extension_directory  # noqa: E402


def atom(
    reference: str = "CA-R-1", *, header: dict | None = None,
    body: str = "## Summary\n\nSummary.\n", form: str = "Definition", version: int = 1,
) -> dict:
    return {
        "source_path": f"source/{reference}.md", "status_group": "Current", "id": reference,
        "ref": reference, "version": version, "status": "Active", "role": "Requirement",
        "form": form, "tier": 1, "updated_at": None, "header_json": header or {},
        "_content_bytes": body.encode("utf-8"), "content_markdown": body,
        "content_properties_json": [], "relation_edges_json": [], "hash": None,
    }


class WorkbenchSchemaAssetTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.database = Path(self.temporary.name) / "workbench" / "projection.duckdb"

    def test_mode_one_uses_canonical_adapter_paths_and_alias_reads_only(self) -> None:
        declaration = atom(
            "CA-R-DECL", form="Declaration", body="""```CFEL
# model
Atom.Header.ID:: [atom id]{::1};
Atom.Header.Context.Role:: [string]{::1};
Atom.Header.Status:: [string]{::1};
Atom.Header.Updated At:: [datetime]{::1};
```
""",
        )
        row = atom(header={
            "atom_id": "CA-R-1", "content_role": "Requirement", "type": "Definition",
            "status": "Active", "label": "known adapter field", "version": 1,
            "updated_at": "2026-11-09 00:00:00 +0000",
            "unknown residue": "not a model column",
        })
        rules = compile_header_rules([declaration])
        schema = declared_header_schema(rules)

        self.assertIn("header.identity.atom_id", schema.names)
        self.assertIn("header.context.role", schema.names)
        self.assertIn("header.state.updated_at", schema.names)
        self.assertNotIn("header.context.label", schema.names)
        self.assertNotIn("header.unknown_residue", schema.names)
        self.assertEqual("Requirement", next(
            schema.value(row, column)
            for column in schema.columns if column.name == "header.context.role"
        ))

        store = QueryStore(
            extension_directory=extension_directory(APP_ROOT.parents[2]), database_path=self.database,
            schema_mode=1,
        )
        self.addCleanup(store.close)
        store.replace([row], [], header_schema=schema)
        self.assertEqual([["CA-R-1", "Requirement", "Active"]], store.run(
            'SELECT "header.identity.atom_id", "header.context.role", "header.state.status" FROM atoms'
        )["rows"])

        changed = atom(header={**row["header_json"], "unknown residue": "changed"}, version=2)
        self.assertFalse(store.apply([changed], [], relation_types=set(), header_schema=schema))
        self.assertFalse(store.schema_changed)

        declared_change = declared_header_schema((*rules, *compile_header_rules([atom(
            "CA-R-DECL-2", form="Declaration", body="""```CFEL
# model
Atom.Header.Declared Later:: [string]{::1};
```
""",
        )])))
        self.assertTrue(store.apply([changed], [], relation_types=set(), header_schema=declared_change))
        self.assertTrue(store.schema_changed)

    def test_mode_one_rejects_conflicting_aliases(self) -> None:
        schema = declared_header_schema(compile_header_rules([atom(
            "CA-R-DECL", form="Declaration", body="""```CFEL
# model
Atom.Header.Context.Role:: [string]{::1};
```
""",
        )]))
        with self.assertRaisesRegex(ValueError, "Conflicting Header aliases"):
            schema.value(atom(header={"role": "Requirement", "content_role": "Method"}), schema.columns[0])
        conflicting = [
            atom("CA-R-INT", form="Declaration", body="""```CFEL
# model
Atom.Header.Version:: [int]{::1};
```
"""),
            atom("CA-R-TEXT", form="Declaration", body="""```CFEL
# model
Atom.Header.Version:: [string]{::1};
```
"""),
        ]
        with self.assertRaisesRegex(ValueError, "declaration collision"):
            declared_header_schema(compile_header_rules(conflicting))

    def test_mode_one_declaration_changes_are_the_schema_boundary(self) -> None:
        original = atom("CA-R-DECL", form="Declaration", body="""```CFEL
# model
Atom.Header.Version:: [int]{::1};
```
""")
        state = SourceHeaderSchema()
        state.rebuild([original])
        assert state.schema is not None
        original_schema = state.schema
        same_shape = dict(original, version=2)
        self.assertFalse(state.update({same_shape["source_path"]: same_shape}))
        assert state.schema is not None
        self.assertEqual(2, state.schema.columns[0].rules[0].source.version)
        changed_body = """```CFEL
# model
Atom.Header.Version:: [string]{::1};
```
"""
        type_changed = dict(
            same_shape, version=3, content_markdown=changed_body, _content_bytes=changed_body.encode("utf-8"),
        )
        self.assertTrue(state.update({type_changed["source_path"]: type_changed}))
        self.assertEqual(original_schema.shape, state.schema.shape)

    def test_mode_one_same_shape_declaration_provenance_writes_after_commit(self) -> None:
        declaration = atom("CA-R-DECL", form="Declaration", body="""~~~CFEL
# model
Atom.Header.Tier:: [int]{::1};
~~~
""")
        header = declared_header_schema(compile_header_rules([declaration]))
        row = atom(header={"tier": 1})
        store = QueryStore(
            extension_directory=extension_directory(APP_ROOT.parents[2]), database_path=self.database,
            schema_mode=1,
        )
        self.addCleanup(store.close)
        store.replace([row], [], header_schema=header)
        changed = declared_header_schema(compile_header_rules([dict(declaration, version=2)]))
        self.assertFalse(store.apply(
            [dict(row, version=2)], [], relation_types=set(), header_schema=changed,
        ))
        payload = json.loads((self.database.parent / "projection-schema.json").read_text(encoding="utf-8"))
        self.assertEqual(2, payload["header_columns"][0]["rules"][0]["source"]["version"])

    def test_header_selector_without_a_literal_header_path_does_not_become_a_column(self) -> None:
        selector = atom("CA-R-2464", form="Declaration", body="""```CFEL
# model
Atom/(.Header.Role: Operations)/Workflow;
```
""")
        self.assertEqual((), compile_header_rules([selector]))

    def test_mode_one_rejects_legacy_type_and_naive_timestamp_without_coercion(self) -> None:
        declaration = atom("CA-R-DECL", form="Declaration", body="""```CFEL
# model
Atom.Header.Tier:: [int]{::1};
Atom.Header.Updated At:: [datetime]{::1};
```
""")
        schema = declared_header_schema(compile_header_rules([declaration]))
        naive = atom(header={"updated_at": "2026-11-09 00:00:00"})
        updated_at = next(column for column in schema.columns if column.reader == "updated_at")
        with self.assertRaisesRegex(ValueError, "offset-bearing"):
            schema.value(naive, updated_at)
        store = QueryStore(
            extension_directory=extension_directory(APP_ROOT.parents[2]), database_path=self.database,
            schema_mode=1,
        )
        self.addCleanup(store.close)
        with self.assertRaises(WorkbenchUnavailableError):
            store.replace([atom(header={"tier": "principle"})], [], header_schema=schema)

    def test_asset_is_deterministic_pinned_and_rejected_when_stale(self) -> None:
        declaration = atom(
            "CA-R-DECL", form="Declaration",
            body="## Claim\n\n```CFEL\n# model\nAtom.Content.Summary{::1}:: {::1};\n```\n",
        )
        content = compile_content_schema([declaration])
        header = declared_header_schema(compile_header_rules([declaration]))
        compilation = compile_schema([declaration], content, header)
        first = schema_asset([declaration], compilation)
        self.assertEqual(first, schema_asset([declaration], compilation))
        payload = json.loads(first)
        self.assertEqual(1, payload["schema_version"])
        self.assertEqual({"1", "2"}, set(payload["modes"]))
        self.assertEqual(["content.summary"], [item["name"] for item in payload["modes"]["2"]["content"]["content_columns"]])
        self.assertEqual(64, len(payload["input_digest"]))

        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "workbench_schema.json"
            write_schema(path, first)
            loaded = load_schema_asset(path, [declaration], compilation)
            self.assertIsNotNone(loaded)
            assert loaded is not None
            self.assertEqual(compilation.mode_two, loaded.mode_two)
            stale = dict(declaration, _content_bytes=b"## Claim\n\nChanged.\n")
            self.assertIsNone(load_schema_asset(path, [stale], compile_schema([stale], content, header)))

    def test_runtime_uses_a_verified_delivered_schema_before_source_fallback(self) -> None:
        row = atom(header={"atom_id": "CA-R-1"})
        header = declared_header_schema(())
        compilation = compile_schema([row], compile_content_schema([]), header)
        service = object.__new__(WorkbenchService)
        service._schema_mode = 2
        with patch(
            "APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.service.load_schema_asset",
            return_value=compilation,
        ) as load:
            selected = service._header_schema([row], compilation.content, header)
        self.assertIs(compilation.mode_two, selected)
        load.assert_called_once()

    def test_project_generator_uses_one_reader_capture_and_writes_exact_bytes(self) -> None:
        row = atom(header={"atom_id": "CA-R-1"})
        content = compile_content_schema([])
        header = declared_header_schema(())
        reader = Mock(capture=Mock(return_value=([row], [])), content_schema=content, header_schema=header)
        with patch(
            "APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.generate_workbench_schema.SourceReader",
            return_value=reader,
        ):
            first = compile_project_schema(Path("/project"))
            second = compile_project_schema(Path("/project"))
        self.assertEqual(first, second)
        self.assertEqual(2, reader.capture.call_count)


if __name__ == "__main__":
    unittest.main()
