"""Resolve and bind one explicit Project without repository or sibling fallback.

Selection is read-only.  The two Project-local TOML carriers are read through
the existing bounded, non-following reader and retained as immutable snapshots.
Container startup may explicitly retain the host identity; ambient environment
variables never select a Project or replace its identity here.
"""

from __future__ import annotations

from collections.abc import Iterator, Mapping
from contextlib import contextmanager
from contextvars import ContextVar
from dataclasses import dataclass, field, replace
import hashlib
import os
from pathlib import Path
import re
import stat
import tomllib
from types import MappingProxyType
from typing import Any

from VALIDATE_ATOMS.validate_atoms_workers.read_io import ReadContext, open_regular, protected
from VALIDATE_ATOMS.validate_atoms_workers.settings import CEILINGS


SETTINGS_FILENAME = "caprmedio_project_settings.toml"
STRUCTURE_FILENAME = "project_structure.toml"
_CONTROL_PREFIX = ".caprmedio_"
_IDENTITY = re.compile(r"[0-9a-f]{64}\Z")


class ProjectSelectionError(ValueError):
    """An attributable refusal, without substituting another Project."""

    code = "PROJECT_SELECTION_REFUSED"
    condition = code


def _freeze(value: Any) -> Any:
    if isinstance(value, Mapping):
        return MappingProxyType({key: _freeze(item) for key, item in value.items()})
    if isinstance(value, (list, tuple)):
        return tuple(_freeze(item) for item in value)
    return value


@dataclass(frozen=True)
class ProjectSelection:
    root: Path
    control_root: Path
    control_relative: Path
    instance_id: str
    settings: Mapping[str, Any]
    structure: Mapping[str, Any]
    provenance: Mapping[str, Any] = field(default_factory=dict)
    host_root: Path | None = None

    def __post_init__(self) -> None:
        object.__setattr__(self, "settings", _freeze(self.settings))
        object.__setattr__(self, "structure", _freeze(self.structure))
        object.__setattr__(self, "provenance", _freeze(self.provenance))

    @property
    def settings_path(self) -> Path:
        return self.control_root / SETTINGS_FILENAME

    @property
    def structure_path(self) -> Path:
        return self.control_root / STRUCTURE_FILENAME

    @property
    def installed_state(self) -> Path:
        return self.launcher_state

    @property
    def compose_project(self) -> str:
        return "caprmedio-mcp-" + self.instance_id[:24]

    @property
    def launcher_state(self) -> Path:
        return self.root / ".caprmedio_install" / "project_mcp" / self.instance_id

    @property
    def reload_state(self) -> Path:
        return self.root / ".caprmedio_install" / "mcp_hot_reload" / self.instance_id


_SELECTION: ContextVar[ProjectSelection | None] = ContextVar("caprmedio_project_selection", default=None)


def _project_root(value: str | Path) -> Path:
    try:
        raw = Path(value).expanduser()
        if ".." in raw.parts or protected(raw):
            raise ProjectSelectionError("Project root is unsafe")
        path = Path(os.path.abspath(raw))
        if path.resolve(strict=True) != path:
            raise ProjectSelectionError("Project root must not contain a symlink")
        descriptor = open_regular(path, directory=True)
        try:
            if not stat.S_ISDIR(os.fstat(descriptor).st_mode):
                raise ProjectSelectionError("Project root is not a directory")
        finally:
            os.close(descriptor)
        return path
    except ProjectSelectionError:
        raise
    except (OSError, RuntimeError, TypeError, ValueError) as error:
        raise ProjectSelectionError("Project root is unavailable or unsafe") from error


def _control_relative(value: str | Path) -> Path:
    if not isinstance(value, (str, Path)) or not str(value):
        raise ProjectSelectionError("Control root must name one direct Project child")
    path = Path(value)
    if (path.is_absolute() or len(path.parts) != 1 or ".." in path.parts
            or not path.name.startswith(_CONTROL_PREFIX) or path.name == _CONTROL_PREFIX
            or str(value) != path.as_posix() or protected(path)):
        raise ProjectSelectionError("Control root must name one normalized direct Project child")
    return path


def _control_candidates(root: Path) -> list[Path]:
    descriptor = open_regular(root, directory=True)
    try:
        with os.scandir(descriptor) as entries:
            candidates = []
            for entry in entries:
                if not entry.name.startswith(_CONTROL_PREFIX):
                    continue
                if entry.is_symlink():
                    raise ProjectSelectionError("Project control candidates must not be symlinks")
                if not entry.is_dir(follow_symlinks=False):
                    continue
                control = root / entry.name
                # Runtime/install/scratch directories are not Project candidates.
                if any(os.path.lexists(control / filename)
                       for filename in (SETTINGS_FILENAME, STRUCTURE_FILENAME)):
                    candidates.append(_control_relative(entry.name))
            return sorted(candidates)
    finally:
        os.close(descriptor)


def _read_toml(reader: ReadContext, path: Path) -> dict[str, Any]:
    try:
        return tomllib.loads(reader.read(path).decode("utf-8"))
    except (OSError, RuntimeError, UnicodeError, ValueError) as error:
        raise ProjectSelectionError(f"Required Project carrier is unavailable or invalid: {path.name}") from error


