from __future__ import annotations

import sys
import unittest
from pathlib import Path

TOOLS = Path(__file__).resolve().parents[1]
MCP = TOOLS.parent / "204_MCP"
sys.path.insert(0, str(TOOLS))
sys.path.insert(0, str(MCP))
sys.path.insert(0, str(MCP / "tests"))
sys.path.insert(0, str(Path(__file__).resolve().parent))

import test_selected_atom_lifecycle as lifecycle_fixture  # noqa: E402
from lifecycle_intents import carrier_descriptor, move_atom_action  # noqa: E402
from selected_definition_sources import CurrentDefinitionSources  # noqa: E402
from selected_routes import SelectedRouteAdapter, canonical_digest, load_selected_manifest  # noqa: E402
from test_selected_routes_mcp import (  # noqa: E402
    FakeRunSupport,
    copy_complete_selected_guard_fixture,
)


CORE = Path(
    ".caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/"
    "METHODOLOGY_SOURCES/001_CORE_META_MODEL/09_operations"
)
PROJECT = Path(
    ".caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/"
    "METHODOLOGY_SOURCES/003_PROJECT_CONFIGURATION/09_operations"
)


class DefinitionMoveContinuationTest(unittest.TestCase):
    def setUp(self) -> None:
        self.fixture = lifecycle_fixture.SelectedAtomLifecycleTest("runTest")
        self.fixture.setUp()
        self.addCleanup(self.fixture.tearDown)
        self.root = self.fixture.root
        self._add_project_scope()
        self.manifest = copy_complete_selected_guard_fixture(self.root)

    def _add_project_scope(self) -> None:
        structure = self.root / ".caprmedio_caprmedio/project_structure.toml"
        structure.write_text(
            structure.read_text(encoding="utf-8")
            + '\n[[scope_units]]\nscope_unit_name = "PROJECT_CONFIGURATION"\n'
            + 'parent = "METHODOLOGY_SOURCES"\nscope_unit_type = "Unordered"\n'
            + 'scope_unit_label = "METHODOLOGY"\nstructural_level = 3\n'
            + 'navigational_order_number = 1\n'
            + 'authority_path = ".caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/003_PROJECT_CONFIGURATION"\n'
            + 'delivery_path = "101_FRAMEWORK_METHODOLOGY/sources/003_PROJECT_CONFIGURATION"\n',
            encoding="utf-8",
        )

    def test_moved_definition_is_reopened_for_next_admission_but_old_reader_stays_stale(self) -> None:
        pin = next(
            route["workflow"]
            for route in self.manifest["routes"]
            if route["workflow"]["atom_id"] == "CA-O-127"
        )
        source = self.root / pin["source_path"]
        destination = self.root / PROJECT / source.name.replace(
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
                    "destination_path": (PROJECT / destination.name).as_posix(),
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
