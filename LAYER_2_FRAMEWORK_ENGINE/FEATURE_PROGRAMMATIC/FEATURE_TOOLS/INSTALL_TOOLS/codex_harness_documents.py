"""Pure Codex JSON/TOML document transformations for host installation."""

from __future__ import annotations

import json
from collections.abc import Mapping
from pathlib import Path
import shlex
import stat

from INSTALL_TOOLS.host_installation_io import HostInstallationError


_MATCHER = "^mcp__caprmedio__"
_OWNED = frozenset(
    {"caprmedio_project_context.py", "codex_project_context.py", "codex_project_context_hook.py"}
)
_TRANSPORTS = frozenset({"http", "https", "sse", "streamable_http", "streamable-http"})
_GROUP_FIELDS = frozenset({"matcher", "hooks"})
_HANDLER_FIELDS = frozenset({"type", "command", "timeout", "async"})
_MISSING = object()
_MAX_FILE_BYTES = 4 * 1024 * 1024


def read_bounded(path: Path, label: str) -> bytes:
    try:
        info = path.lstat()
        if stat.S_ISLNK(info.st_mode) or not stat.S_ISREG(info.st_mode):
            raise HostInstallationError("invalid-target", f"{label} must be a regular file")
        if info.st_size > _MAX_FILE_BYTES:
            raise HostInstallationError(
                "file-too-large", f"{label} exceeds {_MAX_FILE_BYTES} bytes"
            )
        return path.read_bytes()
    except (OSError, UnicodeError) as error:
        raise HostInstallationError("read-failed", f"Cannot read {label}") from error


def _json(path: Path) -> tuple[bytes | None, dict]:
    if not path.exists():
        return None, {}
    original = read_bounded(path, "Codex hooks.json")
    try:
        document = json.loads(original)
    except (UnicodeError, json.JSONDecodeError) as error:
        raise HostInstallationError("hooks-invalid", "Cannot parse Codex hooks.json") from error
    if not isinstance(document, dict):
        raise HostInstallationError("hooks-invalid", "Codex hooks.json root must be an object")
    return original, document


def _owned(handler: object) -> bool:
    if not isinstance(handler, dict) or not isinstance(handler.get("command"), str):
        return False
    try:
        return any(Path(token).name in _OWNED for token in shlex.split(handler["command"]))
    except ValueError:
        return False


def _group_metadata(group: dict) -> dict:
    metadata = {key: value for key, value in group.items() if key not in _GROUP_FIELDS}
    if metadata.get("async") not in (None, False):
        raise HostInstallationError("hooks-conflict", "CAPRMEDIO hook group cannot be asynchronous")
    return metadata


def _merge_group_metadata(target: dict, source: dict) -> None:
    for key, value in _group_metadata(source).items():
        if key in target and target[key] != value:
            raise HostInstallationError(
                "hooks-conflict", f"Conflicting CAPRMEDIO hook group field: {key}"
            )
        target[key] = value


def _merge_handler_policy(target: dict, handler: object) -> None:
    if not isinstance(handler, dict):
        return
    for key, value in handler.items():
        if key == "async" and value not in (None, False):
            raise HostInstallationError(
                "hooks-conflict", "Existing CAPRMEDIO hook policy is asynchronous"
            )
        if key in _HANDLER_FIELDS:
            continue
        if key in target and target[key] != value:
            raise HostInstallationError(
                "hooks-conflict", f"Conflicting CAPRMEDIO hook policy field: {key}"
            )
        target[key] = value


def _merge(groups: list[object], command: str) -> list[object]:
    retained: list[object] = []
    managed: dict | None = None
    owned_policy: dict = {}
    for group in groups:
        if not isinstance(group, dict) or group.get("matcher") != _MATCHER:
            retained.append(group)
            continue
        handlers = group.get("hooks", [])
        if not isinstance(handlers, list):
            raise HostInstallationError(
                "hooks-invalid", "Codex PreToolUse group hooks must be a list"
            )
        cleaned = []
        _group_metadata(group)
        for handler in handlers:
            if _owned(handler):
                _merge_handler_policy(owned_policy, handler)
            else:
                cleaned.append(handler)
        if managed is None:
            managed = dict(group)
            managed["hooks"] = cleaned
            retained.append(managed)
        else:
            _merge_group_metadata(managed, group)
            managed["hooks"].extend(cleaned)
    if managed is None:
        managed = {"matcher": _MATCHER, "hooks": []}
        retained.append(managed)
    managed["hooks"].append({"type": "command", "command": command, "timeout": 5, **owned_policy})
    return retained


def _result(content: bytes, original: bytes | None, include_original: bool):
    return (content, original) if include_original else content


def hooks_content(path: Path, command: str, *, include_original: bool = False):
    original, document = _json(path)
    root = document.get("hooks")
    if root is None:
        root = {}
        document["hooks"] = root
    if not isinstance(root, dict):
        raise HostInstallationError("hooks-invalid", "Codex hooks.json hooks must be an object")
    groups = root.get("PreToolUse", [])
    if not isinstance(groups, list):
        raise HostInstallationError("hooks-invalid", "Codex PreToolUse must be a list")
    root["PreToolUse"] = _merge(groups, command)
    rendered = (json.dumps(document, ensure_ascii=False, indent=2) + "\n").encode()
    return _result(original if original == rendered else rendered, original, include_original)


def _load_toml(path: Path, document, parse) -> tuple[bytes | None, object]:
    if not path.exists():
        return None, document()
    original = read_bounded(path, "Codex config.toml")
    try:
        config = parse(original.decode())
    except (UnicodeError, ValueError) as error:
        raise HostInstallationError("config-invalid", "Cannot parse Codex config.toml") from error
    return original, config


def config_content(path: Path, endpoint: str, *, include_original: bool = False):
    try:
        from tomlkit import document, dumps, parse, table
    except ImportError as error:
        raise HostInstallationError(
            "config-dependency", "tomlkit 0.15.1 is required for Codex config"
        ) from error
    original, config = _load_toml(path, document, parse)
    servers = config.get("mcp_servers")
    if servers is None:
        servers = table()
        config["mcp_servers"] = servers
    if not isinstance(servers, Mapping):
        raise HostInstallationError("mcp-server-conflict", "Codex mcp_servers must be a table")
    server = servers.get("caprmedio")
    if server is None:
        server = table()
        servers["caprmedio"] = server
    if not isinstance(server, Mapping):
        raise HostInstallationError("mcp-server-conflict", "Codex caprmedio server must be a table")
    if "command" in server or "args" in server:
        raise HostInstallationError(
            "mcp-server-conflict", "Existing caprmedio server uses stdio transport"
        )
    if "transport" in server and str(server["transport"]).lower() not in _TRANSPORTS:
        raise HostInstallationError(
            "mcp-server-conflict", "Existing caprmedio server uses a conflicting transport"
        )
    current = server.get("url", _MISSING)
    if current is not _MISSING:
        if not isinstance(current, str) or current != endpoint:
            raise HostInstallationError(
                "mcp-server-conflict", "Existing caprmedio server uses a different URL"
            )
        return _result(
            original if original is not None else dumps(config).encode(), original, include_original
        )
    server["url"] = endpoint
    return _result(dumps(config).encode(), original, include_original)


__all__ = ["config_content", "hooks_content", "read_bounded"]
