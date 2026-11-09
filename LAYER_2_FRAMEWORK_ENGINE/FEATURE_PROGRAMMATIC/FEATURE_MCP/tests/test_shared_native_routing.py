"""Functional shared-host proof with real in-process Workbench gateways."""

from __future__ import annotations

import asyncio
from contextlib import asynccontextmanager
from pathlib import Path
import sys
import tempfile
import unittest

import httpx2
from mcp.client.session import ClientSession
from mcp.client.streamable_http import streamable_http_client

APP = Path(__file__).resolve().parents[1]
ROOT = APP.parents[2]
TOOLS = APP.parent / "FEATURE_TOOLS"
sys.path[:0] = [str(APP), str(TOOLS), str(TOOLS / "VALIDATE_ATOMS")]

from host_runtime_config import load_host_runtime_config  # noqa: E402
from direct_gateway import DirectGateway  # noqa: E402
from test_workspace_end_to_end import _ConfiguredWorkbenchTools  # noqa: E402
from smalltest_support import extension_directory  # noqa: E402
from http_paths import MCP_PATH  # noqa: E402
from scope_declaration_test_support import write_scope_unit_declarations  # noqa: E402
from shared_gateway import SharedGateway  # noqa: E402
from shared_http_server import create_app  # noqa: E402


class SharedNativeRoutingTests(unittest.IsolatedAsyncioTestCase):
    """Exercise isolated native Workbench owners through one HTTP facade."""

    def setUp(self) -> None:
        test_dir = ROOT / ".caprmedio_tmp/tests/shared-native-routing"
        test_dir.mkdir(parents=True, exist_ok=True)
        self.temporary = tempfile.TemporaryDirectory(dir=test_dir)
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name).resolve()
        self.projects = self.root / "My_Repos"
        self.projects.mkdir()
        self.projects_by_name = {name: self._project(name) for name in ("alpha", "beta")}
        self.config_path = self.root / "host_runtime.toml"
        self.config_path.write_text(
            "schema_version=1\n"
            "[shared_mcp]\n"
            f"projects_root={str(self.projects)!r}\n"
            "http_port=18092\n"
            "max_loaded_projects=2\n",
            encoding="utf-8",
        )
        self.config = load_host_runtime_config(self.config_path)

    def _project(self, name: str) -> Path:
        root = self.projects / name
        control = root / f".caprmedio_{name}"
        control.mkdir(parents=True)
        (control / "caprmedio_project_settings.toml").write_text(
            f"[project]\nname={name!r}\n[artifacts.identity]\nproject_prefix={name.upper()!r}\n"
            f"[paths]\ncontrol_root={control.name!r}\n",
            encoding="utf-8",
        )
        write_scope_unit_declarations(root, control_root=control)
        return root.resolve()

    def _native_factory(self):
        def factory(root, *, selection):
            gateway = DirectGateway(root, selection=selection)
            gateway.workbench = _ConfiguredWorkbenchTools(root, extension_directory(ROOT))
            return gateway
        return factory

    @asynccontextmanager
    async def _session(self):
        def host_factory(config):
            return SharedGateway(config, gateway_factory=self._native_factory())

        app = create_app(self.config, gateway_factory=host_factory)
        async with app.starlette_app.router.lifespan_context(app.starlette_app):
            async with httpx2.AsyncClient(
                transport=httpx2.ASGITransport(app=app),
                base_url="http://127.0.0.1:18092",
            ) as client:
                transport = streamable_http_client(
                    "http://127.0.0.1:18092" + MCP_PATH,
                    http_client=client,
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

    async def test_frontdoor_routes_same_workspace_id_to_isolated_native_owners(self):
        async with self._session() as session:
            tools = {tool.name: tool for tool in (await session.list_tools()).tools}
            self.assertEqual(28, len(tools))
            self.assertIn("project_root", tools["workbench_ui_probe"].input_schema["required"])
            uri = tools["workbench_ui_probe"].meta["ui"]["resourceUri"]
            resource = (await session.read_resource(uri)).contents[0]
            self.assertEqual("text/html;profile=mcp-app", resource.mime_type)
            responses = await asyncio.gather(*(
                session.call_tool("workspace_open", {
                    "session_id": "same-id", "project_root": str(self.projects_by_name[name]),
                }) for name in ("alpha", "beta")
            ))
            self.assertTrue(all(not response.is_error for response in responses), responses)
            self.assertEqual(["alpha", "beta"], [r.structured_content["project_name"] for r in responses])
            for root in self.projects_by_name.values():
                self.assertEqual(1, len(list((root / ".caprmedio_runtime/workbench/workspaces").glob("*.json"))))
            created = await session.call_tool("view_create", {
                "project_root": str(self.projects_by_name["alpha"]), "workspace_id": "same-id",
            })
            self.assertFalse(created.is_error, created.structured_content)
            states = await asyncio.gather(*(
                session.call_tool("workspace_get", {
                    "workspace_id": "same-id", "project_root": str(self.projects_by_name[name]),
                }) for name in ("alpha", "beta")
            ))
            self.assertEqual([2, 1], [len(r.structured_content["views"]) for r in states])

    async def test_frontdoor_refuses_missing_and_outside_project_root(self):
        async with self._session() as session:
            common = {}
            missing = await session.call_tool("workbench_ui_ping", common)
            outside = await session.call_tool(
                "workbench_ui_ping",
                {**common, "project_root": str(self.root)},
            )
            self.assertTrue(missing.is_error)
            self.assertTrue(outside.is_error)
            self.assertIn("project_root", str(missing.structured_content).lower())
            self.assertIn("outside", str(outside.structured_content).lower())


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
