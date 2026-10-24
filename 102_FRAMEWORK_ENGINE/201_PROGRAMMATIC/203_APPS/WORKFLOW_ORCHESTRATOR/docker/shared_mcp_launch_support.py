"""Validation, preparation, and bounded readback for the shared MCP launcher."""

from __future__ import annotations

import json
import os
from pathlib import Path
import re
from typing import Any, Callable, Mapping


ROOT = Path(__file__).resolve().parents[5]
TOOLS = ROOT / "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS"
if str(TOOLS) not in os.sys.path:
    os.sys.path.insert(0, str(TOOLS))

COMPOSE = Path(__file__).with_name("shared-mcp.compose.yaml")
DOCKER_ENV = (
    "HOME PATH DOCKER_HOST DOCKER_CONTEXT DOCKER_CONFIG "
    "XDG_RUNTIME_DIR TMPDIR HTTP_PROXY HTTPS_PROXY ALL_PROXY "
    "NO_PROXY http_proxy https_proxy all_proxy no_proxy"
).split()


class SharedLaunchError(ValueError):
    """A safe input or observed Docker boundary failure."""


def _config(path):
    from host_runtime_config import load_host_runtime_config

    try:
        return load_host_runtime_config(path)
    except Exception as error:
        raise SharedLaunchError("invalid_host_settings") from error


def _image(value):
    if not isinstance(value, str) or re.fullmatch(r"sha256:[0-9a-f]{64}\Z", value) is None:
        raise SharedLaunchError("explicit_immutable_image_required")
    return value


def _path(value):
    path = Path(value)
    if path.is_symlink() or not path.is_file() or not path.is_absolute():
        raise SharedLaunchError("compose_file_unavailable")
    return path.resolve(strict=True)


def _environment(config, image):
    return {
        **{name: os.environ[name] for name in DOCKER_ENV if name in os.environ},
        "CAPRMEDIO_IMAGE": image,
        "CAPRMEDIO_HOST_SETTINGS": str(config.source_path),
        "CAPRMEDIO_PROJECTS_ROOT": str(config.projects_root),
        "CAPRMEDIO_MCP_HTTP_PORT": str(config.http_port),
        "CAPRMEDIO_MAX_LOADED_PROJECTS": str(getattr(config, "max_loaded_projects", 2)),
        "CAPRMEDIO_SHARED_RUNTIME_ID": config.shared_runtime_id,
    }


def bounded(value, name, default=120):
    if value is None:
        return default
    if type(value) is not int or not 1 <= value <= 900:
        raise SharedLaunchError(f"invalid_{name}")
    return value


def _prefix(compose, project):
    return "docker compose --env-file /dev/null --project-name".split() + [
        project,
        "-f",
        str(compose),
    ]


def prepare_config(settings_path=None, image=None, *, compose_file=None, timeout=120):
    config = _config(settings_path)
    image = _image(image)
    compose = _path(compose_file or COMPOSE)
    timeout = bounded(timeout, "startup_timeout")
    project = "caprmedio-shared-" + config.shared_runtime_id[:16]
    environment = _environment(config, image)
    prefix = _prefix(compose, project)
    return {
        "mode": "dry-run",
        "service": "shared-mcp",
        "image": image,
        "settings_path": str(config.source_path),
        "projects_root": str(config.projects_root),
        "http_port": config.http_port,
        "max_loaded_projects": getattr(config, "max_loaded_projects", 2),
        "shared_runtime_id": config.shared_runtime_id,
        "compose_file": str(compose),
        "command": prefix + ["up", "-d", "--wait", "--wait-timeout", str(timeout), "shared-mcp"],
        "environment": environment,
        "compose_prefix": prefix,
        "config": config,
    }


def _mounts_match(row, config):
    mounts = row.get("Mounts")
    if not isinstance(mounts, list):
        return False
    binds = []
    for mount in mounts:
        if not isinstance(mount, Mapping) or mount.get("Type") != "bind":
            continue
        rw = mount.get("RW")
        if not isinstance(rw, bool):
            mode = str(mount.get("Mode", "rw")).split(",", 1)[0]
            rw = mode != "ro" and not bool(mount.get("ReadOnly", False))
        binds.append((mount.get("Source"), mount.get("Destination"), rw))
    expected = {
        (str(config.projects_root), str(config.projects_root), True),
        (str(config.source_path), str(config.source_path), False),
    }
    return len(binds) == 2 and set(binds) == expected


def _ports_match(row, port):
    network = row.get("NetworkSettings")
    ports = network.get("Ports") if isinstance(network, Mapping) else None
    rows = ports.get("8092/tcp") if isinstance(ports, Mapping) else None
    if isinstance(rows, list) and len(rows) == 1 and isinstance(rows[0], Mapping):
        return rows[0].get("HostIp") == "127.0.0.1" and rows[0].get("HostPort") == str(port)
    publishers = row.get("Publishers")
    if isinstance(publishers, list) and len(publishers) == 1 and isinstance(publishers[0], Mapping):
        value = publishers[0]
        return (
            value.get("Protocol") == "tcp"
            and value.get("TargetPort") == 8092
            and value.get("PublishedPort") == port
            and value.get("URL") == "127.0.0.1"
        )
    return False


def _runtime_match(row, prepared):
    state = row.get("State")
    return (
        row.get("Image") == prepared["image"]
        and isinstance(state, Mapping)
        and state.get("Status") == "running"
        and _mounts_match(row, prepared["config"])
        and _ports_match(row, prepared["config"].http_port)
    )


def inspect_runtime(docker: Callable[..., Any], prepared, deadline, clock: Callable[[], float]):
    prefix = prepared["compose_prefix"]
    remaining = deadline - clock()
    if remaining <= 0:
        return None
    listed = docker(
        prefix + ["ps", "--all", "-q", "shared-mcp"],
        prepared["environment"],
        min(30, remaining),
    )
    identifiers = str(getattr(listed, "stdout", "") or "").split()
    if listed is None or getattr(listed, "returncode", 1) != 0 or len(identifiers) != 1:
        return None
    remaining = deadline - clock()
    if remaining <= 0:
        return None
    inspected = docker(
        ["docker", "container", "inspect", "--format", "{{json .}}", identifiers[0]],
        prepared["environment"],
        min(30, remaining),
    )
    if inspected is None or getattr(inspected, "returncode", 1) != 0:
        return False
    try:
        row = json.loads(getattr(inspected, "stdout", ""))
        if isinstance(row, list):
            row = row[0] if len(row) == 1 else None
        if not isinstance(row, Mapping):
            row = None
    except TypeError, ValueError, json.JSONDecodeError:
        row = None
    return bool(row and _runtime_match(row, prepared))


def health_ready(opener, port, deadline, clock: Callable[[], float]):
    remaining = deadline - clock()
    if remaining <= 0:
        return False
    try:
        response = opener(f"http://127.0.0.1:{port}/health", timeout=min(2, remaining))
        try:
            return json.load(response).get("ready") is True
        finally:
            close = getattr(response, "close", None)
            if close:
                close()
    except Exception:
        return False
