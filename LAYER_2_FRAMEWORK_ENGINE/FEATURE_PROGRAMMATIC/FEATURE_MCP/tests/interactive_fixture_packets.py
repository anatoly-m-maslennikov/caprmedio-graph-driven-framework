"""Current packet and request materialization for the Interactive fixture."""

from __future__ import annotations

import copy
from pathlib import Path
from typing import Any, Mapping

from selected_route_manifest import canonical_digest


def build_packet_and_request(
    root: Path, manifest: Mapping[str, Any], fixture: Any
) -> tuple[dict[str, Any], dict[str, Any]]:
    parameters = fixture.native_implementation_parameters()
    workspace = (root / "fixture" / "disposable-workspace").resolve()
    workspace.mkdir(parents=True, exist_ok=True)
    base = parameters["base_packet"]
    base["workspace"] = str(workspace)
    base["permissions"]["implementation_workspace"]["path"] = str(workspace)
    parameters["run_visit_limits"]["CA-O-230"] = 2
    manifest_ref = str(manifest["manifest_ref"])
    definition = {
        "manifest_ref": manifest_ref,
        "manifest_digest": manifest["canonical_manifest_sha256"],
    }
    freshness = copy.deepcopy(manifest["source_freshness"])
    frontier = ["fixture/disposable-workspace"]
    request: dict[str, Any] = {
        "operation_route": "run_implementation_workflow",
        "mode": "preview",
        "request_id": "interactive-fixture-request",
        "parameters": parameters,
        "parameters_digest": canonical_digest(parameters),
        "target_frontier": frontier,
        "target_frontier_digest": canonical_digest(frontier),
        "effects": [],
        "effects_digest": canonical_digest([]),
        "definition_manifest": definition,
        "source_freshness": freshness,
        "initiative": {
            "initiative_id": "interactive-fixture",
            "instruction_summary": "current O016 journey",
        },
    }
    return parameters, request
