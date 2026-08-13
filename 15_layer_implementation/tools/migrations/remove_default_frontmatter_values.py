#!/usr/bin/env python3
"""Remove the default ``tier: standard`` entry from Markdown frontmatter.

By default this is a dry run.  Use ``--apply`` to replace files atomically.
Only an exact, top-level frontmatter line is eligible; body text is untouched.
"""

from __future__ import annotations

import argparse
import os
import re
import sys
import tempfile
from pathlib import Path


_CANDIDATE = b"tier: standard"
_TIER_KEY = re.compile(rb"^tier\s*:")


def _line_text(line: bytes) -> bytes:
    return line[:-2] if line.endswith(b"\r\n") else line[:-1] if line.endswith((b"\n", b"\r")) else line


def _transform(path: Path) -> tuple[bytes, bool]:
    original = path.read_bytes()
    lines = original.splitlines(keepends=True)
    if not lines or _line_text(lines[0]) != b"---":
        return original, False

    end = None
    for index in range(1, len(lines)):
        if _line_text(lines[index]) == b"---":
            end = index
            break

    if end is None:
        if any(_line_text(line) == _CANDIDATE for line in lines[1:]):
            raise ValueError("unterminated leading frontmatter")
        return original, False

    tier_indexes = [
        index for index, line in enumerate(lines[1:end], start=1) if _TIER_KEY.match(_line_text(line))
    ]
    if len(tier_indexes) > 1:
        raise ValueError("duplicate top-level tier keys")

    candidate_indexes = [
        index for index in tier_indexes if _line_text(lines[index]) == _CANDIDATE
    ]
    if not candidate_indexes:
        return original, False
    remove = set(candidate_indexes)
    return b"".join(line for index, line in enumerate(lines) if index not in remove), True


def _markdown_files(root: Path):
    for path in sorted(root.rglob("*.md")):
        if ".git" in path.parts or ".caprmadio_runtime" in path.parts:
            continue
        if path.is_file():
            yield path


def _atomic_write(path: Path, data: bytes) -> None:
    mode = path.stat().st_mode & 0o7777
    fd, name = tempfile.mkstemp(prefix=f".{path.name}.", dir=path.parent)
    try:
        with os.fdopen(fd, "wb") as handle:
            handle.write(data)
            handle.flush()
            os.fsync(handle.fileno())
        os.chmod(name, mode)
        os.replace(name, path)
    except Exception:
        try:
            os.unlink(name)
        except FileNotFoundError:
            pass
        raise


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", type=Path, help="root directory to scan recursively")
    parser.add_argument("--apply", action="store_true", help="apply changes atomically")
    args = parser.parse_args(argv)
    if not args.root.is_dir():
        parser.error(f"ROOT is not a directory: {args.root}")

    candidates: list[tuple[Path, bytes]] = []
    try:
        for path in _markdown_files(args.root):
            transformed, changed = _transform(path)
            if changed:
                candidates.append((path, transformed))
    except ValueError as error:
        print(f"error: {path}: {error}", file=sys.stderr)
        return 2

    print(f"Candidates: {len(candidates)}")
    for path, _ in candidates:
        print(path)
    if args.apply:
        for path, transformed in candidates:
            _atomic_write(path, transformed)
        print(f"Applied: {len(candidates)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
