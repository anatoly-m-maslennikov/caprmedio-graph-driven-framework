"""Shared implementation for CAPRMEDIO Markdown Atom operations."""

from __future__ import annotations

import argparse
from contextlib import contextmanager
import fcntl
import hashlib
import json
import os
import re
import stat
import sys
import threading
import tomllib
import uuid
from dataclasses import dataclass, replace
from pathlib import Path
from typing import Any, Mapping, Sequence

from project_runtime import RUNTIME_DIRECTORY, atomic_tempfile
from project_selection import bound_selection
from artifact_metadata import current_timestamp
from authoritative_status_models import StatusModelError
from VALIDATE_ATOMS.validate_atoms_workers.proposed_carrier import (
    CarrierValidationScope,
    ProposedCarrierError,
    source_context_from_project,
    validate_proposed_carrier,
)
from VALIDATE_ATOMS.validate_atoms_workers.parsing import CarrierError, parse_carrier

SCHEMA_VERSION = 1
SETTINGS_PATH = Path(".caprmedio_caprmedio/caprmedio_project_settings.toml")
DEFAULT_CONTROL_ROOT = Path(".caprmedio_caprmedio")
ROLE_DIRECTORY = re.compile(r"^0[1-9]_[a-z0-9_]+$")
CURRENT_FILENAME = re.compile(r"^[A-Za-z0-9][A-Za-z0-9_@-]*--[a-z0-9][a-z0-9_-]*\.md$")
# An order token may precede an Atom ID in a Plan carrier filename.  The
# frontmatter identifier remains canonical; a filename occurrence is a
# consistency check, not the only identity carrier.
ATOM_ID = re.compile(r"(?:^|-)(CA-[CAPRMEDO]-[0-9]+)(?=-|$)")
_IDENTITY_LOCKS = threading.local()


class ToolError(RuntimeError):
    def __init__(self, code: str, message: str, details: Mapping[str, Any] | None = None) -> None:
        self.code = code
        self.message = message
        self.details = dict(details or {})
        super().__init__(message)


@dataclass(frozen=True)
class Atom:
    path: Path
    relative: str
    filename: str
    atom_id: str | None
    lifecycle: str
    role_directory: str
    frontmatter: str
    content: str


@dataclass(frozen=True, slots=True)
class DraftMarker:
    """One validated Draft-only identity marker.

    ``canonical_id`` is only a reference carried by an existing-Atom marker;
    it never becomes ``Atom.atom_id`` while the carrier remains Draft.
    """

    value: str
    canonical_id: str | None
    proposed_version: int | None


@dataclass(frozen=True, slots=True)
class ExistingDraftPromotion:
    """One sealed same-canonical Draft promotion binding."""

    canonical_target: Atom
    marker: DraftMarker
    proposed_version: int
    no_op: bool


def parse_draft_marker(
    value: str | None,
    *,
    project_prefix: str,
    role_letter: str,
) -> DraftMarker | None:
    """Parse one optional Draft atom_id marker without reading or writing state."""

    if value is None:
        return None
    if (not isinstance(value, str) or not isinstance(project_prefix, str)
            or not isinstance(role_letter, str) or not project_prefix
            or re.fullmatch(r"[A-Za-z0-9]+", project_prefix) is None
            or re.fullmatch(r"[A-Z]", role_letter) is None):
        raise ValueError("Draft marker context is invalid")
    role_prefix = f"{project_prefix}-{role_letter}"
    if value == f"{role_prefix}-draft":
        return DraftMarker(value, None, None)
    match = re.fullmatch(rf"({re.escape(role_prefix)}-[0-9]+)@(?:(\d+)-)?draft", value)
    if match is None:
        raise ValueError("Draft atom_id must use an admitted Draft marker")
    version = int(match.group(2)) if match.group(2) is not None else None
    if version is not None and version < 1:
        raise ValueError("Draft proposed Version must be positive")
    return DraftMarker(value, match.group(1), version)


def canonical_json(value: object) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False)


def resolve_repository(value: str | Path) -> Path:
    selection = bound_selection()
    if selection is not None:
        candidate = Path(value).expanduser().resolve()
        if not _inside(candidate, selection.root):
            raise ToolError("outside-project", "path is outside the selected Project")
        return selection.root
    candidate = Path(value).expanduser().resolve()
    for root in (candidate, *candidate.parents):
        if (root / ".git").exists():
            return root
    raise ToolError("repository-not-found", f"cannot resolve Git repository from {candidate}")


def _inside(path: Path, parent: Path) -> bool:
    try:
        path.relative_to(parent)
        return True
    except ValueError:
        return False


def control_root(root: Path) -> Path:
    """Return the configured current Project carrier root, never a legacy root."""

    root = root.resolve()
    selection = bound_selection(root)
    if selection is not None:
        return selection.control_root
    try:
        settings = tomllib.loads((root / SETTINGS_PATH).read_text(encoding="utf-8"))
    except (OSError, tomllib.TOMLDecodeError) as error:
        raise ToolError("project-settings-unavailable", f"cannot read current Project Settings: {error}") from error
    configured = settings.get("paths", {}).get("control_root")
    if not isinstance(configured, str) or not configured:
        raise ToolError("project-settings-invalid", "paths.control_root must name the Project carrier root")
    candidate = Path(configured)
    if candidate.is_absolute() or ".." in candidate.parts or candidate != DEFAULT_CONTROL_ROOT:
        raise ToolError("project-settings-invalid", "paths.control_root must be .caprmedio_caprmedio")
    return (root / candidate).resolve()


def project_identity_prefix(root: Path) -> str:
    """Read the authoritative Project-owned Atom prefix from Project Settings."""

    try:
        selection = bound_selection(root)
        settings = selection.settings if selection is not None else tomllib.loads((root.resolve() / SETTINGS_PATH).read_text(encoding="utf-8"))
    except (OSError, tomllib.TOMLDecodeError) as error:
        raise ToolError("project-settings-unavailable", "cannot read Project Settings identity") from error
    prefix = settings.get("artifacts", {}).get("identity", {}).get("project_prefix")
    if not isinstance(prefix, str) or re.fullmatch(r"[A-Za-z0-9]+", prefix) is None:
        raise ToolError("project-settings-invalid", "artifacts.identity.project_prefix is invalid")
    return prefix


def safe_path(root: Path, value: str, *, must_exist: bool = False) -> Path:
    root = root.resolve()
    if not value or "\x00" in value:
        raise ToolError("path-invalid", "path must be a non-empty string")
    candidate = Path(value).expanduser()
    path = candidate.resolve() if candidate.is_absolute() else (root / candidate).resolve()
    control = control_root(root)
    if not _inside(path, control):
        raise ToolError("outside-control-root", f"path is outside {control.relative_to(root)}: {value}")
    if must_exist and not path.exists():
        raise ToolError("path-not-found", f"path does not exist: {value}")
    return path


def split_frontmatter(text: str) -> tuple[str, str]:
    normalized = text.replace("\r\n", "\n").replace("\r", "\n")
    if not normalized.startswith("---\n"):
        raise ToolError("atom-frontmatter-missing", "Markdown Atom must begin with YAML frontmatter")
    end = normalized.find("\n---\n", 4)
    if end < 0:
        raise ToolError("atom-frontmatter-invalid", "Markdown Atom frontmatter is not closed")
    return normalized[4:end], normalized[end + 5 :]


def _role_directory(path: Path, control: Path) -> str | None:
    relative = path.relative_to(control)
    for part in reversed(relative.parts[:-1]):
        if ROLE_DIRECTORY.fullmatch(part):
            return part
    return None


def _lifecycle(path: Path, control: Path) -> str:
    parts = {part.lower() for part in path.relative_to(control).parts}
    if "archive" in parts or "archived" in parts:
        return "archived"
    if "draft" in parts or "drafts" in parts:
        return "draft"
    if "done" in parts:
        return "done"
    if "resolved" in parts:
        return "resolved"
    if "canceled" in parts or "cancelled" in parts:
        return "canceled"
    return "active"


def atom_from_path(root: Path, path: Path) -> Atom:
    root = root.resolve()
    return _atom_from_path(root, path, control_root(root))


def _atom_from_path(root: Path, path: Path, control: Path) -> Atom:
    """Parse against the validated control-root snapshot for one operation."""
    path = path.resolve()
    if not _inside(path, control) or path.suffix.lower() != ".md" or not path.is_file():
        raise ToolError("not-markdown-atom", f"not a CAPRMEDIO Markdown Atom carrier: {path}")
    if "_projection" in path.relative_to(control).parts:
        raise ToolError("not-markdown-atom", f"Projection Carrier is not an authoritative Atom: {path}")
    role = _role_directory(path, control)
    if role is None and path.parent != control:
        raise ToolError("not-markdown-atom", f"carrier is not placed in a CAPRMEDIO content-role directory: {path}")
    frontmatter, content = split_frontmatter(path.read_text(encoding="utf-8"))
    if re.search(r"(?m)^projection:\s*(?:$|\{)", frontmatter):
        raise ToolError("not-markdown-atom", f"projected Atom view is not an authoritative Atom: {path}")
    lifecycle = _lifecycle(path, control)
    match = ATOM_ID.search(path.name)
    declared = frontmatter_scalar(frontmatter, "atom_id")
    if lifecycle == "draft":
        _draft_marker_identity(root, path, frontmatter)
        atom_id = None
    else:
        if declared is None:
            raise ToolError("atom-frontmatter-id-required", f"active Atom must declare atom_id in frontmatter: {path}")
        if re.fullmatch(r"CA-[CAPRMEDO]-[0-9]+", declared) is None:
            raise ToolError("atom-frontmatter-invalid", f"Atom has an invalid atom_id value: {path}")
        if match is not None and declared != match.group(1):
            raise ToolError("atom-frontmatter-id-mismatch", f"filename and frontmatter atom_id differ: {path}")
        atom_id = declared
    return Atom(path, path.relative_to(root).as_posix(), path.name, atom_id,
                lifecycle, role or "control-root", frontmatter, content)


def scan_atoms(root: Path, *, under: str | None = None, lifecycle: str = "all") -> list[Atom]:
    root = root.resolve()
    control = control_root(root)
    base = safe_path(root, under, must_exist=True) if under else control
    candidates = [base] if base.is_file() else sorted(base.rglob("*.md"), key=lambda p: p.as_posix())
    atoms: list[Atom] = []
    for path in candidates:
        try:
            atom = _atom_from_path(root, path, control)
        except (ToolError, UnicodeDecodeError, OSError):
            continue
        if lifecycle == "all" or atom.lifecycle == lifecycle:
            atoms.append(atom)
    return sorted(atoms, key=lambda atom: atom.relative)


def atom_id_has_preserved_history_evidence(root: Path, atom_id: str) -> bool:
    """Return whether any retained carrier reserves ``atom_id``.

    This is deliberately more conservative than ``scan_atoms``.  A malformed
    or otherwise unparsable retained Markdown file cannot establish Atom
    properties, but a matching historical identity is enough to make reuse
    unsafe.  Callers must block rather than treating parse failure as evidence
    that allocation is free.
    """

    root = root.resolve()
    control = control_root(root)
    for candidate in control.rglob("*.md"):
        if candidate.is_symlink():
            continue
        match = ATOM_ID.search(candidate.name)
        if match is not None and match.group(1) == atom_id:
            return True
        try:
            frontmatter, _ = split_frontmatter(candidate.read_text(encoding="utf-8"))
            if frontmatter_scalar(frontmatter, "atom_id") == atom_id:
                return True
        except (OSError, UnicodeDecodeError, ToolError):
            # The file cannot be trusted as an Atom, but its filename has
            # already been checked above.  Do not infer any further property.
            continue
    return False


def resolve_selector(root: Path, selector: str, atoms: Sequence[Atom] | None = None) -> Atom:
    root = root.resolve()
    if "/" in selector or (selector.endswith(".md") and Path(selector).is_absolute()):
        try:
            return atom_from_path(root, safe_path(root, selector, must_exist=True))
        except ToolError as error:
            if error.code not in {"path-not-found", "not-markdown-atom"}:
                raise
    pool = list(atoms) if atoms is not None else scan_atoms(root)
    normalized = Path(selector).name
    matches = [atom for atom in pool if selector == atom.relative or normalized == atom.filename
               or normalized == Path(atom.filename).stem or selector == atom.atom_id]
    if re.fullmatch(r"CA-[CAPRMEDO]-[0-9]+", selector):
        for lifecycle in ("active", "resolved", "done", "canceled", "archived"):
            current_matches = [atom for atom in matches if atom.lifecycle == lifecycle]
            if current_matches:
                matches = current_matches
                break
    unique = {atom.relative: atom for atom in matches}
    if not unique:
        raise ToolError("atom-not-found", f"no CAPRMEDIO Markdown Atom matches selector: {selector}")
    if len(unique) != 1:
        raise ToolError("atom-selector-ambiguous", f"selector matches more than one Atom: {selector}",
                        {"matches": sorted(unique)})
    return next(iter(unique.values()))


def resolve_selectors(root: Path, selectors: Sequence[str]) -> list[Atom]:
    root = root.resolve()
    if not selectors:
        raise ToolError("atom-selector-required", "at least one Atom selector is required")
    pool = scan_atoms(root)
    resolved = [resolve_selector(root, selector, pool) for selector in selectors]
    paths = [atom.relative for atom in resolved]
    duplicates = sorted({path for path in paths if paths.count(path) > 1})
    if duplicates:
        raise ToolError("duplicate-target", "the same Atom was selected more than once", {"paths": duplicates})
    return resolved


def metadata(atom: Atom) -> dict[str, Any]:
    return {"atom_id": atom.atom_id, "path": atom.relative, "filename": atom.filename,
            "lifecycle": atom.lifecycle, "content_role_directory": atom.role_directory,
            "frontmatter": atom.frontmatter}


