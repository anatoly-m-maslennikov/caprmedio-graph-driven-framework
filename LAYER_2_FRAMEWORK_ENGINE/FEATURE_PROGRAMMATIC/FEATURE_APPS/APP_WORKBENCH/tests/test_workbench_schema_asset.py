# CA-E-677@23
# CA-E-675@14
"""Both Workbench schema modes and their deterministic generated asset."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import Mock, patch


APP_ROOT = Path(__file__).resolve().parents[2]
sys.path[:0] = [str(APP_ROOT), str(Path(__file__).parent)]

from APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.content_schema import (ContentRule, DeclarationSource, _schema_from_rules, compile_content_schema, content_schema_from_statements)  # noqa: E402
from APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.declared_header_rules import HeaderRule, compile_header_rules, header_rules_from_statements  # noqa: E402
from APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.errors import WorkbenchUnavailableError  # noqa: E402
from APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.generate_workbench_schema import (  # noqa: E402
    compile_project_schema,
    write_schema,
)
from APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.header_columns import (  # noqa: E402
    declared_header_schema,
)
from APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.relations import canonical  # noqa: E402
from APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.query_store import QueryStore  # noqa: E402
from APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.source_header_schema import SourceHeaderSchema  # noqa: E402
from APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.workbench_schema_asset import (  # noqa: E402
    compile_schema,
    load_image_schema,
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
            "CA-R-DECL", form="Declaration", body="""## Claim

### Formal Claim

