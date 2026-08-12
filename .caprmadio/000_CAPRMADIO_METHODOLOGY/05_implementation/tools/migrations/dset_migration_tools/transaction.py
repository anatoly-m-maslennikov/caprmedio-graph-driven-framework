"""Transactional staging, replacement, rollback, and cleanup for migrations."""

from __future__ import annotations

import os
from collections.abc import Callable
from contextlib import suppress
from pathlib import Path

from .models import MigrationError, MigrationPlan
from .safety import assert_preimages, sha256

StagedValidator = Callable[[MigrationPlan, dict[Path, Path]], None]
OriginalState = tuple[bytes | None, int | None]


def apply_transaction(
    plan: MigrationPlan,
    validate_staged: StagedValidator,
    verify: Callable[[Path], None],
) -> None:
    """Stage, apply, verify, and roll back a complete plan on any failure."""
    assert_preimages(plan)
    originals = _capture_originals(plan)
    staging_root = _create_staging_root(plan.root)
    try:
        staged = _stage_writes(plan, staging_root)
        validate_staged(plan, staged)
        _replace_and_verify(plan, staged, verify)
    except Exception as error:
        raise _rollback_error(error, originals) from error
    finally:
        _cleanup_staging(staging_root)


def _capture_originals(plan: MigrationPlan) -> dict[Path, OriginalState]:
    originals = {item.path: _read_original(item.path) for item in plan.writes}
    originals.update({item.path: _read_original(item.path) for item in plan.deletes})
    return originals


def _read_original(path: Path) -> OriginalState:
    """Capture bytes and permission bits for exact rollback."""
    if not path.exists():
        return None, None
    return path.read_bytes(), path.stat().st_mode & 0o777


def _create_staging_root(root: Path) -> Path:
    current_runtime = (
        ".caprmadio_runtime"
        if (root / ".caprmadio_runtime").exists()
        else ".caprmadio_runtime"
    )
    runtime_root = root / current_runtime / "migrations"
    runtime_root.mkdir(parents=True, exist_ok=True)
    staging_root = runtime_root / f"dset-meta-gov-carriers-{os.getpid()}"
    staging_root.mkdir()
    return staging_root


def _stage_writes(plan: MigrationPlan, root: Path) -> dict[Path, Path]:
    staged: dict[Path, Path] = {}
    for index, operation in enumerate(plan.writes):
        path = root / f"{index:04d}.stage"
        path.write_bytes(operation.content)
        if operation.mode is not None:
            path.chmod(operation.mode)
        _validate_staged(path, operation.path, operation.content)
        staged[operation.path] = path
    return staged


def _validate_staged(staged: Path, target: Path, content: bytes) -> None:
    if sha256(staged.read_bytes()) != sha256(content):
        raise MigrationError(f"staging digest mismatch: {target}")
    target_ancestor = target.parent
    while not target_ancestor.exists():
        target_ancestor = target_ancestor.parent
    if os.stat(staged).st_dev != os.stat(target_ancestor).st_dev:
        raise MigrationError(
            f"migration staging and target are on different filesystems: {target}"
        )


def _replace_and_verify(
    plan: MigrationPlan, staged: dict[Path, Path], verify: Callable[[Path], None]
) -> None:
    for operation in plan.writes:
        operation.path.parent.mkdir(parents=True, exist_ok=True)
        os.replace(staged[operation.path], operation.path)
    for operation in plan.deletes:
        operation.path.unlink()
    verify(plan.root)


def _rollback_error(
    error: Exception, originals: dict[Path, OriginalState]
) -> MigrationError:
    failures = _restore_originals(originals)
    suffix = (
        f"; rollback failures: {'; '.join(failures)}"
        if failures
        else "; all touched files rolled back"
    )
    return MigrationError(f"migration failed: {error}{suffix}")


def _restore_originals(originals: dict[Path, OriginalState]) -> list[str]:
    failures: list[str] = []
    for path, (content, mode) in reversed(tuple(originals.items())):
        try:
            if content is None:
                path.unlink(missing_ok=True)
            else:
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_bytes(content)
                if mode is not None:
                    path.chmod(mode)
        except OSError as error:
            failures.append(f"{path}: {error}")
    return failures


def _cleanup_staging(root: Path) -> None:
    for path in root.glob("*"):
        path.unlink()
    root.rmdir()
    with suppress(OSError):
        root.parent.rmdir()
