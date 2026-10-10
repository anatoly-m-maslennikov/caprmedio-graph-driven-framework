"""Physical, lock-owned helpers for native portable-runtime publication.

The helpers in this module intentionally do not create authority.  Their
callers must have reopened the CA-O-200 command and Full Gate before taking an
effect here.  They keep the destructive cut-over small: a verified candidate
is copied to a private content-addressed stage, and only that reopened stage
may replace the selected package.
"""
from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass, field
import errno
import hashlib
import json
import os
from pathlib import Path
import shutil
import stat
import tempfile
import tomllib

from framework_package import (
    CurrentPackageSelector,
    FrameworkPackageError,
    VerifiedFrameworkPackage,
    verify_current_package_selector,
    verify_framework_package,
)
from installation_context import TargetProjectContext
from installation_transaction import InstallationPublicationLock, InstallationTransactionError


_INSTALL_ROOT = Path(".caprmedio_install")
_RELEASES = _INSTALL_ROOT / "releases"
_PACKAGE_SELECTOR = _INSTALL_ROOT / "current.toml"
_RUNTIME_SELECTOR = Path(".caprmedio_runtime/installation/current.toml")
_LEGACY_RUNTIME_SELECTOR = Path(".caprmedio_runtime/framework/current.toml")
_GENERATIONS = Path(".caprmedio_runtime/installation/generations")
_STAGING = Path(".caprmedio_tmp/installation/replacements")
_CA_SKILL_STAGING = Path(".caprmedio_tmp/installation/ca-skill")
_CA_SKILL_TARGET = Path(".agents") / "skills" / "ca"
_CA_SKILL_EFFECT_STAGES = frozenset({"remove_prior_skill", "copy_candidate_skill"})
_SHA256 = frozenset("0123456789abcdef")
# A native predecessor handoff is not a serializable capability.  The token is
# checked at every effect-adjacent use so an object with the same documentary
# fields cannot authorize the sole old-Methodology freshness exception.
_NATIVE_PREDECESSOR_HANDOFF_TOKEN = object()


class PortableRuntimePublicationError(RuntimeError):
    """A native publication cannot safely advance."""

    def __init__(
        self,
        code: str,
        message: str,
        *,
        stage: str | None = None,
        os_errno: int | None = None,
        relative_path: str | None = None,
    ) -> None:
        self.code = code
        self.stage = stage
        self.os_errno = os_errno
        self.relative_path = relative_path
        diagnostic = ""
        if stage is not None:
            diagnostic = f"; stage={stage}; errno={os_errno!r}; path={relative_path}"
        super().__init__(f"{code}: {message}{diagnostic}")


@dataclass(frozen=True)
class PreparedNativePublication:
    """Non-authorizing, physically reopenable inputs for one final cut-over.

    A direct O-200 wrapper and a selected O-169 wrapper may construct this
    only after their *own* Action start/currentness path.  This value carries
    no Operator grant, session, callback, or Boolean pass flag: the shared
    publisher below reopens the candidate D604 proof (which in turn reopens
    the retained Full Gate) before an effect.
    """

    package: VerifiedFrameworkPackage
    target_context: TargetProjectContext
    candidate_proof_request: object
    candidate_proof: object
    methodology_delivery: object
    candidate_mcp_binding: object
    prospective_package_selector: bytes
    prospective_runtime_selector: bytes
    old_package_selector: bytes | None
    old_execution_selector: tuple[Path, bytes] | None
    # Native N is frozen independently of legacy state migration.  A normal
    # N->N replacement may own no D605 state roots at all, but still needs its
    # exact predecessor handoff after candidate Methodology publication.
    native_predecessor: "_NativePredecessorHandoff | None" = field(default=None, repr=False, compare=False)
    legacy_replacement: "LegacyReplacementPreparation | None" = None
    ca_skill_publication: "PreparedCaSkillPublication | None" = None


@dataclass(frozen=True, init=False)
class _NativePredecessorHandoff:
    """Frozen native-N evidence retained across candidate Methodology publication.

    An O169 candidate legitimately replaces the canonical Methodology delivery
    before the old N package is deleted.  The normal current-N reader remains
    strict; this private handoff instead retains the exact old binding and raw
    D598/D599 carriers from before that one permitted publication.  It is
    process-local evidence only, never a new persisted recovery surface.
    """

    binding: object = field(repr=False, compare=False)
    package_selector: bytes = field(repr=False, compare=False)
    runtime_selector: bytes = field(repr=False, compare=False)
    target_context_sha256: str
    state_generation: int
    prior_installation_lock_generation: str
    release_proof_sha256: str
    publication_lock_generation: str
    _capture_lock: InstallationPublicationLock = field(repr=False, compare=False)
    _predecessor_proof: object | None = field(default=None, repr=False, compare=False)
    _process_coverage: object | None = field(default=None, repr=False, compare=False)
    _native_quiescence: object | None = field(default=None, repr=False, compare=False)
    _factory_token: object = field(repr=False, compare=False)

    @classmethod
    def _create(
        cls,
        *,
        binding: object,
        package_selector: bytes,
        runtime_selector: bytes,
        target_context_sha256: str,
        state_generation: int,
        prior_installation_lock_generation: str,
        release_proof_sha256: str,
        publication_lock_generation: str,
        capture_lock: InstallationPublicationLock,
        predecessor_proof: object | None = None,
        process_coverage: object | None = None,
        native_quiescence: object | None = None,
    ) -> "_NativePredecessorHandoff":
        value = object.__new__(cls)
        object.__setattr__(value, "binding", binding)
        object.__setattr__(value, "package_selector", package_selector)
        object.__setattr__(value, "runtime_selector", runtime_selector)
        object.__setattr__(value, "target_context_sha256", target_context_sha256)
        object.__setattr__(value, "state_generation", state_generation)
        object.__setattr__(value, "prior_installation_lock_generation", prior_installation_lock_generation)
        object.__setattr__(value, "release_proof_sha256", release_proof_sha256)
        object.__setattr__(value, "publication_lock_generation", publication_lock_generation)
        object.__setattr__(value, "_capture_lock", capture_lock)
        object.__setattr__(value, "_predecessor_proof", predecessor_proof)
        object.__setattr__(value, "_process_coverage", process_coverage)
        object.__setattr__(value, "_native_quiescence", native_quiescence)
        object.__setattr__(value, "_factory_token", _NATIVE_PREDECESSOR_HANDOFF_TOKEN)
        return value

    def _with_coverage(self, predecessor_proof: object, process_coverage: object) -> "_NativePredecessorHandoff":
        if not _is_native_predecessor_handoff(self):
            _refuse(
                "portable-publication-native-handoff-invalid",
                "native predecessor coverage may only extend a publisher-minted handoff",
            )
        return self._create(
            binding=self.binding,
            package_selector=self.package_selector,
            runtime_selector=self.runtime_selector,
            target_context_sha256=self.target_context_sha256,
            state_generation=self.state_generation,
            prior_installation_lock_generation=self.prior_installation_lock_generation,
            release_proof_sha256=self.release_proof_sha256,
            publication_lock_generation=self.publication_lock_generation,
            capture_lock=self._capture_lock,
            predecessor_proof=predecessor_proof,
            process_coverage=process_coverage,
            native_quiescence=self._native_quiescence,
        )

    def _with_native_quiescence(self, native_quiescence: object) -> "_NativePredecessorHandoff":
        if not _is_native_predecessor_handoff(self):
            _refuse(
                "portable-publication-native-handoff-invalid",
                "native quiescence may only extend a publisher-minted handoff",
            )
        return self._create(
            binding=self.binding,
            package_selector=self.package_selector,
            runtime_selector=self.runtime_selector,
            target_context_sha256=self.target_context_sha256,
            state_generation=self.state_generation,
            prior_installation_lock_generation=self.prior_installation_lock_generation,
            release_proof_sha256=self.release_proof_sha256,
            publication_lock_generation=self.publication_lock_generation,
            capture_lock=self._capture_lock,
            predecessor_proof=self._predecessor_proof,
            process_coverage=self._process_coverage,
            native_quiescence=native_quiescence,
        )


def _is_native_predecessor_handoff(value: object) -> bool:
    """Return whether ``value`` was minted by the physical freeze boundary."""

    return (
        type(value) is _NativePredecessorHandoff
        and getattr(value, "_factory_token", None) is _NATIVE_PREDECESSOR_HANDOFF_TOKEN
    )


@dataclass(frozen=True)
class LegacyReplacementPreparation:
    """Retained, non-switching proof for one predecessor replacement.

    The three old runtime subtrees are copied only to the migration staging
    area using the existing D605--D607 evidence grammar.  The historical name
    remains for compatibility, but the same lower proof also freezes a native
    predecessor's owned Project state.  It deliberately carries no selector
    bytes to publish: new D598/D599 selectors remain the sole activation path.
    """

    migration_id: str
    inventory_sha256: str
    quiescence_sha256: str
    staged: Mapping[str, object]
    # The only typed predecessor identity accepted by D607.  It retains raw
    # native D600/selector carriers or the legacy bootstrap selector/receipt
    # closure; no later inventory parser may substitute scalar digests.
    predecessor_proof: object = field(repr=False, compare=False)
    # This is intentionally in-memory only.  Serialized inventory rows retain
    # the evidence snapshot, but only this still-open opaque value can prove
    # that no provider fence was released between preparation and cut-over.
    process_coverage: object = field(repr=False, compare=False)
    # Only native predecessors retain an N binding.  Legacy bootstrap
    # replacements instead retain their authenticated image proof.
    native_predecessor: _NativePredecessorHandoff | None = field(default=None, repr=False, compare=False)


@dataclass(frozen=True)
class PreparedCaSkillPublication:
    """Physical before/after evidence for the package-owned local ``ca`` Skill."""

    target: Path
    preparation_path: Path
    prior_tree_sha256: str | None
    candidate_tree_sha256: str
    package_manifest_sha256: str
    target_context_sha256: str


@dataclass(frozen=True)
class PublishedNativeRuntime:
    """Actual physical cut-over carriers; it asserts no Action outcome."""

    package: VerifiedFrameworkPackage
    generation_proof_path: Path
    package_selector_sha256: str
    runtime_selector_sha256: str
    installed_mcp_binding: object


@dataclass(frozen=True)
class DirectPublishedRuntime:
    """Physical O-200 result plus its separately recorded Journal state."""

    publication: PublishedNativeRuntime | None
    recording: dict[str, object]


def _refuse(code: str, message: str) -> None:
    raise PortableRuntimePublicationError(code, message)


