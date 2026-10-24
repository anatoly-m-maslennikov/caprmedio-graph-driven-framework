"""Bounded Project-installation preflight and source helpers."""

from __future__ import annotations

import hashlib
import os
from pathlib import Path
import re

from INSTALL_TOOLS.host_installation_io import HostInstallationError
from project_selection import ProjectSelectionError, resolve_project


SKILL_FILES = ("SKILL.md", "agents/openai.yaml")
RESERVED_CONTROLS = frozenset({".caprmedio_runtime", ".caprmedio_tmp", ".caprmedio_install"})
LEGACY_DIGESTS = {
    "SKILL.md": "8a6e408af22c78ca4cb143c1a5d9785716ec66109ee5bbfeb665e457f9ef8d06",
    "agents/openai.yaml": "b9b4f314f2773c5a9badee4843625b05f40b9fb3400d55a338275d44e748aba6",
}
SAFE_PREFIX = re.compile(r"[A-Z][A-Z0-9_-]*\Z")


class ProjectInstallationError(HostInstallationError):
    def __init__(self, code: str, message: str) -> None:
        super().__init__(code, message)


def _fail(code: str, message: str) -> None:
    raise ProjectInstallationError(code, message)


def canonical(value: Path, label: str) -> Path:
    if not isinstance(value, Path) or not value.is_absolute() or ".." in value.parts:
        _fail(f"{label}-unsafe", f"{label} must be an absolute canonical directory")
    try:
        resolved = value.resolve(strict=True)
    except (OSError, RuntimeError) as error:
        raise ProjectInstallationError(f"{label}-unavailable", f"{label} is unavailable") from error
    if resolved != value or not resolved.is_dir() or resolved.parent == resolved:
        _fail(f"{label}-unsafe", f"{label} must be a non-root canonical directory")
    return resolved


def project_path(root: Path, relative: str, label: str) -> Path:
    path = Path(relative)
    if path.is_absolute() or ".." in path.parts or not relative or path.as_posix() != relative:
        _fail(f"{label}-unsafe", f"{label} must be a normalized Project-relative path")
    current = root
    for part in path.parts:
        current /= part
        if os.path.lexists(current) and current.is_symlink():
            _fail(f"{label}-symlink", f"{label} contains a symlink")
    return root / path


def directory_target(path: Path, label: str = "Project directory") -> bool:
    if os.path.lexists(path) and (path.is_symlink() or not path.is_dir()):
        _fail(f"{label}-conflict", f"{label} is not an owned directory")
    return not os.path.lexists(path)


def project_prefix(value: object) -> str:
    if not isinstance(value, str) or not SAFE_PREFIX.fullmatch(value):
        _fail("project-prefix-invalid", "project prefix must be uppercase alphanumeric text")
    return value


def control_candidates(root: Path, control_prefix: str) -> list[Path]:
    try:
        entries = sorted(root.iterdir(), key=lambda item: item.name)
    except OSError as error:
        raise ProjectInstallationError(
            "project-list-failed", "cannot inspect Project root"
        ) from error
    result = []
    for entry in entries:
        if entry.name == ".caprmedio":
            _fail("legacy-control-root", "legacy .caprmedio control root is unsupported")
        if not entry.name.startswith(control_prefix) or entry.name in RESERVED_CONTROLS:
            continue
        if entry.is_symlink():
            _fail("control-root-symlink", f"control root is a symlink: {entry.name}")
        if entry.is_dir():
            result.append(entry)
    return result


def select_project(root: Path, control_prefix: str):
    controls = control_candidates(root, control_prefix)
    try:
        selection = resolve_project(root)
    except ProjectSelectionError as error:
        if controls:
            _fail("project-selection-conflict", str(error))
        return None
    if any(path != selection.control_root for path in controls):
        _fail("ambiguous-control-root", "more than one Project control directory exists")
    return selection


def read_skill_source(root: Path) -> dict[str, bytes]:
    skill = (
        root
        if root.name == "ca"
        else project_path(root, "102_FRAMEWORK_ENGINE/202_AGENTIC/205_SKILLS/ca", "skill-source")
    )
    if not skill.is_dir():
        _fail("skill-source-unavailable", "canonical ca Skill source is unavailable")
    result = {}
    for relative in SKILL_FILES:
        path = project_path(skill, relative, "skill-source-file")
        if path.is_symlink() or not path.is_file():
            _fail("skill-source-unavailable", f"canonical ca Skill file is unavailable: {relative}")
        try:
            result[relative] = path.read_bytes()
        except OSError as error:
            raise ProjectInstallationError(
                "skill-source-unavailable", f"cannot read {relative}"
            ) from error
    return result


def _validate_skill_target(skill: Path) -> None:
    if os.path.lexists(skill) and (skill.is_symlink() or not skill.is_dir()):
        _fail("skill-target-conflict", "Project ca Skill target is not an owned directory")
    if not skill.is_dir():
        return
    if any(item.name not in {"SKILL.md", "agents"} for item in skill.iterdir()):
        _fail("skill-target-conflict", "Project ca Skill contains an unowned carrier")
    agents = skill / "agents"
    if os.path.lexists(agents) and (agents.is_symlink() or not agents.is_dir()):
        _fail("skill-target-conflict", "Project ca Skill agents target is not a directory")
    if agents.is_dir() and any(item.name != "openai.yaml" for item in agents.iterdir()):
        _fail("skill-target-conflict", "Project ca Skill agents contains an unowned carrier")


def skill_updates(
    skill: Path, source: dict[str, bytes]
) -> tuple[tuple[Path, bytes, bytes | None], ...]:
    _validate_skill_target(skill)
    updates = []
    for relative, content in source.items():
        path = skill / relative
        if os.path.lexists(path) and (path.is_symlink() or not path.is_file()):
            _fail(
                "skill-target-conflict",
                f"Project ca Skill carrier is not a regular file: {relative}",
            )
        previous = None
        if path.is_file():
            try:
                previous = path.read_bytes()
                digest = hashlib.sha256(previous).hexdigest()
            except OSError as error:
                raise ProjectInstallationError(
                    "skill-target-conflict", f"cannot read {relative}"
                ) from error
            if digest not in {hashlib.sha256(content).hexdigest(), LEGACY_DIGESTS[relative]}:
                _fail("skill-target-conflict", f"Project ca Skill carrier differs: {relative}")
        updates.append((path, content, previous))
    return tuple(updates)


def rollback(created, applied):
    retained, conflicts = [], []
    for update in reversed(applied):
        try:
            update.restore()
        except BaseException as error:
            conflicts.append(f"{update.path}: {error}")
    for path, inode in reversed(created):
        try:
            state = path.stat()
            if (state.st_dev, state.st_ino) != inode:
                retained.append(str(path))
            else:
                path.rmdir()
        except OSError as error:
            retained.append(f"{path} ({error})")
    return retained, conflicts
