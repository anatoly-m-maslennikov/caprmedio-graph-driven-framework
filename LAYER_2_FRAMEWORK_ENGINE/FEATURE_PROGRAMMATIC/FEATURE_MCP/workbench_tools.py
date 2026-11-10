# CA-R-2728@6
# CA-R-2776@6
# CA-M-470@8
# CA-D-673@18
# CA-R-2902@4
# CA-R-2903@2
# CA-D-681@8
# CA-R-2782@2
# CA-D-676@2
# CA-R-2786@1
# CA-M-474@1
# CA-D-679@1
# CA-R-2953@1
# CA-R-2952@1
# CA-M-491@1
# CA-D-696@1

"""Native MCP adapters for the Project-owned Workbench service."""

from __future__ import annotations

import asyncio
from pathlib import Path
import sys
import threading
from typing import TYPE_CHECKING, Any, NoReturn

from mcp import types

if TYPE_CHECKING:
    from APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.service import WorkbenchService

tools = str(Path(__file__).resolve().parents[1] / "FEATURE_TOOLS")
apps = str(Path(__file__).resolve().parents[1] / "FEATURE_APPS")
for location in (tools, apps):
    if location not in sys.path:
        sys.path.insert(0, location)
from operation_error_boundary import ExplicitBlockingRuntimeFailure  # noqa: E402
from APP_WORKBENCH.FEATURE_CODEX_EXTENSION import mcp_app_probe  # noqa: E402
from APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.errors import (  # noqa: E402
    QueryExecutionError, WorkbenchUnavailableError,
)

RUN, PAGE, CHECK, SCHEMA = "query_run", "query_page", "query_check", "query_schema"
SAVE_VIEW, LOAD, SAVED_LIST = "view_save", "query_load", "query_saved_list"
RESTART = "workbench_restart"
REREAD = "workbench_reread"
SYNC_STATUS = "workbench_status"
WORKSPACE_OPEN, WORKSPACE_LIST, WORKSPACE_GET = "workspace_open", "workspace_list", "workspace_get"
VIEW_CREATE, VIEW_DUPLICATE, VIEW_LIST, VIEW_GET, VIEW_UPDATE = (
    "view_create", "view_duplicate", "view_list", "view_get", "view_update"
)
VIEW_RUN, VIEW_CHECK, VIEW_FETCH, VIEW_FOCUS = "view_run", "view_check", "view_fetch", "view_focus"
VIEW_RENAME, VIEW_REMOVE = "view_rename", "view_remove"
QUERY_LOG_LIST, QUERY_LOG_GET = "query_log_list", "query_log_get"
INTERFACE_TOOLS = (
    WORKSPACE_OPEN, WORKSPACE_LIST, WORKSPACE_GET, VIEW_CREATE, VIEW_DUPLICATE, VIEW_LIST, VIEW_GET,
    VIEW_UPDATE, VIEW_RUN, VIEW_CHECK, VIEW_FETCH, VIEW_FOCUS, VIEW_RENAME, VIEW_REMOVE,
    QUERY_LOG_LIST, QUERY_LOG_GET,
)
NATIVE_TOOLS = (*mcp_app_probe.TOOL_NAMES, RUN, PAGE, CHECK, SCHEMA, SAVE_VIEW, LOAD, SAVED_LIST, *INTERFACE_TOOLS, RESTART, REREAD, SYNC_STATUS)