def _digest(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def _sha256(value: object, *, label: str) -> str:
    if not isinstance(value, str) or len(value) != 64 or set(value) - _SHA256:
        _refuse("portable-publication-selector-invalid", f"{label} must be a lowercase SHA-256")
    return value


def _methodology_preparation_route(
    preparation: object,
    *,
    candidate_type: type[object],
    target_type: type[object],
) -> str:
    """Classify the only two lock-owned Methodology publication modes.

    The branch is intentionally type-only.  A direct O200 preparation must not
    be relabelled as a selected candidate merely because both eventually feed a
    prospective D604 proof.
    """

    if isinstance(preparation, candidate_type):
        return "candidate"
    if isinstance(preparation, target_type):
        return "target"
    _refuse("portable-publication-builder-invalid", "builder requires typed candidate or target Methodology preparation")
    raise AssertionError("unreachable")


def _quoted(value: str) -> str:
    return json.dumps(value, ensure_ascii=False)


def _root(lock: object) -> tuple[InstallationPublicationLock, Path]:
    if not isinstance(lock, InstallationPublicationLock):
        _refuse("portable-publication-lock-required", "native publication requires the concrete installation lock")
    try:
        lock.revalidate()
    except InstallationTransactionError as error:
        raise PortableRuntimePublicationError(
            "portable-publication-lock-invalid", "native publication lock is not active"
        ) from error
    root = lock.project_root
    try:
        observed = root.lstat()
    except OSError as error:
        raise PortableRuntimePublicationError("portable-publication-root-invalid", "target Project root is unavailable") from error
    if root.is_symlink() or not stat.S_ISDIR(observed.st_mode):
        _refuse("portable-publication-root-invalid", "target Project root is not a real directory")
    return lock, root


def _regular(path: Path, *, code: str) -> None:
    try:
        observed = path.lstat()
    except OSError as error:
        raise PortableRuntimePublicationError(code, f"carrier is unavailable: {path}") from error
    if path.is_symlink() or not stat.S_ISREG(observed.st_mode) or observed.st_nlink != 1:
        _refuse(code, f"carrier is unsafe: {path}")


def _directory(path: Path, *, code: str) -> None:
    try:
        observed = path.lstat()
    except OSError as error:
        raise PortableRuntimePublicationError(code, f"directory is unavailable: {path}") from error
    if path.is_symlink() or not stat.S_ISDIR(observed.st_mode):
        _refuse(code, f"directory is unsafe: {path}")


def _mkdirs(root: Path, relative: Path) -> Path:
    cursor = root
    for component in relative.parts:
        cursor /= component
        try:
            cursor.mkdir(mode=0o700)
        except FileExistsError:
            pass
        _directory(cursor, code="portable-publication-path-unsafe")
    return cursor


def _atomic_new(path: Path, payload: bytes, *, mode: int) -> None:
    _directory(path.parent, code="portable-publication-path-unsafe")
    if path.exists() or path.is_symlink():
        _refuse("portable-publication-write-conflict", f"refusing to replace existing carrier: {path}")
    temporary: Path | None = None
    try:
        descriptor, temporary_name = tempfile.mkstemp(prefix=f".{path.name}.", dir=path.parent)
        temporary = Path(temporary_name)
        with os.fdopen(descriptor, "wb") as stream:
            stream.write(payload)
            stream.flush()
            os.fsync(stream.fileno())
        temporary.chmod(mode)
        # A final carrier has no replacement semantics.  Link publication
        # provides O_EXCL-like behavior after the precheck, so a raced file
        # cannot be overwritten by this publisher.
        os.link(temporary, path, follow_symlinks=False)
        temporary.unlink()
        directory = os.open(path.parent, os.O_RDONLY | os.O_DIRECTORY)
        try:
            os.fsync(directory)
        finally:
            os.close(directory)
    except OSError as error:
        raise PortableRuntimePublicationError("portable-publication-write-failed", f"cannot publish {path.name}") from error
    finally:
        if temporary is not None:
            try:
                temporary.unlink(missing_ok=True)
            except OSError:
                pass


def _selected_native_package(root: Path, selector: bytes) -> VerifiedFrameworkPackage:
    """Reopen the exact native D598 selection before its tree is removed."""

    try:
        document = tomllib.loads(selector.decode("utf-8"))
        manifest = document.get("package_manifest_sha256") if isinstance(document, dict) else None
        digest = _sha256(manifest, label="current package manifest")
        package = verify_framework_package(root / _RELEASES / digest)
        verify_current_package_selector(selector, package)
    except (UnicodeDecodeError, tomllib.TOMLDecodeError, FrameworkPackageError, OSError, ValueError) as error:
        raise PortableRuntimePublicationError(
            "portable-publication-old-selector-invalid", "selected package cannot be physically reopened"
        ) from error
    return package


_LEGACY_FRAMEWORK_SELECTOR_FIELDS = (
    "schema_version",
    "manifest_sha256",
    "release",
    "selected_release_root",
    "framework_engine_root",
    "methodology_root",
    "image_digest",
)


def _legacy_release_directory(root: Path, release: str) -> Path:
    """Return one non-aliased historical Framework release directory."""

    relative = Path(".caprmedio_runtime") / "framework" / "releases" / release
    cursor = root
    for component in relative.parts:
        cursor /= component
        _directory(cursor, code="portable-publication-old-package-missing")
    return cursor


def _legacy_manifest_relative(value: object, *, label: str) -> Path:
    if not isinstance(value, str) or not value:
        _refuse("portable-publication-old-selector-invalid", f"legacy {label} is not a relative path")
    relative = Path(value)
    if relative.is_absolute() or any(part in {"", ".", ".."} for part in relative.parts):
        _refuse("portable-publication-old-selector-invalid", f"legacy {label} is unsafe")
    if any(part.lower().startswith(".env") for part in relative.parts):
        _refuse("portable-publication-old-selector-invalid", f"legacy {label} names a protected path")
    return relative


def _selected_legacy_framework_package(root: Path, selector: bytes) -> Path:
    """Reopen the historical Framework package named by a legacy selector.

    A legacy Framework selector is not a D598 selector: its identity is the
    digest of ``manifest.toml`` in the historical Framework release tree.  The
    complete closed selector, manifest digest and declared file inventory must
    all reopen before this publisher is allowed to remove that one tree.
    """

    try:
        document = tomllib.loads(selector.decode("utf-8"))
    except (UnicodeDecodeError, tomllib.TOMLDecodeError) as error:
        raise PortableRuntimePublicationError(
            "portable-publication-old-selector-invalid", "legacy Framework selector is not valid TOML"
        ) from error
    if not isinstance(document, dict) or tuple(document) != _LEGACY_FRAMEWORK_SELECTOR_FIELDS:
        _refuse("portable-publication-old-selector-invalid", "legacy Framework selector is not closed")
    if document.get("schema_version") != 1:
        _refuse("portable-publication-old-selector-invalid", "legacy Framework selector has an unsupported schema")
    release = _sha256(document.get("release"), label="legacy Framework release")
    if document.get("manifest_sha256") != release:
        _refuse("portable-publication-old-selector-invalid", "legacy Framework manifest is not bound to its release")
    image = document.get("image_digest")
    if not isinstance(image, str) or not image.startswith("sha256:"):
        _refuse("portable-publication-old-selector-invalid", "legacy Framework image digest is invalid")
    _sha256(image[7:], label="legacy Framework image")
    release_relative = Path(".caprmedio_runtime") / "framework" / "releases" / release
    if document.get("selected_release_root") != release_relative.as_posix():
        _refuse("portable-publication-old-selector-invalid", "legacy Framework release root is not exact")
    if document.get("framework_engine_root") != (release_relative / "FRAMEWORK_ENGINE").as_posix():
        _refuse("portable-publication-old-selector-invalid", "legacy Framework engine root is not exact")
    if document.get("methodology_root") != (release_relative / "METHODOLOGY").as_posix():
        _refuse("portable-publication-old-selector-invalid", "legacy Framework Methodology root is not exact")

    release_root = _legacy_release_directory(root, release)
    _directory(release_root / "FRAMEWORK_ENGINE", code="portable-publication-old-package-missing")
    _directory(release_root / "METHODOLOGY", code="portable-publication-old-package-missing")
    manifest_path = release_root / "manifest.toml"
    _regular(manifest_path, code="portable-publication-old-package-missing")
    try:
        manifest_bytes = manifest_path.read_bytes()
        manifest = tomllib.loads(manifest_bytes.decode("utf-8"))
    except (OSError, UnicodeDecodeError, tomllib.TOMLDecodeError) as error:
        raise PortableRuntimePublicationError(
            "portable-publication-old-selector-invalid", "legacy Framework manifest cannot be reopened"
        ) from error
    if _digest(manifest_bytes) != release:
        _refuse("portable-publication-old-selector-invalid", "legacy Framework manifest digest differs from selection")
    if not isinstance(manifest, dict):
        _refuse("portable-publication-old-selector-invalid", "legacy Framework manifest is not a table")
    base_fields = {"schema_version", "candidate_snapshot_manifest_sha256", "package", "files"}
    versioned_fields = base_fields | {"framework_version", "version_toml_sha256"}
    manifest_fields = set(manifest)
    if manifest_fields != base_fields and manifest_fields != versioned_fields:
        _refuse("portable-publication-old-selector-invalid", "legacy Framework manifest has an unknown shape")
    if manifest.get("schema_version") != 2 or manifest.get("package") != "caprmedio-framework":
        _refuse("portable-publication-old-selector-invalid", "legacy Framework manifest identity is invalid")
    _sha256(manifest.get("candidate_snapshot_manifest_sha256"), label="legacy Framework candidate")
    if manifest_fields == versioned_fields:
        if not isinstance(manifest.get("framework_version"), str) or not manifest["framework_version"]:
            _refuse("portable-publication-old-selector-invalid", "legacy Framework version is invalid")
        _sha256(manifest.get("version_toml_sha256"), label="legacy Framework version.toml")
    rows = manifest.get("files")
    if not isinstance(rows, list) or not rows:
        _refuse("portable-publication-old-selector-invalid", "legacy Framework manifest has no file inventory")
    expected_paths = {"manifest.toml"}
    for row in rows:
        if not isinstance(row, dict) or set(row) != {"resource", "source_path", "destination", "sha256", "mode"}:
            _refuse("portable-publication-old-selector-invalid", "legacy Framework file row is invalid")
        if not isinstance(row.get("resource"), str) or not row["resource"]:
            _refuse("portable-publication-old-selector-invalid", "legacy Framework file resource is invalid")
        _legacy_manifest_relative(row.get("source_path"), label="source path")
        destination = _legacy_manifest_relative(row.get("destination"), label="destination")
        if destination.as_posix() in expected_paths:
            _refuse("portable-publication-old-selector-invalid", "legacy Framework inventory repeats a file")
        expected_paths.add(destination.as_posix())
        expected_digest = _sha256(row.get("sha256"), label="legacy Framework file")
        mode = row.get("mode")
        if isinstance(mode, bool) or not isinstance(mode, int) or not 0 <= mode <= 0o777:
            _refuse("portable-publication-old-selector-invalid", "legacy Framework file mode is invalid")
        carrier = release_root / destination
        _regular(carrier, code="portable-publication-old-package-missing")
        try:
            payload = carrier.read_bytes()
            actual_mode = carrier.stat().st_mode & 0o777
        except OSError as error:
            raise PortableRuntimePublicationError(
                "portable-publication-old-package-missing", "legacy Framework file cannot be reopened"
            ) from error
        if _digest(payload) != expected_digest or actual_mode != mode:
            _refuse("portable-publication-old-selector-invalid", "legacy Framework file differs from its inventory")

    actual_paths: set[str] = set()
    try:
        for carrier in release_root.rglob("*"):
            relative = carrier.relative_to(release_root)
            if any(part.lower().startswith(".env") for part in relative.parts):
                _refuse("portable-publication-old-selector-invalid", "legacy Framework package contains a protected path")
            if carrier.is_symlink():
                _refuse("portable-publication-old-selector-invalid", "legacy Framework package contains a symlink")
            if carrier.is_dir():
                continue
            if not carrier.is_file():
                _refuse("portable-publication-old-selector-invalid", "legacy Framework package contains a special carrier")
            if carrier.name == ".DS_Store":
                continue
            actual_paths.add(relative.as_posix())
    except OSError as error:
        raise PortableRuntimePublicationError(
            "portable-publication-old-selector-invalid", "legacy Framework package cannot be inventoried"
        ) from error
    if actual_paths != expected_paths:
        _refuse("portable-publication-old-selector-invalid", "legacy Framework package inventory differs from its manifest")
    return release_root


def _verify_legacy_tools_selection(root: Path) -> None:
    """Require the old tools selector to remain an actual verified legacy install."""

    try:
        from framework_installation import InstallationError, installation_status

        status = installation_status(root)
    except (ImportError, OSError, RuntimeError) as error:
        raise PortableRuntimePublicationError(
            "portable-publication-old-selector-invalid", "legacy tools installation cannot be physically reopened"
        ) from error
    if not isinstance(status, dict) or status.get("installed") is not True or status.get("verified") is not True:
        _refuse("portable-publication-old-selector-invalid", "legacy tools installation is not verified")


def render_package_selector(
    package: VerifiedFrameworkPackage,
    *,
    full_gate_receipt_sha256: str,
    image_digest: str,
) -> bytes:
    """Render closed prospective CA-D-598 selector bytes for one package."""

    if not isinstance(package, VerifiedFrameworkPackage):
        _refuse("portable-publication-package-invalid", "package must be a typed verified package")
    try:
        reopened = verify_framework_package(package.root)
    except FrameworkPackageError as error:
        raise PortableRuntimePublicationError("portable-publication-package-invalid", "candidate package cannot be reopened") from error
    if reopened != package:
        _refuse("portable-publication-package-stale", "candidate package differs from physical bytes")
    receipt = _sha256(full_gate_receipt_sha256, label="Full Gate receipt")
    image = _sha256(image_digest, label="image digest")
    values = (
        ("schema_version", "1"),
        ("package_manifest_sha256", _quoted(package.manifest_digest)),
        ("release_relpath", _quoted(f"releases/{package.manifest_digest}")),
        ("framework_version", _quoted(package.framework_version)),
        ("version_toml_sha256", _quoted(package.version_toml_sha256)),
        ("source_catalog_sha256", _quoted(package.source_catalog_sha256)),
        ("full_gate_receipt_sha256", _quoted(receipt)),
        ("image_digest", _quoted(image)),
    )
    return ("\n".join(f"{key} = {value}" for key, value in values) + "\n").encode("utf-8")


def render_runtime_selector(
    package: VerifiedFrameworkPackage,
    context: TargetProjectContext,
    *,
    state_generation: int,
    installation_lock_generation: str,
    image_digest: str,
) -> bytes:
    """Render closed prospective CA-D-599 selector bytes without publishing."""

    if not isinstance(package, VerifiedFrameworkPackage) or not isinstance(context, TargetProjectContext):
        _refuse("portable-publication-selector-invalid", "selector requires typed package and context")
    if isinstance(state_generation, bool) or not isinstance(state_generation, int) or state_generation < 1:
        _refuse("portable-publication-selector-invalid", "state generation must be a positive integer")
    if not isinstance(installation_lock_generation, str) or len(installation_lock_generation) != 32 or set(installation_lock_generation) - _SHA256:
        _refuse("portable-publication-selector-invalid", "installation lock generation is invalid")
    image = _sha256(image_digest, label="image digest")
    values = (
        ("schema_version", "1"),
        ("package_manifest_sha256", _quoted(package.manifest_digest)),
        ("target_project_context_sha256", _quoted(context.sha256)),
        ("state_generation", str(state_generation)),
        ("installation_lock_generation", _quoted(installation_lock_generation)),
        ("image_digest", _quoted(image)),
    )
    return ("\n".join(f"{key} = {value}" for key, value in values) + "\n").encode("utf-8")


def stage_replacement_package(package: VerifiedFrameworkPackage, *, lock: InstallationPublicationLock) -> VerifiedFrameworkPackage:
    """Copy and reopen a candidate package under a private lock-generation stage."""

    concrete_lock, root = _root(lock)
    if not isinstance(package, VerifiedFrameworkPackage):
        _refuse("portable-publication-package-invalid", "replacement requires a typed verified package")
    try:
        source = verify_framework_package(package.root)
    except FrameworkPackageError as error:
        raise PortableRuntimePublicationError("portable-publication-package-invalid", "candidate package cannot be reopened") from error
    if source != package:
        _refuse("portable-publication-package-stale", "candidate package differs from physical bytes")
    try:
        package.root.resolve(strict=True).relative_to(root.resolve(strict=True))
    except (OSError, ValueError) as error:
        raise PortableRuntimePublicationError("portable-publication-package-foreign", "candidate package escapes target Project") from error
    parent = _mkdirs(root, _STAGING / concrete_lock.lock_generation)
    target = parent / package.manifest_digest
    if target.exists() or target.is_symlink():
        _refuse("portable-publication-stage-conflict", "replacement stage already exists")
    try:
        target.mkdir(mode=0o700)
        for row in package.inventory:
            relative = Path(row.path)
            source_path = package.root / relative
            _regular(source_path, code="portable-publication-package-stale")
            payload = source_path.read_bytes()
            if _digest(payload) != row.sha256 or source_path.stat().st_mode & 0o777 != row.mode:
                _refuse("portable-publication-package-stale", f"candidate member changed: {row.path}")
            destination = target / relative
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_bytes(payload)
            destination.chmod(row.mode)
        manifest = package.root / "manifest.toml"
        _regular(manifest, code="portable-publication-package-stale")
        (target / "manifest.toml").write_bytes(manifest.read_bytes())
        (target / "manifest.toml").chmod(0o644)
        staged = verify_framework_package(target)
    except FrameworkPackageError as error:
        raise PortableRuntimePublicationError("portable-publication-stage-invalid", "staged package cannot be reopened") from error
    except OSError as error:
        raise PortableRuntimePublicationError("portable-publication-stage-failed", "cannot stage replacement package") from error
    if staged.manifest_digest != package.manifest_digest or staged.inventory != package.inventory:
        _refuse("portable-publication-stage-invalid", "staged package differs from candidate")
    concrete_lock.revalidate()
    return staged


def _ca_skill_records(directory: Path) -> tuple[tuple[str, str, int], ...]:
    """Inventory one local ``ca`` Skill without following aliases."""

    _directory(directory, code="portable-publication-ca-skill-invalid")
    records: list[tuple[str, str, int]] = []
    try:
        for carrier in sorted(directory.rglob("*"), key=lambda item: item.relative_to(directory).as_posix()):
            relative = carrier.relative_to(directory)
            if any(part.lower().startswith(".env") for part in relative.parts):
                _refuse("portable-publication-ca-skill-invalid", "ca Skill contains a protected path")
            if carrier.is_symlink():
                _refuse("portable-publication-ca-skill-invalid", "ca Skill contains a symlink")
            if carrier.is_dir():
                continue
            if not carrier.is_file() or carrier.name == ".DS_Store":
                if carrier.name == ".DS_Store" and carrier.is_file():
                    continue
                _refuse("portable-publication-ca-skill-invalid", "ca Skill contains a special carrier")
            _regular(carrier, code="portable-publication-ca-skill-invalid")
            records.append((relative.as_posix(), _digest(carrier.read_bytes()), carrier.stat().st_mode & 0o777))
    except OSError as error:
        raise PortableRuntimePublicationError(
            "portable-publication-ca-skill-invalid", "ca Skill cannot be physically reopened"
        ) from error
    return tuple(records)


def _ca_skill_digest(records: tuple[tuple[str, str, int], ...]) -> str:
    return _digest(json.dumps(records, ensure_ascii=False, separators=(",", ":")).encode("utf-8"))


def _candidate_ca_skill_records(
    package: VerifiedFrameworkPackage,
    candidate_mcp_binding: object,
) -> tuple[tuple[str, str, int], ...]:
    """Read exactly the ``SKILLS/ca`` inventory already admitted for MCP."""

    members = getattr(candidate_mcp_binding, "package_ca_skill", None)
    if not isinstance(members, tuple) or not members:
        _refuse("portable-publication-ca-skill-invalid", "candidate MCP binding has no canonical ca Skill")
    prefix = "SKILLS/ca/"
    records: list[tuple[str, str, int]] = []
    for member in members:
        path, digest, mode = getattr(member, "path", None), getattr(member, "sha256", None), getattr(member, "mode", None)
        if (
            not isinstance(path, str) or not path.startswith(prefix) or path == prefix
            or not isinstance(mode, int) or isinstance(mode, bool) or not 0 <= mode <= 0o777
        ):
            _refuse("portable-publication-ca-skill-invalid", "candidate MCP ca Skill member is invalid")
        digest = _sha256(digest, label="candidate ca Skill member")
        relative = Path(path.removeprefix(prefix))
        if relative == Path(".") or relative.is_absolute() or any(part in {"", ".", ".."} for part in relative.parts):
            _refuse("portable-publication-ca-skill-invalid", "candidate MCP ca Skill path is unsafe")
        carrier = package.root / Path(path)
        _regular(carrier, code="portable-publication-ca-skill-invalid")
        try:
            payload = carrier.read_bytes()
        except OSError as error:
            raise PortableRuntimePublicationError(
                "portable-publication-ca-skill-invalid", "candidate MCP ca Skill member is unavailable"
            ) from error
        if _digest(payload) != digest or carrier.stat().st_mode & 0o777 != mode:
            _refuse("portable-publication-ca-skill-invalid", "candidate MCP ca Skill differs from package inventory")
        records.append((relative.as_posix(), digest, mode))
    records.sort()
    if not records or records[0][0] != "SKILL.md" or len({record[0] for record in records}) != len(records):
        _refuse("portable-publication-ca-skill-invalid", "candidate MCP ca Skill inventory is incomplete")
    return tuple(records)


def _ca_skill_evidence_payload(
    *,
    lock: InstallationPublicationLock,
    package: VerifiedFrameworkPackage,
    target_context: TargetProjectContext,
    prior: tuple[tuple[str, str, int], ...] | None,
    candidate: tuple[tuple[str, str, int], ...],
) -> bytes:
    payload = {
        "schema_version": 1,
        "installation_lock_generation": lock.lock_generation,
        "package_manifest_sha256": package.manifest_digest,
        "target_project_context_sha256": target_context.sha256,
        "prior_tree_sha256": _ca_skill_digest(prior) if prior is not None else None,
        "candidate_tree_sha256": _ca_skill_digest(candidate),
        "prior_files": [list(record) for record in prior] if prior is not None else [],
        "candidate_files": [list(record) for record in candidate],
    }
    return json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False).encode("utf-8")


