"""Read-only admission of the installed, bounded Project MCP package.

This module deliberately does not install, launch, build, or publish anything.
It turns the typed result of :mod:`framework_package` verification into the
small set of package-relative MCP routes that a later runtime activation may
use.  In particular, a checkout path is never a substitute for the selected
``.caprmedio_install`` release.

The producing boundary supplies one typed
``framework_package.VerifiedFrameworkPackage``.  This module consumes its
content-addressed root, manifest digest, source-catalog digest, and exact
ordered inventory rather than re-deriving a package from a checkout.
"""

from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass
import hashlib
import os
from pathlib import Path, PurePosixPath
import re
import stat
import tomllib
from typing import Any

import yaml

from framework_package import FrameworkPackageError, VerifiedFrameworkPackage, verify_current_package_selector
from installation_context import CONTEXT_DIGEST_FIELD, canonical_target_project_context_toml


SCHEMA_VERSION = 1
CONTEXT_SCHEMA_VERSION = 2
PACKAGE_NAME = "caprmedio-framework"
SHA256 = re.compile(r"[0-9a-f]{64}\Z")
IMAGE_DIGEST = SHA256
LOCK_GENERATION = re.compile(r"[0-9a-f]{32}\Z")

INSTALL_CURRENT_RELATIVE = PurePosixPath(".caprmedio_install/current.toml")
INSTALL_RELEASES_RELATIVE = PurePosixPath(".caprmedio_install/releases")
RUNTIME_CURRENT_RELATIVE = PurePosixPath(".caprmedio_runtime/installation/current.toml")
RUNTIME_CONTEXTS_RELATIVE = PurePosixPath(".caprmedio_runtime/installation/contexts")

MCP_ROUTE = "mcp-http"
CA_SKILL_ROOT = PurePosixPath("SKILLS/ca")
CA_SKILL_ENTRYPOINT = CA_SKILL_ROOT / "SKILL.md"
MCP_FILES = (
    "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/204_MCP/http_server.py",
    "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/204_MCP/server.py",
    "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/204_MCP/implementation_server.py",
    "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/WORKFLOW_ORCHESTRATOR/docker/Dockerfile",
    "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/WORKFLOW_ORCHESTRATOR/docker/entrypoint.py",
    "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/WORKFLOW_ORCHESTRATOR/docker/project_mcp_backend.py",
    "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/WORKFLOW_ORCHESTRATOR/docker/project_mcp_launcher.py",
    "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/WORKFLOW_ORCHESTRATOR/docker/project-mcp.compose.yaml",
)
REQUIRED_PACKAGE_CARRIERS = ("pyproject.toml", "uv.lock", "version.toml", *MCP_FILES)
_PACKAGE_MANIFEST_KEYS = frozenset(
    {"schema_version", "package", "framework_version", "version_toml_sha256", "source_catalog_sha256", "files"}
)
_PACKAGE_SELECTOR_KEYS = frozenset(
    {
        "schema_version", "package_manifest_sha256", "release_relpath", "framework_version",
        "version_toml_sha256", "source_catalog_sha256", "full_gate_receipt_sha256", "image_digest",
    }
)
_RUNTIME_SELECTOR_KEYS = frozenset(
    {
        "schema_version", "package_manifest_sha256", "target_project_context_sha256",
        "state_generation", "installation_lock_generation", "image_digest",
    }
)
_CONTEXT_REQUIRED_KEYS = frozenset(
    {
        "schema_version", "mode", "target_project_identity", "control_child_relpath", "settings_sha256",
        "project_structure_sha256", "registry_sha256", "repository_identity", "root_locator",
        "framework_instance_settings_sha256", "source_catalog_sha256", "methodology_source_identities",
        CONTEXT_DIGEST_FIELD,
    }
)
_CONTEXT_OPTIONAL_KEYS = frozenset({"relocates_context_sha256"})
_COMPOSE_SERVICE_KEYS = frozenset(
    {
        "image", "init", "read_only", "cap_drop", "security_opt", "restart", "stop_grace_period",
        "tmpfs", "pids_limit", "mem_limit", "cpus", "command", "environment", "labels", "volumes",
        "ports", "healthcheck",
    }
)
_COMPOSE_ENVIRONMENT = {
    "CAPRMEDIO_RUNTIME_NAMESPACE": "docker",
    "CAPRMEDIO_CONTROL_ROOT": "${CAPRMEDIO_CONTROL_ROOT:?Selected control root is required}",
    "CAPRMEDIO_PROJECT_INSTANCE_ID": "${CAPRMEDIO_PROJECT_INSTANCE_ID:?Selected identity is required}",
    "CAPRMEDIO_HOST_PROJECT_ROOT": "${CAPRMEDIO_PROJECT_ROOT:?Selected Project root is required}",
}
_COMPOSE_LABELS = {
    "org.caprmedio.project": "${CAPRMEDIO_PROJECT_INSTANCE_ID}",
    "org.caprmedio.runtime.fingerprint": "${CAPRMEDIO_RUNTIME_FINGERPRINT:?Image fingerprint is required}",
    "org.caprmedio.service": MCP_ROUTE,
    "org.caprmedio.control_root": "${CAPRMEDIO_CONTROL_ROOT}",
    "org.caprmedio.host_project_root": "${CAPRMEDIO_PROJECT_ROOT}",
}
_COMPOSE_HEALTHCHECK = {
    "test": ["CMD", "python", "-c", "import json,urllib.request; assert json.load(urllib.request.urlopen('http://127.0.0.1:8092/health',timeout=3))['ready'] is True"],
    "interval": "2s",
    "timeout": "5s",
    "retries": 25,
    "start_period": "3s",
}


