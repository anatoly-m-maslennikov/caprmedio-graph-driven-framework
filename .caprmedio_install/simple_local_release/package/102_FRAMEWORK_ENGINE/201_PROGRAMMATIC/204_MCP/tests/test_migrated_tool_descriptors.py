"""Compilation proofs for the migrated installed Tool providers.

This suite deliberately compiles the descriptor registry only.  It must never
create a root-bound adapter or invoke a Tool while validating the installed
provider metadata.
"""
from __future__ import annotations

from contextlib import ExitStack
from dataclasses import dataclass
import hashlib
import inspect
from pathlib import Path
import sys
import unittest
from unittest.mock import patch

from pydantic import TypeAdapter


MCP_ROOT = Path(__file__).resolve().parents[1]
PROGRAMMATIC_ROOT = MCP_ROOT.parent
REPOSITORY_ROOT = PROGRAMMATIC_ROOT.parents[1]
if str(MCP_ROOT) not in sys.path:
    sys.path.insert(0, str(MCP_ROOT))

import registered_tool_registry as registry  # noqa: E402


@dataclass(frozen=True)
class _ProviderSpec:
    """One current Delivery binding and its installed implementation."""

    name: str
    mcp_name: str | None
    entrypoint: str
    delivery_id: str
    action_ids: tuple[str, ...]
    delivery_path: str

    def binding(self) -> dict[str, object]:
        delivery = REPOSITORY_ROOT / self.delivery_path
        binding: dict[str, object] = {
            "name": self.name,
            "entrypoint": self.entrypoint,
            "action_ids": list(self.action_ids),
            "source_atom": self.delivery_id,
            "source_path": self.delivery_path,
            "sha256": hashlib.sha256(delivery.read_bytes()).hexdigest(),
        }
        # An omitted MCP name and the established explicit empty name are
        # source-only descriptions, not an invitation to mint a public name.
        if self.mcp_name is not None:
            binding["mcp_name"] = self.mcp_name
        return binding


_MCP_DELIVERIES = ".caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/204_FEATURE_MCP/07_delivery"
_TOOLS_DELIVERIES = ".caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/07_delivery"
_WORKFLOW_TOOLS = ".caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/WORKFLOW_OPERATIONS"


