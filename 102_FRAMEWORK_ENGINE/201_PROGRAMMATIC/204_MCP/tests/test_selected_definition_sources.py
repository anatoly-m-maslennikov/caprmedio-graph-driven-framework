"""Current definitions are captured afresh without changing historical evidence."""

from __future__ import annotations

import hashlib
import shutil
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
import selected_routes  # noqa: E402
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

    def test_missing_workflow_hint_resolves_once_and_returns_current_path(self) -> None:
        current_path = self.root / "operations/renamed-action.md"
        current_path.write_text(self.path.read_text().replace("CA-O-030", "CA-O-127"))
        self.path.unlink()
        sources = CurrentDefinitionSources(self.root)
        with patch("selected_definition_sources.CurrentAtomLocator") as locator_type:
            locator = locator_type.return_value
            locator.locate.return_value = "operations/renamed-action.md"
            observed = sources.read("CA-O-127", "operations/action.md", "Action")
            again = sources.read("CA-O-127", observed["source_path"], "Action")
            alias_again = sources.read("CA-O-127", "operations/action.md", "Action")
        locator_type.assert_called_once_with(self.root)
        locator.locate.assert_called_once_with("CA-O-127", "operations/action.md")
        self.assertEqual("operations/renamed-action.md", observed["source_path"])
        self.assertEqual(observed, again)
        self.assertEqual(observed, alias_again)

    def test_one_admission_locator_serves_multiple_missing_workflow_ids(self) -> None:
        first_path = self.root / "operations/renamed-127.md"
        second_path = self.root / "operations/renamed-128.md"
        first_path.write_text(self.path.read_text().replace("CA-O-030", "CA-O-127"))
        second_path.write_text(self.path.read_text().replace("CA-O-030", "CA-O-128"))
        with patch("selected_definition_sources.CurrentAtomLocator") as locator_type:
            locator = locator_type.return_value
            locator.locate.side_effect = (
                "operations/renamed-127.md", "operations/renamed-128.md"
            )
            sources = CurrentDefinitionSources(self.root)
            sources.read("CA-O-127", "operations/old-127.md", "Action")
            sources.read("CA-O-128", "operations/old-128.md", "Action")
            sources.revalidate()
        locator_type.assert_called_once_with(self.root)
        self.assertEqual(2, locator.locate.call_count)
        locator.revalidate.assert_called_once_with()

    def test_duplicate_current_id_fallback_refuses(self) -> None:
        self.path.unlink()
        with patch("selected_definition_sources.CurrentAtomLocator.locate", side_effect=ValueError("duplicate current ID")):
            with self.assertRaisesRegex(ValueError, "duplicate current ID"):
                CurrentDefinitionSources(self.root).read("CA-O-127", "operations/action.md")

    def test_existing_hint_with_foreign_id_does_not_fallback(self) -> None:
        with patch("selected_definition_sources.CurrentAtomLocator.locate") as locate:
            with self.assertRaises(ValueError):
                CurrentDefinitionSources(self.root).read("CA-O-127", "operations/action.md")
        locate.assert_not_called()

    def test_relocated_captured_source_stays_stale_in_same_observation(self) -> None:
        current_path = self.root / "operations/renamed-action.md"
        current_path.write_text(self.path.read_text().replace("CA-O-030", "CA-O-127"))
        self.path.unlink()
        sources = CurrentDefinitionSources(self.root)
        with patch("selected_definition_sources.CurrentAtomLocator.locate", return_value="operations/renamed-action.md"):
            sources.read("CA-O-127", "operations/action.md")
            current_path.rename(self.root / "operations/moved-again.md")
            with self.assertRaises((ValueError, RuntimeError, OSError)):
                sources.revalidate()

    def test_fallback_cannot_bind_historical_or_draft_carriers(self) -> None:
        self.path.unlink()
        for reference in ("operations/archive/old.md", "operations/drafts/working.md"):
            with self.subTest(reference=reference):
                with patch("selected_definition_sources.CurrentAtomLocator.locate", return_value=reference):
                    with self.assertRaises(ValueError):
                        CurrentDefinitionSources(self.root).read("CA-O-127", "operations/action.md")


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

    def test_query_manifest_resolves_moved_o158_without_rewriting_projection(self) -> None:
        structure = self.root / ".caprmedio_caprmedio/project_structure.toml"
        shutil.copyfile(ROOT / ".caprmedio_caprmedio/project_structure.toml", structure)
        first = load_selected_manifest(self.root)
        before = self.carrier.read_bytes()
        accepted = next(row for row in first["query_source_admissions"]
                        if row["route"] == "find_and_fetch_artifacts")
        old_path = self.root / accepted["workflow"]["source_path"]
        fresh_version = accepted["workflow"]["version"] + 1
        new_reference = (
            ".caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/"
            "METHODOLOGY_SOURCES/003_PROJECT_CONFIGURATION/09_operations/"
            "CA-O-158-CORE_META_MODEL-WORKFLOW--find-and-fetch-artifacts.md"
        )
        new_path = self.root / new_reference
        new_path.parent.mkdir(parents=True, exist_ok=True)
        contents = old_path.read_text(encoding="utf-8")
        contents = contents.replace('current_scope_unit: "CORE_META_MODEL"',
                                    'current_scope_unit: "PROJECT_CONFIGURATION"', 1)
        contents = contents.replace('claim_target_scope_unit: "CORE_META_MODEL"',
                                    'claim_target_scope_unit: "PROJECT_CONFIGURATION"', 1)
        contents = contents.replace(f"version: {fresh_version - 1}\n",
                                    f"version: {fresh_version}\n", 1)
        new_path.write_text(contents, encoding="utf-8")
        old_path.unlink()

        specs = selected_routes._query_admission_specs(self.root)
        query = next(row for row in specs if row["route"] == "find_and_fetch_artifacts")
        resolved = query["workflow"]
        self.assertEqual((new_reference, fresh_version),
                         (resolved["source_path"], resolved["version"]))
        self.assertEqual(hashlib.sha256(new_path.read_bytes()).hexdigest(), resolved["digest"])

        current = load_selected_manifest(self.root)
        current_query = next(row for row in current["query_source_admissions"]
                             if row["route"] == "find_and_fetch_artifacts")
        self.assertEqual(resolved, current_query["workflow"])
        self.assertEqual(before, self.carrier.read_bytes())
        self.assertEqual(resolved, next(
            row for row in load_selected_manifest(self.root)["query_source_admissions"]
            if row["route"] == "find_and_fetch_artifacts"
        )["workflow"])

    def test_missing_acceptance_plan_does_not_fallback_by_id(self) -> None:
        first = load_selected_manifest(self.root)
        pin = first["query_source_admissions"][0]["acceptance_frontier"]
        old_path = self.root / pin["source_path"]
        relocated = self.root / "elsewhere/CA-P-1618-TASK--acceptance.md"
        relocated.parent.mkdir(parents=True)
        old_path.rename(relocated)
        with patch("selected_definition_sources.CurrentAtomLocator.locate") as locate:
            with self.assertRaises(ValueError):
                CurrentDefinitionSources(self.root).read("CA-P-1618", pin["source_path"], "Plan")
        locate.assert_not_called()
