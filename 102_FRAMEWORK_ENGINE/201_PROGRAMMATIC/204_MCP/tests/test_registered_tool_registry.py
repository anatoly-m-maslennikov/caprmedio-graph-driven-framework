"""Focused proofs for the generic descriptor-driven MCP registry."""
from __future__ import annotations

import inspect
import os
from pathlib import Path, PurePosixPath
import sys
import tempfile
import textwrap
import unittest
from unittest.mock import patch


MCP_ROOT = Path(__file__).resolve().parents[1]
if str(MCP_ROOT) not in sys.path:
    sys.path.insert(0, str(MCP_ROOT))

import registered_tool_registry as registry  # noqa: E402


class _Server:
    def __init__(self) -> None:
        self.calls: list[tuple[object, dict[str, object]]] = []

    def add_tool(self, function, **metadata) -> None:
        self.calls.append((function, metadata))


_PROVIDER = '''
from pydantic import BaseModel

ENTRYPOINT = "{entrypoint}"
CREATIONS = 0
INVOCATIONS = 0

class Request(BaseModel):
    value: str

class Result(BaseModel):
    value: str

class Adapter:
    def invoke(self, request):
        global INVOCATIONS
        INVOCATIONS += 1
        return {{"value": request.value}}

def create_adapter(root):
    global CREATIONS
    CREATIONS += 1
    return Adapter()

def binding_is_admitted(binding):
    return binding.get("name") == "{name}" and binding.get("entrypoint") == "{entrypoint}"

def describe_tool():
    descriptor = {{
        "schema_version": 1,
        "identity": {{"name": "{name}", "tool_version": 1, "title": "{name}", "description": "{description}", "purpose": "test"}},
        "binding": {{"delivery_atom_id": "CA-D-{delivery}", "action_ids": ["CA-O-{action}"], "implementation_entrypoint": "{entrypoint}"}},
        "models": {{"input": {{"module": ENTRYPOINT, "symbol": "Request"}}, "output": {{"module": ENTRYPOINT, "symbol": "Result"}}}},
        "callable": {{"module": ENTRYPOINT, "symbol": "create_adapter"}},
        "effect_hints": {{"read_only_hint": True, "destructive_hint": False, "idempotent_hint": True, "open_world_hint": False}},
        "permissions": {{"execution": "operator_authorized", "enforcement": "canonical_action_boundary", "metadata_grants_permission": False}},
        "source_pins": {{"delivery_atom_id": "CA-D-{delivery}", "action_ids": ["CA-O-{source_action}"]}},
        "admission": {{"module": ENTRYPOINT, "symbol": "binding_is_admitted", "refresh_after_success": False}},
        "diagnostics": {{"kind": "test"}},
        "failure_contract": {{"invokes_on_discovery": False}},
    }}
    if {incomplete!r}:
        descriptor["models"].pop("output")
    return descriptor
'''


class RegisteredToolRegistryTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory(dir="/private/tmp", ignore_cleanup_errors=True)
        self.addCleanup(self.temporary.cleanup)
        self.programmatic = Path(self.temporary.name) / "201_PROGRAMMATIC"
        (self.programmatic / "204_MCP").mkdir(parents=True)
        registry._MODULE_CACHE.clear()
        self.addCleanup(registry._MODULE_CACHE.clear)

    def _entrypoint(self, stem: str) -> str:
        return (PurePosixPath("102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/204_MCP") / f"{stem}.py").as_posix()

    def _write_provider(self, stem: str, *, name: str, delivery: int, action: int,
                        description: str = "one", incomplete: bool = False,
                        source_action: int | None = None) -> tuple[str, Path]:
        entrypoint = self._entrypoint(stem)
        target = self.programmatic / "204_MCP" / f"{stem}.py"
        target.write_text(textwrap.dedent(_PROVIDER).format(
            name=name, entrypoint=entrypoint, delivery=delivery, action=action,
            source_action=source_action if source_action is not None else action,
            description=description, incomplete=incomplete,
        ), encoding="utf-8")
        return entrypoint, target

    @staticmethod
    def _binding(name: str, mcp_name: str, entrypoint: str, delivery: int, action: int) -> dict[str, object]:
        return {
            "name": name, "mcp_name": mcp_name, "entrypoint": entrypoint,
            "action_ids": [f"CA-O-{action}"], "source_atom": f"CA-D-{delivery}",
            "source_path": f"methodology/{name}.md", "sha256": "a" * 64,
        }

    def test_quarantines_only_incomplete_descriptor_without_invoking_adapters(self) -> None:
        valid_entry, _ = self._write_provider("valid", name="VALID", delivery=1, action=1)
        invalid_entry, _ = self._write_provider("invalid", name="INVALID", delivery=2, action=2, incomplete=True)
        bindings = [
            self._binding("VALID", "valid_tool", valid_entry, 1, 1),
            self._binding("INVALID", "invalid_tool", invalid_entry, 2, 2),
        ]
        with patch.object(registry, "_PROGRAMMATIC_ROOT", self.programmatic):
            snapshot = registry.compile_registry(self.temporary.name, bindings)

        self.assertEqual({"valid_tool"}, snapshot.registered_names)
        self.assertEqual(1, len(snapshot.quarantined))
        self.assertEqual("models", snapshot.quarantined[0]["diagnostics"][0]["field"])

    def test_compilation_never_creates_or_invokes_an_adapter(self) -> None:
        entrypoint, target = self._write_provider("compile_only", name="COMPILE", delivery=8, action=8)
        with patch.object(registry, "_PROGRAMMATIC_ROOT", self.programmatic):
            snapshot = registry.compile_registry(
                self.temporary.name, [self._binding("COMPILE", "compile_only", entrypoint, 8, 8)],
            )

        self.assertEqual({"compile_only"}, snapshot.registered_names)
        module = registry._MODULE_CACHE[target][1]
        self.assertEqual(0, module.CREATIONS)
        self.assertEqual(0, module.INVOCATIONS)

    def test_registers_real_one_request_signature_without_closure_parameters(self) -> None:
        entrypoint, _ = self._write_provider("valid", name="VALID", delivery=1, action=1)
        server = _Server()
        with (
            patch.object(registry, "_PROGRAMMATIC_ROOT", self.programmatic),
            patch.object(registry, "_binding_is_fresh", return_value=True),
        ):
            snapshot = registry.register_catalog_tools(
                server, self.temporary.name, [self._binding("VALID", "valid_tool", entrypoint, 1, 1)],
            )

        self.assertEqual({"valid_tool"}, snapshot.registered_names)
        self.assertEqual(1, len(server.calls))
        function, metadata = server.calls[0]
        signature = inspect.signature(function)
        self.assertEqual(["request"], list(signature.parameters))
        self.assertIsNot(signature.parameters["request"].annotation, inspect.Signature.empty)
        self.assertTrue(metadata["structured_output"])
        request_model = signature.parameters["request"].annotation
        with patch.object(registry, "_binding_is_fresh", return_value=True):
            self.assertEqual("hello", function(request_model(value="hello")).value)

    def test_stale_binding_refuses_before_adapter_invoke(self) -> None:
        entrypoint, target = self._write_provider("stale", name="STALE", delivery=7, action=7)
        server = _Server()
        with (
            patch.object(registry, "_PROGRAMMATIC_ROOT", self.programmatic),
            patch.object(registry, "_binding_is_fresh", return_value=True),
        ):
            registry.register_catalog_tools(
                server, self.temporary.name, [self._binding("STALE", "stale_tool", entrypoint, 7, 7)],
            )
        function, _metadata = server.calls[0]
        request_model = inspect.signature(function).parameters["request"].annotation
        with patch.object(registry, "_binding_is_fresh", return_value=False):
            with self.assertRaises(registry.ToolError):
                function(request_model(value="never"))

        module = registry._MODULE_CACHE[target][1]
        self.assertEqual(1, module.CREATIONS)
        self.assertEqual(0, module.INVOCATIONS)

    def test_quarantines_source_pin_that_conflicts_with_catalog_binding(self) -> None:
        entrypoint, _ = self._write_provider(
            "pin_mismatch", name="PINS", delivery=9, action=9, source_action=10,
        )
        binding = self._binding("PINS", "pin_tool", entrypoint, 9, 9)
        # The descriptor binding is current, but its self-description source
        # pin claims a different Action.  Catalog admission must reject it.
        with patch.object(registry, "_PROGRAMMATIC_ROOT", self.programmatic):
            snapshot = registry.compile_registry(self.temporary.name, [binding])

        self.assertEqual((), snapshot.tools)
        self.assertEqual("source_pins", snapshot.quarantined[0]["diagnostics"][0]["field"])

    def test_cache_is_bound_to_actual_bytes_even_when_mtime_is_preserved(self) -> None:
        entrypoint, target = self._write_provider("mutable", name="MUTABLE", delivery=3, action=3, description="first")
        binding = self._binding("MUTABLE", "mutable_tool", entrypoint, 3, 3)
        with patch.object(registry, "_PROGRAMMATIC_ROOT", self.programmatic):
            first = registry.compile_registry(self.temporary.name, [binding])
            stamp = target.stat().st_mtime_ns
            self._write_provider("mutable", name="MUTABLE", delivery=3, action=3, description="other")
            os.utime(target, ns=(stamp, stamp))
            second = registry.compile_registry(self.temporary.name, [binding])

        self.assertNotEqual(first.digest, second.digest)
        self.assertEqual("other", second.tools[0]["descriptor"]["identity"]["description"])

    def test_refuses_protected_entrypoint_before_import(self) -> None:
        binding = self._binding(
            "PROTECTED", "protected_tool",
            "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/204_MCP/.env_provider.py", 4, 4,
        )
        with patch.object(registry, "_PROGRAMMATIC_ROOT", self.programmatic):
            snapshot = registry.compile_registry(self.temporary.name, [binding])

        self.assertEqual((), snapshot.tools)
        self.assertEqual("entrypoint", snapshot.quarantined[0]["diagnostics"][0]["field"])

    def test_current_three_provider_descriptors_compile_independently(self) -> None:
        bindings = [
            self._binding(
                "FRAMEWORK_IMAGE_RESTORATION", "restore_framework_image",
                "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/204_MCP/framework_image_restoration_mcp.py", 591, 187,
            ),
            self._binding(
                "ADMIT_PACKAGE_SOURCES", "admit_package_sources",
                "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/204_MCP/source_admission_mcp.py", 602, 199,
            ),
            self._binding(
                "INSTALL_FRAMEWORK_RUNTIME", "install_framework_runtime",
                "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/204_MCP/framework_runtime_installation_mcp.py", 620, 200,
            ),
        ]
        snapshot = registry.compile_registry(Path.cwd(), bindings)

        self.assertEqual({binding["mcp_name"] for binding in bindings}, snapshot.registered_names)
        self.assertEqual((), snapshot.quarantined)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
