# CA-R-2726@4
# CA-M-464@7
# CA-D-672@9

"""Extract the declared Markdown Content values exposed by Workbench."""

from __future__ import annotations

from collections.abc import Mapping
from io import StringIO
from typing import Any

from markdown_it import MarkdownIt


CONTENT_COLUMNS = (
    "content.summary",
    "content.claim.formal claim",
    "content.claim.prose claim",
    "content.semantics",
    "content.details",
    "content.notation for subject",
    "content.question",
    "content.scope",
    "content.approach",
    "content.results",
    "content.tldr",
    "content.concern",
    "content.evidences",
    "content.blast radius",
    "content.objective",
    "content.details.definition of done",
    "content.operation",
)

_RMED = {"Requirement", "Method", "Evaluation", "Delivery"}
_ROOTS = {
    "Analysis": {"summary", "question", "scope", "approach", "results", "tldr"},
    "Analysis & Advisory": {"summary", "question", "scope", "approach", "results", "tldr"},
    "Concern": {"summary", "concern", "evidences", "blast radius"},
    "Operations": {"summary", "operation", "details"},
    "Plan": {"summary", "objective", "details"},
}


def content_columns(row: Mapping[str, Any]) -> dict[str, str | None]:
    """Return declared body values; undeclared or absent values are ``None``."""
    result = dict.fromkeys(CONTENT_COLUMNS)
    role = row.get("role")
    body = row.get("content_markdown")
    if not isinstance(role, str) or not isinstance(body, str):
        return result
    roots = _roots(role, row.get("form"))
    if not roots:
        return result
    sections = _sections(body, roots)
    for name, section in sections.items():
        if name in {"summary", "semantics", "details", "question", "scope", "approach", "results", "tldr", "concern", "evidences", "blast radius", "objective", "operation", "notation for subject"}:
            result[f"content.{name}"] = _value(section, ())
    if role in _RMED:
        claim = sections.get("claim")
        if claim is not None:
            children = _children(claim, {"formal claim", "prose claim"})
            formal = children["formal claim"]
            prose = children["prose claim"]
            result["content.claim.formal claim"] = _value(formal, ())
            result["content.claim.prose claim"] = _value(prose, ()) or _value(claim, {"formal claim", "prose claim"})
    if role == "Plan":
        details = sections.get("details")
        if details is not None:
            done, = _children(details, {"definition of done"}).values()
            result["content.details.definition of done"] = _value(done, ())
            result["content.details"] = _value(details, {"definition of done"})
    return result


def _roots(role: str, form: object) -> set[str]:
    if role in _RMED:
        result = {"summary", "claim", "semantics", "details"}
        if role == "Requirement" and form == "Relation Definition":
            result.add("notation for subject")
        return result
    return _ROOTS.get(role, set())


def _sections(body: str, roots: set[str]) -> dict[str, dict[str, Any]]:
    lines = list(StringIO(body, newline=""))
    headings = []
    tokens = MarkdownIt("commonmark").parse(body)
    for index, token in enumerate(tokens):
        if token.type == "heading_open" and token.map is not None:
            headings.append(
                {
                    "name": tokens[index + 1].content.casefold(),
                    "level": int(token.tag[1:]),
                    "start": token.map[0],
                    "body_start": token.map[1],
                }
            )
    summary = next((heading for heading in headings if heading["name"] == "summary"), None)
    root_level = max(2, summary["level"]) if summary is not None else 2
    selected = [
        heading
        for heading in headings
        if heading["name"] in roots
        and (
            (
                summary is not None
                and heading["name"] == "summary"
                and heading["level"] == summary["level"]
            )
            or (heading["name"] != "summary" and heading["level"] == root_level)
        )
    ]
    result = {}
    for index, section in enumerate(selected):
        end = selected[index + 1]["start"] if index + 1 < len(selected) else len(lines)
        if section["name"] in result:
            raise ValueError(f"duplicate declared content property: {section['name']}")
        result[section["name"]] = {**section, "end": end, "lines": lines}
    return result


def _children(section: dict[str, Any], names: set[str]) -> dict[str, dict[str, Any] | None]:
    body = "".join(section["lines"][section["body_start"] : section["end"]])
    offset = section["body_start"]
    tokens = MarkdownIt("commonmark").parse(body)
    headings = []
    for index, token in enumerate(tokens):
        if token.type == "heading_open" and token.map is not None:
            name = tokens[index + 1].content.casefold()
            if name in names and int(token.tag[1:]) == section["level"] + 1:
                headings.append(
                    {
                        "name": name,
                        "level": int(token.tag[1:]),
                        "start": offset + token.map[0],
                        "body_start": offset + token.map[1],
                    }
                )
    result: dict[str, dict[str, Any] | None] = dict.fromkeys(names)
    for index, child in enumerate(headings):
        end = headings[index + 1]["start"] if index + 1 < len(headings) else section["end"]
        if result[child["name"]] is not None:
            raise ValueError(f"duplicate declared content property: {child['name']}")
        result[child["name"]] = {**child, "end": end, "lines": section["lines"]}
    return result


def _value(section: dict[str, Any] | None, child_names: set[str] | tuple[str, ...]) -> str | None:
    if section is None:
        return None
    children = _children(section, set(child_names)) if child_names else {}
    lines = section["lines"]
    cursor = section["body_start"]
    chunks: list[str] = []
    for child in sorted((item for item in children.values() if item), key=lambda item: item["start"]):
        chunks.extend(lines[cursor : child["start"]])
        cursor = child["end"]
    chunks.extend(lines[cursor : section["end"]])
    value = "".join(chunks).strip()
    return value or None
