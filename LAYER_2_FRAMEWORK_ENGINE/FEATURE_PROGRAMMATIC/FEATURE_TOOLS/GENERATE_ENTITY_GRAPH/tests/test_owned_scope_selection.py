"""Focused tests for metadata-owned Scope Unit selection preparation."""

from __future__ import annotations

import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path


TEST_TEMP_ROOT = Path.cwd() / ".caprmedio_tmp" / "tests" / Path(__file__).stem
TEST_TEMP_ROOT.mkdir(parents=True, exist_ok=True)
SCRIPT = Path(__file__).resolve().parents[1] / "owned_scope_selection.py"
TOOLS = SCRIPT.parents[1]
sys.path.insert(0, str(TOOLS))
SPEC = importlib.util.spec_from_file_location("owned_scope_selection_test", SCRIPT)
assert SPEC and SPEC.loader
selection = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = selection
SPEC.loader.exec_module(selection)

from scope_declaration_test_support import write_scope_unit_declarations  # noqa: E402


def atom(atom_id: str | None, owner: str | None, *, status: str = "Active") -> str:
    fields = []
    if atom_id is not None:
        fields.append(f"atom_id: {atom_id}")
    if owner is not None:
        fields.append(f"current_scope_unit: {owner}")
    fields.extend([
        f"status: {status}", "content_role: Requirement", "type: Definition", "version: 1",
        "subjects:", "  governs: Thing", "relations: {}",
    ])
    return "---\n" + "\n".join(fields) + "\n---\n# Atom\n"


class OwnedScopeSelectionTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory(dir=TEST_TEMP_ROOT, ignore_cleanup_errors=True)
        self.root = Path(self.temp.name) / "repo"
        control = self.root / ".caprmedio_fixture"
        control.mkdir(parents=True)
        (control / "caprmedio_project_settings.toml").write_text(
            '[project]\nname = "fixture"\n[paths]\ncontrol_root = ".caprmedio_fixture"\nprojection_root = ".caprmedio_fixture/_projection"\n', encoding="utf-8"
        )
        self.declarations = self.structure(["OWNED", "FOREIGN"])
        self.selected = Path(self.declarations["OWNED"]["delivery_path"])
        self.selected.mkdir(parents=True)

    def tearDown(self) -> None:
        self.temp.cleanup()

    def structure(self, names: list[str]) -> dict[str, dict[str, object]]:
        return write_scope_unit_declarations(
            self.root,
            tuple({"scope_unit_name": name, "parent": "PROJECT"} for name in names),
            control_root=self.root / ".caprmedio_fixture",
        )

    def write(self, name: str, contents: str) -> None:
        (self.selected / name).write_text(contents, encoding="utf-8")

    def test_selects_only_exact_owner_not_target_and_orders_ids(self) -> None:
        self.write("z.md", atom("Z", "OWNED"))
        self.write("a.md", atom("A", "OWNED"))
        foreign = atom("F", "FOREIGN").replace("type: Definition", "claim_target_scope_unit: OWNED\ntype: Definition")
        self.write("foreign.md", foreign)

        result = selection.prepare_owned_scope_selection(self.root, self.selected, "OWNED")

        self.assertEqual("prepared", result["outcome"])
        self.assertEqual(["A", "Z"], result["selection"]["atom_ids"])
        self.assertEqual(["OWNED"], result["selection"]["scope_unit_names"])
        self.assertEqual(["F"], [row["atom_id"] for row in result["inventory"]["support_sources"]])
        self.assertIn("scope_unit_declarations", result["source_frontier"])

    def test_empty_owned_selection_is_incomplete_and_inactive_is_excluded(self) -> None:
        self.write("old.md", atom("OLD", "OWNED", status="Inactive"))
        self.write("foreign.md", atom("F", "FOREIGN"))

        result = selection.prepare_owned_scope_selection(self.root, self.selected, "OWNED")

        self.assertEqual("incomplete", result["outcome"])
        self.assertEqual([], result["selection"]["atom_ids"])
        self.assertEqual(["F"], [row["atom_id"] for row in result["inventory"]["support_sources"]])

    def test_empty_source_set_is_incomplete(self) -> None:
        result = selection.prepare_owned_scope_selection(self.root, self.selected, "OWNED")
        self.assertEqual("incomplete", result["outcome"])
        self.assertEqual("atom-set-empty", result["diagnostics"][-1]["code"])

    def test_missing_explicit_property_fails_without_filename_fallback(self) -> None:
        self.write("FALLBACK.md", atom(None, "OWNED"))
        result = selection.prepare_owned_scope_selection(self.root, self.selected, "OWNED")
        self.assertEqual("failed", result["outcome"])
        self.assertEqual("owned-scope-property-missing", result["diagnostics"][-1]["code"])

    def test_duplicate_explicit_ids_fail_before_selection(self) -> None:
        self.write("one.md", atom("DUP", "OWNED"))
        self.write("two.md", atom("DUP", "FOREIGN"))
        result = selection.prepare_owned_scope_selection(self.root, self.selected, "OWNED")
        self.assertEqual("failed", result["outcome"])
        self.assertEqual("atom-id-duplicate", result["diagnostics"][-1]["code"])

    def test_duplicated_structure_rows_fail(self) -> None:
        self.structure(["OWNED", "OWNED"])
        self.write("one.md", atom("ONE", "OWNED"))
        result = selection.prepare_owned_scope_selection(self.root, self.selected, "OWNED")
        self.assertEqual("failed", result["outcome"])
        self.assertEqual("scope-unit-declaration-ambiguous", result["diagnostics"][-1]["code"])
