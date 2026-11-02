"""Source-only materialization helpers for the Interactive MCP fixture."""

from __future__ import annotations

import hashlib
from pathlib import Path
from typing import Any, Mapping
import sys


TOOLS_ROOT = Path(__file__).resolve().parents[2] / "FEATURE_TOOLS"
if str(TOOLS_ROOT) not in sys.path:
    sys.path.insert(0, str(TOOLS_ROOT))
from scope_declaration_test_support import write_scope_unit_declarations
from frozen_selected_workflows import frozen_manifest, frozen_source_bytes
from test_selected_routes_mcp import _FIXTURE_SCOPE_ROWS


class InteractiveFixtureError(RuntimeError):
    """The disposable verification world cannot be admitted."""


def safe_relative(value: object, label: str) -> Path:
    if not isinstance(value, str) or not value:
        raise InteractiveFixtureError(f"{label} must be a non-empty relative path")
    path = Path(value)
    if path.is_absolute() or ".." in path.parts:
        raise InteractiveFixtureError(f"{label} escapes the disposable Project")
    return path


def write_settings(root: Path) -> dict[str, dict[str, Any]]:
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
    rows = write_scope_unit_declarations(root, _FIXTURE_SCOPE_ROWS)
    (control / "_journal").mkdir(parents=True, exist_ok=True)
    (root / ".caprmedio_runtime").mkdir(parents=True, exist_ok=True)
    (root / ".git").mkdir(parents=True, exist_ok=True)
    return rows


def _declared_source_path(root: Path, relative: object, rows: Mapping[str, Mapping[str, Any]]) -> tuple[Path, Path]:
    path = safe_relative(relative, "current source path")
    parts = path.parts
    role_directories = ("04_requirement", "05_method", "06_evaluation", "07_delivery", "09_operations")
    if "003_PROJECT_CONFIGURATION" in parts:
        marker = parts.index("003_PROJECT_CONFIGURATION")
        scope = "PROJECT_CONFIGURATION"
    elif parts and parts[0] == ".caprmedio_caprmedio" and any(
        role in parts for role in role_directories
    ):
        marker = next(index for index, part in enumerate(parts) if part in role_directories)
        scope = "TOOL_WORKFLOWS"
    elif "102_LAYER_2_FRAMEWORK_ENGINE" in parts and any(
        role in parts for role in role_directories
    ):
        marker = next(
            index for index, part in enumerate(parts)
            if part in role_directories
        )
        scope = "TOOL_WORKFLOWS"
    else:
        raise InteractiveFixtureError(f"current source is outside declared fixture authorities: {path}")
    authority = rows.get(scope, {}).get("authority_path")
    if not isinstance(authority, (str, Path)) or not str(authority):
        raise InteractiveFixtureError(f"fixture Scope Unit Declaration is missing: {scope}")
    return path, Path(authority) / Path(*parts[marker:])


def _copy_source(
    root: Path, relative: object, raw: bytes, expected: object, rows: Mapping[str, Mapping[str, Any]]
) -> None:
    path, target = _declared_source_path(root, relative, rows)
    if not isinstance(expected, str) or hashlib.sha256(raw).hexdigest() != expected:
        raise InteractiveFixtureError(f"current source digest is stale: {path}")
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(raw)
    legacy = root / path
    if legacy != target and legacy.exists():
        legacy.unlink()


def _relative_declared_source_path(
    root: Path, relative: object, rows: Mapping[str, Mapping[str, Any]]
) -> str:
    _, target = _declared_source_path(root, relative, rows)
    try:
        return target.relative_to(root).as_posix()
    except ValueError as error:
        raise InteractiveFixtureError(
            f"derived fixture source escapes the disposable Project: {target}"
        ) from error


def rewrite_source_paths(value: object, root: Path, rows: Mapping[str, Mapping[str, Any]]) -> object:
    """Rebind source-row paths to the authority returned by the fixture declarations."""
    if isinstance(value, Mapping):
        has_source_pin = isinstance(value.get("atom_id"), str) and (
            isinstance(value.get("sha256"), str) or isinstance(value.get("digest"), str)
        )
        result: dict[object, object] = {}
        for key, item in value.items():
            if key == "source_path" and isinstance(item, str):
                result[key] = _relative_declared_source_path(root, item, rows)
            elif key == "path" and has_source_pin and isinstance(item, str):
                result[key] = _relative_declared_source_path(root, item, rows)
            else:
                result[key] = rewrite_source_paths(item, root, rows)
        return result
    if isinstance(value, list):
        return [rewrite_source_paths(item, root, rows) for item in value]
    if isinstance(value, tuple):
        return tuple(rewrite_source_paths(item, root, rows) for item in value)
    return value


def _copy_query_sources(root: Path, rows: Mapping[str, Mapping[str, Any]]) -> None:
    """Move frozen O158-O163 bytes into the declared Project Configuration authority."""
    legacy_root = Path(
        ".caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/"
        "CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL"
    )
    authority = rows["PROJECT_CONFIGURATION"]["authority_path"]
    manifest = frozen_manifest()
    pins = [
        pin
        for admission in manifest["query_source_admissions"]
        for pin in (
            admission["workflow"],
            *admission["ordered_actions"],
            *[pin for item in admission["ordered_steps"] for pin in item.values()],
        )
    ]
    seen: set[str] = set()
    for pin in pins:
        atom_id = str(pin["atom_id"])
        if atom_id in seen:
            continue
        seen.add(atom_id)
        source = safe_relative(pin["source_path"], "frozen query source")
        try:
            source_relative = source.relative_to(legacy_root)
        except ValueError as error:
            raise InteractiveFixtureError(f"frozen query source is outside Core authority: {source}") from error
        target = Path(authority) / Path(*(
            part.replace("-CORE_META_MODEL-", "-PROJECT_CONFIGURATION-")
            for part in source_relative.parts
        ))
        raw = frozen_source_bytes(source, pin.get("digest"))
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(raw)
        legacy = root / source
        if legacy != target and legacy.exists():
            legacy.unlink()


def copy_current_closure(root: Path, fixture: Any, rows: Mapping[str, Mapping[str, Any]]) -> None:
    _copy_query_sources(root, rows)
    for pin in fixture.source_pins():
        _copy_source(
            root, pin["source_path"], fixture.source_bytes(str(pin["atom_id"])), pin["sha256"], rows
        )
    for pin in fixture.method_source_pins():
        _copy_source(
            root, pin["path"], fixture.method_source_bytes(str(pin["atom_id"])), pin["sha256"], rows
        )
    for row in fixture._support_rows():
        _copy_source(
            root, row["path"], fixture.support_source_bytes(str(row["atom_id"])), row["sha256"], rows
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
