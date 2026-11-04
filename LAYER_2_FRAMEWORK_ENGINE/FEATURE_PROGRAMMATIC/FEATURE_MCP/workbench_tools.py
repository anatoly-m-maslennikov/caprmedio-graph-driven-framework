# CA-R-2728@5
# CA-R-2729@6
# CA-R-2776@3
# CA-M-470@3
# CA-D-673@10

"""Native MCP adapters for the Project-owned Workbench service."""

from __future__ import annotations

import asyncio
from pathlib import Path
import sys
from typing import Any

from mcp import types

tools = str(Path(__file__).resolve().parents[1] / "FEATURE_TOOLS")
if tools not in sys.path:
    sys.path.insert(0, tools)
from operation_error_boundary import ExplicitBlockingRuntimeFailure  # noqa: E402

RUN, PAGE, CHECK, SCHEMA = "query_run", "query_page", "query_check", "query_schema"
SAVE, SAVE_WORKSHEET, LOAD, SAVED_LIST = "query_save", "worksheet_save", "query_load", "query_saved_list"
NATIVE_TOOLS = (RUN, PAGE, CHECK, SCHEMA, SAVE, SAVE_WORKSHEET, LOAD, SAVED_LIST)

_CURSOR = {"type": "integer", "minimum": 0}
_SQL = {"type": "string"}
_RUN_SCHEMA = {"type": "object", "properties": {"sql": _SQL, "page_size": {"type": "integer", "minimum": 1, "maximum": 1000}, "cursor_position": _CURSOR}, "required": ["sql"], "additionalProperties": False}
_CHECK_SCHEMA = {"type": "object", "properties": {"sql": _SQL, "cursor_position": _CURSOR}, "required": ["sql"], "additionalProperties": False}
_PAGE_SCHEMA = {"type": "object", "properties": {"query_id": _SQL, "offset": {"type": "integer", "minimum": 0}, "page_size": {"type": "integer", "minimum": 1, "maximum": 1000}}, "required": ["query_id", "offset"], "additionalProperties": False}
_SAVE_SCHEMA = {"type": "object", "properties": {"sql": _SQL, "cursor_position": _CURSOR, "name": _SQL}, "required": ["sql"], "additionalProperties": False}
_WORKSHEET_SCHEMA = {"type": "object", "properties": {"sql": _SQL, "name": _SQL}, "required": ["sql"], "additionalProperties": False}
_LOAD_SCHEMA = {"type": "object", "properties": {"reference": _SQL}, "required": ["reference"], "additionalProperties": False}
_LIST_SCHEMA = {"type": "object", "properties": {"limit": {"type": "integer", "minimum": 1, "maximum": 1000}}, "additionalProperties": False}
_EMPTY_SCHEMA = {"type": "object", "properties": {}, "additionalProperties": False}


def native_tools() -> tuple[types.Tool, ...]:
    schemas = {RUN: _RUN_SCHEMA, PAGE: _PAGE_SCHEMA, CHECK: _CHECK_SCHEMA, SCHEMA: _EMPTY_SCHEMA,
               SAVE: _SAVE_SCHEMA, SAVE_WORKSHEET: _WORKSHEET_SCHEMA, LOAD: _LOAD_SCHEMA,
               SAVED_LIST: _LIST_SCHEMA}
    writes = {SAVE, SAVE_WORKSHEET}
    return tuple(types.Tool(
        name=name, description=f"Workbench {name}.",
        annotations=types.ToolAnnotations(read_only_hint=name not in writes, destructive_hint=False,
                                          idempotent_hint=name not in writes, open_world_hint=False),
        input_schema=schemas[name],
    ) for name in NATIVE_TOOLS)


class WorkbenchTools:
    """One lazy Workbench owner per Project Gateway."""

    def __init__(self, root: Path) -> None:
        self.root, self._service = root, None

    def _owner(self) -> Any:
        if self._service is None:
            apps = str(Path(__file__).resolve().parents[1] / "FEATURE_APPS")
            if apps not in sys.path:
                sys.path.insert(0, apps)
            from APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.service import WorkbenchService
            self._service = WorkbenchService(self.root)
        return self._service

    async def call(self, name: str, arguments: Any) -> dict[str, Any]:
        try:
            if name == RUN:
                sql, page_size, cursor = self._run(arguments)
                return await asyncio.to_thread(self._owner().run, sql, page_size=page_size, cursor_position=cursor)
            if name == CHECK:
                sql, cursor = self._sql(arguments, {"sql", "cursor_position"})
                return await asyncio.to_thread(self._owner().check, sql, cursor_position=cursor)
            if name == PAGE:
                query_id, offset, page_size = self._page(arguments)
                return await asyncio.to_thread(self._owner().page, query_id, offset, page_size=page_size)
            if name == SCHEMA:
                self._empty(arguments)
                return await asyncio.to_thread(self._owner().schema)
            if name == SAVE:
                sql, cursor = self._sql(arguments, {"sql", "cursor_position", "name"})
                return await asyncio.to_thread(self._owner().save, sql, cursor_position=cursor, name=self._name(arguments))
            if name == SAVE_WORKSHEET:
                sql, _ = self._sql(arguments, {"sql", "name"})
                return await asyncio.to_thread(self._owner().save_worksheet, sql, name=self._name(arguments))
            if name == LOAD:
                reference, _ = self._sql(arguments, {"reference"}, key="reference")
                return await asyncio.to_thread(self._owner().load, reference)
            if name == SAVED_LIST:
                return await asyncio.to_thread(self._owner().saved_list, limit=self._limit(arguments))
            raise ValueError("Unknown Workbench tool")
        except Exception as error:
            self._raise_known(error)

    @staticmethod
    def _raise_known(error: Exception) -> None:
        if isinstance(error, ValueError):
            raise ExplicitBlockingRuntimeFailure("query_error", str(error)) from error
        if isinstance(error, RuntimeError):
            reason = str(error)
            if reason.startswith(("query failed:", "query result delivery failed:", "query page failed:", "query page delivery failed:")):
                raise ExplicitBlockingRuntimeFailure("query_error", reason) from error
            if reason == "query store unavailable; Workbench restart required" or reason.startswith(("Workbench indexing failed; restart required:", "Workbench startup failed; restart required:")):
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

    def _run(self, arguments: Any) -> tuple[str, int, int | None]:
        sql, cursor = self._sql(arguments, {"sql", "page_size", "cursor_position"})
        return sql, self._page_size(arguments), cursor

    def _page(self, arguments: Any) -> tuple[str, int, int]:
        if not isinstance(arguments, dict) or set(arguments) - {"query_id", "offset", "page_size"} or {"query_id", "offset"} - set(arguments):
            raise ValueError("Expected query_id, offset, and optional page_size")
        query_id, offset = arguments["query_id"], arguments["offset"]
        if not isinstance(query_id, str):
            raise ValueError("query_id must be a string")
        if isinstance(offset, bool) or not isinstance(offset, int) or offset < 0:
            raise ValueError("offset must be a non-negative integer")
        return query_id, offset, self._page_size(arguments)

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
        if self._service is not None:
            await asyncio.to_thread(self._service.close)


__all__ = ["CHECK", "LOAD", "NATIVE_TOOLS", "PAGE", "RUN", "SAVE", "SAVED_LIST", "SAVE_WORKSHEET", "SCHEMA", "WorkbenchTools", "native_tools"]
