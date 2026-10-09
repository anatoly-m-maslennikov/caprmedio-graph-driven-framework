"""Private, receipt-bound aggregation of the completed Release gates.

This module makes no release selection, image build, host command, or
promotion effect.  It reopens the durable Unit, image, and candidate-E2E
receipts and retains a small aggregate receipt only after their test reports
form one exact, non-overlapping phase partition.
"""

from __future__ import annotations

import hashlib
import os
import tempfile
import xml.etree.ElementTree as ET
from dataclasses import asdict, dataclass, replace
from pathlib import Path, PurePosixPath
from typing import TYPE_CHECKING, Literal

from release_contract import ReleaseContractError, ValidatedCandidate, canonical_json
from release_handoff import SealedCandidateCompilation
from release_inventory import ReleaseInventoryError, refuse_secret_path
from release_package_evidence import PackageEvidenceView, bind_package_evidence, verify_bound_package_evidence
from release_portable_contract import SealedPortableCandidateCompilation
from release_portable_package import PreparedPortableReleasePackage
from release_retained_package import (
    RetainedNativePackageEvidence,
    read_retained_native_package_evidence,
    retain_native_package_evidence,
)
from release_retained_candidate import RetainedCandidateIdentity, reopen_retained_candidate_identity
from release_suite import PortableSuiteGateEvidence, SuiteGateEvidence, verify_bound_suite_evidence
from release_test_phases import ReleaseTestPhaseMap, derive_test_phase_map, derive_test_phase_map_from_rows

if TYPE_CHECKING:
    from release_e2e_gate import CandidateE2EGateEvidence, PortableCandidateE2EGateEvidence
    from release_image import (ImageBuildEvidence, ImageVerificationEvidence,
                               PortableImageBuildEvidence, PortableImageVerificationEvidence)


EVIDENCE_ROOT = ".caprmedio_runtime/release_full_gate"
_SHA256_LENGTH = 64
_MAX_REPORT_BYTES = 8 * 1024 * 1024


@dataclass(frozen=True)
class FullGateEvidence:
    candidate_snapshot_manifest_sha256: str
    candidate_image_digest: str
    phase_map_sha256: str
    suite_receipt_sha256: str
    build_receipt_sha256: str
    image_receipt_sha256: str
    e2e_receipt_sha256: str
    outcome: Literal["passed", "failed", "incomplete", "stale", "recording_uncertain"]
    reason: str
    evidence_root: str
    receipt_sha256: str | None
    executed_tests: int
    framework_version: str = ""
    version_toml_sha256: str = ""

    @property
    def passed(self) -> bool:
        return self.outcome == "passed" and self.receipt_sha256 is not None


@dataclass(frozen=True)
class NativeFullGateEvidence:
    """Schema-1 aggregate receipt bound to one reopened portable package.

    It is deliberately separate from :class:`FullGateEvidence`: legacy
    schema-2 receipts retain their established canonical fieldset and are not
    retroactively interpreted as portable package proof.
    """

    candidate_snapshot_manifest_sha256: str
    candidate_image_digest: str
    phase_map_sha256: str
    suite_receipt_sha256: str
    build_receipt_sha256: str
    image_receipt_sha256: str
    e2e_receipt_sha256: str
    outcome: Literal["passed", "failed", "incomplete", "stale", "recording_uncertain"]
    reason: str
    evidence_root: str
    receipt_sha256: str | None
    executed_tests: int
    package_schema: Literal["portable-1"]
    package_manifest_sha256: str
    package_evidence_sha256: str
    package_evidence_relpath: str
    source_catalog_sha256: str
    candidate_run_id: str
    input_manifest_sha256: str
    framework_version: str
    version_toml_sha256: str

    @property
    def passed(self) -> bool:
        return self.outcome == "passed" and self.receipt_sha256 is not None


