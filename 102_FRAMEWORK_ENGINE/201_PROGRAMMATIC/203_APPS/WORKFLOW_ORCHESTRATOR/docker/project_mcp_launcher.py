"""Start or reuse one selected Project-local HTTP MCP service safely."""

from __future__ import annotations

from contextlib import contextmanager
import fcntl
import json
import os
from pathlib import Path
import re
import sys
import time
from typing import Any, Iterator, Mapping

_TOOLS = Path(__file__).resolve().parents[3] / "201_TOOLS"
if str(_TOOLS) not in sys.path:
    sys.path.insert(0, str(_TOOLS))

from project_selection import ProjectSelectionError, resolve_project

from runtime_images import ImageError


_IMAGE = re.compile(r"sha256:[0-9a-f]{64}\Z")
_FINGERPRINT = re.compile(r"[0-9a-f]{64}\Z")
_CONDITIONS = frozenset({
    "READY_STARTED", "READY_REUSED", "PROJECT_SELECTION_REFUSED",
    "CREDENTIAL_SOURCE_REFUSED", "IMAGE_INPUT_UNAVAILABLE", "IMAGE_REFUSED",
    "PROJECT_LOCK_BUSY", "RUNTIME_MISMATCH", "RUNTIME_UNHEALTHY",
    "BUILD_FAILED", "DOCKER_START_FAILED", "DOCKER_PUBLICATION_FAILED",
    "READINESS_FAILED",
})
_DISPOSITIONS = {
    "READY_STARTED": "started",
    "READY_REUSED": "reused",
    "PROJECT_SELECTION_REFUSED": "refused",
    "CREDENTIAL_SOURCE_REFUSED": "refused",
    "IMAGE_INPUT_UNAVAILABLE": "failed",
    "IMAGE_REFUSED": "refused",
    "PROJECT_LOCK_BUSY": "busy",
    "RUNTIME_MISMATCH": "refused",
    "RUNTIME_UNHEALTHY": "refused",
    "BUILD_FAILED": "failed",
    "DOCKER_START_FAILED": "failed",
    "DOCKER_PUBLICATION_FAILED": "failed",
    "READINESS_FAILED": "failed",
}
_LOCK_RETRY_SECONDS = 0.01
_DEFAULT_STARTUP_TIMEOUT = 60.0
_DEFAULT_BUILD_TIMEOUT = 600.0
_MAX_TOKEN_BYTES = 16 * 1024
_SAFE_RESULT_KEYS = (
    "disposition", "condition", "project_root", "control_root", "project_id",
    "image_id", "fingerprint", "container_id", "service", "port", "readiness",
)


class LaunchError(RuntimeError):
    """A safe non-secret launcher condition."""

    def __init__(self, code: str = "DOCKER_START_FAILED") -> None:
        self.code = code if code in _CONDITIONS else "DOCKER_START_FAILED"
        super().__init__(self.code)


def _selection_root(selection: object) -> Path:
    root = getattr(selection, "root", getattr(selection, "rootPath", None))
    try:
        path = Path(root)
    except (TypeError, ValueError) as error:
        raise LaunchError("PROJECT_SELECTION_REFUSED") from error
    if not path.is_absolute() or path.is_symlink() or not path.is_dir():
        raise LaunchError("PROJECT_SELECTION_REFUSED")
    return path


def _state_root(selection: object) -> Path:
    root = _selection_root(selection)
    value = getattr(selection, "launcher_state", None)
    if value is None:
        instance = getattr(selection, "instance_id", "")
        value = root / ".caprmedio_install" / "project_mcp" / instance
    try:
        state = Path(value)
        relative = state.relative_to(root)
    except (TypeError, ValueError) as error:
        raise LaunchError("PROJECT_SELECTION_REFUSED") from error
    if not relative.parts:
        raise LaunchError("PROJECT_SELECTION_REFUSED")
    current = root
    try:
        for part in relative.parts:
            current = current / part
            if os.path.lexists(current):
                if current.is_symlink() or not current.is_dir():
                    raise LaunchError("PROJECT_SELECTION_REFUSED")
            else:
                current.mkdir(mode=0o700)
        return state
    except LaunchError:
        raise
    except OSError as error:
        raise LaunchError("PROJECT_SELECTION_REFUSED") from error


