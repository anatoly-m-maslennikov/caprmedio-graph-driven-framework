"""Structured, read-only lookup for Atom ``subjects`` relations.

This module is intentionally separate from generic Atom text search.  Subject
hits are derived only from parsed YAML fields, never from carrier body text.
"""

from __future__ import annotations

import hashlib
import tomllib
from collections import Counter
from pathlib import Path
from typing import Any, Iterable

from atom_operations import ATOM_ID, ToolError, _inside, _lifecycle, control_root, safe_path
from VALIDATE_ATOMS.validate_atoms_workers.parsing import CarrierError, parse_carrier


_FIELDS = frozenset({"governs", "depends_on"})
_ROLES = frozenset({"Requirement", "Method", "Evaluation", "Delivery", "Operations", "Analysis", "Plan", "Concern"})
_ROLE_BY_ID_KIND = {"R": "Requirement", "M": "Method", "E": "Evaluation", "D": "Delivery", "O": "Operations",
                    "A": "Analysis", "P": "Plan", "C": "Concern"}


def _diagnostic(code: str, path: Path, message: str) -> dict[str, str]:
    return {"code": code, "path": path.as_posix(), "message": message}


def _request(args: Any) -> tuple[str, set[str], str, set[str], str | None]:
    subject = getattr(args, "subject", None)
    if not isinstance(subject, str) or not subject:
        raise ToolError("subject-required", "subject lookup requires one non-empty subject")
    field = getattr(args, "subject_field", None) or "both"
    if field == "both":
        fields = set(_FIELDS)
    elif field in _FIELDS:
        fields = {field}
    else:
        raise ToolError("subject-field-invalid", "subject_field must be governs, depends_on, or both")
    match = getattr(args, "subject_match", None) or "exact"
    if match not in {"exact", "prefix"}:
        raise ToolError("subject-match-invalid", "subject_match must be exact or prefix")
    requested_roles = getattr(args, "content_role", None) or []
    if not isinstance(requested_roles, (list, tuple)) or any(not isinstance(role, str) for role in requested_roles):
        raise ToolError("content-role-invalid", "content_role must be a list of role names")
    roles = set(requested_roles)
    unknown = sorted(roles - _ROLES)
    if unknown:
        raise ToolError("content-role-unknown", "unknown content role", {"roles": unknown})
    owner = getattr(args, "scope_unit", None)
    if owner is not None and (not isinstance(owner, str) or not owner):
        raise ToolError("scope-unit-invalid", "scope_unit must be one registered scope unit name")
    return subject, fields, match, roles, owner


def _owners(root: Path) -> dict[str, Path]:
    control = control_root(root)
    structure_path = control / "project_structure.toml"
    try:
        structure = tomllib.loads(structure_path.read_text(encoding="utf-8"))
    except (OSError, tomllib.TOMLDecodeError) as error:
        raise ToolError("project-structure-unavailable", "cannot read authoritative project_structure.toml") from error
    rows = structure.get("scope_units")
    if not isinstance(rows, list):
        raise ToolError("project-structure-invalid", "project_structure scope_units must be a list")
    result: dict[str, Path] = {}
    for row in rows:
        if not isinstance(row, dict):
            raise ToolError("project-structure-invalid", "project_structure scope_units must contain tables")
        name, raw_path = row.get("scope_unit_name"), row.get("authority_path")
        if not isinstance(name, str) or not name or not isinstance(raw_path, str) or not raw_path:
            raise ToolError("project-structure-invalid", "scope unit needs scope_unit_name and authority_path")
        declared = Path(raw_path)
        candidate = root / declared
        try:
            resolved = candidate.resolve()
        except OSError as error:
            raise ToolError("project-structure-invalid", "authority_path is unavailable") from error
        if declared.is_absolute() or ".." in declared.parts or not _inside(resolved, root) or resolved != candidate:
            raise ToolError("project-structure-invalid", "authority_path escapes or contains a symlink")
        if name in result:
            raise ToolError("project-structure-invalid", "scope unit names must be unique")
        result[name] = resolved
    return result


def _owner_for(path: Path, owners: dict[str, Path]) -> str | None:
    matches = [(owner_path, name) for name, owner_path in owners.items() if _inside(path, owner_path)]
    return max(matches, key=lambda item: len(item[0].parts))[1] if matches else None


def _subject_match(value: str, subject: str, mode: str) -> bool:
    return value == subject if mode == "exact" else value == subject or value.startswith(subject + "/") or value.startswith(subject + ":")


