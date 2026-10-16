"""Finite frozen grammar carriers for Subject-tool fixtures."""

from __future__ import annotations

from pathlib import Path

from subject_notation import get_profile


_FIXTURES = (
    "legacy-ca-r-1204-v14.md", "legacy-ca-r-1321-v12.md", "legacy-ca-r-1324-v10.md",
    "legacy-ca-m-228-v14.md", "legacy-ca-e-383-v13.md", "approved-ca-r-1931-v1.md",
    "approved-ca-r-1321-v15.md", "approved-ca-r-1324-v13.md", "approved-ca-m-228-v17.md",
    "approved-ca-e-383-v18.md",
)


def grammar_carriers() -> dict[str, bytes]:
    """Return the exact legacy and approved carrier bytes by declared path."""

    paths = [pin.path for profile in ("legacy", "approved") for pin in get_profile(profile).grammar_pins]
    fixture_root = Path(__file__).with_name("fixtures") / "subject_grammar"
    return {path: (fixture_root / fixture).read_bytes() for path, fixture in zip(paths, _FIXTURES, strict=True)}
