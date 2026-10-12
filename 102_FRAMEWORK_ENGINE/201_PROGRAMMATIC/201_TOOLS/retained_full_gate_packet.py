"""Shared immutable transport for original retained native Full Gate evidence.

The packet itself grants neither a pass nor execution authority. Consumers
must reopen its concrete carriers through the existing Full Gate verifier.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from release_e2e_gate import PortableCandidateE2EGateEvidence
    from release_full_gate import NativeFullGateEvidence
    from release_image import PortableImageBuildEvidence, PortableImageVerificationEvidence
    from release_retained_candidate import RetainedCandidateIdentity
    from release_suite import PortableSuiteGateEvidence


@dataclass(frozen=True)
class RetainedNativeFullGatePacket:
    """Exact retained carriers; verification remains the reader's responsibility."""

    artifact_root: Path
    retained_candidate: RetainedCandidateIdentity
    suite: PortableSuiteGateEvidence
    build: PortableImageBuildEvidence
    verification: PortableImageVerificationEvidence
    e2e: PortableCandidateE2EGateEvidence
    evidence: NativeFullGateEvidence


__all__ = ["RetainedNativeFullGatePacket"]
