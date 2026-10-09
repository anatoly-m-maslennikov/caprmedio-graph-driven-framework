"""Read-only admission for one explicit target installation context.

This boundary intentionally does not create runtime state.  In particular,
``.caprmedio_runtime/config.toml`` is mutable target-owned configuration and
is neither an activation indicator nor an output of context binding.
"""

from __future__ import annotations

from dataclasses import dataclass
import hashlib
import json
import os
from pathlib import Path
import re
import stat
import tomllib


SETTINGS_FILENAME = "caprmedio_project_settings.toml"
STRUCTURE_FILENAME = "project_structure.toml"
REGISTRY_FILENAME = "operators_registry.toml"
CONTROL_PREFIX = ".caprmedio_"
RUNTIME_DIRECTORY = Path(".caprmedio_runtime")
INSTALLATION_DIRECTORY = RUNTIME_DIRECTORY / "installation"
CONTEXT_DIGEST_FIELD = "target_project_context_sha256"
_SHA256 = re.compile(r"[0-9a-f]{64}\Z")


class InstallationContextError(ValueError):
    """A target admission refusal before installation state is published."""


def _quoted(value: str) -> str:
    return json.dumps(value, ensure_ascii=False)


def _sha256(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def _require_digest(value: object, field: str) -> str:
    if not isinstance(value, str) or not _SHA256.fullmatch(value):
        raise InstallationContextError(f"{field} must be a lowercase SHA-256 digest")
    return value


def _require_text(value: object, field: str) -> str:
    if not isinstance(value, str) or not value.strip() or "\x00" in value or "\n" in value or "\r" in value:
        raise InstallationContextError(f"{field} must be one non-empty line")
    return value


def _require_relative_locator(value: object) -> str:
    locator = _require_text(value, "root_locator")
    path = Path(locator)
    if path.is_absolute() or ".." in path.parts or path.as_posix() in {"", "."} or path.as_posix() != locator:
        raise InstallationContextError("root_locator must be a normalized relative locator")
    return locator


def canonical_target_project_context_toml(
    *,
    mode: str,
    target_project_identity: str,
    control_child_relpath: str,
    settings_sha256: str,
    project_structure_sha256: str,
    registry_sha256: str,
    repository_identity: str | bool,
    root_locator: str,
    relocates_context_sha256: str | None = None,
) -> bytes:
    """Render the D600 digest preimage, excluding its self-digest carrier.

    The persisted context adds :data:`CONTEXT_DIGEST_FIELD` after these
    canonical bytes.  Both the target-context writer and installed-runtime
    reader use this one renderer so the file name, self-digest and selector
    always identify the same byte preimage.
    """

    lines = [
        "schema_version = 1",
        f"mode = {_quoted(mode)}",
        f"target_project_identity = {_quoted(target_project_identity)}",
        f"control_child_relpath = {_quoted(control_child_relpath)}",
        f"settings_sha256 = {_quoted(settings_sha256)}",
        f"project_structure_sha256 = {_quoted(project_structure_sha256)}",
        f"registry_sha256 = {_quoted(registry_sha256)}",
        (
            "repository_identity = false"
            if repository_identity is False
            else f"repository_identity = {_quoted(str(repository_identity))}"
        ),
        f"root_locator = {_quoted(root_locator)}",
    ]
    if relocates_context_sha256 is not None:
        lines.append(f"relocates_context_sha256 = {_quoted(relocates_context_sha256)}")
    return ("\n".join(lines) + "\n").encode("utf-8")


@dataclass(frozen=True)
class PackageSourcePin:
    """One source pin from an already admitted package catalog."""

    identity: str
    kind: str
    revision: str
    sha256: str
    admission_receipt_sha256: str


@dataclass(frozen=True)
class VerifiedPackageEvidence:
    """Expected package identity and pins for a package-bound installer.

    This value alone grants no authority.  ``bind_target_project_context``
    reopens ``TargetProjectRequest.package_root`` through the package provider
    and compares the provider's evidence to these expected pinned values.
    """

    package_manifest_sha256: str
    catalog_sha256: str
    source_pins: tuple[PackageSourcePin, ...]
    selected_source_identities: tuple[str, ...]
    verified: bool


@dataclass(frozen=True)
class TargetProjectRequest:
    """All explicit inputs necessary to bind one target Project."""

    target_root: Path | str
    control_child: str
    mode: str
    target_project_identity: str
    settings_path: Path | str
    project_structure_path: Path | str
    operators_registry_path: Path | str
    repository_identity: str | bool
    root_locator: str
    package_root: Path | str
    package_evidence: VerifiedPackageEvidence
    relocates_from: TargetProjectContext | None = None


@dataclass(frozen=True)
class TargetProjectContext:
    """The CA-D-600 carrier plus the verified package evidence in memory."""

    mode: str
    target_project_identity: str
    control_child_relpath: str
    settings_sha256: str
    project_structure_sha256: str
    registry_sha256: str
    repository_identity: str | bool
    root_locator: str
    package_evidence: VerifiedPackageEvidence
    relocates_context_sha256: str | None = None

    def toml_bytes(self) -> bytes:
        """Return canonical CA-D-600 bytes excluding the carrier digest itself."""
        return canonical_target_project_context_toml(
            mode=self.mode,
            target_project_identity=self.target_project_identity,
            control_child_relpath=self.control_child_relpath,
            settings_sha256=self.settings_sha256,
            project_structure_sha256=self.project_structure_sha256,
            registry_sha256=self.registry_sha256,
            repository_identity=self.repository_identity,
            root_locator=self.root_locator,
            relocates_context_sha256=self.relocates_context_sha256,
        )

    @property
    def sha256(self) -> str:
        return _sha256(self.toml_bytes())

    def with_digest_toml(self) -> bytes:
        """Render a persisted form whose digest is excluded from ``sha256``."""
        return self.toml_bytes() + f'{CONTEXT_DIGEST_FIELD} = "{self.sha256}"\n'.encode("utf-8")


def _canonical_root(value: Path | str) -> Path:
    try:
        raw = Path(value).expanduser()
        if not raw.is_absolute() or ".." in raw.parts:
            raise InstallationContextError("target_root must be an explicit absolute normalized directory")
        root = Path(os.path.abspath(raw))
        if root.resolve(strict=True) != root:
            raise InstallationContextError("target_root must not contain a symlink")
        status = root.stat()
        if not stat.S_ISDIR(status.st_mode):
            raise InstallationContextError("target_root must be a directory")
        return root
    except InstallationContextError:
        raise
    except (OSError, RuntimeError, TypeError, ValueError) as error:
        raise InstallationContextError("target_root is unavailable or unsafe") from error


def _control_child(value: object) -> str:
    if not isinstance(value, str) or not value:
        raise InstallationContextError("control_child must name one direct Project child")
    path = Path(value)
    if (
        path.is_absolute()
        or len(path.parts) != 1
        or ".." in path.parts
        or path.as_posix() != value
        or not path.name.startswith(CONTROL_PREFIX)
        or path.name == CONTROL_PREFIX
    ):
        raise InstallationContextError("control_child must name one normalized .caprmedio_<name> child")
    return path.name


def _require_control(root: Path, child: str) -> Path:
    control = root / child
    try:
        status = control.lstat()
    except OSError as error:
        raise InstallationContextError("selected control child is unavailable") from error
    if stat.S_ISLNK(status.st_mode) or not stat.S_ISDIR(status.st_mode):
        raise InstallationContextError("selected control child must be a regular directory")
    return control


def _explicit_carrier(value: Path | str, expected: Path, label: str) -> Path:
    try:
        supplied = Path(value)
        if not supplied.is_absolute() or ".." in supplied.parts or supplied != expected:
            raise InstallationContextError(f"{label} must be the exact selected control carrier")
        status = supplied.lstat()
        if stat.S_ISLNK(status.st_mode) or not stat.S_ISREG(status.st_mode):
            raise InstallationContextError(f"{label} must be a regular carrier")
        if supplied.resolve(strict=True) != expected:
            raise InstallationContextError(f"{label} must not resolve through a symlink")
        return supplied
    except InstallationContextError:
        raise
    except (OSError, RuntimeError, TypeError, ValueError) as error:
        raise InstallationContextError(f"{label} is unavailable") from error


def _snapshot_toml(path: Path, label: str) -> tuple[bytes, dict[str, object]]:
    try:
        before = path.stat()
        payload = path.read_bytes()
        after = path.stat()
        if (before.st_dev, before.st_ino, before.st_size, before.st_mtime_ns) != (
            after.st_dev,
            after.st_ino,
            after.st_size,
            after.st_mtime_ns,
        ):
            raise InstallationContextError(f"{label} changed while being reopened")
        document = tomllib.loads(payload.decode("utf-8"))
        if not isinstance(document, dict):
            raise InstallationContextError(f"{label} must be a TOML table")
        return payload, document
    except InstallationContextError:
        raise
    except (OSError, UnicodeError, tomllib.TOMLDecodeError, ValueError) as error:
        raise InstallationContextError(f"{label} is invalid") from error


def _validate_controls(
    settings: dict[str, object], structure: dict[str, object], registry: dict[str, object], *, child: str, identity: str
) -> None:
    paths = settings.get("paths")
    if not isinstance(paths, dict) or paths.get("control_root") != child:
        raise InstallationContextError("settings must bind the selected control_child")
    project = settings.get("project")
    if not isinstance(project, dict) or project.get("name") != identity:
        raise InstallationContextError("settings must confirm the declared target_project_identity")
    if structure.get("schema_version") != 1 or not isinstance(structure.get("scope_units"), list):
        raise InstallationContextError("project structure is incomplete or unsupported")
    if not isinstance(registry.get("operators"), list):
        raise InstallationContextError("operators registry must be supplied without a fabricated Operator")


def _reopen_package_evidence(
    package_root: Path | str, expected: object
) -> VerifiedPackageEvidence:
    """Return physical package evidence, never accepting a caller assertion.

    Revision, source-digest, catalog completeness, and physical tree policy
    remain exclusively owned by ``framework_package``.  Reimplementing those
    checks here would create a divergent package-admission policy.
    """
    if not isinstance(expected, VerifiedPackageEvidence):
        raise InstallationContextError("expected package evidence must be typed")
    try:
        from framework_package import FrameworkPackageError, provide_installation_package_evidence
    except ImportError as error:  # pragma: no cover - protects isolated callers.
        raise InstallationContextError("physical package evidence provider is unavailable") from error
    try:
        reopened = provide_installation_package_evidence(package_root)
    except FrameworkPackageError as error:
        raise InstallationContextError("physical package evidence could not be reopened") from error
    if not isinstance(reopened, VerifiedPackageEvidence):
        raise InstallationContextError("physical package provider returned an unsupported evidence type")
    if (
        reopened.package_manifest_sha256 != expected.package_manifest_sha256
        or reopened.catalog_sha256 != expected.catalog_sha256
        or reopened.source_pins != expected.source_pins
        or reopened.selected_source_identities != expected.selected_source_identities
    ):
        raise InstallationContextError("expected package evidence differs from reopened physical package")
    return reopened


def _runtime_is_empty(root: Path) -> None:
    """Refuse active runtime carriers while allowing mutable config.toml alone."""
    installation = root / INSTALLATION_DIRECTORY
    active = (
        installation / "current.toml",
        installation / "generations",
        root / ".caprmedio_runtime" / "framework" / "current.toml",
        root / ".caprmedio_runtime" / "framework" / "releases",
        root / ".agents" / "skills" / "ca",
    )
    if any(path.exists() or path.is_symlink() for path in active):
        raise InstallationContextError("target has an active runtime boundary")


def bind_target_project_context(request: TargetProjectRequest) -> TargetProjectContext:
    """Reopen and bind one requested Project with zero filesystem effects.

    A verified package is required before a target context becomes usable by an
    installation publisher; this function itself deliberately publishes neither
    the context carrier nor any runtime metadata.
    """
    if not isinstance(request, TargetProjectRequest):
        raise InstallationContextError("target context requires a typed explicit request")
    if request.mode not in {"bootstrap", "adopt"}:
        raise InstallationContextError("mode must be exactly bootstrap or adopt")
    identity = _require_text(request.target_project_identity, "target_project_identity")
    root = _canonical_root(request.target_root)
    child = _control_child(request.control_child)
    control = _require_control(root, child)
    settings_path = _explicit_carrier(request.settings_path, control / SETTINGS_FILENAME, "settings")
    structure_path = _explicit_carrier(
        request.project_structure_path, control / STRUCTURE_FILENAME, "project structure"
    )
    registry_path = _explicit_carrier(
        request.operators_registry_path, control / REGISTRY_FILENAME, "operators registry"
    )
    settings_bytes, settings = _snapshot_toml(settings_path, "settings")
    structure_bytes, structure = _snapshot_toml(structure_path, "project structure")
    registry_bytes, registry = _snapshot_toml(registry_path, "operators registry")
    _validate_controls(settings, structure, registry, child=child, identity=identity)
    evidence = _reopen_package_evidence(request.package_root, request.package_evidence)
    _runtime_is_empty(root)
    locator = _require_relative_locator(request.root_locator)
    repository_identity = request.repository_identity
    if repository_identity is not False:
        repository_identity = _require_digest(repository_identity, "repository_identity")
    predecessor = request.relocates_from
    relocation_sha256: str | None = None
    if predecessor is not None:
        if not isinstance(predecessor, TargetProjectContext):
            raise InstallationContextError("relocation predecessor must be a typed target context")
        if predecessor.target_project_identity != identity:
            raise InstallationContextError("relocation predecessor has a different declared Project identity")
        if predecessor.root_locator == locator:
            raise InstallationContextError("relocation predecessor must have a distinct root_locator")
        relocation_sha256 = predecessor.sha256
    return TargetProjectContext(
        mode=request.mode,
        target_project_identity=identity,
        control_child_relpath=child,
        settings_sha256=_sha256(settings_bytes),
        project_structure_sha256=_sha256(structure_bytes),
        registry_sha256=_sha256(registry_bytes),
        repository_identity=repository_identity,
        root_locator=locator,
        package_evidence=evidence,
        relocates_context_sha256=relocation_sha256,
    )


__all__ = [
    "CONTEXT_DIGEST_FIELD",
    "InstallationContextError",
    "PackageSourcePin",
    "TargetProjectContext",
    "TargetProjectRequest",
    "VerifiedPackageEvidence",
    "bind_target_project_context",
    "canonical_target_project_context_toml",
]