def _ca_skill_effect_failure(stage: str, error: OSError) -> PortableRuntimePublicationError:
    """Retain only the known target and original OS error for a live cut-over stop."""

    if stage not in _CA_SKILL_EFFECT_STAGES:
        raise AssertionError("unknown ca Skill replacement stage")
    os_errno = error.errno
    if isinstance(os_errno, bool) or not isinstance(os_errno, int):
        os_errno = None
    return PortableRuntimePublicationError(
        "portable-publication-ca-skill-failed",
        "local ca Skill replacement stopped with retained preparation",
        stage=stage,
        os_errno=os_errno,
        relative_path=_CA_SKILL_TARGET.as_posix(),
    )


def _prepare_and_publish_ca_skill(
    root: Path,
    *,
    package: VerifiedFrameworkPackage,
    target_context: TargetProjectContext,
    candidate_mcp_binding: object,
    lock: InstallationPublicationLock,
) -> PreparedCaSkillPublication:
    """Stage, retain and replace the package-admitted local ``.agents`` Skill.

    This is intentionally before the final selector publication.  A stopped
    transaction therefore retains the old and candidate trees plus their
    lock-bound evidence instead of claiming a selector-based activation.
    """

    concrete_lock, checked_root = _root(lock)
    if checked_root != root:
        _refuse("portable-publication-ca-skill-invalid", "ca Skill target differs from installation lock")
    candidate = _candidate_ca_skill_records(package, candidate_mcp_binding)
    source = package.root / "SKILLS" / "ca"
    _directory(source, code="portable-publication-ca-skill-invalid")
    if _ca_skill_records(source) != candidate:
        _refuse("portable-publication-ca-skill-invalid", "package ca Skill tree differs from MCP inventory")
    _mkdirs(root, _CA_SKILL_TARGET.parent)
    target = root / _CA_SKILL_TARGET
    prior: tuple[tuple[str, str, int], ...] | None = None
    if target.exists() or target.is_symlink():
        _directory(target, code="portable-publication-ca-skill-invalid")
        prior = _ca_skill_records(target)
    stage_root = _mkdirs(root, _CA_SKILL_STAGING / concrete_lock.lock_generation)
    if any((stage_root / name).exists() or (stage_root / name).is_symlink() for name in ("candidate", "prior", "preparation.json")):
        _refuse("portable-publication-ca-skill-conflict", "ca Skill preparation already exists for this lock")
    candidate_stage = stage_root / "candidate"
    prior_stage = stage_root / "prior"
    try:
        shutil.copytree(source, candidate_stage, copy_function=shutil.copy2)
        if _ca_skill_records(candidate_stage) != candidate:
            _refuse("portable-publication-ca-skill-invalid", "staged candidate ca Skill differs from package inventory")
        if prior is not None:
            shutil.copytree(target, prior_stage, copy_function=shutil.copy2)
            if _ca_skill_records(prior_stage) != prior:
                _refuse("portable-publication-ca-skill-invalid", "staged prior ca Skill differs from active tree")
        evidence = _ca_skill_evidence_payload(
            lock=concrete_lock, package=package, target_context=target_context, prior=prior, candidate=candidate,
        )
        _atomic_new(stage_root / "preparation.json", evidence, mode=0o600)
        _regular(stage_root / "preparation.json", code="portable-publication-ca-skill-invalid")
        if (stage_root / "preparation.json").read_bytes() != evidence:
            _refuse("portable-publication-ca-skill-invalid", "retained ca Skill preparation differs from staged evidence")
        concrete_lock.revalidate()
        if target.exists() or target.is_symlink():
            if prior is None or _ca_skill_records(target) != prior:
                _refuse("portable-publication-ca-skill-stale", "active ca Skill changed before replacement")
            try:
                shutil.rmtree(target)
            except OSError as error:
                raise _ca_skill_effect_failure("remove_prior_skill", error) from error
        try:
            shutil.copytree(candidate_stage, target, copy_function=shutil.copy2)
        except OSError as error:
            raise _ca_skill_effect_failure("copy_candidate_skill", error) from error
        if _ca_skill_records(target) != candidate:
            _refuse("portable-publication-ca-skill-invalid", "published ca Skill differs from candidate package")
    except PortableRuntimePublicationError:
        raise
    except OSError as error:
        raise PortableRuntimePublicationError(
            "portable-publication-ca-skill-failed", "local ca Skill replacement stopped with retained preparation"
        ) from error
    concrete_lock.revalidate()
    return PreparedCaSkillPublication(
        target=target,
        preparation_path=stage_root / "preparation.json",
        prior_tree_sha256=_ca_skill_digest(prior) if prior is not None else None,
        candidate_tree_sha256=_ca_skill_digest(candidate),
        package_manifest_sha256=package.manifest_digest,
        target_context_sha256=target_context.sha256,
    )


def _revalidate_ca_skill_publication(prepared: PreparedNativePublication, *, lock: InstallationPublicationLock) -> None:
    """Require retained prior evidence and exact candidate local Skill pre-delete."""

    concrete_lock, root = _root(lock)
    evidence = prepared.ca_skill_publication
    if not isinstance(evidence, PreparedCaSkillPublication):
        _refuse("portable-publication-ca-skill-missing", "prepared publication has no retained local ca Skill evidence")
    target = root / ".agents" / "skills" / "ca"
    expected_preparation = root / _CA_SKILL_STAGING / concrete_lock.lock_generation / "preparation.json"
    if (
        evidence.target != target or evidence.preparation_path != expected_preparation
        or evidence.package_manifest_sha256 != prepared.package.manifest_digest
        or evidence.target_context_sha256 != prepared.target_context.sha256
    ):
        _refuse("portable-publication-ca-skill-stale", "ca Skill evidence is not bound to this prepared publication")
    _regular(expected_preparation, code="portable-publication-ca-skill-stale")
    try:
        payload = expected_preparation.read_bytes()
        document = json.loads(payload.decode("utf-8"))
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as error:
        raise PortableRuntimePublicationError(
            "portable-publication-ca-skill-stale", "retained ca Skill evidence cannot be reopened"
        ) from error
    if not isinstance(document, dict) or payload != json.dumps(
        document, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False
    ).encode("utf-8"):
        _refuse("portable-publication-ca-skill-stale", "retained ca Skill evidence is not canonical")
    candidate = _candidate_ca_skill_records(prepared.package, prepared.candidate_mcp_binding)
    # The prior tree is opaque at this point; compare its already-retained
    # digest/list separately, then reconstruct the complete canonical record.
    prior_rows = document.get("prior_files")
    if not isinstance(prior_rows, list):
        _refuse("portable-publication-ca-skill-stale", "retained prior ca Skill inventory is invalid")
    prior = tuple((row[0], row[1], row[2]) for row in prior_rows if isinstance(row, list) and len(row) == 3)
    if len(prior) != len(prior_rows) or any(
        not isinstance(path, str) or not isinstance(digest, str) or not isinstance(mode, int)
        for path, digest, mode in prior
    ):
        _refuse("portable-publication-ca-skill-stale", "retained prior ca Skill inventory is invalid")
    prior_value = None if document.get("prior_tree_sha256") is None else prior
    expected_payload = _ca_skill_evidence_payload(
        lock=concrete_lock, package=prepared.package, target_context=prepared.target_context,
        prior=prior_value, candidate=candidate,
    )
    if payload != expected_payload or evidence.prior_tree_sha256 != (
        _ca_skill_digest(prior_value) if prior_value is not None else None
    ):
        _refuse("portable-publication-ca-skill-stale", "retained ca Skill evidence differs from its lock-bound trees")
    if evidence.candidate_tree_sha256 != _ca_skill_digest(candidate) or _ca_skill_records(target) != candidate:
        _refuse("portable-publication-ca-skill-stale", "local ca Skill differs from the candidate package")
    concrete_lock.revalidate()


def publish_final_generation_proof(
    proof_request: object,
    proof: object,
    *,
    lock: InstallationPublicationLock,
) -> Path:
    """Copy one freshly reopened candidate D604 proof to its retained generation.

    The copy is deliberately non-activating: it happens before the destructive
    transition and before either selector becomes current.  The source proof is
    re-read through its candidate reader immediately before copying, so a
    caller cannot promote a once-valid typed handoff after its candidate,
    context, command stage, prospective selectors, or retained Full Gate has
    changed.
    """

    concrete_lock, root = _root(lock)
    try:
        from native_installation_proof import (
            CandidateNativeInstallationProofRequest,
            NativeInstallationProof,
            NativeInstallationProofError,
            read_candidate_native_installation_proof,
        )
    except ImportError as error:  # pragma: no cover - package routing failure.
        raise PortableRuntimePublicationError(
            "portable-publication-proof-unavailable", "candidate D604 proof reader is unavailable"
        ) from error
    if not isinstance(proof_request, CandidateNativeInstallationProofRequest) or not isinstance(proof, NativeInstallationProof):
        _refuse("portable-publication-proof-invalid", "final proof requires typed candidate proof inputs")
    try:
        reopened = read_candidate_native_installation_proof(proof_request, lock=concrete_lock)
    except NativeInstallationProofError as error:
        raise PortableRuntimePublicationError(
            "portable-publication-proof-invalid", "candidate D604 proof cannot be physically reopened"
        ) from error
    if reopened != proof:
        _refuse("portable-publication-proof-stale", "candidate D604 proof differs from its physical carriers")
    if reopened.installation_lock_generation != concrete_lock.lock_generation:
        _refuse("portable-publication-proof-invalid", "candidate proof belongs to another installation lock")
    if reopened.installation_command_sha256 != concrete_lock.command_sha256:
        _refuse("portable-publication-proof-invalid", "candidate proof belongs to another installation command")
    _regular(reopened.selector_path, code="portable-publication-proof-invalid")
    _regular(reopened.proof_path, code="portable-publication-proof-invalid")
    try:
        runtime_selector = reopened.selector_path.read_bytes()
        proof_payload = reopened.proof_path.read_bytes()
    except OSError as error:
        raise PortableRuntimePublicationError(
            "portable-publication-proof-invalid", "candidate D604 proof carriers are unavailable"
        ) from error
    if _digest(runtime_selector) != reopened.selector_sha256:
        _refuse("portable-publication-proof-invalid", "candidate selector bytes differ from the retained proof")
    command_stage = proof_request.command_stage
    try:
        from portable_runtime_materialization import RuntimeCommandStage
    except ImportError as error:  # pragma: no cover - package routing failure.
        raise PortableRuntimePublicationError(
            "portable-publication-command-stage-unavailable", "candidate D601 command-stage reader is unavailable"
        ) from error
    if not isinstance(command_stage, RuntimeCommandStage):
        _refuse("portable-publication-proof-invalid", "candidate proof has no typed D601 command stage")
    if (
        command_stage.lock_generation != concrete_lock.lock_generation
        or command_stage.state_generation != reopened.state_generation
        or command_stage.package_manifest_sha256 != reopened.package_manifest_sha256
        or command_stage.target_project_context_sha256 != reopened.target_project_context_sha256
        or command_stage.command_sha256 != reopened.command_sha256
    ):
        _refuse("portable-publication-proof-invalid", "candidate D601 command stage differs from D604 proof")
    _regular(command_stage.manifest_path, code="portable-publication-proof-invalid")
    try:
        stage_manifest_payload = command_stage.manifest_path.read_bytes()
        stage_manifest = tomllib.loads(stage_manifest_payload.decode("utf-8"))
    except (OSError, UnicodeDecodeError, tomllib.TOMLDecodeError) as error:
        raise PortableRuntimePublicationError(
            "portable-publication-proof-invalid", "candidate D601 stage manifest is unavailable"
        ) from error
    if _digest(stage_manifest_payload) != reopened.command_stage_manifest_sha256:
        _refuse("portable-publication-proof-invalid", "candidate D601 stage manifest differs from D604 proof")
    rows = stage_manifest.get("files") if isinstance(stage_manifest, dict) else None
    if (
        not isinstance(rows, list)
        or stage_manifest.get("schema_version") != 1
        or stage_manifest.get("package_manifest_sha256") != reopened.package_manifest_sha256
        or stage_manifest.get("target_project_context_sha256") != reopened.target_project_context_sha256
        or stage_manifest.get("state_generation") != reopened.state_generation
        or stage_manifest.get("lock_generation") != concrete_lock.lock_generation
    ):
        _refuse("portable-publication-proof-invalid", "candidate D601 stage manifest is not bound to this proof")
    raw_digests: dict[str, str] = {}
    raw_modes: dict[str, int] = {}
    for row in rows:
        if not isinstance(row, dict) or set(row) != {"path", "mode", "sha256"}:
            _refuse("portable-publication-proof-invalid", "candidate D601 stage inventory row is invalid")
        path, mode, digest = row.get("path"), row.get("mode"), row.get("sha256")
        if not isinstance(path, str) or path in raw_digests or path not in {"command.toml", "environment.toml", "wrapper"}:
            _refuse("portable-publication-proof-invalid", "candidate D601 stage inventory paths are invalid")
        if isinstance(mode, bool) or not isinstance(mode, int) or mode not in {0o600, 0o700}:
            _refuse("portable-publication-proof-invalid", "candidate D601 stage inventory mode is invalid")
        raw_digests[str(path)] = _sha256(digest, label="candidate D601 stage carrier")
        raw_modes[str(path)] = mode
    if set(raw_digests) != {"command.toml", "environment.toml", "wrapper"}:
        _refuse("portable-publication-proof-invalid", "candidate D601 stage inventory is incomplete")
    if (
        raw_modes != {"command.toml": 0o600, "environment.toml": 0o600, "wrapper": 0o700}
        or raw_digests["wrapper"] != command_stage.wrapper_sha256
    ):
        _refuse("portable-publication-proof-invalid", "candidate D601 stage inventory differs from typed stage")
    generation = str(reopened.state_generation)
    final_root = _mkdirs(root, _GENERATIONS / generation)
    stage_files = (
        ("command.toml", command_stage.command_path, 0o600, raw_digests["command.toml"]),
        ("environment.toml", command_stage.environment_path, 0o600, raw_digests["environment.toml"]),
        ("wrapper", command_stage.wrapper_path, 0o700, raw_digests["wrapper"]),
        ("stage-manifest.toml", command_stage.manifest_path, 0o600, reopened.command_stage_manifest_sha256),
    )
    for name, source, mode, expected_digest in stage_files:
        _regular(source, code="portable-publication-proof-invalid")
        try:
            payload = source.read_bytes()
        except OSError as error:
            raise PortableRuntimePublicationError(
                "portable-publication-proof-invalid", "candidate D601 stage carrier is unavailable"
            ) from error
        if _digest(payload) != expected_digest or source.stat().st_mode & 0o777 != mode:
            _refuse("portable-publication-proof-invalid", f"candidate D601 {name} differs from retained proof")
        target = final_root / name
        _atomic_new(target, payload, mode=mode)
        _regular(target, code="portable-publication-generation-invalid")
        if target.read_bytes() != payload or target.stat().st_mode & 0o777 != mode:
            _refuse("portable-publication-generation-invalid", f"retained D601 {name} differs from candidate stage")
    final_proof = final_root / "release-proof.toml"
    if final_proof.exists() or final_proof.is_symlink():
        _refuse("portable-publication-generation-conflict", "native generation already has a retained release proof")
    _atomic_new(final_proof, proof_payload, mode=0o600)
    _regular(final_proof, code="portable-publication-generation-invalid")
    if final_proof.read_bytes() != proof_payload:
        _refuse("portable-publication-generation-invalid", "retained release proof differs from candidate proof bytes")
    concrete_lock.revalidate()
    return final_proof


