"""Real generic registry/SDK append protocol using only disposable Journal state."""

from __future__ import annotations

from contextlib import asynccontextmanager
import copy
import hashlib
from pathlib import Path
import shutil
import sys

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
import work_journal as work_journal  # noqa: E402
from VALIDATE_ATOMS.validate_atoms_workers.parsing import parse_carrier  # noqa: E402


AUTHORITY = (
    ".caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS"
)
SOURCE_PINS = (
    (
        "CA-D-009",
        20,
        AUTHORITY
        + "/07_delivery/CA-D-009-TOOLS-DELIVERY--deliver-the-change-record-appender-script.md",
        "05b410f6c6f2ef4abffd4672758d37b9f60f79fa3ff9ee21f331b06769ee4cb0",
    ),
    (
        "CA-O-222",
        1,
        AUTHORITY + "/09_operations/CA-O-222-TOOLS-ACTION--append-journal-change-records.md",
        "da05d24d9f35804b15c8038aaafaecd19e1d637d44c755f11a08fe5af9a82206",
    ),
)


def snapshot(root):
    return {
        path.relative_to(root).as_posix(): ("directory" if path.is_dir() else path.read_bytes())
        for path in root.rglob("*")
    }


class AppendChangeRecordsProtocolFixture:
    def setUp(self):
        self.fixture = native_fixture.AppendChangeRecordsTest("test_dry_run_is_mutation_free")
        self.fixture.setUp()
        self.addCleanup(self.fixture.tearDown)
        self.root = self.fixture.root.resolve()
        for identity, version, relative, digest in SOURCE_PINS:
            source = REPOSITORY / relative
            raw = source.read_bytes()
            self.assertEqual(
                digest, hashlib.sha256(raw).hexdigest(), "reviewed source pin is stale"
            )
            metadata = parse_carrier(raw, source).metadata
            self.assertEqual(
                (identity, version, "TOOLS", "Active"),
                (
                    metadata["atom_id"],
                    metadata["version"],
                    metadata["current_scope_unit"],
                    metadata["status"],
                ),
            )
            destination = self.root / relative
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(source, destination)
        self.context = self.fixture.context()

    @asynccontextmanager
    async def session(self):
        before = snapshot(self.root)
        atoms, bindings, issues = Service(self.root).catalog()
        self.assertEqual([], issues)
        self.assertEqual({"CA-D-009", "CA-O-222"}, set(atoms))
        self.assertEqual(1, len(bindings))
        binding = bindings[0]
        self.assertEqual("APPEND_CHANGE_RECORDS", binding["name"])
        self.assertEqual("append_change_records", binding["mcp_name"])
        self.assertEqual("CA-D-009", binding["source_atom"])
        self.assertEqual(["CA-O-222"], binding["action_ids"])
        self.assertEqual(SOURCE_PINS[0][2], binding["source_path"])
        self.assertEqual(SOURCE_PINS[0][3], binding["sha256"])
        compiled = registry.compile_registry(self.root, bindings)
        self.assertEqual((), compiled.quarantined)
        self.assertEqual({"append_change_records"}, compiled.registered_names)
        server = MCPServer("append-change-records-protocol")
        registered = registry.register_catalog_tools(server, self.root, bindings)
        self.assertEqual((), registered.quarantined)
        self.assertEqual({"append_change_records"}, registered.registered_names)
        self.assertEqual(
            before, snapshot(self.root), "discovery/registration changed Project state"
        )
        async with InMemoryTransport(server, raise_exceptions=True) as streams:
            async with ClientSession(*streams) as client:
                await client.initialize()
                yield client

    async def call(self, client, request, *, pure=False):
        before = snapshot(self.root)
        response = await client.call_tool(
            "append_change_records", {"request": copy.deepcopy(request)}
        )
        if pure:
            self.assertEqual(before, snapshot(self.root), "dry run/refusal changed Project state")
        return response

    def success(self, response):
        self.assertFalse(response.is_error, response)
        result = response.structured_content
        self.assertIs(True, result["ok"], result)
        self.assertEqual("APPEND_CHANGE_RECORDS", result["tool"]["capability_id"])
        return result
