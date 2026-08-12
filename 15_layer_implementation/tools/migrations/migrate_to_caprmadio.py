#!/usr/bin/env python3
"""Rename the complete governed framework identity to CAPRMADIO.

Invocation:
    python migrate_to_caprmadio.py [ROOT]
    python migrate_to_caprmadio.py [ROOT] --apply \
        --expect-plan-digest SHA256
    python migrate_to_caprmadio.py [ROOT] --check

Preview is the default. The tracked inventory comes exclusively from Git's
index. Apply first renames the complete governed and runtime directories so
ignored state is preserved, then transactionally rewrites every tracked path
and text reference. The reviewed digest binds every tracked preimage,
destination, output byte, and permission mode. Collisions, affected binary
content, symlinks, unmerged entries, and partial layouts fail closed.
"""

from __future__ import annotations

import argparse
import os
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path

sys.dont_write_bytecode = True

from dset_migration_tools.models import (
    DeleteOperation,
    MigrationError,
    MigrationPlan,
    WriteOperation,
)
from dset_migration_tools.safety import read_regular_file, sha256, validate_plan
from dset_migration_tools.transaction import apply_transaction

REPOSITORY_ROOT = Path(__file__).resolve().parents[3]
SOURCE_IDENTITY = "CAR" + "MADIO"
TARGET_IDENTITY = "CAPRMADIO"
SOURCE_LOWER = SOURCE_IDENTITY.lower()
TARGET_LOWER = TARGET_IDENTITY.lower()
SOURCE_TITLE = SOURCE_LOWER.title()
TARGET_TITLE = TARGET_LOWER.title()
SOURCE_GOVERNED_DIRECTORY = f".{SOURCE_LOWER}"
SOURCE_RUNTIME_DIRECTORY = f".{SOURCE_LOWER}_runtime"
TARGET_GOVERNED_DIRECTORY = f".{TARGET_LOWER}"
TARGET_RUNTIME_DIRECTORY = f".{TARGET_LOWER}_runtime"
TOP_LEVEL_DIRECTORY_REPLACEMENTS = (
    (SOURCE_RUNTIME_DIRECTORY, TARGET_RUNTIME_DIRECTORY),
    (SOURCE_GOVERNED_DIRECTORY, TARGET_GOVERNED_DIRECTORY),
)
NAME_REPLACEMENTS = (
    (SOURCE_IDENTITY, TARGET_IDENTITY),
    (SOURCE_TITLE, TARGET_TITLE),
    (SOURCE_LOWER, TARGET_LOWER),
)
CONTENT_REPLACEMENTS = tuple(
    (source.encode(), target.encode())
    for source, target in NAME_REPLACEMENTS
)
ALL_CONTENT_REPLACEMENTS = CONTENT_REPLACEMENTS
ALLOWED_FILE_MODES = {"100644": 0o644, "100755": 0o755}
GENERATED_CACHE_DIRECTORIES = {
    "__pycache__",
    ".mypy_cache",
    ".pytest_cache",
    ".ruff_cache",
}


@dataclass(frozen=True)
class TrackedEntry:
    """One stage-zero regular file resolved in the current filesystem."""

    indexed_relative: Path
    current_relative: Path
    mode: str


def git_index(root: Path) -> tuple[tuple[str, Path], ...]:
    """Return deterministic stage-zero tracked paths and Git modes."""
    completed = subprocess.run(
        ["git", "ls-files", "--stage", "-z"],
        cwd=root,
        check=True,
        capture_output=True,
    )
    records: list[tuple[str, Path]] = []
    for raw_record in completed.stdout.split(b"\0"):
        if not raw_record:
            continue
        metadata, raw_path = raw_record.split(b"\t", 1)
        mode, _object_id, stage = metadata.decode("ascii").split()
        if stage != "0":
            raise MigrationError(f"unmerged Git index entry: {raw_path!r}")
        try:
            relative = Path(raw_path.decode("utf-8"))
        except UnicodeDecodeError as error:
            raise MigrationError(f"tracked path is not UTF-8: {raw_path!r}") from error
        records.append((mode, relative))
    return tuple(sorted(records, key=lambda item: item[1].as_posix()))


def replaced_text(value: str) -> str:
    """Replace every admitted case form of the retired identity."""
    for source, target in NAME_REPLACEMENTS:
        value = value.replace(source, target)
    return value


def replaced_path(relative: Path) -> Path:
    """Return the target path for one tracked carrier."""
    return Path(replaced_text(relative.as_posix()))


def candidate_paths(relative: Path) -> tuple[Path, ...]:
    """Return source, root-renamed, and fully migrated path variants."""
    source = relative.as_posix()
    root_renamed = source
    for source_root, target_root in TOP_LEVEL_DIRECTORY_REPLACEMENTS:
        if source == source_root or source.startswith(f"{source_root}/"):
            root_renamed = target_root + source[len(source_root) :]
            break
    return tuple(
        Path(value)
        for value in sorted({source, root_renamed, replaced_text(source)})
    )


