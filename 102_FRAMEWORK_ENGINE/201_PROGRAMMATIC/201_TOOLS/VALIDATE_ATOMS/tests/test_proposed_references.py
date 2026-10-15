"""Synthetic contracts for the bounded proposed-reference inventory."""

from __future__ import annotations

import hashlib
import sys
import tempfile
import unittest
import warnings
from pathlib import Path
from unittest.mock import patch


VALIDATE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(VALIDATE))

from validate_atoms_workers.proposed_references import (  # noqa: E402
    ProposedReferenceError,
    inventory_proposed_references as _inventory_proposed_references,
)
from validate_atoms_workers.read_io import ReadContext  # noqa: E402
from validate_atoms_workers.settings import CEILINGS  # noqa: E402


ROLE_FOLDERS = {"Operations": "09_operations", "Plan": "03_plan"}
PLAN_STATUS_FOLDERS = {"Backlog": "001_backlog", "Done": "done", "Canceled": "canceled", "Archived": "archived"}
STATUS_FOLDERS = {
    "Operations": {"Active": "", "active": "", "Draft": "draft", "Deprecated": "deprecated", "Archived": "archived"},
    "Plan": {"Active": "", **PLAN_STATUS_FOLDERS},
}


def inventory_proposed_references(root, structure, targets, **kwargs):
    return _inventory_proposed_references(
        root, structure, targets, admitted_role_folders=ROLE_FOLDERS,
        admitted_status_folders=STATUS_FOLDERS, **kwargs,
    )


