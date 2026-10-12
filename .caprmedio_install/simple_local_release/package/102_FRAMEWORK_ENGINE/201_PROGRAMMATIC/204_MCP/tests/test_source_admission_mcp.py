"""Closed CA-O-199 MCP adapter coverage; callbacks are never live release proof."""

from __future__ import annotations

import hashlib
import importlib
import json
from pathlib import Path
import shutil
import sys
import tempfile
import unittest


MCP_ROOT = Path(__file__).resolve().parents[1]
PROGRAMMATIC_ROOT = MCP_ROOT.parent
TOOLS_ROOT = PROGRAMMATIC_ROOT / "201_TOOLS"
REPOSITORY_ROOT = PROGRAMMATIC_ROOT.parents[1]
HOST_TEST_ROOT = TOOLS_ROOT / "RELEASE_VERSION" / "tests"
for directory in (MCP_ROOT, TOOLS_ROOT, TOOLS_ROOT / "RELEASE_VERSION", HOST_TEST_ROOT):
    if str(directory) not in sys.path:
        sys.path.insert(0, str(directory))


_host_command_tests = importlib.import_module("test_source_admission_host_command")

from direct_action_session import (  # noqa: E402
    SOURCE_ADMISSION_ACTION_ID,
    SOURCE_ADMISSION_ATOM_RELATIVE,
    SOURCE_ADMISSION_ATOM_SHA256,
    SOURCE_ADMISSION_ATOM_VERSION,
)
from source_admission_mcp import (  # noqa: E402
    ACTION_ID,
    DELIVERY_ID,
    ENTRYPOINT,
    MCP_NAME,
    TOOL_NAME,
    SourceAdmissionAdapter,
    SourceAdmissionMcpError,
    binding_is_admitted,
    input_schema,
    register_source_admission,
)


def _canonical(value: object) -> bytes:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False).encode("utf-8")


class _Server:
    def __init__(self) -> None:
        self.registered: list[tuple[dict, object]] = []

    def tool(self, **metadata):
        def decorate(function):
            self.registered.append((metadata, function))
            return function
        return decorate


class SourceAdmissionMcpTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory(ignore_cleanup_errors=True)
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        control = self.root / ".caprmedio_caprmedio"
        control.mkdir()
        (control / "caprmedio_project_settings.toml").write_text(
            '[paths]\ncontrol_root = ".caprmedio_caprmedio"\n', encoding="utf-8",
        )
        self.registry = (
            b'[[operators]]\nname = "Fixture Operator"\nrole = "project owner"\n'
            b'journal_author = "fixture-operator"\n'
        )
        (control / "operators_registry.toml").write_bytes(self.registry)
        self.registry_sha256 = hashlib.sha256(self.registry).hexdigest()
        self._copy(REPOSITORY_ROOT / SOURCE_ADMISSION_ATOM_RELATIVE, SOURCE_ADMISSION_ATOM_RELATIVE)
        self.assertEqual(
            SOURCE_ADMISSION_ATOM_SHA256,
            hashlib.sha256((self.root / SOURCE_ADMISSION_ATOM_RELATIVE).read_bytes()).hexdigest(),
        )

    def _copy(self, source: Path, relative: Path) -> None:
        destination = self.root / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, destination)

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
    def _request() -> dict[str, str]:
        return {
            "operation": "execute",
            "command_id": "fixture-source-admission",
            "release_run_id": "release-run-fixture",
            "operator": "Fixture Operator",
            "authorization_ref": "operator-commands/o199.json",
            "observed_snapshot_sha256": "a" * 64,
        }

    def _write_authorization(self, request: dict[str, str], *, payload: object | None = None) -> Path:
        path = self.root / request["authorization_ref"]
        path.parent.mkdir(parents=True, exist_ok=True)
        value = payload if payload is not None else {
            "schema_version": 1,
            "operation": "admit_package_sources",
            "command_id": request["command_id"],
            "release_run_id": request["release_run_id"],
            "operator": request["operator"],
            "journal_author": "fixture-operator",
            "snapshot_sha256": request["observed_snapshot_sha256"],
            "operators_registry_sha256": self.registry_sha256,
            "action_source": {
                "atom_id": SOURCE_ADMISSION_ACTION_ID,
                "version": SOURCE_ADMISSION_ATOM_VERSION,
                "path": SOURCE_ADMISSION_ATOM_RELATIVE.as_posix(),
                "sha256": SOURCE_ADMISSION_ATOM_SHA256,
            },
        }
        path.write_bytes(_canonical(value))
        return path

    def test_preview_selects_one_release_and_checks_current_o199_source(self) -> None:
        calls: list[tuple[Path, dict[str, object]]] = []

        def previewer(root: Path, **kwargs: object):
            calls.append((root, kwargs))
            return {"operation": "preview", "snapshot_sha256": "a" * 64}

        adapter = SourceAdmissionAdapter(
            self.root,
            previewer=previewer,
            executor=lambda *_args, **_kwargs: self.fail("preview must not execute"),
            release_authorization_resolver=lambda _root, _run: "fixture/release-authorization",
        )
        self.assertEqual(
            "preview",
            adapter.invoke({"operation": "preview", "release_run_id": "release-run-fixture"})["operation"],
        )
        self.assertEqual(
            [(self.root.resolve(), {
                "release_run_id": "release-run-fixture",
            })],
            calls,
        )
        with self.assertRaisesRegex(SourceAdmissionMcpError, "request-invalid"):
            adapter.invoke({"operation": "preview", "caller_snapshot": "a" * 64})

    def test_preview_refuses_stale_direct_source_before_host_bridge(self) -> None:
        source = self.root / SOURCE_ADMISSION_ATOM_RELATIVE
        source.write_bytes(source.read_bytes() + b"changed\n")
        adapter = SourceAdmissionAdapter(
            self.root,
            previewer=lambda _root: self.fail("stale source must refuse before preview"),
            executor=lambda *_args, **_kwargs: self.fail("stale source must refuse before execute"),
        )
        with self.assertRaisesRegex(SourceAdmissionMcpError, "source-stale"):
            adapter.invoke({"operation": "preview", "release_run_id": "release-run-fixture"})

    def test_execute_reopens_exact_canonical_authorization_before_host_command(self) -> None:
        request = self._request()
        self._write_authorization(request)
        observed: dict[str, object] = {}

        def executor(root: Path, **kwargs: object):
            observed["root"] = root
            observed.update(kwargs)
            return {"outcome": "completed", "snapshot_sha256": kwargs["observed_snapshot_sha256"]}

        adapter = SourceAdmissionAdapter(
            self.root,
            previewer=lambda _root: self.fail("execute must not preview"),
            executor=executor,
            release_authorization_resolver=lambda _root, _run: "fixture/release-authorization",
        )
        result = adapter.invoke(request)
        self.assertEqual("completed", result["outcome"])
        self.assertEqual(self.root.resolve(), observed["root"])
        self.assertEqual(request["command_id"], observed["command_id"])
        self.assertEqual(request["release_run_id"], observed["release_run_id"])
        self.assertEqual("release-run-fixture:step:3:action:1", observed["requested_action_run_id"])
        self.assertEqual(request["operator"], observed["operator"])
        self.assertEqual(request["authorization_ref"], observed["authorization_ref"])
        self.assertEqual("fixture/release-authorization", observed["release_authorization_ref"])
        self.assertEqual(request["observed_snapshot_sha256"], observed["observed_snapshot_sha256"])

    def test_authorization_mismatch_or_noncanonical_bytes_refuse_before_host_command(self) -> None:
        request = self._request()
        authorization = self._write_authorization(request)
        authorization.write_bytes(authorization.read_bytes() + b"\n")
        adapter = SourceAdmissionAdapter(
            self.root,
            previewer=lambda _root: self.fail("invalid execute must not preview"),
            executor=lambda *_args, **_kwargs: self.fail("invalid authorization must not execute"),
        )
        with self.assertRaisesRegex(SourceAdmissionMcpError, "authorization-invalid"):
            adapter.invoke(request)

        mismatched = self._request()
        mismatched["authorization_ref"] = "operator-commands/o199-mismatch.json"
        payload = json.loads(authorization.read_bytes().rstrip())
        payload["snapshot_sha256"] = "b" * 64
        self._write_authorization(mismatched, payload=payload)
        with self.assertRaisesRegex(SourceAdmissionMcpError, "authorization-mismatch"):
            adapter.invoke(mismatched)

    def test_authorization_changed_during_release_reopen_refuses_before_host_command(self) -> None:
        request = self._request()
        authorization = self._write_authorization(request)

        def resolver(_root: Path, _run: str) -> str:
            changed_registry = self.registry + b"\n"
            (self.root / ".caprmedio_caprmedio/operators_registry.toml").write_bytes(changed_registry)
            authorization.write_bytes(_canonical({
                "schema_version": 1,
                "operation": "admit_package_sources",
                "command_id": request["command_id"],
                "release_run_id": request["release_run_id"],
                "operator": request["operator"],
                "journal_author": "fixture-operator",
                "snapshot_sha256": request["observed_snapshot_sha256"],
                "operators_registry_sha256": hashlib.sha256(changed_registry).hexdigest(),
                "action_source": {
                    "atom_id": SOURCE_ADMISSION_ACTION_ID,
                    "version": SOURCE_ADMISSION_ATOM_VERSION,
                    "path": SOURCE_ADMISSION_ATOM_RELATIVE.as_posix(),
                    "sha256": SOURCE_ADMISSION_ATOM_SHA256,
                },
            }))
            return "fixture/release-authorization"

        adapter = SourceAdmissionAdapter(
            self.root,
            previewer=lambda _root: self.fail("execute must not preview"),
            executor=lambda *_args, **_kwargs: self.fail("changed authorization must not execute"),
            release_authorization_resolver=resolver,
        )
        with self.assertRaisesRegex(SourceAdmissionMcpError, "authorization-changed"):
            adapter.invoke(request)

    def test_registry_source_and_relative_path_drift_refuse_before_host_command(self) -> None:
        request = self._request()
        self._write_authorization(request)
        adapter = SourceAdmissionAdapter(
            self.root,
            previewer=lambda _root: self.fail("invalid execute must not preview"),
            executor=lambda *_args, **_kwargs: self.fail("stale inputs must not execute"),
        )
        registry = self.root / ".caprmedio_caprmedio/operators_registry.toml"
        registry.write_text(
            '[[operators]]\nname = "Fixture Operator"\nrole = "project owner"\njournal_author = "other"\n',
            encoding="utf-8",
        )
        with self.assertRaisesRegex(SourceAdmissionMcpError, "authorization-mismatch"):
            adapter.invoke(request)

        request["authorization_ref"] = "../outside.json"
        with self.assertRaisesRegex(SourceAdmissionMcpError, "authorization-invalid"):
            adapter.invoke(request)

        request["authorization_ref"] = ".env"
        with self.assertRaisesRegex(SourceAdmissionMcpError, "authorization-invalid"):
            adapter.invoke(request)

    def test_authorization_uses_project_selected_registry_not_legacy_control_root(self) -> None:
        project = self.root / "selected-project"
        project.mkdir()
        selected = project / ".caprmedio_selected"
        selected.mkdir()
        (selected / "caprmedio_project_settings.toml").write_text(
            '[paths]\ncontrol_root = ".caprmedio_selected"\n', encoding="utf-8",
        )
        (selected / "operators_registry.toml").write_bytes(self.registry)
        self._copy(REPOSITORY_ROOT / SOURCE_ADMISSION_ATOM_RELATIVE, Path("selected-project") / SOURCE_ADMISSION_ATOM_RELATIVE)
        request = self._request()
        request["authorization_ref"] = "operator-commands/o199.json"
        authorization = project / "operator-commands/o199.json"
        authorization.parent.mkdir(parents=True)
        authorization.write_bytes(_canonical({
            "schema_version": 1,
            "operation": "admit_package_sources",
            "command_id": request["command_id"],
            "release_run_id": request["release_run_id"],
            "operator": request["operator"],
            "journal_author": "fixture-operator",
            "snapshot_sha256": request["observed_snapshot_sha256"],
            "operators_registry_sha256": hashlib.sha256(self.registry).hexdigest(),
            "action_source": {
                "atom_id": SOURCE_ADMISSION_ACTION_ID,
                "version": SOURCE_ADMISSION_ATOM_VERSION,
                "path": SOURCE_ADMISSION_ATOM_RELATIVE.as_posix(),
                "sha256": SOURCE_ADMISSION_ATOM_SHA256,
            },
        }))
        observed: dict[str, object] = {}
        adapter = SourceAdmissionAdapter(
            project,
            previewer=lambda _root: self.fail("execute must not preview"),
            executor=lambda _root, **kwargs: observed.update(kwargs) or {"outcome": "completed"},
            release_authorization_resolver=lambda _root, _run: "fixture/release-authorization",
        )
        self.assertEqual("completed", adapter.invoke(request)["outcome"])
        self.assertEqual(".caprmedio_selected/operators_registry.toml", observed["operators_registry_ref"])

    def test_schema_and_registration_are_exact_and_source_bound(self) -> None:
        self.assertTrue(binding_is_admitted(self._binding()))
        changed = self._binding()
        changed["entrypoint"] = "other.py"
        self.assertFalse(binding_is_admitted(changed))
        schema = input_schema()
        self.assertEqual({"request"}, set(schema["properties"]))
        server = _Server()
        self.assertTrue(register_source_admission(server, self.root, binding=self._binding()))
        self.assertEqual(1, len(server.registered))
        metadata, _function = server.registered[0]
        self.assertEqual(MCP_NAME, metadata["name"])
        self.assertFalse(metadata["annotations"].read_only_hint)
        self.assertFalse(metadata["annotations"].idempotent_hint)


