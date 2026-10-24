"""Shared CAPRMEDIO runtime and temporary-path boundaries."""

from __future__ import annotations

import os
import re
import tempfile
from pathlib import Path


RUNTIME_DIRECTORY = Path(".caprmedio_runtime")
TEMPORARY_DIRECTORY = Path(".caprmedio_tmp")
OWNER = re.compile(r"[a-z0-9][a-z0-9_-]{0,63}\Z")


class TemporaryBoundaryError(RuntimeError):
    """A disposable Carrier cannot be placed in the required Project Temporary State."""


def _validate_directory_components(root: Path, directory: Path) -> None:
    """Reject existing symlink or non-directory components below a Project root."""

    try:
        relative = directory.relative_to(root)
    except ValueError as error:
        raise TemporaryBoundaryError(
            f"temporary state path is outside Project root: {directory}"
        ) from error
    current = root
    for component in relative.parts:
        current /= component
        if current.is_symlink():
            raise TemporaryBoundaryError(
                f"temporary state path contains symlinked directory: {current}"
            )
        if current.exists() and not current.is_dir():
            raise TemporaryBoundaryError(f"temporary state path is not a directory: {current}")


def _existing_directory(path: Path) -> Path:
    """Return the nearest existing directory used for a pre-mutation device check."""

    candidate = path
    while not candidate.exists():
        parent = candidate.parent
        if parent == candidate:
            raise TemporaryBoundaryError(f"cannot resolve destination directory: {path}")
        candidate = parent
    if not candidate.is_dir():
        raise TemporaryBoundaryError(f"destination path is not a directory: {candidate}")
    return candidate


def repository_root(reference: Path | str) -> Path:
    """Resolve the nearest checkout or self-contained CAPRMEDIO Project.

    Installed and sealed Projects need not contain Git administration data.
    Their two authoritative control carriers identify the same boundary.
    A lone folder name or runtime/scratch directory is not a Project marker.
    """

    candidate = Path(reference).expanduser().resolve()
    if not candidate.is_dir():
        candidate = candidate.parent
    for root in (candidate, *candidate.parents):
        if (root / ".git").exists():
            return root
        for control in root.glob(".caprmedio_*"):
            if control.is_symlink() or not control.is_dir():
                continue
            markers = (
                control / "caprmedio_project_settings.toml",
                control / "project_structure.toml",
            )
            if all(path.is_file() and not path.is_symlink() for path in markers):
                return root
    raise TemporaryBoundaryError(f"cannot resolve Project root from {candidate}")


def owned_temporary_root(repository: Path | str, owner: str) -> Path:
    """Create and return one component-owned temporary directory."""

    if not OWNER.fullmatch(owner):
        raise TemporaryBoundaryError(f"invalid temporary-state owner: {owner}")
    root = repository_root(repository)
    directory = root / TEMPORARY_DIRECTORY / owner
    _validate_directory_components(root, directory)
    directory.mkdir(parents=True, exist_ok=True)
    return directory


def atomic_tempfile(
    destination: Path,
    owner: str,
    *,
    repository: Path | str | None = None,
    prefix: str | None = None,
    suffix: str = "",
) -> tuple[int, str]:
    """Allocate an atomic-write intermediate only below Project Temporary State."""

    root = repository_root(repository if repository is not None else destination)
    directory = root / TEMPORARY_DIRECTORY / owner / "atomic"
    _validate_directory_components(root, directory)
    staging_device = os.stat(_existing_directory(directory)).st_dev
    destination_device = os.stat(_existing_directory(destination.parent)).st_dev
    if staging_device != destination_device:
        raise TemporaryBoundaryError(
            f"temporary state and destination are on different filesystems: {directory} -> {destination}"
        )
    owned_temporary_root(root, owner)
    directory.mkdir(parents=True, exist_ok=True)
    destination.parent.mkdir(parents=True, exist_ok=True)
    return tempfile.mkstemp(
        prefix=prefix or f".{destination.name}.",
        suffix=suffix,
        dir=directory,
    )


__all__ = [
    "RUNTIME_DIRECTORY",
    "TEMPORARY_DIRECTORY",
    "TemporaryBoundaryError",
    "atomic_tempfile",
    "owned_temporary_root",
    "repository_root",
]
