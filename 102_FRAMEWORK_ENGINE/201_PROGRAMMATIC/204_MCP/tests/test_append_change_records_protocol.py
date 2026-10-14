"""Real generic registry/SDK append protocol using only disposable Journal state."""
from __future__ import annotations

from contextlib import asynccontextmanager
import copy
import hashlib
import json
from pathlib import Path
import shutil
import sys
import unittest

from mcp.client._memory import InMemoryTransport
from mcp.client.session import ClientSession
from mcp.server import MCPServer


MCP_ROOT = Path(__file__).resolve().parents[1]
TOOLS_ROOT = MCP_ROOT.parent / "201_TOOLS"
REPOSITORY = MCP_ROOT.parents[2]
NATIVE_TESTS = TOOLS_ROOT / "APPEND_CHANGE_RECORDS/tests"
for directory in (MCP_ROOT, TOOLS_ROOT, NATIVE_TESTS, TOOLS_ROOT / "VALIDATE_ATOMS"):
    if str(directory) not in sys.path:
        sys.path.insert(0, str(directory))

import registered_tool_registry as registry  # noqa: E402
from capability_discovery.service import Service  # noqa: E402
import test_append_change_records as native_fixture  # noqa: E402
import work_journal  # noqa: E402
from VALIDATE_ATOMS.validate_atoms_workers.parsing import parse_carrier  # noqa: E402


AUTHORITY = ".caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS"
SOURCE_PINS = (
    ("CA-D-009", 18, AUTHORITY + "/07_delivery/CA-D-009-TOOLS-DELIVERY--deliver-the-change-record-appender-script.md",
     "96b9f0a2ed3d96b1cf0b0dfe8c5cc7ba3523f6ec33c77c24b6cb92a08062a600"),
    ("CA-O-221", 1, AUTHORITY + "/09_operations/CA-O-221-TOOLS-ACTION--append-sealed-journal-change-records.md",
     "84f9d9c9814e2c0e939e506cf5f4cebc5bc98eaa883957412b6b3165311b183c"),
)


def snapshot(root):
    return {path.relative_to(root).as_posix():
            ("directory" if path.is_dir() else path.read_bytes())
            for path in root.rglob("*")}


