# implementation of:
# Requirement: CA-R-2117
# Method: CA-M-431
"""Disposable MCP fixture for the current O016 direct-RMED packet."""

from __future__ import annotations

from dataclasses import dataclass
import copy
from pathlib import Path
import sys
from typing import Any


MCP_TESTS = Path(__file__).resolve().parent
PROGRAMMATIC = MCP_TESTS.parents[1]
TOOLS = PROGRAMMATIC / "FEATURE_TOOLS"
WFO_TESTS = PROGRAMMATIC / "FEATURE_APPS" / "APP_WORKFLOW_ORCHESTRATOR" / "tests"
WFO = PROGRAMMATIC / "FEATURE_APPS" / "APP_WORKFLOW_ORCHESTRATOR"
MCP = MCP_TESTS.parent
for location in (MCP, TOOLS, WFO_TESTS, WFO):
    if str(location) not in sys.path:
        sys.path.insert(0, str(location))

from frozen_selected_workflows import frozen_manifest, frozen_source_root  # noqa: E402
from interactive_fixture_materialization import (  # noqa: E402
    InteractiveFixtureError,
    _copy_query_sources,
    _copy_source,
    rewrite_source_paths,
    write_settings,
)
from interactive_fixture_packets import build_packet_and_request  # noqa: E402
from interactive_mcp_fixture import _current_route, _validated_manifest  # noqa: E402
from shared_context_direct_fixture import DirectSharedContextFixture  # noqa: E402


# implementation of:
# Requirement: CA-R-2117
# Method: CA-M-431
@dataclass(frozen=True)
class InteractiveDirectFixture:
    root: Path
    manifest: dict[str, Any]
    current_graph: dict[str, Any]
    current_context_packet: dict[str, Any]
    execution_request: dict[str, Any]
    project_binding: dict[str, str]
    trusted_methods: tuple[dict[str, Any], ...]


# implementation of:
# Requirement: CA-R-2117
# Method: CA-M-431
def copy_direct_closure(root: Path, fixture: DirectSharedContextFixture, rows: dict[str, dict[str, object]]) -> None:
    _copy_query_sources(root, rows)
    for pin in fixture.source_pins():
        _copy_source(root, pin["source_path"], fixture.source_bytes(str(pin["atom_id"])), pin["sha256"], rows)
    for row in (*fixture._support_rows(), *fixture.method_source_pins()):
        _copy_source(root, row["path"], fixture._row_bytes(row), row["sha256"], rows)


# implementation of:
# Requirement: CA-R-2117
# Method: CA-M-431
def build_interactive_direct_fixture(
    parent: Path, *, name: str = "interactive-direct"
) -> InteractiveDirectFixture:
    root = (Path(parent) / name).resolve()
    if root.exists():
        raise InteractiveFixtureError(f"fixture destination already exists: {root}")
    root.mkdir(parents=True)
    frozen_source_root(root)
    scope_rows = write_settings(root)
    fixture = DirectSharedContextFixture.load()
    fixture.verify()
    copy_direct_closure(root, fixture, scope_rows)
    manifest = frozen_manifest()
    graph = fixture.graph()
    _current_route(manifest, graph, fixture, root=root, scope_rows=scope_rows)  # type: ignore[arg-type]
    manifest = _validated_manifest(root, manifest)
    parameters, request = build_packet_and_request(
        root, manifest, fixture, scope_rows=scope_rows
    )
    trusted_methods = tuple(
        rewrite_source_paths(row, root, scope_rows) for row in fixture.trusted_methods
    )
    if any(not isinstance(row, dict) for row in trusted_methods):
        raise TypeError("interactive trusted Method rows must remain mappings")
    return InteractiveDirectFixture(
        root=root,
        manifest=manifest,
        current_graph=copy.deepcopy(graph),
        current_context_packet=parameters,
        execution_request=request,
        project_binding={
            "project_root": str(root),
            "project_prefix": "CA",
            "control_root": ".caprmedio_caprmedio",
        },
        trusted_methods=trusted_methods,  # type: ignore[arg-type]
    )

