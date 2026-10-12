"""Canonical ``RESUME_EXECUTION_CONTEXT`` Tool provider and JSON entrypoint."""

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

from capability_discovery.service import Observation, Service  # noqa: E402
from tool_description import binding_matches, make_tool_description  # noqa: E402


MCP_NAME = "resume_execution_context"
TOOL_NAME = "RESUME_EXECUTION_CONTEXT"
ACTION_ID = "CA-O-116"
DELIVERY_ID = "CA-D-516"
ENTRYPOINT = "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/RESUME_EXECUTION_CONTEXT/resume_execution_context.py"


class ResumeExecutionContextResult(RootModel[dict[str, JsonValue]]):
    """Canonical open result produced by execution-context resumption."""


class _DescriptorAdapter:
    """Root-bound invoker that preserves the existing resumption semantics."""

    def __init__(self, root: str | Path) -> None:
        self._service = Service(root)

    def invoke(self, request: Observation) -> dict[str, Any]:
        return self._service.resume(request)


def create_adapter(root: str | Path) -> _DescriptorAdapter:
    """Create the sole root-bound canonical Tool adapter."""

    return _DescriptorAdapter(root)


def describe_tool() -> dict[str, object]:
    """Return descriptor metadata without reading carriers or invoking resumption."""

    return make_tool_description(
        entrypoint=ENTRYPOINT,
        name=TOOL_NAME,
        delivery_atom_id=DELIVERY_ID,
        action_ids=[ACTION_ID],
        input_symbol="Observation",
        output_symbol="ResumeExecutionContextResult",
        title="Resume execution context",
        description="Load remaining saved execution work and source-drift evidence without dispatching it.",
        purpose="Provide effect-free continuation context from retained Run evidence.",
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
    request = Observation.model_validate_json(raw)
    print(json.dumps(create_adapter(args.project_root).invoke(request), default=str))


if __name__ == "__main__":
    _main()


__all__ = [
    "ACTION_ID", "DELIVERY_ID", "ENTRYPOINT", "MCP_NAME", "Observation", "ResumeExecutionContextResult",
    "TOOL_NAME", "binding_is_admitted", "create_adapter", "describe_tool",
]
