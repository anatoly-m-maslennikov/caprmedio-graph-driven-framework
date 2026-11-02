"""Canonical selected-run terminal and recovery completion."""

from __future__ import annotations

from collections.abc import Mapping
from typing import Any, cast

from selected_execution_contracts import SelectedExecutionError


def finish_selected_run(
    session: Any,
    requested_id: str,
    run_id: str,
    *,
    recovery: bool = False,
    **result: Any,
) -> Mapping[str, Any]:
    """Reuse canonical finals, or record recovery without a second start."""
    if not recovery:
        return cast(Mapping[str, Any], session.finish_run(run_id, **result))
    terminal = session.terminal.get(requested_id)
    if terminal is not None:
        expected = {"run_id": run_id, "disposition": "terminal", **result}
        if any(terminal.get(key) != value for key, value in expected.items()):
            raise SelectedExecutionError(
                "retained Run terminal differs from recovered graph evidence"
            )
        return dict(terminal)
    if requested_id in session.interrupted:
        if result.get("outcome") == "interrupted_pending":
            # Retain the original uncertainty; do not invent another
            # interruption or pretend a failed recovery attempt is final.
            return dict(session.interrupted[requested_id])
        return cast(Mapping[str, Any], session.recover_run(run_id, **result))
    return cast(Mapping[str, Any], session.finish_run(run_id, **result))
