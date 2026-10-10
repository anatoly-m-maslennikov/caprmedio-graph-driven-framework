"""Focused public fresh-E2E boundary tests.

The production adapter accepts only the typed HostE2EExecutor capability. The
positive case replaces that object's subprocess method so it can prove the
sealed four-command shape without starting Docker during this unit suite.
"""
from __future__ import annotations

from dataclasses import asdict, replace
import hashlib
import inspect
import sys
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch


RELEASE_ROOT = Path(__file__).resolve().parents[1]
for _path in (RELEASE_ROOT, RELEASE_ROOT.parent):
    if str(_path) not in sys.path:
        sys.path.insert(0, str(_path))

import release_public_e2e as public_e2e  # noqa: E402
from release_contract import canonical_json  # noqa: E402
from release_e2e_gate import (E2EExecutionResult, ExecutableIdentity, FrozenHostE2ECapability,
                              PortableCandidateE2EGateEvidence, ReleaseE2ELimits)  # noqa: E402
from release_public_gate import PublicFreshGateInputs  # noqa: E402
from release_suite import PortableSuiteGateEvidence  # noqa: E402


_DIGEST = "a" * 64
_IMAGE = "sha256:" + "b" * 64
_SOURCES = (
    "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/WORKFLOW_ORCHESTRATOR/tests/test_docker_e2e.py",
    "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/WORKFLOW_ORCHESTRATOR/tests/test_selected_workflows_docker_e2e.py",
    "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/WORKFLOW_ORCHESTRATOR/tests/test_selected_query_mcp_e2e.py",
)


def _suite(*, receipt: str = "c" * 64) -> PortableSuiteGateEvidence:
    return PortableSuiteGateEvidence(
        input_schema="portable-1", candidate_snapshot_manifest_sha256=_DIGEST,
        candidate_run_id="run-1", input_manifest_sha256="d" * 64,
        source_catalog_sha256="e" * 64, framework_version="1.2.3", version_toml_sha256="f" * 64,
        outcome="passed", reason="fresh", runner="sandbox", command=("uv", "run"),
        working_directory=".", exit_code=0, executed_tests=1, coverage=("module",),
        evidence_root=f".caprmedio_runtime/release_suite/{_DIGEST}/attempt-1",
        stdout_sha256="1" * 64, stderr_sha256="2" * 64, report_sha256="3" * 64,
        executing_selector_sha256="4" * 64, executing_release_package_sha256="5" * 64,
        executing_skill_sha256="6" * 64, receipt_sha256=receipt, elapsed_seconds=0.1,
        control_context_digest="7" * 64, phase_map_sha256="8" * 64,
    )


def _view():
    phase = SimpleNamespace(
        sha256="8" * 64,
        candidate_e2e_paths=tuple(sorted(_SOURCES)),
        rows=tuple((path, hashlib.sha256(path.encode()).hexdigest(), "candidate_e2e") for path in sorted(_SOURCES)),
    )
    return SimpleNamespace(
        candidate_snapshot_manifest_sha256=_DIGEST,
        candidate_run_id="run-1", input_manifest_sha256="d" * 64,
        source_catalog_sha256="e" * 64, framework_version="1.2.3", version_toml_sha256="f" * 64,
        actual_package_manifest_sha256="9" * 64, phase_map=phase,
    )


def _inputs(root: Path, *, old_suite: object | None = None, old_e2e: object | None = None) -> PublicFreshGateInputs:
    suite = old_suite if old_suite is not None else _suite(receipt="0" * 64)
    old_e2e = old_e2e if old_e2e is not None else SimpleNamespace(
        receipt_sha256="b" * 64, grammar_sha256="c" * 64,
        settings_snapshot_path="old/settings.json", evidence_root="old/e2e",
    )
    packet = SimpleNamespace(suite=suite, e2e=old_e2e)
    return PublicFreshGateInputs(
        project_root=root, session=SimpleNamespace(), phase="initial", action_run_id="action",
        action_definition_id="CA-O-194", source=SimpleNamespace(), public_document_closure_sha256="d" * 64,
        original_packet=packet, retained_package=SimpleNamespace(view=_view(), receipt_sha256="e" * 64, receipt_path=root / "sidecar.json"),
        current_native_n=SimpleNamespace(selected=SimpleNamespace(image_digest="b" * 64)),
        fresh_attempt_root=root / ".caprmedio_tmp" / "public_release_full_gate" / "action",
    )