def _validate_structure(structure: Mapping[str, Any], root: Path) -> None:
    if type(structure.get("schema_version")) is not int or structure["schema_version"] != 1:
        raise ProjectSelectionError("Project Structure schema_version must be 1")
    rows = structure.get("scope_units", [])
    if not isinstance(rows, list):
        raise ProjectSelectionError("Project Structure scope_units must be an array of tables")
    names = set()
    for row in rows:
        if not isinstance(row, dict):
            raise ProjectSelectionError("Project Structure scope_units must be tables")
        name = row.get("scope_unit_name")
        if not isinstance(name, str) or not name or name in names:
            raise ProjectSelectionError("Project Structure Scope Unit names must be unique and non-empty")
        names.add(name)
        if "authority_path" in row:
            value = row["authority_path"]
            if not isinstance(value, str) or not value:
                raise ProjectSelectionError("Project Structure authority_path must be a relative path")
            authority = Path(value)
            if (authority.is_absolute() or ".." in authority.parts or value != authority.as_posix()
                    or protected(authority)):
                raise ProjectSelectionError("Project Structure authority_path is unsafe")
            # The authority may be declared before materialization.  Check all
            # existing components without requiring the final directory to exist.
            try:
                declared = root / authority
                if declared.resolve() != declared or not declared.is_relative_to(root):
                    raise ProjectSelectionError("Project Structure authority_path escapes or contains a symlink")
            except (OSError, RuntimeError, ValueError) as error:
                raise ProjectSelectionError("Project Structure authority_path is unavailable or unsafe") from error


def _instance_id(root: Path, relative: Path) -> str:
    return hashlib.sha256(f"{root}\0{relative.as_posix()}".encode("utf-8")).hexdigest()


def resolve_project(project_root: str | Path, control_root: str | Path | None = None) -> ProjectSelection:
    """Read exactly one local Project selection before any runtime effects."""
    root = _project_root(project_root)
    try:
        if control_root is None:
            candidates = _control_candidates(root)
            if len(candidates) != 1:
                raise ProjectSelectionError("Project control root is missing or ambiguous")
            relative = candidates[0]
        else:
            relative = _control_relative(control_root)
        control = root / relative
        descriptor = open_regular(control, directory=True)
        os.close(descriptor)
        reader = ReadContext(roots=[str(root)], limits=dict(CEILINGS))
        settings_path, structure_path = control / SETTINGS_FILENAME, control / STRUCTURE_FILENAME
        settings = _read_toml(reader, settings_path)
        paths = settings.get("paths")
        if not isinstance(paths, dict):
            raise ProjectSelectionError("Project Settings must contain a paths table")
        declared = paths.get("control_root")
        if not isinstance(declared, str) or _control_relative(declared) != relative:
            raise ProjectSelectionError("Project Settings control_root contradicts the selection")
        project = settings.get("project")
        if not isinstance(project, dict) or not isinstance(project.get("name"), str) or not project["name"].strip():
            raise ProjectSelectionError("Project Settings must contain a non-empty Project name")
        structure = _read_toml(reader, structure_path)
        _validate_structure(structure, root)
        if reader.currentness()["state"] != "unchanged":
            raise ProjectSelectionError("Project carriers changed during selection")
        provenance = {
            path.relative_to(root).as_posix(): {
                "sha256": reader.fingerprints[str(path)],
                "size": reader.sizes[str(path)],
                "schema_version": document.get("schema_version"),
            }
            for path, document in ((settings_path, settings), (structure_path, structure))
        }
        return ProjectSelection(root, control, relative, _instance_id(root, relative), settings,
                                structure, provenance, host_root=root)
    except ProjectSelectionError:
        raise
    except (OSError, RuntimeError, TypeError, ValueError) as error:
        raise ProjectSelectionError("Selected Project control is unavailable or unsafe") from error


@contextmanager
def bind_selection(selection: ProjectSelection) -> Iterator[ProjectSelection]:
    """Bind an already selected context for this startup/task and restore it."""
    if not isinstance(selection, ProjectSelection):
        raise ProjectSelectionError("Only a validated ProjectSelection can be bound")
    token = _SELECTION.set(selection)
    try:
        yield selection
    finally:
        _SELECTION.reset(token)


def bound_selection(root: str | Path | None = None) -> ProjectSelection | None:
    """Return only explicit startup context, validating its root when supplied."""
    selection = _SELECTION.get()
    if selection is None:
        return None
    if root is not None and selection.root != _project_root(root):
        raise ProjectSelectionError("Active Project selection belongs to another root")
    return selection


def active_selection(root: str | Path) -> ProjectSelection:
    """Use the bound selection, refusing foreign roots; otherwise resolve once."""
    selection = bound_selection(root)
    return selection if selection is not None else resolve_project(root)


def rebind_selection(selection: ProjectSelection, instance_id: str, *,
                     host_root: str | Path | None = None) -> ProjectSelection:
    """Retain an explicitly admitted host identity after container translation.

    Only startup callers transport this value.  When the canonical host root is
    carried too, verify its identity formula.  Existing host directories must
    use canonical non-symlink spelling; an unmounted host path need not exist
    inside the container.  This helper never reads an environment variable.
    """
    if not isinstance(selection, ProjectSelection) or not isinstance(instance_id, str) or not _IDENTITY.fullmatch(instance_id):
        raise ProjectSelectionError("Transported Project identity is invalid")
    host = selection.host_root if instance_id == selection.instance_id else None
    if host_root is not None:
        try:
            host = Path(host_root)
        except (TypeError, ValueError) as error:
            raise ProjectSelectionError("Transported host root is invalid") from error
        if (not host.is_absolute() or ".." in host.parts or str(host_root) != host.as_posix()
                or host.as_posix().startswith("//")
                or protected(host) or _instance_id(host, selection.control_relative) != instance_id):
            raise ProjectSelectionError("Transported Project identity contradicts its host binding")
        if os.path.lexists(host):
            _project_root(host)
    return replace(selection, instance_id=instance_id, host_root=host)


__all__ = ["ProjectSelection", "ProjectSelectionError", "resolve_project", "bind_selection",
           "bound_selection", "active_selection", "rebind_selection"]
