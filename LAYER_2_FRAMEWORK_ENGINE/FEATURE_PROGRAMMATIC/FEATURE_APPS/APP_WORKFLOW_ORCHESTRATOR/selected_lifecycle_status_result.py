"""Journal and result-envelope capabilities for current-state status changes."""

from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path
from typing import Any

from selected_lifecycle_observation import journal_context, lifecycle_action_type, result_facts


def record_status_change(
    root: Path,
    session: Any,
    binding: Mapping[str, Any],
    action_run_id: str,
    before_facts: Mapping[str, Any],
    result: Mapping[str, Any],
    admitted: Mapping[str, Any],
    structural_scope: str,
    request_id: str,
    effect_refs: list[str],
) -> tuple[list[str], Mapping[str, Any]]:
    """Append after-facts without making Journal delivery an effect gate."""
    observed_facts, observed_bytes = result_facts(root, result.get("observed"))
    if observed_facts["path"] not in effect_refs:
        effect_refs.append(observed_facts["path"])
        effect_refs.sort()
    author, local_date, timezone, occurred_at = journal_context(session)
    action_pin = {
        "action_id": binding["atom_id"],
        "structural_scope": structural_scope,
        "occurred_at": occurred_at,
        "llm_session": {"app": "run-support", "uuid": request_id},
    }
    context = {"author": author, "local_date": local_date, "timezone": timezone}
    import selected_lifecycle_journal

    recording = selected_lifecycle_journal.record_lifecycle_change(
        root,
        before_result=admitted.get("before_result"),
        after_facts=observed_facts,
        current_bytes=observed_bytes,
        action_pin=action_pin,
        run_id=action_run_id,
        context=context,
        action_type=lifecycle_action_type(before_facts, observed_facts),
        native_effects={"result": {"state": "present", **observed_facts}},
    )
    return effect_refs, recording


def try_record_status_change(
    root: Path,
    session: Any,
    binding: Mapping[str, Any],
    action_run_id: str,
    before_facts: Mapping[str, Any],
    result: Mapping[str, Any],
    admitted: Mapping[str, Any],
    structural_scope: str,
    request_id: str,
    effect_refs: list[str],
) -> tuple[list[str], Mapping[str, Any] | None, str | None]:
    """Attempt Journal delivery after the native status result exists."""
    if result.get("outcome") not in {"applied", "pending"}:
        return effect_refs, None, None
    try:
        effect_refs, recording = record_status_change(
            root,
            session,
            binding,
            action_run_id,
            before_facts,
            result,
            admitted,
            structural_scope,
            request_id,
            effect_refs,
        )
    except Exception as error:
        return effect_refs, None, type(error).__name__
    return effect_refs, recording, None


def status_envelope(
    outcome: str,
    result: Mapping[str, Any],
    effect_refs: list[str],
    admitted: Mapping[str, Any],
    recording: Mapping[str, Any] | None,
    recording_error: str | None,
) -> dict[str, Any]:
    """Return the outer-Run evidence envelope for a status result."""
    if outcome == "pending":
        return {
            "result": "recording-pending",
            "terminal_outcome": "partial",
            "effect_refs": effect_refs,
            "native_result": result,
            "lifecycle_prior": dict(admitted),
            "lifecycle_recording": recording,
            "recording_error": recording_error,
        }
    terminal = {
        "applied": "completed",
        "no-op": "no_op",
        "duplicate": "no_op",
    }.get(outcome, "interrupted_pending")
    return {
        "result": {"duplicate": "no-op"}.get(outcome, outcome),
        "terminal_outcome": terminal,
        "effect_refs": effect_refs,
        "native_result": result,
        "lifecycle_prior": dict(admitted),
        "lifecycle_recording": recording,
        "recording_error": recording_error,
    }
