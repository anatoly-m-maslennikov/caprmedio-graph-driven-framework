"""Focused shared-MCP routing checks; native behavior remains a fixture."""

from __future__ import annotations

import asyncio
import json
from pathlib import Path
import sys
import tempfile
from types import SimpleNamespace
import unittest

MCP = Path(__file__).resolve().parents[1]
TOOLS = MCP.parent / "201_TOOLS"
sys.path[:0] = [str(MCP), str(TOOLS), str(TOOLS / "VALIDATE_ATOMS")]

from host_runtime_config import load_host_runtime_config  # noqa: E402
from mcp import types  # noqa: E402
from shared_gateway import SharedGateway  # noqa: E402


def _tool(name="echo", field="request"):
    return types.Tool(
        name=name,
        inputSchema={
            "type": "object",
            "properties": {field: {"type": "string"}},
            "required": [field],
            "additionalProperties": False,
        },
        outputSchema={"type": "object"},
    )


class _Gateway:
    tools_by_root = {}
    blacklist_by_root = {}
    hold = None

    def __init__(self, root, *, selection):
        self.root, self.selection = Path(root), selection
        self.tool_blacklist = self.blacklist_by_root.get(str(root), frozenset())
        self.active = SimpleNamespace(tools=self.tools_by_root[str(root)])
        self.closed = False

    async def initialize(self):
        return None

    async def close(self):
        self.closed = True

    async def call(self, _context, params):
        if self.hold is not None:
            await self.hold.wait()
        return types.CallToolResult(
            content=[],
            structuredContent={
                "root": str(self.root),
                "arguments": params.arguments,
            },
        )


class SharedGatewayTests(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.base = Path(self.temporary.name).resolve()
        self.projects = self.base / "My_Repos"
        self.projects.mkdir()
        self.roots = [self._project(name) for name in ("alpha", "beta")]
        self.nested = self._project("nested/project")
        self.config_path = self.base / "runtime.toml"
        self._config(max_loaded=2)
        _Gateway.tools_by_root = {str(root): [_tool()] for root in (*self.roots, self.nested)}
        _Gateway.blacklist_by_root, _Gateway.hold = {}, None

    def _project(self, name):
        root = self.projects / name
        control = root / (".caprmedio_" + root.name)
        control.mkdir(parents=True)
        (control / "caprmedio_project_settings.toml").write_text(
            f'[project]\nname="{root.name}"\n[paths]\ncontrol_root="{control.name}"\n'
            f'[artifacts.identity]\nproject_prefix="{root.name.upper()}"\n'
        )
        (control / "project_structure.toml").write_text("schema_version=1\nscope_units=[]\n")
        return root

    def _config(self, max_loaded):
        self.config_path.write_text(
            "schema_version=1\n[shared_mcp]\n"
            f'projects_root="{self.projects}"\nhttp_port=8092\nmax_loaded_projects={max_loaded}\n'
        )

    def _gateway(self):
        return SharedGateway(load_host_runtime_config(self.config_path), gateway_factory=_Gateway)

    async def test_concurrent_projects_keep_identical_native_payloads_isolated(self):
        gateway = self._gateway()
        await gateway.initialize()
        self.addAsyncCleanup(gateway.close)
        first, second = await asyncio.gather(
            *[
                gateway.call(
                    None,
                    types.CallToolRequestParams(
                        name="echo",
                        arguments={
                            "project_root": str(root),
                            "request": "same-id",
                        },
                    ),
                )
                for root in self.roots
            ]
        )
        self.assertEqual(
            [str(root) for root in self.roots],
            [
                first.structured_content["root"],
                second.structured_content["root"],
            ],
        )
        self.assertEqual({"request": "same-id"}, first.structured_content["arguments"])
        self.assertEqual({"request": "same-id"}, second.structured_content["arguments"])

    async def test_disabled_outside_and_schema_conflict_refuse(self):
        _Gateway.blacklist_by_root = {str(self.roots[0]): frozenset({"echo"})}
        gateway = self._gateway()
        await gateway.initialize()
        self.addAsyncCleanup(gateway.close)
        disabled = await gateway.call(
            None,
            types.CallToolRequestParams(
                name="echo", arguments={"project_root": str(self.roots[0]), "request": "x"}
            ),
        )
        outside = await gateway.call(
            None,
            types.CallToolRequestParams(
                name="echo", arguments={"project_root": str(self.base), "request": "x"}
            ),
        )
        self.assertTrue(disabled.is_error)
        self.assertTrue(outside.is_error)
        self.assertEqual(["outside_project_root"], outside.structured_content["diagnostics"])

        _Gateway.blacklist_by_root = {}
        _Gateway.tools_by_root[str(self.roots[1])] = [_tool(field="other")]
        conflict = self._gateway()
        await conflict.initialize()
        self.addAsyncCleanup(conflict.close)
        self.assertNotIn("echo", {tool.name for tool in conflict.active.tools})
        self.assertIn(
            "PROJECT_TOOL_CONTRACT_CONFLICT", [row["code"] for row in conflict.status()["warnings"]]
        )

    async def test_nested_project_uses_known_tool_but_new_name_and_secret_refuse(self):
        _Gateway.tools_by_root[str(self.nested)] = [_tool(), _tool(name="new_tool")]
        gateway = self._gateway()
        await gateway.initialize()
        self.addAsyncCleanup(gateway.close)
        known = await gateway.call(
            None,
            types.CallToolRequestParams(
                name="echo", arguments={"project_root": str(self.nested), "request": "x"}
            ),
        )
        new = await gateway.call(
            None,
            types.CallToolRequestParams(
                name="new_tool", arguments={"project_root": str(self.nested), "request": "x"}
            ),
        )
        secret = self.base / "SECRET_PROJECT_ROOT"
        secret.mkdir()
        rejected = await gateway.call(
            None,
            types.CallToolRequestParams(
                name="echo", arguments={"project_root": str(secret), "request": "x"}
            ),
        )
        self.assertEqual(str(self.nested), known.structured_content["root"])
        self.assertEqual(["tool_unavailable"], new.structured_content["diagnostics"])
        self.assertNotIn("SECRET_PROJECT_ROOT", json.dumps(rejected.model_dump(by_alias=True)))


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
