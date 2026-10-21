"""Fixture scratch stays in Project Temporary State, not ambient host temp."""
from pathlib import Path
import sys
import tempfile
import unittest

TESTS = Path(__file__).resolve().parent
sys.path.insert(0, str(TESTS))

from container_lifecycle_fixture import APP, ContainerLifecycleFixture  # noqa: E402

PROJECT_TEMP = APP.parents[3] / ".caprmedio_tmp" / "tests" / "container-lifecycle"


class ContainerLifecycleFixturePathTests(unittest.TestCase):
    def test_default_root_is_project_owned_and_cleaned_up(self):
        fixture = ContainerLifecycleFixture()
        root = fixture.root
        try:
            self.assertTrue(root.is_relative_to(PROJECT_TEMP.resolve()))
            self.assertTrue(root.is_dir())
        finally:
            fixture.close()
        self.assertFalse(root.exists())

    def test_explicit_root_is_preserved_and_not_owned_by_fixture(self):
        PROJECT_TEMP.mkdir(parents=True, exist_ok=True)
        with tempfile.TemporaryDirectory(dir=PROJECT_TEMP) as outer:
            root = Path(outer) / "explicit"
            fixture = ContainerLifecycleFixture(root)
            self.assertEqual(root.resolve(), fixture.root)
            fixture.close()
            self.assertTrue(root.is_dir())
