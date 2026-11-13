# CA-E-812@3
# CA-E-813@2
"""Focused shared-MCP routing checks; native behavior remains a fixture."""

from __future__ import annotations

import asyncio
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

MCP = Path(__file__).resolve().parents[1]
TOOLS = MCP.parent / "FEATURE_TOOLS"
sys.path[:0] = [str(MCP), str(TOOLS), str(TOOLS / "VALIDATE_ATOMS")]

from host_runtime_config import HostRuntimeConfigError, OutsideProjectRootError, load_host_runtime_config  # noqa: E402
from mcp import types  # noqa: E402
from mcp.client._memory import InMemoryTransport  # noqa: E402
from mcp.client.session import ClientSession  # noqa: E402
from scope_declaration_test_support import write_scope_unit_declarations  # noqa: E402
from shared_gateway import SharedGateway  # noqa: E402
from tool_registry_runtime import ToolRegistryStaleError  # noqa: E402


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
        self.ready = True
        self.tools = self.tools_by_root[str(root)]
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
        write_scope_unit_declarations(root, control_root=control)
        return root

    def _config(self, max_loaded):
        self.config_path.write_text(
            "schema_version=1\n[shared_mcp]\n"
            f'projects_root="{self.projects}"\nhttp_port=8092\nmax_loaded_projects={max_loaded}\n'
        )

    def _gateway(self):
        return SharedGateway(load_host_runtime_config(self.config_path), gateway_factory=_Gateway)

    async def test_project_error_codes_do_not_depend_on_message_wording(self):
        from shared_gateway import SharedGatewayRefusal

        gateway = self._gateway()
        for error, expected in (
            (OutsideProjectRootError("a different explanation"), "outside_project_root"),
            (HostRuntimeConfigError("outside is mentioned here"), "invalid_project_root"),
        ):
            with self.subTest(error=error), patch("shared_gateway.resolve_host_project", side_effect=error):
                with self.assertRaises(SharedGatewayRefusal) as caught:
                    gateway._selection(str(self.roots[0]))
                self.assertEqual(expected, caught.exception.code)

    async def test_lifecycle_reuses_selected_project_and_rejects_replaced_root(self):
        from shared_gateway import resolve_host_project

        name = "atom_lifecycle_archive"
        _Gateway.tools_by_root = {
            str(root): [_tool(name)] for root in (*self.roots, self.nested)
        }
        gateway = self._gateway()
        await gateway.initialize()
        self.addAsyncCleanup(gateway.close)

        async def call(root):
            return await gateway.call(None, types.CallToolRequestParams(
                name=name, arguments={"project_root": str(root), "request": "x"}
            ))

        with patch("shared_gateway.resolve_host_project", wraps=resolve_host_project) as resolve:
            first = await call(self.roots[0])
            second = await call(self.roots[0])
            other = await call(self.roots[1])
            self.assertFalse(first.is_error)
            self.assertFalse(second.is_error)
            self.assertFalse(other.is_error)
            self.assertEqual(2, resolve.call_count)
            self.assertEqual(str(self.roots[1]), other.structured_content["root"])
            outside = await call(self.base)
            self.assertTrue(outside.is_error)
            self.assertEqual(["outside_project_root"], outside.structured_content["diagnostics"])

            original = self.roots[0].with_name("alpha-original")
            self.roots[0].rename(original)
            self.roots[0].mkdir()
            replaced = await call(self.roots[0])
            self.assertTrue(replaced.is_error)

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
        self.assertNotIn("echo", {tool.name for tool in conflict.tools})
        self.assertIn(
            "PROJECT_TOOL_CONTRACT_CONFLICT", [row["code"] for row in conflict.status()["warnings"]]
        )

    async def test_invalid_descriptor_is_quarantined_without_blocking_valid_tool(self):
        invalid = types.Tool(
            name="invalid",
            inputSchema={"$ref": "#/$defs/Args", "$defs": {"Args": {"type": "object"}}},
        )
        _Gateway.tools_by_root = {
            str(root): [_tool(), invalid] for root in (*self.roots, self.nested)
        }
        gateway = self._gateway()
        await gateway.initialize()
        self.addAsyncCleanup(gateway.close)

        self.assertIn(
            "PROJECT_TOOL_CONTRACT_INVALID", [row["code"] for row in gateway.status()["warnings"]]
        )
        async with InMemoryTransport(gateway.build_server(), raise_exceptions=True) as streams:
            async with ClientSession(*streams) as client:
                await client.initialize()
                self.assertEqual(
                    {"echo"}, {tool.name for tool in (await client.list_tools()).tools}
                )
                accepted = await client.call_tool(
                    "echo", {"project_root": str(self.roots[0]), "request": "ok"}
                )
                self.assertFalse(accepted.is_error)
                self.assertEqual({"request": "ok"}, accepted.structured_content["arguments"])
                rejected = await client.call_tool("invalid", {"project_root": str(self.roots[0])})
                self.assertTrue(rejected.is_error)

    async def test_stale_registration_is_rejected_before_shared_transport_dispatch(self):
        gateway = self._gateway()
        await gateway.initialize()
        self.addAsyncCleanup(gateway.close)

        class StaleRegistry:
            def ensure_current(self):
                raise ToolRegistryStaleError("tool-registry-stale")

        with (
            patch.object(_Gateway, "registry", StaleRegistry(), create=True),
            patch.object(
                _Gateway, "call", side_effect=AssertionError("must not invoke provider")
            ) as invoke,
        ):
            async with InMemoryTransport(gateway.build_server(), raise_exceptions=True) as streams:
                async with ClientSession(*streams) as client:
                    await client.initialize()
                    refused = await client.call_tool(
                        "echo", {"project_root": str(self.roots[0]), "request": "test"}
                    )
                    self.assertTrue(refused.is_error)
                    self.assertEqual(
                        ["tool_registry_stale"], refused.structured_content["diagnostics"]
                    )
                    invoke.assert_not_awaited()

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
