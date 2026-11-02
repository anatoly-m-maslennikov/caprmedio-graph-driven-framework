"""One lookup per identity does not merge or normalize distinct relation facts."""

from copy import deepcopy
import unittest

import test_proposed_reference_scope_independent as scoped


class CrossKindReferenceIndependentTests(unittest.TestCase):
    def setUp(self):
        self.fixture = scoped.ExplicitReferenceScopeIndependentTests()
        self.addCleanup(self.fixture.doCleanups)
        self.fixture.setUp()

    def test_one_actual_target_can_be_referenced_through_two_kinds(self):
        relations = {"evaluation_for": ["CA-O-702"], "depends_on": ["CA-O-702"]}
        metadata = dict(self.fixture.metadata, relations=relations)
        original = deepcopy(metadata)
        before = scoped.fixtures.snapshot(self.fixture.root)
        for scope in (None, scoped.PRMEDO):
            with self.subTest(scope=scope):
                result = self.fixture.validate(metadata=metadata, scope=scope)
                self.assertEqual((result["findings"], result["gaps"]), ([], []))
                if scope is not None:
                    self.assertEqual(result["reference_scope"]["direct_targets"], ["CA-O-702"])
                self.assertEqual(metadata, original)
        self.assertEqual(scoped.fixtures.snapshot(self.fixture.root), before)

    def test_duplicates_within_each_kind_still_refuse(self):
        for kind in ("evaluation_for", "depends_on"):
            relations = {"evaluation_for": ["CA-O-702"], "depends_on": ["CA-O-702"]}
            relations[kind].append("CA-O-702")
            for scope in (None, scoped.PRMEDO):
                with self.subTest(kind=kind, scope=scope):
                    with self.assertRaises(scoped.admission.ProposedCarrierError):
                        self.fixture.validate(metadata=dict(self.fixture.metadata, relations=relations), scope=scope)

    def test_lookup_dedup_does_not_hide_missing_or_duplicate_carriers(self):
        relations = {"evaluation_for": ["CA-O-702"], "depends_on": ["CA-O-702"]}
        raw = self.fixture.target.read_bytes()
        self.fixture.target.unlink()
        with self.assertRaises(scoped.admission.ProposedCarrierError):
            self.fixture.validate(metadata=dict(self.fixture.metadata, relations=relations))
        self.fixture.target.write_bytes(raw)
        self.fixture.fixture.put(self.fixture.control / "09_operations/duplicate.md", raw)
        with self.assertRaises(scoped.admission.ProposedCarrierError):
            self.fixture.validate(metadata=dict(self.fixture.metadata, relations=relations))


if __name__ == "__main__":
    unittest.main()
