# CA-E-798@1
# ruff: noqa: E402

"""Proofs for the code-owned MCP registry asset boundary."""

from __future__ import annotations

import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch


MCP_ROOT = Path(__file__).resolve().parents[1]
REPOSITORY_ROOT = MCP_ROOT.parents[2]
TOOLS_ROOT = MCP_ROOT.parent / "FEATURE_TOOLS"
sys.path[:0] = [str(MCP_ROOT), str(TOOLS_ROOT), str(TOOLS_ROOT / "VALIDATE_ATOMS")]

from registered_tool_registry import (
    ToolRegistryAssetError,
    _snapshot,
    compile_registry,
)  # noqa: E402
from registered_tool_runtime import register_generated_tools  # noqa: E402
from tool_registry_asset import generated_registry, load_generated_registry, provider_inventory  # noqa: E402


_STAGED_PROVIDER = """
from pydantic import BaseModel

ENTRYPOINT = "LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_TOOLS/fixture_provider.py"

class Request(BaseModel):
    value: str

class Result(BaseModel):
    value: str

def create_adapter(_root):
    raise AssertionError("generation must not create an adapter")

def binding_is_admitted(binding):
    return binding == {
        "name": "FIXTURE",
        "mcp_name": "fixture",
        "entrypoint": ENTRYPOINT,
        "source_atom": "CA-D-1",
        "action_ids": ["CA-O-1"],
    }

def describe_tool():
    return {
        "schema_version": 1,
        "identity": {"name": "FIXTURE", "tool_version": 1, "title": "staged", "description": "staged", "purpose": "test"},
        "binding": {"delivery_atom_id": "CA-D-1", "action_ids": ["CA-O-1"], "implementation_entrypoint": ENTRYPOINT},
        "models": {"input": {"module": ENTRYPOINT, "symbol": "Request"}, "output": {"module": ENTRYPOINT, "symbol": "Result"}},
        "callable": {"module": ENTRYPOINT, "symbol": "create_adapter"},
        "effect_hints": {"read_only_hint": True, "destructive_hint": False, "idempotent_hint": True, "open_world_hint": False},
        "permissions": {"execution": "operator_authorized", "enforcement": "canonical_action_boundary", "metadata_grants_permission": False},
        "source_pins": {"delivery_atom_id": "CA-D-1", "action_ids": ["CA-O-1"]},
        "admission": {"module": ENTRYPOINT, "symbol": "binding_is_admitted", "refresh_after_success": False},
        "diagnostics": {"kind": "test"},
        "failure_contract": {"invokes_on_discovery": False},
    }
"""


class ToolRegistryAssetTests(unittest.TestCase):
    def test_generation_uses_only_explicit_inventory_and_is_deterministic(self) -> None:
        with patch(
            "capability_discovery.service.Service.catalog", side_effect=AssertionError("Atom scan")
        ):
            first = generated_registry(REPOSITORY_ROOT)
            second = generated_registry(REPOSITORY_ROOT)

        self.assertEqual(first, second)
        providers, selected = provider_inventory(REPOSITORY_ROOT)
        self.assertEqual(
            {row["entrypoint"] for row in providers}, {row["entrypoint"] for row in first["tools"]}
        )
        self.assertEqual(list(selected), first["selected_route_names"])
        self.assertNotIn(
            "LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_TOOLS/tool_description.py",
            {row["entrypoint"] for row in first["tools"]},
        )

    def test_source_only_provider_does_not_gain_a_public_name(self) -> None:
        snapshot, _selected = load_generated_registry(REPOSITORY_ROOT)
        source_only = next(row for row in snapshot.tools if row["name"] == "VALIDATE_ATOMS")

        self.assertIsNone(source_only["mcp_name"])
        self.assertNotIn("validate_atoms", snapshot.registered_names)

    def test_generation_uses_the_requested_staged_package_code(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            package_root = Path(temporary)
            programmatic = package_root / "LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC"
            mcp = programmatic / "FEATURE_MCP"
            provider = programmatic / "FEATURE_TOOLS/fixture_provider.py"
            provider.parent.mkdir(parents=True)
            mcp.mkdir(parents=True)
            provider.write_text(_STAGED_PROVIDER, encoding="utf-8")
            (mcp / "tool_providers.json").write_text(
                json.dumps(
                    {
                        "schema_version": 1,
                        "providers": [
                            {
                                "entrypoint": "LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_TOOLS/fixture_provider.py",
                                "mcp_name": "fixture",
                            }
                        ],
                        "selected_route_names": [],
                    }
                ),
                encoding="utf-8",
            )

            generated = generated_registry(package_root)

        self.assertEqual("staged", generated["tools"][0]["descriptor"]["identity"]["title"])

    def test_missing_or_malformed_asset_is_an_explicit_configuration_error(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            mcp = Path(temporary) / "LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_MCP"
            mcp.mkdir(parents=True)
            with self.assertRaises(ToolRegistryAssetError):
                load_generated_registry(temporary)
            (mcp / "tool_registry.json").write_text("{", encoding="utf-8")
            with self.assertRaises(ToolRegistryAssetError):
                load_generated_registry(temporary)

    def test_duplicate_explicit_provider_is_quarantined(self) -> None:
        providers, _selected = provider_inventory(REPOSITORY_ROOT)
        snapshot = compile_registry(REPOSITORY_ROOT, [providers[0], providers[0]])

        self.assertEqual((), snapshot.tools)
        self.assertEqual(2, len(snapshot.quarantined))

    def test_changed_provider_code_refuses_the_generated_asset(self) -> None:
        generated, _selected = load_generated_registry(REPOSITORY_ROOT)
        changed = dict(generated.tools[0])
        changed["code_sha256"] = "0" * 64
        broken = _snapshot([changed, *generated.tools[1:]], generated.quarantined)

        with self.assertRaises(ToolRegistryAssetError):
            register_generated_tools(object(), REPOSITORY_ROOT, broken)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
