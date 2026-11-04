# CA-R-2725@2
# CA-R-2728@2
# CA-R-2729@2
# CA-M-462@5
# CA-M-463@2
# CA-M-464@4
# CA-M-465@7
# CA-D-672@6
# CA-D-673@4
# CA-D-675@4

"""The in-memory DuckDB and DuckPGQ owner for Workbench queries."""

from __future__ import annotations

import base64
import datetime as dt
import json
import math
import sys
import threading
from collections.abc import Mapping
from decimal import Decimal
from pathlib import Path
from typing import Any

from .graph_store import build_graph


_SAFE_INTEGER = 2**53 - 1
_UNREPRESENTABLE = object()
_ATOM_FIELDS = (
    "source_path", "status_group", "id", "ref", "version", "status",
    "current_scope_unit", "claim_target_scope_unit", "role", "form", "tier",
    "updated_at", "header_json", "content_markdown", "content_properties_json",
    "relation_edges_json", "hash",
)
_SCOPE_FIELDS = (
    "name", "scope_unit_id", "parent_name", "declared_label", "ordered",
    "order_number", "declaration_source_path", "declaration_version",
    "relation_edges_json", "hash",
)
_ATOM_JSON_FIELDS = frozenset({"header_json", "content_properties_json", "relation_edges_json"})
_SCOPE_JSON_FIELDS = frozenset({"relation_edges_json"})
_ATOM_DDL = """CREATE TABLE main.atoms(
    source_path VARCHAR PRIMARY KEY,
    status_group VARCHAR NOT NULL,
    id VARCHAR,
    ref VARCHAR UNIQUE,
    version BIGINT,
    status VARCHAR,
    current_scope_unit VARCHAR,
    claim_target_scope_unit VARCHAR,
    role VARCHAR,
    form VARCHAR,
    tier BIGINT,
    updated_at TIMESTAMPTZ,
    header_json JSON NOT NULL,
    content_markdown VARCHAR NOT NULL,
    content_properties_json JSON NOT NULL,
    relation_edges_json JSON NOT NULL,
    hash VARCHAR NOT NULL
)"""
_SCOPE_DDL = """CREATE TABLE main.scope_units(
    name VARCHAR PRIMARY KEY,
    scope_unit_id VARCHAR UNIQUE,
    parent_name VARCHAR,
    declared_label VARCHAR,
    ordered BOOLEAN NOT NULL,
    order_number BIGINT,
    declaration_source_path VARCHAR NOT NULL UNIQUE,
    declaration_version BIGINT NOT NULL,
    relation_edges_json JSON NOT NULL,
    hash VARCHAR NOT NULL
)"""


def _json_value(value: Any) -> Any:
    if value is None or isinstance(value, (str, bool, int)):
        return value
    if isinstance(value, float):
        if not math.isfinite(value):
            raise ValueError("JSON cannot contain NaN or infinity")
        return value
    if isinstance(value, (dt.datetime, dt.date, dt.time)):
        return value.isoformat()
    if isinstance(value, Decimal):
        return str(value)
    if isinstance(value, bytes):
        return "base64:" + base64.b64encode(value).decode("ascii")
    if isinstance(value, (list, tuple)):
        return [_json_value(item) for item in value]
    if isinstance(value, Mapping):
        if any(not isinstance(key, str) for key in value):
            raise ValueError("JSON mapping keys must be strings")
        return {key: _json_value(item) for key, item in value.items()}
    raise ValueError(f"unsupported JSON value: {type(value).__name__}")


def _records(rows: list[dict[str, Any]], fields: tuple[str, ...], json_fields: frozenset[str]) -> list[tuple[Any, ...]]:
    records = []
    for row in rows:
        if not isinstance(row, dict) or set(row) != set(fields):
            raise ValueError("row must contain exactly the declared D672 fields")
        records.append(tuple(
            json.dumps(_json_value(row[field]), separators=(",", ":"), allow_nan=False)
            if field in json_fields else row[field]
            for field in fields
        ))
    return records


def _connect(extension_directory: Path | None):
    try:
        import duckdb
    except ImportError as exc:
        raise RuntimeError("DuckDB runtime is unavailable") from exc
    config = {"temp_directory": ""}
    if extension_directory is not None:
        config["extension_directory"] = str(extension_directory)
    connection = duckdb.connect(":memory:", config=config)
    try:
        connection.execute("LOAD duckpgq")
        connection.execute("SET active_grammar_extensions = ['duckpgq']")
        connection.execute("SET enable_external_access = false")
        connection.execute("SET autoinstall_known_extensions = false")
        connection.execute("SET autoload_known_extensions = false")
        connection.execute("SET lock_configuration = true")
    except Exception as exc:
        connection.close()
        raise RuntimeError("DuckPGQ runtime initialization failed") from exc
    return connection


def _insert_rows(connection, atoms: list[dict[str, Any]], scopes: list[dict[str, Any]]) -> None:
    connection.execute(_ATOM_DDL)
    connection.execute(_SCOPE_DDL)
    if atoms:
        connection.executemany(
            "INSERT INTO main.atoms VALUES (" + ",".join("?" * len(_ATOM_FIELDS)) + ")",
            _records(atoms, _ATOM_FIELDS, _ATOM_JSON_FIELDS),
        )
    if scopes:
        connection.executemany(
            "INSERT INTO main.scope_units VALUES (" + ",".join("?" * len(_SCOPE_FIELDS)) + ")",
            _records(scopes, _SCOPE_FIELDS, _SCOPE_JSON_FIELDS),
        )
    build_graph(connection, atoms, scopes)


