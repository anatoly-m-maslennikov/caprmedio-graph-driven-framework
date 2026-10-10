"""Focused O164@11 action-dispatch coverage.

These tests exercise disposable fixtures only.  They establish neither a
shared-Session receipt nor a Project release proof.
"""

from __future__ import annotations

import json
import sys
import tempfile
import unittest
from dataclasses import replace
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch


RELEASE_ROOT = Path(__file__).resolve().parents[1]
TEST_ROOT = Path(__file__).resolve().parent
for path in (RELEASE_ROOT, TEST_ROOT):
    if str(path) not in sys.path:
        sys.path.insert(0, str(path))

from release_actions import (  # noqa: E402
    AdmittedImageExecutor,
    LocalReleaseHelperBinding,
    PHASES,
    ReleaseActionRun,
    SelectedReleaseActionContext,
    execute_release_action,
)
from release_contract import ReleaseContractError  # noqa: E402
from release_image import (  # noqa: E402
    CANDIDATE_LABEL,
    CONTEXT_LABEL,
    DockerCommandResult,
    PortableImageBuildEvidence,
)
from release_suite_execution import _DEADLINE_GUARD, _PYTHON_CAPABILITY_GUARD  # noqa: E402
import test_portable_release_actions as portable_actions  # noqa: E402
import test_release_image as image_test  # noqa: E402
import test_release_suite as suite_test  # noqa: E402


class SelectedNSuiteDocker(image_test.FakeDocker):
    """Mocked Docker admission plus sandboxed suite run for the selected N image."""

    def __init__(self, root: Path, suite_executor: suite_test.FixtureSandboxExecutor):
        super().__init__()
        self.root = root
        self.suite_executor = suite_executor
        self.selected_release = "N"
        self.source_context_sha256 = "b" * 64

    def run(self, argv, *, cwd, timeout_seconds):
        argv = tuple(argv)
        if argv[:3] == ("docker", "image", "inspect"):
            if self.labels:
                return super().run(argv, cwd=cwd, timeout_seconds=timeout_seconds)
            self.calls.append(argv)
            payload = [{"Id": argv[3], "Config": {"Labels": {
                CANDIDATE_LABEL: self.selected_release,
                CONTEXT_LABEL: self.source_context_sha256,
            }, "Env": ["PATH=/usr/bin:/bin"]}}]
            return DockerCommandResult(0, json.dumps(payload).encode(), b"", False)
        if argv[:2] == ("docker", "run") and "--cidfile" not in argv:
            entrypoint = argv.index("--entrypoint")
            if ("--mount" not in argv and argv[entrypoint + 2] == "sha256:" + "a" * 64
                    and argv[entrypoint + 3] == "-c"):
                self.calls.append(argv)
                return DockerCommandResult(0, b"", b"", False)
        if argv[:2] == ("docker", "run") and "--read-only" in argv and "--mount" in argv:
            self.calls.append(argv)
            image_index = argv.index("sha256:" + "a" * 64)
            command = (argv[argv.index("--entrypoint") + 1], *argv[image_index + 1:])
            if (len(command) >= 7 and command[1] == "-c" and command[4] == "--"
                    and tuple(command[5:]) == suite_test.SUITE_DRIVER_COMMAND):
                command = (
                    sys.executable, *command[1:5], sys.executable,
                    *command[6:], self.suite_executor.mode,
                    self.suite_executor.literal,
                )
            mounts = [argv[index + 1] for index, value in enumerate(argv) if value == "--mount"]
            workspace = Path(next(value.split("src=", 1)[1].split(",", 1)[0] for value in mounts if "dst=/workspace" in value))
            output = Path(next(value.split("src=", 1)[1].split(",", 1)[0] for value in mounts if "dst=/output" in value))
            environment = {
                value.split("=", 1)[0]: value.split("=", 1)[1]
                for index, value in enumerate(argv) if index and argv[index - 1] == "--env"
            }
            result = self.suite_executor.run(
                command, workspace=workspace, output_root=output,
                working_directory=("." if argv[argv.index("--workdir") + 1] == "/workspace"
                                   else argv[argv.index("--workdir") + 1].removeprefix("/workspace/")),
                environment=environment, timeout_seconds=timeout_seconds,
            )
            return DockerCommandResult(result.exit_code, result.stdout, result.stderr, result.timed_out)
        return super().run(argv, cwd=cwd, timeout_seconds=timeout_seconds)


