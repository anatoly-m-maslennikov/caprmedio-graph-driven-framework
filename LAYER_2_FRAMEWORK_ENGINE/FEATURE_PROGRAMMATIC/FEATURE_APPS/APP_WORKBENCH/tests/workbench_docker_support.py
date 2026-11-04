# CA-E-676@8
# CA-E-677@8

"""Small standard-library helpers shared by Workbench Docker E2E tests."""

from __future__ import annotations

import json
from pathlib import Path
import socket
import subprocess
import tomllib
from urllib.error import HTTPError
from urllib.request import Request, urlopen
from uuid import UUID


def free_port() -> int:
    with socket.socket() as probe:
        probe.bind(("127.0.0.1", 0))
        return int(probe.getsockname()[1])


def project_name(control_root: Path) -> str:
    settings_path = control_root / "caprmedio_project_settings.toml"
    settings = tomllib.loads(settings_path.read_text(encoding="utf-8"))
    return settings["project"]["name"]


def request(url: str, *, method: str = "GET", payload: dict | None = None) -> tuple[int, dict | str]:
    body = None if payload is None else json.dumps(payload).encode()
    target = Request(url, data=body, method=method, headers={"content-type": "application/json"})
    try:
        with urlopen(target, timeout=60) as response:  # noqa: S310 -- loopback test server
            data = response.read().decode()
            return response.status, json.loads(data) if response.headers.get_content_type() == "application/json" else data
    except HTTPError as error:
        with error:
            data = error.read().decode()
        return error.code, json.loads(data) if data else {}


def container_memory_metrics(name: str) -> tuple[str, dict[str, int], int | None]:
    for events_path in ("/sys/fs/cgroup/memory.events", "/sys/fs/cgroup/memory/memory.events"):
        result = subprocess.run(
            ["docker", "exec", name, "cat", events_path],
            capture_output=True, text=True, check=False,
        )
        if result.returncode != 0:
            continue
        events = {}
        for line in result.stdout.splitlines():
            key, _, value = line.partition(" ")
            if key and value:
                try:
                    events[key] = int(value)
                except ValueError:
                    pass
        peak_result = subprocess.run(
            ["docker", "exec", name, "cat", events_path.replace("memory.events", "memory.peak")],
            capture_output=True, text=True, check=False,
        )
        peak = int(peak_result.stdout.strip()) if peak_result.returncode == 0 else None
        return events_path, events, peak
    raise AssertionError("Workbench container did not expose cgroup memory.events")


def is_uuid7(value: object) -> bool:
    if not isinstance(value, str):
        return False
    try:
        parsed = UUID(value)
    except ValueError:
        return False
    return parsed.version == 7 and str(parsed) == value
