#!/usr/bin/env python3
"""Rename the governed and runtime repository directories to CARMADIO.

Invocation:
    python migrate_repository_directories_to_carmadio.py [ROOT]
    python migrate_repository_directories_to_carmadio.py [ROOT] --apply \
        --expect-plan-digest SHA256
    python migrate_repository_directories_to_carmadio.py [ROOT] --check

Preview is the default. The tracked inventory comes exclusively from Git's
index. Apply first renames each complete top-level directory atomically so
ignored runtime state is preserved, then transactionally rewrites tracked text
references. The reviewed plan digest binds every tracked preimage, destination,
and output byte. Collisions, binary affected carriers, symlinks, unmerged index
entries, and partial layouts fail closed.
"""

from __future__ import annotations

import argparse
import os
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path

from dset_migration_tools.models import (
    DeleteOperation,
    MigrationError,
    MigrationPlan,
    WriteOperation,
)
from dset_migration_tools.safety import read_regular_file, sha256, validate_plan
from dset_migration_tools.transaction import apply_transaction

sys.dont_write_bytecode = True

REPOSITORY_ROOT = Path(__file__).resolve().parents[3]
SOURCE_GOVERNED_DIRECTORY = "." + "dset"
SOURCE_RUNTIME_DIRECTORY = SOURCE_GOVERNED_DIRECTORY + "_runtime"
TARGET_GOVERNED_DIRECTORY = ".carmadio"
TARGET_RUNTIME_DIRECTORY = ".carmadio_runtime"
DIRECTORY_REPLACEMENTS = (
    (SOURCE_RUNTIME_DIRECTORY, TARGET_RUNTIME_DIRECTORY),
    (SOURCE_GOVERNED_DIRECTORY, TARGET_GOVERNED_DIRECTORY),
)
CONTENT_REPLACEMENTS = tuple(
    (source.encode(), target.encode())
    for source, target in DIRECTORY_REPLACEMENTS
)
IDENTIFIER_REPLACEMENTS = (
    (("dset" + "_root").encode(), b"carmadio_root"),
)
ALL_CONTENT_REPLACEMENTS = CONTENT_REPLACEMENTS + IDENTIFIER_REPLACEMENTS
REGULAR_FILE_MODE = "100644"


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
    """Replace exact retired directory tokens, longest token first."""
    for source, target in DIRECTORY_REPLACEMENTS:
        value = value.replace(source, target)
    return value


def replaced_path(relative: Path) -> Path:
    """Return the target path for one tracked carrier."""
    return Path(replaced_text(relative.as_posix()))


def tracked_entries(root: Path) -> tuple[TrackedEntry, ...]:
    """Resolve indexed paths before or after the filesystem cutover."""
    entries: list[TrackedEntry] = []
    desired_owners: dict[Path, Path] = {}
    for mode, indexed_relative in git_index(root):
        desired_relative = replaced_path(indexed_relative)
        indexed_path = root / indexed_relative
        desired_path = root / desired_relative
        indexed_exists = indexed_path.exists()
        desired_exists = desired_path.exists()
        if indexed_relative == desired_relative:
            if not indexed_exists:
                raise MigrationError(f"tracked file is missing: {indexed_relative}")
            current_relative = indexed_relative
        elif indexed_exists and desired_exists:
            raise MigrationError(
                f"directory migration destination already exists: {desired_relative}"
            )
        elif indexed_exists:
            current_relative = indexed_relative
        elif desired_exists:
            current_relative = desired_relative
        else:
            raise MigrationError(
                "tracked source and expected destination are missing: "
                f"{indexed_relative} -> {desired_relative}"
            )
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
        if entry.mode != REGULAR_FILE_MODE:
            raise MigrationError(
                f"affected tracked file has unsupported mode {entry.mode}: "
                f"{entry.current_relative}"
            )
        writes.append(
            WriteOperation(
                path=desired_path,
                before_sha256=None if path_changes else sha256(content),
                content=migrated,
                reason="rename governed repository directories and references",
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
    """Reject ambiguous or partial top-level directory layouts."""
    for source_name, target_name in DIRECTORY_REPLACEMENTS:
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
        for source_name, target_name in DIRECTORY_REPLACEMENTS:
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
    """Prove staged paths and text contain no retired directory identity."""
    source_tokens = tuple(source for source, _target in DIRECTORY_REPLACEMENTS)
    for operation in plan.writes:
        relative = operation.path.relative_to(plan.root)
        if any(source in relative.as_posix() for source in source_tokens):
            raise MigrationError(
                f"retired directory remains in target path: {relative}"
            )
        content = staged[operation.path].read_bytes()
        if any(source in content for source, _target in ALL_CONTENT_REPLACEMENTS):
            raise MigrationError(
                f"retired directory remains in staged file: {relative}"
            )
        try:
            content.decode("utf-8")
        except UnicodeDecodeError as error:
            raise MigrationError(f"staged file is not UTF-8: {relative}") from error


def verify_complete(root: Path) -> None:
    """Require target directories, zero-operation replay, and zero residue."""
    validate_directory_layout(root, allow_source=False)
    plan = build_plan(root)
    if plan.writes or plan.deletes:
        raise MigrationError(
            f"migration is incomplete: writes={len(plan.writes)}, "
            f"deletes={len(plan.deletes)}"
        )
    source_tokens = tuple(source for source, _target in DIRECTORY_REPLACEMENTS)
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


def render_summary(plan: MigrationPlan) -> str:
    """Render a stable reviewable preview."""
    lines = [
        "CARMADIO repository-directory migration plan",
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
            print("repository-directory migration check: PASS")
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
        print(
            "repository-directory migration applied: "
            f"writes={len(reviewed_plan.writes)}, "
            f"deletes={len(reviewed_plan.deletes)}"
        )
        return 0
    except (MigrationError, OSError, subprocess.CalledProcessError) as error:
        print(f"BLOCKED: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