def _result_scalar(value: Any) -> Any:
    if value is None or isinstance(value, (str, bool)):
        return value
    if isinstance(value, int):
        return str(value) if abs(value) > _SAFE_INTEGER else value
    if isinstance(value, float):
        if not math.isfinite(value):
            raise ValueError("query result contains NaN or infinity")
        return value
    if isinstance(value, Decimal):
        return str(value)
    if isinstance(value, bytes):
        return "base64:" + base64.b64encode(value).decode("ascii")
    if isinstance(value, (dt.datetime, dt.date, dt.time)):
        return value.isoformat()
    return _UNREPRESENTABLE


def _result_value(value: Any) -> Any:
    scalar = _result_scalar(value)
    if scalar is not _UNREPRESENTABLE:
        return scalar
    if isinstance(value, (list, tuple)):
        return [_result_value(item) for item in value]
    if isinstance(value, Mapping):
        if any(not isinstance(key, str) for key in value):
            raise ValueError("query result mapping keys must be strings")
        return {key: _result_value(item) for key, item in value.items()}
    raise ValueError(f"unsupported query result value: {type(value).__name__}")


def _token_words(sql: str) -> list[str]:
    import duckdb

    tokens = duckdb.tokenize(sql)
    if not tokens:
        return []
    words = []
    for index, (position, token_type) in enumerate(tokens):
        end = tokens[index + 1][0] if index + 1 < len(tokens) else len(sql)
        if token_type != duckdb.token_type.comment:
            words.append(sql[position:end].strip())
    return words


def _is_one_tokenized_read_query(sql: str) -> bool:
    words = _token_words(sql)
    if not words:
        return False
    semicolons = [index for index, word in enumerate(words) if word == ";"]
    if semicolons and semicolons != [len(words) - 1]:
        return False
    return words[0].upper() in {"SELECT", "WITH", "FROM"}


class QueryStore:
    """Serialize trusted refresh and public native SQL over one in-memory connection."""

    def __init__(self, *, extension_directory: Path | None = None) -> None:
        self._extension_directory = extension_directory
        self._lock = threading.RLock()
        self._connection = _connect(extension_directory)
        self._available = True
        self._initialized = False
        self.replace([], [])

    def replace(self, atom_rows: list[dict[str, Any]], scope_rows: list[dict[str, Any]]) -> None:
        with self._lock:
            if not self._available:
                raise RuntimeError("query store unavailable; Workbench restart required")
            try:
                self._connection.execute("BEGIN TRANSACTION")
                if self._initialized:
                    self._connection.execute("DROP PROPERTY GRAPH caprmedio")
                    self._connection.execute("DROP SCHEMA internal CASCADE")
                    self._connection.execute("DROP TABLE main.atoms")
                    self._connection.execute("DROP TABLE main.scope_units")
                _insert_rows(self._connection, atom_rows, scope_rows)
                self._connection.execute("COMMIT")
                self._initialized = True
            except Exception as exc:
                self._available = False
                print(f"query store refresh failed: {exc}", file=sys.stderr)
                raise RuntimeError("query store unavailable; Workbench restart required") from exc

    def _admit(self, sql: str) -> None:
        if not isinstance(sql, str):
            raise ValueError("SQL must be a string")
        import duckdb

        try:
            statements = self._connection.extract_statements(sql)
        except Exception:
            if _is_one_tokenized_read_query(sql):
                return
            raise ValueError("public SQL must contain one native read query") from None
        if len(statements) != 1 or statements[0].type is not duckdb.StatementType.SELECT:
            raise ValueError("public SQL must contain exactly one native SELECT statement")

    def _execute(self, sql: str) -> tuple[list[dict[str, str]], list[list[Any]]]:
        if not self._available:
            raise RuntimeError("query store unavailable; Workbench restart required")
        try:
            self._admit(sql)
        except ValueError as exc:
            print(f"query failed: {exc}", file=sys.stderr)
            raise
        try:
            self._connection.execute("BEGIN TRANSACTION READ ONLY")
            cursor = self._connection.execute(sql)
            description = cursor.description
            rows = cursor.fetchall()
        except Exception as exc:
            try:
                self._connection.execute("COMMIT")
            except Exception as commit_error:
                self._available = False
                print(f"query store unavailable: {commit_error}", file=sys.stderr)
            print(f"query failed: {exc}", file=sys.stderr)
            raise RuntimeError(f"query failed: {exc}") from exc
        try:
            shaped_rows = [[_result_value(value) for value in row] for row in rows]
        except ValueError as exc:
            self._connection.execute("COMMIT")
            print(f"query result delivery failed: {exc}", file=sys.stderr)
            raise ValueError(f"query result delivery failed: {exc}") from exc
        try:
            self._connection.execute("COMMIT")
        except Exception as exc:
            self._available = False
            print(f"query store unavailable: {exc}", file=sys.stderr)
            raise RuntimeError("query store unavailable; Workbench restart required") from exc
        return [{"name": column[0], "type": str(column[1])} for column in description], shaped_rows

    def run(self, sql: str) -> dict[str, Any]:
        with self._lock:
            columns, rows = self._execute(sql)
        return {"columns": columns, "rows": rows, "row_count": len(rows), "column_count": len(columns)}

    def check(self, sql: str) -> dict[str, Any]:
        with self._lock:
            columns, rows = self._execute(sql)
        return {"valid": True, "row_count": len(rows), "column_count": len(columns)}

    def close(self) -> None:
        with self._lock:
            self._connection.close()
