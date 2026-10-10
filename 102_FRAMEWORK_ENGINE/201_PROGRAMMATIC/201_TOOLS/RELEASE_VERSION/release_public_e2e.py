"""Fresh, non-promoting public E2E evidence for one admitted public action.

The retained native packet proves the immutable package and image only.  It
cannot be returned as this phase's E2E result.  This producer therefore
reopens the public action and current selected N, reuses only the retained
grammar/limits and image provenance, and invokes the fixed three host
harnesses again through ``HostE2EExecutor``.
"""

from __future__ import annotations

import os
import json
import sys
import tempfile
import time
from dataclasses import asdict, replace
from pathlib import Path, PurePosixPath
from typing import Literal

import release_e2e_gate as _e2e
from release_contract import PROJECT_SKILL_TARGET, ReleaseContractError, canonical_json
from release_e2e_context import CANDIDATE_IMAGE_ENVIRONMENT_VARIABLE, CONTEXT_ENVIRONMENT_VARIABLE
from release_e2e_gate import (E2EExecutionResult, ExecutableIdentity, FrozenHostE2ECapability,
                              HarnessReceipt, HostE2EExecutor, PortableCandidateE2EGateEvidence)
from release_handoff import NativeInstalledNBinding, reopen_native_installed_n, tree_sha256
from release_image import read_detached_image_execution_artifacts
from release_public_gate import PublicFreshGateInputs, reopen_public_fresh_gate_inputs
from release_suite import PortableSuiteGateEvidence, _active_skill_records


class PublicFreshE2EError(ReleaseContractError):
    """The current public action cannot produce fresh host-E2E evidence."""


def _refuse(code: str, message: str) -> None:
    raise PublicFreshE2EError(code, message)


def _root(inputs: PublicFreshGateInputs) -> Path:
    if not isinstance(inputs, PublicFreshGateInputs):
        _refuse("public-fresh-e2e-input-invalid", "public fresh E2E requires reopened PublicFreshGateInputs")
    try:
        root = inputs.project_root.resolve(strict=True)
    except OSError as error:
        raise PublicFreshE2EError("public-fresh-e2e-project-unavailable", "public fresh E2E Project is unavailable") from error
    if inputs.project_root.is_symlink() or not root.is_dir():
        _refuse("public-fresh-e2e-project-invalid", "public fresh E2E Project is unsafe")
    return root


def _reopen_inputs(inputs: PublicFreshGateInputs) -> PublicFreshGateInputs:
    """Reject a caller-assembled input carrier before any E2E side effect."""

    root = _root(inputs)
    try:
        observed = reopen_public_fresh_gate_inputs(
            root, inputs.session, inputs.original_packet, inputs.source,
        )
    except (ReleaseContractError, OSError, TypeError, ValueError) as error:
        raise PublicFreshE2EError("public-fresh-e2e-input-stale", "public fresh E2E inputs cannot be physically reopened") from error
    if observed != inputs:
        _refuse("public-fresh-e2e-input-stale", "public fresh E2E inputs changed after reopening")
    return observed


def _safe_relative(root: Path, path: Path, *, label: str) -> str:
    try:
        relative = path.relative_to(root).as_posix()
    except ValueError as error:
        raise PublicFreshE2EError("public-fresh-e2e-path-unsafe", f"{label} is outside the Project") from error
    parsed = PurePosixPath(relative)
    if (not relative or parsed.is_absolute() or parsed.as_posix() != relative
            or any(part in {"", ".", ".."} for part in parsed.parts)):
        _refuse("public-fresh-e2e-path-unsafe", f"{label} is not a safe Project-relative path")
    return relative


def _fresh_parent(root: Path, inputs: PublicFreshGateInputs, *, create: bool) -> Path:
    relative = _safe_relative(root, inputs.fresh_attempt_root, label="fresh public action root")
    try:
        expected = root / ".caprmedio_tmp" / "public_release_full_gate"
        inputs.fresh_attempt_root.relative_to(expected)
    except ValueError:
        _refuse("public-fresh-e2e-path-unsafe", "fresh public action root is outside its fixed namespace")
    return _e2e._safe_path(root, relative, create=create)


def _regular(root: Path, relative: object, *, label: str) -> Path:
    if not isinstance(relative, str):
        _refuse("public-fresh-e2e-path-unsafe", f"{label} path is invalid")
    try:
        return _e2e._regular(root, relative, label=label)
    except ReleaseContractError as error:
        raise PublicFreshE2EError(error.code, str(error)) from error


