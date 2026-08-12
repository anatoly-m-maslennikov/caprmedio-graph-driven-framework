#!/usr/bin/env python3
"""Flatten the applied Implementation layer without changing carrier bytes.

Preview is the default. ``--apply`` moves every regular file below
``.carmadio/105_layer_implementation`` to that directory's root after first
validating the complete plan. ``--check`` exits successfully only when the
layer is already flat. Destination-name collisions and non-regular carriers
fail closed, so the operation is deterministic, collision-safe, and
idempotent.
"""

from __future__ import annotations

import argparse
import sys
from dataclasses import dataclass
from pathlib import Path

LAYER_ROOT = Path(".carmadio/105_layer_implementation")


class FlattenError(RuntimeError):
    """The applied Implementation layer cannot be flattened safely."""


@dataclass(frozen=True)
class Move:
    """One path-only carrier move."""

    source: Path
    target: Path


def plan(root: Path = LAYER_ROOT) -> tuple[Move, ...]:
    """Return the complete deterministic plan or raise before mutating state."""

    if not root.is_dir():
        raise FlattenError(f"applied Implementation layer is missing: {root}")
    moves: list[Move] = []
    targets: set[Path] = set()
    for source in sorted(root.rglob("*"), key=lambda path: path.as_posix()):
        if source.is_symlink():
            raise FlattenError(f"carrier is not a regular file: {source}")
        if source.parent == root or source.is_dir():
            continue
        if not source.is_file():
            raise FlattenError(f"carrier is not a regular file: {source}")
        target = root / source.name
        if target.exists() or target in targets:
            raise FlattenError(f"destination collision: {target}")
        targets.add(target)
        moves.append(Move(source, target))
    return tuple(moves)


def apply(moves: tuple[Move, ...], root: Path = LAYER_ROOT) -> None:
    """Publish a previously validated move plan and remove empty directories."""

    for move in moves:
        move.source.replace(move.target)
    for directory in sorted(
        (path for path in root.rglob("*") if path.is_dir()),
        key=lambda path: len(path.parts),
        reverse=True,
    ):
        directory.rmdir()


def has_subdirectories(root: Path = LAYER_ROOT) -> bool:
    """Return whether the layer still contains any nested directory."""

    return any(path.is_dir() for path in root.iterdir())


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--apply", action="store_true", help="publish the move plan")
    mode.add_argument(
        "--check",
        action="store_true",
        help="require an already-flat layer",
    )
    args = parser.parse_args()
    try:
        moves = plan()
        if args.check:
            if moves or has_subdirectories():
                print(f"not current: {len(moves)} carrier(s) remain below {LAYER_ROOT}")
                return 1
            print(f"current: {LAYER_ROOT} is flat")
            return 0
        if args.apply:
            apply(moves)
            print(f"applied: moved {len(moves)} carrier(s)")
            return 0
        for move in moves:
            print(f"{move.source} -> {move.target}")
        print(f"planned: {len(moves)} carrier(s)")
        return 0
    except FlattenError as error:
        print(f"error: {error}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
