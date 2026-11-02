"""Source-bound Codex CLI transport for one Implementation Workflow callback.

The returned mapping is intentionally the same narrow shape consumed by
``implementation_actions``: ``result``, ``outputs``, ``evidence`` and
``blockers``.  This transport does not register itself, advance a Workflow, or
apply Project effects.  A caller must explicitly admit a disposable workspace
before the delegated CLI is allowed to use ``workspace-write``.
"""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from pathlib import Path
from typing import Any

from implementation_agent_contracts import (
    ADMITTED_RESULTS,
    MAX_INPUT_BYTES,
    MAX_OUTPUT_BYTES,
    MAX_TRACKED_FILE_BYTES,
    MAX_TRACKED_FILES,
    MAX_TRACKED_TOTAL_BYTES,
    blocked as _blocked,
)
from implementation_agent_transport import dispatch as _dispatch_transport
from implementation_agent_transport import run as _run
from implementation_agent_workspace import (
    snapshot as _snapshot,
    stdin as _stdin,
    timeout as _timeout,
    workspace as _workspace,
    workspace_write_admitted as _workspace_write_admitted,
)


__all__ = [
    "ImplementationAgent",
    "DEFAULT_TIMEOUT_SECONDS",
    "ADMITTED_RESULTS",
    "MAX_INPUT_BYTES",
    "MAX_OUTPUT_BYTES",
    "MAX_TRACKED_FILE_BYTES",
    "MAX_TRACKED_FILES",
    "MAX_TRACKED_TOTAL_BYTES",
    "_run",
    "_snapshot",
    "_workspace",
    "_workspace_write_admitted",
]


DEFAULT_TIMEOUT_SECONDS = 600


class ImplementationAgent:
    """A replaceable ``(prompt, packet)`` Codex CLI-compatible transport.

    ``packet["workspace"]`` must name the existing directory supplied to the
    Agent.  The default invocation is read-only.  To allow implementation work,
    ``packet["permissions"]["implementation_workspace"]`` must be exactly an
    explicit capability mapping with ``kind: disposable_workspace``, the same
    absolute ``path``, and ``allow_write: true``.  The declaration is a caller
    admission, not proof that an arbitrary directory is disposable.
    """

    def __init__(
        self,
        executable: str | Sequence[str] = "codex",
        *,
        default_timeout_seconds: int = DEFAULT_TIMEOUT_SECONDS,
    ) -> None:
        if isinstance(executable, str):
            executable = (executable,)
        if not executable or not all(isinstance(part, str) and part for part in executable):
            raise ValueError("Codex executable is required")
        if not isinstance(default_timeout_seconds, int) or default_timeout_seconds < 1:
            raise ValueError("default timeout must be a positive integer")
        self.executable = tuple(executable)
        self.default_timeout_seconds = default_timeout_seconds

    def __call__(self, prompt: str, packet: Mapping[str, Any]) -> dict[str, Any]:
        return self.execute(prompt, packet)

    def execute(self, prompt: str, packet: Mapping[str, Any]) -> dict[str, Any]:
        """Run one bounded callback and return a truthful current result mapping."""
        if not isinstance(prompt, str) or not prompt.strip():
            return _blocked("Implementation Agent requires a nonempty Action prompt")
        if not isinstance(packet, Mapping):
            return _blocked("Implementation Agent requires an input packet mapping")
        try:
            workspace = _workspace(packet)
            write_admitted = _workspace_write_admitted(packet, workspace)
            timeout = _timeout(packet, self.default_timeout_seconds)
            before = _snapshot(workspace)
            stdin = _stdin(prompt, packet)
        except (OSError, TypeError, ValueError) as error:
            return _blocked(str(error))
        return _dispatch_transport(
            self.command,
            stdin,
            workspace,
            write_admitted,
            timeout,
            before,
            _run,
        )

    def command(
        self,
        workspace: Path,
        sandbox: str,
        schema_path: Path,
        output_path: Path,
    ) -> list[str]:
        """Build the documented non-interactive invocation without auth/model overrides."""
        return [
            *self.executable,
            "exec",
            "--ephemeral",
            "--ignore-user-config",
            "--sandbox",
            sandbox,
            "--ask-for-approval",
            "never",
            "--cd",
            str(workspace),
            "--skip-git-repo-check",
            "--color",
            "never",
            "--output-schema",
            str(schema_path),
            "--output-last-message",
            str(output_path),
            "-",
        ]
