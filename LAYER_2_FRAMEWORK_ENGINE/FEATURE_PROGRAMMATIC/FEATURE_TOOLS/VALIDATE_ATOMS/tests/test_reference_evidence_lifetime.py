"""References remain authenticated through the final carrier admission boundary."""

from pathlib import Path
import unittest
from unittest.mock import patch

import test_plan_blocking_reference_admission_independent as blocking
import test_nested_operation_placement as nested


class ReferenceEvidenceLifetimeTests(unittest.TestCase):
    def setUp(self):
        self.fixture = blocking.PlanBlockingReferenceAdmissionIndependentTests()
        self.fixture.setUp()
        self.addCleanup(self.fixture.doCleanups)
        self.first = self.fixture.target("Backlog", relations='{"blocks": ["CA-P-711"]}')
        self.second = self.fixture.target("Done", identifier="CA-P-711", filename="second.md")

    def after_inventory(self, change, validate=None):
        admission = blocking.scoped.admission
        original = admission.inventory_proposed_references

        def changing_inventory(*args, **kwargs):
            result = original(*args, **kwargs)
            change()
            return result

        with patch.object(admission, "inventory_proposed_references", changing_inventory):
            return (self.fixture.validate if validate is None else validate)()

    def test_unchanged_evidence_passes_final_admission(self):
        result = self.after_inventory(lambda: None)
        self.assertEqual((result["findings"], result["gaps"]), ([], []))

    def test_reachable_edit_after_inventory_refuses(self):
        def change():
            self.second.write_bytes(self.second.read_bytes().replace(
                b"relations: {}", b"relations: {blocks: [CA-P-MISSING]}",
            ))
        with self.assertRaisesRegex(blocking.scoped.admission.ProposedCarrierError, "relation inventory changed"):
            self.after_inventory(change)

    def test_direct_target_edit_after_inventory_refuses(self):
        def change():
            self.first.write_bytes(self.first.read_bytes() + b"\nChanged direct target.\n")
        with self.assertRaisesRegex(blocking.scoped.admission.ProposedCarrierError, "relation inventory changed"):
            self.after_inventory(change)

    def test_parent_edit_after_inventory_refuses(self):
        parent = self.fixture.target("Active", identifier="CA-P-730", filename="parent.md")
        metadata = dict(self.fixture.metadata, relations={"is_decomposition_of": ["CA-P-730"]})
        def validate():
            return blocking.scoped.admission.validate_proposed_carrier(
                metadata, blocking.scoped.fixtures.PLAN_BODY, self.fixture.fixture.context,
                Path("03_plan/parent/proposed.md"), reference_roles=blocking.scoped.PRMEDO,
            )
        def change():
            parent.write_bytes(parent.read_bytes() + b"\nChanged parent.\n")
        with self.assertRaisesRegex(blocking.scoped.admission.ProposedCarrierError, "relation inventory changed"):
            self.after_inventory(change, validate)

    def test_target_deleted_after_inventory_refuses(self):
        with self.assertRaisesRegex(blocking.scoped.admission.ProposedCarrierError, "relation inventory changed"):
            self.after_inventory(self.second.unlink)

    def test_new_competing_target_after_inventory_refuses(self):
        def change():
            self.fixture.target("Backlog", filename="duplicate.md")
        with self.assertRaisesRegex(blocking.scoped.admission.ProposedCarrierError, "relation inventory changed"):
            self.after_inventory(change)

    def test_added_status_frontier_after_inventory_refuses(self):
        def change():
            self.fixture.target("Canceled", identifier="CA-P-799", filename="new.md")
        with self.assertRaisesRegex(blocking.scoped.admission.ProposedCarrierError, "relation inventory changed"):
            self.after_inventory(change)

    def test_excluded_role_change_keeps_explicit_reference_frontier(self):
        def change():
            self.fixture.fixture.fixture.put(
                self.fixture.fixture.control / "01_concern/legacy.md", blocking.scoped.BROKEN,
            )
        result = self.after_inventory(change)
        self.assertEqual((result["findings"], result["gaps"]), ([], []))

    def test_nested_operations_early_return_rechecks_direct_reference(self):
        fixture = nested.NestedOperationsPlacementTests()
        fixture.setUp()
        self.addCleanup(fixture.doCleanups)
        fixture.put("09_operations/workflow.md", atom_id="CA-O-731", type="Workflow")
        def change():
            target = fixture.fixture.target
            target.write_bytes(target.read_bytes() + b"\nChanged direct reference.\n")
        with self.assertRaisesRegex(blocking.scoped.admission.ProposedCarrierError, "relation inventory changed"):
            self.after_inventory(change, lambda: fixture.validate("09_operations/workflow/step.md"))


if __name__ == "__main__":
    unittest.main()
