"""Bounded temporary runtime and subprocess effect for the transport."""

from __future__ import annotations

from collections.abc import Callable, Mapping, Sequence
import json
import os
from pathlib import Path
import signal
import subprocess
import tempfile
from typing import Any

from implementation_agent_contracts import (
    admit_response,
    blocked,
    output_schema,
    read_output,
    transport_evidence,
)
from implementation_agent_workspace import post_dispatch_changes


def dispatch(
    command_factory: Callable[[Path, str, Path, Path], Sequence[str]],
    stdin: str,
    workspace: Path,
    write_admitted: bool,
    timeout: int,
    before: Mapping[str, str],
    run_command: Callable[[Sequence[str], str, int, Path, Path], int],
) -> dict[str, Any]:
    sandbox = "workspace-write" if write_admitted else "read-only"
    # Keep CLI artifacts outside the caller workspace; cleanup may be denied by a managed sandbox.
    with tempfile.TemporaryDirectory(
        prefix="caprmedio-implementation-agent-", ignore_cleanup_errors=True
    ) as runtime:
        runtime_path = Path(runtime)
        schema_path = runtime_path / "output.schema.json"
        output_path = runtime_path / "output.json"
        stdout_path = runtime_path / "stdout.log"
        stderr_path = runtime_path / "stderr.log"
        schema_path.write_text(json.dumps(output_schema(), sort_keys=True), encoding="utf-8")
        command = command_factory(workspace, sandbox, schema_path, output_path)
        outcome = _run_dispatch(
            command,
            stdin,
            timeout,
            stdout_path,
            stderr_path,
            before,
            workspace,
            sandbox,
            run_command,
        )
        if isinstance(outcome, dict):
            return outcome
        return _complete_dispatch(outcome, output_path, write_admitted, sandbox, timeout)


def _run_dispatch(
    command: Sequence[str],
    stdin: str,
    timeout: int,
    stdout_path: Path,
    stderr_path: Path,
    before: Mapping[str, str],
    workspace: Path,
    sandbox: str,
    run_command: Callable[[Sequence[str], str, int, Path, Path], int],
) -> tuple[int, list[dict[str, str | None]], str | None] | dict[str, Any]:
    try:
        returncode = run_command(command, stdin, timeout, stdout_path, stderr_path)
    except subprocess.TimeoutExpired:
        changes, snapshot_error = post_dispatch_changes(before, workspace)
        blockers = ["Codex Implementation Agent timed out; reconcile the bounded dispatch"]
        if snapshot_error:
            blockers.append(snapshot_error)
        return blocked(
            blockers[0],
            evidence=[transport_evidence(sandbox, timeout, "timeout", changes=changes)],
            blockers=blockers,
        )
    except OSError as error:
        return blocked(
            "Codex Implementation Agent could not start",
            evidence=[transport_evidence(sandbox, timeout, "launch_failed")],
            blockers=[f"{type(error).__name__}: {error}"],
        )
    changes, snapshot_error = post_dispatch_changes(before, workspace)
    return returncode, changes, snapshot_error


def _complete_dispatch(
    outcome: tuple[int, list[dict[str, str | None]], str | None],
    output_path: Path,
    write_admitted: bool,
    sandbox: str,
    timeout: int,
) -> dict[str, Any]:
    returncode, changes, snapshot_error = outcome
    if returncode != 0:
        return _nonzero_result(
            returncode, changes, snapshot_error, write_admitted, sandbox, timeout
        )
    try:
        response = read_output(output_path)
        if snapshot_error:
            raise ValueError(snapshot_error)
        return admit_response(response, changes, write_admitted, sandbox, timeout)
    except (OSError, TypeError, ValueError, json.JSONDecodeError) as error:
        blockers = [str(error)]
        if snapshot_error and snapshot_error not in blockers:
            blockers.append(snapshot_error)
        return blocked(
            "Codex Implementation Agent returned invalid or missing bounded output",
            evidence=[transport_evidence(sandbox, timeout, "invalid_output", changes=changes)],
            blockers=blockers,
        )


def _nonzero_result(
    returncode: int,
    changes: list[dict[str, str | None]],
    snapshot_error: str | None,
    write_admitted: bool,
    sandbox: str,
    timeout: int,
) -> dict[str, Any]:
    blockers = ["Codex Implementation Agent exited without an admitted result"]
    if changes and not write_admitted:
        blockers.append(
            "Agent changed the workspace without an admitted disposable write capability"
        )
    if snapshot_error:
        blockers.append(snapshot_error)
    return blocked(
        blockers[0],
        evidence=[
            transport_evidence(sandbox, timeout, "nonzero_exit", returncode, changes=changes)
        ],
        blockers=blockers,
    )


def run(
    command: Sequence[str],
    prompt: str,
    timeout: int,
    stdout_path: Path,
    stderr_path: Path,
) -> int:
    with stdout_path.open("wb") as stdout, stderr_path.open("wb") as stderr:
        child = subprocess.Popen(
            list(command),
            stdin=subprocess.PIPE,
            stdout=stdout,
            stderr=stderr,
            start_new_session=True,
        )
        try:
            child.communicate(prompt.encode("utf-8"), timeout=timeout)
        except subprocess.TimeoutExpired:
            os.killpg(child.pid, signal.SIGTERM)
            try:
                child.wait(timeout=2)
            except subprocess.TimeoutExpired:
                os.killpg(child.pid, signal.SIGKILL)
                child.wait()
            raise
    return child.returncode
