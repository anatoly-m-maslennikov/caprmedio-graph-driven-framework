"""Temporary edit-draft markers; canonical Atom identity grammar stays unchanged."""

from __future__ import annotations

import hashlib
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


def _marker_context(root: Path, canonical_id: str) -> tuple[str, str]:
    parts = canonical_id.split("-", 2)
    if len(parts) != 3 or not parts[0] or len(parts[1]) != 1:
        raise ValueError("Subject edit-draft target must carry one canonical Atom ID")
    return operations.project_identity_prefix(root), parts[1]


def _parse_marker(root: Path, canonical_id: str, value: str):
    project_prefix, role_letter = _marker_context(root, canonical_id)
    try:
        marker = operations.parse_draft_marker(
            value, project_prefix=project_prefix, role_letter=role_letter
        )
    except ValueError as error:
        raise ValueError("Subject edit-draft temporary identity is invalid") from error
    if marker is None or marker.canonical_id != canonical_id:
        raise ValueError("Subject edit-draft temporary identity differs from its canonical target")
    return marker


def _marker_value(root: Path, canonical_id: str, proposed_version: int | None) -> str:
    if proposed_version is None:
        value = canonical_id + "@draft"
    else:
        if type(proposed_version) is not int or proposed_version < 1:
            raise ValueError("Subject edit-draft proposed version must be a positive integer")
        value = f"{canonical_id}@{proposed_version}-draft"
    marker = _parse_marker(root, canonical_id, value)
    if proposed_version is not None and marker.proposed_version != proposed_version:
        raise ValueError("Subject edit-draft marker does not carry its proposed version")
    return marker.value


def _draft_path_for_marker(root: Path, target: Mapping[str, Any], marker_value: str) -> Path:
    current: Path = root / target["path"]
    role = next(
        parent for parent in current.parents if operations.ROLE_DIRECTORY.fullmatch(parent.name)
    )
    name = current.name.replace(target["atom_id"], marker_value, 1)
    if name == current.name:
        raise ValueError("Subject edit-draft target filename does not carry its canonical Atom ID")
    return role / "draft" / name


def _id_free_marker(root: Path, target: Mapping[str, Any]) -> str:
    project_prefix, role_letter = _marker_context(root, target["atom_id"])
    return f"{project_prefix}-{role_letter}"


def subject_batch_draft_path(
    root: Path, target: Mapping[str, Any], proposed_version: int | None = None
) -> Path:
    marker = _marker_value(root, target["atom_id"], proposed_version)
    return _draft_path_for_marker(root, target, marker)


def _filename_marker(root: Path, target: Mapping[str, Any], path: Path) -> str | None:
    current_name = (root / target["path"]).name
    canonical_id = target["atom_id"]
    if path.name == current_name.replace(canonical_id, _id_free_marker(root, target), 1):
        return None
    prefix, separator, suffix = current_name.partition(canonical_id)
    if not separator:
        raise ValueError("Subject edit-draft target filename does not carry its canonical Atom ID")
    name = path.name
    if not name.startswith(prefix) or (suffix and not name.endswith(suffix)):
        raise ValueError("Subject edit-draft filename does not preserve its target shape")
    end = len(name) - len(suffix) if suffix else len(name)
    marker = name[len(prefix):end]
    if not marker:
        raise ValueError("Subject edit-draft filename is missing its temporary identity marker")
    return marker


def _scalars(raw: bytes) -> tuple[str, str, dict[str, ScalarNode]]:
    text = raw.decode("utf-8")
    frontmatter, _ = _raw_frontmatter(operations, text)
    document = yaml.compose(frontmatter, Loader=yaml.SafeLoader)
    if not isinstance(document, MappingNode):
        raise ValueError("Subject edit-draft requires one frontmatter mapping")
    scalars = {}
    for key, value in document.value:
        if key.value in {"atom_id", "status", "updated_at", "version"}:
            if key.value in scalars or not isinstance(value, ScalarNode):
                raise ValueError("Subject edit-draft marker fields must be unique scalars")
            scalars[key.value] = value
    if not {"status", "updated_at", "version"}.issubset(scalars):
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


def _remove_scalar(raw: bytes, name: str) -> bytes:
    text, frontmatter, scalars = _scalars(raw)
    node = scalars.get(name)
    if node is None:
        return raw
    start = frontmatter.rfind("\n", 0, node.start_mark.index) + 1
    end = frontmatter.find("\n", node.end_mark.index)
    end = len(frontmatter) if end < 0 else end + 1
    changed = frontmatter[:start] + frontmatter[end:]
    return _replace_frontmatter(text, frontmatter, changed).encode("utf-8")


def make_subject_edit_draft(
    canonical_raw: bytes,
    canonical_id: str,
    proposed_version: int | None = None,
    *,
    root: Path,
) -> bytes:
    marker = _marker_value(root, canonical_id, proposed_version)
    return _replace_scalars(
        canonical_raw,
        {"atom_id": _yaml_scalar(marker), "status": _yaml_scalar("Draft")},
    )


def _positive_version(scalars: Mapping[str, ScalarNode]) -> int:
    carried_version = scalars["version"].value
    if not carried_version.isascii() or not carried_version.isdecimal():
        raise ValueError("Subject edit-draft carried Version must be a positive integer")
    version = int(carried_version)
    if version < 1:
        raise ValueError("Subject edit-draft carried Version must be a positive integer")
    return version


