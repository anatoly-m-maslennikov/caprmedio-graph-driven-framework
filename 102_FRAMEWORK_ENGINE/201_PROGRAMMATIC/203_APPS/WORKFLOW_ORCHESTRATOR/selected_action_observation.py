"""Read one selected Action Run without changing queue or Journal state."""
from __future__ import annotations

import json
import re
from collections.abc import Mapping
from pathlib import Path
from typing import Any


_ACTION_ID = re.compile(
    r"^(?P<workflow>[A-Za-z0-9][A-Za-z0-9_-]{0,127}):step:(?P<step>[1-9][0-9]*)"
    r"(?::visit:(?P<visit>[2-9][0-9]*))?:action:(?P<action>[1-9][0-9]*)$"
)
_DIGEST = re.compile(r"^[0-9a-f]{64}$")
_RUNTIME = Path(".caprmedio_install/workflow_orchestrator/runs")
_MAX_JSON_BYTES = 512 * 1024
_MAX_JOURNAL_BYTES = 8 * 1024 * 1024
_MAX_JOURNAL_LINES = 100_000


class SelectedActionObservationError(ValueError):
    """A requested Action observation cannot be safely bound to saved evidence."""


def _safe_json(path: Path, *, limit: int = _MAX_JSON_BYTES) -> dict[str, Any] | None:
    """Read a bounded regular JSON carrier, never following a symlink."""
    try:
        if path.is_symlink() or not path.is_file() or path.stat().st_size > limit:
            return None
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, json.JSONDecodeError):
        return None
    return value if isinstance(value, dict) else None


def _safe_relative_path(root: Path, relative: str) -> Path | None:
    """Resolve one known repository-relative carrier without symlink escape."""
    candidate = Path(relative)
    if candidate.is_absolute() or not candidate.parts or ".." in candidate.parts:
        return None
    cursor = root
    for part in candidate.parts:
        cursor /= part
        if cursor.is_symlink():
            return None
    try:
        resolved = (root / candidate).resolve(strict=True)
        resolved.relative_to(root)
    except (OSError, ValueError):
        return None
    return resolved


def _support_definition(pin: Mapping[str, Any]) -> dict[str, Any] | None:
    if not isinstance(pin, Mapping) or set(pin) != {"atom_id", "version", "source_path", "digest"}:
        return None
    if (not isinstance(pin["atom_id"], str) or not pin["atom_id"]
            or type(pin["version"]) is not int or pin["version"] < 1
            or not isinstance(pin["source_path"], str) or not pin["source_path"]
            or not isinstance(pin["digest"], str) or not _DIGEST.fullmatch(pin["digest"])):
        return None
    return {"atom_id": pin["atom_id"], "version": pin["version"],
            "path": pin["source_path"], "digest": pin["digest"]}


def _graph_definition(definition: Mapping[str, Any], kind: str) -> dict[str, Any]:
    return {"atom_id": definition["atom_id"], "kind": kind, "version": definition["version"],
            "path": definition["path"], "sha256": definition["digest"]}


def _manifest_identity(manifest: Mapping[str, Any]) -> tuple[str, str, dict[str, Any], list[dict[str, Any]]]:
    reference = manifest.get("manifest_ref")
    digest = manifest.get("canonical_manifest_sha256")
    freshness = manifest.get("source_freshness")
    routes = manifest.get("routes")
    if (not isinstance(reference, str) or Path(reference).is_absolute() or ".." in Path(reference).parts
            or not isinstance(digest, str) or not _DIGEST.fullmatch(digest)
            or not isinstance(freshness, Mapping) or not isinstance(routes, list)):
        raise SelectedActionObservationError("current selected manifest is unavailable")
    normalized_routes = [dict(route) for route in routes if isinstance(route, Mapping)]
    if len(normalized_routes) != len(routes):
        raise SelectedActionObservationError("current selected manifest is invalid")
    return reference, digest, dict(freshness), normalized_routes


