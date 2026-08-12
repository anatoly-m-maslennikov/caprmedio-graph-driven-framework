#!/usr/bin/env python3
"""Rename public DSET skill IDs to CARMADIO's ``carmadio``/``ca-*`` scheme.

Invocation:
    python migrate_public_skill_ids_to_ca.py [ROOT]
    python migrate_public_skill_ids_to_ca.py [ROOT] --apply \
        --expect-plan-digest SHA256
    python migrate_public_skill_ids_to_ca.py [ROOT] --check

Preview is the default. The migration reads Git's tracked-file index, renames
only registered public skill package directories, replaces specialist IDs only
at token boundaries, and changes the primary ``dset`` ID only in explicit
skill-identity contexts. It intentionally does not rename the ``dset`` CLI,
Python package, runtime package directory, repository, or historical archives.
"""

from __future__ import annotations

import argparse
import os
import re
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
PRIMARY_SOURCE_ID = "dset"
PRIMARY_TARGET_ID = "carmadio"
SPECIALIST_ACTIONS = (
    "clarify",
    "compile",
    "complete",
    "configure",
    "decisions",
    "decompose",
    "diagnose",
    "implement",
    "init",
    "landscape",
    "overview",
    "plan-implementation",
    "plan-proof",
    "prototype",
    "release",
    "repair-governance",
    "triage",
    "verify",
)
SKILL_ID_MAP = {
    PRIMARY_SOURCE_ID: PRIMARY_TARGET_ID,
    **{f"dset-{action}": f"ca-{action}" for action in SPECIALIST_ACTIONS},
}
REGULAR_FILE_MODE = "100644"
SELF_PATH = Path("15_layer_implementation/tools/migrations") / Path(__file__).name

PRIMARY_CONTEXT_REPLACEMENTS = (
    (r"(?<![A-Za-z0-9-])\$dset(?![A-Za-z0-9-])", "$carmadio"),
    (r"(?<![A-Za-z0-9-])--skill dset(?![A-Za-z0-9-])", "--skill carmadio"),
    (r"(?m)^name: dset$", "name: carmadio"),
    (r"skills/dset(?=/|\b)", "skills/carmadio"),
    (r"\[skills\.dset\]", "[skills.carmadio]"),
    (r'"dset": "lifecycle-orchestration"', '"carmadio": "lifecycle-orchestration"'),
    (r'"dset": None', '"carmadio": None'),
    (r'public_entrypoint == "dset"', 'public_entrypoint == "carmadio"'),
    (r'public_entrypoint="dset"', 'public_entrypoint="carmadio"'),
    (r'skill_id="dset"', 'skill_id="carmadio"'),
    (r'entrypoint != "dset"', 'entrypoint != "carmadio"'),
    (
        r'data\.get\("public_entrypoint", "dset"\)',
        'data.get("public_entrypoint", "carmadio")',
    ),
    (r'"lifecycle-orchestration": "dset"', '"lifecycle-orchestration": "carmadio"'),
    (r'skill = "dset"', 'skill = "carmadio"'),
    (r'name == "dset"', 'name == "carmadio"'),
    (r'_skill_text\("dset"\)', '_skill_text("carmadio")'),
    (r'/ "dset" / "SKILL\.md"', '/ "carmadio" / "SKILL.md"'),
    (r'\["dset", "dset-', '["carmadio", "dset-'),
    (r'enum = \["dset",', 'enum = ["carmadio",'),
)


@dataclass(frozen=True)
class TrackedEntry:
    """One supported stage-zero tracked file in its current location."""

    indexed_relative: Path
    current_relative: Path
    mode: str


def git_index(root: Path) -> tuple[tuple[str, Path], ...]:
    """Return deterministic stage-zero tracked paths and modes."""
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


def is_current_surface(relative: Path) -> bool:
    """Return whether a carrier participates in the current skill interface."""
    if relative == SELF_PATH or relative.parts[:1] == ("90_legacy",):
        return False
    if relative.parts[:1] == (".carmadio",):
        return relative == Path(".carmadio/carmadio_settings.toml")
    if relative.name == "bootstrap_bundle.json":
        return False
    return not any(part in {"archive", "_obsolete"} for part in relative.parts)


def replaced_path(relative: Path) -> Path:
    """Rename only a registered package directly below ``skills``."""
    if len(relative.parts) < 2 or relative.parts[0] != "skills":
        return relative
    target = SKILL_ID_MAP.get(relative.parts[1])
    if target is None:
        return relative
    return Path("skills", target, *relative.parts[2:])


def candidate_paths(relative: Path) -> tuple[Path, ...]:
    """Return valid pre- and post-migration filesystem locations."""
    target = replaced_path(relative)
    return (relative,) if target == relative else (relative, target)


