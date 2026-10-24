"""MCP regression coverage for the selected executor public error boundary."""

from __future__ import annotations

from pathlib import Path
import sys
import tempfile
import unittest
from typing import Any, Mapping
from unittest.mock import patch


MCP = Path(__file__).resolve().parents[1]
ORCHESTRATOR = MCP.parent / "203_APPS" / "WORKFLOW_ORCHESTRATOR"
TOOLS = MCP.parent / "201_TOOLS"
for import_root in (MCP, ORCHESTRATOR, TOOLS):
    if str(import_root) not in sys.path:
        sys.path.insert(0, str(import_root))

import selected_route_request  # noqa: E402
import selected_execution  # noqa: E402


class _BoundedAdapter:
    def __init__(self, root: Path) -> None:
        self.root = root

    def _result(
        self,
        request: Mapping[str, Any],
        disposition: str,
        outcome: str,
        diagnostic: str,
    ) -> dict[str, Any]:
        return {
            "request_id": request.get("request_id"),
            "disposition": disposition,
            "outcome": outcome,
            "diagnostics": [diagnostic],
        }


class SelectedExecutorExportTest(unittest.TestCase):
    def test_missing_preview_admission_is_structured_blocked_result(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            adapter = _BoundedAdapter(root)
            request = {
                "operation_route": "change_atom_status",
                "mode": "execute",
                "request_id": "fixture-request",
                "parameters": {"status": "active"},
                "proposal_receipt": {"source_freshness": {"observed": {}}},
            }
            with patch.object(
                selected_execution,
                "preflight_selected_lifecycle",
                return_value={"admission": "current"},
            ) as preflight:
                result = selected_route_request.preflight_lifecycle(adapter, request)

        assert result is not None
        preflight.assert_called_once_with(root, "change_atom_status", {"status": "active"})
        self.assertEqual("blocked", result["disposition"])
        self.assertEqual("blocked", result["outcome"])
        self.assertEqual([], result["effect_refs"])
        self.assertEqual("status-preview-admission-missing", result["lifecycle_error"]["code"])
        self.assertIn("source-derived preview admission", result["diagnostics"][0])


if __name__ == "__main__":
    unittest.main()
