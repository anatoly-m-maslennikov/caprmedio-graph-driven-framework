# CA-R-2727@2
# CA-R-2729@2
# CA-D-673@4
# CA-D-674@2

"""Small HTTP representation of the shared Project Workbench connector."""

from __future__ import annotations

from pathlib import Path
import sys
from typing import Any

from mcp import types
from starlette.requests import Request
from starlette.responses import HTMLResponse, JSONResponse
from starlette.routing import Route

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "FEATURE_TOOLS"))
from operation_error_boundary import ExplicitBlockingRuntimeFailure
from runtime_failure_diagnostics import report_failure
from workbench_tools import CHECK, RUN


_PAGE = """<!doctype html><html lang=\"en\"><meta charset=\"utf-8\"><title>Workbench</title>
<main><h1>Workbench</h1><form id=\"query\"><label for=\"sql\">SQL</label>
<textarea id=\"sql\" name=\"sql\" rows=\"12\" cols=\"80\"></textarea>{project_root}
<button formaction=\"/workbench/check\">Check</button><button formaction=\"/workbench/run\">Run</button></form>
<p id=\"counts\" aria-live=\"polite\"></p><pre id=\"results\" aria-live=\"polite\"></pre></main>
<script>document.querySelectorAll('button').forEach(button=>button.onclick=async event=>{{event.preventDefault();let form=document.querySelector('#query');let response=await fetch(button.formAction,{{method:'POST',headers:{{'content-type':'application/json'}},body:JSON.stringify(Object.fromEntries(new FormData(form)))}});let value=await response.json();document.querySelector('#counts').textContent=value.row_count===undefined?'':`${{value.row_count}} rows, ${{value.column_count}} columns`;document.querySelector('#results').textContent=response.ok?JSON.stringify(value,null,2):value.error;}});</script></html>"""


async def _arguments(request: Request, shared: bool) -> dict[str, str]:
    try:
        if request.headers.get("content-type", "").split(";", 1)[0] == "application/json":
            value = await request.json()
        else:
            value = dict(await request.form())
    except ValueError as error:
        raise ExplicitBlockingRuntimeFailure("query_error", str(error)) from error
    if not isinstance(value, dict) or not isinstance(value.get("sql"), str):
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


async def _execute(gateway: Any, name: str, arguments: dict[str, str], shared: bool) -> dict[str, Any]:
    if not shared:
        return await gateway.workbench.call(name, {"sql": arguments["sql"]})
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
    async def page(request: Request) -> HTMLResponse:
        project_root = ""
        if shared:
            project_root = request.query_params.get("project_root", "")
            try:
                gateway._selection(project_root)
            except (TypeError, ValueError) as error:
                return HTMLResponse(str(error), status_code=400)
            project_root = '<input type="hidden" name="project_root" value="' + project_root.replace("&", "&amp;").replace('"', "&quot;") + '">'
        return HTMLResponse(_PAGE.format(project_root=project_root))

    async def operation(request: Request) -> JSONResponse:
        name = RUN if request.url.path.endswith("/run") else CHECK
        try:
            return JSONResponse(await _execute(gateway, name, await _arguments(request, shared), shared))
        except Exception as error:
            return _error(gateway, error)

    return [
        Route("/workbench", page),
        Route("/workbench/run", operation, methods=["POST"]),
        Route("/workbench/check", operation, methods=["POST"]),
    ]


__all__ = ["routes"]