def present(atom: Atom, view: str) -> dict[str, Any]:
    result: dict[str, Any] = {}
    if view in {"metadata", "both"}:
        result["metadata"] = metadata(atom)
    if view in {"content", "both"}:
        result["content"] = atom.content
    return result


def _load_payload(path: str) -> dict[str, Any]:
    try:
        text = sys.stdin.read() if path == "-" else Path(path).read_text(encoding="utf-8")
        value = json.loads(text)
    except (OSError, json.JSONDecodeError) as error:
        raise ToolError("input-invalid", f"cannot read JSON input: {error}") from error
    if not isinstance(value, dict):
        raise ToolError("input-invalid", "JSON input root must be an object")
    return value


def _items(payload: Mapping[str, Any]) -> list[dict[str, Any]]:
    raw = payload.get("atoms")
    if not isinstance(raw, list) or not raw or any(not isinstance(item, dict) for item in raw):
        raise ToolError("input-invalid", "input must contain a non-empty atoms array of objects")
    return [dict(item) for item in raw]


def _normalize_frontmatter(value: Any) -> str:
    if not isinstance(value, str):
        raise ToolError("input-invalid", "frontmatter must be a YAML string without delimiters")
    normalized = value.replace("\r\n", "\n").replace("\r", "\n").strip("\n")
    if normalized.startswith("---") or "\n---" in normalized:
        raise ToolError("input-invalid", "frontmatter must not include YAML delimiters")
    return normalized


def _revision(root: Path, frontmatter: str, *, creating: bool) -> str:
    lines = frontmatter.splitlines()
    index = next((i for i, line in enumerate(lines) if re.fullmatch(r"version:\s*[0-9]+\s*", line)), None)
    current = int(lines[index].split(":", 1)[1]) if index is not None else 0
    marker = frontmatter_scalar(frontmatter, "atom_id")
    existing_draft = marker is not None and re.fullmatch(
        r"[A-Za-z0-9]+-[A-Z]-[0-9]+@(?:[0-9]+-)?draft", marker
    ) is not None
    line = f"version: {current if creating and existing_draft and current > 0 else 1 if creating else current + 1}"
    if index is None:
        lines.append(line)
    else:
        lines[index] = line
    stamp = current_timestamp(root)
    index = next((i for i, line in enumerate(lines) if line.startswith("updated_at:")), None)
    line = f'updated_at: "{stamp}"'
    if index is None:
        lines.append(line)
    else:
        lines[index] = line
    return "\n".join(lines)


def _with_atom_id(frontmatter: str, atom_id: str | None, *, allow_draft_marker: bool = False) -> str:
    """Make the current carrier identity explicit without accepting a conflict."""

    declared = frontmatter_scalar(frontmatter, "atom_id")
    if atom_id is None:
        if declared is not None and not allow_draft_marker:
            raise ToolError("draft-has-stable-id", "a draft cannot declare atom_id")
        return frontmatter
    if declared is not None:
        if declared != atom_id:
            raise ToolError("atom-frontmatter-id-mismatch", "frontmatter atom_id must equal the filename Atom ID")
        return frontmatter
    return (frontmatter + "\n" if frontmatter else "") + f"atom_id: {atom_id}"


def frontmatter_scalar(frontmatter: str, name: str) -> str | None:
    """Read one simple top-level scalar without reserializing the carrier."""

    matches = re.findall(rf"(?m)^{re.escape(name)}:\s*(.*?)\s*$", frontmatter)
    if len(matches) > 1:
        raise ToolError("atom-frontmatter-invalid", f"Atom has duplicate {name} values")
    if not matches:
        return None
    value = matches[0].strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
        value = value[1:-1]
    return value


_DRAFT_MARKER_VALUE = re.compile(
    r"[A-Za-z0-9]+-[A-Z]-(?:draft|[0-9]+@(?:[0-9]+-)?draft)"
)
_DRAFT_MARKER_PARTS = re.compile(
    r"(?P<prefix>[A-Za-z0-9]+)-(?P<role>[A-Z])-(?:draft|[0-9]+@(?:[0-9]+-)?draft)"
)


def _draft_marker_from_filename(filename: str) -> str | None:
    """Return the identity-segment Draft marker, if this filename carries one."""

    head = Path(filename).stem.split("--", 1)[0]
    head = re.sub(r"^[0-9]+-", "", head)
    if _DRAFT_MARKER_VALUE.fullmatch(head):
        return head
    if "@" in head and re.search(r"draft$", head):
        raise ValueError("filename contains a malformed Draft marker")
    return None


def _draft_marker_metadata(frontmatter: str, role: str) -> None:
    """Reject Draft markers whose carrier metadata contradicts their role/status."""

    content_role = frontmatter_scalar(frontmatter, "content_role")
    if content_role is not None and (not content_role or content_role[0].upper() != role):
        raise ToolError("draft-marker-invalid", "Draft marker role differs from Content Role")
    status = frontmatter_scalar(frontmatter, "status")
    if status is not None and status.casefold() != "draft":
        raise ToolError("draft-marker-status-invalid", "Draft marker is permitted only with Draft status")


def _draft_marker_identity(root: Path, path: Path, frontmatter: str) -> DraftMarker | None:
    """Validate one Draft marker against its exact filename and project role."""
    try:
        filename_value = _draft_marker_from_filename(path.name)
    except ValueError as error:
        raise ToolError("draft-marker-invalid", str(error)) from error
    declared = frontmatter_scalar(frontmatter, "atom_id")
    if filename_value is None and declared is None:
        return None
    candidate = filename_value or declared
    assert candidate is not None
    parts = _DRAFT_MARKER_PARTS.fullmatch(candidate)
    if parts is None:
        raise ToolError("draft-has-stable-id", "a Draft cannot declare a canonical Atom ID")
    if filename_value != declared:
        raise ToolError("atom-frontmatter-id-mismatch", "Draft filename and frontmatter marker differ")
    configured_prefix = project_identity_prefix(root)
    if parts.group("prefix") != configured_prefix:
        raise ToolError("draft-marker-invalid", "Draft marker does not use the configured Project prefix")
    try:
        marker = parse_draft_marker(candidate, project_prefix=configured_prefix, role_letter=parts.group("role"))
    except ValueError as error:
        raise ToolError("draft-marker-invalid", str(error)) from error
    _draft_marker_metadata(frontmatter, parts.group("role"))
    return marker


def _without_promotion_metadata(frontmatter: str) -> str:
    return re.sub(r"(?m)^(?:atom_id|status|version|updated_at):[^\n]*(?:\n|$)", "", frontmatter).rstrip("\n")


def _draft_summary(content: str) -> str:
    match = re.search(r"(?ms)^# Summary\s*\n+(.+?)(?=^#|\Z)", content)
    if match is None:
        raise ToolError("summary-missing", "# Summary must carry a non-empty value")
    return match.group(1).strip()


def _bind_existing_draft_marker(
    root: Path, draft: Atom, canonical_target: Atom, proposed_version: int | None,
) -> tuple[DraftMarker, int]:
    if draft.lifecycle != "draft" or draft.atom_id is not None:
        raise ToolError("atom-not-draft", "existing promotion requires one identity-less Draft carrier")
    marker = _draft_marker_identity(root, draft.path, draft.frontmatter)
    if marker is None or marker.canonical_id is None:
        raise ToolError("draft-promotion-marker-required", "existing promotion requires one carried canonical Draft marker")
    if canonical_target.atom_id != marker.canonical_id:
        raise ToolError("canonical-target-mismatch", "canonical target must be the marker's exact current Atom")
    if isinstance(proposed_version, bool) or not isinstance(proposed_version, int) or proposed_version < 1:
        raise ToolError("draft-proposed-version-required", "existing Draft promotion requires one positive proposed_version")
    if marker.proposed_version is not None and proposed_version != marker.proposed_version:
        raise ToolError("draft-proposed-version-mismatch", "qualified Draft marker and request disagree on proposed_version")
    if atom_version(draft) != proposed_version:
        raise ToolError("draft-proposed-version-mismatch", "Draft carrier Version must equal its proposed Version")
    return marker, proposed_version


def _require_exact_current_canonical(root: Path, canonical_target: Atom) -> None:
    require_current_atom(root, canonical_target)
    from current_atom_locator import CurrentAtomLocator
    CurrentAtomLocator(root).assert_unique_current_claim(canonical_target.atom_id or "", canonical_target.relative)


def _existing_draft_preserves_canonical(draft: Atom, canonical_target: Atom) -> bool:
    if frontmatter_scalar(draft.frontmatter, "content_role") != frontmatter_scalar(canonical_target.frontmatter, "content_role"):
        raise ToolError("atom-role-changed", "existing Draft promotion must retain the canonical Content Role")
    if frontmatter_scalar(draft.frontmatter, "type") != frontmatter_scalar(canonical_target.frontmatter, "type"):
        raise ToolError("atom-type-changed", "existing Draft promotion must retain the canonical Type")
    if _draft_summary(draft.content) != _draft_summary(canonical_target.content):
        raise ToolError("summary-changed", "existing Draft promotion must retain the canonical Summary")
    return _normalized_promotion_candidate_matches(draft.frontmatter, draft.content, canonical_target)


def _normalized_promotion_candidate_matches(frontmatter: str, content: str, canonical_target: Atom) -> bool:
    return (_without_promotion_metadata(frontmatter) == _without_promotion_metadata(canonical_target.frontmatter)
            and content == canonical_target.content)


def bind_existing_draft_promotion(
    root: Path,
    draft: Atom,
    canonical_target: Atom,
    *,
    proposed_version: int | None = None,
    requested_status: str = "Active",
) -> ExistingDraftPromotion:
    """Bind one existing-marker Draft to its exact current canonical target."""

    root = root.resolve()
    marker, version = _bind_existing_draft_marker(root, draft, canonical_target, proposed_version)
    _require_exact_current_canonical(root, canonical_target)
    no_op = (_existing_draft_preserves_canonical(draft, canonical_target)
             and frontmatter_scalar(canonical_target.frontmatter, "status") == requested_status)
    current_version = atom_version(canonical_target)
    if version not in {current_version, current_version + 1}:
        raise ToolError("atom-version-invalid", "existing Draft proposed Version must be current or next")
    if not no_op and version != current_version + 1:
        raise ToolError("atom-version-invalid", "existing Draft promotion Version must be the canonical current Version plus one")
    return ExistingDraftPromotion(canonical_target, marker, version, no_op)


def prepare_existing_draft_promotion_frontmatter(
    root: Path, frontmatter: str, binding: ExistingDraftPromotion, requested_status: str,
) -> str:
    """Materialize only the admitted identity, Status, Version, and effect time."""

    prepared = replace_frontmatter_scalar(frontmatter, "atom_id", binding.canonical_target.atom_id or "")
    prepared = replace_frontmatter_scalar(prepared, "status", requested_status)
    prepared = replace_frontmatter_scalar(prepared, "version", str(binding.proposed_version))
    return replace_frontmatter_scalar(prepared, "updated_at", f'"{current_timestamp(root)}"')


def _bundle_content_and_mode_match(expected: Mapping, observed: Mapping) -> bool:
    if expected.keys() != observed.keys():
        return False
    return all(before is not None and observed[key] is not None
               and before[0] == observed[key][0] and before[1][-1] == observed[key][1][-1]
               for key, before in expected.items())


def _restore_moved_existing_canonical(
    root: Path, canonical_target: Atom, published: Atom, published_bundle: Mapping,
    canonical_bundle: Mapping,
) -> None:
    if status_bundle_snapshot(root, published) != published_bundle:
        raise ToolError("status-recovery-blocked", "published canonical bundle changed before recovery")
    source_bundle, destination_bundle = canonical_target.path.with_suffix(""), published.path.with_suffix("")
    if "directory" in canonical_bundle:
        expected = {key: value for key, value in canonical_bundle.items() if key != "markdown"}
        observed = {key: value for key, value in published_bundle.items() if key != "markdown"}
        if source_bundle.exists() or not destination_bundle.is_dir() or not carrier_directory_snapshot_matches(expected, observed, renamed=True):
            raise ToolError("status-recovery-blocked", "canonical container bundle cannot be returned")
        destination_bundle.rename(source_bundle)
    elif destination_bundle.exists():
        raise ToolError("status-recovery-blocked", "unexpected canonical destination bundle")
    _, fingerprint = published_bundle["markdown"]
    if canonical_target.path.exists():
        raise ToolError("status-recovery-blocked", "canonical source unexpectedly reappeared")
    write_raw_atom_revision(root, canonical_target.path, canonical_bundle["markdown"][0], expected=None, mode=fingerprint[-1])
    write_raw_atom_revision(root, published.path, None, expected=fingerprint, mode=fingerprint[-1])


def _restore_same_path_existing_canonical(
    root: Path, canonical_target: Atom, published: Atom | None, published_bundle: Mapping | None,
    canonical_bundle: Mapping,
) -> None:
    current_bundle = status_bundle_snapshot(root, canonical_target)
    if published is None:
        if current_bundle != canonical_bundle:
            raise ToolError("status-recovery-blocked", "canonical publication ownership is unknown")
        return
    if published_bundle is None or current_bundle != published_bundle:
        raise ToolError("status-recovery-blocked", "published canonical bundle changed before recovery")
    _, fingerprint = current_bundle["markdown"]
    write_raw_atom_revision(root, canonical_target.path, canonical_bundle["markdown"][0],
                            expected=fingerprint, mode=fingerprint[-1])


def _restore_existing_history(root: Path, history: Path | None, canonical_raw: bytes) -> None:
    if history is None or not history.exists():
        return
    history_raw, fingerprint = read_raw_atom_revision(root, history)
    if history_raw != canonical_raw:
        raise ToolError("status-recovery-blocked", "predecessor history bytes are not exact")
    write_raw_atom_revision(root, history, None, expected=fingerprint, mode=fingerprint[-1])