def _reopen_native_predecessor_context(
    root: Path,
    *,
    package_selector: bytes,
    runtime_selector: bytes,
) -> tuple[object, object]:
    """Return a native predecessor's physically re-opened D607 proof.

    D607 coverage is not allowed to bind a prospective context to a prior
    runtime.  The predecessor must therefore reopen its original concrete
    Full-Gate packet through its recorded O200/O169 completion and then pass
    the complete D598/D599/D604 reader.  A selector digest is never a packet
    locator or a substitute for command/stage/Methodology carrier bytes.
    """

    try:
        from installed_mcp_binding import _RUNTIME_SELECTOR_KEYS
    except ImportError as error:  # pragma: no cover - package routing failure.
        raise PortableRuntimePublicationError(
            "portable-publication-native-prior-unavailable",
            "native predecessor readers are unavailable",
        ) from error
    try:
        runtime_document = tomllib.loads(runtime_selector.decode("utf-8"))
    except (UnicodeDecodeError, tomllib.TOMLDecodeError) as error:
        raise PortableRuntimePublicationError(
            "portable-publication-native-prior-invalid",
            "native predecessor runtime selector is not valid TOML",
        ) from error
    if not isinstance(runtime_document, dict) or set(runtime_document) != _RUNTIME_SELECTOR_KEYS:
        _refuse("portable-publication-native-prior-invalid", "native predecessor runtime selector is not closed")
    if runtime_document.get("schema_version") != 1:
        _refuse("portable-publication-native-prior-invalid", "native predecessor runtime selector schema is unsupported")
    context_sha256 = runtime_document.get("target_project_context_sha256")
    generation = runtime_document.get("state_generation")
    if not isinstance(context_sha256, str) or len(context_sha256) != 64 or set(context_sha256) - _SHA256:
        _refuse("portable-publication-native-prior-invalid", "native predecessor context digest is invalid")
    if isinstance(generation, bool) or not isinstance(generation, int) or generation < 1:
        _refuse("portable-publication-native-prior-invalid", "native predecessor state generation is invalid")
    package_path = root / _PACKAGE_SELECTOR
    runtime_path = root / _RUNTIME_SELECTOR
    _regular(package_path, code="portable-publication-native-prior-invalid")
    _regular(runtime_path, code="portable-publication-native-prior-invalid")
    if package_path.read_bytes() != package_selector or runtime_path.read_bytes() != runtime_selector:
        _refuse("portable-publication-native-prior-invalid", "native predecessor selectors changed while reopening")
    package = _selected_native_package(root, package_selector)
    try:
        selected_package = verify_current_package_selector(package_selector, package)
    except FrameworkPackageError as error:  # Defensive: reopen both D598 readers.
        raise PortableRuntimePublicationError(
            "portable-publication-native-prior-invalid",
            "native predecessor package selector cannot be physically reopened",
        ) from error
    proof_path = root / _GENERATIONS / str(generation) / "release-proof.toml"
    try:
        from native_selected_installation import _PROOF_KEYS, _read as _read_native_carrier

        proof_payload = _read_native_carrier(
            proof_path,
            code="portable-publication-native-prior-invalid",
            mode=None,
        )
        proof_document = tomllib.loads(proof_payload.decode("utf-8"))
        if (
            not isinstance(proof_document, dict)
            or set(proof_document) != _PROOF_KEYS
            or proof_document.get("schema_version") != 2
        ):
            _refuse("portable-publication-native-prior-invalid", "native predecessor release proof is not closed")
        installation_digest = _sha256(
            proof_document.get("installation_command_sha256"), label="native predecessor installation command"
        )
        command_payload = _read_native_carrier(
            root / ".caprmedio_runtime" / "installation" / "commands" / f"{installation_digest}.json",
            code="portable-publication-native-prior-invalid",
            mode=None,
        )
        command_document = json.loads(command_payload.decode("utf-8"))
        operation = command_document.get("operation") if isinstance(command_document, dict) else None
        if operation == "install_framework_runtime":
            binding = _reopen_direct_native_predecessor_binding(
                root,
                package=package,
                context_sha256=context_sha256,
                generation=generation,
                proof=proof_document,
                command_payload=command_payload,
                command_sha256=installation_digest,
            )
        elif operation == "promote_selected_runtime":
            # The selected reader owns the O169 Session/run checkpoint path.
            # Its return value still reaches ``bind_native_installed_n`` and
            # therefore the same final D598/D599/D604 physical reader below.
            from release_promotion import bind_selected_native_n_from_checkpoint

            binding = bind_selected_native_n_from_checkpoint(root)
        else:
            _refuse(
                "portable-publication-native-prior-invalid",
                "native predecessor installation command has no designated operation",
            )
    except PortableRuntimePublicationError:
        raise
    except Exception as error:
        raise PortableRuntimePublicationError(
            "portable-publication-native-prior-invalid",
            "native predecessor original packet or final proof cannot be physically reopened",
        ) from error
    if binding is None:
        _refuse(
            "portable-publication-native-prior-unavailable",
            "native predecessor has no retained original publication packet",
        )
    actual_package = getattr(binding, "verified_package", None)
    selected = getattr(binding, "selected", None)
    if (
        actual_package != package
        or getattr(selected, "package_manifest_sha256", None) != package.manifest_digest
        or getattr(selected, "framework_version", None) != package.framework_version
        or getattr(selected, "version_toml_sha256", None) != package.version_toml_sha256
        or getattr(selected, "source_catalog_sha256", None) != package.source_catalog_sha256
        or getattr(selected, "full_gate_receipt_sha256", None) != selected_package.full_gate_receipt_sha256
        or getattr(selected, "target_project_context_sha256", None) != context_sha256
        or getattr(selected, "state_generation", None) != generation
        or getattr(selected, "installation_lock_generation", None)
        != runtime_document.get("installation_lock_generation")
        or getattr(selected, "selector_sha256", None) != _digest(runtime_selector)
        or getattr(selected, "release_proof_sha256", None) != _digest(proof_payload)
    ):
        _refuse("portable-publication-native-prior-invalid", "native predecessor binding differs from selected carriers")
    if package_path.read_bytes() != package_selector or runtime_path.read_bytes() != runtime_selector:
        _refuse("portable-publication-native-prior-invalid", "native predecessor selectors changed after full proof reopening")
    try:
        from legacy_process_coverage import NativeTargetContextProof
        from release_handoff import NativeInstalledNBinding

        if not isinstance(binding, NativeInstalledNBinding):
            _refuse(
                "portable-publication-native-prior-invalid",
                "native predecessor did not produce the concrete installed-N binding",
            )

        return (
            NativeTargetContextProof(
                execution_selector_bytes=runtime_selector,
                prior_target_context_sha256=context_sha256,
            ),
            binding,
        )
    except Exception as error:
        raise PortableRuntimePublicationError(
            "portable-publication-native-prior-invalid",
            "native predecessor D607 binding cannot retain its physical D600 and selector carriers",
        ) from error


def _reopen_direct_native_predecessor_binding(
    root: Path,
    *,
    package: VerifiedFrameworkPackage,
    context_sha256: str,
    generation: int,
    proof: Mapping[str, object],
    command_payload: bytes,
    command_sha256: str,
) -> object:
    """Reopen a prior direct O200 packet from its canonical terminal result.

    This is intentionally the direct half of
    :func:`release_promotion.bind_selected_native_n_from_checkpoint`, rather
    than that broader helper.  A direct predecessor has no selected-workflow
    run to import or discover.  Its only admitted packet locator is the exact
    O200 command named by D604, its reopened Action start, and that start's
    canonical completed result.  The result reader reconstructs the Full Gate
    exclusively from its seven retained effect references before the native
    reader reopens all D598/D599/D604 carriers.
    """

    from framework_installation_command import (
        read_framework_installation_command_receipt,
        reopen_framework_installation_command_start,
    )
    from installed_mcp_binding import admit_installed_mcp_binding
    from release_checkpoint import read_direct_native_result_effects, read_direct_native_result_packet
    from release_handoff import bind_native_installed_n
    from release_promotion import _reopen_completed_direct_native_result

    command = read_framework_installation_command_receipt(
        command_payload,
        expected_sha256=command_sha256,
    )
    if (
        command.package_manifest_sha256 != package.manifest_digest
        or command.target_project_context_sha256 != context_sha256
        or command.full_gate_receipt_sha256 != proof.get("full_gate_receipt_sha256")
    ):
        _refuse(
            "portable-publication-native-prior-invalid",
            "direct predecessor command differs from its retained native proof",
        )
    installed_binding = admit_installed_mcp_binding(
        root,
        package,
        target_context_sha256=context_sha256,
    )
    started = reopen_framework_installation_command_start(
        root,
        command,
        action_package=package,
        operators_registry_ref=Path(installed_binding.target_context.control_child_relpath) / "operators_registry.toml",
    )
    run = started.get("run") if isinstance(started, Mapping) else None
    action_run_id = run.get("run_id") if isinstance(run, Mapping) else None
    if (
        not isinstance(action_run_id, str)
        or not action_run_id
        or "/" in action_run_id
        or "\\" in action_run_id
        or action_run_id in {".", ".."}
    ):
        _refuse(
            "portable-publication-native-prior-invalid",
            "direct predecessor Action identity is not one safe path component",
        )
    result_ref = f".caprmedio_tmp/installation/results/{action_run_id}/result.json"
    from native_selected_installation import _read as _read_native_carrier

    result_payload = _read_native_carrier(
        root / result_ref,
        code="portable-publication-native-prior-invalid",
        mode=None,
    )
    effects = read_direct_native_result_effects(
        result_payload,
        command=command,
        action_run_id=action_run_id,
        state_generation=generation,
    )
    _reopen_completed_direct_native_result(root, started, result_ref, effects)
    packet = read_direct_native_result_packet(
        result_payload,
        project_root=str(root),
        command=command,
        action_run_id=action_run_id,
        state_generation=generation,
    )
    binding = bind_native_installed_n(
        root,
        package,
        packet,
        target_context_sha256=context_sha256,
    )
    if (
        binding.selected.state_generation != generation
        or binding.selected.full_gate_receipt_sha256 != command.full_gate_receipt_sha256
    ):
        _refuse(
            "portable-publication-native-prior-invalid",
            "direct predecessor original packet differs from the selected native generation",
        )
    return binding


def _reopen_legacy_predecessor_context(
    root: Path,
    *,
    package_selector: bytes,
    runtime_selector: bytes,
) -> object:
    """Reopen the complete bootstrap proof for a legacy predecessor.

    Pre-D600 installs cannot truthfully acquire a target-context identity.
    Their D607 admission is instead the exact pair of retained Framework and
    Tools selectors plus the sealed first-N bootstrap-image proof.  The
    bootstrap reader authenticates only retained package/proof carriers; it
    never consults current candidate sources or manufactures a D600 alias.
    """

    _verify_legacy_tools_selection(root)
    _selected_legacy_framework_package(root, runtime_selector)
    try:
        framework_document = tomllib.loads(runtime_selector.decode("utf-8"))
        if not isinstance(framework_document, dict):
            _refuse("portable-publication-legacy-prior-context-unavailable", "legacy Framework selector is not closed")
        release = _sha256(framework_document.get("release"), label="legacy Framework release")
        image_digest = framework_document.get("image_digest")
        if not isinstance(image_digest, str) or not image_digest.startswith("sha256:"):
            _refuse(
                "portable-publication-legacy-prior-context-unavailable",
                "legacy Framework selector has no immutable image identity",
            )
        _sha256(image_digest.removeprefix("sha256:"), label="legacy Framework image")

        tools_selector_path = root / ".caprmedio_runtime" / "tools" / "current.toml"
        framework_selector_path = root / _LEGACY_RUNTIME_SELECTOR
        _regular(tools_selector_path, code="portable-publication-legacy-prior-context-unavailable")
        _regular(framework_selector_path, code="portable-publication-legacy-prior-context-unavailable")
        tools_selector = tools_selector_path.read_bytes()
        if tools_selector != package_selector:
            _refuse(
                "portable-publication-legacy-prior-context-unavailable",
                "legacy D605 package selection is not the verified Tools selector",
            )
        if framework_selector_path.read_bytes() != runtime_selector:
            _refuse(
                "portable-publication-legacy-prior-context-unavailable",
                "legacy Framework selector changed while reopening its bootstrap proof",
            )

        from bootstrap_image import BOOTSTRAP_IMAGE_RELATIVE, read_retained_initial_framework_image
        from legacy_process_coverage import LegacyBootstrapSourceProof

        evidence = read_retained_initial_framework_image(root, release, image_digest)
        proof_key = _sha256(evidence.bootstrap_proof_key, label="legacy bootstrap proof key")
        receipt_path = root / BOOTSTRAP_IMAGE_RELATIVE / proof_key / "evidence.toml"
        _regular(receipt_path, code="portable-publication-legacy-prior-context-unavailable")
        raw_receipt = receipt_path.read_bytes()
        if (
            evidence.manifest_sha256 != release
            or evidence.image_digest != image_digest
            or evidence.receipt_sha256 != _digest(raw_receipt)
            or evidence.proof_root != (BOOTSTRAP_IMAGE_RELATIVE / proof_key).as_posix()
            or evidence.evidence_root != evidence.proof_root
        ):
            _refuse(
                "portable-publication-legacy-prior-context-unavailable",
                "retained legacy bootstrap proof differs from the selected Framework carriers",
            )
        return LegacyBootstrapSourceProof(
            framework_selector_bytes=runtime_selector,
            tool_selector_bytes=tools_selector,
            package_manifest_sha256=evidence.manifest_sha256,
            source_context_sha256=evidence.source_context_sha256,
            image_digest=image_digest,
            bootstrap_proof_key=proof_key,
            raw_receipt_bytes=raw_receipt,
        )
    except PortableRuntimePublicationError:
        raise
    except Exception as error:
        raise PortableRuntimePublicationError(
            "portable-publication-legacy-prior-context-unavailable",
            "verified legacy selectors have no complete retained bootstrap-image proof",
        ) from error


def _freeze_native_predecessor_handoff(
    root: Path,
    *,
    package_selector: bytes,
    runtime_selector: bytes,
    lock: InstallationPublicationLock,
) -> tuple[object, _NativePredecessorHandoff]:
    """Freeze physical N without depending on legacy state migration roots."""

    concrete_lock, locked_root = _root(lock)
    if locked_root != root:
        _refuse("portable-publication-native-prior-invalid", "native predecessor belongs to another Project lock")
    predecessor_proof, binding = _reopen_native_predecessor_context(
        root,
        package_selector=package_selector,
        runtime_selector=runtime_selector,
    )
    prior_context_sha256 = getattr(predecessor_proof, "prior_target_context_sha256", None)
    selected = getattr(binding, "selected", None)
    lock_generation = getattr(selected, "installation_lock_generation", None)
    release_proof_sha256 = getattr(selected, "release_proof_sha256", None)
    state_generation = getattr(selected, "state_generation", None)
    if (
        not isinstance(prior_context_sha256, str)
        or len(prior_context_sha256) != 64
        or set(prior_context_sha256) - _SHA256
        or isinstance(state_generation, bool)
        or not isinstance(state_generation, int)
        or state_generation < 1
        or not isinstance(lock_generation, str)
        or not lock_generation
        or not isinstance(release_proof_sha256, str)
        or len(release_proof_sha256) != 64
        or set(release_proof_sha256) - _SHA256
    ):
        _refuse(
            "portable-publication-native-prior-invalid",
            "native predecessor handoff is not fully bound to the physical installed N",
        )
    return (
        predecessor_proof,
        _NativePredecessorHandoff._create(
            binding=binding,
            package_selector=package_selector,
            runtime_selector=runtime_selector,
            target_context_sha256=prior_context_sha256,
            state_generation=state_generation,
            prior_installation_lock_generation=lock_generation,
            release_proof_sha256=release_proof_sha256,
            publication_lock_generation=concrete_lock.lock_generation,
            capture_lock=concrete_lock,
        ),
    )


