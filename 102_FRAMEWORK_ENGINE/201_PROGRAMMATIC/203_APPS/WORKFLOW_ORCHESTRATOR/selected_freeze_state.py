"""Source-bound selected-Run freeze, load, and revalidation capabilities."""

from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path
from typing import Any

from selected_execution_contracts import SelectedExecutionError, canonical_json
from selected_execution_run_plan import build_requested_runs, declared_run_visit_limits
from selected_evidence_io import atomic_write, bounded_read, run_directory
from selected_graph_admission import validate_lifecycle_admission, validate_query_admission
from selected_graph_validation import validate_graph


def workflow_identity(execution: Mapping[str, Any]) -> str | None:
    direct = execution.get("workflow_run_id")
    if isinstance(direct, str):
        return direct
    requested = execution.get("requested_runs")
    if isinstance(requested, list):
        rows = [
            row for row in requested if isinstance(row, Mapping) and row.get("kind") == "workflow"
        ]
        if len(rows) == 1 and isinstance(rows[0].get("requested_run_id"), str):
            return str(rows[0]["requested_run_id"])
    return None


def _expected_requested_runs(
    root: Path, execution: Mapping[str, Any], graph: Mapping[str, Any], run_id: str
) -> list[dict[str, Any]]:
    expected = build_requested_runs(graph, run_id, declared_run_visit_limits(execution))
    parameters = execution.get("parameters", {})
    if graph.get("route") == "update_atom" and "subject_batch" in parameters:
        from subject_batch import build_subject_batch_requested_runs, load_subject_batch

        packet = load_subject_batch(root, execution["parameters"])
        expected = build_subject_batch_requested_runs(graph, run_id, len(packet["atoms"]))
    return expected


def validate_requested_runs(
    root: Path, execution: Mapping[str, Any], graph: Mapping[str, Any], run_id: str
) -> None:
    """Require caller Runs to exactly bind every allowed selected-graph visit."""
    requested = execution.get("requested_runs")
    if not isinstance(requested, list):
        raise SelectedExecutionError("selected execution must declare requested Runs")
    expected = _expected_requested_runs(root, execution, graph, run_id)
    if canonical_json(requested) != canonical_json(expected):
        raise SelectedExecutionError(
            "requested Runs do not exactly bind the selected Workflow graph"
        )


def _validated_freeze(root: Path, request: Mapping[str, Any]) -> dict[str, Any]:
    if not isinstance(request, Mapping) or request.get("operation") != "enqueue_selected":
        raise SelectedExecutionError("selected enqueue operation is required")
    run_id = request.get("run_id")
    execution = request.get("execution")
    if not isinstance(run_id, str) or not isinstance(execution, Mapping):
        raise SelectedExecutionError("selected run ID and execution are required")
    if workflow_identity(execution) != run_id:
        raise SelectedExecutionError(
            "requested Workflow Run identity must match enqueue_selected run_id"
        )
    graph = validate_graph(root, execution)
    validate_requested_runs(root, execution, graph, run_id)
    return {
        "request": {
            "operation": "enqueue_selected",
            "run_id": run_id,
            "execution": dict(execution),
        },
        "graph": graph,
    }


def _attach_admissions(root: Path, frozen: dict[str, Any]) -> None:
    execution = frozen["request"]["execution"]
    validate_query_admission(frozen["graph"], execution)
    lifecycle = validate_lifecycle_admission(root, frozen["graph"], execution)
    if lifecycle is not None:
        frozen["lifecycle_admission"] = lifecycle


def freeze(root: Path, request: Mapping[str, Any]) -> dict[str, Any]:
    """Validate and durably freeze one selected request before queue dispatch."""
    frozen = _validated_freeze(root, request)
    _attach_admissions(root, frozen)
    run_id = frozen["request"]["run_id"]
    path = run_directory(root, run_id) / "selected_request.json"
    if path.exists():
        saved = bounded_read(path)
        if canonical_json(saved) != canonical_json(frozen):
            raise SelectedExecutionError("Run ID already binds a different selected request")
        return saved
    atomic_write(path, frozen)
    return frozen


def load(root: Path, run_id: str) -> dict[str, Any]:
    """Read only the exact frozen selected request for one queue identity."""
    path = run_directory(root, run_id) / "selected_request.json"
    if not path.is_file():
        raise FileNotFoundError(path)
    return bounded_read(path)


def revalidate(root: Path, frozen: Mapping[str, Any]) -> dict[str, Any]:
    request = frozen.get("request")
    if not isinstance(request, Mapping) or not isinstance(request.get("execution"), Mapping):
        raise SelectedExecutionError("saved selected request is invalid")
    current = validate_graph(root, request["execution"])
    if canonical_json(current) != canonical_json(frozen.get("graph")):
        raise SelectedExecutionError("selected Workflow graph changed after queue admission")
    return current
