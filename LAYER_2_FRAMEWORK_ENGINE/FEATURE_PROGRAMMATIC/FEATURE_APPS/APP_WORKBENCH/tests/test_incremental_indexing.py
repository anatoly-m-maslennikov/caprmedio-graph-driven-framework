# CA-E-677@14
"""Real file-to-DuckDB deltas without full schema or graph work."""
from contextlib import ExitStack
from pathlib import Path
import re
import sys
import tempfile
import unittest
from unittest.mock import patch

APP_ROOT = Path(__file__).resolve().parents[2]
sys.path[:0] = [str(APP_ROOT), str(APP_ROOT.parent / "FEATURE_TOOLS"), str(Path(__file__).parent)]
from APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.query_store import QueryStore  # noqa: E402
from APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.service import WorkbenchService  # noqa: E402
from scope_declaration_test_support import write_scope_unit_declarations  # noqa: E402
from smalltest_support import built_assets, extension_directory, source_path, write_atom, write_settings  # noqa: E402

BACKEND = "APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND."


class IncrementalIndexingTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        control = write_settings(self.root)
        self.declarations = write_scope_unit_declarations(
            self.root, ({"scope_unit_name": "ENGINE", "scope_unit_type": "Ordered", "scope_unit_label": "LAYER", "local_order": 1},),
            control_root=control,
        )
        self.paths = {key: source_path(self.declarations, "ENGINE", "04_requirement", f"{key}.md") for key in ("A", "B", "C", "D", "relation")}
        for key in ("B", "C", "D"):
            write_atom(self.paths[key], f"CA-R-{key}")
        write_atom(self.paths["A"], "CA-R-A", relations="{BLOCKS: 'CA-R-B'}")
        write_atom(
            self.paths["relation"], "CA-R-REL", subjects="{governs: ['Relation//BLOCKS', 'Relation//IS_BLOCKED_BY']}",
            body=(
                "## Claim\n\n### Formal Claim\n\n```CFEL\n"
                "Relation//BLOCKS ((HAS_CLASSIFICATION)) Derivation == Direct;\n"
                "Relation//BLOCKS ((HAS_INVERSE)) Relation//IS_BLOCKED_BY;\n"
                "```\n"
            ),
        )
        self.service = WorkbenchService(self.root, **built_assets(self.root))
        self.service._store = QueryStore(extension_directory=extension_directory(APP_ROOT.parents[2]))
        self.addCleanup(self.service.close)
        self.service._refresh()
        self.store = self.service._store

    def event(self, path, *, old=None, operation="update"):
        return {"operation": operation, "old_path": old.relative_to(self.root).as_posix() if old else None,
                "new_path": path.relative_to(self.root).as_posix() if path else None}

    def no_full_work(self):
        stack = ExitStack()
        for name in (
            "header_columns.HeaderSchemaState.from_atoms", "query_store.compile_content_schema",
            "source_content_schema.SourceContentSchema.rebuild", "projection_delta.snapshot",
            "graph_store.graph_state", "incremental_relations._full_state",
        ):
            stack.enter_context(patch(BACKEND + name, side_effect=AssertionError("ordinary delta attempted " + name)))
        return stack

    def graph(self):
        return self.store.run(
            "FROM GRAPH_TABLE (caprmedio MATCH (a:Reference)-[e:BLOCKS]->(b:Reference) "
            "COLUMNS (a.ref AS source, b.ref AS target)) ORDER BY source, target"
        )["rows"]

    def test_value_and_relation_edit_skip_full_builders_and_keep_unrelated_row(self):
        previous = self.store._projection
        untouched = next(row for row in previous.atoms.values() if row["reference"] == "CA-R-D")
        self.assertEqual([["CA-R-A", "CA-R-B"]], self.graph())
        write_atom(self.paths["A"], "CA-R-A", version=2, relations="{BLOCKS: 'CA-R-C'}")
        with self.no_full_work():
            self.service._refresh([self.event(self.paths["A"])])
        self.assertEqual([["CA-R-A", "CA-R-C"]], self.graph())
        self.assertEqual([[2]], self.store.run(
            'SELECT "header.version" FROM atoms WHERE "header.atom_id"=\'CA-R-A\''
        )["rows"])
        current_untouched = next(row for row in self.store._projection.atoms.values() if row["reference"] == "CA-R-D")
        self.assertIs(untouched, current_untouched)
        self.assertEqual(1, len(previous.graph.edges["BLOCKS"]))

    def test_remove_and_reappear_preserve_dangling_target_then_rename_stays_delta(self):
        old = self.paths["B"]
        old.unlink()
        with self.no_full_work():
            self.service._refresh([self.event(None, old=old, operation="remove")])
        self.assertEqual([["CA-R-A", "CA-R-B"]], self.graph())
        self.assertEqual([[0]], self.store.run(
            'SELECT count(*) FROM atoms WHERE "header.atom_id"=\'CA-R-B\''
        )["rows"])
        write_atom(old, "CA-R-B")
        with self.no_full_work():
            self.service._refresh([self.event(old, operation="create")])
        renamed = old.with_name("CA-R-B-renamed.md")
        old.rename(renamed)
        with self.no_full_work():
            self.service._refresh([self.event(renamed, old=old, operation="rename")])
        self.assertEqual([["CA-R-B-renamed.md"]], self.store.run(
            'SELECT filename FROM atoms WHERE "header.atom_id"=\'CA-R-B\''
        )["rows"])
        self.assertEqual([["CA-R-A", "CA-R-B"]], self.graph())

    def test_scope_declaration_full_capture_diffs_without_replacing_projection(self):
        declaration = Path(self.declarations["ENGINE"]["declaration_path"])
        saved = self.store.run("SELECT 42 AS marker")
        before_edges = self.graph()
        before_audits = self.store.run("SELECT count(*) FROM atom_physical_carrier_issues")["rows"]
        text, count = re.subn(r"(?m)^version: [0-9]+$", "version: 2", declaration.read_text())
        self.assertEqual(1, count)
        declaration.write_text(text)
        with patch.object(self.store, "replace", side_effect=AssertionError("projection replaced")), \
             patch.object(self.store, "apply", wraps=self.store.apply) as apply:
            self.service._refresh([self.event(declaration)])
        self.assertIsNone(apply.call_args.kwargs["delta"])
        self.assertEqual([[2]], self.store.run(
            "SELECT declaration_version FROM scope_units WHERE name = 'ENGINE'"
        )["rows"])
        self.assertEqual(before_edges, self.graph())
        self.assertEqual(before_audits, self.store.run("SELECT count(*) FROM atom_physical_carrier_issues")["rows"])
        self.assertEqual([[42]], self.store.page(saved["query_id"], 0)["rows"])

    def test_declaration_changes_require_new_built_assets(self):
        declaration = self.paths["relation"].with_name("CA-R-content-model.md")
        def model(field):
            write_atom(declaration, "CA-R-MODEL", body=(
                "## Claim\n\n### Formal Claim\n\n```CFEL\n"
                f"Atom.Content.{field}{{::1}}:: {{::1}};\n```\n"
            ))
            declaration.write_text(declaration.read_text().replace('form: "Definition"', 'form: "Declaration"'))

        model("Summary")
        old_assets = built_assets(self.root)
        self.service.close()

        def open_with(assets):
            service = WorkbenchService(self.root, **assets)
            service._store = QueryStore(extension_directory=extension_directory(APP_ROOT.parents[2]))
            service._refresh()
            return service

        self.service = open_with(old_assets)
        self.addCleanup(lambda: self.service.close())
        def columns():
            return {row[0] for row in self.service._store.run("DESCRIBE atoms")["rows"]}

        self.assertIn("content.summary", columns())
        self.assertNotIn("content.details", columns())
        model("Details")
        write_atom(self.paths["A"], "CA-R-A", version=2)
        self.service._refresh([self.event(declaration), self.event(self.paths["A"])])
        self.assertIn("content.summary", columns())
        self.assertNotIn("content.details", columns())
        self.assertEqual([[2]], self.service._store.run(
            'SELECT "header.version" FROM atoms WHERE "header.atom_id"=\'CA-R-A\''
        )["rows"])
        self.service.close()
        self.service = open_with(old_assets)
        self.assertIn("content.summary", columns())
        self.assertNotIn("content.details", columns())
        self.service.close()
        self.service = open_with(built_assets(self.root))
        self.assertNotIn("content.summary", columns())
        self.assertIn("content.details", columns())

    def test_unchanged_source_skips_database_and_materialization(self):
        source = self.paths["A"]
        source.write_text(source.read_text())
        with patch(BACKEND + "service.materialize_delta", side_effect=AssertionError("no-op materialized")), self.no_full_work():
            self.service._refresh([self.event(source)])
        self.assertEqual([["CA-R-A", "CA-R-B"]], self.graph())


if __name__ == "__main__":
    unittest.main()
