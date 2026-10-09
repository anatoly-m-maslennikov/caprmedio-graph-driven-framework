"""Shared, non-executable CAPRMEDIO Tool runtime-publication library.

The canonical source is ``102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS`` in the target
repository.  Installed releases are content-addressed and live below
``.caprmedio_runtime/tools``. Persistent operational state belongs below
``.caprmedio_runtime``; disposable staging and cache state belongs below
``.caprmedio_tmp``.
"""

from __future__ import annotations

import hashlib
import json
import os
import re
import shutil
import stat
import subprocess
import tempfile
import tomllib
import uuid
from collections.abc import Mapping, Sequence
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from framework_package import (
    CurrentPackageSelector,
    FrameworkPackageError,
    VerifiedFrameworkPackage,
    verify_current_package_selector,
    verify_framework_package,
)
from installation_context import (
    InstallationContextError,
    TargetProjectContext,
    TargetProjectRequest,
    bind_target_project_context,
)
from project_mcp_configuration import DEFAULT_MEMBER, parse_project_mcp_settings
from project_runtime import RUNTIME_DIRECTORY, TEMPORARY_DIRECTORY, atomic_tempfile
from runtime_configuration import (
    RuntimeConfigurationError,
    RuntimeConfigurationResult,
    read_admitted_runtime_default,
    read_runtime_configuration,
)


SCHEMA_VERSION = 1
PACKAGE = "caprmedio-framework-engine-tools"
SOURCE_DIRECTORY = Path("102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS")
TOOLS_RUNTIME_DIRECTORY = RUNTIME_DIRECTORY / "tools"
TEMP_DIRECTORY = TEMPORARY_DIRECTORY
CURRENT_MANIFEST = "current.toml"
RELEASE_MANIFEST = "manifest.toml"
TOOLS_DIRECTORY = "TOOLS"
INSTALL_ENTRYPOINT = "TOOLS/INSTALL_TOOLS/install_tools.py"
TRIGGER_ENTRYPOINT = "TOOLS/COMMIT_TRIGGER/commit_trigger.py"
SERVICE_ENTRYPOINT = "TOOLS/START_BACKGROUND_SERVICES/start_background_services.py"
RELEASE_REFERENCE_CONTEXT = "RELEASE_VERSION/release_suite_reference_context.py"
PRIVATE_READER_DIRECTORY = "204_MCP"
PRIVATE_READER_FILES = (
    "release_source_admission.py",
    "selected_routes.py",
)
REQUIRED_FILES = (
    "framework_installation.py",
    "project_runtime.py",
    "atom_operations.py",
    "background_services.toml",
    "INSTALL_TOOLS/install_tools.py",
    "START_BACKGROUND_SERVICES/start_background_services.py",
    "COMMIT_TRIGGER/commit_trigger.py",
    "COMMIT_CONTEXT/commit_context.py",
    "COMMIT_CONTEXT/commit_context_logic.py",
    "APPEND_CHANGE_RECORDS/append_change_records.py",
    "COMMIT_CHANGE_SET/commit_change_set.py",
    "ATOM_SEARCH/atom_search.py",
    "ATOM_READ/atom_read.py",
    "ATOM_CREATE/atom_create.py",
    "ATOM_UPDATE/atom_update.py",
    "ATOM_MOVE/atom_move.py",
    "ATOM_ARCHIVE/atom_archive.py",
    "ATOM_PROMOTE/atom_promote.py",
    "ATOM_UPGRADE/atom_upgrade.py",
    "MIGRATE_ATOM_IDENTITY/migrate_atom_identity.py",
    "REBIND_ATOM_RELATIONS/rebind_atom_relations.py",
    "CLOSE_ATOM/close_atom.py",
    "REPLACE_ATOM/replace_atom.py",
    "caprmedio_relation_types.toml",
    "lifecycle_intents.py",
    "work_journal.py",
)
SHA256 = re.compile(r"[0-9a-f]{64}\Z")
EXCLUDED_DIRECTORY_NAMES = {"__pycache__", "tests"}
EXCLUDED_FILE_NAMES = {".DS_Store", ".gitkeep"}


class InstallationError(RuntimeError):
    """One stable installation or verification failure."""

    def __init__(self, code: str, message: str) -> None:
        self.code = code
        self.message = message
        super().__init__(message)


