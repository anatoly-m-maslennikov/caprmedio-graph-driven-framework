# CA-R-2726@3
# CA-M-464@7
# CA-D-672@8

"""CommonMark heading sections for the Workbench in-memory projection."""

from __future__ import annotations

from io import StringIO
from typing import Any

from markdown_it import MarkdownIt


def parse_content(body: str) -> list[dict[str, Any]]:
    """Return Content Properties in CommonMark heading order."""
    lines = list(StringIO(body, newline=""))
    headings = _headings(MarkdownIt("commonmark").parse(body))
    records = _records(headings, lines)
    _reject_duplicate_siblings(records)
    return [_public_record(record, records, lines) for record in records]


def _headings(tokens: list[Any]) -> list[dict[str, Any]]:
    headings: list[dict[str, Any]] = []
    for index, token in enumerate(tokens):
        if token.type != "heading_open" or token.map is None:
            continue
        inline = tokens[index + 1]
        headings.append(
            {
                "heading": inline.content,
                "heading_level": int(token.tag[1:]),
                "start": token.map[0],
                "body_start": token.map[1],
            }
        )
    return headings


def _records(headings: list[dict[str, Any]], lines: list[str]) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    ancestors: list[dict[str, Any]] = []
    for position, heading in enumerate(headings, start=1):
        while ancestors and ancestors[-1]["heading_level"] >= heading["heading_level"]:
            ancestors.pop()
        key = _normalized_key(heading["heading"])
        path = [*(ancestors[-1]["property_path"] if ancestors else []), key]
        records.append(
            {
                **heading,
                "property_path": path,
                "position": position,
                "end": _section_end(heading, headings, len(lines)),
            }
        )
        ancestors.append(records[-1])
    return records


def _normalized_key(heading: str) -> str:
    key = "".join(
        character
        for character in heading.lower().replace(" ", "_")
        if character.isalnum() or character in "_-"
    )
    if not key:
        raise ValueError("heading normalizes to an empty property key")
    return key


def _section_end(heading: dict[str, Any], headings: list[dict[str, Any]], line_count: int) -> int:
    start = headings.index(heading) + 1
    for later in headings[start:]:
        if later["heading_level"] <= heading["heading_level"]:
            return later["start"]
    return line_count


def _reject_duplicate_siblings(records: list[dict[str, Any]]) -> None:
    sibling_keys: dict[tuple[str, ...], set[str]] = {}
    for record in records:
        parent = tuple(record["property_path"][:-1])
        key = record["property_path"][-1]
        if key in sibling_keys.setdefault(parent, set()):
            raise ValueError(f"duplicate normalized heading key: {key}")
        sibling_keys[parent].add(key)


def _public_record(
    record: dict[str, Any], records: list[dict[str, Any]], lines: list[str]
) -> dict[str, Any]:
    children = [
        child
        for child in records
        if child["property_path"][:-1] == record["property_path"]
    ]
    direct = _direct_markdown(record, children, lines)
    return {
        "property_path": record["property_path"],
        "heading": record["heading"],
        "heading_level": record["heading_level"],
        "position": record["position"],
        "direct_markdown": direct if direct.strip() else None,
        "section_markdown": "".join(lines[record["start"] : record["end"]]),
    }


def _direct_markdown(
    record: dict[str, Any], children: list[dict[str, Any]], lines: list[str]
) -> str:
    chunks: list[str] = []
    cursor = record["body_start"]
    for child in children:
        chunks.extend(lines[cursor : child["start"]])
        cursor = child["end"]
    chunks.extend(lines[cursor : record["end"]])
    return "".join(chunks)
