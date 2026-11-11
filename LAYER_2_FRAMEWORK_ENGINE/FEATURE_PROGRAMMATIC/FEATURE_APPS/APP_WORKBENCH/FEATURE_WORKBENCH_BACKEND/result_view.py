# CA-R-2953@5

"""Validate a read-only grid request and compile native cached-result reads."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from .graph_store import quote_identifier


@dataclass(frozen=True)
class Sort:
    column: int
    direction: str


@dataclass(frozen=True)
class Contains:
    column: int
    value: str


@dataclass(frozen=True)
class Grid:
    sort: tuple[Sort, ...]
    filters: tuple[Contains, ...]
    group_by: Sort | None


@dataclass(frozen=True)
class PageQuery:
    count_sql: str
    count_parameters: tuple[str, ...]
    page_sql: str
    page_parameters: tuple[Any, ...]
    group_column: int | None


EMPTY_GRID = Grid((), (), None)


def ctas_source_sql(sql: str) -> str:
    """Remove only DuckDB's final statement delimiter from derived relation SQL."""

    import duckdb

    raw = sql.encode("utf-8")
    tokens = duckdb.tokenize(sql)
    meaningful = [index for index, (_, kind) in enumerate(tokens) if kind != duckdb.token_type.comment]
    if not meaningful:
        return sql
    offset = tokens[meaningful[-1]][0]
    if raw[offset:offset + 1] != b";":
        return sql
    return (raw[:offset] + raw[offset + 1:]).decode("utf-8")


def _column(value: object, *, name: str) -> int:
    if type(value) is not int or value < 0:
        raise ValueError(f"grid {name} must be a non-negative integer")
    return value


def _direction(value: object) -> str:
    if type(value) is not str or value not in {"asc", "desc"}:
        raise ValueError("grid direction must be asc or desc")
    return value


def _sort(value: object) -> Sort:
    if type(value) is not dict or set(value) != {"column", "direction"}:
        raise ValueError("grid sort must contain exactly column and direction")
    return Sort(_column(value["column"], name="column"), _direction(value["direction"]))


def _filter(value: object) -> Contains:
    if type(value) is not dict or set(value) != {"column", "operator", "value"}:
        raise ValueError("grid filter must contain exactly column, operator and value")
    if value["operator"] != "contains":
        raise ValueError("grid operator must be contains")
    if type(value["value"]) is not str:
        raise ValueError("grid filter value must be a string")
    return Contains(_column(value["column"], name="column"), value["value"])


def parse_grid(value: object) -> Grid:
    """Reject malformed public grid data without touching a result table."""

    if value is None:
        return EMPTY_GRID
    if type(value) is not dict or set(value) - {"sort", "filters", "group_by"}:
        raise ValueError("grid must contain only sort, filters and group_by")
    sort = value.get("sort", [])
    filters = value.get("filters", [])
    group_by = value.get("group_by")
    if type(sort) is not list or type(filters) is not list:
        raise ValueError("grid sort and filters must be lists")
    if "group_by" in value and type(group_by) is not dict:
        raise ValueError("grid group_by must be an object")
    return Grid(tuple(_sort(item) for item in sort), tuple(_filter(item) for item in filters),
                _sort(group_by) if group_by is not None else None)


def validate_columns(grid: Grid, column_count: int) -> None:
    """Validate zero-based public positions after result metadata is available."""

    for entry in (*grid.sort, *grid.filters, *((grid.group_by,) if grid.group_by else ())):
        if entry.column >= column_count:
            raise ValueError("grid column is out of range")


def build_page_query(
    table: str, stored_columns: tuple[str, ...], grid: Grid, *, page_size: int, offset: int,
) -> PageQuery:
    """Compile parameterized native reads over exactly one cached result table."""

    private, *public = stored_columns
    result_table = f"workbench_results.{quote_identifier(table)}"
    view = f"result_view AS (SELECT * FROM {result_table})"

    def physical(column: int, *, qualified: bool) -> str:
        name = quote_identifier(public[column])
        return f"result_view.{name}" if qualified else name

    predicates = [
        f"instr(lower(CAST({physical(item.column, qualified=True)} AS VARCHAR)), lower(?)) > 0"
        for item in grid.filters
    ]
    filtered = "filtered AS (SELECT * FROM result_view"
    if predicates:
        filtered += " WHERE " + " AND ".join(predicates)
    filtered += ")"
    prefix = f"WITH {view}, {filtered}"
    parameters = tuple(item.value for item in grid.filters)

    order: list[str] = []
    if grid.group_by is not None:
        order.append(f"{physical(grid.group_by.column, qualified=False)} {grid.group_by.direction.upper()} NULLS LAST")
    order.extend(
        f"{physical(item.column, qualified=False)} {item.direction.upper()} NULLS LAST"
        for item in grid.sort
    )
    order.append(f"{quote_identifier(private)} ASC")
    if grid.group_by is None:
        page_sql = f"{prefix} SELECT * FROM filtered ORDER BY {', '.join(order)} LIMIT ? OFFSET ?"
    else:
        group_count = quote_identifier(f"__workbench_group_count_{table.removeprefix('query_')}")
        grouped = (
            "ranked AS (SELECT *, COUNT(*) OVER (PARTITION BY "
            f"{physical(grid.group_by.column, qualified=False)}) AS {group_count} FROM filtered)"
        )
        page_sql = f"{prefix}, {grouped} SELECT * FROM ranked ORDER BY {', '.join(order)} LIMIT ? OFFSET ?"
    return PageQuery(
        count_sql=f"{prefix} SELECT count(*) FROM filtered",
        count_parameters=parameters,
        page_sql=page_sql,
        page_parameters=(*parameters, page_size, offset),
        group_column=grid.group_by.column if grid.group_by is not None else None,
    )
