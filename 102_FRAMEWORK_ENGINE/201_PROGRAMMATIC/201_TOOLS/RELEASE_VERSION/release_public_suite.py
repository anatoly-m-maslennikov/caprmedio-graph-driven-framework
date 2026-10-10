"""Fresh immutable-package Unit execution for one admitted public action.

The public Full Gate cannot reuse its original Unit receipt as fresh proof.
This adapter reopens the already-admitted public Action, its detached package
evidence, and the currently selected native N+1 before a later executor is
allowed to run the common suite engine.  The only execution API below accepts
an admitted Docker boundary and writes a normal, durable Unit attempt; it has
no publication or caller-supplied callback path.
"""

from __future__ import annotations

import hashlib
import os
import tempfile
import time
from dataclasses import asdict, dataclass, replace
from pathlib import Path, PurePosixPath
from typing import Literal

from release_contract import ReleaseContractError
from release_handoff import NativeInstalledNBinding, reopen_native_installed_n
from release_image import DockerExecutor
from release_public_gate import PublicFreshGateInputs, reopen_public_fresh_gate_inputs
from release_retained_candidate import reopen_retained_candidate_identity
from release_suite import (
    EVIDENCE_ROOT, SANDBOX_OUTPUT_PATH, SANDBOX_WORKSPACE_PATH,
    MODULE_RULES_RELATIVE, PortableSuiteGateEvidence, SuiteExecutionResult,
    _copy_report_from_output, _durable_bytes, _materialize_suite_workspace,
    _observe_report, _suite_process_environment, _write_capture, _active_native_n_state,
    _write_unit_deadline, _verify_unit_deadline, _safe_path, canonical_json,
    require_declared_suite_command,
)
from release_suite_execution import installed_public_n_suite_executor
from release_suite_limits import resolve_unit_deadline
from release_suite_reference_context import (
    ReleaseSuiteReferenceContextError, capture_context, revalidate_context,
)
from release_suite_inputs import SealedSourcePath
from release_test_phases import ReleaseTestPhaseMap


_SHA256 = frozenset("0123456789abcdef")
_PACKAGE_ROLE = {
    "engine": ("FRAMEWORK_ENGINE", "engine"),
    "skill": ("SKILL", "skill_projection"),
    "methodology": ("METHODOLOGY", "methodology"),
    "methodology-support": ("METHODOLOGY", "support"),
}


class PublicSuiteInputError(ReleaseContractError):
    """A fresh public Unit suite input cannot be physically reopened."""


@dataclass(frozen=True)
class DetachedPublicSuiteInputs:
    """Only immutable package rows and current-N facts for a fresh Unit run."""

    project_root: Path
    package_root: Path
    candidate_snapshot_manifest_sha256: str
    candidate_run_id: str
    input_manifest_sha256: str
    source_catalog_sha256: str
    framework_version: str
    version_toml_sha256: str
    current_native_n: NativeInstalledNBinding
    phase: Literal["initial", "history_link"]
    action_run_id: str
    fresh_attempt_root: Path
    command: tuple[str, ...]
    working_directory: str
    source_rows: tuple[SealedSourcePath, ...]
    compiled_root: str
    phase_map: ReleaseTestPhaseMap


def _error(code: str, message: str) -> PublicSuiteInputError:
    return PublicSuiteInputError(code, message)


def _sha256(value: object, *, field: str) -> str:
    if not isinstance(value, str) or len(value) != 64 or set(value) - _SHA256:
        raise _error("public-suite-input-invalid", f"{field} must be a lowercase SHA-256")
    return value


def _safe_package_path(value: object, *, field: str) -> PurePosixPath:
    if not isinstance(value, str) or not value or "\\" in value:
        raise _error("public-suite-package-path-invalid", f"{field} must be a package-relative path")
    path = PurePosixPath(value)
    if path.is_absolute() or path.as_posix() != value or any(part in {"", ".", ".."} for part in path.parts):
        raise _error("public-suite-package-path-invalid", f"{field} must be a package-relative path")
    return path