class SelectedNSuiteDockerContractTests(unittest.TestCase):
    def test_preflight_and_deadline_wrapper_preserve_the_fixed_child_argv(self):
        class CapturingExecutor:
            mode = "success"
            literal = "$HOME;$(should-stay-literal)"

            def run(self, command, *, workspace, output_root, working_directory, environment, timeout_seconds):
                self.call = (command, workspace, output_root, working_directory, environment, timeout_seconds)
                return SimpleNamespace(exit_code=0, stdout=b"suite", stderr=b"", timed_out=False)

        with tempfile.TemporaryDirectory(ignore_cleanup_errors=True) as temporary:
            root = Path(temporary)
            workspace, output = root / "workspace", root / "output"
            workspace.mkdir()
            output.mkdir()
            executor = CapturingExecutor()
            docker = SelectedNSuiteDocker(root, executor)
            image = "sha256:" + "a" * 64
            preflight = (
                "docker", "run", "--rm", "--network=none", "--read-only", "--cap-drop=ALL",
                "--security-opt=no-new-privileges", "--pids-limit=128",
                "--tmpfs", "/tmp:rw,nosuid,nodev,exec,size=2g,mode=1777",
                "--entrypoint", "python", image, "-c", _PYTHON_CAPABILITY_GUARD,
            )
            self.assertEqual(docker.run(preflight, cwd=root, timeout_seconds=30).exit_code, 0)
            wrapped = (
                "docker", "run", "--rm", "--read-only",
                "--mount", f"type=bind,src={workspace},dst=/workspace,readonly",
                "--mount", f"type=bind,src={output},dst=/output",
                "--cidfile", str(output / "container.cid"),
                "--workdir", "/workspace", "--entrypoint", "python", image,
                "-c", _DEADLINE_GUARD, "17.5", "--", *suite_test.SUITE_DRIVER_COMMAND,
            )
            result = docker.run(wrapped, cwd=root, timeout_seconds=17.5)
            docker.spec = {
                "candidate_snapshot_manifest_sha256": "candidate",
                "package_manifest_sha256": "package",
                "package_rows": [],
            }
            canary = (
                "docker", "run", "--rm", "--network=none", "--read-only", "--cap-drop=ALL",
                "--security-opt=no-new-privileges", "--pids-limit=128",
                "--tmpfs", "/tmp:rw,nosuid,nodev,size=128m",
                "--entrypoint", "python", image, "/opt/caprmedio-release-canary.py",
            )
            canary_result = docker.run(canary, cwd=root, timeout_seconds=120)

        self.assertEqual(result.exit_code, 0)
        self.assertEqual(json.loads(canary_result.stdout)["candidate_snapshot_manifest_sha256"], "candidate")
        command, observed_workspace, observed_output, working_directory, environment, timeout = executor.call
        self.assertEqual(command, (
            sys.executable, "-c", _DEADLINE_GUARD, "17.5", "--",
            sys.executable, suite_test.SUITE_DRIVER_COMMAND[1], executor.mode, executor.literal,
        ))
        self.assertEqual((observed_workspace, observed_output, working_directory, environment, timeout),
                         (workspace, output, ".", {}, 17.5))
        self.assertEqual(docker.calls, [preflight, wrapped, canary])


