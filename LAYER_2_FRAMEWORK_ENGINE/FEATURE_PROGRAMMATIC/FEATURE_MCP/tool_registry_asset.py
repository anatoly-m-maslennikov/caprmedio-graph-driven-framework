# CA-R-1106@21
# CA-M-506@2
# CA-D-704@1

"""Read and materialize the MCP package's code-owned registration asset."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from registered_tool_registry import (
    RegistrySnapshot,
    ToolRegistryAssetError,
    _snapshot,
    compile_registry,
)
from selected_route_spec import ADMITTED_SELECTED_ROUTE_NAMES


_INVENTORY = "tool_providers.json"
_ASSET = "tool_registry.json"


def registry_paths(package_root: str | Path) -> tuple[Path, Path]:
    root = Path(package_root).resolve(strict=True)
    mcp_root = root / "LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_MCP"
    if not mcp_root.is_dir():
        raise ToolRegistryAssetError("MCP package root is unavailable")
    return mcp_root / _INVENTORY, mcp_root / _ASSET


def _read_json(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as error:
        raise ToolRegistryAssetError(
            f"generated MCP registry is unavailable: {path.name}"
        ) from error
    if not isinstance(value, dict):
        raise ToolRegistryAssetError(f"generated MCP registry is invalid: {path.name}")
    return value


def provider_inventory(
    package_root: str | Path,
) -> tuple[tuple[dict[str, object], ...], tuple[str, ...]]:
    inventory_path, _asset_path = registry_paths(package_root)
    inventory = _read_json(inventory_path)
    if (
        set(inventory) != {"schema_version", "providers", "selected_route_names"}
        or inventory["schema_version"] != 1
    ):
        raise ToolRegistryAssetError("generated MCP registry is invalid: tool_providers.json")
    providers = inventory["providers"]
    selected = inventory["selected_route_names"]
    if not isinstance(providers, list) or not isinstance(selected, list):
        raise ToolRegistryAssetError("generated MCP registry is invalid: tool_providers.json")
    rows: list[dict[str, object]] = []
    for provider in providers:
        if not isinstance(provider, dict) or set(provider) != {"entrypoint", "mcp_name"}:
            raise ToolRegistryAssetError("generated MCP registry is invalid: tool provider")
        entrypoint, mcp_name = provider["entrypoint"], provider["mcp_name"]
        if (
            not isinstance(entrypoint, str)
            or not entrypoint
            or not (isinstance(mcp_name, str) or mcp_name is None)
        ):
            raise ToolRegistryAssetError("generated MCP registry is invalid: tool provider")
        rows.append({"entrypoint": entrypoint, "mcp_name": mcp_name})
    if not all(isinstance(name, str) and name for name in selected) or len(selected) != len(
        set(selected)
    ):
        raise ToolRegistryAssetError("generated MCP registry is invalid: selected route names")
    if not set(selected) <= set(ADMITTED_SELECTED_ROUTE_NAMES):
        raise ToolRegistryAssetError("generated MCP registry is invalid: selected route names")
    return tuple(rows), tuple(sorted(selected))


def generated_registry(package_root: str | Path) -> dict[str, object]:
    providers, selected = provider_inventory(package_root)
    snapshot = compile_registry(package_root, providers)
    if snapshot.quarantined:
        raise ToolRegistryAssetError("generated MCP registry rejected an installed provider")
    return {**snapshot.projection(), "selected_route_names": list(selected)}


def write_generated_registry(package_root: str | Path) -> dict[str, object]:
    _inventory_path, asset_path = registry_paths(package_root)
    registry = generated_registry(package_root)
    asset_path.write_text(
        json.dumps(registry, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n",
        encoding="utf-8",
    )
    return registry


def load_generated_registry(package_root: str | Path) -> tuple[RegistrySnapshot, tuple[str, ...]]:
    _inventory_path, asset_path = registry_paths(package_root)
    registry = _read_json(asset_path)
    required = {
        "schema_version",
        "tools",
        "quarantined",
        "withheld",
        "public_mcp_names",
        "digest",
        "selected_route_names",
    }
    if set(registry) != required or registry["schema_version"] != 1:
        raise ToolRegistryAssetError("generated MCP registry is invalid: tool_registry.json")
    if not all(
        isinstance(registry[key], list)
        for key in ("tools", "quarantined", "withheld", "public_mcp_names", "selected_route_names")
    ):
        raise ToolRegistryAssetError("generated MCP registry is invalid: tool_registry.json")
    if not all(
        isinstance(row, dict)
        for key in ("tools", "quarantined", "withheld")
        for row in registry[key]
    ):
        raise ToolRegistryAssetError("generated MCP registry is invalid: tool_registry.json")
    snapshot = _snapshot(registry["tools"], registry["quarantined"], withheld=registry["withheld"])
    if snapshot.projection() != {key: registry[key] for key in snapshot.projection()}:
        raise ToolRegistryAssetError("generated MCP registry digest is invalid")
    selected = registry["selected_route_names"]
    if not all(isinstance(name, str) and name for name in selected) or len(selected) != len(
        set(selected)
    ):
        raise ToolRegistryAssetError("generated MCP registry is invalid: selected route names")
    return snapshot, tuple(selected)