def _restore_existing_draft_source(root: Path, draft: Atom, draft_bundle: Mapping) -> None:
    draft_raw, fingerprint = draft_bundle["markdown"]
    if draft.path.exists():
        restored_raw, _ = read_raw_atom_revision(root, draft.path)
        if restored_raw != draft_raw:
            raise ToolError("status-recovery-blocked", "Draft source bytes are not exact")
        return
    write_raw_atom_revision(root, draft.path, draft_raw, expected=None, mode=fingerprint[-1])


def _verify_existing_promotion_recovery(
    root: Path, draft: Atom, canonical_target: Atom, draft_bundle: Mapping, canonical_bundle: Mapping,
) -> None:
    if not _bundle_content_and_mode_match(canonical_bundle, status_bundle_snapshot(root, canonical_target)):
        raise ToolError("status-recovery-blocked", "canonical container bundle is not restored")
    restored_draft = atom_from_path(root, draft.path)
    if not _bundle_content_and_mode_match(draft_bundle, status_bundle_snapshot(root, restored_draft)):
        raise ToolError("status-recovery-blocked", "Draft container bundle is not restored")


def _restore_existing_draft_promotion(
    root: Path, draft: Atom, canonical_target: Atom, published: Atom | None,
    published_bundle: Mapping | None, history: Path | None, draft_bundle: Mapping,
    canonical_bundle: Mapping,
) -> None:
    try:
        if published is not None and published.path != canonical_target.path:
            if published_bundle is None:
                raise ToolError("status-recovery-blocked", "published canonical bundle is unknown")
            _restore_moved_existing_canonical(root, canonical_target, published, published_bundle, canonical_bundle)
        else:
            _restore_same_path_existing_canonical(root, canonical_target, published, published_bundle, canonical_bundle)
        _restore_existing_history(root, history, canonical_bundle["markdown"][0])
        _restore_existing_draft_source(root, draft, draft_bundle)
        _verify_existing_promotion_recovery(root, draft, canonical_target, draft_bundle, canonical_bundle)
    except BaseException as error:
        raise ToolError("status-recovery-uncertain", "existing Draft promotion recovery is unverified; do not replay",
                        {"automatic_retry": False, "source": draft.relative}) from error


def _existing_promotion_destination(root: Path, atom: Atom, status: str) -> str:
    """Resolve the admitted current-status location for an existing canonical Atom."""

    control = control_root(root)
    try:
        relative = atom.path.relative_to(control)
        index = next(i for i, part in enumerate(relative.parts[:-1]) if re.fullmatch(r"0[1-9]_[a-z0-9_]+", part))
    except (ValueError, StopIteration) as error:
        raise ToolError("status-location-missing", "canonical target has no content-role status location") from error
    role = control.joinpath(*relative.parts[:index + 1])
    stem = re.sub(r"@[0-9]+$", "", atom.path.stem)
    if frontmatter_scalar(atom.frontmatter, "content_role") in {"Plan", "Operations"}:
        local = atom.path.parent.parent if atom.path.parent.name in {"001_backlog", "done", "canceled", "archived", "draft"} else atom.path.parent
        folder = {"Active": None, "Backlog": "001_backlog", "Done": "done", "Canceled": "canceled", "Archived": "archived"}.get(status)
        if status in {"Active", "Backlog", "Done", "Canceled", "Archived"}:
            return (local / folder / f"{stem}.md" if folder else local / f"{stem}.md").relative_to(root).as_posix()
    if status.casefold() == "active":
        return (role / f"{stem}.md").relative_to(root).as_posix()
    folder = status.casefold()
    if re.fullmatch(r"[a-z0-9][a-z0-9_-]*", folder) is None:
        raise ToolError("status-location-invalid", "admitted status cannot name a safe carrier subfolder")
    return (role / folder / f"{stem}.md").relative_to(root).as_posix()


def _existing_promotion_history_path(atom: Atom) -> Path:
    stem = re.sub(r"@[0-9]+$", "", atom.path.stem)
    local = atom.path.parent.parent if atom.path.parent.name in {
        "001_backlog", "done", "canceled", "archived", "resolved", "draft",
    } else atom.path.parent
    return local / "archived" / f"{stem}@{atom_version(atom)}.md"


def _existing_promotion_is_noop(atom: Atom, prepared: str, content: str, requested_status: str) -> bool:
    return (frontmatter_scalar(atom.frontmatter, "status") == requested_status
            and _normalized_promotion_candidate_matches(prepared, content, atom))


def _validate_existing_promotion_destination(
    destination: Path, canonical_target: Atom, identity: str | None, history: Path,
) -> None:
    if identity != canonical_target.atom_id:
        raise ToolError("canonical-target-mismatch", "existing Draft promotion must publish only its canonical target")
    if history.exists() or history.is_symlink() or (destination != canonical_target.path and
                                                    (destination.exists() or destination.is_symlink())):
        raise ToolError("destination-collision", "existing Draft promotion destination already exists")


def promote_existing_draft_atom(
    root: Path, draft: Atom, binding: ExistingDraftPromotion, frontmatter: str, content: str, *,
    requested_status: str, expected_draft_digest: str, expected_canonical_digest: str,
) -> tuple[Atom, Atom | None, bool]:
    """Use the status revision owner, then conditionally remove its sealed Draft source."""

    root = root.resolve()
    with atom_identity_lock(root):
        current_draft = atom_from_path(root, draft.path)
        current_canonical = atom_from_path(root, binding.canonical_target.path)
        if atom_digest(current_draft) != expected_draft_digest or atom_digest(current_canonical) != expected_canonical_digest:
            raise ToolError("carrier-stale", "Draft or canonical predecessor changed before publication")
        refreshed = bind_existing_draft_promotion(
            root, current_draft, current_canonical, proposed_version=binding.proposed_version,
            requested_status=requested_status,
        )
        prepared = prepare_existing_draft_promotion_frontmatter(root, frontmatter, refreshed, requested_status)
        if _existing_promotion_is_noop(current_canonical, prepared, content, requested_status):
            return current_canonical, None, True
        canonical_relative = _existing_promotion_destination(root, current_canonical, requested_status)
        destination, normalized, identity = prepare_create_atom_revision(
            root, canonical_relative, prepared, content, creating=False,
        )
        history = _existing_promotion_history_path(current_canonical)
        _validate_existing_promotion_destination(destination, current_canonical, identity, history)
        draft_bundle = status_bundle_snapshot(root, current_draft)
        canonical_bundle = status_bundle_snapshot(root, current_canonical)
        if "directory" in draft_bundle:
            raise ToolError("draft-container-publication-unsupported", "Draft container publication requires an explicit child action")
        if (hashlib.sha256(draft_bundle["markdown"][0]).hexdigest() != expected_draft_digest
                or hashlib.sha256(canonical_bundle["markdown"][0]).hexdigest() != expected_canonical_digest):
            raise ToolError("carrier-stale", "Draft or canonical bundle changed before publication")
        observed: Atom | None = None
        published_bundle: Mapping | None = None
        try:
            observed, written_history = publish_status_atom_revision(
                root, current_canonical, canonical_relative, normalized, content,
                expected_bundle=canonical_bundle,
            )
            if written_history != history:
                raise ToolError("status-history-verification-failed", "canonical predecessor location changed")
            published_bundle = status_bundle_snapshot(root, observed)
            write_raw_atom_revision(root, current_draft.path, None,
                                    expected=draft_bundle["markdown"][1], mode=draft_bundle["markdown"][1][-1])
            if current_draft.path.exists():
                raise ToolError("draft-cleanup-failed", "Draft carrier remains after promotion")
            return observed, atom_from_path(root, history) if history is not None else None, False
        except BaseException:
            if observed is None and destination != current_canonical.path and destination.exists():
                observed = atom_from_path(root, destination)
                published_bundle = status_bundle_snapshot(root, observed)
            _restore_existing_draft_promotion(root, current_draft, current_canonical, observed,
                                              published_bundle, history, draft_bundle, canonical_bundle)
            raise


def replace_frontmatter_scalar(frontmatter: str, name: str, value: str) -> str:
    """Replace one top-level scalar while retaining every unrelated YAML block."""

    if not isinstance(value, str) or not value:
        raise ToolError("input-invalid", f"{name} must be a non-empty scalar")
    expression = re.compile(rf"(?m)^{re.escape(name)}:\s*.*?\s*$")
    matches = list(expression.finditer(frontmatter))
    if len(matches) > 1:
        raise ToolError("atom-frontmatter-invalid", f"Atom has duplicate {name} values")
    replacement = f"{name}: {value}"
    if matches:
        return expression.sub(replacement, frontmatter, count=1)
    return (frontmatter + "\n" if frontmatter else "") + replacement


def remove_frontmatter_scalar(frontmatter: str, name: str) -> str:
    """Remove one top-level scalar without changing unrelated carrier bytes."""

    expression = re.compile(rf"(?m)^{re.escape(name)}:\s*.*?(?:\n|$)")
    matches = list(expression.finditer(frontmatter))
    if len(matches) > 1:
        raise ToolError("atom-frontmatter-invalid", f"Atom has duplicate {name} values")
    return expression.sub("", frontmatter, count=1).rstrip("\n")


def draft_revision_lineage(frontmatter: str) -> dict[str, Any] | None:
    """Read the one serialized Draft provenance map without treating it as identity."""

    raw = frontmatter_scalar(frontmatter, "revision_lineage")
    if raw is None:
        return None
    try:
        value = json.loads(raw)
    except json.JSONDecodeError as error:
        raise ToolError("draft-lineage-invalid", "revision_lineage must be one JSON-compatible YAML map") from error
    if not isinstance(value, dict):
        raise ToolError("draft-lineage-invalid", "revision_lineage must be one map")
    return value


def replace_draft_revision_lineage(frontmatter: str, lineage: Mapping[str, Any]) -> str:
    """Serialize the source-governed Draft lineage map as one YAML map value."""

    return replace_frontmatter_scalar(frontmatter, "revision_lineage", json.dumps(dict(lineage), sort_keys=True))


def atom_version(atom: Atom) -> int:
    """Return the current carried Version without manufacturing a default."""

    raw = frontmatter_scalar(atom.frontmatter, "version")
    if raw is None or re.fullmatch(r"[0-9]+", raw) is None:
        raise ToolError("atom-version-invalid", f"Atom lacks a non-negative integer Version: {atom.relative}")
    return int(raw)


def atom_digest(atom: Atom) -> str:
    """Return the digest of the full, current carrier bytes."""

    return hashlib.sha256(atom.path.read_bytes()).hexdigest()


def write_atom_revision(atom: Atom, frontmatter: str, content: str) -> None:
    """Persist one already-validated full carrier revision atomically."""

    _atomic_write(atom.path, render(frontmatter, content))


def _raw_revision_parent(root: Path, path: Path, *, create: bool = False) -> int:
    """Hold the lexical destination directory without following any alias."""

    try:
        relative = path.relative_to(root)
        if not relative.parts or ".." in relative.parts:
            raise ValueError("unsafe path")
        flags = os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW
        descriptor = os.open(root, flags)
        try:
            for part in relative.parts[:-1]:
                if create:
                    try:
                        os.mkdir(part, dir_fd=descriptor)
                    except FileExistsError:
                        pass
                child = os.open(part, flags, dir_fd=descriptor)
                os.close(descriptor)
                descriptor = child
            return descriptor
        except BaseException:
            os.close(descriptor)
            raise
    except (OSError, ValueError, AttributeError) as error:
        raise ToolError("subject-destination-unsafe", "Subject destination cannot be safely opened") from error


def _raw_revision_fingerprint(value: os.stat_result) -> tuple[int, ...]:
    return (value.st_dev, value.st_ino, value.st_size, value.st_mtime_ns, value.st_ctime_ns,
            stat.S_IMODE(value.st_mode))


@contextmanager
def atom_identity_lock(root: Path):
    """Serialize identity admission/publication across Project threads and processes."""
    root = root.resolve()
    key = (os.getpid(), root)
    held = getattr(_IDENTITY_LOCKS, "held", None)
    if held is None:
        held = _IDENTITY_LOCKS.held = set()
    if key in held:
        yield
        return
    path = root / RUNTIME_DIRECTORY / "state" / "atom_operations" / "identity.lock"
    parent = _raw_revision_parent(root, path, create=True)
    descriptor = None
    try:
        # Guard concurrent secure opens before the file lock can serialize callers.
        fcntl.flock(parent, fcntl.LOCK_EX)
        descriptor = os.open(path.name, os.O_RDWR | os.O_CREAT | os.O_NOFOLLOW, 0o600, dir_fd=parent)
        if not stat.S_ISREG(os.fstat(descriptor).st_mode):
            raise OSError("identity lock is not a regular file")
        fcntl.flock(descriptor, fcntl.LOCK_EX)
    except BaseException as error:
        if descriptor is not None:
            os.close(descriptor)
        if isinstance(error, OSError):
            raise ToolError("atom-identity-lock-unavailable", "Project identity publication lock is unavailable") from error
        raise
    finally:
        os.close(parent)
    held.add(key)
    try:
        yield
    finally:
        held.remove(key)
        try:
            fcntl.flock(descriptor, fcntl.LOCK_UN)
        finally:
            os.close(descriptor)


def read_raw_atom_revision(root: Path, path: Path) -> tuple[bytes, tuple[int, ...]]:
    """Read exact bytes and mode through a no-follow, stable regular-file handle."""

    parent = _raw_revision_parent(root, path)
    try:
        descriptor = os.open(path.name, os.O_RDONLY | os.O_NOFOLLOW | os.O_NONBLOCK, dir_fd=parent)
        with os.fdopen(descriptor, "rb") as stream:
            before = os.fstat(stream.fileno())
            if not stat.S_ISREG(before.st_mode):
                raise ToolError("subject-source-unsafe", "Subject revision is not a regular file")
            raw = stream.read()
            after = os.fstat(stream.fileno())
        if _raw_revision_fingerprint(before) != _raw_revision_fingerprint(after):
            raise ToolError("subject-source-changed", "Subject revision changed during readback")
        return raw, _raw_revision_fingerprint(after)
    finally:
        os.close(parent)


