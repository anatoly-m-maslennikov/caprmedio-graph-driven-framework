"""Synthetic O164@9 portable-frontier action/checkpoint coverage."""

from __future__ import annotations

import copy
import sys
import unittest
from pathlib import Path
from unittest.mock import patch


RELEASE_ROOT = Path(__file__).resolve().parents[1]
TEST_ROOT = Path(__file__).resolve().parent
for path in (RELEASE_ROOT, TEST_ROOT):
    if str(path) not in sys.path:
        sys.path.insert(0, str(path))

from release_actions import (  # noqa: E402
    PHASES,
    AdmittedImageExecutor,
    SelectedReleaseActionContext,
    begin_release_action_run,
    execute_release_action,
)
from release_checkpoint import (  # noqa: E402
    NATIVE_PORTABLE_RELEASE_ACTION_CHECKPOINT_SCHEMA,
    dump_release_checkpoint,
    release_action_checkpoint_sha256,
    restore_release_action_checkpoint,
)
from release_contract import ReleaseContractError, canonical_json  # noqa: E402
from release_portable_contract import SealedPortableCandidateCompilation  # noqa: E402
from release_portable_package import PreparedPortableReleasePackage  # noqa: E402
from release_suite import PortableSuiteGateEvidence  # noqa: E402
import test_portable_contract as portable_fixture  # noqa: E402


class _Docker:
    def run(self, *args, **kwargs):  # pragma: no cover - Unit is patched below.
        raise AssertionError("the native unit fixture must not invoke Docker")