class SourceAdmissionMcpBridgeTests(unittest.TestCase):
    """Exercise the public adapter against the retained-O164 producer bridge.

    The imported fixture creates its candidate, sealed source snapshot, O164
    Journal, and selected-run carriers through the real producer helpers.  It
    is intentionally not a mock previewer or executor.
    """

    def _host_fixture(self):
        case_type = getattr(_host_command_tests, "SourceAdmissionHostCommandTests")
        case = case_type(methodName="runTest")
        case.setUp()
        self.addCleanup(case.doCleanups)
        return case

    @staticmethod
    def _authorization(
        root: Path,
        *,
        release_run_id: str,
        snapshot_sha256: str,
        command_id: str,
    ) -> Path:
        registry = root / ".caprmedio_caprmedio/operators_registry.toml"
        payload = {
            "schema_version": 1,
            "operation": "admit_package_sources",
            "command_id": command_id,
            "release_run_id": release_run_id,
            "operator": "Fixture Operator",
            "journal_author": "fixture-operator",
            "snapshot_sha256": snapshot_sha256,
            "operators_registry_sha256": hashlib.sha256(registry.read_bytes()).hexdigest(),
            "action_source": {
                "atom_id": SOURCE_ADMISSION_ACTION_ID,
                "version": SOURCE_ADMISSION_ATOM_VERSION,
                "path": SOURCE_ADMISSION_ATOM_RELATIVE.as_posix(),
                "sha256": SOURCE_ADMISSION_ATOM_SHA256,
            },
        }
        path = root / "operator-commands/o199.json"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(_canonical(payload))
        return path

    def test_default_adapter_reopens_real_frontier_and_refuses_snapshot_drift_before_o199(self) -> None:
        host = self._host_fixture()
        root = host.fixture.root
        adapter = SourceAdmissionAdapter(root)
        graph_patch, tracker_patch = host._bridge_patches()
        with graph_patch, tracker_patch:
            preview = adapter.invoke({"operation": "preview", "release_run_id": host.release_run_id})

        snapshot_sha256 = preview["snapshot_sha256"]
        self.assertEqual(host.requested_action_run_id, preview["requested_action_run_id"])
        self.assertRegex(snapshot_sha256, r"^[0-9a-f]{64}$")

        command_id = "fixture-mcp-o199"
        before = host._events()
        self._authorization(
            root,
            release_run_id=host.release_run_id,
            snapshot_sha256="f" * 64,
            command_id=command_id,
        )
        graph_patch, tracker_patch = host._bridge_patches()
        with graph_patch, tracker_patch, self.assertRaises(SourceAdmissionMcpError) as refused:
            adapter.invoke({
                "operation": "execute",
                "command_id": command_id,
                "release_run_id": host.release_run_id,
                "operator": "Fixture Operator",
                "authorization_ref": "operator-commands/o199.json",
                "observed_snapshot_sha256": "f" * 64,
            })
        self.assertEqual("source-admission-mcp-execute-refused", refused.exception.code)
        self.assertEqual(
            "source-admission-host-command-snapshot-mismatch",
            getattr(refused.exception.__cause__, "code", None),
        )
        self.assertEqual(before, host._events())
        self.assertFalse((root / "catalog.toml").exists())

        self._authorization(
            root,
            release_run_id=host.release_run_id,
            snapshot_sha256=snapshot_sha256,
            command_id=command_id,
        )
        graph_patch, tracker_patch = host._bridge_patches()
        with graph_patch, tracker_patch:
            result = adapter.invoke({
                "operation": "execute",
                "command_id": command_id,
                "release_run_id": host.release_run_id,
                "operator": "Fixture Operator",
                "authorization_ref": "operator-commands/o199.json",
                "observed_snapshot_sha256": snapshot_sha256,
            })

        self.assertEqual("execute", result["operation"])
        self.assertEqual(snapshot_sha256, result["snapshot_sha256"])
        self.assertEqual(host.requested_action_run_id, result["requested_action_run_id"])
        self.assertEqual("completed", result["outcome"])
        self.assertTrue((root / "catalog.toml").is_file())
        command_receipt = root / result["command_receipt_ref"]
        self.assertTrue(command_receipt.is_file())
        self.assertEqual(result["command_receipt_sha256"], hashlib.sha256(command_receipt.read_bytes()).hexdigest())
        self.assertEqual(snapshot_sha256, json.loads(command_receipt.read_text(encoding="utf-8"))["snapshot_sha256"])
        admission_receipt = root / result["admission_receipt_ref"]
        self.assertTrue(admission_receipt.is_file())
        self.assertEqual(result["admission_receipt_sha256"], hashlib.sha256(admission_receipt.read_bytes()).hexdigest())
        catalog = root / result["catalog_ref"]
        self.assertTrue(catalog.is_file())
        self.assertEqual(result["catalog_sha256"], hashlib.sha256(catalog.read_bytes()).hexdigest())
        terminal = result["terminal_event"]
        self.assertEqual(result["outcome"], terminal["outcome"])
        self.assertEqual(result["admission_receipt_ref"], terminal["result_ref"])
        self.assertEqual(
            [result["command_receipt_ref"], result["admission_receipt_ref"], result["catalog_ref"]],
            terminal["effect_refs"],
        )
        self.assertRegex(terminal["event_sha256"], r"^[0-9a-f]{64}$")
        carrier = root / terminal["carrier_ref"]
        self.assertTrue(carrier.is_file())
        self.assertEqual(terminal["raw_sha256"], hashlib.sha256(carrier.read_bytes()).hexdigest())
        actual_terminal = next(event for event in host._events() if event["event_id"] == terminal["event_id"])
        self.assertEqual(terminal["event_sha256"], actual_terminal["event_digest"])
        self.assertEqual(
            ["CA-O-199", "CA-O-199"],
            [event["action_id"] for event in host._events() if event["action_id"] == "CA-O-199"],
        )


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