def _regular_member(package_root: Path, path: PurePosixPath, *, sha256: str, mode: int) -> None:
    target = package_root.joinpath(*path.parts)
    cursor = package_root
    for part in path.parts:
        cursor = cursor / part
        if cursor.is_symlink():
            raise _error("public-suite-package-stale", "retained package member path contains a symlink")
    try:
        if not target.is_file() or target.stat().st_mode & 0o777 != mode:
            raise ValueError
        if hashlib.sha256(target.read_bytes()).hexdigest() != sha256:
            raise ValueError
    except (OSError, ValueError) as error:
        raise _error("public-suite-package-stale", "retained package member differs from its evidence") from error


def _destination(path: PurePosixPath, role: str) -> tuple[str, str]:
    """Derive the existing Unit workspace projection from package identity."""

    text = path.as_posix()
    if role == "engine":
        prefix = "102_FRAMEWORK_ENGINE/"
        if not text.startswith(prefix):
            raise _error("public-suite-package-invalid", "engine member has no Framework Engine package path")
        return text, "FRAMEWORK_ENGINE/" + text.removeprefix(prefix)
    if role == "skill":
        if not text.startswith("SKILLS/ca/"):
            raise _error("public-suite-package-invalid", "Skill member is outside the ca Skill projection")
        return text, text
    for prefix in ("methodology/active/", "methodology/support/"):
        if text.startswith(prefix):
            return text, "METHODOLOGY/sources/" + text.removeprefix(prefix)
    for prefix in ("methodology/compiled/", "METHODOLOGY/compiled/"):
        if text.startswith(prefix):
            return text, "METHODOLOGY/compiled/" + text.removeprefix(prefix)
    raise _error("public-suite-package-invalid", "Methodology member has no declared public suite projection")


def _package_rows(inputs: PublicFreshGateInputs, package_root: Path, view: object) -> tuple[tuple[SealedSourcePath, ...], str]:
    inventory = getattr(view, "member_inventory", None)
    if not isinstance(inventory, tuple) or not inventory:
        raise _error("public-suite-package-invalid", "retained package has no immutable member inventory")
    rows: list[SealedSourcePath] = []
    compiled_roots: set[str] = set()
    for member in inventory:
        role = getattr(member, "role", None)
        projection = _PACKAGE_ROLE.get(role)
        if projection is None:
            continue
        path = _safe_package_path(getattr(member, "path", None), field="retained package member path")
        sha256 = _sha256(getattr(member, "sha256", None), field="retained package member digest")
        mode = getattr(member, "mode", None)
        if type(mode) is not int or not 0 <= mode <= 0o777:
            raise _error("public-suite-package-invalid", "retained package member mode is invalid")
        _regular_member(package_root, path, sha256=sha256, mode=mode)
        resource, origin_kind = projection
        source_path, destination_path = _destination(path, role)
        if source_path.startswith("methodology/compiled/"):
            compiled_roots.add("methodology/compiled")
        elif source_path.startswith("METHODOLOGY/compiled/"):
            compiled_roots.add("METHODOLOGY/compiled")
        rows.append(SealedSourcePath(
            resource, source_path, destination_path, sha256, mode, source_path, origin_kind,
        ))
    ordered = tuple(sorted(rows, key=lambda row: row.source_path))
    if len({row.source_path for row in ordered}) != len(ordered):
        raise _error("public-suite-package-invalid", "retained package has duplicate executable source members")
    if len(compiled_roots) != 1:
        raise _error("public-suite-package-invalid", "retained package has no single compiled Methodology root")
    if not any(row.source_path == MODULE_RULES_RELATIVE for row in ordered):
        raise _error("public-suite-package-invalid", "retained package has no sealed Unit module-rules carrier")
    phase_map = getattr(view, "phase_map", None)
    if not isinstance(phase_map, ReleaseTestPhaseMap):
        raise _error("public-suite-package-invalid", "retained package has no typed Unit phase map")
    source_paths = {row.source_path for row in ordered}
    if not set(phase_map.unit_paths) <= source_paths:
        raise _error("public-suite-package-invalid", "retained Unit phase map names a source outside the package")
    return ordered, next(iter(compiled_roots))