def _open_predecessor_process_coverage(
    root: Path,
    *,
    target_context: TargetProjectContext,
    old_package_selector: bytes,
    old_execution_selector: tuple[Path, bytes],
    lock: InstallationPublicationLock,
) -> tuple[str | None, object, object, _NativePredecessorHandoff | None]:
    """Open the sole internal D607 coverage source under the held lock."""

    concrete_lock, locked_root = _root(lock)
    if locked_root != root or concrete_lock.target_context_sha256 != target_context.sha256:
        _refuse(
            "portable-publication-process-coverage-lock-invalid",
            "predecessor coverage must use this active Project/context publication lock",
        )
    relative, raw_selector = old_execution_selector
    family = "legacy" if relative == _LEGACY_RUNTIME_SELECTOR else "native"
    if family == "native":
        predecessor_proof, handoff = _freeze_native_predecessor_handoff(
            root,
            package_selector=old_package_selector,
            runtime_selector=raw_selector,
            lock=concrete_lock,
        )
        prior_context_sha256 = getattr(predecessor_proof, "prior_target_context_sha256", None)
    else:
        predecessor_proof = _reopen_legacy_predecessor_context(
            root,
            package_selector=old_package_selector,
            runtime_selector=raw_selector,
        )
        prior_context_sha256 = None
        handoff = None
    try:
        from legacy_process_coverage import LegacyProcessCoverageError, open_legacy_process_coverage
        from legacy_process_providers import (
            LegacyProcessAdmission,
            LegacyProcessCoverageError as ProviderCoverageError,
            fenced_legacy_process_providers,
        )
        from project_selection import ProjectSelectionError, resolve_project

        selection = resolve_project(root)
        admission = LegacyProcessAdmission(
            project_root=root,
            project_instance_id=selection.instance_id,
            target_context_sha256=target_context.sha256,
            prior_target_context_sha256=prior_context_sha256,
            prior_selector_bytes=raw_selector,
            fence=lock,
            selection=selection,
            predecessor_proof=predecessor_proof,
        )
        coverage = open_legacy_process_coverage(
            fenced_legacy_process_providers(admission),
            target_context_sha256=target_context.sha256,
            prior_target_context_sha256=prior_context_sha256,
            prior_selector_sha256=_digest(raw_selector),
            predecessor_proof=predecessor_proof,
        )
    except (LegacyProcessCoverageError, ProviderCoverageError, ProjectSelectionError) as error:
        raise PortableRuntimePublicationError(
            f"portable-publication-{family}-process-coverage-invalid",
            "internally opened predecessor process coverage is unavailable",
        ) from error
    try:
        # Ownership transfers to the prepared replacement only after the
        # final lock reopen.  If it fails, this frame still owns every
        # provider fence opened above and must release them before exposing no
        # coverage value to its caller.
        concrete_lock.revalidate()
    except BaseException:
        _close_process_coverage(coverage, suppress_errors=True)
        raise
    if handoff is not None:
        handoff = handoff._with_coverage(predecessor_proof, coverage)
    return prior_context_sha256, predecessor_proof, coverage, handoff


def _close_process_coverage(coverage: object, *, suppress_errors: bool) -> None:
    """Release one opaque coverage value without accepting a caller substitute."""

    close = getattr(coverage, "close", None)
    if not callable(close):
        _refuse("portable-publication-process-coverage-invalid", "prepared predecessor coverage has no close operation")
    try:
        close()
    except Exception as error:
        if suppress_errors:
            return
        raise PortableRuntimePublicationError(
            "portable-publication-process-coverage-release-failed",
            "a predecessor provider fence could not be released",
        ) from error


def _has_complete_legacy_state_roots(root: Path) -> bool:
    """Classify the three historic state roots without treating absence as quiet.

    A native N may never have had D605 state.  In that case no inventory/copy
    carrier is possible or needed, but D607 coverage remains mandatory.  A
    partial historic tree is neither of those cases and therefore refuses.
    """

    names = ("project_mcp", "mcp_hot_reload", "workflow_orchestrator")
    observed = tuple((root / _INSTALL_ROOT / name).exists() or (root / _INSTALL_ROOT / name).is_symlink() for name in names)
    if any(observed) and not all(observed):
        _refuse(
            "portable-publication-native-legacy-state-partial",
            "native predecessor has only part of the governed legacy state surface",
        )
    return all(observed)


def _retain_rootless_native_quiescence(
    handoff: _NativePredecessorHandoff,
    *,
    target_context: TargetProjectContext,
    lock: InstallationPublicationLock,
) -> _NativePredecessorHandoff:
    """Retain and reopen D607v4 provider evidence before Methodology effects.

    Native predecessors without D605 roots have no migration inventory.  Their
    provider rows therefore live in the dedicated existing D607 quiescence
    carrier, which is written even when the bounded query is unsafe/unknown.
    The carrier is retained before deciding whether its physically reopened
    ``safe`` result permits any live Methodology or ``ca`` publication.
    """

    if not _is_native_predecessor_handoff(handoff):
        _refuse(
            "portable-publication-native-process-coverage-missing",
            "rootless native replacement has no publisher-minted coverage handoff",
        )
    concrete_lock, root = _root(lock)
    coverage = handoff._process_coverage
    predecessor_proof = handoff._predecessor_proof
    if coverage is None or predecessor_proof is None or handoff._capture_lock is not concrete_lock:
        _refuse(
            "portable-publication-native-process-coverage-missing",
            "rootless native replacement has no still-open provider coverage",
        )
    try:
        from installation_state import (
            InstallationStateError,
            RetainedNativeQuiescence,
            read_native_quiescence,
            retain_native_quiescence,
        )
        from legacy_process_coverage import LegacyProcessCoverage, NativeTargetContextProof

        if not isinstance(coverage, LegacyProcessCoverage) or not isinstance(predecessor_proof, NativeTargetContextProof):
            _refuse(
                "portable-publication-native-process-coverage-invalid",
                "rootless native replacement coverage has invalid typed bindings",
            )
        retained = retain_native_quiescence(
            root,
            process_coverage=coverage,
            predecessor_proof=predecessor_proof,
            lock=concrete_lock,
        )
        if not isinstance(retained, RetainedNativeQuiescence):
            _refuse(
                "portable-publication-native-process-coverage-invalid",
                "rootless native quiescence writer returned an invalid carrier",
            )
        reopened = read_native_quiescence(
            root,
            retained,
            process_coverage=coverage,
            predecessor_proof=predecessor_proof,
            lock=concrete_lock,
        )
    except InstallationStateError as error:
        raise PortableRuntimePublicationError(
            "portable-publication-native-quiescence-blocked",
            "rootless native D607 quiescence cannot be physically reopened",
        ) from error
    if reopened != retained:
        _refuse(
            "portable-publication-native-quiescence-stale",
            "rootless native quiescence changed while reopening its retained carrier",
        )
    if not reopened.safe:
        _refuse(
            "portable-publication-native-quiescence-blocked",
            "rootless native provider evidence is not safe for replacement",
        )
    concrete_lock.revalidate()
    return handoff._with_native_quiescence(reopened)


def _revalidate_rootless_native_quiescence(
    handoff: _NativePredecessorHandoff,
    *,
    target_context: TargetProjectContext,
    lock: InstallationPublicationLock,
) -> None:
    """Persist/reopen the final D607 outcome immediately before deletion."""

    if not _is_native_predecessor_handoff(handoff):
        _refuse(
            "portable-publication-native-process-coverage-missing",
            "rootless native replacement has no publisher-minted coverage handoff",
        )
    retained = handoff._native_quiescence
    if retained is None:
        _refuse(
            "portable-publication-native-quiescence-missing",
            "rootless native replacement has no retained D607 quiescence carrier",
        )
    refreshed = _retain_rootless_native_quiescence(
        handoff,
        target_context=target_context,
        lock=lock,
    )
    if refreshed._native_quiescence != retained:
        _refuse(
            "portable-publication-native-quiescence-stale",
            "rootless native provider outcome changed after preparation",
        )


def _prepare_legacy_replacement(
    root: Path,
    *,
    target_context: TargetProjectContext,
    old_package_selector: bytes | None,
    old_execution_selector: tuple[Path, bytes] | None,
    lock: InstallationPublicationLock,
    native_predecessor: _NativePredecessorHandoff | None = None,
) -> LegacyReplacementPreparation | None:
    """Retain D605--D607 proof with internally opened process coverage.

    ``installation_state.run_retained_legacy_migration`` intentionally owns an
    obsolete selector switch and is therefore not usable here.  This smaller
    composition invokes only inventory, quiescence, and private-copy helpers.
    The process proof is not supplied by the caller: it comes from a complete
    internally constructed D607 coverage view and stays open until final
    selector publication or a failure exit.
    """

    if old_execution_selector is None:
        return None
    relative, expected_execution = old_execution_selector
    if relative not in {_RUNTIME_SELECTOR, _LEGACY_RUNTIME_SELECTOR} or not isinstance(expected_execution, bytes):
        _refuse("portable-publication-prior-selector-invalid", "predecessor execution selector is invalid")
    family = "legacy" if relative == _LEGACY_RUNTIME_SELECTOR else "native"
    if old_package_selector is None:
        _refuse(
            f"portable-publication-{family}-package-missing",
            "predecessor replacement requires the exact selected package carrier",
        )
    package_selector = root / _PACKAGE_SELECTOR
    _regular(package_selector, code=f"portable-publication-{family}-package-missing")
    if package_selector.read_bytes() != old_package_selector:
        _refuse(
            f"portable-publication-{family}-package-stale",
            "predecessor package selection changed before migration inventory",
        )
    execution_selector = root / relative
    _regular(execution_selector, code=f"portable-publication-{family}-selector-missing")
    if execution_selector.read_bytes() != expected_execution:
        _refuse(
            f"portable-publication-{family}-selector-stale",
            "predecessor execution selection changed before migration inventory",
        )
    if family == "native" and native_predecessor is not None:
        if (
            not _is_native_predecessor_handoff(native_predecessor)
            or native_predecessor._capture_lock is not lock
            or native_predecessor.package_selector != old_package_selector
            or native_predecessor.runtime_selector != expected_execution
            or native_predecessor._predecessor_proof is None
            or native_predecessor._process_coverage is None
        ):
            _refuse(
                "portable-publication-native-prior-stale",
                "native D607 coverage does not belong to this frozen predecessor and lock",
            )
        prior_context_sha256 = native_predecessor.target_context_sha256
        predecessor_proof = native_predecessor._predecessor_proof
        coverage = native_predecessor._process_coverage
    else:
        prior_context_sha256, predecessor_proof, coverage, opened_handoff = _open_predecessor_process_coverage(
            root,
            target_context=target_context,
            old_package_selector=old_package_selector,
            old_execution_selector=old_execution_selector,
            lock=lock,
        )
        if family == "native":
            native_predecessor = opened_handoff
    try:
        from installation_state import (
            InstallationStateError,
            build_legacy_inventory,
            prove_quiescence,
            read_inventory,
            read_quiescence,
            stage_legacy_copy,
            verify_staged_copy,
            write_inventory,
            write_quiescence,
        )
    except ImportError as error:  # pragma: no cover - package routing failure.
        _close_process_coverage(coverage, suppress_errors=True)
        raise PortableRuntimePublicationError(
            f"portable-publication-{family}-unavailable", "predecessor replacement evidence helpers are unavailable"
        ) from error
    try:
        inventory = build_legacy_inventory(
            root,
            migration_id=lock.lock_generation,
            target_context_sha256=target_context.sha256,
            process_coverage=coverage,
            prior_execution_context_sha256=prior_context_sha256,
            prior_execution_selector_sha256=_digest(expected_execution),
            predecessor_proof=predecessor_proof,
        )
        if inventory.get("legacy_selector_sha256") != _digest(old_package_selector):
            _refuse(
                f"portable-publication-{family}-package-stale",
                "predecessor inventory does not bind the exact selected package",
            )
        write_inventory(root, inventory, lock=lock, predecessor_proof=predecessor_proof)
        reopened_inventory = read_inventory(root, lock.lock_generation, predecessor_proof=predecessor_proof)
        if reopened_inventory != inventory:
            _refuse(
                f"portable-publication-{family}-inventory-stale",
                "persisted predecessor inventory differs from the prepared inventory",
            )
        quiescence = prove_quiescence(
            reopened_inventory,
            process_coverage=coverage,
            predecessor_proof=predecessor_proof,
        )
        write_quiescence(
            root,
            reopened_inventory,
            quiescence,
            lock=lock,
            predecessor_proof=predecessor_proof,
        )
        reopened_quiescence = read_quiescence(root, reopened_inventory, predecessor_proof=predecessor_proof)
        if reopened_quiescence != quiescence or reopened_quiescence.get("safe") is not True:
            _refuse(
                f"portable-publication-{family}-quiescence-blocked",
                "predecessor processes are not proven quiescent",
            )
        staged = stage_legacy_copy(
            root,
            reopened_inventory,
            reopened_quiescence,
            lock=lock,
            process_coverage=coverage,
            predecessor_proof=predecessor_proof,
        )
        verify_staged_copy(root, reopened_inventory, staged, predecessor_proof=predecessor_proof)
        # The opaque coverage remains ours until the lock is revalidated after
        # the final pre-delete copy.  A failed revalidation cannot leave those
        # provider fences held without a returned preparation owning them.
        lock.revalidate()
        return LegacyReplacementPreparation(
            migration_id=lock.lock_generation,
            inventory_sha256=str(reopened_inventory["inventory_sha256"]),
            quiescence_sha256=str(reopened_quiescence["quiescence_sha256"]),
            staged=dict(staged),
            predecessor_proof=predecessor_proof,
            process_coverage=coverage,
            native_predecessor=native_predecessor,
        )
    except InstallationStateError as error:
        _close_process_coverage(coverage, suppress_errors=True)
        raise PortableRuntimePublicationError(
            f"portable-publication-{family}-migration-invalid", "predecessor replacement evidence cannot be retained"
        ) from error
    except BaseException:
        _close_process_coverage(coverage, suppress_errors=True)
        raise


def _revalidate_legacy_replacement(
    prepared: PreparedNativePublication,
    *,
    lock: InstallationPublicationLock,
) -> None:
    """Reopen prior source/copy/quiescence facts immediately before deletion."""

    _concrete_lock, root = _root(lock)
    predecessor_selector = prepared.old_execution_selector
    if predecessor_selector is None:
        if prepared.legacy_replacement is not None:
            _refuse(
                "portable-publication-legacy-unexpected",
                "migration evidence is present without a predecessor execution selector",
            )
        return
    relative, expected_selector = predecessor_selector
    if relative not in {_RUNTIME_SELECTOR, _LEGACY_RUNTIME_SELECTOR} or not isinstance(expected_selector, bytes):
        _refuse("portable-publication-prior-selector-invalid", "predecessor execution selector is invalid")
    family = "legacy" if relative == _LEGACY_RUNTIME_SELECTOR else "native"
    evidence_missing = f"portable-publication-{family}-evidence-missing" if family == "legacy" else "portable-publication-native-quiescence-missing"
    evidence_stale = f"portable-publication-{family}-evidence-stale" if family == "legacy" else "portable-publication-native-quiescence-stale"
    evidence = prepared.legacy_replacement
    if family == "native" and evidence is None:
        if _has_complete_legacy_state_roots(root):
            _refuse(
                "portable-publication-native-evidence-missing",
                "native predecessor acquired governed legacy state after preparation",
            )
        handoff = prepared.native_predecessor
        if not _is_native_predecessor_handoff(handoff):
            _refuse(evidence_missing, "rootless native predecessor has no opaque coverage handoff")
        _revalidate_rootless_native_quiescence(
            handoff, target_context=prepared.target_context, lock=lock
        )
        return
    if not isinstance(evidence, LegacyReplacementPreparation):
        _refuse(
            evidence_missing,
            "predecessor replacement requires retained inventory and quiescence evidence",
        )
    coverage = evidence.process_coverage
    if coverage is None:
        _refuse(
            evidence_missing,
            "predecessor replacement has no still-open provider coverage",
        )
    if evidence.migration_id != lock.lock_generation:
        _refuse(
            evidence_stale,
            "predecessor replacement evidence belongs to another installation lock",
        )
    if prepared.old_package_selector is None:
        _refuse(
            f"portable-publication-{family}-package-missing",
            "predecessor replacement has no exact package selection",
        )
    try:
        from installation_state import (
            InstallationStateError,
            read_inventory,
            read_quiescence,
            verify_inventory,
            verify_staged_copy,
        )
    except ImportError as error:  # pragma: no cover - package routing failure.
        raise PortableRuntimePublicationError(
            "portable-publication-legacy-unavailable", "legacy replacement evidence readers are unavailable"
        ) from error
    try:
        inventory = read_inventory(root, evidence.migration_id, predecessor_proof=evidence.predecessor_proof)
        if (
            inventory.get("inventory_sha256") != evidence.inventory_sha256
            or inventory.get("target_context_sha256") != prepared.target_context.sha256
            or inventory.get("legacy_selector_sha256") != _digest(prepared.old_package_selector)
        ):
            _refuse(
                evidence_stale,
                "predecessor inventory no longer binds this exact replacement",
            )
        verify_inventory(
            root,
            inventory,
            process_coverage=coverage,
            predecessor_proof=evidence.predecessor_proof,
        )
        quiescence = read_quiescence(root, inventory, predecessor_proof=evidence.predecessor_proof)
        if quiescence.get("quiescence_sha256") != evidence.quiescence_sha256 or quiescence.get("safe") is not True:
            _refuse(
                f"portable-publication-{family}-quiescence-blocked",
                "predecessor processes are no longer proven quiescent",
            )
        verify_staged_copy(root, inventory, evidence.staged, predecessor_proof=evidence.predecessor_proof)
    except InstallationStateError as error:
        raise PortableRuntimePublicationError(
            evidence_stale, "predecessor replacement proof cannot be physically reopened"
        ) from error
    lock.revalidate()