def write_raw_atom_revision(root: Path, path: Path, raw: bytes | None, *,
                            expected: tuple[int, ...] | None, mode: int) -> tuple[int, ...] | None:
    """Prototype raw publication; final compare-to-replace/remove is not concurrency-safe."""

    parent = _raw_revision_parent(root, path, create=expected is None and raw is not None)
    staging = None
    temporary = ".subject-" + uuid.uuid4().hex + ".tmp"
    staged = False
    published: tuple[int, ...] | None = None
    publication_occurred = False
    try:
        if raw is not None:
            staging = _raw_revision_parent(root, root / ".caprmedio_tmp" / "atom_subject_apply" / "atomic" / temporary, create=True)
            if os.fstat(staging).st_dev != os.fstat(parent).st_dev:
                raise ToolError("subject-destination-unsafe", "Subject temporary state is on a different filesystem")
            descriptor = os.open(temporary, os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW,
                                 mode, dir_fd=staging)
            staged = True
            with os.fdopen(descriptor, "wb") as stream:
                stream.write(raw)
                stream.flush()
                os.fchmod(stream.fileno(), mode)
                os.fsync(stream.fileno())
        try:
            current = os.stat(path.name, dir_fd=parent, follow_symlinks=False)
        except FileNotFoundError:
            current = None
        if ((expected is None and current is not None)
                or (expected is not None and (current is None or not stat.S_ISREG(current.st_mode)
                                             or _raw_revision_fingerprint(current) != expected))):
            raise ToolError("subject-destination-stale", "Subject destination differs from the captured revision")
        fresh_parent = _raw_revision_parent(root, path)
        try:
            if (os.fstat(fresh_parent).st_dev, os.fstat(fresh_parent).st_ino) != (os.fstat(parent).st_dev, os.fstat(parent).st_ino):
                raise ToolError("subject-destination-stale", "Subject destination directory changed")
        finally:
            os.close(fresh_parent)
        if raw is None:
            os.unlink(path.name, dir_fd=parent)
            publication_occurred = True
        elif expected is None:
            os.link(temporary, path.name, src_dir_fd=staging, dst_dir_fd=parent, follow_symlinks=False)
            publication_occurred = True
            published = _raw_revision_fingerprint(os.stat(path.name, dir_fd=parent, follow_symlinks=False))
            os.unlink(temporary, dir_fd=staging)
            staged = False
        else:
            os.replace(temporary, path.name, src_dir_fd=staging, dst_dir_fd=parent)
            publication_occurred = True
            staged = False
        if raw is not None:
            published = _raw_revision_fingerprint(os.stat(path.name, dir_fd=parent, follow_symlinks=False))
        os.fsync(parent)
        if raw is None:
            return None
        return published
    except OSError as error:
        # Removing the staging hardlink changes ctime on the published inode.
        # Retain a post-cleanup fingerprint only while the same bytes/inode remain.
        if publication_occurred and staged and published is not None:
            try:
                os.unlink(temporary, dir_fd=staging)
                staged = False
                current = _raw_revision_fingerprint(os.stat(path.name, dir_fd=parent, follow_symlinks=False))
                published = current if current[:4] + current[5:] == published[:4] + published[5:] else None
            except OSError:
                published = None
        raise ToolError("subject-publication-failed", "Subject raw-byte publication failed",
                        {"publication_occurred": publication_occurred,
                         **({"publication_fingerprint": published} if published is not None else {})}) from error
    finally:
        try:
            if staged:
                os.unlink(temporary, dir_fd=staging)
        except OSError as error:
            raise ToolError("subject-publication-failed", "Subject temporary cleanup failed",
                            {"publication_occurred": publication_occurred,
                             **({"publication_fingerprint": published} if published is not None else {})}) from error
        finally:
            if staging is not None:
                os.close(staging)
            os.close(parent)


def _validate_complete_carrier(root: Path, path: Path, frontmatter: str, content: str, *, creating: bool,
                               validation_scope: CarrierValidationScope | None = None) -> None:
    try:
        parsed = parse_carrier(("---\n" + frontmatter + "\n---\n" + content).encode("utf-8"), Path("proposed.md"))
        # D570 permits retained lineage data, but never makes its encoding an
        # admission capability. YAML syntax and all other schema rules remain.
        parsed.metadata.pop("revision_lineage", None)
        relative = path.relative_to(control_root(root))
        if validation_scope is None:
            validate_proposed_carrier(parsed.metadata, parsed.body, source_context_from_project(root), relative,
                                      allow_existing_relations=not creating)
        else:
            validation_scope.validate(root, parsed.metadata, parsed.body, relative,
                                      allow_existing_relations=not creating)
    except (CarrierError, ProposedCarrierError, UnicodeError, StatusModelError) as error:
        raise ToolError("complete-carrier-invalid", "new Atom carrier is incomplete, invalid, or unresolved") from error


def _validate_revision_filename(path: Path, frontmatter: str, *, creating: bool) -> None:
    """Apply ordinary filename grammar plus the carried Archived Version suffix."""
    filename = path.name
    if frontmatter_scalar(frontmatter, "status") == "Archived":
        version = "1" if creating else frontmatter_scalar(frontmatter, "version")
        if version is None or not version.isdecimal() or not filename.endswith(f"@{int(version)}.md"):
            raise ToolError("filename-invalid", "Archived carrier requires its Revision suffix immediately before .md")
        filename = re.sub(r"@[0-9]+(?=\.md$)", "", filename)
    if not CURRENT_FILENAME.fullmatch(filename):
        raise ToolError("filename-invalid", f"new Atom filename does not follow current grammar: {path.name}")


def prepare_create_atom_revision(
    root: Path, relative_path: str, frontmatter: str, content: str | None = None, *, creating: bool = True
) -> tuple[Path, str, str | None]:
    """Validate the explicit identity and destination of one new full carrier.

    The lifecycle adapter calls this before authorization and before any effect.
    It deliberately never derives or inserts an Atom ID from a filename: a
    non-draft carrier has to carry the same stable ID in both places.
    """

    root = root.resolve()
    path = safe_path(root, relative_path)
    _validate_destination(root, path, filename_required=True)
    normalized = _normalize_frontmatter(frontmatter)
    _validate_revision_filename(path, normalized, creating=creating)
    match = ATOM_ID.search(path.name)
    atom_id = match.group(1) if match else None
    destination_lifecycle = _lifecycle(path, control_root(root))
    declared = frontmatter_scalar(normalized, "atom_id")
    if destination_lifecycle == "draft":
        _draft_marker_identity(root, path, normalized)
        if atom_id is not None:
            raise ToolError("draft-has-stable-id", f"draft filename must not contain a stable Atom ID: {path.name}")
    if destination_lifecycle != "draft" and atom_id is None:
        raise ToolError("atom-id-required", f"non-draft Atom filename must contain a stable Atom ID: {path.name}")
    if atom_id is not None and declared is None:
        raise ToolError("atom-frontmatter-id-required", "non-draft Atom frontmatter must declare atom_id")
    if atom_id is not None and declared != atom_id:
        raise ToolError("atom-frontmatter-id-mismatch", "frontmatter atom_id must equal the filename Atom ID")
    # Legacy lifecycle previews currently pass only the frontmatter.  They keep
    # their existing identity/destination preflight until their owner supplies
    # the already-carried body to this shared boundary.
    if content is None:
        return path, normalized, atom_id
    if not isinstance(content, str):
        raise ToolError("complete-carrier-required", "new Atom carrier content is required before preparation")
    prepared = _revision(root, normalized, creating=creating) if creating else normalized
    _validate_complete_carrier(root, path, prepared, content, creating=creating)
    return path, prepared, atom_id


def create_atom_revision(root: Path, relative_path: str, frontmatter: str, content: str) -> Atom:
    """Create one validated, complete Markdown Atom carrier atomically."""

    root = root.resolve()
    with atom_identity_lock(root):
        path, prepared, atom_id = prepare_create_atom_revision(root, relative_path, frontmatter, content)
        if path.exists():
            raise ToolError("destination-collision", f"Atom destination already exists: {path.relative_to(root)}")
        if atom_id and atom_id_has_preserved_history_evidence(root, atom_id):
            raise ToolError("atom-id-collision", f"Atom ID was already used: {atom_id}")
        _atomic_write(path, render(prepared, content))
        return atom_from_path(root, path)


def require_current_atom(root: Path, atom: Atom) -> None:
    """Distinguish a current Archived carrier from immutable predecessor bytes."""
    relative = atom.path.relative_to(control_root(root))
    if "archive" in relative.parts:
        raise ToolError("atom-not-current", "preserved Atom revisions are immutable")
    if atom.lifecycle == "archived":
        if frontmatter_scalar(atom.frontmatter, "status") != "Archived":
            raise ToolError("atom-not-current", "preserved Atom revisions are immutable")
        if any(candidate.atom_id == atom.atom_id and atom_version(candidate) > atom_version(atom)
               for candidate in scan_atoms(root)):
            raise ToolError("atom-not-current", "a later Atom revision is already current")


def move_atom_revision(root: Path, atom: Atom, relative_path: str, frontmatter: str, content: str,
                       *, expected_bundle: Mapping) -> Atom:
    """Atomically relocate one current carrier bundle while retaining its identity."""

    root = root.resolve()
    target, normalized, atom_id = prepare_create_atom_revision(
        root, relative_path, frontmatter, content, creating=False
    )
    if atom.atom_id is None or atom_id != atom.atom_id:
        raise ToolError("atom-frontmatter-id-mismatch", "moved carrier must retain the current Atom ID")
    if target != atom.path and target.exists():
        raise ToolError("destination-collision", f"Atom destination already exists: {target.relative_to(root)}")
    source_directory, destination_directory = atom.path.with_suffix(""), target.with_suffix("")
    if target != atom.path and (destination_directory.exists() or destination_directory.is_symlink()):
        raise ToolError("destination-collision", "matching destination directory already exists")
    if status_bundle_snapshot(root, atom) != expected_bundle:
        raise ToolError("status-bundle-stale", "move carrier bundle changed after admission")
    _atomic_write(target, render(normalized, content))
    if "directory" in expected_bundle and target != atom.path:
        source_directory.rename(destination_directory)
    if target != atom.path:
        atom.path.unlink()
    return atom_from_path(root, target)


def _prepare_draft_rename(root: Path, atom: Atom, relative_path: str, frontmatter: str, content: str,
                          expected_bundle: Mapping) -> tuple[Path, str, bytes, int]:
    if atom.lifecycle != "draft" or atom.atom_id is not None:
        raise ToolError("atom-not-draft", "only one Draft marker carrier can be renamed")
    target, normalized, identity = prepare_create_atom_revision(
        root, relative_path, frontmatter, content, creating=False
    )
    if identity is not None or _draft_marker_identity(root, target, normalized) is None:
        raise ToolError("draft-marker-invalid", "Draft marker rename requires one aligned Draft marker")
    if target != atom.path and target.exists():
        raise ToolError("destination-collision", f"Draft destination already exists: {target.relative_to(root)}")
    if status_bundle_snapshot(root, atom) != expected_bundle:
        raise ToolError("status-bundle-stale", "Draft carrier changed after admission")
    before = atom.path.read_bytes()
    mode = atom.path.stat().st_mode & 0o777
    destination_directory = target.with_suffix("")
    if target != atom.path and "directory" in expected_bundle and destination_directory.exists():
        raise ToolError("destination-collision", "matching Draft carrier directory already exists")
    return target, normalized, before, mode


def _restore_draft_rename(atom: Atom, target: Path, before: bytes, mode: int) -> None:
    destination_directory, source_directory = target.with_suffix(""), atom.path.with_suffix("")
    if target != atom.path and destination_directory.exists() and not source_directory.exists():
        destination_directory.rename(source_directory)
    if target != atom.path and target.exists():
        target.unlink()
    if not atom.path.exists() or atom.path.read_bytes() != before:
        _atomic_write(atom.path, before)
        atom.path.chmod(mode)


def _publish_draft_rename(root: Path, atom: Atom, target: Path, normalized: str, content: str,
                          expected_bundle: Mapping) -> Atom:
    source_directory, destination_directory = atom.path.with_suffix(""), target.with_suffix("")
    output = render(normalized, content)
    _atomic_write(target, output)
    if target != atom.path and "directory" in expected_bundle:
        source_directory.rename(destination_directory)
    if target != atom.path:
        atom.path.unlink()
    observed = atom_from_path(root, target)
    if status_bundle_snapshot(root, observed)["markdown"][0] != output:
        raise ToolError("status-bundle-verification-failed", "renamed Draft carrier differs")
    return observed


def rename_draft_revision(root: Path, atom: Atom, relative_path: str, frontmatter: str, content: str,
                          *, expected_bundle: Mapping) -> Atom:
    """Rename one carried Draft marker while preserving its exact carrier bytes."""

    root = root.resolve()
    target, normalized, before, mode = _prepare_draft_rename(
        root, atom, relative_path, frontmatter, content, expected_bundle,
    )
    try:
        return _publish_draft_rename(root, atom, target, normalized, content, expected_bundle)
    except BaseException:
        _restore_draft_rename(atom, target, before, mode)
        raise


def status_bundle_snapshot(root: Path, atom: Atom) -> dict[str, tuple[bytes, tuple[int, ...]] | None]:
    """Seal this Markdown and its optional matching directory, without following links."""
    bundle = atom.path.with_suffix("")
    result = {"markdown": read_raw_atom_revision(root, atom.path)}
    if bundle.is_symlink():
        raise ToolError("status-bundle-unsafe", "matching directory must not be a symlink")
    if bundle.exists():
        if not bundle.is_dir():
            raise ToolError("status-bundle-unsafe", "matching carrier is not a directory")
        role, kind = frontmatter_scalar(atom.frontmatter, "content_role"), frontmatter_scalar(atom.frontmatter, "type")
        if role != "Plan" and (role != "Operations" or kind not in {"Workflow", "Step"}):
            raise ToolError("status-bundle-unsupported", "matching directory is not an admitted P/O container")
        try:
            result.update(carrier_directory_snapshot(root, bundle))
        except ToolError as error:
            if error.code == "carrier-bundle-unsafe":
                raise ToolError("status-bundle-unsafe", error.message) from error
            raise
    return result


