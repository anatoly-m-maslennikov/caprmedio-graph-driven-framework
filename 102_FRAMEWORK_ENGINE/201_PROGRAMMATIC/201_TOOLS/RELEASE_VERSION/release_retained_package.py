"""Retain and reopen one immutable schema-1 native-package evidence sidecar.

The sidecar is a D597 proof carrier beside a private candidate package.  It is
not part of the closed Framework package inventory and it confers no gate,
release, installation, promotion, runtime, image, or Workflow authority.
"""

from __future__ import annotations

from dataclasses import dataclass
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import re
import stat
import sys
import tempfile
from typing import Mapping


_TOOLS_ROOT = Path(__file__).resolve().parents[1]
if str(_TOOLS_ROOT) not in sys.path:
    sys.path.insert(0, str(_TOOLS_ROOT))

from framework_package import FrameworkPackageError, verify_framework_package  # noqa: E402
from release_contract import ReleaseContractError, ValidatedCandidate, canonical_json  # noqa: E402
from release_handoff import CANONICAL_SOURCE_RELATIVE  # noqa: E402
from release_inventory import ReleaseInventoryError, refuse_secret_path  # noqa: E402
from release_package_evidence import (  # noqa: E402
    PackageEvidenceError,
    PackageEvidenceView,
    PackageMemberEvidence,
    bind_package_evidence,
    verify_bound_package_evidence,
)
from release_portable_contract import SealedPortableCandidateCompilation  # noqa: E402
from release_portable_package import PreparedPortableReleasePackage  # noqa: E402
from release_test_phases import ReleaseTestPhaseMap, derive_test_phase_map_from_rows  # noqa: E402


SCHEMA_VERSION = 1
PACKAGE_SCHEMA = "portable-1"
SIDE_CAR_DIRECTORY = Path("package_evidence")
_SHA256 = re.compile(r"[0-9a-f]{64}\Z")
_PHASES = frozenset({"unit", "candidate_e2e"})
_SIDE_CAR_KEYS = frozenset(
    {
        "schema_version",
        "package_schema",
        "candidate_snapshot_manifest_sha256",
        "package_manifest_sha256",
        "source_catalog_sha256",
        "candidate_run_id",
        "input_manifest_sha256",
        "framework_version",
        "version_toml_sha256",
        "member_inventory",
        "test_bindings",
        "phase_map_sha256",
    }
)
_MEMBER_KEYS = frozenset({"path", "sha256", "mode", "role"})
_TEST_BINDING_KEYS = frozenset({"source_path", "package_path", "sha256", "phase"})


class RetainedNativePackageError(ReleaseContractError):
    """Stable refusal from the D597 retained native-package evidence boundary."""


@dataclass(frozen=True)
class RetainedNativePackageEvidence:
    """A detached, reopened package identity and its content-addressed sidecar."""

    view: PackageEvidenceView
    receipt_sha256: str
    receipt_path: Path


@dataclass(frozen=True)
class _TestBinding:
    source_path: str
    package_path: str
    sha256: str
    phase: str

    def record(self) -> dict[str, object]:
        return {
            "source_path": self.source_path,
            "package_path": self.package_path,
            "sha256": self.sha256,
            "phase": self.phase,
        }


@dataclass(frozen=True)
class _PhaseRow:
    source_path: str
    sha256: str


def _error(code: str, message: str) -> RetainedNativePackageError:
    return RetainedNativePackageError(code, message)


