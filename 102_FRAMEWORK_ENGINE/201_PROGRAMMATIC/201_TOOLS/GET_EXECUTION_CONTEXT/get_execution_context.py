"""Canonical ``GET_EXECUTION_CONTEXT`` Tool provider and JSON entrypoint."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys
from typing import Any, Mapping

from pydantic import JsonValue, RootModel


TOOLS = Path(__file__).resolve().parents[1]
for path in (TOOLS, TOOLS / "VALIDATE_ATOMS"):
    if str(path) not in sys.path:
        sys.path.insert(0, str(path))

from capability_discovery.service import Context, Service  # noqa: E402
from tool_description import binding_matches, make_tool_description  # noqa: E402


MCP_NAME = "get_execution_context"
TOOL_NAME = "GET_EXECUTION_CONTEXT"
ACTION_ID = "CA-O-114"
DELIVERY_ID = "CA-D-514"
ENTRYPOINT = "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/GET_EXECUTION_CONTEXT/get_execution_context.py"


class GetExecutionContextResult(RootModel[dict[str, JsonValue]]):
    """Canonical open result produced by execution-context retrieval."""


class _DescriptorAdapter:
    """Root-bound invoker that preserves the existing context semantics."""

    def __init__(self, root: str | Path) -> None:
        self._service = Service(root)

    def invoke(self, request: Context) -> dict[str, Any]:
        return self._service.context(request)


def create_adapter(root: str | Path) -> _DescriptorAdapter:
    """Create the sole root-bound canonical Tool adapter."""

    return _DescriptorAdapter(root)


def describe_tool() -> dict[str, object]:
    """Return descriptor metadata without reading carriers or invoking context lookup."""

    return make_tool_description(
        entrypoint=ENTRYPOINT,
        name=TOOL_NAME,
        delivery_atom_id=DELIVERY_ID,
        action_ids=[ACTION_ID],
        input_symbol="Context",
        output_symbol="GetExecutionContextResult",
        title="Get execution context",
        description="Load one selected execution definition and its directly relevant context without dispatching it.",
        purpose="Provide effect-free execution context needed to inspect a declared capability.",
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
    request = Context.model_validate_json(raw)
    print(json.dumps(create_adapter(args.project_root).invoke(request), default=str))


if __name__ == "__main__":
    _main()


__all__ = [
    "ACTION_ID", "Context", "DELIVERY_ID", "ENTRYPOINT", "GetExecutionContextResult", "MCP_NAME",
    "TOOL_NAME", "binding_is_admitted", "create_adapter", "describe_tool",
]
