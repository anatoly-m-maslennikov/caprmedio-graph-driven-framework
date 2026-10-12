"""Descriptor coverage for the six capability-discovery Tool providers."""

from __future__ import annotations

import asyncio
import importlib.util
import inspect
from pathlib import Path
import sys
from types import ModuleType
import unittest
from unittest.mock import AsyncMock, patch

from pydantic import RootModel, TypeAdapter


MCP_ROOT = Path(__file__).resolve().parents[1]
PROGRAMMATIC_ROOT = MCP_ROOT.parent
TOOLS_ROOT = PROGRAMMATIC_ROOT / "201_TOOLS"
for directory in (MCP_ROOT, TOOLS_ROOT):
    if str(directory) not in sys.path:
        sys.path.insert(0, str(directory))


PROVIDERS = (
    {
        "folder": "DISCOVER_TOOLS",
        "filename": "discover_tools.py",
        "input_symbol": "Query",
        "output_symbol": "DiscoverToolsResult",
        "request": {"query": "atom", "limit": 1},
        "method": "discover",
        "expected": {"matches": [], "total": 0, "next_offset": None, "coverage_issues": []},
        "kwargs": {},
    },
    {
        "folder": "DISCOVER_OPERATIONS",
        "filename": "discover_operations.py",
        "input_symbol": "Query",
        "output_symbol": "DiscoverOperationsResult",
        "request": {"query": "workflow", "limit": 1},
        "method": "discover",
        "expected": {"matches": [], "total": 0, "next_offset": None, "coverage_issues": []},
        "kwargs": {"operations": True},
    },
    {
        "folder": "GET_EXECUTION_CONTEXT",
        "filename": "get_execution_context.py",
        "input_symbol": "Context",
        "output_symbol": "GetExecutionContextResult",
        "request": {"id": "DISCOVER_TOOLS"},
        "method": "context",
        "expected": {"definition": {}, "related_definitions": [], "context_complete": True},
        "kwargs": {},
    },
    {
        "folder": "GET_EXECUTION_STATUS",
        "filename": "get_execution_status.py",
        "input_symbol": "Observation",
        "output_symbol": "GetExecutionStatusResult",
        "request": {"run_id": "fixture-run"},
        "method": "status",
        "expected": {"outcome": "running"},
        "kwargs": {},
    },
    {
        "folder": "RESUME_EXECUTION_CONTEXT",
        "filename": "resume_execution_context.py",
        "input_symbol": "Observation",
        "output_symbol": "ResumeExecutionContextResult",
        "request": {"run_id": "fixture-run", "include_results": True},
        "method": "resume",
        "expected": {"pending": [], "source_drift": []},
        "kwargs": {},
    },
    {
        "folder": "WATCH_EXECUTION",
        "filename": "watch_execution.py",
        "input_symbol": "Watch",
        "output_symbol": "WatchExecutionResult",
        "request": {"run_id": "fixture-run", "timeout_seconds": 0},
        "method": "watch",
        "expected": {"changed": False, "terminal": False, "notifications": [], "cursor": "fixture"},
        "kwargs": {},
    },
)


def _provider_module(provider: dict[str, object]) -> ModuleType:
    """Load a provider from the exact Engine-relative file advertised by it."""

    path = TOOLS_ROOT / str(provider["folder"]) / str(provider["filename"])
    name = f"_discovery_descriptor_{path.stem}_{path.parent.name.lower()}"
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:  # pragma: no cover - fixture failure
        raise AssertionError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    previous = sys.modules.get(name)
    sys.modules[name] = module
    try:
        spec.loader.exec_module(module)
    finally:
        if previous is None:
            sys.modules.pop(name, None)
        else:
            sys.modules[name] = previous
    return module


