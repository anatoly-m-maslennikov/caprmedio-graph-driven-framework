"""Local mechanics for the public Full-Gate producer.

The component producers are deliberately mocked here: these tests establish
ordering and immutable-record mechanics, not a Unit, E2E, aggregate, or public
gate pass claim.
"""

from __future__ import annotations

from contextlib import ExitStack
import json
from pathlib import Path
import sys
import tempfile
import unittest
from types import SimpleNamespace
from unittest.mock import patch


RELEASE_ROOT = Path(__file__).resolve().parents[1]
for _path in (RELEASE_ROOT, RELEASE_ROOT.parent):
    if str(_path) not in sys.path:
        sys.path.insert(0, str(_path))

import release_public_producer as producer  # noqa: E402
from release_e2e_gate import PortableCandidateE2EGateEvidence  # noqa: E402
from release_full_gate import NativeFullGateEvidence  # noqa: E402
from release_public_gate import PublicFreshGateInputs  # noqa: E402
from release_suite import PortableSuiteGateEvidence  # noqa: E402


def _suite(*, outcome: str = "passed") -> PortableSuiteGateEvidence:
    return PortableSuiteGateEvidence(
        input_schema="portable-1", candidate_snapshot_manifest_sha256="a" * 64,
        candidate_run_id="candidate-run", input_manifest_sha256="b" * 64,
        source_catalog_sha256="c" * 64, framework_version="0.4.2",
        version_toml_sha256="d" * 64, outcome=outcome, reason="mocked component",
        runner="mock", command=("uv", "run"), working_directory=".",
        exit_code=0 if outcome == "passed" else 1, executed_tests=1,
        coverage=("module",), evidence_root="fresh-suite/attempt-1",
        stdout_sha256="e" * 64, stderr_sha256="f" * 64, report_sha256="0" * 64,
        executing_selector_sha256="1" * 64,
        executing_release_package_sha256="2" * 64,
        executing_skill_sha256="3" * 64, receipt_sha256="4" * 64,
        elapsed_seconds=0.0, control_context_digest="5" * 64,
        phase_map_sha256="6" * 64,
    )


def _e2e(*, outcome: str = "passed") -> PortableCandidateE2EGateEvidence:
    return PortableCandidateE2EGateEvidence(
        candidate_snapshot_manifest_sha256="a" * 64,
        candidate_image_digest="sha256:" + "b" * 64, phase_map_sha256="6" * 64,
        grammar_sha256="7" * 64, outcome=outcome, reason="mocked component",
        harness_receipts=(), evidence_root="fresh-e2e/attempt-1", receipt_sha256="8" * 64,
        settings_snapshot_path=None, settings_snapshot_sha256=None,
        host_capability_path=None, host_capability_sha256=None,
        execution_kind="host-subprocess", package_schema="portable-1",
        package_manifest_sha256="9" * 64, package_evidence_sha256="0" * 64,
        package_evidence_relpath="retained-package.json", source_catalog_sha256="c" * 64,
        candidate_run_id="candidate-run", input_manifest_sha256="b" * 64,
        framework_version="0.4.2", version_toml_sha256="d" * 64,
    )


def _aggregate(*, outcome: str = "passed") -> NativeFullGateEvidence:
    return NativeFullGateEvidence(
        candidate_snapshot_manifest_sha256="a" * 64,
        candidate_image_digest="sha256:" + "b" * 64, phase_map_sha256="6" * 64,
        suite_receipt_sha256="4" * 64, build_receipt_sha256="1" * 64,
        image_receipt_sha256="2" * 64, e2e_receipt_sha256="8" * 64,
        outcome=outcome, reason="mocked component", evidence_root="fresh-full-gate",
        receipt_sha256="3" * 64, executed_tests=2, package_schema="portable-1",
        package_manifest_sha256="9" * 64, package_evidence_sha256="0" * 64,
        package_evidence_relpath="retained-package.json", source_catalog_sha256="c" * 64,
        candidate_run_id="candidate-run", input_manifest_sha256="b" * 64,
        framework_version="0.4.2", version_toml_sha256="d" * 64,
    )


