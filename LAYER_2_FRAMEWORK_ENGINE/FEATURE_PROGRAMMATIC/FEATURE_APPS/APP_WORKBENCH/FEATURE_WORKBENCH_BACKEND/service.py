# CA-R-2728@6
# CA-R-2729@7
# CA-R-2950@1
# CA-R-2952@1
# CA-M-465@19
# CA-M-490@2
# CA-M-491@1
# CA-D-695@2
# CA-D-696@1
# CA-D-673@13
# CA-R-2786@1
# CA-M-474@1
# CA-R-2903@3
# CA-M-502@1

"""One Project's direct file reader, background indexer, and SQL capability."""

from __future__ import annotations

import datetime as dt
from pathlib import Path
import shutil
import sys
import threading
import time
from typing import Any

from .errors import QueryExecutionError, WorkbenchUnavailableError
from .query_store import QueryStore
from .query_log import QueryLog
from .incremental_relations import RelationState, materialize_delta
from .runtime_settings import result_ttl_seconds
from .saved_queries import SavedQueryStore
from .source_reader import SourceReader
from .source_watcher import Change, SourceWatcher
from .statements import select_statement
from .watcher_change_log import WatcherChangeLog
from .workspace import WorkspaceStore


TOOLS = Path(__file__).resolve().parents[3] / "FEATURE_TOOLS"
if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))

from work_journal import configured_journal_root  # noqa: E402


