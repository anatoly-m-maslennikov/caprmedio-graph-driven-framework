"""Source-bound scalar, identity, and collection encodings."""

from __future__ import annotations

import re
from datetime import datetime
from typing import Any

from .authority import Record
from .check_support import Check, _integer, _string, _strings


def _draft_identity_context(metadata: Record, check: Check) -> tuple[str, str] | None:
    """Resolve the exact Project prefix and D378 role letter for Draft markers."""
    from .support_authority import exact_source, require_sources

    if not require_sources(check, ("CA-D-378",)):
        return None
    project = check.inputs.get("_project_identity", {})
    identity = project.get("identity", {}) if isinstance(project, dict) else {}
    prefix = identity.get("project_prefix") if isinstance(identity, dict) else None
    source = exact_source(check.inputs, "CA-D-378")
    text = source.get("text") if isinstance(source, dict) else None
    letters = dict(re.findall(r"([A-Za-z]+): ([A-Z])(?:,|\))", text)) if isinstance(text, str) else {}
    letter = letters.get(metadata.get("content_role"))
    if not _string(prefix) or not _string(letter):
        check.gap(
            "atom_id",
            "Draft identity requires the selected Project prefix and exact D378 Content Role letter.",
        )
        return None
    return prefix, letter


def _looks_like_draft_marker(value: object) -> bool:
    return isinstance(value, str) and (value.endswith("-draft") or value.endswith("@draft"))


def _draft_value(metadata: Record, check: Check) -> object | None:
    if "atom_id" not in metadata:
        check.forbid(metadata, "identifier")
        return None
    value = metadata.get("atom_id")
    if not _string(value):
        check.fail(
            "PROPERTY_TYPE",
            "atom_id",
            "A carried Draft atom_id must be a nonempty Draft marker string.",
        )
        return None
    return value


def _parse_draft_marker(
    value: object, context: tuple[str, str] | None, check: Check
) -> tuple[object | None, bool]:
    if context is None:
        return None, False
    prefix, letter = context
    try:
        from atom_operations import parse_draft_marker

        return parse_draft_marker(value, project_prefix=prefix, role_letter=letter), False
    except ValueError as error:
        check.fail("DRAFT_ID_INVALID", "atom_id", str(error))
        return None, True


def _check_draft_identity(metadata: Record, check: Check) -> None:
    value = _draft_value(metadata, check)
    if value is None:
        return
    context = _draft_identity_context(metadata, check)
    if context is None:
        if not _looks_like_draft_marker(value):
            check.fail(
                "DRAFT_ID_INVALID", "atom_id", "A carried Draft atom_id must use a D378 Draft-only marker."
            )
        return
    marker, invalid = _parse_draft_marker(value, context, check)
    if invalid:
        return
    if marker is None:
        check.fail(
            "DRAFT_ID_INVALID", "atom_id", "A carried Draft atom_id must use a D378 Draft-only marker."
        )
        return
    proposed_version = getattr(marker, "proposed_version", None)
    if proposed_version is not None and proposed_version != metadata.get("version"):
        check.fail(
            "DRAFT_ID_VERSION", "atom_id", "Draft marker proposed Version must equal the carried Version."
        )


def _check_non_draft_marker(metadata: Record, value: object, check: Check) -> None:
    if not _looks_like_draft_marker(value):
        return
    context = _draft_identity_context(metadata, check)
    marker, _ = _parse_draft_marker(value, context, check)
    if context is None or marker is not None:
        check.fail(
            "DRAFT_ID_STATUS",
            "atom_id",
            "Draft-only identity markers are forbidden on Current or Archived sources.",
        )


def _check_non_draft_identity(metadata: Record, check: Check) -> None:
    value = metadata.get("atom_id")
    check.require(metadata, "atom_id", _string)
    _check_non_draft_marker(metadata, value, check)
    check.forbid(metadata, "identifier")


