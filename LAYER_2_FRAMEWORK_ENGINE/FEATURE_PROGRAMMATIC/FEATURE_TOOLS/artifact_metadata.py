"""Shared metadata reads and atomic artifact writes."""

from __future__ import annotations



import datetime as dt
import os
import re
import tomllib
from pathlib import Path
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError

from project_runtime import atomic_tempfile
from project_selection import bound_selection
from collections.abc import Mapping


SETTINGS_PATH = Path(".caprmedio_caprmedio/caprmedio_project_settings.toml")
TIMESTAMP_FORMAT = "%Y-%m-%d %H:%M:%S %z"


def project_identity(root: Path) -> dict[str, dict[str, object]]:
    """Read Project identity only from the selected Project Settings Carrier."""
    selection = bound_selection(root)
    path = selection.settings_path if selection is not None else root / SETTINGS_PATH
    if not path.is_file() or path.is_symlink():
        raise ValueError(f"Project Settings Carrier is missing or invalid: {SETTINGS_PATH}")
    try:
        settings = selection.settings if selection is not None else tomllib.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, tomllib.TOMLDecodeError) as error:
        raise ValueError(f"invalid Project Settings: {SETTINGS_PATH}") from error
    project = settings.get("project")
    artifacts = settings.get("artifacts")
    identity = artifacts.get("identity") if isinstance(artifacts, Mapping) else None
    if not isinstance(project, Mapping) or not isinstance(identity, Mapping):
        raise ValueError("Project Settings lacks project or artifacts.identity")
    for key in ("key", "name", "repository_slug"):
        value = project.get(key)
        if not isinstance(value, str) or not value.strip():
            raise ValueError(f"Project Settings lacks project.{key}")
    if project["name"] != project["name"].strip().lower():
        raise ValueError("Project Settings project.name must be lowercase without surrounding whitespace")
    prefix = identity.get("project_prefix")
    if not isinstance(prefix, str) or not prefix.strip():
        raise ValueError("Project Settings lacks artifacts.identity.project_prefix")
    obsolete = project.get("obsolete_names", [])
    if not isinstance(obsolete, (list, tuple)) or any(not isinstance(name, str) or not name for name in obsolete):
        raise ValueError("Project Settings project.obsolete_names must be a list of names")
    return {"project": dict(project, obsolete_names=list(obsolete)), "identity": dict(identity)}


def atom_identifier(filename: str, explicit: str | None = None) -> str:
    """Resolve stable identity without absorbing mutable scope, tier, type, or sequence."""
    if explicit:
        return explicit.strip().strip('\"\'')
    name = Path(filename).name
    canonical = re.match(r"(?:[0-9]+-)?(CA-[CAPRMEDIO]-[0-9]+)(?:-|\.|@|$)", name)
    if canonical:
        return canonical.group(1)
    # Unmigrated legacy identities remain opaque; never allocate or renumber here.
    return name.removesuffix(".md").split("--", 1)[0]


def repository_root(path: Path) -> Path:
    selection = bound_selection()
    if selection is not None:
        if not path.resolve().is_relative_to(selection.root):
            raise RuntimeError("carrier is outside the selected Project")
        return selection.root
    for candidate in (path.resolve(), *path.resolve().parents):
        if (candidate / SETTINGS_PATH).is_file():
            return candidate
    raise RuntimeError(f"cannot locate {SETTINGS_PATH} from {path}")


def configured_timezone(root: Path) -> dt.tzinfo | None:
    selection = bound_selection(root)
    settings = selection.settings if selection is not None else tomllib.loads((root / SETTINGS_PATH).read_text(encoding="utf-8"))
    value = settings.get("artifact_timestamps", {}).get("timezone", "local")
    return _timezone_value(value)


def _timezone_value(value: str) -> dt.tzinfo | None:
    if value == "local":
        return None
    if value == "UTC":
        return dt.UTC
    try:
        return ZoneInfo(value)
    except ZoneInfoNotFoundError as error:
        raise RuntimeError(f"unknown artifact timestamp timezone: {value}") from error


def _timestamp(timezone: dt.tzinfo | None) -> str:
    moment = dt.datetime.now().astimezone() if timezone is None else dt.datetime.now(timezone)
    return moment.strftime(TIMESTAMP_FORMAT)


def current_timestamp(root: Path) -> str:
    return _timestamp(configured_timezone(root))


def split_frontmatter(text: str, path: Path) -> tuple[str, str, str]:
    first_line, separator, remainder = text.partition("\n")
    if not separator or first_line not in {"---", "+++"}:
        raise RuntimeError(f"{path}: missing supported frontmatter")
    marker = f"\n{first_line}\n"
    boundary = remainder.find(marker)
    if boundary < 0:
        raise RuntimeError(f"{path}: unterminated frontmatter")
    return first_line, remainder[:boundary], remainder[boundary + len(marker) :]


def atomic_write(path: Path, text: str) -> None:
    descriptor, temporary_name = atomic_tempfile(path, "artifact_metadata")
    try:
        with os.fdopen(descriptor, "w", encoding="utf-8", newline="\n") as handle:
            handle.write(text)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary_name, path)
    except BaseException:
        try:
            os.unlink(temporary_name)
        except FileNotFoundError:
            pass
        raise
