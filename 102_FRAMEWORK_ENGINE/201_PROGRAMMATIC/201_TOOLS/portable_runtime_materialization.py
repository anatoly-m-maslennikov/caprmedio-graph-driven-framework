"""Stage an inert, package-owned runtime command fragment.

This module deliberately has no execution or activation entry point.  It
materializes the closed CA-D-601 command/environment/wrapper carriers beneath
the target temporary boundary while a concrete installation lock is held.  A
later publisher must obtain its own installation-specific command authority
before it can treat this prospective data as invocable.
"""

from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import re
import shlex
import stat
import tomllib

from framework_package import (
    FrameworkPackageError,
    VerifiedFrameworkPackage,
    verify_current_package_selector,
    verify_framework_package,
)
from installation_context import TargetProjectContext
from installation_transaction import InstallationPublicationLock, InstallationTransactionError


_NONCE = re.compile(r"[A-Za-z0-9][A-Za-z0-9._-]{0,127}\Z")
_UV_PREFIX = ("uv", "run", "--locked", "--no-sync", "--no-env-file")
_VARIABLE_NAMES = ("HOME", "PATH", "UV_CACHE_DIR", "UV_PROJECT_ENVIRONMENT")
_PACKAGE_CURRENT = Path(".caprmedio_install/current.toml")
_PACKAGE_RELEASES = Path(".caprmedio_install/releases")
_CONTEXTS = Path(".caprmedio_runtime/installation/contexts")
_STAGING = Path(".caprmedio_tmp/installation/staging")
_UV_PROJECT_ENVIRONMENT = Path(".caprmedio_runtime/launcher-venv")
_UV_CACHE_DIRECTORY = Path(".caprmedio_tmp/uv-cache")
_COMMAND_NAME = "command.toml"
_ENVIRONMENT_NAME = "environment.toml"
_WRAPPER_NAME = "wrapper"
_MANIFEST_NAME = "stage-manifest.toml"


class PortableRuntimeMaterializationError(RuntimeError):
    """Stable refusal at the inert runtime-command staging boundary."""

    def __init__(self, code: str, message: str) -> None:
        self.code = code
        super().__init__(f"{code}: {message}")


@dataclass(frozen=True)
class RuntimeCommandStageRequest:
    """Prospective, non-executable command data for one native generation."""

    package: VerifiedFrameworkPackage
    target_context: TargetProjectContext
    state_generation: int
    entrypoint: str
    fixed_arguments: tuple[str, ...]
    invocation_nonce: str
    path_directories: tuple[Path | str, ...]
    home: Path | str


@dataclass(frozen=True)
class RuntimeCommandStage:
    """Physically reopened inert command data; it grants no invocation right."""

    root: Path
    command_path: Path
    environment_path: Path
    wrapper_path: Path
    manifest_path: Path
    package_manifest_sha256: str
    target_project_context_sha256: str
    state_generation: int
    lock_generation: str
    command_sha256: str
    environment_sha256: str
    wrapper_sha256: str


def _refuse(code: str, message: str) -> None:
    raise PortableRuntimeMaterializationError(code, message)


