# CA-R-2791@1
# CA-D-680@1

"""Read the deliberately small Workbench Codex runtime state."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any
from urllib.parse import urlsplit


def runtime_directory(root: Path) -> Path:
    return root / ".caprmedio_runtime" / "workbench" / "codex"


def public_state(root: Path, expected_host_root: Path | None = None) -> dict[str, Any]:
    root = Path(root).resolve(strict=True)
    directory = runtime_directory(root)
    try:
        bridge = json.loads((directory / "bridge.json").read_text())
    except (OSError, ValueError, TypeError):
        bridge = {}
    try:
        thread = json.loads((directory / "thread.json").read_text())
    except (OSError, ValueError, TypeError):
        thread = {}
    bridge_url = bridge.get("url") if isinstance(bridge.get("url"), str) else None
    if expected_host_root is not None and bridge.get("project_root") != str(expected_host_root):
        bridge_url = None
    if not _loopback_url(bridge_url):
        bridge_url = None
    return {
        "bridge_url": bridge_url,
        "ready": bridge.get("ready") is True and bridge_url is not None,
        "thread_id": thread.get("thread_id") if isinstance(thread.get("thread_id"), str) else None,
    }


def _loopback_url(value: str | None) -> bool:
    if not isinstance(value, str):
        return False
    try:
        parsed = urlsplit(value)
        port = parsed.port
    except ValueError:
        return False
    return (
        parsed.scheme == "http"
        and parsed.hostname == "127.0.0.1"
        and port is not None
        and parsed.username is None
        and parsed.password is None
        and parsed.path in {"", "/"}
        and not parsed.query
        and not parsed.fragment
    )
