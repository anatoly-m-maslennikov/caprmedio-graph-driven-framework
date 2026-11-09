"""Shared, non-executable Work Journal persistence library.

Rows are caller data. Tool CLI entry points live in their respective units;
the shared source-request helpers retain their separate runtime authority.
"""

from __future__ import annotations

import datetime as dt
import json
import os
import re
import sys
import tomllib
import uuid
from concurrent.futures import CancelledError as FutureCancelledError
from pathlib import Path
from typing import Any, Mapping, Sequence
from urllib.parse import quote
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError

from VALIDATE_ATOMS.validate_atoms_workers.read_io import ReadContext, open_regular, protected
from VALIDATE_ATOMS.validate_atoms_workers.settings import CEILINGS


MODULE_PATH = Path(__file__).resolve()
for _parent in MODULE_PATH.parents:
    if _parent.name == ".caprmedio_runtime":
        sys.pycache_prefix = str(_parent.parent / ".caprmedio_tmp" / "cache" / "python")
        break
    if _parent.name == ".caprmedio_install":
        sys.pycache_prefix = str(_parent.parent / ".caprmedio_tmp" / "cache" / "python")
        break
    if _parent.name == ".caprmedio":
        sys.pycache_prefix = str(_parent.parent / ".caprmedio_tmp" / "cache" / "python")
        break


SETTINGS_PATH = Path(".caprmedio_caprmedio/caprmedio_project_settings.toml")
MAX_EVENTS_PER_PART = 1000
AUTHOR_RE = re.compile(r"^[A-Za-z0-9](?:[A-Za-z0-9-]{0,37}[A-Za-z0-9])?$")


def _settings_control_relative(value: str | Path) -> Path:
    path = Path(value)
    if (path.is_absolute() or len(path.parts) != 1 or path.name == ".caprmedio_"
            or not path.name.startswith(".caprmedio_") or str(value) != path.as_posix()
            or protected(path)):
        raise RuntimeError("paths.control_root must name one normalized direct Project child")
    return path


def _read_project_settings(root: Path, control_root: str | Path | None = None) -> tuple[Path, dict[str, Any]]:
    """Read one Project-local settings carrier without repository fallback."""
    try:
        # Canonicalize the supplied boundary (including macOS's /var spelling),
        # then use non-following I/O for every Project-local path component.
        supplied = Path(root).expanduser()
        if ".." in supplied.parts or protected(supplied) or supplied.is_symlink():
            raise RuntimeError("Project root must not be unsafe or a symlink")
        project = supplied.resolve(strict=True)
        if protected(project):
            raise RuntimeError("Project root is protected")
        descriptor = open_regular(project, directory=True)
        try:
            if control_root is None:
                candidates = []
                with os.scandir(descriptor) as entries:
                    for entry in entries:
                        if not entry.name.startswith(".caprmedio_"):
                            continue
                        if entry.is_symlink():
                            raise RuntimeError("Project control candidates must not be symlinks")
                        if entry.is_dir(follow_symlinks=False) and os.path.lexists(
                            project / entry.name / "caprmedio_project_settings.toml"
                        ):
                            candidates.append(_settings_control_relative(entry.name))
                if len(candidates) != 1:
                    raise RuntimeError("Project Settings control root is missing or ambiguous")
                relative = candidates[0]
            else:
                relative = _settings_control_relative(control_root)
        finally:
            os.close(descriptor)
        settings_path = project / relative / "caprmedio_project_settings.toml"
        reader = ReadContext(roots=[str(project)], limits=dict(CEILINGS))
        settings = tomllib.loads(reader.read(settings_path).decode("utf-8"))
        paths = settings.get("paths")
        if not isinstance(paths, dict):
            raise RuntimeError("Project Settings requires a paths table")
        declared = paths.get("control_root")
        if not isinstance(declared, str) or not declared:
            raise RuntimeError("Project Settings requires paths.control_root")
        if _settings_control_relative(declared) != relative:
            raise RuntimeError("paths.control_root must be exactly the selected settings carrier's Project child")
        if reader.currentness()["state"] != "unchanged":
            raise RuntimeError("Project Settings changed during resolution")
        return settings_path, settings
    except (OSError, UnicodeError, ValueError) as error:
        raise RuntimeError("Project Settings carrier is unavailable, invalid, or unsafe") from error


def _assert_project_relative_path(root: Path, relative: Path, label: str) -> None:
    project = root.resolve(strict=True)
    path = project / relative
    if path.resolve() != path:
        raise RuntimeError(f"{label} must not contain a symlink or escape the Project root")


def current_timestamp(root: Path) -> str:
    _, settings = _read_project_settings(root)
    value = settings.get("artifact_timestamps", {}).get("timezone", "local")
    if value == "local":
        moment = dt.datetime.now().astimezone()
    elif value == "UTC":
        moment = dt.datetime.now(dt.UTC)
    else:
        try:
            moment = dt.datetime.now(ZoneInfo(value))
        except ZoneInfoNotFoundError as error:
            raise RuntimeError(f"unknown artifact timestamp timezone: {value}") from error
    return moment.strftime("%Y-%m-%d %H:%M:%S %z")


class WorkJournalError(RuntimeError):
    """Stable machine-readable Work Journal failure."""

    def __init__(self, code: str, message: str) -> None:
        self.code = code
        super().__init__(message)


