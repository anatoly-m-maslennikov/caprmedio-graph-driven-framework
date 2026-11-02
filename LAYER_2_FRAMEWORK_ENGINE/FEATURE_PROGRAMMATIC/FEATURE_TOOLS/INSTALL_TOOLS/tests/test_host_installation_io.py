"""Functional checks for preserving host files across installation failures."""

import os
from pathlib import Path
import stat
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from INSTALL_TOOLS.host_installation_io import FileUpdate, HostInstallationError  # noqa: E402


class HostInstallationIoTests(unittest.TestCase):
    def setUp(self):
        directory = Path.cwd() / ".caprmedio_tmp/tests/host_installation_io"
        directory.mkdir(parents=True, exist_ok=True)
        self.temporary = tempfile.TemporaryDirectory(dir=directory)
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name).resolve()

    def test_new_nested_file_preview_apply_and_restore(self):
        path = self.root / "missing/parent/settings.toml"
        update = FileUpdate(path, b"new\n")
        self.assertTrue(update.changed)
        self.assertFalse(path.parent.exists())
        update.apply()
        self.assertEqual(path.read_bytes(), b"new\n")
        update.restore()
        self.assertFalse(path.exists())

    def test_existing_file_permissions_and_exact_bytes_survive_update_restore(self):
        path = self.root / "settings.toml"
        path.write_bytes(b"# original\n")
        path.chmod(0o640)
        update = FileUpdate(path, b"new\n")
        update.apply()
        self.assertEqual(stat.S_IMODE(path.stat().st_mode), 0o640)
        update.restore()
        self.assertEqual(path.read_bytes(), b"# original\n")
        self.assertEqual(stat.S_IMODE(path.stat().st_mode), 0o640)

    def test_identical_update_is_noop_and_does_not_change_mode(self):
        path = self.root / "settings.toml"
        path.write_bytes(b"same\n")
        path.chmod(0o644)
        before = path.stat()
        update = FileUpdate(path, b"same\n")
        self.assertFalse(update.changed)
        update.apply()
        self.assertEqual(path.stat().st_ino, before.st_ino)
        self.assertEqual(stat.S_IMODE(path.stat().st_mode), 0o644)

    def test_stale_write_and_restore_never_overwrite_concurrent_changes(self):
        path = self.root / "settings.toml"
        path.write_bytes(b"before\n")
        stale = FileUpdate(path, b"installation\n")
        path.write_bytes(b"user edit\n")
        with self.assertRaises(HostInstallationError):
            stale.apply()
        self.assertEqual(path.read_bytes(), b"user edit\n")
        current = FileUpdate(path, b"installation\n")
        current.apply()
        path.write_bytes(b"later user edit\n")
        with self.assertRaises(HostInstallationError):
            current.restore()
        self.assertEqual(path.read_bytes(), b"later user edit\n")

    def test_symlink_and_non_directory_ancestors_are_refused(self):
        real = self.root / "real"
        real.mkdir()
        link = self.root / "link"
        link.symlink_to(real, target_is_directory=True)
        file = self.root / "file"
        file.write_bytes(b"keep")
        for path in (link / "settings", file / "settings"):
            with self.subTest(path=path), self.assertRaises(HostInstallationError):
                FileUpdate(path, b"unsafe")
        self.assertEqual(file.read_bytes(), b"keep")
        self.assertEqual(os.listdir(real), [])


if __name__ == "__main__":
    unittest.main()
