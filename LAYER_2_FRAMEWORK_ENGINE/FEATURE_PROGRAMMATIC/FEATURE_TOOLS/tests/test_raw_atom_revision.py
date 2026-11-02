from __future__ import annotations

from pathlib import Path
import os
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import atom_operations
from atom_operations import ToolError, read_raw_atom_revision, write_raw_atom_revision


class RawAtomRevisionTests(unittest.TestCase):
    def setUp(self):
        scratch = Path(__file__).resolve().parents[4] / ".caprmedio_tmp" / "tests" / "raw-atom-revision"
        scratch.mkdir(parents=True, exist_ok=True)
        self.directory = tempfile.TemporaryDirectory(dir=scratch)
        self.addCleanup(self.directory.cleanup)
        self.root = Path(self.directory.name).resolve()
        self.path = self.root / "role" / "current.md"
        self.path.parent.mkdir()
        self.before = b"---\r\nversion: 1\r\n---\r\nunchanged body\r\n"
        self.path.write_bytes(self.before)
        self.path.chmod(0o640)
        _, self.fingerprint = read_raw_atom_revision(self.root, self.path)

    def test_exact_current_and_history_bytes_modes_and_owned_removal(self):
        archive = self.path.parent / "archive" / "current@1.md"
        owner = write_raw_atom_revision(self.root, archive, self.before, expected=None, mode=0o640)
        self.assertEqual(read_raw_atom_revision(self.root, archive), (self.before, owner))
        after = self.before.replace(b"version: 1", b"version: 2")
        current_owner = write_raw_atom_revision(self.root, self.path, after, expected=self.fingerprint, mode=0o640)
        self.assertEqual(read_raw_atom_revision(self.root, self.path), (after, current_owner))
        write_raw_atom_revision(self.root, self.path, self.before, expected=current_owner, mode=0o640)
        write_raw_atom_revision(self.root, archive, None, expected=owner, mode=0o640)
        self.assertEqual(self.path.read_bytes(), self.before)
        self.assertEqual(self.path.stat().st_mode & 0o777, 0o640)
        self.assertFalse(archive.exists())
        self.assertEqual(list((self.root / ".caprmedio_tmp").rglob("*.tmp")), [])

    def test_existing_archive_and_stale_current_are_never_overwritten(self):
        archive = self.path.parent / "archive" / "current@1.md"
        write_raw_atom_revision(self.root, archive, b"other history", expected=None, mode=0o600)
        with self.assertRaises(ToolError):
            write_raw_atom_revision(self.root, archive, self.before, expected=None, mode=0o640)
        self.path.write_bytes(b"concurrent source")
        with self.assertRaises(ToolError):
            write_raw_atom_revision(self.root, self.path, b"replacement", expected=self.fingerprint, mode=0o640)
        self.assertEqual(archive.read_bytes(), b"other history")
        self.assertEqual(self.path.read_bytes(), b"concurrent source")

    def test_symlink_file_parent_and_temporary_root_are_rejected(self):
        outside = self.root / "outside"
        outside.mkdir()
        victim = outside / "victim.md"
        victim.write_bytes(b"outside remains")
        self.path.unlink()
        self.path.symlink_to(victim)
        with self.assertRaises((ToolError, OSError)):
            read_raw_atom_revision(self.root, self.path)
        with self.assertRaises(ToolError):
            write_raw_atom_revision(self.root, self.path, b"replacement", expected=self.fingerprint, mode=0o640)
        alias = self.root / "alias"
        alias.symlink_to(outside, target_is_directory=True)
        with self.assertRaises(ToolError):
            write_raw_atom_revision(self.root, alias / "new.md", b"replacement", expected=None, mode=0o640)
        (self.root / ".caprmedio_tmp").rename(self.root / "old_tmp")
        (self.root / ".caprmedio_tmp").symlink_to(outside, target_is_directory=True)
        with self.assertRaises(ToolError):
            write_raw_atom_revision(self.root, self.root / "new.md", b"replacement", expected=None, mode=0o640)
        self.assertEqual(victim.read_bytes(), b"outside remains")
        self.assertFalse((outside / "new.md").exists())

    def test_removal_requires_exact_attempt_owned_revision(self):
        self.path.chmod(0o600)
        with self.assertRaises(ToolError):
            write_raw_atom_revision(self.root, self.path, None, expected=self.fingerprint, mode=0o640)
        self.assertEqual(self.path.read_bytes(), self.before)

    def test_history_collision_at_native_create_preserves_foreign_history(self):
        archive = self.path.parent / "archive" / "current@1.md"
        foreign = b"existing unrelated history\n"
        real_link = os.link

        def collide(source, destination, *, src_dir_fd, dst_dir_fd, follow_symlinks):
            archive.write_bytes(foreign)
            archive.chmod(0o600)
            return real_link(source, destination, src_dir_fd=src_dir_fd,
                             dst_dir_fd=dst_dir_fd, follow_symlinks=follow_symlinks)

        with patch.object(atom_operations.os, "link", side_effect=collide):
            with self.assertRaises(ToolError) as refused:
                write_raw_atom_revision(self.root, archive, self.before, expected=None, mode=0o640)
        self.assertEqual("subject-publication-failed", refused.exception.code)
        self.assertNotIn("publication_fingerprint", refused.exception.details)
        self.assertEqual(foreign, archive.read_bytes())
        self.assertEqual(0o600, archive.stat().st_mode & 0o777)
        self.assertEqual(self.before, self.path.read_bytes())
        self.assertEqual([], list((self.root / ".caprmedio_tmp").rglob("*.tmp")))

    def test_failure_after_publication_retains_exact_attempt_owner_for_restoration(self):
        after = self.before.replace(b"version: 1", b"version: 2")
        real_fsync = os.fsync
        failed = False

        def fail_published_parent(descriptor):
            nonlocal failed
            if self.path.read_bytes() == after and not failed:
                failed = True
                raise OSError("fixture post-publication durability failure")
            return real_fsync(descriptor)

        with patch.object(atom_operations.os, "fsync", side_effect=fail_published_parent):
            with self.assertRaises(ToolError) as failure:
                write_raw_atom_revision(self.root, self.path, after, expected=self.fingerprint, mode=0o640)
        self.assertTrue(failed)
        owner = tuple(failure.exception.details["publication_fingerprint"])
        self.assertEqual((after, owner), read_raw_atom_revision(self.root, self.path))
        write_raw_atom_revision(self.root, self.path, self.before, expected=owner, mode=0o640)
        self.assertEqual(self.before, self.path.read_bytes())
        self.assertEqual(0o640, self.path.stat().st_mode & 0o777)

    def test_identical_bytes_at_a_foreign_inode_never_establish_cleanup_ownership(self):
        archive = self.path.parent / "archive" / "current@1.md"
        owner = write_raw_atom_revision(self.root, archive, self.before, expected=None, mode=0o640)
        saved = archive.with_name("attempt-owned.md")
        archive.rename(saved)
        archive.write_bytes(self.before)
        archive.chmod(0o640)
        with self.assertRaises(ToolError) as refused:
            write_raw_atom_revision(self.root, archive, None, expected=owner, mode=0o640)
        self.assertEqual("subject-destination-stale", refused.exception.code)
        self.assertEqual(self.before, archive.read_bytes())
        self.assertEqual(self.before, saved.read_bytes())

    def test_parent_substitution_before_effect_preserves_both_directory_frontiers(self):
        saved = self.root / "original-role"
        real_parent = atom_operations._raw_revision_parent
        switched = False

        def substitute(project_root, path, *, create=False):
            nonlocal switched
            if path == self.path and not create and not switched:
                # The second open is the writer's final parent recheck.
                switched = True
                self.path.parent.rename(saved)
                self.path.parent.mkdir()
                self.path.write_bytes(b"foreign directory state\n")
            return real_parent(project_root, path, create=create)

        first = True
        def open_then_substitute(project_root, path, *, create=False):
            nonlocal first
            if path == self.path and first:
                first = False
                return real_parent(project_root, path, create=create)
            return substitute(project_root, path, create=create)

        with patch.object(atom_operations, "_raw_revision_parent", side_effect=open_then_substitute):
            with self.assertRaises(ToolError) as refused:
                write_raw_atom_revision(self.root, self.path, b"requested new state\n",
                                        expected=self.fingerprint, mode=0o640)
        self.assertEqual("subject-destination-stale", refused.exception.code)
        self.assertEqual(self.before, (saved / self.path.name).read_bytes())
        self.assertEqual(b"foreign directory state\n", self.path.read_bytes())


if __name__ == "__main__":
    unittest.main()
