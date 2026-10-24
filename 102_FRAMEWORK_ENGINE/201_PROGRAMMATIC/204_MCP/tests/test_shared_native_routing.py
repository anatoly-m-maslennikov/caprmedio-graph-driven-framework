"""Functional shared-host proof with real native Gateway child processes."""

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
TOOLS = APP.parent / "201_TOOLS"
sys.path[:0] = [str(APP), str(TOOLS), str(TOOLS / "VALIDATE_ATOMS")]

from host_runtime_config import load_host_runtime_config  # noqa: E402
from hot_reload import Gateway  # noqa: E402
from shared_gateway import SharedGateway  # noqa: E402
from shared_http_server import create_app  # noqa: E402


class SharedNativeRoutingTests(unittest.IsolatedAsyncioTestCase):
    """Exercise the HTTP facade through two real Project-local MCP children."""

    def setUp(self) -> None:
        test_dir = ROOT / ".caprmedio_tmp/tests/shared-native-routing"
        test_dir.mkdir(parents=True, exist_ok=True)
        self.temporary = tempfile.TemporaryDirectory(dir=test_dir)
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name).resolve()
        self.projects = self.root / "My_Repos"
        self.projects.mkdir()
        self.projects_by_name = {name: self._project(name) for name in ("alpha", "beta")}
        self.provider = self.root / "native_provider.py"
        self.provider.write_text(
            "import os\n"
            "import sys\n"
            "from pathlib import Path\n"
            "from mcp.server import MCPServer\n"
            "\n"
            "server = MCPServer('shared-native-routing-fixture')\n"
            "project_root = str(Path(sys.argv[sys.argv.index('--project-root') + 1]).resolve())\n"
            "@server.tool(name='read_effect_free', structured_output=True)\n"
            "def read_effect_free(atom_id: str, run_id: str, payload: str) -> dict[str, str]:\n"
            "    return {'atom_id': atom_id, 'run_id': run_id, 'payload': payload,\n"
            "            'native_project_root': project_root, 'native_pid': str(os.getpid())}\n"
            "\n"
            "server.run(transport='stdio')\n",
            encoding="utf-8",
        )
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
        (control / "project_structure.toml").write_text(
            "schema_version=1\nscope_units=[]\n",
            encoding="utf-8",
        )
        return root.resolve()

    def _native_factory(self):
        provider = self.provider

        def factory(root, *, selection):
            return Gateway(root, implementation=provider, selection=selection)

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
                    "http://127.0.0.1:18092/mcp",
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

    async def test_frontdoor_routes_same_ids_to_isolated_native_children(self):
        async with self._session() as session:
            tools = {tool.name: tool for tool in (await session.list_tools()).tools}
            self.assertIn("read_effect_free", tools)
            schema = tools["read_effect_free"].input_schema
            self.assertEqual(
                {"atom_id", "run_id", "payload", "project_root"},
                set(schema["properties"]),
            )
            self.assertEqual(
                {"atom_id", "run_id", "payload", "project_root"},
                set(schema["required"]),
            )
            self.assertEqual("string", schema["properties"]["atom_id"]["type"])
            self.assertEqual("string", schema["properties"]["run_id"]["type"])
            self.assertEqual("string", schema["properties"]["payload"]["type"])

            request = {"atom_id": "atom-same", "run_id": "run-same", "payload": "unchanged"}
            responses = await asyncio.gather(
                *(
                    session.call_tool(
                        "read_effect_free",
                        {**request, "project_root": str(self.projects_by_name[name])},
                    )
                    for name in ("alpha", "beta")
                )
            )

            self.assertTrue(all(not response.is_error for response in responses))
            observed = [response.structured_content for response in responses]
            self.assertEqual(
                [request] * 2,
                [{key: row[key] for key in request} for row in observed],
            )
            self.assertEqual(
                set(self.projects_by_name.values()),
                {Path(row["native_project_root"]) for row in observed},
            )
            self.assertEqual(2, len({row["native_pid"] for row in observed}))

    async def test_frontdoor_refuses_missing_and_outside_project_root(self):
        async with self._session() as session:
            common = {"atom_id": "atom-same", "run_id": "run-same", "payload": "unchanged"}
            missing = await session.call_tool("read_effect_free", common)
            outside = await session.call_tool(
                "read_effect_free",
                {**common, "project_root": str(self.root)},
            )
            self.assertTrue(missing.is_error)
            self.assertTrue(outside.is_error)
            self.assertIn("project_root", str(missing.structured_content).lower())
            self.assertIn("outside", str(outside.structured_content).lower())


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