class ReleaseActionsTests(portable_actions.PortableReleaseActionsTests):
    """Current native O164 dispatch, reusing the sealed portable fixture."""

    def test_v11_prepare_is_effect_free_for_every_selected_phase(self) -> None:
        request = {**self.request, "operation": "prepare"}
        for index, (_step, _action, phase) in enumerate(PHASES):
            result = execute_release_action(request, context=self.context(index), run=self.run)
            self.assertEqual((result.phase, result.outcome), (phase, "prepared"))
            self.assertEqual(result.attempted_effects, ())
            self.assertEqual(result.effect_evidence_refs, ())
        self.assertEqual(self.run.next_phase, 0)
        self.assertEqual(self.run.contexts, {})
        self.assertEqual(self.run.results, {})

    def test_v11_rejects_wrong_graph_and_retirement_is_not_selectable(self) -> None:
        for context in (
            replace(self.context(0), workflow_version=6),
            replace(self.context(0), action_atom_id="CA-O-199"),
            replace(self.context(9), action_atom_id="CA-O-199"),
        ):
            with self.subTest(context=context), self.assertRaises(ReleaseContractError):
                execute_release_action(self.request, context=context, run=self.run)
        self.assertNotIn("retire", {phase for _step, _action, phase in PHASES})
        self.assertEqual(self.run.contexts, {})
        self.assertEqual(self.run.results, {})

    def test_v11_selection_mismatches_refuse_before_dispatch_or_frontier_change(self) -> None:
        mismatches = (
            (self.request, replace(self.context(0), project_root=str(TEST_ROOT.resolve()))),
            (self.request, replace(self.context(0), workflow_run_id="foreign-workflow")),
            (self.request, replace(self.context(0), parent_workflow_run_id="foreign-parent")),
            (self.request, replace(self.context(0), parent_step_run_id="foreign-parent-step")),
            (self.request, replace(self.context(0), frozen_parameters_sha256="0" * 64)),
            ({**self.request, "run_receipt_refs": ["altered-receipt"]}, self.context(0)),
        )
        with patch("release_actions._invoke") as invoke:
            for request, context in mismatches:
                with self.subTest(context=context), self.assertRaises(ReleaseContractError):
                    execute_release_action(request, context=context, run=self.run)
                self.assertEqual(self.run.next_phase, 0)
                self.assertEqual(self.run.contexts, {})
                self.assertEqual(self.run.results, {})
            invoke.assert_not_called()

        self.assertEqual(self.execute(0).outcome, "completed")
        before_contexts, before_results = dict(self.run.contexts), dict(self.run.results)
        duplicate = replace(self.context(1), action_run_id=self.context(0).action_run_id)
        with patch("release_actions._invoke") as invoke, self.assertRaises(ReleaseContractError):
            execute_release_action(self.request, context=duplicate, run=self.run)
        invoke.assert_not_called()
        self.assertEqual(self.run.contexts, before_contexts)
        self.assertEqual(self.run.results, before_results)
        self.assertEqual(self.run.next_phase, 1)

    def test_v11_unit_refuses_missing_stage_and_foreign_executor_before_helper(self) -> None:
        (self.root / "catalog.toml").unlink()
        self.assertEqual(self.execute(0).outcome, "completed")
        with patch("release_actions.execute_bound_release_suite") as unit:
            missing_stage = self.execute(2)
        self.assertEqual(missing_stage.outcome, "blocked")
        self.assertIn("prerequisites are skipped", missing_stage.reason)
        unit.assert_not_called()
        self.assertEqual(self.run.next_phase, 1)

        self.bind_stage_session()
        self.assertEqual(self.execute(1).outcome, "completed")
        self.run.image_executor = AdmittedImageExecutor(str(self.root), "foreign-run", portable_actions._Docker())
        with patch("release_actions.execute_bound_release_suite") as unit:
            foreign_executor = self.execute(2)
        self.assertEqual(foreign_executor.outcome, "blocked")
        self.assertIn("executor-unadmitted", foreign_executor.reason)
        unit.assert_not_called()
        self.assertTrue(self.run.stopped)
        self.assertEqual(self.run.next_phase, 2)

    def test_v11_test_double_build_stops_later_gates_and_delivery(self) -> None:
        (self.root / "catalog.toml").unlink()
        self.assertEqual(self.execute(0).outcome, "completed")
        self.bind_stage_session()
        self.assertEqual(self.execute(1).outcome, "completed")
        suite = self._portable_suite()
        with (
            patch("release_actions.fresh_unit_suite_executor", return_value=object()),
            patch("release_actions.execute_bound_release_suite", return_value=suite),
        ):
            self.assertEqual(self.execute(2).outcome, "completed")

        portable = self.run.portable_compilation
        self.assertIsNotNone(portable)
        # This test isolates dispatch disposition.  The portable fixture's
        # checkpoint encoder correctly rejects synthetic image receipt bytes.
        self.run.checkpoint_callback = lambda _run: None
        test_double = PortableImageBuildEvidence(
            candidate_snapshot_manifest_sha256=self.candidate.manifest.sha256,
            outcome="built",
            reason="synthetic test-double build",
            candidate_image_digest="sha256:" + "a" * 64,
            context_root=".caprmedio_tmp/image",
            context_sha256="b" * 64,
            package_manifest_sha256="c" * 64,
            suite_receipt_sha256="d" * 64,
            evidence_root=".caprmedio_tmp/image",
            commands_sha256="e" * 64,
            execution_kind="test-double",
            receipt_sha256="f" * 64,
            source_catalog_sha256=portable.source_catalog_sha256,
            candidate_run_id=portable.candidate_run_id,
            input_manifest_sha256=portable.input_manifest_sha256,
            framework_version=portable.framework_version,
            version_toml_sha256=portable.version_toml_sha256,
            package_evidence_sha256="0" * 64,
            package_evidence_relpath="private/package-evidence.json",
        )
        with patch("release_actions.build_candidate_image", return_value=test_double):
            build = self.execute(3)
        self.assertEqual(build.outcome, "pending", build.reason)
        self.assertIs(self.run.build, test_double)
        self.assertTrue(self.run.stopped)
        self.assertEqual(self.run.next_phase, 3)
        with (
            patch("release_actions.verify_candidate_image") as canary,
            patch("release_actions._selected_local_bindings") as delivery,
        ):
            self.assertEqual(self.execute(4).outcome, "blocked")
            self.assertEqual(self.execute(7).outcome, "blocked")
        canary.assert_not_called()
        delivery.assert_not_called()

    def test_v11_unknown_or_interrupted_invocation_stops_without_replay(self) -> None:
        for error in (SystemExit(1), TypeError("unexpected result")):
            with self.subTest(error=type(error).__name__):
                self.setUp()
                try:
                    with patch("release_actions._invoke", side_effect=error) as invoke:
                        result = self.execute(0)
                        self.assertEqual(result.outcome, "effect_uncertain")
                        self.assertTrue(self.run.stopped)
                        self.assertEqual(self.run.next_phase, 0)
                        self.assertIs(self.execute(0), result)
                    invoke.assert_called_once()
                finally:
                    self.doCleanups()

    def test_v11_publish_stays_blocked_until_every_gate_precedes_delivery(self) -> None:
        (self.root / "catalog.toml").unlink()
        self.assertEqual(self.execute(0).outcome, "completed")
        self.bind_stage_session()
        self.assertEqual(self.execute(1).outcome, "completed")
        suite = self._portable_suite()
        with (
            patch("release_actions.fresh_unit_suite_executor", return_value=object()),
            patch("release_actions.execute_bound_release_suite", return_value=suite),
        ):
            self.assertEqual(self.execute(2).outcome, "completed")

        with patch("release_actions._selected_local_bindings") as delivery:
            blocked = self.execute(7)
        self.assertEqual(blocked.outcome, "blocked")
        self.assertIn("prerequisites are skipped", blocked.reason)
        delivery.assert_not_called()
        self.assertEqual(self.run.next_phase, 3)
        self.assertEqual(
            tuple(phase for _step, _action, phase in PHASES[2:7]),
            ("closed_unit_gate", "candidate_image_build", "candidate_image_canary",
             "host_candidate_e2e", "aggregate_full_gate"),
        )


