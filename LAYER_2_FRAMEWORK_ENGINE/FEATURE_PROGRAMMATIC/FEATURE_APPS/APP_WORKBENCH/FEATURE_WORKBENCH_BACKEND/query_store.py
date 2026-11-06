# CA-R-2728@6
# CA-R-2729@7
# CA-R-2953@1
# CA-M-462@10
# CA-M-463@6
# CA-M-493@1
# CA-D-673@13
# CA-D-697@1
# CA-R-2950@1
# CA-R-2724@3
# CA-M-490@1
# CA-D-695@1
# CA-M-465@17
# CA-D-675@13

"""The DuckDB and DuckPGQ owner for disk-backed, paged Workbench queries."""

from __future__ import annotations

from dataclasses import dataclass
import json
import sys
import threading
import time
import uuid
from pathlib import Path
from typing import Any

from .errors import QueryExecutionError, WorkbenchUnavailableError
from .graph_store import quote_identifier
from .header_columns import HeaderSchema, infer_header_schema, schema_asset_path
from .content_schema import compile_content_schema, content_schema_asset_path
from .projection_delta import ProjectionSnapshot, apply as apply_projection_delta, snapshot
from .public_rows import insert_rows
from .query_admission import is_duckdb_internal, is_one_tokenized_read_query
from .result_columns import result_columns
from .result_values import group_key, result_value
from .result_view import Grid, build_page_query, ctas_source_sql, parse_grid, validate_columns
from .query_schema import public_schema
from .watcher_change_log import WatcherChangeLog, validate_change_record


def _connect(extension_directory: Path | None, database_path: Path | None) -> Any:
    try:
        import duckdb
    except ImportError as exc:
        raise WorkbenchUnavailableError("DuckDB runtime is unavailable") from exc
    config: dict[str, str | bool | int | float | list[str]] = {"temp_directory": "", "memory_limit": "256MB"}
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
        raise WorkbenchUnavailableError("DuckPGQ runtime initialization failed") from exc
    return connection


@dataclass
class _Result:
    columns: list[dict[str, Any]]
    row_count: int
    sql: str
    stored_columns: tuple[str, ...]
    created_at: float
    pinned: bool = False


