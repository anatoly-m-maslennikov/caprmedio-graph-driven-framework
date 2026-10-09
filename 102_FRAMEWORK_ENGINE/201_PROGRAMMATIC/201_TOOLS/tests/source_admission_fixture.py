"""Canonical synthetic source-admission receipts for package-boundary tests.

These fixtures model only the retained D602 proof carrier.  They do not stand
in for an Action Run, a release gate, or any host-side approval action.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import sys
from typing import Mapping

TOOLS_ROOT = Path(__file__).resolve().parents[1]
if str(TOOLS_ROOT) not in sys.path:
    sys.path.insert(0, str(TOOLS_ROOT))

from source_catalog_admission import (  # noqa: E402
    build_source_admission_receipt as _build_source_admission_receipt,
    read_source_admission_receipt,
)


@dataclass(frozen=True)
class SourceAdmissionFixture:
    """One retained synthetic proof and its content-addressed package path."""

    payload: bytes
    sha256: str
    relative_path: Path


def build_source_admission_receipt(
    sources: tuple[Mapping[str, object], ...],
    *,
    operator: str = "fixture-operator",
    command_ref: str = "commands/admit-package-sources",
    action_run_id: str = "fixture-admit-package-sources",
) -> SourceAdmissionFixture:
    """Build one D602v3 canonical receipt from exact catalog-shaped sources."""

    if not sources:
        raise ValueError("source admission receipt requires sources")
    payload = _build_source_admission_receipt(
        operator=operator,
        command_ref=command_ref,
        action_run_id=action_run_id,
        sources=sources,
    )
    receipt = read_source_admission_receipt(payload)
    return SourceAdmissionFixture(payload, receipt.sha256, Path("admissions") / f"{receipt.sha256}.json")


def write_source_admission_receipt(
    package_root: Path,
    sources: tuple[Mapping[str, object], ...],
    **kwargs: str,
) -> SourceAdmissionFixture:
    """Materialize a canonical receipt in the exact package-owned location."""

    fixture = build_source_admission_receipt(sources, **kwargs)
    target = package_root / fixture.relative_path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(fixture.payload)
    return fixture
