"""Program-owned fresh public Full Gate: execute Unit, three E2Es, aggregate.

This producer neither builds nor installs an image/package and performs no Git
effect. Original image receipts are immutable provenance, never a fresh test
result. Component failures retain their actual artifacts and stop the cycle.
"""
from __future__ import annotations

import hashlib
import os
import sys
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Literal

_TOOLS = Path(__file__).resolve().parents[1]
for _path in (_TOOLS, _TOOLS / "PUBLIC_RELEASE"):
    if str(_path) not in sys.path:
        sys.path.insert(0, str(_path))

from document_gate_bridge import canonical_bytes as bridge_bytes, derive_bridge
from public_release import _safe_ref
from release_contract import ReleaseContractError, canonical_json
from release_e2e_gate import HostE2EExecutor, PortableCandidateE2EGateEvidence
from release_full_gate import NativeFullGateEvidence
from release_image import DockerExecutor, DockerSubprocessExecutor
from release_public_gate import PublicFreshGateInputs, reopen_public_fresh_gate_inputs
from release_suite import PortableSuiteGateEvidence

SCHEMA = "caprmedio.public_native_full_gate_result.v1"


class PublicNativeFullGateError(ReleaseContractError):
    """Fresh public execution or its immutable recording is unavailable."""


@dataclass(frozen=True)
class PublicNativeFullGateResult:
    inputs: PublicFreshGateInputs
    suite: PortableSuiteGateEvidence | None
    e2e: PortableCandidateE2EGateEvidence | None
    evidence: NativeFullGateEvidence | None
    outcome: Literal["passed", "failed", "interrupted_pending"]
    producer_result_ref: str
    producer_result_sha256: str
    bridge_ref: str | None
    bridge_sha256: str | None
    failure_code: str | None = None

    @property
    def passed(self) -> bool:
        return (self.outcome == "passed" and self.evidence is not None
                and self.evidence.passed and self.bridge_ref is not None
                and self.bridge_sha256 is not None)


def _record(result: PublicNativeFullGateResult) -> bytes:
    """One immutable result record, without any session or source contents."""
    inputs = result.inputs
    return canonical_json({
        "schema": SCHEMA,
        "phase": inputs.phase,
        "action_run_id": inputs.action_run_id,
        "action_definition_id": inputs.action_definition_id,
        "public_document_closure_sha256": inputs.public_document_closure_sha256,
        "original_full_gate_receipt_sha256": inputs.original_packet.evidence.receipt_sha256,
        "outcome": result.outcome,
        "failure_code": result.failure_code,
        "suite": asdict(result.suite) if result.suite is not None else None,
        "e2e": asdict(result.e2e) if result.e2e is not None else None,
        "full_gate": asdict(result.evidence) if result.evidence is not None else None,
    })


def _safe_path(root: Path, relative: str) -> Path:
    _safe_ref(relative, "public producer evidence")
    path = root / relative
    cursor = root
    for part in Path(relative).parts:
        cursor /= part
        if cursor.is_symlink():
            raise PublicNativeFullGateError("public-gate-evidence-unsafe", "evidence has a symlinked ancestor")
    return path


def _write_new(path: Path, payload: bytes) -> None:
    with path.open("xb") as stream:
        stream.write(payload)
        stream.flush()
        os.fsync(stream.fileno())


