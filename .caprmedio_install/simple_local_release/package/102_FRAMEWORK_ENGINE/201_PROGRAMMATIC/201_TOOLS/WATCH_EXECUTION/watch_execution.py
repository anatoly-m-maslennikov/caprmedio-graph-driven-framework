"""Canonical ``WATCH_EXECUTION`` Tool provider and JSON entrypoint."""

from __future__ import annotations

import argparse
import asyncio
import json
from pathlib import Path
import sys
from typing import Any, Mapping

from pydantic import JsonValue, RootModel


TOOLS = Path(__file__).resolve().parents[1]
for path in (TOOLS, TOOLS / "VALIDATE_ATOMS"):
    if str(path) not in sys.path:
        sys.path.insert(0, str(path))

from capability_discovery.service import Service, Watch  # noqa: E402
from tool_description import binding_matches, make_tool_description  # noqa: E402


MCP_NAME = "watch_execution"
TOOL_NAME = "WATCH_EXECUTION"
ACTION_ID = "CA-O-117"
DELIVERY_ID = "CA-D-517"
ENTRYPOINT = "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/WATCH_EXECUTION/watch_execution.py"


class WatchExecutionResult(RootModel[dict[str, JsonValue]]):
    """Canonical open result produced by bounded execution observation."""


class _DescriptorAdapter:
    """Root-bound asynchronous invoker for the existing bounded watcher."""

    def __init__(self, root: str | Path) -> None:
        self._service = Service(root)

    async def invoke(self, request: Watch) -> dict[str, Any]:
        return await self._service.watch(request)


def create_adapter(root: str | Path) -> _DescriptorAdapter:
    """Create the sole root-bound canonical Tool adapter."""

    return _DescriptorAdapter(root)


def describe_tool() -> dict[str, object]:
    """Return descriptor metadata without reading carriers or starting a watch."""

    return make_tool_description(
        entrypoint=ENTRYPOINT,
        name=TOOL_NAME,
        delivery_atom_id=DELIVERY_ID,
        action_ids=[ACTION_ID],
        input_symbol="Watch",
        output_symbol="WatchExecutionResult",
        title="Watch execution",
        description="Observe confirmed execution changes with cursor replay and a bounded asynchronous wait.",
        purpose="Provide effect-free, bounded observation of retained Run and Journal evidence.",
        read_only=True,
        idempotent=True,
    )


def binding_is_admitted(binding: Mapping[str, object] | None) -> bool:
    """Require the current catalog binding to match this exact provider."""

    return binding_matches(
        binding,
        entrypoint=ENTRYPOINT,
        name=TOOL_NAME,
        delivery_atom_id=DELIVERY_ID,
        action_ids=[ACTION_ID],
    )


def _main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project-root", required=True)
    parser.add_argument("--input", default="-")
    args = parser.parse_args()
    raw = sys.stdin.read() if args.input == "-" else Path(args.input).read_text()
    request = Watch.model_validate_json(raw)
    print(json.dumps(asyncio.run(create_adapter(args.project_root).invoke(request)), default=str))


if __name__ == "__main__":
    _main()


__all__ = [
    "ACTION_ID", "DELIVERY_ID", "ENTRYPOINT", "MCP_NAME", "TOOL_NAME", "Watch", "WatchExecutionResult",
    "binding_is_admitted", "create_adapter", "describe_tool",
]
