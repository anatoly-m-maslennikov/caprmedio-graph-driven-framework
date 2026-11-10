# Implementation of:
# Requirement: CA-R-3013
# Method: CA-M-506
# Delivery: CA-D-704

"""Registry provider that delegates the retained Workbench frontier."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from operation_error_boundary import ExplicitBlockingRuntimeFailure
from workbench_links import context_project_root, public_saved, public_workspace, validate_reference
from workbench_tools import LOAD, WORKSPACE_GET, WORKSPACE_OPEN, native_tools


class WorkbenchProvider:
    def __init__(self, gateway: Any) -> None:
        self.gateway = gateway

    async def call(self, name: str, arguments: dict[str, Any]) -> dict[str, Any]:
        return await self.gateway.workbench.call(name, arguments)

    def prepare_arguments(self, name: str, arguments: dict[str, Any], context: Any) -> dict[str, Any]:
        if name != LOAD or not isinstance(arguments.get("reference"), str):
            return arguments
        try:
            reference = validate_reference(
                arguments["reference"], getattr(context, "request", None), self.gateway.selection,
                context_project_root(context),
            )
        except ValueError as error:
            raise ExplicitBlockingRuntimeFailure("query_error", str(error)) from error
        return {**arguments, "reference": reference}

    def present_result(self, name: str, value: dict[str, Any], context: Any) -> dict[str, Any]:
        request = getattr(context, "request", None)
        if request is None:
            return value
        root = context_project_root(context)
        value = public_saved(value, request, self.gateway.selection, root)
        return public_workspace(value, request, self.gateway.selection, root) if name in {
            WORKSPACE_OPEN, WORKSPACE_GET,
        } else value

    async def close(self) -> None:
        return None


def create_provider(_root: Path, gateway: Any) -> WorkbenchProvider:
    return WorkbenchProvider(gateway)


def tool_descriptors():
    return native_tools()
