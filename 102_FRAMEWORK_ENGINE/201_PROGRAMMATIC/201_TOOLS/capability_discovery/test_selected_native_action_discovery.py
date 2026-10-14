"""Native Action associations from an admitted selected-route loader result."""

from __future__ import annotations

import copy
from pathlib import Path
import sys
import unittest
from unittest.mock import patch


TOOLS = Path(__file__).resolve().parents[1]
for directory in (TOOLS, TOOLS / "VALIDATE_ATOMS", TOOLS.parent / "204_MCP"):
    sys.path.insert(0, str(directory))

from capability_discovery.service import Context, Query, Service  # noqa: E402


class SelectedNativeActionDiscoveryTests(unittest.TestCase):
    def setUp(self):
        self.service = Service(TOOLS.parents[2])
        self.service.bind_server_frontier(registered_names=("update_atom",))
        # This is the admitted loader's output seam, not a bypass of manifest validation.
        self.manifest = {
            "manifest_ref": "admitted-fixture.json", "canonical_manifest_sha256": "a" * 64,
            "source_freshness": {"selected_binding_digest": "b" * 64},
            "routes": [{"route": "update_atom", "workflow": {"atom_id": "CA-O-127"},
                        "ordered_actions": [{"atom_id": "CA-O-067"}, {"atom_id": "CA-O-128"}],
                        "native_action_calls": [{"atom_id": "CA-O-030"}, {"atom_id": "CA-O-128"}]}],
        }
        self.atoms = {
            identity: {"id": identity, "content_role": "Operations", "scope_unit": "fixture",
                       "type": "Workflow" if identity == "CA-O-127" else "Action",
                       "content": "# Summary\n" + identity, "properties": {}}
            for identity in ("CA-O-127", "CA-O-067", "CA-O-128", "CA-O-030", "CA-O-999")
        }

    def catalog(self):
        issues = []
        return copy.deepcopy(self.atoms), self.service._admitted_selected_route_tools(issues), issues

    def test_native_action_uses_the_shared_route_association_in_discovery_and_context(self):
        with patch("selected_routes.load_selected_manifest", return_value=self.manifest), \
             patch.object(self.service, "catalog", side_effect=self.catalog):
            operations = self.service.discover(Query(query="CA-O-030", availability="mcp"), operations=True)
            context = self.service.context(Context(id="CA-O-030"))
            tools = self.service.discover(Query(query="CA-O-030", availability="mcp"))
            ordered = self.service.discover(Query(query="CA-O-067", availability="mcp"), operations=True)

        self.assertEqual(1, operations["total"])
        self.assertEqual("CA-O-030", operations["matches"][0]["id"])
        self.assertEqual(["update_atom"], operations["matches"][0]["tools"])
        self.assertEqual("mcp", context["definition"]["availability"])
        self.assertEqual(["update_atom"], context["definition"]["tools"])
        self.assertEqual({"manifest_ref": "admitted-fixture.json", "manifest_digest": "a" * 64},
                         context["definition"]["definition_manifest"])
        self.assertEqual(self.manifest["source_freshness"], context["definition"]["source_freshness"])
        self.assertEqual("update_atom", context["input_schema"]["properties"]["operation_route"]["const"])
        self.assertEqual(["update_atom"], [row["name"] for row in tools["matches"]])
        self.assertEqual(["CA-O-067", "CA-O-128", "CA-O-030"], tools["matches"][0]["action_ids"])
        self.assertEqual(["update_atom"], ordered["matches"][0]["tools"])

    def test_unexposed_route_does_not_make_its_native_action_available(self):
        self.service.bind_server_frontier(registered_names=())
        with patch("selected_routes.load_selected_manifest", return_value=self.manifest), \
             patch.object(self.service, "catalog", side_effect=self.catalog):
            self.assertEqual(0, self.service.discover(
                Query(query="CA-O-030", availability="mcp"), operations=True)["total"])
            context = self.service.context(Context(id="CA-O-030"))
        self.assertNotIn("tools", context["definition"])
        self.assertIsNone(context["input_schema"])

    def test_stale_invalid_and_unavailable_loader_evidence_stay_closed(self):
        for error, issue in (
            (ValueError("source pin is stale: private-secret"),
             "binding evidence stale: refresh source bindings, then re-preview selected routes"),
            (ValueError("malformed private-secret"),
             "binding evidence invalid: correct bindings, then re-preview selected routes"),
            (OSError("private-secret"),
             "binding evidence unavailable: restore or regenerate binding evidence, then re-preview selected routes"),
        ):
            with self.subTest(error=type(error).__name__, issue=issue), \
                 patch("selected_routes.load_selected_manifest", side_effect=error), \
                 patch.object(self.service, "catalog", side_effect=self.catalog):
                result = self.service.discover(Query(query="CA-O-030"), operations=True)
                self.assertEqual("unresolved", result["matches"][0]["availability"])
                self.assertEqual([], result["matches"][0]["tools"])
                self.assertEqual([issue], result["coverage_issues"])
                self.assertEqual(0, self.service.discover(
                    Query(query="CA-O-030", availability="mcp"), operations=True)["total"])
                context = self.service.context(Context(id="CA-O-030"))
                self.assertNotIn("tools", context["definition"])
                self.assertIsNone(context["input_schema"])

    def test_source_only_action_and_empty_native_calls_do_not_gain_route_associations(self):
        for identity, empty_native in (("CA-O-999", False), ("CA-O-030", True)):
            manifest = copy.deepcopy(self.manifest)
            if empty_native:
                manifest["routes"][0]["native_action_calls"] = []
            with self.subTest(identity=identity), \
                 patch("selected_routes.load_selected_manifest", return_value=manifest), \
                 patch.object(self.service, "catalog", side_effect=self.catalog):
                self.assertEqual(0, self.service.discover(
                    Query(query=identity, availability="mcp"), operations=True)["total"])
                context = self.service.context(Context(id=identity))
            self.assertNotIn("tools", context["definition"])
            self.assertIsNone(context["input_schema"])


if __name__ == "__main__":
    unittest.main()