def _evidence(*, receipt: str) -> PortableCandidateE2EGateEvidence:
    return PortableCandidateE2EGateEvidence(
        candidate_snapshot_manifest_sha256=_DIGEST, candidate_image_digest=_IMAGE,
        phase_map_sha256="8" * 64, grammar_sha256="c" * 64, outcome="passed", reason="fresh",
        harness_receipts=(), evidence_root=".caprmedio_tmp/public_release_full_gate/action/e2e/attempt-1",
        receipt_sha256=receipt, settings_snapshot_path=None, settings_snapshot_sha256=None,
        host_capability_path=None, host_capability_sha256=None, execution_kind="host-subprocess",
        package_schema="portable-1", package_manifest_sha256="9" * 64,
        package_evidence_sha256="e" * 64, package_evidence_relpath="sidecar.json",
        source_catalog_sha256="e" * 64, candidate_run_id="run-1", input_manifest_sha256="d" * 64,
        framework_version="1.2.3", version_toml_sha256="f" * 64,
    )


def _capability() -> FrozenHostE2ECapability:
    return FrozenHostE2ECapability(
        "4" * 64, "5" * 64, "6" * 64,
        ExecutableIdentity("n_host_controller", "/trusted/n-driver", "1" * 64),
        ExecutableIdentity("python", sys.executable, "2" * 64),
        ExecutableIdentity("driver", "/trusted/n-driver", "1" * 64),
        ExecutableIdentity("docker", "/trusted/docker", "3" * 64), "/trusted",
    )


def _materialize_fresh_suite(root: Path, inputs: PublicFreshGateInputs) -> PortableSuiteGateEvidence:
    suite = _suite(receipt="0" * 64)
    unit_root = root / suite.evidence_root
    unit_root.mkdir(parents=True)
    stdout, stderr = b"fresh unit stdout", b"fresh unit stderr"
    coverage = b"<coverage/>"
    suite = replace(
        suite,
        stdout_sha256=hashlib.sha256(stdout).hexdigest(),
        stderr_sha256=hashlib.sha256(stderr).hexdigest(),
        report_sha256=hashlib.sha256(coverage).hexdigest(),
        receipt_sha256=None,
    )
    receipt = canonical_json(asdict(suite))
    suite = replace(suite, receipt_sha256=hashlib.sha256(receipt).hexdigest())
    (unit_root / "stdout.bin").write_bytes(stdout)
    (unit_root / "stderr.bin").write_bytes(stderr)
    (unit_root / "coverage.xml").write_bytes(coverage)
    (unit_root / "receipt.json").write_bytes(receipt)
    action = inputs.fresh_attempt_root
    action.mkdir(parents=True)
    phase = {
        "schema": "caprmedio.public_unit_phase_binding.v1",
        "action_run_id": inputs.action_run_id,
        "phase": inputs.phase,
        "public_document_closure_sha256": inputs.public_document_closure_sha256,
        "suite_evidence_root": suite.evidence_root,
        "suite_receipt_sha256": suite.receipt_sha256,
    }
    (action / "unit-phase.json").write_bytes(canonical_json(phase))
    return suite


