"""Public-release consumption of one original detached native Full Gate packet.

The shared fixture writes physical synthetic retained artifacts.  It never
executes Docker, a host E2E process, Git, GitHub, promotion, or a public
release; these are packet-reader compatibility and refusal tests only.
"""

from __future__ import annotations

from dataclasses import replace
import shutil
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


TOOLS = Path(__file__).resolve().parents[2]
PUBLIC_RELEASE = TOOLS / "PUBLIC_RELEASE"
RELEASE_VERSION = TOOLS / "RELEASE_VERSION"
RELEASE_TESTS = RELEASE_VERSION / "tests"
for path in (TOOLS, PUBLIC_RELEASE, RELEASE_VERSION, RELEASE_TESTS):
    rendered = str(path)
    if rendered not in sys.path:
        sys.path.insert(0, rendered)

from release_retained_candidate import read_retained_candidate_identity  # noqa: E402
from retained_full_gate_packet import RetainedNativeFullGatePacket  # noqa: E402
from public_release import (  # noqa: E402
    DetachedNativeFullGateBinding,
    GateResult,
    PublicReleaseError,
    SourceProof,
    ToolCallEvidence,
    _full_gate_receipt_ref,
    _gate,
)
import test_detached_native_full_gate as retained_packets  # noqa: E402


class DetachedNativePublicGateTests(unittest.TestCase):
    """Use the RELEASE_VERSION packet fixture once; do not discover its TestCase."""

    @classmethod
    def setUpClass(cls) -> None:
        fixture = retained_packets.DetachedNativeFullGateTests(
            "test_reopens_relocated_packet_after_checkout_source_drift",
        )
        (cls.archive, cls.identity, cls.suite, cls.build, cls.verification,
         cls.e2e, cls.evidence) = fixture._packet()
        cls.packet = RetainedNativeFullGatePacket(
            artifact_root=cls.archive,
            retained_candidate=cls.identity,
            suite=cls.suite,
            build=cls.build,
            verification=cls.verification,
            e2e=cls.e2e,
            evidence=cls.evidence,
        )

    @classmethod
    def source(cls, **changes: object) -> SourceProof:
        values: dict[str, object] = {
            "candidate_snapshot_manifest_sha256": cls.evidence.candidate_snapshot_manifest_sha256,
            "framework_version": cls.evidence.framework_version,
            "version_toml_sha256": cls.evidence.version_toml_sha256,
            "readme_ref": "README.md",
            "readme_sha256": "a" * 64,
            "pr_body_ref": "docs/public-pr.md",
            "pr_body_sha256": "b" * 64,
            "version_history_ref": "VERSION_HISTORY.md",
            "version_history_sha256": "c" * 64,
            "version_history_summary": "Retained native Full Gate packet.",
            "version_history_pr_url": None,
            "version_history_pr_number": None,
        }
        values.update(changes)
        return SourceProof(**values)  # type: ignore[arg-type]

    @staticmethod
    def call() -> ToolCallEvidence:
        return ToolCallEvidence(
            "inputs/detached-native-full-gate.json",
            "results/detached-native-full-gate.json",
            report_refs=("reports/detached-native-full-gate.json",),
        )

    def gate(self, packet: object, source: SourceProof | None = None) -> GateResult:
        result = GateResult(self.call(), DetachedNativeFullGateBinding(packet))  # type: ignore[arg-type]
        return _gate(
            result,
            "detached native Full Gate",
            self.source() if source is None else source,
            project_root=Path("/unavailable-live-candidate-root"),
            selected_version=self.evidence.framework_version,
        )

    def copied_packet(self) -> RetainedNativeFullGatePacket:
        target = Path(tempfile.mkdtemp(prefix="caprmedio-public-detached-gate-")).resolve(strict=True) / "artifact-root"
        shutil.copytree(self.archive, target)
        descriptor = target / self.identity.descriptor_path.relative_to(self.archive)
        sidecar = target / self.identity.package_evidence.receipt_path.relative_to(self.archive)
        package_root = target / self.identity.package_evidence.view.package_root.relative_to(self.archive)
        identity = read_retained_candidate_identity(
            descriptor,
            expected_sha256=self.identity.descriptor_sha256,
            package_root=package_root,
            sidecar_path=sidecar,
            expected_sidecar_sha256=self.identity.package_evidence.receipt_sha256,
        )
        return RetainedNativeFullGatePacket(
            artifact_root=target,
            retained_candidate=identity,
            suite=self.suite,
            build=self.build,
            verification=self.verification,
            e2e=self.e2e,
            evidence=self.evidence,
        )

    def test_reopens_original_packet_after_source_and_selector_drift(self) -> None:
        with (
            patch("release_full_gate.verify_bound_full_gate_evidence", side_effect=AssertionError("legacy reader used")) as legacy,
            patch("release_promotion.verify_bound_promotion_evidence", side_effect=AssertionError("legacy promotion reader used")) as promotion,
        ):
            result = self.gate(self.packet)

        self.assertEqual(self.evidence.receipt_sha256, result.binding.packet.evidence.receipt_sha256)
        self.assertEqual(
            f"{self.evidence.evidence_root}/receipt.json",
            _full_gate_receipt_ref(result.binding),
        )
        legacy.assert_not_called()
        promotion.assert_not_called()

    def test_tampered_original_receipt_is_refused(self) -> None:
        packet = self.copied_packet()
        receipt = packet.artifact_root / packet.evidence.evidence_root / "receipt.json"
        receipt.write_bytes(b"tampered retained Full Gate receipt")

        with self.assertRaisesRegex(PublicReleaseError, "full-gate-unproven"):
            self.gate(packet)

    def test_foreign_retained_identity_is_refused(self) -> None:
        packet = replace(
            self.packet,
            retained_candidate=replace(
                self.identity,
                descriptor_path=Path("/private/foreign/candidate-snapshot.json"),
            ),
        )

        with self.assertRaisesRegex(PublicReleaseError, "full-gate-unproven"):
            self.gate(packet)

    def test_mismatched_source_version_is_refused(self) -> None:
        source = self.source(framework_version="9.9.9")

        with self.assertRaisesRegex(PublicReleaseError, "new-local-cycle-required"):
            self.gate(self.packet, source)

    def test_boolean_packet_is_not_a_pass(self) -> None:
        with self.assertRaisesRegex(PublicReleaseError, "invalid-full-gate"):
            self.gate(True)

    def test_changed_source_closure_requires_its_own_original_packet(self) -> None:
        source = self.source(candidate_snapshot_manifest_sha256="f" * 64)

        with self.assertRaisesRegex(PublicReleaseError, "stale-full-gate"):
            self.gate(self.packet, source)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
