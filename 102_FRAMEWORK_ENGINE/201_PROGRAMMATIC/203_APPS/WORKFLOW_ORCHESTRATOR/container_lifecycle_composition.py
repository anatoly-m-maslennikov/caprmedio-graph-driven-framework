"""Inline composition of source-sealed container lifecycle Runs.

The coordinator identity is only a durable progress/aggregate carrier.  Each
member is frozen and dispatched through the ordinary selected execution
boundary, so the coordinator never becomes an O127 Run itself.
"""

from __future__ import annotations

from collections.abc import Mapping
from copy import deepcopy
import hashlib
import json
from pathlib import Path
import re
from typing import Any, TYPE_CHECKING

if TYPE_CHECKING:
    from selected_execution import SelectedExecution


class ContainerLifecycleCompositionError(RuntimeError):
    """A sealed container cannot be safely composed into member Runs."""


def _canonical(value: object) -> bytes:
    return json.dumps(value, ensure_ascii=False, allow_nan=False,
                      sort_keys=True, separators=(",", ":")).encode("utf-8")


def _seal_contained_status_changes(root: Path, parameters: Mapping[str, Any], admission: Mapping[str, Any]) -> object:
    from container_lifecycle_admission import seal_contained_status_changes

    return seal_contained_status_changes(root, parameters, admission)


def _context(frozen: Mapping[str, Any]) -> tuple[str, dict[str, Any], Mapping[str, Any]]:
    request = frozen.get("request")
    if (not isinstance(request, Mapping) or not isinstance(request.get("run_id"), str)
            or re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_-]{0,127}", request["run_id"]) is None):
        raise ContainerLifecycleCompositionError("frozen coordinator request is invalid")
    execution = request.get("execution")
    if not isinstance(execution, Mapping) or not isinstance(execution.get("proposal_receipt"), Mapping):
        raise ContainerLifecycleCompositionError("frozen coordinator execution is invalid")
    source = execution["proposal_receipt"].get("source_freshness")
    observed = source.get("observed") if isinstance(source, Mapping) else None
    if not isinstance(observed, Mapping) or not isinstance(observed.get("container_lifecycle"), Mapping):
        raise ContainerLifecycleCompositionError("root container lifecycle seal is missing")
    return request["run_id"], dict(execution), observed["container_lifecycle"]


def _rows(seal: Mapping[str, Any]) -> list[dict[str, Any]]:
    descendants = seal.get("descendants")
    parent = seal.get("parent")
    if not isinstance(descendants, list) or not isinstance(parent, Mapping):
        raise ContainerLifecycleCompositionError("container lifecycle seal is malformed")
    rows = [*descendants, {"target": parent.get("prior"),
                           "status": parent.get("requested_status"),
                           "admission": dict(parent)}]
    for row in rows:
        if not isinstance(row, Mapping) or not isinstance(row.get("target"), Mapping):
            raise ContainerLifecycleCompositionError("container lifecycle member is malformed")
        target = row["target"]
        if not all(isinstance(target.get(key), (str, int)) and target.get(key) != ""
                   for key in ("atom_id", "path", "version")):
            raise ContainerLifecycleCompositionError("container lifecycle member identity is invalid")
        digest = target.get("digest", target.get("sha256"))
        if not isinstance(digest, str) or re.fullmatch(r"[0-9a-f]{64}", digest) is None:
            raise ContainerLifecycleCompositionError("container lifecycle member digest is invalid")
        if not isinstance(row.get("status"), str) or not row["status"]:
            raise ContainerLifecycleCompositionError("container lifecycle member status is invalid")
        if not isinstance(row.get("admission"), Mapping):
            raise ContainerLifecycleCompositionError("container lifecycle member admission is missing")
    return [dict(row) for row in rows]


def _member_id(coordinator_id: str, ordinal: int, atom_id: str) -> str:
    suffix = hashlib.sha256(f"{coordinator_id}:{ordinal}:{atom_id}".encode()).hexdigest()[:24]
    return f"container-member-{ordinal:04d}-{suffix}"


