"""Source-only materialization helpers for the Interactive MCP fixture."""

from __future__ import annotations

import hashlib
from pathlib import Path
from typing import Any


class InteractiveFixtureError(RuntimeError):
    """The disposable verification world cannot be admitted."""


def safe_relative(value: object, label: str) -> Path:
    if not isinstance(value, str) or not value:
        raise InteractiveFixtureError(f"{label} must be a non-empty relative path")
    path = Path(value)
    if path.is_absolute() or ".." in path.parts:
        raise InteractiveFixtureError(f"{label} escapes the disposable Project")
    return path


def write_settings(root: Path) -> None:
    control = root / ".caprmedio_caprmedio"
    control.mkdir(parents=True, exist_ok=True)
    (control / "caprmedio_project_settings.toml").write_text(
        '[project]\nkey = "interactive-mcp-fixture"\n'
        'name = "interactive-mcp-fixture"\nrepository_slug = "fixture"\n'
        '[artifacts.identity]\nproject_prefix = "CA"\n\n'
        '[paths]\ncontrol_root = ".caprmedio_caprmedio"\n'
        'journal_root = ".caprmedio_caprmedio/_journal"\n'
        'runtime_root = ".caprmedio_runtime"\n\n'
        '[authority_modes]\ndefault = "casual"\n',
        encoding="utf-8",
    )
    (control / "operators_registry.toml").write_text(
        '[[operators]]\nname = "golden-operator"\nrole = "project owner"\n',
        encoding="utf-8",
    )
    (control / "project_structure.toml").write_text("schema_version = 1\n", encoding="utf-8")
    (control / "_journal").mkdir(parents=True, exist_ok=True)
    (root / ".caprmedio_runtime").mkdir(parents=True, exist_ok=True)
    (root / ".git").mkdir(parents=True, exist_ok=True)


def _copy_source(root: Path, relative: object, raw: bytes, expected: object) -> None:
    path = safe_relative(relative, "current source path")
    if not isinstance(expected, str) or hashlib.sha256(raw).hexdigest() != expected:
        raise InteractiveFixtureError(f"current source digest is stale: {path}")
    target = root / path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(raw)


def copy_current_closure(root: Path, fixture: Any) -> None:
    for pin in fixture.source_pins():
        _copy_source(
            root, pin["source_path"], fixture.source_bytes(str(pin["atom_id"])), pin["sha256"]
        )
    for pin in fixture.method_source_pins():
        _copy_source(
            root, pin["path"], fixture.method_source_bytes(str(pin["atom_id"])), pin["sha256"]
        )
    for row in fixture._support_rows():
        _copy_source(
            root, row["path"], fixture.support_source_bytes(str(row["atom_id"])), row["sha256"]
        )


def materialize_method_projection(root: Path, fixture: Any) -> Path:
    spec = fixture.support_inventory["method_projection"]
    name = safe_relative(str(spec["projection"]), "Method projection name").name
    target = root / ".caprmedio_runtime" / "interactive" / name
    content = fixture.method_projection_content().encode("utf-8")
    if hashlib.sha256(content).hexdigest() != spec["content_sha256"]:
        raise InteractiveFixtureError("Method projection digest is stale")
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(content)
    return target
