"""Temporary-state confinement and atomic precondition tests."""

from __future__ import annotations

from pathlib import Path
import os
import sys
import tempfile
import unittest
from unittest.mock import patch


TOOLS_ROOT = Path(__file__).resolve().parents[1]
if str(TOOLS_ROOT) not in sys.path:
    sys.path.insert(0, str(TOOLS_ROOT))

from project_runtime import TEMPORARY_DIRECTORY, TemporaryBoundaryError, atomic_tempfile  # noqa: E402


TEST_TEMP_ROOT = (
    Path(__file__).resolve().parents[4]
    / TEMPORARY_DIRECTORY
    / "tests"
    / "project-runtime-temp-safety"
)
TEST_TEMP_ROOT.mkdir(parents=True, exist_ok=True)


class ProjectRuntimeTemporarySafetyTests(unittest.TestCase):
    def project(self) -> Path:
        fixture = tempfile.TemporaryDirectory(dir=TEST_TEMP_ROOT)
        self.addCleanup(fixture.cleanup)
        root = Path(fixture.name)
        (root / ".git").mkdir()
        return root

    def test_symlinked_temporary_root_is_refused_without_outside_mutation(self) -> None:
        root = self.project()
        outside = root / "outside"
        outside.mkdir()
        sentinel = outside / "sentinel.txt"
        sentinel.write_text("unchanged\n", encoding="utf-8")
        (root / TEMPORARY_DIRECTORY).symlink_to(outside, target_is_directory=True)
        destination = root / "state" / "current.json"

        with self.assertRaises(TemporaryBoundaryError):
            atomic_tempfile(destination, "unit")

        self.assertEqual(sentinel.read_text(encoding="utf-8"), "unchanged\n")
        self.assertEqual({path.name for path in outside.iterdir()}, {sentinel.name})
        self.assertFalse(destination.parent.exists())

    def test_symlinked_owner_or_atomic_directory_is_refused(self) -> None:
        for atomic_parent in (False, True):
            with self.subTest(atomic_parent=atomic_parent):
                root = self.project()
                temporary_root = root / TEMPORARY_DIRECTORY
                temporary_root.mkdir()
                outside = root / "outside"
                outside.mkdir()
                sentinel = outside / "sentinel.txt"
                sentinel.write_text("unchanged\n", encoding="utf-8")
                owner = temporary_root / "unit"
                link = owner / "atomic" if atomic_parent else owner
                if atomic_parent:
                    owner.mkdir()
                link.symlink_to(outside, target_is_directory=True)
                destination = root / "state" / "current.json"

                with self.assertRaises(TemporaryBoundaryError):
                    atomic_tempfile(destination, "unit")

                self.assertEqual(sentinel.read_text(encoding="utf-8"), "unchanged\n")
                self.assertEqual({path.name for path in outside.iterdir()}, {sentinel.name})
                self.assertFalse(destination.parent.exists())

    def test_valid_allocation_stays_below_project_temporary_state(self) -> None:
        root = self.project()
        destination = root / "state" / "current.json"
        descriptor, temporary_name = atomic_tempfile(destination, "unit")
        temporary = Path(temporary_name)
        try:
            self.assertTrue(
                temporary.is_relative_to(root / TEMPORARY_DIRECTORY / "unit" / "atomic")
            )
            with os.fdopen(descriptor, "w", encoding="utf-8") as handle:
                handle.write("{}\n")
        finally:
            temporary.unlink(missing_ok=True)

    def test_cross_filesystem_refusal_precedes_stage_and_destination_creation(self) -> None:
        root = self.project()
        owner = root / TEMPORARY_DIRECTORY / "unit"
        owner.mkdir(parents=True)
        destination = root / "state" / "current.json"
        real_stat = os.stat

        def fake_stat(path: str | os.PathLike[str]) -> os.stat_result:
            value = real_stat(path)
            if Path(path) == owner:
                modified = list(value)
                modified[2] = value.st_dev + 1
                return os.stat_result(modified)
            return value

        with patch.object(os, "stat", side_effect=fake_stat):
            with self.assertRaises(TemporaryBoundaryError):
                atomic_tempfile(destination, "unit")

        self.assertFalse((owner / "atomic").exists())
        self.assertFalse(destination.parent.exists())


if __name__ == "__main__":
    unittest.main()
