"""Shared, non-executable Work Journal persistence library.

Rows are caller data. Tool CLI entry points live in their respective units;
the shared source-request helpers retain their separate runtime authority.
"""

from __future__ import annotations

import datetime as dt
import hashlib
import json
import os
import re
import sys
import time
import tomllib
import uuid
from concurrent.futures import CancelledError as FutureCancelledError
from contextlib import contextmanager
from pathlib import Path
from typing import Any, Iterator, Mapping, Sequence
from urllib.parse import quote
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError

from project_runtime import atomic_tempfile
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


def repository_root(path: Path) -> Path:
    for candidate in (path.resolve(), *path.resolve().parents):
        if any(control.is_dir() and (control / "caprmedio_project_settings.toml").exists()
               for control in candidate.glob(".caprmedio_*")):
            resolve_settings_path(candidate)
            return candidate
    raise RuntimeError(f"cannot locate Project Settings from {path}")


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


def resolve_settings_path(root: Path, control_root: str | Path | None = None) -> Path:
    """Return the safely validated settings path for exactly this Project root.

    The optional control child is an explicit selection; the compatibility
    form requires a unique root-level ``.caprmedio_*`` settings carrier.
    Neither form searches parent or sibling Projects.
    """
    return _read_project_settings(root, control_root)[0]


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


def canonical_json_digest(value: object) -> str:
    return hashlib.sha256(canonical_json_bytes(value)).hexdigest()


def _sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _write_all(descriptor: int, payload: bytes) -> None:
    offset = 0
    while offset < len(payload):
        written = os.write(descriptor, payload[offset:])
        if written <= 0:
            raise OSError("could not write Work Journal payload")
        offset += written