def _digest(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def _error(code: str, message: str) -> ReleaseContractError:
    return ReleaseContractError(code, message)


def _is_sha256(value: object) -> bool:
    return isinstance(value, str) and len(value) == _SHA256_LENGTH and all(character in "0123456789abcdef" for character in value)


def _root(candidate: ValidatedCandidate) -> Path:
    root = Path(candidate.project_root).resolve()
    if root.is_symlink() or not root.is_dir():
        raise _error("release-full-gate-project-missing", "candidate Project root is unavailable")
    return root


def _path(root: Path, relative: str, *, label: str, create: bool = False) -> Path:
    parsed = PurePosixPath(relative)
    if (not relative or parsed.is_absolute() or parsed.as_posix() != relative
            or any(part in {"", ".", ".."} for part in parsed.parts)):
        raise _error("release-full-gate-path-unsafe", f"{label} is not a safe Project-relative path")
    target = root.joinpath(*parsed.parts)
    if create:
        target.mkdir(parents=True, exist_ok=True)
    if target.is_symlink() or (not create and not target.exists()):
        raise _error("release-full-gate-path-unsafe", f"{label} is absent or unsafe")
    try:
        target.resolve(strict=True).relative_to(root.resolve(strict=True))
    except ValueError as error:
        raise _error("release-full-gate-path-unsafe", f"{label} escapes the Project root") from error
    return target


def _write_new(path: Path, payload: bytes) -> None:
    with path.open("xb") as stream:
        stream.write(payload)
        stream.flush()
        os.fsync(stream.fileno())


def _phase_map(candidate: ValidatedCandidate, compilation: SealedCandidateCompilation) -> ReleaseTestPhaseMap:
    """Use the shared package-row partition and require its inventory twin."""

    package_map = derive_test_phase_map_from_rows(compilation.package_rows)
    inventory_map = derive_test_phase_map(candidate)
    if package_map != inventory_map:
        raise _error("release-full-gate-phase-map-mismatch", "candidate inventory and compiled package rows have different phase maps")
    if not package_map.unit_paths or not package_map.candidate_e2e_paths:
        raise _error("release-full-gate-phase-map-invalid", "sealed phase map lacks a required Unit or candidate-E2E partition")
    return package_map


def _portable_package_view(
    candidate: ValidatedCandidate,
    compilation: SealedPortableCandidateCompilation,
    prepared_package: PreparedPortableReleasePackage | None,
) -> PackageEvidenceView:
    """Reopen the only schema-1 package authority for native aggregation."""

    if not isinstance(prepared_package, PreparedPortableReleasePackage):
        raise _error(
            "release-full-gate-portable-package-required",
            "native Full Gate requires a typed prepared portable package receipt",
        )
    view = verify_bound_package_evidence(
        candidate,
        compilation,
        bind_package_evidence(candidate, compilation, prepared_package=prepared_package),
        prepared_package=prepared_package,
    )
    if (
        view.package_schema != "portable-1"
        or view.source_catalog_sha256 is None
        or view.candidate_run_id is None
        or view.input_manifest_sha256 is None
        or view.candidate_snapshot_manifest_sha256 != candidate.manifest.sha256
        or view.framework_version != candidate.manifest.framework_version
        or view.version_toml_sha256 != candidate.manifest.version_toml_sha256
    ):
        raise _error(
            "release-full-gate-portable-package-mismatch",
            "reopened portable package does not bind the candidate/version/catalog",
        )
    return view


def _native_package_evidence(
    candidate: ValidatedCandidate,
    compilation: SealedPortableCandidateCompilation,
    prepared_package: PreparedPortableReleasePackage | None,
) -> RetainedNativePackageEvidence:
    """Retain the one package sidecar which every native receipt must name.

    This helper is solely for the active aggregation boundary.  Retained
    consumers must reopen its immutable sidecar directly and must not call it:
    this route revalidates current candidate/source state before publication.
    """

    view = _portable_package_view(candidate, compilation, prepared_package)
    assert isinstance(prepared_package, PreparedPortableReleasePackage)
    retained = retain_native_package_evidence(candidate, compilation, prepared_package)
    if retained.view != view:
        raise _error(
            "release-full-gate-portable-package-mismatch",
            "retained package sidecar differs from the active physical package binding",
        )
    return retained


def _native_phase_map(candidate: ValidatedCandidate, view: PackageEvidenceView) -> ReleaseTestPhaseMap:
    """Require the active package projection to remain the inventory twin."""

    inventory_map = derive_test_phase_map(candidate)
    if view.phase_map != inventory_map:
        raise _error(
            "release-full-gate-phase-map-mismatch",
            "native package test projection differs from the candidate inventory",
        )
    if not inventory_map.unit_paths or not inventory_map.candidate_e2e_paths:
        raise _error("release-full-gate-phase-map-invalid", "native package lacks a required test phase")
    return inventory_map


def _native_predecessor_bindings(
    candidate: ValidatedCandidate,
    retained: RetainedNativePackageEvidence,
    suite: object,
    build: object,
    verification: object,
    e2e: object,
) -> None:
    """Compare every schema-1 predecessor with one retained package sidecar."""
    _native_predecessor_bindings_at_root(_root(candidate), retained, suite, build, verification, e2e)


def _native_predecessor_bindings_at_root(
    root: Path,
    retained: RetainedNativePackageEvidence,
    suite: object,
    build: object,
    verification: object,
    e2e: object,
) -> None:
    """Compare predecessors with a retained sidecar below an explicit root."""

    from release_e2e_gate import PortableCandidateE2EGateEvidence
    from release_image import PortableImageBuildEvidence, PortableImageVerificationEvidence

    if not isinstance(suite, PortableSuiteGateEvidence):
        raise _error("release-full-gate-native-predecessor-untrusted", "native Full Gate requires typed portable Unit evidence")
    if not isinstance(build, PortableImageBuildEvidence):
        raise _error("release-full-gate-native-predecessor-untrusted", "native Full Gate requires typed portable image-build evidence")
    if not isinstance(verification, PortableImageVerificationEvidence):
        raise _error("release-full-gate-native-predecessor-untrusted", "native Full Gate requires typed portable image verification evidence")
    if not isinstance(e2e, PortableCandidateE2EGateEvidence):
        raise _error("release-full-gate-native-predecessor-untrusted", "native Full Gate requires typed portable candidate-E2E evidence")

    try:
        sidecar_relpath = retained.receipt_path.relative_to(root).as_posix()
    except ValueError as error:  # pragma: no cover - retainer construction invariant
        raise _error("release-full-gate-sidecar-path-invalid", "retained package sidecar is outside the candidate Project") from error
    # A caller cannot elide a sidecar binding by replacing receipts with
    # similarly shaped values.  Each native predecessor must name this exact
    # content-addressed durable sidecar as well as the reopened package.
    view = retained.view
    shared = {
        "candidate_snapshot_manifest_sha256": view.candidate_snapshot_manifest_sha256,
        "source_catalog_sha256": view.source_catalog_sha256,
        "candidate_run_id": view.candidate_run_id,
        "input_manifest_sha256": view.input_manifest_sha256,
        "framework_version": view.framework_version,
        "version_toml_sha256": view.version_toml_sha256,
    }
    expected = (
        ("portable Unit", suite, {**shared, "input_schema": "portable-1", "phase_map_sha256": view.phase_map.sha256}),
        ("portable image build", build, {
            **shared,
            "package_schema": "portable-1",
            "package_manifest_sha256": view.actual_package_manifest_sha256,
            "package_evidence_sha256": retained.receipt_sha256,
            "package_evidence_relpath": sidecar_relpath,
        }),
        ("portable image verification", verification, {
            **shared,
            "package_schema": "portable-1",
            "package_manifest_sha256": view.actual_package_manifest_sha256,
            "package_evidence_sha256": retained.receipt_sha256,
            "package_evidence_relpath": sidecar_relpath,
        }),
        ("portable candidate E2E", e2e, {
            **shared,
            "package_schema": "portable-1",
            "package_manifest_sha256": view.actual_package_manifest_sha256,
            "package_evidence_sha256": retained.receipt_sha256,
            "package_evidence_relpath": sidecar_relpath,
        }),
    )
    for label, evidence, fields in expected:
        for field, value in fields.items():
            if getattr(evidence, field, None) != value:
                raise _error(
                    "release-full-gate-native-predecessor-mismatch",
                    f"{label} does not bind the retained native package: {field}",
                )


def _reopen_native_package_evidence(
    root: Path,
    evidence: NativeFullGateEvidence,
    retained_package: RetainedNativePackageEvidence | None,
) -> RetainedNativePackageEvidence:
    """Reopen the canonical private package and exact immutable sidecar.

    The caller-supplied typed receipt is deliberately compared to a fresh
    physical observation.  This is a retained read path: it does not call the
    current package binder, candidate revalidator, or source admission.
    """

    if not isinstance(retained_package, RetainedNativePackageEvidence):
        raise _error(
            "release-full-gate-retained-package-required",
            "native retained verification requires its typed package-sidecar receipt",
        )
    if evidence.package_schema != "portable-1":
        raise _error("release-full-gate-evidence-mismatch", "native aggregate names an unsupported package schema")
    if not _is_sha256(evidence.package_manifest_sha256) or not _is_sha256(evidence.package_evidence_sha256):
        raise _error("release-full-gate-evidence-mismatch", "native aggregate package digests are invalid")
    if not isinstance(evidence.candidate_run_id, str) or not evidence.candidate_run_id:
        raise _error("release-full-gate-evidence-mismatch", "native aggregate candidate run is invalid")
    if PurePosixPath(evidence.candidate_run_id).name != evidence.candidate_run_id:
        raise _error("release-full-gate-evidence-mismatch", "native aggregate candidate run is unsafe")
    if not isinstance(evidence.package_evidence_relpath, str):
        raise _error("release-full-gate-evidence-mismatch", "native aggregate sidecar path is invalid")
    sidecar = _path(root, evidence.package_evidence_relpath, label="retained package evidence")
    if sidecar.parent.name != "package_evidence" or sidecar.name != f"{evidence.package_evidence_sha256}.json":
        raise _error("release-full-gate-evidence-mismatch", "native aggregate sidecar path is not content addressed")
    package_root = (
        root / ".caprmedio_tmp" / "release_candidates" / evidence.candidate_run_id
        / "package" / evidence.package_manifest_sha256
    )
    if package_root.is_symlink() or not package_root.is_dir():
        raise _error("release-full-gate-retained-package-missing", "native aggregate package root is missing or unsafe")
    try:
        package_root.resolve(strict=True).relative_to(root.resolve(strict=True))
    except (OSError, ValueError) as error:
        raise _error("release-full-gate-retained-package-missing", "native aggregate package root escapes the Project") from error
    observed = read_retained_native_package_evidence(
        package_root,
        sidecar,
        expected_sha256=evidence.package_evidence_sha256,
    )
    if observed != retained_package:
        raise _error(
            "release-full-gate-retained-package-mismatch",
            "caller-provided retained package receipt differs from the physical sidecar/package",
        )
    view = observed.view
    bindings = {
        "package_schema": "portable-1",
        "candidate_snapshot_manifest_sha256": evidence.candidate_snapshot_manifest_sha256,
        "actual_package_manifest_sha256": evidence.package_manifest_sha256,
        "source_catalog_sha256": evidence.source_catalog_sha256,
        "candidate_run_id": evidence.candidate_run_id,
        "input_manifest_sha256": evidence.input_manifest_sha256,
        "framework_version": evidence.framework_version,
        "version_toml_sha256": evidence.version_toml_sha256,
    }
    if any(getattr(view, field, None) != value for field, value in bindings.items()):
        raise _error("release-full-gate-retained-package-mismatch", "native aggregate does not bind the reopened package sidecar")
    if not view.phase_map.unit_paths or not view.phase_map.candidate_e2e_paths:
        raise _error("release-full-gate-phase-map-invalid", "retained native package lacks a required test phase")
    return observed


def _reopen_retained_native_suite(
    root: Path,
    suite: object,
    view: PackageEvidenceView,
) -> PortableSuiteGateEvidence:
    """Read the original schema-1 Unit receipt without a live rebind.

    This deliberately checks only durable receipt/output/report carriers and
    the retained package's sealed input identity.  It does not consult the
    current selector, source checkout, or portable-compilation binder.
    """

    if not isinstance(suite, PortableSuiteGateEvidence) or not suite.passed:
        raise _error("release-full-gate-native-suite-untrusted", "native retained Full Gate requires passed portable Unit evidence")
    expected = {
        "input_schema": "portable-1",
        "candidate_snapshot_manifest_sha256": view.candidate_snapshot_manifest_sha256,
        "candidate_run_id": view.candidate_run_id,
        "input_manifest_sha256": view.input_manifest_sha256,
        "source_catalog_sha256": view.source_catalog_sha256,
        "framework_version": view.framework_version,
        "version_toml_sha256": view.version_toml_sha256,
        "phase_map_sha256": view.phase_map.sha256,
    }
    if any(getattr(suite, field, None) != value for field, value in expected.items()):
        raise _error("release-full-gate-native-suite-mismatch", "portable Unit receipt binds another retained package")
    if not isinstance(suite.evidence_root, str):
        raise _error("release-full-gate-native-suite-untrusted", "portable Unit evidence root is invalid")
    prefix = f".caprmedio_runtime/release_suite/{view.candidate_snapshot_manifest_sha256}/"
    suffix = suite.evidence_root.removeprefix(prefix)
    if (
        not isinstance(suite.receipt_sha256, str)
        or not _is_sha256(suite.receipt_sha256)
        or suite.exit_code != 0
        or not suite.evidence_root.startswith(prefix)
        or not suffix.startswith("attempt-")
        or "/" in suffix
    ):
        raise _error("release-full-gate-native-suite-untrusted", "portable Unit evidence root or receipt is invalid")
    receipt = _path(root, f"{suite.evidence_root}/receipt.json", label="retained portable Unit receipt")
    stdout = _path(root, f"{suite.evidence_root}/stdout.bin", label="retained portable Unit stdout")
    stderr = _path(root, f"{suite.evidence_root}/stderr.bin", label="retained portable Unit stderr")
    report = _path(root, f"{suite.evidence_root}/coverage.xml", label="retained portable Unit report")
    payload = receipt.read_bytes()
    if (
        _digest(payload) != suite.receipt_sha256
        or payload != canonical_json(asdict(replace(suite, receipt_sha256=None)))
        or not _is_sha256(suite.stdout_sha256)
        or not _is_sha256(suite.stderr_sha256)
        or not _is_sha256(suite.report_sha256)
        or _digest(stdout.read_bytes()) != suite.stdout_sha256
        or _digest(stderr.read_bytes()) != suite.stderr_sha256
        or _digest(report.read_bytes()) != suite.report_sha256
    ):
        raise _error("release-full-gate-native-suite-untrusted", "portable Unit receipt or captured output changed")
    return suite


def _reopen_retained_native_constituents(
    candidate: ValidatedCandidate,
    compilation: SealedPortableCandidateCompilation,
    suite: object,
    build: object,
    verification: object,
    e2e: object,
    retained: RetainedNativePackageEvidence,
) -> Path:
    """Read original native suite/image/E2E evidence without current binding."""

    from release_e2e_gate import read_candidate_e2e_execution_artifacts
    from release_image import read_image_execution_artifacts

    root = _root(candidate)
    _native_predecessor_bindings(candidate, retained, suite, build, verification, e2e)
    native_suite = _reopen_retained_native_suite(root, suite, retained.view)
    image_attempt = read_image_execution_artifacts(
        candidate, compilation, native_suite, build, verification,
    )
    e2e_root = read_candidate_e2e_execution_artifacts(
        candidate, compilation, native_suite, verification, e2e, image_build=build,
    )
    if image_attempt != _path(root, verification.evidence_root, label="retained native image attempt") or e2e_root != root:
        raise _error("release-full-gate-root-mismatch", "a retained native predecessor does not belong to the candidate Project")
    return root


def _reopen_constituents(
    candidate: ValidatedCandidate,
    compilation: SealedCandidateCompilation | SealedPortableCandidateCompilation,
    suite: SuiteGateEvidence | PortableSuiteGateEvidence,
    build: ImageBuildEvidence,
    verification: ImageVerificationEvidence,
    e2e: CandidateE2EGateEvidence,
    *,
    prepared_package: PreparedPortableReleasePackage | None = None,
) -> Path:
    """Reopen every predecessor reader; no fields are trusted by themselves."""

    # Image retirement consumes this module through promotion.  These imports
    # are delayed until the concrete readers exist, keeping that cycle private.
    from release_e2e_gate import verify_bound_candidate_e2e_evidence
    from release_image import verify_bound_image_evidence

    root = _root(candidate)
    suite_root = verify_bound_suite_evidence(candidate, compilation, suite)
    if isinstance(compilation, SealedPortableCandidateCompilation):
        verify_bound_image_evidence(
            candidate, compilation, suite, build, verification, prepared_package=prepared_package,
        )
        e2e_root = verify_bound_candidate_e2e_evidence(
            candidate, compilation, suite, verification, e2e,
            image_build=build, prepared_package=prepared_package,
        )
    else:
        verify_bound_image_evidence(candidate, compilation, suite, build, verification)
        e2e_root = verify_bound_candidate_e2e_evidence(
            candidate, compilation, suite, verification, e2e, image_build=build,
        )
    if suite_root != root or e2e_root != root:
        raise _error("release-full-gate-root-mismatch", "a reopened predecessor does not belong to the candidate Project")
    return root


def _constituent_receipts(
    candidate: ValidatedCandidate,
    suite: SuiteGateEvidence | PortableSuiteGateEvidence,
    build: ImageBuildEvidence,
    verification: ImageVerificationEvidence,
    e2e: CandidateE2EGateEvidence,
) -> tuple[str, str, str, str]:
    values = (suite.receipt_sha256, build.receipt_sha256, verification.receipt_sha256, e2e.receipt_sha256)
    if (not all(_is_sha256(value) for value in values)
            or build.candidate_snapshot_manifest_sha256 != candidate.manifest.sha256
            or verification.candidate_snapshot_manifest_sha256 != candidate.manifest.sha256
            or e2e.candidate_snapshot_manifest_sha256 != candidate.manifest.sha256
            or build.candidate_image_digest != verification.candidate_image_digest
            or verification.candidate_image_digest != e2e.candidate_image_digest):
        raise _error("release-full-gate-binding-mismatch", "constituent receipts do not share one candidate and immutable image")
    return values  # type: ignore[return-value]


def _reopen_retained_constituents(
    candidate: ValidatedCandidate,
    compilation: SealedCandidateCompilation,
    suite: SuiteGateEvidence,
    build: ImageBuildEvidence,
    verification: ImageVerificationEvidence,
    e2e: CandidateE2EGateEvidence,
) -> Path:
    """Read original evidence after selection; later effects admit currentness."""

    from release_e2e_gate import read_candidate_e2e_execution_artifacts
    from release_image import read_image_execution_artifacts

    root = _root(candidate)
    image_attempt = read_image_execution_artifacts(candidate, compilation, suite, build, verification)
    e2e_root = read_candidate_e2e_execution_artifacts(
        candidate, compilation, suite, verification, e2e, image_build=build,
    )
    if image_attempt != _path(root, verification.evidence_root, label="retained image attempt") or e2e_root != root:
        raise _error("release-full-gate-root-mismatch", "a retained predecessor does not belong to the candidate Project")
    return root


def _read_xml(path: Path, *, label: str) -> ET.Element:
    if path.is_symlink() or not path.is_file() or path.stat().st_size > _MAX_REPORT_BYTES:
        raise _error("release-full-gate-report-invalid", f"{label} report is missing, unsafe or too large")
    with path.open("rb") as stream:
        payload = stream.read(_MAX_REPORT_BYTES + 1)
    if len(payload) > _MAX_REPORT_BYTES or b"<!DOCTYPE" in payload.upper() or b"<!ENTITY" in payload.upper():
        raise _error("release-full-gate-report-invalid", f"{label} report is unsupported")
    try:
        report = ET.fromstring(payload)
    except ET.ParseError as error:
        raise _error("release-full-gate-report-invalid", f"{label} report is malformed") from error
    if report.tag not in {"testsuite", "testsuites"}:
        raise _error("release-full-gate-report-invalid", f"{label} report has an unsupported root")
    return report


def _report_cases(report: ET.Element, *, label: str) -> tuple[tuple[str, str], ...]:
    cases = list(report.iter("testcase"))
    if not cases:
        raise _error("release-full-gate-report-invalid", f"{label} report has no executed testcases")
    identities: list[tuple[str, str]] = []
    for case in cases:
        classname, name = case.get("classname"), case.get("name")
        if (not isinstance(classname, str) or not classname or not isinstance(name, str) or not name
                or list(case.iter("failure")) or list(case.iter("error")) or list(case.iter("skipped"))):
            raise _error("release-full-gate-report-invalid", f"{label} report has an ambiguous or non-passing testcase")
        identities.append((classname, name))
    if len(identities) != len(set(identities)):
        raise _error("release-full-gate-report-invalid", f"{label} report has duplicate testcase identities")
    for suite in (node for node in report.iter() if node.tag in {"testsuite", "testsuites"}):
        actual = len(list(suite.iter("testcase")))
        for key, expected in (("tests", actual), ("failures", 0), ("errors", 0), ("skipped", 0)):
            if key in suite.attrib:
                try:
                    if int(suite.attrib[key]) != expected:
                        raise _error("release-full-gate-report-invalid", f"{label} report summary is inconsistent")
                except ValueError as error:
                    raise _error("release-full-gate-report-invalid", f"{label} report summary is invalid") from error
    return tuple(identities)


def _observe_partition(
    root: Path,
    suite: SuiteGateEvidence,
    e2e: CandidateE2EGateEvidence,
    phase_map: ReleaseTestPhaseMap,
) -> int:
    """Require one complete Unit/E2E test partition with globally unique cases."""

    if suite.phase_map_sha256 != phase_map.sha256:
        raise _error("release-full-gate-phase-map-mismatch", "Unit receipt does not bind the sealed phase map")
    suite_report = _read_xml(
        _path(root, f"{suite.evidence_root}/coverage.xml", label="retained Unit"), label="Unit",
    )
    if (suite_report.get("caprmedio.phase") != "unit"
            or suite_report.get("caprmedio.phase_map_sha256") != phase_map.sha256):
        raise _error("release-full-gate-phase-map-mismatch", "Unit report does not bind the exact Unit phase map")
    unit_cases = _report_cases(suite_report, label="Unit")
    if {classname for classname, _name in unit_cases} != set(phase_map.unit_paths):
        raise _error("release-full-gate-partition-invalid", "Unit report does not cover the exact declared Unit modules")
    if suite.executed_tests != len(unit_cases):
        raise _error("release-full-gate-report-invalid", "Unit receipt testcase count does not match its retained report")

    expected_e2e_paths = phase_map.candidate_e2e_paths
    if (len(e2e.harness_receipts) != len(expected_e2e_paths)
            or tuple(sorted(row.source_path for row in e2e.harness_receipts)) != expected_e2e_paths):
        raise _error("release-full-gate-partition-invalid", "candidate E2E receipt does not cover the exact declared E2E modules")
    identities = set(unit_cases)
    total = len(unit_cases)
    for row in e2e.harness_receipts:
        report = _read_xml(_path(root, row.junit_path, label="retained candidate E2E"), label="candidate E2E")
        observed = _report_cases(report, label="candidate E2E")
        module_name = PurePosixPath(row.source_path).stem
        if any(classname != module_name and not classname.startswith(module_name + ".")
               for classname, _name in observed):
            raise _error("release-full-gate-partition-invalid", "candidate E2E report does not cover its declared E2E module")
        if row.executed_tests != len(observed):
            raise _error("release-full-gate-report-invalid", "candidate E2E receipt testcase count does not match its retained report")
        if identities.intersection(observed):
            raise _error("release-full-gate-partition-invalid", "Unit and candidate E2E reports share a testcase identity")
        identities.update(observed)
        total += len(observed)
    return total


def aggregate_bound_release_gates(
    candidate: ValidatedCandidate,
    compilation: SealedCandidateCompilation | SealedPortableCandidateCompilation,
    suite: SuiteGateEvidence | PortableSuiteGateEvidence,
    build: ImageBuildEvidence,
    verification: ImageVerificationEvidence,
    e2e: CandidateE2EGateEvidence,
    *,
    prepared_package: PreparedPortableReleasePackage | None = None,
) -> FullGateEvidence | NativeFullGateEvidence:
    """Retain a read-only aggregate only after all bound gates and reports agree."""

    retained_native: RetainedNativePackageEvidence | None = None
    # Do not let a native aggregate descend into the legacy readers.  The
    # native predecessor receipts have a different canonical fieldset and can
    # only begin after their physical D597 package is reopened and retained.
    if isinstance(compilation, SealedPortableCandidateCompilation):
        retained_native = _native_package_evidence(candidate, compilation, prepared_package)
        _native_predecessor_bindings(candidate, retained_native, suite, build, verification, e2e)
    elif prepared_package is not None:
        raise _error(
            "release-full-gate-package-schema-mismatch",
            "schema-2 Full Gate does not accept a portable prepared package",
        )
    root = _reopen_constituents(
        candidate, compilation, suite, build, verification, e2e, prepared_package=prepared_package,
    )
    if (
        compilation.framework_version != candidate.manifest.framework_version
        or compilation.version_toml_sha256 != candidate.manifest.version_toml_sha256
    ):
        raise _error("release-full-gate-binding-mismatch", "compiled package does not bind the candidate root version.toml")
    phase_map = (
        _native_phase_map(candidate, retained_native.view)
        if retained_native is not None
        else _phase_map(candidate, compilation)
    )
    suite_receipt, build_receipt, image_receipt, e2e_receipt = _constituent_receipts(
        candidate, suite, build, verification, e2e,
    )
    parent = _path(root, f"{EVIDENCE_ROOT}/{candidate.manifest.sha256}", label="full-gate evidence", create=True)
    attempt = Path(tempfile.mkdtemp(prefix="attempt-", dir=parent))
    evidence_root = attempt.relative_to(root).as_posix()
    outcome: Literal["passed", "failed", "incomplete", "stale", "recording_uncertain"] = "failed"
    reason = "aggregate reports are incomplete"
    executed_tests = 0
    try:
        executed_tests = _observe_partition(root, suite, e2e, phase_map)
        outcome, reason = "passed", "all bound Unit and candidate E2E reports form one complete partition"
    except ReleaseContractError as error:
        outcome, reason = "failed", str(error)
    if retained_native is None:
        evidence: FullGateEvidence | NativeFullGateEvidence = FullGateEvidence(
            candidate.manifest.sha256, verification.candidate_image_digest, phase_map.sha256,
            suite_receipt, build_receipt, image_receipt, e2e_receipt,
            outcome, reason, evidence_root, None, executed_tests,
            candidate.manifest.framework_version, candidate.manifest.version_toml_sha256,
        )
    else:
        sidecar_relpath = retained_native.receipt_path.relative_to(root).as_posix()
        evidence = NativeFullGateEvidence(
            candidate_snapshot_manifest_sha256=candidate.manifest.sha256,
            candidate_image_digest=verification.candidate_image_digest,
            phase_map_sha256=phase_map.sha256,
            suite_receipt_sha256=suite_receipt,
            build_receipt_sha256=build_receipt,
            image_receipt_sha256=image_receipt,
            e2e_receipt_sha256=e2e_receipt,
            outcome=outcome,
            reason=reason,
            evidence_root=evidence_root,
            receipt_sha256=None,
            executed_tests=executed_tests,
            package_schema="portable-1",
            package_manifest_sha256=retained_native.view.actual_package_manifest_sha256,
            package_evidence_sha256=retained_native.receipt_sha256,
            package_evidence_relpath=sidecar_relpath,
            source_catalog_sha256=retained_native.view.source_catalog_sha256,
            candidate_run_id=retained_native.view.candidate_run_id,
            input_manifest_sha256=retained_native.view.input_manifest_sha256,
            framework_version=retained_native.view.framework_version,
            version_toml_sha256=retained_native.view.version_toml_sha256,
        )
    try:
        receipt = canonical_json(asdict(evidence))
        _write_new(attempt / "receipt.json", receipt)
        descriptor = os.open(attempt, os.O_RDONLY)
        try:
            os.fsync(descriptor)
        finally:
            os.close(descriptor)
        return replace(evidence, receipt_sha256=_digest(receipt))
    except OSError:
        return replace(evidence, outcome="recording_uncertain", reason="full-gate aggregate receipt could not be durably recorded")


def _verify_retained_native_full_gate(
    candidate: ValidatedCandidate,
    compilation: SealedPortableCandidateCompilation,
    suite: object,
    build: object,
    verification: object,
    e2e: object,
    evidence: NativeFullGateEvidence,
    retained_package: RetainedNativePackageEvidence | None,
) -> Path:
    """Verify one original schema-1 aggregate without reopening live inputs."""

    if not evidence.passed:
        raise _error("release-full-gate-evidence-untrusted", "later admission requires passed aggregate gate evidence")
    root = _root(candidate)
    retained = _reopen_native_package_evidence(root, evidence, retained_package)
    view = retained.view
    if (
        evidence.candidate_snapshot_manifest_sha256 != candidate.manifest.sha256
        or evidence.candidate_snapshot_manifest_sha256 != view.candidate_snapshot_manifest_sha256
        or evidence.phase_map_sha256 != view.phase_map.sha256
        or evidence.package_schema != "portable-1"
        or evidence.package_manifest_sha256 != view.actual_package_manifest_sha256
        or evidence.package_evidence_sha256 != retained.receipt_sha256
        or evidence.package_evidence_relpath != retained.receipt_path.relative_to(root).as_posix()
        or evidence.source_catalog_sha256 != view.source_catalog_sha256
        or evidence.candidate_run_id != view.candidate_run_id
        or evidence.input_manifest_sha256 != view.input_manifest_sha256
        or evidence.framework_version != view.framework_version
        or evidence.version_toml_sha256 != view.version_toml_sha256
    ):
        raise _error("release-full-gate-evidence-mismatch", "native aggregate does not bind the exact retained package")
    _reopen_retained_native_constituents(
        candidate, compilation, suite, build, verification, e2e, retained,
    )
    suite_receipt, build_receipt, image_receipt, e2e_receipt = _constituent_receipts(
        candidate, suite, build, verification, e2e,
    )
    if not isinstance(evidence.evidence_root, str):
        raise _error("release-full-gate-evidence-mismatch", "native aggregate evidence root is invalid")
    prefix = f"{EVIDENCE_ROOT}/{candidate.manifest.sha256}/"
    if (
        evidence.candidate_image_digest != getattr(verification, "candidate_image_digest", None)
        or (evidence.suite_receipt_sha256, evidence.build_receipt_sha256,
            evidence.image_receipt_sha256, evidence.e2e_receipt_sha256)
        != (suite_receipt, build_receipt, image_receipt, e2e_receipt)
        or not _is_sha256(evidence.receipt_sha256)
        or not evidence.evidence_root.startswith(prefix)
        or not evidence.evidence_root.removeprefix(prefix).startswith("attempt-")
        or "/" in evidence.evidence_root.removeprefix(prefix)
    ):
        raise _error("release-full-gate-evidence-mismatch", "native aggregate does not belong to the exact retained predecessors")
    receipt = _path(root, f"{evidence.evidence_root}/receipt.json", label="native full-gate receipt")
    payload = receipt.read_bytes()
    if (
        _digest(payload) != evidence.receipt_sha256
        or payload != canonical_json(asdict(replace(evidence, receipt_sha256=None)))
    ):
        raise _error("release-full-gate-evidence-untrusted", "native aggregate receipt changed or is caller-forged")
    if _observe_partition(root, suite, e2e, view.phase_map) != evidence.executed_tests:
        raise _error("release-full-gate-evidence-untrusted", "native aggregate executed testcase count changed")
    return root


def _detached_artifact_root(value: Path) -> Path:
    """Open the explicit retained-artifact root without source authority."""

    if not isinstance(value, Path) or not value.is_absolute() or any(part == ".." for part in value.parts):
        raise _error("release-full-gate-artifact-root-invalid", "detached native verification needs an absolute artifact root")
    try:
        refuse_secret_path(value)
    except ReleaseInventoryError as error:
        raise _error(error.code, str(error)) from error
    try:
        observed = value.lstat()
        root = value.resolve(strict=True)
    except OSError as error:
        raise _error("release-full-gate-artifact-root-invalid", "detached artifact root is unavailable") from error
    if value.is_symlink() or not root.is_dir() or not os.path.samestat(observed, root.stat()):
        raise _error("release-full-gate-artifact-root-invalid", "detached artifact root is unsafe")
    return root


def _require_detached_candidate_under_root(root: Path, retained: RetainedCandidateIdentity) -> None:
    """Reject untrusted external carrier paths before any retained reopen."""

    if not isinstance(retained, RetainedCandidateIdentity):
        raise _error("release-full-gate-detached-candidate-untrusted", "detached native verification requires a retained candidate identity")
    package = retained.package_evidence
    if not isinstance(package, RetainedNativePackageEvidence) or not isinstance(package.view, PackageEvidenceView):
        raise _error("release-full-gate-detached-candidate-untrusted", "detached native verification requires typed package evidence")
    for label, path in (
        ("descriptor", retained.descriptor_path),
        ("package evidence", package.receipt_path),
        ("package", package.view.package_root),
    ):
        if not isinstance(path, Path) or not path.is_absolute() or any(part == ".." for part in path.parts):
            raise _error("release-full-gate-detached-candidate-untrusted", f"detached {label} path is unsafe")
        try:
            path.relative_to(root)
        except ValueError as error:
            raise _error(
                "release-full-gate-detached-candidate-untrusted",
                f"detached {label} path is outside the supplied artifact root",
            ) from error


def _reopen_detached_native_package_evidence(
    root: Path,
    evidence: NativeFullGateEvidence,
    retained_candidate: RetainedCandidateIdentity,
) -> RetainedNativePackageEvidence:
    """Bind one aggregate to a freshly reopened D597 descriptor/package pair."""

    if not isinstance(evidence, NativeFullGateEvidence):
        raise _error("release-full-gate-evidence-untrusted", "detached native verification requires typed schema-1 evidence")
    retained = reopen_retained_candidate_identity(retained_candidate)
    package = retained.package_evidence
    if evidence.package_schema != "portable-1" or not evidence.passed:
        raise _error("release-full-gate-evidence-untrusted", "detached native verification requires passed schema-1 evidence")
    if (
        not _is_sha256(evidence.package_manifest_sha256)
        or not _is_sha256(evidence.package_evidence_sha256)
        or not isinstance(evidence.candidate_run_id, str)
        or not evidence.candidate_run_id
        or PurePosixPath(evidence.candidate_run_id).name != evidence.candidate_run_id
        or not isinstance(evidence.package_evidence_relpath, str)
    ):
        raise _error("release-full-gate-evidence-mismatch", "native aggregate sidecar path is invalid")
    expected_sidecar = _path(root, evidence.package_evidence_relpath, label="retained package evidence")
    if (
        expected_sidecar != package.receipt_path
        or expected_sidecar.parent.name != "package_evidence"
        or expected_sidecar.name != f"{evidence.package_evidence_sha256}.json"
        or package.view.package_root != root / ".caprmedio_tmp" / "release_candidates" / evidence.candidate_run_id
        / "package" / evidence.package_manifest_sha256
    ):
        raise _error("release-full-gate-retained-package-mismatch", "native aggregate does not name the reopened retained package")
    view = package.view
    bindings = {
        "candidate_snapshot_manifest_sha256": retained.candidate_snapshot_manifest_sha256,
        "actual_package_manifest_sha256": evidence.package_manifest_sha256,
        "source_catalog_sha256": evidence.source_catalog_sha256,
        "candidate_run_id": evidence.candidate_run_id,
        "input_manifest_sha256": evidence.input_manifest_sha256,
        "framework_version": retained.framework_version,
        "version_toml_sha256": retained.version_toml_sha256,
    }
    if (
        any(getattr(view, field, None) != value for field, value in bindings.items())
        or evidence.candidate_snapshot_manifest_sha256 != retained.candidate_snapshot_manifest_sha256
        or evidence.framework_version != retained.framework_version
        or evidence.version_toml_sha256 != retained.version_toml_sha256
        or evidence.package_evidence_sha256 != package.receipt_sha256
        or evidence.phase_map_sha256 != view.phase_map.sha256
    ):
        raise _error("release-full-gate-retained-package-mismatch", "native aggregate does not bind the reopened candidate/package")
    return retained.package_evidence


def _detached_constituent_receipts(
    candidate_snapshot_manifest_sha256: str,
    build: object,
    verification: object,
    e2e: object,
) -> tuple[str, str, str, str]:
    values = (
        getattr(build, "receipt_sha256", None),
        getattr(verification, "receipt_sha256", None),
        getattr(e2e, "receipt_sha256", None),
    )
    if (
        not all(_is_sha256(value) for value in values)
        or getattr(build, "candidate_snapshot_manifest_sha256", None) != candidate_snapshot_manifest_sha256
        or getattr(verification, "candidate_snapshot_manifest_sha256", None) != candidate_snapshot_manifest_sha256
        or getattr(e2e, "candidate_snapshot_manifest_sha256", None) != candidate_snapshot_manifest_sha256
        or getattr(build, "candidate_image_digest", None) != getattr(verification, "candidate_image_digest", None)
        or getattr(verification, "candidate_image_digest", None) != getattr(e2e, "candidate_image_digest", None)
    ):
        raise _error("release-full-gate-binding-mismatch", "detached constituents do not share one candidate and immutable image")
    return ("", values[0], values[1], values[2])  # Unit is added by its retained reader.


def verify_detached_native_full_gate_evidence(
    artifact_root: Path,
    retained_candidate: RetainedCandidateIdentity,
    suite: object,
    build: object,
    verification: object,
    e2e: object,
    evidence: NativeFullGateEvidence,
) -> RetainedNativePackageEvidence:
    """Reopen a D597 Full Gate packet without live candidate or checkout state."""

    root = _detached_artifact_root(artifact_root)
    _require_detached_candidate_under_root(root, retained_candidate)
    retained = reopen_retained_candidate_identity(retained_candidate)
    package = _reopen_detached_native_package_evidence(root, evidence, retained)
    view = package.view
    _native_predecessor_bindings_at_root(root, package, suite, build, verification, e2e)
    native_suite = _reopen_retained_native_suite(root, suite, view)
    from release_image import read_detached_image_execution_artifacts
    from release_e2e_gate import read_detached_candidate_e2e_execution_artifacts

    image_attempt = read_detached_image_execution_artifacts(root, retained, native_suite, build, verification)
    e2e_root = read_detached_candidate_e2e_execution_artifacts(
        root, retained, native_suite, verification, e2e, image_build=build,
    )
    if image_attempt != _path(root, getattr(verification, "evidence_root", ""), label="retained native image attempt") or e2e_root != root:
        raise _error("release-full-gate-root-mismatch", "a detached native predecessor does not belong to the artifact root")
    _unit, build_receipt, image_receipt, e2e_receipt = _detached_constituent_receipts(
        retained.candidate_snapshot_manifest_sha256, build, verification, e2e,
    )
    suite_receipt = getattr(native_suite, "receipt_sha256", None)
    prefix = f"{EVIDENCE_ROOT}/{retained.candidate_snapshot_manifest_sha256}/"
    if (
        evidence.candidate_image_digest != getattr(verification, "candidate_image_digest", None)
        or (evidence.suite_receipt_sha256, evidence.build_receipt_sha256,
            evidence.image_receipt_sha256, evidence.e2e_receipt_sha256)
        != (suite_receipt, build_receipt, image_receipt, e2e_receipt)
        or not _is_sha256(evidence.receipt_sha256)
        or not isinstance(evidence.evidence_root, str)
        or not evidence.evidence_root.startswith(prefix)
        or not evidence.evidence_root.removeprefix(prefix).startswith("attempt-")
        or "/" in evidence.evidence_root.removeprefix(prefix)
    ):
        raise _error("release-full-gate-evidence-mismatch", "native aggregate does not belong to the exact detached predecessors")
    receipt = _path(root, f"{evidence.evidence_root}/receipt.json", label="detached native full-gate receipt")
    payload = receipt.read_bytes()
    if (
        _digest(payload) != evidence.receipt_sha256
        or payload != canonical_json(asdict(replace(evidence, receipt_sha256=None)))
    ):
        raise _error("release-full-gate-evidence-untrusted", "detached native aggregate receipt changed or is caller-forged")
    if _observe_partition(root, native_suite, e2e, view.phase_map) != evidence.executed_tests:
        raise _error("release-full-gate-evidence-untrusted", "detached native aggregate executed testcase count changed")
    return package


def verify_bound_full_gate_evidence(
    candidate: ValidatedCandidate,
    compilation: SealedCandidateCompilation | SealedPortableCandidateCompilation,
    suite: SuiteGateEvidence | PortableSuiteGateEvidence,
    build: ImageBuildEvidence,
    verification: ImageVerificationEvidence,
    e2e: CandidateE2EGateEvidence,
    evidence: FullGateEvidence | NativeFullGateEvidence,
    *,
    retained_package: RetainedNativePackageEvidence | None = None,
) -> Path:
    """Read exact original aggregate artifacts independently of active selection.

    This byte reader does not admit a new effect.  Promotion and recovery must
    separately establish their intent, current source/package and selection.
    """

    if isinstance(evidence, NativeFullGateEvidence):
        if not isinstance(compilation, SealedPortableCandidateCompilation):
            raise _error("release-full-gate-package-schema-mismatch", "native aggregate requires a schema-1 sealed compilation")
        return _verify_retained_native_full_gate(
            candidate, compilation, suite, build, verification, e2e, evidence, retained_package,
        )
    if retained_package is not None:
        raise _error("release-full-gate-package-schema-mismatch", "schema-2 aggregate does not accept a native retained package")
    if not isinstance(compilation, SealedCandidateCompilation):
        raise _error("release-full-gate-package-schema-mismatch", "schema-1 compilation requires native aggregate evidence")
    root = _reopen_retained_constituents(candidate, compilation, suite, build, verification, e2e)
    if not isinstance(evidence, FullGateEvidence) or not evidence.passed:
        raise _error("release-full-gate-evidence-untrusted", "later admission requires passed aggregate gate evidence")
    phase_map = _phase_map(candidate, compilation)
    suite_receipt, build_receipt, image_receipt, e2e_receipt = _constituent_receipts(
        candidate, suite, build, verification, e2e,
    )
    prefix = f"{EVIDENCE_ROOT}/{candidate.manifest.sha256}/"
    if (evidence.candidate_snapshot_manifest_sha256 != candidate.manifest.sha256
            or evidence.framework_version != candidate.manifest.framework_version
            or evidence.version_toml_sha256 != candidate.manifest.version_toml_sha256
            or compilation.framework_version != candidate.manifest.framework_version
            or compilation.version_toml_sha256 != candidate.manifest.version_toml_sha256
            or evidence.candidate_image_digest != verification.candidate_image_digest
            or evidence.phase_map_sha256 != phase_map.sha256
            or (evidence.suite_receipt_sha256, evidence.build_receipt_sha256,
                evidence.image_receipt_sha256, evidence.e2e_receipt_sha256)
            != (suite_receipt, build_receipt, image_receipt, e2e_receipt)
            or not _is_sha256(evidence.receipt_sha256)
            or not evidence.evidence_root.startswith(prefix)
            or not evidence.evidence_root.removeprefix(prefix).startswith("attempt-")
            or "/" in evidence.evidence_root.removeprefix(prefix)):
        raise _error("release-full-gate-evidence-mismatch", "aggregate evidence does not belong to the exact bound candidate")
    receipt = _path(root, f"{evidence.evidence_root}/receipt.json", label="full-gate receipt")
    receipt_bytes = receipt.read_bytes()
    if (_digest(receipt_bytes) != evidence.receipt_sha256
            or receipt_bytes != canonical_json(asdict(replace(evidence, receipt_sha256=None)))):
        raise _error("release-full-gate-evidence-untrusted", "full-gate aggregate receipt changed or is caller-forged")
    if _observe_partition(root, suite, e2e, phase_map) != evidence.executed_tests:
        raise _error("release-full-gate-evidence-untrusted", "aggregate executed testcase count changed")
    return root


__all__ = [
    "FullGateEvidence",
    "NativeFullGateEvidence",
    "aggregate_bound_release_gates",
    "verify_detached_native_full_gate_evidence",
    "verify_bound_full_gate_evidence",
]
