"""Digest, regular-file, and exact-preimage safeguards for migrations."""

from __future__ import annotations

import hashlib
from pathlib import Path

from .models import MigrationError, MigrationPlan


def sha256(content: bytes) -> str:
    """Return the stable digest used for migration preimages."""
    return hashlib.sha256(content).hexdigest()


def read_regular_file(path: Path) -> bytes:
    """Read one non-symlink regular file or raise a safety error."""
    if path.is_symlink():
        raise MigrationError(f"symlink is outside the migration contract: {path}")
    if not path.is_file():
        raise MigrationError(f"expected a regular file: {path}")
    return path.read_bytes()


def assert_preimages(plan: MigrationPlan) -> None:
    """Refuse a plan whose source bytes changed after preflight."""
    validate_plan(plan)
    for operation in plan.writes:
        _assert_write_preimage(operation.path, operation.before_sha256)
    for operation in plan.deletes:
        _assert_delete_preimage(operation.path, operation.before_sha256)


def _assert_write_preimage(path: Path, digest: str | None) -> None:
    if digest is None:
        if path.exists():
            raise MigrationError(f"new target appeared after planning: {path}")
        return
    if sha256(read_regular_file(path)) != digest:
        raise MigrationError(f"file changed after planning: {path}")


def _assert_delete_preimage(path: Path, digest: str) -> None:
    if sha256(read_regular_file(path)) != digest:
        raise MigrationError(f"file changed after planning: {path}")


def validate_plan(plan: MigrationPlan) -> None:
    """Enforce containment and collision rules for every migration recipe."""
    root = plan.root.resolve()
    if not root.is_dir():
        raise MigrationError(f"migration root is not a directory: {root}")
    write_paths = [item.path for item in plan.writes]
    delete_paths = [item.path for item in plan.deletes]
    resolved_writes = _validated_paths(root, write_paths, "write")
    resolved_deletes = _validated_paths(root, delete_paths, "delete")
    overlap = set(resolved_writes) & set(resolved_deletes)
    if overlap:
        raise MigrationError(f"write/delete collision: {sorted(overlap)}")


def _validated_paths(root: Path, paths: list[Path], kind: str) -> list[Path]:
    resolved = [_contained_path(root, path) for path in paths]
    if len(resolved) != len(set(resolved)):
        raise MigrationError(f"duplicate {kind} target in migration plan")
    return resolved


def _contained_path(root: Path, path: Path) -> Path:
    if not path.is_absolute():
        raise MigrationError(f"migration target is not absolute: {path}")
    resolved = path.resolve(strict=False)
    try:
        relative = resolved.relative_to(root)
    except ValueError as error:
        raise MigrationError(f"migration target escapes root: {path}") from error
    if not relative.parts:
        raise MigrationError(f"migration target is the repository root: {path}")
    return resolved