def _directory(root: Path, relative: object, *, label: str) -> Path:
    if not isinstance(relative, str):
        _refuse("public-fresh-e2e-path-unsafe", f"{label} path is invalid")
    parsed = PurePosixPath(relative)
    if (not relative or parsed.is_absolute() or parsed.as_posix() != relative
            or any(part in {"", ".", ".."} for part in parsed.parts)):
        _refuse("public-fresh-e2e-path-unsafe", f"{label} path is invalid")
    target = root.joinpath(*parsed.parts)
    try:
        resolved = target.resolve(strict=True)
        resolved.relative_to(root.resolve(strict=True))
    except (OSError, ValueError) as error:
        raise PublicFreshE2EError("public-fresh-e2e-path-unsafe", f"{label} escapes the Project") from error
    if target.is_symlink() or not resolved.is_dir():
        _refuse("public-fresh-e2e-path-unsafe", f"{label} is absent or unsafe")
    return resolved


def _read_unit_phase_binding(root: Path, inputs: PublicFreshGateInputs,
                             suite: PortableSuiteGateEvidence) -> None:
    """Open the action-local edge to an otherwise canonical Unit receipt."""

    action_root = _fresh_parent(root, inputs, create=False)
    try:
        phase_path = action_root / "unit-phase.json"
        relative = phase_path.relative_to(root).as_posix()
    except ValueError as error:  # guarded by _fresh_parent; retain a stable refusal
        raise PublicFreshE2EError("public-fresh-e2e-phase-binding-invalid", "fresh Unit phase binding is outside the Project") from error
    payload = _regular(root, relative, label="fresh Unit phase binding").read_bytes()
    try:
        document = json.loads(payload.decode("utf-8"), object_pairs_hook=_e2e._reject_duplicates)
    except (UnicodeDecodeError, json.JSONDecodeError, ReleaseContractError) as error:
        raise PublicFreshE2EError("public-fresh-e2e-phase-binding-invalid", "fresh Unit phase binding is not canonical JSON") from error
    expected = {
        "schema": "caprmedio.public_unit_phase_binding.v1",
        "action_run_id": inputs.action_run_id,
        "phase": inputs.phase,
        "public_document_closure_sha256": inputs.public_document_closure_sha256,
        "suite_evidence_root": suite.evidence_root,
        "suite_receipt_sha256": suite.receipt_sha256,
    }
    if not isinstance(document, dict) or set(document) != set(expected) or document != expected or canonical_json(document) != payload:
        _refuse("public-fresh-e2e-phase-binding-mismatch", "fresh Unit phase binding differs from the admitted public action and Unit")


def _read_fresh_suite(root: Path, inputs: PublicFreshGateInputs,
                      suite: object) -> PortableSuiteGateEvidence:
    """Open canonical Unit evidence and the program-owned action phase edge.

    This reader never executes Unit. Freshness originates in the preceding
    program-owned Unit invocation, which writes canonical runtime evidence and
    supplies the outer producer's six-field action edge. The canonical root,
    physical digests, and edge prevent exact predecessor reuse, but neither a
    root nor a receipt-digest inequality alone proves fresh execution.
    """

    if not isinstance(suite, PortableSuiteGateEvidence) or not suite.passed:
        _refuse("public-fresh-e2e-suite-untrusted", "public fresh E2E requires passed typed portable Unit evidence")
    if type(suite.exit_code) is not int or suite.exit_code != 0:
        _refuse("public-fresh-e2e-suite-untrusted", "fresh portable Unit has no successful process exit")
    view = inputs.retained_package.view
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
    if any(getattr(suite, key, None) != value for key, value in expected.items()):
        _refuse("public-fresh-e2e-suite-mismatch", "fresh portable Unit does not bind the retained package")
    if suite.receipt_sha256 == inputs.original_packet.suite.receipt_sha256:
        _refuse("public-fresh-e2e-suite-stale", "original native Unit receipt cannot prove the public fresh gate")
    if not isinstance(suite.evidence_root, str) or not isinstance(suite.receipt_sha256, str):
        _refuse("public-fresh-e2e-suite-untrusted", "fresh portable Unit receipt fields are invalid")
    suite_root = _directory(root, suite.evidence_root, label="fresh portable Unit evidence")
    expected_prefix = Path(".caprmedio_runtime") / "release_suite" / view.candidate_snapshot_manifest_sha256
    try:
        relative = suite_root.relative_to(root)
    except ValueError:
        _refuse("public-fresh-e2e-suite-stale", "fresh portable Unit is outside the Project")
    if (
        len(relative.parts) != len(expected_prefix.parts) + 1
        or relative.parts[:len(expected_prefix.parts)] != expected_prefix.parts
        or not relative.parts[-1].startswith("attempt-")
    ):
        _refuse("public-fresh-e2e-suite-stale", "fresh portable Unit is outside the canonical candidate attempt layout")
    files = {
        name: _regular(root, f"{suite.evidence_root}/{name}", label=f"fresh portable Unit {name}")
        for name in ("receipt.json", "stdout.bin", "stderr.bin", "coverage.xml")
    }
    receipt = files["receipt.json"].read_bytes()
    if (
        _e2e._digest(receipt) != suite.receipt_sha256
        or receipt != canonical_json(asdict(replace(suite, receipt_sha256=None)))
        or _e2e._digest(files["stdout.bin"].read_bytes()) != suite.stdout_sha256
        or _e2e._digest(files["stderr.bin"].read_bytes()) != suite.stderr_sha256
        or _e2e._digest(files["coverage.xml"].read_bytes()) != suite.report_sha256
    ):
        _refuse("public-fresh-e2e-suite-untrusted", "fresh portable Unit receipt or artifacts changed")
    _read_unit_phase_binding(root, inputs, suite)
    current = _current_binding(root, inputs)
    capability = _freeze_current_capability(root, current)
    if (
        suite.executing_selector_sha256 != capability.executing_selector_sha256
        or suite.executing_release_package_sha256 != capability.executing_release_package_sha256
        or suite.executing_skill_sha256 != capability.executing_skill_sha256
    ):
        _refuse("public-fresh-e2e-suite-current-n-mismatch", "fresh Unit did not execute against current selected native N")
    return suite