def revalidate_prepared_native_predecessor(
    prepared: PreparedNativePublication,
    expected_binding: object,
    *,
    lock: InstallationPublicationLock,
) -> object:
    """Reopen frozen native N after O169 Methodology publication.

    The ordinary current-N reader deliberately rejects an old D604 proof once
    a selected candidate has replaced the canonical Methodology output.  That
    strict behavior remains correct for every ordinary reader.  This function
    is the sole narrow handoff for the selected wrapper: it reopens the old
    package, D598/D599, D600 controls, D601, original D604 command/start and
    detached Full Gate exactly as frozen before publication.  The one carrier
    that may have changed is admitted independently through the already
    staged *candidate* D604 proof, whose typed delivery must be this
    preparation's exact candidate delivery.

    It has no effects and creates no durable authority.  It only proves that
    the original predecessor still matches the preparation immediately before
    the shared destructive publisher is entered.
    """

    if not isinstance(prepared, PreparedNativePublication):
        _refuse("portable-publication-native-handoff-invalid", "native predecessor handoff requires typed preparation")
    concrete_lock, root = _root(lock)
    predecessor = prepared.old_execution_selector
    if (
        predecessor is None
        or predecessor[0] != _RUNTIME_SELECTOR
        or prepared.old_package_selector is None
        or not _is_native_predecessor_handoff(prepared.native_predecessor)
    ):
        _refuse(
            "portable-publication-native-handoff-unavailable",
            "selected native publication has no frozen native predecessor handoff",
        )
    handoff = prepared.native_predecessor
    try:
        from framework_installation_command import read_framework_installation_command_receipt
        from installed_mcp_binding import InstalledMcpBindingError, admit_installed_mcp_binding
        from native_installation_proof import (
            CandidateNativeInstallationProofRequest,
            NativeInstallationProof,
            NativeInstallationProofError,
            read_candidate_native_installation_proof,
        )
        from native_selected_installation import (
            _PROOF_KEYS,
            _read as _read_native_carrier,
            _reopen_installation_command,
        )
        from portable_methodology_installation import CandidatePortableMethodologyDelivery
        from portable_runtime_materialization import (
            PortableRuntimeMaterializationError,
            reopen_final_runtime_command_fragment,
        )
        from release_full_gate import verify_detached_native_full_gate_evidence
        from release_handoff import NativeInstalledNBinding
    except ImportError as error:  # pragma: no cover - package routing failure.
        raise PortableRuntimePublicationError(
            "portable-publication-native-handoff-unavailable",
            "native predecessor handoff readers are unavailable",
        ) from error
    if not isinstance(expected_binding, NativeInstalledNBinding) or not isinstance(handoff.binding, NativeInstalledNBinding):
        _refuse("portable-publication-native-handoff-invalid", "native predecessor handoff requires an admitted installed-N binding")
    if expected_binding != handoff.binding:
        _refuse("portable-publication-native-handoff-stale", "selected native predecessor differs from builder-frozen N")
    selected = handoff.binding.selected
    if (
        handoff.package_selector != prepared.old_package_selector
        or handoff.runtime_selector != predecessor[1]
        or handoff.publication_lock_generation != concrete_lock.lock_generation
        or handoff._capture_lock is not concrete_lock
        or handoff.target_context_sha256 != selected.target_project_context_sha256
        or handoff.state_generation != selected.state_generation
        or handoff.prior_installation_lock_generation != selected.installation_lock_generation
        or handoff.release_proof_sha256 != selected.release_proof_sha256
    ):
        _refuse("portable-publication-native-handoff-stale", "builder-frozen native predecessor carriers are inconsistent")
    if (
        not isinstance(prepared.methodology_delivery, CandidatePortableMethodologyDelivery)
        or not isinstance(prepared.candidate_proof_request, CandidateNativeInstallationProofRequest)
        or not isinstance(prepared.candidate_proof, NativeInstallationProof)
        or prepared.candidate_proof_request.methodology_delivery is not prepared.methodology_delivery
    ):
        _refuse(
            "portable-publication-native-handoff-invalid",
            "selected native handoff requires the exact candidate D604 Methodology delivery",
        )
    package_path = root / _PACKAGE_SELECTOR
    runtime_path = root / _RUNTIME_SELECTOR
    _regular(package_path, code="portable-publication-native-handoff-stale")
    _regular(runtime_path, code="portable-publication-native-handoff-stale")
    try:
        package_selector = package_path.read_bytes()
        runtime_selector = runtime_path.read_bytes()
    except OSError as error:
        raise PortableRuntimePublicationError(
            "portable-publication-native-handoff-stale", "native predecessor selectors cannot be reopened"
        ) from error
    if package_selector != handoff.package_selector or runtime_selector != handoff.runtime_selector:
        _refuse("portable-publication-native-handoff-stale", "native predecessor D598 or D599 changed after freezing")
    package = handoff.binding.verified_package
    try:
        reopened_package = verify_framework_package(package.root)
        selected_package = verify_current_package_selector(package_selector, package)
        live_binding = admit_installed_mcp_binding(
            root, package, target_context_sha256=selected.target_project_context_sha256
        )
    except (FrameworkPackageError, InstalledMcpBindingError) as error:
        raise PortableRuntimePublicationError(
            "portable-publication-native-handoff-stale", "native predecessor package or current D600 controls cannot be reopened"
        ) from error
    if (
        reopened_package != package
        or selected_package.package_manifest_sha256 != selected.package_manifest_sha256
        or selected_package.full_gate_receipt_sha256 != selected.full_gate_receipt_sha256
        or live_binding != selected.binding
        or _digest(runtime_selector) != selected.selector_sha256
    ):
        _refuse("portable-publication-native-handoff-stale", "native predecessor D598, D599, or D600 differs from frozen N")
    try:
        runtime_document = tomllib.loads(runtime_selector.decode("utf-8"))
    except (UnicodeDecodeError, tomllib.TOMLDecodeError) as error:
        raise PortableRuntimePublicationError(
            "portable-publication-native-handoff-stale", "native predecessor D599 is no longer valid TOML"
        ) from error
    try:
        from installed_mcp_binding import _RUNTIME_SELECTOR_KEYS
    except ImportError as error:  # pragma: no cover - package routing failure.
        raise PortableRuntimePublicationError(
            "portable-publication-native-handoff-unavailable", "native runtime selector reader is unavailable"
        ) from error
    if (
        not isinstance(runtime_document, dict)
        or set(runtime_document) != _RUNTIME_SELECTOR_KEYS
        or runtime_document.get("package_manifest_sha256") != selected.package_manifest_sha256
        or runtime_document.get("target_project_context_sha256") != selected.target_project_context_sha256
        or runtime_document.get("state_generation") != selected.state_generation
        or runtime_document.get("installation_lock_generation") != selected.installation_lock_generation
    ):
        _refuse("portable-publication-native-handoff-stale", "native predecessor D599 differs from frozen N")
    proof_path = root / _GENERATIONS / str(selected.state_generation) / "release-proof.toml"
    try:
        proof_payload = _read_native_carrier(
            proof_path, code="portable-publication-native-handoff-stale", mode=None
        )
        proof = tomllib.loads(proof_payload.decode("utf-8"))
    except (OSError, UnicodeDecodeError, tomllib.TOMLDecodeError, RuntimeError) as error:
        raise PortableRuntimePublicationError(
            "portable-publication-native-handoff-stale", "native predecessor D604 proof cannot be reopened"
        ) from error
    expected_proof = {
        "schema_version": 2,
        "package_manifest_sha256": selected.package_manifest_sha256,
        "framework_version": selected.framework_version,
        "version_toml_sha256": selected.version_toml_sha256,
        "source_catalog_sha256": selected.source_catalog_sha256,
        "full_gate_receipt_sha256": selected.full_gate_receipt_sha256,
        "image_digest": selected.image_digest,
        "target_project_context_sha256": selected.target_project_context_sha256,
        "state_generation": selected.state_generation,
        "installation_lock_generation": selected.installation_lock_generation,
        "selector_sha256": selected.selector_sha256,
    }
    if (
        not isinstance(proof, dict)
        or set(proof) != _PROOF_KEYS
        or _digest(proof_payload) != handoff.release_proof_sha256
        or any(proof.get(name) != value for name, value in expected_proof.items())
    ):
        _refuse("portable-publication-native-handoff-stale", "native predecessor D604 proof differs from frozen N")
    installation_command_sha256 = _sha256(
        proof.get("installation_command_sha256"), label="native predecessor installation command"
    )
    command_sha256 = _sha256(proof.get("command_sha256"), label="native predecessor D601 command")
    stage_manifest_sha256 = _sha256(
        proof.get("command_stage_manifest_sha256"), label="native predecessor D601 stage"
    )
    # The old proof's Methodology manifest remains hash-validated as part of
    # the immutable D604 bytes.  Its old output is intentionally not reopened:
    # the only allowed replacement is verified below by candidate D604.
    _sha256(proof.get("methodology_delivery_manifest_sha256"), label="native predecessor Methodology delivery")
    old_methodology_ref = proof.get("methodology_delivery_manifest_ref")
    if not isinstance(old_methodology_ref, str) or not old_methodology_ref:
        _refuse("portable-publication-native-handoff-stale", "native predecessor D604 Methodology reference is invalid")
    packet = handoff.binding.full_gate_packet
    try:
        retained = verify_detached_native_full_gate_evidence(
            packet.artifact_root, packet.retained_candidate, packet.suite, packet.build,
            packet.verification, packet.e2e, packet.evidence,
        )
        command_payload = _read_native_carrier(
            root / ".caprmedio_runtime" / "installation" / "commands" / f"{installation_command_sha256}.json",
            code="portable-publication-native-handoff-stale",
            mode=None,
        )
        receipt = _reopen_installation_command(
            root,
            command_payload,
            installation_command_sha256,
            action_package=package,
            operators_registry_ref=Path(live_binding.target_context.control_child_relpath) / "operators_registry.toml",
        )
        reopen_final_runtime_command_fragment(
            root,
            package,
            target_context_sha256=selected.target_project_context_sha256,
            state_generation=selected.state_generation,
            installation_lock_generation=selected.installation_lock_generation,
            command_sha256=command_sha256,
            stage_manifest_sha256=stage_manifest_sha256,
            release_proof_sha256=handoff.release_proof_sha256,
        )
    except (AttributeError, OSError, RuntimeError, ValueError, PortableRuntimeMaterializationError) as error:
        raise PortableRuntimePublicationError(
            "portable-publication-native-handoff-stale",
            "native predecessor detached gate, command/start, or D601 carriers cannot be reopened",
        ) from error
    if (
        retained.view.actual_package_manifest_sha256 != selected.package_manifest_sha256
        or receipt.package_manifest_sha256 != selected.package_manifest_sha256
        or receipt.target_project_context_sha256 != selected.target_project_context_sha256
        or receipt.full_gate_receipt_sha256 != selected.full_gate_receipt_sha256
    ):
        _refuse("portable-publication-native-handoff-stale", "native predecessor detached gate or command differs from D604")
    try:
        candidate = read_candidate_native_installation_proof(prepared.candidate_proof_request, lock=concrete_lock)
    except NativeInstallationProofError as error:
        raise PortableRuntimePublicationError(
            "portable-publication-native-handoff-candidate-invalid",
            "candidate D604 cannot authenticate the canonical replacement Methodology delivery",
        ) from error
    if candidate != prepared.candidate_proof:
        _refuse("portable-publication-native-handoff-candidate-stale", "candidate D604 differs from its prepared physical proof")
    if candidate.methodology_delivery_manifest_ref != old_methodology_ref:
        _refuse(
            "portable-publication-native-handoff-candidate-invalid",
            "candidate D604 Methodology delivery does not replace the old canonical delivery path",
        )
    concrete_lock.revalidate()
    return handoff.binding


def _remove_selected_package_tree(path: Path) -> bool:
    """Remove one already-reopened package; return whether its empty root remains.

    A restrictive local filesystem can reject directory removal while still
    allowing removal of every package member.  In that narrow case only empty
    directories remain and the replacement is copied into that exact former
    package root.  No unverified source or unrelated directory is touched.
    """

    try:
        shutil.rmtree(path)
        return False
    except OSError as error:
        if error.errno not in {errno.EACCES, errno.EPERM}:
            raise
    try:
        for carrier in sorted(path.rglob("*"), key=lambda item: len(item.relative_to(path).parts), reverse=True):
            if carrier.is_symlink():
                _refuse("portable-publication-old-package-removal-failed", "selected package changed to a symlink")
            if carrier.is_file():
                carrier.unlink()
            elif carrier.is_dir():
                try:
                    carrier.rmdir()
                except OSError as error:
                    if error.errno not in {errno.EACCES, errno.EPERM}:
                        raise
            else:
                _refuse("portable-publication-old-package-removal-failed", "selected package has a special carrier")
        leftovers = [carrier for carrier in path.rglob("*") if not carrier.is_dir()]
        if leftovers:
            _refuse("portable-publication-old-package-removal-failed", "selected package members remain after removal")
        try:
            path.rmdir()
            return False
        except OSError as error:
            if error.errno not in {errno.EACCES, errno.EPERM}:
                raise
    except PortableRuntimePublicationError:
        raise
    except OSError as error:
        raise PortableRuntimePublicationError(
            "portable-publication-old-package-removal-failed", "selected predecessor package could not be removed"
        ) from error
    # A permissions-constrained local filesystem may leave only the exact
    # selected, empty root.  It is never reused unless the staged destination
    # is that same verified location.
    return True


