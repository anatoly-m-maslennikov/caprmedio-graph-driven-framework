# CA-R-2728@2
# CA-R-2729@2
# CA-M-462@5
# CA-M-463@2
# CA-D-673@4

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
_SQL_SCHEMA = {
    "type": "object",
    "properties": {"sql": {"type": "string"}},
    "required": ["sql"],
    "additionalProperties": False,
}


def native_tools() -> tuple[types.Tool, types.Tool]:
    return (
        types.Tool(
            name=RUN,
            description="Run one read-only native SQL query against the Project Workbench.",
            annotations=types.ToolAnnotations(
                read_only_hint=True, destructive_hint=False, idempotent_hint=True,
                open_world_hint=False,
            ),
            input_schema=_SQL_SCHEMA,
        ),
        types.Tool(
            name=CHECK,
            description="Check one read-only native SQL query against the Project Workbench.",
            annotations=types.ToolAnnotations(
                read_only_hint=True, destructive_hint=False, idempotent_hint=True,
                open_world_hint=False,
            ),
            input_schema=_SQL_SCHEMA,
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
            from APP_WORKBENCH.service import WorkbenchService
            self._service = WorkbenchService(self.root)
        return self._service

    async def call(self, name: str, arguments: Any) -> dict[str, Any]:
        try:
            if not isinstance(arguments, dict) or set(arguments) != {"sql"}:
                raise ValueError("Expected only sql")
            sql = arguments["sql"]
            if not isinstance(sql, str):
                raise ValueError("sql must be a string")
            method = self._owner().run if name == RUN else self._owner().check
            return await asyncio.to_thread(method, sql)
        except ValueError as error:
            raise ExplicitBlockingRuntimeFailure("query_error", str(error)) from error
        except RuntimeError as error:
            reason = str(error)
            if reason.startswith(("query failed:", "query result delivery failed:")):
                raise ExplicitBlockingRuntimeFailure("query_error", reason) from error
            if reason == "query store unavailable; Workbench restart required" or reason.startswith((
                "Workbench indexing failed; restart required:",
                "Workbench startup failed; restart required:",
            )):
                raise ExplicitBlockingRuntimeFailure(
                    "workbench_unavailable", "Workbench unavailable; restart required"
                ) from error
            raise

    async def close(self) -> None:
        if self._service is not None:
            await asyncio.to_thread(self._service.close)


__all__ = ["CHECK", "RUN", "WorkbenchTools", "native_tools"]