def _atomic_json(path: Path, value: Mapping[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    descriptor, temporary_name = atomic_tempfile(path, "work_journal")
    temporary = Path(temporary_name)
    try:
        with os.fdopen(descriptor, "wb") as handle:
            handle.write(canonical_json_bytes(value) + b"\n")
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, path)
    except BaseException:
        try:
            temporary.unlink()
        except FileNotFoundError:
            pass
        raise


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


def configured_runtime_root(root: Path) -> Path:
    _, settings = _read_project_settings(root)
    value = settings.get("paths", {}).get("runtime_root", ".caprmedio_runtime")
    if not isinstance(value, str) or not value:
        raise RuntimeError("Project Settings requires paths.runtime_root")
    path = Path(value)
    if path.is_absolute() or ".." in path.parts or path.parts != (".caprmedio_runtime",):
        raise RuntimeError("paths.runtime_root must be .caprmedio_runtime")
    _assert_project_relative_path(root, path, "paths.runtime_root")
    return path


# Schema-v1 compatibility ---------------------------------------------------

def segment_path(root: Path, occurred_at: str) -> Path:
    """Return the legacy v1 carrier path for existing callers only."""
    return root / configured_journal_root(root) / f"src-work-journal-{occurred_at[:10]}.ndjson"


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


# Optional event metadata --------------------------------------------------

def event_digest(event: Mapping[str, Any]) -> str:
    unsigned = dict(event)
    unsigned.pop("event_digest", None)
    return canonical_json_digest(unsigned)


def with_event_digest(event: Mapping[str, Any]) -> dict[str, Any]:
    sealed = dict(event)
    sealed["event_digest"] = event_digest(sealed)
    return sealed




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


def _carrier_records(path: Path) -> tuple[bytes, list[Any]]:
    data = _read_part_bytes(path) if path.exists() else b""
    return data, [json.loads(line) for line in data.splitlines()]


def _read_part_bytes(path: Path) -> bytes:
    with os.fdopen(open_regular(path.absolute()), "rb") as stream:
        return stream.read()


def read_records(root: Path) -> list[Any]:
    """Read stored JSON rows without interpreting their metadata."""
    return [
        record
        for path in _all_journal_parts(root)
        for record in _carrier_records(path)[1]
    ]


def _all_journal_parts(root: Path) -> list[Path]:
    directory = root / configured_journal_root(root)
    if not directory.exists():
        return []
    return sorted((path for path in directory.glob("*.ndjson") if path.is_file()), key=_part_order)


def _part_order(path: Path) -> tuple[str, int]:
    partition, _, batch = path.stem.rpartition("-part-")
    return (partition, int(batch)) if partition and batch.isdecimal() else (path.stem, 0)


@contextmanager
def _event_lock(root: Path, event_id: str) -> Iterator[None]:
    """Serialize an Event identity across every author/date partition."""
    locks = root / configured_runtime_root(root) / "state" / "work_journal" / "locks" / "events"
    locks.mkdir(parents=True, exist_ok=True)
    path = locks / f"{_sha256(event_id.encode('utf-8'))}.lock"
    token = str(uuid.uuid4())
    deadline = time.monotonic() + 30.0
    descriptor: int | None = None
    while descriptor is None:
        try:
            descriptor = os.open(path, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o600)
        except FileExistsError:
            if time.monotonic() >= deadline:
                raise WorkJournalError("journal-lock-unavailable", f"Journal event lock remains held: {event_id}")
            time.sleep(0.05)
    try:
        try:
            _write_all(descriptor, canonical_json_bytes({"token": token, "pid": os.getpid()}) + b"\n")
            os.fsync(descriptor)
        finally:
            os.close(descriptor)
        yield
    finally:
        try:
            value = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            value = {}
        if value.get("token") == token:
            path.unlink(missing_ok=True)


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




def register_selected_run_dispatch(
    root: Path,
    *,
    request_id: str,
    canonical_request_bytes: bytes,
) -> tuple[dict[str, Any], bool]:
    """Persist one accepted selected-run dispatch before any route effect.

    The carrier is runtime recovery evidence, not a second historical Journal.
    A process restart can therefore refuse to dispatch the same request again
    until it inspects or recovers the original evidence.
    """
    if not isinstance(request_id, str) or not request_id:
        raise WorkJournalError("invalid-dispatch", "request_id must be a non-empty string")
    if not isinstance(canonical_request_bytes, bytes) or not canonical_request_bytes:
        raise WorkJournalError("invalid-dispatch", "canonical_request_bytes must be non-empty bytes")
    try:
        parsed = json.loads(canonical_request_bytes)
    except json.JSONDecodeError as error:
        raise WorkJournalError("invalid-dispatch", "canonical request bytes must be JSON") from error
    if canonical_json_bytes(parsed) != canonical_request_bytes:
        raise WorkJournalError("invalid-dispatch", "request dispatch bytes must be canonical JSON")
    digest = _sha256(canonical_request_bytes)
    path = (
        root
        / configured_runtime_root(root)
        / "state"
        / "work_journal"
        / "selected_runs"
        / "requests"
        / f"{_sha256(request_id.encode('utf-8'))}.json"
    )
    value = {
        "schema_version": 1,
        "request_id": request_id,
        "canonical_request_bytes": canonical_request_bytes.decode("utf-8"),
        "canonical_request_bytes_digest": digest,
        "state": "accepted",
    }
    with _event_lock(root, f"selected-run-request:{request_id}"):
        if path.exists():
            try:
                prior = json.loads(path.read_text(encoding="utf-8"))
            except (OSError, json.JSONDecodeError) as error:
                raise WorkJournalError("invalid-dispatch", f"cannot read selected-run dispatch for {request_id}") from error
            expected = {"schema_version", "request_id", "canonical_request_bytes", "canonical_request_bytes_digest", "state"}
            if not isinstance(prior, dict) or set(prior) != expected or prior.get("schema_version") != 1 or prior.get("request_id") != request_id:
                raise WorkJournalError("invalid-dispatch", f"selected-run dispatch for {request_id} has invalid fields")
            if prior.get("canonical_request_bytes") != canonical_request_bytes.decode("utf-8") or prior.get("canonical_request_bytes_digest") != digest:
                raise WorkJournalError("request-id-conflict", f"request_id {request_id} already has different accepted dispatch bytes")
            if prior.get("state") != "accepted":
                raise WorkJournalError("invalid-dispatch", f"selected-run dispatch for {request_id} has invalid state")
            return prior, False
        _atomic_json(path, value)
        return value, True