class CheckpointCallbackTests(unittest.TestCase):
    """Pure callback ordering tests; no fixture, filesystem, or Tool runs."""

    def setUp(self):
        self.project_root = str(TEST_ROOT.resolve())
        self.request = SimpleNamespace(
            candidate_snapshot_manifest=SimpleNamespace(sha256="a" * 64),
            run_receipt_refs=(),
            operation="apply",
        )
        self.context = SelectedReleaseActionContext(
            self.project_root, "workflow", "step", "action", "workflow", "step",
            "CA-O-170", "CA-O-165", "f" * 64, workflow_version=11,
        )
        self.helper_binding = LocalReleaseHelperBinding("b" * 64, "c" * 64)
        self.helper_binding_patcher = patch(
            "release_actions._freeze_local_release_helper_binding",
            return_value=self.helper_binding,
        )
        self.helper_binding_patcher.start()
        self.addCleanup(self.helper_binding_patcher.stop)

    def execute(self, run, invoke):
        with patch("release_actions._request", return_value=self.request), \
             patch("release_actions._selection", return_value=(0, "freeze")), \
             patch("release_actions._invoke", return_value=invoke):
            return execute_release_action({}, context=self.context, run=run)

    def test_callback_sees_in_progress_before_invoke_and_completed_frontier_after(self):
        observations = []

        def checkpoint(run):
            observations.append((run.in_progress, run.results.get(0), run.next_phase, run.stopped))

        run = ReleaseActionRun(self.project_root, "workflow", "f" * 64, self.request, checkpoint_callback=checkpoint)
        result = self.execute(run, ("completed", "frozen", (), {"frozen": True}))
        self.assertEqual(result.outcome, "completed")
        self.assertEqual(observations[0], (self.context, None, 0, False))
        self.assertEqual(observations[1], (None, result, 1, False))

    def test_missing_callback_refuses_before_any_phase_invocation(self):
        run = ReleaseActionRun(self.project_root, "workflow", "f" * 64, self.request)
        with patch("release_actions._request", return_value=self.request), \
             patch("release_actions._selection", return_value=(0, "freeze")), \
             patch("release_actions._invoke", side_effect=AssertionError("invoke must not run")) as invoke:
            result = execute_release_action({}, context=self.context, run=run)
        self.assertEqual(result.outcome, "blocked")
        self.assertIn("checkpoint recorder is required", result.reason)
        self.assertEqual(invoke.call_count, 0)
        self.assertEqual(run.contexts, {})
        self.assertEqual(run.results, {})
        self.assertIsNone(run.in_progress)
        self.assertFalse(run.stopped)

    def test_pre_effect_checkpoint_failure_refuses_without_invocation(self):
        callbacks = []

        def fail_checkpoint(run):
            callbacks.append(run.in_progress)
            raise OSError("checkpoint unavailable")

        run = ReleaseActionRun(self.project_root, "workflow", "f" * 64, self.request, checkpoint_callback=fail_checkpoint)
        with patch("release_actions._request", return_value=self.request), \
             patch("release_actions._selection", return_value=(0, "freeze")), \
             patch("release_actions._invoke", side_effect=AssertionError("invoke must not run")) as invoke:
            result = execute_release_action({}, context=self.context, run=run)
        self.assertEqual(invoke.call_count, 0)
        self.assertEqual(result.outcome, "blocked")
        self.assertIn("before phase invocation", result.reason)
        self.assertTrue(run.stopped)
        self.assertIsNone(run.in_progress)
        self.assertEqual(callbacks, [self.context])

    def test_post_effect_checkpoint_failure_is_uncertain_and_never_replays(self):
        calls = []

        def fail_second_checkpoint(run):
            calls.append(run.in_progress)
            if len(calls) == 2:
                raise OSError("terminal checkpoint unavailable")

        run = ReleaseActionRun(self.project_root, "workflow", "f" * 64, self.request,
                               checkpoint_callback=fail_second_checkpoint)
        result = self.execute(run, ("completed", "frozen", (), {"frozen": True}))
        self.assertEqual(result.outcome, "effect_uncertain")
        self.assertIn("after phase invocation", result.reason)
        self.assertTrue(run.stopped)
        self.assertEqual(run.next_phase, 0)
        self.assertIs(run.results[0], result)
        repeated = self.execute(run, AssertionError("effect replayed"))
        self.assertIs(repeated, result)
        self.assertEqual(calls, [self.context, None])


if __name__ == "__main__":
    unittest.main()
