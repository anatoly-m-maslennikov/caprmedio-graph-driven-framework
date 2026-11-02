"""Execute and record one source-observed lifecycle mutation."""

from __future__ import annotations

from collections.abc import Callable, Mapping
from pathlib import Path
from typing import Any, cast

from selected_execution_contracts import SelectedExecutionError
from selected_lifecycle_observation import (
    bound_action_structural_scope,
    lifecycle_structural_scope,
    result_facts,
)
from selected_run_completion import finish_selected_run
from selected_lifecycle_result import (
    action_call,
    child_completed,
    effect_refs,
    terminal_outcome,
    try_append_record,
    write_payload,
)


Action = Callable[..., Mapping[str, Any]]


def _run_action(
    root: Path,
    context: Mapping[str, Any],
    action: Action,
    effect_call: Mapping[str, Any],
) -> dict[str, Any]:
    result = action(root, context["parameters"], **dict(effect_call))
    if not isinstance(result, Mapping) or not isinstance(result.get("outcome"), str):
        raise SelectedExecutionError("lifecycle Action returned an invalid result")
    return dict(result)


def _admit_before(
    root: Path,
    context: Mapping[str, Any],
    binding: Mapping[str, Any],
    preview: Mapping[str, Any],
) -> tuple[dict[str, Any], str, str]:
    observer_binding = context.get("action_binding")
    observer_run_id = context.get("action_run_id")
    if (
        not isinstance(observer_binding, Mapping)
        or not isinstance(observer_run_id, str)
        or not observer_run_id
    ):
        raise SelectedExecutionError("lifecycle observation has no actual observing Action Run")
    bound_action_structural_scope(root, observer_binding)
    structural_scope = lifecycle_structural_scope(root, binding)
    before_facts, _ = result_facts(root, preview.get("observed"))
    request_id = context.get("execution_request_id")
    if not isinstance(request_id, str) or not request_id:
        raise SelectedExecutionError("lifecycle request identity is invalid")
    admitted = {"state": "observed", "before_result": {"state": "present", **before_facts}}
    return admitted, structural_scope, request_id


def _preview(
    root: Path, context: Mapping[str, Any], action: Action, call: Mapping[str, Any]
) -> dict[str, Any]:
    preview_call = {**dict(call), "execute": False, "authorized": True}
    preview = action(root, context["parameters"], **preview_call)
    if not isinstance(preview, Mapping) or not isinstance(preview.get("outcome"), str):
        raise SelectedExecutionError("lifecycle Action preview returned an invalid result")
    return dict(preview)


def _non_preview(preview: Mapping[str, Any]) -> dict[str, Any]:
    outcome = cast(str, preview["outcome"])
    if outcome in {"no-op", "duplicate"}:
        return {
            "result": "no-op",
            "terminal_outcome": "no_op",
            "effect_refs": [],
            "native_result": dict(preview),
        }
    label = {"duplicate": "no-op", "no-op": "no-op"}.get(outcome, outcome)
    return {
        "result": label,
        "terminal_outcome": {
            "applied": "completed",
            "no-op": "no_op",
            "duplicate": "no_op",
            "failed": "failed",
            "partial": "partial",
            "canceled": "cancelled",
            "recording-blocked": "interrupted_pending",
            "blocked": "interrupted_pending",
        }.get(outcome, "interrupted_pending"),
        "effect_refs": [],
        "native_result": dict(preview),
    }


def lifecycle_change_atom(
    root: Path,
    context: dict[str, Any],
    action: Action,
    call: Mapping[str, Any],
) -> dict[str, Any]:
    """Record W02/W04's observed transition around one native child Run."""
    session = context.get("session")
    requested_child = context.get("lifecycle_requested_run_id")
    binding = context.get("lifecycle_action_binding")
    writer = context.get("lifecycle_result_writer")
    if (
        session is None
        or not isinstance(requested_child, str)
        or not requested_child
        or not isinstance(binding, Mapping)
        or not callable(writer)
    ):
        return {
            "result": "lifecycle-recording-unavailable",
            "terminal_outcome": "interrupted_pending",
            "effect_refs": [],
        }
    if requested_child in getattr(session, "actual", {}):
        return {
            "result": "lifecycle-recovery-required",
            "terminal_outcome": "interrupted_pending",
            "effect_refs": [],
        }
    preview = _preview(root, context, action, call)
    if cast(str, preview["outcome"]) != "preview":
        return _non_preview(preview)
    try:
        admitted, structural_scope, request_id = _admit_before(root, context, binding, preview)
    except Exception:
        return {
            "result": "lifecycle-prior-unavailable",
            "terminal_outcome": "interrupted_pending",
            "effect_refs": [],
        }
    child_actual = session.start_run(requested_child)
    child_run_id = cast(str, child_actual["run_id"])
    result = _run_action(
        root, context, action, action_call(context, action, call, session, child_run_id, admitted)
    )
    before_facts = cast(Mapping[str, Any], admitted["before_result"])
    refs, recording, recording_error = try_append_record(
        root,
        session,
        binding,
        admitted,
        before_facts,
        result,
        child_run_id,
        request_id,
        structural_scope,
        effect_refs(root, result),
    )
    writer_fn = cast(Callable[[dict[str, Any]], object], writer)
    result_ref = write_payload(
        writer_fn, child_run_id, binding, admitted, result, recording, recording_error
    )
    outcome = cast(str, result["outcome"])
    child_outcome = terminal_outcome(outcome)
    if refs:
        session.note_effects(child_run_id, result_ref=result_ref, effect_refs=refs)
    child_receipt = finish_selected_run(
        session,
        requested_child,
        child_run_id,
        outcome=child_outcome,
        result_ref=result_ref,
        effect_refs=refs,
    )
    if outcome in {"applied", "pending"} and (
        outcome != "applied"
        or not isinstance(child_receipt, Mapping)
        or not child_completed(child_receipt, child_run_id, result_ref, refs)
    ):
        return {
            "result": "recording-pending",
            "terminal_outcome": "partial",
            "effect_refs": refs,
            "native_result": result,
            "lifecycle_recording": recording,
            "recording_error": recording_error,
            "lifecycle_child_receipt": child_receipt,
        }
    return {
        "result": {"duplicate": "no-op", "no-op": "no-op"}.get(outcome, outcome),
        "terminal_outcome": child_outcome,
        "effect_refs": refs,
        "native_result": result,
        "lifecycle_recording": recording,
        "recording_error": recording_error,
        "lifecycle_child_receipt": child_receipt,
    }