def _member_execution(root: Mapping[str, Any], row: Mapping[str, Any], run_id: str,
                      graph: Mapping[str, Any]) -> dict[str, Any]:
    inventory_target = row["target"]
    admission = row["admission"]
    prior = admission.get("prior") if isinstance(admission, Mapping) else None
    digest = inventory_target.get("digest", inventory_target.get("sha256"))
    if (not isinstance(prior, Mapping) or prior.get("atom_id") != inventory_target.get("atom_id")
            or prior.get("path") != inventory_target.get("path") or prior.get("version") != inventory_target.get("version")
            or prior.get("digest", prior.get("sha256")) != digest
            or prior.get("content_role") != inventory_target.get("content_role")
            or ("atom_type" in inventory_target and prior.get("type") != inventory_target.get("atom_type"))
            or admission.get("requested_status") != row.get("status")):
        raise ContainerLifecycleCompositionError("member sealed identity or status differs from admission")
    target = dict(prior)
    execution = deepcopy(dict(root))
    execution["request_id"] = f"{run_id}-request"
    parameters = deepcopy(dict(execution.get("parameters", {})))
    parameters["target"] = target
    parameters["status"] = row["status"]
    execution["parameters"] = parameters
    from selected_execution import build_requested_runs
    from workflow_run_support import _canonical_digest

    execution["parameters_digest"] = _canonical_digest(parameters)
    execution["target_frontier"] = [str(target["path"])]
    execution["target_frontier_digest"] = _canonical_digest(execution["target_frontier"])
    execution["effects"] = [{"type": "change_atom_status", "target": str(target["path"]),
                              "status": row["status"]}]
    execution["effects_digest"] = _canonical_digest(execution["effects"])
    execution["requested_runs"] = build_requested_runs(graph, run_id)
    # Freeze needs the ordinary one-Atom admission.  The complete preview
    # receipt and exact child authorization are rebound from the real tracker
    # observation immediately before the final freeze.
    execution["proposal_receipt"] = {
        "source_freshness": {"observed": {"lifecycle_admission": dict(admission)}},
    }
    execution["proposal_receipt_digest"] = "0" * 64
    return execution


def _digest(value: object) -> str:
    return hashlib.sha256(_canonical(value)).hexdigest()


def _preview_request(execution: Mapping[str, Any]) -> dict[str, Any]:
    preview = {key: value for key, value in execution.items() if key not in {
        "proposal_receipt", "proposal_receipt_digest", "assigned_action_id",
        "operator_authorization", "requested_runs",
    }}
    preview["mode"] = "preview"
    return preview


def _bind_preview(execution: dict[str, Any], prepared: Mapping[str, Any]) -> None:
    receipt = prepared.get("proposal_receipt")
    digest = prepared.get("proposal_receipt_digest")
    if not isinstance(receipt, Mapping) or not isinstance(digest, str):
        raise ContainerLifecycleCompositionError("member preview receipt is invalid")
    execution["proposal_receipt"] = dict(receipt)
    execution["proposal_receipt_digest"] = digest
    auth = deepcopy(dict(execution.get("operator_authorization", {})))
    auth.update({
        "request_id": execution["request_id"],
        "operation_route": execution["operation_route"],
        "proposal_receipt_digest": digest,
        "parameters_digest": execution["parameters_digest"],
        "target_frontier_digest": execution["target_frontier_digest"],
        "effects_digest": execution["effects_digest"],
        "definition_manifest": execution["definition_manifest"],
        "source_freshness": execution["source_freshness"],
    })
    execution["operator_authorization"] = auth


def _preview_with_tracker(selected: Any, frozen: Mapping[str, Any], execution: Mapping[str, Any]) -> tuple[dict[str, Any], Any]:
    from workflow_run_support import _canonical_digest, _proposal, _validate_common

    preview = _preview_request(execution)
    parsed = _validate_common(preview)
    tracker = selected._shared_tracker(frozen)
    observation = tracker._observe(parsed)
    if (not isinstance(observation, Mapping) or observation.get("selected") is not True
            or observation.get("current") is not True):
        raise ContainerLifecycleCompositionError("member ordinary observer refused currentness")
    observed = observation.get("observed")
    expected = execution.get("proposal_receipt", {}).get("source_freshness", {}).get("observed", {})
    expected_admission = expected.get("lifecycle_admission") if isinstance(expected, Mapping) else None
    if not isinstance(observed, Mapping) or observed.get("lifecycle_admission") != expected_admission:
        raise ContainerLifecycleCompositionError("member lifecycle admission differs from sealed member admission")
    if "container_lifecycle" in observed:
        raise ContainerLifecycleCompositionError("member ordinary observation widened to container scope")
    proposal = _proposal(parsed, observation)
    proposal_digest = _canonical_digest(proposal)
    prepared = tracker.run_selected_operation(preview)
    if (not isinstance(prepared, Mapping) or prepared.get("disposition") != "preview"
            or prepared.get("proposal_receipt") != proposal
            or prepared.get("proposal_receipt_digest") != proposal_digest):
        raise ContainerLifecycleCompositionError("member preview is not current")
    return dict(prepared), tracker