def carrier_directory_snapshot(root: Path, bundle: Path) -> dict[str, tuple[bytes, tuple[int, ...]] | None]:
    """Seal a carrier directory and its entries without following links."""
    if bundle.is_symlink():
        raise ToolError("carrier-bundle-unsafe", "matching directory must not be a symlink")
    if not bundle.is_dir():
        raise ToolError("carrier-bundle-unsafe", "matching carrier is not a directory")
    result = {"directory": (b"", _raw_revision_fingerprint(bundle.stat()))}
    for path in sorted(bundle.rglob("*")):
        if path.is_symlink():
            raise ToolError("carrier-bundle-unsafe", "matching directory contains a symlink")
        key = "directory/" + path.relative_to(bundle).as_posix()
        result[key] = (b"", _raw_revision_fingerprint(path.stat())) if path.is_dir() else read_raw_atom_revision(root, path)
    return result


def carrier_directory_snapshot_matches(
    expected: Mapping[str, tuple[bytes, tuple[int, ...]] | None],
    observed: Mapping[str, tuple[bytes, tuple[int, ...]] | None],
    *, renamed: bool = False,
) -> bool:
    """Compare bundle bytes and fingerprints, allowing root ctime to change on rename."""
    if expected.keys() != observed.keys():
        return False
    for key, prior in expected.items():
        current = observed[key]
        if prior is None or current is None:
            if prior != current:
                return False
            continue
        if prior[0] != current[0] or prior[1] != current[1]:
            if (not renamed or key != "directory" or prior[0] != current[0]
                    or prior[1][:4] != current[1][:4] or prior[1][5:] != current[1][5:]):
                return False
    return True


def publish_status_atom_revision(root: Path, atom: Atom, relative_path: str, frontmatter: str,
                                 content: str, *, expected_bundle: Mapping) -> tuple[Atom, Path | None]:
    if atom.atom_id is None:
        with atom_identity_lock(root):
            return _publish_status_atom_revision(root, atom, relative_path, frontmatter, content,
                                                 expected_bundle=expected_bundle)
    return _publish_status_atom_revision(root, atom, relative_path, frontmatter, content,
                                         expected_bundle=expected_bundle)


def _publish_status_atom_revision(root: Path, atom: Atom, relative_path: str, frontmatter: str,
                                  content: str, *, expected_bundle: Mapping) -> tuple[Atom, Path | None]:
    """Publish one admitted status bundle with checked before/after bytes."""
    require_current_atom(root, atom)
    target, normalized, identity = prepare_create_atom_revision(
        root, relative_path, frontmatter, content, creating=False)
    draft = frontmatter_scalar(normalized, "status").casefold() == "draft"
    if atom.atom_id is None:
        if identity is None or atom_id_has_preserved_history_evidence(root, identity):
            raise ToolError("atom-id-collision", "Draft publication requires one unused assigned identity")
    elif (draft and identity is not None) or (not draft and identity != atom.atom_id):
        raise ToolError("atom-frontmatter-id-mismatch", "status publication must retain identity except at the Draft boundary")
    version = atom_version(atom)
    if frontmatter_scalar(normalized, "version") != str(version + 1):
        raise ToolError("atom-version-invalid", "status publication must increment Version exactly once")
    stem = re.sub(r"@[0-9]+$", "", atom.path.stem)
    local = atom.path.parent
    if local.name in {"001_backlog", "done", "canceled", "archived", "resolved", "draft"}:
        local = local.parent
    history = local / ("archive" if draft else "archived") / f"{stem}@{version}.md" if atom.atom_id is not None else None
    source_directory, destination_directory = atom.path.with_suffix(""), target.with_suffix("")
    raw, source_fingerprint = expected_bundle["markdown"]
    output = render(normalized, content)
    for path in (target, history, destination_directory):
        if path is None:
            continue
        parent = _raw_revision_parent(root, path) if path.parent.exists() else None
        if parent is not None:
            os.close(parent)
        if path not in {atom.path, source_directory} and (path.exists() or path.is_symlink()):
            raise ToolError("destination-collision", f"status destination exists: {path.relative_to(root)}")
    if status_bundle_snapshot(root, atom) != expected_bundle:
        raise ToolError("status-bundle-stale", "status carrier bundle changed after admission")
    created: dict[Path, tuple[int, ...]] = {}
    removed = moved = False
    def publish(path, data, expected):
        try:
            created[path] = write_raw_atom_revision(root, path, data, expected=expected,
                                                    mode=source_fingerprint[-1])
        except ToolError as error:
            fingerprint = error.details.get("publication_fingerprint")
            if fingerprint is not None:
                created[path] = fingerprint
            elif error.details.get("publication_occurred"):
                raise ToolError("status-recovery-uncertain", "status publication occurred without a verified fingerprint; do not replay",
                                {"automatic_retry": False, "destination": path.relative_to(root).as_posix()}) from error
            raise
    try:
        if history is not None and history != atom.path:
            publish(history, raw, None)
        if target == atom.path:
            publish(target, output, source_fingerprint)
        else:
            publish(target, output, None)
        if "directory" in expected_bundle and source_directory != destination_directory:
            if destination_directory.exists() or destination_directory.is_symlink():
                raise ToolError("destination-collision", "matching destination directory appeared")
            moved = None  # A failed call can still leave an observed rename effect.
            source_directory.rename(destination_directory)
            moved = True
        if target != atom.path and history != atom.path:
            try:
                write_raw_atom_revision(root, atom.path, None, expected=source_fingerprint, mode=source_fingerprint[-1])
            finally:
                removed = not atom.path.exists()
        observed = atom_from_path(root, target)
        actual = status_bundle_snapshot(root, observed)
        if actual["markdown"][0] != output or {k: v[0] for k, v in actual.items() if k != "markdown"} != {
                k: v[0] for k, v in expected_bundle.items() if k != "markdown"}:
            raise ToolError("status-bundle-verification-failed", "published status bundle differs")
        if history is not None and read_raw_atom_revision(root, history)[0] != raw:
            raise ToolError("status-history-verification-failed", "exact predecessor was not retained")
        return observed, history
    except BaseException as error:
        try:
            if moved is None:
                moved = not (source_directory.exists() and not destination_directory.exists()
                             and _raw_revision_fingerprint(source_directory.stat())[:2]
                             == expected_bundle["directory"][1][:2])
            if moved:
                if (source_directory.exists() or destination_directory.is_symlink()
                        or _raw_revision_fingerprint(destination_directory.stat())[:2]
                        != expected_bundle["directory"][1][:2]):
                    raise ToolError("status-recovery-blocked", "matching directory ownership is unverified")
                destination_directory.rename(source_directory)
            if removed:
                write_raw_atom_revision(root, atom.path, raw, expected=None, mode=source_fingerprint[-1])
            for path, fingerprint in reversed(list(created.items())):
                write_raw_atom_revision(root, path, raw if path == atom.path else None,
                                        expected=fingerprint, mode=source_fingerprint[-1])
        except BaseException as recovery:
            raise ToolError("status-recovery-uncertain", "status publication recovery is unverified; do not replay",
                            {"automatic_retry": False, "source": atom.relative,
                             "destination": relative_path}) from recovery
        raise error


def migrate_atom_identity_revision(root: Path, atom: Atom, relative_path: str, frontmatter: str, content: str) -> Atom:
    with atom_identity_lock(root):
        return _migrate_atom_identity_revision(root, atom, relative_path, frontmatter, content)


def _migrate_atom_identity_revision(root: Path, atom: Atom, relative_path: str, frontmatter: str, content: str) -> Atom:
    """Persist one separately proven legacy-to-canonical identity encoding.

    Admission and the old-to-new mapping belong to the sealed lifecycle caller,
    not lookup. Preserve the source scope/role location and roll back both paths
    if publication or removal fails. The caller preserves prior bytes first.
    """

    root = root.resolve()
    target, normalized, atom_id = prepare_create_atom_revision(
        root, relative_path, frontmatter, content, creating=False
    )
    if atom.atom_id is None or atom_id is None or atom_id == atom.atom_id:
        raise ToolError("identity-mapping-invalid", "migration requires distinct explicitly bound legacy and canonical encodings")
    if target.parent != atom.path.parent:
        raise ToolError("identity-mapping-invalid", "identity migration cannot change the source scope or Content Role location")
    if target.exists():
        raise ToolError("destination-collision", f"Atom destination already exists: {target.relative_to(root)}")
    # Include prior revisions and unnormalized owners: canonical IDs are never
    # reusable merely because an old/current carrier is not normally parseable.
    for candidate in control_root(root).rglob("*.md"):
        match = ATOM_ID.search(candidate.name)
        if match is not None and match.group(1) == atom_id:
            raise ToolError("atom-id-collision", f"Atom ID was already used: {atom_id}")
        try:
            candidate_frontmatter, _ = split_frontmatter(candidate.read_text(encoding="utf-8"))
            if frontmatter_scalar(candidate_frontmatter, "atom_id") == atom_id:
                raise ToolError("atom-id-collision", f"Atom ID was already used: {atom_id}")
        except (UnicodeDecodeError, OSError):
            continue
        except ToolError as error:
            if error.code == "atom-id-collision":
                raise
    snapshots = {atom.path: atom.path.read_bytes(), target: None}
    try:
        _atomic_write(target, render(normalized, content))
        observed = atom_from_path(root, target)
        atom.path.unlink()
    except BaseException:
        _restore(snapshots)
        raise
    return observed


def preserve_atom_revision(root: Path, atom: Atom, *, allow_nonactive: bool = False,
                           allow_legacy_identity: bool = False) -> Atom:
    """Copy one prior semantic revision to its native role-local history path."""

    root = root.resolve()
    control = control_root(root)
    require_current_atom(root, atom)
    if atom.lifecycle == "draft" or atom.atom_id is None:
        raise ToolError("atom-not-current", f"only identified current Atoms can preserve history: {atom.relative}")
    if not allow_nonactive and atom.lifecycle != "active":
        raise ToolError("atom-not-active", f"only active Atoms with stable identity can preserve history: {atom.relative}")
    role_name = _role_directory(atom.path, control)
    if role_name is None:
        raise ToolError("archive-location-missing", f"Atom has no content-role history location: {atom.relative}")
    role = next(parent for parent in atom.path.parents if parent.name == role_name)
    stem = re.sub(r"@[0-9]+$", "", atom.path.stem)
    target = (role / "archive" / f"{stem}@{atom_version(atom)}{atom.path.suffix}").resolve()
    if target.exists():
        raise ToolError("destination-collision", f"history destination already exists: {target.relative_to(root)}")
    _atomic_write(target, atom.path.read_bytes())
    if frontmatter_scalar(atom.frontmatter, "atom_id") is None or allow_legacy_identity:
        # Explicit legacy Update admission has already proven this identity.
        # Keep its original historical bytes, without granting lookup fallback.
        return replace(atom, path=target, relative=target.relative_to(root).as_posix(),
                       filename=target.name, lifecycle="archived")
    return atom_from_path(root, target)


def archive_atom_revision(root: Path, atom: Atom, frontmatter: str, content: str, *,
                         expected_bundle: Mapping | None = None) -> Atom:
    """Archive the next Revision while retaining the exact current predecessor."""

    root = root.resolve()
    control = control_root(root)
    if atom.lifecycle in {"archived", "draft"} or atom.atom_id is None:
        raise ToolError("atom-not-current", f"only identified current Atoms can be archived: {atom.relative}")
    role_name = _role_directory(atom.path, control)
    if role_name is None:
        raise ToolError("archive-location-missing", f"Atom has no content-role archive location: {atom.relative}")
    local = atom.path.parent
    if local.name in {"001_backlog", "done", "canceled", "archived", "resolved", "draft"}:
        local = local.parent
    stem = re.sub(r"@[0-9]+$", "", atom.path.stem)
    target = local / "archived" / f"{stem}@{atom_version(atom) + 1}{atom.path.suffix}"
    archived, _history = publish_status_atom_revision(
        root, atom, target.relative_to(root).as_posix(), frontmatter, content,
        expected_bundle=status_bundle_snapshot(root, atom) if expected_bundle is None else expected_bundle)
    return archived


def demote_atom_to_draft(root: Path, atom: Atom, frontmatter: str, content: str, *,
                          expected_bundle: Mapping | None = None) -> Atom:
    """Move one identified current revision to its same-role unassigned Draft carrier."""

    root = root.resolve()
    control = control_root(root)
    require_current_atom(root, atom)
    if atom.lifecycle == "draft" or atom.atom_id is None:
        raise ToolError("atom-not-current", "only one identified current Atom can become Draft")
    role_name = _role_directory(atom.path, control)
    if role_name is None:
        raise ToolError("archive-location-missing", f"Atom has no content-role location: {atom.relative}")
    role = next(parent for parent in atom.path.parents if parent.name == role_name)
    filename = re.sub(r"@[0-9]+(?=\.md$)", "", atom.filename)
    draft_name = re.sub(r"^([A-Za-z0-9]+-[A-Z]+)-[0-9]+(?:--|-)", r"\1--", filename, count=1)
    if draft_name == atom.filename:
        raise ToolError("draft-filename-invalid", "identified filename cannot be converted to the admitted Draft form")
    target = (role / "draft" / draft_name).resolve()
    if target.exists():
        raise ToolError("destination-collision", f"draft destination already exists: {target.relative_to(root)}")
    normalized = remove_frontmatter_scalar(_normalize_frontmatter(frontmatter), "atom_id")
    if frontmatter_scalar(normalized, "atom_id") is not None:
        raise ToolError("draft-has-stable-id", "Draft carrier cannot retain atom_id")
    prepare_create_atom_revision(root, target.relative_to(root).as_posix(), normalized, content, creating=False)
    observed, _history = publish_status_atom_revision(
        root, atom, target.relative_to(root).as_posix(), normalized, content,
        expected_bundle=status_bundle_snapshot(root, atom) if expected_bundle is None else expected_bundle)
    return observed


