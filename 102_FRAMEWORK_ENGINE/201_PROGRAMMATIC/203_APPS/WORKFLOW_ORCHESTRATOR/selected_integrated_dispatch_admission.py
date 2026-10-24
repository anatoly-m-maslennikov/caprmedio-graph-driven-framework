"""Canonical admission without LazyRunTracker's terminal interruption path."""

from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path
import sys
from typing import Any

from selected_execution_contracts import SelectedExecutionError


def validate(tracker: Any, execution: Mapping[str, Any]) -> dict[str, Any]:
    """Run the common selected-Run gates for every Integrated entry."""
    tools = str(Path(__file__).resolve().parents[2] / "201_TOOLS")
    if tools not in sys.path:
        sys.path.insert(0, tools)
    from workflow_run_support import (
        RunExecutionSession,
        _canonical_digest,
        _common_bytes,
        _proposal,
        _validate_common,
    )

    parsed = _validate_common(execution)
    if parsed["mode"] != "execute":
        raise SelectedExecutionError("Integrated dispatch requires an execute request")
    requests = getattr(tracker, "_requests", None)
    if not isinstance(requests, dict):
        raise SelectedExecutionError("Integrated dispatch requires a canonical Run tracker")
    fingerprint = _common_bytes(parsed)
    recorded = requests.get(parsed["request_id"])
    if recorded is not None and recorded != fingerprint:
        raise SelectedExecutionError("selected request ID already binds different request bytes")
    requests.setdefault(parsed["request_id"], fingerprint)
    observation = tracker._observe(parsed)
    proposal = _proposal(parsed, observation)
    if not observation["selected"] or not observation["current"]:
        raise SelectedExecutionError("selected source currentness requires revalidation")
    tracker._validate_execute(parsed, proposal, _canonical_digest(proposal))
    RunExecutionSession.canonical_requested_definition_bindings(parsed["requested_runs"])
    return parsed


def register(root: Path, tracker: Any, parsed: Mapping[str, Any]) -> None:
    """Register only the first admitted dispatch, after common validation."""
    tools = str(Path(__file__).resolve().parents[2] / "201_TOOLS")
    if tools not in sys.path:
        sys.path.insert(0, tools)
    import work_journal

    dispatch, created = work_journal.register_selected_run_dispatch(
        root,
        request_id=parsed["request_id"],
        canonical_request_bytes=tracker._dispatch_bytes(parsed),
    )
    if not created:
        raise SelectedExecutionError(
            f"accepted selected dispatch is retained as {dispatch['state']}; inspect before replay"
        )