def reopen_public_retained_suite_inputs(inputs: PublicFreshGateInputs) -> DetachedPublicSuiteInputs:
    """Reopen the only detached carriers admissible to a fresh public Unit run."""

    if not isinstance(inputs, PublicFreshGateInputs):
        raise _error("public-suite-input-untrusted", "fresh public Unit requires PublicFreshGateInputs")
    try:
        current_inputs = reopen_public_fresh_gate_inputs(
            inputs.project_root, inputs.session, inputs.original_packet, inputs.source,
        )
    except ReleaseContractError as error:
        raise _error(error.code, str(error)) from error
    if current_inputs != inputs:
        raise _error("public-suite-input-stale", "public fresh-gate inputs changed before Unit execution")
    try:
        identity = reopen_retained_candidate_identity(inputs.original_packet.retained_candidate)
        current_n = reopen_native_installed_n(inputs.project_root, inputs.current_native_n)
    except ReleaseContractError as error:
        raise _error(error.code, str(error)) from error
    if identity != inputs.original_packet.retained_candidate or identity.package_evidence != inputs.retained_package:
        raise _error("public-suite-input-stale", "retained candidate package differs from public gate inputs")
    if current_n != inputs.current_native_n or current_n.full_gate_packet != inputs.original_packet:
        raise _error("public-suite-current-n-stale", "current selected N+1 differs from public gate inputs")
    view = identity.package_evidence.view
    candidate_sha = _sha256(getattr(view, "candidate_snapshot_manifest_sha256", None), field="candidate snapshot manifest")
    if candidate_sha != identity.candidate_snapshot_manifest_sha256:
        raise _error("public-suite-package-invalid", "retained package candidate differs from its descriptor")
    rows, compiled_root = _package_rows(inputs, view.package_root, view)
    suite = inputs.original_packet.suite
    if not isinstance(suite, PortableSuiteGateEvidence) or not suite.passed:
        raise _error("public-suite-original-unit-invalid", "original retained Unit receipt is unavailable for its sealed declaration")
    require_declared_suite_command(suite)
    if (
        suite.candidate_snapshot_manifest_sha256 != candidate_sha
        or suite.candidate_run_id != view.candidate_run_id
        or suite.input_manifest_sha256 != view.input_manifest_sha256
        or suite.source_catalog_sha256 != view.source_catalog_sha256
        or suite.framework_version != view.framework_version
        or suite.version_toml_sha256 != view.version_toml_sha256
        or suite.phase_map_sha256 != view.phase_map.sha256
    ):
        raise _error("public-suite-original-unit-invalid", "original Unit declaration differs from the reopened retained package")
    return DetachedPublicSuiteInputs(
        project_root=inputs.project_root,
        package_root=view.package_root,
        candidate_snapshot_manifest_sha256=candidate_sha,
        candidate_run_id=view.candidate_run_id,
        input_manifest_sha256=view.input_manifest_sha256,
        source_catalog_sha256=view.source_catalog_sha256,
        framework_version=view.framework_version,
        version_toml_sha256=view.version_toml_sha256,
        current_native_n=current_n,
        phase=inputs.phase,
        action_run_id=inputs.action_run_id,
        fresh_attempt_root=inputs.fresh_attempt_root,
        command=suite.command,
        working_directory=suite.working_directory,
        source_rows=rows,
        compiled_root=compiled_root,
        phase_map=view.phase_map,
    )


def _public_context(inputs: DetachedPublicSuiteInputs, executor: object):
    image_context = getattr(executor, "source_context_sha256", None)
    if not isinstance(image_context, str) or len(image_context) != 64 or set(image_context) - _SHA256:
        raise _error("public-suite-executor-untrusted", "current selected N+1 executor has no immutable image context")
    try:
        return capture_context(inputs.project_root, {
            "candidate_snapshot_manifest_sha256": inputs.candidate_snapshot_manifest_sha256,
            "compiled_candidate_root": inputs.compiled_root,
            "selected_n_identity": inputs.candidate_snapshot_manifest_sha256,
            "selected_n_image_context": image_context,
        })
    except ReleaseSuiteReferenceContextError as error:
        raise _error("public-suite-reference-context-invalid", str(error)) from error


