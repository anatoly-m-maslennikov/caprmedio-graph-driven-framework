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
import tempfile
import tomllib


SETTINGS_FILENAME = "caprmedio_project_settings.toml"
STRUCTURE_FILENAME = "project_structure.toml"
REGISTRY_FILENAME = "operators_registry.toml"
CONTROL_PREFIX = ".caprmedio_"
RUNTIME_DIRECTORY = Path(".caprmedio_runtime")
INSTALLATION_DIRECTORY = RUNTIME_DIRECTORY / "installation"
CONTEXTS_DIRECTORY = INSTALLATION_DIRECTORY / "contexts"
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


def _require_methodology_source_identities(value: object) -> tuple[str, ...]:
    if not isinstance(value, tuple) or not value:
        raise InstallationContextError("methodology_source_identities must be a non-empty tuple")
    if any(not isinstance(identity, str) or not identity for identity in value):
        raise InstallationContextError("methodology_source_identities must contain non-empty strings")
    if tuple(sorted(value)) != value or len(set(value)) != len(value):
        raise InstallationContextError("methodology_source_identities must be uniquely sorted")
    return value


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
    framework_instance_settings_sha256: str | None = None,
    source_catalog_sha256: str | None = None,
    methodology_source_identities: tuple[str, ...] | None = None,
) -> bytes:
    """Render the D600 digest preimage, excluding its self-digest carrier.

    The persisted context adds :data:`CONTEXT_DIGEST_FIELD` after these
    canonical bytes.  Both the target-context writer and installed-runtime
    reader use this one renderer so the file name, self-digest and selector
    always identify the same byte preimage.
    """

    schema_two = (
        framework_instance_settings_sha256 is not None
        or source_catalog_sha256 is not None
        or methodology_source_identities is not None
    )
    if schema_two:
        if (
            framework_instance_settings_sha256 is None
            or source_catalog_sha256 is None
            or methodology_source_identities is None
        ):
            raise InstallationContextError("schema 2 target context requires settings, catalog, and Methodology selection")
        framework_instance_settings_sha256 = _require_digest(
            framework_instance_settings_sha256, "framework_instance_settings_sha256"
        )
        source_catalog_sha256 = _require_digest(source_catalog_sha256, "source_catalog_sha256")
        methodology_source_identities = _require_methodology_source_identities(methodology_source_identities)
    lines = [
        f"schema_version = {2 if schema_two else 1}",
        f"mode = {_quoted(mode)}",
        f"target_project_identity = {_quoted(target_project_identity)}",
        f"control_child_relpath = {_quoted(control_child_relpath)}",
        f"settings_sha256 = {_quoted(settings_sha256)}",
        f"project_structure_sha256 = {_quoted(project_structure_sha256)}",
        f"registry_sha256 = {_quoted(registry_sha256)}",
    ]
    if schema_two:
        lines.extend(
            [
                f"framework_instance_settings_sha256 = {_quoted(framework_instance_settings_sha256)}",
                f"source_catalog_sha256 = {_quoted(source_catalog_sha256)}",
                "methodology_source_identities = ["
                + ", ".join(_quoted(identity) for identity in methodology_source_identities)
                + "]",
            ]
        )
    lines.extend(
        [
            (
            "repository_identity = false"
            if repository_identity is False
            else f"repository_identity = {_quoted(str(repository_identity))}"
            ),
            f"root_locator = {_quoted(root_locator)}",
        ]
    )
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
    path: str


