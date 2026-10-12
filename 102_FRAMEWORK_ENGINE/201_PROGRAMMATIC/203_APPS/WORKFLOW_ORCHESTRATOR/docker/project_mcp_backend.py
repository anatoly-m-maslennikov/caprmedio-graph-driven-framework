"""Docker and loopback-MCP backend for the bounded Project MCP launcher."""

from __future__ import annotations

import asyncio
import json
import os
from pathlib import Path
import re
import selectors
import subprocess
import time
from typing import Any, Mapping
from urllib.parse import urlsplit

from runtime_images import ImageManager


_DIRECTORY = Path(__file__).resolve().parent
_COMPOSE = _DIRECTORY / "project-mcp.compose.yaml"
_CONTAINER_ID = re.compile(r"[0-9a-f]{12,64}\Z")
_MAX_STDOUT = 64 * 1024
_DOCKER_CLIENT_ENV = (
    "HOME", "DOCKER_HOST", "DOCKER_CONTEXT", "DOCKER_CONFIG", "XDG_RUNTIME_DIR", "TMPDIR",
    "HTTP_PROXY", "HTTPS_PROXY", "ALL_PROXY", "NO_PROXY",
    "http_proxy", "https_proxy", "all_proxy", "no_proxy",
)
_PROJECTED_INSPECT_KEYS = frozenset({
    "Id", "Image", "Config", "State", "NetworkSettings", "Mounts",
})
_INSPECT_FORMAT = (
    '{"Id":{{json .Id}},"Image":{{json .Image}},'
    '"Config":{"Labels":{{json .Config.Labels}}},'
    '"State":{{json .State}},'
    '"NetworkSettings":{"Ports":{{json .NetworkSettings.Ports}}},'
    '"Mounts":{{json .Mounts}}}'
)


class BackendError(RuntimeError):
    """Safe lifecycle failure; command diagnostics are deliberately discarded."""

    def __init__(self, code: str = "DOCKER_START_FAILED") -> None:
        self.code = code
        super().__init__(code)


def _unique_object(pairs):
    value = {}
    for key, item in pairs:
        if key in value:
            raise ValueError("duplicate Docker inspect member")
        value[key] = item
    return value


def _bounded_run(argv: list[str], *, timeout: float, env: Mapping[str, str] | None = None) -> str:
    """Run one finite Docker command with bounded stdout and discarded stderr."""
    process = subprocess.Popen(argv, stdin=subprocess.DEVNULL, stdout=subprocess.PIPE,
                               stderr=subprocess.DEVNULL, env=dict(env) if env else None,
                               shell=False)
    selector = selectors.DefaultSelector()
    output = bytearray()
    deadline = time.monotonic() + timeout
    try:
        if process.stdout is None:
            raise BackendError()
        selector.register(process.stdout, selectors.EVENT_READ)
        while selector.get_map():
            remaining = deadline - time.monotonic()
            if remaining <= 0:
                raise BackendError()
            for key, _ in selector.select(remaining):
                chunk = os.read(key.fileobj.fileno(), min(65536, _MAX_STDOUT + 1 - len(output)))
                if not chunk:
                    selector.unregister(key.fileobj)
                    continue
                output.extend(chunk)
                if len(output) > _MAX_STDOUT:
                    raise BackendError()
        remaining = deadline - time.monotonic()
        if remaining <= 0 or process.wait(timeout=remaining) != 0:
            raise BackendError()
        return output.decode("utf-8")
    except (OSError, UnicodeError, subprocess.TimeoutExpired, ValueError) as error:
        if isinstance(error, BackendError):
            raise
        raise BackendError() from None
    finally:
        selector.close()
        if process.stdout is not None:
            process.stdout.close()
        if process.poll() is None:
            try:
                process.kill()
                process.wait(timeout=1)
            except (OSError, subprocess.TimeoutExpired):
                pass