def _current_binding(root: Path, inputs: PublicFreshGateInputs) -> NativeInstalledNBinding:
    try:
        current = reopen_native_installed_n(root, inputs.current_native_n)
    except (ReleaseContractError, OSError, TypeError, ValueError) as error:
        raise PublicFreshE2EError("public-fresh-e2e-current-n-stale", "current selected native N cannot be reopened") from error
    if current != inputs.current_native_n:
        _refuse("public-fresh-e2e-current-n-stale", "current selected native N changed after public input reopening")
    return current


def _freeze_current_capability(root: Path, binding: NativeInstalledNBinding) -> FrozenHostE2ECapability:
    """Freeze the currently selected N, not the predecessor retained packet."""

    package = binding.verified_package
    try:
        package_relative = package.root.resolve(strict=True).relative_to(root).as_posix()
    except (OSError, ValueError) as error:
        raise PublicFreshE2EError("public-fresh-e2e-current-n-invalid", "current native package is outside the Project") from error
    expected_skill = {
        row.path.removeprefix("SKILLS/ca/"): (row.sha256, row.mode)
        for row in package.inventory if row.path.startswith("SKILLS/ca/")
    }
    expected_directories = {
        parent.as_posix() for name in expected_skill for parent in Path(name).parents if parent != Path(".")
    }
    actual_skill, actual_directories = _active_skill_records(root, PROJECT_SKILL_TARGET)
    if actual_skill != expected_skill or actual_directories != expected_directories:
        _refuse("public-fresh-e2e-current-n-invalid", "project-local ca Skill differs from current selected native package")
    controller_relative = f"{package_relative}/{_e2e._N_DRIVER_RELATIVE}"
    controller = _regular(root, controller_relative, label="current N host controller")
    try:
        python = HostE2EExecutor._external_identity(Path(sys.executable), role="python")
        docker_path = next((Path(value) for value in _e2e._DOCKER_CANDIDATES if Path(value).is_file()), None)
        if docker_path is None:
            _refuse("public-fresh-e2e-host-missing", "trusted Docker executable is unavailable")
        docker = HostE2EExecutor._external_identity(docker_path, role="docker")
    except (OSError, ReleaseContractError) as error:
        raise PublicFreshE2EError("public-fresh-e2e-host-invalid", "trusted host executable cannot be frozen") from error
    controller_identity = ExecutableIdentity("n_host_controller", str(controller), _e2e._digest(controller.read_bytes()))
    driver_identity = ExecutableIdentity("driver", str(controller), _e2e._digest(controller.read_bytes()))
    return FrozenHostE2ECapability(
        binding.selected.selector_sha256,
        tree_sha256(root, package_relative),
        _e2e._digest(canonical_json({"files": actual_skill, "directories": sorted(actual_directories)})),
        controller_identity,
        python,
        driver_identity,
        docker,
        str(Path(docker.path).parent),
    )


def _reopen_original_image(inputs: PublicFreshGateInputs) -> str:
    """Use original build/verification only to prove immutable image provenance."""

    packet = inputs.original_packet
    try:
        read_detached_image_execution_artifacts(
            packet.artifact_root, packet.retained_candidate, packet.suite, packet.build, packet.verification,
        )
    except (ReleaseContractError, OSError, TypeError, ValueError) as error:
        raise PublicFreshE2EError("public-fresh-e2e-image-untrusted", "original native image provenance cannot be reopened") from error
    image = packet.verification.candidate_image_digest
    if image != packet.build.candidate_image_digest or image != f"sha256:{inputs.current_native_n.selected.image_digest}":
        _refuse("public-fresh-e2e-image-mismatch", "current selected native image differs from original verified image")
    return image