def _common(metadata: Record, body: str, check: Check) -> None:
    del body
    for field in ("content_role", "current_scope_unit"):
        check.require(metadata, field, _string)
    role = metadata.get("content_role")
    if "type" in metadata:
        check.require(metadata, "type", _string)
    elif role not in ("Requirement", "Method", "Delivery"):
        check.require(metadata, "type", _string)
    check.require(metadata, "global_tier", _integer)
    if metadata.get("type") == "Goal" and metadata.get("claim_target_scope_unit") == "PROJECT":
        check.gap("local_tier", "Project Goal admission is required to decide Local Tier presence.")
    else:
        check.require(metadata, "local_tier", _string)
    for field in ("operators", "identifier", "summary", "claim"):
        check.forbid(metadata, field)


def _version(metadata: Record, body: str, check: Check) -> None:
    del body
    check.require(metadata, "version", lambda value: _integer(value) and value >= 1)


_TIMESTAMP = re.compile(
    r"\d{4}-\d{2}-\d{2}(?: \d{2}:\d{2}:\d{2}(?:\.\d+)? [+-]\d{4}|T\d{2}:\d{2}:\d{2}(?:\.\d+)?(?:Z|[+-]\d{2}:\d{2}))\Z"
)


def _timestamp_valid(value: Any) -> bool:
    if not isinstance(value, str) or _TIMESTAMP.fullmatch(value) is None:
        return False
    offset = re.search(r"[+-](\d{2}):?(\d{2})$", value)
    if offset and (int(offset[1]) > 23 or int(offset[2]) > 59):
        return False
    try:
        return datetime.fromisoformat(value.replace("Z", "+00:00")).utcoffset() is not None
    except ValueError:
        return False


def _updated(metadata: Record, body: str, check: Check) -> None:
    del body
    check.require(metadata, "updated_at", _timestamp_valid)


def _scalar(metadata: Record, body: str, check: Check) -> None:
    del body
    field = check.obligation.code.rsplit(".", 1)[1]
    check.require(metadata, field, _string)
    if field == "claim_target_scope_unit":
        check.forbid(metadata, "claim_scope")


def _identity(metadata: Record, body: str, check: Check) -> None:
    del body
    status = metadata.get("status")
    if not _string(status):
        check.gap("atom_id", "Identity applicability requires a resolved carried Status.")
        return
    if status == "Draft":
        _check_draft_identity(metadata, check)
    else:
        _check_non_draft_identity(metadata, check)


def _retired(metadata: Record, body: str, check: Check) -> None:
    del body
    for field in ("cce_version", "cce_form", "llm_session_ids"):
        if field in metadata:
            check.fail(
                "PROPERTY_RETIRED", field, "Retired Atom property is present: " + field + "."
            )


def _subjects(metadata: Record, body: str, check: Check) -> None:
    del body
    check.require(metadata, "subjects", lambda value: isinstance(value, dict))
    subjects = metadata.get("subjects")
    if not isinstance(subjects, dict):
        return
    if isinstance(subjects.get("governs"), dict):
        check.gap(
            "subjects.governs",
            "Legacy Subject encoding requires explicit migration-status authority.",
        )
        return
    check.require(subjects, "governs", _string)
    if not _strings(subjects.get("depends_on", [])):
        check.fail(
            "PROPERTY_TYPE",
            "subjects.depends_on",
            "Subject dependencies must be unique nonempty strings.",
        )
    if set(subjects) - {"governs", "depends_on"}:
        check.fail("PROPERTY_UNADMITTED", "subjects", "Subjects contains an unadmitted nested key.")


def _relations(metadata: Record, body: str, check: Check) -> None:
    del body
    relations = metadata.get("relations", {})
    if not isinstance(relations, dict):
        check.fail("PROPERTY_TYPE", "relations", "Relations must be a mapping.")
        return
    for kind, targets in relations.items():
        if not _string(kind) or not _strings(targets) or not targets:
            check.fail(
                "PROPERTY_TYPE",
                "relations",
                "Each Relation Kind must carry a nonempty collection of unique string targets.",
            )
