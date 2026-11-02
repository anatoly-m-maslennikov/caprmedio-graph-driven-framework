"""Durable W01 result, Journal attempt, and child receipt handling."""

from __future__ import annotations

from collections.abc import Callable, Mapping
from pathlib import Path
from typing import Any

from selected_execution_contracts import SelectedExecutionError
from selected_run_completion import finish_selected_run


def canonical_creation_record(
    session: Any,
    context: Mapping[str, Any],
    result: Mapping[str, Any],
    binding: Mapping[str, Any],
    child_run_id: str,
    structural_scope: str,
) -> tuple[Mapping[str, Any] | None, tuple[str, str, str] | None, str | None]:
    """Attempt the canonical ADD fact without making it an admission gate."""
    if result.get("outcome") != "applied":
        return None, None, None
    try:
        import selected_creation_journal
        from selected_lifecycle_observation import journal_context

        author, local_date, timezone, occurred_at = journal_context(session)
        event = selected_creation_journal.canonical_event(
            parameters=context.get("parameters"),
            native_result=result,
            creation_binding=binding,
            creation_action_run_id=child_run_id,
            execution_request_id=context.get("execution_request_id"),
            author=author,
            occurred_at=occurred_at,
            structural_scope=structural_scope,
        )
        return event, (author, local_date, timezone), None
    except Exception as error:
        return None, None, type(error).__name__


def write_creation_result(
    writer: Callable[..., Any],
    child_run_id: str,
    result: Mapping[str, Any],
    canonical_event: Mapping[str, Any] | None,
    recording_error: str | None,
) -> str:
    """Persist the actual child result before any Journal delivery attempt."""
    payload: dict[str, Any] = {
        "creation_action_run_id": child_run_id,
        "native_result": result,
    }
    if canonical_event is not None:
        payload["canonical_event"] = dict(canonical_event)
    if recording_error is not None:
        payload["recording_error"] = recording_error
    result_ref = writer(payload)
    if not isinstance(result_ref, str) or not result_ref:
        raise SelectedExecutionError("creation result writer returned an invalid reference")
    return result_ref


def record_creation_event(
    root: Path,
    canonical_event: Mapping[str, Any] | None,
    journal_context_values: tuple[str, str, str] | None,
) -> tuple[Mapping[str, Any] | None, str | None]:
    """Attempt Journal delivery only after the actual child result is durable."""
    if canonical_event is None or journal_context_values is None:
        return None, None
    author, local_date, timezone = journal_context_values
    try:
        import selected_creation_journal

        recording = selected_creation_journal.record_selected_creation(
            root,
            canonical_event=canonical_event,
            author=author,
            local_date=local_date,
            timezone=timezone,
        )
    except Exception as error:
        return None, type(error).__name__
    return recording, None


def complete_creation(
    session: Any,
    requested_child: str,
    child_run_id: str,
    native_outcome: str,
    effect_refs: list[str],
    result_ref: str,
    result: Mapping[str, Any],
    recording: Mapping[str, Any] | None,
    recording_error: str | None,
) -> dict[str, Any]:
    """Finish the child once and expose recording-pending when required."""
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
        and child_receipt.get("run_id") == child_run_id
        and child_receipt.get("disposition") == "terminal"
        and child_receipt.get("outcome") == "completed"
        and child_receipt.get("result_ref") == result_ref
        and child_receipt.get("effect_refs") == effect_refs
    )
    if native_outcome == "applied" and not child_recorded:
        return {
            "result": "recording-pending",
            "terminal_outcome": "partial",
            "effect_refs": effect_refs,
            "native_result": result,
            "creation_recording": recording,
            "recording_error": recording_error,
            "creation_child_receipt": child_receipt,
        }
    return {
        "result": {"duplicate": "no-op", "no-op": "no-op"}.get(native_outcome, native_outcome),
        "terminal_outcome": child_outcome,
        "effect_refs": effect_refs,
        "native_result": result,
        "creation_recording": recording,
        "recording_error": recording_error,
        "creation_child_receipt": child_receipt,
    }