_CURSOR = {"type": "integer", "minimum": 0}
_SQL = {"type": "string"}
_DELIVERY = {"type": "string", "enum": ["file", "inline"], "default": "file"}
_RESULT_FORMAT = {"type": "string", "enum": ["json_matrix", "csv", "toon"], "default": "json_matrix"}
_PREVIEW = {"type": "integer", "minimum": 0}
_RUN_SCHEMA = {"type": "object", "properties": {"sql": _SQL, "page_size": {"type": "integer", "minimum": 1, "maximum": 1000}, "cursor_position": _CURSOR, "preview": _PREVIEW, "save": {"type": "boolean", "default": False}, "name": _SQL, "result_delivery": _DELIVERY, "result_format": _RESULT_FORMAT}, "required": ["sql"], "additionalProperties": False}
_CHECK_SCHEMA = {"type": "object", "properties": {"sql": _SQL, "cursor_position": _CURSOR}, "required": ["sql"], "additionalProperties": False}
_COLUMN_INDEX = {"type": "integer", "minimum": 0}
_GRID_ORDER = {"type": "object", "properties": {"column": _COLUMN_INDEX, "direction": {"type": "string", "enum": ["asc", "desc"]}}, "required": ["column", "direction"], "additionalProperties": False}
_GRID_FILTER = {"type": "object", "properties": {"column": _COLUMN_INDEX, "operator": {"type": "string", "enum": ["contains"]}, "value": _SQL}, "required": ["column", "operator", "value"], "additionalProperties": False}
_GRID_SCHEMA = {"type": "object", "properties": {"sort": {"type": "array", "items": _GRID_ORDER}, "filters": {"type": "array", "items": _GRID_FILTER}, "group_by": _GRID_ORDER}, "additionalProperties": False}
_PAGE_SCHEMA = {"type": "object", "properties": {"grid": _GRID_SCHEMA, "query_id": _SQL, "offset": {"type": "integer", "minimum": 0, "default": 0}, "page_size": {"type": "integer", "minimum": 1, "maximum": 1000}, "preview": _PREVIEW, "result_delivery": _DELIVERY, "result_format": _RESULT_FORMAT}, "required": ["query_id"], "additionalProperties": False}
_VIEW_SCHEMA = {"type": "object", "properties": {"sql": _SQL, "name": _SQL}, "required": ["sql"], "additionalProperties": False}
_LOAD_SCHEMA = {"type": "object", "properties": {"reference": _SQL}, "required": ["reference"], "additionalProperties": False}
_LIST_SCHEMA = {"type": "object", "properties": {"limit": {"type": "integer", "minimum": 1, "maximum": 1000}}, "additionalProperties": False}
_EMPTY_SCHEMA = {"type": "object", "properties": {}, "additionalProperties": False}
_WORKSPACE_ID = {"type": "string", "minLength": 1}
_VIEW_ID = {"type": "string", "minLength": 1}
_POSITION = {"type": "string", "enum": ["first", "last"], "default": "last"}
_WORKSPACE_OPEN_SCHEMA = {"type": "object", "properties": {"session_id": _WORKSPACE_ID}, "required": ["session_id"], "additionalProperties": False}
_WORKSPACE_GET_SCHEMA = {"type": "object", "properties": {"workspace_id": _WORKSPACE_ID}, "required": ["workspace_id"], "additionalProperties": False}
_VIEW_CREATE_SCHEMA = {"type": "object", "properties": {"workspace_id": _WORKSPACE_ID, "position": _POSITION, "name": _SQL}, "required": ["workspace_id"], "additionalProperties": False}
_VIEW_DUPLICATE_SCHEMA = {"type": "object", "properties": {"workspace_id": _WORKSPACE_ID, "view_id": _VIEW_ID}, "required": ["workspace_id", "view_id"], "additionalProperties": False}
_VIEW_GET_SCHEMA = {"type": "object", "properties": {"workspace_id": _WORKSPACE_ID, "view_id": _VIEW_ID}, "required": ["workspace_id", "view_id"], "additionalProperties": False}
_VIEW_UPDATE_SCHEMA = {"type": "object", "properties": {"workspace_id": _WORKSPACE_ID, "view_id": _VIEW_ID, "sql": _SQL, "cursor_position": _CURSOR, "expected_revision": {"type": "integer", "minimum": 0}}, "required": ["workspace_id", "view_id", "sql", "expected_revision"], "additionalProperties": False}
_VIEW_RUN_SCHEMA = {"type": "object", "properties": {"workspace_id": _WORKSPACE_ID, "view_id": _VIEW_ID, "cursor_position": _CURSOR, "preview": _PREVIEW, "save": {"type": "boolean", "default": False}, "name": _SQL}, "required": ["workspace_id", "view_id"], "additionalProperties": False}
_VIEW_FETCH_SCHEMA = {"type": "object", "properties": {"grid": _GRID_SCHEMA, "workspace_id": _WORKSPACE_ID, "view_id": _VIEW_ID, "offset": {"type": "integer", "minimum": 0, "default": 0}, "page_size": {"type": "integer", "minimum": 1, "maximum": 1000, "default": 100}, "preview": _PREVIEW, "result_delivery": _DELIVERY, "result_format": _RESULT_FORMAT}, "required": ["workspace_id", "view_id"], "additionalProperties": False}
_VIEW_CHECK_SCHEMA = {"type": "object", "properties": {"workspace_id": _WORKSPACE_ID, "view_id": _VIEW_ID, "cursor_position": _CURSOR}, "required": ["workspace_id", "view_id"], "additionalProperties": False}
_VIEW_RENAME_SCHEMA = {"type": "object", "properties": {"workspace_id": _WORKSPACE_ID, "view_id": _VIEW_ID, "name": _SQL}, "required": ["workspace_id", "view_id", "name"], "additionalProperties": False}
_QUERY_LOG_GET_SCHEMA = {"type": "object", "properties": {"log_id": _WORKSPACE_ID}, "required": ["log_id"], "additionalProperties": False}
# shortcut: backend validates exclusive save modes, upgrade when the shared selector supports root schema unions.
_SAVE_VIEW_SCHEMA = {"type": "object", "properties": {"workspace_id": _WORKSPACE_ID, "view_id": _VIEW_ID, "sql": _SQL, "name": _SQL}, "additionalProperties": False}


