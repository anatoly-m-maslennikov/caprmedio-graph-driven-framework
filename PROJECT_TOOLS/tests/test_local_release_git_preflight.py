"""The existing first checkpoint commits safe changes and proves clean input."""

from pathlib import Path
import subprocess
import unittest

import test_simple_local_release as fixtures
from local_release import run_local_release


class LocalReleaseGitPreflightTests(unittest.TestCase):
    def execute(
        self, mode: str
    ) -> tuple[dict[str, object], list[tuple[str, ...]], fixtures.SimpleLocalReleaseTests]:
        fixture = fixtures.SimpleLocalReleaseTests("runTest")
        fixture.setUp()
        self.addCleanup(fixture.doCleanups)
        calls: list[tuple[str, ...]] = []
        staged = mode in {"dirty", "commit-failed"}

        def runner(argv: tuple[str, ...], root: Path) -> subprocess.CompletedProcess[str]:
            nonlocal staged
            calls.append(argv)
            if argv[:4] == ("git", "diff", "--cached", "--name-only"):
                return subprocess.CompletedProcess(
                    argv, 0, ".env\n" if mode == "staged-env" else "", ""
                )
            if argv == ("git", "diff", "--cached", "--quiet"):
                return subprocess.CompletedProcess(argv, int(staged), "", "")
            if argv[:2] == ("git", "commit"):
                staged = False
                return subprocess.CompletedProcess(argv, int(mode == "commit-failed"), "", "")
            if argv[:2] == ("git", "status"):
                return subprocess.CompletedProcess(
                    argv,
                    int(mode == "status-failed"),
                    "?? .env.local\n" if mode == "residual-dirty" else "",
                    "",
                )
            return subprocess.CompletedProcess(argv, 0, "", "")

        with fixture._compiler():
            result = run_local_release(fixture.root, run_id="first-commit", runner=runner)
        return result, calls, fixture

    def test_dirty_input_committed_before_tests_and_build_provenance(self) -> None:
        result, calls, fixture = self.execute("dirty")
        self.assertEqual(result["outcome"], "completed")
        commit = next(index for index, argv in enumerate(calls) if argv[:2] == ("git", "commit"))
        test = next(
            index
            for index, argv in enumerate(calls)
            if any(value.endswith("run_full_test_suite.py") for value in argv)
        )
        self.assertLess(commit, test)
        self.assertEqual(
            calls[commit + 1], ("git", "status", "--porcelain", "--untracked-files=all")
        )
        self.assertEqual(sum(argv[:2] == ("git", "commit") for argv in calls), 1)
        fixture.provenance.assert_called_once()

    def test_clean_input_does_not_create_empty_commit(self) -> None:
        result, calls, _ = self.execute("clean")
        self.assertEqual(result["outcome"], "completed")
        self.assertFalse(any(argv[:2] == ("git", "commit") for argv in calls))

    def test_commit_status_and_residual_dirt_fail_before_tests_or_build(self) -> None:
        for mode in ("commit-failed", "status-failed", "residual-dirty"):
            with self.subTest(mode=mode):
                result, calls, fixture = self.execute(mode)
                self.assertEqual(result["outcome"], "failed")
                self.assertEqual(result["failed_step"], "git_before_validate_inputs")
                self.assertFalse(any(argv[0] in {"docker", "uv"} for argv in calls))
                fixture.image_factory.assert_not_called()
                fixture.provenance.assert_not_called()
                add = next(argv for argv in calls if argv[:3] == ("git", "add", "-A"))
                self.assertIn(":(exclude,glob)**/.env*", add)
                self.assertIn(":(exclude,glob)**/*.env", add)

    def test_pre_staged_environment_file_refuses_without_changing_index(self) -> None:
        result, calls, fixture = self.execute("staged-env")
        self.assertEqual(result["outcome"], "failed")
        self.assertEqual(len(calls), 1)
        self.assertEqual(calls[0][:4], ("git", "diff", "--cached", "--name-only"))
        fixture.image_factory.assert_not_called()


if __name__ == "__main__":
    unittest.main()
