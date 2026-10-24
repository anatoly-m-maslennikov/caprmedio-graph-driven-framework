"""Deterministic fake gateways for shared Project pool tests."""

from __future__ import annotations

import asyncio
from pathlib import Path
from types import SimpleNamespace


class _Gate:
    def __init__(self, behavior):
        self.behavior = behavior
        self.initialize_started = behavior.get("initialize_started")
        self.initialize_release = behavior.get("initialize_release")
        self.closed = 0

    async def initialize(self):
        if self.initialize_started is not None:
            self.initialize_started.set()
        if self.initialize_release is not None:
            try:
                await self.initialize_release.wait()
            except asyncio.CancelledError:
                if not self.behavior.get("ignore_initialize_cancel"):
                    raise
                await self.initialize_release.wait()
        if self.behavior.get("initialize_error") is not None:
            raise self.behavior["initialize_error"]

    async def close(self):
        self.closed += 1
        if self.behavior.get("close_release") is not None:
            await self.behavior["close_release"].wait()
        if self.behavior.get("close_error") is not None:
            raise self.behavior["close_error"]


class _Factory:
    def __init__(self, behaviors=None):
        self.behaviors = behaviors or {}
        self.gates = {}

    def __call__(self, root, *, selection):
        gate = _Gate(self.behaviors.get(str(root), {}))
        self.gates[str(root)] = gate
        return gate


def _selection(name):
    return SimpleNamespace(root=Path("/projects") / name)
