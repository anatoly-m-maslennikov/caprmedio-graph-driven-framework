"""One real identified-Atom status publication, not cascade/Run acceptance."""
from pathlib import Path
import sys
import unittest
from unittest.mock import patch
import yaml

TOOLS = Path(__file__).resolve().parents[1]
sys.path[:0] = [str(TOOLS), str(TOOLS / "VALIDATE_ATOMS/tests")]
import test_proposed_reference_scope as fixtures
from golden_authority import write_frozen_authority
from project_selection import bind_selection
import atom_operations as operations
import lifecycle_intents as lifecycle


class StatusBundlePublicationTests(unittest.TestCase):
    def setUp(self):
        self.fixture = fixtures.ProposedReferenceScopeTests()
        self.fixture.setUp()
        self.addCleanup(self.fixture.doCleanups)
        self.root, self.control = self.fixture.root, self.fixture.control
        write_frozen_authority(self.root, self.control, ("CA-D-289", "CA-D-378"))
        self.binding = bind_selection(self.fixture.selection)
        self.binding.__enter__()
        self.addCleanup(self.binding.__exit__, None, None, None)

    def put(self, relative, identity="CA-P-701", *, role="Plan", kind="Plan", status="Active", relations=None):
        metadata = self.fixture.fixture.metadata(atom_id=identity, content_role=role, type=kind,
                                                status=status, relations=relations or {})
        if role == "Operations":
            metadata.pop("label")
        body = fixtures.fixtures.PLAN_BODY if role == "Plan" else "# Summary\n\nFixture workflow.\n\n## Operation\n\nOne step.\n\n## Details\n\nFixture.\n"
        return self.fixture.fixture.put(self.control / relative,
            ("---\n" + yaml.safe_dump(metadata, sort_keys=False) + "---\n" + body).encode())

    def request(self, path, status):
        return {"target": lifecycle.carrier_descriptor(self.root, operations.atom_from_path(self.root, path)),
                "status": status}

    def execute(self, request):
        return lifecycle.change_status_atom_action(self.root, request, execute=True, authorized=True)

    def snapshot(self):
        return {p.relative_to(self.root): p.read_bytes() for p in (self.root / self.control).rglob("*") if p.is_file()}

    def test_plan_bundle_history_noop_and_local_reactivation(self):
        parent = self.put("03_plan/CA-P-701--parent.md")
        child = self.put("03_plan/CA-P-701--parent/CA-P-702--child.md", "CA-P-702",
                         relations={"is_decomposition_of": ["CA-P-701"]})
        original, child_raw = parent.read_bytes(), child.read_bytes()
        result = self.execute(self.request(parent, "Done"))
        current = self.root / result["observed"]["path"]
        self.assertEqual(self.root / self.control / "03_plan/done/CA-P-701--parent.md", current)
        self.assertEqual(original, (self.root / result["history"]["prior_revision"]["path"]).read_bytes())
        self.assertEqual(child_raw, (current.with_suffix("") / child.name).read_bytes())
        self.assertFalse(parent.exists())
        before = self.snapshot()
        self.assertEqual("no-op", self.execute(self.request(current, "Done"))["outcome"])
        self.assertEqual(before, self.snapshot())
        result = self.execute(self.request(current, "Active"))
        self.assertEqual(parent, self.root / result["observed"]["path"])
        self.assertEqual(3, result["observed"]["version"])
        self.assertEqual(child_raw, child.read_bytes())

    def test_archive_suffix_matches_new_version_and_matching_directory(self):
        parent = self.put("03_plan/CA-P-701--parent.md")
        self.fixture.fixture.put(self.control / "03_plan/CA-P-701--parent/archive/legacy.bin", b"old bytes")
        raw = parent.read_bytes()
        result = self.execute(self.request(parent, "Archived"))
        current = self.root / result["observed"]["path"]
        self.assertEqual("CA-P-701--parent@2.md", current.name)
        self.assertEqual(raw, current.with_name("CA-P-701--parent@1.md").read_bytes())
        self.assertEqual(b"old bytes", (current.with_suffix("") / "archive/legacy.bin").read_bytes())

    def test_nested_workflow_step_archive_stays_inside_container(self):
        workflow = self.put("09_operations/CA-O-701--workflow.md", "CA-O-701", role="Operations", kind="Workflow")
        step = self.put("09_operations/CA-O-701--workflow/CA-O-702--step.md", "CA-O-702", role="Operations", kind="Step")
        nested = self.fixture.fixture.put(self.control / "09_operations/CA-O-701--workflow/CA-O-702--step/archive/old.bin", b"history")
        workflow_raw, step_raw = workflow.read_bytes(), step.read_bytes()
        result = self.execute(self.request(step, "Archived"))
        current = self.root / result["observed"]["path"]
        self.assertEqual(workflow.with_suffix("") / "archived/CA-O-702--step@2.md", current)
        self.assertEqual(step_raw, current.with_name("CA-O-702--step@1.md").read_bytes())
        self.assertEqual(workflow_raw, workflow.read_bytes())
        self.assertEqual(b"history", (current.with_suffix("") / "archive/old.bin").read_bytes())
        self.assertFalse(nested.exists())

    def test_stale_markdown_and_symlink_bundle_refuse(self):
        parent = self.put("03_plan/CA-P-701--parent.md")
        request = self.request(parent, "Done")
        parent.write_bytes(parent.read_bytes() + b"\nchanged\n")
        with self.assertRaises(lifecycle.LifecycleError):
            self.execute(request)
        parent.with_suffix("").symlink_to(parent.parent, target_is_directory=True)
        with self.assertRaises(operations.ToolError):
            self.execute(self.request(parent, "Done"))

    def test_destination_collision_and_stale_bundle_refuse(self):
        parent = self.put("03_plan/CA-P-701--parent.md")
        occupied = self.root / self.control / "03_plan/done/CA-P-701--parent"
        occupied.mkdir(parents=True)
        request = self.request(parent, "Done")
        before = self.snapshot()
        with self.assertRaises(lifecycle.LifecycleError):
            self.execute(request)
        self.assertEqual(before, self.snapshot())
        occupied.rmdir()
        allowed = lifecycle._execute_allowed
        def mutate(**kwargs):
            self.fixture.fixture.put(self.control / "03_plan/CA-P-701--parent/late.bin", b"late")
            return allowed(**kwargs)
        with patch.object(lifecycle, "_execute_allowed", side_effect=mutate), self.assertRaises(lifecycle.LifecycleError):
            self.execute(request)
        self.assertTrue(parent.exists())

    def test_failed_verification_restores_own_effect(self):
        parent = self.put("03_plan/CA-P-701--parent.md")
        child = self.fixture.fixture.put(self.control / "03_plan/CA-P-701--parent/asset.bin", b"unchanged")
        before = self.snapshot()
        parse = operations.atom_from_path
        def fail(root, path):
            if path.parent.name == "done":
                raise operations.ToolError("injected", "post-publication verification failure")
            return parse(root, path)
        with patch.object(operations, "atom_from_path", side_effect=fail), self.assertRaises(lifecycle.LifecycleError):
            self.execute(self.request(parent, "Done"))
        self.assertEqual(before, self.snapshot())
        self.assertEqual(b"unchanged", child.read_bytes())

    def test_staging_cleanup_failure_after_history_link_restores_published_history(self):
        parent = self.put("03_plan/CA-P-701--parent.md")
        before = self.snapshot()
        unlink = operations.os.unlink
        failed = False
        def fail_once(path, *args, **kwargs):
            nonlocal failed
            if str(path).startswith(".subject-") and not failed:
                failed = True
                raise OSError("injected staging cleanup failure after publication")
            return unlink(path, *args, **kwargs)
        with patch.object(operations.os, "unlink", side_effect=fail_once), self.assertRaises(lifecycle.LifecycleError):
            self.execute(self.request(parent, "Done"))
        self.assertTrue(failed)
        self.assertEqual(before, self.snapshot())

    def test_post_rename_stat_failure_recovers_or_retains_uncertain_bundle(self):
        for persistent in (False, True):
            with self.subTest(persistent=persistent):
                identity = "CA-P-702" if persistent else "CA-P-701"
                parent = self.put(f"03_plan/{identity}--parent.md", identity)
                child = parent.with_suffix("") / "asset.bin"
                child.parent.mkdir()
                child.write_bytes(b"exact descendant")
                destination = parent.parent / "done" / parent.name
                destination_directory = destination.with_suffix("")
                before = self.snapshot()
                rename, stat = Path.rename, Path.stat
                moved = failed = False
                def observe_rename(path, target):
                    nonlocal moved
                    result = rename(path, target)
                    if path == parent.with_suffix(""):
                        moved = True
                    return result
                def fail_stat(path, *args, **kwargs):
                    nonlocal failed
                    if path == destination_directory and moved and (persistent or not failed):
                        failed = True
                        raise OSError("injected destination stat failure after rename")
                    return stat(path, *args, **kwargs)
                with patch.object(Path, "rename", observe_rename), patch.object(Path, "stat", fail_stat):
                    with self.assertRaises((lifecycle.LifecycleError, OSError)) as caught:
                        self.execute(self.request(parent, "Done"))
                self.assertTrue(failed)
                if persistent:
                    self.assertEqual("status-recovery-uncertain", caught.exception.code)
                    self.assertTrue(destination.exists())
                    self.assertEqual(b"exact descendant", (destination_directory / "asset.bin").read_bytes())
                    self.assertTrue((parent.parent / "archived" / f"{parent.stem}@1.md").exists())
                else:
                    self.assertEqual(before, self.snapshot())

    def test_recovery_does_not_move_a_substituted_foreign_directory(self):
        parent = self.put("03_plan/CA-P-701--parent.md")
        bundle = parent.with_suffix("")
        bundle.mkdir()
        (bundle / "asset.bin").write_bytes(b"owned")
        destination = parent.parent / "done" / parent.name
        destination_bundle = destination.with_suffix("")
        retained = self.root / "retained-owned-directory"
        parse = operations.atom_from_path
        def substitute(root, path):
            if path == destination:
                destination_bundle.rename(retained)
                destination_bundle.mkdir()
                (destination_bundle / "foreign.bin").write_bytes(b"foreign")
                raise operations.ToolError("injected", "foreign directory substituted")
            return parse(root, path)
        with patch.object(operations, "atom_from_path", side_effect=substitute), self.assertRaises(lifecycle.LifecycleError) as caught:
            self.execute(self.request(parent, "Done"))
        self.assertEqual("status-recovery-uncertain", caught.exception.code)
        self.assertFalse(bundle.exists())
        self.assertTrue(destination.exists())
        self.assertEqual(b"foreign", (destination_bundle / "foreign.bin").read_bytes())
        self.assertEqual(b"owned", (retained / "asset.bin").read_bytes())


if __name__ == "__main__":
    unittest.main()
