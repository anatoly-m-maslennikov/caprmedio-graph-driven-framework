# CA-R-2785@3
# CA-M-473@3
# CA-D-678@3
# CA-D-679@1
# CA-R-1804@13
# CA-D-512@16
# CA-D-681@1
# CA-D-696@1

"""Read and write the released MCP tool-catalog projection."""

from __future__ import annotations

from datetime import UTC, datetime
import json
import os
from pathlib import Path
import stat
import tempfile
from typing import Any, Mapping, Sequence


CATALOG_PARTS = (".caprmedio_runtime", "mcp", "tools_catalog.json")
GROUPS = ("Workspaces", "Views", "Queries", "Service")
SERVICE_TOOLS = frozenset({
    "reload_mcp_implementation", "get_mcp_reload_status", "workbench_reread", "workbench_status",
})


class ToolCatalogError(ValueError):
    """The released catalog cannot safely be used."""


def _root(root: str | Path) -> Path:
    try:
        return Path(root).resolve(strict=True)
    except OSError as error:
        raise ToolCatalogError("Project root is unavailable") from error


def catalog_path(root: str | Path) -> Path:
    """Return the fixed, project-owned catalog path."""

    return _root(root).joinpath(*CATALOG_PARTS)


def group_for(name: str) -> str | None:
    """Return the one visible group owned by a native MCP tool name."""

    if name.startswith("workspace_"):
        return "Workspaces"
    if name.startswith("query_"):
        return "Queries"
    if name.startswith("view_"):
        return "Views"
    if name in SERVICE_TOOLS or name.endswith("_restart"):
        return "Service"
    return None


def _descriptor(value: object) -> dict[str, Any]:
    if isinstance(value, Mapping):
        result = dict(value)
    else:
        model_dump = getattr(value, "model_dump", None)
        if not callable(model_dump):
            raise ToolCatalogError("MCP tool descriptor is invalid")
        result = model_dump(mode="json", by_alias=True, exclude_none=True)
    if not isinstance(result.get("name"), str) or not result["name"]:
        raise ToolCatalogError("MCP tool descriptor has no name")
    return result


def _root_sort_key(descriptor: Mapping[str, Any]) -> tuple[int, str]:
    name = str(descriptor["name"])
    return (0 if name == "discover_tools" else 1, name)


def build_catalog(tools: Sequence[object]) -> dict[str, Any]:
    """Build one deterministic catalog from actual MCP ``tools/list`` data."""

    descriptors = [_descriptor(tool) for tool in tools]
    names = [descriptor["name"] for descriptor in descriptors]
    if len(names) != len(set(names)):
        raise ToolCatalogError("MCP tool descriptors have duplicate names")
    if names.count("discover_tools") != 1:
        raise ToolCatalogError("MCP tool descriptors must contain exactly one discover_tools")
    grouped = {group: [] for group in GROUPS}
    root: list[dict[str, Any]] = []
    for descriptor in descriptors:
        group = group_for(descriptor["name"])
        (grouped[group] if group else root).append(descriptor)
    root.sort(key=_root_sort_key)
    for group in GROUPS:
        grouped[group].sort(key=lambda descriptor: descriptor["name"])
    return {
        "updated_at": datetime.now(UTC).isoformat().replace("+00:00", "Z"),
        "root": root,
        "groups": grouped,
    }


def _require_regular_catalog(root: Path) -> Path:
    directory = root
    for part in CATALOG_PARTS[:-1]:
        directory /= part
        try:
            mode = os.lstat(directory).st_mode
        except FileNotFoundError as error:
            raise ToolCatalogError("Generated MCP tool catalog is missing") from error
        if stat.S_ISLNK(mode) or not stat.S_ISDIR(mode):
            raise ToolCatalogError("Generated MCP tool catalog path is unsafe")
    path = directory / CATALOG_PARTS[-1]
    try:
        mode = os.lstat(path).st_mode
    except FileNotFoundError as error:
        raise ToolCatalogError("Generated MCP tool catalog is missing") from error
    if stat.S_ISLNK(mode) or not stat.S_ISREG(mode):
        raise ToolCatalogError("Generated MCP tool catalog is unsafe")
    return path


