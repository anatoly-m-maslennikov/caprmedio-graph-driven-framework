from __future__ import annotations

from collections.abc import Callable, Mapping
from pathlib import Path
from typing import Any, cast

from selected_execution_contracts import SelectedExecutionError
from selected_lifecycle_observation import journal_context, lifecycle_action_type, result_facts


def effect_paths(value: object) -> list[str]:
    candidates = value.get("paths", []) if isinstance(value, Mapping) else value
    if not isinstance(candidates, list):
        return []
    paths: list[str] = []
    for item in candidates:
        candidate = item.get("path") if isinstance(item, Mapping) else item
        if isinstance(item, Mapping) and not isinstance(candidate, str):
            carrier = item.get("carrier")
            candidate = carrier.get("path") if isinstance(carrier, Mapping) else None
        if isinstance(candidate, str):
            paths.append(candidate)
    return sorted(set(paths))


def terminal_outcome(outcome: str) -> str:
    return {
        "applied": "completed",
        "no-op": "no_op",
        "duplicate": "no_op",
        "failed": "failed",
        "partial": "partial",
        "canceled": "cancelled",
        "pending": "partial",
        "recording-blocked": "interrupted_pending",
        "blocked": "interrupted_pending",
    }.get(outcome, "interrupted_pending")


def effect_refs(root: Path, result: Mapping[str, Any]) -> list[str]:
    effects = result.get("effects")
    changed_effects = (
        [
            effect
            for effect in effects
            if isinstance(effect, Mapping) and effect.get("state") == "changed"
        ]
        if isinstance(effects, list)
        else []
    )
    refs = effect_paths(changed_effects)
    history = result.get("history")
    prior_revision = history.get("prior_revision") if isinstance(history, Mapping) else None
    if isinstance(prior_revision, Mapping):
        try:
            prior_facts, _ = result_facts(root, prior_revision)
        except SelectedExecutionError:
            pass
        else:
            refs = sorted({*refs, cast(str, prior_facts["path"])})
    return refs


def action_call(
    context: Mapping[str, Any],
    action: Callable[..., Mapping[str, Any]],
    call: Mapping[str, Any],
    session: Any,
    child_run_id: str,
    admitted: Mapping[str, Any],
) -> dict[str, Any]:
    effect_call = dict(call)
    import lifecycle_intents

    if (
        action is lifecycle_intents.update_atom_action
        and "subject_patches" in context["parameters"]
    ):
        effect_call.update(session=session, action_run_id=child_run_id, prior=admitted)
    return effect_call


def append_record(
    root: Path,
    session: Any,
    binding: Mapping[str, Any],
    admitted: Mapping[str, Any],
    before_facts: Mapping[str, Any],
    child_run_id: str,
    request_id: str,
    structural_scope: str,
    observed: tuple[dict[str, Any], bytes],
    effect_refs_value: list[str],
) -> tuple[list[str], Mapping[str, Any]]:
    observed_facts, observed_bytes = observed
    observed_path = cast(str, observed_facts["path"])
    if observed_path not in effect_refs_value:
        effect_refs_value = sorted([*effect_refs_value, observed_path])
    author, local_date, timezone, occurred_at = journal_context(session)
    action_pin = {
        "action_id": binding["atom_id"],
        "structural_scope": structural_scope,
        "occurred_at": occurred_at,
        "llm_session": {"app": "run-support", "uuid": request_id},
    }
    append_context = {"author": author, "local_date": local_date, "timezone": timezone}
    import selected_lifecycle_journal

    recording = selected_lifecycle_journal.record_lifecycle_change(
        root,
        before_result=admitted.get("before_result"),
        after_facts=observed_facts,
        current_bytes=observed_bytes,
        action_pin=action_pin,
        run_id=child_run_id,
        context=append_context,
        action_type=lifecycle_action_type(before_facts, observed_facts),
        native_effects={"result": {"state": "present", **observed_facts}},
    )
    return effect_refs_value, recording


def try_append_record(
    root: Path,
    session: Any,
    binding: Mapping[str, Any],
    admitted: Mapping[str, Any],
    before_facts: Mapping[str, Any],
    result: Mapping[str, Any],
    child_run_id: str,
    request_id: str,
    structural_scope: str,
    effect_refs_value: list[str],
) -> tuple[list[str], Mapping[str, Any] | None, str | None]:
    if result.get("outcome") not in {"applied", "pending"}:
        return effect_refs_value, None, None
    refs = effect_refs_value
    try:
        observed = result_facts(root, result.get("observed"))
        observed_path = cast(str, observed[0]["path"])
        refs = sorted({*effect_refs_value, observed_path})
        refs, recording = append_record(
            root,
            session,
            binding,
            admitted,
            before_facts,
            child_run_id,
            request_id,
            structural_scope,
            observed,
            refs,
        )
        return refs, recording, None
    except Exception as error:
        return refs, None, type(error).__name__


def write_payload(
    writer: Callable[[dict[str, Any]], object],
    child_run_id: str,
    binding: Mapping[str, Any],
    admitted: Mapping[str, Any],
    result: Mapping[str, Any],
    recording: Mapping[str, Any] | None,
    recording_error: str | None,
) -> str:
    payload: dict[str, Any] = {
        "lifecycle_action_run_id": child_run_id,
        "lifecycle_action_binding": dict(binding),
        "lifecycle_prior": dict(admitted),
        "native_result": dict(result),
    }
    if recording is not None:
        payload["lifecycle_recording"] = dict(recording)
    if recording_error is not None:
        payload["recording_error"] = recording_error
    result_ref = writer(payload)
    if not isinstance(result_ref, str) or not result_ref:
        raise SelectedExecutionError("lifecycle result writer returned an invalid reference")
    return result_ref


def child_completed(
    receipt: Mapping[str, Any], run_id: str, result_ref: str, refs: list[str]
) -> bool:
    return (
        receipt.get("run_id") == run_id
        and receipt.get("disposition") == "terminal"
        and receipt.get("outcome") == "completed"
        and receipt.get("result_ref") == result_ref
        and receipt.get("effect_refs") == refs
    )
