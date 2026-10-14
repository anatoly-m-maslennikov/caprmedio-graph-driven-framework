#!/usr/bin/env python3
"""Append supplied Journal rows; default dry run writes nothing."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys
from typing import Any, Mapping

from pydantic import BaseModel, ConfigDict, JsonValue, RootModel

SCRIPT_PATH = Path(__file__).resolve()
TOOLS_ROOT = SCRIPT_PATH.parents[1]
for parent in SCRIPT_PATH.parents:
    if parent.name in {".caprmedio_runtime", ".caprmedio_install", ".caprmedio"}:
        sys.pycache_prefix = str(parent.parent / ".caprmedio_tmp/cache/python")
        break
for directory in (TOOLS_ROOT, SCRIPT_PATH.parent):
    if str(directory) not in sys.path:
        sys.path.insert(0, str(directory))

from tool_description import binding_matches, make_tool_description  # noqa: E402
from work_journal import append_sealed_events  # noqa: E402
from append_change_records_mcp import AppendChangeRecordsAdapter  # noqa: E402

TOOL_ID = "APPEND_CHANGE_RECORDS"
TOOL_KIND = "doer"
TOOL_SCHEMA_VERSION = 1
MCP_ENTRYPOINT = (
    "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/APPEND_CHANGE_RECORDS/append_change_records.py"
)
_MCP_NATIVE_MODULE = sys.modules[__name__]


class _AppendChangeRecordsRequestBody(BaseModel):
    model_config = ConfigDict(extra="forbid", strict=True)
    context: dict[str, JsonValue]
    apply: bool = False


class AppendChangeRecordsRequest(RootModel[_AppendChangeRecordsRequestBody]):
    """Existing context transport; its Journal rows are not validated."""


class AppendChangeRecordsResult(RootModel[dict[str, JsonValue]]):
    """Append locations are observations, not validation receipts."""


def create_adapter(root: str | Path) -> AppendChangeRecordsAdapter:
    return AppendChangeRecordsAdapter(Path(root).resolve(), _MCP_NATIVE_MODULE)


def describe_tool() -> dict[str, Any]:
    return make_tool_description(
        entrypoint=MCP_ENTRYPOINT,
        name=TOOL_ID,
        delivery_atom_id="CA-D-009",
        action_ids=["CA-O-222"],
        input_symbol="AppendChangeRecordsRequest",
        output_symbol="AppendChangeRecordsResult",
        title="Append Change Records",
        description="Append supplied records to the Project Journal.",
        purpose="Write supplied rows without validation, deduplication or retries.",
        read_only=False,
        idempotent=False,
    )


def binding_is_admitted(binding: Mapping[str, object] | None) -> bool:
    return binding_matches(
        binding,
        entrypoint=MCP_ENTRYPOINT,
        name=TOOL_ID,
        delivery_atom_id="CA-D-009",
        action_ids=["CA-O-222"],
    )


def _json_result(*, ok: bool, mode: str, **values: Any) -> dict[str, Any]:
    return {
        "schema_version": TOOL_SCHEMA_VERSION,
        "tool": {"capability_id": TOOL_ID, "kind": TOOL_KIND},
        "ok": ok,
        "mode": mode,
        **values,
    }


def run(root: Path, payload: Mapping[str, Any], *, apply: bool) -> dict[str, Any]:
    if "context" in payload:
        context = payload["context"]
    elif isinstance(payload.get("result"), Mapping) and "context" in payload["result"]:
        context = payload["result"]["context"]
    else:
        context = payload
    events = context["predictions"]["journal_records"]
    receipts = (
        append_sealed_events(
            root,
            events,
            author=context["author"],
            local_date=context["local_date"],
            timezone=context["timezone"],
        )
        if apply
        else []
    )
    return _json_result(
        ok=True,
        mode="apply" if apply else "dry-run",
        diagnostics=[],
        result={
            "resolved_targets": {"repository": str(root)},
            "planned_effects": {"journal_records": events},
            "receipts": receipts,
            "state": "complete" if apply else "dry-run",
        },
    )


def describe() -> dict[str, Any]:
    return _json_result(
        ok=True,
        mode="read-only",
        diagnostics=[],
        result={
            "capability": {
                "capability_id": TOOL_ID,
                "kind": TOOL_KIND,
                "summary": "Append supplied Journal rows.",
            },
            "input_schema": {
                "command": "--repository REPOSITORY run --input CONTEXT.json [--apply]",
                "context": "author, local_date, timezone, predictions.journal_records",
            },
            "result_schema": {"journal_records": "supplied rows", "receipts": "append locations"},
        },
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repository", type=Path, default=Path("."))
    parser.add_argument("--root", dest="repository", type=Path, help=argparse.SUPPRESS)
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("describe")
    command = commands.add_parser("run")
    command.add_argument("--input", required=True, help="JSON path or - for stdin")
    command.add_argument("--apply", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        if args.command == "describe":
            result = describe()
        else:
            text = (
                sys.stdin.read()
                if args.input == "-"
                else Path(args.input).read_text(encoding="utf-8")
            )
            result = run(args.repository.resolve(), json.loads(text), apply=args.apply)
    except (OSError, ValueError, KeyError, TypeError, RuntimeError) as error:
        # An append failure may follow a partial write; do not inspect or retry.
        result = _json_result(
            ok=False,
            mode="apply" if getattr(args, "apply", False) else "dry-run",
            diagnostics=[{"code": "append-failed", "message": str(error)}],
        )
    print(json.dumps(result, ensure_ascii=False))
    return 0 if result["ok"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
