"""Author checks for finite prerequisite evidence on the existing read frontier."""

from copy import deepcopy
import unittest

import test_proposed_references as fixture


class PlanPrerequisiteClosureTests(unittest.TestCase):
    def setUp(self):
        self.fixture = fixture.ProposedReferenceInventoryTest()
        self.fixture.setUp()
        self.addCleanup(self.fixture.tearDown)
        self.metadata = {
            "atom_id": "CA-P-CANDIDATE", "content_role": "Plan", "type": "Plan",
            "status": "Active", "relations": {"blocks": ["CA-P-FIRST"]},
        }

    def plan(self, name, identity, *, status="Active", version=1, relations=None):
        folder = fixture.STATUS_FOLDERS["Plan"][status]
        path = self.fixture._carrier(
            "/".join(part for part in ("authority/03_plan", folder, name) if part),
            identity, role="Plan", status=status, version=version,
        )
        if relations is not None:
            import json
            path.write_text(path.read_text().replace(
                "  is_decomposition_of: []", "  blocks: " + json.dumps(relations),
            ))
        return path

    def inventory(self, metadata=None):
        metadata = self.metadata if metadata is None else metadata
        return fixture.inventory_proposed_references(
            self.fixture.root, self.fixture.structure, ["CA-P-FIRST"],
            candidate_metadata=metadata,
            admitted_plan_status_folders=fixture.STATUS_FOLDERS["Plan"],
        )

    def test_reachable_current_statuses_are_retained_without_transitive_authoring(self):
        self.plan("first.md", "CA-P-FIRST", status="Backlog", relations=["CA-P-SECOND"])
        self.plan("second.md", "CA-P-SECOND", status="Done", relations=["CA-P-THIRD"])
        self.plan("third.md", "CA-P-THIRD", status="Canceled")
        self.plan("unrelated.md", "CA-P-UNRELATED", relations=["CA-P-MISSING"])
        authored = deepcopy(self.metadata)
        result = self.inventory()
        self.assertEqual([row.atom_id for row in result.direct_targets], ["CA-P-FIRST"])
        self.assertEqual([(row.atom_id, row.status) for row in result.plan_prerequisite_closure],
                         [("CA-P-SECOND", "Done"), ("CA-P-THIRD", "Canceled")])
        self.assertEqual(result.plan_parent_closure, ())
        self.assertEqual(self.metadata, authored)
        self.assertEqual(result.direct_targets[0].metadata["relations"], {"blocks": ["CA-P-SECOND"]})

    def test_shared_endpoint_is_deduplicated(self):
        self.plan("first.md", "CA-P-FIRST", relations=["CA-P-SECOND", "CA-P-THIRD"])
        self.plan("second.md", "CA-P-SECOND", relations=["CA-P-THIRD"])
        self.plan("third.md", "CA-P-THIRD")
        ids = [row.atom_id for row in self.inventory().plan_prerequisite_closure]
        self.assertEqual(set(ids), {"CA-P-SECOND", "CA-P-THIRD"})
        self.assertEqual(len(ids), 2)

    def test_reachability_requires_typed_candidate_with_blocks(self):
        self.plan("first.md", "CA-P-FIRST", relations=["CA-P-MISSING"])
        for metadata in (None, dict(self.metadata, type="Task"),
                         dict(self.metadata, relations={"depends_on": ["CA-P-FIRST"]})):
            with self.subTest(metadata=metadata):
                result = fixture.inventory_proposed_references(
                    self.fixture.root, self.fixture.structure, ["CA-P-FIRST"],
                    candidate_metadata=metadata,
                )
                self.assertEqual(result.plan_prerequisite_closure, ())

    def test_reachable_historical_revision_does_not_replace_current(self):
        self.plan("first.md", "CA-P-FIRST", relations=["CA-P-SECOND"])
        self.plan("second.md", "CA-P-SECOND", status="Done", version=2)
        old = self.plan("second@1.md", "CA-P-SECOND", status="Archived")
        old.write_text(old.read_text().replace("status: Archived", "status: Active"))
        result = self.inventory()
        self.assertEqual([(row.atom_id, row.version, row.status) for row in result.plan_prerequisite_closure],
                         [("CA-P-SECOND", 2, "Done")])

    def test_missing_reachable_plan_refuses(self):
        self.plan("first.md", "CA-P-FIRST", relations=["CA-P-MISSING"])
        with self.assertRaisesRegex(fixture.ProposedReferenceError, "current Revision is unresolved"):
            self.inventory()

    def test_reachable_malformed_relation_refuses(self):
        path = self.plan("first.md", "CA-P-FIRST", relations=["CA-P-SECOND"])
        path.write_text(path.read_text().replace('["CA-P-SECOND"]', "CA-P-SECOND"))
        with self.assertRaisesRegex(fixture.ProposedReferenceError, "blocks relation is malformed"):
            self.inventory()

    def test_cycle_evidence_is_finite_and_omits_candidate_record(self):
        self.plan("first.md", "CA-P-FIRST", relations=["CA-P-SECOND"])
        self.plan("second.md", "CA-P-SECOND", relations=["CA-P-CANDIDATE", "CA-P-FIRST"])
        result = self.inventory()
        self.assertEqual([row.atom_id for row in result.plan_prerequisite_closure], ["CA-P-SECOND"])


if __name__ == "__main__":
    unittest.main()
