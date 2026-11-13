"""Workbench interface operations."""
from __future__ import annotations
import sys
from typing import Any
from .errors import QueryExecutionError, WorkbenchUnavailableError
from .query_store import QueryStore
from .result_delivery import deliver, validate_delivery, result_metadata, failed_metadata
from .saved_queries import SavedQueryStore
from .statements import select_statement
from .workspace import WorkspaceStore


class ServiceInterface:
    def run(
        self, sql: str, page_size: int = 100, cursor_position: int | None = None,
        *, save: bool = False, preview: int | None = None, name: str | None = None,
        result_delivery: str = "file", result_format: str = "json_matrix",
    ) -> dict[str, Any]:
        validate_delivery(result_delivery, result_format)
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
                except (ValueError, OSError) as error:
                    print(f"saved query failed: {error}", file=sys.stderr)
                    result |= {"outcome": "partial", "save_error": str(error)}
            self._log_attempt(selected, result_metadata(result))
            assert self._store is not None
            return deliver(self._store, self._root, result, result_delivery, result_format, full=True)
        except ValueError as error:
            self._log_attempt(selected, failed_metadata(error))
            raise
        except (QueryExecutionError, WorkbenchUnavailableError) as error:
            self._log_attempt(selected, failed_metadata(error))
            raise
    def _run_store(
        self, selected: str, *, page_size: int = 100, preview: int | None = None,
        include_rows: bool,
    ) -> dict[str, Any]:
        self._flush_lifecycle_changes()
        assert self._store is not None
        self._store.prune_results()
        return self._store.run(selected, page_size=page_size, preview=preview, include_rows=include_rows)
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
            metadata = result_metadata(result)
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
            metadata, saved = failed_metadata(error), {}
        except ValueError as error:
            metadata, saved = failed_metadata(error), {}
        self._log_attempt(selected, metadata)
        self._workspaces.set_result(args["workspace_id"], args["view_id"], metadata)
        return {"workspace_id": view["workspace_id"], "view_id": view["view_id"], "revision": view["revision"]} | metadata | saved

    def _view_fetch(self, arguments: object) -> dict[str, Any]:
        args = self._arguments("view_fetch", arguments, {"workspace_id", "view_id", "offset", "page_size", "preview", "grid", "result_delivery", "result_format"}, {"workspace_id", "view_id"})
        if "grid" in args and not isinstance(args["grid"], dict):
            raise ValueError("grid must be an object")
        validate_delivery(args.get("result_delivery", "file"), args.get("result_format", "json_matrix"))
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
        page = deliver(self._store, self._root, page, args.get("result_delivery", "file"), args.get("result_format", "json_matrix"))
        return {"workspace_id": view["workspace_id"], "view_id": view["view_id"]} | page