def publish_replacement_package(
    staged: VerifiedFrameworkPackage,
    *,
    lock: InstallationPublicationLock,
    old_package_selector: bytes | None,
    old_execution_selector: tuple[Path, bytes] | None,
) -> VerifiedFrameworkPackage:
    """Perform only the destructive package-tree transition under a held lock.

    This removes the exactly selected old native package only after callers have
    completed all non-destructive validation.  It deliberately does not write
    a selector; the publisher must publish selection later, after every final
    carrier is present.
    """

    concrete_lock, root = _root(lock)
    if not isinstance(staged, VerifiedFrameworkPackage):
        _refuse("portable-publication-package-invalid", "staged replacement must be typed")
    try:
        reopened = verify_framework_package(staged.root)
    except FrameworkPackageError as error:
        raise PortableRuntimePublicationError("portable-publication-stage-invalid", "staged replacement cannot be reopened") from error
    if reopened != staged or staged.root.parent.name != concrete_lock.lock_generation:
        _refuse("portable-publication-stage-invalid", "replacement is not this lock's staged package")
    releases = _mkdirs(root, _RELEASES)
    current = root / _PACKAGE_SELECTOR
    execution_path: Path | None = None
    legacy_execution = False
    if old_execution_selector is None:
        if (root / _RUNTIME_SELECTOR).exists() or (root / _RUNTIME_SELECTOR).is_symlink():
            _refuse("portable-publication-old-selector-unexpected", "bootstrap has an existing native execution selector")
        if (root / _LEGACY_RUNTIME_SELECTOR).exists() or (root / _LEGACY_RUNTIME_SELECTOR).is_symlink():
            _refuse("portable-publication-old-selector-unexpected", "bootstrap has an existing legacy execution selector")
    else:
        relative, expected = old_execution_selector
        if relative not in {_RUNTIME_SELECTOR, _LEGACY_RUNTIME_SELECTOR} or not isinstance(expected, bytes):
            _refuse("portable-publication-old-selector-invalid", "predecessor execution selector is invalid")
        execution_path = root / relative
        _regular(execution_path, code="portable-publication-old-selector-missing")
        if execution_path.read_bytes() != expected:
            _refuse("portable-publication-old-selector-stale", "execution selector changed before deletion")
        legacy_execution = relative == _LEGACY_RUNTIME_SELECTOR
    if old_package_selector is None:
        if current.exists() or current.is_symlink():
            _refuse("portable-publication-old-selector-unexpected", "bootstrap has an existing package selector")
    else:
        _regular(current, code="portable-publication-old-selector-missing")
        actual = current.read_bytes()
        if actual != old_package_selector:
            _refuse("portable-publication-old-selector-stale", "current package selector changed before deletion")
        if legacy_execution:
            # A historical selector points to the old Framework package while
            # ``.caprmedio_install/current.toml`` selects the old Tool
            # release.  Neither is D598.  Both must reopen before this one
            # historical Framework package is removed.
            _verify_legacy_tools_selection(root)
            if old_execution_selector is None:  # Narrowing for type checkers.
                _refuse("portable-publication-old-selector-invalid", "legacy execution selector is unavailable")
            old_path = _selected_legacy_framework_package(root, old_execution_selector[1])
        else:
            old_package = _selected_native_package(root, actual)
            old_path = old_package.root
        _directory(old_path, code="portable-publication-old-package-missing")
    # Remove execution selection before its referenced bytes.  A failed
    # destructive phase is therefore honestly unavailable, never a stale
    # selector that claims a removed package is still executable.
    if execution_path is not None:
        try:
            execution_path.unlink()
        except OSError as error:
            raise PortableRuntimePublicationError(
                "portable-publication-old-selector-removal-failed",
                "selected predecessor execution selector could not be removed",
            ) from error
    destination_reuses_old_root = False
    if old_package_selector is not None:
        try:
            current.unlink()
        except OSError as error:
            raise PortableRuntimePublicationError(
                "portable-publication-old-selector-removal-failed",
                "selected predecessor package selector could not be removed",
            ) from error
        try:
            destination_reuses_old_root = _remove_selected_package_tree(old_path)
        except OSError as error:
            raise PortableRuntimePublicationError(
                "portable-publication-old-package-removal-failed", "selected predecessor package could not be removed"
            ) from error
    destination = releases / staged.manifest_digest
    if (destination.exists() or destination.is_symlink()) and not (
        destination_reuses_old_root and destination == old_path
    ):
        _refuse("portable-publication-destination-conflict", "replacement release path already exists")
    try:
        if destination_reuses_old_root:
            shutil.copytree(staged.root, destination, copy_function=shutil.copy2, dirs_exist_ok=True)
        else:
            try:
                os.replace(staged.root, destination)
            except OSError as error:
                # Some sandboxed filesystems deny a directory rename between two
                # separately-created private trees even though both are inside
                # the held Project root.  A fresh no-overwrite copy remains safe:
                # activation still waits for a complete reopened inventory and a
                # later selector publication.  Other rename failures stay
                # unavailable rather than being mistaken for a retryable copy.
                if error.errno not in {errno.EACCES, errno.EPERM}:
                    raise
                if destination.exists() or destination.is_symlink():
                    _refuse("portable-publication-destination-conflict", "replacement release path already exists")
                shutil.copytree(staged.root, destination, copy_function=shutil.copy2)
        installed = verify_framework_package(destination)
    except (OSError, FrameworkPackageError) as error:
        raise PortableRuntimePublicationError("portable-publication-install-failed", "replacement package installation failed") from error
    if installed != VerifiedFrameworkPackage(
        staged.manifest_digest, destination, staged.inventory, staged.framework_version,
        staged.version_toml_sha256, staged.source_catalog_sha256, staged.binding_atoms,
    ):
        _refuse("portable-publication-install-invalid", "installed replacement differs from stage")
    concrete_lock.revalidate()
    return installed


def publish_selectors(
    *,
    package_selector: bytes,
    runtime_selector: bytes,
    lock: InstallationPublicationLock,
) -> tuple[str, str]:
    """Atomically publish already-admitted package then runtime selectors."""

    concrete_lock, root = _root(lock)
    if not isinstance(package_selector, bytes) or not isinstance(runtime_selector, bytes):
        _refuse("portable-publication-selector-invalid", "selectors must be exact bytes")
    package_path = _mkdirs(root, _INSTALL_ROOT) / "current.toml"
    runtime_path = _mkdirs(root, _RUNTIME_SELECTOR.parent) / "current.toml"
    if package_path.exists() or package_path.is_symlink() or runtime_path.exists() or runtime_path.is_symlink():
        _refuse("portable-publication-selector-conflict", "final selectors must be absent before same-byte publication")
    _atomic_new(package_path, package_selector, mode=0o600)
    _regular(package_path, code="portable-publication-selector-invalid")
    if package_path.read_bytes() != package_selector:
        _refuse("portable-publication-selector-invalid", "published package selector differs from admitted bytes")
    concrete_lock.revalidate()
    _atomic_new(runtime_path, runtime_selector, mode=0o600)
    _regular(runtime_path, code="portable-publication-selector-invalid")
    if runtime_path.read_bytes() != runtime_selector:
        _refuse("portable-publication-selector-invalid", "published runtime selector differs from admitted bytes")
    concrete_lock.revalidate()
    return _digest(package_selector), _digest(runtime_selector)


def _prepared_process_coverage(
    prepared: PreparedNativePublication,
    *,
    lock: InstallationPublicationLock,
) -> object | None:
    """Return the one coverage value whose fence lifetime this publisher owns."""

    predecessor = prepared.old_execution_selector
    evidence = prepared.legacy_replacement
    if predecessor is None:
        if evidence is not None:
            _refuse(
                "portable-publication-legacy-unexpected",
                "bootstrap preparation cannot retain predecessor coverage",
            )
        return None
    relative, _raw_selector = predecessor
    if relative not in {_RUNTIME_SELECTOR, _LEGACY_RUNTIME_SELECTOR}:
        _refuse("portable-publication-prior-selector-invalid", "prepared predecessor selector is invalid")
    family = "legacy" if relative == _LEGACY_RUNTIME_SELECTOR else "native"
    if family == "native":
        handoff = prepared.native_predecessor
        if not _is_native_predecessor_handoff(handoff) or handoff._capture_lock is not lock:
            _refuse(
                "portable-publication-native-process-coverage-missing",
                "prepared native predecessor has no same-lock opaque coverage handoff",
            )
        if handoff._process_coverage is None:
            _refuse(
                "portable-publication-native-process-coverage-missing",
                "prepared native predecessor coverage is not still open",
            )
        if evidence is not None and evidence.process_coverage is not handoff._process_coverage:
            _refuse(
                "portable-publication-native-process-coverage-invalid",
                "native migration evidence does not retain the frozen predecessor coverage",
            )
        return handoff._process_coverage
    if not isinstance(evidence, LegacyReplacementPreparation):
        _refuse("portable-publication-legacy-evidence-missing", "prepared replacement has no provider-owned process coverage")
    if evidence.process_coverage is None:
        _refuse(
            "portable-publication-legacy-process-coverage-missing",
            "prepared replacement has no still-open provider coverage",
        )
    return evidence.process_coverage


def _publish_prepared_native_runtime(
    prepared: PreparedNativePublication,
    *,
    lock: InstallationPublicationLock,
) -> PublishedNativeRuntime:
    """Run the shared non-authorizing physical cut-over for O-200 or O-169.

    The caller is responsible for the Action-specific start and for complete
    candidate Methodology/Skill/MCP preparation.  This boundary owns only the
    common publication effects and validates the candidate proof immediately
    before deleting a predecessor.  It intentionally accepts neither a
    callable nor a "gate passed" Boolean.
    """

    if not isinstance(prepared, PreparedNativePublication):
        _refuse("portable-publication-preparation-invalid", "publication requires a typed prepared native installation")
    concrete_lock, _ = _root(lock)
    if not isinstance(prepared.package, VerifiedFrameworkPackage) or not isinstance(prepared.target_context, TargetProjectContext):
        _refuse("portable-publication-preparation-invalid", "prepared package and target context must be typed")
    try:
        candidate_selector = verify_current_package_selector(prepared.prospective_package_selector, prepared.package)
    except FrameworkPackageError as error:
        raise PortableRuntimePublicationError(
            "portable-publication-preparation-invalid", "prospective D598 selector does not bind the candidate package"
        ) from error
    if (
        candidate_selector.package_manifest_sha256 != prepared.package.manifest_digest
        or prepared.target_context.sha256 != concrete_lock.target_context_sha256
    ):
        _refuse("portable-publication-preparation-invalid", "prepared facts do not bind this installation lock")
    try:
        from installed_mcp_binding import (
            InstalledMcpBinding,
            InstalledMcpBindingError,
            admit_candidate_mcp_binding,
            admit_installed_mcp_binding,
        )
    except ImportError as error:  # pragma: no cover - package routing failure.
        raise PortableRuntimePublicationError(
            "portable-publication-mcp-unavailable", "installed-MCP admission reader is unavailable"
        ) from error
    if not isinstance(prepared.candidate_mcp_binding, InstalledMcpBinding):
        _refuse("portable-publication-preparation-invalid", "candidate MCP binding must be typed")
    try:
        candidate_binding = admit_candidate_mcp_binding(
            concrete_lock.project_root,
            prepared.package,
            target_context_sha256=prepared.target_context.sha256,
            prospective_package_selector=prepared.prospective_package_selector,
            prospective_runtime_selector=prepared.prospective_runtime_selector,
        )
    except InstalledMcpBindingError as error:
        raise PortableRuntimePublicationError(
            "portable-publication-mcp-invalid", "candidate MCP binding cannot be physically reopened"
        ) from error
    if candidate_binding != prepared.candidate_mcp_binding:
        _refuse("portable-publication-mcp-stale", "candidate MCP binding differs from physical candidate carriers")
    # Make an independent content-addressed copy first.  It is fully reopened
    # before either predecessor selector is removed.
    staged = stage_replacement_package(prepared.package, lock=concrete_lock)
    # This is the last complete D604/Full-Gate candidate reopen before the
    # destructive transition.  It also retains the D604 proof at its governed
    # final generation location while selection is still inactive.
    generation_proof = publish_final_generation_proof(
        prepared.candidate_proof_request, prepared.candidate_proof, lock=concrete_lock
    )
    # A legacy predecessor has its own retained-state surface.  Reopen its
    # exact inventory, shutdown proof and staged copy after every candidate
    # carrier is complete and immediately before any selected bytes disappear.
    _revalidate_legacy_replacement(prepared, lock=concrete_lock)
    _revalidate_ca_skill_publication(prepared, lock=concrete_lock)
    installed = publish_replacement_package(
        staged,
        lock=concrete_lock,
        old_package_selector=prepared.old_package_selector,
        old_execution_selector=prepared.old_execution_selector,
    )
    package_digest, runtime_digest = publish_selectors(
        package_selector=prepared.prospective_package_selector,
        runtime_selector=prepared.prospective_runtime_selector,
        lock=concrete_lock,
    )
    try:
        verified_selector = verify_current_package_selector(prepared.prospective_package_selector, installed)
    except FrameworkPackageError as error:
        raise PortableRuntimePublicationError(
            "portable-publication-final-invalid", "installed D598 selector cannot be physically reopened"
        ) from error
    if verified_selector != candidate_selector:
        _refuse("portable-publication-final-invalid", "installed package selector differs from staged candidate selector")
    try:
        installed_binding = admit_installed_mcp_binding(
            concrete_lock.project_root, installed, target_context_sha256=prepared.target_context.sha256
        )
    except InstalledMcpBindingError as error:
        raise PortableRuntimePublicationError(
            "portable-publication-final-invalid", "installed MCP binding cannot be physically reopened"
        ) from error
    try:
        from native_selected_installation import (
            NativeSelectedInstallationError,
            reopen_current_native_installation,
        )

        final_selected = reopen_current_native_installation(
            concrete_lock.project_root,
            installed,
            prepared.candidate_proof_request.full_gate_packet,
            target_context_sha256=prepared.target_context.sha256,
        )
    except (AttributeError, NativeSelectedInstallationError, RuntimeError) as error:
        raise PortableRuntimePublicationError(
            "portable-publication-final-invalid",
            "final D601, D604, and Methodology delivery cannot be physically reopened",
        ) from error
    if (
        final_selected.package_manifest_sha256 != installed.manifest_digest
        or final_selected.target_project_context_sha256 != prepared.target_context.sha256
        or final_selected.full_gate_receipt_sha256 != candidate_selector.full_gate_receipt_sha256
        or final_selected.selector_sha256 != runtime_digest
    ):
        _refuse(
            "portable-publication-final-invalid",
            "final selected native carriers differ from the prepared publication",
        )
    concrete_lock.revalidate()
    return PublishedNativeRuntime(
        package=installed,
        generation_proof_path=generation_proof,
        package_selector_sha256=package_digest,
        runtime_selector_sha256=runtime_digest,
        installed_mcp_binding=installed_binding,
    )


def publish_prepared_native_runtime(
    prepared: PreparedNativePublication,
    *,
    lock: InstallationPublicationLock,
) -> PublishedNativeRuntime:
    """Publish once and release predecessor provider fences on every exit.

    Coverage is opened while the builder still has both exact predecessor
    selectors.  The handles must stay live through the last pre-delete
    revalidation, removal, and selector switch, then close whether the switch
    completed or a later physical operation failed.
    """

    if not isinstance(prepared, PreparedNativePublication):
        _refuse("portable-publication-preparation-invalid", "publication requires a typed prepared native installation")
    coverage = _prepared_process_coverage(prepared, lock=lock)
    try:
        publication = _publish_prepared_native_runtime(prepared, lock=lock)
    except BaseException:
        if coverage is not None:
            _close_process_coverage(coverage, suppress_errors=True)
        raise
    if coverage is not None:
        _close_process_coverage(coverage, suppress_errors=False)
    return publication


