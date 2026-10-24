"""Nested W01 creation execution below the selected O128 Action."""

from __future__ import annotations

from collections.abc import Callable, Mapping
from pathlib import Path
from typing import Any

from selected_creation_result import (
    canonical_creation_record,
    complete_creation,
    record_creation_event,
    write_creation_result,
)
from selected_execution_contracts import SelectedExecutionError
from selected_lifecycle_observation import creation_structural_scope


def _effect_paths(value: object) -> list[str]:
    candidates = value.get("paths", []) if isinstance(value, Mapping) else value
    if not isinstance(candidates, list):
        return []
    output: list[str] = []
    for item in candidates:
        if isinstance(item, str):
            output.append(item)
        elif isinstance(item, Mapping):
            carrier = item.get("carrier")
            candidate = item.get("path")
            if not isinstance(candidate, str) and isinstance(carrier, Mapping):
                candidate = carrier.get("path")
            if isinstance(candidate, str):
                output.append(candidate)
    return sorted(set(output))


def _creation_admission(
    root: Path,
    context: Mapping[str, Any],
) -> tuple[Any, str, Mapping[str, Any], Callable[..., Any], str] | dict[str, Any]:
    session = context.get("session")
    requested_child = context.get("creation_requested_run_id")
    binding = context.get("creation_action_binding")
    writer = context.get("creation_result_writer")
    unavailable = {
        "result": "creation-recording-unavailable",
        "terminal_outcome": "interrupted_pending",
        "effect_refs": [],
    }
    if (
        session is None
        or not isinstance(requested_child, str)
        or not requested_child
        or not isinstance(binding, Mapping)
        or not callable(writer)
    ):
        return unavailable
    try:
        structural_scope = creation_structural_scope(root, binding)
    except SelectedExecutionError:
        return unavailable
    if requested_child in getattr(session, "actual", {}):
        return {
            "result": "creation-recovery-required",
            "terminal_outcome": "interrupted_pending",
            "effect_refs": [],
        }
    return session, requested_child, binding, writer, structural_scope


def _run_creation_action(
    root: Path,
    context: Mapping[str, Any],
    action: Callable[..., Mapping[str, Any]],
    call: Mapping[str, Any],
) -> tuple[dict[str, Any], str, list[str]]:
    result = action(root, context["parameters"], **dict(call))
    if not isinstance(result, Mapping) or not isinstance(result.get("outcome"), str):
        raise SelectedExecutionError("creation Action returned an invalid result")
    result = dict(result)
    native_outcome = result["outcome"]
    changed_effects = (
        [
            effect
            for effect in result.get("effects", [])
            if isinstance(effect, Mapping) and effect.get("state") == "changed"
        ]
        if isinstance(result.get("effects"), list)
        else []
    )
    return result, native_outcome, _effect_paths(changed_effects)


def creation_atom(
    root: Path,
    context: dict[str, Any],
    action: Callable[..., Mapping[str, Any]],
    call: Mapping[str, Any],
) -> dict[str, Any]:
    """Execute O032 once below O128 and preserve its canonical ADD fact."""
    admission = _creation_admission(root, context)
    if isinstance(admission, dict):
        return admission
    session, requested_child, binding, writer, structural_scope = admission
    child_actual = session.start_run(requested_child)
    child_run_id = child_actual["run_id"]
    result, native_outcome, effect_refs = _run_creation_action(
        root,
        context,
        action,
        call,
    )
    canonical_event, journal_values, recording_error = canonical_creation_record(
        session,
        context,
        result,
        binding,
        child_run_id,
        structural_scope,
    )
    result_ref = write_creation_result(
        writer,
        child_run_id,
        result,
        canonical_event,
        recording_error,
    )
    recording, delivery_error = record_creation_event(root, canonical_event, journal_values)
    if canonical_event is not None:
        recording_error = delivery_error
    return complete_creation(
        session,
        requested_child,
        child_run_id,
        native_outcome,
        effect_refs,
        result_ref,
        result,
        recording,
        recording_error,
    )