class ProjectMcpBackend:
    """Default seam: build/inspect/start one HTTP MCP service, never a worker."""

    def __init__(self, *, build_if_missing: bool = True, build_timeout: float = 600.0) -> None:
        self.build_if_missing = build_if_missing
        self.build_timeout = build_timeout

    def resolve_image(self, source_root, explicit_id):
        manager = ImageManager(source_root, timeout=self.build_timeout)
        image_id = manager.resolve(explicit_id=explicit_id, build_if_missing=self.build_if_missing)
        return image_id, manager.identity().fingerprint

    @staticmethod
    def _safe_instance(selection: object) -> str:
        value = getattr(selection, "instance_id", None)
        if not isinstance(value, str) or not re.fullmatch(r"[0-9a-f]{64}", value):
            raise BackendError()
        return value

    @staticmethod
    def _root(selection: object) -> Path:
        try:
            root = Path(getattr(selection, "root"))
        except (TypeError, ValueError) as error:
            raise BackendError() from error
        if not root.is_absolute() or root.is_symlink() or not root.is_dir():
            raise BackendError()
        return root

    @staticmethod
    def _control(selection: object) -> str:
        value = getattr(selection, "control_relative", None)
        if not isinstance(value, Path) or value.is_absolute() or len(value.parts) != 1:
            raise BackendError()
        return value.as_posix()

    @staticmethod
    def _compose_project(selection: object) -> str:
        value = getattr(selection, "compose_project", None)
        if not isinstance(value, str) or not re.fullmatch(r"caprmedio-mcp-[0-9a-f]{24}", value):
            raise BackendError()
        return value

    @staticmethod
    def _environment(selection: object, image_id: str, fingerprint: str,
                     port: int | None = None) -> dict[str, str]:
        root = ProjectMcpBackend._root(selection)
        if not isinstance(image_id, str) or not re.fullmatch(r"sha256:[0-9a-f]{64}", image_id):
            raise BackendError()
        if not isinstance(fingerprint, str) or not re.fullmatch(r"[0-9a-f]{64}", fingerprint):
            raise BackendError()
        if (port is not None and (isinstance(port, bool) or not isinstance(port, int)
                                  or not 1 <= port <= 65535)):
            raise BackendError()
        environment = {
            "PATH": os.environ.get("PATH", ""),
            "CAPRMEDIO_IMAGE": image_id,
            "CAPRMEDIO_PROJECT_ROOT": str(root),
            "CAPRMEDIO_CONTROL_ROOT": ProjectMcpBackend._control(selection),
            "CAPRMEDIO_PROJECT_INSTANCE_ID": ProjectMcpBackend._safe_instance(selection),
            "CAPRMEDIO_RUNTIME_FINGERPRINT": fingerprint,
            # An empty segment preserves Compose's Docker-owned dynamic
            # `127.0.0.1::8092` publication; a decimal segment is exact.
            "CAPRMEDIO_MCP_HTTP_PORT": "" if port is None else str(port),
        }
        for name in _DOCKER_CLIENT_ENV:
            if name in os.environ:
                environment[name] = os.environ[name]
        return environment

    @staticmethod
    def _docker_client_environment() -> dict[str, str]:
        """Pass Docker client context without ambient service credentials."""
        environment = {"PATH": os.environ.get("PATH", "")}
        for name in _DOCKER_CLIENT_ENV:
            if name in os.environ:
                environment[name] = os.environ[name]
        return environment

    @staticmethod
    def _projection_matches_selection(row: Mapping[str, Any], selection: object) -> bool:
        """Require the narrow inspect projection to bind exactly one Project mount."""
        if set(row) != _PROJECTED_INSPECT_KEYS:
            return False
        config = row.get("Config")
        labels = config.get("Labels") if isinstance(config, Mapping) else None
        root = ProjectMcpBackend._root(selection)
        if not isinstance(labels, Mapping) or (
            labels.get("org.caprmedio.project") != ProjectMcpBackend._safe_instance(selection)
            or labels.get("org.caprmedio.service") != "mcp-http"
            or labels.get("org.caprmedio.control_root") != ProjectMcpBackend._control(selection)
            or labels.get("org.caprmedio.host_project_root") != str(root)
        ):
            return False
        mounts = row.get("Mounts")
        if not isinstance(mounts, list) or len(mounts) != 1 or not isinstance(mounts[0], Mapping):
            return False
        mount = mounts[0]
        source = mount.get("Source")
        return (
            mount.get("Type") == "bind"
            and mount.get("Destination") == "/project"
            and isinstance(source, str)
            and Path(source) == root
        )

    def inspect(self, selection, *, timeout: float = 30.0):
        """Read the selected Project's Docker namespace within one deadline."""
        if (isinstance(timeout, bool) or not isinstance(timeout, (int, float))
                or not 0 < timeout <= 30.0):
            raise BackendError("DOCKER_PUBLICATION_FAILED")
        deadline = time.monotonic() + float(timeout)
        def remaining() -> float:
            value = deadline - time.monotonic()
            if value <= 0:
                raise BackendError("DOCKER_PUBLICATION_FAILED")
            return value
        instance = self._safe_instance(selection)
        listing = _bounded_run([
            "docker", "ps", "--all", "--filter", f"label=org.caprmedio.project={instance}",
            "--format", "{{.ID}}",
        ], timeout=remaining(), env=self._docker_client_environment())
        identifiers = [line.strip() for line in listing.splitlines() if line.strip()]
        if len(identifiers) > 1 or any(_CONTAINER_ID.fullmatch(value) is None for value in identifiers):
            raise BackendError("DOCKER_PUBLICATION_FAILED")
        rows: list[dict[str, Any]] = []
        for identifier in identifiers:
            raw = _bounded_run([
                "docker", "container", "inspect", "--format", _INSPECT_FORMAT, identifier,
            ], timeout=remaining(), env=self._docker_client_environment())
            try:
                value = json.loads(raw, object_pairs_hook=_unique_object)
                if not isinstance(value, dict) or not self._projection_matches_selection(value, selection):
                    raise ValueError()
                rows.append(value)
            except (TypeError, ValueError, json.JSONDecodeError) as error:
                raise BackendError("RUNTIME_MISMATCH") from error
        return rows

    def collect_legacy_processes(self, admission: object, deadline: float) -> Mapping[str, object]:
        """Query the actual Docker namespace without acting on any container.

        The generic migration collector validates a complete sealed process
        identity before it can classify a non-empty roster as ``observed``.
        Docker's existing inspect projection does not carry that identity, so
        a live row is deliberately returned as raw provider evidence and the
        caller will block rather than guess that it belongs to the predecessor.
        """
        selection = getattr(admission, "selection", None)
        root = getattr(admission, "project_root", None)
        instance = getattr(admission, "project_instance_id", None)
        if (selection is None or getattr(selection, "root", None) != root
                or getattr(selection, "instance_id", None) != instance):
            return {"outcome": "unavailable", "records": []}
        remaining = deadline - time.monotonic()
        if remaining <= 0:
            return {"outcome": "unavailable", "records": []}
        rows = self.inspect(selection, timeout=min(30.0, remaining))
        records: list[dict[str, object]] = []
        for row in rows:
            if not isinstance(row, Mapping):
                return {"outcome": "unavailable", "records": []}
            config = row.get("Config")
            labels = config.get("Labels") if isinstance(config, Mapping) else None
            records.append({
                "container_id": row.get("Id"),
                "labels": dict(labels) if isinstance(labels, Mapping) else None,
            })
        return {"outcome": "complete", "records": records}

    @staticmethod
    def _compose_file(value: Path | str) -> Path:
        """Admit one regular, absolute Compose carrier before invoking Docker."""
        try:
            compose = Path(value)
            if not compose.is_absolute() or compose.is_symlink() or not compose.is_file():
                raise BackendError()
            return compose
        except BackendError:
            raise
        except (OSError, TypeError, ValueError) as error:
            raise BackendError() from error

    def _start(self, selection, image_id, fingerprint, compose_file: Path | str, timeout, port=None):
        if not isinstance(timeout, (int, float)) or isinstance(timeout, bool) or timeout <= 0:
            raise BackendError()
        compose = self._compose_file(compose_file)
        command = [
            "docker", "compose", "--env-file", "/dev/null", "--project-name",
            self._compose_project(selection), "-f", str(compose), "up", "-d", "--wait",
            "--wait-timeout", str(max(1, int(timeout))), "--no-recreate", "--no-deps", "mcp-http",
        ]
        _bounded_run(command, timeout=float(timeout),
                     env=self._environment(selection, image_id, fingerprint, port))

    def start(self, selection, image_id, fingerprint, timeout, port=None):
        """Start development mode from its checked-in Compose carrier."""
        self._start(selection, image_id, fingerprint, _COMPOSE, timeout, port)

    def start_installed(self, selection, image_id, fingerprint, compose_file, timeout, port=None):
        """Start an admitted installation with its selected package Compose file."""
        self._start(selection, image_id, fingerprint, compose_file, timeout, port)

    @staticmethod
    async def _initialize(url: str, timeout: float) -> None:
        import httpx2
        from mcp.client.session import ClientSession
        from mcp.client.streamable_http import streamable_http_client

        async with httpx2.AsyncClient(trust_env=False, follow_redirects=False, timeout=timeout) as client:
            transport = streamable_http_client(url, http_client=client)
            async with transport as streams:
                async with ClientSession(*streams) as session:
                    await session.initialize()

    def health(self, full_mcp_url, timeout):
        try:
            address = urlsplit(full_mcp_url)
            valid = (address.scheme == 'http' and address.hostname == '127.0.0.1'
                     and address.port is not None and 1 <= address.port <= 65535
                     and address.path == '/mcp' and not address.query and not address.fragment
                     and address.username is None and address.password is None
                     and address.netloc == f'127.0.0.1:{address.port}')
        except (TypeError, ValueError):
            valid = False
        if (not valid or isinstance(timeout, bool)
                or not isinstance(timeout, (int, float)) or timeout <= 0):
            return False
        try:
            asyncio.run(asyncio.wait_for(self._initialize(full_mcp_url, float(timeout)),
                                         timeout=float(timeout)))
        except Exception:
            return False
        return True


def collect_legacy_processes(admission: object, deadline: float) -> Mapping[str, object]:
    """Provider hook used only by retained-migration read-only collection."""
    return ProjectMcpBackend(build_if_missing=False).collect_legacy_processes(admission, deadline)


__all__ = ["BackendError", "ProjectMcpBackend", "collect_legacy_processes"]
