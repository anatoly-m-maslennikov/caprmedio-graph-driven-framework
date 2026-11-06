# CA-R-2726@5
# CA-M-500@1
# CA-D-672@12

"""Compile declared Markdown Content properties into a Workbench SQL schema."""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from dataclasses import dataclass
import json
from pathlib import Path
import re
from typing import Any

from markdown_it import MarkdownIt

from .markdown_content import content_key, parse_content


_DECLARATION_FORMS = frozenset({"Declaration", "Entity Definition", "Relation Definition"})
_ROLE_SETS = {"RMED": frozenset({"Requirement", "Method", "Evaluation", "Delivery"})}


@dataclass(frozen=True)
class DeclarationSource:
    """One Current Declaration which contributed to the compiled schema."""

    reference: str | None
    version: int | None
    source_path: str | None

    def asset(self) -> dict[str, object]:
        return {
            "reference": self.reference,
            "version": self.version,
            "source_path": self.source_path,
        }


@dataclass(frozen=True)
class ContentRule:
    """A literal declared Content path and its narrow applicability."""

    path: tuple[str, ...]
    roles: frozenset[str] | None
    forms: frozenset[str] | None
    value_bearing: bool
    source: DeclarationSource

    def applies(self, row: Mapping[str, Any]) -> bool:
        return (
            (self.roles is None or row.get("role") in self.roles)
            and (self.forms is None or row.get("form") in self.forms)
        )


@dataclass(frozen=True)
class ContentColumn:
    """One declared scalar Markdown property exposed as a VARCHAR column."""

    path: tuple[str, ...]
    name: str
    rules: tuple[ContentRule, ...]

    def applies(self, row: Mapping[str, Any]) -> bool:
        return any(rule.applies(row) for rule in self.rules)


