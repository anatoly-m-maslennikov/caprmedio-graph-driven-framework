"""D591 direct MCP adapter contract; fixture callbacks are never live Docker proof."""

from __future__ import annotations

import hashlib
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
for directory in (MCP_ROOT, TOOLS_ROOT, TOOLS_ROOT / "VALIDATE_ATOMS", TOOLS_ROOT / "RELEASE_VERSION"):
    if str(directory) not in sys.path:
        sys.path.insert(0, str(directory))

from capability_discovery.service import Context, Query, Service  # noqa: E402
from direct_action_session import (  # noqa: E402
    RESTORATION_ATOM_ID,
    RESTORATION_ATOM_RELATIVE,
    RESTORATION_ATOM_SHA256,
    RESTORATION_ATOM_VERSION,
)
from framework_image_restoration_mcp import (  # noqa: E402
    ACTION_ID,
    DELIVERY_ID,
    ENTRYPOINT,
    FrameworkImageRestorationAdapter,
    FrameworkImageRestorationMcpError,
    MCP_NAME,
    TOOL_NAME,
    binding_is_admitted,
    input_schema,
    register_framework_image_restoration,
)


D591_RELATIVE = Path(
    ".caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/"
    "201_FEATURE_TOOLS/07_delivery/"
    "CA-D-591-TOOLS-DELIVERY--bind-same-package-bootstrap-image-restoration-carriers.md"
)


def _canonical(value: object) -> bytes:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False).encode("utf-8")


class _Session:
    instances: list["_Session"] = []

    def __init__(self, root, *, author, operator_authorization, action_id):
        self.root = root
        self.author = author
        self.authorization = operator_authorization
        self.action_id = action_id
        self.actual: dict[str, dict[str, object]] = {}
        self.__class__.instances.append(self)

    def __enter__(self):
        return self

    def __exit__(self, *_unused):
        return None

    def begin_action(self, **_kwargs):
        self.actual["direct-action:fixture"] = {}
        return {"run_id": "direct-action:fixture", "disposition": "started"}

    def reopen_restoration_for_recording(self, *_args, **_kwargs):
        self.actual["direct-action:fixture"] = {}
        return {"run_id": "direct-action:fixture", "disposition": "recording_only"}


class _Server:
    def __init__(self):
        self.registered = []

    def tool(self, **metadata):
        def decorate(function):
            self.registered.append((metadata, function))
            return function
        return decorate


class FrameworkImageRestorationMcpTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(ignore_cleanup_errors=True)
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        control = self.root / ".caprmedio_caprmedio"
        control.mkdir()
        (control / "caprmedio_project_settings.toml").write_text(
            '[paths]\ncontrol_root = ".caprmedio_caprmedio"\n', encoding="utf-8"
        )
        registry = (
            b'[[operators]]\nname = "Fixture Operator"\nrole = "project owner"\n'
            b'journal_author = "fixture-operator"\n'
        )
        (control / "operators_registry.toml").write_bytes(registry)
        self.registry_sha256 = hashlib.sha256(registry).hexdigest()
        self._copy(REPOSITORY_ROOT / RESTORATION_ATOM_RELATIVE, RESTORATION_ATOM_RELATIVE)
        self._copy(REPOSITORY_ROOT / D591_RELATIVE, D591_RELATIVE)
        self.assertEqual(
            RESTORATION_ATOM_SHA256,
            hashlib.sha256((self.root / RESTORATION_ATOM_RELATIVE).read_bytes()).hexdigest(),
        )
        _Session.instances.clear()

    def _copy(self, source: Path, relative: Path) -> None:
        destination = self.root / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, destination)

    @staticmethod
    def _binding():
        return {
            "name": TOOL_NAME,
            "mcp_name": MCP_NAME,
            "entrypoint": ENTRYPOINT,
            "action_ids": [ACTION_ID],
            "source_atom": DELIVERY_ID,
        }

    def _write_command(self, request: dict, *, payload=None) -> str:
        command = payload if payload is not None else {
            "schema_version": 1,
            "operation": request["operation"],
            "command_id": "o187-fixture-command",
            "operator": request["operator"],
            "journal_author": "fixture-operator",
            "operators_registry_sha256": self.registry_sha256,
            "action_source": {
                "atom_id": RESTORATION_ATOM_ID,
                "version": RESTORATION_ATOM_VERSION,
                "path": RESTORATION_ATOM_RELATIVE.as_posix(),
                "sha256": RESTORATION_ATOM_SHA256,
            },
            "input": {
                key: value for key, value in request.items()
                if key in {"requested_run_id", "expected_selector_sha256", "retry_of_terminal_event_id", "result_ref"}
                and value is not None
            },
        }
        raw = _canonical(command)
        reference = "operator-commands/" + hashlib.sha256(raw).hexdigest() + ".json"
        destination = self.root / reference
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_bytes(raw)
        return reference

    def test_preview_is_source_checked_and_has_no_session_or_executor(self):
        calls = []

        def previewer(root):
            calls.append(root)
            return {"state": "preview", "intent": {"selected_selector_sha256": "a" * 64}}

        adapter = FrameworkImageRestorationAdapter(
            self.root,
            session_factory=lambda *_args, **_kwargs: self.fail("preview must not construct a Journal Session"),
            executor_factory=lambda: self.fail("preview must not construct a Docker executor"),
            previewer=previewer,
        )
        self.assertEqual("preview", adapter.invoke({"operation": "preview"})["state"])
        self.assertEqual([self.root.resolve()], calls)
        self.assertEqual([], _Session.instances)
        with self.assertRaises(FrameworkImageRestorationMcpError):
            adapter.invoke({"operation": "preview", "unexpected": True})

    def test_execute_reopens_exact_canonical_command_before_native_call(self):
        request = {
            "operation": "execute",
            "requested_run_id": "o187-fixture-run",
            "expected_selector_sha256": "a" * 64,
            "operator": "Fixture Operator",
        }
        request["authorization_ref"] = self._write_command(request)
        observed = {}

        def restorer(root, *, journal, requested_run_id, expected_selector_sha256, image_executor,
                     retry_of_terminal_event_id):
            observed.update({
                "root": root,
                "requested_run_id": requested_run_id,
                "expected_selector_sha256": expected_selector_sha256,
                "image_executor": image_executor,
                "retry": retry_of_terminal_event_id,
            })
            journal.begin_action(action_id="FRAMEWORK_IMAGE_RESTORATION", requested_run_id=requested_run_id, intent={})
            return {"state": "blocked", "reason": "fixture-only-no-live-restoration"}

        executor = object()
        adapter = FrameworkImageRestorationAdapter(
            self.root,
            session_factory=_Session,
            executor_factory=lambda: executor,
            restorer=restorer,
        )
        result = adapter.invoke(request)
        self.assertEqual("blocked", result["state"])
        self.assertEqual(self.root.resolve(), observed["root"])
        self.assertIs(executor, observed["image_executor"])
        self.assertEqual("fixture-operator", _Session.instances[0].author)
        command = _Session.instances[0].actual["direct-action:fixture"]["operator_command"]
        self.assertEqual(request["authorization_ref"], command["authorization_ref"])
        self.assertEqual(hashlib.sha256((self.root / request["authorization_ref"]).read_bytes()).hexdigest(), command["sha256"])

    def test_invalid_or_mismatched_command_refuses_before_session(self):
        request = {
            "operation": "execute",
            "requested_run_id": "o187-fixture-run",
            "expected_selector_sha256": "a" * 64,
            "operator": "Fixture Operator",
        }
        reference = self._write_command(request)
        # A trailing newline is valid JSON but not the D591 canonical carrier.
        destination = self.root / reference
        destination.write_bytes(destination.read_bytes() + b"\n")
        request["authorization_ref"] = reference
        adapter = FrameworkImageRestorationAdapter(
            self.root,
            session_factory=lambda *_args, **_kwargs: self.fail("invalid command must refuse before a session"),
            executor_factory=lambda: self.fail("invalid command must refuse before an executor"),
        )
        with self.assertRaisesRegex(FrameworkImageRestorationMcpError, "command-invalid"):
            adapter.invoke(request)
        self.assertEqual([], _Session.instances)

    def test_command_filename_must_equal_the_exact_raw_digest(self):
        request = {
            "operation": "execute",
            "requested_run_id": "o187-content-address-refusal",
            "expected_selector_sha256": "a" * 64,
            "operator": "Fixture Operator",
        }
        reference = self._write_command(request)
        wrong_reference = "operator-commands/" + "0" * 64 + ".json"
        (self.root / reference).rename(self.root / wrong_reference)
        request["authorization_ref"] = wrong_reference
        adapter = FrameworkImageRestorationAdapter(
            self.root,
            session_factory=lambda *_args, **_kwargs: self.fail("misnamed command must refuse before a session"),
            executor_factory=lambda: self.fail("misnamed command must refuse before an executor"),
        )
        with self.assertRaisesRegex(FrameworkImageRestorationMcpError, "command-invalid"):
            adapter.invoke(request)

    def test_record_terminal_uses_only_the_exact_recovery_api(self):
        request = {
            "operation": "record_terminal",
            "result_ref": ".caprmedio_runtime/framework_image_restoration/" + "b" * 64 + "/result.json",
            "operator": "Fixture Operator",
        }
        request["authorization_ref"] = self._write_command(request)
        calls = []

        def recorder(root, *, journal, result_ref, image_executor, recording_authorization_ref):
            calls.append((root, result_ref, image_executor, recording_authorization_ref))
            journal.reopen_restoration_for_recording("fixture", {})
            return {"state": "recovery_required", "reason": "fixture-only-no-live-recovery"}

        executor = object()
        adapter = FrameworkImageRestorationAdapter(
            self.root,
            session_factory=_Session,
            executor_factory=lambda: executor,
            terminal_recoverer=recorder,
        )
        self.assertEqual("recovery_required", adapter.invoke(request)["state"])
        self.assertEqual(
            [(self.root.resolve(), request["result_ref"], executor, request["authorization_ref"])],
            calls,
        )
        self.assertIn("operator_command", _Session.instances[0].actual["direct-action:fixture"])

    def test_registration_and_discovery_are_source_bound_and_schema_exact(self):
        service = Service(self.root, exposed=(MCP_NAME,))
        tools = service.catalog()[1]
        bindings = [tool for tool in tools if tool.get("name") == TOOL_NAME]
        self.assertEqual(1, len(bindings))
        self.assertEqual("mcp", bindings[0]["availability"])
        self.assertTrue(binding_is_admitted(bindings[0]))
        server = _Server()
        self.assertTrue(register_framework_image_restoration(server, self.root, binding=bindings[0]))
        self.assertEqual(1, len(server.registered))
        metadata, _function = server.registered[0]
        self.assertEqual(MCP_NAME, metadata["name"])
        self.assertFalse(metadata["annotations"].read_only_hint)
        self.assertFalse(metadata["annotations"].idempotent_hint)

        operations = service.discover(Query(query="restore selected missing bootstrap", limit=10), operations=True)
        operation = next(row for row in operations["matches"] if row["id"] == ACTION_ID)
        self.assertEqual("mcp", operation["availability"])
        self.assertEqual([TOOL_NAME], operation["tools"])
        self.assertEqual(input_schema(), service.context(Context(id=ACTION_ID))["input_schema"])

        unavailable = Service(self.root)
        unavailable_operations = unavailable.discover(
            Query(query="restore selected missing bootstrap", limit=10), operations=True,
        )
        unavailable_operation = next(item for item in unavailable_operations["matches"] if item["id"] == ACTION_ID)
        self.assertEqual("unresolved", unavailable_operation["availability"])
        self.assertIsNone(unavailable.context(Context(id=ACTION_ID))["input_schema"])

        altered = dict(bindings[0])
        altered["entrypoint"] = "other.py"
        self.assertFalse(binding_is_admitted(altered))


if __name__ == "__main__":
    unittest.main()
