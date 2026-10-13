"""Lookup identities are unique; authored relations remain distinct by kind."""

import copy
import unittest
from unittest.mock import patch

import test_proposed_reference_scope as fixtures
from VALIDATE_ATOMS.validate_atoms_workers import proposed_carrier


class ProposedCrossKindLookupTests(unittest.TestCase):
    def setUp(self):
        self.fixture = fixtures.ProposedReferenceScopeTests()
        self.fixture.setUp()
        self.addCleanup(self.fixture.doCleanups)

    def test_same_target_in_two_kinds_is_looked_up_once_without_rewriting_relations(self):
        metadata = dict(self.fixture.metadata, relations={
            "evaluation_for": ["CA-O-901"], "depends_on": ["CA-O-901"],
        })
        original = copy.deepcopy(metadata)
        before = fixtures.fixtures.snapshot(self.fixture.root)
        for options in ({}, {"reference_roles": fixtures.PRMEDO}):
            with self.subTest(options=options), patch.object(
                proposed_carrier, "inventory_proposed_references",
                wraps=proposed_carrier.inventory_proposed_references,
            ) as lookup:
                result = self.fixture.validate(metadata=metadata, **options)
                self.assertFalse(result["findings"] or result["gaps"])
                self.assertEqual(lookup.call_count, 1)
                self.assertEqual(list(lookup.call_args.args[2]), ["CA-O-901"])
                self.assertEqual(metadata, original)
                self.assertEqual(fixtures.fixtures.snapshot(self.fixture.root), before)

    def test_duplicate_inside_one_kind_still_refuses_before_lookup(self):
        for kind in ("evaluation_for", "depends_on"):
            metadata = dict(self.fixture.metadata, relations={
                "evaluation_for": ["CA-O-901"], "depends_on": ["CA-O-901"],
            })
            metadata["relations"][kind].append("CA-O-901")
            for options in ({}, {"reference_roles": fixtures.PRMEDO}):
                with self.subTest(kind=kind, options=options), patch.object(
                    proposed_carrier, "inventory_proposed_references",
                    wraps=proposed_carrier.inventory_proposed_references,
                ) as lookup:
                    with self.assertRaises(proposed_carrier.ProposedCarrierError):
                        self.fixture.validate(metadata=metadata, **options)
                    lookup.assert_not_called()

    def test_deduplicated_lookup_does_not_skip_other_relation_kind_semantics(self):
        metadata = dict(self.fixture.metadata, relations={
            "evaluation_for": ["CA-O-901"], "method_for": ["CA-O-901"],
        })
        with self.assertRaises(proposed_carrier.ProposedCarrierError):
            self.fixture.validate(metadata=metadata)


if __name__ == "__main__":
    unittest.main()
