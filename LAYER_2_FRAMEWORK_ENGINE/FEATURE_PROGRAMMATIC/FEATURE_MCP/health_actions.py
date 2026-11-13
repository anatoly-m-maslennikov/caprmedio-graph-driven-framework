# CA-R-2782@5
# CA-D-677@1
# CA-D-679@1

"""Fixed native health-page actions."""

from __future__ import annotations

from typing import Any

from mcp import types
from starlette.requests import Request


async def _workbench_action(
    request: Request, gateway: Any, *, shared: bool, tool: str, verb: str,
) -> tuple[bool, str]:
    """Run one fixed Workbench health action through the MCP boundary."""
    if not shared and await request.body():
        return False, f"Workbench {verb} does not accept a request body."
    try:
        form = await request.form()
    except Exception:
        return False, f"Invalid Workbench {verb} request."
    items = list(form.multi_items())
    if shared:
        if len(items) != 1 or items[0][0] != "project_root" or not isinstance(items[0][1], str) or not items[0][1].strip():
            return False, "Enter one Project folder."
        arguments = {"project_root": items[0][1]}
    elif items:
        return False, f"Workbench {verb} does not accept form fields."
    else:
        arguments = {}
    try:
        result = await gateway.call(
            None,
            types.CallToolRequestParams(name=tool, arguments=arguments),
        )
    except Exception:
        return False, f"Workbench {verb} failed."
    value = result.structured_content
    if (
        not result.is_error
        and isinstance(value, dict)
        and value.get("service") == "workbench"
        and value.get("status") == "ready"
    ):
        return True, "Workbench is ready."
    return False, f"Workbench {verb} failed."


async def restart_workbench(request: Request, gateway: Any, *, shared: bool) -> tuple[bool, str]:
    return await _workbench_action(
        request, gateway, shared=shared, tool="workbench_restart", verb="restart",
    )


async def reread_workbench(request: Request, gateway: Any, *, shared: bool) -> tuple[bool, str]:
    return await _workbench_action(
        request, gateway, shared=shared, tool="workbench_reread", verb="full reread",
    )


__all__ = ["restart_workbench", "reread_workbench"]
