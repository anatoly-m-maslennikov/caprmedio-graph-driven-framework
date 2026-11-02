"""Independent Scope reader boundary checks against Current Declarations."""

from pathlib import Path
import sys
import unittest

TOOLS = Path(__file__).resolve().parents[1]
sys.path[:0] = [str(TOOLS), str(TOOLS / "VALIDATE_ATOMS/tests")]

import test_connector_independent_contract as contract_fixtures
from connector_scope_parsing import validate_scope_request
from connector_scope_reading import execute_scope_request
from project_selection import bind_selection, resolve_project


class ScopeReaderBoundaryIndependentTests(unittest.TestCase):
    """Read-only Scope admission keeps its selected boundary and has no effects."""

    def setUp(self):
        self.contract = contract_fixtures.IndependentConnectorContractTests()
        self.addCleanup(self.contract.doCleanups)
        (
            self.fixture,
            self.request,
            self.bindings,
            self.settings,
            self.declaration_paths,
        ) = self.contract.scope_fixture()
        self.selection = resolve_project(self.fixture.root)

    def run_request(self, bindings=None):
        with bind_selection(self.selection):
            return execute_scope_request(
                self.request,
                bindings=self.bindings if bindings is None else bindings,
                project_name="demo",
                source_view="current",
            )

    def test_scope_reader_refuses_foreign_project_without_effects(self):
        self.assertEqual(self.run_request()["errors"], [])
        marker = self.declaration_paths[1].parent.parent / "caprmedio_project_settings.toml"
        marker.parent.mkdir(parents=True, exist_ok=True)
        marker.write_text(
            '[project]\nname = "demo"\n[paths]\ncontrol_root = ".caprmedio_other"\n',
            encoding="utf-8",
        )
        before = self.contract.snapshot(self.fixture.root)
        result = self.run_request()
        self.assertTrue(result["errors"])
        self.assertEqual(result["effects"], [])
        self.assertEqual(self.contract.snapshot(self.fixture.root), before)

    def test_scope_reader_rechecks_absence_after_bound_permission_revalidation(self):
        calls = 0

        def introduce_marker(value):
            nonlocal calls
            validate_scope_request(value)
            calls += 1
            if calls == 2:
                marker = declaration_paths[1].parent.parent / "caprmedio_project_settings.toml"
                marker.parent.mkdir(parents=True, exist_ok=True)
                marker.write_text(
                    '[project]\nname = "demo"\n[paths]\ncontrol_root = ".caprmedio_other"\n',
                    encoding="utf-8",
                )

        fixture, request, bindings, _, declaration_paths = self.contract.scope_fixture(introduce_marker)
        with bind_selection(resolve_project(fixture.root)):
            result = execute_scope_request(
                request, bindings=bindings, project_name="demo", source_view="current"
            )
        self.assertGreaterEqual(calls, 2)
        self.assertTrue(result["errors"])
        self.assertEqual(result["effects"], [])
        self.assertIsNone(result["data"])


if __name__ == "__main__":
    unittest.main()