def _structured_subjects(metadata: dict[str, Any], fields: set[str]) -> Iterable[tuple[str, int | None, str]]:
    subjects = metadata.get("subjects")
    if not isinstance(subjects, dict):
        raise ValueError("subjects must be one mapping")
    value = subjects.get("governs")
    if not isinstance(value, str) or not value:
        raise ValueError("subjects.governs must be one non-empty scalar")
    dependencies = subjects.get("depends_on", [])
    if not isinstance(dependencies, list) or any(not isinstance(dependency, str) or not dependency for dependency in dependencies):
        raise ValueError("subjects.depends_on must be a list of non-empty scalars")
    if len(set(dependencies)) != len(dependencies):
        raise ValueError("subjects.depends_on must not contain duplicates")
    values: list[tuple[str, int | None, str]] = []
    if "governs" in fields:
        values.append(("governs", None, value))
    if "depends_on" in fields:
        values.extend(("depends_on", index, value) for index, value in enumerate(dependencies))
    return values


def _matches_query(relative: str, frontmatter: str, body: str, queries: Any) -> bool:
    for query in queries or []:
        if not isinstance(query, str):
            raise ToolError("query-invalid", "query must be text")
        if query.casefold() not in "\n".join((relative, frontmatter, body)).casefold():
            return False
    return True


def _validate_pre_traversal(args: Any) -> tuple[list[str], list[str], int | None]:
    atom_filter = getattr(args, "atom", None) or []
    if not isinstance(atom_filter, (list, tuple)) or any(
        not isinstance(value, str) or not value or "\x00" in value or ".." in Path(value).parts for value in atom_filter
    ):
        raise ToolError("atom-invalid", "atom must be a list of safe, non-empty selectors")
    queries = getattr(args, "query", None) or []
    if not isinstance(queries, (list, tuple)) or any(not isinstance(query, str) for query in queries):
        raise ToolError("query-invalid", "query must be text")
    limit = getattr(args, "limit", None)
    if limit is not None and (type(limit) is not int or limit < 0):
        raise ToolError("limit-invalid", "limit must be a non-negative integer")
    return list(atom_filter), list(queries), limit


def _safe_frontier(root: Path, under: str | None) -> Path:
    if under is None:
        return control_root(root)
    declared = Path(under)
    if not under or "\x00" in under:
        return safe_path(root, under, must_exist=True)
    # Establish the shared control-root boundary first.  ``safe_path`` resolves
    # aliases, so inspect the original lexical route afterwards to prevent an
    # absolute path inside the control tree from concealing a symlink hop.
    base = safe_path(root, under, must_exist=True)
    lexical = declared if declared.is_absolute() else root / declared
    try:
        relative = lexical.relative_to(root)
    except ValueError as error:
        raise ToolError("path-symlink", "under must not enter the Project through a symlink alias") from error
    probe = root
    for part in relative.parts:
        probe /= part
        if probe.is_symlink():
            raise ToolError("path-symlink", "under must not traverse a symlink")
    return base


