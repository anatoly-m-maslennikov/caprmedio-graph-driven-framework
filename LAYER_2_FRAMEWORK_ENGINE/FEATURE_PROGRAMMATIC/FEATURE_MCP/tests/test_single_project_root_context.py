# CA-E-281@18
# CA-E-599@15

"""Real MCP proof for the optional single-Project root envelope."""

from __future__ import annotations

from contextlib import asynccontextmanager
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

import httpx2
from mcp.client.session import ClientSession
from mcp.client.streamable_http import streamable_http_client


REPOSITORY = Path(__file__).resolve().parents[4]
PROGRAMMATIC = REPOSITORY / "LAYER_2_FRAMEWORK_ENGINE" / "FEATURE_PROGRAMMATIC"
MCP = PROGRAMMATIC / "FEATURE_MCP"
TOOLS = PROGRAMMATIC / "FEATURE_TOOLS"
APP = PROGRAMMATIC / "FEATURE_APPS" / "APP_WORKBENCH"
for location in (MCP, TOOLS, APP.parent, APP / "tests"):
    if str(location) not in sys.path:
        sys.path.insert(0, str(location))

from APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.service import WorkbenchService  # noqa: E402
from http_paths import MCP_PATH  # noqa: E402
from http_server import create_app  # noqa: E402
from direct_gateway import startup_selection  # noqa: E402
from project_selection import resolve_project  # noqa: E402
from scope_declaration_test_support import write_scope_unit_declarations  # noqa: E402
from smalltest_support import write_settings  # noqa: E402
from workbench_tools import WorkbenchTools  # noqa: E402


class _ConfiguredWorkbenchTools(WorkbenchTools):
    def __init__(self, root: Path, extension_directory: Path) -> None:
        super().__init__(root)
        self.extension_directory = extension_directory

    def _owner(self):
        if self._service is None:
            self._service = WorkbenchService(self.root, extension_directory=self.extension_directory)
        return self._service


class SingleProjectRootContextTests(unittest.IsolatedAsyncioTestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        base = Path(self.temporary.name).resolve()
        self.host = self._project(base / "host")
        self.container = self._project(base / "container")
        self.foreign = self._project(base / "foreign")
        self.alias = base / "container-alias"
        self.alias.symlink_to(self.container, target_is_directory=True)
        selection = startup_selection(
            self.container,
            instance_id=resolve_project(self.host).instance_id,
            host_root=self.host,
        )
        self.app = create_app(
            self.container, selection=selection,
        )
        extensions = REPOSITORY / ".caprmedio_tmp" / "workbench" / "extensions"
        self.app.gateway.workbench = _ConfiguredWorkbenchTools(self.container, extensions)

    @staticmethod
    def _project(root: Path) -> Path:
        root.mkdir()
        control = write_settings(root)
        write_scope_unit_declarations(
            root,
            (({"scope_unit_name": "ENGINE", "scope_unit_type": "Ordered", "scope_unit_label": "LAYER", "local_order": 1}),),
            control_root=control,
        )
        return root

    @asynccontextmanager
    async def session(self):
        async with self.app.starlette_app.router.lifespan_context(self.app.starlette_app):
            async with httpx2.AsyncClient(
                transport=httpx2.ASGITransport(app=self.app),
                base_url="http://127.0.0.1:18093",
            ) as client:
                transport = streamable_http_client(
                    "http://127.0.0.1:18093" + MCP_PATH, http_client=client,
                )
                streams = await transport.__aenter__()
                session = ClientSession(*streams)
                await session.__aenter__()
                try:
                    await session.initialize()
                    yield session
                finally:
                    await session.__aexit__(None, None, None)
                    await transport.__aexit__(None, None, None)

    async def test_single_project_envelope_is_advertised_validated_and_not_forwarded(self) -> None:
        async with self.session() as session:
            listed = {tool.name: tool for tool in (await session.list_tools()).tools}
            self.assertIn("workbench_ui_ping", listed)
            for name, tool in listed.items():
                with self.subTest(name=name):
                    schema = tool.input_schema
                    self.assertEqual("string", schema["properties"]["project_root"]["type"])
                    self.assertNotIn("project_root", schema.get("required", []))

            native = {tool.name: tool for tool in self.app.gateway.tools}
            self.assertNotIn("project_root", native["workbench_ui_ping"].input_schema["properties"])

            for root in (None, str(self.container), str(self.host)):
                arguments = {} if root is None else {"project_root": root}
                response = await session.call_tool("workbench_ui_ping", arguments)
                self.assertFalse(response.is_error, response.structured_content)
                self.assertEqual({"message": "Tool bridge passed"}, response.structured_content)

            checked = await session.call_tool("query_check", {
                "sql": "SELECT 1", "project_root": str(self.host),
            })
            self.assertFalse(checked.is_error, checked.structured_content)
            self.assertTrue(checked.structured_content["valid"])

            workspace = await session.call_tool("workspace_open", {
                "session_id": "root-envelope", "project_root": str(self.host),
            })
            self.assertFalse(workspace.is_error, workspace.structured_content)
            self.assertEqual("root-envelope", workspace.structured_content["workspace_id"])

            backend_call = self.app.gateway.workbench.call
            with patch.object(self.app.gateway.workbench, "call", wraps=backend_call) as backend:
                for root in (str(self.foreign), ".", "../container", str(self.alias), "\0", 1):
                    with self.subTest(root=repr(root)):
                        response = await session.call_tool("workbench_ui_ping", {"project_root": root})
                        self.assertTrue(response.is_error)
                backend.assert_not_awaited()


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