def build_prepared_native_publication(
    request: object,
    *,
    package: object,
    target_context: object,
    installation_command_sha256: object,
    full_gate_packet: object,
    runtime_stage_request: object,
    methodology_preparation: object,
    state_generation: int,
    old_package_selector: bytes | None,
    old_execution_selector: tuple[Path, bytes] | None,
    lock: InstallationPublicationLock,
) -> PreparedNativePublication:
    """Construct, publish, and physically reopen every non-selector input.

    This is authority-neutral common preparation for direct O-200 and selected
    O-169 publication.  The caller must have independently reopened its own
    Action command/start before acquiring ``lock``; this builder consumes only
    the typed package/context and exact command digest bound by that lock.  It
    persists D600, preserves/creates config, stages D601, proves predecessor
    quiescence, then publishes either the direct target's precompiled
    Methodology or the selected candidate's sealed Methodology and local ``ca``
    Skill before staging D604.  It does not delete or select a package.
    """
    try:
        from framework_installation import PortableInstallationRequest
        from installation_context import persist_target_project_context
        from runtime_configuration import ensure_runtime_configuration
        from portable_runtime_materialization import CandidateRuntimeCommandStageRequest, stage_candidate_runtime_command
        from native_installation_proof import (
            CandidateNativeInstallationProofRequest,
            stage_candidate_native_installation_proof,
        )
        from installed_mcp_binding import admit_candidate_mcp_binding
        from portable_methodology_installation import (
            PreparedCandidateMethodologyPublication,
            PreparedTargetMethodologyPublication,
            TargetPortableMethodologyDelivery,
            publish_prepared_candidate_portable_methodology,
            publish_prepared_target_portable_methodology,
        )
    except ImportError as error:  # pragma: no cover
        raise PortableRuntimePublicationError("portable-publication-builder-unavailable", "portable preparation dependencies are unavailable") from error
    if not isinstance(request, PortableInstallationRequest):
        _refuse("portable-publication-builder-invalid", "builder requires a typed portable installation request")
    if not isinstance(package, VerifiedFrameworkPackage) or not isinstance(target_context, TargetProjectContext):
        _refuse("portable-publication-builder-invalid", "builder requires typed package and target context")
    command_sha256 = _sha256(installation_command_sha256, label="installation command")
    if not isinstance(runtime_stage_request, CandidateRuntimeCommandStageRequest):
        _refuse("portable-publication-builder-invalid", "builder requires typed candidate D601 stage request")
    methodology_route = _methodology_preparation_route(
        methodology_preparation,
        candidate_type=PreparedCandidateMethodologyPublication,
        target_type=PreparedTargetMethodologyPublication,
    )
    if request.full_gate_packet != full_gate_packet:
        _refuse("portable-publication-builder-invalid", "Methodology request and runtime staging must share one Full Gate packet")
    receipt = getattr(getattr(full_gate_packet, "evidence", None), "receipt_sha256", None)
    image = getattr(getattr(full_gate_packet, "evidence", None), "candidate_image_digest", None)
    if not isinstance(receipt, str) or len(receipt) != 64 or set(receipt) - _SHA256:
        _refuse("portable-publication-builder-invalid", "retained Full Gate receipt is invalid")
    if not isinstance(image, str) or not image.startswith("sha256:"):
        _refuse("portable-publication-builder-invalid", "retained Full Gate image is invalid")
    if getattr(methodology_preparation, "gate_receipt_sha256", None) != receipt:
        _refuse("portable-publication-builder-stale", "Methodology preparation binds another Full Gate receipt")
    concrete_lock, root = _root(lock)
    context = target_context
    if context.sha256 != concrete_lock.target_context_sha256 or command_sha256 != concrete_lock.command_sha256:
        _refuse("portable-publication-builder-stale", "prepared facts differ from the installation lock")
    persist_target_project_context(request.target, context, lock=concrete_lock)
    try:
        configuration = ensure_runtime_configuration(
            root, package, default_member=request.runtime_default_member, lock=concrete_lock
        )
    except RuntimeError as error:
        raise PortableRuntimePublicationError("portable-publication-config-invalid", "runtime configuration cannot be preserved or created") from error
    if configuration.state not in {"created", "preserved"} or configuration.configuration is None:
        _refuse(
            "portable-publication-config-invalid",
            "runtime configuration cannot be preserved or created",
        )
    package_selector = render_package_selector(package, full_gate_receipt_sha256=receipt, image_digest=image[7:])
    runtime_selector = render_runtime_selector(
        package, context, state_generation=state_generation,
        installation_lock_generation=concrete_lock.lock_generation, image_digest=image[7:],
    )
    if (
        runtime_stage_request.package != package or runtime_stage_request.target_context != context
        or runtime_stage_request.prospective_package_selector != package_selector
        or runtime_stage_request.full_gate_packet != full_gate_packet or runtime_stage_request.state_generation != state_generation
    ):
        _refuse("portable-publication-builder-stale", "candidate D601 request differs from retained direct inputs")
    native_predecessor: _NativePredecessorHandoff | None = None
    legacy_replacement: LegacyReplacementPreparation | None = None
    try:
        native_without_legacy_state = False
        if old_execution_selector is not None and old_execution_selector[0] == _RUNTIME_SELECTOR:
            if old_package_selector is None:
                _refuse(
                    "portable-publication-native-package-missing",
                    "native predecessor handoff requires its exact D598 package selector",
                )
            # D562/D607: freeze N and open all three provider fences before
            # any candidate stage or live Methodology/ca effect.  The opaque
            # coverage stays on the internal handoff through selector switch.
            _prior_context, _prior_proof, _coverage, native_predecessor = _open_predecessor_process_coverage(
                root,
                target_context=context,
                old_package_selector=old_package_selector,
                old_execution_selector=old_execution_selector,
                lock=concrete_lock,
            )
            native_without_legacy_state = not _has_complete_legacy_state_roots(root)
            if native_without_legacy_state:
                native_predecessor = _retain_rootless_native_quiescence(
                    native_predecessor, target_context=context, lock=concrete_lock
                )
        # D562 freezes N before any candidate runtime stage is written.  A
        # stage is inert, but retaining the original N first makes its proof
        # independent of every subsequent candidate carrier.
        stage = stage_candidate_runtime_command(runtime_stage_request, lock=concrete_lock)
        if not native_without_legacy_state:
            legacy_replacement = _prepare_legacy_replacement(
                root,
                target_context=context,
                old_package_selector=old_package_selector,
                old_execution_selector=old_execution_selector,
                lock=concrete_lock,
                native_predecessor=native_predecessor,
            )
    except BaseException:
        coverage = (
            legacy_replacement.process_coverage
            if legacy_replacement is not None
            else getattr(native_predecessor, "_process_coverage", None)
        )
        if coverage is not None:
            _close_process_coverage(coverage, suppress_errors=True)
        raise
    if (
        native_predecessor is not None
        and legacy_replacement is not None
        and legacy_replacement.native_predecessor is not None
        and (
            legacy_replacement.native_predecessor.binding != native_predecessor.binding
            or legacy_replacement.native_predecessor.package_selector != native_predecessor.package_selector
            or legacy_replacement.native_predecessor.runtime_selector != native_predecessor.runtime_selector
            or legacy_replacement.native_predecessor.release_proof_sha256 != native_predecessor.release_proof_sha256
        )
    ):
        _close_process_coverage(legacy_replacement.process_coverage, suppress_errors=True)
        _refuse(
            "portable-publication-native-prior-stale",
            "native predecessor changed between handoff freezing and D607 coverage",
        )
    try:
        selector = verify_current_package_selector(package_selector, package)
        if methodology_route == "candidate":
            methodology_delivery = publish_prepared_candidate_portable_methodology(
                request, methodology_preparation, package=package, target_context=context,
                prospective_selector=selector, lock=concrete_lock,
            )
            proof_methodology_delivery = methodology_delivery
        else:
            methodology_delivery = publish_prepared_target_portable_methodology(
                request, methodology_preparation, package=package, target_context=context,
                prospective_selector=selector, lock=concrete_lock,
            )
            if not isinstance(methodology_delivery, TargetPortableMethodologyDelivery):
                _refuse("portable-publication-methodology-invalid", "direct target publisher returned an untyped delivery")
            # D604 accepts the actual target delivery directly.  It owns the
            # physical re-open of that returned carrier; converting it into a
            # candidate-shaped value here would discard the direct publisher's
            # exact typed result and invite reconstruction drift.
            proof_methodology_delivery = methodology_delivery
        candidate_mcp = admit_candidate_mcp_binding(
            root, package, target_context_sha256=context.sha256,
            prospective_package_selector=package_selector, prospective_runtime_selector=runtime_selector,
        )
        proof_request = CandidateNativeInstallationProofRequest(
            package=package, target_context=context, command_stage=stage,
            prospective_package_selector=package_selector, prospective_selector=runtime_selector,
            full_gate_packet=full_gate_packet, methodology_delivery=proof_methodology_delivery,
        )
        proof = stage_candidate_native_installation_proof(proof_request, lock=concrete_lock)
        ca_skill_publication = _prepare_and_publish_ca_skill(
            root,
            package=package,
            target_context=context,
            candidate_mcp_binding=candidate_mcp,
            lock=concrete_lock,
        )
        return PreparedNativePublication(
            package=package, target_context=context, candidate_proof_request=proof_request,
            candidate_proof=proof, methodology_delivery=methodology_delivery, candidate_mcp_binding=candidate_mcp,
            prospective_package_selector=package_selector, prospective_runtime_selector=runtime_selector,
            old_package_selector=old_package_selector,
            old_execution_selector=old_execution_selector,
            native_predecessor=native_predecessor,
            legacy_replacement=legacy_replacement,
            ca_skill_publication=ca_skill_publication,
        )
    except BaseException:
        coverage = (
            legacy_replacement.process_coverage
            if legacy_replacement is not None
            else getattr(native_predecessor, "_process_coverage", None)
        )
        if coverage is not None:
            _close_process_coverage(coverage, suppress_errors=True)
        raise


def publish_direct_native_runtime(
    command_result: object,
    prepared: PreparedNativePublication,
    *,
    lock: InstallationPublicationLock,
) -> PublishedNativeRuntime:
    """Use one already-started, physically reopened direct O-200 command.

    This is deliberately a thin authority adapter over
    :func:`publish_prepared_native_runtime`: O-200 command construction/start
    remains in ``framework_installation_command`` and the common cut-over is
    exactly the same one a selected O-169 provider may call under its own
    authority.  The caller must still record the Journal terminal outcome from
    the returned actual carriers.
    """

    try:
        from framework_installation_command import (
            COMMAND_DIRECTORY,
            FrameworkInstallationCommandResult,
            read_framework_installation_command_receipt,
        )
    except ImportError as error:  # pragma: no cover - release package routing failure.
        raise PortableRuntimePublicationError(
            "portable-publication-command-unavailable", "direct O-200 command reader is unavailable"
        ) from error
    if not isinstance(command_result, FrameworkInstallationCommandResult):
        _refuse("portable-publication-command-invalid", "direct publication requires a typed O-200 command result")
    concrete_lock, root = _root(lock)
    if not isinstance(prepared, PreparedNativePublication):
        _refuse("portable-publication-preparation-invalid", "publication requires typed prepared facts")
    if command_result.target_context != prepared.target_context or command_result.package != prepared.package:
        _refuse("portable-publication-command-stale", "O-200 command no longer binds the prepared package/context")
    if concrete_lock.operation != "install_framework_runtime":
        _refuse("portable-publication-command-stale", "direct O-200 requires its exact installation lock operation")
    if concrete_lock.command_sha256 != command_result.command_receipt.sha256:
        _refuse("portable-publication-command-stale", "installation lock names another O-200 command")
    try:
        receipt_relative = command_result.command_receipt_path.relative_to(root)
        if receipt_relative != COMMAND_DIRECTORY / f"{command_result.command_receipt.sha256}.json":
            _refuse("portable-publication-command-invalid", "O-200 command receipt is not at its canonical digest path")
        receipt_payload = command_result.command_receipt_path.read_bytes()
        reopened_receipt = read_framework_installation_command_receipt(
            receipt_payload, expected_sha256=command_result.command_receipt.sha256
        )
    except (OSError, ValueError, RuntimeError) as error:
        raise PortableRuntimePublicationError(
            "portable-publication-command-invalid", "retained O-200 command cannot be physically reopened"
        ) from error
    _regular(root / receipt_relative, code="portable-publication-command-invalid")
    if reopened_receipt != command_result.command_receipt:
        _refuse("portable-publication-command-stale", "retained O-200 command differs from typed command result")
    started_run = command_result.action_start.get("run_id") if isinstance(command_result.action_start, dict) else None
    if not isinstance(started_run, str) or concrete_lock.owner_run_id != started_run:
        _refuse("portable-publication-command-stale", "installation lock is not owned by the actual O-200 Action Run")
    try:
        if command_result.action_session.read_recorded_action_start(started_run) != command_result.action_provenance:
            _refuse("portable-publication-command-stale", "O-200 Action start differs from retained command provenance")
    except RuntimeError as error:
        raise PortableRuntimePublicationError(
            "portable-publication-command-invalid", "O-200 Action start cannot be physically reopened"
        ) from error
    return publish_prepared_native_runtime(prepared, lock=concrete_lock)


def record_direct_publication_result(
    command_result: object,
    *,
    full_gate_effects: object,
    state_generation: int,
    effect_outcome: str,
    reason: str | None,
) -> dict[str, object]:
    """Delegate direct D604 result retention to the O200 command boundary.

    The shared publisher supplies only the closure it had already reopened
    before any cut-over.  It cannot manufacture packet locations from a
    digest, add observed paths, or replay the installation while recording.
    """

    try:
        from framework_installation_command import (
            FrameworkInstallationCommandError,
            record_direct_installation_result,
        )
    except ImportError as error:  # pragma: no cover
        raise PortableRuntimePublicationError("portable-publication-command-unavailable", "O-200 command reader is unavailable") from error
    try:
        return record_direct_installation_result(
            command_result,
            full_gate_effects=full_gate_effects,
            state_generation=state_generation,
            effect_outcome=effect_outcome,
            reason=reason,
        )
    except FrameworkInstallationCommandError as error:
        raise PortableRuntimePublicationError("portable-publication-result-invalid", str(error)) from error


def retained_publication_failure_reason(error: BaseException) -> str:
    """Return only vetted local diagnostics for a retained terminal result."""

    if isinstance(error, PortableRuntimePublicationError):
        if (
            error.code == "portable-publication-ca-skill-failed"
            and error.stage in _CA_SKILL_EFFECT_STAGES
            and error.relative_path == _CA_SKILL_TARGET.as_posix()
            and (error.os_errno is None or (not isinstance(error.os_errno, bool) and isinstance(error.os_errno, int)))
        ):
            return f"{error.code}; stage={error.stage}; errno={error.os_errno!r}; path={error.relative_path}"
        return error.code
    code = getattr(error, "code", None)
    if isinstance(code, str) and code and "\n" not in code and "\r" not in code and "\x00" not in code:
        return code
    return type(error).__name__


def execute_direct_native_runtime(
    command_result: object,
    prepared: PreparedNativePublication,
    *,
    lock: InstallationPublicationLock,
) -> DirectPublishedRuntime:
    """Publish once under O-200 and truthfully record its actual outcome."""

    if not isinstance(prepared, PreparedNativePublication):
        _refuse("portable-publication-preparation-invalid", "direct publication requires typed prepared facts")
    generation = getattr(prepared.candidate_proof, "state_generation", None)
    if isinstance(generation, bool) or not isinstance(generation, int) or generation < 1:
        _refuse("portable-publication-proof-invalid", "prepared D604 proof has no positive generation")
    try:
        from framework_installation_command import (
            FrameworkInstallationCommandError,
            prepare_direct_full_gate_effect_closure,
        )

        full_gate_effects = prepare_direct_full_gate_effect_closure(
            command_result,
            full_gate_packet=prepared.candidate_proof_request.full_gate_packet,
        )
    except (AttributeError, FrameworkInstallationCommandError) as error:
        raise PortableRuntimePublicationError(
            "portable-publication-full-gate-invalid",
            "direct O-200 cannot retain the original Full Gate closure before replacement",
        ) from error
    try:
        publication = publish_direct_native_runtime(command_result, prepared, lock=lock)
    except PortableRuntimePublicationError as error:
        _lock, root = _root(lock)
        package_current = root / _PACKAGE_SELECTOR
        expected_execution = prepared.old_execution_selector
        execution_selector_missing: bool | None = False
        if expected_execution is not None:
            try:
                execution_relative, execution_bytes = expected_execution
            except (TypeError, ValueError):
                execution_selector_missing = None
            else:
                if (
                    execution_relative not in {_RUNTIME_SELECTOR, _LEGACY_RUNTIME_SELECTOR}
                    or not isinstance(execution_bytes, bytes)
                ):
                    # A malformed retained predecessor prevents knowing
                    # whether deletion began.  It must not be reported as a
                    # pre-delete block.
                    execution_selector_missing = None
                else:
                    execution_current = root / execution_relative
                    execution_selector_missing = (
                        not execution_current.exists() and not execution_current.is_symlink()
                    )
        predecessor_removed = (
            prepared.old_package_selector is not None
            and not package_current.exists()
            and not package_current.is_symlink()
            and execution_selector_missing is True
        )
        selectors_present = (
            package_current.exists()
            and expected_execution is not None
            and execution_selector_missing is False
        )
        new_package_present = (root / _RELEASES / prepared.package.manifest_digest).is_dir()
        outcome = (
            "effect_uncertain" if selectors_present or execution_selector_missing is None
            else "unavailable_after_delete" if (
                predecessor_removed or new_package_present or execution_selector_missing is True
            )
            else "blocked_before_delete"
        )
        recording = record_direct_publication_result(
            command_result,
            full_gate_effects=full_gate_effects,
            state_generation=generation,
            effect_outcome=outcome,
            reason=retained_publication_failure_reason(error),
        )
        if recording.get("state") == "recorded":
            lock.release("partial" if outcome == "unavailable_after_delete" else "blocked")
        return DirectPublishedRuntime(publication=None, recording=recording)
    recording = record_direct_publication_result(
        command_result,
        full_gate_effects=full_gate_effects,
        state_generation=generation,
        effect_outcome="completed",
        reason=None,
    )
    if recording.get("state") == "recorded":
        lock.release("completed")
    return DirectPublishedRuntime(publication=publication, recording=recording)


__all__ = [
    "PortableRuntimePublicationError",
    "PreparedNativePublication",
    "LegacyReplacementPreparation",
    "PreparedCaSkillPublication",
    "DirectPublishedRuntime",
    "PublishedNativeRuntime",
    "publish_final_generation_proof",
    "build_prepared_native_publication",
    "publish_direct_native_runtime",
    "publish_prepared_native_runtime",
    "revalidate_prepared_native_predecessor",
    "record_direct_publication_result",
    "retained_publication_failure_reason",
    "execute_direct_native_runtime",
    "publish_replacement_package",
    "publish_selectors",
    "render_package_selector",
    "render_runtime_selector",
    "stage_replacement_package",
]
