# Implementation of:
# Requirement: CA-R-3013
# Method: CA-M-506
# Delivery: CA-D-704

"""Import configured Provider symbols only from an installed MCP package."""

from __future__ import annotations

from contextlib import contextmanager
import importlib
from pathlib import Path
import sys
from typing import Any, Iterator

from tool_registry_assets import ProviderInventory, ToolRegistryAssetError


@contextmanager
def package_import_path(asset_root: Path) -> Iterator[None]:
    paths = [asset_root, asset_root.parent / "FEATURE_TOOLS", asset_root.parent / "FEATURE_APPS"]
    original = list(sys.path)
    sys.path[:0] = [str(path) for path in paths]
    try:
        yield
    finally:
        sys.path[:] = original


def _module(asset_root: Path, entry: ProviderInventory) -> Any:
    with package_import_path(asset_root):
        importlib.invalidate_caches()
        try:
            module = importlib.import_module(entry.module)
        except Exception as error:
            raise ToolRegistryAssetError("tool-provider-module-unavailable") from error
    origin = getattr(module, "__file__", None)
    try:
        if not isinstance(origin, str) or not Path(origin).resolve().is_relative_to(asset_root.resolve()):
            raise ToolRegistryAssetError("tool-provider-module-outside-package")
    except OSError as error:
        raise ToolRegistryAssetError("tool-provider-module-unavailable") from error
    return module


def provider_symbol(asset_root: Path, entry: ProviderInventory, field: str) -> Any:
    module = _module(asset_root, entry)
    symbol = getattr(module, getattr(entry, field), None)
    if not callable(symbol):
        raise ToolRegistryAssetError(f"tool-provider-{field}-unavailable")
    return symbol


__all__ = ["package_import_path", "provider_symbol"]
