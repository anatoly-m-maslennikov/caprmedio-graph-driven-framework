"""Source-bound scalar, identity, and collection encodings."""

from __future__ import annotations

import hashlib
import re
from datetime import datetime
from typing import Any

from subject_notation import SubjectNotationError, parse_subject_expression

from .authority import Record, _verified
from .check_support import Check, _integer, _string, _strings


_LEGACY_D378_SOURCES = frozenset({
    "d4e6f0569f81a54f434d060ea6e2a271dea51611a66a1afd0f6a10ca127c7562",
})


def _legacy_draft_identity_source(check: Check) -> Record | None:
    """Select the reviewed historical D378 revision required by D276 only."""
    rows = [
        row for row in check.inputs.get("sources", [])
        if row.get("binding", {}).get("atom_id") == "CA-D-378"
    ]
    if len(rows) != 1 or not _verified(rows[0], {}):
        check.gap("authority", "Missing or changed historical CA-D-378 authority for the D276 profile.")
        return None
    binding = rows[0]["binding"]
    if binding.get("sha256") not in _LEGACY_D378_SOURCES or binding.get("version") != 16:
        check.gap("authority", "The D276 profile requires its reviewed historical CA-D-378 revision.")
        return None
    return rows[0]


def _draft_identity_context(metadata: Record, check: Check) -> tuple[str, str] | None:
    """Resolve the exact Project prefix and D378 role letter for Draft markers."""
    from .support_authority import exact_source

    project = check.inputs.get("_project_identity", {})
    identity = project.get("identity", {}) if isinstance(project, dict) else {}
    prefix = identity.get("project_prefix") if isinstance(identity, dict) else None
    source = (
        _legacy_draft_identity_source(check)
        if _selected_encoding_profile(check) == "legacy"
        else exact_source(check.inputs, "CA-D-378")
    )
    if source is None:
        check.gap("authority", "Missing or changed supporting authority: CA-D-378.")
        return None
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


def _selected_encoding_profile(check: Check) -> str | None:
    rows = [
        row for row in check.inputs.get("sources", [])
        if row.get("binding", {}).get("atom_id") in {"CA-D-276", "CA-D-657"}
    ]
    if len(rows) != 1 or not _verified(rows[0], {}):
        return None
    return reviewed_encoding_profile(rows[0])


def _current_draft_contract(check: Check) -> bool:
    from .support_authority import exact_source, matches_source_pin, require_sources, support_sources

    if not require_sources(check, ("CA-D-378",)):
        return False
    source = exact_source(check.inputs, "CA-D-378")
    if source is None or not matches_source_pin(source, support_sources().get("CA-D-378", {})):
        check.gap("authority", "Missing or changed supporting authority: CA-D-378.")
        return False
    text = source.get("text") if isinstance(source, dict) else None
    if not isinstance(text, str) or (
        "Every Draft carries its base canonical ID in the Header" not in text
        or "<canonical-ID>@<version>-draft" not in text
    ):
        check.gap("atom_id", "Selected Draft identity authority does not settle the Current canonical-ID contract.")
        return False
    return True


def _check_current_draft_identity(metadata: Record, check: Check) -> None:
    """Apply D378's ordinary Current Draft identity; packet drafts stay external."""
    if not _current_draft_contract(check):
        return
    value = metadata.get("atom_id")
    check.require(metadata, "atom_id", _string)
    if not _string(value):
        return
    project = check.inputs.get("_project_identity", {})
    identity = project.get("identity", {}) if isinstance(project, dict) else {}
    prefix = identity.get("project_prefix") if isinstance(identity, dict) else None
    role = metadata.get("role")
    try:
        from atom_operations import parse_draft_marker
    except ImportError:
        check.gap("atom_id", "Current Draft canonical-ID parser is unavailable.")
        return
    if (
        not _string(prefix)
        or not _string(role)
        or prefix != prefix.upper()
    ):
        check.fail(
            "DRAFT_ID_INVALID",
            "atom_id",
            "An ordinary Current Draft must carry one canonical allocated Atom ID.",
        )
        return
    try:
        # The shared marker parser owns the project-prefix-aware canonical
        # identity grammar.  A Current Header carries its base ID, so parse
        # the equivalent version-qualified marker only for grammar checking.
        marker = parse_draft_marker(
            f"{value}@1-draft", project_prefix=prefix, role_letter=role[0].upper()
        )
    except ValueError:
        marker = None
    if marker is None or marker.canonical_id != value:
        check.fail(
            "DRAFT_ID_INVALID",
            "atom_id",
            "An ordinary Current Draft must carry one canonical allocated Atom ID.",
        )


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
    profile = _selected_encoding_profile(check)
    if profile == "current":
        # D657's Subjects-only marker is admitted by its separately pinned
        # batch-review flow, never by a standalone carrier.
        _check_current_draft_identity(metadata, check)
        return
    if profile != "legacy":
        check.gap(
            "atom_id",
            "Draft identity requires exactly one reviewed Current or legacy encoding profile.",
        )
        return
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


_ENCODING_PROFILES = {
    "CA-D-276": "legacy",
}

# This is the reviewed D657 Claim from the proposed Current carrier, not a
# source-file pin.  The locator binds the observed bytes and this marker keeps
# a changed governing Claim from inheriting a historical adapter.
_D657_CURRENT_CLAIM = "5d4d963bc139bb72920e04272b2f019687bf0d1f13e9021792c989dc0c609ae4"


