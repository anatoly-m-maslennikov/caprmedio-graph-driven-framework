"""Pure coherence checks for the selected batch's declared Artifact effects."""

from __future__ import annotations

from pathlib import Path
import json
from typing import Any, Mapping

import atom_operations as operations
from connector_bindings import FileSource


def _pinned_atom(root: Path, target: Mapping[str, Any]) -> operations.Atom:
    path = root / target["path"]
    raw = FileSource(root, Path(target["path"]), target["digest"]).read_bytes()
    frontmatter, content = operations.split_frontmatter(raw.decode("utf-8"))
    control = operations.control_root(root)
    role = operations._role_directory(path.resolve(), control)
    if role is None:
        raise ValueError("Subject target has no content-role history location")
    return operations.Atom(
        path.resolve(),
        target["path"],
        target["filename"],
        target["atom_id"],
        target["lifecycle"],
        role,
        frontmatter,
        content,
    )


def _changed(item: Mapping[str, Any]) -> bool:
    for patch in item["subject_patches"]:
        if patch.get("operation") == "replace_set":
            if set(patch["old"]) != set(patch["new"]):
                return True
        elif patch["old"] != patch["new"]:
            return True
    return False


def subject_batch_frontier(packet: Mapping[str, Any], *, root: Path) -> tuple[list[str], list[dict[str, Any]]]:
    """Derive exact paths and revision effects without preparing or validating Carriers."""
    root = Path(root).resolve()
    frontier, effects = [], []
    for item in packet["atoms"]:
        target = item["target"]
        frontier.append(target["path"])
        if _changed(item):
            archive = operations.preserved_revision_destination(root, _pinned_atom(root, target))
            archive = archive.relative_to(root).as_posix()
            frontier.append(archive)
            effects.extend(
                [
                    {
                        "type": "subjectUpdate",
                        "path": target["path"],
                        "atom_id": target["atom_id"],
                        "before_version": target["version"],
                        "version": target["version"] + 1,
                    },
                    {
                        "type": "predecessorArchive",
                        "atom_id": target["atom_id"],
                        "version": target["version"],
                        "path": archive,
                        "sha256": target["digest"],
                        "lifecycle": "archived",
                    },
                ]
            )
        if "draft" in item:
            frontier.append(item["draft"]["path"])
            effects.append(
                {
                    "type": "draftRemoval",
                    "path": item["draft"]["path"],
                    "atom_id": target["atom_id"],
                    "sha256": item["draft"]["digest"],
                }
            )
    return frontier, effects


def require_subject_batch_frontier(
    packet: Mapping[str, Any], execution: Mapping[str, Any], *, root: Path
) -> None:
    frontier, expected = subject_batch_frontier(packet, root=root)
    if execution.get("target_frontier") != frontier:
        raise ValueError("Subject batch declared frontier differs from its exact ordered packet")
    declared = execution.get("effects")
    if not isinstance(declared, list) or len(declared) != len(expected):
        raise ValueError("Subject batch declared effects differ from its exact ordered packet")
    for effect, wanted in zip(declared, expected, strict=True):
        actual = dict(effect)
        if json.dumps(actual, sort_keys=True) != json.dumps(wanted, sort_keys=True):
            raise ValueError(
                "Subject batch declared effect differs from its exact packet target or revision"
            )
