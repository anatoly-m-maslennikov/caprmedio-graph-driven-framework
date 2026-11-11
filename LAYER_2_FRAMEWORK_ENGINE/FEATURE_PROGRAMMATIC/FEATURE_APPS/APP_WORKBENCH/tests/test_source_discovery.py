# CA-E-677@28
"""Authority-root discovery is independent of declared Scope membership."""

from __future__ import annotations

import json
import unittest
from unittest.mock import patch

import test_source_reader as fixtures
from APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.generate_relation_registry import compile_project_registry
from APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.generate_workbench_schema import compile_project_schema


class SourceDiscoveryTests(unittest.TestCase):
    def setUp(self):
        self.fixture = fixtures.SourceReaderTests()
        self.fixture.setUp()
        self.addCleanup(self.fixture.doCleanups)
        self.root, self.control = self.fixture.root, self.fixture.control
        self.reader = self.fixture.reader

    def source(self, relative: str, atom_id: str, *, status="Active", form="Declaration", body=None):
        template = self.fixture._write_atom(
            "MAIN", "04_requirement", "seed.md", atom_id=atom_id, status=status,
            form=form, body=body or "## Summary\n\nA source outside the Scope tree.\n",
        )
        raw = template.read_bytes()
        template.unlink()
        path = self.control / relative
        path = path.with_name(f"{atom_id}-{path.name}")
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(raw)
        return path

    def test_root_discovery_includes_loose_and_unregistered_sources_only_inside_boundary(self):
        current = self.source("retired-owner/04_requirement/current.md", "CA-R-780")
        draft = self.source("loose/draft/proposal.md", "CA-R-781", status="Draft")
        copied = self.source("installed-copy/custom/record.md", "CA-R-782")
        excluded = [
            self.source("retired-owner/archive/old.md", "CA-R-783"),
            self.source("_projection/copy.md", "CA-R-784"),
            self.source("loose/old.md", "CA-R-785", status="Archived"),
        ]
        outside = self.root / "CA-R-786-outside.md"
        outside.write_bytes(current.read_bytes().replace(b"CA-R-780", b"CA-R-786"))
        atoms, scopes, diagnostics = self.fixture._capture()
        self.assertEqual("", diagnostics)
        paths = {row["source_path"] for row in atoms}
        for path in (current, draft, copied):
            self.assertIn(path.relative_to(self.root).as_posix(), paths)
        for path in (*excluded, outside):
            self.assertNotIn(path.relative_to(self.root).as_posix(), paths)
        self.assertEqual({"fixture", "MAIN", "CHILD"}, {row["name"] for row in scopes})
        self.assertEqual("Draft", next(row for row in atoms if row["id"] == "CA-R-781")["status_group"])

    def test_orphan_source_lifecycle_does_not_rescan_scope_or_atom_inventory(self):
        self.source("loose/seed.md", "CA-R-790")
        self.fixture._capture()
        source = self.source("new-owner/entry.md", "CA-R-791")
        with patch.object(self.reader, "_inventory_paths", side_effect=AssertionError("unexpected full scan")), \
             patch.object(fixtures.source_reader_module, "read_scope_unit_declarations", side_effect=AssertionError("unexpected Scope scan")):
            def capture(operation, old=None, new=None):
                return self.reader.capture([{
                    "operation": operation,
                    "old_path": old.relative_to(self.root).as_posix() if old else None,
                    "new_path": new.relative_to(self.root).as_posix() if new else None,
                }])[0]

            self.assertIn("CA-R-791", {row["id"] for row in capture("create", new=source)})
            source.write_text(source.read_text().replace("version: 1", "version: 2"))
            rows = capture("update", new=source)
            self.assertEqual(2, next(row for row in rows if row["id"] == "CA-R-791")["version"])
            renamed = source.with_name("CA-R-791-renamed.md")
            source.rename(renamed)
            rows = capture("rename", source, renamed)
            moved = self.control / "other-owner" / renamed.name
            moved.parent.mkdir()
            renamed.rename(moved)
            rows = capture("move", renamed, moved)
            self.assertIn(moved.relative_to(self.root).as_posix(), {row["source_path"] for row in rows})
            self.assertNotIn(source.relative_to(self.root).as_posix(), {row["source_path"] for row in rows})
            moved.unlink()
            self.assertNotIn("CA-R-791", {row["id"] for row in capture("remove", old=moved)})
            capture("create", new=self.root / "outside.md")
            self.assertFalse(self.reader.capture_changed)

    def test_filename_marker_defines_atoms_instead_of_yaml_or_role_folder(self):
        current = self.source("02_analysis/record.md", "CA-R-798")
        plain = current.with_name("ordinary.md")
        plain.write_bytes(current.read_bytes().replace(b"CA-R-798", b"CA-R-799"))
        foreign = current.with_name("OTHER-R-800-record.md")
        foreign.write_bytes(current.read_bytes().replace(b"CA-R-798", b"OTHER-R-800"))
        broken = current.with_name("CA-R-801-broken.md")
        broken.write_text("---\nrole: [invalid\n---\n")
        atoms, _, diagnostics = self.fixture._capture()
        self.assertIn(current.relative_to(self.root).as_posix(), {row["source_path"] for row in atoms})
        self.assertNotIn("CA-R-799", {row["id"] for row in atoms})
        self.assertNotIn("OTHER-R-800", {row["id"] for row in atoms})
        self.assertIn(str(broken), diagnostics)

    def test_new_method_delegation_refreshes_the_structural_source_pins(self):
        self.fixture._capture()
        parent = self.reader._declarations.by_name["MAIN"]
        source = self.fixture._write_atom(
            "MAIN", "05_method", "CA-M-803-delegation.md", atom_id="CA-M-803", form="Scope Delegation",
            body="## Claim\n\n### Prose Claim\n\nDeliver the child capability.\n",
        )
        raw = source.read_text().replace('role: "Requirement"', 'role: "Method"')
        raw = raw.replace("subjects: {}", f"container:\n  scope_unit: {parent.scope_unit_id}\n"
                          "topics:\n  main_subject: Scope Unit//CHILD")
        source.write_text(raw)
        atoms, scopes = self.reader.capture([{
            "operation": "create", "old_path": None, "new_path": source.relative_to(self.root).as_posix(),
        }])
        self.assertIn("CA-M-803", {row["id"] for row in atoms})
        self.assertEqual({"fixture", "MAIN", "CHILD"}, {row["name"] for row in scopes})
        self.assertEqual(
            [source.resolve()],
            [item.source for item in self.reader._declarations.by_name["CHILD"].delegations],
        )
        self.assertIn(source.relative_to(self.root).as_posix(), self.reader._declarations.source_pins)

    def test_duplicate_loads_one_carrier_reports_the_other_and_promotes_after_delete(self):
        copies = [self.source(f"{directory}/copy.md", "CA-R-802") for directory in ("a", "z")]
        atoms, _, _ = self.fixture._capture()
        selected = [row for row in atoms if row["ref"] == "CA-R-802"]
        self.assertEqual(1, len(selected))
        winner = self.root / selected[0]["source_path"]
        later = next(path for path in copies if path != winner)
        public = {(str(winner.parent.relative_to(self.root)), winner.name): selected[0]}
        issues = self.reader.audit_issues(public)["atom_content_issues"]
        duplicates = [row for row in issues if row[0] == "CA-R-802"]
        self.assertEqual(1, len(duplicates))
        self.assertEqual(later.name, duplicates[0][2])
        self.assertIn("duplicate", duplicates[0][-1])
        winner.unlink()
        with patch.object(self.reader, "_inventory_paths", side_effect=AssertionError("unexpected full scan")):
            atoms, _ = self.reader.capture([{
                "operation": "remove", "old_path": winner.relative_to(self.root).as_posix(), "new_path": None,
            }])
        selected = [row for row in atoms if row["ref"] == "CA-R-802"]
        self.assertEqual([later.relative_to(self.root).as_posix()], [row["source_path"] for row in selected])
        self.assertIsNone(self.reader.capture_delta[winner.relative_to(self.root).as_posix()])
        self.assertIsNotNone(self.reader.capture_delta[later.relative_to(self.root).as_posix()])

    def test_image_compilers_use_formal_declarations_outside_scope_inventory(self):
        declaration = self.source("native-model/content.md", "CA-R-795", body="""## Claim

### Formal Claim

```CFEL
Atom.Content.Summary{::1}:: {::1};
```
""")
        relation = self.source("native-model/relation.md", "CA-R-796", form="Relation Declaration", body="""## Claim

### Formal Claim

```CFEL
Relation//DIRECT ((HAS_INVERSE)) Relation//INVERSE;
```
""")
        relation.write_text(relation.read_text().replace("subjects: {}", "subjects:\n  active: CFEL <+ Relation//DIRECT"))
        inverse = self.source("native-model/inverse.md", "CA-R-797", form="Relation Declaration", body="""## Claim

### Formal Claim

```CFEL
Relation//INVERSE <((HAS_INVERSE)) Relation//DIRECT;
```
""")
        inverse.write_text(inverse.read_text().replace("subjects: {}", "subjects:\n  active: CFEL <+ Relation//INVERSE"))
        schema = json.loads(compile_project_schema(self.root))
        columns = schema["modes"]["2"]["content"]["content_columns"]
        self.assertEqual(["content.summary"], [column["name"] for column in columns])
        self.assertIn(declaration.relative_to(self.root).as_posix(), {item["path"] for item in schema["sources"]})
        registry = json.loads(compile_project_registry(self.root))
        self.assertEqual(["DIRECT", "INVERSE"], registry["registered_names"])
        self.assertEqual([{"direct": "DIRECT", "inverse": "INVERSE"}], registry["inverse_bindings"])
        self.assertEqual({"CA-R-796", "CA-R-797"}, {item["atom_id"] for item in registry["sources"]})

    def test_registry_prefers_current_declared_scope_source_over_earlier_copy(self):
        copied = self.source("000_copy/record.md", "CA-R-810", form="Relation Declaration", body="""## Claim

### Formal Claim

```CFEL
Relation//STALE;
```
""")
        native = self.fixture._write_atom(
            "MAIN", "04_requirement", "native.md", atom_id="CA-R-810", version=2,
            form="Relation Declaration", body="""## Claim

### Formal Claim

```CFEL
Relation//CURRENT;
```
""",
        )
        atoms, _, _ = self.fixture._capture()
        self.assertEqual(str(copied.relative_to(self.root)), next(row["source_path"] for row in atoms if row["id"] == "CA-R-810"))
        registry = json.loads(compile_project_registry(self.root))
        self.assertIn("CURRENT", registry["registered_names"])
        self.assertNotIn("STALE", registry["registered_names"])
        pin = next(row for row in registry["sources"] if row["atom_id"] == "CA-R-810")
        self.assertEqual((2, native.relative_to(self.root).as_posix()), (pin["version"], pin["path"]))

    def test_schema_prefers_current_declared_scope_source_over_earlier_copy(self):
        template = "## Claim\n\n### Formal Claim\n\n```CFEL\nAtom.Content.{}{{::1}}:: {{::1}};\n```\n"
        self.source("000_copy/record.md", "CA-R-809", body=template.format("Old Field"))
        native = self.fixture._write_atom(
            "MAIN", "04_requirement", "native.md", atom_id="CA-R-809", version=2,
            form="Declaration", body=template.format("Current Field"),
        )
        schema = json.loads(compile_project_schema(self.root))
        for mode in ("1", "2"):
            columns = schema["modes"][mode]["content"]["content_columns"]
            self.assertEqual(["content.current_field"], [column["name"] for column in columns])
        pins = {(row["version"], row["path"]) for row in schema["sources"] if row["atom_id"] == "CA-R-809"}
        self.assertIn((2, native.relative_to(self.root).as_posix()), pins)

    def test_registry_skips_invalid_duplicate_scope_data(self):
        self.source("000_copy/record.md", "CA-R-811", form="Rule")
        invalid = self.fixture._write_atom(
            "MAIN", "04_requirement", "invalid.md", atom_id="CA-R-811", form="Rule",
            body="## Summary\n\nInvalid ordinary data.\n",
        )
        self.source("loose/relation.md", "CA-R-812", form="Relation Declaration", body="""## Claim

### Formal Claim

```CFEL
Relation//VALID;
```
""")
        schema = fixtures.source_reader_module.SourceContentSchema
        original = schema.validation_errors
        invalid_path = invalid.relative_to(self.root).as_posix()

        def validation_errors(instance, rows, *args, **kwargs):
            rows = list(rows)
            if any(row.get("source_path") == invalid_path for row in rows):
                raise AssertionError("ordinary duplicate passed to registry validation")
            return original(instance, rows, *args, **kwargs)

        with patch.object(schema, "validation_errors", validation_errors):
            registry = json.loads(compile_project_registry(self.root))
        self.assertIn("VALID", registry["registered_names"])


if __name__ == "__main__":
    unittest.main()