def canonical_json(value: object) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False)


def digest(value: object) -> str:
    payload = value if isinstance(value, bytes) else canonical_json(value).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def resolve_repository(path: Path | str) -> Path:
    candidate = Path(path).expanduser().resolve()
    for root in (candidate, *candidate.parents):
        if (root / ".git").exists():
            return root
    raise InstallationError("repository-not-found", f"cannot resolve Git repository from {candidate}")


def _quoted(value: str) -> str:
    return json.dumps(value, ensure_ascii=False)


def _atomic_write(path: Path, content: str, *, mode: int | None = None) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    descriptor, temporary_name = atomic_tempfile(path, "install_tools")
    temporary = Path(temporary_name)
    try:
        with os.fdopen(descriptor, "w", encoding="utf-8", newline="\n") as handle:
            handle.write(content)
            handle.flush()
            os.fsync(handle.fileno())
        if mode is not None:
            temporary.chmod(mode)
        os.replace(temporary, path)
    except BaseException:
        try:
            temporary.unlink()
        except FileNotFoundError:
            pass
        raise


def _source_files(source_root: Path) -> list[Path]:
    if not source_root.is_dir() or source_root.is_symlink():
        raise InstallationError("canonical-source-missing", f"canonical Tool source is missing: {source_root}")
    paths: list[Path] = []
    for path in source_root.rglob("*"):
        relative = path.relative_to(source_root)
        if any(part in EXCLUDED_DIRECTORY_NAMES for part in relative.parts):
            continue
        if not path.is_file() or path.is_symlink():
            continue
        if path.name in EXCLUDED_FILE_NAMES or path.suffix in {".pyc", ".pyo"}:
            continue
        paths.append(path)
    return sorted(paths, key=lambda item: item.relative_to(source_root).as_posix())


def source_inventory(repository: Path | str, *, source_root: Path | None = None) -> tuple[list[dict[str, Any]], str]:
    root = resolve_repository(repository)
    canonical = (source_root or (root / SOURCE_DIRECTORY)).resolve()
    files = _source_files(canonical)
    available = {path.relative_to(canonical).as_posix() for path in files}
    missing = [relative for relative in REQUIRED_FILES if relative not in available]
    if missing:
        raise InstallationError("canonical-source-incomplete", "canonical Tool source is missing: " + ", ".join(missing))
    rows: list[dict[str, Any]] = []
    for path in files:
        relative = f"{TOOLS_DIRECTORY}/{path.relative_to(canonical).as_posix()}"
        rows.append(
            {
                "path": relative,
                "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
                "mode": path.stat().st_mode & 0o777,
            }
        )
    if RELEASE_REFERENCE_CONTEXT in available:
        private_root = canonical.parent / PRIVATE_READER_DIRECTORY
        if not private_root.is_dir() or private_root.is_symlink():
            raise InstallationError("canonical-source-incomplete", "canonical private reader source is missing")
        for name in PRIVATE_READER_FILES:
            path = private_root / name
            if not path.is_file() or path.is_symlink():
                raise InstallationError("canonical-source-incomplete", f"canonical private reader source is missing: {name}")
            rows.append(
                {
                    "path": f"{PRIVATE_READER_DIRECTORY}/{name}",
                    "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
                    "mode": path.stat().st_mode & 0o777,
                }
            )
    rows.sort(key=lambda row: str(row["path"]))
    release = digest({"schema_version": SCHEMA_VERSION, "package": PACKAGE, "files": rows})
    return rows, release


def _inventory_source(canonical: Path, relative: Path) -> Path:
    """Map one verified inventory row back to its canonical source carrier."""
    if relative.parts[:1] == (TOOLS_DIRECTORY,):
        return canonical / relative.relative_to(TOOLS_DIRECTORY)
    if relative.parts[:1] == (PRIVATE_READER_DIRECTORY,) and relative.name in PRIVATE_READER_FILES and len(relative.parts) == 2:
        return canonical.parent / relative
    raise InstallationError("install-manifest-invalid", f"release inventory path is unsupported: {relative.as_posix()}")