class AppendChangeRecordsProtocolTests(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        self.fixture = native_fixture.AppendChangeRecordsTest("test_dry_run_is_mutation_free")
        self.fixture.setUp()
        self.addCleanup(self.fixture.tearDown)
        self.root = self.fixture.root.resolve()
        for identity, version, relative, digest in SOURCE_PINS:
            source = REPOSITORY / relative
            raw = source.read_bytes()
            self.assertEqual(digest, hashlib.sha256(raw).hexdigest(), "reviewed source pin is stale")
            metadata = parse_carrier(raw, source).metadata
            self.assertEqual((identity, version, "TOOLS", "Active"),
                             (metadata["atom_id"], metadata["version"], metadata["current_scope_unit"], metadata["status"]))
            destination = self.root / relative
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(source, destination)
        self.context = self.fixture.context()

    @asynccontextmanager
    async def session(self):
        before = snapshot(self.root)
        atoms, bindings, issues = Service(self.root).catalog()
        self.assertEqual([], issues)
        self.assertEqual({"CA-D-009", "CA-O-221"}, set(atoms))
        self.assertEqual(1, len(bindings))
        binding = bindings[0]
        self.assertEqual("APPEND_CHANGE_RECORDS", binding["name"])
        self.assertEqual("append_change_records", binding["mcp_name"])
        self.assertEqual("CA-D-009", binding["source_atom"])
        self.assertEqual(["CA-O-221"], binding["action_ids"])
        self.assertEqual(SOURCE_PINS[0][2], binding["source_path"])
        self.assertEqual(SOURCE_PINS[0][3], binding["sha256"])
        compiled = registry.compile_registry(self.root, bindings)
        self.assertEqual((), compiled.quarantined)
        self.assertEqual({"append_change_records"}, compiled.registered_names)
        server = MCPServer("append-change-records-protocol")
        registered = registry.register_catalog_tools(server, self.root, bindings)
        self.assertEqual((), registered.quarantined)
        self.assertEqual({"append_change_records"}, registered.registered_names)
        self.assertEqual(before, snapshot(self.root), "discovery/registration changed Project state")
        async with InMemoryTransport(server, raise_exceptions=True) as streams:
            async with ClientSession(*streams) as client:
                await client.initialize()
                yield client

    async def call(self, client, request, *, pure=False):
        before = snapshot(self.root)
        response = await client.call_tool("append_change_records", {"request": copy.deepcopy(request)})
        if pure:
            self.assertEqual(before, snapshot(self.root), "dry run/refusal changed Project state")
        return response

    def success(self, response):
        self.assertFalse(response.is_error, response)
        result = response.structured_content
        self.assertIs(True, result["ok"], result)
        self.assertEqual("APPEND_CHANGE_RECORDS", result["tool"]["capability_id"])
        return result

    async def test_actual_sources_register_closed_sdk_schema_once(self):
        async with self.session() as client:
            tools = (await client.list_tools()).tools
            self.assertEqual(["append_change_records"], [tool.name for tool in tools])
            tool = tools[0]
            schema = tool.input_schema
            self.assertEqual(["request"], schema["required"])
            self.assertEqual({"request"}, set(schema["properties"]))
            request = schema["properties"]["request"]
            while "$ref" in request:
                resolved = schema
                for part in request["$ref"].split("/")[1:]:
                    resolved = resolved[part]
                request = resolved
            self.assertEqual({"context", "apply"}, set(request["properties"]))
            self.assertEqual(["context"], request["required"])
            self.assertFalse(request["additionalProperties"])
            self.assertEqual("boolean", request["properties"]["apply"]["type"])
            self.assertIs(False, request["properties"]["apply"]["default"])
            self.assertFalse(tool.annotations.read_only_hint)
            self.assertFalse(tool.annotations.destructive_hint)
            self.assertTrue(tool.annotations.idempotent_hint)
            self.assertIsNotNone(tool.output_schema)

    async def test_default_dry_run_returns_original_events_without_effects(self):
        async with self.session() as client:
            result = self.success(await self.call(client, {"context": self.context}, pure=True))
        self.assertEqual("dry-run", result["mode"])
        self.assertEqual(self.context["predictions"]["journal_records"],
                         result["result"]["planned_effects"]["journal_records"])
        self.assertFalse((self.root / ".caprmedio_caprmedio/_journal").exists())
        self.assertFalse((self.root / ".caprmedio_runtime").exists())

    async def test_apply_returns_actual_canonical_receipt_and_idempotent_readback(self):
        artifact = self.fixture.artifact.read_bytes()
        index = (self.root / ".git/index").read_bytes()
        head = (self.root / ".git/HEAD").read_bytes()
        async with self.session() as client:
            first = self.success(await self.call(client, {"context": self.context, "apply": True}))
            before_retry = snapshot(self.root)
            second = self.success(await self.call(client, {"context": self.context, "apply": True}))
            self.assertEqual(before_retry, snapshot(self.root), "identical retry changed recording/source state")
        self.assertEqual("apply", first["mode"])
        self.assertEqual("complete", first["result"]["state"])
        self.assertEqual(first["result"]["receipts"], second["result"]["receipts"])
        self.assertEqual(1, len(first["result"]["receipts"]))
        receipt = first["result"]["receipts"][0]
        event = self.context["predictions"]["journal_records"][0]
        raw = (self.root / receipt["carrier"]).read_bytes()
        self.assertEqual(work_journal.canonical_json_bytes(event) + b"\n", raw)
        self.assertEqual(event["event_id"], receipt["event_id"])
        self.assertEqual(event["action_id"], receipt["action_id"])
        self.assertEqual(event["event_digest"], receipt["event_digest"])
        self.assertEqual(1, receipt["line"])
        self.assertEqual(hashlib.sha256(b"").hexdigest(), receipt["previous_carrier_digest"])
        self.assertEqual(hashlib.sha256(raw).hexdigest(), receipt["appended_carrier_digest"])
        stored = self.root / ".caprmedio_runtime/state/work_journal/receipts" / (event["event_id"] + ".json")
        self.assertEqual(receipt, json.loads(stored.read_text()))
        self.assertEqual(artifact, self.fixture.artifact.read_bytes())
        self.assertEqual(index, (self.root / ".git/index").read_bytes())
        self.assertEqual(head, (self.root / ".git/HEAD").read_bytes())
        self.assertFalse((self.root / ".caprmedio_runtime/state/commit_change_set").exists())
        self.assertFalse((self.root / ".caprmedio_runtime/state/commit_trigger").exists())

    async def test_strict_boolean_and_unknown_request_fields_refuse_without_effects(self):
        requests = [
            {"context": self.context, "apply": value} for value in (0, 1, "true", None)
        ] + [{"context": self.context, field: value} for field, value in (
            ("root", str(self.root)), ("event", {}), ("wait_seconds", 0), ("authorized", True),
        )] + [{}]
        async with self.session() as client:
            for request in requests:
                with self.subTest(request=request.keys()):
                    response = await self.call(client, request, pure=True)
                    self.assertTrue(response.is_error, response)

    async def test_source_binding_drift_refuses_before_any_append(self):
        async with self.session() as client:
            source = self.root / SOURCE_PINS[0][2]
            original = source.read_bytes()
            source.write_bytes(original + b"\nsource drift\n")
            response = await self.call(client, {"context": self.context, "apply": True}, pure=True)
            self.assertTrue(response.is_error, response)
            source.write_bytes(original)
        self.assertFalse((self.root / ".caprmedio_caprmedio/_journal").exists())


if __name__ == "__main__":
    unittest.main()
