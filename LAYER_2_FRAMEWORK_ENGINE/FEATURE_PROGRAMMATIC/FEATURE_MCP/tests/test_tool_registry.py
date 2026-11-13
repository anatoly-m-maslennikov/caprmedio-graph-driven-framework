# CA-E-798@5
# CA-E-810@3
# CA-E-811@3
# CA-E-812@3
# CA-E-813@2
# CA-E-814@1
# CA-E-820@2

"""Functional registry generation and generic MCP Provider dispatch."""

from __future__ import annotations

import json
from pathlib import Path
import sys
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import patch
from uuid import uuid4

from mcp.client._memory import InMemoryTransport
from mcp.client.session import ClientSession
from mcp import types


MCP = Path(__file__).resolve().parents[1]
sys.path[:0] = [str(MCP), str(MCP.parent / "FEATURE_TOOLS")]
from direct_gateway import DirectGateway  # noqa: E402
from generate_tool_registry import generate  # noqa: E402
from shared_project_catalog import SharedToolFrontier, _discover_project  # noqa: E402
from tool_registry_assets import FEATURE_RELATIVE, ToolRegistryAssetError  # noqa: E402
from tool_registry_runtime import (  # noqa: E402
    ToolRegistryRuntimeError, ToolRegistryStaleError, load_active_registry,
)


def _provider_source() -> str:
    return '''from mcp import types
class Provider:
    async def call(self, name, arguments):
        return {"name": name, "arguments": arguments}
    async def close(self):
        return None
def create_provider(root, gateway):
    return Provider()
def tool_descriptors():
    schema = {"type": "object", "properties": {}, "additionalProperties": False}
    return (types.Tool(name="demo", description="Demo", input_schema=schema),
            types.Tool(name="blocked", description="Blocked", input_schema=schema))
'''


def _mixed_descriptor_provider_source() -> str:
    return '''from mcp import types
class Provider:
    async def call(self, name, arguments):
        return {"name": name, "arguments": arguments}
    async def close(self):
        return None
def create_provider(root, gateway):
    return Provider()
def tool_descriptors():
    valid = {"type": "object", "properties": {}, "additionalProperties": False}
    invalid = {"type": "not-a-json-schema-type"}
    return (types.Tool(name="demo", description="Demo", input_schema=valid),
            types.Tool(name="broken", description="Broken", input_schema=invalid))
'''


def _drifting_provider_source() -> str:
    return '''import asyncio
from pathlib import Path
from mcp import types
calls = 0
class Provider:
    async def prepare_arguments(self, name, arguments, context):
        await asyncio.sleep(0)
        registry = Path(__file__).with_name("tool_registry.json")
        registry.write_text(registry.read_text(encoding="utf-8") + "\\n", encoding="utf-8")
        return arguments
    async def call(self, name, arguments):
        global calls
        calls += 1
        return {"ok": True}
    async def close(self):
        return None
def create_provider(root, gateway):
    return Provider()
def tool_descriptors():
    schema = {"type": "object", "properties": {}, "additionalProperties": False}
    return (types.Tool(name="demo", description="Demo", input_schema=schema),)
'''


def _context_provider_source() -> str:
    return '''from mcp import types
from runtime_request_context import current_request_context
calls = 0
class Provider:
    async def call(self, name, arguments):
        global calls
        calls += 1
        current = current_request_context()
        return {"native": arguments, "caller": current.session_id if current else None}
    async def close(self):
        return None
def create_provider(root, gateway):
    return Provider()
def tool_descriptors():
    schema = {"type": "object", "properties": {"session_id": {"type": "string"}}, "additionalProperties": False}
    return (types.Tool(name="demo", description="Demo", input_schema=schema),)
'''


def _schema_provider_source() -> str:
    return '''from mcp import types
calls = 0
closed = 0
class Provider:
    async def call(self, name, arguments):
        global calls
        calls += 1
        return {"ok": "invalid"}
    async def close(self):
        global closed
        closed += 1
def create_provider(root, gateway):
    return Provider()
def tool_descriptors():
    input_schema = {"type": "object", "properties": {"value": {"type": "string"}}, "required": ["value"], "additionalProperties": False}
    output_schema = {"type": "object", "properties": {"ok": {"type": "boolean"}}, "required": ["ok"], "additionalProperties": False}
    return (types.Tool(name="demo", description="Demo", input_schema=input_schema, output_schema=output_schema),)
'''


