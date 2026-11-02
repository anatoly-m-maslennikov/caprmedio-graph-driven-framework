# implementation of:
# Method: CA-M-410
"""Capture carrier bound to one retained Integrated frontier."""

from __future__ import annotations

from collections.abc import Mapping
import json
from pathlib import Path
from typing import Any, cast

from selected_evidence_io import atomic_write, bounded_bytes, run_directory
from selected_execution_contracts import SelectedExecutionError
from selected_integrated_frontier_records import MAX_RECORD_BYTES, canonical, digest


CAPTURE_NAME = "integrated_capture.json"
_FIELDS = frozenset({"frontier_digest", "capture", "capture_digest"})


def _path(root: Path, run_id: str, frontier: Mapping[str, Any]) -> Path:
    continuation = frontier.get("continuation_id")
    if not isinstance(continuation, str) or len(continuation) != 64:
        raise SelectedExecutionError("Integrated frontier continuation is invalid")
    return run_directory(root, run_id) / f"{CAPTURE_NAME.removesuffix('.json')}-{continuation}.json"


def _checked(root: Path, frontier: Mapping[str, Any], capture: Mapping[str, Any]) -> dict[str, Any]:
    packet = capture.get("packet")
    definitions = capture.get("definitions")
    if not isinstance(packet, Mapping) or not isinstance(definitions, Mapping):
        raise SelectedExecutionError("Integrated capture is incomplete")
    run_binding = capture.get("run_binding")
    if (
        not isinstance(run_binding, Mapping)
        or set(run_binding)
        != {
            "workflow_run_id",
            "step_run_id",
            "action_run_id",
            "requested_action_id",
        }
        or any(not isinstance(value, str) or not value for value in run_binding.values())
    ):
        raise SelectedExecutionError("Integrated capture Run binding is invalid")
    project = frontier.get("project")
    step = frontier.get("step")
    action = frontier.get("action")
    if not all(isinstance(value, Mapping) for value in (project, step, action)):
        raise SelectedExecutionError("Integrated frontier is incomplete")
    step_binding = cast(Mapping[str, Any], step)
    action_binding = cast(Mapping[str, Any], action)
    trusted_sources = {
        "profile": definitions.get("trusted_workflow_binding"),
        "method_projection": definitions.get("trusted_method_projection"),
        "methods": definitions.get("trusted_methods"),
    }
    if (
        capture.get("selected_project_root") != root.as_posix()
        or capture.get("step_id") != step_binding.get("id")
        or capture.get("action_id") != action_binding.get("id")
        or digest(packet) != frontier.get("packet_digest")
        or digest(trusted_sources) != frontier.get("source_digest")
    ):
        raise SelectedExecutionError("Integrated capture differs from its frontier")
    return dict(capture)


def save_capture(
    root: Path, run_id: str, frontier: Mapping[str, Any], capture: Mapping[str, Any]
) -> None:
    """Persist a pending capture while its :class:`IntegratedFrontierStore` is held."""
    checked = _checked(root, frontier, capture)
    value = {
        "frontier_digest": digest(frontier),
        "capture": checked,
        "capture_digest": digest(checked),
    }
    if len(canonical(value)) > MAX_RECORD_BYTES:
        raise SelectedExecutionError("Integrated capture exceeds its bounded carrier size")
    path = _path(root, run_id, frontier)
    if path.is_symlink() or (path.exists() and not path.is_file()):
        raise SelectedExecutionError("Integrated capture destination is unsafe")
    if path.exists():
        retained = load_capture(root, run_id, frontier)
        if retained != checked:
            raise SelectedExecutionError("Integrated capture conflicts with retained frontier")
        return
    atomic_write(path, value)


def load_capture(root: Path, run_id: str, frontier: Mapping[str, Any]) -> dict[str, Any]:
    """Load only a capture whose packet and source pins bind the frontier."""
    path = _path(root, run_id, frontier)
    if not path.exists():
        raise SelectedExecutionError("pending Integrated frontier has no retained capture")
    try:
        value = json.loads(bounded_bytes(path, MAX_RECORD_BYTES))
    except (SelectedExecutionError, UnicodeDecodeError, ValueError) as error:
        raise SelectedExecutionError("retained Integrated capture is invalid") from error
    if not isinstance(value, dict):
        raise SelectedExecutionError("retained Integrated capture is invalid")
    if set(value) != _FIELDS or value.get("frontier_digest") != digest(frontier):
        raise SelectedExecutionError("retained Integrated capture differs from its frontier")
    capture = value.get("capture")
    if not isinstance(capture, Mapping) or value.get("capture_digest") != digest(capture):
        raise SelectedExecutionError("retained Integrated capture is invalid")
    return _checked(root, frontier, cast(Mapping[str, Any], capture))
