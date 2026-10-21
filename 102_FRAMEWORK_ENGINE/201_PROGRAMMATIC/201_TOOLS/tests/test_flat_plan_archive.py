"""Synthetic functional checks for flat Archived Plan publication."""

from __future__ import annotations

from pathlib import Path
import sys
import unittest
from unittest.mock import patch

TOOLS = Path(__file__).resolve().parents[1]
TESTS = TOOLS / "tests"
sys.path.insert(0, str(TOOLS))
sys.path.insert(0, str(TESTS))

import atom_operations  # noqa: E402
from atom_operations import atom_from_path, frontmatter_scalar  # noqa: E402
from lifecycle_intents import (  # noqa: E402
    LifecycleError,
    carrier_descriptor,
    change_status_atom_action,
)
from current_atom_locator import CurrentAtomLocator, CurrentAtomLocatorError  # noqa: E402


class FlatPlanArchiveTests(unittest.TestCase):
    """Exercise only the public one-Atom status publication boundary."""

    def setUp(self) -> None:
        from test_selected_atom_lifecycle import SelectedAtomLifecycleTest

        self.fixture = SelectedAtomLifecycleTest(methodName="runTest")
        self.fixture.setUp()
        self.addCleanup(self.fixture.tearDown)
        self.fixture._copy_frozen_atom("CA-R-1539")
        self.root = self.fixture.root
        self.requirements = self.fixture.requirements
        structure = self.root / ".caprmedio_caprmedio/project_structure.toml"
        fixture_authority = ".caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/LIFECYCLE_FIXTURE"
        structure_text = structure.read_text(encoding="utf-8")
        for authority in (
            ".caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE",
            ".caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC",
            ".caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS",
            fixture_authority,
        ):
            structure_text = structure_text.replace(
                f'authority_path = "{authority}"\n'
                f'delivery_path = "{authority}"',
                f'authority_path = "{authority}"\n'
                'delivery_path = "fixture-delivery/registered"',
            )
        structure.write_text(structure_text, encoding="utf-8")
        self.plan_root = self.requirements.parent / "03_plan"
        self.plan_root.mkdir(parents=True, exist_ok=True)

    def _plan(
        self,
        atom_id: str | None,
        slug: str,
        *,
        parent: Path | None = None,
        status: str = "Active",
        version: int = 3,
        relations: str = "relations: {}\n",
        folder: str | None = None,
        filename_id: str | None = None,
    ) -> Path:
        directory = self.plan_root if parent is None else parent.with_suffix("")
        if folder is not None:
            directory = self.plan_root / folder
        directory.mkdir(parents=True, exist_ok=True)
        path = directory / f"{filename_id or atom_id or 'CA-P'}--{slug}.md"
        identity = f"atom_id: {atom_id}\n" if atom_id is not None else ""
        path.write_text(
            "---\n"
            f"{identity}content_role: Plan\ntype: Plan\nlabel: Task\n"
            "current_scope_unit: LIFECYCLE_FIXTURE\nclaim_target_scope_unit: LIFECYCLE_FIXTURE\n"
            "local_tier: Standard\nglobal_tier: 14\nwork_sequence_number: 1\n"
            "author: Anatoly Maslennikov\n"
            f"status: {status}\nversion: {version}\n"
            'updated_at: "2026-01-01 00:00:00 +0000"\n'
            "subjects:\n  governs: Atom/Test\n  depends_on: []\n"
            f"{relations}"
            "---\n"
            f"# Summary\n\n{slug} summary\n\n"
            "## Objective\n\nPreserve the selected Plan carrier.\n\n"
            "## Details\n\nArchive only this explicitly selected Plan.\n\n"
            "### Definition of Done\n\nThe exact predecessor remains readable.\n",
            encoding="utf-8",
        )
        return path

    def _draft_plan(self, slug: str, *, marker: str | None = None, version: int = 3) -> Path:
        return self._plan(
            marker,
            slug,
            status="Draft",
            version=version,
            folder="draft",
            filename_id=marker or "CA-P",
        )

    def _marker_draft(self, current: Path, *, version: int, parent: Path | None = None) -> Path:
        current_atom = atom_from_path(self.root, current)
        marker = f"{current_atom.atom_id}@{version}-draft"
        directory = current.parent / "draft" if parent is None else parent
        suffix = current.name.split("--", 1)[1] if "--" in current.name else current.stem
        draft = directory / f"{marker}--{suffix}"
        source = current.read_text(encoding="utf-8")
        source = source.replace(f"atom_id: {current_atom.atom_id}", f"atom_id: {marker}", 1)
        source = source.replace(
            f"status: {frontmatter_scalar(current_atom.frontmatter, 'status')}",
            "status: Draft",
            1,
        )
        source = source.replace(
            f"version: {frontmatter_scalar(current_atom.frontmatter, 'version')}",
            f"version: {version}",
            1,
        )
        draft.parent.mkdir(parents=True, exist_ok=True)
        draft.write_text(source, encoding="utf-8")
        return draft

    def _archive(self, path: Path, **extra: object) -> dict[str, object]:
        request = {
            "target": carrier_descriptor(self.root, atom_from_path(self.root, path)),
            "status": "Archived",
            **extra,
        }
        return change_status_atom_action(
            self.root,
            request,
            execute=True,
            authorized=True,
        )

    def _files(self) -> dict[str, bytes]:
        control = self.root / ".caprmedio_caprmedio"
        return {
            path.relative_to(self.root).as_posix(): path.read_bytes()
            for path in control.rglob("*")
            if path.is_file()
        }

    def test_root_plan_archives_flat_with_exact_predecessor_and_relations(self) -> None:
        plan = self._plan(
            "CA-P-701",
            "root",
            relations="relations:\n  depends_on: [CA-R-100]\n",
        )
        predecessor = plan.read_bytes()

        result = self._archive(plan)

        destination = self.plan_root / "archived" / "CA-P-701--root@4.md"
        history = self.plan_root / "archived" / "CA-P-701--root@3.md"
        self.assertEqual("applied", result["outcome"])
        self.assertEqual(destination.relative_to(self.root).as_posix(), result["observed"]["path"])
        self.assertEqual("Archived", result["observed"]["status"])
        self.assertEqual(4, result["observed"]["version"])
        self.assertEqual(predecessor, history.read_bytes())
        self.assertIn(b"depends_on: [CA-R-100]", destination.read_bytes())
        self.assertFalse(plan.exists())
        self.assertFalse((self.plan_root / "archived" / "CA-P-701--root").is_dir())

    def test_existing_marker_draft_archives_same_canonical_identity_and_predecessor(self) -> None:
        current = self._plan("CA-P-710", "existing", version=3)
        predecessor = current.read_bytes()
        draft = self._draft_plan("existing", marker="CA-P-710@4-draft", version=4)
        draft.write_text(draft.read_text(encoding="utf-8") + "\nChanged plan detail.\n", encoding="utf-8")

        result = self._archive(
            draft,
            canonical_target=carrier_descriptor(self.root, atom_from_path(self.root, current)),
            proposed_version=4,
        )

        destination = self.plan_root / "archived" / "CA-P-710--existing@4.md"
        history = self.plan_root / "archived" / "CA-P-710--existing@3.md"
        self.assertEqual("applied", result["outcome"])
        self.assertEqual(destination.relative_to(self.root).as_posix(), result["observed"]["path"])
        self.assertEqual("CA-P-710", result["observed"]["atom_id"])
        self.assertEqual(4, result["observed"]["version"])
        self.assertEqual(history.relative_to(self.root).as_posix(), result["history"]["prior_revision"]["path"])
        self.assertEqual(predecessor, history.read_bytes())
        self.assertFalse(current.exists())
        self.assertFalse(draft.exists())
        self.assertEqual(
            {destination, history},
            {path for path in self.plan_root.rglob("*CA-P-710*.md")},
        )
        with self.assertRaises(CurrentAtomLocatorError):
            CurrentAtomLocator(self.root).assert_unique_current_claim(
                "CA-P-710", destination.relative_to(self.root)
            )

    def test_existing_marker_draft_uses_admitted_nonarchive_plan_status(self) -> None:
        current = self._plan("CA-P-713", "marker-done", version=3)
        predecessor = current.read_bytes()
        draft = self._draft_plan("marker-done", marker="CA-P-713@4-draft", version=4)
        draft.write_text(draft.read_text(encoding="utf-8") + "\nCompleted plan detail.\n", encoding="utf-8")
        result = change_status_atom_action(
            self.root,
            {
                "target": carrier_descriptor(self.root, atom_from_path(self.root, draft)),
                "status": "Done",
                "canonical_target": carrier_descriptor(self.root, atom_from_path(self.root, current)),
                "proposed_version": 4,
            },
            execute=True,
            authorized=True,
        )

        destination = self.plan_root / "done" / "CA-P-713--marker-done.md"
        history = self.plan_root / "archived" / "CA-P-713--marker-done@3.md"
        self.assertEqual("applied", result["outcome"])
        self.assertEqual(destination.relative_to(self.root).as_posix(), result["observed"]["path"])
        self.assertEqual("CA-P-713", result["observed"]["atom_id"])
        self.assertEqual("Done", result["observed"]["status"])
        self.assertEqual(4, result["observed"]["version"])
        self.assertEqual(predecessor, history.read_bytes())
        self.assertFalse(current.exists())
        self.assertFalse(draft.exists())

    def test_existing_marker_requirement_promotes_with_exact_archived_predecessor(self) -> None:
        current = self.fixture.target
        predecessor = current.read_bytes()
        draft = self._marker_draft(current, version=2)
        draft.write_text(draft.read_text(encoding="utf-8") + "\nRequirement detail.\n", encoding="utf-8")
        result = change_status_atom_action(
            self.root,
            {
                "target": carrier_descriptor(self.root, atom_from_path(self.root, draft)),
                "status": "Active",
                "canonical_target": carrier_descriptor(self.root, atom_from_path(self.root, current)),
                "proposed_version": 2,
            },
            execute=True,
            authorized=True,
        )

        history = current.parent / "archived" / "CA-R-100--target@1.md"
        orphan = current.parent / "archive" / "CA-R-100--target@1.md"
        self.assertEqual("applied", result["outcome"])
        self.assertEqual(current.relative_to(self.root).as_posix(), result["observed"]["path"])
        self.assertEqual("CA-R-100", result["observed"]["atom_id"])
        self.assertEqual(2, result["observed"]["version"])
        self.assertEqual(history.relative_to(self.root).as_posix(), result["history"]["prior_revision"]["path"])
        self.assertEqual(predecessor, history.read_bytes())
        self.assertFalse(orphan.exists())
        self.assertFalse(draft.exists())

    def test_nested_plan_marker_done_keeps_predecessor_in_flat_plan_history(self) -> None:
        for authority in (
            "CA-D-434", "CA-D-467", "CA-D-460", "CA-D-481",
            "CA-R-1608", "CA-R-1875", "CA-R-1397", "CA-R-1398",
            "CA-R-1399", "CA-R-1874", "CA-R-1309",
        ):
            self.fixture._copy_frozen_atom(authority)
        parent = self._plan("CA-P-714", "nested-parent")
        leaf = self._plan(
            "CA-P-715",
            "nested",
            parent=parent,
            relations="relations:\n  is_decomposition_of: [CA-P-714]\n",
        )
        predecessor = leaf.read_bytes()
        draft = self._marker_draft(leaf, version=4, parent=leaf.parent / "draft")
        draft.write_text(draft.read_text(encoding="utf-8") + "\nNested completion detail.\n", encoding="utf-8")
        result = change_status_atom_action(
            self.root,
            {
                "target": carrier_descriptor(self.root, atom_from_path(self.root, draft)),
                "status": "Done",
                "canonical_target": carrier_descriptor(self.root, atom_from_path(self.root, leaf)),
                "proposed_version": 4,
            },
            execute=True,
            authorized=True,
        )

        destination = leaf.parent / "done" / "CA-P-715--nested.md"
        history = self.plan_root / "archived" / "CA-P-715--nested@3.md"
        self.assertEqual("applied", result["outcome"])
        self.assertEqual(destination.relative_to(self.root).as_posix(), result["observed"]["path"])
        self.assertEqual("Done", result["observed"]["status"])
        self.assertEqual(4, result["observed"]["version"])
        self.assertEqual(predecessor, history.read_bytes())
        self.assertTrue(destination.exists())
        self.assertFalse(leaf.exists())
        self.assertFalse(draft.exists())

    def test_requirement_marker_cleanup_failure_restores_full_file_frontier(self) -> None:
        current = self.fixture.target
        draft = self._marker_draft(current, version=2)
        draft.write_text(draft.read_text(encoding="utf-8") + "\nCleanup failure detail.\n", encoding="utf-8")
        before = self._files()
        real_write = atom_operations.write_raw_atom_revision
        injected = False

        def fail_draft_cleanup(root, path, raw, *, expected, mode):
            nonlocal injected
            if not injected and path == draft and raw is None:
                injected = True
                raise atom_operations.ToolError("draft-cleanup-failed", "injected cleanup failure")
            return real_write(root, path, raw, expected=expected, mode=mode)

        with patch.object(atom_operations, "write_raw_atom_revision", side_effect=fail_draft_cleanup):
            with self.assertRaises(LifecycleError):
                change_status_atom_action(
                    self.root,
                    {
                        "target": carrier_descriptor(self.root, atom_from_path(self.root, draft)),
                        "status": "Active",
                        "canonical_target": carrier_descriptor(self.root, atom_from_path(self.root, current)),
                        "proposed_version": 2,
                    },
                    execute=True,
                    authorized=True,
                )

        self.assertTrue(injected)
        self.assertEqual(before, self._files())
        self.assertTrue(current.exists())
        self.assertTrue(draft.exists())

    def test_id_free_draft_archives_with_fresh_canonical_filename(self) -> None:
        draft = self._draft_plan("fresh")
        result = self._archive(draft)

        allocated_id = result["observed"]["atom_id"]
        destination = self.root / result["observed"]["path"]
        self.assertRegex(allocated_id, r"^CA-P-[0-9]{3,}$")
        self.assertEqual("applied", result["outcome"])
        self.assertEqual("Archived", result["observed"]["status"])
        self.assertEqual(4, result["observed"]["version"])
        self.assertEqual(f"{allocated_id}--fresh@4.md", destination.name)
        self.assertNotEqual("CA-P--fresh@4.md", destination.name)
        self.assertFalse(draft.exists())
        self.assertTrue(destination.is_file())
        self.assertEqual([], list(self.plan_root.rglob("CA-P--fresh@4.md")))
        with self.assertRaises(CurrentAtomLocatorError):
            CurrentAtomLocator(self.root).assert_unique_current_claim(
                allocated_id, destination.relative_to(self.root)
            )

    def test_nested_leaf_archives_flat_without_parent_cascade(self) -> None:
        parent = self._plan("CA-P-702", "parent")
        leaf = self._plan(
            "CA-P-703",
            "leaf",
            parent=parent,
            relations="relations:\n  is_decomposition_of: [CA-P-702]\n  depends_on: [CA-R-100]\n",
        )
        parent_before = parent.read_bytes()
        leaf_before = leaf.read_bytes()

        result = self._archive(leaf)

        destination = self.plan_root / "archived" / "CA-P-703--leaf@4.md"
        history = self.plan_root / "archived" / "CA-P-703--leaf@3.md"
        self.assertEqual(destination.relative_to(self.root).as_posix(), result["observed"]["path"])
        self.assertEqual(leaf_before, history.read_bytes())
        self.assertIn(b"is_decomposition_of: [CA-P-702]", destination.read_bytes())
        self.assertIn(b"depends_on: [CA-R-100]", destination.read_bytes())
        self.assertEqual(parent_before, parent.read_bytes())
        self.assertFalse(leaf.exists())

    def test_current_parent_with_current_descendant_refuses_before_effect(self) -> None:
        parent = self._plan("CA-P-711", "guard-parent")
        child = self._plan(
            "CA-P-712",
            "guard-child",
            parent=parent,
            relations="relations:\n  is_decomposition_of: [CA-P-711]\n",
        )
        before = self._files()

        with self.assertRaises(LifecycleError):
            self._archive(parent)

        self.assertEqual(before, self._files())
        self.assertTrue(parent.exists())
        self.assertTrue(child.exists())

    def test_archived_plan_revision_and_predecessor_are_not_current(self) -> None:
        plan = self._plan("CA-P-709", "withdrawn")
        predecessor = plan.read_bytes()
        locator = CurrentAtomLocator(self.root)
        locator.assert_unique_current_claim("CA-P-709", plan.relative_to(self.root))

        result = self._archive(plan)

        destination = self.plan_root / "archived" / "CA-P-709--withdrawn@4.md"
        history = self.plan_root / "archived" / "CA-P-709--withdrawn@3.md"
        self.assertEqual(destination.relative_to(self.root).as_posix(), result["observed"]["path"])
        self.assertEqual(predecessor, history.read_bytes())
        self.assertIn(b"status: Active", history.read_bytes())
        self.assertIn(b"status: Archived", destination.read_bytes())
        with self.assertRaises(CurrentAtomLocatorError):
            locator.assert_unique_current_claim("CA-P-709", destination.relative_to(self.root))

    def test_empty_and_asset_only_matching_plan_directories_follow_flat_destination(self) -> None:
        for number, asset in ((704, None), (705, b"asset bytes")):
            with self.subTest(asset=asset is not None):
                plan = self._plan(f"CA-P-{number}", "bundle")
                bundle = plan.with_suffix("")
                bundle.mkdir()
                if asset is not None:
                    (bundle / "asset.bin").write_bytes(asset)

                result = self._archive(plan)

                destination = self.plan_root / "archived" / f"CA-P-{number}--bundle@4.md"
                destination_bundle = destination.with_suffix("")
                self.assertEqual(destination.relative_to(self.root).as_posix(), result["observed"]["path"])
                self.assertTrue(destination_bundle.is_dir())
                if asset is not None:
                    self.assertEqual(asset, (destination_bundle / "asset.bin").read_bytes())
                self.assertFalse(bundle.exists())

    def test_flat_destination_collision_preserves_everything(self) -> None:
        plan = self._plan("CA-P-706", "collision")
        destination = self.plan_root / "archived" / "CA-P-706--collision@4.md"
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_bytes(b"do not overwrite")
        before = self._files()

        with self.assertRaisesRegex(LifecycleError, "destination-collision"):
            self._archive(plan)

        self.assertEqual(before, self._files())

    def test_non_plan_archive_stays_role_local_and_plan_done_stays_nonflat(self) -> None:
        requirement = self.fixture.target
        requirement_before = requirement.read_bytes()
        requirement_result = self._archive(requirement)
        self.assertIn("04_requirement/archived/", requirement_result["observed"]["path"])
        self.assertNotIn("03_plan/archived/", requirement_result["observed"]["path"])
        self.assertEqual(requirement_before, (self.root / requirement_result["history"]["prior_revision"]["path"]).read_bytes())

        plan = self._plan("CA-P-707", "done")
        done = change_status_atom_action(
            self.root,
            {"target": carrier_descriptor(self.root, atom_from_path(self.root, plan)), "status": "Done"},
            execute=True,
            authorized=True,
        )
        self.assertIn("03_plan/done/", done["observed"]["path"])
        self.assertNotIn("03_plan/archived/", done["observed"]["path"])

    def test_legacy_archive_bytes_are_preserved_without_assuming_relocation(self) -> None:
        plan = self._plan("CA-P-708", "legacy")
        bundle = plan.with_suffix("")
        legacy = bundle / "archive" / "legacy.bin"
        legacy.parent.mkdir(parents=True)
        legacy.write_bytes(b"legacy bytes must remain exact")
        retained = bundle / "archive" / "CA-P-708--legacy@2.md"
        retained.write_text(
            "---\n"
            "atom_id: CA-P-708\ncontent_role: Plan\ntype: Plan\nstatus: Active\nversion: 2\n"
            'updated_at: "2025-12-01 00:00:00 +0000"\n'
            "---\n# Summary\n\nRetained Plan history.\n",
            encoding="utf-8",
        )
        retained_before = retained.read_bytes()
        legacy_before = legacy.read_bytes()

        self._archive(plan)

        retained_candidates = [
            path for path in (self.root / ".caprmedio_caprmedio").rglob(retained.name)
            if "archive" in path.parts
        ]
        legacy_candidates = [
            path for path in (self.root / ".caprmedio_caprmedio").rglob("legacy.bin")
            if "archive" in path.parts
        ]
        self.assertTrue(retained_candidates)
        for candidate in retained_candidates:
            self.assertEqual(retained_before, candidate.read_bytes())
            observed = atom_from_path(self.root, candidate)
            self.assertEqual("CA-P-708", observed.atom_id)
            self.assertEqual("Plan", frontmatter_scalar(observed.frontmatter, "content_role"))
            self.assertEqual("Active", frontmatter_scalar(observed.frontmatter, "status"))
            self.assertEqual("2", frontmatter_scalar(observed.frontmatter, "version"))
        self.assertTrue(legacy_candidates)
        self.assertTrue(all(path.read_bytes() == legacy_before for path in legacy_candidates))


if __name__ == "__main__":
    unittest.main()
