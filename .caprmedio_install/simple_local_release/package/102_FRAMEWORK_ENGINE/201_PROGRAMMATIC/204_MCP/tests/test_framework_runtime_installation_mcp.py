"""D620 direct MCP adapter contract for the one CA-O-200 composition.

The native packet is documentary JSON in the pre-existing release-checkpoint
codec. Test doubles here never claim a live installation or Full Gate.
"""

from __future__ import annotations

from pathlib import Path
import sys
import tempfile
import unittest
from types import SimpleNamespace
from unittest.mock import patch


MCP_ROOT = Path(__file__).resolve().parents[1]
TOOLS_ROOT = MCP_ROOT.parent / "201_TOOLS"
for directory in (MCP_ROOT, TOOLS_ROOT, TOOLS_ROOT / "RELEASE_VERSION"):
    if str(directory) not in sys.path:
        sys.path.insert(0, str(directory))

import framework_runtime_installation_mcp as runtime_mcp  # noqa: E402
from framework_runtime_installation_mcp import (  # noqa: E402
    ACTION_ID,
    DELIVERY_ID,
    ENTRYPOINT,
    MCP_NAME,
    TOOL_NAME,
    ExecuteRequest,
    FrameworkRuntimeInstallationAdapter,
    FrameworkRuntimeInstallationMcpError,
    binding_is_admitted,
    input_schema,
    register_framework_runtime_installation,
)
from project_selection import ProjectSelection  # noqa: E402
from retained_full_gate_packet import RetainedNativeFullGatePacket  # noqa: E402


class _Server:
    def __init__(self) -> None:
        self.registered: list[tuple[dict[str, object], object]] = []

    def tool(self, **metadata: object):
        def decorate(function: object) -> object:
            self.registered.append((metadata, function))
            return function
        return decorate


class FrameworkRuntimeInstallationMcpTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory(ignore_cleanup_errors=True)
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        control = self.root / ".caprmedio_caprmedio"
        control.mkdir()
        (control / "caprmedio_project_settings.toml").write_text(
            '[paths]\ncontrol_root = ".caprmedio_caprmedio"\n'
            '[project]\nname = "Fixture Project"\n',
            encoding="utf-8",
        )
        (control / "project_structure.toml").write_text(
            "schema_version = 1\nscope_units = []\n", encoding="utf-8",
        )
        (control / "operators_registry.toml").write_text(
            '[[operators]]\nname = "Fixture Operator"\nrole = "project owner"\n'
            'journal_author = "fixture-operator"\n',
            encoding="utf-8",
        )
        self.selection = ProjectSelection(
            root=self.root.resolve(),
            control_root=control,
            control_relative=Path(".caprmedio_caprmedio"),
            instance_id="f" * 64,
            settings={"paths": {"control_root": ".caprmedio_caprmedio"}, "project": {"name": "Fixture Project"}},
            structure={"schema_version": 1, "scope_units": []},
        )

    @staticmethod
    def _binding() -> dict[str, object]:
        return {
            "name": TOOL_NAME,
            "mcp_name": MCP_NAME,
            "entrypoint": ENTRYPOINT,
            "action_ids": [ACTION_ID],
            "source_atom": DELIVERY_ID,
        }

    @staticmethod
    def _request(**changes: object) -> dict[str, object]:
        value: dict[str, object] = {
            "operation": "execute",
            "command_id": "fixture-o200-command",
            "operator": "Fixture Operator",
            "native_packet": {},
        }
        value.update(changes)
        return value

    def test_schema_is_execute_only_closed_four_field_contract(self) -> None:
        schema = input_schema()
        self.assertEqual("object", schema["type"])
        self.assertFalse(schema["additionalProperties"])
        self.assertEqual({"request"}, set(schema["properties"]))
        request_schema = schema["properties"]["request"]
        self.assertEqual("object", request_schema["type"])
        self.assertFalse(request_schema["additionalProperties"])
        self.assertEqual(
            {"operation", "command_id", "operator", "native_packet"},
            set(request_schema["properties"]),
        )
        self.assertEqual(
            ["command_id", "native_packet", "operation", "operator"],
            sorted(request_schema["required"]),
        )
        self.assertEqual("execute", request_schema["properties"]["operation"]["const"])

        parsed = ExecuteRequest.model_validate(self._request())
        self.assertEqual("execute", parsed.operation)
        self.assertEqual("fixture-o200-command", parsed.command_id)
        self.assertEqual("Fixture Operator", parsed.operator)
        self.assertEqual({}, parsed.native_packet)

    def test_malformed_or_override_request_refuses_without_creating_runtime_effects(self) -> None:
        adapter = FrameworkRuntimeInstallationAdapter(self.root)
        invalid = (
            {},
            self._request(operation="preview"),
            self._request(packet_ref="outside.json"),
            self._request(project_root="/private/tmp/override"),
            self._request(control_root=".caprmedio_caprmedio"),
            self._request(package_root="package"),
            self._request(full_gate_receipt_ref="gate.json"),
            self._request(selector_ref="current.toml"),
            self._request(action_id="CA-O-169"),
        )
        for request in invalid:
            with self.subTest(request=request), self.assertRaises(FrameworkRuntimeInstallationMcpError):
                adapter.invoke(request)
        self.assertFalse((self.root / ".caprmedio_runtime/installation").exists())

    def test_unregistered_operator_and_malformed_native_packet_refuse_without_effects(self) -> None:
        adapter = FrameworkRuntimeInstallationAdapter(self.root)
        with self.assertRaises(FrameworkRuntimeInstallationMcpError):
            adapter.invoke(self._request(operator="Unregistered Operator"))
        with self.assertRaises(FrameworkRuntimeInstallationMcpError):
            adapter.invoke(self._request())
        self.assertFalse((self.root / ".caprmedio_runtime/installation").exists())

    def test_embedded_secret_alias_and_escape_locators_refuse_before_packet_codec(self) -> None:
        target = self.root / "packet-target"
        target.write_text("fixture", encoding="utf-8")
        (self.root / "packet-alias").symlink_to(target)
        packet_values = (
            "../outside",
            "/private/tmp/outside",
            ".env/private",
            "app.env",
            "nested/APP.ENV/private",
            "private_settings/packet",
            "packet-alias",
        )
        with patch("release_checkpoint._load_native_packet", side_effect=self.fail) as codec:
            for locator in packet_values:
                native_packet = {"artifact_root": {"type": "path", "value": locator}}
                with self.subTest(locator=locator), self.assertRaises(FrameworkRuntimeInstallationMcpError):
                    runtime_mcp.read_native_packet(self.root, native_packet)
        codec.assert_not_called()

    def test_delegates_once_and_reports_pending_recording_without_claiming_effect_success(self) -> None:
        packet = object.__new__(RetainedNativeFullGatePacket)
        installation = object()
        packet_calls: list[tuple[Path, dict[str, object]]] = []
        installer_calls: list[tuple[object, str, str]] = []
        pending = SimpleNamespace(
            publication=SimpleNamespace(recording={
                "state": "recording_pending",
                "result_ref": "runtime-results/fixture.json",
                "result": {"effect_outcome": "blocked_before_delete"},
                "terminal": None,
            }),
        )

        def packet_reader(root: str | Path, native_packet: dict[str, object]) -> RetainedNativeFullGatePacket:
            packet_calls.append((Path(root), native_packet))
            return packet

        def installer(value: object, *, command_id: str, operator: str) -> object:
            installer_calls.append((value, command_id, operator))
            return pending

        adapter = FrameworkRuntimeInstallationAdapter(
            self.root,
            packet_reader=packet_reader,
            installer=installer,
            selection_resolver=lambda _root: self.selection,
        )
        with patch.object(runtime_mcp, "_fixed_installation_request", return_value=installation) as fixed:
            result = adapter.invoke(self._request(native_packet={"fixture": "documentary"}))

        self.assertEqual(
            {
                "operation": "execute",
                "effect_outcome": "blocked_before_delete",
                "recording_state": "recording_pending",
                "result_ref": "runtime-results/fixture.json",
            },
            result,
        )
        self.assertEqual([(self.root.resolve(), {"fixture": "documentary"})], packet_calls)
        fixed.assert_called_once_with(self.root.resolve(), self.selection, packet)
        self.assertEqual([(installation, "fixture-o200-command", "Fixture Operator")], installer_calls)

    def test_registration_is_exact_and_exposes_only_the_source_declared_binding(self) -> None:
        self.assertEqual("CA-O-200", ACTION_ID)
        self.assertEqual("CA-D-620", DELIVERY_ID)
        self.assertTrue(binding_is_admitted(self._binding()))
        altered = self._binding()
        altered["entrypoint"] = "other.py"
        self.assertFalse(binding_is_admitted(altered))

        server = _Server()
        self.assertTrue(register_framework_runtime_installation(server, self.root, binding=self._binding()))
        self.assertEqual(1, len(server.registered))
        metadata, _function = server.registered[0]
        self.assertEqual(MCP_NAME, metadata["name"])
        self.assertFalse(metadata["annotations"].read_only_hint)
        self.assertTrue(metadata["annotations"].destructive_hint)
        self.assertFalse(metadata["annotations"].idempotent_hint)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
