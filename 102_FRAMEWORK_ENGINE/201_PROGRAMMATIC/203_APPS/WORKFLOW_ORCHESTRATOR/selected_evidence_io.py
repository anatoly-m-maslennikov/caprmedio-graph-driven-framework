"""Safe filesystem transport for selected Workflow evidence."""

from __future__ import annotations

import json
import os
from pathlib import Path
import stat
import sys
from typing import Any

from selected_execution_contracts import RUN_ID, SelectedExecutionError, canonical_json


def run_directory(root: Path, run_id: str) -> Path:
    """Return the Project-local directory for a validated selected Run."""
    if not isinstance(run_id, str) or not RUN_ID.fullmatch(run_id):
        raise SelectedExecutionError("invalid selected Run ID")
    folder = root / ".caprmedio_install/workflow_orchestrator/runs" / run_id
    cursor = root
    for part in folder.relative_to(root).parts:
        cursor = cursor / part
        if cursor.is_symlink() or (cursor.exists() and not cursor.is_dir()):
            raise SelectedExecutionError("selected Run directory contains an unsafe carrier")
    return folder


def safe_path(root: Path, relative: str) -> Path:
    """Resolve an existing, regular, non-symlink definition under ``root``."""
    if not isinstance(relative, str) or not relative:
        raise SelectedExecutionError("definition path is required")
    candidate = root / relative
    if Path(relative).is_absolute() or ".." in Path(relative).parts:
        raise SelectedExecutionError("unsafe definition path")
    try:
        resolved = candidate.resolve(strict=True)
        resolved.relative_to(root)
    except (OSError, ValueError, FileNotFoundError) as error:
        raise SelectedExecutionError("unsafe or unavailable definition path") from error
    cursor = root
    for part in Path(relative).parts:
        cursor /= part
        if cursor.is_symlink():
            raise SelectedExecutionError("definition symlinks are not admitted")
    if not resolved.is_file():
        raise SelectedExecutionError("definition path is not a file")
    return resolved


def atomic_write(path: Path, value: object) -> None:
    """Write canonical evidence and durably replace its destination."""
    tools = str(Path(__file__).resolve().parents[2] / "201_TOOLS")
    if tools not in sys.path:
        sys.path.insert(0, tools)
    from project_runtime import atomic_tempfile

    payload = canonical_json(value)
    descriptor, name = atomic_tempfile(path, "workflow_orchestrator")
    temporary_path = Path(name)
    try:
        with os.fdopen(descriptor, "wb") as temporary:
            temporary.write(payload)
            temporary.flush()
            os.fsync(temporary.fileno())
        os.replace(temporary_path, path)
        directory = os.open(path.parent, os.O_RDONLY)
        try:
            os.fsync(directory)
        finally:
            os.close(directory)
    finally:
        temporary_path.unlink(missing_ok=True)


def bounded_bytes(path: Path, maximum_bytes: int) -> bytes:
    """Read a bounded regular carrier through one non-following descriptor."""
    if type(maximum_bytes) is not int or maximum_bytes < 1:
        raise SelectedExecutionError("evidence byte limit must be a positive integer")
    flags = os.O_RDONLY | getattr(os, "O_NOFOLLOW", 0) | getattr(os, "O_NONBLOCK", 0)
    descriptor = -1
    try:
        descriptor = os.open(path, flags)
        metadata = os.fstat(descriptor)
        if not stat.S_ISREG(metadata.st_mode) or metadata.st_size > maximum_bytes:
            raise SelectedExecutionError("saved evidence carrier is unsafe or oversized")
        payload = bytearray()
        while len(payload) <= maximum_bytes:
            chunk = os.read(descriptor, maximum_bytes + 1 - len(payload))
            if not chunk:
                break
            payload.extend(chunk)
        if len(payload) > maximum_bytes:
            raise SelectedExecutionError("saved evidence carrier is oversized")
        return bytes(payload)
    except (OSError, ValueError) as error:
        raise SelectedExecutionError("saved evidence carrier is unsafe or unreadable") from error
    finally:
        if descriptor >= 0:
            os.close(descriptor)


def bounded_read(path: Path) -> dict[str, Any]:
    """Read one saved evidence object, rejecting links and non-mappings."""
    if path.is_symlink():
        raise SelectedExecutionError("saved selected execution evidence cannot be a symlink")
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as error:
        raise SelectedExecutionError("invalid saved selected execution evidence") from error
    if not isinstance(value, dict):
        raise SelectedExecutionError("invalid saved selected execution evidence")
    return value