def _validate_root(selected: Any, frozen: Mapping[str, Any], execution: Mapping[str, Any],
                   root_seal: Mapping[str, Any]) -> None:
    from workflow_run_support import _canonical_digest, _proposal, _validate_common

    parsed = _validate_common(_preview_request(execution))
    tracker = selected._shared_tracker(frozen)
    observation = tracker._observe(parsed)
    if (not isinstance(observation, Mapping) or observation.get("selected") is not True
            or observation.get("current") is not True):
        raise ContainerLifecycleCompositionError("root ordinary observer refused currentness")
    raw_observed = observation.get("observed")
    if not isinstance(raw_observed, Mapping):
        raise ContainerLifecycleCompositionError("root ordinary observation is missing")
    observed = dict(raw_observed)
    current_seal = observed.get("container_lifecycle")
    if current_seal is not None and _canonical(current_seal) != _canonical(root_seal):
        raise ContainerLifecycleCompositionError("ordinary observer container seal differs from root seal")
    observed["container_lifecycle"] = dict(root_seal)
    proposal = _proposal(parsed, {"selected": observation["selected"], "current": observation["current"],
                                  "observed": observed})
    digest = _canonical_digest(proposal)
    receipt = execution.get("proposal_receipt")
    if receipt != proposal or execution.get("proposal_receipt_digest") != digest:
        raise ContainerLifecycleCompositionError("root preview receipt is stale")
    execute = _validate_common(execution)
    tracker._validate_execute(execute, proposal, digest)


def _admit_member(selected: Any, frozen: Mapping[str, Any], execution: Mapping[str, Any]) -> None:
    prepared, tracker = _preview_with_tracker(selected, frozen, execution)
    proposal = prepared["proposal_receipt"]
    proposal_digest = prepared["proposal_receipt_digest"]
    if execution.get("proposal_receipt") != proposal or execution.get("proposal_receipt_digest") != proposal_digest:
        raise ContainerLifecycleCompositionError("member frozen receipt differs from fresh preview")
    from workflow_run_support import _validate_common
    execute = _validate_common(execution)
    tracker._validate_execute(execute, proposal, proposal_digest)


def _terminal(result: object, run_id: str) -> tuple[str, list[str], bool, str | None]:
    if not isinstance(result, Mapping) or not isinstance(result.get("terminal_runs"), list):
        raise ContainerLifecycleCompositionError("member terminal evidence is unavailable")
    matches = [row for row in result["terminal_runs"]
               if isinstance(row, Mapping) and row.get("run_id") == run_id]
    if len(matches) != 1:
        raise ContainerLifecycleCompositionError("member terminal evidence is ambiguous")
    row = matches[0]
    outcome = row.get("outcome")
    effects = row.get("effect_refs", [])
    if not isinstance(effects, list) or any(not isinstance(item, str) or not item for item in effects):
        raise ContainerLifecycleCompositionError("member terminal effects are invalid")
    if row.get("disposition") != "terminal":
        return "interrupted_pending", list(effects), False, str(row["run_id"])
    if not isinstance(outcome, str) or not outcome:
        raise ContainerLifecycleCompositionError("member terminal outcome is invalid")
    if outcome == "no_op" and effects:
        raise ContainerLifecycleCompositionError("member no_op evidence carries effects")
    return outcome, list(effects), True, str(row["run_id"])


def _aggregate(coordinator_id: str, member_rows: list[dict[str, Any]], completed: list[str],
               failed: Mapping[str, Any] | None, untouched: list[str], effects: list[str],
               outcome: str, disposition: str) -> dict[str, Any]:
    return {
        "schema": "container-lifecycle/v1",
        "coordinator_id": coordinator_id,
        "parent_requested_run_id": member_rows[-1].get("requested_run_id") if member_rows else None,
        "parent_run_id": member_rows[-1].get("actual_run_id") if member_rows else None,
        "original_requested_root_run_started": False,
        "members": member_rows,
        "completed": completed,
        "failed": dict(failed) if failed is not None else None,
        "untouched": untouched,
        "effect_refs": list(dict.fromkeys(effects)),
        "outcome": outcome,
        "disposition": disposition,
    }


