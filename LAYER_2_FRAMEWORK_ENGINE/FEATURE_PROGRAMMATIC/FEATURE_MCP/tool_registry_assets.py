# CA-M-506@8
# CA-D-704@6

"""Strict asset formats for generated MCP tool registration."""

from __future__ import annotations

from dataclasses import dataclass
import hashlib
import json
from pathlib import Path
import re
from typing import Any


SCHEMA_VERSION = 1
FEATURE_RELATIVE = Path("LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_MCP")
INVENTORY_NAME = "tool_providers.json"
REGISTRY_NAME = "tool_registry.json"
_TOOL_NAME = re.compile(r"[A-Za-z][A-Za-z0-9_.-]*\Z")
_IDENTIFIER = re.compile(r"[A-Za-z_][A-Za-z0-9_]*\Z")
_INVENTORY_KEYS = frozenset({"schema_version", "mcp_blacklist", "providers"})
_PROVIDER_KEYS = frozenset({"provider_id", "module", "factory", "descriptor_factory"})


class ToolRegistryAssetError(ValueError):
    """One installed registry asset is missing, stale, or malformed."""


@dataclass(frozen=True)
class ProviderInventory:
    provider_id: str
    module: str
    factory: str
    descriptor_factory: str


@dataclass(frozen=True)
class ToolInventory:
    blacklist: tuple[str, ...]
    providers: tuple[ProviderInventory, ...]
    digest: str


def feature_root(package_root: Path | str) -> Path:
    root = Path(package_root)
    candidate = root / FEATURE_RELATIVE
    if not candidate.is_dir():
        raise ToolRegistryAssetError("package-feature-root-unavailable")
    return candidate


def read_json(path: Path, label: str) -> dict[str, Any]:
    def unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
        value: dict[str, Any] = {}
        for key, item in pairs:
            if key in value:
                raise ToolRegistryAssetError(f"{label}-contains-duplicate-key")
            value[key] = item
        return value

    try:
        value = json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=unique_object)
    except (OSError, UnicodeDecodeError, json.JSONDecodeError, ToolRegistryAssetError) as error:
        raise ToolRegistryAssetError(f"{label}-unavailable-or-invalid") from error
    if not isinstance(value, dict):
        raise ToolRegistryAssetError(f"{label}-must-be-an-object")
    return value


def inventory_digest(path: Path) -> str:
    try:
        return hashlib.sha256(path.read_bytes()).hexdigest()
    except OSError as error:
        raise ToolRegistryAssetError("tool-inventory-unavailable") from error


def _text(value: Any, label: str, *, pattern: re.Pattern[str] = _IDENTIFIER) -> str:
    if not isinstance(value, str) or pattern.fullmatch(value) is None:
        raise ToolRegistryAssetError(f"{label}-invalid")
    return value


def _names(value: Any, label: str) -> tuple[str, ...]:
    if not isinstance(value, list):
        raise ToolRegistryAssetError(f"{label}-must-be-a-list")
    names = tuple(_text(item, label, pattern=_TOOL_NAME) for item in value)
    if len(names) != len(set(names)):
        raise ToolRegistryAssetError(f"{label}-contains-duplicates")
    return names


def _provider(value: Any) -> ProviderInventory:
    if not isinstance(value, dict) or set(value) != _PROVIDER_KEYS:
        raise ToolRegistryAssetError("tool-provider-fields-invalid")
    module = value["module"]
    if not isinstance(module, str) or not module:
        raise ToolRegistryAssetError("tool-provider-module-invalid")
    if any(_IDENTIFIER.fullmatch(part) is None for part in module.split(".")):
        raise ToolRegistryAssetError("tool-provider-module-invalid")
    return ProviderInventory(
        _text(value["provider_id"], "tool-provider-id"),
        module,
        _text(value["factory"], "tool-provider-factory"),
        _text(value["descriptor_factory"], "tool-provider-descriptor-factory"),
    )


def read_inventory(asset_root: Path) -> ToolInventory:
    path = asset_root / INVENTORY_NAME
    value = read_json(path, "tool-inventory")
    version = value.get("schema_version")
    if (set(value) != _INVENTORY_KEYS or type(version) is not int
            or version != SCHEMA_VERSION):
        raise ToolRegistryAssetError("tool-inventory-schema-invalid")
    blacklist = _names(value["mcp_blacklist"], "mcp-blacklist")
    providers_value = value["providers"]
    if not isinstance(providers_value, list) or not providers_value:
        raise ToolRegistryAssetError("tool-providers-must-be-a-nonempty-list")
    providers = tuple(_provider(item) for item in providers_value)
    if len({item.provider_id for item in providers}) != len(providers):
        raise ToolRegistryAssetError("tool-provider-id-duplicates")
    return ToolInventory(blacklist, providers, inventory_digest(path))


def provider_fields(entry: ProviderInventory) -> dict[str, str]:
    return {
        "provider_id": entry.provider_id,
        "module": entry.module,
        "factory": entry.factory,
        "descriptor_factory": entry.descriptor_factory,
    }


def stable_json(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


__all__ = [
    "FEATURE_RELATIVE",
    "INVENTORY_NAME",
    "REGISTRY_NAME",
    "SCHEMA_VERSION",
    "ProviderInventory",
    "ToolInventory",
    "ToolRegistryAssetError",
    "feature_root",
    "provider_fields",
    "read_inventory",
    "read_json",
    "stable_json",
]
