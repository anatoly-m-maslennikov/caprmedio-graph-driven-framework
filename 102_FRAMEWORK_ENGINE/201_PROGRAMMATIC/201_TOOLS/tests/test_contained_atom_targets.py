"""Author tests for private admitted P/O containment discovery."""

import hashlib
from pathlib import Path
import sys
import unittest
from unittest.mock import patch

TOOLS = Path(__file__).resolve().parents[1]
sys.path[:0] = [str(TOOLS), str(TOOLS / "VALIDATE_ATOMS/tests")]

import test_proposed_reference_scope as fixtures
import contained_atom_targets as subject


class ContainedAtomTargetsTests(unittest.TestCase):
    def setUp(self):
        self.fixture = fixtures.ProposedReferenceScopeTests()
        self.fixture.setUp()
        self.addCleanup(self.fixture.doCleanups)
        self.context = self.fixture.context
        self.root = self.fixture.root
        self.control = self.fixture.control
        self.parent = self.put("03_plan/parent.md", "CA-P-900")

    def put(self, relative, identity, *, role="Plan", kind="Plan", status="Active", version=1, parent=None):
        relations = "{}" if parent is None else "{is_decomposition_of: [" + parent + "]}"
        return self.fixture.fixture.put(self.control / relative, (
            f"---\natom_id: {identity}\ncontent_role: {role}\ntype: {kind}\n"
            f"current_scope_unit: amber\nstatus: {status}\nversion: {version}\n"
            f"relations: {relations}\n---\n# Summary\n\nFixture.\n"
        ).encode())

    def discover(self, path=None, identity="CA-P-900", version=1):
        path = self.parent if path is None else path
        return subject.discover_contained_atom_targets(
            self.context, identity, expected_version=version,
            expected_sha256=hashlib.sha256(path.read_bytes()).hexdigest(),
        )

    def test_nested_plans_all_statuses_and_stable_tree_order(self):
        child = self.put("03_plan/parent/done/child.md", "CA-P-901", status="Done", parent="CA-P-900")
        self.put("03_plan/parent/done/child/001_backlog/grandchild.md", "CA-P-902", status="Backlog", parent="CA-P-901")
        self.put("03_plan/parent/other.md", "CA-P-903", parent="CA-P-900")
        before = fixtures.fixtures.snapshot(self.root)
        result = self.discover()
        self.assertEqual(["CA-P-901", "CA-P-902", "CA-P-903"], [r.atom_id for r in result.targets])
        self.assertEqual(["Done", "Backlog", "Active"], [r.status for r in result.targets])
        self.assertEqual("CA-P-901", result.targets[1].parent_atom_id)
        self.assertEqual(str(child.with_suffix("").relative_to(self.root)), result.targets[1].container_path)
        self.assertEqual(result, self.discover())
        self.assertEqual(before, fixtures.fixtures.snapshot(self.root))

    def test_workflow_steps_and_substeps_do_not_follow_outside_references(self):
        workflow = self.put("09_operations/workflow.md", "CA-O-900", role="Operations", kind="Workflow")
        self.put("09_operations/workflow/step.md", "CA-O-902", role="Operations", kind="Step")
        self.put("09_operations/workflow/step/draft/substep.md", "CA-O-903", role="Operations", kind="Step", status="Draft")
        self.put("09_operations/outside.md", "CA-O-904", role="Operations", kind="Step")
        self.assertEqual(["CA-O-902", "CA-O-903"], [r.atom_id for r in self.discover(workflow, "CA-O-900").targets])

    def test_empty_parent(self):
        self.assertEqual((), self.discover().targets)

    def test_latest_canonical_history_and_legacy_archive_exclusion(self):
        self.put("03_plan/parent/child.md", "CA-P-901", version=3, parent="CA-P-900")
        self.put("03_plan/parent/archived/child@1.md", "CA-P-901", version=1, parent="CA-P-900")
        self.put("03_plan/parent/archived/retired@2.md", "CA-P-902", version=2, status="Archived", parent="CA-P-900")
        self.put("03_plan/parent/archived/retired@4.md", "CA-P-902", version=4, status="Archived", parent="CA-P-900")
        self.fixture.fixture.put(self.control / "03_plan/parent/archive/broken.md", b"not a carrier")
        self.assertEqual({("CA-P-901", 3), ("CA-P-902", 4)}, {(r.atom_id, r.version) for r in self.discover().targets})

    def test_duplicate_current_and_same_version_refuse(self):
        self.put("03_plan/parent/child.md", "CA-P-901", parent="CA-P-900")
        extra = self.put("03_plan/outside.md", "CA-P-901", version=2)
        with self.assertRaises(subject.ContainedAtomTargetsError):
            self.discover()
        extra.unlink()
        self.put("03_plan/parent/archived/child@1.md", "CA-P-901", parent="CA-P-900")
        with self.assertRaises(subject.ContainedAtomTargetsError):
            self.discover()

    def test_old_archived_bundle_children_are_history_not_current_duplicates(self):
        self.put("03_plan/parent/archived/child@2.md", "CA-P-901", version=2, status="Archived", parent="CA-P-900")
        self.put("03_plan/parent/archived/child@4.md", "CA-P-901", version=4, status="Archived", parent="CA-P-900")
        self.put("03_plan/parent/archived/child@2/grandchild.md", "CA-P-902", version=1, parent="CA-P-901")
        self.put("03_plan/parent/archived/child@4/grandchild.md", "CA-P-902", version=1, parent="CA-P-901")
        self.assertEqual(["CA-P-901", "CA-P-902"], [r.atom_id for r in self.discover().targets])

    def test_unadmitted_newer_carrier_cannot_retire_a_contained_bundle(self):
        self.put("03_plan/parent/archived/child@2.md", "CA-P-901", version=2, status="Archived", parent="CA-P-900")
        self.put("03_plan/parent/archived/child@2/grandchild.md", "CA-P-902", parent="CA-P-901")
        competitor = self.put("03_plan/outside.md", "CA-P-901", version=4)
        raw = competitor.read_bytes()
        for old, new in ((b"current_scope_unit: amber", b"current_scope_unit: unadmitted"),
                         (b"status: Active", b"status: Done"),
                         (b"type: Plan", b"type: Action")):
            with self.subTest(field=old):
                competitor.write_bytes(raw.replace(old, new))
                before = fixtures.fixtures.snapshot(self.root)
                with self.assertRaises(subject.ContainedAtomTargetsError):
                    self.discover()
                self.assertEqual(before, fixtures.fixtures.snapshot(self.root))

    def test_malformed_or_unsupported_contained_placement_refuses(self):
        wrong = self.put("03_plan/parent/child.md", "CA-P-901", status="Done", parent="CA-P-900")
        with self.assertRaises(subject.ContainedAtomTargetsError):
            self.discover()
        wrong.write_bytes(b"---\natom_id: [broken\n---\n")
        with self.assertRaises(subject.ContainedAtomTargetsError):
            self.discover()

    def test_parent_expected_state_and_source_context_stale_refuse(self):
        with self.assertRaises(subject.ContainedAtomTargetsError):
            self.discover(version=2)
        self.context._selection.structure_path.write_text("changed")
        with self.assertRaises(subject.ContainedAtomTargetsError):
            self.discover()

    def test_frontier_changed_during_discovery_refuses(self):
        real = subject._frontier
        calls = 0

        def changing(*args):
            nonlocal calls
            result = real(*args)
            calls += 1
            if calls == 1:
                self.put("03_plan/parent/late.md", "CA-P-901", parent="CA-P-900")
            return result

        with patch.object(subject, "_frontier", changing), self.assertRaises(subject.ContainedAtomTargetsError):
            self.discover()


if __name__ == "__main__":
    unittest.main()
