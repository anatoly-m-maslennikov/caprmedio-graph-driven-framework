from __future__ import annotations

from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from atom_operations import ToolError, read_raw_atom_revision, write_raw_atom_revision


class RawAtomRevisionTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
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


if __name__ == "__main__":
    unittest.main()