class PublicFreshE2ETests(unittest.TestCase):
    def test_public_api_accepts_no_executor_or_pass_argument(self) -> None:
        self.assertEqual(
            ("inputs", "suite", "executor"), tuple(inspect.signature(public_e2e.run_public_candidate_e2e_gate).parameters),
        )
        self.assertEqual(
            ("inputs", "fresh_suite", "fresh_e2e"), tuple(inspect.signature(public_e2e.read_public_candidate_e2e_execution_artifacts).parameters),
        )

    def test_producer_refuses_an_untyped_executor_before_input_reopen(self) -> None:
        with tempfile.TemporaryDirectory(dir="/private/tmp", ignore_cleanup_errors=True) as temporary:
            root = Path(temporary).resolve()
            with self.assertRaises(public_e2e.PublicFreshE2EError) as caught:
                public_e2e.run_public_candidate_e2e_gate(_inputs(root), _suite(), executor=object())
        self.assertEqual("public-fresh-e2e-executor-untrusted", caught.exception.code)

    def test_original_unit_receipt_is_refused_before_any_path_read(self) -> None:
        with tempfile.TemporaryDirectory(dir="/private/tmp", ignore_cleanup_errors=True) as temporary:
            root = Path(temporary).resolve()
            stale = _suite(receipt="0" * 64)
            with self.assertRaises(public_e2e.PublicFreshE2EError) as caught:
                public_e2e._read_fresh_suite(root, _inputs(root, old_suite=stale), stale)
        self.assertEqual("public-fresh-e2e-suite-stale", caught.exception.code)

    def test_nonzero_or_missing_fresh_unit_exit_is_refused_before_path_read(self) -> None:
        with tempfile.TemporaryDirectory(dir="/private/tmp", ignore_cleanup_errors=True) as temporary:
            root = Path(temporary).resolve()
            inputs = _inputs(root)
            for exit_code in (None, 1):
                with self.subTest(exit_code=exit_code):
                    forged = replace(_suite(receipt="c" * 64), exit_code=exit_code)
                    with self.assertRaises(public_e2e.PublicFreshE2EError) as caught:
                        public_e2e._read_fresh_suite(root, inputs, forged)
                    self.assertEqual("public-fresh-e2e-suite-untrusted", caught.exception.code)

    def test_canonical_unit_and_matching_action_phase_edge_are_required(self) -> None:
        with tempfile.TemporaryDirectory(dir="/private/tmp", ignore_cleanup_errors=True) as temporary:
            root = Path(temporary).resolve()
            inputs = _inputs(root)
            suite = _materialize_fresh_suite(root, inputs)
            capability = _capability()
            with (
                patch.object(public_e2e, "_current_binding", return_value=inputs.current_native_n),
                patch.object(public_e2e, "_freeze_current_capability", return_value=capability),
            ):
                self.assertEqual(suite, public_e2e._read_fresh_suite(root, inputs, suite))
                phase_path = inputs.fresh_attempt_root / "unit-phase.json"
                for label, changed in (
                    ("closure", {"public_document_closure_sha256": "f" * 64}),
                    ("falsely same phase", {"suite_receipt_sha256": inputs.original_packet.suite.receipt_sha256}),
                ):
                    with self.subTest(binding=label):
                        payload = {
                            "schema": "caprmedio.public_unit_phase_binding.v1",
                            "action_run_id": inputs.action_run_id,
                            "phase": inputs.phase,
                            "public_document_closure_sha256": inputs.public_document_closure_sha256,
                            "suite_evidence_root": suite.evidence_root,
                            "suite_receipt_sha256": suite.receipt_sha256,
                            **changed,
                        }
                        phase_path.write_bytes(canonical_json(payload))
                        with self.assertRaises(public_e2e.PublicFreshE2EError) as caught:
                            public_e2e._read_fresh_suite(root, inputs, suite)
                        self.assertEqual("public-fresh-e2e-phase-binding-mismatch", caught.exception.code)

    def test_original_e2e_receipt_is_refused_before_image_or_host_reopen(self) -> None:
        with tempfile.TemporaryDirectory(dir="/private/tmp", ignore_cleanup_errors=True) as temporary:
            root = Path(temporary).resolve()
            stale = _evidence(receipt="b" * 64)
            with self.assertRaises(public_e2e.PublicFreshE2EError) as caught:
                public_e2e._read_fresh_e2e(root, _inputs(root, old_e2e=stale), _suite(), stale)
        self.assertEqual("public-fresh-e2e-evidence-stale", caught.exception.code)

    def test_evidence_directories_are_not_misread_as_regular_files(self) -> None:
        with tempfile.TemporaryDirectory(dir="/private/tmp", ignore_cleanup_errors=True) as temporary:
            root = Path(temporary).resolve()
            directory = root / "e2e" / "attempt-1"
            directory.mkdir(parents=True)
            self.assertEqual(directory, public_e2e._directory(root, "e2e/attempt-1", label="fresh E2E"))

    def test_host_producer_runs_exact_inspection_plus_three_fixed_harnesses(self) -> None:
        with tempfile.TemporaryDirectory(dir="/private/tmp", ignore_cleanup_errors=True) as temporary:
            root = Path(temporary).resolve()
            inputs = _inputs(root)
            suite = _suite()
            attempt = root / ".caprmedio_runtime" / "release_e2e" / _DIGEST / "attempt-test"
            attempt.parent.mkdir(parents=True)
            attempt.mkdir()
            capability = FrozenHostE2ECapability(
                "4" * 64, "5" * 64, "6" * 64,
                ExecutableIdentity("n_host_controller", "/trusted/n-driver", "1" * 64),
                ExecutableIdentity("python", sys.executable, "2" * 64),
                ExecutableIdentity("driver", "/trusted/n-driver", "1" * 64),
                ExecutableIdentity("docker", "/trusted/docker", "3" * 64), "/trusted",
            )
            grammar = {
                "harnesses": [
                    {"source_path": path, "argv": ["{trusted_python}", public_e2e._e2e.DRIVER_RELATIVE,
                        "--start-directory", "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/WORKFLOW_ORCHESTRATOR/tests",
                        "--pattern", Path(path).name, "--junit", "{e2e_junit_path}"], "context_optins": {}}
                    for path in _SOURCES
                ],
            }
            calls: list[tuple[str, ...]] = []

            def run(_self, argv, **_kwargs):
                calls.append(tuple(argv))
                if argv[0] == "docker":
                    return E2EExecutionResult(0, (_IMAGE + "\n").encode(), b"")
                junit = Path(argv[-1])
                junit.parent.mkdir(parents=True, exist_ok=True)
                junit.write_bytes(b"<testsuite tests='1' failures='0' errors='0' skipped='0'><testcase/></testsuite>")
                return E2EExecutionResult(0, b"ok", b"")

            with (
                patch.object(public_e2e, "_reopen_inputs", side_effect=lambda value: value),
                patch.object(public_e2e, "_read_fresh_suite", side_effect=lambda *_args: suite),
                patch.object(public_e2e, "_current_binding", return_value=inputs.current_native_n),
                patch.object(public_e2e, "_reopen_original_image", return_value=_IMAGE),
                patch.object(public_e2e, "_fresh_grammar_and_limits", return_value=(grammar, b"grammar", "c" * 64, ReleaseE2ELimits(1, 1, 1, 4096, 4096, 4096))),
                patch.object(public_e2e, "_freeze_current_capability", return_value=capability),
                patch.object(public_e2e, "_attempt", return_value=(attempt, attempt.relative_to(root).as_posix())),
                patch.object(public_e2e, "_write_configuration", return_value=("settings.json", "d" * 64)),
                patch.object(public_e2e.HostE2EExecutor, "run", new=run),
            ):
                evidence = public_e2e.run_public_candidate_e2e_gate(
                    inputs, suite, executor=public_e2e.HostE2EExecutor(),
                )
            self.assertTrue(evidence.passed)
            self.assertEqual("host-subprocess", evidence.execution_kind)
            self.assertEqual(4, len(calls))
            self.assertEqual(3, len(evidence.harness_receipts))
            self.assertNotEqual(inputs.original_packet.e2e.receipt_sha256, evidence.receipt_sha256)
            receipt = (attempt / "receipt.json").read_bytes()
            self.assertEqual(hashlib.sha256(receipt).hexdigest(), evidence.receipt_sha256)
            self.assertEqual(canonical_json(asdict(replace(evidence, receipt_sha256=None))), receipt)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
