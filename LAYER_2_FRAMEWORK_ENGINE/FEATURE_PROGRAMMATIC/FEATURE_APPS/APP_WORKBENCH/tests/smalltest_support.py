# CA-E-675@4
# CA-E-676@3
# CA-E-677@6

"""Small real-carrier fixture helpers shared by Workbench integration tests."""

from __future__ import annotations

import os
from pathlib import Path
from typing import Any


def extension_directory(root: Path) -> Path:
    """Use the suite-prepared DuckPGQ cache, overridable for local runs."""
    return Path(os.environ.get(
        "CAPRMEDIO_DUCKPGQ_EXTENSION_DIRECTORY",
        root / ".caprmedio_tmp" / "workbench" / "extensions",
    ))


def write_settings(root: Path) -> Path:
    control = root / ".caprmedio_caprmedio"
    control.mkdir()
    (control / "caprmedio_project_settings.toml").write_text(
        '[project]\nname = "fixture"\n[paths]\ncontrol_root = ".caprmedio_caprmedio"\n',
        encoding="utf-8",
    )
    return control


def write_atom(
    path: Path,
    atom_id: str,
    *,
    status: str = "Active",
    version: int = 1,
    relations: str = "{}",
    subjects: str = "{}",
    body: str = "# Summary\n\nFixture source.\n",
    extra: str = "",
) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        "---\n"
        f'atom_id: "{atom_id}"\n'
        'role: "Requirement"\n'
        'form: "Definition"\n'
        f'status: "{status}"\n'
        f"version: {version}\n"
        'updated_at: "2026-11-04 00:00:00 +0000"\n'
        f"subjects: {subjects}\n"
        f"relations: {relations}\n"
        f"{extra}"
        "---\n"
        + body,
        encoding="utf-8",
    )
    return path


def source_path(declarations: dict[str, dict[str, Any]], scope: str, role: str, name: str) -> Path:
    return Path(declarations[scope]["authority_path"]) / role / name