@contextmanager
def _project_lock(selection: object, timeout: float) -> Iterator[None]:
    """Hold one non-blocking flock for the selected Project identity."""
    state = _state_root(selection)
    lock_path = state / "launch.lock"
    descriptor = None
    deadline = time.monotonic() + timeout
    try:
        flags = os.O_RDWR | os.O_CREAT
        if hasattr(os, "O_NOFOLLOW"):
            flags |= os.O_NOFOLLOW
        descriptor = os.open(lock_path, flags, 0o600)
        while True:
            try:
                fcntl.flock(descriptor, fcntl.LOCK_EX | fcntl.LOCK_NB)
                break
            except BlockingIOError:
                remaining = deadline - time.monotonic()
                if remaining <= 0:
                    raise LaunchError("PROJECT_LOCK_BUSY")
                time.sleep(min(_LOCK_RETRY_SECONDS, remaining))
        yield
    except LaunchError:
        raise
    except OSError as error:
        raise LaunchError("PROJECT_SELECTION_REFUSED") from error
    finally:
        if descriptor is not None:
            try:
                fcntl.flock(descriptor, fcntl.LOCK_UN)
            except OSError:
                pass
            os.close(descriptor)


def _positive_timeout(value: object, *, ceiling: float, default: float) -> float:
    if value is None:
        return default
    if isinstance(value, bool) or not isinstance(value, (int, float)) or not 0 < value <= ceiling:
        raise LaunchError("READINESS_FAILED")
    return float(value)


def _requested_port(value: object) -> int | None:
    """Admit the optional Docker-owned or caller-selected host port."""
    if value is None:
        return None
    if isinstance(value, bool) or not isinstance(value, int) or not 1 <= value <= 65535:
        # CA-O-188 has a closed public condition vocabulary.  This defensive
        # programmatic seam is never reached by the CLI's argument validator.
        raise LaunchError("DOCKER_START_FAILED")
    return value


def _labels(row: Mapping[str, Any]) -> Mapping[str, Any] | None:
    config = row.get("Config")
    labels = config.get("Labels") if isinstance(config, Mapping) else None
    return labels if isinstance(labels, Mapping) else None


def _project_mount_is_exact(row: Mapping[str, Any], selection: object) -> bool:
    """Validate a raw inspect mount when Docker supplied one.

    The injected contract fake deliberately omits `Mounts`; real `docker inspect`
    rows carry it and are consequently checked here.
    """
    if "Mounts" not in row:
        return True
    mounts = row.get("Mounts")
    if not isinstance(mounts, list) or len(mounts) != 1 or not isinstance(mounts[0], Mapping):
        return False
    mount = mounts[0]
    source = mount.get("Source")
    root = _selection_root(selection)
    return (
        mount.get("Type") == "bind"
        and mount.get("Destination") == "/project"
        and isinstance(source, str)
        and Path(source) == root
    )


def _project_labels_are_exact(labels: Mapping[str, Any], row: Mapping[str, Any],
                              selection: object) -> bool:
    """Bind real Docker inspect rows to exactly the selected Project.

    The frozen backend seam intentionally supplies the small common subset of
    inspect fields and has no ``Mounts`` member.  Docker's actual inspect
    schema always includes that member, so once it is present require the
    compose labels that bind the selected direct control root and host root.
    Together with the sole ``/project`` bind this excludes sibling, ancestor,
    and Docker-socket binds.
    """
    if "Mounts" not in row:
        return True
    control = getattr(selection, "control_relative", None)
    if not isinstance(control, Path) or control.is_absolute():
        return False
    return (
        labels.get("org.caprmedio.control_root") == control.as_posix()
        and labels.get("org.caprmedio.host_project_root") == str(_selection_root(selection))
    )