def _render_release_manifest(release: str, rows: Sequence[Mapping[str, Any]]) -> str:
    lines = [f"schema_version = {SCHEMA_VERSION}", f"package = {_quoted(PACKAGE)}", f"release = {_quoted(release)}", ""]
    for row in rows:
        lines.extend(
            [
                "[[files]]",
                f"path = {_quoted(str(row['path']))}",
                f"sha256 = {_quoted(str(row['sha256']))}",
                f"mode = {int(row['mode'])}",
                "",
            ]
        )
    return "\n".join(lines)


def _render_current_manifest(release: str) -> str:
    return "\n".join(
        [
            f"schema_version = {SCHEMA_VERSION}",
            f"package = {_quoted(PACKAGE)}",
            f"release = {_quoted(release)}",
            f"tools_root = {_quoted(TOOLS_DIRECTORY)}",
            f"entrypoint = {_quoted(INSTALL_ENTRYPOINT)}",
            "",
        ]
    )


def _safe_manifest_path(value: object, field: str) -> str:
    if not isinstance(value, str) or not value:
        raise InstallationError("install-manifest-invalid", f"{field} must be a non-empty relative path")
    path = Path(value)
    if path.is_absolute() or ".." in path.parts or path.as_posix() in {"", "."}:
        raise InstallationError("install-manifest-invalid", f"{field} is unsafe")
    return path.as_posix()


def _read_toml(path: Path, code: str) -> dict[str, Any]:
    try:
        document = tomllib.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as error:
        raise InstallationError(code, f"missing manifest: {path}") from error
    except tomllib.TOMLDecodeError as error:
        raise InstallationError(code, f"invalid TOML: {path}") from error
    if not isinstance(document, dict):
        raise InstallationError(code, f"manifest root must be a table: {path}")
    return document


def installation_status(repository: Path | str) -> dict[str, Any]:
    root = resolve_repository(repository)
    tools_runtime_root = root / TOOLS_RUNTIME_DIRECTORY
    current_path = tools_runtime_root / CURRENT_MANIFEST
    if not current_path.is_file():
        return {"installed": False, "tools_runtime_root": TOOLS_RUNTIME_DIRECTORY.as_posix()}
    current = _read_toml(current_path, "current-manifest-invalid")
    release = current.get("release")
    if current.get("schema_version") != SCHEMA_VERSION or current.get("package") != PACKAGE:
        raise InstallationError("current-manifest-invalid", "installed package identity is invalid")
    if not isinstance(release, str) or not SHA256.fullmatch(release):
        raise InstallationError("current-manifest-invalid", "installed release identity is invalid")
    tools_root_name = _safe_manifest_path(current.get("tools_root"), "tools_root")
    entrypoint_name = _safe_manifest_path(current.get("entrypoint"), "entrypoint")
    release_root = tools_runtime_root / "releases" / release
    manifest = _read_toml(release_root / RELEASE_MANIFEST, "release-manifest-invalid")
    if (
        manifest.get("schema_version") != SCHEMA_VERSION
        or manifest.get("package") != PACKAGE
        or manifest.get("release") != release
    ):
        raise InstallationError("release-manifest-invalid", "installed release manifest identity is invalid")
    raw_rows = manifest.get("files")
    if not isinstance(raw_rows, list) or not raw_rows:
        raise InstallationError("release-manifest-invalid", "installed release has no file inventory")
    rows: list[dict[str, Any]] = []
    for raw in raw_rows:
        if not isinstance(raw, Mapping):
            raise InstallationError("release-manifest-invalid", "installed file row must be a table")
        relative = _safe_manifest_path(raw.get("path"), "files.path")
        expected = raw.get("sha256")
        mode = raw.get("mode")
        if not isinstance(expected, str) or not SHA256.fullmatch(expected) or not isinstance(mode, int):
            raise InstallationError("release-manifest-invalid", f"invalid file metadata: {relative}")
        carrier = release_root / relative
        if not carrier.is_file() or carrier.is_symlink():
            raise InstallationError("installed-file-missing", f"installed file is missing: {relative}")
        actual = hashlib.sha256(carrier.read_bytes()).hexdigest()
        if actual != expected:
            raise InstallationError("installed-file-drift", f"installed file digest differs: {relative}")
        actual_mode = carrier.stat().st_mode & 0o777
        if actual_mode != mode:
            raise InstallationError("installed-file-mode-drift", f"installed file mode differs: {relative}")
        rows.append({"path": relative, "sha256": actual, "mode": mode})
    actual_release = digest({"schema_version": SCHEMA_VERSION, "package": PACKAGE, "files": rows})
    if actual_release != release:
        raise InstallationError("release-digest-mismatch", "installed release digest differs from its identity")
    tools_root = release_root / tools_root_name
    entrypoint = release_root / entrypoint_name
    for required in (tools_root, entrypoint, tools_root / "COMMIT_TRIGGER/commit_trigger.py", tools_root / "START_BACKGROUND_SERVICES/start_background_services.py"):
        if not required.exists():
            raise InstallationError("installed-entrypoint-missing", f"installed entrypoint is missing: {required}")
    return {
        "installed": True,
        "verified": True,
        "release": release,
        "tools_runtime_root": TOOLS_RUNTIME_DIRECTORY.as_posix(),
        "release_root": release_root.relative_to(root).as_posix(),
        "package_root": tools_root.relative_to(root).as_posix(),
        "entrypoint": entrypoint.relative_to(root).as_posix(),
        "file_count": len(rows),
    }


