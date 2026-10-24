"""Assemble retained graph output after evidence and terminal checks."""

from __future__ import annotations

from collections.abc import Callable, Mapping
import hashlib
from pathlib import Path
from typing import Any

from graph_completion import construction_outcome
from selected_evidence_io import bounded_read, safe_path
from selected_execution_contracts import SelectedExecutionError, canonical_json


def read_progress(
    root: Path,
    folder: Path,
    requested_action: str,
    session: Any,
) -> tuple[dict[str, Any], Path, str, list[str], str]:
    progress_path = folder / f"{requested_action}.json"
    progress_ref = progress_path.relative_to(root).as_posix()
    progress = bounded_read(safe_path(root, progress_ref))
    observation = progress.get("graph_construction_observation")
    action = session.actual.get(requested_action)
    if (
        progress.get("graph_construction_digest")
        != hashlib.sha256(canonical_json(observation)).hexdigest()
        or not isinstance(action, Mapping)
        or progress.get("action_run_id") != action.get("run_id")
    ):
        raise SelectedExecutionError(
            "saved graph construction evidence differs from its retained binding"
        )
    if not isinstance(observation, Mapping):
        raise SelectedExecutionError("saved graph construction evidence is invalid")
    effect_refs = progress.get("effect_refs")
    output_effects = observation.get("output_effects")
    if (
        not isinstance(effect_refs, list)
        or not isinstance(output_effects, Mapping)
        or effect_refs != output_effects.get("paths")
    ):
        raise SelectedExecutionError("saved graph effects differ from construction observation")
    expected_outcome = construction_outcome(observation)
    return progress, progress_path, progress_ref, list(effect_refs), expected_outcome


def read_aggregate(
    root: Path,
    folder: Path,
    graph: Mapping[str, Any],
    session: Any,
    run_id: str,
    requested_step: str,
    requested_action: str,
    effect_refs: list[str],
) -> tuple[dict[str, Any], Path, str, Mapping[str, Any]]:
    aggregate_path = folder / "graph_result.json"
    aggregate_ref = aggregate_path.relative_to(root).as_posix()
    aggregate = bounded_read(safe_path(root, aggregate_ref))
    rows = aggregate.get("step_results")
    actual_workflow = session.actual.get(run_id)
    actual_step = session.actual.get(requested_step)
    actual_action = session.actual.get(requested_action)
    if not all(
        isinstance(value, Mapping) for value in (actual_workflow, actual_step, actual_action)
    ):
        raise SelectedExecutionError("saved graph aggregate lacks its actual Run frontier")
    workflow_run_id = actual_workflow["run_id"]
    step_run_id = actual_step["run_id"]
    action_run_id = actual_action["run_id"]
    actions = graph["steps"][0]["actions"]
    if (
        aggregate.get("workflow_run_id") != workflow_run_id
        or aggregate.get("workflow_definition_id") != graph["workflow"]["atom_id"]
        or not isinstance(rows, list)
        or len(rows) != 1
        or not isinstance(rows[0], Mapping)
        or rows[0].get("action_run_id") != action_run_id
        or rows[0].get("step_run_id") != step_run_id
        or rows[0].get("action_definition_id") != actions[0]["atom_id"]
        or rows[0].get("step_definition_id") != graph["steps"][0]["atom_id"]
        or rows[0].get("effect_refs") != effect_refs
    ):
        raise SelectedExecutionError(
            "saved graph aggregate does not bind its actual Action frontier"
        )
    return aggregate, aggregate_path, aggregate_ref, rows[0]


def reconcile_outputs(
    progress: Mapping[str, Any],
    aggregate: Mapping[str, Any],
    row: Mapping[str, Any],
    finalized: Mapping[str, Any],
    result_label: str,
    session: Any,
    requested_step: str,
    run_id: str,
    aggregate_ref: str,
    effect_refs: list[str],
    expected_outcome: str,
    confirmer: Callable[[object, str, str, str, list[str]], bool],
) -> tuple[dict[str, Any], dict[str, Any]]:
    updated_progress = {
        **progress,
        "result": result_label,
        "native_result": dict(finalized),
    }
    updated_aggregate = {
        **aggregate,
        "outcome": "interrupted_pending",
        "step_results": [{**row, "result": result_label}],
    }
    actual_step = session.actual[requested_step]["run_id"]
    actual_workflow = session.actual[run_id]["run_id"]
    if all(
        confirmer(session.terminal.get(identity), actual_id, expected_outcome, aggregate_ref, refs)
        for identity, actual_id, refs in (
            (requested_step, actual_step, effect_refs),
            (run_id, actual_workflow, effect_refs),
        )
    ):
        updated_aggregate["outcome"] = expected_outcome
    return updated_progress, updated_aggregate