def _sha256(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def _canonical_digest(value: object) -> str:
    try:
        payload = json.dumps(
            value,
            sort_keys=True,
            separators=(",", ":"),
            ensure_ascii=False,
            allow_nan=False,
        ).encode("utf-8")
    except (TypeError, ValueError) as error:  # pragma: no cover - guarded by typed input checks.
        _refuse("runtime-stage-schema-invalid", "carrier digest input is not canonical JSON")
        raise AssertionError from error
    return _sha256(payload)


def _quoted(value: str) -> str:
    return json.dumps(value, ensure_ascii=False)


def _toml_array(values: Sequence[str]) -> str:
    return "[" + ", ".join(_quoted(value) for value in values) + "]"


def _target_root(lock: object) -> tuple[InstallationPublicationLock, Path]:
    if not isinstance(lock, InstallationPublicationLock):
        _refuse("runtime-stage-lock-required", "staging requires the concrete installation publication lock")
    try:
        lock.revalidate()
    except InstallationTransactionError as error:
        _refuse("runtime-stage-lock-invalid", "installation publication lock is not active")
    root = lock.project_root
    try:
        observed = root.lstat()
    except OSError as error:
        _refuse("runtime-stage-target-invalid", "locked target root is unavailable")
    if root.is_symlink() or not stat.S_ISDIR(observed.st_mode):
        _refuse("runtime-stage-target-invalid", "locked target root is not a real directory")
    return lock, root


def _safe_relative(value: Path, *, code: str, label: str) -> Path:
    if value.is_absolute() or not value.parts or any(part in {"", ".", ".."} for part in value.parts):
        _refuse(code, f"{label} is not target-contained")
    return value


def _read_target_regular(
    root: Path, relative: Path, *, code: str, label: str, expected_mode: int | None = None
) -> bytes:
    """Reopen one regular target carrier without following a path component."""

    _safe_relative(relative, code=code, label=label)
    directory_flags = os.O_RDONLY | os.O_CLOEXEC | os.O_NOFOLLOW | os.O_DIRECTORY
    file_flags = os.O_RDONLY | os.O_CLOEXEC | os.O_NOFOLLOW
    try:
        directory_fd = os.open(root, directory_flags)
    except OSError as error:
        _refuse(code, f"{label} target root cannot be safely opened")
    try:
        for component in relative.parts[:-1]:
            try:
                next_fd = os.open(component, directory_flags, dir_fd=directory_fd)
            except OSError as error:
                _refuse(code, f"{label} has an unsafe ancestor")
            os.close(directory_fd)
            directory_fd = next_fd
        try:
            descriptor = os.open(relative.name, file_flags, dir_fd=directory_fd)
        except OSError as error:
            _refuse(code, f"{label} cannot be safely opened")
        try:
            observed = os.fstat(descriptor)
            if (
                not stat.S_ISREG(observed.st_mode)
                or observed.st_nlink != 1
                or (expected_mode is not None and observed.st_mode & 0o777 != expected_mode)
            ):
                _refuse(code, f"{label} is not an unaliased regular file")
            chunks: list[bytes] = []
            while True:
                chunk = os.read(descriptor, 65536)
                if not chunk:
                    break
                chunks.append(chunk)
            return b"".join(chunks)
        finally:
            os.close(descriptor)
    finally:
        os.close(directory_fd)


def _open_stage_parent(root: Path) -> int:
    """Open the declared staging parent through held no-follow descriptors."""

    directory_flags = os.O_RDONLY | os.O_CLOEXEC | os.O_NOFOLLOW | os.O_DIRECTORY
    try:
        descriptor = os.open(root, directory_flags)
    except OSError as error:
        _refuse("runtime-stage-path-unsafe", "target root cannot anchor staging")
    try:
        for component in _STAGING.parts:
            try:
                os.mkdir(component, mode=0o700, dir_fd=descriptor)
            except FileExistsError:
                pass
            except OSError as error:
                _refuse("runtime-stage-write-failed", "staging ancestor cannot be created")
            try:
                next_descriptor = os.open(component, directory_flags, dir_fd=descriptor)
            except OSError as error:
                _refuse("runtime-stage-path-unsafe", "staging ancestor cannot be safely opened")
            observed = os.fstat(next_descriptor)
            if not stat.S_ISDIR(observed.st_mode):  # pragma: no cover - O_DIRECTORY already protects this.
                os.close(next_descriptor)
                _refuse("runtime-stage-path-unsafe", "staging ancestor is not a real directory")
            os.close(descriptor)
            descriptor = next_descriptor
        return descriptor
    except BaseException:
        os.close(descriptor)
        raise


def _open_stage(stage_parent_fd: int, lock_generation: str) -> int:
    directory_flags = os.O_RDONLY | os.O_CLOEXEC | os.O_NOFOLLOW | os.O_DIRECTORY
    try:
        os.mkdir(lock_generation, mode=0o700, dir_fd=stage_parent_fd)
    except FileExistsError as error:
        _refuse("runtime-stage-conflict", "stage already exists for this installation lock generation")
    except OSError as error:
        _refuse("runtime-stage-write-failed", "stage root cannot be created")
    try:
        descriptor = os.open(lock_generation, directory_flags, dir_fd=stage_parent_fd)
    except OSError as error:
        _refuse("runtime-stage-path-unsafe", "new stage root cannot be safely opened")
    try:
        observed = os.fstat(descriptor)
        if not stat.S_ISDIR(observed.st_mode):  # pragma: no cover - O_DIRECTORY already protects this.
            _refuse("runtime-stage-path-unsafe", "new stage root is not a directory")
        return descriptor
    except BaseException:
        os.close(descriptor)
        raise


def _write_new(directory_fd: int, name: str, payload: bytes, *, mode: int) -> None:
    try:
        descriptor = os.open(
            name,
            os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_CLOEXEC | os.O_NOFOLLOW,
            mode,
            dir_fd=directory_fd,
        )
    except FileExistsError as error:
        _refuse("runtime-stage-conflict", f"stage carrier already exists: {name}")
    except OSError as error:
        _refuse("runtime-stage-write-failed", f"stage carrier cannot be created: {name}")
    try:
        offset = 0
        while offset < len(payload):
            written = os.write(descriptor, payload[offset:])
            if written <= 0:
                raise OSError("short write")
            offset += written
        os.fchmod(descriptor, mode)
        os.fsync(descriptor)
    except OSError as error:
        _refuse("runtime-stage-write-failed", f"stage carrier cannot be written: {name}")
    finally:
        os.close(descriptor)


def _read_stage_regular(directory_fd: int, name: str, *, expected_mode: int) -> bytes:
    try:
        descriptor = os.open(name, os.O_RDONLY | os.O_CLOEXEC | os.O_NOFOLLOW, dir_fd=directory_fd)
    except OSError as error:
        _refuse("runtime-stage-reopen-failed", f"stage carrier cannot be reopened: {name}")
    try:
        observed = os.fstat(descriptor)
        if not stat.S_ISREG(observed.st_mode) or observed.st_nlink != 1 or observed.st_mode & 0o777 != expected_mode:
            _refuse("runtime-stage-reopen-failed", f"stage carrier mode or kind changed: {name}")
        chunks: list[bytes] = []
        while True:
            chunk = os.read(descriptor, 65536)
            if not chunk:
                return b"".join(chunks)
            chunks.append(chunk)
    finally:
        os.close(descriptor)


def _absolute_path(value: Path | str, *, code: str, label: str, require_directory: bool) -> Path:
    try:
        candidate = Path(value)
    except (TypeError, ValueError) as error:
        _refuse(code, f"{label} is invalid")
    if not candidate.is_absolute() or any(part == ".." for part in candidate.parts):
        _refuse(code, f"{label} must be an explicit absolute path")
    rendered = candidate.as_posix()
    if not rendered or "\x00" in rendered or "\n" in rendered or "\r" in rendered:
        _refuse(code, f"{label} is unsafe")
    if require_directory:
        try:
            observed = candidate.lstat()
        except OSError as error:
            _refuse(code, f"{label} is unavailable")
        if candidate.is_symlink() or not stat.S_ISDIR(observed.st_mode):
            _refuse(code, f"{label} must name a real directory")
    return candidate


def _validate_fixed_arguments(value: object) -> tuple[str, ...]:
    if not isinstance(value, tuple):
        _refuse("runtime-stage-arguments-invalid", "fixed arguments must be an immutable tuple")
    checked: list[str] = []
    for argument in value:
        if not isinstance(argument, str) or "\x00" in argument or "\n" in argument or "\r" in argument:
            _refuse("runtime-stage-arguments-invalid", "fixed argument is unsafe")
        if argument == "--env-file" or argument.startswith("--env-file=") or argument == "-c" or argument.startswith("-c"):
            _refuse("runtime-stage-arguments-invalid", "environment-file and inline-code arguments are forbidden")
        if Path(argument).is_absolute():
            _refuse("runtime-stage-arguments-invalid", "fixed argument cannot name an absolute host path")
        checked.append(argument)
    return tuple(checked)


def _validate_entrypoint(target_root: Path, package: VerifiedFrameworkPackage, value: object) -> str:
    if not isinstance(value, str) or not value:
        _refuse("runtime-stage-entrypoint-invalid", "entrypoint must be a non-empty package-relative path")
    relative = PurePosixPath(value)
    if (
        relative.is_absolute()
        or relative.as_posix() != value
        or relative.suffix != ".py"
        or not relative.parts
        or any(part in {"", ".", ".."} for part in relative.parts)
    ):
        _refuse("runtime-stage-entrypoint-invalid", "entrypoint must be a safe package-relative Python member")
    rows = [row for row in package.inventory if row.path == value and row.role == "engine"]
    if len(rows) != 1:
        _refuse("runtime-stage-entrypoint-unadmitted", "entrypoint is not one admitted engine member")
    payload = _read_target_regular(
        target_root,
        _PACKAGE_RELEASES / package.manifest_digest / Path(relative.as_posix()),
        code="runtime-stage-entrypoint-unadmitted",
        label="entrypoint",
        expected_mode=rows[0].mode,
    )
    if _sha256(payload) != rows[0].sha256:
        _refuse("runtime-stage-entrypoint-unadmitted", "entrypoint differs from the package inventory")
    return value


def _reopen_selected_package(root: Path, value: object) -> VerifiedFrameworkPackage:
    if not isinstance(value, VerifiedFrameworkPackage):
        _refuse("runtime-stage-package-invalid", "stage requires a typed verified Framework package")
    try:
        reopened = verify_framework_package(value.root)
    except FrameworkPackageError as error:
        _refuse("runtime-stage-package-invalid", "Framework package cannot be physically reopened")
    if reopened != value:
        _refuse("runtime-stage-package-stale", "typed package differs from its physical package bytes")
    expected_root = root / _PACKAGE_RELEASES / reopened.manifest_digest
    if reopened.root != expected_root:
        _refuse("runtime-stage-package-unselected", "package is not at the target selected-release location")
    selector_payload = _read_target_regular(
        root, _PACKAGE_CURRENT, code="runtime-stage-selector-invalid", label="current package selector"
    )
    try:
        verify_current_package_selector(selector_payload, reopened)
    except FrameworkPackageError as error:
        _refuse("runtime-stage-selector-invalid", "current package selector does not admit the reopened package")
    lock_member = next((row for row in reopened.inventory if row.path == "uv.lock" and row.role == "dependency"), None)
    if lock_member is None:
        _refuse("runtime-stage-package-invalid", "selected package omits its admitted uv.lock carrier")
    lock_payload = _read_target_regular(
        root,
        _PACKAGE_RELEASES / reopened.manifest_digest / "uv.lock",
        code="runtime-stage-package-stale",
        label="selected package uv.lock",
        expected_mode=lock_member.mode,
    )
    if _sha256(lock_payload) != lock_member.sha256:
        _refuse("runtime-stage-package-stale", "selected package uv.lock differs from its inventory")
    return reopened


def _reopen_context(root: Path, value: object, package: VerifiedFrameworkPackage, lock: InstallationPublicationLock) -> TargetProjectContext:
    if not isinstance(value, TargetProjectContext):
        _refuse("runtime-stage-context-invalid", "stage requires a typed target Project context")
    if value.sha256 != lock.target_context_sha256:
        _refuse("runtime-stage-context-mismatch", "installation lock names another target context")
    evidence = value.package_evidence
    if (
        evidence.package_manifest_sha256 != package.manifest_digest
        or evidence.catalog_sha256 != package.source_catalog_sha256
        or evidence.verified is not True
    ):
        _refuse("runtime-stage-context-mismatch", "target context does not bind the reopened package")
    relative = _CONTEXTS / f"{value.sha256}.toml"
    actual = _read_target_regular(root, relative, code="runtime-stage-context-stale", label="target context")
    if actual != value.with_digest_toml():
        _refuse("runtime-stage-context-stale", "persisted target context differs from typed context bytes")
    return value


def _environment(root: Path, request: RuntimeCommandStageRequest) -> tuple[dict[str, str], str, bytes]:
    if not isinstance(request.path_directories, tuple) or not request.path_directories:
        _refuse("runtime-stage-environment-invalid", "PATH needs a non-empty immutable directory tuple")
    directories = tuple(
        _absolute_path(value, code="runtime-stage-environment-invalid", label="PATH entry", require_directory=True)
        for value in request.path_directories
    )
    if len({directory.as_posix() for directory in directories}) != len(directories):
        _refuse("runtime-stage-environment-invalid", "PATH directory entries must be unique")
    home = _absolute_path(request.home, code="runtime-stage-environment-invalid", label="HOME", require_directory=False)
    variables = {
        "HOME": home.as_posix(),
        "PATH": ":".join(directory.as_posix() for directory in directories),
        "UV_CACHE_DIR": (root / _UV_CACHE_DIRECTORY).as_posix(),
        "UV_PROJECT_ENVIRONMENT": (root / _UV_PROJECT_ENVIRONMENT).as_posix(),
    }
    payload = {"schema_version": 1, "variables": variables}
    digest = _canonical_digest(payload)
    rendered = _render_environment(variables, digest)
    return variables, digest, rendered


def _render_command(document: dict[str, object]) -> bytes:
    return (
        "\n".join(
            (
                "schema_version = 1",
                f"package_manifest_sha256 = {_quoted(str(document['package_manifest_sha256']))}",
                f"target_project_context_sha256 = {_quoted(str(document['target_project_context_sha256']))}",
                f"state_generation = {document['state_generation']}",
                f"entrypoint = {_quoted(str(document['entrypoint']))}",
                f"argv = {_toml_array(document['argv'])}",  # type: ignore[arg-type]
                f"environment_sha256 = {_quoted(str(document['environment_sha256']))}",
                f"wrapper_sha256 = {_quoted(str(document['wrapper_sha256']))}",
                f"invocation_nonce = {_quoted(str(document['invocation_nonce']))}",
                f"command_sha256 = {_quoted(str(document['command_sha256']))}",
                "",
            )
        ).encode("utf-8")
    )


def _render_environment(variables: dict[str, str], digest: str) -> bytes:
    lines = ["schema_version = 1", f"environment_sha256 = {_quoted(digest)}", "", "[variables]"]
    lines.extend(f"{name} = {_quoted(variables[name])}" for name in _VARIABLE_NAMES)
    return ("\n".join((*lines, ""))).encode("utf-8")


def _render_wrapper(package_root: Path, variables: dict[str, str], argv: tuple[str, ...]) -> bytes:
    assignments = " ".join(shlex.quote(f"{name}={variables[name]}") for name in _VARIABLE_NAMES)
    command = " ".join(shlex.quote(value) for value in argv)
    return f"#!/bin/sh\ncd {shlex.quote(package_root.as_posix())}\nexec env -i {assignments} {command}\n".encode("utf-8")


def _render_manifest(
    *, package_manifest_sha256: str, target_project_context_sha256: str, state_generation: int, lock_generation: str,
    files: tuple[tuple[str, int, str], ...],
) -> bytes:
    lines = [
        "schema_version = 1",
        f"package_manifest_sha256 = {_quoted(package_manifest_sha256)}",
        f"target_project_context_sha256 = {_quoted(target_project_context_sha256)}",
        f"state_generation = {state_generation}",
        f"lock_generation = {_quoted(lock_generation)}",
        "",
    ]
    for path, mode, digest in files:
        lines.extend(("[[files]]", f"path = {_quoted(path)}", f"mode = {mode}", f"sha256 = {_quoted(digest)}", ""))
    return "\n".join(lines).encode("utf-8")


def _parse_toml(payload: bytes, *, code: str, label: str) -> dict[str, object]:
    try:
        document = tomllib.loads(payload.decode("utf-8"))
    except (UnicodeDecodeError, tomllib.TOMLDecodeError) as error:
        _refuse(code, f"{label} is not valid UTF-8 TOML")
    if not isinstance(document, dict):  # pragma: no cover - tomllib uses dict for table roots.
        _refuse(code, f"{label} is not a TOML table")
    return document


def _validate_reopened_fragment(
    stage_fd: int,
    *,
    expected_command: bytes,
    expected_environment: bytes,
    expected_wrapper: bytes,
    expected_manifest: bytes,
    command_digest: str,
    environment_digest: str,
    wrapper_digest: str,
) -> None:
    observed: dict[str, bytes] = {}
    for name, expected, mode in (
        (_COMMAND_NAME, expected_command, 0o600),
        (_ENVIRONMENT_NAME, expected_environment, 0o600),
        (_WRAPPER_NAME, expected_wrapper, 0o700),
        (_MANIFEST_NAME, expected_manifest, 0o600),
    ):
        payload = _read_stage_regular(stage_fd, name, expected_mode=mode)
        if payload != expected:
            _refuse("runtime-stage-reopen-failed", f"stage carrier bytes differ: {name}")
        observed[name] = payload
    command = _parse_toml(observed[_COMMAND_NAME], code="runtime-stage-reopen-failed", label="command")
    environment = _parse_toml(observed[_ENVIRONMENT_NAME], code="runtime-stage-reopen-failed", label="environment")
    manifest = _parse_toml(observed[_MANIFEST_NAME], code="runtime-stage-reopen-failed", label="stage manifest")
    command_keys = {
        "schema_version", "package_manifest_sha256", "target_project_context_sha256", "state_generation", "entrypoint",
        "argv", "environment_sha256", "wrapper_sha256", "invocation_nonce", "command_sha256",
    }
    if set(command) != command_keys or command.get("command_sha256") != command_digest:
        _refuse("runtime-stage-reopen-failed", "command carrier is not closed")
    command_body = {key: value for key, value in command.items() if key != "command_sha256"}
    if _canonical_digest(command_body) != command_digest:
        _refuse("runtime-stage-reopen-failed", "command digest differs from canonical command data")
    if set(environment) != {"schema_version", "variables", "environment_sha256"} or environment.get("environment_sha256") != environment_digest:
        _refuse("runtime-stage-reopen-failed", "environment carrier is not closed")
    environment_body = {key: value for key, value in environment.items() if key != "environment_sha256"}
    if _canonical_digest(environment_body) != environment_digest:
        _refuse("runtime-stage-reopen-failed", "environment digest differs from canonical environment data")
    if set(manifest) != {"schema_version", "package_manifest_sha256", "target_project_context_sha256", "state_generation", "lock_generation", "files"}:
        _refuse("runtime-stage-reopen-failed", "stage manifest is not closed")
    rows = manifest.get("files")
    expected_rows = [
        {"path": _COMMAND_NAME, "mode": 0o600, "sha256": _sha256(observed[_COMMAND_NAME])},
        {"path": _ENVIRONMENT_NAME, "mode": 0o600, "sha256": _sha256(observed[_ENVIRONMENT_NAME])},
        {"path": _WRAPPER_NAME, "mode": 0o700, "sha256": wrapper_digest},
    ]
    if rows != expected_rows:
        _refuse("runtime-stage-reopen-failed", "stage manifest inventory differs from staged carriers")


def _validate_visible_fragment(
    target_root: Path,
    lock_generation: str,
    *,
    expected_command: bytes,
    expected_environment: bytes,
    expected_wrapper: bytes,
    expected_manifest: bytes,
) -> None:
    """Ensure the returned target-relative paths still name the held stage."""

    for name, expected, mode in (
        (_COMMAND_NAME, expected_command, 0o600),
        (_ENVIRONMENT_NAME, expected_environment, 0o600),
        (_WRAPPER_NAME, expected_wrapper, 0o700),
        (_MANIFEST_NAME, expected_manifest, 0o600),
    ):
        actual = _read_target_regular(
            target_root,
            _STAGING / lock_generation / name,
            code="runtime-stage-reopen-failed",
            label=f"visible stage carrier {name}",
            expected_mode=mode,
        )
        if actual != expected:
            _refuse("runtime-stage-reopen-failed", f"visible stage carrier differs: {name}")


def stage_runtime_command(request: RuntimeCommandStageRequest, *, lock: InstallationPublicationLock) -> RuntimeCommandStage:
    """Create and reopen one inert native command fragment under a live lock.

    The function only writes beneath ``.caprmedio_tmp/installation/staging``.
    It neither invokes the wrapper nor changes configuration, any selector,
    Skills, projections, package bytes, or runtime environment directories.
    """

    if not isinstance(request, RuntimeCommandStageRequest):
        _refuse("runtime-stage-request-invalid", "staging requires a typed request")
    concrete_lock, target_root = _target_root(lock)
    package = _reopen_selected_package(target_root, request.package)
    context = _reopen_context(target_root, request.target_context, package, concrete_lock)
    if isinstance(request.state_generation, bool) or not isinstance(request.state_generation, int) or request.state_generation < 1:
        _refuse("runtime-stage-generation-invalid", "native state generation must be a positive integer")
    if not isinstance(request.invocation_nonce, str) or _NONCE.fullmatch(request.invocation_nonce) is None:
        _refuse("runtime-stage-nonce-invalid", "invocation nonce is invalid")
    entrypoint = _validate_entrypoint(target_root, package, request.entrypoint)
    fixed_arguments = _validate_fixed_arguments(request.fixed_arguments)
    variables, environment_digest, environment_payload = _environment(target_root, request)
    argv = (*_UV_PREFIX, "--project", package.root.as_posix(), "python", entrypoint, *fixed_arguments)
    wrapper_payload = _render_wrapper(package.root, variables, argv)
    wrapper_digest = _sha256(wrapper_payload)
    command_body: dict[str, object] = {
        "schema_version": 1,
        "package_manifest_sha256": package.manifest_digest,
        "target_project_context_sha256": context.sha256,
        "state_generation": request.state_generation,
        "entrypoint": entrypoint,
        "argv": list(argv),
        "environment_sha256": environment_digest,
        "wrapper_sha256": wrapper_digest,
        "invocation_nonce": request.invocation_nonce,
    }
    command_digest = _canonical_digest(command_body)
    command = {**command_body, "command_sha256": command_digest}
    command_payload = _render_command(command)

    concrete_lock.revalidate()
    parent_fd = _open_stage_parent(target_root)
    stage_root = target_root / _STAGING / concrete_lock.lock_generation
    files = (
        (_COMMAND_NAME, 0o600, _sha256(command_payload)),
        (_ENVIRONMENT_NAME, 0o600, _sha256(environment_payload)),
        (_WRAPPER_NAME, 0o700, wrapper_digest),
    )
    manifest_payload = _render_manifest(
        package_manifest_sha256=package.manifest_digest,
        target_project_context_sha256=context.sha256,
        state_generation=request.state_generation,
        lock_generation=concrete_lock.lock_generation,
        files=files,
    )
    try:
        stage_fd = _open_stage(parent_fd, concrete_lock.lock_generation)
        try:
            _write_new(stage_fd, _COMMAND_NAME, command_payload, mode=0o600)
            _write_new(stage_fd, _ENVIRONMENT_NAME, environment_payload, mode=0o600)
            _write_new(stage_fd, _WRAPPER_NAME, wrapper_payload, mode=0o700)
            _write_new(stage_fd, _MANIFEST_NAME, manifest_payload, mode=0o600)
            os.fsync(stage_fd)
            concrete_lock.revalidate()
            _validate_reopened_fragment(
                stage_fd,
                expected_command=command_payload,
                expected_environment=environment_payload,
                expected_wrapper=wrapper_payload,
                expected_manifest=manifest_payload,
                command_digest=command_digest,
                environment_digest=environment_digest,
                wrapper_digest=wrapper_digest,
            )
            _validate_visible_fragment(
                target_root,
                concrete_lock.lock_generation,
                expected_command=command_payload,
                expected_environment=environment_payload,
                expected_wrapper=wrapper_payload,
                expected_manifest=manifest_payload,
            )
            concrete_lock.revalidate()
        finally:
            os.close(stage_fd)
    finally:
        os.close(parent_fd)
    return RuntimeCommandStage(
        root=stage_root,
        command_path=stage_root / _COMMAND_NAME,
        environment_path=stage_root / _ENVIRONMENT_NAME,
        wrapper_path=stage_root / _WRAPPER_NAME,
        manifest_path=stage_root / _MANIFEST_NAME,
        package_manifest_sha256=package.manifest_digest,
        target_project_context_sha256=context.sha256,
        state_generation=request.state_generation,
        lock_generation=concrete_lock.lock_generation,
        command_sha256=command_digest,
        environment_sha256=environment_digest,
        wrapper_sha256=wrapper_digest,
    )


__all__ = [
    "PortableRuntimeMaterializationError",
    "RuntimeCommandStage",
    "RuntimeCommandStageRequest",
    "stage_runtime_command",
]
