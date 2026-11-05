# CA-D-681@5

"""Read-only MCP Apps compatibility probe, served by the existing MCP gateway."""

from pathlib import Path
from typing import Any

from mcp import MCPError, types

URI = "ui://caprmedio/workbench-compatibility.html"
MIME_TYPE = "text/html;profile=mcp-app"
TOOL_NAMES = ("workbench_ui_probe", "workbench_ui_ping")


def tools() -> tuple[types.Tool, ...]:
    return tuple(types.Tool(
        name=name,
        description=("Render the CAPRMEDIO MCP App compatibility probe without a browser or project data."
                     if name == TOOL_NAMES[0] else "Read-only check of the MCP App tool bridge."),
        input_schema={"type": "object", "properties": {}, "additionalProperties": False},
        output_schema={"type": "object", "properties": {"message": {"type": "string"}},
                       "required": ["message"], "additionalProperties": False},
        annotations=types.ToolAnnotations(read_only_hint=True, destructive_hint=False,
                                          idempotent_hint=True, open_world_hint=False),
        _meta={"ui": {"resourceUri": URI}} if name == TOOL_NAMES[0] else None,
    ) for name in TOOL_NAMES)


def call(name: str) -> dict[str, str]:
    if name not in TOOL_NAMES:
        raise ValueError("Unknown UI probe tool")
    return {"message": "CAPRMEDIO MCP App resource loaded" if name == TOOL_NAMES[0] else "Tool bridge passed"}


async def list_resources(_context: Any, _params: Any) -> types.ListResourcesResult:
    return types.ListResourcesResult(resources=[types.Resource(
        name="CAPRMEDIO UI compatibility probe", uri=URI, mime_type=MIME_TYPE,
    )])


async def read_resource(_context: Any, params: types.ReadResourceRequestParams) -> types.ReadResourceResult:
    if params.uri != URI:
        raise MCPError(-32002, "Unknown UI resource")
    return types.ReadResourceResult(contents=[types.TextResourceContents(
        uri=URI, mime_type=MIME_TYPE,
        text=Path(__file__).with_suffix(".html").read_text(),
    )])