class ProposedReferenceInventoryTest(unittest.TestCase):
    def setUp(self) -> None:
        parent = Path(__file__).resolve().parents[5] / ".caprmedio_tmp"
        parent.mkdir(exist_ok=True)
        self.root = Path(tempfile.mkdtemp(prefix="proposed-references-", dir=parent))
        (self.root / "authority").mkdir(parents=True)
        self.structure = {"scope_units": [{"scope_unit_name": "TEST", "authority_path": "authority"}]}

    def tearDown(self) -> None:
        try:
            for path in sorted(self.root.rglob("*"), key=lambda item: len(item.parts), reverse=True):
                if path.is_file() or path.is_symlink():
                    path.unlink()
                else:
                    path.rmdir()
            self.root.rmdir()
        except PermissionError:
            warnings.warn(f"Host denied temporary fixture cleanup; retained {self.root}", RuntimeWarning)

    def _carrier(
        self, relative: str, atom_id: str, *, status: str = "Active", version: int = 1,
        role: str = "Operations", parent: str | None = None,
        kind: str = "Action", owner: str = "TEST",
    ) -> Path:
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        relation = "[]" if parent is None else f"[{parent}]"
        path.write_text(
            "---\n"
            f"atom_id: {atom_id}\ncontent_role: {role}\nstatus: {status}\nversion: {version}\n"
            f"type: {role if role == 'Plan' else kind}\ncurrent_scope_unit: {owner}\n"
            "relations:\n"
            f"  is_decomposition_of: {relation}\n"
            "---\n# carrier\n",
            encoding="utf-8",
        )
        return path

    def test_direct_targets_are_exact_and_projection_copy_is_excluded(self) -> None:
        source = self._carrier("authority/09_operations/current.md", "CA-O-001", version=7)
        self._carrier(
            "authority/_projection/09_operations/copy.md", "CA-O-001", version=99,
        )

        result = inventory_proposed_references(self.root, self.structure, ["CA-O-001"])

        self.assertEqual(1, len(result.direct_targets))
        target = result.direct_targets[0]
        self.assertEqual("CA-O-001", target.atom_id)
        self.assertEqual("Active", target.status)
        self.assertEqual(7, target.version)
        self.assertEqual("authority/09_operations/current.md", target.path)
        self.assertEqual(hashlib.sha256(source.read_bytes()).hexdigest(), target.sha256)
        self.assertEqual("CA-O-001", target.metadata["atom_id"])
        self.assertEqual((), result.plan_parent_closure)

    def test_direct_target_accepts_canonical_lowercase_active_without_rewriting(self) -> None:
        self._carrier("authority/09_operations/lower-active.md", "CA-O-001A", status="active")

        result = inventory_proposed_references(self.root, self.structure, ["CA-O-001A"])

        self.assertEqual("active", result.direct_targets[0].status)
        self.assertEqual("active", result.direct_targets[0].metadata["status"])

    def test_unknown_directories_and_role_lookalikes_are_not_read(self) -> None:
        requested = self._carrier("authority/09_operations/requested.md", "CA-O-001")
        for relative in (
            "authority/evidence/broken.md",
            "authority/evidence/09_operations/broken.md",
            "authority/09_operations/evidence/broken.md",
        ):
            path = self.root / relative
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text("---\natom_id: [unterminated\n---\n", encoding="utf-8")

        with patch.object(ReadContext, "read", autospec=True, side_effect=ReadContext.read) as reads:
            result = inventory_proposed_references(self.root, self.structure, ["CA-O-001"])

        self.assertEqual(["CA-O-001"], [item.atom_id for item in result.direct_targets])
        self.assertTrue(all(call.args[1] == requested for call in reads.call_args_list))

    def test_protected_and_markdown_named_unknown_directories_are_not_read(self) -> None:
        requested = self._carrier("authority/09_operations/requested.md", "CA-O-001")
        for directory in (".aws", ".env", "notes.md"):
            with self.subTest(directory=directory):
                path = self.root / "authority/09_operations" / directory / "broken.md"
                path.parent.mkdir()
                path.write_text("---\natom_id: [unterminated\n---\n", encoding="utf-8")
                try:
                    with patch.object(ReadContext, "read", autospec=True, side_effect=ReadContext.read) as reads:
                        inventory_proposed_references(self.root, self.structure, ["CA-O-001"])
                    self.assertTrue(all(call.args[1] == requested for call in reads.call_args_list))
                finally:
                    path.unlink()
                    path.parent.rmdir()

    def test_unknown_directory_carriers_cannot_satisfy_named_targets(self) -> None:
        self._carrier("authority/evidence/09_operations/named.md", "CA-O-001")

        with self.assertRaisesRegex(ProposedReferenceError, "missing"):
            inventory_proposed_references(self.root, self.structure, ["CA-O-001"])

    def test_unknown_directory_carrier_cannot_supply_plan_parent(self) -> None:
        self._carrier("authority/03_plan/requested.md", "CA-P-CHILD", role="Plan")
        self._carrier("authority/evidence/03_plan/parent.md", "CA-P-PARENT", role="Plan")
        candidate = {
            "content_role": "Plan", "status": "Active",
            "relations": {"is_decomposition_of": ["CA-P-PARENT"]},
        }

        with self.assertRaisesRegex(ProposedReferenceError, "parent is missing"):
            inventory_proposed_references(
                self.root, self.structure, ["CA-P-CHILD"], candidate_metadata=candidate,
                candidate_path="authority/evidence/03_plan/parent/child.md",
            )

    def test_exact_project_and_independently_declared_nested_scope_roots(self) -> None:
        self.structure["scope_units"].append({"scope_unit_name": "NESTED", "authority_path": "authority/nested"})
        self._carrier("authority/09_operations/root.md", "CA-O-ROOT")
        self._carrier("authority/nested/09_operations/nested.md", "CA-O-NESTED", owner="NESTED")
        self._carrier(".control/09_operations/project.md", "CA-O-PROJECT", owner="fixture")
        self._carrier("authority/not-declared/09_operations/copy.md", "CA-O-NESTED")
        self._carrier(".control/not-declared/09_operations/copy.md", "CA-O-PROJECT")

        result = inventory_proposed_references(
            self.root, self.structure, ["CA-O-ROOT", "CA-O-NESTED", "CA-O-PROJECT"],
            project_authority_paths=(".control",), project_name="fixture",
        )

        self.assertEqual(
            ["authority/09_operations/root.md", "authority/nested/09_operations/nested.md", ".control/09_operations/project.md"],
            [item.path for item in result.direct_targets],
        )

    def test_more_specific_scope_owner_wins_in_both_structure_row_orders(self) -> None:
        self._carrier("authority/03_plan/parent.md", "CA-P-PARENT", role="Plan", owner="A")
        self._carrier("authority/03_plan/parent/03_plan.md", "CA-P-INNER", role="Plan", owner="A", parent="CA-P-PARENT")
        rows = [
            {"scope_unit_name": "A", "authority_path": "authority"},
            {"scope_unit_name": "B", "authority_path": "authority/03_plan/parent"},
        ]
        for owners in (rows, list(reversed(rows))):
            for owner in ("A", "B"):
                with self.subTest(order=[row["scope_unit_name"] for row in owners], owner=owner):
                    self._carrier(
                        "authority/03_plan/parent/03_plan/child.md", "CA-P-TARGET", role="Plan", owner=owner,
                        parent="CA-P-INNER" if owner == "A" else None,
                    )
                    if owner == "A":
                        with self.assertRaises(ProposedReferenceError):
                            inventory_proposed_references(self.root, {"scope_units": owners}, ["CA-P-TARGET"])
                    else:
                        result = inventory_proposed_references(self.root, {"scope_units": owners}, ["CA-P-TARGET"])
                        self.assertEqual("B", result.direct_targets[0].metadata["current_scope_unit"])

    def test_legacy_archive_is_not_read_or_used_as_identity(self) -> None:
        self._carrier("authority/09_operations/requested.md", "CA-O-001")
        old = self._carrier("authority/09_operations/archive/old.md", "CA-O-OLD")
        old.write_text("---\natom_id: [unterminated\n---\n", encoding="utf-8")

        inventory_proposed_references(self.root, self.structure, ["CA-O-001"])
        with self.assertRaisesRegex(ProposedReferenceError, "missing"):
            inventory_proposed_references(self.root, self.structure, ["CA-O-OLD"])

    def test_archived_revision_with_preserved_active_header_cannot_satisfy_target(self) -> None:
        self._carrier("authority/09_operations/archived/old.md", "CA-O-OLD")

        with self.assertRaises(ProposedReferenceError):
            inventory_proposed_references(self.root, self.structure, ["CA-O-OLD"])

    def test_current_target_coexists_with_archived_active_header_and_historical_owner(self) -> None:
        self._carrier("authority/09_operations/current.md", "CA-O-001", version=2)
        self._carrier("authority/09_operations/archived/old.md", "CA-O-001", owner="PREVIOUS")

        result = inventory_proposed_references(self.root, self.structure, ["CA-O-001"])

        self.assertEqual("authority/09_operations/current.md", result.direct_targets[0].path)
        self.assertEqual(2, result.direct_targets[0].version)

    def test_current_plan_parent_coexists_with_archived_active_header(self) -> None:
        self._carrier("authority/03_plan/parent.md", "CA-P-PARENT", role="Plan", version=2)
        self._carrier("authority/03_plan/archived/old.md", "CA-P-PARENT", role="Plan", owner="PREVIOUS")
        candidate = {"content_role": "Plan", "status": "Active", "relations": {"is_decomposition_of": ["CA-P-PARENT"]}}

        result = inventory_proposed_references(
            self.root, self.structure, ["CA-P-PARENT"], candidate_metadata=candidate,
            candidate_path="authority/03_plan/parent/child.md",
        )

        self.assertEqual(["authority/03_plan/parent.md"], [item.path for item in result.plan_parent_closure])
        self.assertEqual(2, result.direct_targets[0].version)

    def test_declared_scope_root_named_archived_is_not_a_status_container(self) -> None:
        self._carrier("archived/09_operations/current.md", "CA-O-001")
        structure = {"scope_units": [{"scope_unit_name": "TEST", "authority_path": "archived"}]}

        result = inventory_proposed_references(self.root, structure, ["CA-O-001"])

        self.assertEqual("Active", result.direct_targets[0].status)

    def test_archived_revision_with_preserved_active_header_cannot_supply_parent(self) -> None:
        self._carrier("authority/09_operations/requested.md", "CA-O-001")
        self._carrier("authority/03_plan/archived/parent.md", "CA-P-PARENT", role="Plan")
        candidate = {"content_role": "Plan", "status": "Active", "relations": {"is_decomposition_of": ["CA-P-PARENT"]}}

        with self.assertRaises(ProposedReferenceError):
            inventory_proposed_references(
                self.root, self.structure, ["CA-O-001"], candidate_metadata=candidate,
                candidate_path="authority/03_plan/archived/parent/child.md",
            )

    def test_requested_target_requires_its_role_owner_and_local_status_placement(self) -> None:
        cases = (
            ("authority/03_plan/wrong-role.md", "TEST"),
            ("authority/09_operations/wrong-owner.md", "OTHER"),
            ("authority/09_operations/draft/wrong-status.md", "TEST"),
        )
        for relative, owner in cases:
            with self.subTest(relative=relative):
                path = self._carrier(relative, "CA-O-001", owner=owner)
                try:
                    with self.assertRaises(ProposedReferenceError):
                        inventory_proposed_references(self.root, self.structure, ["CA-O-001"])
                finally:
                    path.unlink()

    def test_requested_role_without_status_authority_refuses(self) -> None:
        self._carrier("authority/08_implementation/current.md", "CA-I-001", role="Implementation")

        with self.assertRaises(ProposedReferenceError):
            _inventory_proposed_references(
                self.root, self.structure, ["CA-I-001"],
                admitted_role_folders={"Implementation": "08_implementation"},
                admitted_status_folders={},
            )

    def test_malformed_immediate_admitted_carrier_refuses_before_descending(self) -> None:
        self._carrier("authority/09_operations/requested.md", "CA-O-001")
        malformed = self._carrier("authority/09_operations/broken.md", "CA-O-BROKEN", kind="Workflow")
        malformed.write_text("---\natom_id: [unterminated\n---\n", encoding="utf-8")
        self._carrier("authority/09_operations/broken/step.md", "CA-O-STEP", kind="Step")

        with patch.object(ReadContext, "read", autospec=True, side_effect=ReadContext.read) as reads:
            with self.assertRaises(ProposedReferenceError):
                inventory_proposed_references(self.root, self.structure, ["CA-O-001"])
        self.assertTrue(all("broken" not in call.args[1].parts for call in reads.call_args_list))

    def test_malformed_canonical_archived_carrier_still_refuses(self) -> None:
        self._carrier("authority/09_operations/requested.md", "CA-O-001")
        old = self._carrier("authority/09_operations/archived/old.md", "CA-O-OLD")
        old.write_text("---\natom_id: [unterminated\n---\n", encoding="utf-8")

        with self.assertRaises(ProposedReferenceError):
            inventory_proposed_references(self.root, self.structure, ["CA-O-001"])

    def test_workflow_and_recursive_step_siblings_admit_separate_step_carriers(self) -> None:
        self._carrier("authority/09_operations/workflow.md", "CA-O-WORKFLOW", kind="Workflow")
        self._carrier("authority/09_operations/workflow/step.md", "CA-O-STEP", kind="Step")
        self._carrier("authority/09_operations/workflow/step/deep.md", "CA-O-DEEP", kind="Step")
        self._carrier("authority/09_operations/standalone-step.md", "CA-O-STANDALONE", kind="Step")
        self._carrier("authority/09_operations/action.md", "CA-O-ACTION")

        ids = ["CA-O-WORKFLOW", "CA-O-STEP", "CA-O-DEEP", "CA-O-STANDALONE", "CA-O-ACTION"]
        result = inventory_proposed_references(self.root, self.structure, ids)

        self.assertEqual(ids, [item.atom_id for item in result.direct_targets])
        self.assertEqual((), result.plan_parent_closure)

    def test_operations_directory_needs_exact_authenticated_workflow_or_step_sibling(self) -> None:
        self._carrier("authority/09_operations/unrelated.md", "CA-O-WORKFLOW", kind="Workflow")
        self._carrier("authority/09_operations/wrong-name/step.md", "CA-O-STEP", kind="Step")
        with self.assertRaisesRegex(ProposedReferenceError, "missing"):
            inventory_proposed_references(self.root, self.structure, ["CA-O-STEP"])
        for kind in ("Action", "[Workflow]"):
            with self.subTest(kind=kind):
                self._carrier("authority/09_operations/wrong-name.md", "CA-O-ACTION", kind=kind)
                with self.assertRaises(ProposedReferenceError):
                    inventory_proposed_references(self.root, self.structure, ["CA-O-STEP"])

    def test_workflow_tree_refuses_actions_and_second_workflow_definitions(self) -> None:
        self._carrier("authority/09_operations/workflow.md", "CA-O-WORKFLOW", kind="Workflow")
        self._carrier("authority/09_operations/workflow/step.md", "CA-O-STEP", kind="Step")
        for kind in ("Action", "Workflow"):
            with self.subTest(kind=kind):
                self._carrier("authority/09_operations/workflow/step/illegal.md", "CA-O-ILLEGAL", kind=kind)
                with self.assertRaises(ProposedReferenceError):
                    inventory_proposed_references(self.root, self.structure, ["CA-O-WORKFLOW"])

    def test_plan_directory_requires_matching_authenticated_parent_and_owner(self) -> None:
        parent = self._carrier("authority/03_plan/parent.md", "CA-P-PARENT", role="Plan", owner="OTHER")
        self._carrier("authority/03_plan/parent/child.md", "CA-P-CHILD", role="Plan", parent="CA-P-PARENT")
        with self.assertRaises(ProposedReferenceError):
            inventory_proposed_references(self.root, self.structure, ["CA-P-CHILD"])
        parent.unlink()
        with self.assertRaisesRegex(ProposedReferenceError, "missing"):
            inventory_proposed_references(self.root, self.structure, ["CA-P-CHILD"])

    def test_candidate_plan_parent_requires_plan_type_as_well_as_role(self) -> None:
        self._carrier("authority/09_operations/requested.md", "CA-O-001")
        parent = self._carrier("authority/03_plan/parent.md", "CA-P-PARENT", role="Plan")
        parent.write_bytes(parent.read_bytes().replace(b"type: Plan", b"type: Action"))
        candidate = {"content_role": "Plan", "status": "Active", "relations": {"is_decomposition_of": ["CA-P-PARENT"]}}

        with self.assertRaises(ProposedReferenceError):
            inventory_proposed_references(
                self.root, self.structure, ["CA-O-001"], candidate_metadata=candidate,
                candidate_path="authority/03_plan/parent/child.md",
            )

    def test_plan_and_operations_status_folders_do_not_make_nonactive_targets_active(self) -> None:
        for role, statuses in STATUS_FOLDERS.items():
            for status, folder in statuses.items():
                if not folder:
                    continue
                with self.subTest(role=role, status=status):
                    path = self._carrier(
                        f"authority/{ROLE_FOLDERS[role]}/{folder}/inactive.md", "CA-O-INACTIVE",
                        role=role, status=status,
                    )
                    with self.assertRaisesRegex(ProposedReferenceError, "inactive"):
                        inventory_proposed_references(self.root, self.structure, ["CA-O-INACTIVE"])
                    path.unlink()

    def test_parent_status_never_substitutes_for_carried_child_status(self) -> None:
        self._carrier("authority/09_operations/workflow.md", "CA-O-WORKFLOW", kind="Workflow")
        self._carrier("authority/09_operations/workflow/draft/step.md", "CA-O-STEP", kind="Step", status="Draft")
        with self.assertRaisesRegex(ProposedReferenceError, "inactive"):
            inventory_proposed_references(self.root, self.structure, ["CA-O-STEP"])

    def test_active_nested_target_keeps_own_status_under_nonactive_ancestor(self) -> None:
        self._carrier("authority/09_operations/draft/workflow.md", "CA-O-WORKFLOW", kind="Workflow", status="Draft")
        self._carrier("authority/09_operations/draft/workflow/step.md", "CA-O-STEP", kind="Step")

        result = inventory_proposed_references(self.root, self.structure, ["CA-O-STEP"])

        self.assertEqual("Active", result.direct_targets[0].status)

    def test_symlinks_in_admitted_files_and_role_directories_refuse(self) -> None:
        target = self._carrier("outside/requested.md", "CA-O-001")
        role = self.root / "authority/09_operations"
        role.mkdir()
        link = role / "requested.md"
        link.symlink_to(target)
        with self.assertRaises(ProposedReferenceError):
            inventory_proposed_references(self.root, self.structure, ["CA-O-001"])
        link.unlink()
        role.rmdir()
        role.symlink_to(target.parent, target_is_directory=True)
        with self.assertRaises(ProposedReferenceError):
            inventory_proposed_references(self.root, self.structure, ["CA-O-001"])

    def test_unknown_symlink_directory_is_not_followed(self) -> None:
        self._carrier("authority/09_operations/requested.md", "CA-O-001")
        (self.root / "authority/evidence").symlink_to(self.root, target_is_directory=True)
        inventory_proposed_references(self.root, self.structure, ["CA-O-001"])

    def test_unknown_carriers_do_not_consume_candidate_budget(self) -> None:
        self._carrier("authority/09_operations/requested.md", "CA-O-001")
        for index in range(3):
            self._carrier(f"authority/evidence/{index}.md", f"CA-O-UNKNOWN-{index}")
        with patch.dict(CEILINGS, max_candidates=1):
            inventory_proposed_references(self.root, self.structure, ["CA-O-001"])

    def test_authenticated_container_symlink_refuses(self) -> None:
        self._carrier("authority/09_operations/workflow.md", "CA-O-WORKFLOW", kind="Workflow")
        step = self._carrier("outside/step.md", "CA-O-STEP", kind="Step")
        (self.root / "authority/09_operations/workflow").symlink_to(step.parent, target_is_directory=True)
        with self.assertRaises(ProposedReferenceError):
            inventory_proposed_references(self.root, self.structure, ["CA-O-WORKFLOW"])

    def test_admitted_bytes_changed_during_inventory_refuse(self) -> None:
        source = self._carrier("authority/09_operations/requested.md", "CA-O-001")
        original_read = ReadContext.read
        changed = False

        def read_and_change(reader, path, **kwargs):
            nonlocal changed
            raw = original_read(reader, path, **kwargs)
            if path == source and not changed:
                changed = True
                source.write_bytes(raw.replace(b"version: 1", b"version: 2"))
            return raw

        with patch.object(ReadContext, "read", read_and_change):
            with self.assertRaisesRegex(ProposedReferenceError, "changed"):
                inventory_proposed_references(self.root, self.structure, ["CA-O-001"])

    def test_unknown_directory_change_does_not_expand_currentness_frontier(self) -> None:
        source = self._carrier("authority/09_operations/requested.md", "CA-O-001")
        original_read = ReadContext.read

        def read_and_change_unknown(reader, path, **kwargs):
            raw = original_read(reader, path, **kwargs)
            if path == source:
                self._carrier("authority/evidence/09_operations/new.md", "CA-O-UNKNOWN")
            return raw

        with patch.object(ReadContext, "read", read_and_change_unknown):
            inventory_proposed_references(self.root, self.structure, ["CA-O-001"])

    def test_admitted_membership_and_new_role_directory_changes_refuse(self) -> None:
        source = self._carrier("authority/09_operations/requested.md", "CA-O-001")
        for relative, role in (("authority/09_operations/new.md", "Operations"), ("authority/03_plan/new.md", "Plan")):
            with self.subTest(relative=relative):
                original_read = ReadContext.read
                introduced = False

                def read_and_add(reader, path, **kwargs):
                    nonlocal introduced
                    raw = original_read(reader, path, **kwargs)
                    if path == source and not introduced:
                        introduced = True
                        self._carrier(relative, "CA-NEW", role=role)
                    return raw

                with patch.object(ReadContext, "read", read_and_add):
                    with self.assertRaisesRegex(ProposedReferenceError, "changed"):
                        inventory_proposed_references(self.root, self.structure, ["CA-O-001"])
                (self.root / relative).unlink()

    def test_named_nonactive_status_refuses_instead_of_satisfying_target(self) -> None:
        self._carrier("authority/09_operations/archived/old.md", "CA-O-002", status="Archived")

        with self.assertRaisesRegex(ProposedReferenceError, "inactive or archived"):
            inventory_proposed_references(self.root, self.structure, ["CA-O-002"])

    def test_duplicate_active_target_and_missing_target_fail_closed(self) -> None:
        self._carrier("authority/09_operations/one.md", "CA-O-003")
        self._carrier("authority/09_operations/two.md", "CA-O-003")
        with self.assertRaisesRegex(ProposedReferenceError, "ambiguous"):
            inventory_proposed_references(self.root, self.structure, ["CA-O-003"])
        with self.assertRaisesRegex(ProposedReferenceError, "missing"):
            inventory_proposed_references(self.root, self.structure, ["CA-O-404"])

    def test_nonpositive_target_versions_fail_closed(self) -> None:
        path = self._carrier("authority/09_operations/version.md", "CA-O-004", version=0)
        with self.assertRaisesRegex(ProposedReferenceError, "identity, status, or version"):
            inventory_proposed_references(self.root, self.structure, ["CA-O-004"])
        path.unlink()
        self._carrier("authority/09_operations/version.md", "CA-O-004", version=-1)
        with self.assertRaisesRegex(ProposedReferenceError, "identity, status, or version"):
            inventory_proposed_references(self.root, self.structure, ["CA-O-004"])

    def test_nested_plan_requires_actual_authenticated_parent_chain(self) -> None:
        root_parent = self._carrier(
            "authority/03_plan/CA-P-ROOT--root.md", "CA-P-ROOT", role="Plan",
        )
        parent = self._carrier(
            "authority/03_plan/CA-P-ROOT--root/CA-P-PARENT--parent.md",
            "CA-P-PARENT", role="Plan", parent="CA-P-ROOT",
        )
        candidate_path = "authority/03_plan/CA-P-ROOT--root/CA-P-PARENT--parent/child.md"
        candidate = {
            "content_role": "Plan",
            "status": "Active",
            "relations": {"is_decomposition_of": ["CA-P-PARENT"]},
        }

        result = inventory_proposed_references(
            self.root, self.structure, ["CA-P-PARENT"],
            candidate_metadata=candidate, candidate_path=candidate_path,
        )

        self.assertEqual(["CA-P-PARENT"], [item.atom_id for item in result.direct_targets])
        self.assertEqual(["CA-P-PARENT", "CA-P-ROOT"], [item.atom_id for item in result.plan_parent_closure])
        self.assertEqual(root_parent.name, Path(result.plan_parent_closure[1].path).name)
        self.assertEqual(parent.name, Path(result.plan_parent_closure[0].path).name)

    def test_nested_plan_rejects_off_frontier_lookalike_parent_directory(self) -> None:
        self._carrier(
            "authority/03_plan/CA-P-PARENT--parent.md", "CA-P-PARENT", role="Plan",
        )
        candidate = {
            "content_role": "Plan",
            "status": "Active",
            "relations": {"is_decomposition_of": ["CA-P-PARENT"]},
        }

        with self.assertRaisesRegex(ProposedReferenceError, "authenticated Markdown parent carrier"):
            inventory_proposed_references(
                self.root, self.structure, ["CA-P-PARENT"],
                candidate_metadata=candidate,
                candidate_path="untrusted/CA-P-PARENT--parent/child.md",
            )

    def test_nested_done_plan_uses_only_the_source_admitted_status_folder(self) -> None:
        self._carrier("authority/03_plan/CA-P-PARENT--parent.md", "CA-P-PARENT", role="Plan")
        candidate = {
            "content_role": "Plan",
            "status": "Done",
            "relations": {"is_decomposition_of": ["CA-P-PARENT"]},
        }
        admitted = {"Done": "done"}

        result = inventory_proposed_references(
            self.root, self.structure, ["CA-P-PARENT"],
            candidate_metadata=candidate,
            candidate_path="authority/03_plan/CA-P-PARENT--parent/done/child.md",
            admitted_plan_status_folders=admitted,
        )

        self.assertEqual(["CA-P-PARENT"], [item.atom_id for item in result.plan_parent_closure])
        with self.assertRaisesRegex(ProposedReferenceError, "authenticated Markdown parent carrier"):
            inventory_proposed_references(
                self.root, self.structure, ["CA-P-PARENT"],
                candidate_metadata=candidate,
                candidate_path="authority/03_plan/CA-P-PARENT--parent/wrong/child.md",
                admitted_plan_status_folders=admitted,
            )

    def test_nested_plan_cycle_wrong_parent_path_and_changed_frontier_fail_closed(self) -> None:
        self._carrier(
            "authority/03_plan/CA-P-A--a/CA-P-B--b.md", "CA-P-B", role="Plan", parent="CA-P-A",
        )
        self._carrier(
            "authority/03_plan/CA-P-A--a.md", "CA-P-A", role="Plan", parent="CA-P-B",
        )
        candidate = {"content_role": "Plan", "relations": {"is_decomposition_of": ["CA-P-A"]}}
        with self.assertRaisesRegex(ProposedReferenceError, "cycle"):
            inventory_proposed_references(
                self.root, self.structure, ["CA-P-A"], candidate_metadata=candidate,
                candidate_path="authority/03_plan/CA-P-A--a/child.md",
            )

        self._carrier("authority/09_operations/plain.md", "CA-O-005")
        with patch("validate_atoms_workers.proposed_references.ReadContext.currentness", return_value={"state": "changed"}):
            with self.assertRaisesRegex(ProposedReferenceError, "changed"):
                inventory_proposed_references(self.root, self.structure, ["CA-O-005"])


if __name__ == "__main__":
    unittest.main()