def tracked_entries(root: Path) -> tuple[TrackedEntry, ...]:
    """Resolve indexed paths before or after the filesystem cutover."""
    entries: list[TrackedEntry] = []
    desired_owners: dict[Path, Path] = {}
    for mode, indexed_relative in git_index(root):
        desired_relative = replaced_path(indexed_relative)
        existing = tuple(
            candidate
            for candidate in candidate_paths(indexed_relative)
            if (root / candidate).exists()
        )
        if len(existing) > 1:
            raise MigrationError(
                f"multiple migration path variants exist for {indexed_relative}: "
                + ", ".join(item.as_posix() for item in existing)
            )
        if not existing:
            raise MigrationError(
                "tracked source and all expected path variants are missing: "
                f"{indexed_relative} -> {desired_relative}"
            )
        current_relative = existing[0]
        owner = desired_owners.setdefault(desired_relative, indexed_relative)
        if owner != indexed_relative:
            raise MigrationError(
                f"multiple tracked paths map to {desired_relative}: "
                f"{owner}, {indexed_relative}"
            )
        entries.append(TrackedEntry(indexed_relative, current_relative, mode))
    return tuple(entries)


def migrated_content(relative: Path, content: bytes) -> bytes:
    """Rewrite directory references after validating the text boundary."""
    if not any(source in content for source, _target in ALL_CONTENT_REPLACEMENTS):
        return content
    if b"\0" in content:
        raise MigrationError(f"affected tracked file is binary: {relative}")
    try:
        content.decode("utf-8")
    except UnicodeDecodeError as error:
        raise MigrationError(
            f"affected tracked file is not UTF-8: {relative}"
        ) from error
    migrated = content
    for source, target in ALL_CONTENT_REPLACEMENTS:
        migrated = migrated.replace(source, target)
    if any(source in migrated for source, _target in ALL_CONTENT_REPLACEMENTS):
        raise MigrationError(f"retired directory token survived rewrite: {relative}")
    return migrated


def build_plan(root: Path) -> MigrationPlan:
    """Build the complete collision-free tracked-carrier plan."""
    root = root.resolve()
    writes: list[WriteOperation] = []
    deletes: list[DeleteOperation] = []
    for entry in tracked_entries(root):
        current_path = root / entry.current_relative
        desired_relative = replaced_path(entry.indexed_relative)
        desired_path = root / desired_relative
        content = read_regular_file(current_path)
        migrated = migrated_content(entry.current_relative, content)
        path_changes = entry.current_relative != desired_relative
        content_changes = migrated != content
        if not path_changes and not content_changes:
            continue
        if entry.mode not in ALLOWED_FILE_MODES:
            raise MigrationError(
                f"affected tracked file has unsupported mode {entry.mode}: "
                f"{entry.current_relative}"
            )
        writes.append(
            WriteOperation(
                path=desired_path,
                before_sha256=None if path_changes else sha256(content),
                content=migrated,
                reason="replace the retired framework identity",
                mode=ALLOWED_FILE_MODES[entry.mode],
            )
        )
        if path_changes:
            deletes.append(
                DeleteOperation(
                    path=current_path,
                    before_sha256=sha256(content),
                    reason="remove retired repository-directory path",
                )
            )
    plan = MigrationPlan(root, tuple(writes), tuple(deletes))
    validate_plan(plan)
    return plan


def validate_directory_layout(root: Path, allow_source: bool) -> None:
    """Reject ambiguous or partial governed and runtime root layouts."""
    for source_name, target_name in TOP_LEVEL_DIRECTORY_REPLACEMENTS:
        source = root / source_name
        target = root / target_name
        if source.exists() and target.exists():
            raise MigrationError(
                f"both source and target directories exist: {target_name}"
            )
        if source.exists() and not allow_source:
            raise MigrationError(f"retired directory remains: {source_name}")
        selected = source if source.exists() else target
        if not selected.is_dir():
            raise MigrationError(
                f"required repository directory is missing: {target_name}"
            )
        if selected.is_symlink():
            raise MigrationError(
                f"repository directory cannot be a symlink: {selected}"
            )


def rename_source_directories(root: Path) -> tuple[tuple[Path, Path], ...]:
    """Atomically rename complete source directories and return rollback pairs."""
    validate_directory_layout(root, allow_source=True)
    renamed: list[tuple[Path, Path]] = []
    try:
        for source_name, target_name in TOP_LEVEL_DIRECTORY_REPLACEMENTS:
            source = root / source_name
            target = root / target_name
            if not source.exists():
                continue
            os.replace(source, target)
            renamed.append((source, target))
    except OSError as error:
        rollback_directory_renames(renamed)
        raise MigrationError(f"directory rename failed: {error}") from error
    return tuple(renamed)