def _prepare_member(selected: Any, graph: Mapping[str, Any], execution: dict[str, Any]) -> dict[str, Any]:
    run_id = execution["requested_runs"][0]["requested_run_id"]
    admission = execution["proposal_receipt"]["source_freshness"]["observed"]["lifecycle_admission"]
    provisional = {"request": {"operation": "enqueue_selected", "run_id": run_id, "execution": execution},
                   "graph": graph, "lifecycle_admission": admission}
    prepared, _tracker = _preview_with_tracker(selected, provisional, execution)
    _bind_preview(execution, prepared)
    frozen = selected.freeze({"operation": "enqueue_selected", "run_id": run_id, "execution": execution})
    _admit_member(selected, frozen, execution)
    return frozen


def _actual_workflow_id(selected: Any, execution: Mapping[str, Any], requested_id: str,
                        result: Mapping[str, Any]) -> str | None:
    run_ids = result.get("run_ids")
    terminal_runs = result.get("terminal_runs")
    workflows = [item for item in execution.get("requested_runs", [])
                 if isinstance(item, Mapping) and item.get("kind") == "workflow"]
    if (len(workflows) != 1 or workflows[0].get("requested_run_id") != requested_id
            or not isinstance(workflows[0].get("definition"), Mapping)
            or not isinstance(terminal_runs, list) or not isinstance(run_ids, list)):
        return None
    terminal_ids = {row.get("run_id") for row in terminal_runs if isinstance(row, Mapping)}
    # Canonical selected execution starts this Workflow first; Session-owned
    # terminal evidence remains valid even when Journal recording is incomplete.
    if requested_id in terminal_ids and run_ids.count(requested_id) == 1:
        return requested_id
    if requested_id in run_ids:
        return None
    definition = workflows[0]["definition"]
    try:
        import work_journal
        records = work_journal.read_records(selected.root)
    except (ImportError, OSError, RuntimeError, ValueError, TypeError):
        return None
    matches = {
        run.get("run_id") for event in records
        if isinstance(event, Mapping)
        and isinstance(event.get("llm_session"), Mapping)
        and event["llm_session"].get("uuid") == execution.get("request_id")
        and isinstance(event.get("run"), Mapping)
        and event["run"].get("kind") == "workflow"
        and event["run"].get("definition") == definition
        and isinstance((run := event["run"]).get("run_id"), str)
        and run.get("run_id") in run_ids
        and run.get("run_id") in terminal_ids
    }
    return next(iter(matches)) if len(matches) == 1 else None


def _dispatch_member(selected: Any, frozen: Mapping[str, Any], execution: Mapping[str, Any], run_id: str) -> tuple[str, list[str], bool, str | None]:
    workflow = next((item for item in execution.get("requested_runs", [])
                     if isinstance(item, Mapping) and item.get("kind") == "workflow"), None)
    if (not isinstance(workflow, Mapping) or workflow.get("requested_run_id") != run_id
            or not isinstance(workflow.get("definition"), Mapping)):
        raise ContainerLifecycleCompositionError("member Workflow binding is missing")
    result = selected.dispatch(frozen)
    if not isinstance(result, Mapping):
        return "interrupted_pending", [], False, None
    actual_id = _actual_workflow_id(selected, execution, run_id, result)
    if actual_id is None:
        return "interrupted_pending", [], False, None
    try:
        return _terminal(result, actual_id)
    except ContainerLifecycleCompositionError:
        return "interrupted_pending", [], False, None


def _root_frozen_digest(selected: Any, root_dir: Path, frozen: Mapping[str, Any]) -> str:
    saved_path = root_dir / "selected_request.json"
    if not saved_path.is_file():
        raise ContainerLifecycleCompositionError("root frozen request carrier is missing")
    saved = selected._read(saved_path)
    if _canonical(saved) != _canonical(frozen):
        raise ContainerLifecycleCompositionError("root frozen request differs from durable selected request")
    return _digest(frozen)


def _verify_member_request(selected: Any, frozen: Mapping[str, Any]) -> str:
    request = frozen.get("request")
    if not isinstance(request, Mapping) or not isinstance(request.get("run_id"), str):
        raise ContainerLifecycleCompositionError("member frozen request is invalid")
    path = selected.run_directory(request["run_id"]) / "selected_request.json"
    if not path.is_file() or _canonical(selected._read(path)) != _canonical(frozen):
        raise ContainerLifecycleCompositionError("member frozen request carrier differs from dispatch request")
    return _digest(frozen)


