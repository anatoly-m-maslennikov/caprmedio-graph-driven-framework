# CA-R-2726@5
# CA-M-500@1
# CA-D-672@12

"""Build the Workbench Header SQL schema from raw source Headers."""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from dataclasses import dataclass
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


def schema_asset_path(database_path: Path | None) -> Path | None:
    return database_path.parent / "projection-schema.json" if database_path is not None else None


def infer_header_schema(atom_rows: Sequence[Mapping[str, Any]]) -> HeaderSchema:
    """Return every observed actual Header leaf; relations stay graph materialized."""
    values: dict[tuple[str, ...], list[Any]] = {}
    direct: set[tuple[str, ...]] = set()
    names: dict[str, tuple[str, ...]] = {}
    for row in atom_rows:
        header = row.get("header_json")
        if not isinstance(header, Mapping):
            continue
        _collect(header, values, direct)
    for path in direct:
        name = _column_name(path)
        previous = names.setdefault(name, path)
        if previous != path:
            raise ValueError(
                f"Header SQL column collision: {'.'.join(previous)} and {'.'.join(path)} -> {name}"
            )
    return HeaderSchema(tuple(
        HeaderColumn(
            path, _column_name(path), _format(values[path]), any(not _empty(value) for value in values[path]),
        )
        for path in sorted(direct, key=_column_name)
    ))


def _collect(
    value: Mapping[str, Any], values: dict[tuple[str, ...], list[Any]],
    direct: set[tuple[str, ...]], prefix: tuple[str, ...] = (),
) -> None:
    for key, item in value.items():
        if not isinstance(key, str):
            raise ValueError("Header SQL properties require string keys")
        path = (*prefix, key)
        if not path[:-1] and key == "relations":
            continue
        values.setdefault(path, []).append(item)
        if isinstance(item, Mapping):
            if item:
                _collect(item, values, direct, path)
            else:
                direct.add(path)
        else:
            direct.add(path)


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


def _format(values: Sequence[Any]) -> str:
    formats = {_value_format(value) for value in values if value is not None}
    return formats.pop() if len(formats) == 1 else "JSON"


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
