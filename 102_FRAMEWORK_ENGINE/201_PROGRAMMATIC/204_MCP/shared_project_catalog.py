"""A bounded, startup-time public Tool frontier for the shared MCP."""

from __future__ import annotations

import asyncio
from concurrent.futures import CancelledError as FutureCancelledError
from dataclasses import dataclass, field
from pathlib import Path
import os
from typing import Any, Callable

from mcp import types

from hot_reload import CONTROL, STATUS
from host_runtime_config import HostRuntimeConfig, resolve_host_project
from operation_error_boundary import FailureRecord
from project_selection import ProjectSelection
from runtime_failure_diagnostics import report_failure
from shared_tool_contract import ToolContract, contract_digest, public_tool

MAX_PROJECT_CANDIDATES = 256


@dataclass
class SharedToolFrontier:
    tools: dict[str, ToolContract] = field(default_factory=dict)
    project_contracts: dict[str, dict[str, str]] = field(default_factory=dict)
    quarantined: set[str] = field(default_factory=set)
    warnings: list[dict[str, str]] = field(default_factory=list)

    def warning(self, code: str, root: Path | None = None, tool: str | None = None) -> None:
        row = {"code": code}
        if root is not None:
            row["project_root"] = str(root)
        if tool is not None:
            row["tool"] = tool
        try:
            secondary = report_failure(
                root,
                FailureRecord("WARNING", code, "shared MCP catalog warning"),
                component="SHARED_MCP_CATALOG",
                operation="frontier_discovery",
            )[1]
        except FutureCancelledError:
            raise
        except Exception:
            secondary = "technical diagnostic emission failed"
        if secondary:
            row["diagnostic_error"] = secondary
        self.warnings.append(row)


def native_tools(gateway: Any) -> list[types.Tool]:
    """Read the native, initialized frontier without reconstructing a Tool."""
    active = getattr(gateway, "active", None)
    if active is None:
        raise RuntimeError("Project Gateway has no active generation")
    blocked = getattr(gateway, "tool_blacklist", frozenset())
    return [tool for tool in (CONTROL, STATUS, *active.tools) if tool.name not in blocked]


def _has_marker(root: Path, frontier: SharedToolFrontier) -> bool:
    try:
        with os.scandir(root) as nested:
            for index, entry in enumerate(nested):
                if index >= MAX_PROJECT_CANDIDATES:
                    frontier.warning("PROJECT_MARKER_SCAN_BOUND_REACHED")
                    break
                if entry.name.startswith(".caprmedio_"):
                    return True
    except OSError:
        frontier.warning("PROJECT_CANDIDATE_UNAVAILABLE")
    return False


def _candidate_paths(config: HostRuntimeConfig, frontier: SharedToolFrontier) -> list[Path]:
    entries: list[Path] = []
    try:
        with os.scandir(config.projects_root) as children:
            visited = 0
            for child in children:
                try:
                    is_symlink = child.is_symlink()
                    is_directory = child.is_dir(follow_symlinks=False)
                except OSError:
                    frontier.warning("PROJECT_CANDIDATE_UNAVAILABLE")
                    continue
                if is_symlink or not is_directory:
                    continue
                if visited >= MAX_PROJECT_CANDIDATES:
                    frontier.warning("PROJECT_CATALOG_SCAN_BOUND_REACHED")
                    break
                visited += 1
                root = Path(child.path)
                if _has_marker(root, frontier):
                    entries.append(root)
    except OSError:
        frontier.warning("PROJECT_CATALOG_READ_FAILED")
    return sorted(entries)


def _add_project(
    frontier: SharedToolFrontier, selection: ProjectSelection, tools: list[types.Tool]
) -> None:
    contracts: dict[str, str] = {}
    for native in tools:
        try:
            candidate = public_tool(native)
            digest = contract_digest(native)
        except TypeError, ValueError:
            frontier.warning("PROJECT_TOOL_CONTRACT_INVALID", selection.root, native.name)
            continue
        contracts[native.name] = digest
        existing = frontier.tools.get(native.name)
        if existing is None:
            frontier.tools[native.name] = ToolContract(candidate, digest)
        elif existing.digest != digest:
            frontier.quarantined.add(native.name)
            frontier.warning("PROJECT_TOOL_CONTRACT_CONFLICT", selection.root, native.name)
            for root, contracts in frontier.project_contracts.items():
                if native.name in contracts:
                    frontier.warning("PROJECT_TOOL_CONTRACT_CONFLICT", Path(root), native.name)
    frontier.project_contracts[str(selection.root)] = contracts


async def _discover_project(
    config: HostRuntimeConfig,
    root: Path,
    gateway_factory: Callable[..., Any],
    frontier: SharedToolFrontier,
) -> None:
    gateway = None
    selection = None
    try:
        selection = resolve_host_project(config, root)
        if selection.root.parent != config.projects_root:
            raise ValueError("Project root is not a direct host child")
        gateway = gateway_factory(selection.root, selection=selection)
        await gateway.initialize()
        _add_project(frontier, selection, native_tools(gateway))
    except asyncio.CancelledError, FutureCancelledError:
        raise
    except OSError, RuntimeError, TypeError, ValueError, KeyError:
        frontier.warning("PROJECT_CANDIDATE_INVALID", selection.root if selection else None)
    finally:
        if gateway is not None:
            try:
                await gateway.close()
            except asyncio.CancelledError, FutureCancelledError:
                raise
            except OSError, RuntimeError, TypeError, ValueError, KeyError:
                frontier.warning(
                    "PROJECT_CANDIDATE_CLOSE_FAILED", selection.root if selection else None
                )


async def discover_frontier(
    config: HostRuntimeConfig, gateway_factory: Callable[..., Any]
) -> SharedToolFrontier:
    """Eagerly union direct child Projects; discovery children never stay warm."""
    frontier = SharedToolFrontier()
    try:
        roots = _candidate_paths(config, frontier)
    except asyncio.CancelledError, FutureCancelledError:
        raise
    except OSError, RuntimeError, TypeError, ValueError:
        frontier.warning("PROJECT_CATALOG_READ_FAILED")
        roots = []
    for root in roots:
        await _discover_project(config, root, gateway_factory, frontier)
    for name in frontier.quarantined:
        frontier.tools.pop(name, None)
    return frontier


__all__ = [
    "SharedToolFrontier",
    "ToolContract",
    "contract_digest",
    "discover_frontier",
    "native_tools",
    "public_tool",
]
