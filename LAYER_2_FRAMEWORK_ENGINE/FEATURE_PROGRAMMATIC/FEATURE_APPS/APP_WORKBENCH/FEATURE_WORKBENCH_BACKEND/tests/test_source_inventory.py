"""Check Markdown inventory at the directory and symlink boundaries."""

import os
from pathlib import Path
import sys
from tempfile import TemporaryDirectory
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[3]))
from APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.source_inventory import markdown_paths


class SourceInventoryTest(unittest.TestCase):
    def test_markdown_inventory_skips_symlinks_and_unreadable_directories(self):
        with TemporaryDirectory() as temporary:
            root = Path(temporary)
            current = root / "current.md"
            current.touch()
            folder = root / "folder.md"
            folder.mkdir()
            nested = folder / "nested.md"
            nested.touch()
            archive = folder / "099_archived"
            archive.mkdir()
            historical = archive / "historical.md"
            historical.touch()
            (root / "link.md").symlink_to(current)
            (root / "linked-folder.md").symlink_to(folder)
            (root / ".md").touch()
            blocked = root / "blocked"
            blocked.mkdir()
            (blocked / "unreadable.md").touch()
            scandir = os.scandir

            def scan(path):
                if path == blocked:
                    raise PermissionError(path)
                return scandir(path)

            with patch("os.scandir", side_effect=scan):
                self.assertEqual(set(markdown_paths(root)), {current, folder, nested, historical})
                self.assertEqual(set(markdown_paths(root, include_archived=False)), {current, folder, nested})
