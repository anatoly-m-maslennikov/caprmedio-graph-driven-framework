"""Fence-aware checks for named Atom body Properties."""

from __future__ import annotations

import re

from .authority import Record
from .check_support import Check, _plan


def _headings(body: str) -> list[tuple[int, str, int]]:
    headings: list[tuple[int, str, int]] = []
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
        heading = re.match(r"^(#{1,6}) (.+)$", line)
        if fence is None and heading:
            headings.append((len(heading[1]), heading[2], index))
    return headings


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
    if not properties or properties[0][:2] != (1, "Summary"):
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
            (
                row[2]
                for row in properties[position + 1 :]
                if row[0] <= level or (title == "Summary" and row[:2] == (2, "Claim"))
            ),
            len(lines),
        )
        if not any(line.strip() for line in lines[index + 1 : end]):
            check.fail("BODY_SECTION", title, "Body Property value is empty: " + title + ".")


def _body(metadata: Record, body: str, check: Check) -> None:
    del metadata
    _sections(body, check, [(1, "Summary"), (2, "Claim")])


def _plan_sections(metadata: Record, body: str, check: Check) -> None:
    if not _plan(metadata, check):
        return
    required = [(1, "Summary"), (2, "Claim"), (2, "Definition of Done")]
    _sections(body, check, required)
    properties = [(level, title, index) for level, title, index in _headings(body) if level <= 2]
    details = [index for level, title, index in properties if (level, title) == (2, "Details")]
    dod = [
        index for level, title, index in properties if (level, title) == (2, "Definition of Done")
    ]
    if len(details) > 1 or (details and dod and details[0] < dod[0]):
        check.fail(
            "BODY_SECTION", "Details", "Details must occur at most once after Definition of Done."
        )
    for field in ("summary", "claim", "definition_of_done", "details", "scope"):
        check.forbid(metadata, field)
