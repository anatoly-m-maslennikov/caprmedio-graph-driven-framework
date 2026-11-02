"""Nested W03 replacement execution below the selected O128 Action."""

from __future__ import annotations

from collections.abc import Callable, Mapping
from pathlib import Path
from typing import Any

from selected_execution_contracts import SelectedExecutionError
from selected_replacement_result import (
    execute_replacement_action,
    finish_replacement,
    record_replacement,
)


def replacement_atom(
    root: Path,
    context: dict[str, Any],
    action: Callable[..., Mapping[str, Any]],
    call: Mapping[str, Any],
) -> dict[str, Any]:
    """Execute O051 once as O128's predeclared source-bound child."""
    session = context.get("session")
    requested_child = context.get("replacement_requested_run_id")
    binding = context.get("replacement_action_binding")
    writer = context.get("replacement_result_writer")
    if (
        session is None
        or not isinstance(requested_child, str)
        or not requested_child
        or not isinstance(binding, Mapping)
        or not callable(writer)
    ):
        return {
            "result": "replacement-recording-unavailable",
            "terminal_outcome": "interrupted_pending",
            "effect_refs": [],
        }
    try:
        from selected_lifecycle_observation import journal_context, replacement_structural_scope

        author, local_date, timezone, occurred_at = journal_context(session)
        structural_scope = replacement_structural_scope(root, binding)
    except SelectedExecutionError:
        return {
            "result": "predecessor-journal-required",
            "terminal_outcome": "interrupted_pending",
            "effect_refs": [],
        }

    # A retained child is evidence of an earlier invocation; never replay O051.
    if requested_child in getattr(session, "actual", {}):
        return {
            "result": "replacement-recovery-required",
            "terminal_outcome": "interrupted_pending",
            "effect_refs": [],
        }
    child_actual = session.start_run(requested_child)
    child_run_id = child_actual["run_id"]
    result, effect_refs, canonical_event, recording_error, native_outcome, result_ref = (
        execute_replacement_action(
            root,
            context,
            action,
            call,
            binding,
            writer,
            child_run_id,
            author,
            occurred_at,
            structural_scope,
        )
    )
    recording = None
    if canonical_event is not None:
        recording, append_error = record_replacement(
            root, canonical_event, author, local_date, timezone
        )
        if append_error is not None:
            recording_error = append_error
    return finish_replacement(
        session,
        requested_child,
        child_run_id,
        native_outcome,
        result_ref,
        effect_refs,
        result,
        recording,
        recording_error,
    )
