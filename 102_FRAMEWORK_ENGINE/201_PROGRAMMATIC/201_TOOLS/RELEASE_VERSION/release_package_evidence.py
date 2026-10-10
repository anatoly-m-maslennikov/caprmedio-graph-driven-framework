"""Read-only package evidence binding for a later Release full-gate consumer.

The adapter has one deliberately small job: reopen one already-produced
package against one current sealed candidate/compilation and expose the exact
package identity and test-phase projection.  It neither stages a legacy
package nor prepares a portable package, and it never aggregates gate inputs
into a pass/fail claim.
"""

from __future__ import annotations

import hashlib
from dataclasses import dataclass
from pathlib import Path
from typing import Literal

from release_contract import ReleaseContractError, ValidatedCandidate
from release_handoff import CANONICAL_SOURCE_RELATIVE, SealedCandidateCompilation, _revalidate
from release_packaging import MANIFEST_NAME, _complete_rows, _render_manifest, _verify_release
from release_portable_contract import (
    SealedPortableCandidateCompilation,
    revalidate_sealed_portable_compilation,
)
from release_portable_package import (
    PreparedPortableReleasePackage,
    reopen_portable_release_package,
)
from release_test_phases import ReleaseTestPhaseMap, derive_test_phase_map, derive_test_phase_map_from_rows


_SHA256 = frozenset("0123456789abcdef")
_LEGACY_RELEASE_ROOT = Path(".caprmedio_runtime/framework/releases")
_PORTABLE_RESOURCE_ROLE = {
    "FRAMEWORK_ENGINE": "engine",
    "SKILL": "skill",
    "DEPENDENCY": "dependency",
    "PACKAGE_CONTROL": "version",
    "CATALOG": "catalog",
    "SOURCE_ADMISSION": "source-admission",
    "DEFAULT": "default",
    "METHODOLOGY": "methodology",
    "METHODOLOGY_SUPPORT": "methodology-support",
    "BINDING_PROJECTION": "binding-projection",
}


class PackageEvidenceError(ReleaseContractError):
    """The package/candidate binding cannot be physically reopened."""


@dataclass(frozen=True)
class PackageMemberEvidence:
    """One normalized physical package member for a later copy/canary consumer."""

    path: str
    sha256: str
    mode: int
    role: str


@dataclass(frozen=True)
class PackageEvidenceView:
    """Frozen, read-only package identity for one later full-gate algorithm.

    This is package evidence only.  It intentionally has no gate receipt,
    execution result, aggregate fields, or ``passed`` property.
    """

    package_schema: Literal["legacy-2", "portable-1"]
    candidate_snapshot_manifest_sha256: str
    actual_package_manifest_sha256: str
    source_catalog_sha256: str | None
    candidate_run_id: str | None
    input_manifest_sha256: str | None
    framework_version: str
    version_toml_sha256: str
    package_root: Path
    member_inventory: tuple[PackageMemberEvidence, ...]
    phase_map: ReleaseTestPhaseMap


@dataclass(frozen=True)
class _PhaseRow:
    """The two attested fields consumed by the shared phase projection."""

    source_path: str
    sha256: str


def _error(code: str, message: str) -> PackageEvidenceError:
    return PackageEvidenceError(code, message)


