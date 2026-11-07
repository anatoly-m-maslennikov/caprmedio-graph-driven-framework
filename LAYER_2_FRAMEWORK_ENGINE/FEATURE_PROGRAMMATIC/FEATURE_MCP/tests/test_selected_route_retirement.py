# CA-E-796@2

"""Generic selected routes exclude retired AI-integrated routing."""

from __future__ import annotations

import importlib
from pathlib import Path
import sys
import tempfile
import unittest


MCP = Path(__file__).resolve().parents[1]
for path in (MCP, MCP.parent / "FEATURE_TOOLS"):
    if str(path) not in sys.path:
        sys.path.insert(0, str(path))


class SelectedRouteRetirementTests(unittest.TestCase):
    def test_generic_adapter_import_has_no_interactive_profile_dependency(self) -> None:
        sys.modules.pop("selected_route_interactive", None)
        sys.modules.pop("selected_route_workflow_profiles", None)
        adapter = importlib.import_module("selected_route_adapter")
        importlib.reload(adapter)
        self.assertNotIn("selected_route_interactive", sys.modules)
        self.assertNotIn("selected_route_workflow_profiles", sys.modules)

    def test_retained_route_name_is_explicitly_rejected(self) -> None:
        adapter_module = importlib.import_module("selected_route_adapter")
        with tempfile.TemporaryDirectory() as directory:
            adapter = adapter_module.SelectedRouteAdapter(directory, strict_manifest=False)
            result = adapter.invoke("run_implementation_workflow", {"request_id": "retired-route"})
        self.assertEqual("rejected", result["disposition"])
        self.assertEqual("retired", result["outcome"])
        self.assertEqual("retired-route", result["request_id"])
        self.assertEqual("run_implementation_workflow is retired", result["diagnostics"][0])

    def test_generic_adapter_dispatches_without_an_interactive_branch(self) -> None:
        adapter_module = importlib.import_module("selected_route_adapter")
        calls = []

        class Support:
            @staticmethod
            def run_selected_operation(request):
                calls.append(request)
                return {"disposition": "preview", "outcome": "prepared"}

        route_adapter = object.__new__(adapter_module.SelectedRouteAdapter)
        route_adapter._support = lambda: Support()
        request = {"mode": "preview", "operation_route": "create_atom"}
        self.assertEqual(
            {"disposition": "preview", "outcome": "prepared"},
            route_adapter._invoke_validated("create_atom", request),
        )
        self.assertEqual([request], calls)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
