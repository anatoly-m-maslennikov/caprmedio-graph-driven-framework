# CA-R-3013@2
# CA-M-506@8
# CA-D-704@6
# CA-M-536@1

"""Generate the installed MCP Tool registry from one provider inventory."""

from __future__ import annotations

import argparse
import json
import logging
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator, SchemaError
from mcp import types

from tool_registry_assets import (
    REGISTRY_NAME,
    SCHEMA_VERSION,
    ToolRegistryAssetError,
    feature_root,
    provider_fields,
    read_inventory,
    stable_json,
)
from tool_registry_imports import provider_symbol


def _schema(value: Any, label: str) -> None:
    if value is None and label == "output":
        return
    if not isinstance(value, dict):
        raise ToolRegistryAssetError(f"tool-{label}-schema-invalid")
    try:
        Draft202012Validator.check_schema(value)
    except SchemaError as error:
        raise ToolRegistryAssetError(f"tool-{label}-schema-invalid") from error


def _tool_payloads(value: Any) -> tuple[list[dict[str, Any]], list[str]]:
    if not isinstance(value, (list, tuple)) or not value:
        raise ToolRegistryAssetError("tool-descriptor-factory-return-invalid")
    payloads: list[dict[str, Any]] = []
    names: list[str] = []
    for item in value:
        if not isinstance(item, types.Tool):
            raise ToolRegistryAssetError("tool-descriptor-invalid")
        try:
            payload = item.model_dump(mode="json", by_alias=True)
            valid = types.Tool.model_validate(payload)
        except (TypeError, ValueError) as error:
            raise ToolRegistryAssetError("tool-descriptor-invalid") from error
        if not isinstance(payload, dict) or valid.name != item.name:
            raise ToolRegistryAssetError("tool-descriptor-invalid")
        names.append(valid.name)
        try:
            _schema(valid.input_schema, "input")
            _schema(valid.output_schema, "output")
        except ToolRegistryAssetError as error:
            logging.getLogger(__name__).warning(
                json.dumps({
                    "severity": "WARNING", "event": "TOOL_DESCRIPTOR_INVALID",
                    "tool": valid.name, "reason": str(error),
                }, sort_keys=True)
            )
            continue
        payloads.append(payload)
    return payloads, names


def _provider_payload(asset_root: Path, entry: Any) -> tuple[dict[str, Any], list[str]]:
    descriptor_factory = provider_symbol(asset_root, entry, "descriptor_factory")
    provider_symbol(asset_root, entry, "factory")
    try:
        tools, names = _tool_payloads(descriptor_factory())
    except ToolRegistryAssetError:
        raise
    except Exception as error:
        raise ToolRegistryAssetError("tool-descriptor-factory-failed") from error
    return {**provider_fields(entry), "tools": tools}, names


def _names(providers: list[dict[str, Any]]) -> list[str]:
    names = [tool["name"] for provider in providers for tool in provider["tools"]]
    if len(names) != len(set(names)):
        raise ToolRegistryAssetError("tool-descriptor-name-duplicates")
    return names


def generate(package_root: Path | str) -> Path:
    root = feature_root(package_root)
    inventory = read_inventory(root)
    provider_results = [_provider_payload(root, entry) for entry in inventory.providers]
    all_names = [name for _, names in provider_results for name in names]
    if len(all_names) != len(set(all_names)):
        raise ToolRegistryAssetError("tool-descriptor-name-duplicates")
    providers = [provider for provider, _ in provider_results]
    names = _names(providers)
    if not names:
        raise ToolRegistryAssetError("tool-descriptor-frontier-empty")
    payload = {
        "schema_version": SCHEMA_VERSION,
        "inventory_sha256": inventory.digest,
        "mcp_blacklist": list(inventory.blacklist),
        "providers": providers,
        "public_tools": [name for name in names if name not in inventory.blacklist],
    }
    destination = root / REGISTRY_NAME
    try:
        destination.write_text(stable_json(payload) + "\n", encoding="utf-8")
    except OSError as error:
        raise ToolRegistryAssetError("generated-tool-registry-write-failed") from error
    return destination


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--package-root", required=True, type=Path)
    arguments = parser.parse_args(argv)
    try:
        print(generate(arguments.package_root))
    except ToolRegistryAssetError as error:
        parser.error(str(error))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