def run_public_native_full_gate(
    inputs: PublicFreshGateInputs, *, docker: DockerExecutor | None = None,
) -> PublicNativeFullGateResult:
    """Execute the fixed real producers once below an active public Action."""
    # Resolve program-owned implementations before creating an attempt. There
    # is no callback or host-Python fallback when a dependency is unavailable.
    from release_public_suite import execute_public_release_suite
    from release_public_e2e import run_public_candidate_e2e_gate
    from release_full_gate import aggregate_public_native_full_gate

    if not isinstance(inputs, PublicFreshGateInputs):
        raise PublicNativeFullGateError("public-gate-input-invalid", "reopened typed inputs are required")
    reopened = reopen_public_fresh_gate_inputs(
        inputs.project_root, inputs.session, inputs.original_packet, inputs.source,
    )
    if reopened != inputs:
        raise PublicNativeFullGateError("public-gate-input-stale", "fresh public inputs changed before execution")
    root = inputs.project_root
    attempt_ref = inputs.fresh_attempt_root.relative_to(root).as_posix()
    attempt = _safe_path(root, attempt_ref)
    if attempt.exists():
        raise PublicNativeFullGateError("public-gate-attempt-exists", "this Action already has an attempt; do not replay it")
    attempt.parent.mkdir(parents=True, exist_ok=True)
    attempt.mkdir()
    _write_new(attempt / "intent.json", canonical_json({
        "schema": SCHEMA,
        "action_run_id": inputs.action_run_id,
        "phase": inputs.phase,
        "public_document_closure_sha256": inputs.public_document_closure_sha256,
    }))
    suite = e2e = evidence = None
    outcome: Literal["passed", "failed", "interrupted_pending"] = "failed"
    failure_code: str | None = "public-gate-unit-failed"
    try:
        suite = execute_public_release_suite(inputs, docker=docker or DockerSubprocessExecutor())
        if not isinstance(suite, PortableSuiteGateEvidence):
            raise PublicNativeFullGateError("public-gate-unit-invalid", "Unit producer returned untyped evidence")
        if suite.outcome == "recording_uncertain":
            outcome, failure_code = "interrupted_pending", "public-gate-unit-recording-uncertain"
        if suite.passed:
            failure_code = "public-gate-e2e-failed"
            _write_new(attempt / "unit-phase.json", canonical_json({
                "schema": "caprmedio.public_unit_phase_binding.v1",
                "action_run_id": inputs.action_run_id,
                "phase": inputs.phase,
                "public_document_closure_sha256": inputs.public_document_closure_sha256,
                "suite_evidence_root": suite.evidence_root,
                "suite_receipt_sha256": suite.receipt_sha256,
            }))
            e2e = run_public_candidate_e2e_gate(inputs, suite, executor=HostE2EExecutor())
            if not isinstance(e2e, PortableCandidateE2EGateEvidence):
                raise PublicNativeFullGateError("public-gate-e2e-invalid", "E2E producer returned untyped evidence")
            if e2e.outcome == "recording_uncertain":
                outcome, failure_code = "interrupted_pending", "public-gate-e2e-recording-uncertain"
            if e2e.passed:
                failure_code = "public-gate-aggregate-failed"
                evidence = aggregate_public_native_full_gate(inputs, suite, e2e)
                if not isinstance(evidence, NativeFullGateEvidence):
                    raise PublicNativeFullGateError("public-gate-aggregate-invalid", "aggregate returned untyped evidence")
                if evidence.outcome == "recording_uncertain":
                    outcome, failure_code = "interrupted_pending", "public-gate-aggregate-recording-uncertain"
                if evidence.passed:
                    outcome = "passed"
                    failure_code = None
        if reopen_public_fresh_gate_inputs(root, inputs.session, inputs.original_packet, inputs.source) != inputs:
            raise PublicNativeFullGateError("public-gate-input-stale", "public inputs changed during execution")
    except ReleaseContractError as error:
        # A known refusal is not permission to replay any component. Available
        # component receipts remain attached to this failed producer result.
        if outcome != "interrupted_pending":
            outcome = "failed"
            failure_code = getattr(error, "code", "public-gate-refused")
    except Exception as error:
        outcome = "interrupted_pending"
        failure_code = "public-gate-interrupted-" + type(error).__name__

    result_ref = (attempt / "producer-result.json").relative_to(root).as_posix()
    pending = PublicNativeFullGateResult(inputs, suite, e2e, evidence, outcome,
                                        result_ref, "", None, None, failure_code)
    payload = _record(pending)
    try:
        _write_new(attempt / "producer-result.json", payload)
        bridge_ref = bridge_sha = None
        if outcome == "passed":
            bridge = derive_bridge(inputs=inputs, evidence=evidence, producer_result_ref=result_ref)
            encoded = bridge_bytes(bridge)
            bridge_path = attempt / "document-gate-bridge.json"
            _write_new(bridge_path, encoded)
            bridge_ref = bridge_path.relative_to(root).as_posix()
            bridge_sha = hashlib.sha256(encoded).hexdigest()
    except (OSError, ValueError) as error:
        raise PublicNativeFullGateError(
            "public-gate-recording-uncertain", "producer recording is incomplete; preserve its attempt",
        ) from error
    return PublicNativeFullGateResult(inputs, suite, e2e, evidence, outcome,
                                     result_ref, hashlib.sha256(payload).hexdigest(),
                                     bridge_ref, bridge_sha, failure_code)


def verify_public_native_full_gate_result(result: PublicNativeFullGateResult) -> NativeFullGateEvidence:
    """Reopen a completed fresh result; never execute or replay its Action."""
    from release_full_gate import verify_public_native_full_gate_evidence

    if not isinstance(result, PublicNativeFullGateResult) or not result.passed:
        raise PublicNativeFullGateError("public-gate-not-passed", "fresh public gate has no complete pass")
    root, inputs = result.inputs.project_root, result.inputs
    expected_root = inputs.fresh_attempt_root.relative_to(root)
    if result.producer_result_ref != (expected_root / "producer-result.json").as_posix():
        raise PublicNativeFullGateError("public-gate-result-stale", "producer result belongs to another Action")
    path = _safe_path(root, result.producer_result_ref)
    expected = _record(result)
    if (not path.is_file() or path.read_bytes() != expected
            or hashlib.sha256(expected).hexdigest() != result.producer_result_sha256):
        raise PublicNativeFullGateError("public-gate-result-stale", "physical producer result changed")
    verify_public_native_full_gate_evidence(inputs, result.suite, result.e2e, result.evidence)
    bridge = derive_bridge(inputs=inputs, evidence=result.evidence, producer_result_ref=result.producer_result_ref)
    expected_bridge = bridge_bytes(bridge)
    if result.bridge_ref != (expected_root / "document-gate-bridge.json").as_posix():
        raise PublicNativeFullGateError("public-gate-bridge-stale", "bridge belongs to another Action")
    bridge_path = _safe_path(root, result.bridge_ref)
    if (not bridge_path.is_file() or bridge_path.read_bytes() != expected_bridge
            or hashlib.sha256(expected_bridge).hexdigest() != result.bridge_sha256):
        raise PublicNativeFullGateError("public-gate-bridge-stale", "physical document gate bridge changed")
    return result.evidence


__all__ = ["PublicNativeFullGateError", "PublicNativeFullGateResult",
           "run_public_native_full_gate", "verify_public_native_full_gate_result"]
