"""Closed, ordered Subjects-only packet and selected Run planning."""

from __future__ import annotations

import hashlib
import json
import subprocess
from pathlib import Path
from typing import Any, Literal, Mapping

from pydantic import BaseModel, ConfigDict, Field

from ATOM_UPDATE.atom_update import TargetDescriptor
from connector_bindings import FileSource
from selected_execution_run_plan import lifecycle_native_binding, support_definition
from VALIDATE_ATOMS.validate_atoms_workers.contracts import _unique_keys


class _Closed(BaseModel):
    model_config = ConfigDict(extra="forbid", strict=True)


class _Pin(_Closed):
    path: str = Field(min_length=1)
    digest: str = Field(pattern=r"^[0-9a-f]{64}$")


class _Request(_Closed):
    subject_batch: _Pin


class _ScalarPatch(_Closed):
    field: Literal["governs", "depends_on"]
    old: str = Field(min_length=1)
    new: str = Field(min_length=1)


class _SetPatch(_Closed):
    field: Literal["depends_on"]
    operation: Literal["replace_set"]
    old: list[str]
    new: list[str]


class _Item(_Closed):
    target: TargetDescriptor
    subject_patches: list[_ScalarPatch | _SetPatch] = Field(min_length=1)
    draft: _Pin | None = None


class _Packet(_Closed):
    schema_version: Literal[1]
    subject_profile: Literal["approved"]
    git_checkpoint: str = Field(pattern=r"^(?:[0-9a-f]{40}|[0-9a-f]{64})$")
    atoms: list[_Item] = Field(min_length=1)


def load_subject_batch(root: Path, parameters: Mapping[str, Any]) -> dict[str, Any]:
    """Reopen an exact packet; no candidate staging or publication occurs."""
    request = _Request.model_validate(parameters)
    source = FileSource(
        Path(root).resolve(), Path(request.subject_batch.path), request.subject_batch.digest
    )
    value = json.loads(source.read_bytes(), object_pairs_hook=_unique_keys)
    if not isinstance(value, dict) or type(value.get("schema_version")) is not int:
        raise ValueError("Subject batch schema version must be an integer")
    packet = _Packet.model_validate(value).model_dump()
    for item in packet["atoms"]:
        if item["draft"] is None:
            item.pop("draft")
    drafted = ["draft" in item for item in packet["atoms"]]
    if any(drafted) and not all(drafted):
        raise ValueError("A reviewed Subject packet must bind all drafts or none")
    paths, identities = set(), set()
    for item in packet["atoms"]:
        target = item["target"]
        from atom_subject_apply import _parameters

        _parameters(
            {
                "target": target,
                "subject_patches": item["subject_patches"],
                "subject_intent_sha256": "0" * 64,
                "subject_profile": "approved",
            }
        )
        relative = target["path"]
        raw = FileSource(source.root, Path(relative), target["digest"]).read_bytes()
        if relative in paths or target["atom_id"] in identities:
            raise ValueError("Subject batch targets must be distinct current Atoms")
        paths.add(relative)
        identities.add(target["atom_id"])
        if "draft" in item:
            from subject_batch_drafts import read_reviewed_draft

            read_reviewed_draft(source.root, item)
        if hashlib.sha256(raw).hexdigest() != target["digest"]:
            raise ValueError("Subject batch target differs from its exact original")
    source.revalidate()
    return packet


def require_git_checkpoint(root: Path, packet: Mapping[str, Any]) -> None:
    """Require one recoverable committed pre-state for the complete packet."""
    commit = packet["git_checkpoint"]
    try:
        kind = subprocess.run(
            ["git", "cat-file", "-t", commit],
            cwd=root,
            check=True,
            capture_output=True,
            timeout=15,
            text=True,
        )
        if kind.stdout.strip() != "commit":
            raise ValueError("Subject batch checkpoint must identify a Git commit")
        paths = [item["target"]["path"] for item in packet["atoms"]]
        tracked = subprocess.run(
            ["git", "ls-tree", "-r", "--name-only", "-z", commit, "--", *paths],
            cwd=root,
            check=True,
            capture_output=True,
            timeout=30,
            text=True,
        )
        if set(tracked.stdout.rstrip("\0").split("\0")) != set(paths):
            raise ValueError("Subject batch checkpoint omits a selected original")
        subprocess.run(
            ["git", "diff", "--quiet", commit, "--", *paths],
            cwd=root,
            check=True,
            capture_output=True,
            timeout=30,
        )
    except subprocess.SubprocessError as error:
        raise ValueError(
            "Subject batch checkpoint does not preserve the exact committed pre-state"
        ) from error


def build_subject_batch_requested_runs(
    graph: Mapping[str, Any], run_id: str, count: int
) -> list[dict[str, Any]]:
    """Plan actual mapping-review branch Runs, without fictitious assessments."""
    steps = [step for step in graph["steps"] if step["atom_id"] == "CA-O-129"]
    if len(steps) != 1 or count < 1:
        raise ValueError("Subject batch requires the existing O129 lifecycle Step")
    actions = [action for action in steps[0]["actions"] if action["atom_id"] == "CA-O-128"]
    if len(actions) != 1:
        raise ValueError("Subject batch requires the existing O128 lifecycle Action")
    native = lifecycle_native_binding(graph, "CA-O-030")
    rows = [
        {
            "requested_run_id": run_id,
            "kind": "workflow",
            "definition": support_definition(graph["workflow"]),
        }
    ]
    for ordinal in range(1, count + 1):
        step, action, child = subject_batch_run_ids(run_id, ordinal)
        for identity, kind, binding, parent in (
            (step, "step", steps[0], run_id),
            (action, "action", actions[0], step),
            (child, "action", native, action),
        ):
            rows.append(
                {
                    "requested_run_id": identity,
                    "kind": kind,
                    "definition": support_definition(binding),
                    "parent_requested_run_id": parent,
                }
            )
    return rows


def subject_batch_run_ids(run_id: str, ordinal: int) -> tuple[str, str, str]:
    step = f"{run_id}:subject:{ordinal}"
    action = f"{step}:action:1"
    return step, action, f"{action}:native:CA-O-030"


def subject_batch_progress_summary(
    progress: Mapping[str, Any], *, result_ref: str
) -> dict[str, Any]:
    """Expose aggregate progress; full per-Atom facts remain in the existing result carrier."""
    return {
        "state": progress["state"],
        "count": progress["count"],
        "completed": progress["completed"],
        "remaining": progress.get("remaining", progress["count"] - progress["completed"]),
        "automatic_retry": False,
        "result_ref": result_ref,
    }
