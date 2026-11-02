"""Narrow request-context controls for the reused current Plan selector."""

from pathlib import Path
import unittest

import test_proposed_reference_scope_independent as scoped


class PlanBlockingReferenceAdmissionTests(unittest.TestCase):
    def setUp(self):
        self.fixture = scoped.ExplicitReferenceScopeIndependentTests()
        self.fixture.setUp()
        self.addCleanup(self.fixture.doCleanups)
        self.metadata = self.fixture.fixture.metadata(relations={"blocks": ["CA-P-710"]})
        sources = {row["binding"]["atom_id"]: row for row in self.fixture.context.inputs["sources"]}
        self.plans = scoped.admission._plan_mapping(sources["CA-D-461"]["text"])
        self.statuses = scoped.admission._frontier_status_folders(
            self.fixture.context, self.plans, self.fixture.status_index,
        )

    def plan(self, path, identity, status, parent=None):
        relations = "{}" if parent is None else f'{{"is_decomposition_of":["{parent}"]}}'
        return self.fixture.fixture.put(self.fixture.control / "03_plan" / path, (
            f"---\natom_id: {identity}\ncontent_role: Plan\ntype: Plan\ncurrent_scope_unit: amber\n"
            f"status: {status}\nversion: 1\nrelations: {relations}\n---\n# Summary\n\nEndpoint\n"
        ).encode())

    def inventory(self, metadata=None, *, plan_mapping=True, path="03_plan/proposed.md"):
        targets = tuple(dict.fromkeys(value for values in self.metadata["relations"].values() for value in values))
        return scoped.references.inventory_proposed_references(
            self.fixture.root, self.fixture.context.inputs["structure"], targets,
            admitted_role_folders={"Plan": "03_plan"}, admitted_status_folders={"Plan": self.statuses["Plan"]},
            project_authority_paths=(self.fixture.control,), project_name="amber",
            candidate_metadata=metadata, candidate_path=self.fixture.control / path,
            admitted_plan_status_folders=self.plans if plan_mapping else None,
        )

    def test_standalone_or_untyped_lookup_retains_active_only(self):
        self.plan(Path("001_backlog/target.md"), "CA-P-710", "Backlog")
        before = scoped.fixtures.snapshot(self.fixture.root)
        for candidate in (None, dict(self.metadata, type="Task")):
            with self.subTest(candidate=candidate):
                with self.assertRaises(scoped.references.ProposedReferenceError):
                    self.inventory(candidate)
        self.assertEqual(self.inventory(self.metadata).direct_targets[0].status, "Backlog")
        self.assertEqual(scoped.fixtures.snapshot(self.fixture.root), before)

    def test_blocking_lookup_requires_the_verified_plan_status_mapping(self):
        self.plan(Path("001_backlog/target.md"), "CA-P-710", "Backlog")
        with self.assertRaisesRegex(scoped.references.ProposedReferenceError, "status-directory authority"):
            self.inventory(self.metadata, plan_mapping=False)

    def test_blocking_endpoint_cannot_supply_inactive_indirect_decomposition_parent(self):
        self.plan(Path("001_backlog/grandparent.md"), "CA-P-710", "Backlog")
        self.plan(Path("001_backlog/grandparent/parent.md"), "CA-P-711", "Active", "CA-P-710")
        self.metadata["relations"]["is_decomposition_of"] = ["CA-P-711"]
        before = scoped.fixtures.snapshot(self.fixture.root)
        with self.assertRaisesRegex(scoped.references.ProposedReferenceError, "Plan parent is missing, inactive"):
            self.inventory(self.metadata, path="03_plan/001_backlog/grandparent/parent/proposed.md")
        self.assertEqual(scoped.fixtures.snapshot(self.fixture.root), before)


if __name__ == "__main__":
    unittest.main()
