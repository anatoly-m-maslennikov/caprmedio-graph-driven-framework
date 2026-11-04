# CA-R-2727@4
# CA-R-2729@3
# CA-D-673@7
# CA-D-674@8

"""Small HTTP representation of the shared Project Workbench connector."""

from __future__ import annotations

import json
from collections.abc import Mapping
from pathlib import Path
import sys
from typing import Any

from mcp import types
from starlette.requests import Request
from starlette.responses import FileResponse, JSONResponse, StreamingResponse
from starlette.routing import Mount, Route
from starlette.staticfiles import StaticFiles

from http_paths import WORKBENCH_PATH

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "FEATURE_TOOLS"))
from operation_error_boundary import ExplicitBlockingRuntimeFailure
from runtime_failure_diagnostics import report_failure
from workbench_tools import CHECK, PAGE, RUN


_FRONTEND = (
    Path(__file__).resolve().parents[1]
    / "FEATURE_APPS"
    / "APP_WORKBENCH"
    / "FEATURE_WORKBENCH_FRONTEND"
    / "dist"
)


async def _arguments(request: Request, shared: bool, name: str) -> dict[str, Any]:
    try:
        if request.headers.get("content-type", "").split(";", 1)[0] == "application/json":
            value = await request.json()
        else:
            value = dict(await request.form())
    except ValueError as error:
        raise ExplicitBlockingRuntimeFailure("query_error", str(error)) from error
    if not isinstance(value, dict):
        raise ExplicitBlockingRuntimeFailure("query_error", "query arguments must be an object")
    if name == PAGE:
        if not isinstance(value.get("query_id"), str):
            raise ExplicitBlockingRuntimeFailure("query_error", "query_id must be a string")
        if type(value.get("offset")) is not int or value["offset"] < 0:
            raise ExplicitBlockingRuntimeFailure("query_error", "offset must be a non-negative integer")
    elif not isinstance(value.get("sql"), str):
        raise ExplicitBlockingRuntimeFailure("query_error", "sql must be a string")
    if shared and not isinstance(value.get("project_root"), str):
        raise ExplicitBlockingRuntimeFailure("query_error", "project_root must be a string")
    return value


def _error(gateway: Any, error: Exception) -> JSONResponse:
    failure, _ = report_failure(
        getattr(gateway, "root", None), error,
        component="MCP_HTTP", operation="workbench",
    )
    return JSONResponse({"error": failure.message}, status_code=400)


def _json_stream(value: dict[str, Any]):
    return json.JSONEncoder(ensure_ascii=False, allow_nan=False, separators=(",", ":")).iterencode(value)


def _project_name_matches(selection: Any, project_name: str) -> bool:
    settings = getattr(selection, "settings", None)
    project = settings.get("project") if isinstance(settings, Mapping) else None
    return isinstance(project, Mapping) and project.get("name") == project_name


def _unknown_project() -> JSONResponse:
    return JSONResponse({"error": "unknown Workbench project"}, status_code=404)


async def _execute(gateway: Any, name: str, arguments: dict[str, Any], shared: bool) -> dict[str, Any]:
    if not shared:
        return await gateway.workbench.call(
            name, {key: value for key, value in arguments.items() if key != "project_root"}
        )
    response = await gateway.call(
        None,
        types.CallToolRequestParams(name=name, arguments=arguments),
    )
    value = response.structured_content
    if response.is_error:
        raise ExplicitBlockingRuntimeFailure(
            "query_error",
            value.get("diagnostics", ["query failed"])[0] if isinstance(value, dict) else "query failed",
        )
    if not isinstance(value, dict):
        raise RuntimeError("Workbench returned an invalid result")
    return value


def routes(gateway: Any, *, shared: bool = False) -> list[Route]:
    async def page(request: Request):
        project_name = request.path_params["project_name"]
        if shared:
            project_root = request.query_params.get("project_root", "")
            try:
                selection = gateway._selection(project_root)
            except (TypeError, ValueError) as error:
                return JSONResponse({"error": str(error)}, status_code=400)
        else:
            selection = getattr(gateway, "selection", None)
        if not _project_name_matches(selection, project_name):
            return _unknown_project()
        if not (_FRONTEND / "index.html").is_file():
            return JSONResponse(
                {"error": "Workbench frontend is unavailable; build required"}, status_code=503
            )
        return FileResponse(_FRONTEND / "index.html")

    async def operation(request: Request):
        name = PAGE if request.url.path.endswith("/page") else RUN if request.url.path.endswith("/run") else CHECK
        try:
            arguments = await _arguments(request, shared, name)
            if shared:
                selection = gateway._selection(arguments["project_root"])
            else:
                selection = getattr(gateway, "selection", None)
            if not _project_name_matches(selection, request.path_params["project_name"]):
                return _unknown_project()
            return StreamingResponse(
                _json_stream(await _execute(gateway, name, arguments, shared)),
                media_type="application/json",
            )
        except Exception as error:
            return _error(gateway, error)

    return [
        Route(f"{WORKBENCH_PATH}/{{project_name}}", page),
        Route(f"{WORKBENCH_PATH}/{{project_name}}/run", operation, methods=["POST"]),
        Route(f"{WORKBENCH_PATH}/{{project_name}}/check", operation, methods=["POST"]),
        Route(f"{WORKBENCH_PATH}/{{project_name}}/page", operation, methods=["POST"]),
        Mount(
            f"{WORKBENCH_PATH}/assets",
            app=StaticFiles(directory=_FRONTEND / "assets", check_dir=False),
        ),
    ]


__all__ = ["routes"]