def _inputs(root: Path, action_run_id: str = "public-action") -> PublicFreshGateInputs:
    return PublicFreshGateInputs(
        project_root=root, session=SimpleNamespace(), phase="initial",
        action_run_id=action_run_id, action_definition_id="CA-O-194",
        source=SimpleNamespace(), public_document_closure_sha256="c" * 64,
        original_packet=SimpleNamespace(evidence=SimpleNamespace(receipt_sha256="d" * 64)),
        retained_package=SimpleNamespace(), current_native_n=SimpleNamespace(),
        fresh_attempt_root=root / ".caprmedio_tmp" / "public_release_full_gate" / action_run_id,
    )


class PublicProducerMechanicsTests(unittest.TestCase):
    def _root(self) -> Path:
        # Retained intentionally: fixture cleanup must not mask a refused write.
        return Path(tempfile.mkdtemp(prefix="public-producer-"))

    def _run_patches(self, inputs: PublicFreshGateInputs, *, suite, e2e, aggregate):
        stack = ExitStack()
        stack.enter_context(patch.object(producer, "reopen_public_fresh_gate_inputs", return_value=inputs))
        stack.enter_context(patch("release_public_suite.execute_public_release_suite", side_effect=suite))
        stack.enter_context(patch("release_public_e2e.run_public_candidate_e2e_gate", side_effect=e2e))
        stack.enter_context(patch("release_full_gate.aggregate_public_native_full_gate", side_effect=aggregate))
        stack.enter_context(patch.object(producer, "derive_bridge", return_value=SimpleNamespace()))
        stack.enter_context(patch.object(producer, "bridge_bytes", return_value=b"mock bridge bytes\n"))
        return stack

    def test_failed_unit_stops_e2e_and_aggregate_but_records_unit_result(self) -> None:
        inputs, calls = _inputs(self._root()), []
        suite = _suite(outcome="failed")
        with self._run_patches(
            inputs,
            suite=lambda *_args, **_kwargs: calls.append("unit") or suite,
            e2e=lambda *_args, **_kwargs: self.fail("E2E must not run after failed Unit"),
            aggregate=lambda *_args, **_kwargs: self.fail("aggregate must not run after failed Unit"),
        ):
            result = producer.run_public_native_full_gate(inputs)

        self.assertEqual(["unit"], calls)
        self.assertEqual("failed", result.outcome)
        self.assertIs(result.suite, suite)
        self.assertIsNone(result.e2e)
        self.assertTrue((inputs.project_root / result.producer_result_ref).is_file())
        self.assertEqual(producer._record(result), (inputs.project_root / result.producer_result_ref).read_bytes())

    def test_failed_e2e_stops_aggregate(self) -> None:
        inputs, calls = _inputs(self._root()), []
        suite, e2e = _suite(), _e2e(outcome="failed")
        with self._run_patches(
            inputs,
            suite=lambda *_args, **_kwargs: calls.append("unit") or suite,
            e2e=lambda *_args, **_kwargs: calls.append("e2e") or e2e,
            aggregate=lambda *_args, **_kwargs: self.fail("aggregate must not run after failed E2E"),
        ):
            result = producer.run_public_native_full_gate(inputs)

        self.assertEqual(["unit", "e2e"], calls)
        self.assertEqual("failed", result.outcome)
        self.assertIs(result.e2e, e2e)
        self.assertIsNone(result.evidence)

    def test_returned_recording_uncertainty_is_not_an_ordinary_failure(self) -> None:
        for phase in ("unit", "e2e", "aggregate"):
            with self.subTest(phase=phase):
                inputs, calls = _inputs(self._root()), []
                suite = _suite(outcome="recording_uncertain" if phase == "unit" else "passed")
                e2e = _e2e(outcome="recording_uncertain" if phase == "e2e" else "passed")
                aggregate = _aggregate(outcome="recording_uncertain")
                with self._run_patches(
                    inputs,
                    suite=lambda *_args, **_kwargs: calls.append("unit") or suite,
                    e2e=lambda *_args, **_kwargs: calls.append("e2e") or e2e,
                    aggregate=lambda *_args, **_kwargs: calls.append("aggregate") or aggregate,
                ):
                    result = producer.run_public_native_full_gate(inputs)
                self.assertEqual(["unit", "e2e", "aggregate"][:("unit", "e2e", "aggregate").index(phase) + 1], calls)
                self.assertEqual("interrupted_pending", result.outcome)
                self.assertEqual(f"public-gate-{phase}-recording-uncertain", result.failure_code)
                self.assertFalse(result.passed)
                self.assertIsNone(result.bridge_ref)
                self.assertEqual(producer._record(result), (inputs.project_root / result.producer_result_ref).read_bytes())

    def test_success_records_six_field_unit_phase_before_e2e(self) -> None:
        inputs, calls = _inputs(self._root()), []
        suite, e2e, evidence = _suite(), _e2e(), _aggregate()

        def produce_e2e(*args, **_kwargs):
            self.assertIs(suite, args[1])
            phase_path = inputs.fresh_attempt_root / "unit-phase.json"
            self.assertTrue(phase_path.is_file())
            self.assertEqual({
                "schema": "caprmedio.public_unit_phase_binding.v1",
                "action_run_id": inputs.action_run_id,
                "phase": inputs.phase,
                "public_document_closure_sha256": inputs.public_document_closure_sha256,
                "suite_evidence_root": suite.evidence_root,
                "suite_receipt_sha256": suite.receipt_sha256,
            }, json.loads(phase_path.read_text(encoding="utf-8")))
            calls.append("e2e")
            return e2e

        def aggregate_unit_and_e2e(*args, **_kwargs):
            self.assertIs(suite, args[1])
            self.assertIs(e2e, args[2])
            calls.append("aggregate")
            return evidence

        with self._run_patches(
            inputs,
            suite=lambda *_args, **_kwargs: calls.append("unit") or suite,
            e2e=produce_e2e,
            aggregate=aggregate_unit_and_e2e,
        ):
            result = producer.run_public_native_full_gate(inputs)

        self.assertEqual(["unit", "e2e", "aggregate"], calls)
        self.assertTrue(result.passed)
        self.assertEqual(evidence, result.evidence)

    def test_duplicate_attempt_refuses_without_component_replay(self) -> None:
        inputs, calls = _inputs(self._root()), []
        suite = _suite(outcome="failed")
        with self._run_patches(
            inputs,
            suite=lambda *_args, **_kwargs: calls.append("unit") or suite,
            e2e=lambda *_args, **_kwargs: self.fail("E2E must not run"),
            aggregate=lambda *_args, **_kwargs: self.fail("aggregate must not run"),
        ):
            producer.run_public_native_full_gate(inputs)
            with self.assertRaises(producer.PublicNativeFullGateError) as raised:
                producer.run_public_native_full_gate(inputs)

        self.assertEqual("public-gate-attempt-exists", raised.exception.code)
        self.assertEqual(["unit"], calls)

    def test_verifier_refuses_mutated_result_or_bridge_bytes(self) -> None:
        for name, filename in (("producer", "producer-result.json"), ("bridge", "document-gate-bridge.json")):
            with self.subTest(name=name):
                inputs = _inputs(self._root(), action_run_id=f"public-{name}")
                suite, e2e, evidence = _suite(), _e2e(), _aggregate()
                with self._run_patches(
                    inputs,
                    suite=lambda *_args, **_kwargs: suite,
                    e2e=lambda *_args, **_kwargs: e2e,
                    aggregate=lambda *_args, **_kwargs: evidence,
                ), patch("release_full_gate.verify_public_native_full_gate_evidence", return_value=None):
                    result = producer.run_public_native_full_gate(inputs)
                    (inputs.fresh_attempt_root / filename).write_bytes(b"tampered\n")
                    with self.assertRaises(producer.PublicNativeFullGateError) as raised:
                        producer.verify_public_native_full_gate_result(result)
                self.assertEqual(
                    "public-gate-result-stale" if name == "producer" else "public-gate-bridge-stale",
                    raised.exception.code,
                )


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
