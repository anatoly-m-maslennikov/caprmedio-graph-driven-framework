"""Freeze current definitions for fifteen-route fixtures, not retired portfolios."""

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

    def test_current_fifteen_routes_and_observed_pins_are_copied_without_source_rewrite(self):
        before = (ROOT / MANIFEST_REF).read_bytes()
        copied = self.project._copy_reviewed_manifest()
        from selected_routes import load_selected_manifest

        expected = load_selected_manifest(ROOT)
        expected.pop("manifest_ref")
        self.assertEqual(expected, copied)
        self.assertEqual(MANIFEST_ROUTE_NAMES, tuple(row["route"] for row in copied["routes"]))
        self.assertEqual(copied, json.loads(self.project.manifest_path.read_text()))
        self.assertEqual(before, (ROOT / MANIFEST_REF).read_bytes())
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

    def test_next_fixture_observes_current_rule_revision_without_constant_repin(self):
        first = self.project._copy_reviewed_manifest()
        route = next(row for row in first["routes"] if row["route"] == "update_atom")
        action = next(pin for pin in route["native_action_calls"] if pin["atom_id"] == "CA-O-030")
        source = self.root / action["source_path"]
        source.write_text(source.read_text().replace(
            f"version: {action['version']}\n", f"version: {action['version'] + 1}\n"
        ) + "\nCurrent fixture rule revision.\n", encoding="utf-8")
        before = self.project.manifest_path.read_bytes()
        target = self.root / "next-project"
        target.mkdir()
        next_project = GoldenProject(self.root, target, GoldenCase("W02", "update_atom"))

        second = next_project._copy_reviewed_manifest()

        second_route = next(row for row in second["routes"] if row["route"] == "update_atom")
        current = next(pin for pin in second_route["native_action_calls"] if pin["atom_id"] == "CA-O-030")
        self.assertEqual(action["version"] + 1, current["version"])
        self.assertNotEqual(action["digest"], current["digest"])
        self.assertEqual(source.read_bytes(), (target / current["source_path"]).read_bytes())
        self.assertEqual(before, self.project.manifest_path.read_bytes())

    def test_source_change_after_current_capture_still_refuses_copy(self):
        first = self.project._copy_reviewed_manifest()
        action = next(pin for row in first["routes"] for pin in row["native_action_calls"]
                      if pin["atom_id"] == "CA-O-030")
        target = self.root / "changed-project"
        target.mkdir()
        project = GoldenProject(self.root, target, GoldenCase("W02", "update_atom"))
        copy_pinned = project._copy_pinned

        def change_before_copy(relative, expected_digest):
            if relative.as_posix() == action["source_path"]:
                source = self.root / relative
                source.write_text(source.read_text() + "\nChanged after observation.\n", encoding="utf-8")
            copy_pinned(relative, expected_digest)

        with patch.object(project, "_copy_pinned", side_effect=change_before_copy):
            with self.assertRaisesRegex(GoldenCorpusError, "unavailable or stale"):
                project._copy_reviewed_manifest()
        self.assertFalse(project.manifest_path.exists())


if __name__ == "__main__":
    unittest.main()
