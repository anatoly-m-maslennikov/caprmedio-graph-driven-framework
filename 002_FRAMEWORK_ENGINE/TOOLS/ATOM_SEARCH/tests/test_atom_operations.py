from __future__ import annotations

import argparse
import json
import tempfile
import unittest
from pathlib import Path

import sys

TOOLS = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(TOOLS))

import atom_operations as operations  # noqa: E402


class AtomOperationsTest(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary.name)
        (self.root / ".git").mkdir()
        self.requirements = self.root / ".caprmedio/UNIT/04_requirement"
        self.methods = self.root / ".caprmedio/UNIT/05_method"
        self.archive = self.requirements / "archive"
        self.drafts = self.requirements / "drafts"
        for directory in (self.requirements, self.methods, self.archive, self.drafts):
            directory.mkdir(parents=True, exist_ok=True)
        (self.root / ".caprmedio/project_graph_state.toml").write_text(
            '[[scope_units]]\nname = "CAPRMEDIO"\nprefix = "CA"\nauthority_path = ".caprmedio"\nstructural_kind = "project_root"\nstructural_parent = ""\n\n'
            '[[scope_units]]\nname = "UNIT"\nprefix = "UNIT"\nauthority_path = "UNIT"\nstructural_kind = "unordered_unit"\nstructural_parent = "CAPRMEDIO"\n',
            encoding="utf-8",
        )
        self.first = self._atom(self.requirements / "CA-R-343-REQUIREMENT-UNIT--first.md", "# First\n\nAlpha")
        self.second = self._atom(self.methods / "CA-M-101-IMPL_METHOD-UNIT--second.md", "# Second\n\nBeta")
        self._atom(self.archive / "CA-R-100-REQUIREMENT-UNIT--old.md", "# Old")
        self._atom(self.drafts / "CA-R--REQUIREMENT-UNIT--candidate.md", "# Candidate")
        (self.root / ".caprmedio/README.md").write_text("not an Atom", encoding="utf-8")

    def tearDown(self) -> None:
        self.temporary.cleanup()

    @staticmethod
    def _atom(path: Path, content: str, version: int = 1) -> Path:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(f"---\nsubject_scopes:\n  - test\ntier: standard\nversion: {version}\nupdated_at: 2026-01-01 00:00:00\n---\n{content}\n", encoding="utf-8")
        return path

    def _input(self, payload: dict) -> str:
        path = self.root / "input.json"
        path.write_text(json.dumps(payload), encoding="utf-8")
        return str(path)

    def test_resolves_id_filename_stem_and_path(self) -> None:
        selectors = ["CA-R-343", self.first.name, self.first.stem, self.first.relative_to(self.root).as_posix()]
        for selector in selectors:
            self.assertEqual(operations.resolve_selector(self.root, selector).atom_id, "CA-R-343")

    def test_read_views_are_selective_and_bulk(self) -> None:
        content = operations.run_read(self.root, argparse.Namespace(atom=["CA-R-343"], view="content"))
        self.assertEqual(set(content["atoms"][0]), {"content"})
        metadata = operations.run_read(self.root, argparse.Namespace(atom=["CA-R-343", "CA-M-101"], view="metadata"))
        self.assertEqual(metadata["count"], 2)
        self.assertEqual(set(metadata["atoms"][0]), {"metadata"})

    def test_search_filters_lifecycle_content_and_non_atoms(self) -> None:
        args = argparse.Namespace(under=None, lifecycle="active", atom=None, query=["beta"], limit=None, view="metadata")
        result = operations.run_search(self.root, args)
        self.assertEqual(result["count"], 1)
        self.assertEqual(result["atoms"][0]["metadata"]["atom_id"], "CA-M-101")
        self.assertNotIn("README.md", [atom.relative for atom in operations.scan_atoms(self.root)])

    def test_create_is_dry_run_then_bulk_apply(self) -> None:
        paths = [self.requirements / "CA-R-344-REQUIREMENT-UNIT--third.md", self.methods / "CA-M-102-IMPL_METHOD-UNIT--fourth.md"]
        payload = {"atoms": [{"path": path.relative_to(self.root).as_posix(), "frontmatter": "subject_scopes:\n  - test", "content": "# New\n"} for path in paths]}
        dry = operations.run_create(self.root, argparse.Namespace(input=self._input(payload), apply=False))
        self.assertEqual(dry["count"], 2)
        self.assertTrue(all(not path.exists() for path in paths))
        operations.run_create(self.root, argparse.Namespace(input=self._input(payload), apply=True))
        self.assertTrue(all(path.exists() for path in paths))
        self.assertIn("version: 1", paths[0].read_text(encoding="utf-8"))

    def test_create_collision_preflights_whole_bulk(self) -> None:
        new_path = self.requirements / "CA-R-344-REQUIREMENT-UNIT--new.md"
        payload = {"atoms": [
            {"path": new_path.relative_to(self.root).as_posix(), "content": "# New"},
            {"path": self.first.relative_to(self.root).as_posix(), "content": "# Collision"},
        ]}
        with self.assertRaises(operations.ToolError):
            operations.run_create(self.root, argparse.Namespace(input=self._input(payload), apply=True))
        self.assertFalse(new_path.exists())

    def test_update_preserves_identity_and_advances_revision(self) -> None:
        before_path = self.first
        payload = {"atoms": [{"selector": "CA-R-343", "content": "# Changed\n"}, {"selector": "CA-M-101", "frontmatter": "subject_scopes:\n  - changed\nversion: 4"}]}
        operations.run_update(self.root, argparse.Namespace(input=self._input(payload), apply=False))
        self.assertIn("Alpha", self.first.read_text(encoding="utf-8"))
        operations.run_update(self.root, argparse.Namespace(input=self._input(payload), apply=True))
        self.assertEqual(before_path, self.first)
        self.assertIn("# Changed", self.first.read_text(encoding="utf-8"))
        self.assertIn("version: 2", self.first.read_text(encoding="utf-8"))
        self.assertIn("version: 5", self.second.read_text(encoding="utf-8"))

    def test_move_is_dry_run_and_preserves_bytes(self) -> None:
        target = self.root / ".caprmedio/102_UNIT/04_requirement"
        before = self.first.read_bytes()
        args = argparse.Namespace(atom=["CA-R-343"], from_path=None, to=target.relative_to(self.root).as_posix(), flatten=False, apply=False)
        operations.run_move(self.root, args)
        self.assertTrue(self.first.exists())
        args.apply = True
        operations.run_move(self.root, args)
        moved = target / self.first.name
        self.assertEqual(moved.read_bytes(), before)
        self.assertFalse(self.first.exists())

    def test_bulk_move_preserves_subtree_by_default_and_flattens_explicitly(self) -> None:
        nested = self.archive / "nested"
        source_atom = self._atom(nested / "CA-R-101-REQUIREMENT-UNIT--nested.md", "# Nested")
        target = self.root / ".caprmedio/102_UNIT/04_requirement"
        args = argparse.Namespace(atom=None, from_path=self.requirements.relative_to(self.root).as_posix(), to=target.relative_to(self.root).as_posix(), flatten=False, apply=True)
        operations.run_move(self.root, args)
        self.assertTrue((target / "archive/nested" / source_atom.name).exists())
        flattened = self.root / ".caprmedio/103_UNIT/04_requirement"
        args = argparse.Namespace(atom=None, from_path=(target / "archive").relative_to(self.root).as_posix(), to=flattened.relative_to(self.root).as_posix(), flatten=True, apply=True)
        operations.run_move(self.root, args)
        self.assertTrue((flattened / source_atom.name).exists())

    def test_rejects_paths_outside_control_root(self) -> None:
        with self.assertRaises(operations.ToolError) as context:
            operations.safe_path(self.root, "outside.md")
        self.assertEqual(context.exception.code, "outside-control-root")

    def test_archive_is_dry_run_then_bulk_apply(self) -> None:
        first_bytes = self.first.read_bytes()
        args = argparse.Namespace(atom=["CA-R-343", "CA-M-101"], apply=False)
        result = operations.run_archive(self.root, args)
        self.assertEqual(result["count"], 2)
        self.assertTrue(self.first.exists())
        args.apply = True
        operations.run_archive(self.root, args)
        first_target = self.requirements / "archive" / self.first.name
        second_target = self.methods / "archive" / self.second.name
        self.assertEqual(first_target.read_bytes(), first_bytes)
        self.assertTrue(second_target.exists())

    def test_archive_rejects_drafts_and_archived_atoms(self) -> None:
        for selector in ("CA-R--REQUIREMENT-UNIT--candidate.md", "CA-R-100"):
            with self.assertRaises(operations.ToolError) as context:
                operations.run_archive(self.root, argparse.Namespace(atom=[selector], apply=False))
            self.assertEqual(context.exception.code, "atom-not-active")

    def test_promote_assigns_identity_and_preserves_bytes(self) -> None:
        draft = self.drafts / "CA-R--REQUIREMENT-UNIT--candidate.md"
        before = draft.read_bytes()
        payload = {"atoms": [{"selector": draft.name, "atom_id": "CA-R-344"}]}
        args = argparse.Namespace(input=self._input(payload), apply=False)
        result = operations.run_promote(self.root, args)
        target = self.requirements / "CA-R-344-REQUIREMENT-UNIT--candidate.md"
        self.assertEqual(result["count"], 1)
        self.assertTrue(draft.exists())
        self.assertFalse(target.exists())
        args.apply = True
        operations.run_promote(self.root, args)
        self.assertFalse(draft.exists())
        self.assertEqual(target.read_bytes(), before)
        self.assertEqual(operations.resolve_selector(self.root, "CA-R-344").lifecycle, "active")

    def test_promote_bulk_preflight_rejects_role_mismatch_without_mutation(self) -> None:
        second_draft = self._atom(self.drafts / "CA-R--REQUIREMENT-UNIT--another.md", "# Another")
        original = self.drafts / "CA-R--REQUIREMENT-UNIT--candidate.md"
        payload = {"atoms": [
            {"selector": original.name, "atom_id": "CA-R-344"},
            {"selector": second_draft.name, "atom_id": "CA-M-102"},
        ]}
        with self.assertRaises(operations.ToolError) as context:
            operations.run_promote(self.root, argparse.Namespace(input=self._input(payload), apply=True))
        self.assertEqual(context.exception.code, "atom-id-role-mismatch")
        self.assertTrue(original.exists())
        self.assertTrue(second_draft.exists())

    def test_upgrade_requires_explicit_higher_tier_and_bulk_applies(self) -> None:
        payload = {"atoms": [
            {"selector": "CA-R-343", "tier": "core"},
            {"selector": "CA-M-101", "tier": "core"},
        ]}
        args = argparse.Namespace(input=self._input(payload), apply=False)
        result = operations.run_upgrade(self.root, args)
        self.assertEqual(result["count"], 2)
        self.assertIn("tier: standard", self.first.read_text(encoding="utf-8"))
        args.apply = True
        operations.run_upgrade(self.root, args)
        self.assertIn("tier: core", self.first.read_text(encoding="utf-8"))
        self.assertIn("version: 2", self.second.read_text(encoding="utf-8"))
        invalid = {"atoms": [{"selector": "CA-R-343", "tier": "core"}]}
        with self.assertRaises(operations.ToolError) as context:
            operations.run_upgrade(self.root, argparse.Namespace(input=self._input(invalid), apply=False))
        self.assertEqual(context.exception.code, "target-tier-not-higher")

    def test_upgrade_to_upper_scope_moves_and_rewrites_scope_segment(self) -> None:
        before_id = operations.resolve_selector(self.root, "CA-R-343").atom_id
        payload = {"atoms": [{"selector": "CA-R-343", "tier": "standard", "to_scope": "CAPRMEDIO"}]}
        args = argparse.Namespace(input=self._input(payload), apply=False)
        result = operations.run_upgrade(self.root, args)
        target = self.root / ".caprmedio/04_requirement/CA-R-343-REQUIREMENT-CA--first.md"
        self.assertEqual(result["changes"][0]["to_scope"], "CAPRMEDIO")
        self.assertFalse(target.exists())
        args.apply = True
        operations.run_upgrade(self.root, args)
        self.assertFalse(self.first.exists())
        self.assertTrue(target.exists())
        self.assertEqual(operations.resolve_selector(self.root, "CA-R-343").atom_id, before_id)

    def test_upgrade_rejects_missing_explicit_tier(self) -> None:
        payload = {"atoms": [{"selector": "CA-R-343"}]}
        with self.assertRaises(operations.ToolError) as context:
            operations.run_upgrade(self.root, argparse.Namespace(input=self._input(payload), apply=False))
        self.assertEqual(context.exception.code, "target-tier-invalid")

    def test_draft_has_no_derived_atom_id_and_cannot_move_to_active(self) -> None:
        draft = operations.resolve_selector(self.root, "CA-R--REQUIREMENT-UNIT--candidate.md")
        self.assertIsNone(draft.atom_id)
        target = self.root / ".caprmedio/102_UNIT/04_requirement"
        args = argparse.Namespace(atom=[draft.filename], from_path=None, to=target.relative_to(self.root).as_posix(), flatten=False, apply=False)
        with self.assertRaises(operations.ToolError) as context:
            operations.run_move(self.root, args)
        self.assertEqual(context.exception.code, "atom-id-required")


if __name__ == "__main__":
    unittest.main()