class InstalledMcpBindingError(RuntimeError):
    """A stable refusal from the installed-MCP admission boundary."""

    def __init__(self, code: str, message: str) -> None:
        self.code = code
        super().__init__(message)


@dataclass(frozen=True)
class TargetProjectContext:
    """The reopened target context used by the selected runtime selector."""

    sha256: str
    mode: str
    target_project_identity: str
    control_child_relpath: str
    path: Path


@dataclass(frozen=True)
class PackageCaSkillMember:
    """One verified package member for the canonical public ``ca`` Skill."""

    path: str
    sha256: str
    mode: int


@dataclass(frozen=True)
class InstalledMcpBinding:
    """The only package-relative MCP routes admitted for later activation."""

    package_manifest_sha256: str
    source_catalog_sha256: str
    target_context: TargetProjectContext
    package_selector_sha256: str
    runtime_selector_sha256: str
    image_digest: str
    package_root: Path
    mcp_server: Path
    mcp_http_server: Path
    dockerfile: Path
    compose_file: Path
    route: str = MCP_ROUTE
    anonymous: bool = True
    loopback_host: str = "127.0.0.1"
    loopback_path: str = "/mcp"
    readonly_container: bool = True
    pids_limit: int = 128
    memory_limit: str = "512m"
    cpu_limit: int = 1
    package_ca_skill: tuple[PackageCaSkillMember, ...] = ()


def _refuse(code: str, message: str) -> None:
    raise InstalledMcpBindingError(code, message)


def _sha256(value: object, *, code: str, label: str) -> str:
    if not isinstance(value, str) or SHA256.fullmatch(value) is None:
        _refuse(code, f"{label} must be a lowercase SHA-256")
    return value


def _safe_relative(value: object, *, code: str, label: str) -> PurePosixPath:
    if not isinstance(value, str) or not value:
        _refuse(code, f"{label} must be a non-empty package-relative path")
    path = PurePosixPath(value)
    if path.is_absolute() or any(part in {"", ".", ".."} for part in path.parts) or path.as_posix() != value:
        _refuse(code, f"{label} is unsafe")
    return path


def _project_root(value: str | Path) -> Path:
    try:
        root = Path(value)
        if not root.is_absolute() or root.is_symlink() or not root.is_dir() or root.resolve(strict=True) != root:
            _refuse("target-project-invalid", "target Project root must be a canonical regular directory")
        return root
    except InstalledMcpBindingError:
        raise
    except (OSError, TypeError, ValueError) as error:
        raise InstalledMcpBindingError("target-project-invalid", "target Project root is unavailable") from error


def _regular_file(root: Path, relative: PurePosixPath, *, code: str, label: str) -> tuple[Path, bytes]:
    """Open a project-contained regular file without following a symlink."""

    path = root.joinpath(*relative.parts)
    cursor = root
    try:
        for index, part in enumerate(relative.parts):
            cursor = cursor / part
            metadata = os.lstat(cursor)
            if stat.S_ISLNK(metadata.st_mode):
                _refuse(code, f"{label} contains a symlink")
            if index + 1 < len(relative.parts) and not stat.S_ISDIR(metadata.st_mode):
                _refuse(code, f"{label} has a non-directory parent")
        if not stat.S_ISREG(os.lstat(path).st_mode):
            _refuse(code, f"{label} is not a regular file")
        flags = os.O_RDONLY
        if hasattr(os, "O_NOFOLLOW"):
            flags |= os.O_NOFOLLOW
        descriptor = os.open(path, flags)
        try:
            if not stat.S_ISREG(os.fstat(descriptor).st_mode):
                _refuse(code, f"{label} changed while being opened")
            chunks = []
            while True:
                chunk = os.read(descriptor, 64 * 1024)
                if not chunk:
                    break
                chunks.append(chunk)
            return path, b"".join(chunks)
        finally:
            os.close(descriptor)
    except InstalledMcpBindingError:
        raise
    except (FileNotFoundError, NotADirectoryError, OSError) as error:
        raise InstalledMcpBindingError(code, f"{label} is missing or unsafe") from error


