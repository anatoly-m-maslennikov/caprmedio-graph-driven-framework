"""Disposable verification world for the current Integrated O016 journey.

This module is test preparation only.  It composes the checked-in selected-route
Golden corpus with the checked-in current O016 shared-context closure; it never
reads the live Project authority.
"""

from __future__ import annotations

from dataclasses import dataclass
import copy
import json
from pathlib import Path
import sys
from typing import Any, Mapping


MCP_TESTS = Path(__file__).resolve().parent
PROGRAMMATIC = MCP_TESTS.parents[1]
TOOLS = PROGRAMMATIC / "201_TOOLS"
WFO_TESTS = PROGRAMMATIC / "203_APPS" / "WORKFLOW_ORCHESTRATOR" / "tests"
WFO = PROGRAMMATIC / "203_APPS" / "WORKFLOW_ORCHESTRATOR"
MCP = MCP_TESTS.parent
if str(MCP) not in sys.path:
    sys.path.insert(0, str(MCP))
if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))
if str(WFO_TESTS) not in sys.path:
    sys.path.insert(0, str(WFO_TESTS))
if str(WFO) not in sys.path:
    sys.path.insert(0, str(WFO))

from frozen_selected_workflows import (  # type: ignore[import-not-found]  # noqa: E402
    frozen_manifest,
    frozen_source_root,
)
from selected_route_manifest import canonical_digest, selected_manifest_ref  # noqa: E402
from selected_route_validation import validate_selected_manifest_document  # noqa: E402
from shared_context_current_fixture import (  # type: ignore[import-not-found]  # noqa: E402
    CurrentSharedContextFixture,
)
from interactive_fixture_materialization import (  # noqa: E402
    InteractiveFixtureError,
    copy_current_closure,
    materialize_method_projection,
    write_settings,
)
from interactive_fixture_packets import build_packet_and_request  # noqa: E402


@dataclass(frozen=True)
class InteractiveMcpFixture:
    """All inputs needed by a future in-process MCP journey test."""

    root: Path
    manifest: dict[str, Any]
    current_graph: dict[str, Any]
    current_context_packet: dict[str, Any]
    execution_request: dict[str, Any]
    project_binding: dict[str, str]
    method_projection_path: Path


def _pin(row: Mapping[str, Any]) -> dict[str, Any]:
    return {
        "atom_id": row["atom_id"],
        "version": row["version"],
        "source_path": row.get("source_path", row.get("path")),
        "digest": row["sha256"],
    }


def _current_route(
    manifest: dict[str, Any], graph: Mapping[str, Any], fixture: CurrentSharedContextFixture
) -> None:
    routes = manifest.get("routes")
    if not isinstance(routes, list):
        raise InteractiveFixtureError("Golden manifest has no route list")
    try:
        route = next(row for row in routes if row.get("route") == "run_implementation_workflow")
    except StopIteration as error:
        raise InteractiveFixtureError("Golden manifest lacks the implementation route") from error
    pins = {str(row["atom_id"]): row for row in fixture.source_pins()}
    step_rows = graph["steps"]
    step_ids = {str(row["atom_id"]) for row in step_rows}
    route["workflow"] = _pin(pins["CA-O-016"])
    route["entry_step"] = graph["entry_step"]
    route["ordered_steps"] = [
        {"step": _pin(row["source"]), "action": _pin(row["actions"][0]["source"])}
        for row in step_rows
    ]
    route["ordered_actions"] = [item["action"] for item in route["ordered_steps"]]
    route["native_action_calls"] = []
    # The selected-route admission schema has one terminal sentinel, while the
    # current graph retains its exact blocked/completed targets in current_graph.
    route["on_result"] = [
        {
            "from": edge["from"],
            "condition": edge["result"],
            "to": edge["to"] if edge["to"] in step_ids else "complete",
        }
        for edge in graph["transitions"]
    ]


def _validated_manifest(root: Path, manifest: dict[str, Any]) -> dict[str, Any]:
    manifest["source_freshness"]["selected_binding_digest"] = canonical_digest(manifest["routes"])
    manifest["canonical_manifest_sha256"] = canonical_digest(
        {key: value for key, value in manifest.items() if key != "canonical_manifest_sha256"}
    )
    validated = validate_selected_manifest_document(root, manifest)
    path = root / selected_manifest_ref(root)
    path.parent.mkdir(parents=True, exist_ok=True)
    persisted = {key: value for key, value in validated.items() if key != "manifest_ref"}
    path.write_text(
        json.dumps(persisted, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n",
        encoding="utf-8",
    )
    return validated


def build_interactive_mcp_fixture(
    parent: Path, *, name: str = "interactive-mcp"
) -> InteractiveMcpFixture:
    """Compose one closed, disposable current-O016 verification Project."""
    root = (Path(parent) / name).resolve()
    if root.exists():
        raise InteractiveFixtureError(f"fixture destination already exists: {root}")
    root.mkdir(parents=True)
    frozen_source_root(root)
    write_settings(root)
    fixture = CurrentSharedContextFixture.load()
    fixture.verify()
    copy_current_closure(root, fixture)
    projection_path = materialize_method_projection(root, fixture)
    manifest = frozen_manifest()
    graph = fixture.graph()
    _current_route(manifest, graph, fixture)
    manifest = _validated_manifest(root, manifest)
    parameters, request = build_packet_and_request(root, manifest, fixture)
    return InteractiveMcpFixture(
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
        method_projection_path=projection_path,
    )