def _fresh_grammar_and_limits(root: Path, inputs: PublicFreshGateInputs) -> tuple[dict, bytes, str, _e2e.ReleaseE2ELimits]:
    """Open retained grammar/limits as immutable execution configuration only."""

    original = inputs.original_packet.e2e
    try:
        grammar, grammar_bytes = _e2e._reopen_retained_grammar(root, original)
        limits = _e2e._reopen_retained_release_e2e_settings(root, original)
    except ReleaseContractError as error:
        raise PublicFreshE2EError("public-fresh-e2e-configuration-untrusted", "retained E2E grammar or limits cannot be reopened") from error
    grammar_sha256 = _e2e._digest(grammar_bytes)
    if grammar_sha256 != original.grammar_sha256:
        _refuse("public-fresh-e2e-configuration-untrusted", "retained E2E grammar digest changed")
    phase_map = inputs.retained_package.view.phase_map
    grammar_paths = tuple(sorted(row["source_path"] for row in grammar["harnesses"]))
    if grammar_paths != phase_map.candidate_e2e_paths:
        _refuse("public-fresh-e2e-phase-map-mismatch", "retained E2E grammar does not match the retained exact three-host phase map")
    for source_path, source_sha256, phase in phase_map.rows:
        if phase == "candidate_e2e" and _e2e._digest(_regular(root, source_path, label="fresh E2E source").read_bytes()) != source_sha256:
            _refuse("public-fresh-e2e-source-stale", "current host harness source differs from the retained package pin")
    return grammar, grammar_bytes, grammar_sha256, limits


def _attempt(root: Path, inputs: PublicFreshGateInputs) -> tuple[Path, str]:
    """Allocate the established E2E receipt location for the retained candidate."""

    candidate = inputs.retained_package.view.candidate_snapshot_manifest_sha256
    if not isinstance(candidate, str) or len(candidate) != 64:
        _refuse("public-fresh-e2e-package-invalid", "retained candidate identity is invalid")
    parent = _e2e._safe_path(root, f"{_e2e.EVIDENCE_ROOT}/{candidate}", create=True)
    attempt = Path(tempfile.mkdtemp(prefix="attempt-", dir=parent))
    return attempt, _safe_relative(root, attempt, label="fresh public E2E attempt")


def _write_configuration(root: Path, inputs: PublicFreshGateInputs, attempt: Path, grammar_bytes: bytes) -> tuple[str, str]:
    """Copy only configuration bytes into the new receipt namespace."""

    old = inputs.original_packet.e2e
    settings = _regular(root, old.settings_snapshot_path, label="retained E2E settings snapshot").read_bytes()
    default = _regular(root, f"{old.evidence_root}/{_e2e._RETAINED_DEFAULT_SETTINGS_FILENAME}", label="retained default E2E settings").read_bytes()
    instance = _regular(root, f"{old.evidence_root}/{_e2e._RETAINED_INSTANCE_SETTINGS_FILENAME}", label="retained instance E2E settings").read_bytes()
    _e2e._write_new(attempt / _e2e._SETTINGS_SNAPSHOT_FILENAME, settings)
    _e2e._write_new(attempt / _e2e._RETAINED_GRAMMAR_FILENAME, grammar_bytes)
    _e2e._write_new(attempt / _e2e._RETAINED_DEFAULT_SETTINGS_FILENAME, default)
    _e2e._write_new(attempt / _e2e._RETAINED_INSTANCE_SETTINGS_FILENAME, instance)
    return (
        (attempt / _e2e._SETTINGS_SNAPSHOT_FILENAME).relative_to(root).as_posix(),
        _e2e._digest(settings),
    )