def _lifecycle_provider_source() -> str:
    return '''from mcp import types
created = 0
closed = 0
class Provider:
    async def call(self, name, arguments):
        return {"ok": True}
    async def close(self):
        global closed
        closed += 1
def create_provider(root, gateway):
    global created
    created += 1
    return Provider()
def tool_descriptors():
    schema = {"type": "object", "properties": {}, "additionalProperties": False}
    output = {"type": "object", "properties": {"ok": {"type": "boolean"}}, "required": ["ok"], "additionalProperties": False}
    return (types.Tool(name="demo", description="Demo", input_schema=schema, output_schema=output),)
'''


def _saved_id_provider_source() -> str:
    return '''from mcp import types
class Provider:
    async def call(self, name, arguments):
        return {"saved_query_id": "q_0123456789abcdef0123456789abcdef"}
    async def close(self):
        return None
def create_provider(root, gateway):
    return Provider()
def tool_descriptors():
    schema = {"type": "object", "properties": {}, "additionalProperties": False}
    output = {"type": "object", "properties": {"saved_query_id": {"type": "string"}}, "required": ["saved_query_id"], "additionalProperties": False}
    return (types.Tool(name="demo", description="Demo", input_schema=schema, output_schema=output),)
'''


def _partial_provider_source() -> str:
    return '''from mcp import types
created = 0
closed = 0
class Provider:
    async def close(self):
        global closed
        closed += 1
def create_provider(root, gateway):
    global created
    created += 1
    return Provider()
def tool_descriptors():
    schema = {"type": "object", "properties": {}, "additionalProperties": False}
    return (types.Tool(name="demo", description="Demo", input_schema=schema),)
'''


