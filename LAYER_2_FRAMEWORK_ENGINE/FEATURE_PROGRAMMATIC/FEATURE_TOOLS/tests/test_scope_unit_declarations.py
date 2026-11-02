from __future__ import annotations

from copy import deepcopy
import sys
import tempfile
import unittest
from pathlib import Path

TOOLS = Path(__file__).resolve().parents[1]
if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))

from project_selection import resolve_project
from scope_declaration_parse import ScopeDeclarationError, parse_scope_unit_declaration
from scope_declaration_render import PROJECT, render_scope_declaration
from scope_unit_declarations import read_scope_unit_declarations
from VALIDATE_ATOMS.validate_atoms_workers.read_io import ReadContext
from VALIDATE_ATOMS.validate_atoms_workers.settings import CEILINGS


class ScopeUnitDeclarationReaderTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name).resolve()
        self.control = self.root / ".caprmedio_demo"
        self.control.mkdir()
        (self.control / "caprmedio_project_settings.toml").write_text(
            '[project]\nname = "demo"\n[paths]\ncontrol_root = ".caprmedio_demo"\n', encoding="utf-8",
        )

    def declaration(
        self, name: str, atom_id: str, *, source: Path | None = None, scope_id: str | None = None,
        label: str | None = None, ordered: bool = False, order_number: int | None = None,
        parent: str | None = None, project: bool = False,
    ) -> Path:
        source = source or self.control / "04_requirement" / f"{atom_id}-{name}.md"
        source.parent.mkdir(parents=True, exist_ok=True)
        source.write_text(render_scope_declaration(
            name=name, project_name="demo", atom_id=atom_id, updated_at="2026-11-02 00:00:00 +0000",
            scope_id=scope_id, label=label, ordered=ordered, order_number=order_number,
            parent=parent, project=project,
        ), encoding="utf-8")
        return source

    def complete_tree(self) -> tuple[Path, Path, Path]:
        root = self.declaration("demo", "CA-R-1", source=self.control / "CA-R-1-demo.md", project=True)
        parent = self.declaration(
            "PARENT", "CA-R-2", scope_id="CA-SU-1", label="LAYER", ordered=True,
            order_number=1, parent=PROJECT,
        )
        child = self.declaration(
            "CHILD", "CA-R-3", source=self.control / "CA-SU-1_LAYER_1_PARENT" / "04_requirement" / "child.md",
            scope_id="CA-SU-2", label="FEATURE", parent="PARENT",
        )
        return root, parent, child

    def test_discovers_current_sources_and_derives_all_paths(self) -> None:
        root_source, parent_source, child_source = self.complete_tree()
        result = read_scope_unit_declarations(self.root, self.control.name)

        self.assertEqual(result.root.name, "demo")
        self.assertEqual(tuple(result.paths), tuple(sorted((root_source, parent_source, child_source))))
        self.assertEqual(set(result.by_name), {"demo", "PARENT", "CHILD"})
        self.assertEqual(len(result.digest), 64)
        self.assertEqual(
            set(result.source_pins),
            {source.relative_to(self.root).as_posix() for source in (root_source, parent_source, child_source)},
        )
        rows = {row["scope_unit_name"]: row for row in result.as_structure()["scope_units"]}
        self.assertEqual(rows["demo"], {
            "scope_unit_name": "demo", "parent": "PROJECT", "scope_unit_id": None,
            "scope_unit_label": None, "scope_unit_type": "Unordered",
            "authority_path": ".caprmedio_demo", "delivery_path": ".",
        })
        self.assertEqual(rows["PARENT"]["authority_path"], ".caprmedio_demo/CA-SU-1_LAYER_1_PARENT")
        self.assertEqual(rows["PARENT"]["delivery_path"], "LAYER_1_PARENT")
        self.assertEqual(rows["CHILD"]["authority_path"], ".caprmedio_demo/CA-SU-1_LAYER_1_PARENT/CA-SU-2_FEATURE_CHILD")
        self.assertEqual(rows["CHILD"]["delivery_path"], "LAYER_1_PARENT/FEATURE_CHILD")

    def test_project_selection_exposes_derived_structure_and_declaration_provenance(self) -> None:
        self.complete_tree()
        selection = resolve_project(self.root)

        self.assertIn("scope_units", selection.structure)
        self.assertFalse(hasattr(selection, "structure_path"))
        self.assertEqual(len(selection.declaration_paths), 3)
        self.assertEqual(len(selection.declaration_digest), 64)
        self.assertEqual(len(selection.declaration_source_pins), 3)

    def test_deepcopy_retains_one_immutable_declaration_aggregate(self) -> None:
        self.complete_tree()
        declarations = read_scope_unit_declarations(self.root, self.control.name)

        copied = deepcopy({"scope_unit_declarations": declarations})

        self.assertIs(copied["scope_unit_declarations"], declarations)

    def test_draft_archived_generated_and_unrelated_legacy_carriers_are_not_sources(self) -> None:
        self.complete_tree()
        self.declaration(
            "DRAFT", "CA-R-4", source=self.control / "04_requirement" / "draft" / "draft.md",
            scope_id="CA-SU-4", parent=PROJECT,
        )
        self.declaration(
            "ARCHIVED", "CA-R-5", source=self.control / "04_requirement" / "archive" / "archive.md",
            scope_id="CA-SU-5", parent=PROJECT,
        )
        (self.control / "01_concern").mkdir()
        (self.control / "01_concern" / "broken.md").write_text("not an Atom", encoding="utf-8")

        result = read_scope_unit_declarations(self.root, self.control.name)
        self.assertNotIn("DRAFT", result.by_name)
        self.assertNotIn("ARCHIVED", result.by_name)

    def test_ordinary_current_requirement_does_not_conflict_with_declaration_frontier(self) -> None:
        self.complete_tree()
        ordinary = self.control / "04_requirement" / "CA-R-99-ordinary.md"
        ordinary.write_text(
            "---\natom_id: CA-R-99\nrole: Requirement\nform: Policy\nstatus: Active\nversion: 1\n---\n"
            "## Summary\n\nOrdinary Requirement\n",
            encoding="utf-8",
        )
        (self.control / "README.md").write_text("unrelated Markdown", encoding="utf-8")

        result = read_scope_unit_declarations(self.root, self.control.name)
        self.assertEqual(len(result.paths), 3)
        self.assertNotIn(ordinary, result.paths)

    def test_malformed_ordinary_requirement_is_outside_declaration_parser_boundary(self) -> None:
        self.complete_tree()
        ordinary = self.control / "04_requirement" / "CA-R-99-malformed-ordinary.md"
        ordinary.write_text(
            "---\natom_id: CA-R-99\natom_id: CA-R-99\nrole: Requirement\nform: Policy\n---\n",
            encoding="utf-8",
        )

        self.assertEqual(len(read_scope_unit_declarations(self.root, self.control.name).paths), 3)

    def test_malformed_selected_declaration_refuses(self) -> None:
        self.complete_tree()
        malformed = self.control / "04_requirement" / "CA-R-99-malformed-declaration.md"
        malformed.write_text(
            "---\natom_id: CA-R-99\natom_id: CA-R-99\nrole: Requirement\n"
            "form: 'Scope Unit Declaration'\nstatus: Active\nversion: 1\n---\n",
            encoding="utf-8",
        )

        with self.assertRaisesRegex(ScopeDeclarationError, "unique strings"):
            read_scope_unit_declarations(self.root, self.control.name)

    def test_projection_marked_copy_outside_projection_folder_is_not_authority(self) -> None:
        _, _, source = self.complete_tree()
        projected = self.control / "legacyapplied000" / "04_requirement" / "copied-declaration.md"
        projected.parent.mkdir(parents=True)
        projected.write_text(source.read_text(encoding="utf-8").replace(
            "relations: {}",
            "projection:\n  source_carrier_path: ../../CA-SU-1_LAYER_1_PARENT/04_requirement/child.md\nrelations: {}",
        ), encoding="utf-8")

        reader = ReadContext(roots=[str(self.root)], limits=dict(CEILINGS))
        original_read, read_paths = reader.read, []

        def record(path: Path, *, remember: bool = True) -> bytes:
            read_paths.append(path)
            return original_read(path, remember=remember)

        reader.read = record  # type: ignore[method-assign]
        result = read_scope_unit_declarations(self.root, self.control.name, reader=reader)
        self.assertEqual(len(result.paths), 3)
        self.assertNotIn(projected, result.paths)
        self.assertNotIn(projected, read_paths)

    def test_root_declaration_is_admitted_only_from_control_top_level(self) -> None:
        root_source, _, _ = self.complete_tree()
        result = read_scope_unit_declarations(self.root, self.control.name)

        self.assertEqual(result.root.source, root_source)
        self.assertEqual(root_source.parent, self.control)

    def test_project_root_declaration_in_requirement_folder_refuses(self) -> None:
        self.declaration("demo", "CA-R-1", project=True)

        with self.assertRaisesRegex(ScopeDeclarationError, "no current Scope Unit Declarations"):
            read_scope_unit_declarations(self.root, self.control.name)

    def test_parser_rejects_order_number_for_unordered_scope_unit(self) -> None:
        source = self.declaration("UNIT", "CA-R-2", scope_id="CA-SU-2", parent=PROJECT)
        source.write_text(source.read_text(encoding="utf-8").replace(
            "Scope Unit//UNIT.order.ordered == false;",
            "Scope Unit//UNIT.order.ordered == false;\nScope Unit//UNIT.order.number == 1;",
        ), encoding="utf-8")

        with self.assertRaisesRegex(ScopeDeclarationError, "required only"):
            parse_scope_unit_declaration(source.read_bytes(), source)

    def test_duplicate_scope_unit_name_refuses(self) -> None:
        self.declaration("demo", "CA-R-1", source=self.control / "CA-R-1-demo.md", project=True)
        self.declaration("UNIT", "CA-R-2", scope_id="CA-SU-2", parent=PROJECT)
        self.declaration(
            "UNIT", "CA-R-3", source=self.control / "04_requirement" / "duplicate.md",
            scope_id="CA-SU-3", parent=PROJECT,
        )

        with self.assertRaisesRegex(ScopeDeclarationError, "names and IDs"):
            read_scope_unit_declarations(self.root, self.control.name)

    def test_duplicate_scope_unit_id_refuses(self) -> None:
        self.declaration("demo", "CA-R-1", source=self.control / "CA-R-1-demo.md", project=True)
        self.declaration("FIRST", "CA-R-2", scope_id="TEST-SU-1", parent=PROJECT)
        self.declaration("SECOND", "CA-R-3", scope_id="TEST-SU-1", parent=PROJECT)

        with self.assertRaisesRegex(ScopeDeclarationError, "names and IDs"):
            read_scope_unit_declarations(self.root, self.control.name)

    def test_unsafe_control_root_refuses(self) -> None:
        with self.assertRaisesRegex(ScopeDeclarationError, "direct Project control"):
            read_scope_unit_declarations(self.root, "../.caprmedio_demo")

    def test_non_ca_scope_id_and_spaced_project_name_remain_declaration_data(self) -> None:
        (self.control / "caprmedio_project_settings.toml").write_text(
            '[project]\nname = "Friendly Demo"\n[paths]\ncontrol_root = ".caprmedio_demo"\n', encoding="utf-8",
        )
        self.declaration("Friendly Demo", "CA-R-1", source=self.control / "CA-R-1-demo.md", project=True)
        self.declaration("UNIT", "CA-R-2", scope_id="TEST-SU-1", parent="Friendly Demo")

        result = read_scope_unit_declarations(self.root, self.control.name)
        self.assertEqual(result.root.name, "Friendly Demo")
        self.assertEqual(result.by_name["UNIT"].scope_unit_id, "TEST-SU-1")


if __name__ == "__main__":
    unittest.main()
