"""Exact inert direct-Action carriers for disposable test Projects/packages."""

from __future__ import annotations

import hashlib
from pathlib import Path

from direct_action_session import (
    ACTION_ATOM_RELATIVE,
    ACTION_ATOM_SHA256,
    INSTALLATION_ATOM_RELATIVE,
    INSTALLATION_ATOM_SHA256,
    RESTORATION_ATOM_RELATIVE,
    RESTORATION_ATOM_SHA256,
)


_ACTION_FIXTURES = Path(__file__).resolve().parent / "direct_action_golden"


def action_fixture(relative: Path) -> Path:
    """Reopen only the exact reviewed inert Action carrier for a test fixture.

    Production admission still checks the copied Project/package carrier;
    these data files are never an installed-source fallback for production.
    """
    fixtures = {
        ACTION_ATOM_RELATIVE: ("CA-O-180-v3.md", ACTION_ATOM_SHA256),
        RESTORATION_ATOM_RELATIVE: ("CA-O-187-v2.md", RESTORATION_ATOM_SHA256),
        INSTALLATION_ATOM_RELATIVE: ("CA-O-200-v1.md", INSTALLATION_ATOM_SHA256),
    }
    name, digest = fixtures[relative]
    source = _ACTION_FIXTURES / name
    if (_ACTION_FIXTURES.is_symlink() or source.is_symlink() or not source.is_file()
            or source.resolve(strict=True).parent != _ACTION_FIXTURES.resolve(strict=True)
            or hashlib.sha256(source.read_bytes()).hexdigest() != digest):
        raise RuntimeError("direct Action golden fixture is unavailable or differs from its reviewed pin")
    return source