def run_subject_search(root: Path, args: Any) -> dict[str, Any]:
    """Return pinned occurrences matching a structured subject relation."""

    root = Path(root).resolve()
    subject, fields, match_mode, roles, requested_owner = _request(args)
    atom_filter, queries, limit = _validate_pre_traversal(args)
    owners = _owners(root)
    if requested_owner is not None and requested_owner not in owners:
        raise ToolError("scope-unit-unknown", "scope_unit is not registered in project_structure", {"scope_unit": requested_owner})
    under = getattr(args, "under", None)
    base = _safe_frontier(root, under)
    lifecycle = getattr(args, "lifecycle", None) or "active"
    if lifecycle not in {"all", "active", "draft", "archived", "done", "resolved", "canceled"}:
        raise ToolError("lifecycle-invalid", "unsupported lifecycle")
    diagnostics: list[dict[str, str]] = []
    candidates = [base] if base.is_file() else sorted(base.rglob("*.md"), key=lambda path: path.as_posix())
    valid: list[tuple[Path, dict[str, Any], str, str, str]] = []
    control = control_root(root)
    for path in candidates:
        if "_projection" in path.relative_to(control).parts:
            continue
        # Lifecycle and requested content-role frontiers constrain the source
        # set before parsing: archived history is not an invalid active source.
        if lifecycle != "all" and _lifecycle(path, control) != lifecycle:
            continue
        filename_id = ATOM_ID.search(path.name)
        # A plain Markdown document is not an Atom candidate.  A filename
        # claiming a stable Atom identity is a candidate even if its metadata
        # is malformed or absent, so it receives a diagnostic below.
        if filename_id is None:
            continue
        filename_role = _ROLE_BY_ID_KIND[filename_id.group(1).split("-")[1]]
        if roles and filename_role not in roles:
            continue
        if path.is_symlink():
            diagnostics.append(_diagnostic("source-symlink", path, "source file is a symlink"))
            continue
        try:
            raw = path.read_bytes()
            parsed = parse_carrier(raw, path)
        except (OSError, UnicodeError, CarrierError) as error:
            diagnostics.append(_diagnostic("source-invalid", path, "carrier cannot be parsed"))
            continue
        metadata = parsed.metadata
        if "projection" in metadata:
            continue
        atom_id, version, status = metadata.get("atom_id"), metadata.get("version"), metadata.get("status")
        role, owner, updated_at = metadata.get("content_role"), metadata.get("current_scope_unit"), metadata.get("updated_at")
        # A Markdown document without an Atom identity is simply outside this
        # tool's domain.  Once an identity is asserted, incomplete metadata is
        # an invalid selected source and must not disappear silently.
        if not isinstance(atom_id, str) or ATOM_ID.fullmatch(atom_id) is None:
            diagnostics.append(_diagnostic("source-invalid", path, "filename-identified Atom lacks a valid atom_id"))
            continue
        if atom_id != filename_id.group(1):
            diagnostics.append(_diagnostic("source-invalid", path, "filename and atom_id disagree"))
            continue
        if (type(version) is not int or version < 1 or not isinstance(status, str) or not status
                or not isinstance(role, str) or role not in _ROLES or not isinstance(owner, str) or owner not in owners):
            diagnostics.append(_diagnostic("source-invalid", path, "Atom metadata is incomplete or invalid"))
            continue
        if role != filename_role:
            diagnostics.append(_diagnostic("source-invalid", path, "filename Atom ID kind and content_role disagree"))
            continue
        expected_owner = _owner_for(path.resolve(), owners)
        if expected_owner != owner:
            diagnostics.append(_diagnostic("owner-path-mismatch", path, "current_scope_unit disagrees with authority_path"))
            continue
        if not isinstance(updated_at, str) or not updated_at:
            diagnostics.append(_diagnostic("source-invalid", path, "Atom updated_at is required"))
            continue
        try:
            _structured_subjects(metadata, set())
        except ValueError as error:
            diagnostics.append(_diagnostic("subject-invalid", path, str(error)))
            continue
        valid.append((path, metadata, parsed.frontmatter, parsed.body, hashlib.sha256(raw).hexdigest()))
    original_counts = Counter(
        metadata["atom_id"] for path, metadata, *_ in valid if _lifecycle(path, control) not in {"archived", "draft"}
    )
    duplicate_ids = {atom_id for atom_id, count in original_counts.items() if count > 1}
    if duplicate_ids:
        for path, metadata, *_ in valid:
            if metadata["atom_id"] in duplicate_ids:
                diagnostics.append(_diagnostic("duplicate-original-id", path, "duplicate original atom_id"))
    occurrences: list[dict[str, Any]] = []
    for path, metadata, frontmatter, body, digest in valid:
        if metadata["atom_id"] in duplicate_ids or (lifecycle != "all" and _lifecycle(path, control) != lifecycle):
            continue
        if lifecycle == "active" and metadata["status"].casefold() != "active":
            continue
        if roles and metadata["content_role"] not in roles:
            continue
        if requested_owner is not None and metadata["current_scope_unit"] != requested_owner:
            continue
        relative = path.relative_to(root).as_posix()
        if atom_filter and not any(selector in {relative, path.name, path.stem, metadata["atom_id"]} for selector in atom_filter):
            continue
        if not _matches_query(relative, frontmatter, body, queries):
            continue
        subjects = _structured_subjects(metadata, fields)
        for field, index, value in subjects:
            if _subject_match(value, subject, match_mode):
                occurrences.append({"atom_id": metadata["atom_id"], "version": metadata["version"], "status": metadata["status"],
                                    "owner": metadata["current_scope_unit"], "current_scope_unit": metadata["current_scope_unit"],
                                    "relative_path": relative, "sha256": digest, "updated_at": metadata.get("updated_at"),
                                    "field": field, "index": index, "value": value,
                                    "source_pin": {"relative_path": relative, "sha256": digest}})
    field_order = {"governs": 0, "depends_on": 1}
    occurrences.sort(key=lambda item: (item["relative_path"], field_order[item["field"]], -1 if item["index"] is None else item["index"]))
    limited = limit is not None and len(occurrences) > limit
    if limit is not None:
        occurrences = occurrences[:limit]
    return {"source_root": base.relative_to(root).as_posix(), "count": len(occurrences), "occurrences": occurrences,
            "diagnostics": diagnostics, "coverage": "limited" if limited or diagnostics else "full"}
