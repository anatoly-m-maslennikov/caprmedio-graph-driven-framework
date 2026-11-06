# CA-R-2902@4
# CA-M-476@4
# CA-E-684@5
# CA-D-681@7

"""Resource-registry checks for the native Workbench MCP App."""

from __future__ import annotations

import asyncio
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

from mcp import MCPError, types


EXTENSION = Path(__file__).resolve().parents[1]
APPS = EXTENSION.parents[1]
if str(APPS) not in sys.path:
    sys.path.insert(0, str(APPS))

from APP_WORKBENCH.FEATURE_CODEX_EXTENSION import mcp_app_probe  # noqa: E402


class MCPAppProbeTests(unittest.TestCase):
    def test_registry_lists_probe_and_workbench_resources(self) -> None:
        resources = asyncio.run(mcp_app_probe.list_resources(None, None)).resources

        self.assertEqual([mcp_app_probe.URI, mcp_app_probe.WORKBENCH_URI],
                         [resource.uri for resource in resources])
        self.assertTrue(all(resource.mime_type == mcp_app_probe.MIME_TYPE for resource in resources))

    def test_read_workbench_uses_built_resource(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            built = Path(temporary) / "mcp-app.html"
            built.write_text("<html>built workbench</html>", encoding="utf-8")
            with patch.object(mcp_app_probe, "WORKBENCH_HTML", built):
                result = asyncio.run(mcp_app_probe.read_resource(
                    None, types.ReadResourceRequestParams(uri=mcp_app_probe.WORKBENCH_URI),
                ))

        self.assertEqual(mcp_app_probe.WORKBENCH_URI, result.contents[0].uri)
        self.assertEqual(mcp_app_probe.MIME_TYPE, result.contents[0].mime_type)
        self.assertEqual("<html>built workbench</html>", result.contents[0].text)

    def test_missing_workbench_resource_is_an_mcp_error(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            missing = Path(temporary) / "mcp-app.html"
            with patch.object(mcp_app_probe, "WORKBENCH_HTML", missing):
                with self.assertRaises(MCPError):
                    asyncio.run(mcp_app_probe.read_resource(
                        None, types.ReadResourceRequestParams(uri=mcp_app_probe.WORKBENCH_URI),
                    ))

    def test_probe_contract_is_retained(self) -> None:
        self.assertEqual(("workbench_ui_probe", "workbench_ui_ping"), mcp_app_probe.TOOL_NAMES)
        self.assertEqual({"message": "CAPRMEDIO MCP App resource loaded"},
                         mcp_app_probe.call("workbench_ui_probe"))
        self.assertEqual({"message": "Tool bridge passed"}, mcp_app_probe.call("workbench_ui_ping"))


if __name__ == "__main__":
    unittest.main()
