"""Currentness-checked publication of the next Integrated frontier."""

# implementation of:
# Requirement: CA-R-1524
# Method: CA-M-405

from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path
from typing import Any

from selected_integrated_dispatch import frontier_for_capture
from selected_integrated_dispatch_capture import load_capture, save_capture
from selected_integrated_dispatch_handler import actual_run_ids
from selected_integrated_dispatch_pending import revalidate_pending
from selected_integrated_frontier import IntegratedFrontierStore
from selected_integrated_session import restore_checkpoint


def pending_response(
    root: Path,
    run_id: str,
    frozen: Mapping[str, Any],
    tracker: Any,
    frontier: Mapping[str, Any],
) -> dict[str, Any]:
    """Return the exact current prompt with checkpoint-derived Run identities."""
    capture = load_capture(root, run_id, frontier)
    return {
        "disposition": "started",
        "status": "pending_action",
        "continuation_id": frontier["continuation_id"],
        "capture": capture,
        **actual_run_ids(restore_checkpoint(root, frozen, tracker), run_id, capture),
    }


def publish_pending(
    store: IntegratedFrontierStore,
    frozen: Mapping[str, Any],
    tracker: Any,
    session: Any,
    profile: Mapping[str, Any],
    method_projection: object | None,
    methods: object | None,
    pending: Mapping[str, Any],
) -> dict[str, Any]:
    """Validate and durably publish one later prompt before exposing it."""
    request = frozen["request"]
    run_id = request["run_id"]
    frontier = frontier_for_capture(store.root, run_id, frozen, profile, pending)
    revalidate_pending(store.root, frozen, profile, method_projection, methods, frontier, pending)
    session.save()
    save_capture(store.root, run_id, frontier, pending)
    store.save(frontier)
    return pending_response(store.root, run_id, frozen, tracker, frontier)
