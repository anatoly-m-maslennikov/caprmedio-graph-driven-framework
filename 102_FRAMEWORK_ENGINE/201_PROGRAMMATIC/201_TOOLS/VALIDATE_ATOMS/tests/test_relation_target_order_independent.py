"""Independent real-carrier controls for nonsemantic relation-target order."""

from copy import deepcopy
import hashlib
from itertools import permutations
from pathlib import Path
import unittest

import test_proposed_reference_scope_independent as scoped


class RelationTargetOrderIndependentTests(unittest.TestCase):
    def setUp(self):
        self.fixture = scoped.ExplicitReferenceScopeIndependentTests()
        self.addCleanup(self.fixture.doCleanups)
        self.fixture.setUp()
        self.targets = ("CA-O-702", "CA-O-703", "CA-O-704")
        for identifier in (*self.targets[1:], "CA-O-705"):
            self.fixture.fixture.put(
                self.fixture.control / f"09_operations/{identifier}.md",
                self.fixture.target.read_bytes().replace(b"CA-O-702", identifier.encode()),
            )

    def validate(self, relations, *, scope=scoped.PRMEDO):
        metadata = dict(self.fixture.metadata, relations=relations)
        before = deepcopy(metadata)
        result = self.fixture.validate(metadata=metadata, scope=scope)
        self.assertEqual(metadata, before, "Admission must not normalize source relation order")
        self.assertEqual((result["findings"], result["gaps"]), ([], []))
        return result

    def test_all_target_permutations_pass_typed_and_generic_relations_without_normalization(self):
        before = scoped.fixtures.snapshot(self.fixture.root)
        for ordered in permutations(self.targets):
            for scope in (None, scoped.PRMEDO):
                for relations in (
                    {"evaluation_for": list(ordered)},
                    {"evaluation_for": ["CA-O-705"], "depends_on": list(ordered)},
                ):
                    with self.subTest(relations=relations, scope=scope):
                        self.validate(relations, scope=scope)
        self.assertEqual(scoped.fixtures.snapshot(self.fixture.root), before)

    def test_empty_duplicate_missing_noncanonical_and_unsupported_relations_still_refuse(self):
        for relations in (
            {"evaluation_for": []},
            {"evaluation_for": ["CA-O-702", "CA-O-702"]},
            {"evaluation_for": ["CA-O-702", "CA-O-999"]},
            {"evaluation_for": ["CA-O-702", "not-an-atom"]},
            {"evaluation_for": ["CA-O-702"], "relates_to": ["CA-O-703", "CA-O-704"]},
            {"evaluation_for": ["CA-O-702"], "parent_of": ["CA-O-703", "CA-O-704"]},
        ):
            with self.subTest(relations=relations):
                with self.assertRaises(scoped.admission.ProposedCarrierError):
                    self.validate(relations)

    def test_order_change_does_not_relax_typed_endpoint_roles(self):
        self.fixture.fixture.put(self.fixture.control / "03_plan/target.md", (
            b"---\natom_id: CA-P-705\ncontent_role: Plan\ntype: Plan\n"
            b"current_scope_unit: amber\nstatus: Active\nversion: 1\n---\n# Summary\n\nPlan\n"
        ))
        for targets in (["CA-P-705", "CA-O-702"], ["CA-O-702", "CA-P-705"]):
            with self.subTest(targets=targets):
                with self.assertRaisesRegex(scoped.admission.ProposedCarrierError, "relation or Plan decomposition"):
                    self.validate({"evaluation_for": targets})

    def test_current_d268_v13_is_exact_and_stale_or_missing_authority_refuses(self):
        entry = scoped.admission._entry("CA-D-268")
        self.assertEqual(entry["version"], 13)
        self.assertEqual(entry["sha256"], "eba35171683bf9219f32d264cc3eaff985bd7939817114135c3a04faccf8df96")
        path = self.fixture.root / self.fixture.control.joinpath(*Path(entry["source_path"]).parts[1:])
        original = path.read_bytes()
        self.assertEqual(hashlib.sha256(original).hexdigest(), entry["sha256"])
        for replacement in (original + b"\n# changed after admission binding\n", None):
            with self.subTest(missing=replacement is None):
                if replacement is None:
                    path.unlink()
                else:
                    path.write_bytes(replacement)
                try:
                    with self.assertRaises(scoped.admission.ProposedCarrierError):
                        self.validate({"evaluation_for": ["CA-O-704", "CA-O-702"]})
                finally:
                    path.write_bytes(original)


if __name__ == "__main__":
    unittest.main()