def install_release(
    repository: Path | str,
    *,
    apply: bool,
    source_root: Path | None = None,
) -> dict[str, Any]:
    root = resolve_repository(repository)
    canonical = (source_root or (root / SOURCE_DIRECTORY)).resolve()
    rows, release = source_inventory(root, source_root=canonical)
    tools_runtime_root = root / TOOLS_RUNTIME_DIRECTORY
    release_root = tools_runtime_root / "releases" / release
    result = {
        "installed": apply,
        "verified": False,
        "release": release,
        "tools_runtime_root": TOOLS_RUNTIME_DIRECTORY.as_posix(),
        "release_root": release_root.relative_to(root).as_posix(),
        "package_root": (release_root / TOOLS_DIRECTORY).relative_to(root).as_posix(),
        "entrypoint": (release_root / INSTALL_ENTRYPOINT).relative_to(root).as_posix(),
        "file_count": len(rows),
        "planned_effect": "install-or-select-content-addressed-tool-release",
    }
    if not apply:
        return result
    tools_runtime_root.mkdir(parents=True, exist_ok=True)
    staging_root = root / TEMP_DIRECTORY / "install_tools"
    staging_root.mkdir(parents=True, exist_ok=True)
    staging = Path(tempfile.mkdtemp(prefix=f".staging-{uuid.uuid4().hex}-", dir=staging_root))
    try:
        for row in rows:
            relative = Path(str(row["path"]))
            source = _inventory_source(canonical, relative)
            if not source.is_file() or source.is_symlink():
                raise InstallationError("canonical-source-incomplete", f"canonical release source is unavailable: {relative.as_posix()}")
            if (hashlib.sha256(source.read_bytes()).hexdigest() != row["sha256"]
                    or source.stat().st_mode & 0o777 != row["mode"]):
                raise InstallationError("canonical-source-drift", f"canonical release source changed: {relative.as_posix()}")
            target = staging / relative
            if not target.parent.is_dir():
                target.parent.mkdir(parents=True, exist_ok=True)
            try:
                with source.open("rb") as source_handle, target.open("wb") as target_handle:
                    shutil.copyfileobj(source_handle, target_handle)
            except PermissionError:
                copied = subprocess.run(["cp", str(source), str(target)], capture_output=True, check=False)
                if copied.returncode != 0:
                    raise InstallationError(
                        "release-copy-failed",
                        copied.stderr.decode("utf-8", "replace").strip() or f"cannot copy release file: {relative}",
                    )
            target.chmod(int(row["mode"]))
            if (hashlib.sha256(target.read_bytes()).hexdigest() != row["sha256"]
                    or target.stat().st_mode & 0o777 != row["mode"]):
                raise InstallationError("release-copy-failed", f"copied release file differs: {relative.as_posix()}")
        _atomic_write(staging / RELEASE_MANIFEST, _render_release_manifest(release, rows), mode=0o644)
        if release_root.exists():
            expected_manifest = _render_release_manifest(release, rows)
            manifest_path = release_root / RELEASE_MANIFEST
            if not manifest_path.is_file() or manifest_path.read_text(encoding="utf-8") != expected_manifest:
                raise InstallationError("installed-release-collision", f"existing release manifest differs: {release}")
            for row in rows:
                carrier = release_root / str(row["path"])
                if (
                    not carrier.is_file()
                    or carrier.is_symlink()
                    or hashlib.sha256(carrier.read_bytes()).hexdigest() != row["sha256"]
                    or carrier.stat().st_mode & 0o777 != row["mode"]
                ):
                    raise InstallationError("installed-release-collision", f"existing release file differs: {row['path']}")
        else:
            release_root.parent.mkdir(parents=True, exist_ok=True)
            try:
                os.replace(staging, release_root)
            except PermissionError:
                release_root.mkdir()
                promoted = subprocess.run(
                    ["cp", "-R", f"{staging}/.", str(release_root)],
                    capture_output=True,
                    check=False,
                )
                if promoted.returncode != 0:
                    raise InstallationError(
                        "release-promotion-failed",
                        promoted.stderr.decode("utf-8", "replace").strip()
                        or f"cannot promote release: {release}",
                    )
        _atomic_write(tools_runtime_root / CURRENT_MANIFEST, _render_current_manifest(release), mode=0o644)
    finally:
        if staging.exists():
            try:
                shutil.rmtree(staging)
            except PermissionError:
                # Some sandboxed hosts permit file cleanup but prohibit
                # directory removal. Reclaim the disposable bytes and leave
                # only empty cleanup remnants in Project Temporary State.
                for carrier in staging.rglob("*"):
                    if carrier.is_file() or carrier.is_symlink():
                        try:
                            carrier.unlink()
                        except (FileNotFoundError, PermissionError):
                            pass
    return installation_status(root)


