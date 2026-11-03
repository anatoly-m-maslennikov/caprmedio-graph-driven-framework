"""Fence-aware checks for named Atom body Properties."""

from __future__ import annotations

import hashlib
import re
from dataclasses import replace

from .authority import Record, _verified
from .check_support import Check, _plan
from .support_authority import require_sources
from subject_notation import get_profile


GRAPH_RULE_SOURCES = (
    "CA-R-2001", "CA-D-637", "CA-R-1996",
    *(source.atom_id for source in get_profile("approved").grammar_pins),
)


def is_graph_rule(metadata: Record) -> bool:
    return metadata.get("content_role") == "Requirement" and metadata.get("type") == "Graph Rule"


# Ordinary role layouts; formal Graph Rules use the source-bound exception below.
ROLE_SECTIONS = {
    "Requirement": ("Scope", "Claim", "Details"),
    "Method": ("Scope", "Claim", "Details"),
    "Evaluation": ("Scope", "Claim", "Details"),
    "Delivery": ("Scope", "Claim", "Details"),
    "Analysis": ("Question", "Scope", "Approach", "Results", "TLDR"),
    "Concern": ("Concern", "Evidences", "Blast radius"),
    "Plan": ("Objective", "Details"),
    "Operations": ("Operation", "Details"),
}


_RMED = frozenset({"Requirement", "Method", "Evaluation", "Delivery"})
# Reviewed D479 Claims, bound to the actually supplied source bytes below.
_LAYOUT_CLAIMS = {
    "41b58fe9fef47bbd787d612787611a59314965c0928b19c3cb9a8f21ded2f4c3": "legacy",
    "64f422cfcd6ea14a067c046caf3af786ae083d07d4e549d71d36fdc68f408bcc": "rmed_siblings",
    "f1ae7821f1e70d211d27569a86f9c8eaac400ca2a894831461f8643d12514dc2": "claim_children",
}
_LEGACY_LAYOUT_SOURCES = frozenset({
    "0819f8433cde89484e21a200466504a9fdcad31b58958c777a761637fbb45ff1",
    "427e309ef7ea9c49a4ba168cc1420df015366544ff0746b27a98ab39a8ab7feb",
})
_RMED_PROPERTIES = ("Summary", "Claim scope", "Claim", "Semantics", "Details")
_RELATION_TYPE_CLAIMS = frozenset({
    "a860a0d55a53a6253f9fa9f1848096b925df860ca6b91c553183506277f0769a",
    "4d9d384928ce49dcb7ca2d70692b11ff31b561a9ad905b170d012e4f2e8df907",
})


def _relation_notation_contract(check: Check) -> bool:
    """Bind the Type's own registered body Property, not an arbitrary extra heading."""
    from .check_schema_extended import type_definition_coordinate

    rows = [row for row in check.inputs.get("sources", [])
            if row.get("binding", {}).get("atom_id") == "CA-R-2228"]
    if len(rows) == 1 and type_definition_coordinate(rows[0]) == ("Requirement", "Relation Definition"):
        body = rows[0]["text"].split("---", 2)[-1]
        headings, lines = _headings(body), body.splitlines()
        claims = [row for row in headings if row[:2] == (2, "Claim")]
        if len(claims) == 1:
            start = claims[0][2]
            end = next((row[2] for row in headings if row[2] > start and row[0] <= 2), len(lines))
            claim = "\n".join(lines[start + 1:end]).strip()
            if hashlib.sha256(claim.encode()).hexdigest() in _RELATION_TYPE_CLAIMS:
                binding = rows[0]["binding"]
                if binding not in check.obligation.authority:
                    check.obligation = replace(check.obligation, authority=[*check.obligation.authority, binding])
                return True
    check.gap("notation_for_subject", "The loaded Relation Definition Type has no reviewed body-Property adapter.")
    return False


def body_layout(check: Check) -> str | None:
    """Recognize only reviewed D479 Claims, never layout from a Version number."""
    sources = [row for row in check.inputs.get("sources", [])
               if row.get("binding", {}).get("atom_id") == "CA-D-479"]
    if len(sources) == 1 and _verified(sources[0], {}):
        text = sources[0]["text"].split("---", 2)[-1]
        headings, lines = _headings(text), text.splitlines()
        claims = [row for row in headings if row[:2] == (2, "Claim")]
        if len(claims) == 1:
            start = claims[0][2]
            end = next((row[2] for row in headings if row[2] > start and row[0] <= 2), len(lines))
            claim = "\n".join(lines[start + 1:end]).strip()
            layout = _LAYOUT_CLAIMS.get(hashlib.sha256(claim.encode("utf-8")).hexdigest())
            if layout is not None:
                return layout
    elif not sources:
        # Older facade callers retain already-verified historical bindings only.
        bound = [row for row in check.context.bindings if row.get("atom_id") == "CA-D-479"]
        if len(bound) == 1 and bound[0].get("sha256") in _LEGACY_LAYOUT_SOURCES:
            return "legacy"
    check.gap("body", "The exact loaded CA-D-479 Claim has no reviewed body-layout adapter.")
    return None


