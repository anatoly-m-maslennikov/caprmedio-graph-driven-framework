"""Real fifteen-route discovery; seventeen-row projection is not admission."""

import asyncio
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

TOOLS = Path(__file__).resolve().parents[1]
for directory in (TOOLS, TOOLS / "VALIDATE_ATOMS", TOOLS.parent / "204_MCP"):
    sys.path.insert(0, str(directory))

from capability_discovery.service import Context, Query, Service  # noqa: E402


class SelectedRegistryDiscoveryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        sys.path.insert(0, str(TOOLS.parent / "204_MCP" / "tests"))
        import test_selected_routes_mcp as guard_fixture

        temporary = tempfile.TemporaryDirectory(
            dir=guard_fixture.TEST_TEMP_ROOT, ignore_cleanup_errors=True
        )
        cls.addClassCleanup(temporary.cleanup)
        cls.root = Path(temporary.name).resolve()
        cls.manifest = guard_fixture.copy_complete_selected_guard_fixture(cls.root)

    def setUp(self):
        self.service = Service(self.root)
        self.service.bind_server_frontier(
            registered_names=(
                *(entry["route"] for entry in self.manifest["routes"]),
                "release_version",
                "public.release",
            )
        )

    def test_real_admitted_registry_keeps_exact_shared_context(self):
        issues = []
        rows = self.service._admitted_selected_route_tools(issues)
        self.assertEqual([], issues)
        self.assertEqual(17, len(rows))
        self.assertEqual(
            {entry["route"] for entry in self.manifest["routes"]}
            | {"release_version", "public.release"},
            {row["name"] for row in rows},
        )
        context = self.service.context(Context(id="create_atom"))
        self.assertEqual(
            "create_atom", context["input_schema"]["properties"]["operation_route"]["const"]
        )
        self.assertEqual(
            self.manifest["canonical_manifest_sha256"],
            context["definition"]["definition_manifest"]["manifest_digest"],
        )

    def test_missing_actual_registry_advertises_only_registered_direct_releases(self):
        path = self.root / self.manifest["manifest_ref"]
        saved = path.read_bytes()
        path.unlink()
        try:
            result = self.service.discover(Query(availability="mcp", limit=50))
            self.assertEqual(
                ["public.release", "release_version"], [row["name"] for row in result["matches"]]
            )
            self.assertTrue(result["coverage_issues"])
            for route in ("release_version", "public.release"):
                self.assertTrue(
                    self.service.context(Context(id=route))["definition"]["direct_route"]
                )
        finally:
            path.write_bytes(saved)

    def test_stale_actual_unselected_pin_withholds_only_ordinary_routes(self):
        route = next(row for row in self.manifest["routes"] if row["route"] == "update_atom")
        path = self.root / route["native_action_calls"][0]["source_path"]
        saved = path.read_bytes()
        path.write_bytes(saved + b"\nsource drift\n")
        try:
            issues = []
            rows = self.service._admitted_selected_route_tools(issues)
            self.assertEqual({"release_version", "public.release"}, {row["name"] for row in rows})
            self.assertEqual(
                [
                    "binding evidence stale: refresh source bindings, then re-preview selected routes"
                ],
                issues,
            )
        finally:
            path.write_bytes(saved)

    def test_old_seventeen_row_projection_cannot_override_direct_release_contracts(self):
        # Exercise the admitted-output projection seam only; current17 is not admitted.
        from selected_routes import selected_manifest_ref

        root = TOOLS.parents[2]
        manifest = json.loads((root / selected_manifest_ref(root)).read_text())
        manifest["manifest_ref"] = selected_manifest_ref(root)
        self.assertEqual(17, len(manifest["routes"]))
        rows = self.service._selected_route_rows(manifest)
        self.assertEqual(15, len(rows))
        with patch.object(self.service, "catalog", return_value=({}, rows, [])):
            for entry in manifest["routes"]:
                if entry["route"] in {"release_version", "public.release"}:
                    continue
                with self.subTest(route=entry["route"]):
                    context = self.service.context(Context(id=entry["route"]))
                    schema = context["input_schema"]
                    self.assertEqual(
                        entry["route"], schema["properties"]["operation_route"]["const"]
                    )
                    self.assertIn("request_id", schema["required"])
                    self.assertIn("definition_manifest", schema["required"])
                    self.assertFalse(schema["additionalProperties"])
                    self.assertNotIn("project_root", schema["properties"])
                    self.assertNotIn("run_id", schema["properties"])
                    self.assertEqual([entry["route"]], context["definition"]["tools"])
                    self.assertTrue(context["definition"]["selected_route"])

    def test_actual_mcp_direct_request_schemas_are_closed(self):
        from mcp.server import MCPServer
        from selected_routes import register_selected_routes

        server = MCPServer("direct-release-schema-fixture")
        register_selected_routes(server, self.root)
        tools = {tool.name: tool for tool in asyncio.run(server.list_tools())}
        for route in ("release_version", "public.release"):
            schema = tools[route].input_schema
            request_ref = schema["properties"]["request"]["$ref"].split("/")[-1]
            request = schema["$defs"][request_ref]
            self.assertFalse(request["additionalProperties"])
            self.assertEqual(["project_root", "run_id"], request["required"])
            self.assertEqual(
                {"project_root", "run_id"}
                | ({"content_draft"} if route == "public.release" else set()),
                set(request["properties"]),
            )
        draft = tools["public.release"].input_schema["$defs"]["DirectReleaseDraft"]
        self.assertFalse(draft["additionalProperties"])
        self.assertEqual(["description", "summary"], draft["required"])


if __name__ == "__main__":
    unittest.main()
