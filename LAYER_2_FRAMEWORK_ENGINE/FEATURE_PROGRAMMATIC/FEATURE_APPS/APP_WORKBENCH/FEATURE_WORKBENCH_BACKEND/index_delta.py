# CA-M-465@19

"""Changed materialized rows for one committed Workbench source batch."""

from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class MaterializationDelta:
    old_atoms: dict[str, dict[str, Any]]
    new_atoms: dict[str, dict[str, Any]]
    old_scopes: dict[str, dict[str, Any]]
    new_scopes: dict[str, dict[str, Any]]