def _parse_toml(payload: bytes, *, code: str, label: str) -> dict[str, Any]:
    try:
        value = tomllib.loads(payload.decode("utf-8"))
    except (UnicodeError, tomllib.TOMLDecodeError) as error:
        raise InstalledMcpBindingError(code, f"{label} is not valid UTF-8 TOML") from error
    if not isinstance(value, dict):
        _refuse(code, f"{label} root must be a TOML table")
    return value


def _verification(verified_package: VerifiedFrameworkPackage) -> tuple[Path, str, str, tuple[dict[str, Any], ...]]:
    """Normalize the exact public output contract of ``framework_package``."""

    if not isinstance(verified_package, VerifiedFrameworkPackage):
        _refuse("package-verification-invalid", "installed MCP requires a typed Framework package verification")
    package_root = verified_package.root
    manifest_sha256 = _sha256(verified_package.manifest_digest, code="package-verification-invalid", label="package manifest")
    catalog_sha256 = _sha256(getattr(verified_package, "source_catalog_sha256"), code="package-verification-invalid", label="source catalog")
    if not isinstance(package_root, Path) or not package_root.is_absolute():
        _refuse("package-verification-invalid", "package verification must retain an absolute package root")
    supplied_rows = verified_package.inventory
    if not isinstance(supplied_rows, tuple) or not supplied_rows:
        _refuse("package-verification-invalid", "package verification has no ordered inventory")
    rows: list[dict[str, Any]] = []
    seen: set[str] = set()
    for supplied in supplied_rows:
        path = _safe_relative(getattr(supplied, "path", None), code="package-verification-invalid", label="package inventory path").as_posix()
        checksum = _sha256(getattr(supplied, "sha256", None), code="package-verification-invalid", label="package inventory digest")
        mode = getattr(supplied, "mode", None)
        role = getattr(supplied, "role", None)
        if isinstance(mode, bool) or not isinstance(mode, int) or not 0 <= mode <= 0o777 or not isinstance(role, str) or not role:
            _refuse("package-verification-invalid", "package inventory metadata is invalid")
        if path in seen:
            _refuse("package-verification-invalid", "package inventory repeats a path")
        seen.add(path)
        rows.append({"path": path, "sha256": checksum, "mode": mode, "role": role})
    return package_root, manifest_sha256, catalog_sha256, tuple(rows)


def _package_root(root: Path, package_root: Path, manifest_sha256: str) -> Path:
    expected = root.joinpath(*INSTALL_RELEASES_RELATIVE.parts, manifest_sha256)
    if package_root != expected:
        _refuse("installed-package-foreign", "verified package root is not the selected installed release")
    try:
        if package_root.is_symlink() or not package_root.is_dir() or package_root.resolve(strict=True) != package_root:
            _refuse("installed-package-foreign", "installed release root is unavailable or symlinked")
    except InstalledMcpBindingError:
        raise
    except OSError as error:
        raise InstalledMcpBindingError("installed-package-foreign", "installed release root is unavailable") from error
    return expected


def _actual_package_paths(package_root: Path) -> set[str]:
    """Return all package files and refuse every undeclared symlink or special file."""

    found: set[str] = set()
    stack = [package_root]
    while stack:
        folder = stack.pop()
        try:
            entries = list(os.scandir(folder))
        except OSError as error:
            raise InstalledMcpBindingError("installed-package-tampered", "installed package cannot be enumerated") from error
        for entry in entries:
            relative = Path(entry.path).relative_to(package_root).as_posix()
            try:
                metadata = entry.stat(follow_symlinks=False)
            except OSError as error:
                raise InstalledMcpBindingError("installed-package-tampered", "installed package entry is unavailable") from error
            if stat.S_ISLNK(metadata.st_mode):
                _refuse("installed-package-tampered", f"installed package contains a symlink: {relative}")
            if stat.S_ISDIR(metadata.st_mode):
                stack.append(Path(entry.path))
            elif stat.S_ISREG(metadata.st_mode):
                found.add(relative)
            else:
                _refuse("installed-package-tampered", f"installed package contains a non-regular carrier: {relative}")
    return found