_PACKAGE_CURRENT_RELATIVE = Path(".caprmedio_install/current.toml")
_PROTECTED_RECEIPT_COMPONENTS = frozenset({"secrets", "credentials", "private_settings"})


@dataclass(frozen=True)
class PortableInstallationRequest:
    """Explicit portable-package inputs, deliberately without activation intent.

    ``retained_gate_receipt_path`` is an opaque retained receipt carrier.  Its
    exact bytes must match the digest already bound by the real current-package
    selector; this facade never accepts a caller boolean or renders a gate.
    """

    target: TargetProjectRequest
    retained_gate_receipt_path: Path | str
    runtime_default_member: str = DEFAULT_MEMBER


@dataclass(frozen=True)
class PortableInstallationPreparation:
    """Read-only result for a future, gate-aware publication adapter."""

    target_context: TargetProjectContext
    package: VerifiedFrameworkPackage
    selector: CurrentPackageSelector
    gate_receipt_sha256: str
    runtime_default_sha256: str
    configuration: RuntimeConfigurationResult
    status: str
    blocker: str


@dataclass(frozen=True)
class _PortableTargetRoot:
    """Selected Project root retained as an inode-checked read anchor."""

    path: Path
    device: int
    inode: int


def _portable_root(request: PortableInstallationRequest) -> _PortableTargetRoot:
    if not isinstance(request.target, TargetProjectRequest):
        raise InstallationError("portable-target-invalid", "portable installation requires a typed target request")
    try:
        supplied = Path(request.target.target_root).expanduser()
        if not supplied.is_absolute() or ".." in supplied.parts:
            raise InstallationError("portable-target-invalid", "target Project root must be an explicit absolute path")
        root = Path(os.path.abspath(supplied))
        if any(candidate.is_symlink() for candidate in (root, *root.parents)):
            raise InstallationError("portable-target-invalid", "target Project root has a symlink ancestor")
        observed = root.lstat()
    except InstallationError:
        raise
    except (OSError, TypeError, ValueError) as error:
        raise InstallationError("portable-target-invalid", "target Project root is unavailable") from error
    if stat.S_ISLNK(observed.st_mode) or not stat.S_ISDIR(observed.st_mode):
        raise InstallationError("portable-target-invalid", "target Project root is unsafe")
    return _PortableTargetRoot(path=root, device=observed.st_dev, inode=observed.st_ino)