@dataclass(frozen=True)
class VerifiedPackageEvidence:
    """Expected package identity and pins for a package-bound installer.

    This value alone grants no authority.  ``bind_target_project_context``
    reopens ``TargetProjectRequest.package_root`` through the package provider
    and compares the provider's evidence to these expected pinned values.
    ``selected_source_identities`` is retained only as a package-availability
    compatibility summary; D600v3 target applicability is exclusively
    ``TargetProjectContext.methodology_source_identities``.
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
    framework_instance_settings_sha256: str | None = None
    source_catalog_sha256: str | None = None
    methodology_source_identities: tuple[str, ...] = ()

    def toml_bytes(self) -> bytes:
        """Return canonical CA-D-600 bytes excluding the carrier digest itself."""
        framework_settings = _require_digest(
            self.framework_instance_settings_sha256, "framework_instance_settings_sha256"
        )
        source_catalog = _require_digest(self.source_catalog_sha256, "source_catalog_sha256")
        identities = _require_methodology_source_identities(self.methodology_source_identities)
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
            framework_instance_settings_sha256=framework_settings,
            source_catalog_sha256=source_catalog,
            methodology_source_identities=identities,
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
        root / ".caprmedio_install" / "current.toml",
        root / ".caprmedio_runtime" / "framework" / "current.toml",
        root / ".caprmedio_runtime" / "framework" / "releases",
        root / ".agents" / "skills" / "ca",
    )
    if any(path.exists() or path.is_symlink() for path in active):
        raise InstallationContextError("target has an active runtime boundary")


def _relative_directory(root: Path, relative: Path, *, create: bool) -> Path:
    """Return one real Project-contained directory without following aliases."""

    if relative.is_absolute() or not relative.parts or any(part in {"", ".", ".."} for part in relative.parts):
        raise InstallationContextError("target context directory is unsafe")
    cursor = root
    try:
        for part in relative.parts:
            cursor = cursor / part
            try:
                observed = cursor.lstat()
            except FileNotFoundError:
                if not create:
                    raise InstallationContextError("target context directory is unavailable")
                cursor.mkdir(mode=0o700)
                observed = cursor.lstat()
            if stat.S_ISLNK(observed.st_mode) or not stat.S_ISDIR(observed.st_mode):
                raise InstallationContextError("target context directory is aliased or invalid")
        return cursor
    except InstallationContextError:
        raise
    except OSError as error:
        raise InstallationContextError("target context directory is unavailable") from error


def _read_context_carrier(root: Path, digest: str) -> bytes:
    directory = _relative_directory(root, CONTEXTS_DIRECTORY, create=False)
    carrier = directory / f"{digest}.toml"
    try:
        observed = carrier.lstat()
        if stat.S_ISLNK(observed.st_mode) or not stat.S_ISREG(observed.st_mode) or observed.st_nlink != 1:
            raise InstallationContextError("target context carrier is aliased or invalid")
        before = (observed.st_dev, observed.st_ino, observed.st_size, observed.st_mtime_ns)
        payload = carrier.read_bytes()
        after = carrier.stat()
        if before != (after.st_dev, after.st_ino, after.st_size, after.st_mtime_ns):
            raise InstallationContextError("target context carrier changed while being reopened")
        return payload
    except InstallationContextError:
        raise
    except OSError as error:
        raise InstallationContextError("target context carrier is unavailable") from error


def _require_active_context_lock(lock: object, *, root: Path, context: TargetProjectContext) -> None:
    """Require the shared installation lock that owns mutable D600 publication."""

    try:
        from installation_transaction import InstallationPublicationLock, InstallationTransactionError
    except ImportError as error:  # pragma: no cover - protects isolated readers.
        raise InstallationContextError("installation publication lock is unavailable") from error
    if not isinstance(lock, InstallationPublicationLock):
        raise InstallationContextError("target context persistence requires the typed installation publication lock")
    if lock.project_root != root or lock.target_context_sha256 != context.sha256:
        raise InstallationContextError("installation publication lock does not bind this Project context")
    try:
        lock.revalidate()
    except InstallationTransactionError as error:
        raise InstallationContextError("installation publication lock is not current") from error


def _publish_context_carrier(root: Path, context: TargetProjectContext) -> Path:
    """Publish exact canonical bytes once, reusing only identical carriers."""

    directory = _relative_directory(root, CONTEXTS_DIRECTORY, create=True)
    payload = context.with_digest_toml()
    carrier = directory / f"{context.sha256}.toml"
    try:
        try:
            existing = carrier.lstat()
        except FileNotFoundError:
            existing = None
        if existing is not None:
            if stat.S_ISLNK(existing.st_mode) or not stat.S_ISREG(existing.st_mode) or existing.st_nlink != 1:
                raise InstallationContextError("target context carrier is aliased or invalid")
            if _read_context_carrier(root, context.sha256) != payload:
                raise InstallationContextError("target context carrier conflicts with the immutable context")
            return carrier
        descriptor, temporary_name = tempfile.mkstemp(prefix=".context-", dir=directory)
        temporary = Path(temporary_name)
        try:
            os.fchmod(descriptor, 0o600)
            with os.fdopen(descriptor, "wb", closefd=True) as stream:
                stream.write(payload)
                stream.flush()
                os.fsync(stream.fileno())
            try:
                os.link(temporary, carrier)
            except FileExistsError:
                if _read_context_carrier(root, context.sha256) != payload:
                    raise InstallationContextError("target context carrier conflicts with the immutable context")
            return carrier
        finally:
            temporary.unlink(missing_ok=True)
    except InstallationContextError:
        raise
    except OSError as error:
        raise InstallationContextError("target context carrier could not be published") from error


def reopen_target_project_context(
    request: TargetProjectRequest,
    *,
    expected_sha256: str,
) -> TargetProjectContext:
    """Reopen one persisted D600 context against current physical controls.

    The context carrier is not a substitute for its target controls or package:
    the request is rebound first, then the exact digest-named canonical bytes
    are compared with the retained carrier.
    """

    digest = _require_digest(expected_sha256, "expected target context")
    # A retained context is reopened both before staging and after a completed
    # installation.  Bootstrap emptiness is an admission precondition, not a
    # property that remains true once the admitted runtime exists.
    current = _bind_target_project_context(request, require_empty_bootstrap=False)
    if current.sha256 != digest:
        raise InstallationContextError("target context differs from current target controls")
    root = _canonical_root(request.target_root)
    if _read_context_carrier(root, digest) != current.with_digest_toml():
        raise InstallationContextError("target context carrier differs from current canonical context")
    return current


def persist_target_project_context(
    request: TargetProjectRequest,
    context: TargetProjectContext,
    *,
    lock: object,
) -> Path:
    """Write the one locked, immutable D600 context carrier.

    This is preparation only: it publishes no package selector, runtime
    selector, configuration, process observation, or deletion decision.
    """

    if not isinstance(context, TargetProjectContext):
        raise InstallationContextError("target context persistence requires a typed context")
    rebound = bind_target_project_context(request)
    if rebound != context:
        raise InstallationContextError("target context changed before persistence")
    root = _canonical_root(request.target_root)
    _require_active_context_lock(lock, root=root, context=context)
    carrier = _publish_context_carrier(root, context)
    _require_active_context_lock(lock, root=root, context=context)
    reopened = reopen_target_project_context(request, expected_sha256=context.sha256)
    if reopened != context or carrier != root / CONTEXTS_DIRECTORY / f"{context.sha256}.toml":
        raise InstallationContextError("persisted target context did not reopen exactly")
    _require_active_context_lock(lock, root=root, context=context)
    return carrier


def _bind_target_project_context(
    request: TargetProjectRequest,
    *,
    require_empty_bootstrap: bool,
) -> TargetProjectContext:
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
    try:
        from target_methodology_selection import TargetMethodologySelectionError, resolve_target_methodology_selection

        selection = resolve_target_methodology_selection(
            control_root=control,
            package_root=request.package_root,
            package_evidence=evidence,
        )
    except TargetMethodologySelectionError as error:
        raise InstallationContextError(str(error)) from error
    if require_empty_bootstrap and request.mode == "bootstrap":
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
        framework_instance_settings_sha256=selection.framework_instance_settings_sha256,
        source_catalog_sha256=selection.source_catalog_sha256,
        methodology_source_identities=selection.methodology_source_identities,
    )


def bind_target_project_context(request: TargetProjectRequest) -> TargetProjectContext:
    """Reopen and bind one requested Project with zero filesystem effects.

    A bootstrap admission is valid only before there is an active native or
    legacy runtime.  The retained-context reader intentionally uses the same
    control/package validation without reimposing that historical condition.
    """

    return _bind_target_project_context(request, require_empty_bootstrap=True)


__all__ = [
    "CONTEXT_DIGEST_FIELD",
    "CONTEXTS_DIRECTORY",
    "InstallationContextError",
    "PackageSourcePin",
    "TargetProjectContext",
    "TargetProjectRequest",
    "VerifiedPackageEvidence",
    "bind_target_project_context",
    "canonical_target_project_context_toml",
    "persist_target_project_context",
    "reopen_target_project_context",
]