def _publisher(row: Mapping[str, Any]) -> tuple[str, int] | None:
    network = row.get("NetworkSettings")
    ports = network.get("Ports") if isinstance(network, Mapping) else None
    if not isinstance(ports, Mapping) or set(ports) != {"8092/tcp"}:
        return None
    rows = ports.get("8092/tcp")
    if not isinstance(rows, list) or len(rows) != 1 or not isinstance(rows[0], Mapping):
        return None
    publisher = rows[0]
    value = publisher.get("HostPort")
    if publisher.get("HostIp") != "127.0.0.1" or not isinstance(value, str) or not value.isdecimal():
        return None
    port = int(value)
    return ("http://127.0.0.1:" + value + "/mcp", port) if 1 <= port <= 65535 else None


def _attribution(selection: object | None, image_id: str | None = None,
                 fingerprint: str | None = None) -> dict[str, Any]:
    """Return only fields that remain safe if a launch stops early."""
    root = control = project_id = None
    if selection is not None:
        try:
            root = str(_selection_root(selection))
            control_value = getattr(selection, "control_root", None)
            if isinstance(control_value, Path) and control_value.is_absolute():
                control = str(control_value)
            value = getattr(selection, "instance_id", None)
            if isinstance(value, str) and _FINGERPRINT.fullmatch(value):
                project_id = value
        except LaunchError:
            pass
    return {
        "project_root": root,
        "control_root": control,
        "project_id": project_id,
        "image_id": image_id if isinstance(image_id, str) and _IMAGE.fullmatch(image_id) else None,
        "fingerprint": (fingerprint if isinstance(fingerprint, str)
                        and _FINGERPRINT.fullmatch(fingerprint) else None),
        "container_id": None,
        "service": "mcp-http",
        "port": None,
        "readiness": False,
    }


def _atomic_metadata(state: Path, name: str, payload: Mapping[str, Any]) -> None:
    """Replace a fixed, Project-local metadata file without following links."""
    target = state / name
    temporary = state / ("." + name + "." + str(os.getpid()) + ".tmp")
    descriptor = None
    try:
        if os.path.lexists(target) and (target.is_symlink() or not target.is_file()):
            return
        flags = os.O_WRONLY | os.O_CREAT | os.O_EXCL
        if hasattr(os, "O_NOFOLLOW"):
            flags |= os.O_NOFOLLOW
        descriptor = os.open(temporary, flags, 0o600)
        encoded = (json.dumps(dict(payload), sort_keys=True, separators=(",", ":"),
                              ensure_ascii=True) + "\n").encode("utf-8")
        os.write(descriptor, encoded)
        os.fsync(descriptor)
        os.close(descriptor)
        descriptor = None
        os.replace(temporary, target)
    except (OSError, TypeError, ValueError):
        if descriptor is not None:
            os.close(descriptor)
        try:
            temporary.unlink(missing_ok=True)
        except OSError:
            pass


def _record_safe_metadata(selection: object, result: Mapping[str, Any]) -> None:
    """Persist only attributable lifecycle metadata; credentials and URL stay out."""
    try:
        state = _state_root(selection)
        metadata = {key: result.get(key) for key in _SAFE_RESULT_KEYS}
        _atomic_metadata(state, "last_launch.json", metadata)
        if result.get("readiness") is True:
            _atomic_metadata(state, "ready.json", metadata)
    except (LaunchError, OSError, TypeError, ValueError):
        # A metadata write can neither turn an uncertain Docker effect into a
        # retry nor expose an exception/credential in the launcher result.
        pass


def _valid_token(token: object) -> bool:
    return (
        isinstance(token, str)
        and bool(token)
        and "\r" not in token
        and "\n" not in token
        and "\0" not in token
        and len(token.encode("utf-8")) <= _MAX_TOKEN_BYTES
    )


