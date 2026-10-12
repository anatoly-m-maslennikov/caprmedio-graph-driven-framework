"""D597 detached native Full Gate packet reader coverage."""

from __future__ import annotations

from dataclasses import asdict, replace
import hashlib
import shutil
import sys
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch


RELEASE_ROOT = Path(__file__).resolve().parents[1]
TEST_ROOT = Path(__file__).resolve().parent
for path in (RELEASE_ROOT, TEST_ROOT):
    if str(path) not in sys.path:
        sys.path.insert(0, str(path))

from release_contract import ReleaseContractError, ValidatedCandidate, canonical_json  # noqa: E402
import release_full_gate  # noqa: E402
import release_promotion  # noqa: E402
from release_full_gate import verify_detached_native_full_gate_evidence  # noqa: E402
from release_retained_candidate import read_retained_candidate_identity  # noqa: E402
import test_portable_release_full_gate as packet_fixtures  # noqa: E402


class DetachedNativeFullGateTests(unittest.TestCase):
    def _packet(self, fixture: packet_fixtures._NativeHappyPathFixture | None = None):
        fixture = packet_fixtures._NativeHappyPathFixture() if fixture is None else fixture
        helper = packet_fixtures.PortableReleaseFullGateBoundaryTests()
        with packet_fixtures._fixture_authority(fixture._fixture_authority_pin):
            suite, build, verification, e2e, full, identity = helper._run_mock_native_retained_happy_path(fixture)
        archive = Path(tempfile.mkdtemp(prefix="caprmedio-detached-full-gate-")).resolve(strict=True) / "artifact-root"
        shutil.copytree(fixture.root, archive)
        descriptor = archive / identity.descriptor_path.relative_to(fixture.root)
        sidecar = archive / identity.package_evidence.receipt_path.relative_to(fixture.root)
        package = archive / identity.package_evidence.view.package_root.relative_to(fixture.root)
        relocated = read_retained_candidate_identity(
            descriptor,
            expected_sha256=identity.descriptor_sha256,
            package_root=package,
            sidecar_path=sidecar,
            expected_sidecar_sha256=identity.package_evidence.receipt_sha256,
        )
        return archive, relocated, suite, build, verification, e2e, full

    @staticmethod
    def _scrub_predecessor_n(archive: Path, executing_release: str) -> None:
        predecessor = archive / ".caprmedio_runtime/framework/releases" / executing_release
        if not predecessor.is_dir():
            raise AssertionError("fixture has no predecessor N package")
        # The copied package preserves its sealed file modes.  Scrub every
        # predecessor byte from this disposable archive.  Some macOS test
        # filesystems retain empty provenance-marked directories, but those
        # empty directories cannot serve as a retained N package or backup.
        for path in sorted((predecessor, *predecessor.rglob("*")), key=lambda item: len(item.parts)):
            path.chmod(0o700 if path.is_dir() else 0o600)
        for path in sorted(predecessor.rglob("*"), key=lambda item: len(item.parts), reverse=True):
            if path.is_file():
                path.unlink()
        if any(path.is_file() for path in predecessor.rglob("*")):
            raise AssertionError("predecessor N bytes remained in the archive")

    def test_reopens_relocated_packet_after_checkout_source_drift(self) -> None:
        archive, identity, suite, build, verification, e2e, full = self._packet()

        package = verify_detached_native_full_gate_evidence(
            archive, identity, suite, build, verification, e2e, full,
        )

        self.assertEqual(full.package_manifest_sha256, package.view.actual_package_manifest_sha256)

    def test_reopens_historical_packet_after_predecessor_n_is_removed(self) -> None:
        archive, identity, suite, build, verification, e2e, full = self._packet()
        self._scrub_predecessor_n(archive, identity.descriptor.executing_release)

        package = verify_detached_native_full_gate_evidence(
            archive, identity, suite, build, verification, e2e, full,
        )

        self.assertEqual(full.package_manifest_sha256, package.view.actual_package_manifest_sha256)

    def test_promotion_recovery_reopens_historical_packet_after_predecessor_n_is_removed(self) -> None:
        fixture = packet_fixtures._NativeHappyPathFixture()
        archive, identity, suite, build, verification, e2e, full = self._packet(fixture)
        self._scrub_predecessor_n(archive, identity.descriptor.executing_release)
        candidate = ValidatedCandidate(
            str(archive), fixture.candidate.manifest, fixture.candidate.authority, fixture.candidate.intent,
        )
        prepared = SimpleNamespace(private_package_root=identity.package_evidence.view.package_root)

        packet = release_promotion._reopen_historical_native_promotion_packet(
            candidate, suite, build, verification, e2e, full, prepared,
        )

        self.assertEqual(full.receipt_sha256, packet.evidence.receipt_sha256)
        self.assertEqual(identity, packet.retained_candidate)

    def test_refuses_tampered_aggregate_and_malformed_typed_evidence(self) -> None:
        archive, identity, suite, build, verification, e2e, full = self._packet()
        receipt = archive / full.evidence_root / "receipt.json"
        receipt.write_bytes(canonical_json(asdict(replace(full, receipt_sha256=None, reason="tampered"))))

        with self.assertRaises(ReleaseContractError) as changed:
            verify_detached_native_full_gate_evidence(
                archive, identity, suite, build, verification, e2e, full,
            )
        self.assertEqual("release-full-gate-evidence-untrusted", changed.exception.code)

        with self.assertRaises(ReleaseContractError) as malformed:
            verify_detached_native_full_gate_evidence(
                archive, identity, suite, build, verification, e2e, object(),  # type: ignore[arg-type]
            )
        self.assertEqual("release-full-gate-evidence-untrusted", malformed.exception.code)

    def test_refuses_a_canonical_aggregate_with_another_version_binding(self) -> None:
        archive, identity, suite, build, verification, e2e, full = self._packet()
        forged = replace(full, framework_version="9.9.9")
        receipt = archive / full.evidence_root / "receipt.json"
        payload = canonical_json(asdict(replace(forged, receipt_sha256=None)))
        receipt.write_bytes(payload)
        forged = replace(forged, receipt_sha256=hashlib.sha256(payload).hexdigest())

        with self.assertRaises(ReleaseContractError) as raised:
            verify_detached_native_full_gate_evidence(
                archive, identity, suite, build, verification, e2e, forged,
            )
        self.assertEqual("release-full-gate-retained-package-mismatch", raised.exception.code)

    def test_refuses_foreign_typed_identity_before_physical_reopen(self) -> None:
        archive, identity, suite, build, verification, e2e, full = self._packet()
        foreign = replace(identity, descriptor_path=Path("/private/foreign/candidate-snapshot.json"))

        with patch.object(release_full_gate, "reopen_retained_candidate_identity", side_effect=AssertionError("must not reopen")) as reopen:
            with self.assertRaises(ReleaseContractError) as raised:
                verify_detached_native_full_gate_evidence(
                    archive, foreign, suite, build, verification, e2e, full,
                )

        self.assertEqual("release-full-gate-detached-candidate-untrusted", raised.exception.code)
        reopen.assert_not_called()


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
