"""Ordered batch coordination through the existing Session and native writer."""

from __future__ import annotations

from pathlib import Path
from typing import Any, Mapping

from atom_subject_apply import subject_update_action
from atom_subject_patch import prepare_subject_intent
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
    runner: Any, session: Any, child: Mapping[str, Any], result: Mapping[str, Any]
) -> Any:
    from selected_lifecycle_journal import record_lifecycle_change

    if result["outcome"] != "applied":
        return None
    before = result["history"]["prior"]
    after, raw = runner._lifecycle_result_facts(result["observed"])
    runner._lifecycle_result_facts(result["history"]["prior_revision"])
    author, local_date, timezone, occurred_at = runner._replacement_journal_context(session)
    binding = batch_definition_binding(child["definition"])
    if binding["path"] == result["observed"]["path"]:
        binding["sha256"] = result["observed"]["digest"]
    pin = {
        "action_id": "CA-O-030",
        "structural_scope": runner._lifecycle_structural_scope(binding),
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
        runner.root,
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
    runner: Any, frozen: Mapping[str, Any], session: Any, item: Mapping[str, Any], ordinal: int
) -> dict[str, Any]:
    run_id = frozen["request"]["run_id"]
    identities = subject_batch_run_ids(run_id, ordinal)
    actual = [session.start_run(identity) for identity in identities]
    parameters = _parameters(runner.root, item)
    result = subject_update_action(
        runner.root,
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
        **finish_subject_draft_promotion(runner.root, item, result),
    }
    result_path = runner.run_directory(run_id) / f"subject-{ordinal}.json"
    try:
        row["lifecycle_recording"] = _record_change(runner, session, actual[-1], result)
    except Exception as error:
        row["recording_error"] = type(error).__name__
    return _finish_target(runner, session, actual, result_path, row)


def _finish_target(
    runner: Any, session: Any, actual: list[dict[str, Any]], result_path: Path, row: dict[str, Any]
) -> dict[str, Any]:
    effects = row["effect_refs"]
    runner._write(result_path, row)
    reference = result_path.relative_to(runner.root).as_posix()
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
    runner._write(result_path, row)
    return row


def execute_subject_batch(runner: Any, frozen: Mapping[str, Any], session: Any) -> dict[str, Any]:
    """Run only untouched targets in this first dispatch; any uncertain attempt stops."""
    run_id = frozen["request"]["run_id"]
    path = runner.run_directory(run_id) / PROGRESS
    if path.exists():
        raise ValueError(
            "Subject batch already attempted; inspect durable results without automatic replay"
        )
    with bind_subject_batch(runner, frozen, session) as state:
        workflow = session.start_run(run_id)
        progress: dict[str, Any] = {
            "state": "running",
            "count": len(state.packet["atoms"]),
            "atoms": [],
            "completed": 0,
            "automatic_retry": False,
        }
        runner._write(path, progress)
        for ordinal, item in enumerate(state.packet["atoms"], 1):
            state.ordinal = ordinal - 1
            progress["in_flight"] = {"ordinal": ordinal, "target": item["target"]}
            runner._write(path, progress)
            try:
                row = _execute_target(runner, frozen, session, item, ordinal)
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
            runner._write(path, progress)
        return _finish_batch(runner, session, workflow, path, progress)


def _finish_batch(
    runner: Any, session: Any, workflow: Mapping[str, Any], path: Path, progress: dict[str, Any]
) -> dict[str, Any]:
    complete = progress["completed"] == progress["count"]
    progress.update(
        state="completed" if complete else "stopped",
        remaining=progress["count"] - len(progress["atoms"]),
    )
    effects = sorted({effect for row in progress["atoms"] for effect in row.get("effect_refs", [])})
    runner._write(path, progress)
    outcome = "completed" if complete else "interrupted_pending"
    receipt = session.finish_run(
        workflow["run_id"],
        outcome=outcome,
        result_ref=path.relative_to(runner.root).as_posix(),
        effect_refs=effects,
    )
    if receipt.get("recording_error"):
        progress["recording_error"] = receipt["recording_error"]
        runner._write(path, progress)
    return progress