def prepare_draft_promotion(root: Path, atom: Atom, atom_id: str, frontmatter: str, content: str, *,
                            relative_path: str | None = None) -> tuple[Path, str, bytes]:
    """Derive exact identified output bytes without consuming the Draft carrier."""

    root = root.resolve()
    control = control_root(root)
    if atom.lifecycle != "draft" or atom.atom_id is not None:
        raise ToolError("draft-promotion-invalid", "only an ID-free Draft carrier can be promoted")
    marker = _draft_marker_identity(root, atom.path, atom.frontmatter)
    if marker is not None and marker.canonical_id is not None:
        raise ToolError("draft-promotion-marker-unsupported", "carried Draft markers require their admitted source-bound promotion effect")
    match = (re.fullmatch(rf"{re.escape(marker.value)}--(.+)", atom.filename) if marker is not None
             else re.fullmatch(r"([A-Za-z0-9]+-[A-Z]+)--(.+)", atom.filename))
    identity = re.fullmatch(r"([A-Za-z0-9]+-[A-Z]+)-(\d+)", atom_id)
    role_prefix = marker.value.removesuffix("-draft") if marker is not None else match.group(1) if match else None
    if match is None or identity is None or role_prefix != identity.group(1):
        raise ToolError("draft-promotion-invalid", "Draft filename and assigned identity do not share one role prefix")
    role_name = _role_directory(atom.path, control)
    if role_name is None:
        raise ToolError("archive-location-missing", "Draft has no content-role location")
    role = next(parent for parent in atom.path.parents if parent.name == role_name)
    summary = match.group(1) if marker is not None else match.group(2)
    separator = "-" if "--" in summary else "--"
    target = (role / f"{identity.group(1)}-{identity.group(2)}{separator}{summary}").resolve()
    if relative_path is not None:
        target = safe_path(root, relative_path)
    if target.exists() or atom_id_has_preserved_history_evidence(root, atom_id):
        raise ToolError("atom-id-collision", f"Atom ID already exists: {atom_id}")
    normalized = re.sub(r"(?m)^revision_lineage:[^\n]*(?:\n[ \t]+[^\n]*)*(?:\n|$)", "", _normalize_frontmatter(frontmatter))
    normalized = replace_frontmatter_scalar(normalized, "atom_id", atom_id)
    prepare_create_atom_revision(root, target.relative_to(root).as_posix(), normalized, content, creating=False)
    return target, normalized, render(normalized, content)


def prepare_native_fresh_draft_promotion(
    root: Path, atom: Atom, atom_id: str, *, relative_path: str | None = None,
) -> tuple[Path, str, bytes]:
    """Prepare one native fresh-Draft promotion without changing its Version or time."""

    frontmatter = replace_frontmatter_scalar(atom.frontmatter, "status", "Active")
    return prepare_draft_promotion(root, atom, atom_id, frontmatter, atom.content,
                                   relative_path=relative_path)


def promote_draft_atom(root: Path, atom: Atom, atom_id: str, frontmatter: str, content: str, *,
                       relative_path: str | None = None, expected_bundle: Mapping | None = None) -> Atom:
    """Write one identified output without a retained-history prerequisite."""

    root = root.resolve()
    target, normalized, _output = prepare_draft_promotion(root, atom, atom_id, frontmatter, content,
                                                        relative_path=relative_path)
    observed, _history = publish_status_atom_revision(
        root, atom, target.relative_to(root).as_posix(), normalized, content,
        expected_bundle=status_bundle_snapshot(root, atom) if expected_bundle is None else expected_bundle)
    return observed




def render(frontmatter: str, content: str) -> bytes:
    if not isinstance(content, str):
        raise ToolError("input-invalid", "content must be a string")
    return ("---\n" + frontmatter.rstrip("\n") + "\n---\n" + content).encode("utf-8")


def _validate_destination(root: Path, path: Path, *, filename_required: bool) -> None:
    control = control_root(root)
    if not _inside(path, control):
        raise ToolError("outside-control-root", f"destination is outside {control.relative_to(root)}: {path}")
    probe = path.parent if filename_required else path
    if not any(ROLE_DIRECTORY.fullmatch(part) for part in probe.relative_to(control).parts):
        raise ToolError("destination-not-atom-place", f"destination has no CAPRMEDIO content-role directory: {path}")


def _atomic_write(path: Path, data: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    descriptor, temporary_name = atomic_tempfile(path, "atom_operations")
    temporary = Path(temporary_name)
    try:
        with os.fdopen(descriptor, "wb") as handle:
            handle.write(data)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, path)
    except BaseException:
        temporary.unlink(missing_ok=True)
        raise


def _restore(snapshots: Mapping[Path, bytes | None]) -> None:
    for path, previous in reversed(list(snapshots.items())):
        if previous is None:
            path.unlink(missing_ok=True)
        else:
            _atomic_write(path, previous)


def run_search(root: Path, args: argparse.Namespace) -> dict[str, Any]:
    root = root.resolve()
    if getattr(args, "subject", None) is not None:
        from atom_subject_lookup import run_subject_search

        return run_subject_search(root, args)
    if (any(getattr(args, field, None) for field in ("subject_field", "subject_match", "content_role", "scope_unit"))
            or getattr(args, "subject_profile", None) is not None):
        raise ToolError("input-invalid", "Subject filters require --subject")
    atoms = scan_atoms(root, under=args.under, lifecycle=args.lifecycle or "all")
    if args.atom:
        selected = {atom.relative for atom in resolve_selectors(root, args.atom)}
        atoms = [atom for atom in atoms if atom.relative in selected]
    for query in args.query or []:
        needle = query.casefold()
        atoms = [atom for atom in atoms if needle in "\n".join((atom.relative, atom.frontmatter, atom.content)).casefold()]
    if args.limit is not None:
        atoms = atoms[:args.limit]
    return {"count": len(atoms), "atoms": [present(atom, args.view) for atom in atoms]}


def run_read(root: Path, args: argparse.Namespace) -> dict[str, Any]:
    root = root.resolve()
    atoms = resolve_selectors(root, args.atom)
    return {"count": len(atoms), "atoms": [present(atom, args.view) for atom in atoms]}


def run_create(root: Path, args: argparse.Namespace) -> dict[str, Any]:
    if not args.apply:
        return _run_create(root, args)
    with atom_identity_lock(root):
        return _run_create(root, args)


def _run_create(root: Path, args: argparse.Namespace) -> dict[str, Any]:
    root = root.resolve()
    plans: list[tuple[Path, bytes]] = []
    planned_ids: set[str] = set()
    for item in _items(_load_payload(args.input)):
        if "path" in item:
            if "directory" in item or "filename" in item:
                raise ToolError("input-invalid", "create item uses path or directory plus filename, not both")
            path = safe_path(root, str(item["path"]))
        else:
            directory = safe_path(root, str(item.get("directory", "")))
            filename = item.get("filename")
            if not isinstance(filename, str):
                raise ToolError("input-invalid", "create item requires filename")
            path = (directory / filename).resolve()
        _validate_destination(root, path, filename_required=True)
        frontmatter = _normalize_frontmatter(item.get("frontmatter", ""))
        _validate_revision_filename(path, frontmatter, creating=True)
        if path.exists() or any(existing == path for existing, _ in plans):
            raise ToolError("destination-collision", f"Atom destination already exists: {path.relative_to(root)}")
        match = ATOM_ID.search(path.name)
        atom_id = match.group(1) if match else None
        destination_lifecycle = _lifecycle(path, control_root(root))
        if destination_lifecycle == "draft":
            _draft_marker_identity(root, path, frontmatter)
            if atom_id is not None:
                raise ToolError("draft-has-stable-id", f"draft filename must not contain a stable Atom ID: {path.name}")
        if destination_lifecycle != "draft" and atom_id is None:
            raise ToolError("atom-id-required", f"non-draft Atom filename must contain a stable Atom ID: {path.name}")
        if atom_id and (atom_id in planned_ids or atom_id_has_preserved_history_evidence(root, atom_id)):
            raise ToolError("atom-id-collision", f"Atom ID already exists: {atom_id}")
        if atom_id:
            planned_ids.add(atom_id)
        frontmatter = _with_atom_id(frontmatter, atom_id, allow_draft_marker=destination_lifecycle == "draft")
        frontmatter = _revision(root, frontmatter, creating=True)
        plans.append((path, render(frontmatter, item.get("content", ""))))
    result = {"count": len(plans), "changes": [{"operation": "create", "path": p.relative_to(root).as_posix()} for p, _ in plans]}
    if not args.apply:
        return result
    snapshots = {path: None for path, _ in plans}
    try:
        for path, data in plans:
            _atomic_write(path, data)
    except BaseException:
        _restore(snapshots)
        raise
    return result


def run_update(root: Path, args: argparse.Namespace) -> dict[str, Any]:
    root = root.resolve()
    staging = getattr(args, "stage_preview", False)
    if staging and args.apply:
        raise ToolError("subject-stage-apply-rejected", "staged preview cannot be combined with --apply")
    payload = _load_payload(args.input)
    raw_items = _items(payload)
    subject_items = ["subject_patches" in item for item in raw_items]
    if any(subject_items):
        if not set(payload) <= {"atoms", "subject_profile"}:
            raise ToolError("input-invalid", "Subject-only root contains only atoms and optional subject_profile")
        if not all(subject_items):
            raise ToolError("input-invalid", "Subject-only and generic update items cannot be mixed")
        if args.apply:
            raise ToolError("subject-apply-not-admitted", "Subject-only updates are local previews, not an admitted live writer")
        from atom_subject_patch import preview_subject_patches

        profile = payload.get("subject_profile", "legacy")
        if not isinstance(profile, str) or profile not in {"legacy", "approved"}:
            raise ToolError("subject-profile-invalid", "subject_profile must be legacy or approved")

        if staging:
            from atom_subject_stage import stage_subject_preview

            return stage_subject_preview(root, raw_items, subject_profile=profile)
        return preview_subject_patches(root, raw_items, subject_profile=profile)
    if staging:
        raise ToolError("subject-stage-input-invalid", "staged preview requires Subject-only update items")
    if "subject_profile" in payload:
        raise ToolError("input-invalid", "subject_profile requires Subject-only update items")
    return _run_generic_update(root, args, raw_items)


def _run_generic_update(root: Path, args: argparse.Namespace, raw_items: list[dict[str, Any]]) -> dict[str, Any]:
    selectors = [item.get("selector") for item in raw_items]
    if any(not isinstance(selector, str) for selector in selectors):
        raise ToolError("input-invalid", "every update item requires selector")
    atoms = resolve_selectors(root, selectors)
    plans: list[tuple[Atom, bytes]] = []
    for item, atom in zip(raw_items, atoms, strict=True):
        if "frontmatter" not in item and "content" not in item:
            raise ToolError("input-invalid", "update item must provide frontmatter or content")
        frontmatter = _normalize_frontmatter(item["frontmatter"]) if "frontmatter" in item else atom.frontmatter
        if atom.lifecycle == "draft":
            _draft_marker_identity(root, atom.path, frontmatter)
        frontmatter = _with_atom_id(frontmatter, atom.atom_id, allow_draft_marker=atom.lifecycle == "draft")
        content = item["content"] if "content" in item else atom.content
        plans.append((atom, render(_revision(root, frontmatter, creating=False), content)))
    result = {"count": len(plans), "changes": [{"operation": "update", "path": atom.relative} for atom, _ in plans]}
    if not args.apply:
        return result
    snapshots = {atom.path: atom.path.read_bytes() for atom, _ in plans}
    try:
        for atom, data in plans:
            _atomic_write(atom.path, data)
    except BaseException:
        _restore(snapshots)
        raise
    return result


def _execute_move_plans(
    root: Path,
    plans: Sequence[tuple[Atom, Path]],
    *,
    operation: str,
    apply: bool,
) -> dict[str, Any]:
    targets = [target for _, target in plans]
    if len(set(targets)) != len(targets):
        raise ToolError("destination-collision", "more than one selected Atom resolves to the same destination")
    selected_sources = {atom.path for atom, _ in plans}
    for atom, target in plans:
        if target.exists() and target not in selected_sources:
            raise ToolError("destination-collision", f"destination already exists: {target.relative_to(root)}")
        if target == atom.path:
            raise ToolError(f"{operation}-noop", f"destination equals source: {atom.relative}")
    result = {"count": len(plans), "changes": [{"operation": operation, "from": atom.relative,
               "to": target.relative_to(root).as_posix()} for atom, target in plans]}
    if not apply:
        return result
    snapshots: dict[Path, bytes | None] = {}
    for atom, target in plans:
        snapshots.setdefault(atom.path, atom.path.read_bytes())
        snapshots.setdefault(target, target.read_bytes() if target.exists() else None)
    try:
        payloads = [(atom, target, atom.path.read_bytes()) for atom, target in plans]
        for _, target, data in payloads:
            _atomic_write(target, data)
        for atom, target, _ in payloads:
            if atom.path != target:
                atom.path.unlink()
    except BaseException:
        _restore(snapshots)
        raise
    return result


