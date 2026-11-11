from __future__ import annotations

from copy import deepcopy
import sys
import tempfile
import unittest
from pathlib import Path

import yaml

TOOLS = Path(__file__).resolve().parents[1]
if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))

from project_selection import resolve_project
from scope_declaration_parse import ScopeDeclarationError, parse_scope_unit_declaration
from scope_declaration_render import PROJECT, render_scope_declaration
from scope_unit_declarations import _selects_structural_form, read_scope_unit_declarations
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
        parent: str | None = None, project: bool = False, project_name: str = "demo",
    ) -> Path:
        source = source or self.control / "04_requirement" / f"{atom_id}-{name}.md"
        source.parent.mkdir(parents=True, exist_ok=True)
        source.write_text(render_scope_declaration(
            name=name, project_name=project_name, atom_id=atom_id, updated_at="2026-11-02 00:00:00 +0000",
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

    def test_formal_claim_layout_and_ambiguous_fences(self) -> None:
        source = self.declaration("demo", "CA-R-1", project=True)
        current = source.read_text(encoding="utf-8")
        self.assertIn("## Claim\n\n### Formal Claim\n\n```CFEL\n# instances", current)
        legacy = current.replace("### Formal Claim\n\n", "").replace("# instances\n", "")
        current += "\n### Prose Claim\n\nExplanation.\n\n## Unregistered heading\n\nMore prose.\n\n## Details\n\nDetails.\n"
        self.assertEqual("demo", parse_scope_unit_declaration(current.encode(), source).name)
        self.assertEqual("demo", parse_scope_unit_declaration(legacy.encode(), source).name)
        for invalid in (
            current + "\n```CFEL\nextra\n```\n",
            current.replace("### Formal Claim", "### Formal Claim\n\n```CFEL\nextra\n```\n\n### Formal Claim"),
            current + "\n```\nunterminated\n",
        ):
            with self.subTest(invalid=invalid), self.assertRaises(ScopeDeclarationError):
                parse_scope_unit_declaration(invalid.encode(), source)

    def test_cfel_comments_preserve_quoted_hash_and_reject_inline_junk(self) -> None:
        source = self.declaration("CHILD", "CA-R-2", scope_id="CA-SU-1", label="L#1", parent=PROJECT)
        current = source.read_text(encoding="utf-8")
        current = current.replace("# instances\n", "# model\n# explanatory comment\n# instances\n")
        self.assertEqual("L#1", parse_scope_unit_declaration(current.encode(), source).label)
        invalid = current.replace('"L#1";', '"L#1" # comment;')
        with self.assertRaises(ScopeDeclarationError):
            parse_scope_unit_declaration(invalid.encode(), source)
        variable = current.replace("Scope Unit//CHILD", "Scope Unit//$x")
        with self.assertRaises(ScopeDeclarationError):
            parse_scope_unit_declaration(variable.encode(), source)

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

    def test_prefixed_active_subjects_roundtrip_while_claims_stay_local(self) -> None:
        root_source = self.declaration(
            "caprmedio", "CA-R-1", source=self.control / "CA-R-1-caprmedio.md",
            project=True, project_name="caprmedio",
        )
        parent_source = self.declaration(
            "PARENT", "CA-R-2", scope_id="CA-SU-1", label="LAYER", ordered=True,
            order_number=1, parent=PROJECT, project_name="caprmedio",
        )
        child_source = self.declaration(
            "CHILD", "CA-R-3", source=self.control / "CA-SU-1_LAYER_1_PARENT" / "04_requirement" / "child.md",
            scope_id="CA-SU-2", label="FEATURE", parent="PARENT", project_name="caprmedio",
        )

        for source, local_subject in (
            (root_source, "Project//caprmedio"),
            (parent_source, "Scope Unit//PARENT"),
            (child_source, "Scope Unit//CHILD"),
        ):
            text = source.read_text(encoding="utf-8")
            self.assertIn(f'active: "CAPRMEDIO_STRUCTURE <+ {local_subject}"', text)
            self.assertIn(local_subject, text.split("## Claim", 1)[1])
            self.assertNotIn("CAPRMEDIO", text.split("## Claim", 1)[1])
            parsed = parse_scope_unit_declaration(text.encode(), source)
            self.assertEqual(parsed.name, local_subject.split("//", 1)[1])

    def test_legacy_bare_active_subject_remains_compatible(self) -> None:
        source = self.declaration(
            "UNIT", "CA-R-2", scope_id="CA-SU-2", parent=PROJECT, project_name="caprmedio",
        )
        raw = source.read_text(encoding="utf-8").replace(
            'CAPRMEDIO_STRUCTURE <+ Scope Unit//UNIT', "Scope Unit//UNIT",
        )
        source.write_text(raw, encoding="utf-8")

        self.assertEqual(parse_scope_unit_declaration(source.read_bytes(), source).name, "UNIT")

    def test_current_main_subject_replaces_legacy_active_subject(self) -> None:
        source = self.declaration(
            "UNIT", "CA-R-2", scope_id="CA-SU-2", parent=PROJECT, project_name="caprmedio",
        )
        source.write_text(source.read_text(encoding="utf-8").replace(
            "subjects:\n  active:", "topics:\n  main_subject:",
        ).replace("\n  passive: []", ""), encoding="utf-8")

        self.assertEqual(parse_scope_unit_declaration(source.read_bytes(), source).name, "UNIT")

    def test_missing_or_ambiguous_main_subject_refuses(self) -> None:
        source = self.declaration(
            "UNIT", "CA-R-2", scope_id="CA-SU-2", parent=PROJECT, project_name="caprmedio",
        )
        current = source.read_text(encoding="utf-8")
        missing = current.replace(
            'subjects:\n  active: "CAPRMEDIO_STRUCTURE <+ Scope Unit//UNIT"\n  passive: []\n', "",
        )
        equal_aliases = current.replace(
            "subjects:\n", "topics:\n  main_subject: \"CAPRMEDIO_STRUCTURE <+ Scope Unit//UNIT\"\nsubjects:\n",
        )
        ambiguous = equal_aliases.replace(
            'main_subject: "CAPRMEDIO_STRUCTURE <+ Scope Unit//UNIT"',
            'main_subject: "CAPRMEDIO_STRUCTURE <+ Scope Unit//OTHER"',
        )
        invalid_current = current.replace(
            "subjects:\n", "topics:\n  main_subject: 1\nsubjects:\n",
        )

        with self.assertRaisesRegex(ScopeDeclarationError, "requires one main Subject"):
            parse_scope_unit_declaration(missing.encode(), source)
        self.assertEqual("UNIT", parse_scope_unit_declaration(equal_aliases.encode(), source).name)
        with self.assertRaisesRegex(ScopeDeclarationError, "invalid declaration carrier"):
            parse_scope_unit_declaration(ambiguous.encode(), source)
        with self.assertRaisesRegex(ScopeDeclarationError, "invalid declaration carrier"):
            parse_scope_unit_declaration(invalid_current.encode(), source)

    def test_prefixed_active_subject_wrong_branch_refuses(self) -> None:
        source = self.declaration(
            "UNIT", "CA-R-2", scope_id="CA-SU-2", parent=PROJECT, project_name="caprmedio",
        )
        source.write_text(source.read_text(encoding="utf-8").replace(
            "CAPRMEDIO_STRUCTURE <+ Scope Unit//UNIT",
            "CAPRMEDIO_MODEL <+ Scope Unit//UNIT",
        ), encoding="utf-8")

        with self.assertRaisesRegex(ScopeDeclarationError, "namespace branch"):
            parse_scope_unit_declaration(source.read_bytes(), source)

    def test_named_structure_namespace_is_read_without_changing_the_source(self) -> None:
        source = self.declaration(
            "UNIT", "CA-R-2", scope_id="CA-SU-2", parent=PROJECT, project_name="caprmedio",
        )
        carrier = source.read_bytes().replace(
            b"CAPRMEDIO_STRUCTURE <+ Scope Unit//UNIT",
            b"PROJECT STRUCTURE//CAPRMEDIO <+ Scope Unit//UNIT",
        )
        self.assertEqual("UNIT", parse_scope_unit_declaration(carrier, source).name)
        with self.assertRaisesRegex(ScopeDeclarationError, "namespace branch"):
            parse_scope_unit_declaration(carrier.replace(b"PROJECT STRUCTURE//", b"MODEL//"), source)

    def test_prefixed_active_subject_invalid_namespace_chain_refuses(self) -> None:
        source = self.declaration(
            "UNIT", "CA-R-2", scope_id="CA-SU-2", parent=PROJECT, project_name="caprmedio",
        )
        source.write_text(source.read_text(encoding="utf-8").replace(
            "CAPRMEDIO_STRUCTURE <+ Scope Unit//UNIT",
            "CAPRMEDIO_STRUCTURE {1}<+ Scope Unit//UNIT",
        ), encoding="utf-8")

        with self.assertRaisesRegex(ScopeDeclarationError, "namespace chain"):
            parse_scope_unit_declaration(source.read_bytes(), source)

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

    def test_vanished_ordinary_requirement_does_not_block_declaration_discovery(self) -> None:
        self.complete_tree()
        ordinary = self.control / "04_requirement" / "CA-R-99-ordinary.md"
        ordinary.write_text("ordinary", encoding="utf-8")
        reader = ReadContext(roots=[str(self.root)], limits=dict(CEILINGS))
        original_read = reader.read

        def vanish(path: Path, *, remember: bool = True) -> bytes:
            if path == ordinary:
                ordinary.unlink()
            return original_read(path, remember=remember)

        reader.read = vanish  # type: ignore[method-assign]

        result = read_scope_unit_declarations(self.root, self.control.name, reader=reader)

        self.assertEqual({"demo", "PARENT", "CHILD"}, set(result.by_name))

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

    def test_non_root_scope_delegation_is_read_during_cutover(self) -> None:
        root_source, parent_source, child_source = self.complete_tree()
        parent_source.write_text(parent_source.read_text(encoding="utf-8").replace(
            "form: Scope Unit Declaration", "form: Scope Delegation",
        ), encoding="utf-8")

        declarations = read_scope_unit_declarations(self.root, self.control.name)

        self.assertEqual("Scope Unit Declaration", declarations.root.form)
        self.assertEqual("Scope Delegation", declarations.by_name["PARENT"].form)
        self.assertEqual("Scope Unit Declaration", declarations.by_name["CHILD"].form)
        self.assertEqual({root_source, parent_source, child_source}, set(declarations.paths))

    def test_encoded_scope_delegation_carrier_and_fail_closed_negatives(self) -> None:
        self.declaration("caprmedio", "CA-R-1", source=self.control / "CA-R-1-root.md", project=True, project_name="caprmedio")
        source = self.control / "04_requirement" / "CA-R-3034.md"
        source.parent.mkdir(parents=True, exist_ok=True)
        carrier = '''---
atom_id: CA-R-3034
ref_id: CA-R-3034
container:
  scope_unit: CA-SU-00
role: requirement
form: scope_delegation
subjects:
  active: "scope_unit//FRAMEWORK_METHODOLOGY"
tier: 3
status: active
version: 1
updated_at: "2026-11-10 22:57:48 +0400"
destination:
  file:
    name: CA-R-3034.md
    path: .caprmedio_demo/04_requirement
---

## Summary

Delegate FRAMEWORK_METHODOLOGY

## Claim

### Prose Claim

Delegation permissions.

### Formal Claim

```CFEL
# instances
Scope Unit//FRAMEWORK_METHODOLOGY.ID == "CA-SU-9";
Scope Unit//FRAMEWORK_METHODOLOGY.Name == "FRAMEWORK_METHODOLOGY";
Scope Unit//FRAMEWORK_METHODOLOGY.Label == "LAYER";
Scope Unit//FRAMEWORK_METHODOLOGY.order.ordered == true;
Scope Unit//FRAMEWORK_METHODOLOGY.order.number == 1;
Scope Unit//FRAMEWORK_METHODOLOGY ((IS_CONTAINED_BY)) Project//caprmedio
```
'''
        source.write_text(carrier, encoding="utf-8")
        declaration = read_scope_unit_declarations(self.root, self.control.name).by_name["FRAMEWORK_METHODOLOGY"]
        self.assertEqual((declaration.scope_unit_id, declaration.parent, declaration.form),
                         ("CA-SU-9", "caprmedio", "Scope Delegation"))
        for invalid in (
            carrier.replace("scope_unit//FRAMEWORK_METHODOLOGY", "scope_unit//framework_methodology"),
            carrier.replace("Scope Unit//FRAMEWORK_METHODOLOGY ((IS_CONTAINED_BY))", "scope_unit//FRAMEWORK_METHODOLOGY ((IS_CONTAINED_BY))"),
            carrier.replace("status: active", "status: inactive"),
            carrier.replace("atom_id: CA-R-3034", "atom_id: CA-R-3034\natom_id: CA-R-3034"),
        ):
            with self.subTest(invalid=invalid), self.assertRaises(ScopeDeclarationError):
                source.write_text(invalid, encoding="utf-8")
                read_scope_unit_declarations(self.root, self.control.name)

    def test_nested_non_root_scope_delegation_is_read_during_cutover(self) -> None:
        _, parent_source, child_source = self.complete_tree()
        raw = parent_source.read_text(encoding="utf-8")
        _, frontmatter, body = raw.split("---", 2)
        header = yaml.safe_load(frontmatter)
        header.setdefault("context", {})["form"] = "Scope Delegation"
        header.pop("form", None)
        parent_source.write_text(
            "---\n" + yaml.safe_dump(header, sort_keys=False) + "---" + body,
            encoding="utf-8",
        )

        declarations = read_scope_unit_declarations(self.root, self.control.name)

        self.assertEqual("Scope Delegation", declarations.by_name["PARENT"].form)
        self.assertEqual("CHILD", declarations.by_name["CHILD"].name)

    def test_structural_form_reader_accepts_valid_header_indentation_and_flow_style(self) -> None:
        for serializer in (
            lambda value: yaml.safe_dump(value, sort_keys=False, indent=4),
            lambda value: yaml.safe_dump(value, sort_keys=False, default_flow_style=True),
        ):
            with self.subTest(serializer=serializer):
                _, parent_source, _ = self.complete_tree()
                _, frontmatter, body = parent_source.read_text(encoding="utf-8").split("---", 2)
                header = yaml.safe_load(frontmatter)
                header.setdefault("context", {})["form"] = "Scope Delegation"
                header.pop("form", None)
                parent_source.write_text("---\n" + serializer(header) + "---" + body, encoding="utf-8")

                declarations = read_scope_unit_declarations(self.root, self.control.name)

                self.assertEqual("Scope Delegation", declarations.by_name["PARENT"].form)

    def test_nested_non_header_form_is_not_a_structural_candidate(self) -> None:
        raw = b"""---
context:
  role: Requirement
  form: Policy
parameters:
  form: Scope Delegation
---
"""

        self.assertFalse(_selects_structural_form(raw))

    def test_malformed_canonical_flow_form_fails_closed(self) -> None:
        for context in (
            "context: {form: Scope Delegation, role: Requirement",
            "context: {role: Requirement, form: Scope Delegation",
        ):
            with self.subTest(context=context):
                raw = f"---\n{context}\n---\n".encode()
                self.assertTrue(_selects_structural_form(raw))

        unrelated = b"---\nparameters: {form: Scope Delegation\n---\n"
        self.assertFalse(_selects_structural_form(unrelated))

    def test_scope_delegation_allows_prose_before_its_formal_claim(self) -> None:
        _, parent_source, _ = self.complete_tree()
        raw = parent_source.read_text(encoding="utf-8").replace(
            "form: Scope Unit Declaration", "form: Scope Delegation",
        ).replace("### Formal Claim\n\n", "Delegation permissions.\n\n### Formal Claim\n\n")

        self.assertEqual("PARENT", parse_scope_unit_declaration(raw.encode(), parent_source).name)

        with self.assertRaisesRegex(ScopeDeclarationError, "ambiguous Claim container"):
            parse_scope_unit_declaration(
                raw.replace("form: Scope Delegation", "form: Scope Unit Declaration").encode(), parent_source,
            )

    def test_project_root_scope_delegation_refuses(self) -> None:
        source = self.declaration("demo", "CA-R-1", source=self.control / "CA-R-1-demo.md", project=True)
        source.write_text(source.read_text(encoding="utf-8").replace(
            "form: Scope Unit Declaration", "form: Scope Delegation",
        ), encoding="utf-8")

        with self.assertRaisesRegex(ScopeDeclarationError, "Project Scope Unit must use Scope Unit Declaration"):
            parse_scope_unit_declaration(source.read_bytes(), source)
        with self.assertRaisesRegex(ScopeDeclarationError, "Project Scope Unit must use Scope Unit Declaration"):
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
