"""Start one selected Project's Workbench Codex bridge."""

# Implemented by:
# CA-R-2791@1
# CA-M-475@1
# CA-D-680@1
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import signal
import subprocess
import sys
import time
from typing import Any
from urllib.parse import urlsplit
from urllib.request import urlopen


_STARTUP_TIMEOUT_SECONDS = 5.0


def _state_path(root: Path) -> Path:
    return root / ".caprmedio_runtime" / "workbench" / "codex" / "bridge.json"


def _read_state(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError, TypeError):
        return {}
    return value if isinstance(value, dict) else {}


def _owned_bridge(state: dict[str, Any], root: Path, server: Path) -> int | None:
    """Return a PID only when its state and command prove this Project owns it."""
    pid = state.get("pid")
    if state.get("project_root") != str(root) or not isinstance(pid, int) or pid <= 0:
        return None
    try:
        probe = subprocess.run(
            ("ps", "-p", str(pid), "-o", "command="), text=True,
            capture_output=True, check=False,
        )
    except OSError:
        return None
    command = probe.stdout.strip() if probe.returncode == 0 else ""
    if str(server) not in command or "--project-root" not in command or str(root) not in command:
        return None
    return pid


def _group_exists(pid: int) -> bool:
    try:
        if os.name == "posix":
            os.killpg(pid, 0)
        else:
            os.kill(pid, 0)
    except ProcessLookupError:
        return False
    return True


def _stop_owned_bridge(pid: int) -> bool:
    try:
        if os.name == "posix":
            os.killpg(pid, signal.SIGTERM)
        else:
            os.kill(pid, signal.SIGTERM)
    except ProcessLookupError:
        return True
    deadline = time.monotonic() + _STARTUP_TIMEOUT_SECONDS
    while _group_exists(pid) and time.monotonic() < deadline:
        time.sleep(0.05)
    return not _group_exists(pid)


def _valid_bridge_url(value: object) -> str | None:
    if not isinstance(value, str):
        return None
    parsed = urlsplit(value)
    if parsed.scheme != "http" or parsed.hostname != "127.0.0.1" or parsed.port is None:
        return None
    return value.rstrip("/")


def _wait_until_ready(path: Path, root: Path, pid: int) -> str:
    deadline = time.monotonic() + _STARTUP_TIMEOUT_SECONDS
    while time.monotonic() < deadline:
        state = _read_state(path)
        if state.get("project_root") == str(root) and state.get("pid") == pid and state.get("ready") is True:
            url = _valid_bridge_url(state.get("url"))
            if url is not None:
                try:
                    with urlopen(f"{url}/health", timeout=0.2) as response:  # noqa: S310 - loopback URL is validated above.
                        if response.status == 200:
                            return url
                except OSError:
                    pass
        time.sleep(0.05)
    raise RuntimeError("Workbench Codex bridge did not become ready")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--project-root", required=True, type=Path)
    parser.add_argument("--mcp-url", required=True)
    args = parser.parse_args(argv)
    root = args.project_root.resolve(strict=True)
    server = Path(__file__).with_name("bridge_server.py").resolve(strict=True)
    state_path = _state_path(root)
    prior = _owned_bridge(_read_state(state_path), root, server)
    if prior is not None and not _stop_owned_bridge(prior):
        raise RuntimeError("Existing Workbench Codex bridge did not stop")

    process = subprocess.Popen(
        (sys.executable, str(server), "--project-root", str(root), "--mcp-url", args.mcp_url),
        cwd=root,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        start_new_session=os.name == "posix",
    )
    try:
        url = _wait_until_ready(state_path, root, process.pid)
    except BaseException:
        _stop_owned_bridge(process.pid)
        raise
    print(url)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
