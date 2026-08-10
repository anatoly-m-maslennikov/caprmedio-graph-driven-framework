"""Transactional staging, replacement, rollback, and cleanup for migrations."""

from __future__ import annotations

import os
from collections.abc import Callable
from contextlib import suppress
from pathlib import Path

from .models import MigrationError, MigrationPlan
from .safety import assert_preimages, sha256

StagedValidator = Callable[[MigrationPlan, dict[Path, Path]], None]


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


def _capture_originals(plan: MigrationPlan) -> dict[Path, bytes | None]:
    originals = {
        item.path: item.path.read_bytes() if item.path.exists() else None
        for item in plan.writes
    }
    originals.update({item.path: item.path.read_bytes() for item in plan.deletes})
    return originals


def _create_staging_root(root: Path) -> Path:
    runtime_root = root / ".carmadio_runtime" / "migrations"
    runtime_root.mkdir(parents=True, exist_ok=True)
    staging_root = runtime_root / f"dset-meta-gov-carriers-{os.getpid()}"
    staging_root.mkdir()
    return staging_root


def _stage_writes(plan: MigrationPlan, root: Path) -> dict[Path, Path]:
    staged: dict[Path, Path] = {}
    for index, operation in enumerate(plan.writes):
        path = root / f"{index:04d}.stage"
        path.write_bytes(operation.content)
        _validate_staged(path, operation.path, operation.content)
        staged[operation.path] = path
    return staged


def _validate_staged(staged: Path, target: Path, content: bytes) -> None:
    if sha256(staged.read_bytes()) != sha256(content):
        raise MigrationError(f"staging digest mismatch: {target}")
    if os.stat(staged).st_dev != os.stat(target.parent).st_dev:
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
    error: Exception, originals: dict[Path, bytes | None]
) -> MigrationError:
    failures = _restore_originals(originals)
    suffix = (
        f"; rollback failures: {'; '.join(failures)}"
        if failures
        else "; all touched files rolled back"
    )
    return MigrationError(f"migration failed: {error}{suffix}")


def _restore_originals(originals: dict[Path, bytes | None]) -> list[str]:
    failures: list[str] = []
    for path, content in reversed(tuple(originals.items())):
        try:
            if content is None:
                path.unlink(missing_ok=True)
            else:
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_bytes(content)
        except OSError as error:
            failures.append(f"{path}: {error}")
    return failures


def _cleanup_staging(root: Path) -> None:
    for path in root.glob("*"):
        path.unlink()
    root.rmdir()
    with suppress(OSError):
        root.parent.rmdir()