def _verify_package_tree(package_root: Path, manifest_sha256: str, catalog_sha256: str,
                         rows: tuple[dict[str, Any], ...]) -> dict[str, dict[str, Any]]:
    row_map = {row["path"]: row for row in rows}
    expected_files = {"manifest.toml", *row_map}
    actual_files = _actual_package_paths(package_root)
    if actual_files != expected_files:
        _refuse("installed-package-tampered", "installed package files differ from its verified inventory")

    _, manifest_payload = _regular_file(package_root, PurePosixPath("manifest.toml"), code="installed-package-missing", label="package manifest")
    if hashlib.sha256(manifest_payload).hexdigest() != manifest_sha256:
        _refuse("installed-package-tampered", "installed package manifest digest differs from its identity")
    manifest = _parse_toml(manifest_payload, code="installed-package-tampered", label="package manifest")
    if set(manifest) != _PACKAGE_MANIFEST_KEYS or manifest.get("schema_version") != SCHEMA_VERSION or manifest.get("package") != PACKAGE_NAME:
        _refuse("installed-package-tampered", "package manifest schema is not closed")
    if not isinstance(manifest.get("framework_version"), str) or not manifest["framework_version"]:
        _refuse("installed-package-tampered", "package manifest framework version is invalid")
    _sha256(manifest.get("version_toml_sha256"), code="installed-package-tampered", label="package version carrier")
    if manifest.get("source_catalog_sha256") != catalog_sha256:
        _refuse("catalog-digest-stale", "package manifest source catalog differs from its verified catalog")
    manifest_rows = manifest.get("files")
    if not isinstance(manifest_rows, list) or manifest_rows != list(rows):
        _refuse("installed-package-tampered", "package manifest inventory differs from typed verification")
    for row in rows:
        relative = PurePosixPath(row["path"])
        carrier, payload = _regular_file(package_root, relative, code="installed-package-missing", label=f"package carrier {row['path']}")
        if hashlib.sha256(payload).hexdigest() != row["sha256"] or carrier.stat().st_mode & 0o777 != row["mode"]:
            _refuse("installed-package-tampered", f"package carrier differs from inventory: {row['path']}")
    catalog_path, catalog_payload = _regular_file(package_root, PurePosixPath("catalog.toml"), code="installed-package-missing", label="package catalog")
    if catalog_path.as_posix() not in {package_root.joinpath(*PurePosixPath(row["path"]).parts).as_posix() for row in rows}:
        _refuse("installed-package-tampered", "package catalog is not inventory-declared")
    if hashlib.sha256(catalog_payload).hexdigest() != catalog_sha256:
        _refuse("catalog-digest-stale", "installed source catalog digest is stale")
    _parse_toml(catalog_payload, code="installed-package-tampered", label="package catalog")
    for required in REQUIRED_PACKAGE_CARRIERS:
        if required not in row_map:
            _refuse("installed-package-missing", f"installed package omits required MCP carrier: {required}")
    if not any(path.startswith("102_FRAMEWORK_ENGINE/") for path in row_map):
        _refuse("installed-package-missing", "installed package omits the Engine inventory")
    return row_map


def _package_ca_skill(row_map: Mapping[str, Mapping[str, Any]]) -> tuple[PackageCaSkillMember, ...]:
    """Extract only the verified canonical ``SKILLS/ca`` package subtree."""

    members: list[PackageCaSkillMember] = []
    prefix = CA_SKILL_ROOT.as_posix() + "/"
    for path, row in row_map.items():
        if not path.startswith(prefix):
            continue
        if row.get("role") != "skill":
            _refuse("package-ca-skill-invalid", "canonical ca Skill contains a non-Skill inventory member")
        members.append(PackageCaSkillMember(path, row["sha256"], row["mode"]))
    members.sort(key=lambda member: member.path)
    if not members or members[0].path != CA_SKILL_ENTRYPOINT.as_posix():
        _refuse("package-ca-skill-missing", "installed package omits canonical SKILLS/ca/SKILL.md")
    if any(member.path == CA_SKILL_ENTRYPOINT.as_posix() and member.mode != 0o644 for member in members):
        _refuse("package-ca-skill-invalid", "canonical ca Skill entrypoint mode is invalid")
    return tuple(members)