PROVIDERS = (
    _ProviderSpec(
        "ADMIT_PACKAGE_SOURCES", "admit_package_sources",
        "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/204_MCP/source_admission_mcp.py",
        "CA-D-602", ("CA-O-199",),
        f"{_TOOLS_DELIVERIES}/CA-D-602-TOOLS-DELIVERY--encode-admitted-package-source-catalog.md",
    ),
    _ProviderSpec(
        "INSTALL_FRAMEWORK_RUNTIME", "install_framework_runtime",
        "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/204_MCP/framework_runtime_installation_mcp.py",
        "CA-D-620", ("CA-O-200",),
        f"{_MCP_DELIVERIES}/CA-D-620-MCP-DELIVERY--expose-direct-framework-runtime-installation.md",
    ),
    _ProviderSpec(
        "DISCOVER_TOOLS", "discover_tools",
        "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/DISCOVER_TOOLS/discover_tools.py",
        "CA-D-512", ("CA-O-112",),
        ".caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/DISCOVER_TOOLS/07_delivery/CA-D-512-DISCOVER_TOOLS--encode-discover-tools-bindings.md",
    ),
    _ProviderSpec(
        "DISCOVER_OPERATIONS", "discover_operations",
        "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/DISCOVER_OPERATIONS/discover_operations.py",
        "CA-D-513", ("CA-O-113",),
        ".caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/DISCOVER_OPERATIONS/07_delivery/CA-D-513-DISCOVER_OPERATIONS--encode-discover-operations-bindings.md",
    ),
    _ProviderSpec(
        "GET_EXECUTION_CONTEXT", "get_execution_context",
        "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/GET_EXECUTION_CONTEXT/get_execution_context.py",
        "CA-D-514", ("CA-O-114",),
        ".caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/GET_EXECUTION_CONTEXT/07_delivery/CA-D-514-GET_EXECUTION_CONTEXT--encode-get-execution-context-bindings.md",
    ),
    _ProviderSpec(
        "GET_EXECUTION_STATUS", "get_execution_status",
        "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/GET_EXECUTION_STATUS/get_execution_status.py",
        "CA-D-515", ("CA-O-115",),
        ".caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/GET_EXECUTION_STATUS/07_delivery/CA-D-515-GET_EXECUTION_STATUS--encode-get-execution-status-bindings.md",
    ),
    _ProviderSpec(
        "RESUME_EXECUTION_CONTEXT", "resume_execution_context",
        "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/RESUME_EXECUTION_CONTEXT/resume_execution_context.py",
        "CA-D-516", ("CA-O-116",),
        ".caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/RESUME_EXECUTION_CONTEXT/07_delivery/CA-D-516-RESUME_EXECUTION_CONTEXT--encode-resume-execution-context-bindings.md",
    ),
    _ProviderSpec(
        "WATCH_EXECUTION", "watch_execution",
        "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/WATCH_EXECUTION/watch_execution.py",
        "CA-D-517", ("CA-O-117",),
        ".caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/WATCH_EXECUTION/07_delivery/CA-D-517-WATCH_EXECUTION--encode-watch-execution-bindings.md",
    ),
    _ProviderSpec(
        "FIND_AND_FETCH_ARTIFACTS", "find_and_fetch_artifacts",
        "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/FIND_AND_FETCH_ARTIFACTS/find_and_fetch_artifacts.py",
        "CA-D-551", ("CA-O-159",),
        f"{_TOOLS_DELIVERIES}/CA-D-551-TOOLS-DELIVERY--place-artifact-query-tool-and-golden-test.md",
    ),
    _ProviderSpec(
        "FIND_AND_FETCH_JOURNAL_EVENTS", "find_and_fetch_journal_events",
        "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/FIND_AND_FETCH_JOURNAL_EVENTS/find_and_fetch_journal_events.py",
        "CA-D-557", ("CA-O-162",),
        f"{_TOOLS_DELIVERIES}/CA-D-557-TOOLS-DELIVERY--bind-journal-query-source-route-to-one-tool.md",
    ),
    _ProviderSpec(
        "VALIDATE_ATOMS", "",
        "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/VALIDATE_ATOMS/validate_atoms.py",
        "CA-D-519", ("CA-O-087",),
        f"{_TOOLS_DELIVERIES}/CA-D-519-TOOLS--register-validate-atoms-discovery-binding.md",
    ),
    _ProviderSpec(
        "COMPILE_APPLICABLE_METHODOLOGY", None,
        "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/COMPILE_APPLICABLE_METHODOLOGY/compile_applicable_methodology.py",
        "CA-D-541", ("CA-O-004", "CA-O-005", "CA-O-006", "CA-O-007", "CA-O-008", "CA-O-009"),
        f"{_WORKFLOW_TOOLS}/APPLICABLE_METHODOLOGY/07_delivery/CA-D-541-APPLICABLE_METHODOLOGY--encode-the-compiler-request-boundary.md",
    ),
    _ProviderSpec(
        "REVERT_CHANGES", "revert_changes",
        "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/WORKFLOW_OPERATIONS/REVERT_CHANGES/revert_changes.py",
        "CA-D-536", ("CA-O-131",),
        f"{_WORKFLOW_TOOLS}/REVERT_CHANGES/07_delivery/CA-D-536-REVERT_CHANGES--encode-revert-changes-tool-binding.md",
    ),
    _ProviderSpec(
        "GENERATE_ENTITY_GRAPH", "generate_entity_graph",
        "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/GENERATE_ENTITY_GRAPH/generate_entity_graph.py",
        "CA-D-538", ("CA-O-134", "CA-O-137"),
        f"{_WORKFLOW_TOOLS}/GRAPH_PROJECTIONS/07_delivery/CA-D-538-GRAPH_PROJECTIONS--bind-graph-projection-tool-carriers.md",
    ),
    _ProviderSpec(
        "RMED_ATOMS_BASE_REVISE", "rmed_atoms_base_revise",
        "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/RMED_ATOMS_BASE_REVISE/rmed_atoms_base_revise.py",
        "CA-D-518", ("CA-O-105", "CA-O-106", "CA-O-111"),
        f"{_TOOLS_DELIVERIES}/CA-D-518-TOOLS--register-rmed-atoms-base-revise-discovery-binding.md",
    ),
)


class _RecordingServer:
    """Minimal MCP SDK registration surface without a live server."""

    def __init__(self) -> None:
        self.calls: list[tuple[object, dict[str, object]]] = []

    def add_tool(self, function: object, **metadata: object) -> None:
        self.calls.append((function, metadata))


