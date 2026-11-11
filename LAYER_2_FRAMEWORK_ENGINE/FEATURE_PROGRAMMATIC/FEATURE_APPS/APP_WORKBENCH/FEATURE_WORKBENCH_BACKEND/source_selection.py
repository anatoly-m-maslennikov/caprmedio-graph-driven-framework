# CA-M-464@15
"""Keep the first readable carrier of each Atom reference."""

from __future__ import annotations

import sys
from typing import Any


def first_reference_rows(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    selected = []
    seen = {}
    for row in rows:
        reference = row.get("ref")
        if reference is not None and reference in seen:
            print(f"Workbench: {row.get('source_path')}: duplicate reference {reference}; "
                  f"already loaded from {seen[reference]}; skipped", file=sys.stderr)
            continue
        selected.append(row)
        if reference is not None:
            seen[reference] = row.get("source_path")
    return selected