def tracked_entries(root: Path) -> tuple[TrackedEntry, ...]:
    """Resolve tracked paths before or after filesystem application."""
    entries: list[TrackedEntry] = []
    desired_owners: dict[Path, Path] = {}
    for mode, indexed_relative in git_index(root):
        desired_relative = replaced_path(indexed_relative)
        existing = tuple(
            candidate
            for candidate in candidate_paths(indexed_relative)
            if (root / candidate).exists()
        )
        if len(existing) != 1:
            raise MigrationError(
                f"expected one path variant for {indexed_relative}, found {existing}"
            )
        owner = desired_owners.setdefault(desired_relative, indexed_relative)
        if owner != indexed_relative:
            raise MigrationError(
                f"multiple tracked paths map to {desired_relative}: "
                f"{owner}, {indexed_relative}"
            )
        entries.append(TrackedEntry(indexed_relative, existing[0], mode))
    return tuple(entries)


def rename_skill_directories(root: Path) -> tuple[tuple[Path, Path], ...]:
    """Atomically rename complete public skill packages before file rewrites."""
    pairs = tuple(
        (root / "skills" / source, root / "skills" / target)
        for source, target in SKILL_ID_MAP.items()
    )
    for source, target in pairs:
        if source.exists() and target.exists():
            raise MigrationError(f"both skill package identities exist: {source}, {target}")
        selected = source if source.exists() else target
        if not selected.is_dir() or selected.is_symlink():
            raise MigrationError(f"skill package is missing or invalid: {selected}")
    renamed: list[tuple[Path, Path]] = []
    try:
        for source, target in pairs:
            if not source.exists():
                continue
            os.replace(source, target)
            renamed.append((source, target))
    except OSError as error:
        rollback_skill_directories(renamed)
        raise MigrationError(f"skill directory rename failed: {error}") from error
    return tuple(renamed)


def rollback_skill_directories(
    renamed: tuple[tuple[Path, Path], ...] | list[tuple[Path, Path]],
) -> None:
    """Restore package directories after a failed content transaction."""
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
        raise MigrationError("skill directory rollback failed: " + "; ".join(failures))


def replace_specialist_ids(text: str) -> str:
    """Replace registered specialist IDs without touching longer DSET names."""
    for source, target in SKILL_ID_MAP.items():
        if source == PRIMARY_SOURCE_ID:
            continue
        pattern = rf"(?<![A-Za-z0-9-]){re.escape(source)}(?![A-Za-z0-9-])"
        text = re.sub(pattern, target, text)
    return text


def replace_wrapper_digests(text: str, digests: dict[str, str]) -> str:
    """Refresh hashes inside governance-registry wrapper blocks."""
    lines = text.splitlines(keepends=True)
    in_wrapper = False
    skill_id: str | None = None
    for index, line in enumerate(lines):
        stripped = line.strip()
        if stripped.startswith("[["):
            in_wrapper = stripped == "[[governance_registry.wrappers]]"
            skill_id = None
            continue
        if not in_wrapper:
            continue
        match = re.fullmatch(r'skill = "([^"]+)"', stripped)
        if match:
            skill_id = match.group(1)
            continue
        if skill_id is None or not stripped.startswith('sha256 = "'):
            continue
        digest = digests.get(skill_id)
        if digest is None:
            raise MigrationError(f"registry names unknown public skill: {skill_id}")
        newline = "\n" if line.endswith("\n") else ""
        lines[index] = f'sha256 = "{digest}"{newline}'
    return "".join(lines)


def migrated_content(
    relative: Path,
    content: bytes,
    skill_digests: dict[str, str] | None = None,
) -> bytes:
    """Return one current carrier with only governed skill identities changed."""
    if not is_current_surface(relative):
        return content
    if b"\0" in content:
        return content
    try:
        text = content.decode("utf-8")
    except UnicodeDecodeError:
        return content
    migrated = replace_specialist_ids(text)
    for pattern, replacement in PRIMARY_CONTEXT_REPLACEMENTS:
        migrated = re.sub(pattern, replacement, migrated)
    if relative.parts[:1] == ("skills",):
        migrated = migrated.replace("DSET", "CARMADIO")
        if relative == Path("skills/README.md"):
            migrated = re.sub(r"(?<![A-Za-z0-9-])`dset`", "`carmadio`", migrated)
            migrated = migrated.replace("(dset/SKILL.md)", "(carmadio/SKILL.md)")
        if relative == Path("skills/host-distribution.md"):
            migrated = migrated.replace(
                "exact 19-skill catalog: `dset`,",
                "exact 19-skill catalog: `carmadio`,",
            )
    if skill_digests is not None:
        migrated = replace_wrapper_digests(migrated, skill_digests)
    return migrated.encode("utf-8")


