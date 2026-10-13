"""Independent literal containment controls; not cascade or runtime evidence."""

from contextlib import ExitStack
import hashlib
import os
from pathlib import Path
import sys
import unittest
from unittest.mock import patch

TOOLS = Path(__file__).resolve().parents[1]
sys.path[:0] = [str(TOOLS), str(TOOLS / "VALIDATE_ATOMS/tests")]

import test_proposed_reference_scope as admitted_fixtures
from contained_atom_targets import ContainedAtomTargetsError, discover_contained_atom_targets
from VALIDATE_ATOMS.validate_atoms_workers.read_io import ReadContext


def carrier(atom_id, *, role="Plan", kind="Plan", status="Active", version=1, parent=None):
    relation = "{}" if parent is None else "{is_decomposition_of: [" + parent + "]}"
    return (
        f"---\natom_id: {atom_id}\ncontent_role: {role}\ntype: {kind}\n"
        f"current_scope_unit: amber\nstatus: {status}\nversion: {version}\n"
        f"relations: {relation}\n---\n# Summary\n\nLiteral fixture.\n"
        "\n## Details\n\n### Definition of Done\n\nIndependent checks pass.\n"
    ).encode()


def snapshot(root):
    result = {}
    for path in root.rglob("*"):
        stat = path.lstat()
        result[path.relative_to(root).as_posix()] = (
            "directory" if path.is_dir() else path.read_bytes(),
            stat.st_ino, stat.st_mode, stat.st_mtime_ns,
        )
    return result