def _selector(root: Path, package_root: Path, package: VerifiedFrameworkPackage,
              manifest: Mapping[str, Any]) -> tuple[dict[str, Any], str]:
    _, payload = _regular_file(root, INSTALL_CURRENT_RELATIVE, code="installed-selector-missing", label="installed package selector")
    return _selector_payload(payload, package_root, package, installed_root=root)


def _selector_payload(payload: bytes, package_root: Path, package: VerifiedFrameworkPackage,
                      *, installed_root: Path | None = None) -> tuple[dict[str, Any], str]:
    """Verify exact D598 selector bytes without requiring their publication."""

    selector = _parse_toml(payload, code="installed-selector-invalid", label="installed package selector")
    if (set(selector) == _PACKAGE_SELECTOR_KEYS
            and selector.get("source_catalog_sha256") != package.source_catalog_sha256):
        _refuse("catalog-digest-stale", "installed package selector catalog digest is stale")
    if (set(selector) == _PACKAGE_SELECTOR_KEYS
            and selector.get("release_relpath") != f"releases/{package.manifest_digest}"):
        _refuse("installed-selector-mismatch", "installed package selector release path is not canonical")
    try:
        typed_selector = verify_current_package_selector(payload, package)
    except FrameworkPackageError as error:
        if error.code == "package-selector-mismatch":
            _refuse("installed-selector-mismatch", str(error))
        _refuse("installed-selector-invalid", str(error))
    expected_relpath = f"releases/{package.manifest_digest}"
    if installed_root is not None and package_root != installed_root / ".caprmedio_install" / expected_relpath:
        _refuse("installed-selector-mismatch", "installed package selector root differs")
    return {
        "package_manifest_sha256": typed_selector.package_manifest_sha256,
        "source_catalog_sha256": typed_selector.source_catalog_sha256,
        "image_digest": typed_selector.image_digest,
    }, hashlib.sha256(payload).hexdigest()


