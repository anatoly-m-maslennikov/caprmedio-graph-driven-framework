"""Shared Methodology export inventory safety, independent of Release seals."""

from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from release_inventory import (  # noqa: E402
    ReleaseInventoryError,
    persistent_regular_files,
    refuse_secret_path,
)


class ReleaseInventoryTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory(prefix="shared-inventory-")
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name).resolve()
        self.source = self.root / "source"
        self.source.mkdir()

    def file(self, relative, content=b"ordinary bytes\n"):
        path = self.source / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(content)
        return path

    def test_ordinary_persisted_files_are_ordered_without_atom_metadata(self):
        files = [self.file("z/tool.py"), self.file("a/note.md"), self.file("data.json")]
        self.assertEqual(sorted(files), persistent_regular_files(self.root, self.source))

    def test_transient_state_is_not_exported(self):
        ordinary = self.file("tool.py")
        for name in (
            ".caprmedio_tmp/report.json",
            "__pycache__/tool.pyc",
            ".venv/bin/python",
            ".pytest_cache/state",
            ".DS_Store",
            "standalone.pyc",
        ):
            self.file(name)
        self.assertEqual([ordinary], persistent_regular_files(self.root, self.source))

    def test_secret_shaped_names_are_refused_before_content_read(self):
        for name in (".env", ".env.production", "credentials.env", "nested/.env/value"):
            with self.subTest(name=name), self.assertRaises(ReleaseInventoryError):
                refuse_secret_path(name)
        self.file(".env", b"never export\n")
        with self.assertRaisesRegex(ReleaseInventoryError, "secret-shaped"):
            persistent_regular_files(self.root, self.source)

    def test_symlink_file_is_refused(self):
        original = self.file("real.py")
        (self.source / "alias.py").symlink_to(original)
        with self.assertRaisesRegex(ReleaseInventoryError, "symlink"):
            persistent_regular_files(self.root, self.source)

    def test_symlink_directory_is_refused_without_following_it(self):
        target = self.root / "target"
        target.mkdir()
        (self.source / "alias").symlink_to(target, target_is_directory=True)
        with self.assertRaisesRegex(ReleaseInventoryError, "symlink"):
            persistent_regular_files(self.root, self.source)

    def test_inventory_root_cannot_escape_project(self):
        with self.assertRaisesRegex(ReleaseInventoryError, "escapes project"):
            persistent_regular_files(self.root, self.root.parent)


if __name__ == "__main__":
    unittest.main()
