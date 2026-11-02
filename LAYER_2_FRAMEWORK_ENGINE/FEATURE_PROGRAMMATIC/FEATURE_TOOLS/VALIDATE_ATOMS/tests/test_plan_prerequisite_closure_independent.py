"""Finite reachable Plan evidence; no transitive authoring or whole-Project claim."""

from copy import deepcopy
import unittest
from unittest.mock import patch

import test_plan_blocking_reference_admission_independent as blocking
from contained_atom_targets import _bindings


class PlanPrerequisiteClosureIndependentTests(unittest.TestCase):
    def setUp(self):
        self.fixture = blocking.PlanBlockingReferenceAdmissionIndependentTests()
        self.fixture.setUp()
        self.addCleanup(self.fixture.doCleanups)

    def inventory(self, metadata=None, path="03_plan/proposed.md"):
        fixture = self.fixture.fixture
        _, roles, statuses = _bindings(fixture.context)
        metadata = self.fixture.metadata if metadata is None else metadata
        targets = list(dict.fromkeys(target for values in metadata["relations"].values() for target in values))
        return blocking.scoped.references.inventory_proposed_references(
            fixture.root, fixture.context.inputs["structure"], targets,
            admitted_role_folders=roles, admitted_status_folders=statuses,
            project_authority_paths=(fixture.control,), project_name="amber",
            candidate_metadata=metadata, candidate_path=fixture.control / path,
            admitted_plan_status_folders=statuses["Plan"],
        )

    def chain(self):
        self.fixture.target("Backlog", relations='{"blocks": ["CA-P-711"]}')
        self.fixture.target("Done", identifier="CA-P-711", filename="second.md",
                            relations='{"blocks": ["CA-P-712"]}')
        self.fixture.target("Canceled", identifier="CA-P-712", filename="third.md")
        self.fixture.target("Active", identifier="CA-P-799", filename="unrelated.md",
                            relations='{"blocks": ["CA-P-999999"]}')

    def test_inventory_captures_multihop_without_rewriting_or_claiming_unrelated_graph(self):
        self.chain()
        before = blocking.scoped.fixtures.snapshot(self.fixture.fixture.root)
        authored = deepcopy(self.fixture.metadata)
        result = self.inventory()
        self.assertEqual([row.atom_id for row in result.direct_targets], ["CA-P-710"])
        identifiers = [row.atom_id for row in result.plan_prerequisite_closure]
        self.assertTrue({"CA-P-711", "CA-P-712"}.issubset(identifiers))
        self.assertEqual(len(identifiers), len(set(identifiers)))
        self.assertNotIn("CA-P-799", identifiers)
        self.assertNotIn("CA-P-999999", identifiers)
        self.assertNotIn(self.fixture.metadata["atom_id"], identifiers)
        self.assertEqual(result.plan_parent_closure, ())
        self.assertEqual(self.fixture.metadata, authored)
        self.assertEqual(blocking.scoped.fixtures.snapshot(self.fixture.fixture.root), before)

    def test_complete_carrier_admits_the_same_finite_multihop_graph(self):
        self.chain()
        result = self.fixture.validate()
        self.assertEqual((result["findings"], result["gaps"]), ([], []))
        self.assertEqual(result["reference_scope"]["extent"], "finite-proposed-carrier")
        self.assertEqual(result["reference_scope"]["direct_targets"], ["CA-P-710"])

    def test_inventory_default_preserves_existing_two_field_construction(self):
        result = blocking.scoped.references.ProposedReferenceInventory((), ())
        self.assertEqual(result.plan_prerequisite_closure, ())

    def test_shared_reachable_endpoint_is_authenticated_once(self):
        self.fixture.target("Backlog", relations='{"blocks": ["CA-P-711", "CA-P-712"]}')
        self.fixture.target("Done", identifier="CA-P-711", filename="left.md",
                            relations='{"blocks": ["CA-P-713"]}')
        self.fixture.target("Canceled", identifier="CA-P-712", filename="right.md",
                            relations='{"blocks": ["CA-P-713"]}')
        self.fixture.target("Archived", identifier="CA-P-713", filename="leaf@1.md")
        result = self.inventory()
        self.assertEqual({row.atom_id for row in result.plan_prerequisite_closure},
                         {"CA-P-711", "CA-P-712", "CA-P-713"})
        self.assertEqual(len(result.plan_prerequisite_closure), 3)
        admitted = self.fixture.validate()
        self.assertEqual((admitted["findings"], admitted["gaps"]), ([], []))

    def test_blocking_child_parent_and_parent_blocks_are_prerequisites_not_candidate_placement(self):
        self.fixture.target("Active", identifier="CA-P-730", filename="parent.md",
                            relations='{"blocks": ["CA-P-711"]}')
        self.fixture.target("Done", identifier="CA-P-711", filename="leaf.md")
        target = self.fixture.target("Backlog", relations='{"is_decomposition_of": ["CA-P-730"]}')
        self.fixture.fixture.fixture.put(self.fixture.fixture.control / "03_plan/parent/001_backlog/target.md",
                                         target.read_bytes())
        target.unlink()
        result = self.inventory()
        self.assertEqual([row.atom_id for row in result.direct_targets], ["CA-P-710"])
        self.assertEqual(result.plan_parent_closure, ())
        self.assertEqual({row.atom_id for row in result.plan_prerequisite_closure},
                         {"CA-P-730", "CA-P-711"})
        admitted = self.fixture.validate()
        self.assertEqual((admitted["findings"], admitted["gaps"]), ([], []))

    def test_reachable_plan_history_selects_current_backlog_and_ignores_older_relations(self):
        self.fixture.target("Active", relations='{"blocks": ["CA-P-711"]}')
        current = self.fixture.target("Backlog", identifier="CA-P-711", version=2, filename="current.md")
        old = self.fixture.target("Active", identifier="CA-P-711", version=1, filename="old.md",
                                 relations='{"blocks": ["CA-P-999999"]}')
        self.fixture.fixture.fixture.put(self.fixture.fixture.control / "03_plan/archived/current@1.md",
                                         old.read_bytes())
        old.unlink()
        before = blocking.scoped.fixtures.snapshot(self.fixture.fixture.root)
        result = self.inventory()
        self.assertEqual([(row.atom_id, row.status, row.version) for row in result.plan_prerequisite_closure],
                         [("CA-P-711", "Backlog", 2)])
        admitted = self.fixture.validate()
        self.assertEqual((admitted["findings"], admitted["gaps"]), ([], []))
        self.assertEqual(blocking.scoped.fixtures.snapshot(self.fixture.fixture.root), before)
        current.unlink()
        with self.assertRaises(blocking.scoped.references.ProposedReferenceError):
            self.inventory()

    def test_reachable_missing_wrong_role_and_wrong_plan_type_refuse(self):
        root_target = self.fixture.target("Active", relations='{"blocks": ["CA-P-711"]}')
        with self.assertRaises(blocking.scoped.references.ProposedReferenceError):
            self.inventory()
        target = self.fixture.target("Active", identifier="CA-P-711", filename="second.md")
        raw = target.read_bytes()
        for before, after in ((b"content_role: Plan", b"content_role: Operations"),
                              (b"type: Plan", b"type: Action"),
                              (b"current_scope_unit: amber", b"current_scope_unit: OTHER"),
                              (b"status: Active", b"status: Backlog")):
            with self.subTest(after=after):
                target.write_bytes(raw.replace(before, after))
                with self.assertRaises(blocking.scoped.references.ProposedReferenceError):
                    self.inventory()
        target.write_bytes(raw)
        root_target.write_bytes(root_target.read_bytes().replace(b"CA-P-711", b"CA-O-702"))
        with self.assertRaises(blocking.scoped.references.ProposedReferenceError):
            self.inventory()

    def test_reachable_ambiguous_and_conflicting_revisions_refuse(self):
        self.fixture.target("Active", relations='{"blocks": ["CA-P-711"]}')
        self.fixture.target("Backlog", identifier="CA-P-711", version=2, filename="second.md")
        for status, version, filename in (("Backlog", 2, "duplicate.md"),
                                          ("Done", 3, "other.md"),
                                          ("Archived", 3, "later@3.md"),
                                          ("Archived", 1, "bad@2.md")):
            with self.subTest(filename=filename):
                competing = self.fixture.target(status, identifier="CA-P-711", version=version,
                                                filename=filename)
                with self.assertRaises(blocking.scoped.references.ProposedReferenceError):
                    self.inventory()
                competing.unlink()

    def test_reachable_malformed_relations_refuse_as_controlled_errors(self):
        self.fixture.target("Active", relations='{"blocks": ["CA-P-711"]}')
        target = self.fixture.target("Done", identifier="CA-P-711", filename="second.md")
        raw = target.read_bytes()
        for relations in ('{"blocks": "CA-P-712"}', '{"blocks": ["CA-P-712", "CA-P-712"]}',
                          '{"is_decomposition_of": ["CA-P-712", "CA-P-713"]}',
                          '{"blocks": [null]}'):
            with self.subTest(relations=relations):
                target.write_bytes(raw.replace(b"relations: {}", f"relations: {relations}".encode()))
                with self.assertRaises(blocking.scoped.references.ProposedReferenceError):
                    self.inventory()

    def test_block_cycle_inventory_is_finite_and_carrier_refuses_cycle(self):
        self.fixture.target("Active", relations='{"blocks": ["CA-P-711"]}')
        self.fixture.target("Done", identifier="CA-P-711", filename="second.md",
                            relations='{"blocks": ["CA-P-710"]}')
        result = self.inventory()
        self.assertEqual([row.atom_id for row in result.plan_prerequisite_closure], ["CA-P-711"])
        with self.assertRaises(blocking.scoped.admission.ProposedCarrierError):
            self.fixture.validate()

    def test_cycle_returning_to_candidate_refuses_without_candidate_carrier(self):
        self.fixture.target("Active", relations='{"blocks": ["CA-P-711"]}')
        self.fixture.target("Done", identifier="CA-P-711", filename="second.md",
                            relations='{"blocks": ["' + self.fixture.metadata["atom_id"] + '"]}')
        with self.assertRaises(blocking.scoped.admission.ProposedCarrierError):
            self.fixture.validate()

    def test_reachable_mixed_decomposition_and_block_cycle_refuses(self):
        self.fixture.target("Active", identifier="CA-P-730", filename="parent.md",
                            relations='{"blocks": ["CA-P-710"]}')
        self.fixture.target("Active", filename="parent/target.md",
                            relations='{"is_decomposition_of": ["CA-P-730"]}')
        result = self.inventory()
        self.assertEqual([row.atom_id for row in result.direct_targets], ["CA-P-710"])
        self.assertEqual([row.atom_id for row in result.plan_prerequisite_closure], ["CA-P-730"])
        self.assertEqual(result.plan_parent_closure, ())
        with self.assertRaises(blocking.scoped.admission.ProposedCarrierError):
            self.fixture.validate()

    def test_closure_does_not_relax_ordinary_active_reference_authority(self):
        self.chain()
        metadata = dict(self.fixture.metadata,
                        relations={"blocks": ["CA-P-710"], "depends_on": ["CA-P-711"]})
        with self.assertRaises(blocking.scoped.references.ProposedReferenceError):
            self.inventory(metadata)
        with self.assertRaises(blocking.scoped.admission.ProposedCarrierError):
            self.fixture.validate(metadata)

    def test_changed_reachable_carrier_refuses_currentness_check(self):
        self.chain()
        original = blocking.scoped.references._frontier
        calls = 0

        def changing_frontier(*args, **kwargs):
            nonlocal calls
            result = original(*args, **kwargs)
            calls += 1
            if calls == 1:
                target = self.fixture.fixture.root / self.fixture.fixture.control / "03_plan/done/second.md"
                target.write_bytes(target.read_bytes() + b"\nChanged reachable evidence.\n")
            return result

        with patch.object(blocking.scoped.references, "_frontier", changing_frontier):
            with self.assertRaises(blocking.scoped.references.ProposedReferenceError):
                self.inventory()
        self.assertGreaterEqual(calls, 2)

    def test_finite_frontier_limits_fail_closed(self):
        self.chain()
        for name, value in (("max_candidates", 1), ("max_total_read_bytes", 1), ("timeout_seconds", 0)):
            with self.subTest(limit=name):
                with patch.dict(blocking.scoped.references.CEILINGS, {name: value}):
                    with self.assertRaises(blocking.scoped.references.ProposedReferenceError):
                        self.inventory()


if __name__ == "__main__":
    unittest.main()
