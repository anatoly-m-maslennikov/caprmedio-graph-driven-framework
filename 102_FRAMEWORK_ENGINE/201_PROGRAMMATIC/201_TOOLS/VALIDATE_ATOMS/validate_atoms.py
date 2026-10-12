#!/usr/bin/env python3
"""Validate selected Atom carriers without changing inputs."""

import json
from collections.abc import Mapping
from pathlib import Path
import sys
from typing import Any

sys.dont_write_bytecode = True

PROVIDER_ROOT = Path(__file__).resolve().parent
TOOLS_ROOT = PROVIDER_ROOT.parent
for _path in (TOOLS_ROOT, PROVIDER_ROOT):
    if str(_path) not in sys.path:
        sys.path.insert(0, str(_path))

from tool_description import binding_matches, make_tool_description  # noqa: E402
from validate_atoms_workers.contracts import parse_request, request_error_report, validate_report  # noqa: E402
from validate_atoms_workers.read_io import protected, open_regular  # noqa: E402
from validate_atoms_workers.request_models import Request as CheckerRequest  # noqa: E402
from validate_atoms_workers.result_models import Report as CheckerReport  # noqa: E402
from validate_atoms_workers.runtime import execute  # noqa: E402


TOOL_NAME = "VALIDATE_ATOMS"
DELIVERY_ID = "CA-D-519"
ACTION_ID = "CA-O-087"
ENTRYPOINT = "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/VALIDATE_ATOMS/validate_atoms.py"


class _DescriptorAdapter:
    """Root-bound transport-neutral adapter over the existing CA-O-087 checker."""

    def __init__(self, root: str | Path) -> None:
        self.root = Path(root)

    def invoke(self, request: CheckerRequest) -> CheckerReport:
        """Validate canonical input, invoke the checker, and return its canonical Report."""

        accepted = CheckerRequest.model_validate(request)
        report = execute(accepted.model_dump(mode="json", exclude_unset=True))
        return CheckerReport.model_validate(report)


def create_adapter(root: str | Path) -> _DescriptorAdapter:
    """Create the canonical CA-O-087 invoker without invoking the Tool."""

    return _DescriptorAdapter(root)


def describe_tool() -> dict[str, Any]:
    """Describe VALIDATE_ATOMS without reading carriers or running validation."""

    return make_tool_description(
        entrypoint=ENTRYPOINT,
        name=TOOL_NAME,
        delivery_atom_id=DELIVERY_ID,
        action_ids=[ACTION_ID],
        input_symbol="CheckerRequest",
        output_symbol="CheckerReport",
        title="Validate Atoms",
        description="Check selected Atom carriers against admitted authority without changing inputs.",
        purpose="Return structured CA-O-087 conformance findings through the existing read-only checker.",
        read_only=True,
        idempotent=True,
    )


def binding_is_admitted(binding: Mapping[str, object] | None) -> bool:
    """Accept only D519's current source-only discovery declaration.

    D519 deliberately has no public MCP name.  Transport registration decides
    separately whether a source declaration is eligible for a public route.
    """

    return (
        isinstance(binding, Mapping)
        and binding.get("mcp_name") == ""
        and binding_matches(
            binding,
            entrypoint=ENTRYPOINT,
            name=TOOL_NAME,
            delivery_atom_id=DELIVERY_ID,
            action_ids=[ACTION_ID],
        )
    )


def main() -> int:
    try:
        if len(sys.argv) != 3 or sys.argv[1] != "--input":
            raise ValueError("Expected --input path or --input -")
        if sys.argv[2] == "-":
            raw = sys.stdin.buffer.read(8 * 1024 * 1024 + 1)
        else:
            path = Path(sys.argv[2]).absolute()
            if protected(path):
                raise ValueError("Protected input.")
            import os

            with os.fdopen(open_regular(path), "rb") as stream:
                raw = stream.read(8 * 1024 * 1024 + 1)
        if len(raw) > 8 * 1024 * 1024:
            raise ValueError("Request exceeds host input ceiling.")
        request = parse_request(raw.decode("utf-8"))
    except OSError, ValueError, UnicodeError, RecursionError:
        report = request_error_report()
    else:
        report = execute(request.model_dump(mode="json", exclude_unset=True))
    report = validate_report(report)
    print(json.dumps(report, ensure_ascii=False, sort_keys=True, indent=2))
    return {"valid": 0, "invalid": 1, "incomplete": 2, "error": 3}[report["result"]]


if __name__ == "__main__":
    raise SystemExit(main())
