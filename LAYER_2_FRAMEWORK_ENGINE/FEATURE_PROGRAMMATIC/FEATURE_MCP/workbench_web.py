# CA-R-2728@5
# CA-R-2729@6
# CA-R-2776@3
# CA-D-673@10
# CA-D-674@12
# CA-D-674@12

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
from workbench_links import public_saved, validate_reference
from workbench_tools import CHECK, LOAD, PAGE, RUN, SAVE, SAVED_LIST, SAVE_WORKSHEET, SCHEMA


_FRONTEND = (
    Path(__file__).resolve().parents[1]
    / "FEATURE_APPS"
    / "APP_WORKBENCH"
    / "FEATURE_WORKBENCH_FRONTEND"
    / "dist"
)


async def _arguments(request: Request, shared: bool, name: str) -> dict[str, Any]:  # noqa: C901
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
    elif name == LOAD:
        if not isinstance(value.get("reference"), str):
            raise ExplicitBlockingRuntimeFailure("query_error", "reference must be a string")
    elif name == SAVED_LIST:
        limit = value.get("limit", 20)
        if type(limit) is not int or not 1 <= limit <= 1000:
            raise ExplicitBlockingRuntimeFailure("query_error", "limit must be an integer from 1 to 1000")
    elif name != SCHEMA and not isinstance(value.get("sql"), str):
        raise ExplicitBlockingRuntimeFailure("query_error", "sql must be a string")
    if shared and not isinstance(value.get("project_root"), str):
        raise ExplicitBlockingRuntimeFailure("query_error", "project_root must be a string")
    return value


def _error(gateway: Any, request: Request, selection: Any, arguments: dict[str, Any], error: Exception) -> JSONResponse:
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
            value.get("error") if isinstance(value, dict) and isinstance(value.get("error"), str)
            else value.get("diagnostics", ["query failed"])[0] if isinstance(value, dict) else "query failed",
        )
    if not isinstance(value, dict):
        raise RuntimeError("Workbench returned an invalid result")
    return value


def routes(gateway: Any, *, shared: bool = False) -> list[Route]:  # noqa: C901
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

    def operation(name: str):
        async def endpoint(request: Request):  # noqa: C901
            arguments: dict[str, Any] = {}
            selection = None
            try:
                arguments = await _arguments(request, shared, name)
                selection = gateway._selection(arguments["project_root"]) if shared else getattr(gateway, "selection", None)
                if not _project_name_matches(selection, request.path_params["project_name"]):
                    return _unknown_project()
                if name == LOAD:
                    try:
                        arguments["reference"] = validate_reference(
                            arguments["reference"], request, selection, arguments.get("project_root"),
                        )
                    except ValueError as error:
                        raise ExplicitBlockingRuntimeFailure("query_error", str(error)) from error
                value = await _execute(gateway, name, arguments, shared)
                return StreamingResponse(
                    _json_stream(public_saved(value, request, selection, arguments.get("project_root"))),
                    media_type="application/json",
                )
            except Exception as error:
                return _error(gateway, request, selection, arguments, error)
        return endpoint

    return [
        Route(f"{WORKBENCH_PATH}/{{project_name}}", page),
        *[Route(f"{WORKBENCH_PATH}/{{project_name}}/{path}", operation(name), methods=["POST"])
          for path, name in (("run", RUN), ("page", PAGE), ("check", CHECK), ("schema", SCHEMA),
                             ("save", SAVE), ("worksheet-save", SAVE_WORKSHEET), ("load", LOAD),
                             ("saved-list", SAVED_LIST))],
        Mount(
            f"{WORKBENCH_PATH}/assets",
            app=StaticFiles(directory=_FRONTEND / "assets", check_dir=False),
        ),
    ]


__all__ = ["routes"]