def _native_state(inputs: DetachedPublicSuiteInputs) -> tuple[str, str, str]:
    """Reopen the current N+1 package and Skill, never a removed predecessor."""

    try:
        return _active_native_n_state(inputs.project_root, inputs.current_native_n)
    except ReleaseContractError as error:
        raise _error(error.code, str(error)) from error


def _evidence(inputs: DetachedPublicSuiteInputs, *, outcome: str, reason: str,
              exit_code: int | None, executed_tests: int, coverage: tuple[str, ...],
              evidence_root: str, stdout_sha256: str | None, stderr_sha256: str | None,
              report_sha256: str | None, active_n: tuple[str, str, str],
              receipt_sha256: str | None, elapsed_seconds: float,
              control_context_digest: str | None) -> PortableSuiteGateEvidence:
    return PortableSuiteGateEvidence(
        input_schema="portable-1", candidate_snapshot_manifest_sha256=inputs.candidate_snapshot_manifest_sha256,
        candidate_run_id=inputs.candidate_run_id, input_manifest_sha256=inputs.input_manifest_sha256,
        source_catalog_sha256=inputs.source_catalog_sha256, framework_version=inputs.framework_version,
        version_toml_sha256=inputs.version_toml_sha256, outcome=outcome, reason=reason,
        runner="local-subprocess", command=inputs.command, working_directory=inputs.working_directory,
        exit_code=exit_code, executed_tests=executed_tests, coverage=coverage, evidence_root=evidence_root,
        stdout_sha256=stdout_sha256, stderr_sha256=stderr_sha256, report_sha256=report_sha256,
        executing_selector_sha256=active_n[0], executing_release_package_sha256=active_n[1],
        executing_skill_sha256=active_n[2], receipt_sha256=receipt_sha256, elapsed_seconds=elapsed_seconds,
        control_context_digest=control_context_digest, phase_map_sha256=inputs.phase_map.sha256,
    )


