"""Focused functional checks for selected-route manifest diagnostics."""

from __future__ import annotations

import unittest

from test_selected_routes_mcp import SelectedRoutesMCPTest


class SelectedRouteManifestDiagnosticsTest(unittest.TestCase):
    def setUp(self) -> None:
        fixture = SelectedRoutesMCPTest("runTest")
        fixture.setUp()
        self.addCleanup(fixture.doCleanups)
        self.fixture = fixture

    def test_definition_manifest_distinguishes_malformed_from_stale(self) -> None:
        malformed = self.fixture.request("create_atom")
        malformed["definition_manifest"] = {
            "manifest_ref": self.fixture.manifest["manifest_ref"],
        }
        result = self.fixture.adapter.invoke("create_atom", malformed)
        self.assertEqual("definition_manifest is invalid", result["diagnostics"][0])

        stale = self.fixture.request("create_atom")
        stale["definition_manifest"]["manifest_digest"] = "b" * 64
        result = self.fixture.adapter.invoke("create_atom", stale)
        self.assertEqual(
            "definition_manifest is stale or does not identify the canonical binding",
            result["diagnostics"][0],
        )


if __name__ == "__main__":
    unittest.main()
