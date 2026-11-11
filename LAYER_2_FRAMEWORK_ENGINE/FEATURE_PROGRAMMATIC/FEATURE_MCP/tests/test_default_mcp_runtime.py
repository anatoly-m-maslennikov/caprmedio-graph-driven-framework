"""Workbench MCP starts and closes without a provider process or generation."""

from contextlib import nullcontext
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

MCP = Path(__file__).resolve().parents[1]
sys.path[:0] = [str(MCP), str(MCP.parent / "FEATURE_TOOLS")]
from direct_gateway import DirectGateway  # noqa: E402
from http_server import create_app  # noqa: E402
import server as mcp_server  # noqa: E402


class DefaultMCPRuntimeTests(unittest.IsolatedAsyncioTestCase):
    async def test_gateway_lifecycle_needs_no_child_process(self):
        with tempfile.TemporaryDirectory() as directory:
            gateway = DirectGateway(Path(directory))
            with patch("asyncio.create_subprocess_exec", side_effect=AssertionError("unexpected child")):
                self.assertFalse(gateway.ready)
                await gateway.initialize()
                self.assertTrue(gateway.ready)
                self.assertEqual(34, len(gateway.tools))
                await gateway.close()
                self.assertFalse(gateway.ready)

    def test_http_app_uses_native_gateway(self):
        with tempfile.TemporaryDirectory() as directory:
            self.assertIsInstance(create_app(Path(directory)).gateway, DirectGateway)

    def test_stdio_uses_native_gateway(self):
        made = []

        class Gateway:
            def __init__(self, *args, **kwargs):
                made.append((args, kwargs))

            async def serve(self):
                pass

        args = type("Args", (), {
            "project_root": Path("/project"), "control_root": None,
            "instance_id": None, "host_project_root": None,
        })()
        selection = object()
        with (
            patch.object(mcp_server, "DirectGateway", Gateway),
            patch.object(mcp_server, "startup_selection", return_value=selection),
            patch.object(mcp_server, "bind_selection", return_value=nullcontext()),
        ):
            mcp_server._serve_stdio(args)
        self.assertEqual([((Path("/project"),), {"selection": selection})], made)


if __name__ == "__main__":
    unittest.main()
