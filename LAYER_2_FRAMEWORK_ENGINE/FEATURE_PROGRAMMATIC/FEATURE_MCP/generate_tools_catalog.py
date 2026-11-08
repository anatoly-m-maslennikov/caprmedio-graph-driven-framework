# CA-R-2785@4
# CA-D-678@5

"""Generate the released MCP discovery catalog after server readiness."""

from __future__ import annotations

import argparse
import asyncio
from pathlib import Path
import sys
from typing import Any

from mcp import types
from mcp.client.session import ClientSession
from mcp.client.streamable_http import streamable_http_client


TOOLS_ROOT = Path(__file__).resolve().parents[1] / "FEATURE_TOOLS"
if str(TOOLS_ROOT) not in sys.path:
    sys.path.insert(0, str(TOOLS_ROOT))

from capability_discovery.tool_catalog import build_catalog, write_catalog  # noqa: E402


async def _list_tools(mcp_url: str, http_client: Any = None) -> list[object]:
    """Read every public tool descriptor without invoking a Tool."""

    tools: list[object] = []
    async with streamable_http_client(mcp_url, http_client=http_client) as streams:
        async with ClientSession(*streams) as session:
            await session.initialize()
            page = await session.list_tools()
            while True:
                tools.extend(page.tools)
                if page.next_cursor is None:
                    return tools
                page = await session.list_tools(
                    params=types.PaginatedRequestParams(cursor=page.next_cursor),
                )


async def generate_catalog(
    project_root: str | Path,
    mcp_url: str,
    http_client: Any = None,
) -> dict[str, Any]:
    """Fetch the public MCP tool frontier and atomically publish its catalog."""

    catalog = build_catalog(await _list_tools(mcp_url, http_client=http_client))
    path = write_catalog(project_root, catalog)
    return {
        "path": str(path),
        "tool_count": len(catalog["root"]) + sum(len(items) for items in catalog["groups"].values()),
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project-root", required=True, type=Path)
    parser.add_argument("--mcp-url", required=True)
    args = parser.parse_args(argv)
    try:
        result = asyncio.run(generate_catalog(args.project_root, args.mcp_url))
    except Exception as error:
        print(f"tools catalog generation failed: {error}", file=sys.stderr)
        return 1
    print(f"generated tools catalog: {result['path']} ({result['tool_count']} tools)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
