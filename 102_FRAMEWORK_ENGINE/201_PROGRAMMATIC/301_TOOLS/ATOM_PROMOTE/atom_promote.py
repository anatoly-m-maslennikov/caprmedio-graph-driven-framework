#!/usr/bin/env python3
"""Promote CAPRMEDIO Markdown Atom drafts to active authority."""
from pathlib import Path
import sys

SCRIPT = Path(__file__).resolve()
TOOLS = SCRIPT.parents[1]
for parent in SCRIPT.parents:
    if parent.name == ".caprmedio_install":
        sys.pycache_prefix = str(parent.parent / ".caprmedio_runtime/cache/python")
        break
sys.path.insert(0, str(TOOLS))
from atom_operations import cli  # noqa: E402

if __name__ == "__main__":
    raise SystemExit(cli("ATOM_PROMOTE"))
