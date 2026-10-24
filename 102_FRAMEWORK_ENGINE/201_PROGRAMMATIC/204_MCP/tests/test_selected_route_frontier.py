# implementation of:
# Evaluation: CA-E-567
"""Frozen frontier checks; optional support does not admit a production route."""

from __future__ import annotations

import copy
from pathlib import Path
import sys
import tempfile
import unittest

MCP = Path(__file__).resolve().parents[1]
ROOT = MCP.parents[2]
sys.path.insert(0, str(MCP))

from interactive_mcp_fixture import (  # noqa: E402
    _validated_manifest,
    build_interactive_mcp_fixture,
)
from mcp.server import MCPServer  # noqa: E402
from selected_route_spec import (  # noqa: E402
    ADMITTED_SELECTED_ROUTE_NAMES,
    SELECTED_ROUTE_NAMES,
)
from selected_routes import register_selected_routes  # noqa: E402


class SelectedRouteFrontierTests(unittest.IsolatedAsyncioTestCase):
    def setUp(self) -> None:
        temporary_root = ROOT / ".caprmedio_tmp/tests/selected-route-frontier"
        temporary_root.mkdir(parents=True, exist_ok=True)
        temporary = tempfile.TemporaryDirectory(dir=temporary_root)
        self.addCleanup(temporary.cleanup)
        self.fixture = build_interactive_mcp_fixture(Path(temporary.name))

    async def _registered_names(self) -> set[str]:
        server = MCPServer("selected-frontier-test")
        register_selected_routes(server, self.fixture.root)
        return {tool.name for tool in await server.list_tools()}

    async def test_fifteen_route_selection_does_not_publish_optional_move(self) -> None:
        routes = tuple(row["route"] for row in self.fixture.manifest["routes"])
        self.assertEqual(SELECTED_ROUTE_NAMES, routes)
        self.assertEqual(15, len(routes))
        names = await self._registered_names()
        self.assertTrue(set(routes) <= names)
        self.assertNotIn("move_atom", names)

    async def test_optional_move_requires_an_explicit_fixture_selection(self) -> None:
        manifest = copy.deepcopy(self.fixture.manifest)
        manifest.pop("manifest_ref")
        move = copy.deepcopy(manifest["routes"][0])
        move.update(route="move_atom", native_action_calls=[])
        manifest["routes"].insert(4, move)
        validated = _validated_manifest(self.fixture.root, manifest)
        names = tuple(row["route"] for row in validated["routes"])
        self.assertEqual(ADMITTED_SELECTED_ROUTE_NAMES, names)
        self.assertEqual(16, len(names))
        self.assertIn("move_atom", await self._registered_names())


if __name__ == "__main__":
    unittest.main()
