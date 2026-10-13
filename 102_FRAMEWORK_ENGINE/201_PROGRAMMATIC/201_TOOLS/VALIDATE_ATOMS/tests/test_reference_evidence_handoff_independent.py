"""Real reference lookup evidence must remain current through final admission."""

from copy import deepcopy
from pathlib import Path
import unittest
from unittest.mock import patch

import test_plan_blocking_reference_admission_independent as blocking
import test_nested_operation_placement_independent as nested


class ReferenceEvidenceHandoffIndependentTests(unittest.TestCase):
    def setUp(self):
        self.fixture = blocking.PlanBlockingReferenceAdmissionIndependentTests()
        self.fixture.setUp()
        self.addCleanup(self.fixture.doCleanups)

    def after_lookup(self, mutate, validate=None):
        original = blocking.scoped.admission.inventory_proposed_references
        captured = []

        def lookup_then_change(*args, **kwargs):
            inventory = original(*args, **kwargs)
            captured.append(inventory)
            mutate(inventory)
            return inventory

        with patch.object(blocking.scoped.admission, "inventory_proposed_references", lookup_then_change):
            try:
                result = (self.fixture.validate if validate is None else validate)()
            finally:
                self.assertEqual(len(captured), 1)
        return result, captured[0]

    def test_unchanged_actual_lookup_passes_without_rewriting(self):
        self.fixture.target("Backlog")
        before = blocking.scoped.fixtures.snapshot(self.fixture.fixture.root)
        authored = deepcopy(self.fixture.metadata)
        result, inventory = self.after_lookup(lambda _: None)
        inventory.assert_current()
        self.assertEqual((result["findings"], result["gaps"]), ([], []))
        self.assertEqual(self.fixture.metadata, authored)
        self.assertEqual(blocking.scoped.fixtures.snapshot(self.fixture.fixture.root), before)

    def test_direct_target_bytes_changed_after_lookup_refuse_complete_admission(self):
        target = self.fixture.target("Backlog")
        with self.assertRaises(blocking.scoped.admission.ProposedCarrierError):
            self.after_lookup(lambda _: target.write_bytes(target.read_bytes() + b"\nChanged after lookup.\n"))

    def test_reachable_target_bytes_changed_after_lookup_refuse_complete_admission(self):
        self.fixture.target("Backlog", relations='{"blocks": ["CA-P-711"]}')
        target = self.fixture.target("Done", identifier="CA-P-711", filename="leaf.md")
        with self.assertRaises(blocking.scoped.admission.ProposedCarrierError):
            self.after_lookup(lambda _: target.write_bytes(target.read_bytes() + b"\nChanged closure evidence.\n"))

    def test_new_ambiguous_target_after_lookup_refuses_complete_admission(self):
        self.fixture.target("Backlog")
        with self.assertRaises(blocking.scoped.admission.ProposedCarrierError):
            self.after_lookup(lambda _: self.fixture.target("Backlog", filename="duplicate.md"))

    def test_new_unrelated_frontier_carrier_after_lookup_refuses_complete_admission(self):
        self.fixture.target("Backlog")
        with self.assertRaises(blocking.scoped.admission.ProposedCarrierError):
            self.after_lookup(lambda _: self.fixture.target("Active", identifier="CA-P-799", filename="new.md"))

    def test_target_removed_after_lookup_refuses_complete_admission(self):
        target = self.fixture.target("Backlog")
        with self.assertRaises(blocking.scoped.admission.ProposedCarrierError):
            self.after_lookup(lambda _: target.unlink())

    def test_ordinary_active_target_changed_after_lookup_also_refuses(self):
        scoped = self.fixture.fixture
        with self.assertRaises(blocking.scoped.admission.ProposedCarrierError):
            self.after_lookup(lambda _: scoped.target.write_bytes(scoped.target.read_bytes() + b"\nChanged action.\n"),
                              scoped.validate)

    def test_nested_operations_final_return_preserves_unchanged_evidence(self):
        fixture = nested.NestedOperationPlacementIndependentTests()
        fixture.setUp()
        self.addCleanup(fixture.doCleanups)
        fixture.parent()
        before = blocking.scoped.fixtures.snapshot(fixture.root)
        result, inventory = self.after_lookup(lambda _: None, fixture.validate)
        inventory.assert_current()
        self.assertEqual((result["findings"], result["gaps"]), ([], []))
        self.assertEqual(blocking.scoped.fixtures.snapshot(fixture.root), before)

    def test_nested_operations_final_return_refuses_changed_reference_evidence(self):
        fixture = nested.NestedOperationPlacementIndependentTests()
        fixture.setUp()
        self.addCleanup(fixture.doCleanups)
        fixture.parent()
        target = fixture.fixture.target
        with self.assertRaises(blocking.scoped.admission.ProposedCarrierError):
            self.after_lookup(lambda _: target.write_bytes(target.read_bytes() + b"\nChanged after lookup.\n"),
                              fixture.validate)

    def test_typed_plan_endpoint_with_wrong_role_or_foreign_namespace_refuses(self):
        for identifier in ("CA-O-710", "FOREIGN-P-710", "CA-P-710-extra"):
            with self.subTest(identifier=identifier):
                path = self.fixture.target("Backlog", identifier=identifier)
                metadata = dict(self.fixture.metadata, relations={"blocks": [identifier]})
                with self.assertRaisesRegex(blocking.scoped.admission.ProposedCarrierError, "assigned Atom identity"):
                    self.fixture.validate(metadata)
                path.unlink()

    def test_reachable_plan_endpoint_with_wrong_role_or_foreign_namespace_refuses(self):
        for identifier in ("CA-O-711", "FOREIGN-P-711"):
            with self.subTest(identifier=identifier):
                direct = self.fixture.target("Backlog", relations='{"blocks": ["' + identifier + '"]}')
                leaf = self.fixture.target("Done", identifier=identifier, filename="leaf.md")
                with self.assertRaisesRegex(blocking.scoped.admission.ProposedCarrierError, "assigned Atom identity"):
                    self.fixture.validate()
                direct.unlink()
                leaf.unlink()

    def test_selected_custom_prefix_is_used_for_candidate_and_reachable_plan_evidence(self):
        scoped = self.fixture.fixture
        settings = scoped.selection.settings_path
        settings.write_text(settings.read_text().replace('project_prefix = "CA"', 'project_prefix = "LOCAL"'))
        selection = blocking.scoped.fixtures.resolve_project(scoped.root, scoped.control)
        with blocking.scoped.bind_selection(selection):
            scoped.context = blocking.scoped.admission.source_context_from_project(scoped.root)
        self.fixture.target("Backlog", identifier="LOCAL-P-710", relations='{"blocks": ["LOCAL-P-711"]}')
        self.fixture.target("Done", identifier="LOCAL-P-711", filename="leaf.md")
        metadata = dict(self.fixture.metadata, atom_id="LOCAL-P-701", relations={"blocks": ["LOCAL-P-710"]})
        before = blocking.scoped.fixtures.snapshot(scoped.root)
        result = self.fixture.validate(metadata)
        self.assertEqual((result["findings"], result["gaps"]), ([], []))
        self.assertEqual(result["reference_scope"]["direct_targets"], ["LOCAL-P-710"])
        self.assertEqual(blocking.scoped.fixtures.snapshot(scoped.root), before)

    def test_plan_namespace_authority_changed_after_context_capture_refuses(self):
        self.fixture.target("Backlog")
        scoped = self.fixture.fixture
        entry = blocking.scoped.admission._entry("CA-D-378")
        path = scoped.root / scoped.control.joinpath(*Path(entry["source_path"]).parts[1:])
        path.write_bytes(path.read_bytes() + b"\nChanged identity authority.\n")
        with self.assertRaises(blocking.scoped.admission.ProposedCarrierError):
            self.fixture.validate()


if __name__ == "__main__":
    unittest.main()
