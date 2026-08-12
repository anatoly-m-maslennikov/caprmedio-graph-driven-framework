#!/usr/bin/env python3
"""Synchronize reusable root methodology into the installed CARMADIO copy.

Usage:
    python scripts/sync_carmadio.py [ROOT]
    python scripts/sync_carmadio.py [ROOT] --apply

Preview is the default. ``--apply`` performs the one-way root-to-installed
copy and verifies that no methodology drift remains. The installed copy is
never used as a source.
"""

from __future__ import annotations

import argparse
import sys
from collections.abc import Sequence
from pathlib import Path

REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPOSITORY_ROOT))

from dset_toolchain.methodology_sync import (  # noqa: E402
    MethodologyDrift,
    methodology_drift,
    sync_methodology,
)
from scripts.build_bootstrap_bundle import render_bundle, write_bundle  # noqa: E402


def _refresh_bootstrap_bundle(root: Path) -> bool:
    """Refresh the distributable bundle and report whether it changed."""

    destination = root / "dset_toolchain/bootstrap_bundle.json"
    rendered = render_bundle(root)
    if destination.is_file() and destination.read_text(encoding="utf-8") == rendered:
        return False
    write_bundle(root)
    return True


def synchronize(root: Path, *, apply: bool = False) -> tuple[MethodologyDrift, ...]:
    """Preview or apply one-way synchronization and return initial drift."""

    repository = root.resolve()
    initial = methodology_drift(repository)
    if not apply:
        return initial
    sync_methodology(repository, execute=True)
    bundle_changed = _refresh_bootstrap_bundle(repository)
    if bundle_changed:
        sync_methodology(repository, execute=True)
    residual = methodology_drift(repository)
    if residual:
        carriers = ", ".join(item.carrier for item in residual)
        raise RuntimeError(f"methodology remains out of sync: {carriers}")
    if bundle_changed and not any(
        item.carrier == "bootstrap_bundle.json" for item in initial
    ):
        return (*initial, MethodologyDrift("bootstrap_bundle.json", "changed"))
    return initial


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "root",
        nargs="?",
        type=Path,
        default=Path.cwd(),
        help="repository root; defaults to the current directory",
    )
    parser.add_argument(
        "--apply",
        action="store_true",
        help="copy root methodology into .carmadio and verify zero drift",
    )
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    """Run the command-line interface."""

    args = _parser().parse_args(argv)
    try:
        drift = synchronize(args.root, apply=args.apply)
    except (FileNotFoundError, RuntimeError, ValueError) as error:
        print(f"ERROR {error}", file=sys.stderr)
        return 2
    label = "SYNCHRONIZED" if args.apply else "PREVIEW"
    print(f"{label} carriers={len(drift)}")
    for item in drift:
        print(f"{item.status.upper()} {item.carrier}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
