# CA-R-2726@6
# CA-M-465@24
# CA-M-500@3
# CA-D-672@14

"""Retain the compiled Content schema used to validate changed source Atoms."""

from __future__ import annotations

from collections.abc import Iterable, Mapping
from collections import Counter
from dataclasses import dataclass, field
from typing import Any

from .content_schema import ContentRule, ContentSchema, declaration_rules, observed_paths, schema_from_rules


Observation = tuple[str | None, str | None, tuple[str, ...]]


@dataclass
class SourceContentSchema:
    """Keep Content declarations in memory; source files remain authoritative."""

    schema: ContentSchema | None = None
    _contributions: dict[str, tuple[ContentRule, ...]] = field(default_factory=dict)
    _observations: dict[str, frozenset[Observation]] = field(default_factory=dict)
    _counts: Counter[Observation] = field(default_factory=Counter)

    def reset(self) -> None:
        self.schema = None
        self._contributions.clear()
        self._observations.clear()
        self._counts.clear()

    def rebuild(self, rows: Iterable[Mapping[str, Any]]) -> dict[str, ValueError]:
        """Compile valid rows, excluding only rows with duplicate declared headings."""
        remaining = list(rows)
        errors: dict[str, ValueError] = {}
        while True:
            contributions = _contributions(remaining)
            observations = {
                path: observed_paths(row)
                for row in remaining if (path := source_path(row)) is not None
            }
            counts: Counter[Observation] = Counter(
                item for items in observations.values() for item in items
            )
            schema = schema_from_rules(
                (rule for rules in contributions.values() for rule in rules), counts,
            )
            invalid = self.validation_errors(remaining, schema)
            if not invalid:
                self.schema = schema
                self._contributions = contributions
                self._observations = observations
                self._counts = counts
                return errors
            errors.update(invalid)
            remaining = [row for row in remaining if source_path(row) not in invalid]

    def changes_schema(self, rows: Mapping[str, Mapping[str, Any] | None]) -> bool:
        """Compare only changed declaration rules, not declaration provenance."""
        if self.schema is None:
            return True
        try:
            schema, _contributions, _observations, _counts = self._candidate(rows)
        except ValueError:
            return True
        return schema.shape != self.schema.shape

    def update(self, rows: Mapping[str, Mapping[str, Any] | None]) -> bool:
        """Commit changed declaration provenance unless its schema shape changed."""
        if self.schema is None:
            return True
        try:
            schema, contributions, observations, counts = self._candidate(rows)
        except ValueError:
            return True
        if schema.shape != self.schema.shape:
            return True
        self.schema = schema
        self._contributions = contributions
        for path, items in observations.items():
            if items:
                self._observations[path] = items
            else:
                self._observations.pop(path, None)
        self._counts = counts
        return False

    def _candidate(
        self, rows: Mapping[str, Mapping[str, Any] | None],
    ) -> tuple[
        ContentSchema, dict[str, tuple[ContentRule, ...]],
        dict[str, frozenset[Observation]], Counter[Observation],
    ]:
        contributions = dict(self._contributions)
        counts = self._counts.copy()
        observations: dict[str, frozenset[Observation]] = {}
        for path, row in rows.items():
            counts.subtract(self._observations.get(path, ()))
            items = observed_paths(row) if row is not None else frozenset()
            observations[path] = items
            counts.update(items)
            rules = declaration_rules(row)
            if rules:
                contributions[path] = rules
            else:
                contributions.pop(path, None)
        counts += Counter()
        schema = schema_from_rules(
            (rule for rules in contributions.values() for rule in rules), counts,
        )
        return schema, contributions, observations, counts

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
                active_schema.validate(row)
            except ValueError as error:
                errors[path] = error
        return errors


def source_path(row: Mapping[str, Any]) -> str | None:
    value = row.get("source_path")
    return value if isinstance(value, str) else None


def _contributions(rows: Iterable[Mapping[str, Any]]) -> dict[str, tuple[ContentRule, ...]]:
    return {
        path: rules
        for row in rows
        if (path := source_path(row)) is not None and (rules := declaration_rules(row))
    }
