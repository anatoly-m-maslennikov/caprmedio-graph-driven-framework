from __future__ import annotations

import sys
import unittest
from pathlib import Path

TOOLS = Path(__file__).resolve().parents[1]
MCP = TOOLS.parent / "FEATURE_MCP"
sys.path.insert(0, str(TOOLS))
sys.path.insert(0, str(MCP))
sys.path.insert(0, str(MCP / "tests"))
sys.path.insert(0, str(Path(__file__).resolve().parent))

import test_selected_atom_lifecycle as lifecycle_fixture  # noqa: E402
from atom_operations import remove_frontmatter_scalar, replace_frontmatter_scalar, split_frontmatter  # noqa: E402
from lifecycle_intents import carrier_descriptor, move_atom_action  # noqa: E402
from selected_definition_sources import CurrentDefinitionSources  # noqa: E402
from selected_routes import SelectedRouteAdapter, canonical_digest, load_selected_manifest  # noqa: E402
from test_selected_routes_mcp import (  # noqa: E402
    FakeRunSupport,
    copy_complete_selected_guard_fixture,
)


class DefinitionMoveContinuationTest(unittest.TestCase):
    def setUp(self) -> None:
        self.fixture = lifecycle_fixture.SelectedAtomLifecycleTest("runTest")
        self.fixture.setUp()
        self.fixture._materialize_fixture_type_definition("Operations", "Workflow")
        self.addCleanup(self.fixture.tearDown)
        self.root = self.fixture.root
        self.project_operations = self.fixture.declarations["PROJECT_CONFIGURATION"]["authority_path"] / "09_operations"
        self.manifest = copy_complete_selected_guard_fixture(self.root)

    def test_moved_definition_is_reopened_for_next_admission_but_old_reader_stays_stale(self) -> None:
        pin = next(
            route["workflow"]
            for route in self.manifest["routes"]
            if route["workflow"]["atom_id"] == "CA-O-127"
        )
        source = self.root / pin["source_path"]
        frontmatter, body = split_frontmatter(source.read_text(encoding="utf-8"))
        for field in ("local_tier", "global_tier", "author", "current_scope_unit", "claim_target_scope_unit"):
            frontmatter = remove_frontmatter_scalar(frontmatter, field)
        frontmatter = frontmatter.replace("content_role: Operations", "role: Operations")
        frontmatter = frontmatter.replace("type: Workflow", "form: Workflow")
        frontmatter = frontmatter.replace("  governs:", "  active:").replace("  depends_on:", "  passive:")
        frontmatter = frontmatter.replace(
            "relations:\n",
            "relations:\n  IS_CONTAINED_BY:\n"
            f"    scope_unit: {self.fixture.declarations['CORE_META_MODEL']['scope_id']}\n",
            1,
        )
        frontmatter = replace_frontmatter_scalar(frontmatter, "tier", "14")
        source.write_text("---\n" + frontmatter + "\n---\n" + body, encoding="utf-8")
        destination = self.project_operations / source.name.replace(
            "CORE_META_MODEL", "PROJECT_CONFIGURATION"
        )
        before = source.read_bytes()
        old_reader = CurrentDefinitionSources(self.root)
        old_reader.read("CA-O-127", pin["source_path"], "Workflow")
        archive = source.parent / "archive" / f"{source.stem}@{pin['version']}.md"

        result = move_atom_action(
            self.root,
            {
                "target": carrier_descriptor(self.root, pin["source_path"]),
                "placement": {
                    "destination_path": destination.relative_to(self.root).as_posix(),
                    "owning_scope_unit": "PROJECT_CONFIGURATION",
                    "claim_target_scope_unit": "PROJECT_CONFIGURATION",
                },
            },
            execute=True,
            authorized=True,
        )

        self.assertEqual("applied", result["outcome"])
        self.assertFalse(source.exists())
        self.assertTrue(destination.is_file())
        self.assertEqual(before, archive.read_bytes())
        with self.assertRaises((OSError, RuntimeError, ValueError)):
            old_reader.revalidate()

        current = CurrentDefinitionSources(self.root).read(
            "CA-O-127", pin["source_path"], "Workflow"
        )
        self.assertEqual(destination.relative_to(self.root).as_posix(), current["source_path"])
        self.assertEqual(pin["version"] + 1, current["version"])

        admitted = load_selected_manifest(self.root)
        create = next(route for route in admitted["routes"] if route["route"] == "create_atom")
        self.assertEqual(destination.relative_to(self.root).as_posix(), create["workflow"]["source_path"])
        self.assertEqual(pin["version"] + 1, create["workflow"]["version"])

        parameters, frontier, effects = {"route_input": "create_atom"}, ["target:fixture"], []
        request = {
            "operation_route": "create_atom",
            "request_id": "post-move-preview",
            "parameters": parameters,
            "parameters_digest": canonical_digest(parameters),
            "target_frontier": frontier,
            "target_frontier_digest": canonical_digest(frontier),
            "effects": effects,
            "effects_digest": canonical_digest(effects),
            "definition_manifest": {
                "manifest_ref": admitted["manifest_ref"],
                "manifest_digest": admitted["canonical_manifest_sha256"],
            },
            "source_freshness": admitted["source_freshness"],
            "initiative": {"initiative_id": "fixture", "instruction_summary": "post-move"},
        }
        next_admission = SelectedRouteAdapter(self.root, service=FakeRunSupport()).invoke(
            "create_atom", request
        )
        self.assertEqual("preview", next_admission["disposition"])


if __name__ == "__main__":
    unittest.main()
