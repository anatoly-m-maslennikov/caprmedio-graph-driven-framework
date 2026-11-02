"""Project-path and canonical serialization helpers for selected routes."""

from __future__ import annotations

import copy
import hashlib
import json
import re
import tomllib
from pathlib import Path
from typing import Any, Mapping

from project_selection import bound_selection
from selected_definition_sources import CurrentDefinitionSources
from selected_route_contract import selected_manifest_contract as _selected_manifest_contract
from selected_route_spec import (
    DEFAULT_CONTROL_ROOT,
    MANIFEST_FILENAME,
    PROJECT_SETTINGS_REF,
    _DIGEST,
    _QUERY_SOURCE_ADMISSION_SPECS,
    SelectedRouteError,
)

selected_manifest_contract = _selected_manifest_contract


def canonical_json(value: Any) -> str:
    return json.dumps(
        value, ensure_ascii=False, allow_nan=False, sort_keys=True, separators=(",", ":")
    )


def canonical_digest(value: Any) -> str:
    return hashlib.sha256(canonical_json(value).encode("utf-8")).hexdigest()


def _configured_control_root(root: Path) -> Path:
    selection = bound_selection(root)
    if selection is not None:
        return selection.control_relative
    settings_path = root / PROJECT_SETTINGS_REF
    if settings_path.is_symlink():
        raise SelectedRouteError("project settings carrier is unavailable")
    if not settings_path.exists():
        return DEFAULT_CONTROL_ROOT
    if not settings_path.is_file():
        raise SelectedRouteError("project settings carrier is unavailable")
    try:
        settings = tomllib.loads(settings_path.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, tomllib.TOMLDecodeError) as error:
        raise SelectedRouteError("project settings carrier is invalid") from error
    paths = settings.get("paths")
    value = paths.get("control_root") if isinstance(paths, Mapping) else None
    if value is None:
        return DEFAULT_CONTROL_ROOT
    if not isinstance(value, str) or not value:
        raise SelectedRouteError("paths.control_root must be a safe repository-relative path")
    candidate = Path(value)
    if candidate.is_absolute() or candidate == Path(".") or ".." in candidate.parts:
        raise SelectedRouteError("paths.control_root must be a safe repository-relative path")
    resolved = (root / candidate).resolve()
    if root != resolved and root not in resolved.parents:
        raise SelectedRouteError("paths.control_root escapes project root")
    return candidate


def _selected_authority_ref(root: Path, reference: str) -> str:
    selection = bound_selection(root)
    path = Path(reference)
    if selection is not None and path.is_relative_to(DEFAULT_CONTROL_ROOT):
        return (selection.control_relative / path.relative_to(DEFAULT_CONTROL_ROOT)).as_posix()
    return reference


def _query_admission_specs(
    root: Path, sources: CurrentDefinitionSources | None = None
) -> tuple[dict[str, Any], ...]:
    specifications = copy.deepcopy(_QUERY_SOURCE_ADMISSION_SPECS)
    owned_sources = sources is None
    sources = sources or CurrentDefinitionSources(root)

    def bind(value: Any) -> None:
        if isinstance(value, dict):
            if set(value) == {"atom_id", "source_path"}:
                value["source_path"] = _selected_authority_ref(root, value["source_path"])
                value.update(_current_pin(root, value, sources))
                return
            for key, child in value.items():
                if key == "source_path":
                    value[key] = _selected_authority_ref(root, child)
                else:
                    bind(child)
        elif isinstance(value, list):
            for child in value:
                bind(child)

    bind(list(specifications))
    if owned_sources:
        sources.revalidate()
    return specifications


def selected_manifest_ref(root: str | Path | None = None) -> str:
    if root is None:
        control_root = DEFAULT_CONTROL_ROOT
    else:
        project_root = Path(root).resolve(strict=True)
        control_root = _configured_control_root(project_root)
    return (control_root / "_projection" / MANIFEST_FILENAME).as_posix()


def _safe_path(root: Path, relative: str) -> Path:
    bound_selection(root)
    if (
        not isinstance(relative, str)
        or not relative
        or relative.startswith("/")
        or "\\" in relative
    ):
        raise SelectedRouteError("source_path must be a safe repository-relative path")
    path = (root / relative).resolve()
    if root != path and root not in path.parents:
        raise SelectedRouteError("source_path escapes project root")
    return path


def _frontmatter_value(contents: str, field: str) -> str | None:
    match = re.search(rf"(?m)^{re.escape(field)}:\s*[\"']?([^\n\"']+)", contents)
    return match.group(1).strip() if match else None


def _current_pin(
    root: Path,
    pin: Mapping[str, Any],
    sources: CurrentDefinitionSources,
    expected_type: str | None = None,
) -> dict[str, Any]:
    source_path = pin["source_path"]
    path = _safe_path(root, source_path)
    selection = bound_selection(root)
    relative_parts = path.relative_to(root).parts
    if (
        selection is not None
        and relative_parts
        and relative_parts[0].startswith(".caprmedio_")
        and not path.is_relative_to(selection.control_root)
    ):
        raise SelectedRouteError("source pin belongs to another Project authority")
    try:
        return sources.read(pin["atom_id"], source_path, expected_type)
    except (OSError, ValueError, RuntimeError) as error:
        raise SelectedRouteError(
            f"current definition is unavailable or invalid: {source_path}"
        ) from error


def _validate_pin(
    root: Path,
    pin: Any,
    sources: CurrentDefinitionSources | None = None,
    expected_type: str | None = None,
) -> dict[str, Any]:
    if not isinstance(pin, Mapping) or set(pin) != {"atom_id", "version", "source_path", "digest"}:
        raise SelectedRouteError(
            "definition pin must contain atom_id, version, source_path, and digest"
        )
    atom_id, version, digest = pin["atom_id"], pin["version"], pin["digest"]
    if not isinstance(atom_id, str) or not atom_id or type(version) is not int or version < 1:
        raise SelectedRouteError("definition pin has invalid identity or version")
    if not isinstance(digest, str) or not _DIGEST.fullmatch(digest):
        raise SelectedRouteError("definition pin has invalid digest")
    owned_sources = sources is None
    sources = sources or CurrentDefinitionSources(root)
    observed = _current_pin(root, pin, sources, expected_type)
    if owned_sources:
        sources.revalidate()
    return observed


def _manifest_path(root: Path) -> Path:
    return _safe_path(root, selected_manifest_ref(root))
