"""Plain, nonblocking Journal recording for host release invocations."""

from collections.abc import Callable
from pathlib import Path


def record_release_event(
    root: Path,
    operation: str,
    run_id: str,
    event: str,
    preceding: str | None,
    outcome: str | None = None,
) -> tuple[str | None, str | None]:
    try:
        from work_journal import append_record, event_record

        record = event_record(
            root=root,
            event=event,
            action_id=run_id,
            kind="workflow",
            scope="project",
            operation=operation,
            session_id=run_id,
            subjects=[],
            outputs=[],
            preceding_event=preceding,
            details={"outcome": outcome} if outcome is not None else {},
        )
        append_record(root, record)
        event_id = record.get("event_id")
        return event_id if isinstance(event_id, str) else None, None
    except (AttributeError, ImportError, OSError, RuntimeError, TypeError, ValueError) as error:
        return None, f"Release {event} recording failed: {error}"


def run_recorded_release(
    root: Path,
    operation: str,
    run_id: str,
    invoke: Callable[[], dict[str, object]],
) -> dict[str, object]:
    started, start_error = record_release_event(root, operation, run_id, "started", None)
    try:
        result = invoke()
    except (AttributeError, ImportError, OSError, RuntimeError, TypeError, ValueError) as error:
        result = {
            "outcome": "failed",
            "failed_step": "invocation",
            "error_type": type(error).__name__,
        }
    observed_outcome = result.get("outcome", "failed")
    outcome = observed_outcome if isinstance(observed_outcome, str) else "failed"
    _, terminal_error = record_release_event(
        root,
        operation,
        run_id,
        "completed" if outcome == "completed" else "failed",
        started,
        outcome,
    )
    result.update(run_id=run_id, project_root=str(root))
    errors = [error for error in (start_error, terminal_error) if error is not None]
    if errors:
        result["recording_error"] = "; ".join(errors)
    return result
