# CA-M-506@2
# CA-D-704@1

"""Generate the deterministic MCP registration asset from installed code."""

from __future__ import annotations

import argparse
from pathlib import Path
import sys
from typing import Sequence

TOOLS_ROOT = Path(__file__).resolve().parents[1] / "FEATURE_TOOLS"
for _path in (TOOLS_ROOT, TOOLS_ROOT / "VALIDATE_ATOMS"):
    if str(_path) not in sys.path:
        sys.path.insert(0, str(_path))

from tool_registry_asset import write_generated_registry  # noqa: E402


def generate(package_root: str | Path) -> dict[str, object]:
    """Write and return the package-local registration asset."""

    return write_generated_registry(package_root)


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--package-root", required=True, type=Path)
    args = parser.parse_args(argv)
    generate(args.package_root)
    return 0


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
