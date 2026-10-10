"""Non-authoritative, closed D615 public-document gate-bridge encoding.

Encoding is not evidence of execution. Production consumers must reopen the
physical fresh producer result and its complete native Full Gate first.
"""
from __future__ import annotations

import json
import re
from dataclasses import dataclass, asdict
from typing import Literal

from public_release import PublicReleaseError, SourceProof, _safe_ref, document_closure_digest
from release_full_gate import NativeFullGateEvidence
from release_public_gate import PublicFreshGateInputs
from release_retained_package import RetainedNativePackageEvidence

_SHA = re.compile(r"^[0-9a-f]{64}$")

class DocumentGateBridgeError(ValueError):
    """The bridge's source, native identity, or encoding is invalid."""

@dataclass(frozen=True)
class PublicDocumentClosureGateBridgeV1:
    schema: Literal["caprmedio.public_release.document_closure_gate_bridge.v1"]
    phase: Literal["initial", "history_link"]
    candidate_snapshot_manifest_sha256: str
    framework_version: str
    version_toml_sha256: str
    package_manifest_sha256: str
    full_gate_candidate_run_id: str
    full_gate_evidence_root: str
    full_gate_receipt_sha256: str
    producer_result_ref: str
    public_document_closure_sha256: str

def canonical_bytes(value: PublicDocumentClosureGateBridgeV1) -> bytes:
    if not isinstance(value, PublicDocumentClosureGateBridgeV1):
        raise DocumentGateBridgeError("one closed D615 bridge is required")
    return json.dumps(asdict(value), ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False).encode("utf-8")


def _ref(value: object, name: str) -> str:
    try:
        result = _safe_ref(value, name)
    except PublicReleaseError as error:
        raise DocumentGateBridgeError(str(error)) from error
    if any(character in result for character in "\r\n"):
        raise DocumentGateBridgeError(f"{name} must be a single-line reference")
    return result

def derive_bridge(*, inputs: PublicFreshGateInputs, evidence: NativeFullGateEvidence, producer_result_ref: str) -> PublicDocumentClosureGateBridgeV1:
    """Encode reopened identities; this function grants no execution authority."""
    if (not isinstance(inputs, PublicFreshGateInputs)
            or not isinstance(inputs.source, SourceProof)
            or not isinstance(inputs.retained_package, RetainedNativePackageEvidence)
            or not isinstance(evidence, NativeFullGateEvidence)):
        raise DocumentGateBridgeError("typed public inputs and native gate evidence are required")
    phase = inputs.phase
    source, view = inputs.source, inputs.retained_package.view
    closure = document_closure_digest(source)
    if (phase not in {"initial", "history_link"}
            or source.public_document_closure_sha256 != closure
            or inputs.public_document_closure_sha256 != closure):
        raise DocumentGateBridgeError("reopened source phase or closure is stale")
    expected = {
        "candidate_snapshot_manifest_sha256": source.candidate_snapshot_manifest_sha256,
        "framework_version": source.framework_version,
        "version_toml_sha256": source.version_toml_sha256,
        "package_manifest_sha256": view.actual_package_manifest_sha256,
        "candidate_run_id": view.candidate_run_id,
    }
    if (not evidence.passed or evidence.package_schema != "portable-1"
            or any(getattr(evidence, key) != value for key, value in expected.items())
            or view.candidate_snapshot_manifest_sha256 != source.candidate_snapshot_manifest_sha256
            or view.framework_version != source.framework_version
            or view.version_toml_sha256 != source.version_toml_sha256):
        raise DocumentGateBridgeError("native gate does not bind this source and retained package")
    fields = (evidence.candidate_snapshot_manifest_sha256, evidence.version_toml_sha256, evidence.package_manifest_sha256, evidence.receipt_sha256, closure)
    if any(not isinstance(x, str) or _SHA.fullmatch(x) is None for x in fields):
        raise DocumentGateBridgeError("fresh native gate evidence and locally derived closure are required")
    if not isinstance(evidence.candidate_run_id, str) or not evidence.candidate_run_id:
        raise DocumentGateBridgeError("native gate has no candidate Run identity")
    evidence_root = _ref(evidence.evidence_root, "full_gate_evidence_root")
    result_ref = _ref(producer_result_ref, "producer_result_ref")
    return PublicDocumentClosureGateBridgeV1("caprmedio.public_release.document_closure_gate_bridge.v1", phase, evidence.candidate_snapshot_manifest_sha256, evidence.framework_version, evidence.version_toml_sha256, evidence.package_manifest_sha256, evidence.candidate_run_id, evidence_root, evidence.receipt_sha256, result_ref, closure)
