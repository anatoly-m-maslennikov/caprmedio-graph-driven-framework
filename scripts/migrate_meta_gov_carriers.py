#!/usr/bin/env python3
"""Compatibility launcher for the authoritative META/GOV carrier migration.

Invocation:
    python scripts/migrate_meta_gov_carriers.py [ROOT] [--apply | --check]
        [--expect-plan-digest SHA256]

The launcher preserves the legacy positional-root and mode grammar. When ROOT
is omitted it targets this repository, not the caller's working directory. It
delegates all effects and exit behavior to the authoritative migration tool.
"""

from __future__ import annotations

import runpy
import sys
from pathlib import Path

sys.dont_write_bytecode = True


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
AUTHORITATIVE_TOOL = (
    REPOSITORY_ROOT
    / "15_layer_implementation/tools/migrations/migrate_meta_gov_carriers.py"
)
AUTHORITATIVE_PACKAGE_ROOT = AUTHORITATIVE_TOOL.parent


def main() -> int:
    """Delegate to the authoritative tool, defaulting ROOT to this repository."""
    arguments = sys.argv[1:]
    if not arguments or arguments[0].startswith("-"):
        arguments.insert(0, str(REPOSITORY_ROOT))
    sys.path.insert(0, str(AUTHORITATIVE_PACKAGE_ROOT))
    sys.argv = [str(AUTHORITATIVE_TOOL), *arguments]
    runpy.run_path(str(AUTHORITATIVE_TOOL), run_name="__main__")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
