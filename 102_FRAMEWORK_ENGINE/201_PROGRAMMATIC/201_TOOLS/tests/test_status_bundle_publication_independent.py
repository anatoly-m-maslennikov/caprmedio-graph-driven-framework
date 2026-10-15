"""Independent real-source single-Atom Status publication checks, not Run admission."""

from __future__ import annotations

import datetime
import hashlib
import os
import re
import stat
import sys
import unittest
from pathlib import Path
from unittest.mock import patch

TOOLS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOLS))

import test_proposed_relation_admission as fixtures
import atom_operations
import lifecycle_intents
from atom_operations import atom_from_path
from lifecycle_intents import carrier_descriptor, change_status_atom_action, LifecycleError


class IndependentStatusBundlePublicationTests(unittest.TestCase):
    def setUp(self):
        self.fixture = fixtures.ProposedRelationAdmissionTest(methodName="runTest")
        self.fixture.setUp()
        self.addCleanup(self.fixture.tearDown)
        self.root, self.authority = self.fixture.root, self.fixture.authority
        (self.root / ".git").mkdir()
        for identifier in ("CA-D-289", "CA-D-378"):
            entry = fixtures.proposed_carrier._entry(identifier)
            raw = (fixtures.PROJECT / entry["source_path"]).read_bytes()
            self.assertEqual(hashlib.sha256(raw).hexdigest(), entry["sha256"])
            self.fixture._copy_source(entry)

    def put(self, relative, identity, *, role="Plan", kind="Plan", parent=None, status="Active", version=3):
        path = self.authority / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        relation = "{}" if parent is None else "{is_decomposition_of: [" + parent + "]}"
        body = ("# Summary\n\nIndependent immutable meaning\n\n"
            + ("## Objective\n\nVerify one target.\n\n## Details\n\n### Definition of Done\n\nExact evidence.\n"
               if role == "Plan" else "## Operation\n\nRetain the explicit operation.\n\n## Details\n\nDo not rewrite this body.\n"))
        raw = (f"---\natom_id: {identity}\ncontent_role: {role}\ntype: {kind}\n"
            "current_scope_unit: PARENT\nclaim_target_scope_unit: PARENT\n"
            "local_tier: Standard\nglobal_tier: 5\nauthor: Anatoly Maslennikov\n"
            f"status: {status}\nversion: {version}\nupdated_at: \"2026-01-01 00:00:00 +0000\"\n"
            "subjects: {governs: Atom/Test, depends_on: []}\n"
            f"relations: {relation}\n---\n" + body).encode()
        path.write_bytes(raw)
        return path

    def bundle(self, role="Plan"):
        letter, folder = ("P", "03_plan") if role == "Plan" else ("O", "09_operations")
        outer = self.put(f"{folder}/CA-{letter}-9700--outer.md", f"CA-{letter}-9700",
            role=role, kind="Plan" if role == "Plan" else "Workflow")
        local = outer.with_suffix("")
        relative = local.relative_to(self.authority) / f"CA-{letter}-9701--target.md"
        target = self.put(relative, f"CA-{letter}-9701", role=role,
            kind="Plan" if role == "Plan" else "Step", parent="CA-P-9700" if role == "Plan" else None)
        child = self.put(target.with_suffix("").relative_to(self.authority) / f"CA-{letter}-9702--child.md",
            f"CA-{letter}-9702", role=role, kind="Plan" if role == "Plan" else "Step",
            parent="CA-P-9701" if role == "Plan" else None, version=7)
        historical = child.parent / "archived" / f"CA-{letter}-9703--old@2.md"
        historical.parent.mkdir(exist_ok=True)
        historical.write_bytes(child.read_bytes().replace(f"CA-{letter}-9702".encode(),
            f"CA-{letter}-9703".encode()).replace(b"version: 7", b"version: 2").replace(
            b"status: Active", b"status: Archived"))
        return target, {p.relative_to(target.with_suffix("")): p.read_bytes()
            for p in target.with_suffix("").rglob("*") if p.is_file()}

    def request(self, path, status):
        return {"target": carrier_descriptor(self.root, atom_from_path(self.root, path)), "status": status}

    def execute(self, request):
        return change_status_atom_action(self.root, request, execute=True, authorized=True)

    def files(self):
        return {p.relative_to(self.authority): p.read_bytes() for p in self.authority.rglob("*") if p.is_file()}

    def assert_revised_bytes(self, prior, actual, status, moment_before, moment_after):
        match = re.search(rb'(?m)^updated_at: "([^"\n]+)"$', actual)
        self.assertIsNotNone(match)
        stamp = datetime.datetime.strptime(match[1].decode(), "%Y-%m-%d %H:%M:%S %z")
        self.assertGreaterEqual(stamp, moment_before - datetime.timedelta(seconds=1))
        self.assertLessEqual(stamp, moment_after + datetime.timedelta(seconds=1))
        expected = prior.replace(b"status: Active\n", f"status: {status}\n".encode()).replace(
            b"version: 3\n", b"version: 4\n").replace(
            b'updated_at: "2026-01-01 00:00:00 +0000"', b'updated_at: "' + match[1] + b'"')
        self.assertEqual(actual, expected)

    def test_nested_plan_done_moves_matching_directory_and_keeps_exact_history(self):
        target, descendants = self.bundle()
        prior, local, stem = target.read_bytes(), target.parent, target.stem
        start = datetime.datetime.now(datetime.timezone.utc)
        result = self.execute(self.request(target, "Done"))
        end = datetime.datetime.now(datetime.timezone.utc)
        destination = local / "done" / target.name
        self.assertEqual(result["outcome"], "applied")
        self.assertEqual(result["observed"]["path"], destination.relative_to(self.root).as_posix())
        self.assertFalse(target.exists())
        self.assertFalse(target.with_suffix("").exists())
        self.assertEqual((local / "archived" / f"{stem}@3.md").read_bytes(), prior)
        self.assert_revised_bytes(prior, destination.read_bytes(), "Done", start, end)
        for relative, raw in descendants.items():
            self.assertEqual((destination.with_suffix("") / relative).read_bytes(), raw)

    def test_nested_step_archive_stays_local_and_increments_only_target(self):
        target, descendants = self.bundle("Operations")
        prior, local, stem = target.read_bytes(), target.parent, target.stem
        start = datetime.datetime.now(datetime.timezone.utc)
        result = self.execute(self.request(target, "Archived"))
        end = datetime.datetime.now(datetime.timezone.utc)
        destination = local / "archived" / f"{stem}@4.md"
        self.assertEqual(result["outcome"], "applied")
        self.assertEqual(result["observed"]["path"], destination.relative_to(self.root).as_posix())
        self.assertEqual((local / "archived" / f"{stem}@3.md").read_bytes(), prior)
        self.assert_revised_bytes(prior, destination.read_bytes(), "Archived", start, end)
        self.assertFalse(target.exists())
        self.assertFalse(target.with_suffix("").exists())
        for relative, raw in descendants.items():
            self.assertEqual((destination.with_suffix("") / relative).read_bytes(), raw)

    def test_noop_preserves_all_bytes_paths_and_has_no_revision_or_history(self):
        target, _ = self.bundle()
        before = self.files()
        result = self.execute(self.request(target, "Active"))
        self.assertEqual(result["outcome"], "no-op")
        self.assertEqual(result["observed"]["version"], 3)
        self.assertTrue(all(row["state"] == "unchanged" for row in result["effects"]))
        self.assertEqual(self.files(), before)

    def test_stale_target_refuses_without_effect(self):
        target, _ = self.bundle()
        request = self.request(target, "Done")
        target.write_bytes(target.read_bytes() + b"\nChanged after observation.\n")
        before = self.files()
        with self.assertRaises(LifecycleError):
            self.execute(request)
        self.assertEqual(self.files(), before)

    def test_destination_and_history_collisions_preserve_existing_bytes(self):
        for collision in ("file", "directory", "history"):
            with self.subTest(collision=collision):
                target, _ = self.bundle()
                if collision == "history":
                    path = target.parent / "archived" / f"{target.stem}@3.md"
                elif collision == "file":
                    path = target.parent / "done" / target.name
                else:
                    path = target.parent / "done" / target.stem / "sentinel.txt"
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_bytes(b"DO NOT OVERWRITE\n")
                before = self.files()
                with self.assertRaises(LifecycleError):
                    self.execute(self.request(target, "Done"))
                self.assertEqual(self.files(), before)
                path.unlink()
                if collision == "directory":
                    path.parent.rmdir()

    def test_descendant_drift_after_initial_seal_refuses_before_publication(self):
        target, descendants = self.bundle()
        child = target.with_suffix("") / next(iter(descendants))
        request = self.request(target, "Done")
        current_time = lifecycle_intents.current_timestamp
        after_external_change = None
        def change_child(root):
            nonlocal after_external_change
            child.write_bytes(child.read_bytes() + b"\nExternal changed child.\n")
            after_external_change = self.files()
            return current_time(root)
        with patch.object(lifecycle_intents, "current_timestamp", side_effect=change_child):
            with self.assertRaises(LifecycleError) as refused:
                self.execute(request)
        self.assertEqual(refused.exception.code, "status-bundle-stale")
        self.assertIsNotNone(after_external_change)
        self.assertEqual(self.files(), after_external_change)

    def assert_fsync_fault_restores_exact_own_action(self, phase):
        target, _ = self.bundle()
        history = target.parent / "archived" / f"{target.stem}@3.md"
        destination = target.parent / "done" / target.name
        before = self.files()
        real_fsync, injected = os.fsync, False
        def fail_after_effect(descriptor):
            nonlocal injected
            condition = {
                "history": history.exists() and not destination.exists(),
                "target": destination.exists() and target.exists(),
                "remove": destination.exists() and not target.exists(),
            }[phase]
            if not injected and condition and stat.S_ISDIR(os.fstat(descriptor).st_mode):
                injected = True
                raise OSError("Independent fault after durable namespace effect: " + phase)
            return real_fsync(descriptor)
        with patch.object(os, "fsync", side_effect=fail_after_effect):
            with self.assertRaises((LifecycleError, OSError)):
                self.execute(self.request(target, "Done"))
        self.assertTrue(injected, "The intended post-effect boundary was never exercised")
        self.assertEqual(self.files(), before)

    def test_history_publication_fsync_fault_restores_exact_before_files(self):
        self.assert_fsync_fault_restores_exact_own_action("history")

    def test_target_publication_fsync_fault_restores_exact_before_files(self):
        self.assert_fsync_fault_restores_exact_own_action("target")

    def test_source_removal_fsync_fault_restores_exact_before_files(self):
        self.assert_fsync_fault_restores_exact_own_action("remove")

    def test_matching_directory_rename_fault_restores_exact_before_files(self):
        target, _ = self.bundle()
        before = self.files()
        original = Path.rename
        injected = False
        def fail_directory(source, destination):
            nonlocal injected
            if source == target.with_suffix("") and not injected:
                injected = True
                raise OSError("Independent directory-move refusal")
            return original(source, destination)
        with patch.object(Path, "rename", fail_directory):
            with self.assertRaises((LifecycleError, OSError)):
                self.execute(self.request(target, "Done"))
        self.assertTrue(injected)
        self.assertEqual(self.files(), before)

    def test_matching_directory_rename_after_effect_fault_restores_exact_before_files(self):
        target, _ = self.bundle()
        before = self.files()
        original = Path.rename
        injected = False
        def rename_then_fail(source, destination):
            nonlocal injected
            result = original(source, destination)
            if source == target.with_suffix("") and not injected:
                injected = True
                raise OSError("Directory moved before rename reported failure")
            return result
        with patch.object(Path, "rename", rename_then_fail):
            with self.assertRaises((LifecycleError, OSError)):
                self.execute(self.request(target, "Done"))
        self.assertTrue(injected)
        self.assertEqual(self.files(), before)

    def test_recovery_stat_fault_after_directory_move_reports_uncertain(self):
        target, descendants = self.bundle()
        prior = target.read_bytes()
        destination = target.parent / "done" / target.name
        destination_directory = destination.with_suffix("")
        original_rename, original_stat = Path.rename, Path.stat
        moved = stat_failed = False
        def rename_then_fail(source, destination):
            nonlocal moved
            result = original_rename(source, destination)
            if source == target.with_suffix(""):
                moved = True
                raise OSError("Directory moved before rename reported failure")
            return result
        def refuse_ownership_stat(path, *args, **options):
            nonlocal stat_failed
            if moved and path == destination_directory:
                stat_failed = True
                raise OSError("Moved directory identity cannot be observed")
            return original_stat(path, *args, **options)
        with patch.object(Path, "rename", rename_then_fail), patch.object(Path, "stat", refuse_ownership_stat):
            with self.assertRaises(LifecycleError) as raised:
                self.execute(self.request(target, "Done"))
        self.assertTrue(moved)
        self.assertTrue(stat_failed)
        self.assertEqual(raised.exception.code, "status-recovery-uncertain")
        self.assertEqual(raised.exception.__cause__.details, {
            "automatic_retry": False, "source": target.relative_to(self.root).as_posix(),
            "destination": destination.relative_to(self.root).as_posix()})
        self.assertEqual(target.read_bytes(), prior)
        self.assertTrue(destination.exists())
        self.assertFalse(target.with_suffix("").exists())
        for relative, raw in descendants.items():
            self.assertEqual((destination_directory / relative).read_bytes(), raw)

    def test_recovery_refuses_to_remove_externally_changed_publication(self):
        target, _ = self.bundle()
        prior = target.read_bytes()
        destination = target.parent / "done" / target.name
        foreign = b"External replacement must survive recovery.\n"
        original = Path.rename
        injected = False
        def change_destination_and_fail(source, destination_directory):
            nonlocal injected
            if source == target.with_suffix("") and not injected:
                injected = True
                destination.write_bytes(foreign)
                raise OSError("External writer changed the published file")
            return original(source, destination_directory)
        with patch.object(Path, "rename", change_destination_and_fail):
            with self.assertRaises(LifecycleError) as raised:
                self.execute(self.request(target, "Done"))
        self.assertTrue(injected)
        self.assertEqual(raised.exception.code, "status-recovery-uncertain")
        self.assertEqual(raised.exception.__cause__.details, {
            "automatic_retry": False, "source": target.relative_to(self.root).as_posix(),
            "destination": destination.relative_to(self.root).as_posix()})
        self.assertEqual(destination.read_bytes(), foreign)
        self.assertEqual(target.read_bytes(), prior)
        self.assertTrue(target.with_suffix("").is_dir())
        self.assertEqual((target.parent / "archived" / f"{target.stem}@3.md").read_bytes(), prior)

    def test_failed_own_recovery_is_explicitly_uncertain_and_never_success(self):
        target, _ = self.bundle()
        destination = target.parent / "done" / target.name
        real_write = atom_operations.write_raw_atom_revision
        def fail_remove_and_rollback(root, path, raw, **options):
            if raw is None and path in {target, destination}:
                raise atom_operations.ToolError("independent-fault", "Source removal or recovery refused")
            return real_write(root, path, raw, **options)
        with patch.object(atom_operations, "write_raw_atom_revision", side_effect=fail_remove_and_rollback):
            with self.assertRaises(LifecycleError) as raised:
                self.execute(self.request(target, "Done"))
        self.assertEqual(raised.exception.code, "status-recovery-uncertain")
        self.assertIsInstance(raised.exception.__cause__, atom_operations.ToolError)
        self.assertEqual(raised.exception.__cause__.details, {
            "automatic_retry": False, "source": target.relative_to(self.root).as_posix(),
            "destination": destination.relative_to(self.root).as_posix()})
        self.assertTrue(target.exists())
        self.assertTrue(destination.exists())
        self.assertTrue(target.with_suffix("").is_dir())

    def test_post_link_staging_cleanup_failure_is_recovered_or_reported_uncertain(self):
        target, _ = self.bundle()
        history = target.parent / "archived" / f"{target.stem}@3.md"
        destination = target.parent / "done" / target.name
        before = self.files()
        real_unlink, injected = os.unlink, False
        def fail_staging_unlink(path, *args, **options):
            nonlocal injected
            if not injected and str(path).startswith(".subject-") and history.exists():
                injected = True
                raise OSError("History is linked but staging cleanup failed")
            return real_unlink(path, *args, **options)
        with patch.object(os, "unlink", side_effect=fail_staging_unlink):
            with self.assertRaises(LifecycleError) as raised:
                self.execute(self.request(target, "Done"))
        self.assertTrue(injected)
        if self.files() != before:
            self.assertEqual(raised.exception.code, "status-recovery-uncertain")
            self.assertEqual(raised.exception.__cause__.details, {
                "automatic_retry": False, "source": target.relative_to(self.root).as_posix(),
                "destination": destination.relative_to(self.root).as_posix()})


if __name__ == "__main__":
    unittest.main()