def role_sections(metadata: Record, check: Check) -> list[tuple[int, str]] | None:
    role = metadata.get("content_role")
    if not isinstance(role, str) or role not in ROLE_SECTIONS:
        check.gap(
            "content_role",
            "Body layout needs a carried Content Role with a supported section contract.",
        )
        return None
    layout = body_layout(check)
    if layout is None:
        return None
    if role in _RMED and layout in {"rmed_siblings", "claim_children"}:
        properties = [(2, name) for name in _RMED_PROPERTIES if layout != "claim_children" or name != "Claim scope"]
        if role == "Requirement" and metadata.get("type") == "Relation Definition":
            if not _relation_notation_contract(check):
                return None
            properties.append((2, "Notation for subject"))
        return properties
    if is_graph_rule(metadata):
        if not require_sources(check, GRAPH_RULE_SOURCES):
            return None
        return [(1, "Summary")]
    return [(1, "Summary"), *((2, name) for name in ROLE_SECTIONS[role])]


def _unfenced_lines(body: str) -> list[tuple[int, str]]:
    result = []
    fence: tuple[str, int] | None = None
    for index, line in enumerate(body.splitlines()):
        marker = re.match(r"^ {0,3}(`{3,}|~{3,})(.*)$", line)
        if marker:
            token = marker[1]
            if fence is None:
                fence = (token[0], len(token))
            elif token[0] == fence[0] and len(token) >= fence[1] and not marker[2].strip():
                fence = None
            continue
        if fence is None:
            result.append((index, line))
    return result


def _headings(body: str) -> list[tuple[int, str, int]]:
    headings = []
    for index, line in _unfenced_lines(body):
        heading = re.match(r"^(#{1,6}) (.+)$", line)
        if heading:
            headings.append((len(heading[1]), heading[2], index))
    return headings


def _claim_model_headings(body: str, registered: list[tuple[int, str]]) -> list[tuple[int, str, int]]:
    """Treat undeclared headings inside Prose Claim as Markdown, not properties."""
    result = []
    in_prose = False
    in_claim = False
    for row in _headings(body):
        level, title, _ = row
        if in_prose and (level, title) not in registered and not (
            level == 3 and title in {"Formal Claim", "Prose Claim"}
        ):
            continue
        if (level, title) in registered:
            in_claim = (level, title) == (2, "Claim")
            in_prose = False
        elif in_claim and (level, title) == (3, "Prose Claim"):
            in_prose = True
        elif in_claim and (level, title) == (3, "Formal Claim"):
            in_prose = False
        result.append(row)
    return result


def _sections(body: str, check: Check, required: list[tuple[int, str]]) -> None:
    headings = _headings(body)
    properties = [(level, title, index) for level, title, index in headings if level <= 2]
    positions = []
    for level, title in required:
        found = [
            index
            for found_level, found_title, index in properties
            if (found_level, found_title) == (level, title)
        ]
        if len(found) != 1:
            check.fail(
                "BODY_SECTION",
                title,
                "Required body section must occur exactly once: " + "#" * level + " " + title + ".",
            )
        else:
            positions.append(found[0])
    if positions != sorted(positions):
        check.fail("BODY_SECTION", "body", "Required body sections are out of order.")
    # Missing/duplicate Summary already has a cardinality diagnostic. Placement
    # is independently actionable only when exactly one Summary exists.
    summaries = [row for row in properties if row[:2] == (1, "Summary")]
    if len(summaries) == 1 and properties[0][:2] != (1, "Summary"):
        check.fail(
            "BODY_SECTION", "Summary", "Main Content must start with the literal # Summary heading."
        )
    _section_values(body, properties, required, check)


def _section_values(
    body: str, properties: list[tuple[int, str, int]], required: list[tuple[int, str]], check: Check
) -> None:
    lines = body.splitlines()
    if properties and any(line.strip() for line in lines[: properties[0][2]]):
        check.fail("BODY_SECTION", "body", "Main Content precedes the Summary heading.")
    for position, (level, title, index) in enumerate(properties):
        if (level, title) not in required:
            continue
        end = next(
            (row[2] for row in properties[position + 1 :] if row[0] <= level or title == "Summary"),
            len(lines),
        )
        if title != "Details" and not any(line.strip() for line in lines[index + 1 : end]):
            check.fail("BODY_SECTION", title, "Body Property value is empty: " + title + ".")