def target_skill_digests(root: Path) -> dict[str, str]:
    """Compute post-migration source digests for every public SKILL carrier."""
    digests: dict[str, str] = {}
    for entry in tracked_entries(root):
        desired = replaced_path(entry.indexed_relative)
        if (
            len(desired.parts) != 3
            or desired.parts[0] != "skills"
            or desired.name != "SKILL.md"
        ):
            continue
        content = read_regular_file(root / entry.current_relative)
        migrated = migrated_content(entry.current_relative, content)
        digests[desired.parts[1]] = sha256(migrated)
    expected = set(SKILL_ID_MAP.values())
    if set(digests) != expected:
        raise MigrationError(
            f"public SKILL digest set differs: expected={sorted(expected)}, "
            f"actual={sorted(digests)}"
        )
    return digests


def build_plan(root: Path) -> MigrationPlan:
    """Build the collision-free migration plan without mutation."""
    writes: list[WriteOperation] = []
    deletes: list[DeleteOperation] = []
    skill_digests = target_skill_digests(root)
    for entry in tracked_entries(root):
        current_path = root / entry.current_relative
        desired_relative = replaced_path(entry.indexed_relative)
        desired_path = root / desired_relative
        content = read_regular_file(current_path)
        migrated = migrated_content(
            entry.current_relative,
            content,
            skill_digests,
        )
        path_changes = entry.current_relative != desired_relative
        if not path_changes and migrated == content:
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
                reason="rename governed public skill identity",
            )
        )
        if path_changes:
            deletes.append(
                DeleteOperation(
                    path=current_path,
                    before_sha256=sha256(content),
                    reason="remove retired public skill package path",
                )
            )
    plan = MigrationPlan(root, tuple(writes), tuple(deletes))
    validate_plan(plan)
    return plan


def validate_staged(plan: MigrationPlan, staged: dict[Path, Path]) -> None:
    """Prove staged public package identities match their target folders."""
    for operation in plan.writes:
        relative = operation.path.relative_to(plan.root)
        if relative.parts[:1] != ("skills",) or len(relative.parts) < 2:
            continue
        if relative.parts[1] in SKILL_ID_MAP:
            raise MigrationError(f"retired skill package path remains: {relative}")
        if relative.name == "SKILL.md":
            expected = relative.parts[1]
            text = staged[operation.path].read_text(encoding="utf-8")
            if f"name: {expected}\n" not in text:
                raise MigrationError(f"skill name/path mismatch: {relative}")


def verify_complete(root: Path) -> None:
    """Require an idempotent replay and no retired current skill packages."""
    plan = build_plan(root)
    if plan.writes or plan.deletes:
        raise MigrationError(
            f"migration incomplete: writes={len(plan.writes)}, "
            f"deletes={len(plan.deletes)}"
        )
    actual = {
        path.parent.name
        for path in (root / "skills").glob("*/SKILL.md")
        if path.is_file()
    }
    expected = set(SKILL_ID_MAP.values())
    if actual != expected:
        raise MigrationError(
            f"public skill packages differ: expected={sorted(expected)}, "
            f"actual={sorted(actual)}"
        )


def render_summary(plan: MigrationPlan) -> str:
    """Render a stable reviewable preview."""
    lines = [
        "CARMADIO public-skill migration plan",
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
    """Preview, apply, or verify the public skill identity cutover."""
    args = arguments()
    root = args.root.resolve()
    try:
        if args.check:
            verify_complete(root)
            print("public-skill migration check: PASS")
            return 0
        plan = build_plan(root)
        if not args.apply:
            print(render_summary(plan))
            return 0
        if not args.expect_plan_digest:
            raise MigrationError("--apply requires --expect-plan-digest")
        if args.expect_plan_digest != plan.digest():
            raise MigrationError(
                f"plan digest changed: expected {args.expect_plan_digest}, "
                f"actual {plan.digest()}"
            )
        renamed = rename_skill_directories(root)
        try:
            filesystem_adjusted_plan = build_plan(root)
            apply_transaction(
                filesystem_adjusted_plan,
                validate_staged,
                verify_complete,
            )
        except Exception:
            rollback_skill_directories(renamed)
            raise
        print(
            "public-skill migration applied: "
            f"writes={len(plan.writes)}, deletes={len(plan.deletes)}"
        )
        return 0
    except (MigrationError, OSError, subprocess.CalledProcessError) as error:
        print(f"BLOCKED: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