class ToolRegistryTests(unittest.IsolatedAsyncioTestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.package = Path(self.temporary.name) / "package"
        self.feature = self.package / FEATURE_RELATIVE
        self.feature.mkdir(parents=True)
        self.module = "provider_" + uuid4().hex
        (self.feature / f"{self.module}.py").write_text(_provider_source(), encoding="utf-8")
        self._write_inventory()

    def tearDown(self) -> None:
        sys.modules.pop(self.module, None)

    def _write_inventory(self, *, blacklist: list[str] | None = None) -> None:
        payload = {
            "schema_version": 1,
            "mcp_blacklist": ["blocked"] if blacklist is None else blacklist,
            "providers": [{
                "provider_id": "demo_provider",
                "module": self.module,
                "factory": "create_provider",
                "descriptor_factory": "tool_descriptors",
            }],
        }
        (self.feature / "tool_providers.json").write_text(json.dumps(payload), encoding="utf-8")

    def _write_provider(self, source: str) -> None:
        sys.modules.pop(self.module, None)
        (self.feature / f"{self.module}.py").write_text(source, encoding="utf-8")

    def _registry(self, root: Path, gateway: object):
        return load_active_registry(self.feature, root, gateway)

    def test_generator_writes_models_and_filters_global_blacklist(self) -> None:
        registry = json.loads(generate(self.package).read_text(encoding="utf-8"))
        self.assertEqual(["demo"], registry["public_tools"])
        self.assertEqual(["demo", "blocked"], [tool["name"] for tool in registry["providers"][0]["tools"]])
        self.assertEqual(["blocked"], registry["mcp_blacklist"])

    def test_generator_refuses_invalid_inventory_before_writing(self) -> None:
        (self.feature / "tool_providers.json").write_text('{"schema_version": 1}', encoding="utf-8")
        with self.assertRaises(ToolRegistryAssetError):
            generate(self.package)
        self.assertFalse((self.feature / "tool_registry.json").exists())

    def test_generator_refuses_an_invalid_registered_tool_schema(self) -> None:
        self._write_provider(
            _provider_source().replace(
                'schema = {"type": "object", "properties": {}, "additionalProperties": False}',
                'schema = {"type": "not-a-json-schema-type"}',
            )
        )
        with self.assertRaises(ToolRegistryAssetError):
            generate(self.package)
        self.assertFalse((self.feature / "tool_registry.json").exists())

    async def test_real_transport_quarantines_one_invalid_installed_descriptor(self) -> None:
        self._write_provider(_mixed_descriptor_provider_source())
        with self.assertLogs("generate_tool_registry", level="WARNING") as generated:
            generate(self.package)
        self.assertIn("broken", generated.output[0])
        root = Path(self.temporary.name).resolve()

        def registry_loader(_asset: Path, selected: Path, gateway: object):
            return self._registry(selected, gateway)

        with patch("direct_gateway.load_active_registry", side_effect=registry_loader):
            gateway = DirectGateway(root)
            with self.assertLogs("generate_tool_registry", level="WARNING") as loaded:
                await gateway.initialize()
            self.assertIn("broken", loaded.output[0])
            try:
                async with InMemoryTransport(gateway.build_server(), raise_exceptions=True) as streams:
                    async with ClientSession(*streams) as client:
                        await client.initialize()
                        self.assertEqual({"demo"}, {tool.name for tool in (await client.list_tools()).tools})
                        accepted = await client.call_tool("demo", {})
                        self.assertFalse(accepted.is_error)
                        rejected = await client.call_tool("broken", {})
                        self.assertTrue(rejected.is_error)
            finally:
                await gateway.close()

    def test_duplicate_identity_refuses_publication_even_if_one_descriptor_is_invalid(self) -> None:
        self._write_provider(_mixed_descriptor_provider_source().replace('name="broken"', 'name="demo"'))
        with self.assertRaises(ToolRegistryAssetError):
            generate(self.package)
        self.assertFalse((self.feature / "tool_registry.json").exists())

    async def test_invalid_only_provider_does_not_block_an_independent_provider(self) -> None:
        invalid_module = "provider_" + uuid4().hex
        self.addCleanup(sys.modules.pop, invalid_module, None)
        source = _mixed_descriptor_provider_source().replace(
            'types.Tool(name="demo", description="Demo", input_schema=valid),\n            ', ""
        ).replace('input_schema=invalid))', 'input_schema=invalid),)')
        (self.feature / f"{invalid_module}.py").write_text(source, encoding="utf-8")
        inventory_path = self.feature / "tool_providers.json"
        inventory = json.loads(inventory_path.read_text(encoding="utf-8"))
        inventory["providers"].append({
            "provider_id": "invalid_provider", "module": invalid_module,
            "factory": "create_provider", "descriptor_factory": "tool_descriptors",
        })
        inventory_path.write_text(json.dumps(inventory), encoding="utf-8")
        with self.assertLogs("generate_tool_registry", level="WARNING"):
            generate(self.package)
        with self.assertLogs("generate_tool_registry", level="WARNING"):
            active = self._registry(Path(self.temporary.name).resolve(), object())
        self.assertEqual({"demo"}, {tool.name for tool in active.tools})
        self.assertEqual({"name": "demo", "arguments": {}}, await active.call("demo", {}))
        await active.close()

    def test_duplicate_identity_across_providers_fails_even_when_one_is_invalid(self) -> None:
        self._write_provider(_mixed_descriptor_provider_source())
        second_module = "provider_" + uuid4().hex
        self.addCleanup(sys.modules.pop, second_module, None)
        source = _provider_source().replace('name="demo"', 'name="broken"')
        (self.feature / f"{second_module}.py").write_text(source, encoding="utf-8")
        inventory_path = self.feature / "tool_providers.json"
        inventory = json.loads(inventory_path.read_text(encoding="utf-8"))
        inventory["providers"].append({
            "provider_id": "second_provider", "module": second_module,
            "factory": "create_provider", "descriptor_factory": "tool_descriptors",
        })
        inventory_path.write_text(json.dumps(inventory), encoding="utf-8")
        with self.assertRaisesRegex(ToolRegistryAssetError, "name-duplicates"):
            generate(self.package)
        self.assertFalse((self.feature / "tool_registry.json").exists())

    async def test_real_transport_dispatches_added_provider_and_denies_global_name(self) -> None:
        generate(self.package)
        root = Path(self.temporary.name).resolve()

        def registry_loader(_asset: Path, selected: Path, gateway: object):
            return self._registry(selected, gateway)

        with patch("direct_gateway.load_active_registry", side_effect=registry_loader):
            gateway = DirectGateway(root)
            await gateway.initialize()
            try:
                async with InMemoryTransport(gateway.build_server(), raise_exceptions=True) as streams:
                    async with ClientSession(*streams) as client:
                        await client.initialize()
                        self.assertEqual({"demo"}, {tool.name for tool in (await client.list_tools()).tools})
                        accepted = await client.call_tool("demo", {})
                        self.assertFalse(accepted.is_error)
                        self.assertEqual({"name": "demo", "arguments": {}}, accepted.structured_content)
                        rejected = await client.call_tool("blocked", {})
                        self.assertTrue(rejected.is_error)
                        self.assertEqual(["Unknown Tool"], rejected.structured_content["diagnostics"])
            finally:
                await gateway.close()

    async def test_tools_list_exposes_admitted_registry_metadata_without_execution(self) -> None:
        source = _schema_provider_source().replace(
            'return (types.Tool(name="demo", description="Demo", input_schema=input_schema, output_schema=output_schema),)',
            'return tuple(types.Tool(name=name, description=name + " description", '
            'input_schema=input_schema, output_schema=output_schema) '
            'for name in ("demo", "blocked", "project_blocked"))',
        ).replace(
            'return {"ok": "invalid"}',
            'open(__file__ + ".written", "w").write(arguments["value"])\n        return {"ok": "invalid"}',
        )
        self._write_provider(source)
        registry_path = generate(self.package)
        installed = json.loads(registry_path.read_text(encoding="utf-8"))
        descriptor = next(t for t in installed["providers"][0]["tools"] if t["name"] == "demo")
        root = Path(self.temporary.name).resolve()
        control = root / ".caprmedio_fixture"
        control.mkdir()
        (control / "caprmedio_project_settings.toml").write_text(
            '[paths]\ncontrol_root = ".caprmedio_fixture"\n'
            '[project_mcp]\ntool_blacklist = ["project_blocked"]\n', encoding="utf-8",
        )

        def registry_loader(_asset: Path, selected: Path, gateway: object):
            return self._registry(selected, gateway)

        with patch("direct_gateway.load_active_registry", side_effect=registry_loader):
            gateway = DirectGateway(root)
            await gateway.initialize()
            try:
                before = {p.relative_to(control) for p in control.rglob("*")}
                async with InMemoryTransport(gateway.build_server(), raise_exceptions=True) as streams:
                    async with ClientSession(*streams) as client:
                        await client.initialize()
                        listed = (await client.list_tools()).tools
                self.assertEqual(["demo"], [tool.name for tool in listed])
                self.assertEqual(descriptor["description"], listed[0].description)
                self.assertEqual(descriptor["inputSchema"]["required"], listed[0].input_schema["required"])
                self.assertEqual(descriptor["inputSchema"]["properties"]["value"],
                                 listed[0].input_schema["properties"]["value"])
                self.assertIsNone(gateway.registry.bindings[0].provider)
                self.assertEqual(0, sys.modules[self.module].calls)
                self.assertFalse((self.feature / f"{self.module}.py.written").exists())
                self.assertEqual(before, {p.relative_to(control) for p in control.rglob("*")})
            finally:
                await gateway.close()

    async def test_real_transport_rejects_a_changed_registration_before_invocation(self) -> None:
        registry_path = generate(self.package)
        root = Path(self.temporary.name).resolve()

        def registry_loader(_asset: Path, selected: Path, gateway: object):
            return self._registry(selected, gateway)

        with patch("direct_gateway.load_active_registry", side_effect=registry_loader):
            gateway = DirectGateway(root)
            await gateway.initialize()
            try:
                async with InMemoryTransport(gateway.build_server(), raise_exceptions=True) as streams:
                    async with ClientSession(*streams) as client:
                        await client.initialize()
                        registry_path.write_text(
                            registry_path.read_text(encoding="utf-8") + "\n", encoding="utf-8"
                        )
                        refused = await client.call_tool("demo", {})
                        self.assertTrue(refused.is_error)
                        self.assertEqual("rejected", refused.structured_content["outcome"])
                        self.assertEqual(
                            ["tool_registry_stale"], refused.structured_content["diagnostics"]
                        )
                        self.assertIsNone(gateway.registry.bindings[0].provider)
            finally:
                await gateway.close()

    async def test_real_transport_refuses_registration_changed_during_prepare(self) -> None:
        self._write_provider(_drifting_provider_source())
        generate(self.package)
        root = Path(self.temporary.name).resolve()

        def registry_loader(_asset: Path, selected: Path, gateway: object):
            return self._registry(selected, gateway)

        with patch("direct_gateway.load_active_registry", side_effect=registry_loader):
            gateway = DirectGateway(root)
            await gateway.initialize()
            try:
                async with InMemoryTransport(gateway.build_server(), raise_exceptions=True) as streams:
                    async with ClientSession(*streams) as client:
                        await client.initialize()
                        refused = await client.call_tool("demo", {})
                        self.assertTrue(refused.is_error)
                        self.assertEqual(["tool_registry_stale"], refused.structured_content["diagnostics"])
                        self.assertEqual(0, sys.modules[self.module].calls)
            finally:
                await gateway.close()

    async def test_direct_transport_preserves_native_session_and_isolates_caller_context(self) -> None:
        self._write_provider(_context_provider_source())
        generate(self.package)
        root = Path(self.temporary.name).resolve()

        def registry_loader(_asset: Path, selected: Path, gateway: object):
            return self._registry(selected, gateway)

        with patch("direct_gateway.load_active_registry", side_effect=registry_loader):
            gateway = DirectGateway(root)
            await gateway.initialize()
            try:
                async with InMemoryTransport(gateway.build_server(), raise_exceptions=True) as streams:
                    async with ClientSession(*streams) as client:
                        await client.initialize()
                        tool = (await client.list_tools()).tools[0]
                        self.assertIn("caller_context", tool.input_schema["properties"])
                        response = await client.call_tool("demo", {
                            "session_id": "native", "caller_context": {"session_id": "caller"},
                        })
                        self.assertFalse(response.is_error)
                        self.assertEqual({"native": {"session_id": "native"}, "caller": "caller"},
                                         response.structured_content)
                        stateless = await client.call_tool("demo", {"session_id": "native"})
                        self.assertEqual({"native": {"session_id": "native"}, "caller": None},
                                         stateless.structured_content)
                invalid = await gateway.call(None, types.CallToolRequestParams(
                    name="demo", arguments={"caller_context": {"session_id": "  "}}
                ))
                self.assertTrue(invalid.is_error)
                self.assertEqual(["invalid_caller_context"], invalid.structured_content["diagnostics"])
                from runtime_request_context import (
                    RuntimeRequestContext, bind_request_context, current_request_context,
                )
                with bind_request_context(RuntimeRequestContext("existing")):
                    matching = await gateway.call(None, types.CallToolRequestParams(
                        name="demo", arguments={"caller_context": {"session_id": "existing"}}
                    ))
                    self.assertFalse(matching.is_error)
                    self.assertEqual("existing", matching.structured_content["caller"])
                    conflict = await gateway.call(None, types.CallToolRequestParams(
                        name="demo", arguments={"caller_context": {"session_id": "other"}}
                    ))
                    self.assertEqual("existing", current_request_context().session_id)
                self.assertTrue(conflict.is_error)
                self.assertEqual(["caller_context_conflict"], conflict.structured_content["diagnostics"])
                self.assertIsNone(current_request_context())
                foreign = await gateway.call(None, types.CallToolRequestParams(
                    name="demo", arguments={"project_root": str(root / "foreign"),
                                            "caller_context": {"session_id": "caller"}}
                ))
                self.assertTrue(foreign.is_error)
                self.assertEqual(3, sys.modules[self.module].calls)
            finally:
                await gateway.close()

    async def test_project_blacklist_cannot_reenable_a_global_deny(self) -> None:
        generate(self.package)
        root = Path(self.temporary.name).resolve()
        control = root / ".caprmedio_fixture"
        control.mkdir()
        (control / "caprmedio_project_settings.toml").write_text(
            '[paths]\ncontrol_root = ".caprmedio_fixture"\n'
            '[project_mcp]\ntool_blacklist = ["demo"]\n', encoding="utf-8",
        )

        def registry_loader(_asset: Path, selected: Path, gateway: object):
            return self._registry(selected, gateway)

        with patch("direct_gateway.load_active_registry", side_effect=registry_loader):
            gateway = DirectGateway(root)
            await gateway.initialize()
            try:
                self.assertEqual(set(), {tool.name for tool in gateway.tools})
                self.assertEqual(frozenset({"blocked", "demo"}), gateway.tool_blacklist)
            finally:
                await gateway.close()

    def test_runtime_refuses_missing_or_stale_generated_asset(self) -> None:
        root = Path(self.temporary.name).resolve()
        with self.assertRaises(ToolRegistryRuntimeError):
            self._registry(root, object())
        generate(self.package)
        self._write_inventory(blacklist=[])
        with self.assertRaises(ToolRegistryRuntimeError):
            self._registry(root, object())

    async def test_registry_refuses_changed_or_missing_inventory_before_provider_creation(self) -> None:
        generate(self.package)
        active = self._registry(Path(self.temporary.name).resolve(), object())
        inventory = self.feature / "tool_providers.json"
        original = inventory.read_text(encoding="utf-8")
        for value in (original + "\n", None):
            with self.subTest(missing=value is None):
                if value is None:
                    inventory.unlink()
                else:
                    inventory.write_text(value, encoding="utf-8")
                with self.assertRaises(ToolRegistryStaleError):
                    await active.call("demo", {})
                self.assertIsNone(active.bindings[0].provider)
                inventory.write_text(original, encoding="utf-8")
        await active.close()

    def test_registry_rejects_duplicate_keys_and_boolean_schema_versions(self) -> None:
        duplicate = '''{"schema_version":1,"mcp_blacklist":["blocked"],"mcp_blacklist":[],"providers":[{"provider_id":"demo_provider","module":"%s","factory":"create_provider","descriptor_factory":"tool_descriptors"}]}''' % self.module
        (self.feature / "tool_providers.json").write_text(duplicate, encoding="utf-8")
        with self.assertRaises(ToolRegistryAssetError):
            generate(self.package)
        self._write_inventory()
        registry = generate(self.package)
        payload = json.loads(registry.read_text(encoding="utf-8"))
        payload["schema_version"] = True
        registry.write_text(json.dumps(payload), encoding="utf-8")
        with self.assertRaises(ToolRegistryRuntimeError):
            self._registry(Path(self.temporary.name).resolve(), object())
        self._write_inventory()
        (self.feature / "tool_providers.json").write_text(
            (self.feature / "tool_providers.json").read_text(encoding="utf-8").replace(
                '"schema_version": 1', '"schema_version": true'
            ), encoding="utf-8",
        )
        with self.assertRaises(ToolRegistryAssetError):
            generate(self.package)

    def test_runtime_refuses_generated_descriptor_drift(self) -> None:
        registry_path = generate(self.package)
        payload = json.loads(registry_path.read_text(encoding="utf-8"))
        payload["providers"][0]["tools"][0]["description"] = "stale"
        registry_path.write_text(json.dumps(payload), encoding="utf-8")
        with self.assertRaises(ToolRegistryRuntimeError):
            self._registry(Path(self.temporary.name).resolve(), object())

    async def test_invalid_metadata_never_creates_provider_and_close_is_exactly_once(self) -> None:
        self._write_provider(_lifecycle_provider_source())
        registry_path = generate(self.package)
        payload = json.loads(registry_path.read_text(encoding="utf-8"))
        payload["public_tools"] = []
        registry_path.write_text(json.dumps(payload), encoding="utf-8")
        with self.assertRaises(ToolRegistryRuntimeError):
            self._registry(Path(self.temporary.name).resolve(), object())
        module = sys.modules[self.module]
        self.assertEqual((0, 0), (module.created, module.closed))

        generate(self.package)
        active = self._registry(Path(self.temporary.name).resolve(), object())
        self.assertEqual((0, 0), (module.created, module.closed))
        self.assertEqual({"ok": True}, await active.call("demo", {}))
        self.assertEqual((1, 0), (module.created, module.closed))
        await active.close()
        await active.close()
        self.assertEqual((1, 1), (module.created, module.closed))

    async def test_invalid_partial_provider_is_closed(self) -> None:
        self._write_provider(_partial_provider_source())
        generate(self.package)
        active = self._registry(Path(self.temporary.name).resolve(), object())
        with self.assertRaises(ToolRegistryRuntimeError):
            await active.call("demo", {})
        module = sys.modules[self.module]
        self.assertEqual((1, 1), (module.created, module.closed))

    async def test_real_mcp_rejects_invalid_input_before_call_and_invalid_output_after_call(self) -> None:
        self._write_provider(_schema_provider_source())
        generate(self.package)
        root = Path(self.temporary.name).resolve()

        def registry_loader(_asset: Path, selected: Path, gateway: object):
            return self._registry(selected, gateway)

        with patch("direct_gateway.load_active_registry", side_effect=registry_loader):
            gateway = DirectGateway(root)
            await gateway.initialize()
            try:
                async with InMemoryTransport(gateway.build_server(), raise_exceptions=True) as streams:
                    async with ClientSession(*streams) as client:
                        await client.initialize()
                        invalid = await client.call_tool("demo", {"value": 1})
                        self.assertTrue(invalid.is_error)
                        self.assertEqual("rejected", invalid.structured_content["outcome"])
                        self.assertEqual(0, sys.modules[self.module].calls)
                        bad_output = await client.call_tool("demo", {"value": "ok"})
                        self.assertTrue(bad_output.is_error)
                        self.assertTrue(
                            bad_output.structured_content["diagnostics"][0].startswith(
                                "tool_output_invalid:"
                            )
                        )
                        self.assertEqual(1, sys.modules[self.module].calls)
            finally:
                await gateway.close()
        self.assertEqual(1, sys.modules[self.module].closed)

    async def test_generic_provider_result_is_not_rewritten_as_a_workbench_url(self) -> None:
        self._write_provider(_saved_id_provider_source())
        generate(self.package)
        root = Path(self.temporary.name).resolve()

        def registry_loader(_asset: Path, selected: Path, gateway: object):
            return self._registry(selected, gateway)

        with patch("direct_gateway.load_active_registry", side_effect=registry_loader):
            gateway = DirectGateway(root)
            await gateway.initialize()
            try:
                gateway.selection = SimpleNamespace(settings={"project": {"name": "example"}})
                context = SimpleNamespace(
                    request=SimpleNamespace(base_url="http://mcp.test"),
                    params=SimpleNamespace(arguments={}),
                )
                response = await gateway._call(context, "demo", {})
                self.assertEqual(
                    {"saved_query_id": "q_0123456789abcdef0123456789abcdef"},
                    response.structured_content,
                )
            finally:
                await gateway.close()

    async def test_registry_failure_is_an_error_and_blocks_shared_discovery(self) -> None:
        root = Path(self.temporary.name).resolve()
        failure = ToolRegistryRuntimeError("tool-registry-unavailable: invalid")
        with patch("direct_gateway.load_active_registry", side_effect=failure), patch(
            "direct_gateway.report_failure", return_value=(None, None)
        ) as reported:
            with self.assertRaises(ToolRegistryRuntimeError):
                await DirectGateway(root).initialize()
        record = reported.call_args.args[1]
        self.assertEqual(("ERROR", "tool_registry_unavailable"), (record.severity, record.code))

        class BrokenGateway:
            def __init__(self, *_args, **_kwargs):
                self.ready = False

            async def initialize(self):
                raise failure

            async def close(self):
                return None

        config = SimpleNamespace(projects_root=root.parent)
        selection = SimpleNamespace(root=root)
        frontier = SharedToolFrontier()
        with patch("shared_project_catalog.resolve_host_project", return_value=selection):
            with self.assertRaises(ToolRegistryRuntimeError):
                await _discover_project(config, root, BrokenGateway, frontier)
        self.assertNotIn("PROJECT_CANDIDATE_INVALID", [row["code"] for row in frontier.warnings])


if __name__ == "__main__":
    unittest.main()
