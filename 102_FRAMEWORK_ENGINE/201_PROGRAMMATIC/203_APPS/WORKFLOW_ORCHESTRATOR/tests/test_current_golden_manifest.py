"""Frozen selected-route manifest checks, with current-project non-mutation separate."""

from __future__ import annotations

import copy
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from frozen_selected_workflows import frozen_manifest
from selected_workflows_docker_fixture import (
    GoldenCase,
    GoldenCorpusError,
    GoldenProject,
    MANIFEST_REF,
    MANIFEST_ROUTE_NAMES,
)


ROOT = Path(__file__).resolve().parents[5]


class FrozenGoldenManifestTests(unittest.TestCase):
    def setUp(self) -> None:
        parent = ROOT / ".caprmedio_tmp/tests/current-golden-manifest"
        parent.mkdir(parents=True, exist_ok=True)
        directory = tempfile.TemporaryDirectory(dir=parent)
        self.addCleanup(directory.cleanup)
        self.root = Path(directory.name)
        self.project = GoldenProject(ROOT, self.root, GoldenCase("W01", "create_atom"))

    def test_fifteen_checked_in_routes_and_pins_are_copied_without_reobservation(self) -> None:
        copied = self.project._copy_reviewed_manifest()
        self.assertEqual(frozen_manifest(), copied)
        self.assertEqual(MANIFEST_ROUTE_NAMES, tuple(row["route"] for row in copied["routes"]))
        self.assertEqual(copied, json.loads(self.project.manifest_path.read_text()))
        self.assertNotIn("release_source_admissions", copied)
        self.assertNotIn("public_release_source_admissions", copied)

    def test_retired_route_rows_are_refused_before_copying_or_repinning(self) -> None:
        retired = copy.deepcopy(frozen_manifest())
        retired["routes"].extend([{"route": "release_version"}, {"route": "public.release"}])
        with (
            patch("selected_workflows_docker_fixture.frozen_manifest", return_value=retired),
            patch.object(self.project, "_copy_pinned") as copy_source,
        ):
            with self.assertRaisesRegex(GoldenCorpusError, "exact closed fifteen-route"):
                self.project._copy_reviewed_manifest()
            copy_source.assert_not_called()
        self.assertFalse(self.project.manifest_path.exists())

    def test_unknown_or_stale_frozen_source_remains_refused(self) -> None:
        route = next(row for row in frozen_manifest()["routes"] if row["route"] == "update_atom")
        pin = next(row for row in route["native_action_calls"] if row["atom_id"] == "CA-O-030")
        with self.assertRaisesRegex(GoldenCorpusError, "unavailable or stale"):
            self.project._copy_pinned(Path(pin["source_path"]), "0" * 64)
        self.assertFalse((self.root / pin["source_path"]).exists())


class CurrentProjectProjectionNonMutationTests(unittest.TestCase):
    """Current Project checks intentionally do not feed golden fixture inputs."""

    def test_golden_copy_does_not_rewrite_current_project_projection(self) -> None:
        current = ROOT / MANIFEST_REF
        before = current.read_bytes()
        parent = ROOT / ".caprmedio_tmp/tests/current-golden-manifest"
        parent.mkdir(parents=True, exist_ok=True)
        with tempfile.TemporaryDirectory(dir=parent) as temporary:
            GoldenProject(ROOT, Path(temporary), GoldenCase("W02", "update_atom"))._copy_reviewed_manifest()
        self.assertEqual(before, current.read_bytes())


if __name__ == "__main__":
    unittest.main()