def _admit_runtime(rows: object, selection: object, image_id: str, fingerprint: str,
                   requested_port: int | None = None):
    """Return absent, a ready candidate, or its terminal safe condition."""
    if not isinstance(rows, list):
        return "DOCKER_PUBLICATION_FAILED"
    if not rows:
        return "absent"
    if len(rows) != 1 or not isinstance(rows[0], Mapping):
        return "DOCKER_PUBLICATION_FAILED"
    row = rows[0]
    labels = _labels(row)
    instance = getattr(selection, "instance_id", None)
    if (
        labels is None
        or labels.get("org.caprmedio.project") != instance
        or labels.get("org.caprmedio.service") != "mcp-http"
        or labels.get("org.caprmedio.runtime.fingerprint") != fingerprint
        or row.get("Image") != image_id
        or not _project_labels_are_exact(labels, row, selection)
        or not _project_mount_is_exact(row, selection)
    ):
        return "RUNTIME_MISMATCH"
    state = row.get("State")
    health = state.get("Health") if isinstance(state, Mapping) else None
    if not (isinstance(state, Mapping) and state.get("Status") == "running"
            and isinstance(health, Mapping) and health.get("Status") == "healthy"):
        return "RUNTIME_UNHEALTHY"
    publisher = _publisher(row)
    if publisher is None:
        return "DOCKER_PUBLICATION_FAILED"
    if requested_port is not None and publisher[1] != requested_port:
        return "RUNTIME_MISMATCH"
    container = row.get("Id")
    if not isinstance(container, str) or not container:
        return "DOCKER_PUBLICATION_FAILED"
    return {"row": row, "container_id": container, "url": publisher[0], "port": publisher[1]}