def _body_keys(headings: list[tuple[int, str, int]], check: Check) -> None:
    stack: list[tuple[int, tuple[str, ...]]] = []
    keys = set()
    for level, title, _ in headings:
        while stack and stack[-1][0] >= level:
            stack.pop()
        key = re.sub(r"[^\w-]", "", title.lower().replace(" ", "_"))
        path = (*(stack[-1][1] if stack else ()), key)
        if not key or path in keys:
            check.fail("BODY_SECTION", title, "Body Property key is empty or duplicated under the same parent.")
        keys.add(path)
        stack.append((level, path))


def _formal_expression(lines: list[str], *, allow_empty: bool = False) -> bool:
    content = "\n".join(lines).strip().splitlines()
    if len(content) < (2 if allow_empty else 3):
        return False
    opening = re.fullmatch(r" {0,3}(`{3,}|~{3,})[^\n]*", content[0])
    closing = re.fullmatch(r" {0,3}(`{3,}|~{3,})[ \t]*", content[-1])
    return bool(opening and closing and opening[1][0] == closing[1][0]
                and len(closing[1]) >= len(opening[1])
                and (allow_empty or any(line.strip() for line in content[1:-1]))
                and not any(re.match(r"^ {0,3}(?:`{3,}|~{3,})", line) for line in content[1:-1]))


def _rmed_formal(body: str, headings: list[tuple[int, str, int]], role: str, check: Check) -> None:
    lines = body.splitlines()
    for level, title, start in headings:
        if title.lower().replace(" ", "_") != "formal_claim":
            continue
        parent = next((row for row in reversed(headings) if row[2] < start and row[0] < level), None)
        end = next((row[2] for row in headings if row[2] > start and row[0] <= level), len(lines))
        if (role != "Requirement" or level != 3 or title != "Formal claim"
                or parent is None or parent[:2] != (2, "Claim")
                or not _formal_expression(lines[start + 1:end])):
            check.fail("BODY_SECTION", title, "Formal claim is one fenced expression directly under a Requirement Claim.")


def _rmed_values(body: str, headings: list[tuple[int, str, int]],
                 properties: list[tuple[int, str, int]], check: Check) -> None:
    lines = body.splitlines()
    unfenced = _unfenced_lines(body)
    for _, title, start in properties:
        if title not in {"Summary", "Claim"}:
            continue
        end = next((row[2] for row in headings if row[2] > start), len(lines))
        if not any(line.strip() for index, line in unfenced if start < index < end):
            check.fail("BODY_SECTION", title, "Required direct body Property prose is empty.")
    for _, title, start in properties:
        if title not in {"Claim scope", "Semantics", "Details"}:
            continue
        end = next((row[2] for row in properties if row[2] > start), len(lines))
        if not any(line.strip() for line in lines[start + 1:end]):
            check.fail("BODY_SECTION", title, "Absent optional Properties must be omitted instead of empty placeholders.")

def _rmed_sections(body: str, role: str, check: Check, registered: list[tuple[int, str]]) -> None:
    headings = _headings(body)
    properties = [row for row in headings if row[0] <= 2]
    required = [(2, "Summary"), (2, "Claim")]
    _sections(body, check, required)
    if properties and properties[0][:2] != (2, "Summary"):
        check.fail("BODY_SECTION", "Summary", "RMED Main Content must start with literal ## Summary.")
    positions = []
    for level, title, _ in properties:
        if (level, title) not in registered:
            check.fail("BODY_SECTION", title, "Unregistered RMED body Property heading.")
        elif title in _RMED_PROPERTIES:
            positions.append(_RMED_PROPERTIES.index(title))
        elif title == "Notation for subject":
            start = next(row[2] for row in properties if row[1] == title)
            end = next((row[2] for row in headings if row[2] > start and row[0] <= 2), len(body.splitlines()))
            if not _formal_expression(body.splitlines()[start + 1:end], allow_empty=True):
                check.fail("BODY_SECTION", title, "Notation for subject must contain one complete fenced String value.")
    if positions != sorted(set(positions)):
        check.fail("BODY_SECTION", "body", "RMED sibling Properties must be unique and in registered order.")
    if (2, "Notation for subject") in registered:
        for level, title, _ in headings:
            if title == "Notation for subject" and level != 2:
                check.fail("BODY_SECTION", title, "The registered Notation for subject Property must be a level-two section.")
    _rmed_values(body, headings, properties, check)
    _body_keys(headings, check)
    _rmed_formal(body, headings, role, check)


