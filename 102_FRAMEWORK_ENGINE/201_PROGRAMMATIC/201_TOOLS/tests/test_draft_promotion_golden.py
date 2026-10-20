"""Native Draft operations need current carriers, not retained-history permission."""
from __future__ import annotations

import copy
from pathlib import Path
import sys
import unittest
from unittest.mock import patch

TOOLS = Path(__file__).resolve().parents[1]
sys.path[:0] = [str(TOOLS), str(TOOLS / "tests")]

import atom_operations
from atom_operations import atom_from_path, atom_identity_lock, frontmatter_scalar, remove_frontmatter_scalar, replace_frontmatter_scalar, scan_atoms
from lifecycle_intents import LifecycleError, carrier_descriptor, change_status_atom_action, create_atom_action, update_atom_action
import test_model_driven_status_lifecycle as fixture_module


class DraftPromotionGoldenTest(unittest.TestCase):
    def setUp(self) -> None:
        fixture_module.ModelDrivenStatusLifecycleTest.setUpClass()
        self.fixture = fixture_module.ModelDrivenStatusLifecycleTest("run")
        self.fixture.setUp()

    def tearDown(self) -> None:
        self.fixture.tearDown()

    def _fresh_draft(self, *, container: str | None = None) -> Path:
        return self.fixture.atom("Requirement", "Draft", draft=True, container=container)

    def _versioned_draft(self) -> Path:
        draft = self._fresh_draft(container="versioned")
        target = draft.with_name("CA-R-8000@4-draft--golden.md")
        draft.rename(target)
        text = target.read_text(encoding="utf-8")
        target.write_text(
            text.replace("---\ncontent_role", "---\natom_id: CA-R-8000@4-draft\ncontent_role")
            .replace("version: 3", "version: 4"),
            encoding="utf-8",
        )
        return target

    def _existing_marker_draft(self, current: Path, version: int) -> Path:
        current_atom = atom_from_path(self.fixture.root, current)
        marker = f"{current_atom.atom_id}@{version}-draft"
        draft = self.fixture.atom(
            frontmatter_scalar(current_atom.frontmatter, "content_role") or "Requirement",
            "Draft",
            draft=True,
            container=f"marker-{version}",
        )
        target = draft.with_name(f"{marker}--golden.md")
        draft.rename(target)
        source = current.read_text(encoding="utf-8")
        source = source.replace(f"atom_id: {current_atom.atom_id}", f"atom_id: {marker}", 1)
        source = source.replace(f"status: {frontmatter_scalar(current_atom.frontmatter, 'status')}", "status: Draft", 1)
        target.write_text(source.replace("version: 3", f"version: {version}", 1), encoding="utf-8")
        return target

    def _update(self, path: Path, *, status: str | None = None) -> dict[str, object]:
        atom = atom_from_path(self.fixture.root, path)
        frontmatter = atom.frontmatter if status is None else replace_frontmatter_scalar(atom.frontmatter, "status", status)
        return {"target": carrier_descriptor(self.fixture.root, atom),
                "proposed": {"frontmatter": frontmatter, "content": atom.content + "\n"},
                "change_class": "carrier_only"}

    def test_manual_draft_promotes_without_history_or_journal(self) -> None:
        draft = self._fresh_draft()
        before = atom_from_path(self.fixture.root, draft)
        result = self.fixture.execute(self.fixture.request(draft, "Active"))
        self.assertEqual("applied", result["outcome"])
        self.assertRegex(result["observed"]["atom_id"], r"^CA-R-[0-9]{3,}$")
        observed = atom_from_path(self.fixture.root, self.fixture.root / result["observed"]["path"])
        self.assertEqual(before.content, observed.content)
        self.assertEqual(4, result["observed"]["version"])
        self.assertFalse(draft.exists())
        self.assertFalse((self.fixture.root / ".caprmedio_caprmedio/archive/_draft_history").exists())
        self.assertFalse((self.fixture.root / ".caprmedio_caprmedio/_journal").exists())

    def test_demoted_draft_gets_fresh_identity_and_retains_actual_predecessor(self) -> None:
        source = self.fixture.atom("Requirement", "Active", number=8000)
        original = source.read_bytes()
        demoted = self.fixture.execute(self.fixture.request(source, "Draft"))
        draft = self.fixture.root / demoted["observed"]["path"]
        history = self.fixture.root / demoted["history"]["prior_revision"]["path"]
        self.assertEqual(original, history.read_bytes())
        self.assertIsNone(frontmatter_scalar(atom_from_path(self.fixture.root, draft).frontmatter, "revision_lineage"))
        promoted = self.fixture.execute(self.fixture.request(draft, "Active"))
        self.assertNotEqual("CA-R-8000", promoted["observed"]["atom_id"])
        self.assertEqual(5, promoted["observed"]["version"])
        self.assertEqual(original, history.read_bytes())

    def test_manual_draft_can_enter_archived_directly(self) -> None:
        draft = self._fresh_draft()
        result = self.fixture.execute(self.fixture.request(draft, "Archived"))
        self.assertEqual("applied", result["outcome"])
        self.assertEqual("Archived", result["observed"]["status"])
        self.assertEqual(4, result["observed"]["version"])
        self.assertTrue(result["observed"]["filename"].endswith("@4.md"))

    def test_all_history_filename_evidence_prevents_identity_reuse(self) -> None:
        from lifecycle_intents import _draft_promotion_identity
        draft = self._fresh_draft()
        reserved = _draft_promotion_identity(self.fixture.root, atom_from_path(self.fixture.root, draft))
        historical = draft.parent.parent / "archive" / f"{reserved}--unparseable.md"
        historical.parent.mkdir()
        historical.write_text("Not a parseable Atom, but a real retained ID filename.", encoding="utf-8")
        result = self.fixture.execute(self.fixture.request(draft, "Active"))
        self.assertNotEqual(reserved, result["observed"]["atom_id"])
        self.assertTrue(historical.exists())

    def test_optional_unresolvable_or_malformed_lineage_is_not_permission(self) -> None:
        for index, value in enumerate(('"not a map"', '{"history_entry_ref": {"bad": true}}', 'null')):
            with self.subTest(value=value):
                draft = self._fresh_draft(container=f"optional-{index}")
                text = draft.read_text(encoding="utf-8")
                draft.write_text(text.replace("version: 3", f"revision_lineage: {value}\nversion: 3"), encoding="utf-8")
                result = self.fixture.execute(self.fixture.request(draft, "Active"))
                self.assertEqual("applied", result["outcome"])

    def test_history_writer_unavailability_cannot_gate_create_or_promotion(self) -> None:
        lock = self.fixture.root / ".caprmedio_caprmedio/.draft_promotion_locks"
        lock.symlink_to(self.fixture.root, target_is_directory=True)
        carrier = self.fixture.create_carrier("Requirement", "Draft", number=9000)
        result = create_atom_action(self.fixture.root, {"carrier": carrier}, execute=True, authorized=True)
        draft = self.fixture.root / result["observed"]["path"]
        self.assertEqual("applied", self.fixture.execute(self.fixture.request(draft, "Active"))["outcome"])
        self.assertTrue(lock.is_symlink())

    def test_manual_draft_updates_without_history_and_stale_target_refuses(self) -> None:
        draft = self._fresh_draft()
        request = self._update(draft)
        result = update_atom_action(self.fixture.root, request, execute=True, authorized=True)
        self.assertEqual("applied", result["outcome"])
        self.assertIsNone(result["observed"]["atom_id"])
        self.assertEqual(4, result["observed"]["version"])
        before = self.fixture.snapshot()
        with self.assertRaises(LifecycleError):
            update_atom_action(self.fixture.root, request, execute=True, authorized=True)
        self.assertEqual(before, self.fixture.snapshot())

    def test_versioned_draft_update_advances_marker_and_filename_together(self) -> None:
        draft = self._versioned_draft()
        atom = atom_from_path(self.fixture.root, draft)
        no_op = {"target": carrier_descriptor(self.fixture.root, atom),
                 "proposed": {"frontmatter": atom.frontmatter, "content": atom.content},
                 "change_class": "carrier_only"}
        before = self.fixture.snapshot()
        self.assertEqual("no-op", update_atom_action(self.fixture.root, no_op, execute=True, authorized=True)["outcome"])
        self.assertEqual(before, self.fixture.snapshot())
        with patch("atom_operations._validate_complete_carrier"):
            result = update_atom_action(self.fixture.root, self._update(draft), execute=True, authorized=True)
        self.assertEqual("applied", result["outcome"])
        observed = self.fixture.root / result["observed"]["path"]
        self.assertFalse(draft.exists())
        self.assertTrue(observed.name.startswith("CA-R-8000@5-draft--"))
        updated = atom_from_path(self.fixture.root, observed)
        self.assertIsNone(updated.atom_id)
        self.assertEqual("CA-R-8000@5-draft", frontmatter_scalar(updated.frontmatter, "atom_id"))
        self.assertEqual(5, int(frontmatter_scalar(updated.frontmatter, "version")))

    def test_existing_marker_requires_sealed_canonical_target(self) -> None:
        current = self.fixture.atom("Requirement", "Active", number=8102)
        draft = self._existing_marker_draft(current, 4)
        before = self.fixture.snapshot()
        with self.assertRaises(LifecycleError) as error:
            self.fixture.execute(self.fixture.request(draft, "Active"))
        self.assertEqual("canonical-target-required", error.exception.code)
        self.assertEqual(before, self.fixture.snapshot())

    def test_existing_marker_done_to_active_requires_next_version(self) -> None:
        current = self.fixture.atom("Plan", "Done", number=8100)
        draft = self._existing_marker_draft(current, 3)
        before = self.fixture.snapshot()
        with self.assertRaises(LifecycleError) as error:
            change_status_atom_action(
                self.fixture.root,
                {"target": carrier_descriptor(self.fixture.root, atom_from_path(self.fixture.root, draft)),
                 "status": "Active",
                 "canonical_target": carrier_descriptor(self.fixture.root, atom_from_path(self.fixture.root, current)),
                 "proposed_version": 3},
                execute=True,
                authorized=True,
            )
        self.assertEqual("atom-version-invalid", error.exception.code)
        self.assertEqual(before, self.fixture.snapshot())

    def test_existing_marker_refuses_boolean_proposed_version(self) -> None:
        current = self.fixture.atom("Plan", "Active", number=8101)
        draft = self._existing_marker_draft(current, 4)
        before = self.fixture.snapshot()
        with self.assertRaises(LifecycleError) as error:
            change_status_atom_action(
                self.fixture.root,
                {"target": carrier_descriptor(self.fixture.root, atom_from_path(self.fixture.root, draft)),
                 "status": "Active",
                 "canonical_target": carrier_descriptor(self.fixture.root, atom_from_path(self.fixture.root, current)),
                 "proposed_version": True},
                execute=True,
                authorized=True,
            )
        self.assertEqual("draft-proposed-version-required", error.exception.code)
        self.assertEqual(before, self.fixture.snapshot())

    def test_existing_marker_publishes_next_canonical_revision(self) -> None:
        current = self.fixture.atom("Requirement", "Active", number=8103)
        predecessor = current.read_bytes()
        draft = self._existing_marker_draft(current, 4)
        draft.write_text(draft.read_text(encoding="utf-8") + "\nChanged detail.\n", encoding="utf-8")
        result = change_status_atom_action(
            self.fixture.root,
            {"target": carrier_descriptor(self.fixture.root, atom_from_path(self.fixture.root, draft)),
             "status": "Active",
             "canonical_target": carrier_descriptor(self.fixture.root, atom_from_path(self.fixture.root, current)),
             "proposed_version": 4},
            execute=True,
            authorized=True,
        )
        self.assertEqual("applied", result["outcome"])
        self.assertEqual("CA-R-8103", result["observed"]["atom_id"])
        self.assertEqual(4, result["observed"]["version"])
        self.assertFalse(draft.exists())
        self.assertEqual(predecessor, self.fixture.root.joinpath(result["history"]["prior_revision"]["path"]).read_bytes())

    def test_existing_marker_done_plan_returns_to_active_with_children(self) -> None:
        current = self.fixture.atom("Plan", "Done", number=8106)
        children = current.with_suffix("")
        child = children / "child.md"
        child.parent.mkdir(parents=True)
        child.write_text("unchanged child\n", encoding="utf-8")
        predecessor = current.read_bytes()
        draft = self._existing_marker_draft(current, 4)
        draft.write_text(draft.read_text(encoding="utf-8") + "\nChanged detail.\n", encoding="utf-8")
        result = change_status_atom_action(
            self.fixture.root,
            {"target": carrier_descriptor(self.fixture.root, atom_from_path(self.fixture.root, draft)),
             "status": "Active",
             "canonical_target": carrier_descriptor(self.fixture.root, atom_from_path(self.fixture.root, current)),
             "proposed_version": 4},
            execute=True,
            authorized=True,
        )
        active = current.parent.parent / current.name
        self.assertEqual("applied", result["outcome"])
        self.assertEqual(active.relative_to(self.fixture.root).as_posix(), result["observed"]["path"])
        self.assertFalse(current.exists())
        self.assertFalse(children.exists())
        self.assertEqual("unchanged child\n", (active.with_suffix("") / "child.md").read_text(encoding="utf-8"))
        self.assertEqual(predecessor, self.fixture.root.joinpath(result["history"]["prior_revision"]["path"]).read_bytes())

    def test_existing_marker_equivalent_current_is_a_byte_exact_noop(self) -> None:
        current = self.fixture.atom("Requirement", "Active", number=8104)
        draft = self._existing_marker_draft(current, 3)
        before = self.fixture.snapshot()
        result = change_status_atom_action(
            self.fixture.root,
            {"target": carrier_descriptor(self.fixture.root, atom_from_path(self.fixture.root, draft)),
             "status": "Active",
             "canonical_target": carrier_descriptor(self.fixture.root, atom_from_path(self.fixture.root, current)),
             "proposed_version": 3},
            execute=True,
            authorized=True,
        )
        self.assertEqual("no-op", result["outcome"])
        self.assertEqual("CA-R-8104", result["observed"]["atom_id"])
        self.assertEqual(before, self.fixture.snapshot())

    def test_existing_marker_moved_cleanup_failure_restores_every_carrier(self) -> None:
        current = self.fixture.atom("Plan", "Done", number=8105)
        children = current.with_suffix("")
        children.mkdir()
        (children / "child.md").write_text("unchanged child\n", encoding="utf-8")
        draft = self._existing_marker_draft(current, 4)
        draft.write_text(draft.read_text(encoding="utf-8") + "\nChanged detail.\n", encoding="utf-8")
        before = {path: value for path, value in self.fixture.snapshot().items()
                  if value is not None and not path.startswith((".caprmedio_runtime/", ".caprmedio_tmp/"))}
        real_write = atom_operations.write_raw_atom_revision
        injected = False

        def fail_draft_cleanup(root, path, raw, *, expected, mode):
            nonlocal injected
            if not injected and path == draft and raw is None:
                injected = True
                raise atom_operations.ToolError("draft-cleanup-failed", "injected cleanup failure")
            return real_write(root, path, raw, expected=expected, mode=mode)

        with patch.object(atom_operations, "write_raw_atom_revision", side_effect=fail_draft_cleanup):
            with self.assertRaises(LifecycleError) as error:
                change_status_atom_action(
                    self.fixture.root,
                    {"target": carrier_descriptor(self.fixture.root, atom_from_path(self.fixture.root, draft)),
                     "status": "Active",
                     "canonical_target": carrier_descriptor(self.fixture.root, atom_from_path(self.fixture.root, current)),
                     "proposed_version": 4},
                    execute=True,
                    authorized=True,
                )
        self.assertTrue(injected)
        self.assertEqual("draft-cleanup-failed", error.exception.code)
        self.assertEqual(before, {path: value for path, value in self.fixture.snapshot().items()
                                  if value is not None and not path.startswith((".caprmedio_runtime/", ".caprmedio_tmp/"))})

    def test_existing_marker_same_path_cleanup_failure_restores_every_carrier(self) -> None:
        current = self.fixture.atom("Requirement", "Active", number=8107)
        draft = self._existing_marker_draft(current, 4)
        draft.write_text(draft.read_text(encoding="utf-8") + "\nChanged detail.\n", encoding="utf-8")
        before = {path: value for path, value in self.fixture.snapshot().items()
                  if value is not None and not path.startswith((".caprmedio_runtime/", ".caprmedio_tmp/"))}
        real_write = atom_operations.write_raw_atom_revision
        injected = False

        def fail_draft_cleanup(root, path, raw, *, expected, mode):
            nonlocal injected
            if not injected and path == draft and raw is None:
                injected = True
                raise atom_operations.ToolError("draft-cleanup-failed", "injected cleanup failure")
            return real_write(root, path, raw, expected=expected, mode=mode)

        with patch.object(atom_operations, "write_raw_atom_revision", side_effect=fail_draft_cleanup):
            with self.assertRaises(LifecycleError) as error:
                change_status_atom_action(
                    self.fixture.root,
                    {"target": carrier_descriptor(self.fixture.root, atom_from_path(self.fixture.root, draft)),
                     "status": "Active",
                     "canonical_target": carrier_descriptor(self.fixture.root, atom_from_path(self.fixture.root, current)),
                     "proposed_version": 4},
                    execute=True,
                    authorized=True,
                )
        self.assertTrue(injected)
        self.assertEqual("draft-cleanup-failed", error.exception.code)
        self.assertEqual(before, {path: value for path, value in self.fixture.snapshot().items()
                                  if value is not None and not path.startswith((".caprmedio_runtime/", ".caprmedio_tmp/"))})

    def test_same_path_external_edit_during_cleanup_is_left_for_recovery(self) -> None:
        current = self.fixture.atom("Requirement", "Active", number=8108)
        draft = self._existing_marker_draft(current, 4)
        draft.write_text(draft.read_text(encoding="utf-8") + "\nChanged detail.\n", encoding="utf-8")
        draft_before = draft.read_bytes()
        external = b"\nExternal canonical edit.\n"
        real_write = atom_operations.write_raw_atom_revision
        injected = False

        def edit_canonical_then_fail(root, path, raw, *, expected, mode):
            nonlocal injected
            if not injected and path == draft and raw is None:
                injected = True
                current.write_bytes(current.read_bytes() + external)
                raise atom_operations.ToolError("draft-cleanup-failed", "injected cleanup failure")
            return real_write(root, path, raw, expected=expected, mode=mode)

        with patch.object(atom_operations, "write_raw_atom_revision", side_effect=edit_canonical_then_fail):
            with self.assertRaises(LifecycleError) as error:
                change_status_atom_action(
                    self.fixture.root,
                    {"target": carrier_descriptor(self.fixture.root, atom_from_path(self.fixture.root, draft)),
                     "status": "Active",
                     "canonical_target": carrier_descriptor(self.fixture.root, atom_from_path(self.fixture.root, current)),
                     "proposed_version": 4},
                    execute=True,
                    authorized=True,
                )
        history = current.parent / "archived" / f"{current.stem}@3.md"
        self.assertTrue(injected)
        self.assertEqual("status-recovery-uncertain", error.exception.code)
        self.assertEqual(draft_before, draft.read_bytes())
        self.assertIn(external, current.read_bytes())
        self.assertTrue(history.exists())

    def test_versioned_draft_update_refuses_destination_collision_without_effect(self) -> None:
        draft = self._versioned_draft()
        collision = draft.with_name("CA-R-8000@5-draft--golden.md")
        collision.write_text(
            draft.read_text(encoding="utf-8").replace("CA-R-8000@4-draft", "CA-R-8000@5-draft")
            .replace("version: 4", "version: 5"),
            encoding="utf-8",
        )
        before = self.fixture.snapshot()
        with patch("atom_operations._validate_complete_carrier"):
            with self.assertRaises(LifecycleError) as error:
                update_atom_action(self.fixture.root, self._update(draft), execute=True, authorized=True)
        self.assertEqual("destination-collision", error.exception.code)
        self.assertEqual(before, self.fixture.snapshot())

    def test_status_update_keeps_complete_admitted_delta(self) -> None:
        source = self.fixture.atom("Requirement", "Active", number=8000)
        before = source.read_bytes()
        request = self._update(source, status="Archived")
        result = update_atom_action(self.fixture.root, request, execute=True, authorized=True)
        self.assertEqual("applied", result["outcome"])
        destination = self.fixture.root / result["observed"]["path"]
        self.assertEqual(request["proposed"]["content"], atom_from_path(self.fixture.root, destination).content)
        self.assertEqual(4, result["observed"]["version"])
        self.assertTrue(destination.name.endswith("@4.md"))
        self.assertEqual(before, (self.fixture.root / result["history"]["prior_revision"]["path"]).read_bytes())

    def test_complete_status_update_crosses_draft_identity_boundary_both_ways(self) -> None:
        source = self.fixture.atom("Requirement", "Active", number=8000)
        before = source.read_bytes()
        request = self._update(source, status="Draft")
        request["proposed"]["frontmatter"] = remove_frontmatter_scalar(request["proposed"]["frontmatter"], "atom_id")
        demoted = update_atom_action(self.fixture.root, request, execute=True, authorized=True)
        self.assertEqual("applied", demoted["outcome"])
        self.assertIsNone(demoted["observed"]["atom_id"])
        draft = self.fixture.root / demoted["observed"]["path"]
        self.assertEqual(request["proposed"]["content"], atom_from_path(self.fixture.root, draft).content)
        self.assertEqual(before, (self.fixture.root / demoted["history"]["prior_revision"]["path"]).read_bytes())
        promoted_request = self._update(draft, status="Active")
        promoted = update_atom_action(self.fixture.root, promoted_request, execute=True, authorized=True)
        self.assertEqual("applied", promoted["outcome"])
        self.assertNotEqual("CA-R-8000", promoted["observed"]["atom_id"])
        self.assertEqual(5, promoted["observed"]["version"])
        destination = self.fixture.root / promoted["observed"]["path"]
        self.assertEqual(promoted_request["proposed"]["content"], atom_from_path(self.fixture.root, destination).content)
        observed = atom_from_path(self.fixture.root, destination)
        no_op = {"target": carrier_descriptor(self.fixture.root, observed),
                 "proposed": {"frontmatter": observed.frontmatter, "content": observed.content},
                 "change_class": "carrier_only"}
        snapshot = self.fixture.snapshot()
        self.assertEqual("no-op", update_atom_action(self.fixture.root, no_op, execute=True, authorized=True)["outcome"])
        self.assertEqual(snapshot, self.fixture.snapshot())

    def test_missing_old_draft_retry_is_truthful_and_does_not_replay(self) -> None:
        draft = self._fresh_draft()
        request = self.fixture.request(draft, "Active")
        first = self.fixture.execute(copy.deepcopy(request))
        before = self.fixture.snapshot()
        with self.assertRaises(LifecycleError):
            self.fixture.execute(copy.deepcopy(request))
        self.assertEqual(before, self.fixture.snapshot())
        self.assertEqual(1, sum(atom.atom_id == first["observed"]["atom_id"] for atom in scan_atoms(self.fixture.root)))

    def test_preview_permission_collision_and_unknown_fields_keep_zero_effect(self) -> None:
        draft = self._fresh_draft()
        request = self.fixture.request(draft, "Active")
        before = self.fixture.snapshot()
        self.assertEqual("preview", change_status_atom_action(self.fixture.root, request)["outcome"])
        with self.assertRaises(LifecycleError):
            self.fixture.execute({**request, "draft_identity_evidence": {}})
        with self.assertRaises(LifecycleError):
            change_status_atom_action(self.fixture.root, request, execute=True, authorized=False)
        self.assertEqual(before, self.fixture.snapshot())
        self.fixture.atom("Requirement", "Active", number=8000)
        # Lock creation is runtime coordination, not an Atom effect. Establish
        # it only after proving preview and unauthorized requests are effect-free.
        with atom_identity_lock(self.fixture.root):
            pass
        before = self.fixture.snapshot()
        with patch("lifecycle_intents._draft_promotion_identity", return_value="CA-R-8000"):
            with self.assertRaises(LifecycleError):
                self.fixture.execute(request)
        self.assertEqual(before, self.fixture.snapshot())


if __name__ == "__main__":
    unittest.main()
