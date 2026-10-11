"""Real private O167 preparation starts without a manually exported candidate."""

from __future__ import annotations

import hashlib
import sys
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch


RELEASE_ROOT = Path(__file__).resolve().parents[1]
TEST_ROOT = Path(__file__).resolve().parent
for directory in (RELEASE_ROOT, TEST_ROOT):
    if str(directory) not in sys.path:
        sys.path.insert(0, str(directory))

import test_portable_contract as fixtures  # noqa: E402
import methodology_export as exporter  # noqa: E402
import release_actions as actions  # noqa: E402
import release_version as native  # noqa: E402
from release_actions import (  # noqa: E402
    PHASES,
    SelectedReleaseActionContext,
    begin_release_action_run,
    execute_release_action,
)
from release_checkpoint import dump_release_checkpoint  # noqa: E402
from release_compilation import read_sealed_private_methodology_compilation  # noqa: E402
from release_handoff import CANONICAL_SOURCE_RELATIVE, bind_sealed_methodology_export  # noqa: E402
from workflow_run_support import RecordedActionStartProvenance, RunExecutionSession  # noqa: E402


class ReleaseStagePreparationTests(unittest.TestCase):
    def setUp(self) -> None:
        self.fixture = fixtures.PortableContractTests("run")
        self.fixture.setUp()
        self.addCleanup(self.fixture.doCleanups)
        self.root = self.fixture.root
        # The fixture's catalog predates our added sources. Start without a
        # catalog so the real selected O167 admission publishes this frontier.
        (self.root / "catalog.toml").unlink()
        self.structure = self.fixture.write(".caprmedio_caprmedio/project_structure.toml", (
            '[[scope_units]]\nscope_unit_name = "FRAMEWORK_METHODOLOGY"\n'
            'delivery_path = "101_FRAMEWORK_METHODOLOGY"\n'
            '[[scope_units]]\nscope_unit_name = "METHODOLOGY_SOURCES"\n'
            'parent = "FRAMEWORK_METHODOLOGY"\n'
            f'authority_path = "{CANONICAL_SOURCE_RELATIVE}"\n'
            'delivery_path = "101_FRAMEWORK_METHODOLOGY/000_METHODOLOGY_SOURCES"\n'
            '[[scope_units]]\nscope_unit_name = "APPLICABLE_METHODOLOGY"\n'
            'parent = "FRAMEWORK_METHODOLOGY"\n'
            'delivery_path = "101_FRAMEWORK_METHODOLOGY/00_APPLICABLE_METHODOLOGY"\n'
            '[[scope_units]]\nscope_unit_name = "FRAMEWORK_ENGINE"\n'
            'authority_path = ".caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE"\n'
            'delivery_path = "102_FRAMEWORK_ENGINE"\n'
        ).encode())
        self.fixture.write("PROJECT_TOOLS/RELEASE_VERSION/local_release.py", b"FIXTURE = True\n")
        self.fixture.write("PROJECT_TOOLS/RELEASE_VERSION/native_hooks.py",
                           b"def bind_local_release_core(module):\n    return None\n")
        self.active = self.fixture.write(
            f"{CANONICAL_SOURCE_RELATIVE}/001_CORE_META_MODEL/04_requirement/CA-R-002--current.md",
            fixtures.carrier("CA-R-002").replace(b"version: 1\n", b"version: 2\n"),
        )
        self.inactive = self.fixture.write(
            f"{CANONICAL_SOURCE_RELATIVE}/003_PROJECT_CONFIGURATION/04_requirement/CA-R-003--inactive.md",
            fixtures.carrier("CA-R-003").replace(b"status: Active\n", b"status: Inactive\n"),
        )
        self.archived = self.fixture.write(
            f"{CANONICAL_SOURCE_RELATIVE}/001_CORE_META_MODEL/04_requirement/archive/CA-R-002--prior.md",
            fixtures.carrier("CA-R-002").replace(b"status: Active\n", b"status: Archived\n"),
        )
        # Existing product and local settings must survive private preparation.
        self.product = self.fixture.write("101_FRAMEWORK_METHODOLOGY/prior.md", b"prior delivery\n")
        self.skill = self.fixture.write(".agents/skills/ca/SKILL.md", b"prior installed skill\n")
        self.runtime_settings = self.fixture.write(".caprmedio_runtime/settings.toml", b"[runtime]\nport = 8765\n")
        self.request = native.prepare_release_request(self.root, {"operation": "apply", "project_root": str(self.root)})
        self.checkpoints = []
        self.run = begin_release_action_run(
            self.request, workflow_run_id="stage-current-active",
            checkpoint_callback=lambda run: self.checkpoints.append(dump_release_checkpoint(run)),
        )
        self.candidate_root = self.root / ".caprmedio_tmp/release_candidates/stage-current-active"

    def context(self, index: int) -> SelectedReleaseActionContext:
        step, action, _phase = PHASES[index]
        return SelectedReleaseActionContext(
            str(self.root), self.run.workflow_run_id,
            f"{self.run.workflow_run_id}:step:{index + 1}",
            f"{self.run.workflow_run_id}:step:{index + 1}:action:1",
            self.run.workflow_run_id, f"{self.run.workflow_run_id}:step:{index + 1}",
            step, action, self.run.frozen_parameters_sha256, workflow_version=12,
        )

    def execute(self, index: int):
        return execute_release_action(self.request, context=self.context(index), run=self.run)

    def bind_stage_session(self) -> None:
        # Only Session lineage is synthetic. Export, compiler, catalog admission
        # and private package producers/readers below are the real implementations.
        context = self.context(1)
        action = self.fixture.write(".caprmedio_caprmedio/09_operations/CA-O-167-ACTION--fixture.md", b"# O167 fixture\n")
        session = object.__new__(RunExecutionSession)
        session.tracker = SimpleNamespace(root=self.root)
        session.actual = {
            "workflow": {"run_id": context.workflow_run_id, "kind": "workflow"},
            "step": {"run_id": context.step_run_id, "kind": "step", "parent_run_id": context.workflow_run_id},
            "action": {
                "run_id": context.action_run_id, "kind": "action", "parent_run_id": context.step_run_id,
                "definition": {"atom_id": "CA-O-167", "version": 1,
                               "path": action.relative_to(self.root).as_posix(),
                               "digest": hashlib.sha256(action.read_bytes()).hexdigest()},
            },
        }
        session.read_recorded_action_start = lambda identity: RecordedActionStartProvenance(
            "fixture-operator", "fixture-start", identity, (context.step_run_id, context.workflow_run_id),
        )
        self.run.selected_action_session = session

    def protected_bytes(self) -> dict[str, bytes]:
        paths = [self.structure, self.fixture.instance_settings, self.product, self.skill,
                 self.runtime_settings, self.root / ".caprmedio_runtime/framework/current.toml",
                 self.root / "version.toml"]
        paths.extend(path for path in self.fixture.source.rglob("*") if path.is_file())
        return {path.relative_to(self.root).as_posix(): path.read_bytes() for path in paths}

    def test_current_active_snapshot_creates_real_export_and_compilation_without_manual_seal(self) -> None:
        before = self.protected_bytes()
        self.assertFalse(self.candidate_root.exists())
        self.assertIsNone(self.run.methodology_export)
        self.assertEqual(self.execute(0).outcome, "completed")
        self.assertFalse(self.candidate_root.exists())
        self.bind_stage_session()
        result = self.execute(1)
        self.assertEqual(result.outcome, "completed", result.reason)
        self.assertEqual(self.run.next_phase, 2)
        bound = bind_sealed_methodology_export(self.run.candidate, self.candidate_root)
        self.assertEqual(bound, self.run.methodology_export)
        private = read_sealed_private_methodology_compilation(bound)
        self.assertEqual(private, self.run.private_compilation)
        sealed = exporter.read_sealed_export(release_candidate_root=self.candidate_root)
        self.assertEqual({(row["atom_id"], row["version"]) for row in sealed.inventory["atoms"]},
                         {("CA-R-001", 1), ("CA-R-002", 2)})
        self.assertEqual({row["path"] for row in sealed.inventory["support"]}, {
            "001_CORE_META_MODEL/caprmedio_framework_default_settings.toml",
            "003_PROJECT_CONFIGURATION/support.txt",
        })
        exported = {path.relative_to(self.candidate_root / "methodology").as_posix()
                    for path in (self.candidate_root / "methodology").rglob("*") if path.is_file()}
        self.assertNotIn(self.inactive.relative_to(self.fixture.source).as_posix(), exported)
        self.assertNotIn(self.archived.relative_to(self.fixture.source).as_posix(), exported)
        self.assertIsNotNone(self.run.prepared_portable_package)
        self.assertTrue((self.run.prepared_portable_package.private_package_root / "manifest.toml").is_file())
        self.assertEqual(self.protected_bytes(), before)
        self.assertEqual(self.request["run_receipt_refs"], [])
        for name in ("portable_suite", "build", "verification", "e2e", "full_gate", "promotion"):
            self.assertIsNone(getattr(self.run, name), name)
        self.assertEqual(self.execute(7).outcome, "blocked")  # No early delivery/full-gate bypass.
        self.assertEqual(self.protected_bytes(), before)

    def test_stage_refuses_frozen_source_or_configuration_drift_before_preparation(self) -> None:
        self.assertEqual(self.execute(0).outcome, "completed")
        self.bind_stage_session()
        for path in (self.active, self.structure, self.fixture.instance_settings):
            with self.subTest(path=path.relative_to(self.root).as_posix()):
                # Independent Run frontier for each drift; a stopped phase is never replayed.
                self.run = begin_release_action_run(
                    self.request, workflow_run_id="stage-current-active",
                    checkpoint_callback=lambda run: self.checkpoints.append(dump_release_checkpoint(run)),
                )
                self.assertEqual(self.execute(0).outcome, "completed")
                self.bind_stage_session()
                original = path.read_bytes()
                try:
                    path.write_bytes(original + b"# changed after freeze\n")
                    result = self.execute(1)
                    self.assertEqual(result.outcome, "blocked", result.reason)
                    self.assertTrue(self.run.stopped)
                    self.assertFalse(self.candidate_root.exists())
                    self.assertIsNone(self.run.methodology_export)
                    self.assertIsNone(self.run.prepared_portable_package)
                finally:
                    path.write_bytes(original)

    def test_stage_without_current_selected_session_does_not_create_private_export(self) -> None:
        self.assertEqual(self.execute(0).outcome, "completed")
        result = self.execute(1)
        self.assertEqual(result.outcome, "blocked", result.reason)
        self.assertIn("release-source-admission-session-unavailable", result.reason)
        self.assertFalse(self.candidate_root.exists())
        self.assertIsNone(self.run.prepared_portable_package)

    def test_concurrent_candidate_directory_claim_refuses_without_writing_into_it(self) -> None:
        self.assertEqual(self.execute(0).outcome, "completed")
        self.bind_stage_session()
        before = self.protected_bytes()
        self.assertFalse(self.candidate_root.exists())
        actual_exporter = actions._exporter_module()
        actual_freeze = actual_exporter.freeze_methodology_manifest
        sentinel = self.candidate_root / "other-writer.txt"

        def concurrent_creator(**kwargs):
            # Real discovery completes after the early absence check. Another
            # writer then owns the path before this Run's final atomic claim.
            frozen = actual_freeze(**kwargs)
            self.candidate_root.mkdir(parents=True)
            sentinel.write_bytes(b"other writer owns this candidate\n")
            return frozen

        # The native loader creates a fresh module each call; retain this real
        # module instance solely to inject the competing filesystem writer.
        with patch.object(actions, "_exporter_module", return_value=actual_exporter), \
             patch.object(actual_exporter, "freeze_methodology_manifest", side_effect=concurrent_creator) as freeze:
            result = self.execute(1)

        freeze.assert_called_once()
        self.assertEqual(result.outcome, "blocked", result.reason)
        self.assertIn("release-private-candidate-collision", result.reason)
        self.assertEqual({path.relative_to(self.candidate_root).as_posix(): path.read_bytes()
                          for path in self.candidate_root.rglob("*") if path.is_file()},
                         {"other-writer.txt": b"other writer owns this candidate\n"})
        self.assertEqual(list(self.candidate_root.iterdir()), [sentinel])
        self.assertEqual(self.protected_bytes(), before)
        self.assertFalse((self.root / "catalog.toml").exists())
        self.assertTrue(self.run.stopped)
        self.assertIsNone(self.run.methodology_export)
        self.assertIsNone(self.run.private_compilation)
        self.assertIsNone(self.run.prepared_portable_package)


if __name__ == "__main__":
    unittest.main()
