"""Pure byte-preserving section selection and the one declared section edit."""

from __future__ import annotations

import re
from dataclasses import dataclass


class SectionError(ValueError):
    def __init__(self, code: str, message: str, field: str = "delta") -> None:
        self.code, self.field = code, field
        super().__init__(message)


@dataclass(frozen=True)
class Section:
    level: int
    title: str
    start: int
    body_start: int
    end: int
    title_start: int
    title_end: int
    parent: int | None

    @property
    def identity(self) -> dict:
        return {"level": self.level, "title": self.title}


def section_identity(value: object) -> dict:
    if (type(value) is not dict or value.keys() != {"level", "title"}
            or type(value["level"]) is not int or not 1 <= value["level"] <= 6
            or type(value["title"]) is not str or not value["title"].strip()
            or value["title"] != value["title"].strip()
            or any(char in value["title"] for char in "\r\n\x00")):
        raise SectionError("input_invalid", "Section identity requires its exact level and title.")
    try:
        value["title"].encode("utf-8")
    except UnicodeError as error:
        raise SectionError("input_invalid", "Section title must be UTF-8 text.") from error
    return value


def parse_sections(raw: bytes) -> list[Section]:
    """Locate literal Atom headings, including nested content, outside code fences."""
    if type(raw) is not bytes:
        raise SectionError("input_invalid", "Section source must be supplied as bytes.")
    try:
        raw.decode("utf-8")
    except UnicodeError as error:
        raise SectionError("schema_invalid", "Section source must be UTF-8.") from error
    lines = raw.splitlines(keepends=True)
    if not lines or lines[0].rstrip(b"\r\n") != b"---":
        raise SectionError("schema_invalid", "Atom source requires YAML frontmatter.")
    boundary = next((i for i in range(1, len(lines)) if lines[i].rstrip(b"\r\n") == b"---"), None)
    if boundary is None:
        raise SectionError("schema_invalid", "Atom frontmatter must be closed.")
    headings = []
    fence = None
    offset = 0
    for index, line in enumerate(lines):
        plain = line.rstrip(b"\r\n")
        if index > boundary:
            marker = re.fullmatch(rb" {0,3}(`{3,}|~{3,})(.*)", plain)
            if fence is not None:
                if marker and marker[1][0] == fence[0] and len(marker[1]) >= fence[1] and not marker[2].strip():
                    fence = None
            elif marker:
                fence = (marker[1][0], len(marker[1]))
            else:
                match = re.fullmatch(rb"(#{1,6})[ \t]+([^\r\n]+?)[ \t]*", plain)
                if match:
                    headings.append((len(match[1]), match[2].decode("utf-8"), offset,
                                     offset + len(line), offset + match.start(2), offset + match.end(2)))
        offset += len(line)
    if fence is not None:
        raise SectionError("schema_invalid", "Section source has an unclosed code fence.")
    sections = []
    stack = []
    for index, (level, title, start, body_start, title_start, title_end) in enumerate(headings):
        while stack and headings[stack[-1]][0] >= level:
            stack.pop()
        parent = stack[-1] if stack and level > 2 else None
        end = next((row[2] for row in headings[index + 1:]
                    if row[0] <= level or (level == 1 and title == "Summary" and row[0] <= 2)), len(raw))
        sections.append(Section(level, title, start, body_start, end, title_start, title_end, parent))
        stack.append(index)
    summaries = [section for section in sections if section.identity == {"level": 1, "title": "Summary"}]
    if len(summaries) != 1 or not sections or sections[0] is not summaries[0]:
        raise SectionError("schema_invalid", "Atom body must begin with one Summary.")
    return sections


def resolve_section(sections: list[Section], identity: object) -> Section:
    identity = section_identity(identity)
    found = [section for section in sections if section.identity == identity]
    if not found:
        raise SectionError("target_not_found", "Selected section does not exist.")
    if len(found) != 1:
        raise SectionError("target_ambiguous", "Selected section is ambiguous.")
    return found[0]


def _position(sections: list[Section], value: object) -> tuple[str, Section]:
    if type(value) is not dict or len(value) != 1 or next(iter(value), None) not in {"before", "after"}:
        raise SectionError("input_invalid", "Section position requires exactly before or after an explicit section.")
    direction = next(iter(value))
    return direction, resolve_section(sections, value[direction])


