"""Ordered batch coordination through the existing Session and native writer."""

from __future__ import annotations

from pathlib import Path
from typing import Any, Mapping

from atom_subject_apply import subject_update_action
from atom_subject_patch import prepare_subject_intent
from selected_evidence_io import atomic_write, run_directory
from subject_batch import subject_batch_run_ids
from subject_batch_authorization import batch_definition_binding, bind_subject_batch
from subject_batch_drafts import finish_subject_draft_promotion

PROGRESS = "subject_batch_progress.json"


def _parameters(root: Path, item: Mapping[str, Any]) -> dict[str, Any]:
    prepared = prepare_subject_intent(
        root, item["target"], item["subject_patches"], subject_profile="approved"
    )
    return {
        "target": item["target"],
        "subject_patches": item["subject_patches"],
        "subject_profile": "approved",
        "subject_intent_sha256": prepared["subject_intent_sha256"],
    }


def _record_change(
    root: Path, session: Any, child: Mapping[str, Any], result: Mapping[str, Any]
) -> Any:
    from selected_lifecycle_journal import record_lifecycle_change
    from selected_lifecycle_observation import (
        journal_context,
        lifecycle_structural_scope,
        result_facts,
    )

    if result["outcome"] != "applied":
        return None
    before = result["history"]["prior"]
    after, raw = result_facts(root, result["observed"])
    result_facts(root, result["history"]["prior_revision"])
    author, local_date, timezone, occurred_at = journal_context(session)
    binding = batch_definition_binding(child["definition"])
    if binding["path"] == result["observed"]["path"]:
        binding["sha256"] = result["observed"]["digest"]
    pin = {
        "action_id": "CA-O-030",
        "structural_scope": lifecycle_structural_scope(root, binding),
        "occurred_at": occurred_at,
        "llm_session": {"app": "run-support", "uuid": session.request["request_id"]},
    }
    prior = {
        "filename": before["filename"],
        "path": before["path"],
        "version": before["version"],
        "sha256": before["digest"],
    }
    return record_lifecycle_change(
        root,
        after_facts=after,
        current_bytes=raw,
        action_pin=pin,
        run_id=child["run_id"],
        context={"author": author, "local_date": local_date, "timezone": timezone},
        action_type="UPDATE",
        native_effects={"result": {"state": "present", **after}},
        before_result=prior,
    )


def _execute_target(
    root: Path, frozen: Mapping[str, Any], session: Any, item: Mapping[str, Any], ordinal: int
) -> dict[str, Any]:
    run_id = frozen["request"]["run_id"]
    identities = subject_batch_run_ids(run_id, ordinal)
    actual = [session.start_run(identity) for identity in identities]
    parameters = _parameters(root, item)
    result = subject_update_action(
        root,
        parameters,
        execute=True,
        authorized=True,
        session=session,
        action_run_id=actual[-1]["run_id"],
    )
    row = {
        "ordinal": ordinal,
        "target": item["target"],
        "outcome": result["outcome"],
        "native_result": result,
        **finish_subject_draft_promotion(root, item, result),
    }
    result_path = run_directory(root, run_id) / f"subject-{ordinal}.json"
    try:
        row["lifecycle_recording"] = _record_change(root, session, actual[-1], result)
    except Exception as error:
        row["recording_error"] = type(error).__name__
    return _finish_target(root, session, actual, result_path, row)


def _finish_target(
    root: Path, session: Any, actual: list[dict[str, Any]], result_path: Path, row: dict[str, Any]
) -> dict[str, Any]:
    effects = row["effect_refs"]
    atomic_write(result_path, row)
    reference = result_path.relative_to(root).as_posix()
    terminal = {
        "applied": "completed",
        "no-op": "no_op",
        "failed": "failed",
        "partial": "partial",
    }.get(row["outcome"], "interrupted_pending")
    if terminal == "no_op" and effects:
        terminal = "completed"
    if effects:
        session.note_effects(actual[-1]["run_id"], result_ref=reference, effect_refs=effects)
    for record in reversed(actual):
        receipt = session.finish_run(
            record["run_id"], outcome=terminal, result_ref=reference, effect_refs=effects
        )
        if receipt.get("recording_error"):
            row["recording_error"] = receipt["recording_error"]
    atomic_write(result_path, row)
    return row


def execute_subject_batch(root: Path, frozen: Mapping[str, Any], session: Any) -> dict[str, Any]:
    """Run only untouched targets in this first dispatch; any uncertain attempt stops."""
    root = Path(root).resolve(strict=True)
    run_id = frozen["request"]["run_id"]
    path = run_directory(root, run_id) / PROGRESS
    if path.exists():
        raise ValueError(
            "Subject batch already attempted; inspect durable results without automatic replay"
        )
    with bind_subject_batch(root, frozen, session) as state:
        workflow = session.start_run(run_id)
        progress: dict[str, Any] = {
            "state": "running",
            "count": len(state.packet["atoms"]),
            "atoms": [],
            "completed": 0,
            "automatic_retry": False,
        }
        atomic_write(path, progress)
        for ordinal, item in enumerate(state.packet["atoms"], 1):
            state.ordinal = ordinal - 1
            progress["in_flight"] = {"ordinal": ordinal, "target": item["target"]}
            atomic_write(path, progress)
            try:
                row = _execute_target(root, frozen, session, item, ordinal)
            except Exception as error:
                row = {
                    "ordinal": ordinal,
                    "target": item["target"],
                    "outcome": "unknown",
                    "diagnostic": type(error).__name__,
                    "inspection_required": True,
                }
            progress["atoms"].append(row)
            progress.pop("in_flight")
            if row["outcome"] not in {"applied", "no-op"}:
                progress["state"] = "stopped"
                break
            state.completed[item["target"]["path"]] = row["native_result"]["observed"]["digest"]
            progress["completed"] += 1
            atomic_write(path, progress)
        return _finish_batch(root, session, workflow, path, progress)


def _finish_batch(
    root: Path, session: Any, workflow: Mapping[str, Any], path: Path, progress: dict[str, Any]
) -> dict[str, Any]:
    complete = progress["completed"] == progress["count"]
    progress.update(
        state="completed" if complete else "stopped",
        remaining=progress["count"] - len(progress["atoms"]),
    )
    effects = sorted({effect for row in progress["atoms"] for effect in row.get("effect_refs", [])})
    atomic_write(path, progress)
    outcome = "completed" if complete else "interrupted_pending"
    receipt = session.finish_run(
        workflow["run_id"],
        outcome=outcome,
        result_ref=path.relative_to(root).as_posix(),
        effect_refs=effects,
    )
    if receipt.get("recording_error"):
        progress["recording_error"] = receipt["recording_error"]
        atomic_write(path, progress)
    return progress
