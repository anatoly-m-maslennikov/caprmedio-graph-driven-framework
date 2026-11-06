# CA-R-2726@5
# CA-M-465@19
# CA-M-500@2
# CA-D-672@12

"""Build the Workbench Header SQL schema from raw source Headers."""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from dataclasses import dataclass, field
import datetime as dt
import json
from pathlib import Path
import re
from typing import Any

from .relations import canonical, json_value


_NAME = re.compile(r"[^a-z0-9_]")
_SEPARATORS = re.compile(r"[\s-]+")


@dataclass(frozen=True)
class HeaderColumn:
    """One source-faithful scalar or collection Header leaf."""

    path: tuple[str, ...]
    name: str
    format: str
    populated: bool


@dataclass(frozen=True)
class HeaderSchema:
    """The derived, reproducible Header part of the public atoms schema."""

    columns: tuple[HeaderColumn, ...]

    @property
    def names(self) -> tuple[str, ...]:
        return tuple(column.name for column in self.columns)

    @property
    def json_names(self) -> frozenset[str]:
        return frozenset(column.name for column in self.columns if column.format == "JSON")

    @property
    def status_names(self) -> tuple[str, ...]:
        return tuple(
            column.name for column in self.columns
            if column.path[-1:] == ("status",) and column.format == "VARCHAR"
        )

    def value(self, header: object, column: HeaderColumn) -> Any:
        value: Any = header
        for key in column.path:
            if not isinstance(value, Mapping) or key not in value:
                return None
            value = value[key]
        return value

    def asset(self) -> dict[str, object]:
        return {
            "version": 1,
            "header_columns": [
                {
                    "path": list(column.path), "name": column.name, "format": column.format,
                    "populated": column.populated,
                }
                for column in self.columns
            ],
        }

    def write(self, path: Path | None) -> None:
        if path is not None:
            path.write_text(json.dumps(self.asset(), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


@dataclass(frozen=True)
class _Contribution:
    values: tuple[tuple[tuple[str, ...], str | None, bool], ...]
    direct: frozenset[tuple[str, ...]]


@dataclass(frozen=True)
class HeaderSchemaState:
    """Owner-local Header observations, updated without reading unchanged Headers."""

    contributions: Mapping[str, _Contribution] = field(default_factory=dict)
    direct_counts: Mapping[tuple[str, ...], int] = field(default_factory=dict)
    format_counts: Mapping[tuple[str, ...], Mapping[str, int]] = field(default_factory=dict)
    populated_counts: Mapping[tuple[str, ...], int] = field(default_factory=dict)

    @classmethod
    def from_atoms(cls, atom_rows: Sequence[Mapping[str, Any]]) -> HeaderSchemaState:
        delta = {}
        for index, row in enumerate(atom_rows):
            key = _source_key(row, index)
            delta[key if key not in delta else f"<row:{index}>"] = row
        return cls().updated(delta)

    @property
    def schema(self) -> HeaderSchema:
        names: dict[str, tuple[str, ...]] = {}
        columns = []
        for path in sorted(self.direct_counts, key=_column_name):
            name = _column_name(path)
            previous = names.setdefault(name, path)
            if previous != path:
                raise ValueError(
                    f"Header SQL column collision: {'.'.join(previous)} and {'.'.join(path)} -> {name}"
                )
            formats = self.format_counts.get(path, {})
            columns.append(HeaderColumn(
                path, name, next(iter(formats)) if len(formats) == 1 else "JSON",
                self.populated_counts.get(path, 0) > 0,
            ))
        return HeaderSchema(tuple(columns))

    def updated(self, delta: Mapping[str, Mapping[str, Any] | None]) -> HeaderSchemaState:
        """Return a candidate state after changed or removed raw source rows."""
        contributions = dict(self.contributions)
        direct_counts = dict(self.direct_counts)
        format_counts = {path: dict(counts) for path, counts in self.format_counts.items()}
        populated_counts = dict(self.populated_counts)
        for source_path, row in delta.items():
            if not isinstance(source_path, str) or not source_path:
                raise ValueError("Header source path must be a non-empty string")
            if previous := contributions.pop(source_path, None):
                _remove(previous, direct_counts, format_counts, populated_counts)
            if row is not None:
                contribution = _contribution(row)
                if contribution is not None:
                    contributions[source_path] = contribution
                    _add(contribution, direct_counts, format_counts, populated_counts)
        return HeaderSchemaState(contributions, direct_counts, format_counts, populated_counts)


def schema_asset_path(database_path: Path | None) -> Path | None:
    return database_path.parent / "projection-schema.json" if database_path is not None else None


def infer_header_schema(atom_rows: Sequence[Mapping[str, Any]]) -> HeaderSchema:
    """Return every observed actual Header leaf; relations stay graph materialized."""
    return HeaderSchemaState.from_atoms(atom_rows).schema


def _source_key(row: Mapping[str, Any], index: int) -> str:
    path = row.get("source_path")
    return path if isinstance(path, str) and path else f"<row:{index}>"


def _contribution(row: Mapping[str, Any]) -> _Contribution | None:
    header = row.get("header_json")
    if not isinstance(header, Mapping):
        return None
    values: list[tuple[tuple[str, ...], str | None, bool]] = []
    direct: set[tuple[str, ...]] = set()
    _collect_contribution(header, values, direct)
    return _Contribution(tuple(values), frozenset(direct))


def _collect_contribution(
    value: Mapping[str, Any], values: list[tuple[tuple[str, ...], str | None, bool]],
    direct: set[tuple[str, ...]], prefix: tuple[str, ...] = (),
) -> None:
    for key, item in value.items():
        if not isinstance(key, str):
            raise ValueError("Header SQL properties require string keys")
        path = (*prefix, key)
        if not path[:-1] and key == "relations":
            continue
        values.append((path, _value_format(item) if item is not None else None, not _empty(item)))
        if isinstance(item, Mapping):
            if item:
                _collect_contribution(item, values, direct, path)
            else:
                direct.add(path)
        else:
            direct.add(path)


def _add(
    contribution: _Contribution, direct_counts: dict[tuple[str, ...], int],
    format_counts: dict[tuple[str, ...], dict[str, int]], populated_counts: dict[tuple[str, ...], int],
) -> None:
    for path in contribution.direct:
        direct_counts[path] = direct_counts.get(path, 0) + 1
    for path, format_name, populated in contribution.values:
        if format_name is not None:
            formats = format_counts.setdefault(path, {})
            formats[format_name] = formats.get(format_name, 0) + 1
        if populated:
            populated_counts[path] = populated_counts.get(path, 0) + 1


def _remove(
    contribution: _Contribution, direct_counts: dict[tuple[str, ...], int],
    format_counts: dict[tuple[str, ...], dict[str, int]], populated_counts: dict[tuple[str, ...], int],
) -> None:
    for path in contribution.direct:
        _decrement(direct_counts, path)
    for path, format_name, populated in contribution.values:
        if format_name is not None:
            formats = format_counts[path]
            _decrement(formats, format_name)
            if not formats:
                format_counts.pop(path)
        if populated:
            _decrement(populated_counts, path)


def _decrement(counts: dict[Any, int], key: Any) -> None:
    if counts[key] == 1:
        counts.pop(key)
    else:
        counts[key] -= 1


def _column_name(path: tuple[str, ...]) -> str:
    parts = []
    for part in path:
        normalized = _NAME.sub("", _SEPARATORS.sub("_", part.casefold())).strip("_")
        if not normalized:
            raise ValueError(f"Header SQL property has no usable name: {'.'.join(path)}")
        parts.append(normalized)
    return "header_" + "_".join(parts)


def _empty(value: object) -> bool:
    return value is None or value == "" or value == [] or value == {}


def _value_format(value: object) -> str:
    if type(value) is bool:
        return "BOOLEAN"
    if type(value) is int and -(2**63) <= value < 2**63:
        return "BIGINT"
    if type(value) is float:
        return "DOUBLE"
    if isinstance(value, str):
        return "VARCHAR"
    if isinstance(value, dt.datetime):
        return "TIMESTAMPTZ" if value.tzinfo is not None else "TIMESTAMP"
    if isinstance(value, dt.date):
        return "DATE"
    if isinstance(value, dt.time):
        return "TIME"
    try:
        canonical(json_value(value))
    except (TypeError, ValueError) as exc:
        raise ValueError(f"Header SQL property has unsupported value: {value!r}") from exc
    return "JSON"