class MigratedToolDescriptorCompilationTests(unittest.TestCase):
    """The current installed Tool set remains compile-only and model-derived."""

    @classmethod
    def setUpClass(cls) -> None:
        cls.bindings = [provider.binding() for provider in PROVIDERS]
        cls.public_names = {
            provider.mcp_name for provider in PROVIDERS if provider.mcp_name
        }

    def setUp(self) -> None:
        registry._MODULE_CACHE.clear()
        self.addCleanup(registry._MODULE_CACHE.clear)

    def _compile(self):
        return registry.compile_registry(REPOSITORY_ROOT, self.bindings)

    def test_all_fifteen_current_descriptions_compile_without_quarantine(self) -> None:
        snapshot = self._compile()

        self.assertEqual((), snapshot.quarantined)
        self.assertEqual(self.public_names, snapshot.registered_names)

    def test_schemas_are_derived_only_from_stable_canonical_model_symbols(self) -> None:
        snapshot = self._compile()
        records = {str(record["name"]): record for record in snapshot.tools}
        self.assertEqual({provider.name for provider in PROVIDERS}, set(records))

        for provider in PROVIDERS:
            individual = registry.compile_registry(REPOSITORY_ROOT, [provider.binding()])
            self.assertEqual((), individual.quarantined)
            entrypoint, _code_hash, module = registry._load_provider(provider.entrypoint)
            descriptor = module.describe_tool()
            self.assertEqual(provider.entrypoint, entrypoint)
            self.assertEqual(
                {"delivery_atom_id": provider.delivery_id, "action_ids": list(provider.action_ids)},
                descriptor["source_pins"],
            )
            self.assertEqual(
                {"module": provider.entrypoint, "symbol": "create_adapter"},
                descriptor["callable"],
            )
            self.assertEqual(provider.entrypoint, descriptor["admission"]["module"])
            for model_kind in ("input", "output"):
                model_ref = descriptor["models"][model_kind]
                self.assertEqual(provider.entrypoint, model_ref["module"])
                model = getattr(module, model_ref["symbol"])
                self.assertIsInstance(TypeAdapter(model).json_schema(), dict)

            record = records[provider.name]
            input_ref = descriptor["models"]["input"]
            output_ref = descriptor["models"]["output"]
            self.assertEqual(
                TypeAdapter(getattr(module, input_ref["symbol"])).json_schema(),
                record["input_schema"],
            )
            self.assertEqual(
                TypeAdapter(getattr(module, output_ref["symbol"])).json_schema(),
                record["output_schema"],
            )
            # Source-only descriptions remain valid compilation records, but
            # their blank/absent catalog name cannot become public transport
            # exposure.
            if not provider.mcp_name:
                self.assertIsNone(record["mcp_name"])

    def test_compilation_neither_constructs_nor_invokes_any_provider_adapter(self) -> None:
        # Preload the sealed modules, then turn every public factory into a
        # fail-fast sentinel.  Compilation can inspect the callable symbol but
        # may not call it; an adapter therefore cannot exist to be invoked.
        for provider in PROVIDERS:
            registry._load_provider(provider.entrypoint)

        with ExitStack() as stack:
            for provider in PROVIDERS:
                _entrypoint, _code_hash, module = registry._load_provider(provider.entrypoint)
                stack.enter_context(
                    patch.object(
                        module,
                        "create_adapter",
                        side_effect=AssertionError(f"compile created adapter for {provider.name}"),
                    )
                )
            snapshot = self._compile()

        self.assertEqual((), snapshot.quarantined)
        self.assertEqual(self.public_names, snapshot.registered_names)

    def test_watch_execution_registers_an_async_sdk_wrapper_without_invocation(self) -> None:
        """Registration preserves WATCH_EXECUTION's awaitable SDK contract."""

        provider = next(item for item in PROVIDERS if item.name == "WATCH_EXECUTION")
        server = _RecordingServer()
        snapshot = registry.register_catalog_tools(server, REPOSITORY_ROOT, [provider.binding()])

        self.assertEqual((), snapshot.quarantined)
        self.assertEqual({"watch_execution"}, snapshot.registered_names)
        self.assertEqual((), snapshot.withheld)
        self.assertEqual(1, len(server.calls))
        wrapper, metadata = server.calls[0]
        self.assertTrue(inspect.iscoroutinefunction(wrapper))
        self.assertEqual(["request"], list(inspect.signature(wrapper).parameters))
        self.assertTrue(metadata["structured_output"])


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