def native_tools() -> tuple[types.Tool, ...]:
    schemas = {RUN: _RUN_SCHEMA, PAGE: _PAGE_SCHEMA, CHECK: _CHECK_SCHEMA, SCHEMA: _EMPTY_SCHEMA,
               SAVE_VIEW: _SAVE_VIEW_SCHEMA, LOAD: _LOAD_SCHEMA, SAVED_LIST: _LIST_SCHEMA,
               WORKSPACE_OPEN: _WORKSPACE_OPEN_SCHEMA, WORKSPACE_LIST: _EMPTY_SCHEMA,
               WORKSPACE_GET: _WORKSPACE_GET_SCHEMA, VIEW_CREATE: _VIEW_CREATE_SCHEMA,
               VIEW_DUPLICATE: _VIEW_DUPLICATE_SCHEMA,
               VIEW_LIST: _WORKSPACE_GET_SCHEMA, VIEW_GET: _VIEW_GET_SCHEMA,
               VIEW_UPDATE: _VIEW_UPDATE_SCHEMA, VIEW_RUN: _VIEW_RUN_SCHEMA,
               VIEW_CHECK: _VIEW_CHECK_SCHEMA, VIEW_FETCH: _VIEW_FETCH_SCHEMA,
               VIEW_FOCUS: _VIEW_GET_SCHEMA, VIEW_RENAME: _VIEW_RENAME_SCHEMA,
               VIEW_REMOVE: _VIEW_GET_SCHEMA, QUERY_LOG_LIST: _LIST_SCHEMA,
               QUERY_LOG_GET: _QUERY_LOG_GET_SCHEMA, RESTART: _EMPTY_SCHEMA, REREAD: _EMPTY_SCHEMA,
               SYNC_STATUS: _EMPTY_SCHEMA}
    writes = {RUN, SAVE_VIEW, WORKSPACE_OPEN, VIEW_CREATE, VIEW_DUPLICATE, VIEW_UPDATE, VIEW_RUN, VIEW_FOCUS,
              VIEW_RENAME, VIEW_REMOVE, RESTART, REREAD}
    descriptions = {
        LOAD: "Load an explicitly requested Bookmark or saved View.",
        SAVED_LIST: "List recent Bookmark and saved View metadata.",
        SYNC_STATUS: "Read source-indexing status without starting or restarting Workbench.",
        WORKSPACE_OPEN: "Initialize or resume the Workspace bound to one browser or native session.",
        WORKSPACE_LIST: "List known Workspace IDs for the selected Project.",
        WORKSPACE_GET: "Get Workspace Views, active View, and result metadata without result rows.",
        VIEW_CREATE: "Create a stable View in a Workspace.",
        VIEW_DUPLICATE: "Duplicate one View's query and cursor into a new independent View.",
        VIEW_LIST: "List ordered Workspace Views and their result metadata.",
        VIEW_GET: "Get one View's SQL, revision, and result metadata without rows.",
        VIEW_UPDATE: "Update one View using its expected revision.",
        VIEW_RUN: "Run one View and return metadata without result rows.",
        VIEW_CHECK: "Check one View without recording a query log entry.",
        VIEW_FETCH: "Fetch an optional page from one View's current result.",
        VIEW_FOCUS: "Set the active View for a Workspace.",
        VIEW_RENAME: "Rename one View.",
        VIEW_REMOVE: "Remove one View while retaining at least one View.",
        QUERY_LOG_LIST: "List retained query-log records without result rows.",
        QUERY_LOG_GET: "Get one retained query-log record without result rows.",
    }
    return mcp_app_probe.tools() + tuple(types.Tool(
        name=name, description=descriptions.get(name, f"Workbench {name.replace('_', ' ')}."),
        annotations=types.ToolAnnotations(read_only_hint=name not in writes, destructive_hint=name in {RESTART, REREAD},
                                          idempotent_hint=name not in writes, open_world_hint=False),
        input_schema=schemas[name],
        _meta={"ui": {"resourceUri": mcp_app_probe.WORKBENCH_URI}}
        if name == WORKSPACE_OPEN else None,
    ) for name in NATIVE_TOOLS if name not in mcp_app_probe.TOOL_NAMES)