def _bound_request(
    saved: Mapping[str, Any], action_run_id: str, manifest: Mapping[str, Any],
) -> dict[str, Any]:
    """Bind exactly one requested Action to its saved parent and current manifest."""
    manifest_ref, manifest_digest, freshness, routes = _manifest_identity(manifest)
    request = saved.get("request")
    graph = saved.get("graph")
    if (set(saved) != {"request", "graph"} or not isinstance(request, Mapping)
            or set(request) != {"operation", "run_id", "execution"} or not isinstance(graph, Mapping)):
        raise SelectedActionObservationError("saved selected request has an invalid outer shape")
    execution = request.get("execution")
    if request.get("operation") != "enqueue_selected" or not isinstance(execution, Mapping):
        raise SelectedActionObservationError("saved selected request is not an admitted enqueue")
    match = _ACTION_ID.fullmatch(action_run_id)
    assert match is not None
    workflow_run_id = match.group("workflow")
    if request.get("run_id") != workflow_run_id:
        raise SelectedActionObservationError("Action identity is not bound to its saved Workflow Run")
    definition_manifest = execution.get("definition_manifest")
    if definition_manifest != {"manifest_ref": manifest_ref, "manifest_digest": manifest_digest}:
        raise SelectedActionObservationError("saved Action request is not bound to the current canonical manifest")
    if execution.get("source_freshness") != freshness:
        raise SelectedActionObservationError("saved Action request has stale source freshness")
    route_name = execution.get("operation_route")
    route_rows = [route for route in routes if route.get("route") == route_name]
    if not isinstance(route_name, str) or len(route_rows) != 1:
        raise SelectedActionObservationError("saved Action request has no current selected route")
    route = route_rows[0]
    if (graph.get("route") != route_name or graph.get("manifest_ref") != manifest_ref
            or graph.get("manifest_digest") != manifest_digest):
        raise SelectedActionObservationError("saved selected graph is not bound to the current canonical manifest")
    workflow_definition = _support_definition(route.get("workflow", {}))
    steps = route.get("ordered_steps")
    if workflow_definition is None or not isinstance(steps, list):
        raise SelectedActionObservationError("current selected route has no bound Run graph")

    requested = execution.get("requested_runs")
    if not isinstance(requested, list):
        raise SelectedActionObservationError("saved Action request has no requested Runs")
    action_rows = [dict(row) for row in requested if isinstance(row, Mapping)
                   and row.get("kind") == "action" and row.get("requested_run_id") == action_run_id]
    if len(action_rows) != 1:
        raise SelectedActionObservationError("Action identity is unknown or ambiguous in the saved request")
    action_row = action_rows[0]
    step_run_id = action_row.get("parent_requested_run_id")
    action_definition = action_row.get("definition")
    if not isinstance(step_run_id, str) or not isinstance(action_definition, Mapping):
        raise SelectedActionObservationError("saved Action request has no source-bound parent Step")
    step_rows = [dict(row) for row in requested if isinstance(row, Mapping)
                 and row.get("kind") == "step" and row.get("requested_run_id") == step_run_id]
    workflow_rows = [dict(row) for row in requested if isinstance(row, Mapping)
                     and row.get("kind") == "workflow" and row.get("requested_run_id") == workflow_run_id]
    if len(step_rows) != 1 or len(workflow_rows) != 1 or workflow_rows[0].get("definition") != workflow_definition:
        raise SelectedActionObservationError("saved Action parent lineage is incomplete or ambiguous")
    step_definition = step_rows[0].get("definition")
    if step_rows[0].get("parent_requested_run_id") != workflow_run_id or not isinstance(step_definition, Mapping):
        raise SelectedActionObservationError("saved Action parent lineage is not source-bound")

    admitted = False
    for item in steps:
        if not isinstance(item, Mapping):
            continue
        source_step = _support_definition(item.get("step", {}))
        source_action = _support_definition(item.get("action", {}))
        if source_step == step_definition and source_action == action_definition:
            admitted = True
            break
    if not admitted:
        raise SelectedActionObservationError("saved Action definition is not admitted by the current route")
    graph_steps = graph.get("steps")
    graph_workflow = graph.get("workflow")
    if not isinstance(graph_steps, list) or not isinstance(graph_workflow, Mapping):
        raise SelectedActionObservationError("saved selected graph has no source-bound Action")
    expected_graph_workflow = _graph_definition(workflow_definition, "workflow")
    graph_action_matches = False
    for item in graph_steps:
        if not isinstance(item, Mapping) or not isinstance(item.get("actions"), list):
            continue
        graph_step = {key: item.get(key) for key in ("atom_id", "kind", "version", "path", "sha256")}
        if graph_step != _graph_definition(step_definition, "step"):
            continue
        for action in item["actions"]:
            if isinstance(action, Mapping) and {
                key: action.get(key) for key in ("atom_id", "kind", "version", "path", "sha256")
            } == _graph_definition(action_definition, "action"):
                graph_action_matches = True
    if graph_workflow != expected_graph_workflow or not graph_action_matches:
        raise SelectedActionObservationError("saved selected graph does not retain the requested Action binding")
    return {
        "action_run_id": action_run_id,
        "workflow_run_id": workflow_run_id,
        "step_run_id": step_run_id,
        "operation_route": route_name,
        "action_definition": dict(action_definition),
        "definition_manifest": {"manifest_ref": manifest_ref, "manifest_digest": manifest_digest},
        "source_freshness": freshness,
    }


