# CA-R-2726@6
# CA-M-500@3
# CA-D-672@14

"""Build the Workbench Header SQL schema from raw source Headers."""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from dataclasses import dataclass, field
import datetime as dt
import json
from pathlib import Path
import re
import sys
from typing import Any

from .relations import canonical, json_value


TOOLS = Path(__file__).resolve().parents[3] / "FEATURE_TOOLS"
if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))

from header_groups import header_field_paths, header_value  # noqa: E402

from .declared_header_rules import HeaderRule, compile_header_rules


_NAME = re.compile(r"[^a-z0-9_]")
_SEPARATORS = re.compile(r"[\s-]+")


@dataclass(frozen=True)
class HeaderColumn:
    """One source-faithful Header value."""

    path: tuple[str, ...]
    name: str
    format: str
    populated: bool
    reader: str | None = None
    rules: tuple[HeaderRule, ...] = ()

    def applies(self, row: Mapping[str, Any]) -> bool:
        return not self.rules or any(_rule_applies(rule, row) for rule in self.rules)


@dataclass(frozen=True)
class HeaderSchema:
    """The derived, reproducible Header part of the public atoms schema."""

    columns: tuple[HeaderColumn, ...]

    @property
    def shape(self) -> tuple[tuple[object, ...], ...]:
        """Table shape without declaration provenance."""
        return tuple(
            (
                column.path, column.name, column.format, column.populated, column.reader,
                tuple(sorted(_rule_shape(rule) for rule in column.rules)),
            )
            for column in self.columns
        )

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

    def value(self, row: Mapping[str, Any], column: HeaderColumn) -> Any:
        if not column.applies(row):
            return None
        header = row.get("header_json")
        if column.reader is not None:
            if not isinstance(header, dict):
                return None
            present, value = header_value(header, column.reader)
            if not present:
                return None
            if column.format == "TIMESTAMPTZ":
                timestamp = dt.datetime.fromisoformat(value.replace("Z", "+00:00")) if isinstance(value, str) else value
                if isinstance(timestamp, dt.datetime) and (timestamp.tzinfo is None or timestamp.utcoffset() is None):
                    raise ValueError(f"Header {column.reader} requires an offset-bearing timestamp")
                return timestamp
            return value
        value: Any = header
        for key in column.path:
            if not isinstance(value, Mapping) or key not in value:
                return None
            value = value[key]
        return value

    def validate(self, row: Mapping[str, Any]) -> None:
        """Reject only a value that cannot occupy its literal declared SQL type."""
        for column in self.columns:
            value = self.value(row, column)
            if value is not None and not _matches_format(value, column.format):
                raise ValueError(f"Header {column.name} requires {column.format}")

    def asset(self) -> dict[str, object]:
        return {
            "version": 1,
            "header_columns": [
                {
                    "path": list(column.path), "name": column.name, "format": column.format,
                    "populated": column.populated, "reader": column.reader,
                    **({"rules": [_rule_asset(rule) for rule in column.rules]} if column.rules else {}),
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
    """Owner-local Header aggregates, updated from exact materialized deltas."""

    direct_counts: Mapping[tuple[str, ...], int] = field(default_factory=dict)
    format_counts: Mapping[tuple[str, ...], Mapping[str, int]] = field(default_factory=dict)
    populated_counts: Mapping[tuple[str, ...], int] = field(default_factory=dict)

    @classmethod
    def from_atoms(cls, atom_rows: Sequence[Mapping[str, Any]]) -> HeaderSchemaState:
        new_rows = {}
        for index, row in enumerate(atom_rows):
            key = _source_key(row, index)
            new_rows[key if key not in new_rows else f"<row:{index}>"] = row
        return cls().updated({}, new_rows)

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

    def updated(
        self, old_rows: Mapping[str, Mapping[str, Any]], new_rows: Mapping[str, Mapping[str, Any]],
    ) -> HeaderSchemaState:
        """Return a candidate state after subtracting old and adding new source rows."""
        direct_counts = dict(self.direct_counts)
        format_counts = {path: dict(counts) for path, counts in self.format_counts.items()}
        populated_counts = dict(self.populated_counts)
        for rows, update in ((old_rows, _remove), (new_rows, _add)):
            for source_path, row in rows.items():
                if not isinstance(source_path, str) or not source_path:
                    raise ValueError("Header source path must be a non-empty string")
                if (contribution := _contribution(row)) is not None:
                    update(contribution, direct_counts, format_counts, populated_counts)
        return HeaderSchemaState(direct_counts, format_counts, populated_counts)


def schema_asset_path(database_path: Path | None) -> Path | None:
    return database_path.parent / "projection-schema.json" if database_path is not None else None


def infer_header_schema(atom_rows: Sequence[Mapping[str, Any]]) -> HeaderSchema:
    """Return observed Header columns; relations stay graph materialized."""
    return HeaderSchemaState.from_atoms(atom_rows).schema


def declared_header_schema(rules: Sequence[HeaderRule]) -> HeaderSchema:
    """Bind only literal model Header declarations to the shared carrier adapter."""
    grouped: dict[tuple[tuple[str, ...], str, str, str], list[HeaderRule]] = {}
    names: dict[str, tuple[tuple[str, ...], str, str]] = {}
    for rule in rules:
        if rule.format is None:
            continue
        reader = _reader_name(rule)
        if reader == "relations":
            continue
        path = header_field_paths(reader, _selector_metadata(rule))[0]
        name = _column_name(path)
        previous = names.setdefault(name, (path, rule.format, reader))
        if previous != (path, rule.format, reader):
            raise ValueError(
                f"Header SQL declaration collision: {name} has incompatible model declarations"
            )
        grouped.setdefault((path, name, rule.format, reader), []).append(rule)
    return HeaderSchema(tuple(
        HeaderColumn(path, name, format_name, False, reader, tuple(sorted(set(column_rules), key=_rule_key)))
        for (path, name, format_name, reader), column_rules in sorted(grouped.items(), key=lambda item: item[0][1])
    ))


def header_schema_for_mode(
    mode: int, atom_rows: Sequence[Mapping[str, Any]], *, header_rules: Sequence[HeaderRule] | None = None,
) -> HeaderSchema:
    """Compile exactly the selected cold-start Header projection."""
    if mode == 1:
        return declared_header_schema(
            compile_header_rules(atom_rows) if header_rules is None else header_rules
        )
    if mode == 2:
        return infer_header_schema(atom_rows)
    raise ValueError("workbench.schema_mode must be 1 or 2")


def _reader_name(rule: HeaderRule) -> str:
    return "atom_id" if rule.path == ("id",) else ".".join(rule.path)


def _selector_metadata(rule: HeaderRule) -> dict[str, Any]:
    if rule.roles is None or len(rule.roles) != 1:
        return {}
    return {"context": {"role": next(iter(rule.roles))}}


def _rule_applies(rule: HeaderRule, row: Mapping[str, Any]) -> bool:
    return (
        (rule.roles is None or row.get("role") in rule.roles)
        and (rule.forms is None or row.get("form") in rule.forms)
    )


def _rule_shape(rule: HeaderRule) -> tuple[object, ...]:
    return rule.path, rule.format, tuple(sorted(rule.roles or ())), tuple(sorted(rule.forms or ()))


def _rule_key(rule: HeaderRule) -> tuple[object, ...]:
    return *_rule_shape(rule), rule.source.reference or "", rule.source.version or -1, rule.source.source_path or ""


def _rule_asset(rule: HeaderRule) -> dict[str, object]:
    return {
        "path": list(rule.path), "format": rule.format,
        "roles": sorted(rule.roles) if rule.roles is not None else None,
        "forms": sorted(rule.forms) if rule.forms is not None else None,
        "source": rule.source.asset(),
    }


def _matches_format(value: object, format_name: str) -> bool:
    if format_name == "VARCHAR":
        return isinstance(value, str)
    if format_name == "BIGINT":
        return type(value) is int and -(2**63) <= value < 2**63
    if format_name == "BOOLEAN":
        return type(value) is bool
    if format_name == "TIMESTAMPTZ":
        return isinstance(value, dt.datetime) and value.tzinfo is not None and value.utcoffset() is not None
    if format_name != "JSON":
        return False
    try:
        canonical(json_value(value))
    except (TypeError, ValueError):
        return False
    return True


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
        if path == ("context", "container"):
            direct.add(path)
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
    return "header." + ".".join(parts)


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
