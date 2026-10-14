"""Append observed lifecycle changes without a Journal-history prerequisite."""

from __future__ import annotations

import hashlib
from collections.abc import Mapping
from pathlib import Path
import sys
from typing import Any

TOOLS = Path(__file__).resolve().parents[2] / "201_TOOLS"
if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))

from work_journal import append_sealed_events  # noqa: E402


class LifecycleJournalError(RuntimeError):
    """Observed source effects do not match the supplied carrier facts."""


def _result(facts: Mapping[str, Any], current_bytes: bytes) -> dict[str, Any]:
    value = dict(facts)
    if set(value) != {"filename", "version", "path", "sha256"}:
        raise LifecycleJournalError(
            "carrier facts must be exactly filename, version, path, and sha256"
        )
    path = Path(value["path"]) if isinstance(value["path"], str) else None
    if (
        not isinstance(value["filename"], str)
        or not value["filename"]
        or type(value["version"]) is not int
        or value["version"] < 1
        or path is None
        or path.is_absolute()
        or ".." in path.parts
        or not isinstance(value["sha256"], str)
        or len(value["sha256"]) != 64
        or not isinstance(current_bytes, bytes)
        or hashlib.sha256(current_bytes).hexdigest() != value["sha256"]
    ):
        raise LifecycleJournalError("carrier facts do not bind the observed bytes")
    return {"state": "present", **value}


def _readback(root: Path, result: Mapping[str, Any]) -> None:
    relative = Path(result["path"])
    candidate = root / relative
    current = root
    for component in relative.parts:
        current = current / component
        if current.is_symlink():
            raise LifecycleJournalError("carrier readback path is unsafe")
    try:
        resolved = candidate.resolve(strict=True)
        resolved.relative_to(root.resolve())
    except (OSError, RuntimeError, ValueError) as error:
        raise LifecycleJournalError("carrier readback path is unsafe") from error
    if (
        not resolved.is_file()
        or hashlib.sha256(resolved.read_bytes()).hexdigest() != result["sha256"]
    ):
        raise LifecycleJournalError("carrier readback differs from observed source result")


def prepare_lifecycle_journal(
    root: Path,
    before_facts: Mapping[str, Any],
    current_bytes: bytes,
    action_pin: Mapping[str, Any],
    run_id: str,
    context: Mapping[str, Any],
) -> Mapping[str, Any]:
    """Keep the native before observation; do not read or append Journal history."""
    return {"state": "observed", "result": _result(before_facts, current_bytes)}


def admit_lifecycle_prior(
    root: Path, prepared: Mapping[str, Any], context: Mapping[str, Any]
) -> Mapping[str, Any]:
    """Read back the source before effects, independently of Journal contents."""
    result = prepared["result"]
    _readback(Path(root), result)
    return {"state": "admitted", "before_result": result}


def record_lifecycle_change(
    root: Path,
    *,
    prior: Mapping[str, Any] | None = None,
    after_facts: Mapping[str, Any],
    current_bytes: bytes,
    action_pin: Mapping[str, Any],
    run_id: str,
    context: Mapping[str, Any],
    action_type: str,
    native_effects: Mapping[str, Any],
    before_result: Mapping[str, Any] | None = None,
) -> Mapping[str, Any]:
    """Append the actual change; previous records do not admit or reject it."""
    after = _result(after_facts, current_bytes)
    before = before_result or (prior.get("result") if isinstance(prior, Mapping) else None)
    if before is not None and all(
        before.get(key) == after.get(key) for key in ("path", "version", "sha256")
    ):
        return {"state": "no_op"}
    if action_type not in {"UPDATE", "MOVE", "MOVE+UPDATE"}:
        raise LifecycleJournalError("lifecycle change action type is invalid")
    if not isinstance(native_effects, Mapping) or native_effects.get("result") != after:
        raise LifecycleJournalError("native lifecycle effects do not match observed after state")
    _readback(Path(root), after)
    event = {
        "schema_version": 3,
        "event_id": f"lifecycle-change:{run_id}",
        "event": "completed",
        "kind": "governed_project_change",
        "subject_kind": "file",
        "author": context["author"],
        **dict(action_pin),
        "action_type": action_type,
        "sources": [],
        "result": after,
    }
    locations = append_sealed_events(
        Path(root),
        [event],
        author=context["author"],
        local_date=context["local_date"],
        timezone=context["timezone"],
        append_context=context,
    )
    return {"state": "admitted", "event": event, "locations": locations}
