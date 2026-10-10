"""Generate one deterministic, non-executing MCP Tool-registry projection."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys
from typing import Sequence


TOOLS_ROOT = Path(__file__).resolve().parents[1] / "201_TOOLS"
for _path in (TOOLS_ROOT, TOOLS_ROOT / "VALIDATE_ATOMS"):
    if str(_path) not in sys.path:
        sys.path.insert(0, str(_path))

from capability_discovery.service import Service  # noqa: E402
from registered_tool_registry import compile_registry  # noqa: E402


def generate(project_root: str | Path) -> dict[str, object]:
    """Return the catalog-derived registry projection without registering Tools."""

    root = Path(project_root).resolve(strict=True)
    _atoms, bindings, _issues = Service(root).catalog()
    return compile_registry(root, bindings).projection()


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project-root", required=True, type=Path)
    parser.add_argument("--output", type=Path, help="optional JSON projection destination")
    args = parser.parse_args(argv)
    projection = generate(args.project_root)
    rendered = json.dumps(projection, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n"
    if args.output is None:
        print(rendered, end="")
    else:
        args.output.write_text(rendered, encoding="utf-8")
    return 0


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
