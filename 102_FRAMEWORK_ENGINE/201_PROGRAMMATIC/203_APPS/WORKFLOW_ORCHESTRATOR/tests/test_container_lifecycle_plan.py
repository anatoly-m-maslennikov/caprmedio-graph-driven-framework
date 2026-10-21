"""Focused pure semantic checks for contained lifecycle planning."""

from __future__ import annotations

from pathlib import Path
import sys
import unittest

APP = Path(__file__).resolve().parents[1]
TOOLS = APP.parents[1] / "201_TOOLS"
for location in (APP, TOOLS):
    sys.path.insert(0, str(location))

from contained_atom_targets import ContainedAtomInventory, ContainedAtomTarget  # noqa: E402
from VALIDATE_ATOMS.validate_atoms_workers.proposed_references import TargetCarrier  # noqa: E402
from container_lifecycle import plan_contained_status_changes  # noqa: E402


def _target(atom_id: str, parent: str, path: str, role: str = "Plan", status: str = "Active"):
    return ContainedAtomTarget(atom_id, role, role, status, 1, path, "a" * 64, parent, path, None)


def _inventory(*targets: ContainedAtomTarget) -> ContainedAtomInventory:
    parent = TargetCarrier("CA-P-ROOT", "Active", 1, "03_plan/root.md", "root" * 16, {})
    return ContainedAtomInventory(parent, targets)


class ContainerLifecyclePlanTests(unittest.TestCase):
    def test_done_is_deepest_first_and_maps_non_done_plans_to_canceled(self):
        grandchild = _target("CA-P-GRAND", "CA-P-CHILD", "03_plan/root/child/grand.md")
        child = _target("CA-P-CHILD", "CA-P-ROOT", "03_plan/root/child.md")
        done = _target("CA-P-DONE", "CA-P-ROOT", "03_plan/root/done.md", status="Done")
        operation = _target("CA-O-STEP", "CA-P-ROOT", "09_operations/step.md", "Operations")
        planned = plan_contained_status_changes(_inventory(done, operation, child, grandchild), "Done")
        self.assertEqual(
            [("CA-P-GRAND", "Canceled"), ("CA-P-CHILD", "Canceled"),
             ("CA-P-DONE", "Done"), ("CA-O-STEP", "Done")],
            [(target.atom_id, status) for target, status in planned],
        )

    def test_archived_includes_done_and_excludes_parent_without_mutation(self):
        done = _target("CA-P-DONE", "CA-P-ROOT", "03_plan/root/done.md", status="Done")
        inventory = _inventory(done)
        before = inventory.targets
        planned = plan_contained_status_changes(inventory, "Archived")
        self.assertEqual(((done, "Archived"),), planned)
        self.assertIs(inventory.targets, before)
        self.assertEqual("Done", done.status)

    def test_other_requested_status_propagates_without_model_validation(self):
        plan = _target("CA-P-PLAN", "CA-P-ROOT", "03_plan/root/plan.md")
        operation = _target("CA-O-STEP", "CA-P-ROOT", "09_operations/step.md", "Operations")
        planned = plan_contained_status_changes(_inventory(plan, operation), "Custom")
        self.assertEqual(["Custom", "Custom"], [status for _target, status in planned])

    def test_malformed_manual_parent_link_is_rejected(self):
        with self.assertRaises(ValueError):
            plan_contained_status_changes(_inventory(_target("CA-P-ORPHAN", "CA-P-MISSING", "orphan.md")), "Done")

    def test_malformed_descendant_id_or_parent_link_is_rejected(self):
        malformed = (
            _target("", "CA-P-ROOT", "blank-id.md"),
            _target(123, "CA-P-ROOT", "numeric-id.md"),
            _target("CA-P-BLANK-PARENT", "", "blank-parent.md"),
            _target("CA-P-NONSTRING-PARENT", 123, "numeric-parent.md"),
        )
        for target in malformed:
            with self.subTest(target=target.path):
                with self.assertRaises(ValueError):
                    plan_contained_status_changes(_inventory(target), "Done")

    def test_blank_requested_status_is_rejected_without_a_status_allowlist(self):
        target = _target("CA-P-CHILD", "CA-P-ROOT", "03_plan/root/child.md")
        for status in ("", "   "):
            with self.subTest(status=repr(status)):
                with self.assertRaises(ValueError):
                    plan_contained_status_changes(_inventory(target), status)


if __name__ == "__main__":
    unittest.main()
