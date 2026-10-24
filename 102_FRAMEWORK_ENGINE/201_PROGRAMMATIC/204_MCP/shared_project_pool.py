"""Bounded warm native gateways for the shared host MCP."""

from __future__ import annotations

import asyncio
from concurrent.futures import CancelledError as FutureCancelledError
from dataclasses import dataclass
import sys
from typing import Any, Callable

from project_selection import ProjectSelection
from runtime_failure_diagnostics import report_failure


class ProjectCapacityError(RuntimeError):
    """A request cannot load another Project without exceeding the host cap."""


@dataclass
class LoadedProject:
    selection: ProjectSelection
    gateway: Any
    in_flight: int = 0
    touched: int = 0


class SharedProjectPool:
    """Keep only a bounded number of initialized per-Project gateways warm."""

    def __init__(self, max_loaded_projects: int, gateway_factory: Callable[..., Any]) -> None:
        self.max_loaded_projects = max_loaded_projects
        self.gateway_factory = gateway_factory
        self._entries: dict[str, LoadedProject] = {}
        self._pending: set[str] = set()
        self._pending_tasks: dict[str, asyncio.Task[Any] | None] = {}
        self._closed = False
        self._clock = 0
        self._lock = asyncio.Lock()

    @staticmethod
    def _key(selection: ProjectSelection) -> str:
        return str(selection.root)

    def _touch(self, entry: LoadedProject) -> None:
        self._clock += 1
        entry.touched = self._clock

    @staticmethod
    def _stderr(message: str) -> None:
        try:
            sys.stderr.write(message)
            sys.stderr.flush()
        except FutureCancelledError:
            raise
        except Exception:
            pass

    def _report(self, selection: ProjectSelection | None, error: Exception, operation: str) -> None:
        _, secondary = report_failure(
            selection.root if selection is not None else None,
            error,
            component="MCP_POOL",
            operation=operation,
        )
        if secondary is not None:
            self._stderr("caprmedio: technical diagnostics unavailable\n")

    async def _close_gateway(
        self, selection: ProjectSelection | None, gateway: Any, operation: str
    ) -> None:
        closing = asyncio.create_task(gateway.close())
        try:
            await asyncio.shield(closing)
        except asyncio.CancelledError:
            await asyncio.shield(closing)
            raise
        except FutureCancelledError:
            raise
        except Exception as error:
            self._report(selection, error, operation)

    async def _cleanup_gateway(
        self, selection: ProjectSelection, gateway: Any, operation: str
    ) -> None:
        if gateway is not None:
            await self._close_gateway(selection, gateway, operation)

    async def _reserve(
        self, selection: ProjectSelection
    ) -> tuple[str, LoadedProject | None, LoadedProject | None]:
        key = self._key(selection)
        evicted = None
        current = asyncio.current_task()
        async with self._lock:
            if self._closed:
                raise ProjectCapacityError("Project gateway pool is closed")
            entry = self._entries.get(key)
            if entry is not None:
                entry.in_flight += 1
                self._touch(entry)
                return key, entry, None
            if key in self._pending:
                raise ProjectCapacityError("Selected Project gateway is initializing")
            if len(self._entries) + len(self._pending) >= self.max_loaded_projects:
                idle = [item for item in self._entries.values() if item.in_flight == 0]
                if not idle:
                    raise ProjectCapacityError("All loaded Project gateways are busy")
                evicted = min(idle, key=lambda item: item.touched)
                del self._entries[self._key(evicted.selection)]
            self._pending.add(key)
            self._pending_tasks[key] = current
        return key, entry, evicted

    async def acquire(self, selection: ProjectSelection) -> LoadedProject:
        """Reserve a gateway, evicting only an idle least-recently-used entry."""
        key, entry, evicted = await self._reserve(selection)
        if entry is not None:
            return entry
        gateway = None
        try:
            if evicted is not None:
                await self._close_gateway(
                    evicted.selection, evicted.gateway, "shared_project_pool.eviction_close"
                )
            gateway = self.gateway_factory(selection.root, selection=selection)
            await gateway.initialize()
            async with self._lock:
                if self._closed:
                    raise ProjectCapacityError("Project gateway pool is closed")
                else:
                    entry = LoadedProject(selection, gateway, in_flight=1)
                    self._touch(entry)
                    self._entries[key] = entry
                    return entry
        except asyncio.CancelledError, FutureCancelledError:
            await self._cleanup_gateway(selection, gateway, "shared_project_pool.cancelled_close")
            raise
        except Exception as error:
            await self._cleanup_gateway(selection, gateway, "shared_project_pool.failure_close")
            self._report(selection, error, "shared_project_pool.initialize")
            raise
        except BaseException:
            await self._cleanup_gateway(selection, gateway, "shared_project_pool.failure_close")
            raise
        finally:
            async with self._lock:
                self._pending.discard(key)
                self._pending_tasks.pop(key, None)

    async def release(self, entry: LoadedProject) -> None:
        async with self._lock:
            if entry.in_flight < 1:
                raise RuntimeError("Project gateway lease was already released")
            entry.in_flight -= 1
            self._touch(entry)

    async def close(self) -> None:
        current = asyncio.current_task()
        async with self._lock:
            if self._closed:
                return
            self._closed = True
            entries, self._entries = list(self._entries.values()), {}
            pending = [
                task
                for task in self._pending_tasks.values()
                if task is not None and task is not current
            ]
        for task in pending:
            if not task.done():
                task.cancel()
        if pending:
            await asyncio.gather(*pending, return_exceptions=True)
        async with self._lock:
            self._pending.clear()
            self._pending_tasks.clear()
        await asyncio.gather(
            *(
                self._close_gateway(entry.selection, entry.gateway, "shared_project_pool.close")
                for entry in entries
            )
        )

    def status(self) -> dict[str, int]:
        return {
            "loaded_projects": len(self._entries),
            "max_loaded_projects": self.max_loaded_projects,
        }


__all__ = ["LoadedProject", "ProjectCapacityError", "SharedProjectPool"]