def edit_section(raw: bytes, delta: object) -> bytes:
    """Derive one private edit representation, without choosing public API schemas.

    Workflow metadata, whole-Atom validation and exact currentness stay external.
    """
    if (type(delta) is not dict or type(delta.get("operation")) is not str
            or delta["operation"] not in {"add", "replace", "remove", "title", "position"}):
        raise SectionError("input_invalid", "Unknown section operation.")
    operation = delta["operation"]
    fields = {"operation", "section"} | ({"content", "position"} if operation == "add"
              else {"content"} if operation == "replace" else {operation} if operation in {"title", "position"} else set())
    if delta.keys() != fields:
        raise SectionError("input_invalid", "Section operation has unknown or missing fields.")
    identity = section_identity(delta["section"])
    sections = parse_sections(raw)
    if operation == "add":
        if any(section.identity == identity for section in sections):
            raise SectionError("target_ambiguous", "Added section identity already exists.")
        selected = None
    else:
        selected = resolve_section(sections, identity)
    if operation in {"add", "replace"}:
        if type(delta["content"]) is not str or "\x00" in delta["content"]:
            raise SectionError("input_invalid", "Section content must be explicit UTF-8 text.")
        try:
            content = delta["content"].encode("utf-8")
        except UnicodeError as error:
            raise SectionError("input_invalid", "Section content must be UTF-8 text.") from error
    summary = resolve_section(sections, {"level": 1, "title": "Summary"})
    if selected is summary:
        if operation == "title" and delta["title"] == "Summary":
            return raw
        if operation == "replace" and content == raw[summary.body_start:summary.end]:
            return raw
        raise SectionError("schema_invalid", "Summary edits require the replacement Workflow.")
    if operation in {"add", "replace"}:
        if operation == "replace":
            proposed = raw[:selected.body_start] + content + raw[selected.end:]
        else:
            direction, anchor = _position(sections, delta["position"])
            if identity["level"] != anchor.level or anchor is summary:
                raise SectionError("schema_invalid", "Added section must share its explicit anchor's level.")
            heading = raw[anchor.start:anchor.body_start]
            newline = b"\r\n" if heading.endswith(b"\r\n") else b"\r" if heading.endswith(b"\r") else b"\n"
            chunk = b"#" * identity["level"] + b" " + identity["title"].encode("utf-8") + newline + content
            point = anchor.start if direction == "before" else anchor.end
            proposed = raw[:point] + chunk + raw[point:]
    elif operation == "remove":
        proposed = raw[:selected.start] + raw[selected.end:]
    elif operation == "title":
        title = section_identity({"level": selected.level, "title": delta["title"]})
        if any(section is not selected and section.identity == title for section in sections):
            raise SectionError("target_ambiguous", "Renamed section identity already exists.")
        proposed = raw[:selected.title_start] + title["title"].encode("utf-8") + raw[selected.title_end:]
    else:
        direction, anchor = _position(sections, delta["position"])
        if selected is anchor:
            raise SectionError("input_invalid", "A section cannot be positioned against itself.")
        if selected.level != anchor.level or selected.parent != anchor.parent:
            raise SectionError("schema_invalid", "Reordering requires a sibling section at the same level.")
        chunk = raw[selected.start:selected.end]
        point = anchor.start if direction == "before" else anchor.end
        remaining = raw[:selected.start] + raw[selected.end:]
        if point > selected.start:
            point -= selected.end - selected.start
        proposed = remaining[:point] + chunk + remaining[point:]
    parsed = parse_sections(proposed)
    after_summary = resolve_section(parsed, summary.identity)
    if proposed[after_summary.body_start:after_summary.end] != raw[summary.body_start:summary.end]:
        raise SectionError("schema_invalid", "Summary edits require the replacement Workflow.")
    expected = identity if operation != "title" else {"level": identity["level"], "title": delta["title"]}
    if operation != "remove":
        changed = resolve_section(parsed, expected)
        if operation in {"add", "replace"} and proposed[changed.body_start:changed.end] != content:
            raise SectionError("schema_invalid", "Section content cannot introduce sibling headings or merge unrelated content.")
        if operation == "position" and proposed[changed.start:changed.end] != chunk:
            raise SectionError("schema_invalid", "Position would merge or change the selected section's complete content.")
    return proposed