def rollback_directory_renames(
    renamed: tuple[tuple[Path, Path], ...] | list[tuple[Path, Path]],
) -> None:
    """Restore atomically renamed directories after a tracked migration failure."""
    failures: list[str] = []
    for source, target in reversed(renamed):
        try:
            if source.exists():
                failures.append(f"rollback source already exists: {source}")
            elif not target.exists():
                failures.append(f"rollback target is missing: {target}")
            else:
                os.replace(target, source)
        except OSError as error:
            failures.append(f"{target} -> {source}: {error}")
    if failures:
        raise MigrationError("directory rollback failed: " + "; ".join(failures))


def validate_staged(plan: MigrationPlan, staged: dict[Path, Path]) -> None:
    """Prove staged paths, bytes, and permission modes are migrated."""
    source_tokens = tuple(source for source, _target in NAME_REPLACEMENTS)
    for operation in plan.writes:
        relative = operation.path.relative_to(plan.root)
        if any(source in relative.as_posix() for source in source_tokens):
            raise MigrationError(
                f"retired directory remains in target path: {relative}"
            )
        content = staged[operation.path].read_bytes()
        if any(source in content for source, _target in ALL_CONTENT_REPLACEMENTS):
            raise MigrationError(
                f"retired identity remains in staged file: {relative}"
            )
        expected_mode = operation.mode
        actual_mode = staged[operation.path].stat().st_mode & 0o777
        if expected_mode is not None and actual_mode != expected_mode:
            raise MigrationError(
                f"staged mode mismatch for {relative}: "
                f"expected={oct(expected_mode)}, actual={oct(actual_mode)}"
            )


def verify_complete(root: Path) -> None:
    """Require target directories, zero-operation replay, and zero residue."""
    validate_directory_layout(root, allow_source=False)
    plan = build_plan(root)
    if plan.writes or plan.deletes:
        raise MigrationError(
            f"migration is incomplete: writes={len(plan.writes)}, "
            f"deletes={len(plan.deletes)}"
        )
    source_tokens = tuple(source for source, _target in NAME_REPLACEMENTS)
    for entry in tracked_entries(root):
        current = root / entry.current_relative
        relative_text = entry.current_relative.as_posix()
        if any(source in relative_text for source in source_tokens):
            raise MigrationError(
                f"retired directory remains in path: {entry.current_relative}"
            )
        content = read_regular_file(current)
        if any(source in content for source, _target in ALL_CONTENT_REPLACEMENTS):
            raise MigrationError(
                f"retired directory remains in content: {entry.current_relative}"
            )


def repository_paths(root: Path) -> tuple[Path, ...]:
    """Return deterministic non-Git filesystem paths for residue handling."""
    return tuple(
        sorted(
            (
                path
                for path in root.rglob("*")
                if ".git" not in path.relative_to(root).parts
            ),
            key=lambda path: path.relative_to(root).as_posix(),
        )
    )


def build_residue_plan(root: Path) -> MigrationPlan:
    """Plan safe rewrites of ignored and runtime identity residue."""
    writes: list[WriteOperation] = []
    deletes: list[DeleteOperation] = []
    for path in repository_paths(root):
        if not path.is_file() or path.is_symlink():
            continue
        relative = path.relative_to(root)
        content = path.read_bytes()
        generated_cache = (
            any(part in GENERATED_CACHE_DIRECTORIES for part in relative.parts)
            or path.suffix == ".pyc"
        )
        if generated_cache:
            deletes.append(
                DeleteOperation(
                    path=path,
                    before_sha256=sha256(content),
                    reason="remove generated Python cache during identity cutover",
                )
            )
            continue
        desired_relative = replaced_path(relative)
        desired_path = root / desired_relative
        migrated = migrated_content(relative, content)
        path_changes = desired_relative != relative
        content_changes = migrated != content
        if not path_changes and not content_changes:
            continue
        if path_changes and desired_path.exists():
            if not desired_path.is_file() or desired_path.read_bytes() != migrated:
                raise MigrationError(
                    f"filesystem identity destination collision: {desired_relative}"
                )
        else:
            writes.append(
                WriteOperation(
                    path=desired_path,
                    before_sha256=None if path_changes else sha256(content),
                    content=migrated,
                    reason="replace ignored or runtime identity residue",
                    mode=path.stat().st_mode & 0o777,
                )
            )
        if path_changes:
            deletes.append(
                DeleteOperation(
                    path=path,
                    before_sha256=sha256(content),
                    reason="remove retired ignored or runtime identity path",
                )
            )
    plan = MigrationPlan(root, tuple(writes), tuple(deletes))
    validate_plan(plan)
    return plan


