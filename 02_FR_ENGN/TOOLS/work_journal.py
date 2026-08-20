#!/usr/bin/env python3
"""Append one governed event to the project Work Journal.

Parameters:
    --event: started, progressed, completed, failed, interrupted, abandoned, or recovered.
    --action-id: stable identifier shared by every event for one action.
    --kind: bounded action category.
    --scope: structural scope performing the action.
    --operation: governed operation name.
    --session-id: LLM or operator session provenance.
    --subject: governed input; repeat when needed.
    --output: produced output; repeat when needed.
    --preceding-event: preceding event identifier when one exists.
    --detail: additional key=value fact; repeat when needed.
    --apply: append the event; omission is dry-run mode.

The tool emits one compact NDJSON record, creates the journal directory only
when the first record is accepted, and fsyncs every append.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import tomllib
import uuid
from pathlib import Path


sys.pycache_prefix = str(
    Path(__file__).resolve().parents[2] / ".caprmedio_runtime/cache/python"
)
TOOLS_ROOT = Path(__file__).resolve().parent
if str(TOOLS_ROOT) not in sys.path:
    sys.path.insert(0, str(TOOLS_ROOT))

from artifact_metadata import current_timestamp, repository_root  # noqa: E402


SETTINGS_PATH = Path(".caprmedio/caprmedio_project_settings.toml")
EVENTS = (
    "started",
    "progressed",
    "completed",
    "failed",
    "interrupted",
    "abandoned",
    "recovered",
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--event", choices=EVENTS, required=True)
    parser.add_argument("--action-id", required=True)
    parser.add_argument("--kind", required=True)
    parser.add_argument("--scope", required=True)
    parser.add_argument("--operation", required=True)
    parser.add_argument("--session-id", required=True)
    parser.add_argument("--subject", action="append", default=[])
    parser.add_argument("--output", action="append", default=[])
    parser.add_argument("--preceding-event")
    parser.add_argument("--detail", action="append", default=[])
    parser.add_argument("--apply", action="store_true")
    parser.add_argument("root", nargs="?", default=".")
    return parser.parse_args()


def parse_details(values: list[str]) -> dict[str, str]:
    details: dict[str, str] = {}
    for value in values:
        key, separator, item = value.partition("=")
        if not separator or not key or key in details:
            raise RuntimeError(f"invalid or duplicate detail: {value!r}")
        details[key] = item
    return details


def event_record(
    *,
    root: Path,
    event: str,
    action_id: str,
    kind: str,
    scope: str,
    operation: str,
    session_id: str,
    subjects: list[str],
    outputs: list[str],
    preceding_event: str | None,
    details: dict[str, str],
    occurred_at: str | None = None,
) -> dict[str, object]:
    record: dict[str, object] = {
        "schema_version": 1,
        "event_id": str(uuid.uuid4()),
        "action_id": action_id,
        "event": event,
        "kind": kind,
        "occurred_at": occurred_at or current_timestamp(root),
        "session_id": session_id,
        "structural_scope": scope,
        "operation": operation,
        "governed_subjects": subjects,
        "produced_outputs": outputs,
    }
    if preceding_event:
        record["preceding_event"] = preceding_event
    if details:
        record["details"] = details
    return record


def configured_journal_root(root: Path) -> Path:
    settings = tomllib.loads((root / SETTINGS_PATH).read_text(encoding="utf-8"))
    value = settings.get("paths", {}).get("journal_root")
    if not isinstance(value, str) or not value:
        raise RuntimeError("Project Settings requires paths.journal_root")
    path = Path(value)
    if path.is_absolute() or ".." in path.parts or path.parts[:1] != (".caprmedio",):
        raise RuntimeError("paths.journal_root must be a safe .caprmedio-relative path")
    return path


def segment_path(root: Path, occurred_at: str) -> Path:
    return root / configured_journal_root(root) / f"src-work-journal-{occurred_at[:10]}.ndjson"


def append_record(root: Path, record: dict[str, object]) -> Path:
    path = segment_path(root, str(record["occurred_at"]))
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = json.dumps(record, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n"
    descriptor = os.open(path, os.O_APPEND | os.O_CREAT | os.O_WRONLY, 0o644)
    try:
        os.write(descriptor, payload.encode("utf-8"))
        os.fsync(descriptor)
    finally:
        os.close(descriptor)
    return path


def main() -> int:
    args = parse_args()
    root = repository_root(Path(args.root))
    record = event_record(
        root=root,
        event=args.event,
        action_id=args.action_id,
        kind=args.kind,
        scope=args.scope,
        operation=args.operation,
        session_id=args.session_id,
        subjects=args.subject,
        outputs=args.output,
        preceding_event=args.preceding_event,
        details=parse_details(args.detail),
    )
    print(json.dumps(record, ensure_ascii=False, sort_keys=True))
    if args.apply:
        path = append_record(root, record)
        print(f"journal={path.relative_to(root)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
