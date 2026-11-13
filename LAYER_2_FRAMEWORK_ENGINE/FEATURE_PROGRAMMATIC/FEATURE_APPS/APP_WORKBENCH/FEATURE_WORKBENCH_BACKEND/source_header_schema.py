# CA-M-500@12
# CA-D-672@22

"""Retain literal Header declaration contributions between source deltas."""

from __future__ import annotations

from collections.abc import Iterable, Mapping
from dataclasses import dataclass, field
from typing import Any

from .content_schema import FormalStatement
from .declared_header_rules import header_rules_from_statements
from .header_columns import HeaderSchema, declared_header_schema
from .source_content_schema import declaration_contributions, updated_declarations


@dataclass
class SourceHeaderSchema:
    """Cache per-source model Header declarations; source files remain authoritative."""

    schema: HeaderSchema | None = None
    _contributions: dict[str, tuple[FormalStatement, ...]] = field(default_factory=dict)

    def reset(self) -> None:
        self.schema = None
        self._contributions.clear()

    def rebuild(self, rows: Iterable[Mapping[str, Any]]) -> None:
        self._contributions = declaration_contributions(rows)
        self.schema = _schema(self._contributions)

    def update(
        self, rows: Mapping[str, Mapping[str, Any] | None], *, accept_shape: bool = False,
    ) -> bool:
        """Commit exact changed contributions; report a table-shape boundary."""
        if self.schema is None:
            return True
        contributions = updated_declarations(self._contributions, rows)
        if contributions is self._contributions:
            return False
        schema = _schema(contributions)
        changed = schema.shape != self.schema.shape
        if changed and not accept_shape:
            return True
        self._contributions = contributions
        self.schema = schema
        return changed

    def validation_errors(
        self, rows: Iterable[Mapping[str, Any]], *, schema: HeaderSchema | None = None,
    ) -> dict[str, ValueError]:
        active_schema = schema if schema is not None else self.schema
        if active_schema is None:
            return {}
        errors = {}
        for row in rows:
            path = row.get("source_path")
            if not isinstance(path, str):
                continue
            try:
                root_header = row.get("_project_root_header")
                active_schema.validate(row if root_header is None else dict(row, header_json=root_header))
            except ValueError as error:
                errors[path] = error
        return errors


def _schema(contributions: Mapping[str, tuple[FormalStatement, ...]]) -> HeaderSchema:
    return declared_header_schema(header_rules_from_statements(
        statement for statements in contributions.values() for statement in statements
    ))