def _sha256(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def _is_sha256(value: object) -> bool:
    return isinstance(value, str) and _SHA256.fullmatch(value) is not None


def _require_sha256(value: object, *, field: str, code: str) -> str:
    if not _is_sha256(value):
        raise _error(code, f"{field} must be a lowercase SHA-256")
    return value


def _safe_relative(value: object, *, field: str, code: str) -> str:
    if not isinstance(value, str) or not value or "\\" in value:
        raise _error(code, f"{field} must be a safe package-relative path")
    path = PurePosixPath(value)
    if path.is_absolute() or path == PurePosixPath(".") or any(part in {"", ".", ".."} for part in path.parts):
        raise _error(code, f"{field} is unsafe")
    if path.as_posix() != value:
        raise _error(code, f"{field} is not normalized")
    try:
        refuse_secret_path(value)
    except ReleaseInventoryError as error:
        raise _error(error.code, str(error)) from error
    return value


def _run_id(value: object, *, code: str) -> str:
    if not isinstance(value, str) or not value or "\\" in value or Path(value).name != value or value in {".", ".."}:
        raise _error(code, "candidate run id must be one safe path component")
    try:
        refuse_secret_path(value)
    except ReleaseInventoryError as error:
        raise _error(error.code, str(error)) from error
    return value


def _canonical_json(value: object) -> bytes:
    try:
        return canonical_json(value)
    except (TypeError, ValueError) as error:
        raise _error("retained-package-sidecar-invalid", "sidecar cannot be rendered canonically") from error


def _project_root(candidate: ValidatedCandidate) -> Path:
    try:
        root = Path(candidate.project_root).resolve(strict=True)
    except OSError as error:
        raise _error("retained-package-project-unavailable", "candidate project root is unavailable") from error
    if root.is_symlink() or not root.is_dir():
        raise _error("retained-package-project-invalid", "candidate project root must be a real directory")
    return root


def _candidate_root(root: Path, run_id: str) -> Path:
    candidate_root = root / ".caprmedio_tmp" / "release_candidates" / run_id
    if candidate_root.is_symlink() or not candidate_root.is_dir():
        raise _error("retained-package-candidate-missing", "private candidate root is unavailable")
    return candidate_root


def _member_inventory_from_view(view: PackageEvidenceView) -> tuple[PackageMemberEvidence, ...]:
    members = view.member_inventory
    if not isinstance(members, tuple) or not members:
        raise _error("retained-package-view-invalid", "package evidence has no complete inventory")
    normalized: list[PackageMemberEvidence] = []
    for member in members:
        path = _safe_relative(getattr(member, "path", None), field="package member path", code="retained-package-view-invalid")
        digest = _require_sha256(getattr(member, "sha256", None), field="package member digest", code="retained-package-view-invalid")
        mode = getattr(member, "mode", None)
        role = getattr(member, "role", None)
        if type(mode) is not int or not 0 <= mode <= 0o777 or not isinstance(role, str) or not role:
            raise _error("retained-package-view-invalid", "package member metadata is invalid")
        normalized.append(PackageMemberEvidence(path, digest, mode, role))
    ordered = tuple(sorted(normalized, key=lambda member: member.path))
    if tuple(normalized) != ordered or len({member.path for member in ordered}) != len(ordered):
        raise _error("retained-package-view-invalid", "package evidence inventory must be path-ordered and unique")
    return ordered


def _normalized_source_path(
    compilation: SealedPortableCandidateCompilation,
    *,
    resource: str,
    source_path: object,
) -> str:
    source = _safe_relative(source_path, field="sealed source path", code="retained-package-binding-invalid")
    if resource not in {"METHODOLOGY", "METHODOLOGY_SUPPORT"}:
        return source
    export_root = Path(compilation.private_compilation.methodology_export.source_export_root)
    canonical_root = Path(CANONICAL_SOURCE_RELATIVE)
    try:
        normalized = canonical_root / Path(source).relative_to(export_root)
    except ValueError as error:
        raise _error(
            "retained-package-origin-invalid",
            "private Methodology/support source is outside the sealed export root",
        ) from error
    return _safe_relative(
        normalized.as_posix(),
        field="normalized Methodology source path",
        code="retained-package-origin-invalid",
    )


def _is_test_module(path: str) -> bool:
    return PurePosixPath(path).name.startswith("test_") and path.endswith(".py")


def _expected_test_source_path(package_path: str) -> str:
    """Restore the one permitted candidate-origin spelling for a package test.

    Core package resources retain their project-relative path.  The two
    Methodology projections are copied from a private export, so the retained
    sidecar records their canonical Methodology origin rather than that
    candidate-local export path.  This is deliberately derivable from the
    package path alone: detached reopening has no compilation authority.
    """

    package = PurePosixPath(
        _safe_relative(
            package_path,
            field="package test path",
            code="retained-package-test-origin-invalid",
        )
    )
    canonical_root = PurePosixPath(CANONICAL_SOURCE_RELATIVE)
    for projection in (PurePosixPath("methodology/active"), PurePosixPath("methodology/support")):
        if package.is_relative_to(projection):
            return (canonical_root / package.relative_to(projection)).as_posix()
    return package.as_posix()


def _require_test_binding_origin(source_path: str, package_path: str) -> None:
    if source_path != _expected_test_source_path(package_path):
        raise _error(
            "retained-package-test-origin-mismatch",
            "sidecar test source path does not match its package projection",
        )


def _test_bindings_from_live_view(
    compilation: SealedPortableCandidateCompilation,
    view: PackageEvidenceView,
) -> tuple[_TestBinding, ...]:
    """Project the sealed source-to-package test mapping without rediscovery."""

    members = {member.path: member for member in _member_inventory_from_view(view)}
    rows = getattr(compilation, "portable_package_rows", None)
    if not isinstance(rows, tuple) or not rows:
        raise _error("retained-package-compilation-invalid", "sealed portable compilation has no package rows")
    phase_rows: list[_PhaseRow] = []
    candidates: list[tuple[str, str, str]] = []
    for row in rows:
        resource = getattr(row, "resource", None)
        source_path = getattr(row, "source_path", None)
        package_path = getattr(row, "destination_path", None)
        digest = getattr(row, "sha256", None)
        if not isinstance(resource, str):
            raise _error("retained-package-compilation-invalid", "sealed package row resource is invalid")
        # This is the one deliberate duplicate exclusion: the separately typed
        # SKILL projection repeats canonical ca bytes already carried by Engine.
        if resource == "SKILL":
            continue
        source = _normalized_source_path(compilation, resource=resource, source_path=source_path)
        package = _safe_relative(package_path, field="sealed package path", code="retained-package-binding-invalid")
        checksum = _require_sha256(digest, field="sealed package source digest", code="retained-package-binding-invalid")
        phase_rows.append(_PhaseRow(source, checksum))
        if _is_test_module(source):
            _require_test_binding_origin(source, package)
            candidates.append((source, package, checksum))
    try:
        phase_map = derive_test_phase_map_from_rows(tuple(phase_rows))
    except ReleaseContractError as error:
        raise _error(error.code, str(error)) from error
    if phase_map != view.phase_map:
        raise _error("retained-package-phase-map-mismatch", "live package view phase projection differs from sealed package rows")
    phases = {path: (checksum, phase) for path, checksum, phase in phase_map.rows}
    bindings: list[_TestBinding] = []
    for source, package, checksum in candidates:
        phase_entry = phases.get(source)
        member = members.get(package)
        if phase_entry is None or phase_entry[0] != checksum:
            raise _error("retained-package-test-binding-invalid", "sealed test row is absent from the phase map")
        if member is None or member.sha256 != checksum or member.role == "skill" or not _is_test_module(member.path):
            raise _error("retained-package-test-binding-invalid", "sealed test row differs from the physical package")
        bindings.append(_TestBinding(source, package, checksum, phase_entry[1]))
    ordered = tuple(sorted(bindings, key=lambda binding: binding.source_path))
    if tuple(bindings) != ordered or len({binding.source_path for binding in ordered}) != len(ordered):
        raise _error("retained-package-test-binding-invalid", "test bindings must be source-path ordered and unique")
    if len({binding.package_path for binding in ordered}) != len(ordered):
        raise _error("retained-package-test-binding-invalid", "test bindings cannot repeat a package member")
    package_tests = {
        member.path
        for member in members.values()
        if member.role != "skill" and _is_test_module(member.path)
    }
    if {binding.package_path for binding in ordered} != package_tests:
        raise _error("retained-package-test-projection-mismatch", "test bindings do not cover the complete non-Skill package test projection")
    return ordered


def _sidecar_document(
    view: PackageEvidenceView,
    bindings: tuple[_TestBinding, ...],
) -> dict[str, object]:
    if view.package_schema != PACKAGE_SCHEMA:
        raise _error("retained-package-schema-mismatch", "retained native evidence requires a schema-1 package")
    catalog = _require_sha256(view.source_catalog_sha256, field="source catalog", code="retained-package-view-invalid")
    run_id = _run_id(view.candidate_run_id, code="retained-package-view-invalid")
    input_manifest = _require_sha256(view.input_manifest_sha256, field="input manifest", code="retained-package-view-invalid")
    candidate_manifest = _require_sha256(
        view.candidate_snapshot_manifest_sha256,
        field="candidate snapshot manifest",
        code="retained-package-view-invalid",
    )
    package_manifest = _require_sha256(
        view.actual_package_manifest_sha256,
        field="package manifest",
        code="retained-package-view-invalid",
    )
    version_digest = _require_sha256(view.version_toml_sha256, field="version carrier", code="retained-package-view-invalid")
    if not isinstance(view.framework_version, str) or not view.framework_version:
        raise _error("retained-package-view-invalid", "framework version is invalid")
    inventory = _member_inventory_from_view(view)
    return {
        "schema_version": SCHEMA_VERSION,
        "package_schema": PACKAGE_SCHEMA,
        "candidate_snapshot_manifest_sha256": candidate_manifest,
        "package_manifest_sha256": package_manifest,
        "source_catalog_sha256": catalog,
        "candidate_run_id": run_id,
        "input_manifest_sha256": input_manifest,
        "framework_version": view.framework_version,
        "version_toml_sha256": version_digest,
        "member_inventory": [
            {"path": member.path, "sha256": member.sha256, "mode": member.mode, "role": member.role}
            for member in inventory
        ],
        "test_bindings": [binding.record() for binding in bindings],
        "phase_map_sha256": view.phase_map.sha256,
    }


def _reject_duplicate_pairs(pairs: list[tuple[str, object]]) -> dict[str, object]:
    result: dict[str, object] = {}
    for key, value in pairs:
        if key in result:
            raise _error("retained-package-sidecar-invalid", "sidecar contains duplicate object keys")
        result[key] = value
    return result


def _reject_json_constant(value: str) -> object:
    raise _error("retained-package-sidecar-invalid", f"sidecar contains a non-JSON value: {value}")


def _inspect_sidecar_path(path: Path) -> None:
    """Reject an aliased/protected path before opening a sidecar byte stream."""

    if not path.is_absolute() or any(part == ".." for part in path.parts):
        raise _error("retained-package-sidecar-path-invalid", "retained sidecar path must be absolute and lexical")
    try:
        refuse_secret_path(path)
    except ReleaseInventoryError as error:
        raise _error(error.code, str(error)) from error
    if path.parent.name != SIDE_CAR_DIRECTORY.name:
        raise _error("retained-package-sidecar-path-invalid", "retained sidecar must be directly below package_evidence")
    for ancestor in reversed(path.parents):
        try:
            metadata = os.lstat(ancestor)
        except OSError as error:
            raise _error("retained-package-sidecar-unavailable", "retained sidecar ancestor cannot be inspected") from error
        if stat.S_ISLNK(metadata.st_mode) or not stat.S_ISDIR(metadata.st_mode):
            raise _error("retained-package-sidecar-path-invalid", "retained sidecar ancestor is not a regular directory")
    try:
        metadata = os.lstat(path)
    except OSError as error:
        raise _error("retained-package-sidecar-unavailable", "retained sidecar cannot be inspected") from error
    if stat.S_ISLNK(metadata.st_mode) or not stat.S_ISREG(metadata.st_mode):
        raise _error("retained-package-sidecar-unavailable", "retained sidecar must be a regular file")


def _read_sidecar(path: Path, *, expected_sha256: str | None) -> tuple[dict[str, object], bytes, str]:
    _inspect_sidecar_path(path)
    try:
        raw = path.read_bytes()
    except OSError as error:
        raise _error("retained-package-sidecar-unavailable", "retained sidecar cannot be read") from error
    digest = _sha256(raw)
    if expected_sha256 is not None and digest != _require_sha256(
        expected_sha256,
        field="expected sidecar digest",
        code="retained-package-sidecar-digest-mismatch",
    ):
        raise _error("retained-package-sidecar-digest-mismatch", "retained sidecar bytes differ from the expected digest")
    if path.parent.name != SIDE_CAR_DIRECTORY.name or path.name != f"{digest}.json":
        raise _error("retained-package-sidecar-path-invalid", "retained sidecar path is not content addressed")
    try:
        document = json.loads(
            raw.decode("utf-8"),
            object_pairs_hook=_reject_duplicate_pairs,
            parse_constant=_reject_json_constant,
        )
    except RetainedNativePackageError:
        raise
    except (UnicodeDecodeError, json.JSONDecodeError) as error:
        raise _error("retained-package-sidecar-invalid", "retained sidecar is not valid UTF-8 JSON") from error
    if not isinstance(document, dict) or raw != _canonical_json(document):
        raise _error("retained-package-sidecar-noncanonical", "retained sidecar bytes are not canonical JSON")
    return document, raw, digest


def _parse_member_inventory(value: object) -> tuple[PackageMemberEvidence, ...]:
    if not isinstance(value, list) or not value:
        raise _error("retained-package-sidecar-invalid", "sidecar member inventory is missing")
    members: list[PackageMemberEvidence] = []
    for raw in value:
        if not isinstance(raw, Mapping) or set(raw) != _MEMBER_KEYS:
            raise _error("retained-package-sidecar-invalid", "sidecar member has an invalid closed schema")
        path = _safe_relative(raw.get("path"), field="sidecar member path", code="retained-package-sidecar-invalid")
        digest = _require_sha256(raw.get("sha256"), field="sidecar member digest", code="retained-package-sidecar-invalid")
        mode = raw.get("mode")
        role = raw.get("role")
        if type(mode) is not int or not 0 <= mode <= 0o777 or not isinstance(role, str) or not role:
            raise _error("retained-package-sidecar-invalid", "sidecar member metadata is invalid")
        members.append(PackageMemberEvidence(path, digest, mode, role))
    ordered = tuple(sorted(members, key=lambda member: member.path))
    if tuple(members) != ordered or len({member.path for member in ordered}) != len(ordered):
        raise _error("retained-package-sidecar-invalid", "sidecar member inventory must be path-ordered and unique")
    return ordered


def _parse_test_bindings(value: object, inventory: tuple[PackageMemberEvidence, ...]) -> tuple[_TestBinding, ...]:
    if not isinstance(value, list):
        raise _error("retained-package-sidecar-invalid", "sidecar test bindings are missing")
    members = {member.path: member for member in inventory}
    bindings: list[_TestBinding] = []
    for raw in value:
        if not isinstance(raw, Mapping) or set(raw) != _TEST_BINDING_KEYS:
            raise _error("retained-package-sidecar-invalid", "sidecar test binding has an invalid closed schema")
        source = _safe_relative(raw.get("source_path"), field="sidecar test source path", code="retained-package-sidecar-invalid")
        package = _safe_relative(raw.get("package_path"), field="sidecar test package path", code="retained-package-sidecar-invalid")
        digest = _require_sha256(raw.get("sha256"), field="sidecar test digest", code="retained-package-sidecar-invalid")
        phase = raw.get("phase")
        if not _is_test_module(source) or not isinstance(phase, str) or phase not in _PHASES:
            raise _error("retained-package-sidecar-invalid", "sidecar test binding is invalid")
        member = members.get(package)
        if member is None or member.role == "skill" or not _is_test_module(member.path) or member.sha256 != digest:
            raise _error("retained-package-test-projection-mismatch", "sidecar test binding differs from its package member")
        _require_test_binding_origin(source, package)
        bindings.append(_TestBinding(source, package, digest, phase))
    ordered = tuple(sorted(bindings, key=lambda binding: binding.source_path))
    if tuple(bindings) != ordered or len({binding.source_path for binding in ordered}) != len(ordered):
        raise _error("retained-package-sidecar-invalid", "sidecar test bindings must be source-path ordered and unique")
    if len({binding.package_path for binding in ordered}) != len(ordered):
        raise _error("retained-package-sidecar-invalid", "sidecar test bindings cannot repeat a package member")
    package_tests = {
        member.path
        for member in inventory
        if member.role != "skill" and _is_test_module(member.path)
    }
    if {binding.package_path for binding in ordered} != package_tests:
        raise _error("retained-package-test-projection-mismatch", "sidecar test bindings do not cover package tests")
    return ordered


def _phase_map(bindings: tuple[_TestBinding, ...]) -> ReleaseTestPhaseMap:
    try:
        phase_map = derive_test_phase_map_from_rows(
            tuple(_PhaseRow(binding.source_path, binding.sha256) for binding in bindings)
        )
    except ReleaseContractError as error:
        raise _error(error.code, str(error)) from error
    expected = {path: (digest, phase) for path, digest, phase in phase_map.rows}
    if any(expected.get(binding.source_path) != (binding.sha256, binding.phase) for binding in bindings):
        raise _error("retained-package-phase-map-mismatch", "sidecar test phases differ from the shared phase projection")
    return phase_map


def _view_from_reopened_package(
    package_root: Path,
    document: dict[str, object],
) -> tuple[PackageEvidenceView, tuple[_TestBinding, ...]]:
    if set(document) != _SIDE_CAR_KEYS:
        raise _error("retained-package-sidecar-invalid", "retained sidecar has an invalid closed schema")
    if type(document.get("schema_version")) is not int or document.get("schema_version") != SCHEMA_VERSION:
        raise _error("retained-package-sidecar-invalid", "retained sidecar schema version is invalid")
    if document.get("package_schema") != PACKAGE_SCHEMA:
        raise _error("retained-package-schema-mismatch", "retained sidecar does not name a schema-1 package")
    candidate_manifest = _require_sha256(
        document.get("candidate_snapshot_manifest_sha256"),
        field="sidecar candidate snapshot manifest",
        code="retained-package-sidecar-invalid",
    )
    package_manifest = _require_sha256(
        document.get("package_manifest_sha256"),
        field="sidecar package manifest",
        code="retained-package-sidecar-invalid",
    )
    catalog = _require_sha256(document.get("source_catalog_sha256"), field="sidecar catalog", code="retained-package-sidecar-invalid")
    run_id = _run_id(document.get("candidate_run_id"), code="retained-package-sidecar-invalid")
    input_manifest = _require_sha256(document.get("input_manifest_sha256"), field="sidecar input manifest", code="retained-package-sidecar-invalid")
    version_digest = _require_sha256(document.get("version_toml_sha256"), field="sidecar version carrier", code="retained-package-sidecar-invalid")
    framework_version = document.get("framework_version")
    if not isinstance(framework_version, str) or not framework_version:
        raise _error("retained-package-sidecar-invalid", "sidecar framework version is invalid")
    inventory = _parse_member_inventory(document.get("member_inventory"))
    bindings = _parse_test_bindings(document.get("test_bindings"), inventory)
    phase_map = _phase_map(bindings)
    if document.get("phase_map_sha256") != phase_map.sha256:
        raise _error("retained-package-phase-map-mismatch", "sidecar phase map digest is invalid")
    try:
        package = verify_framework_package(package_root)
    except FrameworkPackageError as error:
        raise _error(error.code, str(error)) from error
    observed_inventory = tuple(
        PackageMemberEvidence(member.path, member.sha256, member.mode, member.role)
        for member in package.inventory
    )
    if observed_inventory != inventory:
        raise _error("retained-package-inventory-mismatch", "sidecar inventory differs from the reopened package")
    if (
        package.manifest_digest != package_manifest
        or package.source_catalog_sha256 != catalog
        or package.framework_version != framework_version
        or package.version_toml_sha256 != version_digest
    ):
        raise _error("retained-package-package-mismatch", "sidecar bindings differ from the reopened package")
    return (
        PackageEvidenceView(
            package_schema=PACKAGE_SCHEMA,
            candidate_snapshot_manifest_sha256=candidate_manifest,
            actual_package_manifest_sha256=package_manifest,
            source_catalog_sha256=catalog,
            candidate_run_id=run_id,
            input_manifest_sha256=input_manifest,
            framework_version=framework_version,
            version_toml_sha256=version_digest,
            package_root=package.root,
            member_inventory=inventory,
            phase_map=phase_map,
        ),
        bindings,
    )


def _ensure_regular_directory(path: Path, *, code: str, label: str) -> None:
    if path.exists() or path.is_symlink():
        try:
            metadata = os.lstat(path)
        except OSError as error:
            raise _error(code, f"{label} cannot be inspected") from error
        if stat.S_ISLNK(metadata.st_mode) or not stat.S_ISDIR(metadata.st_mode):
            raise _error(code, f"{label} is not a regular directory")
        return
    try:
        path.mkdir(mode=0o755)
    except FileExistsError:
        _ensure_regular_directory(path, code=code, label=label)
    except OSError as error:
        raise _error(code, f"{label} cannot be created") from error


def _read_existing(path: Path, *, code: str) -> bytes | None:
    if not path.exists() and not path.is_symlink():
        return None
    try:
        metadata = os.lstat(path)
    except OSError as error:
        raise _error(code, "retained sidecar cannot be inspected") from error
    if stat.S_ISLNK(metadata.st_mode) or not stat.S_ISREG(metadata.st_mode):
        raise _error(code, "retained sidecar is not a regular file")
    try:
        return path.read_bytes()
    except OSError as error:
        raise _error(code, "retained sidecar cannot be read") from error


def _publish_exact(directory: Path, name: str, payload: bytes) -> None:
    target = directory / name
    existing = _read_existing(target, code="retained-package-sidecar-conflict")
    if existing is not None:
        if existing != payload:
            raise _error("retained-package-sidecar-conflict", "existing retained sidecar differs from this evidence")
        return
    descriptor, temporary_name = tempfile.mkstemp(prefix=f".{name}.", suffix=".next", dir=directory)
    temporary = Path(temporary_name)
    try:
        with os.fdopen(descriptor, "wb", closefd=True) as stream:
            stream.write(payload)
            stream.flush()
            os.fsync(stream.fileno())
        try:
            os.link(temporary, target)
        except FileExistsError:
            existing = _read_existing(target, code="retained-package-sidecar-conflict")
            if existing != payload:
                raise _error("retained-package-sidecar-conflict", "concurrent retained sidecar differs from this evidence")
        except OSError as error:
            raise _error("retained-package-sidecar-publish-failed", "retained sidecar cannot be atomically published") from error
    finally:
        try:
            temporary.unlink(missing_ok=True)
        except OSError:
            pass


def read_retained_native_package_evidence(
    package_root: Path | str,
    sidecar_path: Path | str,
    *,
    expected_sha256: str | None = None,
) -> RetainedNativePackageEvidence:
    """Reopen detached schema-1 package evidence without checkout authority.

    This reader never touches a current selector, candidate source checkout, or
    caller-provided sealed compilation.  It uses only the supplied native
    package bytes and sidecar bytes.
    """

    root = Path(package_root)
    sidecar = Path(sidecar_path)
    if not root.is_absolute() or not sidecar.is_absolute():
        raise _error("retained-package-path-invalid", "package root and sidecar path must be absolute")
    try:
        sidecar.relative_to(root)
    except ValueError:
        pass
    else:
        raise _error("retained-package-sidecar-path-invalid", "retained sidecar must remain outside the closed package tree")
    document, _payload, receipt_sha256 = _read_sidecar(sidecar, expected_sha256=expected_sha256)
    view, _bindings = _view_from_reopened_package(root, document)
    return RetainedNativePackageEvidence(view, receipt_sha256, sidecar)


def retain_native_package_evidence(
    candidate: ValidatedCandidate,
    compilation: SealedPortableCandidateCompilation,
    prepared_package: PreparedPortableReleasePackage,
) -> RetainedNativePackageEvidence:
    """Explicitly retain one current schema-1 package view beneath its candidate.

    A newly constructed view is not accepted.  The shared live binder first
    revalidates current candidate/source/package state, and repeats that exact
    rebind immediately before the only sidecar publication effect.
    """

    if not isinstance(compilation, SealedPortableCandidateCompilation):
        raise _error("retained-package-compilation-untrusted", "retention requires a typed schema-1 sealed compilation")
    if not isinstance(prepared_package, PreparedPortableReleasePackage):
        raise _error("retained-package-prepared-untrusted", "retention requires a typed prepared schema-1 package")
    try:
        view = bind_package_evidence(candidate, compilation, prepared_package=prepared_package)
        current = verify_bound_package_evidence(candidate, compilation, view, prepared_package=prepared_package)
    except (PackageEvidenceError, ReleaseContractError) as error:
        raise _error(error.code, str(error)) from error
    if current != view or view.package_schema != PACKAGE_SCHEMA:
        raise _error("retained-package-view-stale", "live package evidence changed before retention")
    root = _project_root(candidate)
    run_id = _run_id(view.candidate_run_id, code="retained-package-view-invalid")
    candidate_root = _candidate_root(root, run_id)
    expected_package_root = candidate_root / "package" / view.actual_package_manifest_sha256
    if view.package_root != expected_package_root:
        raise _error("retained-package-package-mismatch", "live package root is outside its private candidate location")
    bindings = _test_bindings_from_live_view(compilation, view)
    document = _sidecar_document(view, bindings)
    payload = _canonical_json(document)
    receipt_sha256 = _sha256(payload)
    try:
        final_view = verify_bound_package_evidence(candidate, compilation, view, prepared_package=prepared_package)
    except (PackageEvidenceError, ReleaseContractError) as error:
        raise _error(error.code, str(error)) from error
    if final_view != view:
        raise _error("retained-package-view-stale", "live package evidence changed before sidecar publication")
    evidence_directory = candidate_root / SIDE_CAR_DIRECTORY
    _ensure_regular_directory(
        evidence_directory,
        code="retained-package-sidecar-publish-failed",
        label="private package evidence directory",
    )
    receipt_path = evidence_directory / f"{receipt_sha256}.json"
    _publish_exact(evidence_directory, receipt_path.name, payload)
    retained = read_retained_native_package_evidence(
        view.package_root,
        receipt_path,
        expected_sha256=receipt_sha256,
    )
    if retained.view != view:
        raise _error("retained-package-reopen-mismatch", "retained sidecar differs from the live package evidence")
    return retained


__all__ = [
    "PACKAGE_SCHEMA",
    "RetainedNativePackageEvidence",
    "RetainedNativePackageError",
    "SIDE_CAR_DIRECTORY",
    "read_retained_native_package_evidence",
    "retain_native_package_evidence",
]
