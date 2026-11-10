# CA-R-3013@2
# CA-R-1108@23
# CA-M-506@6
# CA-M-512@2
# CA-D-704@5

"""Load only the generated MCP Tool registry and dispatch registered Providers."""

from __future__ import annotations

from dataclasses import dataclass
import inspect
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator, SchemaError, ValidationError
from mcp import types

from generate_tool_registry import _tool_payloads
from tool_registry_assets import (
    INVENTORY_NAME,
    REGISTRY_NAME,
    SCHEMA_VERSION,
    ProviderInventory,
    ToolInventory,
    ToolRegistryAssetError,
    inventory_digest,
    provider_fields,
    read_inventory,
    read_json,
    stable_json,
)
from tool_registry_imports import provider_symbol


_REGISTRY_KEYS = frozenset(
    {"schema_version", "inventory_sha256", "mcp_blacklist", "providers", "public_tools"}
)
_GENERATED_PROVIDER_KEYS = frozenset(
    {"provider_id", "module", "factory", "descriptor_factory", "tools"}
)


class ToolRegistryRuntimeError(RuntimeError):
    """A runtime cannot safely expose an incomplete or stale registry."""


class ToolRegistryStaleError(ToolRegistryRuntimeError):
    """Installed registration changed since this runtime loaded it."""


class ToolInputValidationError(ValueError):
    """The request does not meet the registered generic Tool contract."""


class ToolOutputValidationError(RuntimeError):
    """A Provider returned data outside its registered generic Tool contract."""


async def _await(value: Any) -> Any:
    return await value if inspect.isawaitable(value) else value


async def _close(value: Any) -> None:
    close = getattr(value, "close", None)
    if callable(close):
        try:
            await _await(close())
        except Exception:
            return


@dataclass
class ProviderBinding:
    factory: Any
    root: Path
    gateway: Any
    provider: Any = None

    async def resolve(self) -> Any:
        if self.provider is not None:
            return self.provider
        try:
            candidate = await _await(self.factory(self.root, self.gateway))
        except Exception as error:
            raise ToolRegistryRuntimeError("tool-provider-factory-failed") from error
        if not callable(getattr(candidate, "call", None)) or not callable(getattr(candidate, "close", None)):
            await _close(candidate)
            raise ToolRegistryRuntimeError("tool-provider-contract-invalid")
        self.provider = candidate
        return candidate

    async def close(self) -> None:
        if self.provider is not None:
            provider, self.provider = self.provider, None
            await _close(provider)


@dataclass(frozen=True)
class RegisteredTool:
    binding: ProviderBinding
    input_validator: Draft202012Validator
    output_validator: Draft202012Validator | None


@dataclass
class ActiveToolRegistry:
    tools: tuple[types.Tool, ...]
    routes: dict[str, RegisteredTool]
    bindings: tuple[ProviderBinding, ...]
    global_blacklist: frozenset[str]
    asset_root: Path
    registry_revision: str
    inventory_revision: str

    def ensure_current(self) -> None:
        try:
            current_registry = inventory_digest(self.asset_root / REGISTRY_NAME)
            current_inventory = inventory_digest(self.asset_root / INVENTORY_NAME)
        except ToolRegistryAssetError as error:
            raise ToolRegistryStaleError("tool-registry-stale") from error
        if (current_registry, current_inventory) != (
            self.registry_revision,
            self.inventory_revision,
        ):
            raise ToolRegistryStaleError("tool-registry-stale")

    def permits(self, name: str) -> bool:
        return name not in self.global_blacklist and name in self.routes

    async def call(self, name: str, arguments: dict[str, Any], *, context: Any = None) -> dict[str, Any]:
        self.ensure_current()
        if not self.permits(name):
            raise ToolRegistryRuntimeError("tool-unavailable")
        registered = self.routes[name]
        try:
            registered.input_validator.validate(arguments)
        except ValidationError as error:
            raise ToolInputValidationError("tool-input-invalid") from error
        provider = await registered.binding.resolve()
        arguments = await _provider_hook(provider, "prepare_arguments", name, arguments, context)
        self.ensure_current()
        value = await _await(provider.call(name, arguments))
        if not isinstance(value, dict):
            raise ToolOutputValidationError("tool-provider-result-invalid")
        if registered.output_validator is not None:
            try:
                registered.output_validator.validate(value)
            except ValidationError as error:
                raise ToolOutputValidationError("tool-output-invalid") from error
        return await _provider_hook(provider, "present_result", name, value, context)

    async def close(self) -> None:
        for binding in self.bindings:
            await binding.close()


async def _provider_hook(provider: Any, name: str, tool: str, value: dict[str, Any], context: Any) -> dict[str, Any]:
    hook = getattr(provider, name, None)
    result = await _await(hook(tool, value, context)) if callable(hook) else value
    if not isinstance(result, dict):
        raise ToolRegistryRuntimeError(f"tool-provider-{name}-invalid")
    return result


def _runtime_error(error: Exception) -> ToolRegistryRuntimeError:
    return ToolRegistryRuntimeError(f"tool-registry-unavailable: {error}")