def _open_target_root(root: _PortableTargetRoot) -> int:
    """Open the validated Project path one no-follow component at a time."""

    flags = os.O_RDONLY | os.O_CLOEXEC | os.O_NOFOLLOW | os.O_DIRECTORY
    try:
        descriptor = os.open(root.path.anchor, flags)
    except OSError as error:
        raise InstallationError("portable-target-invalid", "target Project root cannot be safely opened") from error
    try:
        for component in root.path.parts[1:]:
            try:
                next_descriptor = os.open(component, flags, dir_fd=descriptor)
            except OSError as error:
                raise InstallationError("portable-target-invalid", "target Project root changed while reopening") from error
            os.close(descriptor)
            descriptor = next_descriptor
        observed = os.fstat(descriptor)
        if (observed.st_dev, observed.st_ino) != (root.device, root.inode) or not stat.S_ISDIR(observed.st_mode):
            raise InstallationError("portable-target-invalid", "target Project root changed while reopening")
        return descriptor
    except BaseException:
        os.close(descriptor)
        raise


def _read_target_regular_carrier(root: _PortableTargetRoot, relative: Path, *, label: str) -> bytes:
    """Read one Project-contained regular carrier with no pathname following."""

    if relative.is_absolute() or not relative.parts or any(part in {"", ".", ".."} for part in relative.parts):
        raise InstallationError("portable-carrier-invalid", f"{label} must be a Project-contained carrier")
    directory_flags = os.O_RDONLY | os.O_CLOEXEC | os.O_NOFOLLOW | os.O_DIRECTORY
    file_flags = os.O_RDONLY | os.O_CLOEXEC | os.O_NOFOLLOW
    directory_fd = _open_target_root(root)
    try:
        for component in relative.parts[:-1]:
            try:
                next_fd = os.open(component, directory_flags, dir_fd=directory_fd)
            except OSError as error:
                raise InstallationError("portable-carrier-invalid", f"{label} has an unsafe Project ancestor") from error
            os.close(directory_fd)
            directory_fd = next_fd
        try:
            descriptor = os.open(relative.name, file_flags, dir_fd=directory_fd)
        except FileNotFoundError as error:
            raise InstallationError("portable-carrier-missing", f"{label} is missing") from error
        except OSError as error:
            raise InstallationError("portable-carrier-invalid", f"{label} cannot be safely opened") from error
        try:
            observed = os.fstat(descriptor)
            if not stat.S_ISREG(observed.st_mode) or observed.st_nlink != 1:
                raise InstallationError("portable-carrier-invalid", f"{label} must be an unaliased regular file")
            chunks: list[bytes] = []
            while chunk := os.read(descriptor, 65536):
                chunks.append(chunk)
            return b"".join(chunks)
        finally:
            os.close(descriptor)
    finally:
        os.close(directory_fd)


def _retained_gate_receipt(root: _PortableTargetRoot, value: Path | str, selector: CurrentPackageSelector) -> str:
    try:
        receipt = Path(value)
        if not receipt.is_absolute() or not receipt.is_relative_to(root.path):
            raise InstallationError("portable-gate-invalid", "retained gate receipt must be an explicit Project-contained carrier")
        relative = receipt.relative_to(root.path)
        if any(
            component.lower() in _PROTECTED_RECEIPT_COMPONENTS
            or component.lower().startswith(".env")
            or component.lower().endswith(".env")
            for component in relative.parts
        ):
            raise InstallationError("portable-gate-invalid", "retained gate receipt path is protected")
    except InstallationError:
        raise
    except (TypeError, ValueError) as error:
        raise InstallationError("portable-gate-invalid", "retained gate receipt path is invalid") from error
    payload = _read_target_regular_carrier(root, relative, label="retained full gate receipt")
    actual = hashlib.sha256(payload).hexdigest()
    if actual != selector.full_gate_receipt_sha256:
        raise InstallationError("portable-gate-mismatch", "retained full gate receipt differs from the selected package gate")
    return actual


def _admitted_runtime_default(package: VerifiedFrameworkPackage, member: str) -> str:
    try:
        runtime_default = read_admitted_runtime_default(
            package,
            default_member=member,
            validator=parse_project_mcp_settings,
        )
    except RuntimeConfigurationError as error:
        message = (
            "runtime default is not an admitted package default"
            if error.code == "runtime-config-default-not-admitted"
            else "admitted runtime default cannot be reopened as compatible Project-MCP configuration"
        )
        raise InstallationError(
            "portable-default-invalid",
            message,
        ) from error
    return runtime_default.sha256


