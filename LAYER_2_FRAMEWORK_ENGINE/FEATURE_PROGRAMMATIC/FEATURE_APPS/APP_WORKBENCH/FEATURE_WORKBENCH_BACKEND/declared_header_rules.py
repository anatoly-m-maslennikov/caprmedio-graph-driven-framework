# CA-M-500@12
# CA-D-672@22

"""Compile literal Current-model Header declarations into typed rules."""

from __future__ import annotations

from collections.abc import Iterable, Mapping, Sequence
from dataclasses import dataclass
import re
from typing import Any

from .content_schema import DeclarationSource, FormalStatement, declaration_statements
from .declaration_ancestry import ProjectedStatement, compile_ancestry
from .declaration_cfel import (
    filters as _filters,
    intersect_selectors, segments as _segments, selector_key,
)


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
    format_source: DeclarationSource | None = None
    provenance: tuple[DeclarationSource, ...] = ()


def header_declaration_rules(row: Mapping[str, Any] | None) -> tuple[HeaderRule, ...]:
    """Compile one source's raw literal Header declaration contributions."""
    return _header_rules(
        ProjectedStatement(statement, source) for statement, source in declaration_statements(row)
    )


def _header_rules(statements: Iterable[ProjectedStatement[DeclarationSource]]) -> tuple[HeaderRule, ...]:
    rules = set()
    for projected in statements:
        try:
            parsed = _statement(projected.statement)
        except ValueError as error:
            raise ValueError(f"{projected.source.source_path}: {error}") from error
        if parsed is not None:
            rules.add(HeaderRule(
                parsed.path, parsed.format,
                intersect_selectors(parsed.roles, projected.roles),
                intersect_selectors(parsed.forms, projected.forms),
                projected.source, provenance=tuple(dict.fromkeys(projected.provenance[:-1])),
            ))
    return tuple(sorted(rules, key=_rule_key))


def compile_header_rules(rows: Sequence[Mapping[str, Any]]) -> tuple[HeaderRule, ...]:
    """Compile supplied declarations after resolving their merged raw contributions."""
    return header_rules_from_statements(
        statement for row in rows for statement in declaration_statements(row)
    )


def header_rules_from_statements(statements: Iterable[FormalStatement]) -> tuple[HeaderRule, ...]:
    return resolve_header_rules(_header_rules(compile_ancestry(statements)))


def resolve_header_rules(rules: Iterable[HeaderRule]) -> tuple[HeaderRule, ...]:
    """Apply wildcard formats to named children without replacing either rule."""
    raw = tuple(rules)
    typed = [rule for rule in raw if rule.format is not None and rule.path[-1:] != ("*",)]
    inherited: list[HeaderRule] = []
    for child in raw:
        if child.path[-1:] == ("*",):
            continue
        for wildcard in raw:
            if wildcard.path != (*child.path[:-1], "*") or wildcard.format is None:
                continue
            roles = intersect_selectors(child.roles, wildcard.roles)
            forms = intersect_selectors(child.forms, wildcard.forms)
            if roles != frozenset() and forms != frozenset():
                provenance = tuple(dict.fromkeys((*child.provenance, *wildcard.provenance)))
                inherited.append(HeaderRule(child.path, wildcard.format, roles, forms, child.source, wildcard.source, provenance))
    return tuple(sorted(set((*typed, *inherited)), key=_rule_key))


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


def _rule_key(rule: HeaderRule) -> tuple[object, ...]:
    source = rule.source
    return (
        rule.path, rule.format or "", selector_key(rule.roles), selector_key(rule.forms),
        source.reference or "", source.version or -1, source.source_path or "",
        (rule.format_source.reference or "") if rule.format_source else "",
        (rule.format_source.version or -1) if rule.format_source else -1,
        (rule.format_source.source_path or "") if rule.format_source else "",
        tuple((s.reference or "", s.version or -1, s.source_path or "") for s in rule.provenance),
    )
