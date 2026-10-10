"""In-process MCP protocol proof for the six descriptor-backed discovery Tools."""

from __future__ import annotations

import asyncio
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import AsyncMock, patch

from mcp.client._memory import InMemoryTransport
from mcp.client.session import ClientSession
from mcp.server import MCPServer


MCP_ROOT = Path(__file__).resolve().parents[1]
TOOLS_ROOT = MCP_ROOT.parent / "201_TOOLS"
for directory in (MCP_ROOT, TOOLS_ROOT, TOOLS_ROOT / "VALIDATE_ATOMS"):
    if str(directory) not in sys.path:
        sys.path.insert(0, str(directory))

import registered_tool_registry as registry  # noqa: E402
import capability_discovery.service as discovery_service  # noqa: E402


PROVIDERS = (
    ("DISCOVER_TOOLS", "discover_tools", "DISCOVER_TOOLS/discover_tools.py", "CA-D-512", "CA-O-112"),
    ("DISCOVER_OPERATIONS", "discover_operations", "DISCOVER_OPERATIONS/discover_operations.py", "CA-D-513", "CA-O-113"),
    ("GET_EXECUTION_CONTEXT", "get_execution_context", "GET_EXECUTION_CONTEXT/get_execution_context.py", "CA-D-514", "CA-O-114"),
    ("GET_EXECUTION_STATUS", "get_execution_status", "GET_EXECUTION_STATUS/get_execution_status.py", "CA-D-515", "CA-O-115"),
    ("RESUME_EXECUTION_CONTEXT", "resume_execution_context", "RESUME_EXECUTION_CONTEXT/resume_execution_context.py", "CA-D-516", "CA-O-116"),
    ("WATCH_EXECUTION", "watch_execution", "WATCH_EXECUTION/watch_execution.py", "CA-D-517", "CA-O-117"),
)


def _bindings() -> list[dict[str, object]]:
    """One current, unique catalog row for each real descriptor provider."""

    prefix = "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS"
    return [{
        "name": name,
        "mcp_name": mcp_name,
        "entrypoint": f"{prefix}/{relative}",
        "source_atom": delivery_id,
        "source_path": f"fixtures/{name.lower()}.md",
        "sha256": "a" * 64,
        "action_ids": [action_id],
    } for name, mcp_name, relative, delivery_id, action_id in PROVIDERS]


class DiscoveryDescriptorProtocolTests(unittest.IsolatedAsyncioTestCase):
    async def test_real_discovery_descriptors_register_once_and_accept_sdk_requests(self) -> None:
        """Compile is effect-free; protocol calls use the exact descriptor models."""

        asyncio.get_running_loop().slow_callback_duration = 1.0
        with tempfile.TemporaryDirectory(dir="/private/tmp", ignore_cleanup_errors=True) as temporary:
            root = Path(temporary)
            bindings = _bindings()
            with (
                patch.object(discovery_service, "Service", autospec=True) as service_class,
                patch.object(registry, "_MODULE_CACHE", {}),
                patch.object(registry, "_binding_is_fresh", return_value=True),
            ):
                compiled = registry.compile_registry(root, bindings)
                self.assertEqual((), compiled.quarantined)
                self.assertEqual({item[1] for item in PROVIDERS}, compiled.registered_names)
                service_class.assert_not_called()

                service = service_class.return_value
                discover_tools = {"matches": [{"name": "DISCOVER_TOOLS"}], "total": 1,
                                  "next_offset": None, "coverage_issues": []}
                discover_operations = {"matches": [{"id": "CA-O-112"}], "total": 1,
                                       "next_offset": None, "coverage_issues": []}
                context = {"definition": {"id": "DISCOVER_TOOLS"}, "related_definitions": [],
                           "context_complete": True, "coverage_issues": []}
                status = {"workflow_run_id": "fixture-run", "outcome": "running", "progress": {}}
                resumed = {"workflow_run_id": "fixture-run", "pending": [], "source_drift": []}
                watched = {"status": status, "notifications": [], "changed": False,
                           "terminal": False, "cursor": "fixture-cursor"}
                service.discover.side_effect = [discover_tools, discover_operations]
                service.context.return_value = context
                service.status.return_value = (status, {"events": []})
                service.resume.return_value = resumed
                service.watch = AsyncMock(return_value=watched)

                server = MCPServer("discovery-descriptor-protocol")
                registered = registry.register_catalog_tools(server, root, bindings)
                self.assertEqual((), registered.quarantined)
                self.assertEqual({item[1] for item in PROVIDERS}, registered.registered_names)
                self.assertEqual(6, service_class.call_count)
                self.assertEqual(0, service.discover.call_count)
                service.context.assert_not_called()
                service.status.assert_not_called()
                service.resume.assert_not_called()
                service.watch.assert_not_awaited()

                async with InMemoryTransport(server, raise_exceptions=True) as streams:
                    async with ClientSession(*streams) as session:
                        await session.initialize()
                        listed = (await session.list_tools()).tools
                        names = [tool.name for tool in listed]
                        self.assertEqual({item[1] for item in PROVIDERS}, set(names))
                        self.assertEqual(len(names), len(set(names)), "MCP names must not be duplicated")
                        for tool in listed:
                            self.assertEqual(["request"], tool.input_schema["required"])
                            self.assertIn("request", tool.input_schema["properties"])

                        responses = {
                            "discover_tools": await session.call_tool(
                                "discover_tools", {"request": {"query": "fixture", "limit": 1}},
                            ),
                            "discover_operations": await session.call_tool(
                                "discover_operations", {"request": {"query": "fixture", "limit": 1}},
                            ),
                            "get_execution_context": await session.call_tool(
                                "get_execution_context", {"request": {"id": "DISCOVER_TOOLS"}},
                            ),
                            "get_execution_status": await session.call_tool(
                                "get_execution_status", {"request": {"run_id": "fixture-run"}},
                            ),
                            "resume_execution_context": await session.call_tool(
                                "resume_execution_context", {"request": {"run_id": "fixture-run"}},
                            ),
                            "watch_execution": await session.call_tool(
                                "watch_execution", {"request": {"run_id": "fixture-run", "timeout_seconds": 0}},
                            ),
                        }

                self.assertTrue(all(not response.is_error for response in responses.values()))
                self.assertEqual(discover_tools, responses["discover_tools"].structured_content)
                self.assertEqual(discover_operations, responses["discover_operations"].structured_content)
                self.assertEqual(context, responses["get_execution_context"].structured_content)
                self.assertEqual(status, responses["get_execution_status"].structured_content)
                self.assertEqual(resumed, responses["resume_execution_context"].structured_content)
                self.assertEqual(watched, responses["watch_execution"].structured_content)
                self.assertEqual(2, service.discover.call_count)
                service.context.assert_called_once()
                service.status.assert_called_once()
                service.resume.assert_called_once()
                service.watch.assert_awaited_once()


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
