# CA-M-500@3
# CA-D-672@14

"""Retain literal Header declaration contributions between source deltas."""

from __future__ import annotations

from collections.abc import Iterable, Mapping
from dataclasses import dataclass, field
from typing import Any

from .declared_header_rules import HeaderRule, header_declaration_rules, resolve_header_rules
from .header_columns import HeaderSchema, declared_header_schema


@dataclass
class SourceHeaderSchema:
    """Cache per-source model Header declarations; source files remain authoritative."""

    schema: HeaderSchema | None = None
    _contributions: dict[str, tuple[HeaderRule, ...]] = field(default_factory=dict)

    def reset(self) -> None:
        self.schema = None
        self._contributions.clear()

    def rebuild(self, rows: Iterable[Mapping[str, Any]]) -> None:
        self._contributions = _contributions(rows)
        self.schema = _schema(self._contributions)

    def update(
        self, rows: Mapping[str, Mapping[str, Any] | None], *, accept_shape: bool = False,
    ) -> bool:
        """Commit exact changed contributions; report a table-shape boundary."""
        if self.schema is None:
            return True
        contributions = dict(self._contributions)
        for path, row in rows.items():
            rules = _rules(path, row)
            if rules:
                contributions[path] = rules
            else:
                contributions.pop(path, None)
        schema = _schema(contributions)
        changed = schema.shape != self.schema.shape
        if changed and not accept_shape:
            return True
        self._contributions = contributions
        self.schema = schema
        return changed

    def validation_errors(self, rows: Iterable[Mapping[str, Any]]) -> dict[str, ValueError]:
        if self.schema is None:
            return {}
        errors = {}
        for row in rows:
            path = row.get("source_path")
            if not isinstance(path, str):
                continue
            try:
                self.schema.validate(row)
            except ValueError as error:
                errors[path] = error
        return errors


def _contributions(rows: Iterable[Mapping[str, Any]]) -> dict[str, tuple[HeaderRule, ...]]:
    result = {}
    for row in rows:
        path = row.get("source_path")
        rules = _rules(path, row)
        if isinstance(path, str) and rules:
            result[path] = rules
    return result


def _schema(contributions: Mapping[str, tuple[HeaderRule, ...]]) -> HeaderSchema:
    return declared_header_schema(resolve_header_rules(
        rule for rules in contributions.values() for rule in rules
    ))


def _rules(path: object, row: Mapping[str, Any] | None) -> tuple[HeaderRule, ...]:
    try:
        return header_declaration_rules(row)
    except ValueError as error:
        raise ValueError(f"{path}: {error}") from error