def _sha256(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def _is_sha256(value: object) -> bool:
    return isinstance(value, str) and len(value) == 64 and set(value) <= _SHA256


def _project_root(candidate: ValidatedCandidate) -> Path:
    try:
        root = Path(candidate.project_root).resolve(strict=True)
    except OSError as error:
        raise _error("package-evidence-project-unavailable", "candidate Project root is unavailable") from error
    if root.is_symlink() or not root.is_dir():
        raise _error("package-evidence-project-unavailable", "candidate Project root is not a real directory")
    return root


def _physical_manifest_digest(package_root: Path) -> str:
    manifest = package_root / MANIFEST_NAME
    if package_root.is_symlink() or not package_root.is_dir() or manifest.is_symlink() or not manifest.is_file():
        raise _error("package-evidence-package-unavailable", "package has no regular manifest.toml")
    try:
        manifest.resolve(strict=True).relative_to(package_root.resolve(strict=True))
        return _sha256(manifest.read_bytes())
    except (OSError, ValueError) as error:
        raise _error("package-evidence-package-unavailable", "package manifest cannot be physically reopened") from error


def _phase_map(candidate: ValidatedCandidate, rows: tuple[object, ...]) -> ReleaseTestPhaseMap:
    package_map = derive_test_phase_map_from_rows(rows)
    inventory_map = derive_test_phase_map(candidate)
    if package_map != inventory_map:
        raise _error(
            "package-evidence-phase-map-mismatch",
            "reopened package rows do not match the sealed candidate test inventory",
        )
    return package_map


def _legacy_view(candidate: ValidatedCandidate, compilation: SealedCandidateCompilation) -> PackageEvidenceView:
    if compilation.candidate_snapshot_manifest_sha256 != candidate.manifest.sha256:
        raise _error("package-evidence-candidate-mismatch", "legacy compilation binds a different candidate")
    if compilation.authority != candidate.authority:
        raise _error("package-evidence-authority-mismatch", "legacy compilation authority differs from the candidate")
    root = _project_root(candidate)
    try:
        candidate_sha, rows, _selector_before = _complete_rows(root, compilation)
    except ReleaseContractError:
        raise
    except Exception as error:
        code = getattr(error, "code", "package-evidence-legacy-invalid")
        raise _error(str(code), "legacy package inputs could not be physically revalidated") from error
    if candidate_sha != candidate.manifest.sha256:
        raise _error("package-evidence-candidate-mismatch", "legacy package validator returned a different candidate")
    manifest_text = _render_manifest(
        candidate_sha,
        rows,
        framework_version=compilation.framework_version,
        version_toml_sha256=compilation.version_toml_sha256,
    )
    package_root = root / _LEGACY_RELEASE_ROOT / candidate_sha
    try:
        _verify_release(
            package_root,
            manifest_text,
            rows,
            framework_version=compilation.framework_version,
            version_toml_sha256=compilation.version_toml_sha256,
        )
    except Exception as error:
        code = getattr(error, "code", "package-evidence-legacy-unavailable")
        raise _error(str(code), "staged schema-2 package could not be physically reopened") from error
    actual_manifest = _physical_manifest_digest(package_root)
    expected_manifest = _sha256(manifest_text.encode("utf-8"))
    if actual_manifest != expected_manifest:
        raise _error("package-evidence-manifest-drift", "physical legacy package manifest differs from its exact validator input")
    return PackageEvidenceView(
        package_schema="legacy-2",
        candidate_snapshot_manifest_sha256=candidate_sha,
        actual_package_manifest_sha256=actual_manifest,
        source_catalog_sha256=None,
        candidate_run_id=None,
        input_manifest_sha256=None,
        framework_version=compilation.framework_version,
        version_toml_sha256=compilation.version_toml_sha256,
        package_root=package_root,
        member_inventory=_legacy_member_inventory(tuple(rows)),
        phase_map=_phase_map(candidate, tuple(rows)),
    )


def _portable_phase_rows(compilation: SealedPortableCandidateCompilation) -> tuple[object, ...]:
    """Restore candidate-origin paths without arbitrary duplicate suppression.

    The private export uses a candidate-local source root for Methodology and
    support files, while a portable package contains the ca Skill once inside
    the Engine and once as its typed ``SKILL`` projection.  Only that typed
    projection is ignored; every other duplicate reaches the shared phase
    validator and is refused there.
    """

    export_root = Path(compilation.private_compilation.methodology_export.source_export_root)
    canonical_root = Path(CANONICAL_SOURCE_RELATIVE)
    normalized: list[_PhaseRow] = []
    for raw in compilation.portable_package_rows:
        resource = getattr(raw, "resource", None)
        source_path = getattr(raw, "source_path", None)
        digest = getattr(raw, "sha256", None)
        if not isinstance(resource, str) or not isinstance(source_path, str) or not _is_sha256(digest):
            raise _error("package-evidence-portable-row-invalid", "portable compilation row is not typed")
        if resource == "SKILL":
            continue
        source = Path(source_path)
        if resource in {"METHODOLOGY", "METHODOLOGY_SUPPORT"}:
            try:
                source = canonical_root / source.relative_to(export_root)
            except ValueError as error:
                raise _error(
                    "package-evidence-portable-origin-invalid",
                    "private Methodology/support row is outside its sealed export source root",
                ) from error
        normalized.append(_PhaseRow(source.as_posix(), digest))
    return tuple(normalized)


def _portable_inventory_projection(
    compilation: SealedPortableCandidateCompilation,
) -> tuple[PackageMemberEvidence, ...]:
    """Project sealed portable rows into the verifier's package inventory.

    A content-addressed package may be internally valid yet still be a package
    for another set of source rows.  Catalog/version equality is therefore not
    enough: the reopened verifier inventory must exactly match each sealed
    portable destination, digest, mode, and typed package role.
    """

    projection: list[PackageMemberEvidence] = []
    for raw in compilation.portable_package_rows:
        resource = getattr(raw, "resource", None)
        destination = getattr(raw, "destination_path", None)
        digest = getattr(raw, "sha256", None)
        mode = getattr(raw, "mode", None)
        role = _PORTABLE_RESOURCE_ROLE.get(resource) if isinstance(resource, str) else None
        if (
            not isinstance(destination, str)
            or not destination
            or not _is_sha256(digest)
            or type(mode) is not int
            or not 0 <= mode <= 0o777
            or role is None
        ):
            raise _error("package-evidence-portable-row-invalid", "portable inventory row is not typed")
        projection.append(PackageMemberEvidence(destination, digest, mode, role))
    expected = tuple(sorted(projection, key=lambda row: row.path))
    if len({row.path for row in expected}) != len(expected):
        raise _error("package-evidence-portable-row-invalid", "portable inventory has duplicate destinations")
    return expected


def _assert_portable_inventory(
    package: object,
    compilation: SealedPortableCandidateCompilation,
) -> tuple[PackageMemberEvidence, ...]:
    expected = _portable_inventory_projection(compilation)
    inventory = getattr(package, "inventory", None)
    if not isinstance(inventory, tuple):
        raise _error("package-evidence-portable-package-invalid", "reopened portable package has no typed inventory")
    observed: list[PackageMemberEvidence] = []
    for row in inventory:
        path = getattr(row, "path", None)
        digest = getattr(row, "sha256", None)
        mode = getattr(row, "mode", None)
        role = getattr(row, "role", None)
        if (
            not isinstance(path, str)
            or not path
            or not _is_sha256(digest)
            or type(mode) is not int
            or not 0 <= mode <= 0o777
            or not isinstance(role, str)
        ):
            raise _error("package-evidence-portable-package-invalid", "reopened portable package inventory is invalid")
        observed.append(PackageMemberEvidence(path, digest, mode, role))
    observed_normalized = tuple(sorted(observed, key=lambda row: row.path))
    if observed_normalized != expected:
        raise _error(
            "package-evidence-portable-inventory-mismatch",
            "reopened portable package inventory differs from the sealed portable rows",
        )
    return observed_normalized


def _legacy_member_inventory(rows: tuple[object, ...]) -> tuple[PackageMemberEvidence, ...]:
    members: list[PackageMemberEvidence] = []
    for row in rows:
        resource = getattr(row, "resource", None)
        destination = getattr(row, "destination_path", None)
        digest = getattr(row, "sha256", None)
        mode = getattr(row, "mode", None)
        role = _PORTABLE_RESOURCE_ROLE.get(resource) if isinstance(resource, str) else None
        if (
            not isinstance(destination, str)
            or not destination
            or not _is_sha256(digest)
            or type(mode) is not int
            or not 0 <= mode <= 0o777
            or role is None
        ):
            raise _error("package-evidence-legacy-row-invalid", "legacy package row is not typed")
        members.append(PackageMemberEvidence(destination, digest, mode, role))
    ordered = tuple(sorted(members, key=lambda row: row.path))
    if len({row.path for row in ordered}) != len(ordered):
        raise _error("package-evidence-legacy-row-invalid", "legacy package inventory has duplicate destinations")
    return ordered


def _portable_view(
    candidate: ValidatedCandidate,
    compilation: SealedPortableCandidateCompilation,
    prepared_package: PreparedPortableReleasePackage | None,
) -> PackageEvidenceView:
    if prepared_package is None:
        raise _error("package-evidence-portable-package-required", "portable evidence requires an actual prepared package receipt")
    if not isinstance(prepared_package, PreparedPortableReleasePackage):
        raise _error("package-evidence-portable-package-untrusted", "portable evidence requires a typed prepared package receipt")
    try:
        current = revalidate_sealed_portable_compilation(compilation)
    except ReleaseContractError:
        raise
    except Exception as error:
        code = getattr(error, "code", "package-evidence-portable-invalid")
        raise _error(str(code), "portable compilation could not be physically revalidated") from error
    if current.candidate != candidate:
        raise _error("package-evidence-candidate-mismatch", "portable compilation belongs to a different candidate")
    if (
        prepared_package.candidate_run_id != current.candidate_run_id
        or prepared_package.candidate_snapshot_manifest_sha256 != candidate.manifest.sha256
        or prepared_package.input_manifest_sha256 != current.input_manifest_sha256
    ):
        raise _error("package-evidence-portable-receipt-mismatch", "prepared portable package does not bind the sealed compilation")
    try:
        package = reopen_portable_release_package(
            _project_root(candidate), current.candidate_run_id, prepared_package.package_manifest_sha256,
        )
    except Exception as error:
        code = getattr(error, "code", "package-evidence-portable-package-stale")
        raise _error(str(code), "portable package could not be physically reopened") from error
    if package != prepared_package.package:
        raise _error("package-evidence-portable-reopen-mismatch", "reopened portable package differs from the prepared receipt")
    actual_manifest = _physical_manifest_digest(package.root)
    if actual_manifest != package.manifest_digest:
        raise _error("package-evidence-manifest-drift", "portable package manifest bytes differ from its verified identity")
    if (
        package.framework_version != current.framework_version
        or package.version_toml_sha256 != current.version_toml_sha256
        or package.source_catalog_sha256 != current.source_catalog_sha256
    ):
        raise _error("package-evidence-portable-package-mismatch", "portable package version/catalog binding differs from its sealed inputs")
    members = _assert_portable_inventory(package, current)
    return PackageEvidenceView(
        package_schema="portable-1",
        candidate_snapshot_manifest_sha256=candidate.manifest.sha256,
        actual_package_manifest_sha256=actual_manifest,
        source_catalog_sha256=current.source_catalog_sha256,
        candidate_run_id=current.candidate_run_id,
        input_manifest_sha256=current.input_manifest_sha256,
        framework_version=current.framework_version,
        version_toml_sha256=current.version_toml_sha256,
        package_root=package.root,
        member_inventory=members,
        phase_map=_phase_map(candidate, _portable_phase_rows(current)),
    )


def bind_package_evidence(
    candidate: ValidatedCandidate,
    compilation: SealedCandidateCompilation | SealedPortableCandidateCompilation,
    *,
    prepared_package: PreparedPortableReleasePackage | None = None,
) -> PackageEvidenceView:
    """Bind one physical package to a current candidate without a gate claim."""

    try:
        current_candidate = _revalidate(candidate)
    except ReleaseContractError:
        raise
    except Exception as error:
        code = getattr(error, "code", "package-evidence-candidate-invalid")
        raise _error(str(code), "candidate could not be physically revalidated") from error
    if isinstance(compilation, SealedCandidateCompilation):
        if prepared_package is not None:
            raise _error("package-evidence-schema-mismatch", "legacy schema-2 evidence does not accept a portable package receipt")
        return _legacy_view(current_candidate, compilation)
    if isinstance(compilation, SealedPortableCandidateCompilation):
        return _portable_view(current_candidate, compilation, prepared_package)
    raise _error("package-evidence-compilation-untrusted", "package evidence requires one typed legacy or portable compilation")


def verify_bound_package_evidence(
    candidate: ValidatedCandidate,
    compilation: SealedCandidateCompilation | SealedPortableCandidateCompilation,
    view: PackageEvidenceView,
    *,
    prepared_package: PreparedPortableReleasePackage | None = None,
) -> PackageEvidenceView:
    """Rebuild one physical package binding before accepting a supplied view.

    A frozen dataclass is not authority: callers can construct or replace one.
    The return value is the freshly observed binding, never the caller object.
    """

    if not isinstance(view, PackageEvidenceView):
        raise _error("package-evidence-view-untrusted", "package evidence view must be typed")
    observed = bind_package_evidence(candidate, compilation, prepared_package=prepared_package)
    if observed != view:
        raise _error("package-evidence-view-mismatch", "supplied package evidence differs from the current physical binding")
    return observed


__all__ = [
    "PackageEvidenceError",
    "PackageEvidenceView",
    "PackageMemberEvidence",
    "bind_package_evidence",
    "verify_bound_package_evidence",
]