@dataclass(frozen=True)
class ContentSchema:
    """The reproducible Content portion of the public atoms schema."""

    columns: tuple[ContentColumn, ...]
    rules: tuple[ContentRule, ...]
    sources: tuple[DeclarationSource, ...]

    @property
    def names(self) -> tuple[str, ...]:
        return tuple(column.name for column in self.columns)

    @property
    def shape(self) -> tuple[tuple[object, ...], tuple[object, ...]]:
        """The table/validation shape, excluding declaration provenance."""
        return (
            tuple((column.path, column.name) for column in self.columns),
            tuple(sorted({
                (rule.path, tuple(sorted(rule.roles or ())), tuple(sorted(rule.forms or ())), rule.value_bearing)
                for rule in self.rules
            })),
        )

    def values(self, row: Mapping[str, Any]) -> dict[str, str | None]:
        """Extract declared Content values and reject duplicate declared headings."""
        records = row.get("content_properties_json")
        body = row.get("content_markdown")
        if not isinstance(records, list):
            records = parse_content(body, tolerate_duplicate_siblings=True) if isinstance(body, str) else []
        values = _records_by_path(records)
        self._validate(values, row)
        lines = body.splitlines(keepends=True) if isinstance(body, str) else None
        return {
            column.name: _value(
                values,
                column.path,
                column.applies(row),
                _declared_children(self.rules, column.path, row),
                lines,
            )
            for column in self.columns
        }

    def _validate(
        self, values: Mapping[tuple[str, ...], list[Mapping[str, Any]]], row: Mapping[str, Any],
    ) -> None:
        for rule in self.rules:
            if rule.applies(row) and len(values.get(rule.path, ())) > 1:
                raise ValueError(f"duplicate declared content property: {'.'.join(rule.path)}")

    def asset(self) -> dict[str, object]:
        return {
            "version": 1,
            "content_columns": [
                {
                    "path": list(column.path),
                    "name": column.name,
                    "format": "VARCHAR",
                    "rules": [
                        {
                            "roles": sorted(rule.roles) if rule.roles is not None else None,
                            "forms": sorted(rule.forms) if rule.forms is not None else None,
                            "source": rule.source.asset(),
                        }
                        for rule in column.rules
                    ],
                }
                for column in self.columns
            ],
            "content_declaration_sources": [source.asset() for source in self.sources],
        }

    def write(self, path: Path | None) -> None:
        if path is not None:
            path.write_text(json.dumps(self.asset(), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def content_schema_asset_path(database_path: Path | None) -> Path | None:
    """Keep the independently rebuildable Content schema beside the projection."""
    return database_path.parent / "content-schema.json" if database_path is not None else None


def compile_content_schema(atom_rows: Sequence[Mapping[str, Any]]) -> ContentSchema:
    """Compile Current literal Content declarations; no general CFEL evaluation occurs."""
    rules: list[ContentRule] = []
    sources: list[DeclarationSource] = []
    for row in atom_rows:
        if not _is_declaration(row):
            continue
        source = _source(row)
        declared = _rules(row.get("content_markdown"), source)
        if declared:
            sources.append(source)
            rules.extend(declared)
    unique_rules = tuple(sorted(set(rules), key=_rule_key))
    grouped: dict[tuple[str, ...], list[ContentRule]] = {}
    for rule in unique_rules:
        if rule.value_bearing:
            grouped.setdefault(rule.path, []).append(rule)
    columns = tuple(
        ContentColumn(path, "content." + ".".join(path), tuple(grouped[path]))
        for path in sorted(grouped, key=lambda path: "content." + ".".join(path))
    )
    return ContentSchema(columns, unique_rules, tuple(sorted(set(sources), key=_source_key)))


def _is_declaration(row: Mapping[str, Any]) -> bool:
    return (
        row.get("status_group") == "Current"
        and row.get("role") == "Requirement"
        and row.get("form") in _DECLARATION_FORMS
    )


def _source(row: Mapping[str, Any]) -> DeclarationSource:
    reference = row.get("ref")
    atom_id = row.get("id")
    source_path = row.get("source_path")
    version = row.get("version")
    return DeclarationSource(
        reference if isinstance(reference, str) else atom_id if isinstance(atom_id, str) else None,
        version if type(version) is int else None,
        source_path if isinstance(source_path, str) else None,
    )


def _rules(body: object, source: DeclarationSource) -> list[ContentRule]:
    if not isinstance(body, str):
        return []
    result: list[ContentRule] = []
    for token in MarkdownIt("commonmark").parse(body):
        if token.type != "fence" or token.info.strip().casefold() != "cfel":
            continue
        for statement in _model_statements(token.content):
            result.extend(_statement_rules(statement, source))
    return result


def _declared_children(
    rules: Sequence[ContentRule], parent_path: tuple[str, ...], row: Mapping[str, Any],
) -> frozenset[tuple[str, ...]]:
    return frozenset(
        rule.path
        for rule in rules
        if rule.applies(row) and rule.path[:-1] == parent_path
    )


def _model_statements(body: str) -> list[str]:
    lines = body.splitlines()
    model_start = next((index for index, line in enumerate(lines) if line.strip().casefold() == "# model"), None)
    if model_start is None:
        return []
    model_lines = []
    for line in lines[model_start + 1 :]:
        if line.strip().startswith("#"):
            break
        model_lines.append(line)
    # ``;>`` is a CFEL relation operator, not a statement terminator.
    return [
        statement.strip()
        for statement in re.split(r";(?!>)", "\n".join(model_lines))
        if statement.strip()
    ]


def _statement_rules(statement: str, source: DeclarationSource) -> list[ContentRule]:
    if not statement.startswith("Atom") or ";>" in statement or "((" in statement:
        return []
    content = statement.find(".Content")
    if content < 0:
        return []
    prefix, tail = statement[:content], statement[content + len(".Content") :]
    segments, remainder = _segments(tail)
    if not segments:
        return []
    roles = _filters(prefix, "Role")
    forms = _filters(prefix, "Form")
    if segments[-1] in {"*", "**"}:
        if segments[-1] != "*":
            return []
        choices = _allowed_children(remainder)
        return [
            ContentRule((*segments[:-1], choice), roles, forms, True, source)
            for choice in choices
        ]
    return [ContentRule(tuple(segments), roles, forms, not _container(remainder), source)]


def _segments(tail: str) -> tuple[list[str], str]:
    result: list[str] = []
    index = 0
    while index < len(tail) and tail[index] == ".":
        index += 1
        end = _segment_end(tail, index)
        raw = tail[index:end].strip()
        if not raw:
            return [], tail[index:]
        result.append(raw if raw in {"*", "**"} else _key(raw))
        index = end
    return result, tail[index:]


def _segment_end(value: str, start: int) -> int:
    candidates = [len(value)]
    for token in (".", "[", "{", ";"):
        found = value.find(token, start)
        if found >= 0:
            candidates.append(found)
    colon = value.find("::", start)
    if colon >= 0:
        candidates.append(colon)
    return min(candidates)


def _key(value: str) -> str:
    try:
        return content_key(value)
    except ValueError as error:
        raise ValueError(f"Content declaration property has no usable key: {value!r}") from error


def _filters(prefix: str, field: str) -> frozenset[str] | None:
    groups = _filter_groups(prefix)
    _reject_unsupported_filters(groups)
    matches = [item for item in groups if _selector_field(item) == field]
    if not matches:
        return None
    values = [_filter_values(item, field) for item in matches]
    if len(values) != 1:
        raise ValueError(f"unsupported Content declaration: multiple Header.{field} filters")
    return values[0]


def _filter_groups(prefix: str) -> list[str]:
    groups: list[str] = []
    index = 0
    while True:
        start = prefix.find("/(", index)
        if start < 0:
            return groups
        depth = 1
        end = start + 2
        while end < len(prefix) and depth:
            if prefix[end] == "(":
                depth += 1
            elif prefix[end] == ")":
                depth -= 1
            end += 1
        if depth:
            raise ValueError("unsupported Content declaration: unclosed Header filter")
        groups.append(prefix[start + 2 : end - 1].strip())
        index = end


def _reject_unsupported_filters(groups: Sequence[str]) -> None:
    for expression in groups:
        if _selector_field(expression, complete=True) is not None:
            continue
        known = re.match(r"\.Header\.(?:Context\.)?(Role|Form)\b", expression)
        if known is not None:
            raise ValueError(
                f"unsupported Content declaration Header.{known.group(1)} filter: {expression}"
            )
        raise ValueError(f"unsupported Content declaration selector: {expression}")


def _selector_field(expression: str, *, complete: bool = False) -> str | None:
    if complete:
        match = re.fullmatch(
            r"\.Header\.(?:Context\.)?(Role|Form)\s*(in|:=|=|:)\s*.+", expression,
        )
    else:
        match = re.match(r"\.Header\.(?:Context\.)?(Role|Form)\b", expression)
    return match.group(1) if match is not None else None


def _filter_values(expression: str, field: str) -> frozenset[str]:
    match = re.fullmatch(
        rf"\.Header\.(?:Context\.)?{field}\s*(in|:=|=|:)\s*(.+)", expression,
    )
    if match is None:
        raise ValueError(f"unsupported Content declaration Header.{field} filter: {expression}")
    operator, value = match.groups()
    value = value.strip()
    if operator == "in" and field == "Role" and value in _ROLE_SETS:
        return _ROLE_SETS[value]
    if value.startswith("("):
        if not value.endswith(")"):
            raise ValueError(f"unsupported Content declaration Header.{field} filter: {expression}")
        items = value[1:-1].split(",")
    elif operator == "in":
        raise ValueError(f"unsupported Content declaration Header.{field} filter: {expression}")
    else:
        items = (value,)
    result = frozenset(_unquote(item.strip()) for item in items if item.strip())
    if not result:
        raise ValueError(f"unsupported Content declaration Header.{field} filter: {expression}")
    return result


def _unquote(value: str) -> str:
    return value[1:-1] if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'" else value


def _allowed_children(remainder: str) -> tuple[str, ...]:
    match = re.search(r"\bin\s*\(([^)]*)\)", remainder)
    if match is None:
        return ()
    return tuple(_key(item.strip()) for item in match.group(1).split(",") if item.strip())


def _container(remainder: str) -> bool:
    return bool(re.search(r"::\s*\[\s*\]", remainder))


def _records_by_path(records: object) -> dict[tuple[str, ...], list[Mapping[str, Any]]]:
    result: dict[tuple[str, ...], list[Mapping[str, Any]]] = {}
    if not isinstance(records, list):
        return result
    for record in records:
        if not isinstance(record, Mapping):
            continue
        raw_path = record.get("property_path")
        if not isinstance(raw_path, list) or not all(isinstance(part, str) for part in raw_path):
            continue
        result.setdefault(tuple(raw_path), []).append(record)
    return result


def _value(
    records: Mapping[tuple[str, ...], list[Mapping[str, Any]]], path: tuple[str, ...], applies: bool,
    declared_children: frozenset[tuple[str, ...]], lines: list[str] | None,
) -> str | None:
    if not applies:
        return None
    if path[-1:] == ("prose_claim",):
        prose = _prose_claim(records, path, declared_children, lines)
        if prose is not None:
            return prose
    record = next(iter(records.get(path, ())), None)
    if record is not None:
        value = record.get("direct_markdown")
        if isinstance(value, str) and value.strip():
            return value.strip()
    return None


def _prose_claim(
    records: Mapping[tuple[str, ...], list[Mapping[str, Any]]], path: tuple[str, ...],
    declared_children: frozenset[tuple[str, ...]], lines: list[str] | None,
) -> str | None:
    """Keep undeclared prose headings, subtracting exact declared child spans."""
    record = next(iter(records.get(path, ())), None)
    if record is None:
        return _legacy_prose_claim(records, path[:-1])
    span = _span(record)
    if span is not None and lines is not None:
        body_start, end = span[1:]
        children = sorted(
            (
                child_span
                for child_path in declared_children
                for child in records.get(child_path, ())
                if (child_span := _span(child)) is not None
                and body_start <= child_span[0] < end
            ),
            key=lambda child_span: child_span[0],
        )
        parts: list[str] = []
        cursor = body_start
        for child_start, _child_body_start, child_end in children:
            parts.extend(lines[cursor:child_start])
            cursor = child_end
        parts.extend(lines[cursor:end])
        value = "".join(parts)
        return value.strip() or None
    section = record.get("section_markdown")
    if not isinstance(section, str):
        return None
    value = section.split("\n", 1)[1] if "\n" in section else ""
    return value.strip() or None


def _span(record: Mapping[str, Any]) -> tuple[int, int, int] | None:
    start = record.get("_start_line")
    body_start = record.get("_body_start_line")
    end = record.get("_end_line")
    if all(type(value) is int for value in (start, body_start, end)):
        return start, body_start, end
    return None


def _legacy_prose_claim(
    records: Mapping[tuple[str, ...], list[Mapping[str, Any]]], parent_path: tuple[str, ...],
) -> str | None:
    """Retain admitted direct Claim prose while removing declared Claim children."""
    parent = next(iter(records.get(parent_path, ())), None)
    if parent is None:
        return None
    section = parent.get("section_markdown")
    if not isinstance(section, str):
        return None
    value = section.split("\n", 1)[1] if "\n" in section else ""
    for child_name in ("formal_claim", "prose_claim"):
        child = next(iter(records.get((*parent_path, child_name), ())), None)
        child_section = child.get("section_markdown") if child is not None else None
        if isinstance(child_section, str):
            value = value.replace(child_section, "", 1)
    return value.strip() or None


def _source_key(source: DeclarationSource) -> tuple[str, int, str]:
    return (source.reference or "", source.version or -1, source.source_path or "")


def _rule_key(rule: ContentRule) -> tuple[tuple[str, ...], tuple[str, ...], tuple[str, ...], bool, tuple[str, int, str]]:
    return (
        rule.path,
        tuple(sorted(rule.roles or ())),
        tuple(sorted(rule.forms or ())),
        rule.value_bearing,
        _source_key(rule.source),
    )
