"""Exact operation-bound predecessor controls, independent of frozen fixture oracles."""

import copy
import hashlib
from pathlib import Path
import unittest

import test_nested_header_admission as fixtures
from test_nested_header_validation import text_of
from VALIDATE_ATOMS.validate_atoms_workers import proposed_carrier as admission


class NestedHeaderPreservationTests(unittest.TestCase):
    setUp = fixtures.NestedHeaderFunctionalTests.setUp
    context = fixtures.NestedHeaderFunctionalTests.context

    def pin(self, metadata, path=None):
        path = self.path if path is None else path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text_of(metadata))
        return admission.CarrierPredecessor(path, hashlib.sha256(path.read_bytes()).hexdigest())

    def test_foreign_identity_projection_and_unbound_paths_cannot_supply_residue(self):
        candidate = dict(self.metadata, priority='high')
        foreign = copy.deepcopy(candidate)
        foreign['identity']['atom_id'] = 'CA-P-702'
        for before, path in [
            (foreign, self.path),
            (dict(candidate, projection={'source_carrier_path': 'another.md'}), self.path),
            (candidate, self.root / 'outside.md'),
            (candidate, self.path.parent / 'archive/CA-P-701@1.md'),
            (candidate, self.path.parent / 'archived/CA-P-701@1.md'),
        ]:
            with self.subTest(path=path), self.assertRaises(admission.ProposedCarrierError):
                admission._preserved_root_fields(self.context(), candidate, self.pin(before, path))

    def test_explicit_identity_transition_is_tied_to_actual_source_pair_and_role(self):
        before = dict(copy.deepcopy(self.metadata), priority='high')
        before['identity'].pop('atom_id')
        before['state']['status'] = 'Draft'
        pin = self.pin(before)
        after = dict(self.metadata, priority='high')
        with self.assertRaises(admission.ProposedCarrierError):
            admission._preserved_root_fields(self.context(), after, pin)
        transition = admission.CarrierPredecessor(pin.path, pin.sha256, (None, 'CA-P-701'))
        self.assertEqual({'priority': 'high'}, admission._preserved_root_fields(self.context(), after, transition))
        wrong = admission.CarrierPredecessor(pin.path, pin.sha256, (None, 'CA-P-702'))
        with self.assertRaises(admission.ProposedCarrierError):
            admission._preserved_root_fields(self.context(), after, wrong)
        after = copy.deepcopy(after)
        after['context']['role'] = 'Concern'
        with self.assertRaises(admission.ProposedCarrierError):
            admission._preserved_root_fields(self.context(), after, transition)

    def test_current_archived_state_and_scope_residue_preserve_without_scope_fallback(self):
        before = dict(copy.deepcopy(self.metadata), current_scope_unit='legacy-name', priority='high')
        before['state']['status'] = 'Archived'
        pin = self.pin(before)
        after = copy.deepcopy(before)
        after['state']['status'] = 'Active'
        fields = admission._preserved_root_fields(self.context(), after, pin)
        self.assertEqual({'current_scope_unit': 'legacy-name', 'priority': 'high'}, fields)
        self.assertEqual(self.metadata['context']['container'], after['context']['container'])

    def test_control_root_traversal_is_not_an_authorized_predecessor(self):
        before = dict(self.metadata, priority='high')
        pin = self.pin(before, self.root / 'outside.md')
        traversal = self.selection.control_root / '..' / Path(pin.path.name)
        with self.assertRaises(admission.ProposedCarrierError):
            admission._preserved_root_fields(self.context(), before,
                                             admission.CarrierPredecessor(traversal, pin.sha256))


if __name__ == '__main__':
    unittest.main()
