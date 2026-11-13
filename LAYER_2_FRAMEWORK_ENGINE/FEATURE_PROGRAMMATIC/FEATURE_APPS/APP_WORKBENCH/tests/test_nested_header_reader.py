# CA-E-675@14
# CA-E-677@14
"""Nested Header reading stays source-faithful and graph-compatible."""

from __future__ import annotations

from pathlib import Path
import sys
import tempfile
import unittest
from unittest import mock


APP_ROOT = Path(__file__).resolve().parents[2]
TOOLS_ROOT = APP_ROOT.parent / "FEATURE_TOOLS"
sys.path[:0] = [str(APP_ROOT), str(TOOLS_ROOT), str(TOOLS_ROOT / "VALIDATE_ATOMS")]

from scope_declaration_test_support import write_scope_unit_declarations  # noqa: E402
from smalltest_support import write_settings  # noqa: E402
from APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.relations import materialize  # noqa: E402
from APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND import content_schema as content_schema_module  # noqa: E402
from APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.source_reader import SourceReader  # noqa: E402
from APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.source_watcher import SourceWatcher  # noqa: E402


class NestedHeaderReaderTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name) / "project"
        self.root.mkdir()
        self.control = write_settings(self.root)
        self.declarations = write_scope_unit_declarations(
            self.root,
            ({"scope_unit_name": "MAIN", "scope_unit_label": "LAYER"},),
            control_root=self.control,
        )
        self.reader = SourceReader(self.root)

    def _path(self, name: str) -> Path:
        name = "CA-R-" + name
        path = Path(self.declarations["MAIN"]["authority_path"]) / "04_requirement" / name
        path.parent.mkdir(parents=True, exist_ok=True)
        return path

    def _nested(
        self, name: str, atom_id: str, *, form: str = "Definition",
        container: str | None = None, container_kind: str = "scope_unit", topic: str | None = None,
        body: str = "# Summary\n\nNested source.\n",
    ) -> Path:
        context = "  role: Requirement\n  form: " + form + "\n  tier: 2\n"
        if container is not None:
            context = f"  container:\n    {container_kind}: {container}\n" + context
        if topic is not None:
            context += f"  topics:\n    main_subject: {topic}\n    dependencies: []\n"
        path = self._path(name)
        path.write_text(
            "---\n"
            f"identity:\n  atom_id: {atom_id}\n  ref_id: {atom_id}\n"
            f"context:\n{context}"
            "relations: {}\n"
            "state:\n  status: Active\n  version: 3\n"
            "  updated_at: \"2026-11-06 12:00:00 +0400\"\n"
            "destination:\n  file:\n"
            f"    name: {Path(name).name}\n    path: current\n"
            "---\n" + body,
            encoding="utf-8",
        )
        return path

    def _model_declaration(self, name: str, atom_id: str, statement: str) -> Path:
        return self._nested(
            name,
            atom_id,
            form="Declaration",
            body=f"## Claim\n\n### Formal Claim\n\n```CFEL\n{statement}\n```\n",
        )

    def test_nested_and_flat_headers_keep_typed_values_and_raw_properties(self) -> None:
        nested = self._nested("nested.md", "CA-R-101", topic="Subject/Graph/Node")
        flat = self._path("flat.md")
        flat.write_text(
            "---\natom_id: CA-R-102\nrole: Requirement\nform: Definition\n"
            "status: Active\nversion: 2\ntier: 1\nsubjects: {}\nrelations: {}\n---\n# Summary\n\nFlat.\n",
            encoding="utf-8",
        )

        atoms, _scopes = self.reader.capture()
        by_id = {row["id"]: row for row in atoms}

        self.assertEqual(
            ("CA-R-101", "CA-R-101", 3, "Active", "Requirement", "Definition", 2),
            tuple(by_id["CA-R-101"][name] for name in ("id", "ref", "version", "status", "role", "form", "tier")),
        )
        self.assertNotIn("atom_id", by_id["CA-R-101"]["header_json"])
        self.assertEqual("CA-R-101", by_id["CA-R-101"]["header_json"]["identity"]["atom_id"])
        self.assertEqual("CA-R-102", by_id["CA-R-102"]["id"])
        self.assertEqual(nested.relative_to(self.root).as_posix(), by_id["CA-R-101"]["source_path"])

    def test_nested_identity_id_is_read_without_rewriting_the_raw_header(self) -> None:
        source = self._path("identity-id.md")
        source.write_text(
            "---\n"
            "identity:\n  id: CA-R-103\n  ref_id: CA-R-103\n"
            "context:\n  role: Requirement\n  form: Definition\n  tier: 2\n"
            "relations: {}\n"
            "state:\n  status: Active\n  version: 3\n"
            "destination:\n  file:\n    name: identity-id.md\n    path: current\n"
            "---\n# Summary\n\nNested source.\n",
            encoding="utf-8",
        )

        atoms, _scopes = self.reader.capture()
        row = next(item for item in atoms if item["id"] == "CA-R-103")

        self.assertEqual(("CA-R-103", "CA-R-103"), (row["id"], row["ref"]))
        self.assertEqual("CA-R-103", row["header_json"]["identity"]["id"])
        self.assertNotIn("atom_id", row["header_json"]["identity"])

    def test_nested_topics_and_containers_make_direct_and_derived_graph_facts(self) -> None:
        self._nested(
            "contained-by.md", "CA-R-201", form="Relation Definition",
            topic="Subject/Graph/Relation//IS_CONTAINED_BY",
            body="## Claim\n\n### Formal Claim\n\n```CFEL\nRelation//IS_CONTAINED_BY ((HAS_INVERSE)) Relation//CONTAINS;\n```\n",
        )
        self._nested(
            "contains.md", "CA-R-202", form="Relation Definition",
            topic="Subject/Graph/Relation//CONTAINS",
        )
        self._nested("parent.md", "CA-R-203", container="TEST-SU-1")
        self._nested("child.md", "CA-R-204", container="CA-R-203", container_kind="atom")

        atoms, scopes = materialize(*self.reader.capture())
        by_ref = {row["ref"]: row for row in atoms}
        by_scope = {row["name"]: row for row in scopes}

        self.assertIn(
            {"source_kind": "Atom", "source_ref": "CA-R-203", "target_kind": "Scope Unit",
             "target_ref": "MAIN", "relation_type": "IS_CONTAINED_BY", "derived": False},
            by_ref["CA-R-203"]["relation_edges_json"],
        )
        self.assertIn(
            {"source_kind": "Scope Unit", "source_ref": "MAIN", "target_kind": "Atom",
             "target_ref": "CA-R-203", "relation_type": "CONTAINS", "derived": True},
            by_scope["MAIN"]["relation_edges_json"],
        )
        self.assertIn(
            {"source_kind": "Atom", "source_ref": "CA-R-204", "target_kind": "Atom",
             "target_ref": "CA-R-203", "relation_type": "IS_CONTAINED_BY", "derived": False},
            by_ref["CA-R-204"]["relation_edges_json"],
        )
        self.assertIn(
            {"source_kind": "Atom", "source_ref": "CA-R-203", "target_kind": "Atom",
             "target_ref": "CA-R-204", "relation_type": "CONTAINS", "derived": True},
            by_ref["CA-R-203"]["relation_edges_json"],
        )

    def test_declaration_directory_move_rebuilds_scope_inventory(self) -> None:
        self.reader.capture()
        directory = Path(self.declarations["MAIN"]["declaration_path"]).parent
        moved = self.control / "moved-declarations"
        directory.rename(moved)

        _atoms, scopes = self.reader.capture([{
            "operation": "move",
            "old_path": directory.relative_to(self.root).as_posix(),
            "new_path": moved.relative_to(self.root).as_posix(),
        }])

        self.assertEqual(["fixture"], [row["name"] for row in scopes])

    def test_lexical_symlink_replacement_removes_cached_source(self) -> None:
        source = self._nested("replace-me.md", "CA-R-301")
        self.reader.capture()
        outside = self.root / "outside.md"
        outside.write_text("outside\n", encoding="utf-8")
        source.unlink()
        source.symlink_to(outside)

        atoms, _scopes = self.reader.capture([{
            "operation": "update", "old_path": None,
            "new_path": source.relative_to(self.root).as_posix(),
        }])
        watcher = SourceWatcher(self.root, self.control)

        self.assertNotIn("CA-R-301", {row["id"] for row in atoms})
        self.assertEqual(source.relative_to(self.root).as_posix(), watcher._relative(str(source)))
        self.assertIsNone(watcher._relative(str(self.control / ".." / "outside.md")))

    def test_symlinked_parent_replacement_removes_cached_source(self) -> None:
        source = self._nested("linked/escaped.md", "CA-R-302")
        self.reader.capture()
        outside = self.root / "outside"
        source.parent.rename(outside)
        source.parent.symlink_to(outside, target_is_directory=True)

        atoms, _scopes = self.reader.capture([{
            "operation": "update", "old_path": None,
            "new_path": source.relative_to(self.root).as_posix(),
        }])

        self.assertNotIn("CA-R-302", {row["id"] for row in atoms})

    def test_declared_content_duplicates_are_excluded_but_arbitrary_headings_remain_raw(self) -> None:
        self._model_declaration("content-model.md", "CA-R-401", "Atom.Content.Summary{::1}:: {::1};")
        self._nested("valid.md", "CA-R-402", body="# Summary\n\nOne\n\n## Arbitrary heading\n\nTwo\n")
        self._nested("duplicate.md", "CA-R-403", body="# Summary\n\nOne\n\n# Summary\n\nTwo\n")

        atoms, _scopes = self.reader.capture()

        ids = {row["id"] for row in atoms}
        self.assertIn("CA-R-401", ids)
        self.assertIn("CA-R-402", ids)
        self.assertNotIn("CA-R-403", ids)
        self.assertEqual(("content.summary",), self.reader._content_schema.schema.names)
        self.assertEqual(1, self.reader.excluded_count)

    def test_content_model_change_rebuilds_the_cached_schema(self) -> None:
        declaration = self._model_declaration(
            "content-model.md", "CA-R-404", "Atom.Content.Summary{::1}:: {::1};",
        )
        self._nested("duplicate.md", "CA-R-405", body="# Summary\n\nOne\n\n# Summary\n\nTwo\n")
        first, _scopes = self.reader.capture()
        self.assertNotIn("CA-R-405", {row["id"] for row in first})
        self._model_declaration("content-model.md", "CA-R-404", "Atom.Content.Title{::1}:: {::1};")

        atoms, _scopes = self.reader.capture([{
            "operation": "update", "old_path": None,
            "new_path": declaration.relative_to(self.root).as_posix(),
        }])

        self.assertEqual(("content.title",), self.reader._content_schema.schema.names)
        self.assertIn("CA-R-405", {row["id"] for row in atoms})

    def test_ordinary_update_uses_the_cached_content_schema(self) -> None:
        source = self._nested("ordinary.md", "CA-R-406")
        self.reader.capture()
        self._nested("ordinary.md", "CA-R-406", body="# Summary\n\nUpdated.\n")

        with (
            mock.patch.object(self.reader, "_capture_full", side_effect=AssertionError("full capture")),
            mock.patch.object(
                content_schema_module, "compile_content_schema", side_effect=AssertionError("all source compile"),
            ),
        ):
            atoms, _scopes = self.reader.capture([{
                "operation": "update", "old_path": None,
                "new_path": source.relative_to(self.root).as_posix(),
            }])

        self.assertIn("CA-R-406", {row["id"] for row in atoms})
        self.assertEqual("CA-R-406", self.reader.capture_delta[source.relative_to(self.root).as_posix()]["id"])

    def test_same_shape_declaration_update_refreshes_schema_provenance_without_full_capture(self) -> None:
        declaration = self._model_declaration(
            "content-model.md", "CA-R-407", "Atom.Content.Summary{::1}:: {::1};",
        )
        self.reader.capture()
        declaration.write_text(
            declaration.read_text(encoding="utf-8").replace("version: 3", "version: 4"), encoding="utf-8",
        )

        with mock.patch.object(self.reader, "_capture_full", side_effect=AssertionError("full capture")):
            self.reader.capture([{
                "operation": "update", "old_path": None,
                "new_path": declaration.relative_to(self.root).as_posix(),
            }])

        source = next(item for item in self.reader.content_schema.sources if item.reference == "CA-R-407")
        self.assertEqual(4, source.version)

    def test_role_filter_change_and_declaration_removal_rebuild_content_schema(self) -> None:
        declaration = self._model_declaration(
            "content-model.md", "CA-R-408", "Atom.Content.Summary{::1}:: {::1};",
        )
        self.reader.capture()
        self._model_declaration(
            "content-model.md", "CA-R-408",
            "Atom/(.Header.Role := Plan).Content.Summary{::1}:: {::1};",
        )

        with mock.patch.object(self.reader, "_capture_full", wraps=self.reader._capture_full) as full:
            self.reader.capture([{
                "operation": "update", "old_path": None,
                "new_path": declaration.relative_to(self.root).as_posix(),
            }])
        self.assertEqual(1, full.call_count)
        declaration.unlink()
        with mock.patch.object(self.reader, "_capture_full", wraps=self.reader._capture_full) as full:
            self.reader.capture([{
                "operation": "remove", "old_path": declaration.relative_to(self.root).as_posix(),
                "new_path": None,
            }])
        self.assertEqual(1, full.call_count)

    def test_invalid_incremental_source_has_a_none_delta_entry(self) -> None:
        self._model_declaration("content-model.md", "CA-R-409", "Atom.Content.Summary{::1}:: {::1};")
        source = self._nested("invalid.md", "CA-R-410")
        self.reader.capture()
        self._nested("invalid.md", "CA-R-410", body="# Summary\n\nOne\n\n# Summary\n\nTwo\n")

        self.reader.capture([{
            "operation": "update", "old_path": None,
            "new_path": source.relative_to(self.root).as_posix(),
        }])

        self.assertIsNone(self.reader.capture_delta[source.relative_to(self.root).as_posix()])

    def test_duplicate_model_definition_keeps_first_and_admits_repaired_copy(self) -> None:
        first = self._model_declaration(
            "first-model.md", "CA-R-411", "Atom.Content.Summary{::1}:: {::1};",
        )
        duplicate = self._model_declaration(
            "duplicate-model.md", "CA-R-411", "Atom.Content.Summary{::1}:: {::1};",
        )
        self.reader.capture()
        self.assertEqual(("content.summary",), self.reader.content_schema.names)
        self.assertEqual(1, len(self.reader.content_schema.sources))
        duplicate.write_text(
            duplicate.read_text(encoding="utf-8").replace("CA-R-411", "CA-R-412"), encoding="utf-8",
        )

        with mock.patch.object(self.reader, "_capture_full", wraps=self.reader._capture_full) as full:
            self.reader.capture([{
                "operation": "update", "old_path": None,
                "new_path": duplicate.relative_to(self.root).as_posix(),
            }])

        self.assertEqual(0, full.call_count)
        self.assertEqual(("content.summary",), self.reader.content_schema.names)
        self.assertEqual(2, len(self.reader.content_schema.sources))
        self.assertTrue(first.is_file())


if __name__ == "__main__":
    unittest.main()
