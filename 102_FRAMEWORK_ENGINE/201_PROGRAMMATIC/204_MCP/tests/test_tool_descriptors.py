"""Uniform, side-effect-free descriptors for the direct MCP Tool providers."""

from __future__ import annotations

import importlib
import json
from pathlib import Path
import sys
import unittest
from unittest.mock import patch

from pydantic import ValidationError


MCP_ROOT = Path(__file__).resolve().parents[1]
if str(MCP_ROOT) not in sys.path:
    sys.path.insert(0, str(MCP_ROOT))


PROVIDERS = (
    ("framework_image_restoration_mcp", "FrameworkImageRestorationRequest", "FrameworkImageRestorationResult", False),
    ("source_admission_mcp", "SourceAdmissionToolRequest", "SourceAdmissionToolResult", False),
    (
        "framework_runtime_installation_mcp",
        "FrameworkRuntimeInstallationRequest",
        "FrameworkRuntimeInstallationToolResult",
        True,
    ),
)


class ToolDescriptorTests(unittest.TestCase):
    def test_descriptors_are_json_safe_complete_and_model_referenced(self) -> None:
        expected_fields = {
            "schema_version",
            "identity",
            "binding",
            "models",
            "callable",
            "effect_hints",
            "permissions",
            "source_pins",
            "admission",
            "diagnostics",
            "failure_contract",
        }
        for module_name, input_symbol, output_symbol, refresh_after_success in PROVIDERS:
            with self.subTest(module=module_name):
                module = importlib.import_module(module_name)
                descriptor = module.describe_tool()

                self.assertEqual(expected_fields, set(descriptor))
                self.assertEqual(1, descriptor["schema_version"])
                self.assertEqual(
                    {"name", "tool_version", "title", "description", "purpose"},
                    set(descriptor["identity"]),
                )
                self.assertEqual(
                    {"delivery_atom_id", "action_ids", "implementation_entrypoint"},
                    set(descriptor["binding"]),
                )
                self.assertEqual(module.DELIVERY_ID, descriptor["binding"]["delivery_atom_id"])
                self.assertEqual([module.ACTION_ID], descriptor["binding"]["action_ids"])
                self.assertEqual(module.ENTRYPOINT, descriptor["binding"]["implementation_entrypoint"])
                self.assertEqual(
                    {"input", "output"}, set(descriptor["models"])
                )
                for role, symbol in (("input", input_symbol), ("output", output_symbol)):
                    reference = descriptor["models"][role]
                    self.assertEqual({"module", "symbol"}, set(reference))
                    self.assertEqual(module.ENTRYPOINT, reference["module"])
                    self.assertEqual(symbol, reference["symbol"])
                    self.assertIs(getattr(module, symbol), getattr(module, reference["symbol"]))
                self.assertEqual({"module", "symbol"}, set(descriptor["callable"]))
                self.assertEqual(module.ENTRYPOINT, descriptor["callable"]["module"])
                self.assertEqual("create_adapter", descriptor["callable"]["symbol"])
                self.assertEqual(
                    {
                        "read_only_hint",
                        "destructive_hint",
                        "idempotent_hint",
                        "open_world_hint",
                    },
                    set(descriptor["effect_hints"]),
                )
                self.assertEqual(
                    {
                        "execution": "operator_authorized",
                        "enforcement": "canonical_action_boundary",
                        "metadata_grants_permission": False,
                    },
                    descriptor["permissions"],
                )
                self.assertEqual({"delivery_atom_id", "action_ids"}, set(descriptor["source_pins"]))
                self.assertEqual(module.DELIVERY_ID, descriptor["source_pins"]["delivery_atom_id"])
                self.assertEqual([module.ACTION_ID], descriptor["source_pins"]["action_ids"])
                self.assertEqual(
                    {"module", "symbol", "refresh_after_success"}, set(descriptor["admission"])
                )
                self.assertEqual(module.ENTRYPOINT, descriptor["admission"]["module"])
                self.assertEqual("binding_is_admitted", descriptor["admission"]["symbol"])
                self.assertIs(refresh_after_success, descriptor["admission"]["refresh_after_success"])
                self.assertTrue(descriptor["diagnostics"]["discovery_is_effect_free"])
                self.assertFalse(descriptor["failure_contract"]["invokes_on_discovery"])
                json.dumps(descriptor, sort_keys=True, allow_nan=False)

    def test_root_models_preserve_each_existing_union_request(self) -> None:
        image = importlib.import_module("framework_image_restoration_mcp")
        source = importlib.import_module("source_admission_mcp")
        runtime = importlib.import_module("framework_runtime_installation_mcp")

        image_request = image.FrameworkImageRestorationRequest.model_validate({"operation": "preview"})
        self.assertIsInstance(image_request.root, image.PreviewRequest)
        source_request = source.SourceAdmissionToolRequest.model_validate(
            {"operation": "preview", "release_run_id": "fixture-release"}
        )
        self.assertIsInstance(source_request.root, source.PreviewRequest)
        runtime_request = runtime.FrameworkRuntimeInstallationRequest.model_validate(
            {
                "operation": "execute",
                "command_id": "fixture-command",
                "operator": "Fixture Operator",
                "native_packet": {},
            }
        )
        self.assertIsInstance(runtime_request.root, runtime.ExecuteRequest)

    def test_legacy_mcp_envelopes_derive_the_descriptor_input_model_schema(self) -> None:
        for module_name, input_symbol, _output_symbol, _refresh_after_success in PROVIDERS:
            with self.subTest(module=module_name):
                module = importlib.import_module(module_name)
                canonical = getattr(module, input_symbol).model_json_schema()
                definitions = canonical.pop("$defs", None)
                reference = canonical.get("$ref")
                if isinstance(definitions, dict) and isinstance(reference, str) and reference.startswith("#/$defs/"):
                    canonical = definitions.get(reference.removeprefix("#/$defs/"), canonical)
                expected = {
                    "type": "object",
                    "additionalProperties": False,
                    "required": ["request"],
                    "properties": {"request": canonical},
                }
                if definitions is not None:
                    expected["$defs"] = definitions
                self.assertEqual(expected, module.input_schema())

    def test_descriptor_adapters_unwrap_the_canonical_root_model(self) -> None:
        cases = (
            ("framework_image_restoration_mcp", "FrameworkImageRestorationAdapter", "FrameworkImageRestorationRequest", {"operation": "preview"}),
            (
                "source_admission_mcp",
                "SourceAdmissionAdapter",
                "SourceAdmissionToolRequest",
                {"operation": "preview", "release_run_id": "fixture-release"},
            ),
            (
                "framework_runtime_installation_mcp",
                "FrameworkRuntimeInstallationAdapter",
                "FrameworkRuntimeInstallationRequest",
                {
                    "operation": "execute",
                    "command_id": "fixture-command",
                    "operator": "Fixture Operator",
                    "native_packet": {},
                },
            ),
        )
        for module_name, adapter_symbol, request_symbol, request_value in cases:
            with self.subTest(module=module_name):
                module = importlib.import_module(module_name)
                captured: list[object] = []

                class NativeAdapter:
                    def __init__(self, root: object) -> None:
                        self.root = root

                    def invoke(self, request: object) -> dict[str, str]:
                        captured.append(request)
                        return {"provider": module_name}

                with patch.object(module, adapter_symbol, NativeAdapter):
                    adapter = module.create_adapter("descriptor-test-root")
                    request = getattr(module, request_symbol).model_validate(request_value)
                    self.assertEqual({"provider": module_name}, adapter.invoke(request))
                self.assertEqual([request.root], captured)

    def test_result_models_preserve_open_results_and_runtime_activation(self) -> None:
        image = importlib.import_module("framework_image_restoration_mcp")
        source = importlib.import_module("source_admission_mcp")
        runtime = importlib.import_module("framework_runtime_installation_mcp")

        self.assertEqual(
            {"nested": {"state": "preview"}},
            image.FrameworkImageRestorationResult.model_validate({"nested": {"state": "preview"}}).root,
        )
        self.assertEqual(
            {"items": ["admitted", 1]},
            source.SourceAdmissionToolResult.model_validate({"items": ["admitted", 1]}).root,
        )
        result = runtime.FrameworkRuntimeInstallationToolResult.model_validate(
            {
                "operation": "execute",
                "effect_outcome": "completed",
                "recording_state": "recorded",
                "result_ref": "runtime-results/fixture.json",
                "mcp_activation": {
                    "schema_version": 1,
                    "kind": "image_recreation",
                    "request_id": "fixture-command",
                },
            }
        )
        self.assertEqual("image_recreation", result.mcp_activation.kind)
        with self.assertRaises(ValidationError):
            runtime.FrameworkRuntimeInstallationToolResult.model_validate(
                {
                    "operation": "execute",
                    "effect_outcome": "completed",
                    "recording_state": "recorded",
                    "result_ref": "runtime-results/fixture.json",
                    "unexpected": True,
                }
            )


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
