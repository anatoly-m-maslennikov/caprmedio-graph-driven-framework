"""Disposable integration lifecycle checks without contacting Docker."""

from contextlib import redirect_stderr, redirect_stdout
import io
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import MagicMock, patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import full_suite_docker as docker  # noqa: E402
import run_full_test_suite as full  # noqa: E402

IMAGE = "sha256:" + "a" * 64


class FullSuiteDockerTests(unittest.TestCase):
    def setUp(self):
        parent = Path(__file__).resolve().parents[2] / ".caprmedio_tmp/tests/full-suite-docker"
        parent.mkdir(parents=True, exist_ok=True)
        directory = tempfile.TemporaryDirectory(dir=parent)
        self.addCleanup(directory.cleanup)
        self.root = Path(directory.name)
        self.output, self.errors = io.StringIO(), io.StringIO()

    def test_builds_current_source_once_without_cached_resolution(self):
        with (
            patch.object(docker, "ImageManager", autospec=True) as factory,
            patch.object(docker, "_remove_owned_image") as cleanup,
        ):
            manager = factory.return_value
            manager._build.return_value = IMAGE
            with docker.current_code_test_image(self.root) as environment:
                self.assertEqual(IMAGE, environment["CAPRMEDIO_FIRST_CUT_HTTP_IMAGE"])
                self.assertEqual(IMAGE, environment["CAPRMEDIO_DOCKER_QUERY_IMAGE"])
                scratch = Path(environment["CAPRMEDIO_FIRST_CUT_HTTP_SCRATCH"])
                self.assertEqual(str(scratch), environment["TMPDIR"])
                self.assertTrue(scratch.is_relative_to(self.root / ".caprmedio_tmp"))
                self.assertTrue(scratch.is_dir())
            manager._build.assert_called_once_with(manager.identity.return_value)
            manager.resolve.assert_not_called()
            self.assertEqual(self.root, factory.call_args.args[0])
            self.assertEqual(IMAGE, cleanup.call_args.args[1])

    def test_owned_cleanup_runs_even_when_tests_raise(self):
        with (
            patch.object(docker, "ImageManager", autospec=True) as factory,
            patch.object(docker, "_remove_owned_image") as cleanup,
        ):
            factory.return_value._build.return_value = IMAGE
            with self.assertRaisesRegex(RuntimeError, "test failure"):
                with docker.current_code_test_image(self.root):
                    raise RuntimeError("test failure")
            cleanup.assert_called_once()

    def test_build_executor_adds_only_unique_test_label_and_preserves_bounded_runner(self):
        with patch.object(docker, "_bounded_run") as execute:
            docker._executor("unique-attempt")(
                ["docker", "build", "--file", "Dockerfile", "context"],
                cwd=self.root,
                timeout=600,
                env={"BUILDX_CONFIG": "private-buildx"},
            )
            self.assertEqual(
                [
                    "docker",
                    "build",
                    "--label",
                    f"{docker.ATTEMPT_LABEL}=unique-attempt",
                    "--file",
                    "Dockerfile",
                    "context",
                ],
                execute.call_args.args[0],
            )
            self.assertFalse(execute.call_args.kwargs["capture_stdout"])
            self.assertEqual("private-buildx", execute.call_args.kwargs["buildx_config"])

    def test_cleanup_is_attributed_non_force_and_does_not_touch_containers(self):
        inspection = json.dumps([{"Config": {"Labels": {docker.ATTEMPT_LABEL: "ours"}}}])
        results = [
            subprocess.CompletedProcess([], 0, inspection),
            subprocess.CompletedProcess([], 0, ""),
            subprocess.CompletedProcess([], 0, ""),
        ]
        with patch.object(docker, "_bounded_run", side_effect=results) as execute:
            docker._remove_owned_image(self.root, IMAGE, "ours")
            commands = [call.args[0] for call in execute.call_args_list]
            self.assertEqual(["docker", "image", "rm", IMAGE], commands[-1])
            self.assertFalse(any("--force" in command or "down" in command for command in commands))

    def test_in_use_or_unattributed_image_is_retained_and_reported(self):
        for label, containers in (("other", ""), ("ours", "existing-container")):
            inspection = json.dumps([{"Config": {"Labels": {docker.ATTEMPT_LABEL: label}}}])
            results = [
                subprocess.CompletedProcess([], 0, inspection),
                subprocess.CompletedProcess([], 0, containers),
            ]
            with (
                patch.object(docker, "_bounded_run", side_effect=results) as execute,
                redirect_stderr(self.errors),
            ):
                docker._remove_owned_image(self.root, IMAGE, "ours")
                self.assertFalse(
                    any(
                        call.args[0][:3] == ["docker", "image", "rm"]
                        for call in execute.call_args_list
                    )
                )
        self.assertIn("Test image cleanup", self.errors.getvalue())

    def test_real_launcher_cli_receives_current_image_and_both_groups(self):
        environment = {
            "CAPRMEDIO_FIRST_CUT_HTTP_IMAGE": IMAGE,
            "CAPRMEDIO_FIRST_CUT_HTTP_SCRATCH": str(self.root),
        }
        result = subprocess.CompletedProcess([], 1, "actual output", "actual error")
        with (
            patch.object(docker.subprocess, "run", return_value=result) as execute,
            redirect_stdout(self.output),
            redirect_stderr(self.errors),
        ):
            self.assertFalse(docker.run_launcher(self.root, environment))
            argv = execute.call_args.args[0]
            self.assertEqual(IMAGE, argv[argv.index("--image") + 1])
            self.assertEqual("all", argv[argv.index("--group") + 1])
            self.assertNotIn("--build-missing", argv)
            self.assertEqual(1980, execute.call_args.kwargs["timeout"])
        self.assertEqual("actual error", self.errors.getvalue())

    def test_full_suite_uses_image_environment_and_required_cli_result(self):
        module = self.root / docker.APP / "tests/test_docker_e2e.py"
        lifecycle = MagicMock()
        lifecycle.__enter__.return_value = {"CAPRMEDIO_FIRST_CUT_HTTP_IMAGE": IMAGE}
        with (
            patch.dict(
                full.os.environ,
                {
                    "CAPRMEDIO_RELEASE_E2E_CONTEXT": "old-sealed-context.json",
                    "CAPRMEDIO_CANDIDATE_IMAGE_DIGEST": "sha256:" + "b" * 64,
                },
            ),
            patch.object(full, "discover_test_modules", return_value=[module]),
            patch.object(full, "current_code_test_image", return_value=lifecycle) as build,
            patch.object(full, "run_module", return_value=(True, 2, 0, "", "", 0.0, None)) as run,
            patch.object(full, "run_launcher", return_value=False) as launcher,
            redirect_stdout(self.output),
            redirect_stderr(self.errors),
        ):
            self.assertEqual(1, full.run_full_suite(self.root))
            build.assert_called_once_with(self.root)
            self.assertEqual(IMAGE, run.call_args.args[2]["CAPRMEDIO_FIRST_CUT_HTTP_IMAGE"])
            for environment in (run.call_args.args[2], launcher.call_args.args[1]):
                self.assertNotIn("CAPRMEDIO_RELEASE_E2E_CONTEXT", environment)
                self.assertNotIn("CAPRMEDIO_CANDIDATE_IMAGE_DIGEST", environment)
            launcher.assert_called_once()
            lifecycle.__exit__.assert_called_once()
        self.assertIn("project_launcher_docker_e2e CLI", self.errors.getvalue())

    def test_missing_required_build_environment_fails_without_running_tests(self):
        module = self.root / docker.APP / "tests/test_docker_e2e.py"
        lifecycle = MagicMock()
        lifecycle.__enter__.side_effect = OSError("Docker socket denied")
        with (
            patch.object(full, "discover_test_modules", return_value=[module]),
            patch.object(full, "current_code_test_image", return_value=lifecycle),
            patch.object(full, "run_module") as run,
            redirect_stderr(self.errors),
        ):
            self.assertEqual(1, full.run_full_suite(self.root))
            run.assert_not_called()
        self.assertIn("Docker socket denied", self.errors.getvalue())


if __name__ == "__main__":
    unittest.main()