def prepare_portable_installation(request: PortableInstallationRequest) -> PortableInstallationPreparation:
    """Reopen the complete portable-install inputs without publishing anything.

    The legacy Tool-only installer above remains unchanged.  This new boundary
    intentionally stops before configuration creation, selector replacement,
    wrapper generation, Skill publication, or runtime activation because the
    package selector's receipt digest is not itself a Full Gate verifier.
    """
    if not isinstance(request, PortableInstallationRequest):
        raise InstallationError("portable-request-invalid", "portable installation requires a typed request")
    root = _portable_root(request)
    try:
        context = bind_target_project_context(request.target)
    except InstallationContextError as error:
        raise InstallationError("portable-context-invalid", "target context could not be reopened") from error
    try:
        package = verify_framework_package(request.target.package_root)
    except FrameworkPackageError as error:
        raise InstallationError("portable-package-invalid", "physical Framework package could not be reopened") from error
    if (
        package.manifest_digest != context.package_evidence.package_manifest_sha256
        or package.source_catalog_sha256 != context.package_evidence.catalog_sha256
    ):
        raise InstallationError("portable-package-mismatch", "target context no longer binds the reopened Framework package")
    selector_payload = _read_target_regular_carrier(root, _PACKAGE_CURRENT_RELATIVE, label="current package selector")
    try:
        selector = verify_current_package_selector(selector_payload, package)
    except FrameworkPackageError as error:
        raise InstallationError("portable-selector-invalid", "current package selector is not admitted for the reopened package") from error
    receipt_sha256 = _retained_gate_receipt(root, request.retained_gate_receipt_path, selector)
    default_sha256 = _admitted_runtime_default(package, request.runtime_default_member)
    try:
        configuration = read_runtime_configuration(root.path, validator=parse_project_mcp_settings)
    except RuntimeConfigurationError as error:
        raise InstallationError("portable-configuration-invalid", "target runtime configuration cannot be reopened") from error
    blocker = (
        "runtime-configuration-migration-needed"
        if configuration.state == "blocked"
        else "full-gate-verifier-unavailable"
    )
    return PortableInstallationPreparation(
        target_context=context,
        package=package,
        selector=selector,
        gate_receipt_sha256=receipt_sha256,
        runtime_default_sha256=default_sha256,
        configuration=configuration,
        status="blocked",
        blocker=blocker,
    )


def initialize_portable_runtime_configuration(
    request: PortableInstallationRequest,
    *,
    owner_run_id: str,
    command_sha256: str,
) -> PortableInstallationPreparation:
    """Refuse mutable configuration publication until a Full Gate adapter exists.

    Arguments for a future per-Project publication lock are retained in this
    narrow API, but deliberately not used to create a lock or write config: a
    selector digest cannot stand in for the Full Gate receipt verifier.
    """
    if not isinstance(owner_run_id, str) or not owner_run_id:
        raise InstallationError("portable-owner-invalid", "configuration initialization needs an owner run ID")
    if not isinstance(command_sha256, str) or SHA256.fullmatch(command_sha256) is None:
        raise InstallationError("portable-command-invalid", "configuration initialization needs a command digest")
    preparation = prepare_portable_installation(request)
    if preparation.blocker == "runtime-configuration-migration-needed":
        raise InstallationError("portable-configuration-blocked", "target runtime configuration requires migration")
    raise InstallationError(
        "portable-full-gate-verifier-unavailable",
        "cannot initialize target configuration until a retained full gate verifier is available",
    )


__all__ = [
    "InstallationError",
    "PACKAGE",
    "RUNTIME_DIRECTORY",
    "TEMP_DIRECTORY",
    "TOOLS_RUNTIME_DIRECTORY",
    "SCHEMA_VERSION",
    "SERVICE_ENTRYPOINT",
    "SOURCE_DIRECTORY",
    "TRIGGER_ENTRYPOINT",
    "canonical_json",
    "digest",
    "PortableInstallationPreparation",
    "PortableInstallationRequest",
    "initialize_portable_runtime_configuration",
    "install_release",
    "installation_status",
    "prepare_portable_installation",
    "resolve_repository",
    "source_inventory",
]