def _claim_children(body: str, check: Check, registered: list[tuple[int, str]]) -> None:
    headings, lines = _claim_model_headings(body, registered), body.splitlines()
    properties = [row for row in headings if row[0] <= 2]
    model_indices = {row[2] for row in headings}
    masked = "\n".join(line if index in model_indices or not re.match(r"^#{1,6} ", line)
                       else " " + line for index, line in enumerate(lines))
    _sections(masked, check, [(2, "Summary"), (2, "Claim")])
    if properties and properties[0][:2] != (2, "Summary"):
        check.fail("BODY_SECTION", "Summary", "Main Content must start with literal ## Summary.")
    order = [name for _, name in registered]
    positions = []
    for _, title, start in properties:
        if (2, title) not in registered:
            check.fail("BODY_SECTION", title, "Unregistered body Property heading.")
        else:
            positions.append(order.index(title))
        if title in {"Semantics", "Details"}:
            end = next((row[2] for row in properties if row[2] > start), len(lines))
            if not any(line.strip() for line in lines[start + 1:end]):
                check.fail("BODY_SECTION", title, "Empty optional Properties must be omitted.")
        if title == "Notation for subject":
            end = next((row[2] for row in properties if row[2] > start), len(lines))
            if not _formal_expression(lines[start + 1:end], allow_empty=True):
                check.fail("BODY_SECTION", title, "Notation for subject must contain one complete fenced String value.")
    if positions != sorted(set(positions)):
        check.fail("BODY_SECTION", "body", "Body Properties must be unique and in registered order.")
    for level, title, start in headings:
        if (level, title) not in {(3, "Formal Claim"), (3, "Prose Claim")}:
            continue
        parent = next((row for row in reversed(properties) if row[2] < start), None)
        if parent is None or parent[:2] != (2, "Claim"):
            check.fail("BODY_SECTION", title, "Claim children must be inside Claim.")
    for _, _, start in (row for row in properties if row[:2] == (2, "Claim")):
        end = next((row[2] for row in properties if row[2] > start), len(lines))
        children = [row for row in headings if start < row[2] < end and row[0] == 3]
        if not 1 <= len(children) <= 2 or len({row[1] for row in children}) != len(children):
            check.fail("BODY_SECTION", "Claim", "Claim requires one or two unique declared children.")
        first = children[0][2] if children else end
        if any(line.strip() for line in lines[start + 1:first]):
            check.fail("BODY_SECTION", "Claim", "Claim has no direct value.")
        for _, title, child_start in children:
            child_end = next((row[2] for row in children if row[2] > child_start), end)
            value = lines[child_start + 1:child_end]
            if title not in {"Formal Claim", "Prose Claim"}:
                check.fail("BODY_SECTION", title, "Unregistered Claim child.")
            elif title == "Formal Claim" and (not _formal_expression(value) or not re.fullmatch(
                r" {0,3}(?:`{3,}|~{3,})CFEL[ \t]*", "\n".join(value).strip().splitlines()[0]
            )):
                check.fail("BODY_SECTION", title, "Formal Claim must contain one fenced expression.")
            elif title == "Prose Claim" and not any(line.strip() for line in value):
                check.fail("BODY_SECTION", title, "Prose Claim must contain Markdown.")


def _body(metadata: Record, body: str, check: Check) -> None:
    required = role_sections(metadata, check)
    if required is None:
        return
    if required[0] == (2, "Summary") and body_layout(check) == "claim_children":
        _claim_children(body, check, required)
    elif required[0] == (2, "Summary"):
        _rmed_sections(body, str(metadata["content_role"]), check, required)
    elif is_graph_rule(metadata):
        from .graph_rule_body import validate_graph_rule_body

        if require_sources(check, GRAPH_RULE_SOURCES):
            validate_graph_rule_body(body, check)
    else:
        _sections(body, check, required)


def plan_definition(body: str, check: Check) -> None:
    """CA-D-470@7: one nonempty level-three Property directly inside Details."""
    headings = _headings(body)
    matches = [row for row in headings if row[1] == "Definition of Done"]
    if len(matches) != 1:
        check.fail(
            "BODY_SECTION",
            "Definition of Done",
            "Plan requires exactly one nested Definition of Done section.",
        )
    for level, _, index in matches:
        parent = next(
            (row for row in reversed(headings) if row[2] < index and row[0] < level), None
        )
        if level != 3 or parent is None or parent[:2] != (2, "Details"):
            check.fail(
                "BODY_SECTION",
                "Definition of Done",
                "Definition of Done must be a level-three section directly inside Details.",
            )
        end = next(
            (row[2] for row in headings if row[2] > index and row[0] <= level),
            len(body.splitlines()),
        )
        if not any(line.strip() for line in body.splitlines()[index + 1 : end]):
            check.fail(
                "BODY_SECTION",
                "Definition of Done",
                "Definition of Done must contain its own value.",
            )


def _plan_sections(metadata: Record, body: str, check: Check) -> None:
    if not _plan(metadata, check):
        return
    required = [(1, "Summary"), (2, "Objective"), (2, "Details")]
    _sections(body, check, required)
    plan_definition(body, check)
    for field in ("summary", "claim", "objective", "definition_of_done", "details", "scope"):
        check.forbid(metadata, field)