def _base(bound: Mapping[str, Any], disposition: str, outcome: str, diagnostic: str | None = None) -> dict[str, Any]:
    value = {**bound, "disposition": disposition, "outcome": outcome}
    if diagnostic is not None:
        value["diagnostics"] = [diagnostic]
    return value


def observe_selected_action(root: str | Path, action_run_id: object, manifest: Mapping[str, Any]) -> dict[str, Any]:
    """Return one bounded selected Action observation from source progress.

    This deliberately consults only the Action's deterministic run directory,
    frozen request, and optional progress carrier. It never queues, replays,
    or writes anything.
    """
    if not isinstance(action_run_id, str) or not _ACTION_ID.fullmatch(action_run_id):
        return {"disposition": "rejected", "outcome": "rejected",
                "diagnostics": ["action Run identity is invalid"]}
    try:
        project_root = Path(root).resolve(strict=True)
    except (OSError, ValueError):
        return {"action_run_id": action_run_id, "disposition": "blocked", "outcome": "blocked",
                "diagnostics": ["Project root is unavailable"]}
    workflow_run_id = _ACTION_ID.fullmatch(action_run_id).group("workflow")  # type: ignore[union-attr]
    run_directory = _safe_relative_path(project_root, (_RUNTIME / workflow_run_id).as_posix())
    if run_directory is None or not run_directory.is_dir():
        return {"action_run_id": action_run_id, "workflow_run_id": workflow_run_id,
                "disposition": "unknown", "outcome": "unknown",
                "diagnostics": ["no selected Workflow Run carrier exists for this Action"]}
    saved = _safe_json(run_directory / "selected_request.json")
    if saved is None:
        return {"action_run_id": action_run_id, "workflow_run_id": workflow_run_id,
                "disposition": "unknown", "outcome": "unknown",
                "diagnostics": ["selected Workflow Run has no readable frozen request"]}
    try:
        bound = _bound_request(saved, action_run_id, manifest)
    except SelectedActionObservationError as error:
        return {"action_run_id": action_run_id, "workflow_run_id": workflow_run_id,
                "disposition": "blocked", "outcome": "blocked", "diagnostics": [str(error)]}

    progress_relative = (_RUNTIME / workflow_run_id / f"{action_run_id}.json").as_posix()
    progress = _safe_json(run_directory / f"{action_run_id}.json")
    progress_is_bound = bool(progress and progress.get("action_run_id") == action_run_id
                             and isinstance(progress.get("result"), str))
    if progress_is_bound:
        result = _base(bound, "terminal", str(progress["result"]))
        result["result_ref"] = progress_relative
        return result
    if progress is not None:
        return _base(bound, "pending", "pending", "Action progress is not bound to this Action")
    return _base(bound, "unstarted", "unstarted", "no Action progress or sealed Journal fact is recorded")
