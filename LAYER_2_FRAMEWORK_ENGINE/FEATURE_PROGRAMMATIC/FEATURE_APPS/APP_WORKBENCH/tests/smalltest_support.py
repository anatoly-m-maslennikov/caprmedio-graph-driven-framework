# CA-E-675@6
# CA-E-676@6
# CA-E-677@12
"""Small real-carrier fixture helpers shared by Workbench integration tests."""

from __future__ import annotations

import os
import re
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
        '[project]\nname = "fixture"\n[artifacts.identity]\nproject_prefix = "CA"\n'
        '[paths]\ncontrol_root = ".caprmedio_caprmedio"\n',
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
    relative = Path(name)
    if not re.match(r"^[A-Za-z0-9_]+-[A-Z]-", relative.name):
        name = str(relative.with_name("CA-R-" + relative.name))
    return Path(declarations[scope]["authority_path"]) / role / name


def built_assets(root: Path) -> dict[str, Any]:
    """Compile fixture inputs at the same boundary as an image build."""
    from APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.source_reader import SourceReader
    from APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.workbench_schema_asset import compile_schema
    from APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.relation_registry import compile_registry

    reader = SourceReader(root)
    atoms, _ = reader.capture()
    return {
        "compiled_schema": compile_schema(atoms, reader.content_schema, reader.header_schema),
        "relation_registry": compile_registry(atoms).registry,
    }


def empty_assets() -> dict[str, Any]:
    from APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.content_schema import compile_content_schema
    from APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.workbench_schema_asset import compile_schema
    from APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.relation_registry import compile_registry

    return {"compiled_schema": compile_schema([], compile_content_schema([])),
            "relation_registry": compile_registry([]).registry}