class WorkbenchTools:
    """One lazy Workbench owner per Project Gateway."""

    def __init__(self, root: Path) -> None:
        self.root = root
        self._service: WorkbenchService | None = None
        self._lifecycle_lock = threading.RLock()

    def _owner(self) -> WorkbenchService:
        if self._service is None:
            from APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.service import WorkbenchService
            self._service = WorkbenchService(self.root)
        return self._service

    async def call(self, name: str, arguments: Any) -> dict[str, Any]:
        try:
            return await asyncio.to_thread(self._call, name, arguments)
        except Exception as error:
            self._raise_known(error)

    def _call(self, name: str, arguments: Any) -> dict[str, Any]:  # noqa: C901
        """Keep an owner alive for the complete synchronous Workbench operation."""
        if name in mcp_app_probe.TOOL_NAMES:
            self._empty(arguments)
            return mcp_app_probe.call(name)
        if name == SYNC_STATUS:
            self._empty(arguments)
            owner = self._service
            return owner.sync_status() if owner is not None else {"syncing": False, "last_synced_at": None}
        with self._lifecycle_lock:
            if name in INTERFACE_TOOLS:
                return self._owner().interface_call(name, arguments)
            if name == RUN:
                sql, page_size, cursor, save, preview, query_name, delivery, result_format = self._run(arguments)
                return self._owner().run(
                    sql, page_size=page_size, cursor_position=cursor,
                    save=save, preview=preview, name=query_name,
                    result_delivery=delivery, result_format=result_format,
                )
            if name == CHECK:
                sql, cursor = self._sql(arguments, {"sql", "cursor_position"})
                return self._owner().check(sql, cursor_position=cursor)
            if name == PAGE:
                query_id, offset, page_size, grid, preview, delivery, result_format = self._page(arguments)
                return self._owner().page(query_id, offset, page_size=page_size, grid=grid,
                                          preview=preview, result_delivery=delivery,
                                          result_format=result_format)
            if name == SCHEMA:
                self._empty(arguments)
                return self._owner().schema()
            if name == SAVE_VIEW:
                if isinstance(arguments, dict) and {"workspace_id", "view_id"} <= set(arguments):
                    return self._owner().interface_call(name, arguments)
                sql, _ = self._sql(arguments, {"sql", "name"})
                return self._owner().save_view(sql, name=self._name(arguments))
            if name == LOAD:
                reference, _ = self._sql(arguments, {"reference"}, key="reference")
                return self._owner().load(reference)
            if name == SAVED_LIST:
                return self._owner().saved_list(limit=self._limit(arguments))
            if name == RESTART:
                self._empty(arguments)
                if self._service is not None:
                    self._service.close()
                self._service = None
                self._owner().schema()
                return {"service": "workbench", "status": "ready"}
            if name == REREAD:
                self._empty(arguments)
                previous = self._owner()
                self._service = None
                previous.discard_derived_state()
                self._owner().schema()
                return {"service": "workbench", "status": "ready"}
            raise ValueError("Unknown Workbench tool")

    @staticmethod
    def _raise_known(error: Exception) -> NoReturn:
        if isinstance(error, ValueError):
            raise ExplicitBlockingRuntimeFailure("query_error", str(error)) from error
        if isinstance(error, QueryExecutionError):
            raise ExplicitBlockingRuntimeFailure("query_error", str(error)) from error
        if isinstance(error, WorkbenchUnavailableError):
            raise ExplicitBlockingRuntimeFailure("workbench_unavailable", "Workbench unavailable; restart required") from error
        raise error

    @staticmethod
    def _sql(arguments: Any, allowed: set[str], *, key: str = "sql") -> tuple[str, int | None]:
        if not isinstance(arguments, dict) or set(arguments) - allowed or key not in arguments:
            raise ValueError(f"Expected only {' and '.join(sorted(allowed))}")
        value, cursor = arguments[key], arguments.get("cursor_position")
        if not isinstance(value, str):
            raise ValueError(f"{key} must be a string")
        if cursor is not None and (isinstance(cursor, bool) or not isinstance(cursor, int) or cursor < 0):
            raise ValueError("cursor_position must be a non-negative integer")
        return value, cursor

    @staticmethod
    def _page_size(arguments: dict[str, Any]) -> int:
        value = arguments.get("page_size", 100)
        if isinstance(value, bool) or not isinstance(value, int):
            raise ValueError("page_size must be an integer")
        if not 1 <= value <= 1000:
            raise ValueError("page_size must be between 1 and 1000")
        return value

    @staticmethod
    def _name(arguments: dict[str, Any]) -> str | None:
        value = arguments.get("name")
        if value is not None and not isinstance(value, str):
            raise ValueError("name must be a string")
        return value

    @staticmethod
    def _result_options(arguments: dict[str, Any]) -> tuple[int | None, str, str]:
        preview = arguments.get("preview")
        if preview is not None and (isinstance(preview, bool) or not isinstance(preview, int) or preview < 0):
            raise ValueError("preview must be a non-negative integer")
        delivery = arguments.get("result_delivery", "file")
        if not isinstance(delivery, str) or delivery not in {"file", "inline"}:
            raise ValueError("result_delivery must be file or inline")
        result_format = arguments.get("result_format", "json_matrix")
        if not isinstance(result_format, str) or result_format not in {"json_matrix", "csv", "toon"}:
            raise ValueError("result_format must be json_matrix, csv or toon")
        return preview, delivery, result_format

    def _run(self, arguments: Any) -> tuple[str, int, int | None, bool, int | None, str | None, str, str]:
        sql, cursor = self._sql(arguments, {"sql", "page_size", "cursor_position", "save", "preview", "name", "result_delivery", "result_format"})
        save = arguments.get("save", False)
        if type(save) is not bool:
            raise ValueError("save must be a boolean")
        preview, delivery, result_format = self._result_options(arguments)
        if "name" in arguments and not isinstance(arguments["name"], str):
            raise ValueError("name must be a string")
        query_name = arguments.get("name")
        if query_name is not None and not save:
            raise ValueError("name is only valid when save is true")
        return sql, self._page_size(arguments), cursor, save, preview, query_name, delivery, result_format

    def _page(self, arguments: Any) -> tuple[str, int, int, Any, int | None, str, str]:
        allowed = {"query_id", "offset", "page_size", "grid", "preview", "result_delivery", "result_format"}
        if not isinstance(arguments, dict) or set(arguments) - allowed or "query_id" not in arguments:
            raise ValueError("Expected query_id and optional pagination, grid and result options")
        if "grid" in arguments and not isinstance(arguments["grid"], dict):
            raise ValueError("grid must be an object")
        query_id, offset = arguments["query_id"], arguments.get("offset", 0)
        if not isinstance(query_id, str):
            raise ValueError("query_id must be a string")
        if isinstance(offset, bool) or not isinstance(offset, int) or offset < 0:
            raise ValueError("offset must be a non-negative integer")
        preview, delivery, result_format = self._result_options(arguments)
        return query_id, offset, self._page_size(arguments), arguments.get("grid"), preview, delivery, result_format

    @staticmethod
    def _empty(arguments: Any) -> None:
        if arguments != {}:
            raise ValueError("Expected an empty object")

    @staticmethod
    def _limit(arguments: Any) -> int:
        if not isinstance(arguments, dict) or set(arguments) - {"limit"}:
            raise ValueError("Expected optional limit")
        value = arguments.get("limit", 20)
        if isinstance(value, bool) or not isinstance(value, int) or not 1 <= value <= 1000:
            raise ValueError("limit must be an integer from 1 to 1000")
        return value

    async def close(self) -> None:
        await asyncio.to_thread(self._close)

    def _close(self) -> None:
        with self._lifecycle_lock:
            if self._service is not None:
                self._service.close()
                self._service = None


__all__ = ["CHECK", "INTERFACE_TOOLS", "LOAD", "NATIVE_TOOLS", "PAGE", "QUERY_LOG_GET", "QUERY_LOG_LIST", "REREAD", "RESTART", "RUN", "SAVED_LIST", "SAVE_VIEW", "SCHEMA", "SYNC_STATUS", "VIEW_CHECK", "VIEW_CREATE", "VIEW_DUPLICATE", "VIEW_FETCH", "VIEW_FOCUS", "VIEW_GET", "VIEW_LIST", "VIEW_REMOVE", "VIEW_RENAME", "VIEW_RUN", "VIEW_UPDATE", "WORKSPACE_GET", "WORKSPACE_LIST", "WORKSPACE_OPEN", "WorkbenchTools", "native_tools"]
