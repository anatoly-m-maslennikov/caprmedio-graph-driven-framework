"""Public fresh Full Gate aggregation over real retained fixture artifacts.

The native packet and both partition reports are physically reopened.  The
future action/session and public-E2E readers are patched only at their narrow
entrypoints: this fixture deliberately has no live O194/O198 Run or host
Docker execution and therefore is not production E2E proof.
"""

from __future__ import annotations

from dataclasses import asdict, replace
import hashlib
from pathlib import Path
import shutil
import sys
import unittest
from types import SimpleNamespace
from unittest.mock import patch


RELEASE_ROOT = Path(__file__).resolve().parents[1]
TOOLS_ROOT = RELEASE_ROOT.parent
TEST_ROOT = Path(__file__).resolve().parent
for _path in (RELEASE_ROOT, TOOLS_ROOT, TEST_ROOT):
    if str(_path) not in sys.path:
        sys.path.insert(0, str(_path))

from release_contract import ReleaseContractError, canonical_json  # noqa: E402
import release_full_gate  # noqa: E402
from release_full_gate import (  # noqa: E402
    aggregate_public_native_full_gate,
    verify_detached_native_full_gate_evidence,
    verify_public_native_full_gate_evidence,
)
from release_public_gate import PublicFreshGateInputs  # noqa: E402
from retained_full_gate_packet import RetainedNativeFullGatePacket  # noqa: E402
import test_detached_native_full_gate as detached_fixture  # noqa: E402
import test_public_gate_inputs as public_input_fixture  # noqa: E402


