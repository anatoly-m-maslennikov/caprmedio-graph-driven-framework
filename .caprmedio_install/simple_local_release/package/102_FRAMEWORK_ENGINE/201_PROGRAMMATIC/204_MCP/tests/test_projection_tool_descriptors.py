"""Descriptor coverage for the governed projection and reversal Tools."""

from __future__ import annotations

from pathlib import Path
import sys
import unittest
from unittest.mock import Mock, patch


PROGRAMMATIC_ROOT = Path(__file__).resolve().parents[2]
TOOLS_ROOT = PROGRAMMATIC_ROOT / "201_TOOLS"
MCP_ROOT = PROGRAMMATIC_ROOT / "204_MCP"
for location in (
    MCP_ROOT,
    TOOLS_ROOT,
    TOOLS_ROOT / "COMPILE_APPLICABLE_METHODOLOGY",
    TOOLS_ROOT / "GENERATE_ENTITY_GRAPH",
    TOOLS_ROOT / "WORKFLOW_OPERATIONS" / "REVERT_CHANGES",
):
    if str(location) not in sys.path:
        sys.path.insert(0, str(location))

import compile_applicable_methodology as compiler  # noqa: E402
import generate_entity_graph as graph  # noqa: E402
import revert_changes as revert  # noqa: E402
from registered_tool_registry import compile_registry  # noqa: E402


def _binding(module: object, source_path: str, digest: str, *, mcp_name: str | None = None) -> dict[str, object]:
    binding: dict[str, object] = {
        "name": module.TOOL_NAME,
        "source_atom": module.DELIVERY_ID,
        "source_path": source_path,
        "sha256": digest,
        "entrypoint": module.ENTRYPOINT,
        "action_ids": list(module.ACTION_IDS),
    }
    if mcp_name is not None:
        binding["mcp_name"] = mcp_name
    return binding


class ProjectionToolDescriptorTests(unittest.TestCase):
    def test_descriptors_compile_from_exact_admitted_bindings(self) -> None:
        bindings = [
            _binding(compiler, "methodology/CA-D-541.md", "a" * 64),
            _binding(graph, "graph/CA-D-538.md", "b" * 64, mcp_name="generate_entity_graph"),
            _binding(revert, "revert/CA-D-536.md", "c" * 64, mcp_name="revert_changes"),
        ]

        snapshot = compile_registry(Path.cwd(), bindings)

        self.assertEqual((), snapshot.quarantined)
        compiled = {row["name"]: row for row in snapshot.tools}
        self.assertEqual({compiler.TOOL_NAME, graph.TOOL_NAME, revert.TOOL_NAME}, set(compiled))
        self.assertIsNone(compiled[compiler.TOOL_NAME]["mcp_name"])
        self.assertEqual("generate_entity_graph", compiled[graph.TOOL_NAME]["mcp_name"])
        self.assertEqual("revert_changes", compiled[revert.TOOL_NAME]["mcp_name"])
        for module, binding in zip((compiler, graph, revert), bindings, strict=True):
            with self.subTest(tool=module.TOOL_NAME):
                descriptor = module.describe_tool()
                self.assertEqual(
                    {"delivery_atom_id", "action_ids"}, set(descriptor["source_pins"]),
                )
                self.assertTrue(module.binding_is_admitted(binding))
                altered = dict(binding)
                altered["entrypoint"] = "untrusted.py"
                self.assertFalse(module.binding_is_admitted(altered))

    def test_compiler_adapter_refuses_project_root_override(self) -> None:
        source = PROGRAMMATIC_ROOT
        other = PROGRAMMATIC_ROOT / "unbound-descriptor-root"
        request = compiler.CompileApplicableMethodologyRequest.model_validate(
            {"operation": "dry_run", "project_root": str(source), "governed_bindings": {}}
        )
        adapter = compiler.create_adapter(source)
        with patch.object(compiler, "run_request", return_value={"outcome": "assessed"}) as native:
            self.assertEqual({"outcome": "assessed"}, adapter.invoke(request))
        native.assert_called_once_with(request.root.model_dump(mode="json", exclude_unset=True))

        override = compiler.CompileApplicableMethodologyRequest.model_validate(
            {"operation": "dry_run", "project_root": str(other), "governed_bindings": {}}
        )
        with self.assertRaisesRegex(compiler.CompileError, "cannot override"):
            adapter.invoke(override)

    def test_graph_adapter_passes_only_canonical_public_fields_to_native_run(self) -> None:
        request = graph.GenerateEntityGraphRequest.model_validate(
            {
                "graph_kind": "entities",
                "source_frontier": {},
                "selection": {},
                "representation_configuration": {},
                "capability_permission_evidence": {},
                "output_destination": "artifacts/entity-graph.json",
            }
        )
        with patch.object(graph, "run", return_value={"outcome": "incomplete"}) as native:
            result = graph.create_adapter(PROGRAMMATIC_ROOT).invoke(request)
        self.assertEqual({"outcome": "incomplete"}, result)
        native.assert_called_once_with(
            PROGRAMMATIC_ROOT.resolve(),
            request.root.model_dump(mode="json", exclude_unset=True),
        )

    def test_revert_adapter_preserves_injected_native_service_and_has_no_fallback(self) -> None:
        request = revert.RevertChangesRequest.model_validate(
            {"operation": "admit", "reversal_request": {"targets": []}}
        )
        service = Mock()
        service.handle.return_value = {"outcome": "blocked"}
        adapter = revert.RevertChangesAdapter("descriptor-test-root", service=service)

        self.assertEqual({"outcome": "blocked"}, adapter.invoke(request))
        service.handle.assert_called_once_with(request.root.model_dump(mode="json", exclude_unset=True))
        with self.assertRaisesRegex(revert.RevertChangesError, "selected native provider"):
            revert.create_adapter("descriptor-test-root").invoke(request)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
