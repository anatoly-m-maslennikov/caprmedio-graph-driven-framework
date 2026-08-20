#!/usr/bin/env python3
"""Inspect one COMMIT_TRIGGER and return sealed read-only commit context."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


SCRIPT_ROOT = Path(__file__).resolve().parents[3]
sys.pycache_prefix = str(SCRIPT_ROOT / ".caprmedio_runtime" / "cache" / "python")
if str(Path(__file__).resolve().parent) not in sys.path:
    sys.path.insert(0, str(Path(__file__).resolve().parent))

from commit_context_logic import CONTEXT_SCHEMA_VERSION, ContextError, gather_context, repository_root  # noqa: E402


CAPABILITY = "COMMIT_CONTEXT"
TOOL_KIND = "finder"


INPUT_SCHEMA: dict[str, Any] = {
    "schema_version": 1,
    "type": "COMMIT_TRIGGER",
    "required": [
        "schema_version",
        "trigger_id",
        "adapter.id",
        "source_event_id",
        "repository.root",
        "repository.identity",
        "observed_at",
        "before_path|after_path",
        "llm_session.app",
        "llm_session.uuid",
    ],
}


def parser() -> argparse.ArgumentParser:
    result = argparse.ArgumentParser(description=__doc__)
    result.add_argument("--repository", type=Path, default=Path("."), help="CAPRMEDIO repository root")
    result.add_argument("--input", metavar="JSON_OR_DASH", help="COMMIT_TRIGGER JSON object or - for stdin")
    result.add_argument("--schema", action="store_true", help="print the input schema and exit")
    result.add_argument("--describe", action="store_true", help="print Tool capability metadata and exit")
    result.add_argument("--pretty", action="store_true", help="pretty-print the machine result envelope")
    return result


def read_json(value: str) -> dict[str, Any]:
    raw = sys.stdin.read() if value == "-" else value
    try:
        parsed = json.loads(raw)
    except json.JSONDecodeError as error:
        raise ContextError("input_json_invalid", "--input must contain one JSON object", line=error.lineno, column=error.colno) from error
    if not isinstance(parsed, dict):
        raise ContextError("input_json_invalid", "--input must contain one JSON object")
    return parsed


def envelope(*, ok: bool, diagnostics: list[dict[str, Any]], result: dict[str, Any] | None = None) -> dict[str, Any]:
    value: dict[str, Any] = {
        "schema_version": 1,
        "tool": {"capability_id": CAPABILITY, "kind": TOOL_KIND},
        "ok": ok,
        "mode": "read-only",
        "diagnostics": diagnostics,
    }
    if result is not None:
        value["result"] = result
    return value


def emit(value: dict[str, Any], *, pretty: bool) -> None:
    print(json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2 if pretty else None, separators=None if pretty else (",", ":")))


def main(argv: list[str] | None = None) -> int:
    args = parser().parse_args(argv)
    if args.schema:
        emit(envelope(ok=True, diagnostics=[], result={"input_schema": INPUT_SCHEMA, "context_schema_version": CONTEXT_SCHEMA_VERSION}), pretty=args.pretty)
        return 0
    if args.describe:
        emit(
            envelope(
                ok=True,
                diagnostics=[],
                result={
                    "capability_id": CAPABILITY,
                    "kind": TOOL_KIND,
                    "read_only": True,
                    "input_schema": INPUT_SCHEMA,
                    "result_schema_version": CONTEXT_SCHEMA_VERSION,
                },
            ),
            pretty=args.pretty,
        )
        return 0
    if args.input is None:
        parser().error("--input is required unless --schema or --describe is selected")
    try:
        context = gather_context(repository_root(args.repository), read_json(args.input))
    except ContextError as error:
        emit(envelope(ok=False, diagnostics=[error.diagnostic()]), pretty=args.pretty)
        return 2
    emit(envelope(ok=True, diagnostics=[], result={"context": context}), pretty=args.pretty)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
