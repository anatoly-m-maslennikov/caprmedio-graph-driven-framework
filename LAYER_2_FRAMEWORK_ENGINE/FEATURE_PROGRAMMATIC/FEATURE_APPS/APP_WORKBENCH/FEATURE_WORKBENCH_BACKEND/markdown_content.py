# CA-R-2726@5
# CA-M-464@8
# CA-M-465@21
# CA-D-672@12

"""CommonMark heading sections for the Workbench in-memory projection."""

from __future__ import annotations

from io import StringIO
import re
from typing import Any, Iterable, Mapping

from markdown_it import MarkdownIt


def parse_content(
    body: str, *, tolerate_duplicate_siblings: bool = False, include_spans: bool | None = None,
    compact: bool = False,
) -> list[dict[str, Any]]:
    """Return Content Properties in CommonMark heading order."""
    if include_spans is None:
        # Source rows already request duplicate-tolerant records and need their
        # spans for exact declared-child removal. Ordinary parser callers keep
        # the concise public record shape.
        include_spans = tolerate_duplicate_siblings
    if compact:
        include_spans = True
    lines = content_lines(body)
    headings = _headings(MarkdownIt("commonmark").parse(body))
    records = _records(headings, lines)
    if not tolerate_duplicate_siblings:
        _reject_duplicate_siblings(records)
    return [
        _public_record(record, records, lines, include_spans, compact)
        for record in records
    ]


def content_lines(body: str) -> list[str]:
    """Split Markdown exactly as the CommonMark source parser does."""
    return list(StringIO(body, newline=""))


def source_markdown(row: Mapping[str, Any]) -> str | None:
    """Decode a cached source body only while its Markdown is needed."""
    if isinstance(body := row.get("_content_bytes"), bytes):
        return body.decode("utf-8")
    value = row.get("content_markdown")
    return value if isinstance(value, str) else None


def section_markdown(record: Mapping[str, Any], lines: list[str] | None) -> str | None:
    """Rebuild a compact record's section, preserving source newline semantics."""
    start, end = record.get("_start_line"), record.get("_end_line")
    if lines is not None and type(start) is int and type(end) is int:
        return "".join(lines[start:end])
    value = record.get("section_markdown")
    return value if isinstance(value, str) else None


def direct_markdown(
    record: Mapping[str, Any], records: Iterable[Mapping[str, Any]], lines: list[str] | None,
) -> str | None:
    """Rebuild a compact record's direct Markdown from its immediate children."""
    span = _span(record)
    path = record.get("property_path")
    if span is not None and isinstance(path, list) and all(isinstance(part, str) for part in path) and lines is not None:
        _start, body_start, end = span
        children = sorted(
            (
                child_span
                for child in records
                if isinstance(child_path := child.get("property_path"), list)
                and child_path[:-1] == path
                and (child_span := _span(child)) is not None
                and body_start <= child_span[0] < end
            ),
            key=lambda child_span: child_span[0],
        )
        chunks: list[str] = []
        cursor = body_start
        for child_start, _child_body_start, child_end in children:
            chunks.extend(lines[cursor:child_start])
            cursor = child_end
        chunks.extend(lines[cursor:end])
        value = "".join(chunks)
        return value if value.strip() else None
    value = record.get("direct_markdown")
    return value if isinstance(value, str) else None


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
        key = content_key(heading["heading"])
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


def content_key(heading: str) -> str:
    """Use one carrier-independent spelling for Markdown and Declaration keys."""
    separated = re.sub(r"[\s-]+", "_", heading.casefold())
    key = "".join(character for character in separated if character.isalnum() or character == "_")
    key = re.sub(r"_+", "_", key).strip("_")
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
    record: dict[str, Any], records: list[dict[str, Any]], lines: list[str], include_spans: bool,
    compact: bool,
) -> dict[str, Any]:
    public = {
        "property_path": record["property_path"],
        "heading": record["heading"],
        "heading_level": record["heading_level"],
        "position": record["position"],
    }
    if not compact:
        children = [child for child in records if child["property_path"][:-1] == record["property_path"]]
        direct = _direct_markdown(record, children, lines)
        public["direct_markdown"] = direct if direct.strip() else None
        public["section_markdown"] = "".join(lines[record["start"] : record["end"]])
    if include_spans:
        public.update({
            "_start_line": record["start"],
            "_body_start_line": record["body_start"],
            "_end_line": record["end"],
        })
    return public


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


def _span(record: Mapping[str, Any]) -> tuple[int, int, int] | None:
    start = record.get("_start_line")
    body_start = record.get("_body_start_line")
    end = record.get("_end_line")
    if all(type(value) is int for value in (start, body_start, end)):
        return start, body_start, end
    return None