def _claim_digest(text: object) -> str | None:
    if not isinstance(text, str):
        return None
    body = text.split("---", 2)[-1]
    match = re.search(r"(?ms)^## Claim\n(.*?)(?=^## |\Z)", body)
    if match is None:
        return None
    return hashlib.sha256(match[1].strip().encode("utf-8")).hexdigest()


def reviewed_encoding_profile(row: Record) -> str | None:
    if not _verified(row, {}):
        return None
    # The locator verifies observed source bytes; this additional reviewed
    # Claim marker prevents an evolved governing contract from reusing this adapter.
    identifier = row["binding"]["atom_id"]
    if identifier == "CA-D-657" and _claim_digest(row.get("text")) == _D657_CURRENT_CLAIM:
        return "current"
    return _ENCODING_PROFILES.get(identifier)


def encoding_authority(check: Check) -> tuple[str, Record] | None:
    """Bind the reviewed encoding contract, not an alias between retired and Current IDs."""
    rows = [row for row in check.inputs.get("sources", [])
            if row.get("binding", {}).get("atom_id") in {"CA-D-276", "CA-D-657"}]
    if len(rows) == 1 and _verified(rows[0], {}):
        row = rows[0]
        profile = reviewed_encoding_profile(row)
        if profile is not None:
            return profile, row
    elif not rows:
        bound = [row for row in check.context.bindings if row.get("atom_id") == "CA-D-276"]
        if len(bound) == 1 and bound[0].get("sha256") == "052efd2454be5fe51e60a57fafbc7b767d87bba4a37272615c95b2648583ac02":
            return "legacy", {"binding": bound[0]}
    check.gap("frontmatter", "Exactly one verified reviewed frontmatter encoding authority is required.")
    return None


def _current_common(metadata: Record, check: Check) -> None:
    raw = check.inputs.get("_raw_metadata", metadata)
    raw = raw if isinstance(raw, dict) else metadata
    for field in ("role", "form"):
        check.require(raw, field, _string)
    check.require(raw, "tier", _integer)
    if raw.get("form") == "Project Goal":
        check.gap("tier", "Current Project Goal Tier needs its verified ownership and Tier authority.")
    elif _integer(raw.get("tier")) and raw["tier"] < 0:
        check.fail("PROPERTY_DOMAIN", "tier", "An ordinary Current Atom Tier must be nonnegative.")
    for field in ("label", "tier_label"):
        if field in raw:
            check.require(raw, field, _string)
    if "tier_label" in raw:
        check.gap("tier_label", "An explicit Tier Label requires its current governed numeric-to-label mapping.")
    for field in (
        "author", "local_tier", "global_tier", "operators", "identifier", "summary", "claim",
        "autonomous_confidence_threshold", "implementation_retry_limit",
    ):
        check.forbid(raw, field)
    for field in ("current_scope_unit", "claim_target_scope_unit"):
        if field in raw:
            check.gap(
                field,
                "Current scope compatibility data needs an explicit selected migration disposition.",
            )


def _common(metadata: Record, body: str, check: Check) -> None:
    del body
    authority = encoding_authority(check)
    if authority is None:
        return
    if authority[0] == "current":
        _current_common(metadata, check)
        return
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


def _current_subjects(subjects: Record, check: Check) -> None:
    check.require(subjects, "active", _string)
    if not _strings(subjects.get("passive", [])):
        check.fail(
            "PROPERTY_TYPE",
            "subjects.passive",
            "Subject dependencies must be unique nonempty strings.",
        )
    values = [("subjects.active", subjects.get("active"))]
    passive = subjects.get("passive", [])
    if isinstance(passive, list):
        values.extend(("subjects.passive", value) for value in passive)
    for field, value in values:
        if _string(value):
            try:
                parse_subject_expression(value, subject_profile="approved")
            except SubjectNotationError as error:
                check.fail("SUBJECT_INVALID", field, str(error))
    if set(subjects) - {"active", "passive", "governs", "depends_on"}:
        check.fail("PROPERTY_UNADMITTED", "subjects", "Subjects contains an unadmitted nested key.")


def _subjects(metadata: Record, body: str, check: Check) -> None:
    del body
    inputs = getattr(check, "inputs", {})
    current = (
        isinstance(inputs, dict)
        and any(row.get("binding", {}).get("atom_id") == "CA-D-657" for row in inputs.get("sources", []))
    )
    authority = encoding_authority(check) if current else None
    raw = inputs.get("_raw_metadata", metadata) if isinstance(inputs, dict) else metadata
    raw = raw if isinstance(raw, dict) else metadata
    check.require(raw, "subjects", lambda value: isinstance(value, dict))
    subjects = raw.get("subjects")
    if not isinstance(subjects, dict):
        return
    if authority is not None and authority[0] == "current":
        _current_subjects(subjects, check)
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
    values = [("subjects.governs", subjects.get("governs"))]
    dependencies = subjects.get("depends_on", [])
    if isinstance(dependencies, list):
        values.extend(("subjects.depends_on", value) for value in dependencies)
    for field, value in values:
        if _string(value):
            try:
                parse_subject_expression(value, subject_profile="approved")
            except SubjectNotationError as error:
                check.fail("SUBJECT_INVALID", field, str(error))
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