def run_move(root: Path, args: argparse.Namespace) -> dict[str, Any]:
    root = root.resolve()
    atoms = resolve_selectors(root, args.atom) if args.atom else []
    source: Path | None = None
    if args.from_path:
        source = safe_path(root, args.from_path, must_exist=True)
        known = {atom.relative for atom in atoms}
        atoms.extend(atom for atom in scan_atoms(root, under=args.from_path) if atom.relative not in known)
    if not atoms:
        raise ToolError("atom-selector-required", "move requires --atom or --from")
    destination = safe_path(root, args.to)
    _validate_destination(root, destination, filename_required=False)
    plans: list[tuple[Atom, Path]] = []
    for atom in atoms:
        target = destination / atom.filename
        if source is not None and _inside(atom.path, source) and not args.flatten:
            target = destination / atom.path.relative_to(source)
        target = target.resolve()
        _validate_destination(root, target, filename_required=True)
        target_lifecycle = _lifecycle(target, control_root(root))
        if target_lifecycle == "draft" and atom.atom_id is not None:
            raise ToolError("draft-has-stable-id", f"move would place a stable Atom ID in drafts: {atom.relative}")
        if target_lifecycle != "draft" and atom.atom_id is None:
            raise ToolError("atom-id-required", f"move would place an identity-less draft outside drafts: {atom.relative}")
        plans.append((atom, target))
    return _execute_move_plans(root, plans, operation="move", apply=args.apply)


def run_archive(root: Path, args: argparse.Namespace) -> dict[str, Any]:
    root = root.resolve()
    atoms = resolve_selectors(root, args.atom)
    control = control_root(root)
    plans: list[tuple[Atom, Path]] = []
    for atom in atoms:
        if atom.lifecycle != "active" or atom.atom_id is None:
            raise ToolError("atom-not-active", f"only active Atoms with stable identity can be archived: {atom.relative}")
        role_name = _role_directory(atom.path, control)
        if role_name is None:
            raise ToolError("archive-location-missing", f"Atom has no content-role archive location: {atom.relative}")
        role = next(parent for parent in atom.path.parents if role_name == parent.name)
        target = (role / "archive" / atom.filename).resolve()
        plans.append((atom, target))
    return _execute_move_plans(root, plans, operation="archive", apply=args.apply)


def run_promote(root: Path, args: argparse.Namespace) -> dict[str, Any]:
    if not args.apply:
        return _run_promote(root, args)
    with atom_identity_lock(root):
        return _run_promote(root, args)


_CARRIER_DESCRIPTOR_FIELDS = frozenset(
    {"atom_id", "path", "filename", "version", "digest", "lifecycle", "status", "updated_at", "content_role", "type"}
)


def _carrier_descriptor(atom: Atom) -> dict[str, Any]:
    return {
        "atom_id": atom.atom_id,
        "path": atom.relative,
        "filename": atom.filename,
        "version": atom_version(atom),
        "digest": atom_digest(atom),
        "lifecycle": atom.lifecycle,
        "status": frontmatter_scalar(atom.frontmatter, "status"),
        "updated_at": frontmatter_scalar(atom.frontmatter, "updated_at"),
        "content_role": frontmatter_scalar(atom.frontmatter, "content_role"),
        "type": frontmatter_scalar(atom.frontmatter, "type"),
    }


def _resolve_promotion_descriptor(root: Path, value: object, *, name: str, active: bool) -> Atom:
    if not isinstance(value, Mapping) or set(value) != _CARRIER_DESCRIPTOR_FIELDS:
        raise ToolError("carrier-fields-invalid", f"{name} must carry one complete carrier descriptor")
    if not isinstance(value["path"], str):
        raise ToolError("carrier-path-invalid", f"{name}.path must be a repository-relative string")
    atom = atom_from_path(root, safe_path(root, value["path"], must_exist=True))
    require_current_atom(root, atom)
    observed = _carrier_descriptor(atom)
    if any(value[field] != observed[field] for field in _CARRIER_DESCRIPTOR_FIELDS):
        raise ToolError("stale-carrier", f"{name} no longer matches the observed carrier")
    if active and atom.lifecycle != "active":
        raise ToolError("active-carrier-required", f"{name} must resolve one active carrier")
    return atom


def _promote_fresh_id(root: Path, atom: Atom, item: Mapping[str, Any], planned_ids: set[str]) -> tuple[Path, bytes]:
    if "target" in item or "canonical_target" in item or "proposed_version" in item:
        raise ToolError("canonical-target-unadmitted", "only existing Draft markers accept canonical target evidence")
    requested = item.get("atom_id")
    prefix = re.match(r"^(CA-[A-Z]+)--(.+)$", atom.filename)
    if not isinstance(requested, str) or re.fullmatch(r"CA-[A-Z]+-[0-9]{3,}", requested) is None:
        raise ToolError("atom-id-invalid", "promote item requires an Atom ID such as CA-R-343")
    if prefix is None or not requested.startswith(prefix.group(1) + "-"):
        raise ToolError("atom-id-role-mismatch", f"Atom ID does not match the draft content role: {requested}")
    if requested in planned_ids or atom_id_has_preserved_history_evidence(root, requested):
        raise ToolError("atom-id-collision", f"Atom ID already exists: {requested}")
    planned_ids.add(requested)
    target, _normalized, payload = prepare_native_fresh_draft_promotion(root, atom, requested)
    return target, payload


def _promote_role_marker_id(root: Path, atom: Atom, marker: DraftMarker, item: Mapping[str, Any],
                            planned_ids: set[str]) -> str:
    target = _resolve_promotion_descriptor(root, item.get("target"), name="target", active=False)
    if target.path != atom.path:
        raise ToolError("canonical-target-mismatch", "selector and target descriptor must name the same Draft carrier")
    if "canonical_target" in item or "proposed_version" in item:
        raise ToolError("canonical-target-unadmitted", "new-Atom Draft markers do not accept canonical target evidence")
    requested = item.get("atom_id")
    prefix = marker.value.removesuffix("-draft")
    if (not isinstance(requested, str) or re.fullmatch(r"CA-[A-Z]+-[0-9]{3,}", requested) is None
            or not requested.startswith(prefix + "-")):
        raise ToolError("atom-id-role-mismatch", f"Atom ID does not match the draft content role: {requested}")
    if requested in planned_ids or atom_id_has_preserved_history_evidence(root, requested):
        raise ToolError("atom-id-collision", f"Atom ID already exists: {requested}")
    planned_ids.add(requested)
    return requested


def _promote_existing_marker_binding(root: Path, atom: Atom, marker: DraftMarker,
                                     item: Mapping[str, Any]) -> ExistingDraftPromotion:
    target = _resolve_promotion_descriptor(root, item.get("target"), name="target", active=False)
    if target.path != atom.path or item.get("atom_id") != marker.canonical_id:
        raise ToolError("canonical-target-mismatch", "selector and atom_id must name the carried Draft marker")
    canonical_target = _resolve_promotion_descriptor(root, item.get("canonical_target"), name="canonical_target", active=False)
    return bind_existing_draft_promotion(root, atom, canonical_target, proposed_version=item.get("proposed_version"))


def _plan_promotion_item(root: Path, atom: Atom, item: Mapping[str, Any], planned_ids: set[str]) -> tuple[str, object]:
    if atom.lifecycle != "draft" or atom.atom_id is not None:
        raise ToolError("atom-not-draft", f"only identity-less drafts can be promoted: {atom.relative}")
    marker = _draft_marker_identity(root, atom.path, atom.frontmatter)
    if marker is None:
        return "fresh", _promote_fresh_id(root, atom, item, planned_ids)
    if marker.canonical_id is None:
        return "role", _promote_role_marker_id(root, atom, marker, item, planned_ids)
    return "existing", _promote_existing_marker_binding(root, atom, marker, item)


def _validate_promotion_plans(
    root: Path, plans: Sequence[tuple[Atom, Path, bytes]], existing: Sequence[object], role_drafts: Sequence[object],
) -> None:
    targets = [target for _, target, _ in plans]
    if len(set(targets)) != len(targets):
        raise ToolError("destination-collision", "more than one selected Atom resolves to the same destination")
    if any(target.exists() for _, target, _ in plans):
        raise ToolError("destination-collision", "a promotion destination already exists")
    if (existing or role_drafts) and (plans or len(existing) + len(role_drafts) != 1):
        raise ToolError("mixed-draft-promotion-batch-unadmitted", "existing-marker promotion accepts one independent Draft action per request")


def _promotion_result(root: Path, plans: Sequence[tuple[Atom, Path, bytes]],
                      existing: Sequence[tuple[Atom, ExistingDraftPromotion, dict[str, Any]]],
                      role_drafts: Sequence[tuple[Atom, str]]) -> dict[str, Any]:
    changes = [{"operation": "promote", "from": atom.relative, "to": target.relative_to(root).as_posix()}
               for atom, target, _ in plans]
    changes.extend({"operation": "no-op" if binding.no_op else "promote", "from": atom.relative,
                    "to": _existing_promotion_destination(root, binding.canonical_target, "Active"),
                    "canonical_target": binding.canonical_target.atom_id, "version": binding.proposed_version}
                   for atom, binding, _ in existing)
    changes.extend({"operation": "promote", "from": atom.relative, "atom_id": atom_id}
                   for atom, atom_id in role_drafts)
    return {"count": len(changes), "changes": changes}


def _apply_promotion_plans(root: Path, plans: Sequence[tuple[Atom, Path, bytes]],
                           existing: Sequence[tuple[Atom, ExistingDraftPromotion, dict[str, Any]]],
                           role_drafts: Sequence[tuple[Atom, str]]) -> None:
    if existing:
        atom, binding, item = existing[0]
        frontmatter = prepare_existing_draft_promotion_frontmatter(root, atom.frontmatter, binding, "Active")
        promote_existing_draft_atom(root, atom, binding, frontmatter, atom.content, requested_status="Active",
                                    expected_draft_digest=item["target"]["digest"],
                                    expected_canonical_digest=item["canonical_target"]["digest"])
        return
    if role_drafts:
        atom, atom_id = role_drafts[0]
        target, _normalized, payload = prepare_native_fresh_draft_promotion(root, atom, atom_id)
        plans = [(atom, target, payload)]
    snapshots: dict[Path, bytes | None] = {atom.path: atom.path.read_bytes() for atom, _, _ in plans}
    snapshots.update({target: None for _, target, _ in plans})
    try:
        for _, target, data in plans:
            _atomic_write(target, data)
        for atom, _, _ in plans:
            atom.path.unlink()
    except BaseException:
        _restore(snapshots)
        raise


def _run_promote(root: Path, args: argparse.Namespace) -> dict[str, Any]:
    root = root.resolve()
    raw_items = _items(_load_payload(args.input))
    selectors = [item.get("selector") for item in raw_items]
    if any(not isinstance(selector, str) for selector in selectors):
        raise ToolError("input-invalid", "every promote item requires selector")
    plans: list[tuple[Atom, Path, bytes]] = []
    existing: list[tuple[Atom, ExistingDraftPromotion, dict[str, Any]]] = []
    role_drafts: list[tuple[Atom, str]] = []
    planned_ids: set[str] = set()
    for item, atom in zip(raw_items, resolve_selectors(root, selectors), strict=True):
        kind, value = _plan_promotion_item(root, atom, item, planned_ids)
        if kind == "fresh":
            target, payload = value
            plans.append((atom, target, payload))
        elif kind == "role":
            role_drafts.append((atom, value))
        else:
            existing.append((atom, value, item))
    _validate_promotion_plans(root, plans, existing, role_drafts)
    result = _promotion_result(root, plans, existing, role_drafts)
    if args.apply:
        _apply_promotion_plans(root, plans, existing, role_drafts)
    return result


LOCAL_TIERS = {"standard": 0, "core": 1, "principle": 2}


def _filename_parts(atom: Atom, scope_prefix: str) -> tuple[list[str], str, list[str], str]:
    """Return Atom ID, descriptor tokens, and local tier from the current filename grammar."""

    if atom.atom_id is None:
        raise ToolError("atom-id-required", f"Atom has no stable identity: {atom.relative}")
    head, separator, _ = atom.filename.partition("--")
    if not separator:
        raise ToolError("filename-invalid", f"Atom filename has no summary separator: {atom.filename}")
    tokens = head.split("-")
    identifier = atom.atom_id.split("-")
    identifier_index = next(
        (index for index in range(len(tokens) - len(identifier) + 1)
         if tokens[index:index + len(identifier)] == identifier),
        None,
    )
    if identifier_index is None:
        raise ToolError("filename-invalid", f"Atom filename does not begin with its Atom ID: {atom.filename}")
    leading = tokens[:identifier_index]
    if leading and any(not token.isdigit() for token in leading):
        raise ToolError("filename-invalid", f"only an order token may precede an Atom ID: {atom.filename}")
    descriptor = tokens[identifier_index + len(identifier):]
    if scope_prefix:
        if not descriptor or descriptor[0] != scope_prefix:
            raise ToolError("filename-scope-mismatch", f"Atom filename does not begin with current Scope Unit name: {atom.filename}")
        descriptor = descriptor[1:]
    if descriptor and descriptor[0] in {"CORE", "PRINCIPLE"}:
        tier = descriptor.pop(0).lower()
    else:
        tier = "standard"
    if not descriptor:
        raise ToolError("filename-invalid", f"Atom filename has no Atom Type after its Scope Unit name: {atom.filename}")
    return leading, atom.atom_id, descriptor, tier


def _upgrade_filename(atom: Atom, *, current_prefix: str, target_prefix: str, target_tier: str) -> tuple[str, str]:
    leading, atom_id, descriptor, current_tier = _filename_parts(atom, current_prefix)
    if target_tier not in LOCAL_TIERS:
        raise ToolError("target-tier-invalid", "target tier must be principle, core, or standard")
    tokens = [*leading, *atom_id.split("-")]
    if target_prefix:
        tokens.append(target_prefix)
    if target_tier != "standard":
        tokens.append(target_tier.upper())
    tokens.extend(descriptor)
    summary = atom.filename.partition("--")[2]
    filename = "-".join(tokens) + "--" + summary
    if not CURRENT_FILENAME.fullmatch(filename):
        raise ToolError("filename-invalid", f"upgraded Atom filename does not follow current grammar: {filename}")
    return filename, current_tier