class WorkbenchService:
    """Own only the Workbench lifecycle; QueryStore owns database serialization."""

    def __init__(self, root: Path, *, extension_directory: Path | None = None) -> None:
        self._root = Path(root).resolve()
        self._reader = SourceReader(self._root)
        self._saved_queries = SavedQueryStore(self._root)
        self._workspaces = WorkspaceStore(self._root)
        self._workspaces.clear_transient_results()
        self._query_log = QueryLog(self._root)
        self._watcher_change_log = WatcherChangeLog(self._root)
        self._extension_directory = extension_directory
        self._database_path = (
            self._root / ".caprmedio_runtime" / "workbench" / "projection.duckdb"
        )
        self._start_lock = threading.Lock()
        self._refresh_lock = threading.Lock()
        self._interface_lock = threading.RLock()
        self._sync_status_lock = threading.Lock()
        self._watch_ready = threading.Event()
        self._stop = threading.Event()
        self._store: QueryStore | None = None
        self._thread: threading.Thread | None = None
        self._watcher: SourceWatcher | None = None
        self._relation_state: RelationState | None = None
        self._failure: WorkbenchUnavailableError | None = None
        self._paths: set[str] = set()
        self._syncing = 0
        self._last_synced_at: str | None = None

    def _refresh(self, changes: list[Change] | None = None) -> None:
        self._begin_sync()
        succeeded = False
        try:
            with self._refresh_lock:
                started = time.monotonic()
                atoms, scopes = (
                    self._reader.capture()
                    if changes is None
                    else self._reader.capture(changes)
                )
                captured_at = time.monotonic()
                capture_seconds = captured_at - started
                full = changed = False
                materialize_seconds = write_seconds = 0.0
                if changes is None or self._reader.capture_changed:
                    atoms, scopes, registered, _inverse, next_state, delta = materialize_delta(
                        atoms, scopes, self._relation_state, changes=self._reader.capture_delta,
                    )
                    materialize_seconds = time.monotonic() - captured_at
                    schema = self._reader.content_schema
                    assert schema is not None
                    assert self._store is not None
                    full = delta is None
                    writing_started = time.monotonic()
                    if full:
                        self._store.replace(atoms, scopes, relation_types=registered, content_schema=schema)
                        changed = True
                    else:
                        changed = self._store.apply(
                            atoms, scopes, relation_types=registered, content_schema=schema, delta=delta,
                        )
                    write_seconds += time.monotonic() - writing_started
                    if not full and self._store.schema_changed is True:
                        full = True
                        recapture_started = time.monotonic()
                        atoms, scopes = self._reader.capture()
                        recaptured_at = time.monotonic()
                        capture_seconds += recaptured_at - recapture_started
                        atoms, scopes, registered, _inverse, next_state, _delta = materialize_delta(
                            atoms, scopes, self._relation_state,
                        )
                        materialize_seconds += time.monotonic() - recaptured_at
                        schema = self._reader.content_schema
                        assert schema is not None
                        writing_started = time.monotonic()
                        self._store.replace(atoms, scopes, relation_types=registered, content_schema=schema)
                        write_seconds += time.monotonic() - writing_started
                        changed = True
                    self._relation_state = next_state
                written_at = time.monotonic()
                paths = {row["source_path"] for row in atoms}
                removed = len(self._paths - paths)
                self._paths = paths
                succeeded = True
                print(
                    "Workbench INFO refresh "
                    f"mode={'full' if full else 'delta'} changed={str(changed).lower()} "
                    f"atoms={len(atoms)} scopes={len(scopes)} removed_atom_sources={removed} "
                    f"excluded_sources={self._reader.excluded_count} "
                    f"capture_ms={round(capture_seconds * 1000, 1)} "
                    f"materialize_ms={round(materialize_seconds * 1000, 1)} "
                    f"write_ms={round(write_seconds * 1000, 1)} "
                    f"elapsed_ms={round((written_at - started) * 1000, 1)}",
                    flush=True,
                )
        finally:
            self._finish_sync(succeeded)

    def _begin_sync(self) -> None:
        with self._sync_status_lock:
            self._syncing += 1

    def _finish_sync(self, succeeded: bool) -> None:
        with self._sync_status_lock:
            if succeeded:
                self._last_synced_at = dt.datetime.now(dt.UTC).isoformat()
            self._syncing -= 1

    def sync_status(self) -> dict[str, bool | str | None]:
        """Return the owner-local indexing snapshot without starting Workbench."""
        with self._sync_status_lock:
            return {"syncing": self._syncing > 0, "last_synced_at": self._last_synced_at}

    def _index(self) -> None:
        try:
            self._watcher = SourceWatcher(self._reader.root, self._reader.control_root)
            self._watcher.start()
            self._watch_ready.set()
            while not self._stop.is_set():
                batch = self._watcher.changes(timeout=0.1)
                if batch:
                    self._record_watcher_changes(batch)
                if batch and not self._journal_only(batch):
                    self._refresh(batch)
                self._prune_watcher_changes()
                assert self._store is not None
                self._store.prune_results()
        except Exception as error:
            self._failure = WorkbenchUnavailableError(f"Workbench indexing failed; restart required: {error}")
            self._watch_ready.set()
            if not self._stop.is_set():
                print(self._failure, file=sys.stderr)
        finally:
            if self._watcher is not None:
                self._watcher.close()
                self._watcher = None

    def _rehydrate_watcher_changes(self) -> None:
        assert self._store is not None
        self._store.sync_change_log(self._watcher_change_log, initialize=True)

    def _record_watcher_changes(self, batch: list[Change]) -> None:
        assert self._store is not None
        self._store.sync_change_log(self._watcher_change_log, batch)

    def _prune_watcher_changes(self) -> None:
        assert self._store is not None
        self._store.sync_change_log(self._watcher_change_log)

    def _journal_only(self, batch: list[Change]) -> bool:
        journal = (self._root / configured_journal_root(self._root)).resolve()
        paths = [
            path
            for change in batch
            for path in (change["old_path"], change["new_path"])
            if path is not None
        ]
        return bool(paths) and all(
            (self._root / path).resolve().is_relative_to(journal) for path in paths
        )

    def _start(self) -> None:
        with self._start_lock:
            if self._failure:
                raise self._failure
            if self._store is not None:
                return
            try:
                self._store = QueryStore(
                    extension_directory=self._extension_directory,
                    database_path=self._database_path,
                    result_ttl_seconds=result_ttl_seconds(self._root),
                )
                self._rehydrate_watcher_changes()
                self._thread = threading.Thread(target=self._index, name="workbench-index", daemon=True)
                self._thread.start()
                self._watch_ready.wait()
                if self._failure:
                    raise self._failure
                self._refresh()
            except Exception as error:
                self._stop.set()
                if self._thread is not None:
                    self._thread.join()
                self._failure = WorkbenchUnavailableError(
                    f"Workbench startup failed; restart required: {error}"
                )
                print(self._failure, file=sys.stderr)
                raise self._failure from error

    def run(
        self, sql: str, page_size: int = 100, cursor_position: int | None = None,
        *, save: bool = False, preview: int | None = None, name: str | None = None,
    ) -> dict[str, Any]:
        if type(save) is not bool:
            raise ValueError("save must be a boolean")
        if name is not None and not save:
            raise ValueError("name is only supported when save is true")
        page_size = QueryStore._page_size(page_size)
        preview = QueryStore._preview(preview)
        if save:
            name = SavedQueryStore._name(name)
        selected = select_statement(sql, cursor_position)
        try:
            result = self._run_store(selected, page_size=page_size, preview=preview, include_rows=True)
            if save:
                try:
                    result |= self._saved_queries.save_query(selected, name)
                except ValueError as error:
                    print(f"saved query failed: {error}", file=sys.stderr)
                    result |= {"outcome": "partial", "save_error": str(error)}
            self._log_attempt(selected, self._result_metadata(result))
            return result
        except ValueError as error:
            self._log_attempt(selected, self._failed_metadata(error))
            raise
        except (QueryExecutionError, WorkbenchUnavailableError) as error:
            self._log_attempt(selected, self._failed_metadata(error))
            raise

    def _run_store(
        self, selected: str, *, page_size: int = 100, preview: int | None = None,
        include_rows: bool,
    ) -> dict[str, Any]:
        self._start()
        assert self._store is not None
        self._store.prune_results()
        return self._store.run(selected, page_size=page_size, preview=preview, include_rows=include_rows)

    @staticmethod
    def _result_metadata(result: dict[str, Any]) -> dict[str, Any]:
        return {
            "status": "success", "error": None, "query_id": result["query_id"],
            "row_count": result["row_count"], "column_count": result["column_count"],
        }

    @staticmethod
    def _failed_metadata(error: Exception) -> dict[str, Any]:
        return {"status": "failed", "error": str(error), "query_id": None, "row_count": None, "column_count": None}

    def _log_attempt(self, sql: str, metadata: dict[str, Any]) -> None:
        try:
            self._query_log.append_async(sql, metadata)
        except Exception as error:
            print(f"query log failed: {error}", file=sys.stderr)

    def _drop_result(self, query_id: str | None) -> None:
        if query_id is not None and self._store is not None:
            self._store.drop(query_id)

    def _unpin_result(self, query_id: str | None) -> None:
        if query_id is not None and self._store is not None:
            self._store.unpin(query_id)

    @staticmethod
    def _arguments(name: str, arguments: object, allowed: set[str], required: set[str] = set()) -> dict[str, Any]:
        if not isinstance(arguments, dict) or set(arguments) - allowed or required - set(arguments):
            raise ValueError(f"invalid {name} arguments")
        return arguments

    @staticmethod
    def _limit(value: object, field: str = "limit") -> int:
        if isinstance(value, bool) or not isinstance(value, int) or not 1 <= value <= 1000:
            raise ValueError(f"{field} must be an integer from 1 to 1000")
        return value

    @staticmethod
    def _offset(value: object) -> int:
        if isinstance(value, bool) or not isinstance(value, int) or value < 0:
            raise ValueError("offset must be a non-negative integer")
        return value

    def interface_call(self, name: str, arguments: object) -> dict[str, Any]:  # noqa: C901
        """Perform one explicit Workspace/View action with strict backend validation."""
        with self._interface_lock:
            if name == "workspace_open":
                args = self._arguments(name, arguments, {"session_id"}, {"session_id"})
                return self._workspaces.open(args["session_id"])
            if name == "workspace_list":
                self._arguments(name, arguments, set())
                return self._workspaces.list()
            if name == "workspace_get":
                args = self._arguments(name, arguments, {"workspace_id"}, {"workspace_id"})
                return self._workspaces.get(args["workspace_id"])
            if name == "view_create":
                args = self._arguments(name, arguments, {"workspace_id", "position", "name"}, {"workspace_id"})
                return self._workspaces.create(args["workspace_id"], args.get("position", "last"), args.get("name"))
            if name == "view_duplicate":
                args = self._arguments(name, arguments, {"workspace_id", "view_id"}, {"workspace_id", "view_id"})
                return self._workspaces.duplicate(args["workspace_id"], args["view_id"])
            if name == "view_list":
                args = self._arguments(name, arguments, {"workspace_id"}, {"workspace_id"})
                return self._workspaces.list_views(args["workspace_id"])
            if name == "view_get":
                args = self._arguments(name, arguments, {"workspace_id", "view_id"}, {"workspace_id", "view_id"})
                return self._workspaces.get_view(args["workspace_id"], args["view_id"])
            if name == "view_update":
                args = self._arguments(name, arguments, {"workspace_id", "view_id", "sql", "cursor_position", "expected_revision"}, {"workspace_id", "view_id", "sql", "expected_revision"})
                if "cursor_position" in args:
                    WorkspaceStore.cursor(args["cursor_position"])
                return self._workspaces.update(
                    args["workspace_id"], args["view_id"], args["sql"],
                    args["expected_revision"], args.get("cursor_position"),
                )
            if name == "view_run":
                return self._view_run(arguments)
            if name == "view_check":
                args = self._arguments(name, arguments, {"workspace_id", "view_id", "cursor_position"}, {"workspace_id", "view_id"})
                view = self._workspaces.get_view(args["workspace_id"], args["view_id"])
                return {"workspace_id": view["workspace_id"], "view_id": view["view_id"]} | self.check(view["sql"], args.get("cursor_position"))
            if name == "view_fetch":
                return self._view_fetch(arguments)
            if name == "view_focus":
                args = self._arguments(name, arguments, {"workspace_id", "view_id"}, {"workspace_id", "view_id"})
                return self._workspaces.focus(args["workspace_id"], args["view_id"])
            if name == "view_rename":
                args = self._arguments(name, arguments, {"workspace_id", "view_id", "name"}, {"workspace_id", "view_id", "name"})
                return self._workspaces.rename(args["workspace_id"], args["view_id"], args["name"])
            if name == "view_remove":
                args = self._arguments(name, arguments, {"workspace_id", "view_id"}, {"workspace_id", "view_id"})
                response, query_id = self._workspaces.remove(args["workspace_id"], args["view_id"])
                self._unpin_result(query_id)
                return response
            if name == "view_save":
                args = self._arguments(name, arguments, {"workspace_id", "view_id"}, {"workspace_id", "view_id"})
                view = self._workspaces.get_view(args["workspace_id"], args["view_id"])
                return {"workspace_id": view["workspace_id"], "view_id": view["view_id"]} | self.save_view(view["sql"], view.get("name"))
            if name == "query_log_list":
                args = self._arguments(name, arguments, {"limit"})
                return self._query_log.list(args.get("limit", 20))
            if name == "query_log_get":
                args = self._arguments(name, arguments, {"log_id"}, {"log_id"})
                return self._query_log.get(args["log_id"])
            raise ValueError("unknown Workbench interface operation")

    def _view_run(self, arguments: object) -> dict[str, Any]:
        args = self._arguments("view_run", arguments, {"workspace_id", "view_id", "cursor_position", "preview", "save", "name"}, {"workspace_id", "view_id"})
        save = args.get("save", False)
        if type(save) is not bool:
            raise ValueError("save must be a boolean")
        if args.get("name") is not None and not save:
            raise ValueError("name is only supported when save is true")
        preview = QueryStore._preview(args.get("preview"))
        if save:
            SavedQueryStore._name(args.get("name"))
        current = self._workspaces.get_view(args["workspace_id"], args["view_id"])
        selected = select_statement(current["sql"], args.get("cursor_position"))
        view, prior = self._workspaces.clear_result(args["workspace_id"], args["view_id"])
        self._unpin_result(prior)
        self._drop_result(prior)
        try:
            result = self._run_store(selected, preview=preview, include_rows=False)
            metadata = self._result_metadata(result)
            assert self._store is not None
            self._store.pin(metadata["query_id"])
            saved: dict[str, Any] = {}
            if save:
                try:
                    saved = self._saved_queries.save_query(selected, args.get("name"))
                except ValueError as error:
                    print(f"saved query failed: {error}", file=sys.stderr)
                    saved = {"save_error": str(error)}
        except WorkbenchUnavailableError:
            raise
        except QueryExecutionError as error:
            metadata, saved = self._failed_metadata(error), {}
        except ValueError as error:
            metadata, saved = self._failed_metadata(error), {}
        self._log_attempt(selected, metadata)
        self._workspaces.set_result(args["workspace_id"], args["view_id"], metadata)
        return {"workspace_id": view["workspace_id"], "view_id": view["view_id"], "revision": view["revision"]} | metadata | saved

    def _view_fetch(self, arguments: object) -> dict[str, Any]:
        args = self._arguments("view_fetch", arguments, {"workspace_id", "view_id", "offset", "page_size", "preview", "grid"}, {"workspace_id", "view_id"})
        if "grid" in args and not isinstance(args["grid"], dict):
            raise ValueError("grid must be an object")
        view = self._workspaces.get_view(args["workspace_id"], args["view_id"])
        result = view.get("result")
        if not isinstance(result, dict) or result.get("status") != "success" or not isinstance(result.get("query_id"), str):
            raise ValueError("view has no current result")
        page_size = self._limit(args.get("page_size", 100), "page_size")
        preview = QueryStore._preview(args.get("preview"))
        offset = self._offset(args.get("offset", 0))
        self._start()
        assert self._store is not None
        self._store.prune_results()
        page = self._store.page(
            result["query_id"], offset, page_size=page_size,
            preview=preview, grid=args.get("grid"),
        )
        return {"workspace_id": view["workspace_id"], "view_id": view["view_id"]} | page

    def page(
        self, query_id: str, offset: int, page_size: int = 100, *, grid: object = None,
    ) -> dict[str, Any]:
        self._start()
        assert self._store is not None
        self._store.prune_results()
        return self._store.page(query_id, offset, page_size=page_size, grid=grid)

    def check(self, sql: str, cursor_position: int | None = None) -> dict[str, Any]:
        selected = select_statement(sql, cursor_position)
        self._start()
        assert self._store is not None
        return self._store.check(selected)

    def save_view(self, sql: str, name: str | None = None) -> dict[str, Any]:
        return self._saved_queries.save_view(sql, name)

    def load(self, reference: str) -> dict[str, str]:
        return self._saved_queries.load(reference)

    def saved_list(self, limit: int = 20) -> dict[str, list[dict[str, str]]]:
        return self._saved_queries.list(limit)

    def schema(self) -> dict[str, dict[str, list[dict[str, str]]]]:
        self._start()
        assert self._store is not None
        return self._store.schema()

    def discard_derived_state(self) -> None:
        """Discard only this Workbench's rebuildable database before a full reread."""
        self.close()
        self._database_path.unlink(missing_ok=True)
        self._database_path.with_name(f"{self._database_path.name}.wal").unlink(missing_ok=True)
        temporary = self._database_path.parent / "duckdb-temp"
        if temporary.is_dir():
            shutil.rmtree(temporary)

    def close(self) -> None:
        self._stop.set()
        if self._thread is not None:
            self._thread.join()
        if self._store is not None:
            self._store.close()
        self._query_log.close()
