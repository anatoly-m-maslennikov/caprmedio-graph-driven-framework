"""Execute and record one current-state status mutation on its outer Run."""

from __future__ import annotations

from collections.abc import Callable, Mapping
from pathlib import Path
from typing import Any

from selected_execution_contracts import SelectedExecutionError
from selected_lifecycle_observation import (
    bound_action_structural_scope,
    result_facts,
)
from selected_lifecycle_status_result import status_envelope, try_record_status_change


Action = Callable[..., Mapping[str, Any]]


def _effect_paths(value: object) -> list[str]:
    candidates = value.get("paths", []) if isinstance(value, Mapping) else value
    if not isinstance(candidates, list):
        return []
    paths: list[str] = []
    for item in candidates:
        if isinstance(item, str):
            paths.append(item)
            continue
        if isinstance(item, Mapping):
            candidate = item.get("path")
            carrier = item.get("carrier")
            if not isinstance(candidate, str) and isinstance(carrier, Mapping):
                candidate = carrier.get("path")
            if isinstance(candidate, str):
                paths.append(candidate)
    return sorted(set(paths))


def _preview(
    root: Path, context: Mapping[str, Any], action: Action, call: Mapping[str, Any]
) -> dict[str, Any]:
    preview_call = {**dict(call), "execute": False, "authorized": True}
    preview = action(root, context["parameters"], **preview_call)
    if not isinstance(preview, Mapping) or not isinstance(preview.get("outcome"), str):
        raise SelectedExecutionError("status Action preview returned an invalid result")
    return dict(preview)


def _admit_before(
    root: Path,
    context: Mapping[str, Any],
    binding: Mapping[str, Any],
    preview: Mapping[str, Any],
) -> tuple[dict[str, Any], dict[str, Any], str, str]:
    structural_scope = bound_action_structural_scope(root, binding)
    before_facts, _ = result_facts(root, preview.get("observed"))
    request_id = context.get("execution_request_id")
    if not isinstance(request_id, str) or not request_id:
        raise SelectedExecutionError("status request identity is invalid")
    admitted = {"state": "observed", "before_result": {"state": "present", **before_facts}}
    return admitted, before_facts, structural_scope, request_id


def _run_status(
    root: Path,
    context: Mapping[str, Any],
    action: Action,
    call: Mapping[str, Any],
) -> tuple[dict[str, Any], str, list[str]]:
    result = action(root, context["parameters"], **dict(call))
    if not isinstance(result, Mapping) or not isinstance(result.get("outcome"), str):
        raise SelectedExecutionError("status Action returned an invalid result")
    result = dict(result)
    outcome = result["outcome"]
    effects = result.get("effects")
    changed = (
        [item for item in effects if isinstance(item, Mapping) and item.get("state") == "changed"]
        if isinstance(effects, list)
        else []
    )
    refs = _effect_paths(changed)
    history = result.get("history")
    prior = history.get("prior_revision") if isinstance(history, Mapping) else None
    if isinstance(prior, Mapping):
        try:
            prior_facts, _ = result_facts(root, prior)
        except SelectedExecutionError:
            pass
        else:
            refs = sorted({*refs, prior_facts["path"]})
    return result, outcome, refs


def lifecycle_status_change_atom(
    root: Path,
    context: dict[str, Any],
    action: Action,
    call: Mapping[str, Any],
) -> dict[str, Any]:
    """Retain W04 current state on the actual outer O128 status Run."""
    if context.get("restored_action") is True:
        return {
            "result": "lifecycle-recovery-required",
            "terminal_outcome": "interrupted_pending",
            "effect_refs": [],
        }
    session = context.get("session")
    binding = context.get("action_binding")
    action_run_id = context.get("action_run_id")
    if (
        session is None
        or not isinstance(binding, Mapping)
        or not isinstance(action_run_id, str)
        or not action_run_id
    ):
        return {
            "result": "lifecycle-recording-unavailable",
            "terminal_outcome": "interrupted_pending",
            "effect_refs": [],
        }
    preview = _preview(root, context, action, call)
    if preview["outcome"] in {"no-op", "duplicate"}:
        return {
            "result": "no-op",
            "terminal_outcome": "no_op",
            "effect_refs": [],
            "native_result": preview,
        }
    if preview["outcome"] != "preview":
        return {
            "result": str(preview["outcome"]),
            "terminal_outcome": "interrupted_pending",
            "effect_refs": [],
            "native_result": preview,
        }
    try:
        admitted, before_facts, structural_scope, request_id = _admit_before(
            root,
            context,
            binding,
            preview,
        )
    except Exception:
        return {
            "result": "lifecycle-prior-unavailable",
            "terminal_outcome": "interrupted_pending",
            "effect_refs": [],
        }
    result, outcome, effect_refs = _run_status(root, context, action, call)
    effect_refs, recording, recording_error = try_record_status_change(
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
    return status_envelope(outcome, result, effect_refs, admitted, recording, recording_error)
