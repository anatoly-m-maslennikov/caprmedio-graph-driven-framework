"""Read the two Project Settings values needed before Scope declarations load."""

from __future__ import annotations

from pathlib import Path
import re
import tomllib
from typing import Any, Mapping

from project_selection import bound_selection
from VALIDATE_ATOMS.validate_atoms_workers.read_io import ReadContext
from VALIDATE_ATOMS.validate_atoms_workers.settings import CEILINGS


_SETTINGS_PATH = Path(".caprmedio_caprmedio/caprmedio_project_settings.toml")
_CONTROL_ROOT = Path(".caprmedio_caprmedio")


class ProjectSettingsValueError(RuntimeError):
    def __init__(self, code: str, message: str) -> None:
        self.code = code
        super().__init__(message)


def _settings(root: Path) -> Mapping[str, Any]:
    root = root.resolve()
    selection = bound_selection(root)
    if selection is not None:
        return selection.settings
    try:
        raw = ReadContext(roots=[str(root)], limits=dict(CEILINGS)).read(root / _SETTINGS_PATH)
        return tomllib.loads(raw.decode("utf-8"))
    except (OSError, RuntimeError, UnicodeError, tomllib.TOMLDecodeError) as error:
        raise ProjectSettingsValueError(
            "project-settings-unavailable", "cannot read current Project Settings"
        ) from error


def control_root(root: Path) -> Path:
    """Return the selected control root or the one canonical unbound carrier root."""
    root = root.resolve()
    selection = bound_selection(root)
    if selection is not None:
        return selection.control_root
    settings = _settings(root)
    configured = settings.get("paths", {}).get("control_root")
    candidate = Path(configured) if isinstance(configured, str) and configured else None
    if candidate is None or candidate.is_absolute() or ".." in candidate.parts or candidate != _CONTROL_ROOT:
        raise ProjectSettingsValueError(
            "project-settings-invalid", "paths.control_root must be .caprmedio_caprmedio"
        )
    return (root / candidate).resolve()


def project_identity_prefix(root: Path) -> str:
    """Return the selected or canonical-carrier Project Atom prefix."""
    prefix = _settings(root).get("artifacts", {}).get("identity", {}).get("project_prefix")
    if not isinstance(prefix, str) or re.fullmatch(r"[A-Za-z0-9]+", prefix) is None:
        raise ProjectSettingsValueError(
            "project-settings-invalid", "artifacts.identity.project_prefix is invalid"
        )
    return prefix