class Launcher:
    """Bounded Project MCP start-or-reuse coordinator with an injectable backend."""

    def __init__(self, backend=None) -> None:
        self.backend = backend

    @staticmethod
    def _failure(code: str, selection: object | None = None, image_id: str | None = None,
                 fingerprint: str | None = None) -> dict[str, Any]:
        condition = code if code in _CONDITIONS else "DOCKER_START_FAILED"
        return {
            "disposition": _DISPOSITIONS[condition],
            "condition": condition,
            **_attribution(selection, image_id, fingerprint),
        }

    @staticmethod
    def _backend(backend, *, build_if_missing: bool, build_timeout: float):
        if backend is not None:
            return backend
        from project_mcp_backend import ProjectMcpBackend
        return ProjectMcpBackend(build_if_missing=build_if_missing, build_timeout=build_timeout)

    @staticmethod
    def _image(backend, source_root, image):
        try:
            image_id, fingerprint = backend.resolve_image(source_root, image)
        except ImageError as error:
            raise LaunchError(getattr(error, "code", "IMAGE_REFUSED")) from None
        except LaunchError:
            raise
        except Exception:
            raise LaunchError("IMAGE_REFUSED") from None
        if not isinstance(image_id, str) or _IMAGE.fullmatch(image_id) is None:
            raise LaunchError("IMAGE_REFUSED")
        if not isinstance(fingerprint, str) or _FINGERPRINT.fullmatch(fingerprint) is None:
            raise LaunchError("IMAGE_REFUSED")
        return image_id, fingerprint

    @staticmethod
    def _ready(backend, candidate: Mapping[str, Any], token: str, deadline: float) -> bool:
        remaining = deadline - time.monotonic()
        if remaining <= 0:
            return False
        try:
            return backend.health(candidate["url"], token, remaining) is True
        except Exception:
            return False

    @staticmethod
    def _result(disposition: str, condition: str, selection: object, image_id: str,
                fingerprint: str, candidate: Mapping[str, Any]) -> dict[str, Any]:
        result = {
            "disposition": disposition,
            "condition": condition,
            "readiness": True,
            "url": candidate["url"],
        }
        result.update(_attribution(selection, image_id, fingerprint))
        result.update({
            "container_id": candidate["container_id"],
            "port": candidate["port"],
            "readiness": True,
        })
        return result

    @staticmethod
    def _failure_code(error: Exception, fallback: str) -> str:
        code = getattr(error, "code", None)
        return code if isinstance(code, str) and code in _CONDITIONS else fallback

    def launch(self, project_root, token, control_root=None, image=None, source_root=None,
               timeout=60, *, port=None, build_if_missing=True, build_timeout=600):
        """Return one safe result; never stop, replace, or retry a live runtime."""
        try:
            requested_port = _requested_port(port)
        except LaunchError as error:
            return self._failure(error.code)
        try:
            selection = resolve_project(project_root, control_root)
        except ProjectSelectionError:
            return self._failure("PROJECT_SELECTION_REFUSED")
        except Exception:
            return self._failure("PROJECT_SELECTION_REFUSED")
        if not _valid_token(token):
            return self._failure("CREDENTIAL_SOURCE_REFUSED", selection)
        try:
            startup_timeout = _positive_timeout(timeout, ceiling=_DEFAULT_STARTUP_TIMEOUT,
                                                default=_DEFAULT_STARTUP_TIMEOUT)
            bounded_build_timeout = _positive_timeout(build_timeout, ceiling=_DEFAULT_BUILD_TIMEOUT,
                                                      default=_DEFAULT_BUILD_TIMEOUT)
            if type(build_if_missing) is not bool:
                raise LaunchError("IMAGE_REFUSED")
            if source_root is None:
                return self._failure("IMAGE_INPUT_UNAVAILABLE", selection)
            source = Path(source_root)
            backend = self._backend(self.backend, build_if_missing=build_if_missing,
                                    build_timeout=bounded_build_timeout)
            with _project_lock(selection, startup_timeout):
                def complete(result: dict[str, Any]) -> dict[str, Any]:
                    _record_safe_metadata(selection, result)
                    return result

                try:
                    image_id, fingerprint = self._image(backend, source, image)
                except LaunchError as error:
                    return complete(self._failure(error.code, selection))
                try:
                    candidate = _admit_runtime(backend.inspect(selection), selection,
                                               image_id, fingerprint, requested_port)
                except Exception as error:
                    return complete(self._failure(self._failure_code(
                        error, "DOCKER_PUBLICATION_FAILED"), selection, image_id, fingerprint))
                deadline = time.monotonic() + startup_timeout
                if candidate == "absent":
                    try:
                        remaining = deadline - time.monotonic()
                        if remaining <= 0:
                            return complete(self._failure("DOCKER_START_FAILED", selection,
                                                          image_id, fingerprint))
                        backend.start(selection, image_id, fingerprint, token, remaining,
                                      requested_port)
                    except LaunchError as error:
                        return complete(self._failure(error.code, selection, image_id, fingerprint))
                    except Exception as error:
                        return complete(self._failure(self._failure_code(
                            error, "DOCKER_START_FAILED"), selection, image_id, fingerprint))
                    try:
                        candidate = _admit_runtime(backend.inspect(selection), selection,
                                                   image_id, fingerprint, requested_port)
                    except Exception as error:
                        return complete(self._failure(self._failure_code(
                            error, "DOCKER_PUBLICATION_FAILED"), selection, image_id, fingerprint))
                    if isinstance(candidate, str):
                        # The service was absent before one bounded start attempt.
                        # If Docker leaves no selected runtime afterwards (for
                        # example, an occupied explicitly requested host port),
                        # that attempt failed to start.  A present runtime with
                        # malformed publication still retains its distinct
                        # DOCKER_PUBLICATION_FAILED classification.
                        return complete(self._failure(candidate if candidate != "absent"
                                                      else "DOCKER_START_FAILED", selection,
                                                      image_id, fingerprint))
                    if not self._ready(backend, candidate, token, deadline):
                        return complete(self._failure("READINESS_FAILED", selection,
                                                      image_id, fingerprint))
                    return complete(self._result("started", "READY_STARTED", selection, image_id,
                                                 fingerprint, candidate))
                if isinstance(candidate, str):
                    return complete(self._failure(candidate, selection, image_id, fingerprint))
                if not self._ready(backend, candidate, token, deadline):
                    return complete(self._failure("READINESS_FAILED", selection,
                                                  image_id, fingerprint))
                return complete(self._result("reused", "READY_REUSED", selection, image_id,
                                              fingerprint, candidate))
        except LaunchError as error:
            return self._failure(error.code, selection)


__all__ = ["ImageError", "LaunchError", "Launcher", "ProjectSelectionError"]