class DiscoveryToolDescriptorTests(unittest.TestCase):
    def test_descriptors_reference_canonical_models_without_invocation(self) -> None:
        expected_fields = {
            "schema_version", "identity", "binding", "models", "callable", "effect_hints",
            "permissions", "source_pins", "admission", "diagnostics", "failure_contract",
        }
        for provider in PROVIDERS:
            with self.subTest(provider=provider["folder"]):
                module = _provider_module(provider)
                with patch.object(module, "Service", autospec=True) as service:
                    descriptor = module.describe_tool()
                    admitted = module.binding_is_admitted({
                        "name": module.TOOL_NAME,
                        "mcp_name": module.MCP_NAME,
                        "entrypoint": module.ENTRYPOINT,
                        "action_ids": [module.ACTION_ID],
                        "source_atom": module.DELIVERY_ID,
                    })

                self.assertEqual(expected_fields, set(descriptor))
                self.assertEqual(1, descriptor["schema_version"])
                self.assertEqual(module.TOOL_NAME, descriptor["identity"]["name"])
                self.assertEqual(module.DELIVERY_ID, descriptor["binding"]["delivery_atom_id"])
                self.assertEqual([module.ACTION_ID], descriptor["binding"]["action_ids"])
                self.assertEqual(module.ENTRYPOINT, descriptor["binding"]["implementation_entrypoint"])
                self.assertEqual(module.ENTRYPOINT, descriptor["models"]["input"]["module"])
                self.assertEqual(provider["input_symbol"], descriptor["models"]["input"]["symbol"])
                self.assertEqual(module.ENTRYPOINT, descriptor["models"]["output"]["module"])
                self.assertEqual(provider["output_symbol"], descriptor["models"]["output"]["symbol"])
                self.assertTrue(descriptor["effect_hints"]["read_only_hint"])
                self.assertTrue(descriptor["effect_hints"]["idempotent_hint"])
                self.assertTrue(descriptor["diagnostics"]["discovery_is_effect_free"])
                self.assertFalse(descriptor["failure_contract"]["invokes_on_discovery"])
                self.assertTrue(admitted)
                self.assertFalse(module.binding_is_admitted({
                    "name": module.TOOL_NAME,
                    "entrypoint": module.ENTRYPOINT,
                    "action_ids": [module.ACTION_ID],
                    "source_atom": "CA-D-000",
                }))
                service.assert_not_called()

    def test_input_and_open_result_models_have_usable_schemas(self) -> None:
        for provider in PROVIDERS:
            with self.subTest(provider=provider["folder"]):
                module = _provider_module(provider)
                input_model = getattr(module, str(provider["input_symbol"]))
                output_model = getattr(module, str(provider["output_symbol"]))
                self.assertIs(input_model, getattr(module, module.describe_tool()["models"]["input"]["symbol"]))
                self.assertTrue(issubclass(output_model, RootModel))
                parsed = input_model.model_validate(provider["request"])
                for field, value in provider["request"].items():
                    self.assertEqual(value, getattr(parsed, field))
                self.assertEqual(provider["expected"], output_model.model_validate(provider["expected"]).root)
                self.assertIsInstance(TypeAdapter(input_model).json_schema(), dict)
                self.assertIsInstance(TypeAdapter(output_model).json_schema(), dict)

    def test_registry_compiles_advertised_providers_without_discovery_invocation(self) -> None:
        from registered_tool_registry import compile_registry

        modules = [_provider_module(provider) for provider in PROVIDERS]
        bindings = [{
            "name": module.TOOL_NAME,
            "entrypoint": module.ENTRYPOINT,
            "action_ids": [module.ACTION_ID],
            "source_atom": module.DELIVERY_ID,
            "source_path": f"fixtures/{module.TOOL_NAME.lower()}.md",
            "sha256": "0" * 64,
        } for module in modules]

        with patch("capability_discovery.service.Service", autospec=True) as service:
            snapshot = compile_registry(PROGRAMMATIC_ROOT.parents[1], bindings)

        self.assertEqual((), snapshot.quarantined)
        self.assertEqual({module.TOOL_NAME for module in modules}, {
            record["name"] for record in snapshot.tools
        })
        self.assertEqual({module.ENTRYPOINT for module in modules}, {
            record["entrypoint"] for record in snapshot.tools
        })
        service.assert_not_called()

    def test_adapters_delegate_to_the_existing_service_methods(self) -> None:
        for provider in PROVIDERS:
            with self.subTest(provider=provider["folder"]):
                module = _provider_module(provider)
                request = getattr(module, str(provider["input_symbol"])).model_validate(provider["request"])
                with patch.object(module, "Service", autospec=True) as service_class:
                    service = service_class.return_value
                    method = str(provider["method"])
                    expected = provider["expected"]
                    if method == "status":
                        service.status.return_value = (expected, {"saved": "state"})
                    elif method == "watch":
                        service.watch = AsyncMock(return_value=expected)
                    else:
                        getattr(service, method).return_value = expected

                    adapter = module.create_adapter("descriptor-test-root")
                    if method == "watch":
                        self.assertTrue(inspect.iscoroutinefunction(adapter.invoke))
                        actual = asyncio.run(adapter.invoke(request))
                        service.watch.assert_awaited_once_with(request)
                    else:
                        actual = adapter.invoke(request)
                        getattr(service, method).assert_called_once_with(request, **provider["kwargs"])

                service_class.assert_called_once_with("descriptor-test-root")
                self.assertEqual(expected, actual)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
