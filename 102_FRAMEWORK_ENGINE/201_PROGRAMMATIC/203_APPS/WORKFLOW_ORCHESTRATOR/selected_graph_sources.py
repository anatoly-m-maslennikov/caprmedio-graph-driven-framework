from __future__ import annotations

from collections.abc import Mapping
import hashlib
import re
from pathlib import Path
import sys
import tomllib
from typing import Any

from selected_execution_contracts import SelectedExecutionError


MANIFEST_DEFAULT = "_projection/selected_workflow_bindings.json"


def _sha256(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def _frontmatter(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return {}
    close = text.find("\n---\n", 4)
    if close < 0:
        return {}
    result: dict[str, str] = {}
    for line in text[4:close].splitlines():
        if ":" not in line or line.startswith((" ", "\t")):
            continue
        key, value = line.split(":", 1)
        result[key.strip()] = value.strip().strip('"').strip("'")
    return result


def manifest_relative_path(root: Path) -> str:
    """Resolve the one Project-local selected Workflow projection."""
    root = root.resolve(strict=True)
    settings_paths = sorted(
        path
        for path in root.glob(".caprmedio_*/caprmedio_project_settings.toml")
        if path.is_file() and not path.is_symlink() and not path.parent.is_symlink()
    )
    if len(settings_paths) != 1:
        raise SelectedExecutionError("Project settings carrier is missing or ambiguous")
    settings_path = settings_paths[0]
    try:
        settings = tomllib.loads(settings_path.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, tomllib.TOMLDecodeError) as error:
        raise SelectedExecutionError("Project settings carrier is invalid") from error
    paths = settings.get("paths", {})
    if not isinstance(paths, dict):
        raise SelectedExecutionError("Project control root is invalid")
    default = settings_path.parent.relative_to(root).as_posix()
    value = paths.get("control_root", default)
    if not isinstance(value, str) or not value:
        raise SelectedExecutionError("Project control root is invalid")
    control = Path(value)
    control_path = root / control
    if (
        control.is_absolute()
        or ".." in control.parts
        or control.as_posix() in {"", "."}
        or control_path.is_symlink()
        or not control_path.is_dir()
    ):
        raise SelectedExecutionError("Project control root is invalid")
    try:
        control_path.resolve().relative_to(root)
    except ValueError as error:
        raise SelectedExecutionError("Project control root is invalid") from error
    return (control / MANIFEST_DEFAULT).as_posix()


def safe_definition_path(root: Path, relative: str) -> Path:
    """Resolve a non-symlink, repository-relative definition carrier."""
    root = root.resolve(strict=True)
    if not isinstance(relative, str) or not relative:
        raise SelectedExecutionError("definition path is required")
    candidate = root / relative
    if Path(relative).is_absolute() or ".." in Path(relative).parts:
        raise SelectedExecutionError("unsafe definition path")
    try:
        resolved = candidate.resolve(strict=True)
        resolved.relative_to(root)
    except (OSError, ValueError, FileNotFoundError) as error:
        raise SelectedExecutionError("unsafe or unavailable definition path") from error
    cursor = root
    for part in Path(relative).parts:
        cursor /= part
        if cursor.is_symlink():
            raise SelectedExecutionError("definition symlinks are not admitted")
    if not resolved.is_file():
        raise SelectedExecutionError("definition path is not a file")
    return resolved


def load_manifest(root: Path, execution: Mapping[str, Any]) -> tuple[dict[str, Any], str, str]:
    """Load the selected manifest after checking its sealed Project location."""
    definition = execution.get("definition_manifest")
    definition = definition if isinstance(definition, Mapping) else {}
    manifest_ref = definition.get("manifest_ref")
    manifest_digest = definition.get("manifest_digest")
    if not isinstance(manifest_ref, str) or not isinstance(manifest_digest, str):
        raise SelectedExecutionError("selected definition manifest is required")
    path = safe_definition_path(root, manifest_ref)
    if path.relative_to(root.resolve(strict=True)).as_posix() != manifest_relative_path(root):
        raise SelectedExecutionError("selected definition manifest location is not admitted")
    mcp_root = str(Path(__file__).resolve().parents[2] / "204_MCP")
    if mcp_root not in sys.path:
        sys.path.insert(0, mcp_root)
    try:
        from selected_routes import load_selected_manifest

        manifest = load_selected_manifest(root)
    except (ImportError, OSError, RuntimeError, ValueError) as error:
        raise SelectedExecutionError(
            "complete selected definition manifest is not admitted"
        ) from error
    expected = manifest["canonical_manifest_sha256"]
    if manifest["manifest_ref"] != manifest_ref or manifest_digest != expected:
        raise SelectedExecutionError("selected definition manifest digest is stale or invalid")
    return manifest, manifest_ref, expected


def select_route(manifest: Mapping[str, Any], route: str) -> dict[str, Any]:
    rows = manifest.get("routes")
    if not isinstance(rows, list):
        raise SelectedExecutionError("selected definition manifest routes are invalid")
    matches = [row for row in rows if isinstance(row, dict) and row.get("route") == route]
    if len(matches) != 1:
        raise SelectedExecutionError("selected route is not admitted by the definition manifest")
    return matches[0]


def validate_definition(
    root: Path, binding: Mapping[str, Any], *, expected_kind: str
) -> dict[str, Any]:
    """Validate either a D547 source pin or the legacy test pin shape."""
    if {"atom_id", "version", "source_path", "digest"} <= set(binding):
        normalized = {
            "atom_id": binding["atom_id"],
            "kind": expected_kind,
            "version": binding["version"],
            "path": binding["source_path"],
            "sha256": binding["digest"],
        }
    elif {"atom_id", "kind", "version", "path", "sha256"} <= set(binding):
        normalized = dict(binding)
    else:
        raise SelectedExecutionError(f"invalid {expected_kind} definition binding")
    if normalized.get("kind") != expected_kind:
        raise SelectedExecutionError(f"invalid {expected_kind} definition binding")
    if not isinstance(normalized["atom_id"], str) or not isinstance(normalized["version"], int):
        raise SelectedExecutionError(f"invalid {expected_kind} definition identity")
    digest = normalized.get("sha256")
    if not isinstance(digest, str) or not re.fullmatch(r"[0-9a-f]{64}", digest):
        raise SelectedExecutionError(f"invalid {expected_kind} definition digest")
    path = safe_definition_path(root, str(normalized["path"]))
    if _sha256(path.read_bytes()) != digest:
        raise SelectedExecutionError(f"{expected_kind} definition changed after admission")
    metadata = _frontmatter(path)
    if metadata.get("atom_id") != normalized["atom_id"] or metadata.get("version") != str(
        normalized["version"]
    ):
        raise SelectedExecutionError(f"{expected_kind} definition identity changed after admission")
    return normalized