def _registry(asset_root: Path, inventory: ToolInventory) -> dict[str, Any]:
    value = read_json(asset_root / REGISTRY_NAME, "generated-tool-registry")
    version = value.get("schema_version")
    if (set(value) != _REGISTRY_KEYS or type(version) is not int
            or version != SCHEMA_VERSION):
        raise ToolRegistryAssetError("generated-tool-registry-schema-invalid")
    if value.get("inventory_sha256") != inventory.digest:
        raise ToolRegistryAssetError("generated-tool-registry-stale")
    if value.get("mcp_blacklist") != list(inventory.blacklist):
        raise ToolRegistryAssetError("generated-tool-registry-blacklist-invalid")
    if not isinstance(value.get("providers"), list) or not isinstance(value.get("public_tools"), list):
        raise ToolRegistryAssetError("generated-tool-registry-fields-invalid")
    return value


def _provider_rows(value: dict[str, Any], inventory: ToolInventory) -> list[dict[str, Any]]:
    rows = value["providers"]
    if len(rows) != len(inventory.providers):
        raise ToolRegistryAssetError("generated-tool-registry-provider-count-invalid")
    for row, entry in zip(rows, inventory.providers, strict=True):
        if not isinstance(row, dict) or set(row) != _GENERATED_PROVIDER_KEYS:
            raise ToolRegistryAssetError("generated-tool-registry-provider-invalid")
        if {key: row[key] for key in _GENERATED_PROVIDER_KEYS - {"tools"}} != provider_fields(entry):
            raise ToolRegistryAssetError("generated-tool-registry-provider-stale")
        if not isinstance(row["tools"], list):
            raise ToolRegistryAssetError("generated-tool-registry-tools-invalid")
    return rows


def _validator(schema: Any, label: str) -> Draft202012Validator | None:
    if schema is None and label == "output":
        return None
    if not isinstance(schema, dict):
        raise ToolRegistryAssetError(f"tool-{label}-schema-invalid")
    try:
        Draft202012Validator.check_schema(schema)
    except SchemaError as error:
        raise ToolRegistryAssetError(f"tool-{label}-schema-invalid") from error
    return Draft202012Validator(schema)


def _tools(
    entry: ProviderInventory, row: dict[str, Any], asset_root: Path
) -> tuple[tuple[types.Tool, ...], list[str]]:
    factory = provider_symbol(asset_root, entry, "descriptor_factory")
    try:
        current, names = _tool_payloads(factory())
    except Exception as error:
        raise ToolRegistryAssetError("tool-descriptor-factory-failed") from error
    if stable_json(current) != stable_json(row["tools"]):
        raise ToolRegistryAssetError("generated-tool-registry-descriptor-stale")
    try:
        tools = tuple(types.Tool.model_validate(tool) for tool in row["tools"])
    except (TypeError, ValueError) as error:
        raise ToolRegistryAssetError("generated-tool-registry-tools-invalid") from error
    for tool in tools:
        _validator(tool.input_schema, "input")
        _validator(tool.output_schema, "output")
    return tools, names


def _public_names(value: dict[str, Any], known: list[str], blacklist: frozenset[str]) -> set[str]:
    names = value["public_tools"]
    if not all(isinstance(name, str) for name in names) or len(names) != len(set(names)):
        raise ToolRegistryAssetError("generated-tool-registry-public-tools-invalid")
    expected = {name for name in known if name not in blacklist}
    if set(names) != expected:
        raise ToolRegistryAssetError("generated-tool-registry-public-tools-stale")
    return expected


def load_active_registry(asset_root: Path, root: Path, gateway: Any) -> ActiveToolRegistry:
    try:
        registry_revision = inventory_digest(asset_root / REGISTRY_NAME)
        inventory = read_inventory(asset_root)
        value = _registry(asset_root, inventory)
        rows = _provider_rows(value, inventory)
        tool_results = [
            _tools(entry, row, asset_root)
            for entry, row in zip(inventory.providers, rows, strict=True)
        ]
        tools_by_provider = [tools for tools, _ in tool_results]
        names = [name for _, provider_names in tool_results for name in provider_names]
        if len(names) != len(set(names)):
            raise ToolRegistryAssetError("generated-tool-registry-tool-duplicates")
        blacklist = frozenset(inventory.blacklist)
        valid_names = [tool.name for tools in tools_by_provider for tool in tools]
        if not valid_names:
            raise ToolRegistryAssetError("generated-tool-registry-frontier-empty")
        public = _public_names(value, valid_names, blacklist)
        bindings = tuple(
            ProviderBinding(provider_symbol(asset_root, entry, "factory"), root, gateway)
            for entry in inventory.providers
        )
        routes = {
            tool.name: RegisteredTool(binding, _validator(tool.input_schema, "input"), _validator(tool.output_schema, "output"))
            for binding, tools in zip(bindings, tools_by_provider, strict=True)
            for tool in tools if tool.name in public
        }
        tools = tuple(tool for tools in tools_by_provider for tool in tools if tool.name in public)
        active = ActiveToolRegistry(
            tools, routes, bindings, blacklist, asset_root, registry_revision, inventory.digest
        )
        active.ensure_current()
        return active
    except ToolRegistryAssetError as error:
        raise _runtime_error(error) from error


__all__ = [
    "ActiveToolRegistry", "ToolInputValidationError", "ToolOutputValidationError",
    "ToolRegistryRuntimeError", "ToolRegistryStaleError", "load_active_registry",
]