class ContainedAtomTargetsIndependentTests(unittest.TestCase):
    def setUp(self):
        self.fixture = admitted_fixtures.ProposedReferenceScopeTests()
        self.fixture.setUp()
        self.addCleanup(self.fixture.doCleanups)
        self.root, self.control, self.context = (
            self.fixture.root, self.fixture.control, self.fixture.context,
        )
        self.inputs = {}

    def put(self, relative, raw):
        path = self.fixture.fixture.put(self.control / relative, raw)
        self.inputs[path] = raw
        return path

    def discover(self, path, atom_id, **changes):
        options = {"expected_version": 1, "expected_sha256": hashlib.sha256(self.inputs[path]).hexdigest()}
        options.update(changes)
        return discover_contained_atom_targets(self.context, atom_id, **options)

    def assert_read_only(self, call):
        before = snapshot(self.root)
        real_open = os.open

        def read_only_open(path, flags, *args, **kwargs):
            if flags & (os.O_WRONLY | os.O_RDWR | os.O_CREAT | os.O_TRUNC):
                raise AssertionError("Discovery attempted a writable open")
            return real_open(path, flags, *args, **kwargs)

        with ExitStack() as stack:
            stack.enter_context(patch("os.open", side_effect=read_only_open))
            for name in ("replace", "rename", "unlink", "remove", "mkdir", "rmdir", "chmod"):
                stack.enter_context(patch("os." + name, side_effect=AssertionError("Discovery attempted " + name)))
            result = call()
        self.assertEqual(snapshot(self.root), before)
        return result

    def assert_refused(self, call):
        before = snapshot(self.root)
        with self.assertRaises(ContainedAtomTargetsError):
            call()
        self.assertEqual(snapshot(self.root), before)

    def row(self, item):
        return (item.atom_id, item.content_role, item.atom_type, item.status, item.version,
                item.path, item.parent_atom_id, item.container_path, item.directory_path)

    def test_nested_plans_keep_direct_containers_and_stored_statuses(self):
        parent = self.put(Path("03_plan/01-CA-P-701-EPIC--parent.md"), carrier("CA-P-701"))
        tree = parent.with_suffix("").relative_to(self.root / self.control)
        child = self.put(tree / "02-CA-P-702-TASK--child.md", carrier("CA-P-702", parent="CA-P-701"))
        grandchild = self.put(tree / "02-CA-P-702-TASK--child/done/03-CA-P-703-TASK--grandchild.md",
                              carrier("CA-P-703", parent="CA-P-702", status="Done", version=4))
        sibling = self.put(tree / "done/04-CA-P-704-TASK--sibling.md",
                           carrier("CA-P-704", parent="CA-P-701", status="Done", version=2))
        inventory = self.assert_read_only(lambda: self.discover(parent, "CA-P-701"))
        root_container = parent.with_suffix("").relative_to(self.root).as_posix()
        child_container = child.with_suffix("").relative_to(self.root).as_posix()
        self.assertEqual([self.row(item) for item in inventory.targets], [
            ("CA-P-702", "Plan", "Plan", "Active", 1, child.relative_to(self.root).as_posix(),
             "CA-P-701", root_container, child_container),
            ("CA-P-703", "Plan", "Plan", "Done", 4, grandchild.relative_to(self.root).as_posix(),
             "CA-P-702", child_container, None),
            ("CA-P-704", "Plan", "Plan", "Done", 2, sibling.relative_to(self.root).as_posix(),
             "CA-P-701", root_container, None),
        ])
        self.assertEqual(inventory.parent.atom_id, "CA-P-701")
        for item in inventory.targets:
            self.assertEqual(item.sha256, hashlib.sha256(self.inputs[self.root / item.path]).hexdigest())

    def test_workflow_steps_and_substeps_not_outside_references(self):
        raw = carrier("CA-O-701", role="Operations", kind="Workflow").replace(
            b"relations: {}", b"relations: {depends_on: [CA-O-704]}"
        )
        parent = self.put(Path("09_operations/CA-O-701--workflow.md"), raw)
        tree = Path("09_operations/CA-O-701--workflow")
        first = self.put(tree / "CA-O-702--step.md", carrier("CA-O-702", role="Operations", kind="Step"))
        second = self.put(tree / "CA-O-702--step/CA-O-703--substep.md",
                          carrier("CA-O-703", role="Operations", kind="Step", version=5))
        self.put(Path("09_operations/CA-O-704--outside-step.md"),
                 carrier("CA-O-704", role="Operations", kind="Step"))
        inventory = self.assert_read_only(lambda: self.discover(parent, "CA-O-701"))
        self.assertEqual([(x.atom_id, x.parent_atom_id, x.path) for x in inventory.targets], [
            ("CA-O-702", "CA-O-701", first.relative_to(self.root).as_posix()),
            ("CA-O-703", "CA-O-702", second.relative_to(self.root).as_posix()),
        ])
        self.assertEqual(inventory.targets[0].directory_path, first.with_suffix("").relative_to(self.root).as_posix())
        self.assertIsNone(inventory.targets[1].directory_path)
        nested = self.assert_read_only(lambda: self.discover(first, "CA-O-702"))
        self.assertEqual([(x.atom_id, x.parent_atom_id) for x in nested.targets], [("CA-O-703", "CA-O-702")])

    def test_file_only_and_empty_matching_directory_have_no_children(self):
        parent = self.put(Path("03_plan/01-CA-P-701-TASK--empty.md"), carrier("CA-P-701"))
        for directory in (False, True):
            if directory:
                parent.with_suffix("").mkdir()
            with self.subTest(directory=directory):
                result = self.assert_read_only(lambda: self.discover(parent, "CA-P-701"))
                self.assertEqual(result.targets, ())

    def test_latest_current_only_and_older_canonical_history_excluded(self):
        parent = self.put(Path("03_plan/01-CA-P-701-EPIC--parent.md"), carrier("CA-P-701"))
        tree = Path("03_plan/01-CA-P-701-EPIC--parent")
        self.put(tree / "02-CA-P-702-TASK--current.md", carrier("CA-P-702", version=3, parent="CA-P-701"))
        self.put(tree / "archived/02-CA-P-702-TASK--current@1.md",
                 carrier("CA-P-702", version=1, parent="CA-P-701", status="Archived"))
        self.put(tree / "archived/03-CA-P-703-TASK--archived@4.md",
                 carrier("CA-P-703", version=4, parent="CA-P-701", status="Archived"))
        self.put(tree / "archived/03-CA-P-703-TASK--archived@2.md",
                 carrier("CA-P-703", version=2, parent="CA-P-701", status="Archived"))
        self.put(tree / "archive/legacy.md", b"historical legacy without frontmatter\n")
        result = self.assert_read_only(lambda: self.discover(parent, "CA-P-701"))
        self.assertEqual([(x.atom_id, x.version, x.status) for x in result.targets], [
            ("CA-P-702", 3, "Active"), ("CA-P-703", 4, "Archived"),
        ])

    def test_duplicate_current_identity_refuses_inside_and_outside_tree(self):
        parent = self.put(Path("03_plan/01-CA-P-701-EPIC--parent.md"), carrier("CA-P-701"))
        tree = Path("03_plan/01-CA-P-701-EPIC--parent")
        child = self.put(tree / "02-CA-P-702-TASK--child.md", carrier("CA-P-702", parent="CA-P-701"))
        for duplicate in (tree / "03-CA-P-702-TASK--duplicate.md", Path("03_plan/04-CA-P-702-TASK--outside.md")):
            path = self.put(duplicate, self.inputs[child].replace(b"version: 1", b"version: 2"))
            try:
                with self.subTest(duplicate=duplicate):
                    self.assert_refused(lambda: self.discover(parent, "CA-P-701"))
            finally:
                path.unlink()

    def test_archived_parent_does_not_override_child_currentness_or_status(self):
        parent = self.put(Path("03_plan/archived/01-CA-P-701-EPIC--parent@4.md"),
                          carrier("CA-P-701", status="Archived", version=4))
        self.put(Path("03_plan/archived/01-CA-P-701-EPIC--parent@4/02-CA-P-702-TASK--child.md"),
                 carrier("CA-P-702", parent="CA-P-701", version=3))
        result = self.assert_read_only(lambda: self.discover(parent, "CA-P-701", expected_version=4))
        self.assertEqual([(x.atom_id, x.status, x.version) for x in result.targets], [("CA-P-702", "Active", 3)])

    def test_malformed_child_and_unadmitted_parent_refuse(self):
        parent = self.put(Path("03_plan/01-CA-P-701-EPIC--parent.md"), carrier("CA-P-701"))
        malformed = self.put(Path("03_plan/01-CA-P-701-EPIC--parent/02-CA-P-702-TASK--child.md"),
                             b"---\natom_id: [unterminated\n---\n")
        self.assert_refused(lambda: self.discover(parent, "CA-P-701"))
        malformed.unlink()
        action = self.put(Path("09_operations/CA-O-705--action.md"), carrier("CA-O-705", role="Operations", kind="Action"))
        self.assert_refused(lambda: self.discover(action, "CA-O-705"))

    def test_orphan_matching_directory_is_not_an_empty_admitted_tree(self):
        parent = self.put(Path("03_plan/01-CA-P-701-EPIC--parent.md"), carrier("CA-P-701"))
        self.put(Path("03_plan/01-CA-P-701-EPIC--parent/02-CA-P-702-TASK--missing/03-CA-P-703-TASK--child.md"),
                 carrier("CA-P-703", parent="CA-P-702"))
        self.assert_refused(lambda: self.discover(parent, "CA-P-701"))

    def test_unadmitted_newer_outside_carrier_cannot_hide_contained_history(self):
        parent = self.put(Path("03_plan/01-CA-P-701-EPIC--parent.md"), carrier("CA-P-701"))
        self.put(Path("03_plan/01-CA-P-701-EPIC--parent/archived/02-CA-P-702-TASK--child@1.md"),
                 carrier("CA-P-702", parent="CA-P-701", status="Archived"))
        raw = carrier("CA-P-702", version=2).replace(b"current_scope_unit: amber", b"current_scope_unit: unadmitted")
        self.put(Path("03_plan/03-CA-P-702-TASK--wrong-owner.md"), raw)
        self.assert_refused(lambda: self.discover(parent, "CA-P-701"))

    def test_stale_parent_expected_state_and_selected_context_refuse(self):
        parent = self.put(Path("03_plan/01-CA-P-701-TASK--empty.md"), carrier("CA-P-701"))
        for change in ({"expected_version": 2}, {"expected_sha256": "0" * 64}):
            with self.subTest(change=change):
                self.assert_refused(lambda: self.discover(parent, "CA-P-701", **change))
        settings = self.fixture.selection.settings_path
        settings.write_bytes(settings.read_bytes() + b"\n# independently stale context\n")
        self.assert_refused(lambda: self.discover(parent, "CA-P-701"))

    def test_actual_mid_discovery_change_refuses_without_additional_writes(self):
        parent = self.put(Path("03_plan/01-CA-P-701-EPIC--parent.md"), carrier("CA-P-701"))
        child = self.put(Path("03_plan/01-CA-P-701-EPIC--parent/02-CA-P-702-TASK--child.md"),
                         carrier("CA-P-702", parent="CA-P-701"))
        read = ReadContext.read
        changed = {}

        def introduce_change(reader, path, **options):
            raw = read(reader, path, **options)
            if Path(path) == child and not changed:
                child.write_bytes(raw.replace(b"version: 1", b"version: 2"))
                changed["snapshot"] = snapshot(self.root)
            return raw

        with patch.object(ReadContext, "read", introduce_change), self.assertRaises(ContainedAtomTargetsError):
            self.discover(parent, "CA-P-701")
        self.assertIn("snapshot", changed)
        self.assertEqual(snapshot(self.root), changed["snapshot"])


if __name__ == "__main__":
    unittest.main()
