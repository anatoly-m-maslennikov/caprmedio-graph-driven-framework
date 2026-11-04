# CA-R-2728@2
# CA-R-2729@3
# CA-M-462@7
# CA-M-463@4
# CA-D-673@7

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


RUN = "query_run"
CHECK = "query_check"
PAGE = "query_page"
_RUN_SCHEMA = {
    "type": "object",
    "properties": {
        "sql": {"type": "string"},
        "page_size": {"type": "integer", "minimum": 1, "maximum": 1000},
    },
    "required": ["sql"],
    "additionalProperties": False,
}
_CHECK_SCHEMA = {
    "type": "object",
    "properties": {"sql": {"type": "string"}},
    "required": ["sql"],
    "additionalProperties": False,
}
_PAGE_SCHEMA = {
    "type": "object",
    "properties": {
        "query_id": {"type": "string"},
        "offset": {"type": "integer", "minimum": 0},
        "page_size": {"type": "integer", "minimum": 1, "maximum": 1000},
    },
    "required": ["query_id", "offset"],
    "additionalProperties": False,
}


def native_tools() -> tuple[types.Tool, ...]:
    return (
        types.Tool(
            name=RUN,
            description="Run one read-only native SQL query against the Project Workbench.",
            annotations=types.ToolAnnotations(
                read_only_hint=True, destructive_hint=False, idempotent_hint=True,
                open_world_hint=False,
            ),
            input_schema=_RUN_SCHEMA,
        ),
        types.Tool(
            name=CHECK,
            description="Check one read-only native SQL query against the Project Workbench.",
            annotations=types.ToolAnnotations(
                read_only_hint=True, destructive_hint=False, idempotent_hint=True,
                open_world_hint=False,
            ),
            input_schema=_CHECK_SCHEMA,
        ),
        types.Tool(
            name=PAGE,
            description="Read one stored page from a Project Workbench query.",
            annotations=types.ToolAnnotations(
                read_only_hint=True, destructive_hint=False, idempotent_hint=True,
                open_world_hint=False,
            ),
            input_schema=_PAGE_SCHEMA,
        ),
    )


class WorkbenchTools:
    """One lazy Workbench owner per Project Gateway."""

    def __init__(self, root: Path) -> None:
        self.root = root
        self._service: Any | None = None

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
                sql, page_size = self._run_arguments(arguments)
                return await asyncio.to_thread(self._owner().run, sql, page_size=page_size)
            if name == CHECK:
                sql = self._sql(arguments, {"sql"})
                return await asyncio.to_thread(self._owner().check, sql)
            if name == PAGE:
                query_id, offset, page_size = self._page_arguments(arguments)
                return await asyncio.to_thread(
                    self._owner().page, query_id, offset, page_size=page_size
                )
            raise ValueError("Unknown Workbench tool")
        except ValueError as error:
            raise ExplicitBlockingRuntimeFailure("query_error", str(error)) from error
        except RuntimeError as error:
            reason = str(error)
            if reason.startswith((
                "query failed:", "query result delivery failed:", "query page failed:",
                "query page delivery failed:",
            )):
                raise ExplicitBlockingRuntimeFailure("query_error", reason) from error
            if reason == "query store unavailable; Workbench restart required" or reason.startswith((
                "Workbench indexing failed; restart required:",
                "Workbench startup failed; restart required:",
            )):
                raise ExplicitBlockingRuntimeFailure(
                    "workbench_unavailable", "Workbench unavailable; restart required"
                ) from error
            raise

    @staticmethod
    def _sql(arguments: Any, allowed: set[str]) -> str:
        if not isinstance(arguments, dict) or set(arguments) - allowed or "sql" not in arguments:
            raise ValueError(f"Expected only {' and '.join(sorted(allowed))}")
        sql = arguments["sql"]
        if not isinstance(sql, str):
            raise ValueError("sql must be a string")
        return sql

    @staticmethod
    def _page_size(arguments: dict[str, Any]) -> int:
        value = arguments.get("page_size", 100)
        if isinstance(value, bool) or not isinstance(value, int):
            raise ValueError("page_size must be an integer")
        if not 1 <= value <= 1000:
            raise ValueError("page_size must be between 1 and 1000")
        return value

    def _run_arguments(self, arguments: Any) -> tuple[str, int]:
        sql = self._sql(arguments, {"sql", "page_size"})
        return sql, self._page_size(arguments)

    def _page_arguments(self, arguments: Any) -> tuple[str, int, int]:
        if not isinstance(arguments, dict) or set(arguments) - {"query_id", "offset", "page_size"} or {
            "query_id", "offset"
        } - set(arguments):
            raise ValueError("Expected query_id, offset, and optional page_size")
        query_id, offset = arguments["query_id"], arguments["offset"]
        if not isinstance(query_id, str):
            raise ValueError("query_id must be a string")
        if isinstance(offset, bool) or not isinstance(offset, int) or offset < 0:
            raise ValueError("offset must be a non-negative integer")
        return query_id, offset, self._page_size(arguments)

    async def close(self) -> None:
        if self._service is not None:
            await asyncio.to_thread(self._service.close)


__all__ = ["CHECK", "PAGE", "RUN", "WorkbenchTools", "native_tools"]
