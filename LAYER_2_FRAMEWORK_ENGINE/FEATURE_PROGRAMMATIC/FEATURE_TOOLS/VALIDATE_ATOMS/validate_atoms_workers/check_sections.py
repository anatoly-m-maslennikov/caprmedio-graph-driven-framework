"""Fence-aware headings and pinned Graph Rule authority sources."""

from __future__ import annotations

import re

from subject_notation import get_profile


GRAPH_RULE_SOURCES = (
    "CA-R-2001", "CA-D-637", "CA-R-1996",
    *(source.atom_id for source in get_profile("approved").grammar_pins),
)


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
