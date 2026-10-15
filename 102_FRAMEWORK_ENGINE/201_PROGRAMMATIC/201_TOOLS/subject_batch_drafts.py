"""Temporary edit-draft markers; canonical Atom identity grammar stays unchanged."""

from __future__ import annotations

from pathlib import Path
from typing import Any, Mapping

import yaml
from yaml.nodes import MappingNode, ScalarNode

import atom_operations as operations
from atom_subject_patch import (
    _apply_replacements,
    _raw_frontmatter,
    _replace_frontmatter,
    _Replacement,
    _Span,
    _yaml_scalar,
)
from connector_bindings import FileSource


def subject_batch_draft_path(root: Path, target: Mapping[str, Any]) -> Path:
    current: Path = root / target["path"]
    role = next(
        parent for parent in current.parents if operations.ROLE_DIRECTORY.fullmatch(parent.name)
    )
    name = current.name.replace(target["atom_id"], target["atom_id"] + "@draft", 1)
    return role / "draft" / name


def _scalars(raw: bytes) -> tuple[str, str, dict[str, ScalarNode]]:
    text = raw.decode("utf-8")
    frontmatter, _ = _raw_frontmatter(operations, text)
    document = yaml.compose(frontmatter, Loader=yaml.SafeLoader)
    if not isinstance(document, MappingNode):
        raise ValueError("Subject edit-draft requires one frontmatter mapping")
    scalars = {}
    for key, value in document.value:
        if key.value in {"atom_id", "status", "updated_at"}:
            if key.value in scalars or not isinstance(value, ScalarNode):
                raise ValueError("Subject edit-draft marker fields must be unique scalars")
            scalars[key.value] = value
    if set(scalars) != {"atom_id", "status", "updated_at"}:
        raise ValueError("Subject edit-draft marker fields are incomplete")
    return text, frontmatter, scalars


def _replace_scalars(raw: bytes, replacements: Mapping[str, str]) -> bytes:
    text, frontmatter, scalars = _scalars(raw)
    changes = [
        _Replacement(_Span(scalars[key].start_mark.index, scalars[key].end_mark.index), value)
        for key, value in replacements.items()
    ]
    changed = _apply_replacements(frontmatter, changes)
    return _replace_frontmatter(text, frontmatter, changed).encode("utf-8")


def make_subject_edit_draft(canonical_raw: bytes, canonical_id: str) -> bytes:
    return _replace_scalars(
        canonical_raw,
        {"atom_id": _yaml_scalar(canonical_id + "@draft"), "status": _yaml_scalar("Draft")},
    )


def read_reviewed_draft(root: Path, item: Mapping[str, Any]) -> bytes:
    pin = item["draft"]
    expected = subject_batch_draft_path(root, item["target"]).relative_to(root).as_posix()
    if pin["path"] != expected:
        raise ValueError("Subject edit-draft must use its exact target-derived draft path")
    raw = FileSource(root, Path(pin["path"]), pin["digest"]).read_bytes()
    _, _, scalars = _scalars(raw)
    if (
        scalars["atom_id"].value != item["target"]["atom_id"] + "@draft"
        or scalars["status"].value != "Draft"
    ):
        raise ValueError("Subject edit-draft temporary identity or Draft status differs")
    return raw


def require_reviewed_draft_candidate(
    root: Path, item: Mapping[str, Any], canonical_raw: bytes
) -> None:
    if "draft" not in item:
        return
    raw = read_reviewed_draft(root, item)
    _, canonical_frontmatter, scalars = _scalars(canonical_raw)
    replacements = {
        key: canonical_frontmatter[node.start_mark.index : node.end_mark.index]
        for key, node in scalars.items()
    }
    if _replace_scalars(raw, replacements) != canonical_raw:
        raise ValueError(
            "Reviewed edit-draft differs from the exact Subjects-only canonical candidate"
        )


def require_batch_reviewed_draft(root: Path, canonical_raw: bytes) -> None:
    from subject_batch_authorization import _ACTIVE

    state = _ACTIVE.get()
    if state is None or state.root != root or state.ordinal < 0:
        raise ValueError("Reviewed edit-draft requires its admitted batch target")
    require_reviewed_draft_candidate(root, state.packet["atoms"][state.ordinal], canonical_raw)
