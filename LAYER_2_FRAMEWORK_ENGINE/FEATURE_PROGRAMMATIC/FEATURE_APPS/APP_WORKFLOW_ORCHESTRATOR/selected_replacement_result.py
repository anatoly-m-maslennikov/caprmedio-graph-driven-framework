"""Result and terminalization helpers for nested O051 execution."""

from __future__ import annotations

from collections.abc import Callable, Mapping
from pathlib import Path
from typing import Any

from selected_execution_contracts import SelectedExecutionError
from selected_run_completion import finish_selected_run


def effect_paths(value: object) -> list[str]:
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


def execute_replacement_action(
    root: Path,
    context: Mapping[str, Any],
    action: Callable[..., Mapping[str, Any]],
    call: Mapping[str, Any],
    binding: Mapping[str, Any],
    writer: Callable[..., object],
    child_run_id: str,
    author: str,
    occurred_at: str,
    structural_scope: str,
) -> tuple[
    dict[str, Any],
    list[str],
    Mapping[str, Any] | None,
    str | None,
    str,
    str,
]:
    """Run O051, build its observed event, and durably write child evidence."""
    try:
        result = action(root, context["parameters"], **dict(call))
    except Exception:
        # The shared session interruption path owns unexpected Tool failures.
        raise
    if not isinstance(result, Mapping) or not isinstance(result.get("outcome"), str):
        raise SelectedExecutionError("replacement Action returned an invalid result")
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
    effect_refs = effect_paths(changed_effects)
    canonical_event: Mapping[str, Any] | None = None
    recording_error: str | None = None
    if native_outcome == "applied":
        try:
            import selected_replacement_journal

            canonical_event = selected_replacement_journal.canonical_event(
                parameters=context.get("parameters"),
                native_result=result,
                replacement_binding=binding,
                replacement_action_run_id=child_run_id,
                execution_request_id=context.get("execution_request_id"),
                author=author,
                occurred_at=occurred_at,
                structural_scope=structural_scope,
            )
        except SelectedExecutionError as error:
            recording_error = str(error)
    payload: dict[str, Any] = {
        "replacement_action_run_id": child_run_id,
        "native_result": result,
    }
    if canonical_event is not None:
        payload["canonical_event"] = dict(canonical_event)
    if recording_error is not None:
        payload["recording_error"] = recording_error
    result_ref = writer(payload)
    if not isinstance(result_ref, str) or not result_ref:
        raise SelectedExecutionError("replacement result writer returned an invalid reference")
    return result, effect_refs, canonical_event, recording_error, native_outcome, result_ref


def record_replacement(
    root: Path,
    canonical_event: Mapping[str, Any],
    author: str,
    local_date: str,
    timezone: str,
) -> tuple[Mapping[str, Any] | None, str | None]:
    """Append the observed replacement event without replaying the Tool."""
    try:
        import selected_replacement_journal

        recording = selected_replacement_journal.record_selected_replacement(
            root,
            canonical_event=canonical_event,
            author=author,
            local_date=local_date,
            timezone=timezone,
        )
    except Exception as error:
        # Logging failure does not change the observed native outcome.
        return None, type(error).__name__
    return recording, None


def finish_replacement(
    session: Any,
    requested_child: str,
    child_run_id: str,
    native_outcome: str,
    result_ref: str,
    effect_refs: list[str],
    result: Mapping[str, Any],
    recording: Mapping[str, Any] | None,
    recording_error: str | None,
) -> dict[str, Any]:
    """Finish the nested child and expose truthful partial recording state."""
    child_outcome = {
        "applied": "completed",
        "no-op": "no_op",
        "duplicate": "no_op",
        "failed": "failed",
        "partial": "partial",
        "canceled": "cancelled",
        "recording-blocked": "interrupted_pending",
        "blocked": "interrupted_pending",
    }.get(native_outcome, "interrupted_pending")
    if effect_refs:
        session.note_effects(child_run_id, result_ref=result_ref, effect_refs=effect_refs)
    child_receipt = finish_selected_run(
        session,
        requested_child,
        child_run_id,
        outcome=child_outcome,
        result_ref=result_ref,
        effect_refs=effect_refs,
    )
    child_recorded = (
        isinstance(child_receipt, Mapping)
        and child_receipt.get("disposition") == "terminal"
        and child_receipt.get("outcome") == "completed"
    )
    if native_outcome == "applied" and not child_recorded:
        return {
            "result": "recording-pending",
            "terminal_outcome": "partial",
            "effect_refs": effect_refs,
            "native_result": dict(result),
            "replacement_recording": recording,
            "recording_error": recording_error,
            "replacement_child_receipt": child_receipt,
        }
    result_label = {"duplicate": "no-op", "no-op": "no-op"}.get(native_outcome, native_outcome)
    return {
        "result": result_label,
        "terminal_outcome": child_outcome,
        "effect_refs": effect_refs,
        "native_result": dict(result),
        "replacement_recording": recording,
        "recording_error": recording_error,
        "replacement_child_receipt": child_receipt,
    }
