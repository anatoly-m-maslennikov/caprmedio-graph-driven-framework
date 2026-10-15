"""Current definitions are captured afresh without changing historical evidence."""

from __future__ import annotations

import hashlib
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

MCP = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(MCP))
sys.path.insert(0, str(MCP / "tests"))
sys.path.insert(0, str(MCP.parent / "201_TOOLS"))

from selected_definition_sources import CurrentDefinitionSources  # noqa: E402
from selected_routes import load_selected_manifest, selected_manifest_ref  # noqa: E402
from test_selected_routes_mcp import (  # noqa: E402
    ROOT,
    TEST_TEMP_ROOT,
    copy_complete_selected_guard_fixture,
)


class CurrentDefinitionSourcesTests(unittest.TestCase):
    def setUp(self) -> None:
        temporary = tempfile.TemporaryDirectory(dir=TEST_TEMP_ROOT)
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        self.path = self.root / "operations/action.md"
        self.path.parent.mkdir()
        self.path.write_text(
            "---\natom_id: CA-O-030\nversion: 1\ncontent_role: Operations\n"
            "type: Action\nstatus: Active\n---\nBody\n",
            encoding="utf-8",
        )

    def test_next_observation_uses_current_revision_and_old_pin_stays_frozen(self) -> None:
        first = CurrentDefinitionSources(self.root).read(
            "CA-O-030", "operations/action.md", "Action"
        )
        self.path.write_text(self.path.read_text().replace("version: 1", "version: 2") + "Change\n")
        second = CurrentDefinitionSources(self.root).read(
            "CA-O-030", "operations/action.md", "Action"
        )
        self.assertEqual((1, 2), (first["version"], second["version"]))
        self.assertNotEqual(first["digest"], second["digest"])

    def test_identity_role_type_status_and_duplicate_metadata_are_still_required(self) -> None:
        original = self.path.read_text()
        for old, new in (
            ("CA-O-030", "CA-O-031"),
            ("Operations", "Plan"),
            ("Action", "Step"),
            ("Active", "Archived"),
            ("version: 1", "version: 1\nversion: 2"),
        ):
            with self.subTest(new=new):
                self.path.write_text(original.replace(old, new))
                with self.assertRaises((ValueError, RuntimeError)):
                    CurrentDefinitionSources(self.root).read(
                        "CA-O-030", "operations/action.md", "Action"
                    )

    def test_archived_paths_symlinks_and_competing_identity_paths_refuse(self) -> None:
        sources = CurrentDefinitionSources(self.root)
        sources.read("CA-O-030", "operations/action.md")
        for reference in ("operations/archive/action.md", "operations/other.md"):
            with self.subTest(reference=reference), self.assertRaises(ValueError):
                sources.read("CA-O-030", reference)
        link = self.root / "linked.md"
        link.symlink_to(self.path)
        with self.assertRaises((ValueError, RuntimeError)):
            CurrentDefinitionSources(self.root).read("CA-O-030", "linked.md")

    def test_captured_source_change_refuses_within_observation(self) -> None:
        sources = CurrentDefinitionSources(self.root)
        sources.read("CA-O-030", "operations/action.md")
        self.path.write_text(self.path.read_text() + "Change\n")
        with self.assertRaises((ValueError, RuntimeError)):
            sources.revalidate()


class CurrentSelectedManifestTests(unittest.TestCase):
    def setUp(self) -> None:
        temporary = tempfile.TemporaryDirectory(dir=TEST_TEMP_ROOT)
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        copy_complete_selected_guard_fixture(self.root)
        self.carrier = self.root / selected_manifest_ref(self.root)
        self.carrier.write_bytes((ROOT / selected_manifest_ref(ROOT)).read_bytes())

    def test_old_projection_resolves_new_rule_without_rewrite_or_repin(self) -> None:
        first = load_selected_manifest(self.root)
        before = self.carrier.read_bytes()
        pin = first["routes"][0]["ordered_actions"][0]
        path = self.root / pin["source_path"]
        path.write_text(
            path.read_text().replace(
                f"version: {pin['version']}\n", f"version: {pin['version'] + 1}\n"
            )
            + "\nCurrent revision\n"
        )
        second = load_selected_manifest(self.root)
        current = second["routes"][0]["ordered_actions"][0]
        self.assertEqual(pin["version"] + 1, current["version"])
        self.assertEqual(hashlib.sha256(path.read_bytes()).hexdigest(), current["digest"])
        self.assertNotEqual(first["canonical_manifest_sha256"], second["canonical_manifest_sha256"])
        self.assertEqual(before, self.carrier.read_bytes())

    def test_source_drift_before_final_revalidation_refuses(self) -> None:
        original = CurrentDefinitionSources.revalidate

        def change_then_validate(sources: CurrentDefinitionSources) -> None:
            reference = next(iter(sources.sources))
            path = self.root / reference
            path.write_text(path.read_text() + "\nDrift\n")
            original(sources)

        with patch.object(CurrentDefinitionSources, "revalidate", change_then_validate):
            with self.assertRaises((ValueError, RuntimeError)):
                load_selected_manifest(self.root)