class QueryStore:
    """Serialize trusted refresh and paged public native SQL over one DuckDB connection."""

    def __init__(
        self, *, extension_directory: Path | None = None, database_path: Path | None = None,
        result_ttl_seconds: int = 3600,
    ) -> None:
        if type(result_ttl_seconds) is not int or result_ttl_seconds <= 0:
            raise ValueError("result_ttl_seconds must be a positive integer")
        self._extension_directory = extension_directory
        self._database_path = database_path
        self._result_ttl_seconds = result_ttl_seconds
        self._lock = threading.RLock()
        self._connection = _connect(extension_directory, database_path)
        self._available = True
        self._initialized = False
        self._results: dict[str, _Result] = {}
        self._projection: ProjectionSnapshot | None = None
        self._header_schema = HeaderSchema(())
        self._content_schema = compile_content_schema([])
        self._schema_changed = False
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
            self._connection.execute("DROP TABLE IF EXISTS main.change_log")
            self._connection.execute("CREATE SCHEMA workbench_results")
            self._connection.execute(
                "CREATE TABLE main.change_log (observed_at TIMESTAMPTZ NOT NULL, "
                "operation VARCHAR NOT NULL, old_path VARCHAR, new_path VARCHAR)"
            )
        except Exception as exc:
            self._connection.close()
            raise WorkbenchUnavailableError("query store initialization failed") from exc

    def replace(
        self, atom_rows: list[dict[str, Any]], scope_rows: list[dict[str, Any]],
        *, relation_types: set[str] | None = None,
    ) -> None:
        with self._lock:
            if not self._available:
                raise WorkbenchUnavailableError("query store unavailable; Workbench restart required")
            try:
                header_schema = infer_header_schema(atom_rows)
                content_schema = compile_content_schema(atom_rows)
                self._connection.execute("BEGIN TRANSACTION")
                if self._initialized:
                    self._connection.execute("DROP PROPERTY GRAPH caprmedio")
                    self._connection.execute("DROP SCHEMA internal CASCADE")
                    self._connection.execute("DROP TABLE main.atoms")
                    self._connection.execute("DROP TABLE main.scope_units")
                started = time.monotonic()
                insert_rows(
                    self._connection, atom_rows, scope_rows, header_schema=header_schema,
                    content_schema=content_schema, relation_types=relation_types,
                )
                self._connection.execute("COMMIT")
                self._initialized = True
                self._header_schema = header_schema
                self._content_schema = content_schema
                self._schema_changed = False
                header_schema.write(schema_asset_path(self._database_path))
                content_schema.write(content_schema_asset_path(self._database_path))
                self._projection = snapshot(atom_rows, scope_rows, relation_types, header_schema, content_schema)
                self._info_edit(
                    "replace", "projection", len(self._projection.atoms) + len(self._projection.scopes), started,
                )
            except Exception as exc:
                self._available = False
                print(f"query store refresh failed: {exc}", file=sys.stderr)
                raise WorkbenchUnavailableError("query store unavailable; Workbench restart required") from exc

    def _info_edit(
        self, operation: str, table: str, row_count: int, started: float, reference: str | None = None,
    ) -> None:
        if row_count:
            elapsed_ms = round((time.monotonic() - started) * 1000, 1)
            suffix = f" reference={reference}" if reference is not None else ""
            print(
                f"Workbench INFO database_edit operation={operation} table={table} "
                f"row_count={row_count} elapsed_ms={elapsed_ms}{suffix}",
                flush=True,
            )

    def apply(
        self, atom_rows: list[dict[str, Any]], scope_rows: list[dict[str, Any]],
        *, relation_types: set[str],
    ) -> bool:
        """Apply the materialized delta without replacing unaffected public rows."""
        with self._lock:
            if not self._available:
                raise WorkbenchUnavailableError("query store unavailable; Workbench restart required")
            if self._projection is None:
                self.replace(atom_rows, scope_rows, relation_types=relation_types)
                return True
            try:
                header_schema = infer_header_schema(atom_rows)
                content_schema = compile_content_schema(atom_rows)
                self._schema_changed = (
                    header_schema != self._header_schema or content_schema.shape != self._content_schema.shape
                )
                if self._schema_changed:
                    return True
                self._connection.execute("BEGIN TRANSACTION")
                started = time.monotonic()
                projection, change = apply_projection_delta(
                    self._connection, self._projection, atom_rows, scope_rows, relation_types,
                    header_schema, content_schema,
                )
                self._connection.execute("COMMIT")
                self._projection = projection
                self._content_schema = content_schema
                content_schema.write(content_schema_asset_path(self._database_path))
                self._info_edit("delete", "atoms", change.deleted_atoms, started, change.reference)
                self._info_edit("delete", "scope_units", change.deleted_scopes, started)
                self._info_edit("insert", "atoms", change.inserted_atoms, started, change.reference)
                self._info_edit("insert", "scope_units", change.inserted_scopes, started)
                self._info_edit("update", "graph", change.graph_rows, started, change.reference)
                return bool(
                    change.deleted_atoms or change.deleted_scopes or change.inserted_atoms
                    or change.inserted_scopes or change.graph_rows
                )
            except Exception as exc:
                self._available = False
                print(f"query store refresh failed: {exc}", file=sys.stderr)
                raise WorkbenchUnavailableError("query store unavailable; Workbench restart required") from exc

    @property
    def schema_changed(self) -> bool:
        """Whether the last delta needs a complete source reread and table rebuild."""
        return self._schema_changed

    @staticmethod
    def _change_log_rows(rows: object) -> list[dict[str, str | None]]:
        if not isinstance(rows, list):
            raise ValueError("change log rows must be a list")
        return [validate_change_record(row) for row in rows]

    def replace_change_log(self, rows: object) -> None:
        """Replace the technical table with the NDJSON owner's retained event set."""
        retained = self._change_log_rows(rows)
        with self._lock:
            if not self._available:
                raise WorkbenchUnavailableError("query store unavailable; Workbench restart required")
            try:
                self._connection.execute("BEGIN TRANSACTION")
                self._connection.execute("DELETE FROM main.change_log")
                if retained:
                    self._connection.execute(
                        "INSERT INTO main.change_log "
                        "SELECT json_extract_string(value, '$.observed_at')::TIMESTAMPTZ, "
                        "json_extract_string(value, '$.operation'), "
                        "json_extract_string(value, '$.old_path'), "
                        "json_extract_string(value, '$.new_path') "
                        "FROM json_each(?::JSON)",
                        [json.dumps(retained, separators=(",", ":"))],
                    )
                self._connection.execute("COMMIT")
            except Exception as exc:
                self._available = False
                print(f"query store change-log refresh failed: {exc}", file=sys.stderr)
                raise WorkbenchUnavailableError("query store unavailable; Workbench restart required") from exc

    def sync_change_log(
        self, log: WatcherChangeLog, events: list[dict[str, str | None]] | None = None,
        *, initialize: bool = False,
    ) -> None:
        """Synchronize one retained NDJSON event set under the database-owner lock."""
        with self._lock:
            rows, changed = log.append(events) if events is not None else log.prune()
            if changed or initialize:
                self.replace_change_log(rows)

    def _admit(self, sql: str) -> None:
        if not isinstance(sql, str):
            raise ValueError("SQL must be a string")
        import duckdb

        try:
            statements = self._connection.extract_statements(sql)
        except Exception:
            if is_one_tokenized_read_query(sql):
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

    @staticmethod
    def _preview(value: int | None) -> int | None:
        if value is None:
            return None
        if type(value) is not int or value < 0:
            raise ValueError("preview must be a non-negative integer")
        return value

    def _materialize(self, sql: str, preview: int | None = None) -> tuple[str, _Result]:
        if not self._available:
            raise WorkbenchUnavailableError("query store unavailable; Workbench restart required")
        try:
            self._admit(sql)
            self._verify_read_only(sql)
        except ValueError as exc:
            print(f"query failed: {exc}", file=sys.stderr)
            raise
        except Exception as exc:
            print(f"query failed: {exc}", file=sys.stderr)
            raise QueryExecutionError(f"query failed: {exc}") from exc
        try:
            relation = self._connection.sql(sql)
            if preview is not None:
                relation = relation.limit(preview)
            columns = [
                {"name": name, "type": str(column_type)}
                for name, column_type in zip(relation.columns, relation.types, strict=True)
            ]
        except Exception as exc:
            print(f"query failed: {exc}", file=sys.stderr)
            raise QueryExecutionError(f"query failed: {exc}") from exc
        query_id = uuid.uuid4().hex
        table_name = f"query_{query_id}"
        table = quote_identifier(table_name)
        private_ordinal = f"__workbench_snapshot_{query_id}"
        try:
            # The generated CTAS is one DuckDB statement-atomic cache write.  Do not wrap it
            # in an explicit transaction: a user-data conversion error then remains recoverable.
            materialized_sql = ctas_source_sql(relation.sql_query())
            self._connection.execute(
                f"CREATE TABLE workbench_results.{table} AS "
                f"SELECT row_number() OVER () AS {quote_identifier(private_ordinal)}, * "
                f"FROM ({materialized_sql}) AS source"
            )
            stored_columns = tuple(self._connection.sql(f"SELECT * FROM workbench_results.{table}").columns)
            columns, row_count = result_columns(self._connection, table, columns, private_ordinal=True)
        except Exception as exc:
            if is_duckdb_internal(exc):
                self._available = False
                print(f"query store unavailable: {exc}", file=sys.stderr)
                raise WorkbenchUnavailableError("query store unavailable; Workbench restart required") from exc
            print(f"query failed: {exc}", file=sys.stderr)
            raise QueryExecutionError(f"query failed: {exc}") from exc
        return query_id, _Result(columns, row_count, sql, stored_columns, time.monotonic())

    def _read_page(
        self, query_id: str, result: _Result, offset: int, page_size: int, grid: Grid,
    ) -> dict[str, Any]:
        try:
            query = build_page_query(
                f"query_{query_id}", result.stored_columns, grid, page_size=page_size, offset=offset,
            )
            row_count = self._connection.execute(query.count_sql, query.count_parameters).fetchone()[0]
            rows = self._connection.execute(query.page_sql, query.page_parameters).fetchall()
            shaped_rows = [[result_value(value) for value in row[1:len(result.columns) + 1]] for row in rows]
        except ValueError as exc:
            print(f"query result delivery failed: {exc}", file=sys.stderr)
            raise ValueError(f"query result delivery failed: {exc}") from exc
        except Exception as exc:
            self._available = False
            print(f"query store unavailable: {exc}", file=sys.stderr)
            raise WorkbenchUnavailableError("query store unavailable; Workbench restart required") from exc
        response: dict[str, Any] = {
            "query_id": query_id,
            "sql": result.sql,
            "columns": result.columns,
            "rows": shaped_rows,
            "row_count": row_count,
            "source_row_count": result.row_count,
            "column_count": len(result.columns),
            "offset": offset,
            "page_size": page_size,
            "has_more": offset + len(shaped_rows) < row_count,
        }
        if query.group_column is not None:
            groups: list[dict[str, Any]] = []
            seen: set[str] = set()
            for values, raw in zip(shaped_rows, rows, strict=True):
                value = values[query.group_column]
                key = group_key(value)
                if key not in seen:
                    seen.add(key)
                    groups.append({"value": value, "count": raw[-1]})
            response["groups"] = groups
        return response

    def run(
        self, sql: str, page_size: int = 100, *, preview: int | None = None,
        include_rows: bool = True,
    ) -> dict[str, Any]:
        page_size = self._page_size(page_size)
        preview = self._preview(preview)
        if type(include_rows) is not bool:
            raise ValueError("include_rows must be a boolean")
        with self._lock:
            query_id, result = self._materialize(sql, preview)
            self._results[query_id] = result
            if not include_rows:
                return {
                    "query_id": query_id, "sql": sql, "columns": result.columns,
                    "row_count": result.row_count, "column_count": len(result.columns),
                }
            try:
                return self._read_page(query_id, result, 0, page_size, Grid((), (), None))
            except ValueError:
                self.drop(query_id)
                raise

    def drop(self, query_id: str) -> None:
        """Release one process-local materialized result."""
        with self._lock:
            if not isinstance(query_id, str) or query_id not in self._results:
                raise ValueError("unknown query_id")
            try:
                table = quote_identifier(f"query_{query_id}")
                self._connection.execute(f"DROP TABLE workbench_results.{table}")
                del self._results[query_id]
            except Exception as exc:
                self._available = False
                print(f"query store unavailable: {exc}", file=sys.stderr)
                raise WorkbenchUnavailableError("query store unavailable; Workbench restart required") from exc

    def pin(self, query_id: str) -> None:
        """Keep an existing result while its owner View remains open."""
        with self._lock:
            if not isinstance(query_id, str) or query_id not in self._results:
                raise ValueError("unknown query_id")
            self._results[query_id].pinned = True

    def unpin(self, query_id: str) -> None:
        """Release a View pin without dropping a still-young result."""
        with self._lock:
            if not isinstance(query_id, str) or query_id not in self._results:
                raise ValueError("unknown query_id")
            self._results[query_id].pinned = False

    def prune_results(self) -> None:
        """Drop expired unpinned results when the existing owner performs cleanup."""
        with self._lock:
            now = time.monotonic()
            expired = [
                query_id for query_id, result in self._results.items()
                if not result.pinned and now - result.created_at >= self._result_ttl_seconds
            ]
            for query_id in expired:
                self.drop(query_id)

    def page(
        self, query_id: str, offset: int, page_size: int = 100, *, preview: int | None = None,
        grid: object = None,
    ) -> dict[str, Any]:
        offset = self._offset(offset)
        page_size = self._page_size(page_size)
        preview = self._preview(preview)
        parsed_grid = parse_grid(grid)
        if not isinstance(query_id, str):
            raise ValueError("unknown query_id")
        with self._lock:
            if not self._available:
                raise WorkbenchUnavailableError("query store unavailable; Workbench restart required")
            if query_id not in self._results:
                raise ValueError("unknown query_id")
            result = self._results[query_id]
            validate_columns(parsed_grid, len(result.columns))
            if preview is not None:
                page_size = min(page_size, preview)
            return self._read_page(query_id, result, offset, page_size, parsed_grid)

    def check(self, sql: str) -> dict[str, Any]:
        with self._lock:
            query_id, result = self._materialize(sql)
            table = quote_identifier(f"query_{query_id}")
            try:
                self._connection.execute(f"DROP TABLE workbench_results.{table}")
            except Exception as exc:
                self._available = False
                print(f"query store unavailable: {exc}", file=sys.stderr)
                raise WorkbenchUnavailableError("query store unavailable; Workbench restart required") from exc
        return {"valid": True, "row_count": result.row_count, "column_count": len(result.columns), "sql": sql}

    def schema(self) -> dict[str, dict[str, list[dict[str, Any]]]]:
        with self._lock:
            if not self._available:
                raise WorkbenchUnavailableError("query store unavailable; Workbench restart required")
            return public_schema(self._connection, self._header_schema)

    def close(self) -> None:
        with self._lock:
            self._connection.close()