def _verify_retained_member(selected: Any, progress: Mapping[str, Any]) -> None:
    run_id = progress.get("current")
    digest = progress.get("member_request_digest")
    if not isinstance(run_id, str) or not isinstance(digest, str):
        raise ContainerLifecycleCompositionError("retained member frontier is incomplete")
    path = selected.run_directory(run_id) / "selected_request.json"
    if not path.is_file() or _digest(selected._read(path)) != digest:
        raise ContainerLifecycleCompositionError("retained member request differs from progress")


def _refresh_member_scope(selected: Any, graph: Mapping[str, Any], root_execution: Mapping[str, Any],
                          root_admission: Mapping[str, Any], root_seal: Mapping[str, Any],
                          member: Mapping[str, Any]) -> None:
    current_admission = selected._validate_lifecycle_admission(
        graph, root_execution, expected_admission=root_admission,
    )
    current = _seal_contained_status_changes(selected.root, root_execution["parameters"], current_admission)
    parent = root_seal.get("parent", {})
    parent_prior = parent.get("prior", {}) if isinstance(parent, Mapping) else {}
    parent_id = parent_prior.get("atom_id") if isinstance(parent_prior, Mapping) else None
    original = {row["target"]["atom_id"]: row for row in root_seal.get("descendants", [])
                if isinstance(row, Mapping) and isinstance(row.get("target"), Mapping)}
    if current is None:
        if member.get("atom_id") != parent_id:
            raise ContainerLifecycleCompositionError("pending member disappeared from current containment scope")
        return
    current_rows = _rows(current)
    current_descendants = {row["target"]["atom_id"]: row for row in current_rows[:-1]}
    if not set(current_descendants) <= set(original):
        raise ContainerLifecycleCompositionError("current containment scope contains an unsealed descendant")
    atom_id = member.get("atom_id")
    if atom_id == parent_id:
        if _canonical(current.get("parent")) != _canonical(parent):
            raise ContainerLifecycleCompositionError("parent source admission drifted before dispatch")
    elif atom_id not in current_descendants or _canonical(current_descendants[atom_id]) != _canonical(original[atom_id]):
        raise ContainerLifecycleCompositionError("pending member source admission drifted before dispatch")


def _member_step(selected: Any, graph: Mapping[str, Any], row: Mapping[str, Any], member: dict[str, Any],
                 root_execution: Mapping[str, Any], root_admission: Mapping[str, Any], root_seal: Mapping[str, Any],
                 coordinator_id: str, root_digest: str,
                 member_rows: list[dict[str, Any]], completed: list[str], effects: list[str],
                 index: int, progress_path: Path, accepted_path: Path) -> tuple[dict[str, Any] | None, list[str]]:
    run_id = member["requested_run_id"]
    try:
        _refresh_member_scope(selected, graph, root_execution, root_admission, root_seal, member)
        execution = _member_execution(root_execution, row, run_id, graph)
        member_frozen = _prepare_member(selected, graph, execution)
        member["request_digest"] = _verify_member_request(selected, member_frozen)
    except Exception as error:
        failed = {"atom_id": member["atom_id"], "requested_run_id": run_id, "reason": type(error).__name__}
        member["outcome"] = "blocked"
        aggregate = _aggregate(coordinator_id=coordinator_id, member_rows=member_rows, completed=completed,
                               failed=failed, untouched=[item["requested_run_id"] for item in member_rows[index + 1:]],
                               effects=effects, outcome="partial" if effects else "blocked",
                               disposition="terminal" if effects else "blocked")
        selected._write(accepted_path, {"result": aggregate})
        return aggregate, []
    progress = _aggregate(coordinator_id, member_rows, completed, None,
                           [item["requested_run_id"] for item in member_rows[index + 1:]], effects,
                           "interrupted_pending", "started")
    selected._write(progress_path, {"state": "dispatching", "root_frozen_digest": root_digest,
                                    "member_request_digest": member["request_digest"],
                                    "aggregate": progress, "current": run_id})
    outcome, member_effects, terminal, actual_run_id = _dispatch_member(selected, member_frozen, execution, run_id)
    member["outcome"] = outcome
    member["effect_refs"] = member_effects
    member["actual_run_id"] = actual_run_id
    if outcome in {"completed", "no_op"}:
        return None, member_effects
    aggregate_outcome = outcome
    aggregate_disposition = "started"
    if effects or member_effects or outcome == "partial":
        aggregate_outcome = "partial"
        aggregate_disposition = "terminal" if terminal else "started"
    elif terminal and outcome in {"failed", "cancelled", "canceled"}:
        aggregate_disposition = "terminal"
    failed = {"atom_id": member["atom_id"], "requested_run_id": run_id,
              "actual_run_id": member.get("actual_run_id"), "outcome": outcome}
    aggregate = _aggregate(coordinator_id, member_rows, completed, failed,
                           [item["requested_run_id"] for item in member_rows[index + 1:]],
                           [*effects, *member_effects], aggregate_outcome, aggregate_disposition)
    selected._write(accepted_path, {"result": aggregate})
    return aggregate, []


