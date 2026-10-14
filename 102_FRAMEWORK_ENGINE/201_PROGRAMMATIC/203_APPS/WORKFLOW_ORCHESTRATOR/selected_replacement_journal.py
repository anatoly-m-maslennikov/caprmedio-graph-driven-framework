"""Append an observed replacement after reading back its source carrier."""

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


class ReplacementJournalError(RuntimeError):
    """The observed source carrier does not match the supplied result."""


def _read_verified_result(root: Path, result: Mapping[str, Any]) -> None:
    path = result.get("path")
    digest = result.get("sha256")
    if not isinstance(path, str) or not isinstance(digest, str):
        raise ReplacementJournalError("replacement result must identify a path and sha256")
    relative = Path(path)
    if relative.is_absolute() or ".." in relative.parts or not relative.parts:
        raise ReplacementJournalError("replacement readback path is unsafe")

    canonical_root = root.resolve()
    candidate = root / relative
    current = root
    for component in relative.parts:
        current = current / component
        if current.is_symlink():
            raise ReplacementJournalError("replacement readback path is unsafe")
    try:
        resolved = candidate.resolve(strict=True)
        resolved.relative_to(canonical_root)
    except (OSError, RuntimeError, ValueError) as error:
        raise ReplacementJournalError("replacement readback path is unsafe") from error
    if not resolved.is_file() or resolved.is_symlink():
        raise ReplacementJournalError("replacement readback path is unsafe")
    if hashlib.sha256(resolved.read_bytes()).hexdigest() != digest:
        raise ReplacementJournalError("replacement readback differs from supplied result")


def record_selected_replacement(
    root: Path,
    *,
    canonical_event: Mapping[str, Any],
    author: object,
    local_date: object,
    timezone: object,
    append_context: Mapping[str, Any] | None = None,
) -> Mapping[str, Any]:
    """Append one already-authorized, observed replacement event."""
    result = canonical_event.get("result")
    if not isinstance(result, Mapping):
        raise ReplacementJournalError("replacement event has no source result")
    project_root = Path(root)
    _read_verified_result(project_root, result)
    locations = append_sealed_events(
        project_root,
        [canonical_event],
        author=author,
        local_date=local_date,
        timezone=timezone,
        append_context=append_context,
    )
    return {"state": "completed", "event": canonical_event, "locations": locations}
