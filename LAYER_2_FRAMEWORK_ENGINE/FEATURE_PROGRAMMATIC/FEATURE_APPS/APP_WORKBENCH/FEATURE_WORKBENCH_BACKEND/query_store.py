# CA-R-2725@2
# CA-R-2728@2
# CA-R-2729@3
# CA-M-462@7
# CA-M-463@4
# CA-M-464@7
# CA-M-465@10
# CA-D-672@9
# CA-D-673@7
# CA-D-675@9

"""The DuckDB and DuckPGQ owner for disk-backed, paged Workbench queries."""

from __future__ import annotations

import base64
import datetime as dt
import math
import sys
import threading
import uuid
from collections.abc import Mapping
from decimal import Decimal
from pathlib import Path
from typing import Any

from .graph_store import quote_identifier
from .public_rows import insert_rows
from .result_columns import result_columns


_SAFE_INTEGER = 2**53 - 1
_UNREPRESENTABLE = object()


def _connect(extension_directory: Path | None, database_path: Path | None):
    try:
        import duckdb
    except ImportError as exc:
        raise RuntimeError("DuckDB runtime is unavailable") from exc
    config: dict[str, str] = {"temp_directory": "", "memory_limit": "256MB"}
    database = ":memory:"
    if database_path is not None:
        database_path.parent.mkdir(parents=True, exist_ok=True)
        spill_directory = database_path.parent / "duckdb-temp"
        spill_directory.mkdir(exist_ok=True)
        database = str(database_path)
        config["temp_directory"] = str(spill_directory)
    if extension_directory is not None:
        config["extension_directory"] = str(extension_directory)
    connection = duckdb.connect(database, config=config)
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
    """Serialize trusted refresh and paged public native SQL over one DuckDB connection."""

    def __init__(
        self, *, extension_directory: Path | None = None, database_path: Path | None = None,
    ) -> None:
        self._extension_directory = extension_directory
        self._database_path = database_path
        self._lock = threading.RLock()
        self._connection = _connect(extension_directory, database_path)
        self._available = True
        self._initialized = False
        self._results: dict[str, tuple[list[dict[str, Any]], int]] = {}
        self._clear_startup_projection()
        self.replace([], [])

    def _clear_startup_projection(self) -> None:
        """Discard the disposable projection and any prior process's query cache."""
        try:
            self._connection.execute("DROP PROPERTY GRAPH IF EXISTS caprmedio")
            self._connection.execute("DROP SCHEMA IF EXISTS internal CASCADE")
            self._connection.execute("DROP SCHEMA IF EXISTS workbench_results CASCADE")
            self._connection.execute("DROP TABLE IF EXISTS main.atoms")
            self._connection.execute("DROP TABLE IF EXISTS main.scope_units")
            self._connection.execute("CREATE SCHEMA workbench_results")
        except Exception as exc:
            self._connection.close()
            raise RuntimeError("query store initialization failed") from exc

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
                insert_rows(self._connection, atom_rows, scope_rows)
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

    def _verify_read_only(self, sql: str) -> None:
        """Native planning under DuckDB's read-only transaction rejects writable CTEs."""
        self._connection.execute("BEGIN TRANSACTION READ ONLY")
        try:
            self._connection.execute(f"EXPLAIN {sql}").fetchall()
        finally:
            self._connection.execute("COMMIT")

    @staticmethod
    def _page_size(value: int) -> int:
        if type(value) is not int or not 1 <= value <= 1000:
            raise ValueError("page_size must be an integer from 1 to 1000")
        return value

    @staticmethod
    def _offset(value: int) -> int:
        if type(value) is not int or value < 0:
            raise ValueError("offset must be a non-negative integer")
        return value

    def _materialize(self, sql: str) -> tuple[str, list[dict[str, Any]], int]:
        if not self._available:
            raise RuntimeError("query store unavailable; Workbench restart required")
        try:
            self._admit(sql)
            self._verify_read_only(sql)
        except ValueError as exc:
            print(f"query failed: {exc}", file=sys.stderr)
            raise
        except Exception as exc:
            print(f"query failed: {exc}", file=sys.stderr)
            raise RuntimeError(f"query failed: {exc}") from exc
        try:
            relation = self._connection.sql(sql)
            columns = [
                {"name": name, "type": str(column_type)}
                for name, column_type in zip(relation.columns, relation.types, strict=True)
            ]
        except Exception as exc:
            print(f"query failed: {exc}", file=sys.stderr)
            raise RuntimeError(f"query failed: {exc}") from exc
        query_id = uuid.uuid4().hex
        table = quote_identifier(f"query_{query_id}")
        try:
            # The caller's SQL is already admitted read-only.  This write transaction is
            # solely the trusted, generated cache table that evaluates it once.
            self._connection.execute("BEGIN TRANSACTION")
            self._connection.execute(f"CREATE TABLE workbench_results.{table} AS {sql}")
            columns, row_count = result_columns(self._connection, table, columns)
            self._connection.execute("COMMIT")
        except Exception as exc:
            self._available = False
            print(f"query store unavailable: {exc}", file=sys.stderr)
            print(f"query failed: {exc}", file=sys.stderr)
            raise RuntimeError("query store unavailable; Workbench restart required") from exc
        return query_id, columns, row_count

    def _read_page(
        self, query_id: str, columns: list[dict[str, Any]], row_count: int,
        offset: int, page_size: int,
    ) -> dict[str, Any]:
        try:
            table = quote_identifier(f"query_{query_id}")
            cursor = self._connection.execute(
                f"SELECT * FROM workbench_results.{table} ORDER BY rowid LIMIT ? OFFSET ?",
                [page_size, offset],
            )
            rows = cursor.fetchmany(page_size)
            shaped_rows = [[_result_value(value) for value in row] for row in rows]
        except ValueError as exc:
            print(f"query result delivery failed: {exc}", file=sys.stderr)
            raise ValueError(f"query result delivery failed: {exc}") from exc
        except Exception as exc:
            self._available = False
            print(f"query store unavailable: {exc}", file=sys.stderr)
            raise RuntimeError("query store unavailable; Workbench restart required") from exc
        return {
            "query_id": query_id,
            "columns": columns,
            "rows": shaped_rows,
            "row_count": row_count,
            "column_count": len(columns),
            "offset": offset,
            "page_size": page_size,
            "has_more": offset + len(shaped_rows) < row_count,
        }

    def run(self, sql: str, page_size: int = 100) -> dict[str, Any]:
        page_size = self._page_size(page_size)
        with self._lock:
            query_id, columns, row_count = self._materialize(sql)
            self._results[query_id] = (columns, row_count)
            return self._read_page(query_id, columns, row_count, 0, page_size)

    def page(self, query_id: str, offset: int, page_size: int = 100) -> dict[str, Any]:
        offset = self._offset(offset)
        page_size = self._page_size(page_size)
        with self._lock:
            if not self._available:
                raise RuntimeError("query store unavailable; Workbench restart required")
            if not isinstance(query_id, str) or query_id not in self._results:
                raise ValueError("unknown query_id")
            columns, row_count = self._results[query_id]
            return self._read_page(query_id, columns, row_count, offset, page_size)

    def check(self, sql: str) -> dict[str, Any]:
        with self._lock:
            query_id, columns, row_count = self._materialize(sql)
            table = quote_identifier(f"query_{query_id}")
            try:
                self._connection.execute(f"DROP TABLE workbench_results.{table}")
            except Exception as exc:
                self._available = False
                print(f"query store unavailable: {exc}", file=sys.stderr)
                raise RuntimeError("query store unavailable; Workbench restart required") from exc
        return {"valid": True, "row_count": row_count, "column_count": len(columns)}

    def close(self) -> None:
        with self._lock:
            self._connection.close()
