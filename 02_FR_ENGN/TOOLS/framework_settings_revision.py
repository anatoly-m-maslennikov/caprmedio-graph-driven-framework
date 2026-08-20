#!/usr/bin/env python3
"""Compatibility entry point for Framework Settings Atom revisions."""

from __future__ import annotations

import sys
from pathlib import Path


sys.pycache_prefix = str(
    Path(__file__).resolve().parents[2] / ".caprmedio_runtime/cache/python"
)
TOOLS_ROOT = Path(__file__).resolve().parent
if str(TOOLS_ROOT) not in sys.path:
    sys.path.insert(0, str(TOOLS_ROOT))

from native_atom_revision import cli, current_reference as native_current_reference  # noqa: E402


def current_reference(root: Path) -> str:
    return native_current_reference(root, "framework-settings")


if __name__ == "__main__":
    raise SystemExit(cli(["framework-settings", *sys.argv[1:]]))
