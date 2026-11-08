# CA-R-2726@6
# CA-M-464@9
# CA-M-465@24
# CA-M-500@3
# CA-D-672@14

"""Compile declared Markdown Content properties into a Workbench SQL schema."""

from __future__ import annotations

from collections.abc import Iterable, Mapping, Sequence
from dataclasses import dataclass
import json
from pathlib import Path
from typing import Any

from markdown_it import MarkdownIt

from .declaration_cfel import (
    allowed_children as _allowed_children, container as _container, filters as _filters,
    model_statements as _model_statements, segments as _segments,
)
from .markdown_content import content_lines, direct_markdown, parse_content, section_markdown, source_markdown


_DECLARATION_FORMS = frozenset({"Declaration", "Entity Definition", "Relation Definition"})
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
        body = source_markdown(row)
        if not isinstance(records, list):
            records = parse_content(body, tolerate_duplicate_siblings=True) if isinstance(body, str) else []
        elif isinstance(body, str) and any(
            not isinstance(record, Mapping) or _span(record) is None for record in records
        ):
            records = parse_content(body, tolerate_duplicate_siblings=True)
        values = _records_by_path(records)
        self._validate(values, row)
        lines = content_lines(body) if isinstance(body, str) else None
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
    return schema_from_rules(rule for row in atom_rows for rule in declaration_rules(row))


def declaration_rules(row: Mapping[str, Any] | None) -> tuple[ContentRule, ...]:
    """Compile one source's literal Content declarations."""
    if row is None or not _is_declaration(row):
        return ()
    return tuple(_rules(source_markdown(row), _source(row)))


def schema_from_rules(rules: Iterable[ContentRule]) -> ContentSchema:
    """Assemble a schema from already parsed declaration rules."""
    unique_rules = tuple(sorted(set(rules), key=_rule_key))
    sources = tuple(sorted({rule.source for rule in unique_rules}, key=_source_key))
    grouped: dict[tuple[str, ...], list[ContentRule]] = {}
    for rule in unique_rules:
        if rule.value_bearing:
            grouped.setdefault(rule.path, []).append(rule)
    columns = tuple(
        ContentColumn(path, "content." + ".".join(path), tuple(grouped[path]))
        for path in sorted(grouped, key=lambda path: "content." + ".".join(path))
    )
    return ContentSchema(columns, unique_rules, sources)


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
        spans_available, value = _value_excluding_declared_children(
            record, records, declared_children, lines,
        )
        if not spans_available:
            value = direct_markdown(
                record, (candidate for group in records.values() for candidate in group), lines,
            )
        if isinstance(value, str) and value.strip():
            return value.strip()
    return None


def _value_excluding_declared_children(
    record: Mapping[str, Any], records: Mapping[tuple[str, ...], list[Mapping[str, Any]]],
    declared_children: frozenset[tuple[str, ...]], lines: list[str] | None,
) -> tuple[bool, str | None]:
    """Keep presentation headings, subtracting only declared child spans."""
    span = _span(record)
    if span is None or lines is None:
        return False, None
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
    return True, value.strip() or None


def _prose_claim(
    records: Mapping[tuple[str, ...], list[Mapping[str, Any]]], path: tuple[str, ...],
    declared_children: frozenset[tuple[str, ...]], lines: list[str] | None,
) -> str | None:
    """Keep undeclared prose headings, subtracting exact declared child spans."""
    record = next(iter(records.get(path, ())), None)
    if record is None:
        return _legacy_prose_claim(records, path[:-1], lines)
    spans_available, value = _value_excluding_declared_children(
        record, records, declared_children, lines,
    )
    if spans_available:
        return value
    section = section_markdown(record, lines)
    if section is None:
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
    lines: list[str] | None,
) -> str | None:
    """Retain admitted direct Claim prose while removing declared Claim children."""
    parent = next(iter(records.get(parent_path, ())), None)
    if parent is None:
        return None
    section = section_markdown(parent, lines)
    if section is None:
        return None
    value = section.split("\n", 1)[1] if "\n" in section else ""
    for child_name in ("formal_claim", "prose_claim"):
        child = next(iter(records.get((*parent_path, child_name), ())), None)
        child_section = section_markdown(child, lines) if child is not None else None
        if child_section is not None:
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