def _context(
    root: Path,
    expected_digest: str,
    *,
    verified_package: VerifiedFrameworkPackage | None = None,
) -> TargetProjectContext:
    digest = _sha256(expected_digest, code="target-context-invalid", label="target context")
    relative = RUNTIME_CONTEXTS_RELATIVE / f"{digest}.toml"
    path, payload = _regular_file(root, relative, code="target-context-missing", label="target Project context")
    document = _parse_toml(payload, code="target-context-invalid", label="target Project context")
    if set(document) - _CONTEXT_OPTIONAL_KEYS != _CONTEXT_REQUIRED_KEYS or document.get("schema_version") != CONTEXT_SCHEMA_VERSION:
        _refuse("target-context-invalid", "target Project context schema is not closed")
    if document.get(CONTEXT_DIGEST_FIELD) != digest:
        _refuse("target-context-mismatch", "target Project context self-digest differs from selector identity")
    mode = document.get("mode")
    identity = document.get("target_project_identity")
    control = document.get("control_child_relpath")
    if (
        mode not in {"bootstrap", "adopt"}
        or not isinstance(identity, str)
        or not identity.strip()
        or "\x00" in identity
        or "\n" in identity
        or "\r" in identity
    ):
        _refuse("target-context-invalid", "target Project context identity is invalid")
    control_path = _safe_relative(control, code="target-context-invalid", label="target control child")
    if (
        len(control_path.parts) != 1
        or not control_path.name.startswith(".caprmedio_")
        or control_path.name == ".caprmedio_"
    ):
        _refuse("target-context-invalid", "target control child is not an exact direct control root")
    for key in (
        "settings_sha256",
        "project_structure_sha256",
        "registry_sha256",
        "framework_instance_settings_sha256",
        "source_catalog_sha256",
    ):
        _sha256(document.get(key), code="target-context-invalid", label=key)
    identities = document.get("methodology_source_identities")
    if (
        not isinstance(identities, list)
        or not identities
        or any(not isinstance(identity, str) or not identity for identity in identities)
        or identities != sorted(identities)
        or len(set(identities)) != len(identities)
    ):
        _refuse("target-context-invalid", "target Methodology source identities are invalid")
    repository_identity = document.get("repository_identity")
    if repository_identity is not False:
        _sha256(repository_identity, code="target-context-invalid", label="target repository identity")
    locator = document.get("root_locator")
    locator_path = Path(locator) if isinstance(locator, str) else Path()
    if (
        not isinstance(locator, str)
        or not locator
        or Path(locator).is_absolute()
        or ".." in locator_path.parts
        or locator_path.as_posix() in {"", "."}
        or locator_path.as_posix() != locator
        or "\x00" in locator
        or "\n" in locator
        or "\r" in locator
    ):
        _refuse("target-context-invalid", "target root locator is unsafe")
    relocation = document.get("relocates_context_sha256")
    if relocation is not None:
        _sha256(relocation, code="target-context-invalid", label="relocated context")
        if relocation == digest:
            _refuse("target-context-invalid", "target context cannot relocate itself")
    canonical = canonical_target_project_context_toml(
        mode=mode,
        target_project_identity=identity,
        control_child_relpath=control_path.as_posix(),
        settings_sha256=document["settings_sha256"],
        project_structure_sha256=document["project_structure_sha256"],
        registry_sha256=document["registry_sha256"],
        repository_identity=repository_identity,
        root_locator=locator,
        relocates_context_sha256=relocation,
        framework_instance_settings_sha256=document["framework_instance_settings_sha256"],
        source_catalog_sha256=document["source_catalog_sha256"],
        methodology_source_identities=tuple(identities),
    )
    persisted = canonical + f'{CONTEXT_DIGEST_FIELD} = "{digest}"\n'.encode("utf-8")
    if hashlib.sha256(canonical).hexdigest() != digest or payload != persisted:
        _refuse("target-context-mismatch", "target Project context bytes differ from canonical selector identity")
    control_dir = root.joinpath(*control_path.parts)
    if control_dir.is_symlink() or not control_dir.is_dir():
        _refuse("target-context-mismatch", "target control child is no longer present")
    controls = {
        "settings_sha256": PurePosixPath(control_path.as_posix()) / "caprmedio_project_settings.toml",
        "project_structure_sha256": PurePosixPath(control_path.as_posix()) / "project_structure.toml",
        "registry_sha256": PurePosixPath(control_path.as_posix()) / "operators_registry.toml",
    }
    for field, control_relative in controls.items():
        _, observed = _regular_file(root, control_relative, code="target-context-mismatch", label=field)
        if hashlib.sha256(observed).hexdigest() != document[field]:
            _refuse("target-context-mismatch", f"target control changed: {field}")
    try:
        from target_methodology_selection import (
            FRAMEWORK_INSTANCE_SETTINGS_RELATIVE,
            TargetMethodologySelectionError,
            resolve_target_methodology_selection,
        )

        _, framework_settings = _regular_file(
            root,
            PurePosixPath(control_path.as_posix()) / FRAMEWORK_INSTANCE_SETTINGS_RELATIVE,
            code="target-context-mismatch",
            label="Framework Instance Settings",
        )
        if hashlib.sha256(framework_settings).hexdigest() != document["framework_instance_settings_sha256"]:
            _refuse("target-context-mismatch", "Framework Instance Settings changed")
        if verified_package is not None:
            from framework_package import provide_installation_package_evidence

            if not isinstance(verified_package, VerifiedFrameworkPackage):
                _refuse("target-context-invalid", "target context package is untrusted")
            evidence = provide_installation_package_evidence(verified_package.root)
            if (
                evidence.package_manifest_sha256 != verified_package.manifest_digest
                or evidence.catalog_sha256 != verified_package.source_catalog_sha256
            ):
                _refuse("target-context-mismatch", "target context package evidence is stale")
            selection = resolve_target_methodology_selection(
                control_root=control_dir,
                package_root=verified_package.root,
                package_evidence=evidence,
            )
            if (
                selection.framework_instance_settings_sha256 != document["framework_instance_settings_sha256"]
                or selection.source_catalog_sha256 != document["source_catalog_sha256"]
                or selection.methodology_source_identities != tuple(identities)
            ):
                _refuse("target-context-mismatch", "target Methodology selection changed")
    except InstalledMcpBindingError:
        raise
    except (FrameworkPackageError, TargetMethodologySelectionError) as error:
        raise InstalledMcpBindingError("target-context-mismatch", "target Methodology selection cannot be reopened") from error
    return TargetProjectContext(digest, mode, identity, control_path.as_posix(), path)


def _runtime_selector(root: Path, manifest_sha256: str, context: TargetProjectContext,
                      image_digest: str) -> str:
    _, payload = _regular_file(root, RUNTIME_CURRENT_RELATIVE, code="runtime-selector-missing", label="target runtime selector")
    return _runtime_selector_payload(payload, manifest_sha256, context, image_digest)


