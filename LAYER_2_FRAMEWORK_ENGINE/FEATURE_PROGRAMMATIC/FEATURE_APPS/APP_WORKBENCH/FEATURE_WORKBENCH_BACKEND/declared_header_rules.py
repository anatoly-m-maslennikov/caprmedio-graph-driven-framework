# CA-M-500@3
# CA-D-672@14

"""Compile literal Current-model Header declarations into typed rules."""

from __future__ import annotations

from collections.abc import Iterable, Mapping, Sequence
from dataclasses import dataclass
import re
from typing import Any

from .content_schema import DeclarationSource, _is_declaration, _source
from .declaration_cfel import (
    allowed_children as _allowed_children, filters as _filters,
    model_statements as _model_statements, segments as _segments,
)
from .markdown_content import source_markdown


_SCALAR_FORMATS = {
    "int": "BIGINT",
    "bool": "BOOLEAN",
    "string": "VARCHAR",
    "text": "VARCHAR",
    "atom id": "VARCHAR",
    "datetime": "TIMESTAMPTZ",
}
_FORMAT = re.compile(
    r"::\s*\[\s*([^,\]]+)(?:,[^\]]*)?\]\s*(?:\{\s*::\s*([^}]+)\s*\})?"
)
_COLLECTION = re.compile(r"(?:0|1)\+|\d+\.\.(?:\d+|n)")


@dataclass(frozen=True)
class HeaderRule:
    """One raw or resolved Header declaration and its narrow applicability."""

    path: tuple[str, ...]
    format: str | None
    roles: frozenset[str] | None
    forms: frozenset[str] | None
    source: DeclarationSource


def header_declaration_rules(row: Mapping[str, Any] | None) -> tuple[HeaderRule, ...]:
    """Compile one source's raw literal Header declaration contributions."""
    if row is None or not _is_declaration(row):
        return ()
    body = source_markdown(row)
    if not isinstance(body, str):
        return ()
    source = _source(row)
    return tuple(sorted({
        HeaderRule(parsed.path, parsed.format, parsed.roles, parsed.forms, source)
        for statement in _cfel_statements(body)
        if (parsed := _statement(statement)) is not None
    }, key=_rule_key))


def compile_header_rules(rows: Sequence[Mapping[str, Any]]) -> tuple[HeaderRule, ...]:
    """Compile supplied declarations after resolving their merged raw contributions."""
    return resolve_header_rules(rule for row in rows for rule in header_declaration_rules(row))


def resolve_header_rules(rules: Iterable[HeaderRule]) -> tuple[HeaderRule, ...]:
    """Resolve typed wildcards against explicit untyped child declarations."""
    raw = tuple(rules)
    typed = [rule for rule in raw if rule.format is not None and rule.path[-1:] != ("*",)]
    direct_paths = {rule.path for rule in typed}
    inherited: list[HeaderRule] = []
    for child in raw:
        if child.format is not None or child.path[-1:] == ("*",) or child.path in direct_paths:
            continue
        for wildcard in raw:
            if wildcard.path != (*child.path[:-1], "*") or wildcard.format is None:
                continue
            roles = _intersect_selectors(child.roles, wildcard.roles)
            forms = _intersect_selectors(child.forms, wildcard.forms)
            if roles != frozenset() and forms != frozenset():
                inherited.append(HeaderRule(child.path, wildcard.format, roles, forms, wildcard.source))
    return tuple(sorted(set((*typed, *inherited)), key=_rule_key))


def _cfel_statements(body: str) -> tuple[str, ...]:
    from markdown_it import MarkdownIt

    return tuple(
        statement
        for token in MarkdownIt("commonmark").parse(body)
        if token.type == "fence" and token.info.strip().casefold() == "cfel"
        for statement in _model_statements(token.content)
    )


def _statement(statement: str) -> HeaderRule | None:
    if not statement.startswith("Atom") or ";>" in statement or "((" in statement:
        return None
    header = _literal_header_offset(statement)
    if header < 0:
        return None
    prefix, tail = statement[:header], statement[header + len(".Header") :]
    if "::" not in tail and re.search(r"[=<>!?]", tail):
        return None
    segments, remainder = _segments(tail)
    if not segments or segments[0] == "relations":
        return None
    roles, forms = _filters(prefix, "Role"), _filters(prefix, "Form")
    if segments[-1] == "*":
        choices = _allowed_children(remainder)
        if choices:
            return None
        format = _format(remainder)
        return (
            HeaderRule(tuple(segments), format, roles, forms, DeclarationSource(None, None, None))
            if format
            else None
        )
    if "*" in segments:
        return None
    if _grouping(remainder):
        return None
    return HeaderRule(tuple(segments), _format(remainder), roles, forms, DeclarationSource(None, None, None))


def _format(remainder: str) -> str | None:
    match = _FORMAT.search(remainder)
    if match is None:
        return None
    scalar = _SCALAR_FORMATS.get(" ".join(match.group(1).casefold().split()))
    if scalar is None:
        return None
    return "JSON" if _is_collection(match.group(2)) else scalar


def _literal_header_offset(statement: str) -> int:
    """Ignore Header selectors while finding a model Header property path."""
    depth = 0
    offset = -1
    for index, character in enumerate(statement):
        if character == "(":
            depth += 1
        elif character == ")":
            depth -= 1
        elif depth == 0 and statement.startswith(".Header.", index):
            offset = index
    return offset


def _grouping(remainder: str) -> bool:
    return bool(re.search(r"::\s*\[\s*\]", remainder))


def _is_collection(cardinality: str | None) -> bool:
    if cardinality is None or _COLLECTION.fullmatch(cardinality.strip()) is None:
        return False
    _lower, separator, upper = cardinality.strip().partition("..")
    return not separator or upper == "n" or int(upper) > 1


def _intersect_selectors(
    first: frozenset[str] | None, second: frozenset[str] | None,
) -> frozenset[str] | None:
    if first is None:
        return second
    if second is None:
        return first
    return first & second


def _rule_key(rule: HeaderRule) -> tuple[object, ...]:
    source = rule.source
    return (
        rule.path, rule.format, tuple(sorted(rule.roles or ())), tuple(sorted(rule.forms or ())),
        source.reference or "", source.version or -1, source.source_path or "",
    )
