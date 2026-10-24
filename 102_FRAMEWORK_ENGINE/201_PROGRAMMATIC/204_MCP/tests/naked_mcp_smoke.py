"""Run a real in-memory MCP protocol smoke against a disposable Project.

Usage:
    UV_PROJECT_ENVIRONMENT="$PWD/.caprmedio_runtime/launcher-venv" \
    TMPDIR="$PWD/.caprmedio_tmp" \
    uv run --project . --locked --no-sync --managed-python --python 3.14 \
    --no-env-file --all-groups python -B \
    102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/204_MCP/tests/naked_mcp_smoke.py \
    --project-root "$PWD/.caprmedio_tmp/naked-mcp-project"
"""

# implementation of:
# Method: CA-M-175, CA-M-177, CA-M-178, CA-M-179, CA-M-181

from __future__ import annotations

import argparse
import asyncio
import json
from pathlib import Path
import sys
import tempfile
from typing import Any

from interactive_mcp_fixture import build_interactive_mcp_fixture
from mcp import StdioServerParameters
from mcp.client._memory import InMemoryTransport
from mcp.client.session import ClientSession
from mcp.client.stdio import stdio_client
from implementation_server import create_server


# implementation of:
# Method: CA-M-177
def _disposable_project(value: Path) -> Path:
    root = value.expanduser().resolve()
    temporary_root = (Path.cwd() / ".caprmedio_tmp").resolve()
    if root == temporary_root or not root.is_relative_to(temporary_root):
        raise ValueError("--project-root must be a new child of .caprmedio_tmp")
    if root.exists():
        raise ValueError(f"--project-root already exists: {root}")
    return root


# implementation of:
# Method: CA-M-178, CA-M-179
async def _call_preview(client: ClientSession, fixture: Any) -> tuple[set[str], dict[str, Any]]:
    await client.initialize()
    tools = await client.list_tools()
    names = {tool.name for tool in tools.tools}
    if "run_implementation_workflow" not in names:
        raise AssertionError("current MCP route was not advertised")
    response = await client.call_tool(
        "run_implementation_workflow", {"request": fixture.execution_request}
    )
    if response.is_error or not isinstance(response.structured_content, dict):
        raise AssertionError("current MCP preview returned a protocol or result error")
    result = response.structured_content
    receipt = result.get("proposal_receipt")
    if (
        result.get("disposition") != "preview"
        or not isinstance(receipt, dict)
        or receipt.get("operation_route") != "run_implementation_workflow"
    ):
        raise AssertionError("current MCP preview result has no valid proposal receipt")
    return names, result


# implementation of:
# Method: CA-M-181
def _result(
    fixture: Any, names: set[str], result: dict[str, Any], transport: str
) -> dict[str, Any]:
    return {
        "project_root": str(fixture.root),
        "tool_count": len(names),
        "route": "run_implementation_workflow",
        "disposition": result["disposition"],
        "proposal_receipt": True,
        "transport": transport,
    }


# implementation of:
# Method: CA-M-175
async def run_smoke(project_root: Path) -> dict[str, Any]:
    disposable_root = _disposable_project(project_root)
    fixture = build_interactive_mcp_fixture(disposable_root.parent, name=disposable_root.name)
    server = create_server(fixture.root)  # type: ignore[no-untyped-call]
    async with InMemoryTransport(server, raise_exceptions=True) as streams:
        async with ClientSession(*streams) as client:
            names, result = await _call_preview(client, fixture)
    return _result(fixture, names, result, "in-memory")


# implementation of:
# Method: CA-M-175
async def run_stdio_smoke(project_root: Path) -> dict[str, Any]:
    disposable_root = _disposable_project(project_root)
    fixture = build_interactive_mcp_fixture(disposable_root.parent, name=disposable_root.name)
    parameters = StdioServerParameters(
        command=sys.executable,
        args=[
            "-B",
            str(Path(__file__).resolve().parents[1] / "server.py"),
            "--project-root",
            str(fixture.root),
            "--transport",
            "stdio",
        ],
        cwd=Path.cwd(),
    )
    with tempfile.TemporaryFile(mode="w+", encoding="utf-8") as stderr:
        try:
            async with stdio_client(parameters, errlog=stderr) as streams:
                async with ClientSession(*streams, read_timeout_seconds=120) as client:
                    names, result = await _call_preview(client, fixture)
        except BaseException as error:
            stderr.seek(0)
            detail = stderr.read()[-4096:]
            if detail:
                raise AssertionError(
                    f"MCP stdio smoke failed; stderr follows:\n{detail}"
                ) from error
            raise
    return _result(fixture, names, result, "stdio")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project-root", required=True, type=Path)
    parser.add_argument("--transport", choices=("in-memory", "stdio"), default="in-memory")
    args = parser.parse_args(argv)
    try:
        smoke = run_stdio_smoke if args.transport == "stdio" else run_smoke
        result = asyncio.run(smoke(args.project_root))
    except (AssertionError, OSError, ValueError) as error:
        parser.error(str(error))
    print(json.dumps(result, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