def _require_qualified_marker_version(
    marker: operations.DraftMarker, scalars: Mapping[str, ScalarNode]
) -> None:
    if marker.proposed_version is None:
        return
    if _positive_version(scalars) != marker.proposed_version:
        raise ValueError("Subject edit-draft marker does not match its carried Version")


def read_reviewed_draft(root: Path, item: Mapping[str, Any]) -> bytes:
    pin = item["draft"]
    target = item["target"]
    filename_marker = _filename_marker(root, target, Path(pin["path"]))
    if filename_marker is None:
        expected_path = _draft_path_for_marker(root, target, _id_free_marker(root, target))
    else:
        marker = _parse_marker(root, target["atom_id"], filename_marker)
        expected_path = _draft_path_for_marker(root, target, marker.value)
    expected = expected_path.relative_to(root).as_posix()
    if pin["path"] != expected:
        raise ValueError("Subject edit-draft must use its exact target-derived draft path")
    raw = FileSource(root, Path(pin["path"]), pin["digest"]).read_bytes()
    _, _, scalars = _scalars(raw)
    if scalars["status"].value != "Draft":
        raise ValueError("Subject edit-draft temporary identity or Draft status differs")
    if filename_marker is None:
        if "atom_id" in scalars:
            raise ValueError("ID-free Subject edit-draft filename must omit atom_id")
    else:
        if "atom_id" not in scalars:
            raise ValueError("Marked Subject edit-draft must carry its temporary identity")
        yaml_marker = _parse_marker(root, target["atom_id"], scalars["atom_id"].value)
        marker = _parse_marker(root, target["atom_id"], filename_marker)
        if yaml_marker.value != marker.value:
            raise ValueError("Subject edit-draft temporary identity differs from its filename")
        _require_qualified_marker_version(marker, scalars)
    return raw


def require_reviewed_draft_candidate(
    root: Path, item: Mapping[str, Any], canonical_raw: bytes
) -> None:
    if "draft" not in item:
        return
    raw = read_reviewed_draft(root, item)
    _, _, draft_scalars = _scalars(raw)
    filename_marker = _filename_marker(root, item["target"], Path(item["draft"]["path"]))
    marker = (
        None
        if filename_marker is None
        else _parse_marker(root, item["target"]["atom_id"], draft_scalars["atom_id"].value)
    )
    _, canonical_frontmatter, canonical_scalars = _scalars(canonical_raw)
    draft_version = _positive_version(draft_scalars)
    candidate_version = _positive_version(canonical_scalars)
    if draft_version != candidate_version:
        raise ValueError("Subject edit-draft Version does not match the candidate version")
    if marker is not None and marker.proposed_version is not None:
        if marker.proposed_version != candidate_version:
            raise ValueError("Subject edit-draft marker does not match the candidate version")
    replacements = {
        key: canonical_frontmatter[
            canonical_scalars[key].start_mark.index : canonical_scalars[key].end_mark.index
        ]
        for key in draft_scalars
    }
    expected = canonical_raw if marker is not None else _remove_scalar(canonical_raw, "atom_id")
    if _replace_scalars(raw, replacements) != expected:
        raise ValueError(
            "Reviewed edit-draft differs from the exact Subjects-only canonical candidate"
        )


def require_batch_reviewed_draft(root: Path, canonical_raw: bytes) -> None:
    from subject_batch_authorization import _ACTIVE

    state = _ACTIVE.get()
    if state is None or state.root != root or state.ordinal < 0:
        raise ValueError("Reviewed edit-draft requires its admitted batch target")
    require_reviewed_draft_candidate(root, state.packet["atoms"][state.ordinal], canonical_raw)


def remove_promoted_subject_draft(
    root: Path, item: Mapping[str, Any], result: Mapping[str, Any]
) -> dict[str, Any]:
    """Consume only the exact pinned proposal after canonical publication succeeded."""
    carriers = [result["observed"]]
    if result["outcome"] == "applied":
        carriers.append(result["history"]["prior_revision"])
    for carrier in carriers:
        FileSource(root, Path(carrier["path"]), carrier["digest"]).revalidate()
    read_reviewed_draft(root, item)
    pin = item["draft"]
    path = root / pin["path"]
    raw, fingerprint = operations.read_raw_atom_revision(root, path)
    if hashlib.sha256(raw).hexdigest() != pin["digest"]:
        raise ValueError("Promoted Subject draft changed before conditional removal")
    operations.write_raw_atom_revision(root, path, None, expected=fingerprint, mode=fingerprint[-1])
    FileSource(root, Path(pin["path"]), None).revalidate()
    return {"state": "removed", **pin}


def finish_subject_draft_promotion(
    root: Path, item: Mapping[str, Any], result: Mapping[str, Any]
) -> dict[str, Any]:
    effects = sorted(
        {
            effect["carrier"]["path"]
            for effect in result.get("effects", [])
            if effect.get("state") in {"changed", "unknown"}
        }
    )
    completion = {"outcome": result["outcome"], "effect_refs": effects}
    if "draft" not in item or result["outcome"] not in {"applied", "no-op"}:
        return completion
    try:
        completion["draft_promotion"] = remove_promoted_subject_draft(root, item, result)
    except Exception as error:
        completion.update(
            outcome="partial",
            draft_promotion={
                "state": "unknown",
                **item["draft"],
                "diagnostic": type(error).__name__,
                "automatic_retry": False,
            },
        )
    completion["effect_refs"] = sorted({*effects, item["draft"]["path"]})
    return completion