def verify_residue_files(root: Path) -> None:
    """Require zero retired identity in non-Git file paths and bytes."""
    source_tokens = tuple(source.encode() for source, _target in NAME_REPLACEMENTS)
    for path in repository_paths(root):
        relative = path.relative_to(root)
        if path.is_symlink():
            if any(source in relative.as_posix() for source, _ in NAME_REPLACEMENTS):
                raise MigrationError(f"retired identity remains in symlink: {relative}")
            continue
        if not path.is_file():
            continue
        if any(source in relative.as_posix() for source, _ in NAME_REPLACEMENTS):
            raise MigrationError(f"retired identity remains in file path: {relative}")
        content = path.read_bytes()
        if any(source in content for source in source_tokens):
            raise MigrationError(f"retired identity remains in file bytes: {relative}")


def remove_retired_empty_directories(root: Path) -> None:
    """Remove empty generated directory residue beneath retired identities."""
    directories = sorted(
        (path for path in repository_paths(root) if path.is_dir()),
        key=lambda path: len(path.relative_to(root).parts),
        reverse=True,
    )
    for path in directories:
        relative = path.relative_to(root)
        parts = relative.parts
        under_retired_identity = any(
            any(source in part for source, _target in NAME_REPLACEMENTS)
            for part in parts
        )
        generated_cache = any(
            part in GENERATED_CACHE_DIRECTORIES for part in parts
        )
        if under_retired_identity or generated_cache:
            try:
                path.rmdir()
            except OSError as error:
                raise MigrationError(
                    f"retired directory is not empty after migration: {relative}"
                ) from error


def migrate_residue(root: Path) -> None:
    """Transactionally migrate ignored/runtime files and remove empty residue."""
    plan = build_residue_plan(root)
    apply_transaction(plan, validate_staged, verify_residue_files)
    remove_retired_empty_directories(root)
    verify_residue_files(root)
    for path in repository_paths(root):
        relative = path.relative_to(root).as_posix()
        if any(source in relative for source, _target in NAME_REPLACEMENTS):
            raise MigrationError(f"retired identity remains in path: {relative}")


def render_summary(plan: MigrationPlan) -> str:
    """Render a stable reviewable preview."""
    lines = [
        "CAPRMADIO identity migration plan",
        f"root: {plan.root}",
        f"writes: {len(plan.writes)}",
        f"deletes: {len(plan.deletes)}",
        f"plan-digest: {plan.digest()}",
    ]
    lines.extend(
        f"{'CREATE' if item.before_sha256 is None else 'UPDATE'} "
        f"{item.path.relative_to(plan.root).as_posix()}"
        for item in plan.writes
    )
    lines.extend(
        f"DELETE {item.path.relative_to(plan.root).as_posix()}"
        for item in plan.deletes
    )
    return "\n".join(lines)


def arguments() -> argparse.Namespace:
    """Parse preview, apply, and check modes."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", nargs="?", type=Path, default=REPOSITORY_ROOT)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--apply", action="store_true")
    mode.add_argument("--check", action="store_true")
    parser.add_argument("--expect-plan-digest")
    return parser.parse_args()


def main() -> int:
    """Preview, apply, or verify the repository-directory cutover."""
    args = arguments()
    root = args.root.resolve()
    try:
        if args.check:
            verify_complete(root)
            verify_residue_files(root)
            for path in repository_paths(root):
                relative = path.relative_to(root).as_posix()
                if any(source in relative for source, _target in NAME_REPLACEMENTS):
                    raise MigrationError(
                        f"retired identity remains in path: {relative}"
                    )
            print("CAPRMADIO identity migration check: PASS")
            return 0
        validate_directory_layout(root, allow_source=True)
        reviewed_plan = build_plan(root)
        if not args.apply:
            print(render_summary(reviewed_plan))
            return 0
        if not args.expect_plan_digest:
            raise MigrationError("--apply requires --expect-plan-digest")
        if args.expect_plan_digest != reviewed_plan.digest():
            raise MigrationError(
                "plan digest changed: "
                f"expected {args.expect_plan_digest}, actual {reviewed_plan.digest()}"
            )
        renamed = rename_source_directories(root)
        try:
            filesystem_adjusted_plan = build_plan(root)
            apply_transaction(
                filesystem_adjusted_plan,
                validate_staged,
                verify_complete,
            )
        except Exception:
            rollback_directory_renames(renamed)
            raise
        migrate_residue(root)
        print(
            "CAPRMADIO identity migration applied: "
            f"writes={len(reviewed_plan.writes)}, "
            f"deletes={len(reviewed_plan.deletes)}"
        )
        return 0
    except (MigrationError, OSError, subprocess.CalledProcessError) as error:
        print(f"BLOCKED: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