```CFEL
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
            "CA-R-DECL-2", form="Declaration", body="""## Claim

### Formal Claim

```CFEL
Atom.Header.Declared Later:: [string]{::1};
```
""",
        )])))
        self.assertTrue(store.apply([changed], [], relation_types=set(), header_schema=declared_change))
        self.assertTrue(store.schema_changed)

    def test_mode_one_rejects_conflicting_aliases(self) -> None:
        schema = declared_header_schema(compile_header_rules([atom(
            "CA-R-DECL", form="Declaration", body="""## Claim

### Formal Claim

```CFEL
Atom.Header.Context.Role:: [string]{::1};
```
""",
        )]))
        with self.assertRaisesRegex(ValueError, "Conflicting Header aliases"):
            schema.value(atom(header={"role": "Requirement", "content_role": "Method"}), schema.columns[0])
        conflicting = [
            atom("CA-R-INT", form="Declaration", body="""## Claim

### Formal Claim

```CFEL
Atom.Header.Version:: [int]{::1};
```
"""),
            atom("CA-R-TEXT", form="Declaration", body="""## Claim

### Formal Claim

```CFEL
Atom.Header.Version:: [string]{::1};
```
"""),
        ]
        with self.assertRaisesRegex(ValueError, "declaration collision"):
            declared_header_schema(compile_header_rules(conflicting))

    def test_mode_one_declaration_changes_are_the_schema_boundary(self) -> None:
        original = atom("CA-R-DECL", form="Declaration", body="""## Claim

### Formal Claim

```CFEL
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
        changed_body = """## Claim

### Formal Claim

```CFEL
Atom.Header.Version:: [string]{::1};
```
"""
        type_changed = dict(
            same_shape, version=3, content_markdown=changed_body, _content_bytes=changed_body.encode("utf-8"),
        )
        self.assertTrue(state.update({type_changed["source_path"]: type_changed}))
        self.assertEqual(original_schema.shape, state.schema.shape)

    def test_equal_header_validation_shapes_ignore_distinct_provenance(self) -> None:
        occurrence = DeclarationSource("CA-R-PROPERTY", 1, "property.md")
        first = DeclarationSource("CA-R-PARENT-1", 1, "parent-1.md")
        second = DeclarationSource("CA-R-PARENT-2", 1, "parent-2.md")
        rule = HeaderRule(("context", "label"), "VARCHAR", frozenset({"Operations"}),
                          frozenset({"Workflow"}), occurrence, provenance=(first,))
        another = HeaderRule(("context", "label"), "VARCHAR", frozenset({"Operations"}),
                             frozenset({"Workflow"}), occurrence, provenance=(second,))
        single = declared_header_schema((rule,))
        both = declared_header_schema((rule, another))
        self.assertEqual(single.shape, both.shape)
        self.assertEqual(2, len(both.asset()["header_columns"][0]["rules"]))

    def test_mode_one_same_shape_declaration_provenance_writes_after_commit(self) -> None:
        declaration = atom("CA-R-DECL", form="Declaration", body="""## Claim

### Formal Claim

~~~CFEL
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
        selector = atom("CA-R-2464", form="Declaration", body="""## Claim

### Formal Claim

```CFEL
Atom/(.Header.Role: Operations)/Workflow;
```
""")
        self.assertEqual((), compile_header_rules([selector]))

    def test_mode_one_rejects_legacy_type_and_naive_timestamp_without_coercion(self) -> None:
        declaration = atom("CA-R-DECL", form="Declaration", body="""## Claim

### Formal Claim

```CFEL
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
            body="## Claim\n\n### Formal Claim\n\n```CFEL\nAtom.Content.Summary{::1}:: {::1};\n```\n",
        )
        content = compile_content_schema([declaration])
        header = declared_header_schema(compile_header_rules([declaration]))
        compilation = compile_schema([declaration], content, header)
        first = schema_asset([declaration], compilation)
        self.assertEqual(first, schema_asset([declaration], compilation))
        payload = json.loads(first)
        self.assertEqual(2, payload["schema_version"])
        self.assertEqual({"1", "2"}, set(payload["modes"]))
        self.assertEqual(["content.summary"], [item["name"] for item in payload["modes"]["2"]["content"]["content_columns"]])
        self.assertEqual(64, len(payload["input_digest"]))

        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "workbench_schema.json"
            write_schema(path, first)
            loaded = load_image_schema(path)
            self.assertEqual(compilation, loaded)
            stale = dict(declaration, _content_bytes=b"## Claim\n\nChanged.\n")
            self.assertNotEqual(first, schema_asset([stale], compile_schema([stale], content, header)))
            self.assertEqual(compilation, load_image_schema(path))

    def test_inherited_header_format_preserves_both_declaration_sources(self) -> None:
        parent = atom("CA-R-2716", form="Declaration", body="""## Claim

### Formal Claim

```CFEL
Atom.Header.Carrier Destination.File.*:: [string];
```
""")
        name = atom("CA-R-2717", form="Declaration", body="""## Claim

### Formal Claim

```CFEL
Atom.Header.Carrier Destination.File.Name:: {::1};
```
""")
        path_atom = atom("CA-R-2718", form="Declaration", body=name["content_markdown"].replace("File.Name", "File.Path"))
        compilation = compile_schema([parent, name, path_atom], compile_content_schema([]))
        columns = {column.path[-1]: column for column in compilation.mode_one.columns}
        for field, reference in (("name", "CA-R-2717"), ("path", "CA-R-2718")):
            rule = columns[field].rules[0]
            self.assertEqual(reference, rule.source.reference)
            self.assertEqual("CA-R-2716", rule.format_source.reference)
        asset_path = Path(self.temporary.name) / "schema.json"
        asset_path.write_bytes(schema_asset([parent, name, path_atom], compilation))
        self.assertEqual(compilation, load_image_schema(asset_path))

    def test_image_asset_round_trips_all_content_rules_without_source_reads(self) -> None:
        source = DeclarationSource("CA-R-DECL", 7, "source/declaration.md")
        content = _schema_from_rules([
            ContentRule(("container",), frozenset({"Requirement"}), frozenset({"Declaration"}), False, source),
            ContentRule(("container", "value"), None, None, True, source),
            ContentRule(("container", "*"), None, None, False, source, prohibited=True),
            ContentRule(("container", "**"), None, None, True, source),
        ])
        compilation = compile_schema([], content, declared_header_schema(()))
        path = Path(self.temporary.name) / "schema.json"
        path.write_bytes(schema_asset([], compilation))
        with patch("APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.workbench_schema_asset.compile_schema", side_effect=AssertionError("source reread")):
            loaded = load_image_schema(path)
        self.assertEqual(compilation, loaded)
        self.assertEqual(content.rules, loaded.content.rules)
        self.assertEqual(content.sources, loaded.content.sources)
        payload = json.loads(path.read_bytes())
        payload["modes"]["1"]["content"]["rules"][0]["prohibited"] = True
        path.write_text(json.dumps(payload))
        with self.assertRaisesRegex(ValueError, "digest mismatch"):
            load_image_schema(path)
        payload.pop("input_digest")
        payload["input_digest"] = hashlib.sha256(canonical(payload).encode("utf-8")).hexdigest()
        path.write_text(json.dumps(payload))
        with self.assertRaises(ValueError):
            load_image_schema(path)

    def test_header_ancestry_and_wildcard_provenance_round_trip(self) -> None:
        ancestor = DeclarationSource("CA-R-PARENT", 1, "parent.md")
        binding = DeclarationSource("CA-R-FORM", 2, "form.md")
        occurrence = DeclarationSource("CA-R-CHILD", 3, "child.md")
        wildcard = DeclarationSource("CA-R-FORMAT", 4, "format.md")
        wildcard_ancestor = DeclarationSource("CA-R-OTHER-PARENT", 5, "other-parent.md")
        wildcard_binding = DeclarationSource("CA-R-OTHER-FORM", 6, "other-form.md")
        rules = header_rules_from_statements([
            ("Atom/Workflow", ancestor),
            ("Workflow.Header.Form:: [in (Workflow)]", binding),
            ("Workflow.Header.Context.Label:: {::1}", occurrence),
            ("Atom/FormatOwner", wildcard_ancestor),
            ("FormatOwner.Header.Form:: [in (Workflow)]", wildcard_binding),
            ("FormatOwner.Header.Context.*:: [string]", wildcard),
        ])
        child = next(rule for rule in rules if rule.path == ("context", "label"))
        self.assertEqual(occurrence, child.source)
        self.assertEqual(wildcard, child.format_source)
        self.assertEqual((ancestor, binding, wildcard_ancestor, wildcard_binding), child.provenance)
        declared = declared_header_schema(rules)
        compilation = compile_schema([], _schema_from_rules([]), declared)
        path = Path(self.temporary.name) / "header-provenance.json"
        path.write_bytes(schema_asset([], compilation))
        loaded = load_image_schema(path)
        self.assertEqual(declared, loaded.mode_one)
        self.assertEqual(declared.shape, loaded.mode_one.shape)
        payload = json.loads(path.read_bytes())
        rule = next(c for c in payload["modes"]["1"]["header"]["header_columns"]
                    if c["name"] == "header.context.label")["rules"][0]
        rule["provenance"].append(rule["provenance"][0])
        payload.pop("input_digest")
        payload["input_digest"] = hashlib.sha256(canonical(payload).encode("utf-8")).hexdigest()
        path.write_text(json.dumps(payload))
        with self.assertRaises(ValueError):
            load_image_schema(path)

    def test_content_ancestry_provenance_round_trips_separately_from_occurrence(self) -> None:
        ancestry = DeclarationSource("CA-R-ANCESTRY", 1, "ancestry.md")
        binding = DeclarationSource("CA-R-BINDING", 2, "binding.md")
        occurrence = DeclarationSource("CA-R-PROPERTY", 3, "property.md")
        content = content_schema_from_statements([
            ("Atom/(.Header.Role: Operations)/Workflow", ancestry),
            ("Workflow.Header.Form:: [in (Workflow)]", binding),
            ("Workflow.Content.Steps[string]", occurrence),
        ])
        rule = next(rule for rule in content.rules if rule.path == ("steps",))
        self.assertEqual(occurrence, rule.source)
        self.assertEqual((ancestry, binding), rule.provenance)
        self.assertEqual({ancestry, binding, occurrence}, set(content.sources))
        shared = content_schema_from_statements([
            ("Atom/Workflow", ancestry), ("Atom/Workflow", ancestry),
            ("Workflow.Header.Form:: [in (Workflow)]", occurrence),
            ("Workflow.Header.Form:: [in (Workflow)]", occurrence),
            ("Workflow.Content.Steps[string]", occurrence),
        ])
        shared_rule = next(rule for rule in shared.rules if rule.path == ("steps",))
        self.assertEqual((ancestry, occurrence), shared_rule.provenance)
        self.assertEqual(occurrence, shared_rule.source)
        compilation = compile_schema([], content, declared_header_schema(()))
        path = Path(self.temporary.name) / "provenance.json"
        path.write_bytes(schema_asset([], compilation))
        loaded = load_image_schema(path)
        self.assertEqual(content.rules, loaded.content.rules)
        self.assertEqual(content.shape, loaded.content.shape)
        self.assertEqual(content.columns[0].applies({"role": "Operations", "form": "Workflow"}),
                         loaded.content.columns[0].applies({"role": "Operations", "form": "Workflow"}))
        payload = json.loads(path.read_bytes())
        contributors = payload["modes"]["1"]["content"]["rules"][0]["provenance"]
        contributors.append(contributors[0])
        payload.pop("input_digest")
        payload["input_digest"] = hashlib.sha256(canonical(payload).encode("utf-8")).hexdigest()
        path.write_text(json.dumps(payload))
        with self.assertRaises(ValueError):
            load_image_schema(path)

    def test_image_asset_rejects_missing_and_incomplete_payload(self) -> None:
        path = Path(self.temporary.name) / "missing.json"
        with self.assertRaises(ValueError):
            load_image_schema(path)
        path.write_text('{}')
        with self.assertRaises(ValueError):
            load_image_schema(path)

    def test_project_generator_uses_one_reader_capture_and_writes_exact_bytes(self) -> None:
        row = atom(header={"atom_id": "CA-R-1"})
        draft = atom("CA-R-2", header={"atom_id": "CA-R-2"}, body="## Summary\n\nEdited Draft.\n")
        draft["status_group"] = "Draft"
        reader = Mock(capture=Mock(side_effect=[([row], []), ([row, draft], [])]), model_rows=Mock(return_value=[]))
        with patch(
            "APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.generate_workbench_schema.SourceReader",
            return_value=reader,
        ):
            first = compile_project_schema(Path("/project"))
            second = compile_project_schema(Path("/project"))
        self.assertEqual(first, second)
        self.assertEqual(2, reader.capture.call_count)
        self.assertEqual([], json.loads(first)["sources"])


if __name__ == "__main__":
    unittest.main()