def _validate_entries(entries: object, group: str | None = None) -> list[dict[str, Any]]:
    if not isinstance(entries, list):
        raise ToolCatalogError("Generated MCP tool catalog is invalid")
    checked = [_descriptor(entry) for entry in entries]
    if group is None:
        valid = all(group_for(entry["name"]) is None for entry in checked)
    else:
        valid = all(group_for(entry["name"]) == group for entry in checked)
    if not valid:
        raise ToolCatalogError("Generated MCP tool catalog has an invalid group")
    return checked


def _validate_catalog(value: object) -> dict[str, Any]:
    if not isinstance(value, Mapping) or not isinstance(value.get("updated_at"), str) or not value["updated_at"]:
        raise ToolCatalogError("Generated MCP tool catalog is invalid")
    root = value.get("root")
    groups = value.get("groups")
    if not isinstance(groups, Mapping) or set(groups) != set(GROUPS):
        raise ToolCatalogError("Generated MCP tool catalog is invalid")
    root_entries = _validate_entries(root)
    result = {"updated_at": value["updated_at"], "root": root_entries, "groups": {}}
    all_descriptors = list(root_entries)
    for group in GROUPS:
        checked = _validate_entries(groups[group], group)
        result["groups"][group] = checked
        all_descriptors.extend(checked)
    names = [descriptor["name"] for descriptor in all_descriptors]
    if len(names) != len(set(names)):
        raise ToolCatalogError("Generated MCP tool catalog has duplicate names")
    if names.count("discover_tools") != 1:
        raise ToolCatalogError("Generated MCP tool catalog must contain exactly one discover_tools")
    if result["root"] != sorted(result["root"], key=_root_sort_key):
        raise ToolCatalogError("Generated MCP tool catalog root is unordered")
    if any(result["groups"][group] != sorted(result["groups"][group], key=lambda item: item["name"])
           for group in GROUPS):
        raise ToolCatalogError("Generated MCP tool catalog groups are unordered")
    return result


def read_catalog(root: str | Path) -> dict[str, Any]:
    """Read a complete generated catalog without rescanning source carriers."""

    path = _require_regular_catalog(_root(root))
    flags = os.O_RDONLY | getattr(os, "O_CLOEXEC", 0) | getattr(os, "O_NOFOLLOW", 0)
    try:
        descriptor = os.open(path, flags)
    except OSError as error:
        raise ToolCatalogError("Generated MCP tool catalog is unavailable") from error
    try:
        metadata = os.fstat(descriptor)
        if not stat.S_ISREG(metadata.st_mode):
            raise ToolCatalogError("Generated MCP tool catalog is unsafe")
        with os.fdopen(descriptor, encoding="utf-8") as source:
            descriptor = -1
            value = json.load(source)
    except (OSError, json.JSONDecodeError) as error:
        raise ToolCatalogError("Generated MCP tool catalog is invalid") from error
    finally:
        if descriptor != -1:
            os.close(descriptor)
    return _validate_catalog(value)


def _catalog_directory(root: Path) -> Path:
    directory = root
    for part in CATALOG_PARTS[:-1]:
        directory /= part
        directory.mkdir(exist_ok=True)
        mode = os.lstat(directory).st_mode
        if stat.S_ISLNK(mode) or not stat.S_ISDIR(mode):
            raise ToolCatalogError("Generated MCP tool catalog path is unsafe")
    return directory


def write_catalog(root: str | Path, catalog: Mapping[str, Any]) -> Path:
    """Atomically publish a validated catalog under the selected project root."""

    checked = _validate_catalog(catalog)
    directory = _catalog_directory(_root(root))
    descriptor, temporary = tempfile.mkstemp(prefix=".tools_catalog.", suffix=".tmp", dir=directory)
    try:
        with os.fdopen(descriptor, "w", encoding="utf-8") as target:
            descriptor = -1
            json.dump(checked, target, ensure_ascii=False, separators=(",", ":"))
            target.write("\n")
            target.flush()
            os.fsync(target.fileno())
        os.replace(temporary, directory / CATALOG_PARTS[-1])
    except OSError as error:
        raise ToolCatalogError("Generated MCP tool catalog could not be written") from error
    finally:
        if descriptor != -1:
            os.close(descriptor)
        if os.path.exists(temporary):
            os.unlink(temporary)
    return directory / CATALOG_PARTS[-1]


__all__ = [
    "CATALOG_PARTS", "GROUPS", "ToolCatalogError", "build_catalog", "catalog_path", "group_for",
    "read_catalog", "write_catalog",
]