class PortableReleaseActionsTests(unittest.TestCase):
    def setUp(self) -> None:
        self.fixture = portable_fixture.PortableContractTests("run")
        self.fixture.setUp()
        self.addCleanup(self.fixture.doCleanups)
        self.root = self.fixture.root
        self.fixture.write(
            ".caprmedio_caprmedio/project_structure.toml",
            (
                "[[scope_units]]\n"
                'scope_unit_name = "FRAMEWORK_METHODOLOGY"\n'
                'delivery_path = "101_FRAMEWORK_METHODOLOGY"\n\n'
                "[[scope_units]]\n"
                'scope_unit_name = "METHODOLOGY_SOURCES"\n'
                'parent = "FRAMEWORK_METHODOLOGY"\n'
                f'authority_path = "{portable_fixture.CANONICAL_SOURCE_RELATIVE}"\n'
                'delivery_path = "101_FRAMEWORK_METHODOLOGY/000_METHODOLOGY_SOURCES"\n\n'
                "[[scope_units]]\n"
                'scope_unit_name = "APPLICABLE_METHODOLOGY"\n'
                'parent = "FRAMEWORK_METHODOLOGY"\n'
                'delivery_path = "101_FRAMEWORK_METHODOLOGY/00_APPLICABLE_METHODOLOGY"\n\n'
                "[[scope_units]]\n"
                'scope_unit_name = "FRAMEWORK_ENGINE"\n'
                'authority_path = ".caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE"\n'
                'delivery_path = "102_FRAMEWORK_ENGINE"\n'
            ).encode("utf-8"),
        )
        self.candidate, _private = self.fixture.sealed()
        manifest = self.candidate.manifest.model_dump(mode="json", by_alias=True)
        self.request = {
            "operation": "apply",
            "project_root": str(self.root),
            "candidateSnapshotManifest": manifest,
            "expected_executing_release": manifest["executing_release"],
            "expected_project_structure_digest": manifest["project_structure_digest"],
            "expected_framework_settings_digest": manifest["framework_settings_digest"],
            "expected_source_frontier_digest": manifest["source_frontier_digest"],
            "run_receipt_refs": ["fixture-release-receipt"],
        }
        self.checkpoints = []

        def checkpoint(run):
            self.checkpoints.append(dump_release_checkpoint(run))

        self.run = begin_release_action_run(
            self.request,
            workflow_run_id="portable-001",
            checkpoint_callback=checkpoint,
        )
        self.run.image_executor = AdmittedImageExecutor(str(self.root), "portable-001", _Docker())

    def context(self, index: int) -> SelectedReleaseActionContext:
        step, action, _phase = PHASES[index]
        return SelectedReleaseActionContext(
            str(self.root), "portable-001", f"portable-001:step:{index + 1}",
            f"portable-001:step:{index + 1}:action:1", "portable-001",
            f"portable-001:step:{index + 1}", step, action,
            self.run.frozen_parameters_sha256, workflow_version=11,
        )

    def execute(self, index: int):
        return execute_release_action(self.request, context=self.context(index), run=self.run)

    def _portable_suite(self) -> PortableSuiteGateEvidence:
        portable = self.run.portable_compilation
        assert portable is not None
        return PortableSuiteGateEvidence(
            input_schema="portable-1",
            candidate_snapshot_manifest_sha256=self.candidate.manifest.sha256,
            candidate_run_id=portable.candidate_run_id,
            input_manifest_sha256=portable.input_manifest_sha256,
            source_catalog_sha256=portable.source_catalog_sha256,
            framework_version=portable.framework_version,
            version_toml_sha256=portable.version_toml_sha256,
            outcome="passed",
            reason="synthetic native Unit pass",
            runner="fixture",
            command=("fixture",),
            working_directory=".",
            exit_code=0,
            executed_tests=1,
            coverage=("Methodology", "Tools", "Apps", "MCP", "Agentic", "Skill"),
            evidence_root=".caprmedio_tmp/native-unit",
            stdout_sha256="a" * 64,
            stderr_sha256="b" * 64,
            report_sha256="c" * 64,
            executing_selector_sha256="d" * 64,
            executing_release_package_sha256="e" * 64,
            executing_skill_sha256="f" * 64,
            receipt_sha256="1" * 64,
            elapsed_seconds=0.1,
        )

    def test_native_private_preparation_precedes_the_full_gate(self) -> None:
        catalog_before = (self.root / "catalog.toml").read_bytes()
        for index in range(2):
            result = self.execute(index)
            self.assertEqual(result.outcome, "completed")

        self.assertIsNotNone(self.run.methodology_export)
        self.assertIsNotNone(self.run.private_compilation)
        self.assertIsNotNone(self.run.portable_source_snapshot)
        self.assertIsInstance(self.run.portable_compilation, SealedPortableCandidateCompilation)
        self.assertEqual((self.root / "catalog.toml").read_bytes(), catalog_before)
        self.assertEqual(self.run.next_phase, 2)
        self.assertEqual(
            PHASES,
            (
                ("CA-O-170", "CA-O-165", "freeze"),
                ("CA-O-175", "CA-O-167", "stage_candidate"),
                ("CA-O-185", "CA-O-168", "closed_unit_gate"),
                ("CA-O-176", "CA-O-168", "candidate_image_build"),
                ("CA-O-186", "CA-O-168", "candidate_image_canary"),
                ("CA-O-182", "CA-O-181", "host_candidate_e2e"),
                ("CA-O-184", "CA-O-183", "aggregate_full_gate"),
                ("CA-O-172", "CA-O-166", "deliver_sources"),
                ("CA-O-173", "CA-O-166", "compile"),
                ("CA-O-178", "CA-O-169", "promote"),
            ),
        )

        checkpoint = dump_release_checkpoint(self.run)
        self.assertEqual(checkpoint["schema"], NATIVE_PORTABLE_RELEASE_ACTION_CHECKPOINT_SCHEMA)
        restored = restore_release_action_checkpoint(canonical_json(checkpoint))
        self.assertEqual(restored.portable_compilation, self.run.portable_compilation)
        self.assertEqual(restored.portable_source_snapshot, self.run.portable_source_snapshot)

        malformed = copy.deepcopy(checkpoint)
        malformed["state"]["unexpected"] = None
        malformed["sha256"] = release_action_checkpoint_sha256(malformed)
        with self.assertRaises(ReleaseContractError) as invalid:
            restore_release_action_checkpoint(canonical_json(malformed))
        self.assertEqual(invalid.exception.code, "release-checkpoint-invalid")

    def test_native_private_package_precedes_unit_gate(self) -> None:
        for index in range(2):
            self.assertEqual(self.execute(index).outcome, "completed")
        package_root = self.root / ".caprmedio_tmp/release_candidates/portable-001/package"
        self.assertTrue(package_root.exists())
        suite = self._portable_suite()
        with (
            patch("release_actions.installed_n_suite_executor", return_value=object()),
            patch("release_actions.execute_bound_release_suite", return_value=suite),
        ):
            self.assertEqual(self.execute(2).outcome, "completed")

        self.assertIsInstance(self.run.prepared_portable_package, PreparedPortableReleasePackage)
        self.assertTrue(package_root.exists())

    def test_missing_admitted_catalog_blocks_compile_without_replay(self) -> None:
        self.assertEqual(self.execute(0).outcome, "completed")
        (self.root / "catalog.toml").unlink()

        blocked = self.execute(1)

        self.assertEqual(blocked.outcome, "blocked")
        self.assertEqual(blocked.reason, "phase stopped: portable-contract-catalog-missing")
        self.assertTrue(self.run.stopped)
        self.assertEqual(self.execute(1), blocked)


if __name__ == "__main__":
    unittest.main()