def _digest(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def _seal(root: Path, evidence):
    payload = canonical_json(asdict(replace(evidence, receipt_sha256=None)))
    (root / "receipt.json").write_bytes(payload)
    return replace(evidence, receipt_sha256=_digest(payload))


class PublicNativeFullGateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        # Building the sealed native packet is intentionally expensive.  Keep
        # one immutable retained packet and give every test independent fresh
        # action carriers below it.
        cls._base_packet = detached_fixture.DetachedNativeFullGateTests()._packet()
        cls._fixture_counter = 0

    def _fixture(self):
        """Relocate a real D597 packet, then create fresh report carriers."""

        archive, identity, suite, build, verification, e2e, full = self._base_packet
        type(self)._fixture_counter += 1
        ordinal = type(self)._fixture_counter
        packet = RetainedNativeFullGatePacket(archive, identity, suite, build, verification, e2e, full)
        action_root = archive / ".caprmedio_tmp/public_release_full_gate" / f"{'a' * 62}{ordinal:02d}"
        fresh_suite_root = action_root / "suite/attempt-fixture"
        fresh_e2e_root = action_root / "e2e/attempt-fixture"
        shutil.copytree(archive / suite.evidence_root, fresh_suite_root)
        shutil.copytree(archive / e2e.evidence_root, fresh_e2e_root)
        fresh_suite = _seal(
            fresh_suite_root,
            replace(suite, evidence_root=fresh_suite_root.relative_to(archive).as_posix(), receipt_sha256=None),
        )

        old_root = e2e.evidence_root
        new_root = fresh_e2e_root.relative_to(archive).as_posix()

        def moved(path: str | None) -> str | None:
            if path is None:
                return None
            self.assertTrue(path.startswith(old_root + "/"), path)
            return new_root + path.removeprefix(old_root)

        receipts = tuple(
            replace(
                row,
                stdout_path=moved(row.stdout_path),
                stderr_path=moved(row.stderr_path),
                junit_path=moved(row.junit_path),
            )
            for row in e2e.harness_receipts
        )
        fresh_e2e = _seal(
            fresh_e2e_root,
            replace(
                e2e,
                evidence_root=new_root,
                harness_receipts=receipts,
                settings_snapshot_path=moved(e2e.settings_snapshot_path),
                host_capability_path=moved(e2e.host_capability_path),
                receipt_sha256=None,
            ),
        )
        inputs = PublicFreshGateInputs(
            project_root=archive,
            session=SimpleNamespace(),
            phase="initial",
            action_run_id="fixture-action",
            action_definition_id="CA-O-194",
            source=SimpleNamespace(),
            public_document_closure_sha256="b" * 64,
            original_packet=packet,
            retained_package=identity.package_evidence,
            current_native_n=SimpleNamespace(),
            fresh_attempt_root=action_root,
        )
        return archive, inputs, fresh_suite, fresh_e2e

    def _public_readers(self, inputs: PublicFreshGateInputs):
        """Fixture-only seams; neither seam asserts production host E2E."""

        return (
            patch("release_public_gate.reopen_public_fresh_gate_inputs", return_value=inputs),
            patch("release_public_e2e.read_public_candidate_e2e_execution_artifacts", return_value=inputs.project_root),
            patch("release_public_e2e._read_fresh_suite", side_effect=lambda _root, _inputs, suite: suite),
            patch("release_public_e2e._read_fresh_e2e", return_value=None),
            patch("release_full_gate._reopen_recorded_public_fresh_inputs", return_value=(inputs, inputs.project_root)),
        )

    def test_aggregate_keeps_original_build_image_and_fresh_test_receipts(self) -> None:
        archive, inputs, fresh_suite, fresh_e2e = self._fixture()
        public_inputs, fresh_reader, fresh_suite_reader, fresh_e2e_reader, recorded_inputs = self._public_readers(inputs)
        with public_inputs, fresh_reader, fresh_suite_reader, fresh_e2e_reader, recorded_inputs:
            evidence = aggregate_public_native_full_gate(inputs, fresh_suite, fresh_e2e)
            self.assertTrue(evidence.passed, evidence.reason)
            self.assertEqual(
                inputs.retained_package,
                verify_public_native_full_gate_evidence(inputs, fresh_suite, fresh_e2e, evidence),
            )

        packet = inputs.original_packet
        self.assertEqual(fresh_suite.receipt_sha256, evidence.suite_receipt_sha256)
        self.assertEqual(fresh_e2e.receipt_sha256, evidence.e2e_receipt_sha256)
        self.assertEqual(packet.build.receipt_sha256, evidence.build_receipt_sha256)
        self.assertEqual(packet.verification.receipt_sha256, evidence.image_receipt_sha256)
        self.assertNotEqual(packet.suite.receipt_sha256, evidence.suite_receipt_sha256)
        self.assertNotEqual(packet.e2e.receipt_sha256, evidence.e2e_receipt_sha256)

    def test_public_verifier_reopens_the_fresh_report_partition(self) -> None:
        _archive, inputs, fresh_suite, fresh_e2e = self._fixture()
        public_inputs, fresh_reader, fresh_suite_reader, fresh_e2e_reader, recorded_inputs = self._public_readers(inputs)
        with public_inputs, fresh_reader, fresh_suite_reader, fresh_e2e_reader, recorded_inputs:
            evidence = aggregate_public_native_full_gate(inputs, fresh_suite, fresh_e2e)
            report = inputs.project_root / fresh_suite.evidence_root / "coverage.xml"
            report.write_bytes(report.read_bytes().replace(b"testcase", b"broken-case", 1))
            with self.assertRaises(ReleaseContractError) as raised:
                verify_public_native_full_gate_evidence(inputs, fresh_suite, fresh_e2e, evidence)
        self.assertEqual("release-full-gate-report-invalid", raised.exception.code)

    def test_ordinary_detached_native_reader_refuses_the_mixed_public_lineage(self) -> None:
        archive, inputs, fresh_suite, fresh_e2e = self._fixture()
        public_inputs, fresh_reader, fresh_suite_reader, fresh_e2e_reader, recorded_inputs = self._public_readers(inputs)
        with public_inputs, fresh_reader, fresh_suite_reader, fresh_e2e_reader, recorded_inputs:
            evidence = aggregate_public_native_full_gate(inputs, fresh_suite, fresh_e2e)

        packet = inputs.original_packet
        with self.assertRaises(ReleaseContractError):
            verify_detached_native_full_gate_evidence(
                archive,
                packet.retained_candidate,
                fresh_suite,
                packet.build,
                packet.verification,
                fresh_e2e,
                evidence,
            )

    def test_original_e2e_cannot_substitute_for_the_public_fresh_receipt(self) -> None:
        _archive, inputs, fresh_suite, _fresh_e2e = self._fixture()
        public_inputs, fresh_reader, fresh_suite_reader, fresh_e2e_reader, recorded_inputs = self._public_readers(inputs)
        with public_inputs, fresh_reader, fresh_suite_reader, fresh_e2e_reader, recorded_inputs, self.assertRaises(ReleaseContractError) as raised:
            aggregate_public_native_full_gate(inputs, fresh_suite, inputs.original_packet.e2e)
        self.assertEqual("release-full-gate-public-fresh-untrusted", raised.exception.code)

    def test_recorded_input_reader_accepts_active_and_completed_o194(self) -> None:
        """Verification accepts either the exact live Action or its result."""

        fixture = public_input_fixture.PublicFreshGateInputTests("test_reopens_initial_inputs_without_claiming_a_gate_result")
        fixture.setUp()
        try:
            patches, current = fixture._reopen()
            with patches as patched:
                patched["verify_detached_native_full_gate_evidence"].return_value = fixture.retained
                patched["bind_selected_native_n_from_checkpoint"].return_value = current
                patched["reopen_native_installed_n"].return_value = current
                import release_public_gate

                inputs = release_public_gate.reopen_public_fresh_gate_inputs(
                    fixture.root, fixture.session, fixture.packet, fixture.source,
                )
                active, active_root = release_full_gate._reopen_recorded_public_fresh_inputs(inputs)
                fixture.session.finish_run(
                    inputs.action_run_id, outcome="completed", result_ref="results/public-phase.json", effect_refs=[],
                )
                observed, root = release_full_gate._reopen_recorded_public_fresh_inputs(inputs)
            self.assertEqual(inputs, active)
            self.assertEqual(fixture.root, active_root)
            self.assertEqual(inputs, observed)
            self.assertEqual(fixture.root, root)
        finally:
            fixture.tearDown()

    def test_recorded_input_reader_uses_only_current_o198_when_o194_is_completed(self) -> None:
        """The completed prior phase must not obscure active history-link work."""

        fixture = public_input_fixture.PublicFreshGateInputTests("test_derives_history_link_phase_from_active_o198_action")
        fixture.setUp()
        try:
            fixture.source = fixture._source(pr_number=42)
            fixture.session = fixture._session("CA-O-198")
            patches, current = fixture._reopen()
            with patches as patched:
                patched["verify_detached_native_full_gate_evidence"].return_value = fixture.retained
                patched["bind_selected_native_n_from_checkpoint"].return_value = current
                patched["reopen_native_installed_n"].return_value = current
                import release_public_gate

                inputs = release_public_gate.reopen_public_fresh_gate_inputs(
                    fixture.root, fixture.session, fixture.packet, fixture.source,
                )
                observed, root = release_full_gate._reopen_recorded_public_fresh_inputs(inputs)
            self.assertEqual("history_link", observed.phase)
            self.assertEqual("CA-O-198", observed.action_definition_id)
            self.assertEqual(fixture.root, root)
        finally:
            fixture.tearDown()


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