def execute_public_release_suite(
    inputs: PublicFreshGateInputs,
    *,
    docker: DockerExecutor,
) -> PortableSuiteGateEvidence:
    """Execute one fresh immutable-package Unit suite through current N+1."""

    detached = reopen_public_retained_suite_inputs(inputs)
    parent = _safe_path(
        detached.project_root,
        f"{EVIDENCE_ROOT}/{detached.candidate_snapshot_manifest_sha256}",
        create=True,
    )
    executor = installed_public_n_suite_executor(
        detached.candidate_snapshot_manifest_sha256, detached.current_native_n,
        project_root=str(detached.project_root), compiled_root=detached.compiled_root, docker=docker,
    )
    active_n = _native_state(detached)
    attempt = Path(tempfile.mkdtemp(prefix="attempt-", dir=parent))
    relative = attempt.relative_to(detached.project_root).as_posix()
    workspace, output = attempt / "workspace", attempt / "output"
    workspace.mkdir()
    output.mkdir()
    started = time.monotonic()
    outcome, reason, exit_code = "incomplete", "fresh public suite did not complete", None
    tests, coverage = 0, ()
    stdout_sha = stderr_sha = report_sha = receipt_sha = None
    context = deadline = evidence = None
    try:
        context = _public_context(detached, executor)
        _durable_bytes(attempt / "context.json", canonical_json({
            "schema_version": 1, **dict(context.trusted_binding_values),
            "reference_rows": [row.as_dict() for row in context.reference_rows],
            "control_context_digest": context.control_context_digest,
        }))
        deadline = resolve_unit_deadline(context)
        _write_unit_deadline(attempt / "unit-deadline.json", deadline)
        bindings_sha = _materialize_suite_workspace(
            detached.package_root, workspace, detached.candidate_snapshot_manifest_sha256,
            detached.source_rows, detached.source_rows, detached.compiled_root,
            detached.phase_map, detached.working_directory, context,
        )
        environment = _suite_process_environment(
            SANDBOX_WORKSPACE_PATH, SANDBOX_OUTPUT_PATH / "coverage.xml", detached.compiled_root,
            detached.candidate_snapshot_manifest_sha256, source_bindings_sha256=bindings_sha,
            executable_path=executor.image_path,
        )
        result = executor.run(
            detached.command, workspace=workspace, output_root=output,
            working_directory=detached.working_directory, environment=environment,
            timeout_seconds=deadline.timeout_seconds,
        )
        if not isinstance(result, SuiteExecutionResult):
            raise TypeError("public suite executor returned an untyped result")
        exit_code = result.exit_code
        _write_capture(attempt / "stdout.bin", result.stdout)
        _write_capture(attempt / "stderr.bin", result.stderr)
        if result.timed_out:
            outcome, reason = "timed_out", "fresh public suite command timed out"
        elif result.left_descendants:
            outcome, reason = "incomplete", "fresh public suite left running descendant processes"
        elif exit_code:
            outcome, reason = "failed", "fresh public suite command failed"
        else:
            outcome, reason = "incomplete", "fresh public suite coverage evidence is incomplete"
        _copy_report_from_output(output, attempt / "coverage.xml")
        stdout_sha = hashlib.sha256((attempt / "stdout.bin").read_bytes()).hexdigest()
        stderr_sha = hashlib.sha256((attempt / "stderr.bin").read_bytes()).hexdigest()
        report = attempt / "coverage.xml"
        if report.is_file() and not report.is_symlink():
            report_sha = hashlib.sha256(report.read_bytes()).hexdigest()
            tests, coverage, coverage_reason = _observe_report(
                report, detached.package_root, detached.candidate_snapshot_manifest_sha256,
                detached.source_rows, detached.compiled_root, detached.phase_map, context,
            )
            if exit_code == 0 and not coverage_reason:
                outcome, reason = "passed", "complete fresh public bound suite execution"
            elif exit_code == 0:
                outcome, reason = "incomplete", coverage_reason
        refreshed = reopen_public_retained_suite_inputs(inputs)
        if refreshed != detached:
            raise _error("public-suite-input-stale", "public inputs changed during fresh Unit execution")
        refreshed_context = _public_context(refreshed, executor)
        revalidate_context(detached.project_root, context, dict(refreshed_context.trusted_binding_values))
        _verify_unit_deadline(attempt / "unit-deadline.json", deadline)
        if _native_state(refreshed) != active_n:
            raise _error("public-suite-current-n-stale", "current selected N+1 changed during fresh Unit execution")
        evidence = _evidence(
            detached, outcome=outcome, reason=reason, exit_code=exit_code, executed_tests=tests,
            coverage=coverage, evidence_root=relative, stdout_sha256=stdout_sha,
            stderr_sha256=stderr_sha, report_sha256=report_sha, active_n=active_n,
            receipt_sha256=None, elapsed_seconds=time.monotonic() - started,
            control_context_digest=context.control_context_digest,
        )
        payload = canonical_json(asdict(evidence))
        _durable_bytes(attempt / "receipt.json", payload)
        descriptor = os.open(attempt, os.O_RDONLY)
        try:
            os.fsync(descriptor)
        finally:
            os.close(descriptor)
        receipt_sha = hashlib.sha256(payload).hexdigest()
    except (OSError, ValueError, TypeError, ReleaseContractError) as error:
        outcome = "recording_uncertain" if evidence is None else "stale"
        reason = f"fresh public suite could not complete: {getattr(error, 'code', type(error).__name__)}"
    if evidence is not None:
        return replace(evidence, outcome=outcome, reason=reason, receipt_sha256=receipt_sha)
    return _evidence(
        detached, outcome=outcome, reason=reason, exit_code=exit_code, executed_tests=tests,
        coverage=coverage, evidence_root=relative, stdout_sha256=stdout_sha, stderr_sha256=stderr_sha,
        report_sha256=report_sha, active_n=active_n, receipt_sha256=receipt_sha,
        elapsed_seconds=time.monotonic() - started,
        control_context_digest=getattr(context, "control_context_digest", None),
    )


__all__ = [
    "DetachedPublicSuiteInputs",
    "PublicSuiteInputError",
    "execute_public_release_suite",
    "reopen_public_retained_suite_inputs",
]
