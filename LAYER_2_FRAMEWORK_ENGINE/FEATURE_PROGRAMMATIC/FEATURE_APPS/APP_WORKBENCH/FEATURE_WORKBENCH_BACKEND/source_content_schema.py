# CA-R-2726@5
# CA-M-500@1
# CA-D-672@12

"""Retain the compiled Content schema used to validate changed source Atoms."""

from __future__ import annotations

from collections.abc import Iterable, Mapping
from dataclasses import dataclass, field
from typing import Any

from .content_columns import content_columns
from .content_schema import ContentSchema, compile_content_schema


RuleShape = tuple[tuple[str, ...], tuple[str, ...], tuple[str, ...], bool]


@dataclass
class SourceContentSchema:
    """Keep Content declarations in memory; source files remain authoritative."""

    schema: ContentSchema | None = None
    _contributions: dict[str, frozenset[RuleShape]] = field(default_factory=dict)

    def reset(self) -> None:
        self.schema = None
        self._contributions.clear()

    def rebuild(self, rows: Iterable[Mapping[str, Any]]) -> dict[str, ValueError]:
        """Compile valid rows, excluding only rows with duplicate declared headings."""
        remaining = list(rows)
        errors: dict[str, ValueError] = {}
        while True:
            schema = compile_content_schema(remaining)
            invalid = self.validation_errors(remaining, schema)
            if not invalid:
                self.schema = schema
                self._contributions = {}
                for row in remaining:
                    path = source_path(row)
                    shape = contribution(row)
                    if path is not None and shape:
                        self._contributions[path] = shape
                return errors
            errors.update(invalid)
            remaining = [row for row in remaining if source_path(row) not in invalid]

    def changes_schema(self, rows: Mapping[str, Mapping[str, Any] | None]) -> bool:
        """Compare only changed declaration rules, not declaration provenance."""
        if self.schema is None:
            return True
        contributions = dict(self._contributions)
        try:
            for path, row in rows.items():
                shape = contribution(row) if row is not None else frozenset()
                if shape:
                    contributions[path] = shape
                else:
                    contributions.pop(path, None)
        except ValueError:
            return True
        return union(contributions.values()) != shape_of(self.schema)

    def validation_errors(
        self, rows: Iterable[Mapping[str, Any]], schema: ContentSchema | None = None,
    ) -> dict[str, ValueError]:
        active_schema = schema or self.schema
        if active_schema is None:
            return {}
        errors: dict[str, ValueError] = {}
        for row in rows:
            path = source_path(row)
            if path is None:
                continue
            try:
                content_columns(row, active_schema)
            except ValueError as error:
                errors[path] = error
        return errors


def source_path(row: Mapping[str, Any]) -> str | None:
    value = row.get("source_path")
    return value if isinstance(value, str) else None


def contribution(row: Mapping[str, Any] | None) -> frozenset[RuleShape]:
    if row is None:
        return frozenset()
    return frozenset(
        (rule.path, tuple(sorted(rule.roles or ())), tuple(sorted(rule.forms or ())), rule.value_bearing)
        for rule in compile_content_schema([row]).rules
    )


def union(values: Iterable[frozenset[RuleShape]]) -> frozenset[RuleShape]:
    return frozenset().union(*values)


def shape_of(schema: ContentSchema) -> frozenset[RuleShape]:
    return frozenset(
        (rule.path, tuple(sorted(rule.roles or ())), tuple(sorted(rule.forms or ())), rule.value_bearing)
        for rule in schema.rules
    )