def _admit_composition_root(selected: Any, frozen: Mapping[str, Any], execution: Mapping[str, Any],
                            root_seal: Mapping[str, Any]) -> tuple[Mapping[str, Any], list[dict[str, Any]], Mapping[str, Any]]:
    graph = selected._revalidate(frozen)
    workflow = graph.get("workflow") if isinstance(graph, Mapping) else None
    if (execution.get("operation_route") != "change_atom_status"
            or not isinstance(graph, Mapping)
            or graph.get("route") != "change_atom_status"
            or not isinstance(workflow, Mapping)
            or workflow.get("atom_id") != "CA-O-127"):
        raise ContainerLifecycleCompositionError("container composition requires the admitted CA-O-127 status route")
    admission = selected._validate_lifecycle_admission(
        graph, execution, expected_admission=frozen.get("lifecycle_admission"),
    )
    if not isinstance(admission, Mapping):
        raise ContainerLifecycleCompositionError("root lifecycle admission is unavailable")
    fresh_seal = _seal_contained_status_changes(selected.root, execution["parameters"], admission)
    if not isinstance(fresh_seal, Mapping) or _canonical(fresh_seal) != _canonical(root_seal):
        raise ContainerLifecycleCompositionError("root container lifecycle seal changed")
    _validate_root(selected, frozen, execution, root_seal)
    return graph, _rows(fresh_seal), admission


def coordinate_container_lifecycle(selected: "SelectedExecution", frozen: Mapping[str, Any]) -> dict[str, Any]:
    """Freeze and dispatch a sealed descendant-first lifecycle composition inline."""
    coordinator_id, root_execution, root_seal = _context(frozen)
    root_dir = selected.run_directory(coordinator_id)
    accepted_path = root_dir / "accepted.json"
    progress_path = root_dir / "container_lifecycle_progress.json"
    root_digest = _root_frozen_digest(selected, root_dir, frozen)
    if accepted_path.exists():
        retained = selected._read(accepted_path)
        if not isinstance(retained, Mapping) or not isinstance(retained.get("result"), Mapping):
            raise ContainerLifecycleCompositionError("accepted aggregate is invalid")
        return dict(retained["result"])
    if progress_path.exists():
        retained = selected._read(progress_path)
        if retained.get("root_frozen_digest") != root_digest:
            raise ContainerLifecycleCompositionError("progress is bound to a different root request")
        if retained.get("state") == "dispatching":
            _verify_retained_member(selected, retained)
            return retained["aggregate"]
    graph, rows, root_admission = _admit_composition_root(selected, frozen, root_execution, root_seal)
    member_rows: list[dict[str, Any]] = []
    for index, row in enumerate(rows):
        target = row["target"]
        member_rows.append({"atom_id": target["atom_id"], "requested_run_id": _member_id(coordinator_id, index, target["atom_id"]),
                            "requested_status": row["status"], "version": target["version"],
                            "sha256": target.get("digest", target.get("sha256")), "request_digest": None,
                            "outcome": "untouched", "effect_refs": [], "actual_run_id": None})
    completed: list[str] = []
    effects: list[str] = []
    for index, row in enumerate(rows):
        stopped, member_effects = _member_step(
            selected, graph, row, member_rows[index], root_execution, root_admission, root_seal,
            coordinator_id, root_digest, member_rows, completed, effects, index,
            progress_path, accepted_path,
        )
        if stopped is not None:
            return stopped
        completed.append(member_rows[index]["actual_run_id"])
        effects.extend(member_effects)
    aggregate = _aggregate(coordinator_id, member_rows, completed, None, [], effects, "completed", "terminal")
    selected._write(accepted_path, {"result": aggregate})
    selected._write(progress_path, {"state": "completed", "root_frozen_digest": root_digest, "aggregate": aggregate})
    return aggregate
