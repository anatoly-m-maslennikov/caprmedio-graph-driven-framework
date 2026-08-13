#!/usr/bin/env python3
"""Materialize the CAPRMADIO framework root-entry symlink farm.

The default mode is a read-only plan.  ``--apply`` performs the guarded
migration and is safe to run repeatedly.
"""

from __future__ import annotations

import argparse
import os
import shutil
import subprocess
import tempfile
from pathlib import Path


OLD = "000_CAPRMADIO_METHODOLOGY"
NEW = "000_caprmadio_framework"
TOKEN = OLD
PROJECT_DELIVERY_NAMES = {"50_versions", "changelog", "releases", "versions"}


def git(root: Path, *args: str) -> list[str]:
    out = subprocess.check_output(["git", "-C", str(root), *args])
    return out.decode("utf-8", "surrogateescape").splitlines()


def tracked_files(root: Path) -> list[Path]:
    return [root / p for p in git(root, "ls-files")]


def is_project_delivery_entry(name: str) -> bool:
    normalized = name.lower()
    stem = normalized.rsplit(".", 1)[0]
    return normalized in PROJECT_DELIVERY_NAMES or stem in PROJECT_DELIVERY_NAMES


def top_level_entries(root: Path, files: list[Path]) -> list[str]:
    names = {p.relative_to(root).parts[0] for p in files if p.relative_to(root).parts}
    return sorted(
        name
        for name in names
        if not name.startswith(".")
        and not is_project_delivery_entry(name)
        and (root / name).exists()
        and not (root / name).is_symlink()
    )


def remove_path(path: Path) -> None:
    if path.is_symlink() or path.is_file():
        path.unlink()
    elif path.is_dir():
        shutil.rmtree(path)


def retired_tree_guard(root: Path) -> None:
    retired_relative = f".caprmadio/{OLD}"
    if subprocess.run(
        ["git", "-C", str(root), "diff", "--quiet", "--", retired_relative]
    ).returncode != 0:
        raise SystemExit("refusing --apply: retired tree differs from the index")
    if subprocess.run(
        ["git", "-C", str(root), "diff", "--cached", "--quiet", "--", retired_relative]
    ).returncode != 0:
        raise SystemExit("refusing --apply: retired tree has staged changes")
    status = git(
        root, "status", "--porcelain=v1", "--untracked-files=all", "--", retired_relative
    )
    extras = [
        line[3:]
        for line in status
        if line.startswith("??") and Path(line[3:]).name != ".DS_Store"
    ]
    if extras:
        raise SystemExit("refusing --apply: retired tree has untracked entries: " + ", ".join(extras))


def atomic_replace(path: Path, data: bytes) -> None:
    with tempfile.NamedTemporaryFile(dir=path.parent, prefix=f".{path.name}.", delete=False) as tmp:
        tmp.write(data)
        temp_name = tmp.name
    os.replace(temp_name, path)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", type=Path, help="repository root")
    parser.add_argument("--apply", action="store_true", help="perform the migration")
    args = parser.parse_args()
    root = args.root.resolve()
    files = tracked_files(root)
    entries = top_level_entries(root, files)
    base = root / ".caprmadio"
    farm = base / NEW
    retired = base / OLD

    replacements = []
    for path in files:
        if not path.exists():
            continue
        try:
            rel = path.relative_to(retired)
        except ValueError:
            rel = None
        if rel is not None:
            continue
        if path.is_symlink():
            continue
        data = path.read_bytes()
        if TOKEN.encode() in data:
            try:
                data.decode("utf-8")
            except UnicodeDecodeError:
                continue
            replacements.append(path)

    planned = []
    if retired.exists() or retired.is_symlink():
        planned.append(f"delete {retired.relative_to(root)}")
    existing = set(p.name for p in farm.iterdir()) if farm.is_dir() and not farm.is_symlink() else set()
    for name in sorted(existing - set(entries)):
        planned.append(f"remove {farm.relative_to(root) / name}")
    for name in entries:
        target = f"../../{name}"
        if not (farm / name).is_symlink() or os.readlink(farm / name) != target:
            planned.append(f"link {farm.relative_to(root) / name} -> {target}")
    planned.extend(f"replace {p.relative_to(root)}" for p in replacements)

    if not args.apply:
        print("no changes" if not planned else "\n".join(planned))
        return 0

    if retired.exists() or retired.is_symlink():
        retired_tree_guard(root)
    base.mkdir(exist_ok=True)
    if retired.exists() or retired.is_symlink():
        remove_path(retired)
    if farm.is_symlink() or farm.is_file():
        remove_path(farm)
    farm.mkdir(parents=True, exist_ok=True)
    for child in list(farm.iterdir()):
        if child.name not in entries:
            remove_path(child)
    for name in entries:
        child = farm / name
        target = f"../../{name}"
        if child.is_symlink() and os.readlink(child) == target:
            continue
        if child.exists() or child.is_symlink():
            remove_path(child)
        child.symlink_to(target, target_is_directory=(root / name).is_dir())
    for path in replacements:
        data = path.read_bytes().decode("utf-8").replace(TOKEN, NEW).encode("utf-8")
        atomic_replace(path, data)
    print("no changes" if not planned else "applied migration")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
