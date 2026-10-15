"""Bounded edit-draft staging in the existing selected runner's durable storage."""

from __future__ import annotations

import hashlib
from pathlib import Path
import sys
from typing import Any, Mapping

import atom_operations as operations
from artifact_metadata import current_timestamp
from atom_subject_patch import (
    _assert_original_identity_unique,
    _capture_identity_layout,
    materialize_subject_intent,
    prepare_subject_intent,
)
from atom_subject_stage import _check_candidate, _write_candidate
from connector_bindings import FileSource
from subject_batch import load_subject_batch
from subject_batch_authorization import _ACTIVE, BatchAdmission
from subject_batch_drafts import make_subject_edit_draft, subject_batch_draft_path


def _runner(root: Path) -> Any:
    app = Path(__file__).resolve().parents[1] / "203_APPS/WORKFLOW_ORCHESTRATOR"
    if str(app) not in sys.path:
        sys.path.insert(0, str(app))
    from selected_execution import SelectedExecution

    return SelectedExecution(root)


def _stage_target(root: Path, state: BatchAdmission, item: Mapping[str, Any]) -> dict[str, Any]:
    state.validation_scope = None
    prepared = prepare_subject_intent(
        root, item["target"], item["subject_patches"], subject_profile="approved"
    )
    candidate = materialize_subject_intent(root, prepared, current_timestamp(root))
    raw = make_subject_edit_draft(candidate["carrier_bytes"], item["target"]["atom_id"])
    path = subject_batch_draft_path(root, item["target"])
    import os

    parent = operations._raw_revision_parent(root, path, create=True)
    os.close(parent)
    fingerprint = _write_candidate(root, path, raw)
    reopened, observed = operations.read_raw_atom_revision(root, path)
    _check_candidate(raw, fingerprint, reopened, observed)
    return {
        **item,
        "draft": {
            "path": path.relative_to(root).as_posix(),
            "digest": hashlib.sha256(raw).hexdigest(),
        },
    }


def stage_subject_batch(
    root: Path, parameters: Mapping[str, Any], *, limit: int = 10
) -> dict[str, Any]:
    """Continue only untouched draft targets; uncertain writes stop without replay."""
    if type(limit) is not int or not 1 <= limit <= 10:
        raise ValueError("Subject batch staging limit must be between 1 and 10")
    root = Path(root).resolve()
    packet = load_subject_batch(root, parameters)
    if any("draft" in item for item in packet["atoms"]):
        raise ValueError("Subject staging input must be the original map-only packet")
    runner = _runner(root)
    run_id = "subject-stage-" + parameters["subject_batch"]["digest"]
    folder = runner.run_directory(run_id)
    path = folder / "subject_batch_staging.json"
    progress = (
        runner._read(path)
        if path.exists()
        else {
            "operation": "stage_subject_batch",
            "state": "staging",
            "stage_run_id": run_id,
            "count": len(packet["atoms"]),
            "completed": 0,
            "atoms": [],
            "reviewed_packet": None,
            "automatic_retry": False,
            "remaining": len(packet["atoms"]),
        }
    )
    for item in progress["atoms"]:
        pin = item["draft"]
        FileSource(root, Path(pin["path"]), pin["digest"]).revalidate()
    if "in_flight" in progress or progress["state"] == "stopped":
        return _compact({**progress, "state": "stopped", "inspection_required": True})
    if progress["state"] == "staged":
        pin = progress["reviewed_packet"]
        FileSource(root, Path(pin["path"]), pin["digest"]).revalidate()
        return _compact(progress)
    _assert_original_identity_unique(
        operations,
        root,
        {item["target"]["atom_id"] for item in packet["atoms"]},
        _capture_identity_layout(operations, root),
    )
    state = BatchAdmission(root, packet, None, {})
    token = _ACTIVE.set(state)
    try:
        _stage_chunk(runner, path, progress, state, limit)
    finally:
        _ACTIVE.reset(token)
    load_subject_batch(root, parameters)
    return _seal_staged_packet(runner, packet, progress, folder, path)


def _seal_staged_packet(
    runner: Any, packet: Mapping[str, Any], progress: dict[str, Any], folder: Path, path: Path
) -> dict[str, Any]:
    root = runner.root
    if progress["completed"] == progress["count"]:
        reviewed_path = folder / "reviewed_subject_packet.json"
        reviewed = {**packet, "atoms": progress["atoms"]}
        raw = operations.canonical_json(reviewed).encode("utf-8")
        if reviewed_path.exists():
            FileSource(
                root, reviewed_path.relative_to(root), hashlib.sha256(raw).hexdigest()
            ).revalidate()
        else:
            fingerprint = _write_candidate(root, reviewed_path, raw)
            reopened, observed = operations.read_raw_atom_revision(root, reviewed_path)
            _check_candidate(raw, fingerprint, reopened, observed)
        progress.update(
            state="staged",
            reviewed_packet={
                "path": reviewed_path.relative_to(root).as_posix(),
                "digest": hashlib.sha256(raw).hexdigest(),
            },
        )
        load_subject_batch(root, {"subject_batch": progress["reviewed_packet"]})
    progress["remaining"] = progress["count"] - progress["completed"]
    runner._write(path, progress)
    return _compact(progress)


def _stage_chunk(
    runner: Any, path: Path, progress: dict[str, Any], state: BatchAdmission, limit: int
) -> None:
    start = progress["completed"]
    for ordinal in range(start, min(start + limit, progress["count"])):
        item = state.packet["atoms"][ordinal]
        state.ordinal = ordinal
        progress["in_flight"] = {"ordinal": ordinal + 1, "target": item["target"]}
        runner._write(path, progress)
        try:
            staged = _stage_target(runner.root, state, item)
        except Exception as error:
            progress.update(state="stopped", diagnostic=str(error), inspection_required=True)
            runner._write(path, progress)
            return
        progress["atoms"].append(staged)
        progress["completed"] += 1
        progress.pop("in_flight")
        runner._write(path, progress)


def _compact(progress: Mapping[str, Any]) -> dict[str, Any]:
    return {key: value for key, value in progress.items() if key != "atoms"}
