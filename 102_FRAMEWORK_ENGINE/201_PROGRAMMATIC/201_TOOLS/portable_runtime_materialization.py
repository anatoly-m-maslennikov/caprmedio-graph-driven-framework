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
import sys
import tomllib

from framework_package import (
    FrameworkPackageError,
    VerifiedFrameworkPackage,
    verify_current_package_selector,
    verify_framework_package,
)
from installation_context import TargetProjectContext
from installation_transaction import InstallationPublicationLock, InstallationTransactionError
from installed_mcp_binding import InstalledMcpBindingError, _context as _read_d600_context
from retained_full_gate_packet import RetainedNativeFullGatePacket


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
_FINAL_FRAGMENT_NAMES = frozenset((_COMMAND_NAME, _ENVIRONMENT_NAME, _WRAPPER_NAME, _MANIFEST_NAME))
_FINAL_LOCK_GENERATION = re.compile(r"[0-9a-f]{32}\Z")
_SHA256 = re.compile(r"[0-9a-f]{64}\Z")


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
class CandidateRuntimeCommandStageRequest:
    """Prospective command data for a sealed package before selector publication.

    The packet is merely transport.  ``stage_candidate_runtime_command``
    physically reopens its retained Full Gate before the package can be used.
    """

    package: VerifiedFrameworkPackage
    target_context: TargetProjectContext
    prospective_package_selector: bytes
    full_gate_packet: RetainedNativeFullGatePacket
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
    try:
        package_relative = package.root.relative_to(target_root)
    except ValueError:
        _refuse("runtime-stage-entrypoint-unadmitted", "entrypoint package is outside the target Project")
    payload = _read_target_regular(
        target_root,
        package_relative / Path(relative.as_posix()),
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


def _target_contained_directory(root: Path, value: object, *, code: str, label: str) -> Path:
    """Return one real target-contained directory without traversing aliases."""

    if not isinstance(value, Path) or not value.is_absolute():
        _refuse(code, f"{label} must be an absolute target-contained directory")
    try:
        relative = value.relative_to(root)
    except ValueError:
        _refuse(code, f"{label} is outside the locked target Project")
    if not relative.parts:
        _refuse(code, f"{label} must not be the target Project root")
    if any(component in {"", ".", ".."} for component in relative.parts):
        _refuse(code, f"{label} is not a safe target-contained directory")
    cursor = root
    for component in relative.parts:
        cursor = cursor / component
        try:
            observed = cursor.lstat()
        except OSError:
            _refuse(code, f"{label} is unavailable")
        if cursor.is_symlink() or not stat.S_ISDIR(observed.st_mode):
            _refuse(code, f"{label} has an unsafe directory boundary")
    return value


def _target_retained_full_gate_artifact_root(root: Path, value: object) -> Path:
    """Reopen the retained Full Gate root, which may be the target Project root.

    Retained Full Gate evidence is the sole carrier permitted to name the
    target root itself.  Its descriptor, package, receipt, and every other
    carrier remain required to be strict contained descendants.
    """

    if isinstance(value, Path) and value == root:
        return root
    return _target_contained_directory(
        root,
        value,
        code="candidate-full-gate-invalid",
        label="candidate Full Gate artifact root",
    )


def _target_contained_regular(root: Path, value: object, *, code: str, label: str) -> Path:
    """Return one real target-contained regular carrier without aliases."""

    if not isinstance(value, Path) or not value.is_absolute():
        _refuse(code, f"{label} must be an absolute target-contained carrier")
    try:
        relative = value.relative_to(root)
    except ValueError:
        _refuse(code, f"{label} is outside the locked target Project")
    if not relative.parts:
        _refuse(code, f"{label} must not be the target Project root")
    if any(component in {"", ".", ".."} for component in relative.parts):
        _refuse(code, f"{label} is not a safe target-contained carrier")
    cursor = root
    for component in relative.parts:
        cursor = cursor / component
        try:
            observed = cursor.lstat()
        except OSError:
            _refuse(code, f"{label} is unavailable")
        if cursor.is_symlink():
            _refuse(code, f"{label} has an unsafe directory boundary")
        if component != relative.parts[-1] and not stat.S_ISDIR(observed.st_mode):
            _refuse(code, f"{label} has a non-directory ancestor")
    if not stat.S_ISREG(observed.st_mode):
        _refuse(code, f"{label} is not a regular carrier")
    return value


def _release_version_root() -> Path:
    """Locate only the host-owned retained Full Gate verifier."""

    release_root = Path(__file__).resolve().parent / "RELEASE_VERSION"
    try:
        observed = release_root.lstat()
    except OSError:
        _refuse("candidate-full-gate-unavailable", "package-owned retained Full Gate verifier is unavailable")
    if release_root.is_symlink() or not stat.S_ISDIR(observed.st_mode):
        _refuse("candidate-full-gate-unavailable", "package-owned retained Full Gate verifier is unavailable")
    return release_root


def _candidate_packet_path(root: Path, value: object, *, label: str) -> Path:
    return _target_contained_regular(root, value, code="candidate-full-gate-invalid", label=label)


def _reopen_candidate_full_gate(
    root: Path,
    package: VerifiedFrameworkPackage,
    selector: object,
    packet: object,
) -> None:
    """Physically reopen the retained Full Gate for one sealed target candidate."""

    if not isinstance(packet, RetainedNativeFullGatePacket):
        _refuse("candidate-full-gate-invalid", "candidate retained Full Gate packet must be typed")
    artifact_root = _target_retained_full_gate_artifact_root(root, packet.artifact_root)
    release_root = _release_version_root()
    release_path = release_root.as_posix()
    added_release_path = release_path not in sys.path
    if added_release_path:
        sys.path.insert(0, release_path)
    try:
        try:
            from release_contract import ReleaseContractError
            from release_e2e_gate import PortableCandidateE2EGateEvidence
            from release_full_gate import NativeFullGateEvidence, verify_detached_native_full_gate_evidence
            from release_image import PortableImageBuildEvidence, PortableImageVerificationEvidence
            from release_retained_candidate import RetainedCandidateIdentity
            from release_suite import PortableSuiteGateEvidence
        except ImportError as error:
            _refuse("candidate-full-gate-unavailable", "package-owned retained Full Gate verifier cannot be imported")
            raise AssertionError from error
        if not (
            isinstance(packet.retained_candidate, RetainedCandidateIdentity)
            and isinstance(packet.suite, PortableSuiteGateEvidence)
            and isinstance(packet.build, PortableImageBuildEvidence)
            and isinstance(packet.verification, PortableImageVerificationEvidence)
            and isinstance(packet.e2e, PortableCandidateE2EGateEvidence)
            and isinstance(packet.evidence, NativeFullGateEvidence)
        ):
            _refuse("candidate-full-gate-invalid", "candidate retained Full Gate packet has untrusted carriers")
        retained_candidate = packet.retained_candidate
        retained_package = getattr(retained_candidate, "package_evidence", None)
        retained_view = getattr(retained_package, "view", None)
        _candidate_packet_path(root, getattr(retained_candidate, "descriptor_path", None), label="candidate descriptor")
        _candidate_packet_path(root, getattr(retained_package, "receipt_path", None), label="candidate package sidecar")
        retained_package_root = _target_contained_directory(
            root,
            getattr(retained_view, "package_root", None),
            code="candidate-full-gate-invalid",
            label="candidate sealed package",
        )
        try:
            retained = verify_detached_native_full_gate_evidence(
                artifact_root,
                retained_candidate,
                packet.suite,
                packet.build,
                packet.verification,
                packet.e2e,
                packet.evidence,
            )
        except ReleaseContractError as error:
            _refuse("candidate-full-gate-invalid", "candidate retained Full Gate evidence cannot be reopened")
        if retained.view.package_root != retained_package_root or package.root != retained_package_root:
            _refuse("candidate-package-mismatch", "candidate package is not the retained sealed Full Gate package")
        evidence = packet.evidence
        image_digest = getattr(evidence, "candidate_image_digest", None)
        receipt_sha256 = getattr(evidence, "receipt_sha256", None)
        if not isinstance(image_digest, str) or not image_digest.startswith("sha256:"):
            _refuse("candidate-full-gate-invalid", "candidate Full Gate image digest is invalid")
        if (
            getattr(selector, "image_digest", None) != image_digest.removeprefix("sha256:")
            or getattr(selector, "full_gate_receipt_sha256", None) != receipt_sha256
        ):
            _refuse("candidate-full-gate-mismatch", "prospective package selector differs from the retained Full Gate")
        view = retained.view
        if (
            view.actual_package_manifest_sha256 != package.manifest_digest
            or view.source_catalog_sha256 != package.source_catalog_sha256
            or view.framework_version != package.framework_version
            or view.version_toml_sha256 != package.version_toml_sha256
        ):
            _refuse("candidate-full-gate-mismatch", "retained Full Gate does not bind the physical candidate package")
    finally:
        if added_release_path:
            try:
                sys.path.remove(release_path)
            except ValueError:
                pass


def _reopen_candidate_package(
    root: Path,
    value: object,
    prospective_selector: object,
    full_gate_packet: object,
) -> VerifiedFrameworkPackage:
    """Reopen a sealed candidate without requiring an installed selector."""

    if not isinstance(value, VerifiedFrameworkPackage):
        _refuse("candidate-package-invalid", "candidate stage requires a typed verified Framework package")
    candidate_root = _target_contained_directory(
        root, value.root, code="candidate-package-invalid", label="candidate package root"
    )
    try:
        relative = candidate_root.relative_to(root)
        if relative.parts[0] != ".caprmedio_tmp":
            _refuse("candidate-package-unsealed", "candidate package must remain under target temporary staging")
        reopened = verify_framework_package(candidate_root)
    except FrameworkPackageError:
        _refuse("candidate-package-invalid", "candidate Framework package cannot be physically reopened")
    if reopened != value:
        _refuse("candidate-package-stale", "typed candidate package differs from its physical bytes")
    if not isinstance(prospective_selector, bytes):
        _refuse("candidate-selector-invalid", "candidate package selector must be exact bytes")
    try:
        selector = verify_current_package_selector(prospective_selector, reopened)
    except FrameworkPackageError:
        _refuse("candidate-selector-invalid", "prospective package selector does not admit the physical candidate")
    _reopen_candidate_full_gate(root, reopened, selector, full_gate_packet)
    lock_member = next((row for row in reopened.inventory if row.path == "uv.lock" and row.role == "dependency"), None)
    if lock_member is None:
        _refuse("candidate-package-invalid", "sealed candidate package omits its admitted uv.lock carrier")
    lock_payload = _read_target_regular(
        root,
        relative / "uv.lock",
        code="candidate-package-stale",
        label="candidate package uv.lock",
        expected_mode=lock_member.mode,
    )
    if _sha256(lock_payload) != lock_member.sha256:
        _refuse("candidate-package-stale", "candidate package uv.lock differs from its inventory")
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


def _reopen_candidate_context(
    root: Path, value: object, package: VerifiedFrameworkPackage, lock: InstallationPublicationLock
) -> TargetProjectContext:
    """Require a full D600 physical reopen before candidate-stage writes."""

    context = _reopen_context(root, value, package, lock)
    try:
        persisted = _read_d600_context(root, context.sha256)
    except InstalledMcpBindingError:
        _refuse("candidate-context-invalid", "persisted target context is not a valid D600 carrier")
    if (
        persisted.mode != context.mode
        or persisted.target_project_identity != context.target_project_identity
        or persisted.control_child_relpath != context.control_child_relpath
        or persisted.control_child_relpath == ".caprmedio_"
    ):
        _refuse("candidate-context-mismatch", "persisted target context differs from typed context identity")
    return context


def _environment(
    root: Path, request: RuntimeCommandStageRequest | CandidateRuntimeCommandStageRequest
) -> tuple[dict[str, str], str, bytes]:
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


def _require_fragment_digest(value: object, *, code: str, label: str) -> str:
    if not isinstance(value, str) or _SHA256.fullmatch(value) is None:
        _refuse(code, f"{label} is not a lowercase SHA-256")
    return value


def _validate_fragment_documents(
    command_payload: bytes,
    environment_payload: bytes,
    wrapper_payload: bytes,
    manifest_payload: bytes,
    *,
    code: str,
) -> tuple[dict[str, object], dict[str, object], dict[str, object]]:
    """Validate the one shared D601 carrier schema and inventory policy.

    Both the stage writer and the final-generation reader pass through this
    exact parser.  Callers retain responsibility for their location-specific
    bindings (selected package, current generation, and final wrapper argv).
    """

    command = _parse_toml(command_payload, code=code, label="command")
    environment = _parse_toml(environment_payload, code=code, label="environment")
    manifest = _parse_toml(manifest_payload, code=code, label="stage manifest")
    command_keys = {
        "schema_version", "package_manifest_sha256", "target_project_context_sha256", "state_generation", "entrypoint",
        "argv", "environment_sha256", "wrapper_sha256", "invocation_nonce", "command_sha256",
    }
    if (
        set(command) != command_keys
        or type(command.get("schema_version")) is not int
        or command.get("schema_version") != 1
    ):
        _refuse(code, "command carrier is not closed")
    generation = command.get("state_generation")
    if isinstance(generation, bool) or not isinstance(generation, int) or generation < 1:
        _refuse(code, "command generation is invalid")
    for key in ("package_manifest_sha256", "target_project_context_sha256", "environment_sha256", "wrapper_sha256", "command_sha256"):
        _require_fragment_digest(command.get(key), code=code, label=key)
    if not isinstance(command.get("entrypoint"), str) or not isinstance(command.get("invocation_nonce"), str):
        _refuse(code, "command entrypoint or nonce is invalid")
    if not isinstance(command.get("argv"), list) or any(not isinstance(value, str) for value in command["argv"]):
        _refuse(code, "command argv is invalid")
    command_body = {key: value for key, value in command.items() if key != "command_sha256"}
    if _canonical_digest(command_body) != command["command_sha256"]:
        _refuse(code, "command digest differs from canonical command data")

    if (
        set(environment) != {"schema_version", "variables", "environment_sha256"}
        or type(environment.get("schema_version")) is not int
        or environment.get("schema_version") != 1
        or not isinstance(environment.get("variables"), dict)
    ):
        _refuse(code, "environment carrier is not closed")
    variables = environment["variables"]
    if set(variables) != set(_VARIABLE_NAMES) or any(not isinstance(variables.get(name), str) for name in _VARIABLE_NAMES):
        _refuse(code, "environment variables are not closed")
    environment_digest = _require_fragment_digest(environment.get("environment_sha256"), code=code, label="environment digest")
    environment_body = {key: value for key, value in environment.items() if key != "environment_sha256"}
    if _canonical_digest(environment_body) != environment_digest:
        _refuse(code, "environment digest differs from canonical environment data")
    if command["environment_sha256"] != environment_digest:
        _refuse(code, "command differs from environment binding")
    wrapper_digest = _require_fragment_digest(command.get("wrapper_sha256"), code=code, label="wrapper digest")
    if _sha256(wrapper_payload) != wrapper_digest:
        _refuse(code, "wrapper digest differs from command binding")

    if (
        set(manifest) != {"schema_version", "package_manifest_sha256", "target_project_context_sha256", "state_generation", "lock_generation", "files"}
        or type(manifest.get("schema_version")) is not int
        or manifest.get("schema_version") != 1
        or isinstance(manifest.get("state_generation"), bool)
        or not isinstance(manifest.get("state_generation"), int)
        or manifest["state_generation"] < 1
        or not isinstance(manifest.get("lock_generation"), str)
        or _FINAL_LOCK_GENERATION.fullmatch(manifest["lock_generation"]) is None
        or not isinstance(manifest.get("files"), list)
    ):
        _refuse(code, "stage manifest is not closed")
    for key in ("package_manifest_sha256", "target_project_context_sha256"):
        _require_fragment_digest(manifest.get(key), code=code, label=f"manifest {key}")
    expected_rows = [
        {"path": _COMMAND_NAME, "mode": 0o600, "sha256": _sha256(command_payload)},
        {"path": _ENVIRONMENT_NAME, "mode": 0o600, "sha256": _sha256(environment_payload)},
        {"path": _WRAPPER_NAME, "mode": 0o700, "sha256": _sha256(wrapper_payload)},
    ]
    if manifest["files"] != expected_rows:
        _refuse(code, "stage manifest inventory differs from command carriers")
    return command, environment, manifest


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
    command, environment, _manifest = _validate_fragment_documents(
        observed[_COMMAND_NAME], observed[_ENVIRONMENT_NAME], observed[_WRAPPER_NAME], observed[_MANIFEST_NAME],
        code="runtime-stage-reopen-failed",
    )
    if (
        command.get("command_sha256") != command_digest
        or environment.get("environment_sha256") != environment_digest
        or command.get("wrapper_sha256") != wrapper_digest
    ):
        _refuse("runtime-stage-reopen-failed", "stage carrier digest differs from opened stage")


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


def _final_generation_carriers(
    root: Path, generation: int, *, release_proof_sha256: str | None = None,
) -> dict[str, bytes]:
    """Read the D601 fragment, optionally with its separately bound D604 proof.

    A final native generation contains the four command-fragment carriers and
    the release proof. The proof is not a member of the command-stage manifest;
    its caller has already validated and bound its complete bytes separately.
    """

    relative = Path(".caprmedio_runtime/installation/generations") / str(generation)
    cursor = root
    try:
        for component in relative.parts:
            cursor = cursor / component
            observed = os.lstat(cursor)
            if stat.S_ISLNK(observed.st_mode) or not stat.S_ISDIR(observed.st_mode):
                _refuse("runtime-final-command-invalid", "final command generation has an unsafe directory boundary")
        entries = {entry.name: entry for entry in os.scandir(cursor)}
    except PortableRuntimeMaterializationError:
        raise
    except OSError as error:
        raise PortableRuntimeMaterializationError("runtime-final-command-invalid", "final command generation cannot be reopened") from error
    expected_names = _FINAL_FRAGMENT_NAMES
    if release_proof_sha256 is not None:
        _require_fragment_digest(release_proof_sha256, code="runtime-final-command-invalid", label="release proof digest")
        expected_names = expected_names | {"release-proof.toml"}
    if set(entries) != expected_names:
        _refuse("runtime-final-command-invalid", "final command generation file inventory is not closed")
    modes = {
        _COMMAND_NAME: 0o600,
        _ENVIRONMENT_NAME: 0o600,
        _WRAPPER_NAME: 0o700,
        _MANIFEST_NAME: 0o600,
    }
    if release_proof_sha256 is not None:
        modes["release-proof.toml"] = 0o600
    result: dict[str, bytes] = {}
    for name, expected_mode in modes.items():
        try:
            observed = entries[name].stat(follow_symlinks=False)
        except OSError as error:
            raise PortableRuntimeMaterializationError("runtime-final-command-invalid", f"final command carrier is unavailable: {name}") from error
        if (
            not stat.S_ISREG(observed.st_mode)
            or observed.st_nlink != 1
            or observed.st_mode & 0o777 != expected_mode
        ):
            _refuse("runtime-final-command-invalid", f"final command carrier is unsafe: {name}")
        result[name] = _read_target_regular(
            root,
            relative / name,
            code="runtime-final-command-invalid",
            label=f"final command carrier {name}",
            expected_mode=expected_mode,
        )
    if release_proof_sha256 is not None and _sha256(result["release-proof.toml"]) != release_proof_sha256:
        _refuse("runtime-final-command-mismatch", "release proof changed while reopening the final generation")
    return result


def reopen_final_runtime_command_fragment(
    project_root: str | Path,
    package: VerifiedFrameworkPackage,
    *,
    target_context_sha256: str,
    state_generation: int,
    installation_lock_generation: str,
    command_sha256: str,
    stage_manifest_sha256: str,
    release_proof_sha256: str | None = None,
) -> None:
    """Physically reopen the final D601 carriers selected by one D604 proof.

    The function is read-only and deliberately shares the D601 closed-schema
    and manifest-inventory validator with the stage writer.  It adds final
    generation bindings that the writer cannot establish for a prospective
    selected release: current package location, exact ``uv`` argv, admitted
    entrypoint bytes, canonical environment and the wrapper's rendered bytes.
    """

    root = _absolute_path(
        project_root, code="runtime-final-command-invalid", label="target Project root", require_directory=True
    )
    if isinstance(state_generation, bool) or not isinstance(state_generation, int) or state_generation < 1:
        _refuse("runtime-final-command-invalid", "final command generation is invalid")
    if not isinstance(installation_lock_generation, str) or _FINAL_LOCK_GENERATION.fullmatch(installation_lock_generation) is None:
        _refuse("runtime-final-command-invalid", "final command lock generation is invalid")
    expected_command_sha256 = _require_fragment_digest(
        command_sha256, code="runtime-final-command-invalid", label="expected command digest"
    )
    expected_manifest_sha256 = _require_fragment_digest(
        stage_manifest_sha256, code="runtime-final-command-invalid", label="expected stage manifest digest"
    )
    expected_context_sha256 = _require_fragment_digest(
        target_context_sha256, code="runtime-final-command-invalid", label="target context digest"
    )
    selected_package = _reopen_selected_package(root, package)
    carriers = _final_generation_carriers(root, state_generation, release_proof_sha256=release_proof_sha256)
    command, environment, manifest = _validate_fragment_documents(
        carriers[_COMMAND_NAME], carriers[_ENVIRONMENT_NAME], carriers[_WRAPPER_NAME], carriers[_MANIFEST_NAME],
        code="runtime-final-command-invalid",
    )
    if (
        command["package_manifest_sha256"] != selected_package.manifest_digest
        or command["target_project_context_sha256"] != expected_context_sha256
        or command["state_generation"] != state_generation
        or command["command_sha256"] != expected_command_sha256
    ):
        _refuse("runtime-final-command-mismatch", "final command differs from selected package, context, or D604 proof")
    if carriers[_COMMAND_NAME] != _render_command(command):
        _refuse("runtime-final-command-invalid", "final command bytes are not canonical")
    entrypoint = _validate_entrypoint(root, selected_package, command["entrypoint"])
    if _NONCE.fullmatch(command["invocation_nonce"]) is None:
        _refuse("runtime-final-command-invalid", "final command invocation nonce is invalid")
    argv = tuple(command["argv"])
    prefix = (*_UV_PREFIX, "--project", selected_package.root.as_posix(), "python", entrypoint)
    if argv[:len(prefix)] != prefix:
        _refuse("runtime-final-command-mismatch", "final command argv is not the admitted locked uv invocation")
    fixed_arguments = _validate_fixed_arguments(tuple(argv[len(prefix):]))
    if argv != (*prefix, *fixed_arguments):  # Defensive: preserves the closed tuple interpretation.
        _refuse("runtime-final-command-invalid", "final command argv is invalid")
    variables = {name: environment["variables"][name] for name in _VARIABLE_NAMES}
    if carriers[_ENVIRONMENT_NAME] != _render_environment(variables, environment["environment_sha256"]):
        _refuse("runtime-final-command-invalid", "final environment bytes are not canonical")
    if variables["UV_CACHE_DIR"] != (root / _UV_CACHE_DIRECTORY).as_posix() or variables["UV_PROJECT_ENVIRONMENT"] != (root / _UV_PROJECT_ENVIRONMENT).as_posix():
        _refuse("runtime-final-command-mismatch", "final environment differs from the target runtime boundary")
    if carriers[_WRAPPER_NAME] != _render_wrapper(selected_package.root, variables, argv):
        _refuse("runtime-final-command-mismatch", "final wrapper differs from canonical command and environment")
    files = (
        (_COMMAND_NAME, 0o600, _sha256(carriers[_COMMAND_NAME])),
        (_ENVIRONMENT_NAME, 0o600, _sha256(carriers[_ENVIRONMENT_NAME])),
        (_WRAPPER_NAME, 0o700, _sha256(carriers[_WRAPPER_NAME])),
    )
    if (
        manifest["package_manifest_sha256"] != selected_package.manifest_digest
        or manifest["target_project_context_sha256"] != expected_context_sha256
        or manifest["state_generation"] != state_generation
        or manifest["lock_generation"] != installation_lock_generation
        or carriers[_MANIFEST_NAME] != _render_manifest(
            package_manifest_sha256=selected_package.manifest_digest,
            target_project_context_sha256=expected_context_sha256,
            state_generation=state_generation,
            lock_generation=installation_lock_generation,
            files=files,
        )
        or _sha256(carriers[_MANIFEST_NAME]) != expected_manifest_sha256
    ):
        _refuse("runtime-final-command-mismatch", "final stage manifest differs from final command carriers or D604 proof")


def _stage_opened_runtime_command(
    request: RuntimeCommandStageRequest | CandidateRuntimeCommandStageRequest,
    *,
    lock: InstallationPublicationLock,
    target_root: Path,
    package: VerifiedFrameworkPackage,
    context: TargetProjectContext,
    runtime_package_root: Path,
) -> RuntimeCommandStage:
    """Stage command bytes after a package was physically reopened.

    Candidate validation reads its sealed temporary package, while its inert
    command bytes name the exact future installed release location.  This
    helper never creates or opens that prospective destination.
    """

    if isinstance(request.state_generation, bool) or not isinstance(request.state_generation, int) or request.state_generation < 1:
        _refuse("runtime-stage-generation-invalid", "native state generation must be a positive integer")
    if not isinstance(request.invocation_nonce, str) or _NONCE.fullmatch(request.invocation_nonce) is None:
        _refuse("runtime-stage-nonce-invalid", "invocation nonce is invalid")
    entrypoint = _validate_entrypoint(target_root, package, request.entrypoint)
    fixed_arguments = _validate_fixed_arguments(request.fixed_arguments)
    variables, environment_digest, environment_payload = _environment(target_root, request)
    argv = (*_UV_PREFIX, "--project", runtime_package_root.as_posix(), "python", entrypoint, *fixed_arguments)
    wrapper_payload = _render_wrapper(runtime_package_root, variables, argv)
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

    lock.revalidate()
    parent_fd = _open_stage_parent(target_root)
    stage_root = target_root / _STAGING / lock.lock_generation
    files = (
        (_COMMAND_NAME, 0o600, _sha256(command_payload)),
        (_ENVIRONMENT_NAME, 0o600, _sha256(environment_payload)),
        (_WRAPPER_NAME, 0o700, wrapper_digest),
    )
    manifest_payload = _render_manifest(
        package_manifest_sha256=package.manifest_digest,
        target_project_context_sha256=context.sha256,
        state_generation=request.state_generation,
        lock_generation=lock.lock_generation,
        files=files,
    )
    try:
        stage_fd = _open_stage(parent_fd, lock.lock_generation)
        try:
            _write_new(stage_fd, _COMMAND_NAME, command_payload, mode=0o600)
            _write_new(stage_fd, _ENVIRONMENT_NAME, environment_payload, mode=0o600)
            _write_new(stage_fd, _WRAPPER_NAME, wrapper_payload, mode=0o700)
            _write_new(stage_fd, _MANIFEST_NAME, manifest_payload, mode=0o600)
            os.fsync(stage_fd)
            lock.revalidate()
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
                lock.lock_generation,
                expected_command=command_payload,
                expected_environment=environment_payload,
                expected_wrapper=wrapper_payload,
                expected_manifest=manifest_payload,
            )
            lock.revalidate()
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
        lock_generation=lock.lock_generation,
        command_sha256=command_digest,
        environment_sha256=environment_digest,
        wrapper_sha256=wrapper_digest,
    )


