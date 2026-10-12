"""Descriptor contract for the source-only VALIDATE_ATOMS Tool provider."""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import sys
import unittest
from unittest.mock import patch


PROGRAMMATIC_ROOT = Path(__file__).resolve().parents[2]
TOOLS_ROOT = PROGRAMMATIC_ROOT / "201_TOOLS"
MCP_ROOT = PROGRAMMATIC_ROOT / "204_MCP"
PROVIDER_PATH = TOOLS_ROOT / "VALIDATE_ATOMS" / "validate_atoms.py"
RMED_PROVIDER_PATH = TOOLS_ROOT / "RMED_ATOMS_BASE_REVISE" / "rmed_atoms_base_revise.py"
if str(TOOLS_ROOT) not in sys.path:
    sys.path.insert(0, str(TOOLS_ROOT))
if str(PROVIDER_PATH.parent) not in sys.path:
    sys.path.insert(0, str(PROVIDER_PATH.parent))
if str(MCP_ROOT) not in sys.path:
    sys.path.insert(0, str(MCP_ROOT))

import registered_tool_registry as registry  # noqa: E402
from validate_atoms_workers import runtime as checker_runtime  # noqa: E402


def _provider_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:  # pragma: no cover - static Project invariant
        raise AssertionError("VALIDATE_ATOMS provider is unavailable")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    try:
        spec.loader.exec_module(module)
    finally:
        sys.modules.pop(spec.name, None)
    return module


class ValidationToolDescriptorTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.provider = _provider_module(PROVIDER_PATH, "validation_tool_descriptor_provider")

    def test_descriptor_is_complete_json_safe_and_source_only(self) -> None:
        descriptor = self.provider.describe_tool()

        self.assertEqual(
            {
                "schema_version", "identity", "binding", "models", "callable",
                "effect_hints", "permissions", "source_pins", "admission",
                "diagnostics", "failure_contract",
            },
            set(descriptor),
        )
        self.assertEqual(
            {
                "delivery_atom_id": self.provider.DELIVERY_ID,
                "action_ids": [self.provider.ACTION_ID],
                "implementation_entrypoint": self.provider.ENTRYPOINT,
            },
            descriptor["binding"],
        )
        self.assertEqual(
            {"module": self.provider.ENTRYPOINT, "symbol": "CheckerRequest"},
            descriptor["models"]["input"],
        )
        self.assertEqual(
            {"module": self.provider.ENTRYPOINT, "symbol": "CheckerReport"},
            descriptor["models"]["output"],
        )
        self.assertEqual(
            {
                "read_only_hint": True,
                "destructive_hint": False,
                "idempotent_hint": True,
                "open_world_hint": False,
            },
            descriptor["effect_hints"],
        )
        self.assertTrue(descriptor["diagnostics"]["discovery_is_effect_free"])
        self.assertFalse(descriptor["failure_contract"]["invokes_on_discovery"])
        json.dumps(descriptor, sort_keys=True, allow_nan=False)

    def test_canonical_request_is_validated_before_checker_invocation(self) -> None:
        request = self.provider.CheckerRequest.model_validate(
            {
                "schema_version": 1,
                "source_roots": ["/__fixture__/source"],
                "allowed_read_roots": ["/__fixture__"],
                "methodology": {"kind": "sources", "roots": ["/__fixture__/authority"]},
                "selection": {"atoms": [{"atom_id": "CA-R-9001"}]},
            }
        )
        expected = self.provider.CheckerReport.model_validate(self.provider.request_error_report())

        with patch.object(
            self.provider,
            "execute",
            return_value=expected.model_dump(mode="json", exclude_unset=True),
        ) as checker:
            result = self.provider.create_adapter("/descriptor-root").invoke(request)

        self.assertIsInstance(result, self.provider.CheckerReport)
        self.assertEqual(expected, result)
        checker.assert_called_once_with(request.model_dump(mode="json", exclude_unset=True))

    def test_admission_accepts_only_the_matching_source_binding(self) -> None:
        binding = {
            "name": self.provider.TOOL_NAME,
            "mcp_name": "",
            "entrypoint": self.provider.ENTRYPOINT,
            "action_ids": [self.provider.ACTION_ID],
            "source_atom": self.provider.DELIVERY_ID,
        }
        self.assertTrue(self.provider.binding_is_admitted(binding))
        self.assertFalse(self.provider.binding_is_admitted({**binding, "action_ids": []}))
        self.assertFalse(self.provider.binding_is_admitted({**binding, "source_atom": "CA-D-000"}))
        self.assertFalse(self.provider.binding_is_admitted({**binding, "mcp_name": "validate_atoms"}))

    def test_source_only_descriptor_compiles_without_calling_the_checker(self) -> None:
        binding = {
            "name": self.provider.TOOL_NAME,
            "mcp_name": "",
            "entrypoint": self.provider.ENTRYPOINT,
            "action_ids": [self.provider.ACTION_ID],
            "source_atom": self.provider.DELIVERY_ID,
            "source_path": "tools/validate-atoms.md",
            "sha256": "a" * 64,
        }
        registry._MODULE_CACHE.clear()
        self.addCleanup(registry._MODULE_CACHE.clear)

        with patch.object(checker_runtime, "execute") as checker:
            snapshot = registry.compile_registry(Path.cwd(), [binding])

        self.assertEqual(1, len(snapshot.tools))
        self.assertEqual((), snapshot.quarantined)
        self.assertIsNone(snapshot.tools[0]["mcp_name"])
        checker.assert_not_called()


class RmedToolDescriptorTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.provider = _provider_module(RMED_PROVIDER_PATH, "rmed_tool_descriptor_provider")

    def test_descriptor_preserves_the_authority_bound_action_set(self) -> None:
        descriptor = self.provider.describe_tool()

        self.assertEqual(
            ["CA-O-105", "CA-O-106", "CA-O-111"],
            descriptor["binding"]["action_ids"],
        )
        self.assertEqual(
            {"module": self.provider.ENTRYPOINT, "symbol": "RMEDRequest"},
            descriptor["models"]["input"],
        )
        self.assertEqual(
            {"module": self.provider.ENTRYPOINT, "symbol": "RMEDResult"},
            descriptor["models"]["output"],
        )
        json.dumps(descriptor, sort_keys=True, allow_nan=False)

    def test_adapter_validates_the_canonical_request_before_delegating(self) -> None:
        request = self.provider.RMEDRequest.model_validate({"operation": "describe"})
        native_result = {"workflow": "RMED Atoms Base Revise", "execution": "caller-coordinated"}

        with patch.object(self.provider, "run", return_value=native_result) as run:
            result = self.provider.create_adapter("/descriptor-root").invoke(request)

        self.assertIsInstance(result, self.provider.RMEDResult)
        self.assertEqual(native_result, result.root)
        run.assert_called_once_with(Path("/descriptor-root"), request.root)

    def test_admission_requires_the_real_action_set(self) -> None:
        binding = {
            "name": self.provider.TOOL_NAME,
            "mcp_name": "rmed_atoms_base_revise",
            "entrypoint": self.provider.ENTRYPOINT,
            "action_ids": list(self.provider.ACTION_IDS),
            "source_atom": self.provider.DELIVERY_ID,
        }
        self.assertTrue(self.provider.binding_is_admitted(binding))
        self.assertFalse(self.provider.binding_is_admitted({**binding, "action_ids": ["CA-O-104"]}))
        self.assertFalse(self.provider.binding_is_admitted({**binding, "mcp_name": "another_route"}))


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