def _read_fresh_e2e(root: Path, inputs: PublicFreshGateInputs,
                    suite: PortableSuiteGateEvidence, evidence: object) -> FrozenHostE2ECapability:
    """Physically reopen one fresh action-scoped E2E receipt.

    This deliberately does not delegate to the legacy candidate-E2E reader:
    that reader requires a live pre-install candidate and may reopen its old N.
    Here the frozen host capability is derived from current selected N instead.
    """

    if not isinstance(evidence, PortableCandidateE2EGateEvidence) or not evidence.passed:
        _refuse("public-fresh-e2e-evidence-untrusted", "fresh public E2E requires passed typed host evidence")
    if evidence.execution_kind != "host-subprocess":
        _refuse("public-fresh-e2e-evidence-untrusted", "test-double E2E cannot prove public fresh evidence")
    if evidence.receipt_sha256 == inputs.original_packet.e2e.receipt_sha256:
        _refuse("public-fresh-e2e-evidence-stale", "original native E2E receipt cannot prove the public fresh gate")
    view = inputs.retained_package.view
    image = _reopen_original_image(inputs)
    grammar, _grammar_bytes, grammar_sha256, limits = _fresh_grammar_and_limits(root, inputs)
    expected = {
        "candidate_snapshot_manifest_sha256": view.candidate_snapshot_manifest_sha256,
        "candidate_image_digest": image,
        "phase_map_sha256": view.phase_map.sha256,
        "grammar_sha256": grammar_sha256,
        "package_schema": "portable-1",
        "package_manifest_sha256": view.actual_package_manifest_sha256,
        "package_evidence_sha256": inputs.retained_package.receipt_sha256,
        "source_catalog_sha256": view.source_catalog_sha256,
        "candidate_run_id": view.candidate_run_id,
        "input_manifest_sha256": view.input_manifest_sha256,
        "framework_version": view.framework_version,
        "version_toml_sha256": view.version_toml_sha256,
    }
    if any(getattr(evidence, key, None) != value for key, value in expected.items()):
        _refuse("public-fresh-e2e-evidence-mismatch", "fresh E2E evidence binds another package, image, or source phase")
    try:
        expected_sidecar = inputs.retained_package.receipt_path.relative_to(root).as_posix()
    except ValueError as error:
        raise PublicFreshE2EError("public-fresh-e2e-package-invalid", "retained package sidecar is outside the Project") from error
    if evidence.package_evidence_relpath != expected_sidecar:
        _refuse("public-fresh-e2e-evidence-mismatch", "fresh E2E sidecar reference differs from the reopened package")
    attempt = _directory(root, evidence.evidence_root, label="fresh public E2E evidence")
    try:
        relative = attempt.relative_to(root)
    except ValueError:
        _refuse("public-fresh-e2e-evidence-stale", "fresh E2E evidence is outside the Project")
    expected_prefix = Path(_e2e.EVIDENCE_ROOT) / view.candidate_snapshot_manifest_sha256
    if (
        len(relative.parts) != len(expected_prefix.parts) + 1
        or relative.parts[:len(expected_prefix.parts)] != expected_prefix.parts
        or not relative.parts[-1].startswith("attempt-")
    ):
        _refuse("public-fresh-e2e-evidence-stale", "fresh E2E evidence is outside the canonical candidate attempt layout")
    receipt = _regular(root, f"{evidence.evidence_root}/receipt.json", label="fresh public E2E receipt").read_bytes()
    if _e2e._digest(receipt) != evidence.receipt_sha256 or receipt != canonical_json(asdict(replace(evidence, receipt_sha256=None))):
        _refuse("public-fresh-e2e-evidence-untrusted", "fresh public E2E receipt changed or is caller-forged")
    if (
        evidence.settings_snapshot_path != f"{evidence.evidence_root}/{_e2e._SETTINGS_SNAPSHOT_FILENAME}"
        or not isinstance(evidence.settings_snapshot_sha256, str)
    ):
        _refuse("public-fresh-e2e-evidence-untrusted", "fresh E2E settings snapshot is unbound")
    try:
        retained_limits = _e2e._reopen_retained_release_e2e_settings(root, evidence)
    except ReleaseContractError as error:
        raise PublicFreshE2EError("public-fresh-e2e-evidence-untrusted", "fresh E2E settings packet is invalid") from error
    if retained_limits != limits:
        _refuse("public-fresh-e2e-evidence-untrusted", "fresh E2E limits differ from the retained fixed configuration")
    if (
        evidence.host_capability_path != f"{evidence.evidence_root}/host-identities.json"
        or not isinstance(evidence.host_capability_sha256, str)
    ):
        _refuse("public-fresh-e2e-evidence-untrusted", "fresh host capability carrier is unbound")
    try:
        capability = _e2e._reopen_host_capability(root, evidence)
    except ReleaseContractError as error:
        raise PublicFreshE2EError("public-fresh-e2e-capability-untrusted", "fresh E2E host capability changed or is invalid") from error
    current = _current_binding(root, inputs)
    if capability != _freeze_current_capability(root, current):
        _refuse("public-fresh-e2e-current-n-stale", "fresh E2E host capability differs from current selected native N")
    if (
        suite.executing_selector_sha256 != capability.executing_selector_sha256
        or suite.executing_release_package_sha256 != capability.executing_release_package_sha256
        or suite.executing_skill_sha256 != capability.executing_skill_sha256
    ):
        _refuse("public-fresh-e2e-suite-current-n-mismatch", "fresh Unit and E2E used different current selected native N")
    expected_rows = tuple(grammar["harnesses"])
    if len(evidence.harness_receipts) != 3 or len(expected_rows) != 3:
        _refuse("public-fresh-e2e-evidence-untrusted", "fresh E2E receipt lacks the exact three host harnesses")
    inspect = _regular(root, f"{evidence.evidence_root}/inspect.stdout.bin", label="fresh E2E inspect stdout").read_bytes()
    _regular(root, f"{evidence.evidence_root}/inspect.stderr.bin", label="fresh E2E inspect stderr")
    if inspect.decode("utf-8", "replace").strip() != image:
        _refuse("public-fresh-e2e-evidence-untrusted", "fresh E2E inspection does not prove the immutable image")
    source_sha256s = {path: digest for path, digest, phase in view.phase_map.rows if phase == "candidate_e2e"}
    for index, (row, receipt_row) in enumerate(zip(expected_rows, evidence.harness_receipts, strict=True)):
        pattern = Path(row["source_path"]).name
        expected_argv = (
            capability.python.path, capability.n_host_controller.path,
            *row["argv"][2:7],
            str(attempt / "scratch" / "reports" / f"{pattern}.xml"),
        )
        expected_stdout = f"{evidence.evidence_root}/harness-{index}.stdout.bin"
        expected_stderr = f"{evidence.evidence_root}/harness-{index}.stderr.bin"
        expected_junit = f"{evidence.evidence_root}/harness-{index}.junit.xml"
        if (
            receipt_row.source_path != row["source_path"]
            or receipt_row.source_sha256 != source_sha256s.get(receipt_row.source_path)
            or receipt_row.argv != expected_argv
            or receipt_row.stdout_path != expected_stdout
            or receipt_row.stderr_path != expected_stderr
            or receipt_row.junit_path != expected_junit
            or receipt_row.exit_code != 0
            or receipt_row.timed_out is not False
            or not isinstance(receipt_row.reason, str)
            or receipt_row.reason
        ):
            _refuse("public-fresh-e2e-evidence-untrusted", "fresh E2E harness receipt has unbound fields")
        stdout = _regular(root, expected_stdout, label="fresh E2E stdout").read_bytes()
        stderr = _regular(root, expected_stderr, label="fresh E2E stderr").read_bytes()
        junit = _regular(root, expected_junit, label="fresh E2E JUnit")
        tests, junit_sha, junit_reason, _payload = _e2e._observe_junit(junit, limits.max_junit_bytes)
        if (
            receipt_row.stdout_sha256 != _e2e._digest(stdout)
            or receipt_row.stderr_sha256 != _e2e._digest(stderr)
            or receipt_row.junit_sha256 != junit_sha
            or receipt_row.executed_tests != tests
            or junit_reason
        ):
            _refuse("public-fresh-e2e-evidence-untrusted", "fresh E2E harness artifacts are incomplete or changed")
    return capability