def _runtime_selector_payload(payload: bytes, manifest_sha256: str, context: TargetProjectContext,
                              image_digest: str) -> str:
    """Verify exact prospective D599 selector bytes without publishing them."""

    selector = _parse_toml(payload, code="runtime-selector-invalid", label="target runtime selector")
    if set(selector) != _RUNTIME_SELECTOR_KEYS or selector.get("schema_version") != SCHEMA_VERSION:
        _refuse("runtime-selector-invalid", "target runtime selector schema is not closed")
    if selector.get("package_manifest_sha256") != manifest_sha256:
        _refuse("runtime-selector-mismatch", "target runtime selector chooses another package")
    if selector.get("target_project_context_sha256") != context.sha256:
        _refuse("target-context-mismatch", "target runtime selector chooses another target context")
    if selector.get("image_digest") != image_digest:
        _refuse("runtime-selector-mismatch", "target runtime selector image differs from installed package")
    state_generation = selector.get("state_generation")
    if isinstance(state_generation, bool) or not isinstance(state_generation, int) or state_generation < 1:
        _refuse("runtime-selector-invalid", "target runtime selector state_generation is invalid")
    lock_generation = selector.get("installation_lock_generation")
    if not isinstance(lock_generation, str) or LOCK_GENERATION.fullmatch(lock_generation) is None:
        _refuse("runtime-selector-invalid", "target runtime selector installation_lock_generation is invalid")
    return hashlib.sha256(payload).hexdigest()


def admit_candidate_mcp_binding(
    target_project_root: str | Path,
    verified_package: VerifiedFrameworkPackage,
    *,
    target_context_sha256: str,
    prospective_package_selector: bytes,
    prospective_runtime_selector: bytes,
    route: str = MCP_ROUTE,
) -> InstalledMcpBinding:
    """Read-only admission of one sealed, non-active package/selector packet."""

    if route != MCP_ROUTE:
        _refuse("mcp-route-undesignated", "installed MCP route is not designated")
    if not isinstance(prospective_package_selector, bytes) or not isinstance(prospective_runtime_selector, bytes):
        _refuse("candidate-selector-invalid", "prospective selectors must be exact bytes")
    root = _project_root(target_project_root)
    package_root, manifest_sha256, catalog_sha256, rows = _verification(verified_package)
    try:
        package_root.resolve(strict=True).relative_to(root.resolve(strict=True))
    except (OSError, ValueError) as error:
        raise InstalledMcpBindingError("candidate-package-foreign", "candidate package is outside the target Project") from error
    if package_root.is_symlink() or not package_root.is_dir():
        _refuse("candidate-package-invalid", "candidate package root is unavailable")
    row_map = _verify_package_tree(package_root, manifest_sha256, catalog_sha256, rows)
    ca_skill = _package_ca_skill(row_map)
    _manifest_path, manifest_payload = _regular_file(package_root, PurePosixPath("manifest.toml"), code="installed-package-missing", label="package manifest")
    manifest = _parse_toml(manifest_payload, code="installed-package-tampered", label="package manifest")
    selector, package_selector_sha256 = _selector_payload(prospective_package_selector, package_root, verified_package)
    context = _context(root, target_context_sha256, verified_package=verified_package)
    runtime_selector_sha256 = _runtime_selector_payload(
        prospective_runtime_selector, manifest_sha256, context, selector["image_digest"],
    )
    _compose_contract(package_root)
    for route_file in MCP_FILES:
        if route_file not in row_map:
            _refuse("mcp-route-undesignated", f"candidate package has no verified MCP carrier: {route_file}")
    return InstalledMcpBinding(
        package_manifest_sha256=manifest_sha256, source_catalog_sha256=catalog_sha256,
        target_context=context, package_selector_sha256=package_selector_sha256,
        runtime_selector_sha256=runtime_selector_sha256, image_digest=selector["image_digest"],
        package_root=package_root, mcp_server=package_root / MCP_FILES[1],
        mcp_http_server=package_root / MCP_FILES[0], dockerfile=package_root / MCP_FILES[3],
        compose_file=package_root / MCP_FILES[-1], package_ca_skill=ca_skill,
    )