def _scope_graph(root: Path) -> tuple[dict[str, dict[str, Any]], dict[str, str]]:
    carrier = control_root(root) / "_projection" / "project_scope_unit_graph.projection.toml"
    try:
        document = tomllib.loads(carrier.read_text(encoding="utf-8"))
    except (OSError, tomllib.TOMLDecodeError) as error:
        raise ToolError("scope-projection-unavailable", f"cannot read current Scope Unit projection: {error}") from error
    raw_rows = document.get("scope_units")
    if not isinstance(raw_rows, list) or not raw_rows:
        raise ToolError("scope-projection-invalid", "Scope Unit projection contains no scope_units")
    control = control_root(root)
    rows: dict[str, dict[str, Any]] = {
        "caprmedio": {
            "key": "caprmedio",
            "name": "caprmedio",
            "prefix": "CA",
            "structural_parent": "",
            "full_authority_path": control,
        }
    }
    selectors: dict[str, str] = {"caprmedio": "caprmedio", "ca": "caprmedio"}
    parent_selectors: dict[str, str] = dict(selectors)
    pending: list[tuple[dict[str, Any], str, str, str, Path]] = []
    for raw in raw_rows:
        if not isinstance(raw, dict):
            raise ToolError("scope-projection-invalid", "Scope Unit row must be a table")
        name, authority = (raw.get(field) for field in ("name", "authority_path"))
        parent = raw.get("parent", raw.get("structural_parent", "caprmedio"))
        prefix = raw.get("unit_name", name)
        if not all(isinstance(value, str) for value in (name, prefix, parent, authority)):
            raise ToolError("scope-projection-invalid", "Scope Unit identity and authority fields must be strings")
        key = name
        if key in rows:
            raise ToolError("scope-projection-invalid", f"duplicate Scope Unit key: {key}")
        full_authority_path = (root / authority).resolve()
        if not _inside(full_authority_path, control):
            raise ToolError("scope-projection-invalid", f"Scope Unit authority path is outside Project carrier: {authority}")
        rows[key] = {**raw, "key": key, "prefix": prefix, "structural_parent": parent, "full_authority_path": full_authority_path}
        pending.append((raw, key, name, prefix, full_authority_path))
        for selector in {key, name, prefix, full_authority_path.name}:
            normalized = selector.casefold()
            if normalized in selectors and selectors[normalized] != key:
                raise ToolError("scope-projection-invalid", f"ambiguous Scope Unit selector: {selector}")
            selectors[normalized] = key
            parent_selectors[normalized] = key

    for raw, key, _, _, _ in pending:
        parent = raw.get("parent", raw.get("structural_parent", "caprmedio"))
        assert isinstance(parent, str)
        parent_key = parent_selectors.get(parent.casefold())
        if parent_key is None:
            raise ToolError("scope-projection-invalid", f"unknown Scope Unit parent: {parent}")
        rows[key]["structural_parent"] = parent_key

    return rows, selectors


def _scope_for_atom(atom: Atom, rows: Mapping[str, Mapping[str, Any]], control: Path) -> str:
    role_name = _role_directory(atom.path, control)
    scope_path = control if role_name is None else next(parent.parent for parent in atom.path.parents if parent.name == role_name)
    matches = [key for key, row in rows.items() if row["full_authority_path"] == scope_path]
    if len(matches) != 1:
        raise ToolError("atom-scope-unresolved", f"cannot resolve exactly one Scope Unit for Atom: {atom.relative}")
    return matches[0]


def _is_same_or_ancestor(rows: Mapping[str, Mapping[str, Any]], current: str, target: str) -> bool:
    cursor = current
    while True:
        if cursor == target:
            return True
        parent = str(rows[cursor]["structural_parent"])
        if not parent:
            return False
        cursor = parent


def run_upgrade(root: Path, args: argparse.Namespace) -> dict[str, Any]:
    root = root.resolve()
    raw_items = _items(_load_payload(args.input))
    selectors_raw = [item.get("selector") for item in raw_items]
    if any(not isinstance(selector, str) for selector in selectors_raw):
        raise ToolError("input-invalid", "every upgrade item requires selector")
    atoms = resolve_selectors(root, selectors_raw)
    rows, scope_selectors = _scope_graph(root)
    control = control_root(root)
    plans: list[tuple[Atom, Path, bytes, str, str, str, str]] = []
    for item, atom in zip(raw_items, atoms, strict=True):
        if atom.lifecycle != "active" or atom.atom_id is None:
            raise ToolError("atom-not-active", f"only active Atoms with stable identity can be upgraded: {atom.relative}")
        target_tier = item.get("tier")
        if not isinstance(target_tier, str) or target_tier not in LOCAL_TIERS:
            raise ToolError("target-tier-invalid", "every upgrade item requires explicit tier: principle, core, or standard")
        current_scope = _scope_for_atom(atom, rows, control)
        requested_scope = item.get("to_scope")
        if requested_scope is None:
            target_scope = current_scope
        elif isinstance(requested_scope, str) and requested_scope.casefold() in scope_selectors:
            target_scope = scope_selectors[requested_scope.casefold()]
        else:
            raise ToolError("target-scope-unresolved", f"unknown target Scope Unit: {requested_scope}")
        if not _is_same_or_ancestor(rows, current_scope, target_scope):
            raise ToolError("target-scope-not-upper", "target Scope Unit must be the current Scope Unit or one of its ancestors")
        current_prefix = "" if current_scope == "caprmedio" else str(rows[current_scope]["prefix"])
        target_prefix = "" if target_scope == "caprmedio" else str(rows[target_scope]["prefix"])
        filename, current_tier = _upgrade_filename(
            atom,
            current_prefix=current_prefix,
            target_prefix=target_prefix,
            target_tier=target_tier,
        )
        if target_scope == current_scope and LOCAL_TIERS[target_tier] <= LOCAL_TIERS[current_tier]:
            raise ToolError("target-tier-not-higher", f"target tier is not higher than current tier: {current_tier} -> {target_tier}")
        role_name = _role_directory(atom.path, control)
        if role_name is None:
            raise ToolError("upgrade-location-missing", f"Atom has no content-role location: {atom.relative}")
        target = (rows[target_scope]["full_authority_path"] / role_name / filename).resolve()
        _validate_destination(root, target, filename_required=True)
        frontmatter = _revision(root, atom.frontmatter, creating=False)
        plans.append((atom, target, render(frontmatter, atom.content), current_tier, target_tier, current_scope, target_scope))

    targets = [target for _, target, *_ in plans]
    if len(set(targets)) != len(targets):
        raise ToolError("destination-collision", "more than one upgraded Atom resolves to the same destination")
    selected_sources = {atom.path for atom, *_ in plans}
    for atom, target, *_ in plans:
        if target != atom.path and target.exists() and target not in selected_sources:
            raise ToolError("destination-collision", f"upgrade destination already exists: {target.relative_to(root)}")
    result = {"count": len(plans), "changes": [
        {"operation": "upgrade", "atom_id": atom.atom_id, "from": atom.relative,
         "to": target.relative_to(root).as_posix(), "from_tier": current_tier,
         "to_tier": target_tier, "from_scope": current_scope, "to_scope": target_scope}
        for atom, target, _, current_tier, target_tier, current_scope, target_scope in plans
    ]}
    if not args.apply:
        return result
    snapshots: dict[Path, bytes | None] = {}
    for atom, target, *_ in plans:
        snapshots.setdefault(atom.path, atom.path.read_bytes())
        snapshots.setdefault(target, target.read_bytes() if target.exists() else None)
    try:
        for _, target, data, *_ in plans:
            _atomic_write(target, data)
        for atom, target, *_ in plans:
            if atom.path != target:
                atom.path.unlink()
    except BaseException:
        _restore(snapshots)
        raise
    return result


def describe(tool_id: str) -> dict[str, Any]:
    kinds = {"ATOM_SEARCH": "finder", "ATOM_READ": "finder", "ATOM_CREATE": "doer",
             "ATOM_UPDATE": "doer", "ATOM_MOVE": "doer", "ATOM_ARCHIVE": "doer",
             "ATOM_PROMOTE": "doer", "ATOM_UPGRADE": "doer"}
    result = {"capability_id": tool_id, "kind": kinds[tool_id],
            "scope": "CAPRMEDIO Markdown Atom carriers under .caprmedio_caprmedio", "singular_and_bulk": True,
            "mutation_default": "dry-run" if kinds[tool_id] == "doer" else "read-only",
            "selector_forms": ["repository-relative path", "full filename", "filename stem", "Atom ID"]}
    if tool_id == "ATOM_SEARCH":
        result["subject_lookup"] = {
            "criterion": "--subject VALUE", "fields": ["governs", "depends_on", "both"],
            "matches": ["exact", "prefix", "suffix", "contains"], "prefix_boundaries": ["/", ":"],
            "profile_option": "--subject-profile", "profiles": ["legacy", "approved"],
            "default_profile": "legacy",
            "profile_prefix_boundaries": {"legacy": ["/", ":"], "approved": ["//", "/", ".", ":"]},
            "default_lifecycle": "active", "filters": ["under", "atom", "query", "content_role", "scope_unit", "lifecycle", "limit"],
            "output": ["source_root", "count", "occurrences", "diagnostics", "subject_profile", "subject_profile_evidence"],
            "mcp_binding": None,
        }
    elif tool_id == "ATOM_UPDATE":
        result["subject_preview"] = {
            "root_fields": ["atoms", "subject_profile (optional)"],
            "profiles": ["legacy", "approved"], "default_profile": "legacy",
            "output_evidence": ["subject_profile", "subject_profile_evidence"],
            "item_fields": ["selector", "expected", "subject_patches"],
            "expected_fields": ["atom_id", "version", "sha256"],
            "patch_fields": ["field", "old", "new"],
            "dependency_set_patch_fields": ["field", "operation", "old", "new"],
            "dependency_set_semantics": "depends_on replace_set; unordered unique strings; equal membership preserves source bytes",
            "selector": "exact repository-relative file path", "apply_supported": False,
            "staging_option": "--stage-preview", "staging_only": True,
            "mcp_binding": None,
        }
    return result


def parser(tool_id: str) -> argparse.ArgumentParser:
    result = argparse.ArgumentParser(prog=tool_id.lower().replace("_", "-"))
    result.add_argument("--repository", default=".")
    sub = result.add_subparsers(dest="command", required=True)
    sub.add_parser("describe")
    run = sub.add_parser("run")
    if tool_id == "ATOM_SEARCH":
        run.add_argument("--query", action="append")
        run.add_argument("--atom", action="append")
        run.add_argument("--under")
        run.add_argument("--lifecycle", choices=("all", "active", "draft", "archived", "done", "resolved", "canceled"))
        run.add_argument("--limit", type=int)
        run.add_argument("--view", choices=("metadata", "content", "both"), default="metadata")
        run.add_argument("--subject")
        run.add_argument("--subject-field", choices=("governs", "depends_on", "both"))
        run.add_argument("--subject-match", choices=("exact", "prefix", "suffix", "contains"))
        run.add_argument("--subject-profile", choices=("legacy", "approved"))
        run.add_argument("--content-role", action="append")
        run.add_argument("--scope-unit")
    elif tool_id == "ATOM_READ":
        run.add_argument("--atom", action="append", required=True)
        run.add_argument("--view", choices=("metadata", "content", "both"), default="both")
    elif tool_id in {"ATOM_CREATE", "ATOM_UPDATE", "ATOM_PROMOTE", "ATOM_UPGRADE"}:
        run.add_argument("--input", required=True)
        run.add_argument("--apply", action="store_true")
        if tool_id == "ATOM_UPDATE":
            run.add_argument("--stage-preview", action="store_true")
    elif tool_id == "ATOM_ARCHIVE":
        run.add_argument("--atom", action="append", required=True)
        run.add_argument("--apply", action="store_true")
    else:
        run.add_argument("--atom", action="append")
        run.add_argument("--from", dest="from_path")
        run.add_argument("--to", required=True)
        run.add_argument("--flatten", action="store_true")
        run.add_argument("--apply", action="store_true")
    return result


def cli(tool_id: str) -> int:
    args = parser(tool_id).parse_args()
    kind = "finder" if tool_id in {"ATOM_SEARCH", "ATOM_READ"} else "doer"
    mode = "describe" if args.command == "describe" else "apply" if getattr(args, "apply", False) else "staged-preview" if getattr(args, "stage_preview", False) else "read-only" if kind == "finder" else "dry-run"
    try:
        if (args.command == "run" and getattr(args, "apply", False)
                and tool_id in {"ATOM_CREATE", "ATOM_UPDATE"}):
            raise ToolError(
                "standalone-apply-not-admitted",
                f"{tool_id} --apply requires authorized project-local MCP delegation with a sealed Initiative action envelope",
            )
        root = resolve_repository(args.repository)
        if args.command == "describe":
            operation = describe(tool_id)
        else:
            runners = {"ATOM_SEARCH": run_search, "ATOM_READ": run_read, "ATOM_CREATE": run_create,
                       "ATOM_UPDATE": run_update, "ATOM_MOVE": run_move, "ATOM_ARCHIVE": run_archive,
                       "ATOM_PROMOTE": run_promote, "ATOM_UPGRADE": run_upgrade}
            operation = runners[tool_id](root, args)
        envelope = {"schema_version": SCHEMA_VERSION, "tool": {"capability_id": tool_id, "kind": kind},
                    "ok": True, "mode": mode, "diagnostics": [], "result": operation}
        print(canonical_json(envelope))
        return 0
    except (ToolError, OSError, UnicodeError) as error:
        diagnostic: dict[str, Any] = {"code": getattr(error, "code", "operation-failed"),
                                      "message": getattr(error, "message", str(error))}
        if getattr(error, "details", None):
            diagnostic["details"] = error.details
        envelope = {"schema_version": SCHEMA_VERSION, "tool": {"capability_id": tool_id, "kind": kind},
                    "ok": False, "mode": mode, "diagnostics": [diagnostic], "result": {}}
        print(canonical_json(envelope))
        return 2
