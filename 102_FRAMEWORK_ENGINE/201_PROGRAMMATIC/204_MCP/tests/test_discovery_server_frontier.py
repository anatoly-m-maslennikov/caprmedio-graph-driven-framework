"""Actual server/registry/provider wiring with bounded documentary fixtures."""

from __future__ import annotations

import asyncio
import copy
import inspect
import sys
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch

MCP_ROOT = Path(__file__).resolve().parents[1]
TOOLS_ROOT = MCP_ROOT.parent / "201_TOOLS"
for directory in (MCP_ROOT, TOOLS_ROOT):
    if str(directory) not in sys.path:
        sys.path.insert(0, str(directory))

import implementation_server  # noqa: E402
import registered_tool_registry as registry  # noqa: E402
from capability_discovery.service import Service  # noqa: E402
from GET_EXECUTION_CONTEXT import get_execution_context as context_provider  # noqa: E402
from DISCOVER_TOOLS import discover_tools as tools_provider  # noqa: E402
from DISCOVER_OPERATIONS import discover_operations as operations_provider  # noqa: E402
from WATCH_EXECUTION import watch_execution as source_only_provider  # noqa: E402


class _Server:
    fail_name: str | None = None

    def __init__(self, *_args, **_kwargs):
        self.tools = {}

    def tool(self, **metadata):
        def decorate(function):
            self.tools[metadata["name"]] = function
            return function
        return decorate

    def add_tool(self, function, **metadata):
        if metadata["name"] == self.fail_name:
            raise RuntimeError("fixture registration unavailable")
        self.tools[metadata["name"]] = function


class DiscoveryServerFrontierTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(ignore_cleanup_errors=True)
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name).resolve()
        self.frontiers = []
        self.manifest = {
            "manifest_ref": "bindings.json", "canonical_manifest_sha256": "a" * 64,
            "source_freshness": {"state": "current", "digest": "b" * 64},
            "routes": [{"route": "create_atom", "workflow": {"atom_id": "CA-O-127"},
                        "ordered_actions": [{"atom_id": "CA-O-128"}]}],
        }
        self.bindings = [self.binding(provider) for provider in
                         (context_provider, tools_provider, operations_provider)]
        source_only = self.binding(source_only_provider)
        source_only["mcp_name"] = None
        self.bindings.append(source_only)
        self.bindings.append({"name": "UNAVAILABLE", "mcp_name": "unavailable_tool",
                              "entrypoint": "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/204_MCP/unavailable.py",
                              "source_atom": "CA-D-99999", "action_ids": ["CA-O-99999"],
                              "source_path": "unavailable.md", "sha256": "c" * 64})

    @staticmethod
    def binding(provider):
        return {"name": provider.TOOL_NAME, "mcp_name": provider.MCP_NAME,
                "entrypoint": provider.ENTRYPOINT, "source_atom": provider.DELIVERY_ID,
                "action_ids": [provider.ACTION_ID], "source_path": provider.DELIVERY_ID + ".md",
                "sha256": "c" * 64}

    def create_server(self, *, fail_name=None):
        _Server.fail_name = fail_name
        original_bind = Service.bind_server_frontier

        def bind(service, **frontier):
            original_bind(service, **frontier)
            self.frontiers.append(service)

        def catalog(service):
            issues = []
            # Documentary catalog rows remain unexposed unless admitted through
            # the real selected-route discovery projection below.
            rows = [{**copy.deepcopy(row), "availability": "unresolved"} for row in self.bindings]
            rows.extend(service._admitted_selected_route_tools(issues))
            atoms = {"CA-O-127": {"id": "CA-O-127", "content_role": "Operations",
                                  "scope_unit": "fixture", "content": "fixture operation"}}
            return atoms, rows, issues

        def register_routes(server, root):
            @server.tool(name="create_atom")
            def create_atom(request):
                return {"outcome": "fixture only"}
            return SimpleNamespace(public_route_names=frozenset({"create_atom"}))

        with patch.object(implementation_server, "MCPServer", _Server), \
             patch.object(implementation_server, "register_selected_routes", side_effect=register_routes), \
             patch.object(Service, "catalog", catalog), \
             patch.object(Service, "bind_server_frontier", bind), \
             patch("selected_routes.load_selected_manifest", return_value=self.manifest), \
             patch.object(registry, "_binding_is_fresh", return_value=True):
            server = implementation_server.create_server(self.root)
            context_fn = server.tools["get_execution_context"]
            context_model = inspect.signature(context_fn).parameters["request"].annotation
            context = asyncio.run(context_fn(context_model(id="CA-O-127"))).root
            tools_fn = server.tools["discover_tools"]
            query_model = inspect.signature(tools_fn).parameters["request"].annotation
            tools = asyncio.run(tools_fn(query_model(query="", availability="mcp"))).root
            if "discover_operations" in server.tools:
                operations_fn = server.tools["discover_operations"]
                operations_model = inspect.signature(operations_fn).parameters["request"].annotation
                operations = asyncio.run(operations_fn(operations_model(query="", availability="mcp"))).root
                self.assertEqual([row["id"] for row in operations["matches"]], ["CA-O-127"])
                self.assertEqual(operations["matches"][0]["tools"], ["create_atom"])
        return server, context, tools

    def test_create_server_passes_actual_selected_names_to_canonical_context_and_discovery(self):
        server, context, tools = self.create_server()
        expected = {"workflow_orchestrator", "create_atom", "get_execution_context",
                    "discover_tools", "discover_operations"}
        self.assertEqual(set(server.tools), expected)
        self.assertEqual(len(self.frontiers), 3)
        for service in self.frontiers:
            self.assertEqual(service.root, self.root)
            self.assertEqual(service.exposed, expected)
        self.assertEqual(context["definition"]["availability"], "mcp")
        self.assertEqual(context["definition"]["tools"], ["create_atom"])
        self.assertIsNotNone(context["input_schema"])
        self.assertEqual([row["name"] for row in tools["matches"]], ["create_atom"])

    def test_failed_and_source_only_registrations_never_enter_canonical_exposed_frontier(self):
        server, context, tools = self.create_server(fail_name="discover_operations")
        self.assertNotIn("discover_operations", server.tools)
        self.assertNotIn("watch_execution", server.tools)
        self.assertNotIn("unavailable_tool", server.tools)
        self.assertEqual(len(self.frontiers), 2)
        for service in self.frontiers:
            self.assertEqual(service.exposed, set(server.tools))
            self.assertNotIn("discover_operations", service.exposed)
            self.assertNotIn("watch_execution", service.exposed)
            self.assertNotIn("unavailable_tool", service.exposed)
            self.assertTrue(any(row["source"].get("source_atom") == operations_provider.DELIVERY_ID
                                for row in service.registry_quarantined))
            self.assertTrue(any(row["source"].get("name") == "UNAVAILABLE"
                                for row in service.registry_quarantined))
            self.assertTrue(any(row["source"].get("name") == "WATCH_EXECUTION"
                                and row["reason"] == "source_only" for row in service.registry_withheld))
        self.assertEqual(context["definition"]["availability"], "mcp")
        self.assertEqual([row["name"] for row in tools["matches"]], ["create_atom"])


if __name__ == "__main__":
    unittest.main()
