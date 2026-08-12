#!/usr/bin/env python3
"""Replace the retired project identity prefix in every tracked text carrier.

Invocation:
    python migrate_identity_prefix_to_carmadio.py [ROOT]
    python migrate_identity_prefix_to_carmadio.py [ROOT] --apply \
        --expect-plan-digest SHA256
    python migrate_identity_prefix_to_carmadio.py [ROOT] --check

Preview is the default. The migration inventory comes exclusively from Git's
tracked-file index, rejects non-regular or non-UTF-8 affected files, proves
destination uniqueness, binds the exact preimage and output bytes in a plan
digest, stages the complete result, applies it transactionally, verifies zero
residual source-prefix tokens in tracked paths and content, and rolls back on
failure. A second preview is a zero-operation result even before the caller
stages renamed paths in Git.
"""

from __future__ import annotations

import argparse
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
SOURCE_PREFIX = "DSET" + "-"
TARGET_PREFIX = "CARMADIO-"
SOURCE_BYTES = SOURCE_PREFIX.encode()
TARGET_BYTES = TARGET_PREFIX.encode()
REGULAR_FILE_MODE = "100644"


@dataclass(frozen=True)
class TrackedEntry:
    """One stage-zero regular file from the Git index."""

    indexed_relative: Path
    current_relative: Path
    mode: str


def git_index(root: Path) -> tuple[tuple[str, Path], ...]:
    """Return deterministic stage-zero tracked paths and their Git modes."""
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


def replaced_path(relative: Path) -> Path:
    """Return the exact target path for one tracked identity carrier."""
    return Path(relative.as_posix().replace(SOURCE_PREFIX, TARGET_PREFIX))


def tracked_entries(root: Path) -> tuple[TrackedEntry, ...]:
    """Resolve indexed pre-cutover paths before or after filesystem apply."""
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
                f"identity-prefix destination already exists: {desired_relative}"
            )
        elif indexed_exists:
            current_relative = indexed_relative
        elif desired_exists:
            current_relative = desired_relative
        else:
            raise MigrationError(
                f"tracked source and expected destination are missing: "
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
    """Replace the exact identity prefix after validating the text boundary."""
    if SOURCE_BYTES not in content:
        return content
    if b"\0" in content:
        raise MigrationError(f"affected tracked file is binary: {relative}")
    try:
        content.decode("utf-8")
    except UnicodeDecodeError as error:
        raise MigrationError(f"affected tracked file is not UTF-8: {relative}") from error
    migrated = content.replace(SOURCE_BYTES, TARGET_BYTES)
    if SOURCE_BYTES in migrated:
        raise MigrationError(f"source prefix survived rewrite: {relative}")
    return migrated


def build_plan(root: Path) -> MigrationPlan:
    """Build a complete collision-free prefix migration plan without mutation."""
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
                reason="replace retired identity prefix in path and/or content",
            )
        )
        if path_changes:
            deletes.append(
                DeleteOperation(
                    path=current_path,
                    before_sha256=sha256(content),
                    reason="remove retired identity-prefix path after replacement",
                )
            )
    plan = MigrationPlan(root, tuple(writes), tuple(deletes))
    validate_plan(plan)
    return plan


def validate_staged(plan: MigrationPlan, staged: dict[Path, Path]) -> None:
    """Prove every staged output uses only the target prefix."""
    for operation in plan.writes:
        relative = operation.path.relative_to(plan.root)
        if SOURCE_PREFIX in relative.as_posix():
            raise MigrationError(f"source prefix remains in target path: {relative}")
        content = staged[operation.path].read_bytes()
        if SOURCE_BYTES in content:
            raise MigrationError(f"source prefix remains in staged file: {relative}")
        try:
            content.decode("utf-8")
        except UnicodeDecodeError as error:
            raise MigrationError(f"staged file is not UTF-8: {relative}") from error


def verify_complete(root: Path) -> None:
    """Require a zero-operation replay and no tracked source-prefix residue."""
    plan = build_plan(root)
    if plan.writes or plan.deletes:
        raise MigrationError(
            f"migration is incomplete: writes={len(plan.writes)}, "
            f"deletes={len(plan.deletes)}"
        )
    for entry in tracked_entries(root):
        current = root / entry.current_relative
        if SOURCE_PREFIX in entry.current_relative.as_posix():
            raise MigrationError(
                f"source prefix remains in tracked path: {entry.current_relative}"
            )
        if SOURCE_BYTES in read_regular_file(current):
            raise MigrationError(
                f"source prefix remains in tracked content: {entry.current_relative}"
            )


def render_summary(plan: MigrationPlan) -> str:
    """Render a stable reviewable preview for this bounded recipe."""
    lines = [
        "Identity-prefix migration plan",
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
    """Parse the bounded preview/apply/check interface."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", nargs="?", type=Path, default=REPOSITORY_ROOT)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--apply", action="store_true")
    mode.add_argument("--check", action="store_true")
    parser.add_argument("--expect-plan-digest")
    return parser.parse_args()


def main() -> int:
    """Preview, apply, or verify the exact repository identity cutover."""
    args = arguments()
    root = args.root.resolve()
    try:
        if args.check:
            verify_complete(root)
            print("identity-prefix migration check: PASS")
            return 0
        plan = build_plan(root)
        if not args.apply:
            print(render_summary(plan))
            return 0
        if not args.expect_plan_digest:
            raise MigrationError("--apply requires --expect-plan-digest")
        if args.expect_plan_digest != plan.digest():
            raise MigrationError(
                "plan digest changed: "
                f"expected {args.expect_plan_digest}, actual {plan.digest()}"
            )
        apply_transaction(plan, validate_staged, verify_complete)
        print(
            "identity-prefix migration applied: "
            f"writes={len(plan.writes)}, deletes={len(plan.deletes)}"
        )
        return 0
    except (MigrationError, OSError, subprocess.CalledProcessError) as error:
        print(f"BLOCKED: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