def stage_runtime_command(request: RuntimeCommandStageRequest, *, lock: InstallationPublicationLock) -> RuntimeCommandStage:
    """Stage one selected-package command fragment without effects."""

    if not isinstance(request, RuntimeCommandStageRequest):
        _refuse("runtime-stage-request-invalid", "staging requires a typed selected-package request")
    concrete_lock, target_root = _target_root(lock)
    package = _reopen_selected_package(target_root, request.package)
    context = _reopen_context(target_root, request.target_context, package, concrete_lock)
    return _stage_opened_runtime_command(
        request,
        lock=concrete_lock,
        target_root=target_root,
        package=package,
        context=context,
        runtime_package_root=package.root,
    )


def stage_candidate_runtime_command(
    request: CandidateRuntimeCommandStageRequest, *, lock: InstallationPublicationLock
) -> RuntimeCommandStage:
    """Stage one sealed-candidate command fragment before selector publication.

    This writes only the immutable D601 stage under the lock.  It does not
    publish either prospective selector, configure the target, or invoke the
    rendered wrapper.
    """

    if not isinstance(request, CandidateRuntimeCommandStageRequest):
        _refuse("candidate-stage-request-invalid", "candidate staging requires a typed request")
    concrete_lock, target_root = _target_root(lock)
    package = _reopen_candidate_package(
        target_root,
        request.package,
        request.prospective_package_selector,
        request.full_gate_packet,
    )
    context = _reopen_candidate_context(target_root, request.target_context, package, concrete_lock)
    return _stage_opened_runtime_command(
        request,
        lock=concrete_lock,
        target_root=target_root,
        package=package,
        context=context,
        runtime_package_root=target_root / _PACKAGE_RELEASES / package.manifest_digest,
    )


__all__ = [
    "CandidateRuntimeCommandStageRequest",
    "PortableRuntimeMaterializationError",
    "RuntimeCommandStage",
    "RuntimeCommandStageRequest",
    "reopen_final_runtime_command_fragment",
    "stage_candidate_runtime_command",
    "stage_runtime_command",
]