class PartialAppendError(WorkJournalError, OSError):
    """A plain append stopped with only a prefix of receipts known."""

    def __init__(
        self,
        completed_receipts: Sequence[Mapping[str, Any]],
        *,
        uncertain_event_index: int,
        requested_count: int,
    ) -> None:
        self.completed_receipts = [dict(receipt) for receipt in completed_receipts]
        self.receipts = self.completed_receipts
        self.uncertain_event_index = uncertain_event_index
        self.requested_count = requested_count
        super().__init__(
            "journal-append-incomplete",
            "Journal append stopped before all requested records were observed",
        )


def canonical_json_bytes(value: object) -> bytes:
    """The canonical encoding used for event and receipt digests."""
    return json.dumps(
        value,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
        allow_nan=False,
    ).encode("utf-8")


def configured_journal_root(root: Path) -> Path:
    _, settings = _read_project_settings(root)
    paths = settings.get("paths", {})
    control_value = paths.get("control_root")
    if not isinstance(control_value, str) or not control_value:
        raise RuntimeError("Project Settings requires paths.control_root")
    control = Path(control_value)
    if control.is_absolute() or ".." in control.parts or not control.parts:
        raise RuntimeError("paths.control_root must be a safe repository-relative path")
    canonical = control / "_journal"
    value = paths.get("journal_root", canonical.as_posix())
    if not isinstance(value, str) or not value:
        raise RuntimeError("paths.journal_root must be a non-empty string when provided")
    path = Path(value)
    if path.is_absolute() or ".." in path.parts:
        raise RuntimeError("paths.journal_root must be a safe repository-relative path")
    if path != canonical:
        raise RuntimeError("paths.journal_root must be exactly paths.control_root/_journal")
    _assert_project_relative_path(root, canonical, "paths.journal_root")
    return canonical


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
    """Create a legacy v1 record without changing historic record semantics."""
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


def append_record(root: Path, record: dict[str, object]) -> Path:
    """Append unchanged legacy rows in capped parts; retain old date carriers."""
    location = _append_event(root, record, "src-work-journal", str(record["occurred_at"])[:10])
    return root / location["carrier"]


def _part_path(root: Path, author: str, local_date: str, part: int) -> Path:
    return root / configured_journal_root(root) / f"{quote(author, safe='')}-{quote(local_date, safe='')}-part-{part}.ndjson"


def _part_paths(root: Path, author: str, local_date: str) -> list[tuple[int, Path]]:
    directory = root / configured_journal_root(root)
    if not directory.exists():
        return []
    pattern = re.compile(rf"^{re.escape(quote(author, safe=''))}-{re.escape(quote(local_date, safe=''))}-part-([1-9][0-9]*)\.ndjson$")
    paths: list[tuple[int, Path]] = []
    for path in directory.iterdir():
        if path.is_file() and (match := pattern.fullmatch(path.name)):
            paths.append((int(match.group(1)), path))
    paths.sort()
    return paths


def _read_part_bytes(path: Path) -> bytes:
    with os.fdopen(open_regular(path.absolute()), "rb") as stream:
        return stream.read()


def _open_part(root: Path, author: str, local_date: str) -> tuple[Path, bytes, int]:
    paths = _part_paths(root, author, local_date)
    if not paths:
        return _part_path(root, author, local_date, 1), b"", 0
    part, path = paths[-1]
    data = _read_part_bytes(path)
    count = len(data.splitlines())
    if count < MAX_EVENTS_PER_PART:
        return path, data, count
    return _part_path(root, author, local_date, part + 1), b"", 0


def _append_event(root: Path, event: Any, author: str, local_date: str) -> dict[str, Any]:
    # shortcut: concurrent appends may exceed 1000 rows; serialize only if a strict limit is required.
    path, _, count = _open_part(root, author, local_date)
    path.parent.mkdir(parents=True, exist_ok=True)
    parent = open_regular(path.parent.absolute(), directory=True)
    try:
        descriptor = os.open(path.name, os.O_APPEND | os.O_CREAT | os.O_WRONLY | os.O_NOFOLLOW, 0o644, dir_fd=parent)
    finally:
        os.close(parent)
    with os.fdopen(descriptor, "ab") as stream:
        stream.write(canonical_json_bytes(event) + b"\n")
        stream.flush()
        os.fsync(stream.fileno())
    references = event if isinstance(event, Mapping) else {}
    return {
        "event_id": references.get("event_id"),
        "action_id": references.get("action_id"),
        "event_digest": references.get("event_digest"),
        "carrier": path.relative_to(root).as_posix(),
        "line": count + 1,
    }


def append_sealed_events(
    root: Path,
    events: Sequence[Any],
    *,
    author: object,
    local_date: object,
    timezone: object,
    append_context: Mapping[str, Any] | None = None,
) -> list[dict[str, Any]]:
    """Append caller-supplied rows in order, including repeated rows.

    The existing signature is retained for callers; timezone and append_context
    do not impose storage prerequisites.
    """
    receipts: list[dict[str, Any]] = []
    for index, event in enumerate(events):
        try:
            receipts.append(_append_event(root, event, str(author), str(local_date)))
        except FutureCancelledError:
            raise
        except Exception as error:
            raise PartialAppendError(
                receipts,
                uncertain_event_index=index,
                requested_count=len(events),
            ) from error
    return receipts