def _compose_contract(package_root: Path) -> None:
    relative = PurePosixPath(MCP_FILES[-1])
    _, payload = _regular_file(package_root, relative, code="installed-package-missing", label="installed MCP Compose carrier")
    try:
        document = yaml.safe_load(payload)
    except yaml.YAMLError as error:
        raise InstalledMcpBindingError("mcp-compose-invalid", "installed MCP Compose carrier is invalid YAML") from error
    if not isinstance(document, dict) or set(document) != {"services"} or not isinstance(document["services"], dict) or set(document["services"]) != {MCP_ROUTE}:
        _refuse("mcp-compose-invalid", "installed MCP Compose service set is not closed")
    service = document["services"][MCP_ROUTE]
    if not isinstance(service, dict):
        _refuse("mcp-compose-invalid", "installed MCP service is invalid")
    if set(service) != _COMPOSE_SERVICE_KEYS:
        _refuse("mcp-compose-invalid", "installed MCP Compose service schema is not closed")
    if service.get("image") != "${CAPRMEDIO_IMAGE:?An admitted immutable image is required}" or service.get("init") is not True:
        _refuse("mcp-compose-invalid", "installed MCP image or init contract differs")
    if (service.get("read_only") is not True or service.get("cap_drop") != ["ALL"]
            or service.get("security_opt") != ["no-new-privileges:true"]):
        _refuse("mcp-compose-invalid", "installed MCP is not a read-only, capability-dropped target")
    if service.get("restart") != "no" or service.get("stop_grace_period") != "10s":
        _refuse("mcp-compose-invalid", "installed MCP lifecycle bounds differ from the admitted profile")
    if (service.get("pids_limit") != 128 or service.get("mem_limit") != "512m" or service.get("cpus") != 1
            or service.get("tmpfs") != ["/tmp:size=128m,mode=1777"]):
        _refuse("mcp-compose-invalid", "installed MCP resource bounds differ from the admitted profile")
    if service.get("command") != [MCP_ROUTE] or service.get("ports") != ["127.0.0.1:${CAPRMEDIO_MCP_HTTP_PORT:-}:8092"]:
        _refuse("mcp-compose-invalid", "installed MCP transport is not the anonymous loopback route")
    environment = service.get("environment")
    if environment != _COMPOSE_ENVIRONMENT:
        _refuse("mcp-compose-invalid", "installed MCP anonymous route has an authentication carrier")
    if service.get("labels") != _COMPOSE_LABELS or service.get("healthcheck") != _COMPOSE_HEALTHCHECK:
        _refuse("mcp-compose-invalid", "installed MCP labels or healthcheck differ from the admitted profile")
    volumes = service.get("volumes")
    if volumes != [{"type": "bind", "source": "${CAPRMEDIO_PROJECT_ROOT}", "target": "/project"}]:
        _refuse("mcp-compose-invalid", "installed MCP target mount is not exact")


def admit_installed_mcp_binding(
    target_project_root: str | Path,
    verified_package: VerifiedFrameworkPackage,
    *,
    target_context_sha256: str,
    route: str = MCP_ROUTE,
) -> InstalledMcpBinding:
    """Reopen one installed package and bind its one admitted MCP service.

    No checkout path, caller catalog, arbitrary route, launcher handle, Docker
    client, or target publication input is accepted.  The returned value is a
    read-only admission proof for a later activation lane.
    """

    if route != MCP_ROUTE:
        _refuse("mcp-route-undesignated", "installed MCP route is not designated")
    root = _project_root(target_project_root)
    package_root, manifest_sha256, catalog_sha256, rows = _verification(verified_package)
    package_root = _package_root(root, package_root, manifest_sha256)
    row_map = _verify_package_tree(package_root, manifest_sha256, catalog_sha256, rows)
    ca_skill = _package_ca_skill(row_map)
    _, manifest_payload = _regular_file(package_root, PurePosixPath("manifest.toml"), code="installed-package-missing", label="package manifest")
    manifest = _parse_toml(manifest_payload, code="installed-package-tampered", label="package manifest")
    selector, package_selector_sha256 = _selector(root, package_root, verified_package, manifest)
    context = _context(root, target_context_sha256, verified_package=verified_package)
    runtime_selector_sha256 = _runtime_selector(root, manifest_sha256, context, selector["image_digest"])
    _compose_contract(package_root)
    for route_file in MCP_FILES:
        if route_file not in row_map:
            _refuse("mcp-route-undesignated", f"installed package has no verified MCP carrier: {route_file}")
    return InstalledMcpBinding(
        package_manifest_sha256=manifest_sha256,
        source_catalog_sha256=catalog_sha256,
        target_context=context,
        package_selector_sha256=package_selector_sha256,
        runtime_selector_sha256=runtime_selector_sha256,
        image_digest=selector["image_digest"],
        package_root=package_root,
        mcp_server=package_root / MCP_FILES[1],
        mcp_http_server=package_root / MCP_FILES[0],
        dockerfile=package_root / MCP_FILES[3],
        compose_file=package_root / MCP_FILES[-1],
        package_ca_skill=ca_skill,
    )


__all__ = [
    "InstalledMcpBinding",
    "InstalledMcpBindingError",
    "MCP_FILES",
    "MCP_ROUTE",
    "PackageCaSkillMember",
    "TargetProjectContext",
    "admit_candidate_mcp_binding",
    "admit_installed_mcp_binding",
]
