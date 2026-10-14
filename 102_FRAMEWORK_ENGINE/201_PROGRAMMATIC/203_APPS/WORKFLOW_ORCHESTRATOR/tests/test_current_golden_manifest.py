"""Copy the actual fifteen-route input unchanged; do not adapt retired portfolios."""

import copy
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from selected_workflows_docker_fixture import (
    GoldenCase,
    GoldenCorpusError,
    GoldenProject,
    MANIFEST_REF,
    MANIFEST_ROUTE_NAMES,
)

ROOT = Path(__file__).resolve().parents[5]


class CurrentGoldenManifestTests(unittest.TestCase):
    def setUp(self):
        parent = ROOT / ".caprmedio_tmp/tests/current-golden-manifest"
        parent.mkdir(parents=True, exist_ok=True)
        directory = tempfile.TemporaryDirectory(dir=parent)
        self.addCleanup(directory.cleanup)
        self.root = Path(directory.name)
        self.project = GoldenProject(ROOT, self.root, GoldenCase("W01", "create_atom"))
        self.actual = json.loads((ROOT / MANIFEST_REF).read_text())

    def test_current_fifteen_routes_and_all_pins_are_copied_unchanged(self):
        copied = self.project._copy_reviewed_manifest()
        self.assertEqual(self.actual, copied)
        self.assertEqual(MANIFEST_ROUTE_NAMES, tuple(row["route"] for row in copied["routes"]))
        self.assertEqual(copied, json.loads(self.project.manifest_path.read_text()))
        self.assertNotIn("release_source_admissions", copied)
        self.assertNotIn("public_release_source_admissions", copied)

    def test_old_release_rows_are_refused_before_copying_or_repinning(self):
        retired = copy.deepcopy(self.actual)
        retired["routes"].extend([{"route": "release_version"}, {"route": "public.release"}])
        with (
            patch("selected_workflows_docker_fixture.json.loads", return_value=retired),
            patch.object(self.project, "_copy_pinned") as copy_source,
        ):
            with self.assertRaisesRegex(GoldenCorpusError, "exact closed fifteen-route"):
                self.project._copy_reviewed_manifest()
            copy_source.assert_not_called()
        self.assertFalse(self.project.manifest_path.exists())


if __name__ == "__main__":
    unittest.main()
