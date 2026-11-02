"""Canonical validation for durable selected Run session state."""

# implementation of:
# Requirement: CA-R-1524
# Method: CA-M-405

from __future__ import annotations

from collections.abc import Mapping
from copy import deepcopy
from typing import Any, cast

from selected_execution_contracts import SelectedExecutionError
from workflow_run_support import LazyRunTracker, RunExecutionSession


class _SilentTracker:
    """Exercise canonical lifecycle checks without recording a Journal event."""

    def _record_run_event(self, *_: object) -> tuple[None, None]:
        return None, None


def _invalid(message: str) -> None:
    raise SelectedExecutionError(f"selected checkpoint lifecycle state is invalid: {message}")


def _receipt(
    probe: RunExecutionSession,
    actual: Mapping[str, Any],
    receipt: Mapping[str, Any],
    expected_disposition: str,
    errors: list[str],
) -> None:
    required = {
        "event_id",
        "run_id",
        "disposition",
        "outcome",
        "result_ref",
        "effect_refs",
        "report_ref",
    }
    if set(receipt) - (required | {"recording_error"}) or not required <= set(receipt):
        _invalid("a terminal receipt has unsupported fields")
    event_id = receipt["event_id"]
    if event_id is not None and not isinstance(event_id, str):
        _invalid("a terminal receipt event ID is invalid")
    error = receipt.get("recording_error")
    if error is not None and (not isinstance(error, str) or error not in errors):
        _invalid("a terminal receipt recording error is invalid")
    try:
        rebuilt = probe.finish_run(
            actual["run_id"],
            outcome=receipt["outcome"],
            result_ref=receipt["result_ref"],
            effect_refs=receipt["effect_refs"],
            report_ref=receipt["report_ref"],
        )
    except (KeyError, TypeError, ValueError) as error:
        raise SelectedExecutionError("selected checkpoint lifecycle state is invalid") from error
    if rebuilt["disposition"] != expected_disposition or any(
        receipt[key] != rebuilt[key] for key in required - {"event_id"}
    ):
        _invalid("a terminal receipt differs from the canonical lifecycle")


def _actual_probe(
    request: dict[str, Any],
    actual: Mapping[str, Mapping[str, Any]],
) -> RunExecutionSession:
    probe = RunExecutionSession(cast(LazyRunTracker, _SilentTracker()), deepcopy(request))
    if not set(actual) <= set(probe.requested):
        _invalid("actual Run map has an unknown requested Run")
    for requested_id in request["requested_runs"]:
        key = requested_id["requested_run_id"]
        if key in actual and probe.start_run(key, run_id=actual[key].get("run_id")) != actual[key]:
            _invalid("actual Run differs from the canonical requested Run")
    return probe


def _check_bindings(
    actual: Mapping[str, Mapping[str, Any]],
    terminal: Mapping[str, Mapping[str, Any]],
    interrupted: Mapping[str, Mapping[str, Any]],
) -> None:
    if set(terminal) & set(interrupted):
        _invalid("terminal and interrupted Run maps overlap")
    if not (set(terminal) | set(interrupted)) <= set(actual):
        _invalid("terminal evidence has no actual Run")


def _probe_state(
    request: dict[str, Any],
    actual: Mapping[str, Mapping[str, Any]],
    terminal: Mapping[str, Mapping[str, Any]],
    interrupted: Mapping[str, Mapping[str, Any]],
    observed_effects: Mapping[str, Mapping[str, Any]],
    recording_errors: list[str],
) -> None:
    try:
        _check_bindings(actual, terminal, interrupted)
        if not set(observed_effects) <= set(actual):
            _invalid("observed effects have no actual Run")
        probe = _actual_probe(request, actual)
        for key, observed in observed_effects.items():
            result_ref, effect_refs = observed.get("result_ref"), observed.get("effect_refs")
            if not isinstance(result_ref, str) or not isinstance(effect_refs, list):
                _invalid("observed effects are malformed")
            probe.note_effects(
                actual[key]["run_id"],
                result_ref=cast(str, result_ref),
                effect_refs=cast(list[str], effect_refs),
            )
            if probe.observed_effects[key] != observed:
                _invalid("observed effects differ from the canonical lifecycle")
        for key, receipt in terminal.items():
            _receipt(probe, actual[key], receipt, "terminal", recording_errors)
        for key, receipt in interrupted.items():
            _receipt(probe, actual[key], receipt, "interrupted", recording_errors)
    except (KeyError, TypeError, ValueError) as error:
        raise SelectedExecutionError("selected checkpoint lifecycle state is invalid") from error


def _validate_evidence(
    terminal: Mapping[str, Mapping[str, Any]],
    interrupted: Mapping[str, Mapping[str, Any]],
    evidence_digests: Mapping[str, str],
) -> None:
    references = {
        receipt["result_ref"]
        for receipt in (*terminal.values(), *interrupted.values())
        if isinstance(receipt.get("result_ref"), str)
    }
    if set(evidence_digests) != references or any(
        len(value) != 64 or any(character not in "0123456789abcdef" for character in value)
        for value in evidence_digests.values()
    ):
        _invalid("evidence digests do not exactly bind terminal results")


def validate_checkpoint_state(
    request: dict[str, Any],
    *,
    actual: Mapping[str, Mapping[str, Any]],
    terminal: Mapping[str, Mapping[str, Any]],
    interrupted: Mapping[str, Mapping[str, Any]],
    observed_effects: Mapping[str, Mapping[str, Any]],
    start_event_ids: Mapping[str, str],
    recording_errors: list[str],
    evidence_digests: Mapping[str, str],
) -> None:
    """Refuse a nested snapshot that canonical lifecycle calls cannot recreate."""
    _probe_state(request, actual, terminal, interrupted, observed_effects, recording_errors)
    if not set(start_event_ids) <= set(actual) or any(
        not isinstance(value, str) for value in start_event_ids.values()
    ):
        _invalid("a Run start event ID is invalid")
    _validate_evidence(terminal, interrupted, evidence_digests)