def read_public_candidate_e2e_execution_artifacts(
    inputs: PublicFreshGateInputs,
    fresh_suite: PortableSuiteGateEvidence,
    fresh_e2e: PortableCandidateE2EGateEvidence,
) -> Path:
    """Reopen the invocation-produced Unit/E2E evidence; performs no execution.

    Canonical runtime receipt locations and the action-local Unit phase edge
    authenticate the immutable carriers for this admitted public action. They
    validate, rather than create, the preceding program-owned fresh Unit work.
    """

    inputs = _reopen_inputs(inputs)
    root = _root(inputs)
    suite = _read_fresh_suite(root, inputs, fresh_suite)
    _read_fresh_e2e(root, inputs, suite, fresh_e2e)
    if _reopen_inputs(inputs) != inputs or _read_fresh_suite(root, inputs, suite) != suite:
        _refuse("public-fresh-e2e-currentness-stale", "public fresh E2E inputs changed while reopening evidence")
    return root


def run_public_candidate_e2e_gate(
    inputs: PublicFreshGateInputs,
    suite: PortableSuiteGateEvidence,
    *,
    executor: HostE2EExecutor,
) -> PortableCandidateE2EGateEvidence:
    """Execute exactly one fresh host-Docker/MCP E2E triplet for O194 or O198.

    ``executor`` must be the actual production ``HostE2EExecutor``; it is an
    explicit typed capability, not a callback or caller-supplied result. The
    returned evidence has a new canonical E2E receipt and never carries the
    predecessor E2E receipt as proof.
    """

    if type(executor) is not HostE2EExecutor:
        _refuse("public-fresh-e2e-executor-untrusted", "public fresh E2E requires the production HostE2EExecutor")
    inputs = _reopen_inputs(inputs)
    root = _root(inputs)
    suite = _read_fresh_suite(root, inputs, suite)
    current = _current_binding(root, inputs)
    image = _reopen_original_image(inputs)
    grammar, grammar_bytes, grammar_sha256, limits = _fresh_grammar_and_limits(root, inputs)
    capability = _freeze_current_capability(root, current)
    executor._bind_frozen_limits(limits)
    phase_map = inputs.retained_package.view.phase_map
    if (
        suite.executing_selector_sha256 != capability.executing_selector_sha256
        or suite.executing_release_package_sha256 != capability.executing_release_package_sha256
        or suite.executing_skill_sha256 != capability.executing_skill_sha256
    ):
        _refuse("public-fresh-e2e-suite-current-n-mismatch", "fresh Unit did not execute against the current selected native N")
    attempt, evidence_root = _attempt(root, inputs)
    scratch = attempt / "scratch"
    reports = scratch / "reports"
    scratch.mkdir()
    reports.mkdir()
    settings_path: str | None = None
    settings_sha256: str | None = None
    host_path: str | None = None
    host_sha256: str | None = None
    receipts: list[HarnessReceipt] = []
    outcome: Literal["passed", "failed", "timed_out", "incomplete", "stale", "recording_uncertain"] = "incomplete"
    reason = "fresh public E2E evidence is incomplete"
    source_sha256s = {path: digest for path, digest, phase in phase_map.rows if phase == "candidate_e2e"}
    try:
        settings_path, settings_sha256 = _write_configuration(root, inputs, attempt, grammar_bytes)
        context, harnesses = _e2e._context_bytes_for_binding(
            root, scratch, reports, inputs.retained_package.view.candidate_snapshot_manifest_sha256,
            image, grammar_sha256, phase_map.sha256, grammar,
        )
        context_path = scratch / "context.json"
        _e2e._write_new(context_path, context)
        capability_bytes = _e2e._host_identities_bytes(capability)
        capability_file = attempt / "host-identities.json"
        _e2e._write_new(capability_file, capability_bytes)
        host_path = capability_file.relative_to(root).as_posix()
        host_sha256 = _e2e._digest(capability_bytes)
        environment = {
            "PATH": capability.closed_path,
            "TMPDIR": str(scratch),
            CONTEXT_ENVIRONMENT_VARIABLE: str(context_path),
            CANDIDATE_IMAGE_ENVIRONMENT_VARIABLE: image,
        }
        inspect = _e2e._cap_test_double_result(_e2e._execution_result(executor.run(
            ("docker", "image", "inspect", "--format", "{{.Id}}", image),
            cwd=root, environment=environment, timeout_seconds=limits.inspect_timeout_seconds,
        )), limits)
        _e2e._write_new(attempt / "inspect.stdout.bin", inspect.stdout)
        _e2e._write_new(attempt / "inspect.stderr.bin", inspect.stderr)
        if inspect.cleanup_uncertain:
            outcome, reason = "incomplete", "fresh immutable image inspection cleanup is uncertain"
        elif inspect.timed_out:
            outcome, reason = "timed_out", "fresh immutable image inspection timed out"
        elif inspect.output_limited:
            outcome, reason = "incomplete", "fresh immutable image inspection exceeded a frozen output limit"
        elif inspect.exit_code != 0:
            outcome, reason = "failed", "fresh immutable image inspection failed"
        elif inspect.stdout.decode("utf-8", "replace").strip() != image:
            outcome, reason = "failed", "fresh immutable image inspection returned a different image ID"
        else:
            outcome, reason = "passed", "all three fresh public host E2E harnesses passed"
            for row, harness in zip(grammar["harnesses"], harnesses, strict=True):
                argv = tuple(
                    capability.python.path if token == "{trusted_python}"
                    else capability.n_host_controller.path if token == _e2e.DRIVER_RELATIVE
                    else harness["junit_path"] if token == "{e2e_junit_path}" else token
                    for token in row["argv"]
                )
                started_at = _e2e._utc_timestamp()
                started = time.monotonic()
                result = _e2e._cap_test_double_result(_e2e._execution_result(executor.run(
                    argv, cwd=root, environment=environment, timeout_seconds=limits.harness_timeout_seconds,
                )), limits)
                elapsed = time.monotonic() - started
                finished_at = _e2e._utc_timestamp()
                ordinal = len(receipts)
                stdout_path = f"{evidence_root}/harness-{ordinal}.stdout.bin"
                stderr_path = f"{evidence_root}/harness-{ordinal}.stderr.bin"
                junit_path = f"{evidence_root}/harness-{ordinal}.junit.xml"
                _e2e._write_new(attempt / f"harness-{ordinal}.stdout.bin", result.stdout)
                _e2e._write_new(attempt / f"harness-{ordinal}.stderr.bin", result.stderr)
                tests, junit_sha, junit_reason, junit_payload = _e2e._observe_junit(
                    Path(harness["junit_path"]), limits.max_junit_bytes,
                )
                if junit_sha is not None and junit_payload is not None:
                    _e2e._write_new(attempt / f"harness-{ordinal}.junit.xml", junit_payload)
                phase_reason = ""
                if result.cleanup_uncertain:
                    outcome, reason, phase_reason = "incomplete", f"fresh E2E cleanup is uncertain: {harness['pattern']}", "process cleanup is uncertain"
                elif result.timed_out:
                    outcome, reason, phase_reason = "timed_out", f"fresh E2E timed out: {harness['pattern']}", "harness timed out"
                elif result.output_limited:
                    outcome, reason, phase_reason = "incomplete", f"fresh E2E output exceeded a frozen limit: {harness['pattern']}", "harness output exceeded a frozen limit"
                elif result.exit_code != 0:
                    outcome, reason, phase_reason = "failed", f"fresh E2E failed: {harness['pattern']}", "harness exited nonzero"
                elif junit_reason:
                    outcome, reason, phase_reason = "incomplete", f"fresh E2E JUnit is incomplete: {harness['pattern']}", junit_reason
                receipts.append(HarnessReceipt(
                    harness["source_path"], source_sha256s[harness["source_path"]], argv,
                    started_at, finished_at, result.exit_code, result.timed_out,
                    stdout_path, _e2e._digest(result.stdout), stderr_path, _e2e._digest(result.stderr),
                    junit_path, junit_sha, tests, elapsed, phase_reason,
                ))
                if outcome != "passed":
                    break
        if _reopen_inputs(inputs) != inputs or _read_fresh_suite(root, inputs, suite) != suite:
            raise PublicFreshE2EError("public-fresh-e2e-currentness-stale", "public action or fresh Unit changed during E2E")
        if _current_binding(root, inputs) != current or _freeze_current_capability(root, current) != capability:
            raise PublicFreshE2EError("public-fresh-e2e-currentness-stale", "current selected native N changed during E2E")
        _reopen_original_image(inputs)
        _fresh_grammar_and_limits(root, inputs)
    except ReleaseContractError as error:
        outcome = "stale" if getattr(error, "code", "") in {
            "public-fresh-e2e-currentness-stale", "public-fresh-e2e-input-stale", "public-fresh-e2e-source-stale",
        } else "incomplete"
        reason = str(error)
    except (OSError, TypeError, ValueError) as error:
        outcome, reason = "recording_uncertain", f"fresh public E2E evidence could not be recorded: {type(error).__name__}"
    view = inputs.retained_package.view
    try:
        sidecar = inputs.retained_package.receipt_path.relative_to(root).as_posix()
    except ValueError as error:
        raise PublicFreshE2EError("public-fresh-e2e-package-invalid", "retained package sidecar is outside the Project") from error
    evidence = PortableCandidateE2EGateEvidence(
        candidate_snapshot_manifest_sha256=view.candidate_snapshot_manifest_sha256,
        candidate_image_digest=image,
        phase_map_sha256=phase_map.sha256,
        grammar_sha256=grammar_sha256,
        outcome=outcome,
        reason=reason,
        harness_receipts=tuple(receipts),
        evidence_root=evidence_root,
        receipt_sha256=None,
        settings_snapshot_path=settings_path,
        settings_snapshot_sha256=settings_sha256,
        host_capability_path=host_path,
        host_capability_sha256=host_sha256,
        execution_kind="host-subprocess",
        package_schema="portable-1",
        package_manifest_sha256=view.actual_package_manifest_sha256,
        package_evidence_sha256=inputs.retained_package.receipt_sha256,
        package_evidence_relpath=sidecar,
        source_catalog_sha256=view.source_catalog_sha256,
        candidate_run_id=view.candidate_run_id,
        input_manifest_sha256=view.input_manifest_sha256,
        framework_version=view.framework_version,
        version_toml_sha256=view.version_toml_sha256,
    )
    try:
        receipt = canonical_json(asdict(evidence))
        _e2e._write_new(attempt / "receipt.json", receipt)
        descriptor = os.open(attempt, os.O_RDONLY)
        try:
            os.fsync(descriptor)
        finally:
            os.close(descriptor)
        return replace(evidence, receipt_sha256=_e2e._digest(receipt))
    except OSError:
        return replace(evidence, outcome="recording_uncertain", reason="fresh public E2E receipt could not be durably recorded")


__all__ = [
    "PublicFreshE2EError",
    "read_public_candidate_e2e_execution_artifacts",
    "run_public_candidate_e2e_gate",
]
