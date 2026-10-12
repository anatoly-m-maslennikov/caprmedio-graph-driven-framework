"""Focused coverage for the direct Project-owned public release."""

from __future__ import annotations

from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "PUBLIC_RELEASE"))
from public_release import run_public_release  # noqa: E402


class SimplePublicReleaseTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory(dir="/private/tmp", ignore_cleanup_errors=True)
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        (self.root / "version.toml").write_text('[framework]\nversion = "0.4.2.1"\n', encoding="utf-8")
        (self.root / "README.md").write_text("# Project\n", encoding="utf-8")
        (self.root / "VERSION_HISTORY.md").write_text("# Version History\n", encoding="utf-8")
        self.draft = {
            "description": "## New\n- Direct public release.\n\n## Fixed\n- Removed selector dependency.\n",
            "summary": ["Direct public release with one supplied PR description."],
        }

    def _runner(self, *, fail_tests: bool = False, branch: str = "amm/dev"):
        calls: list[tuple[str, ...]] = []

        def run(argv: tuple[str, ...], cwd: Path) -> subprocess.CompletedProcess[str]:
            self.assertEqual(self.root, cwd)
            calls.append(argv)
            if argv[:3] == ("git", "branch", "--show-current"):
                return subprocess.CompletedProcess(argv, 0, branch + "\n", "")
            if argv[:2] == ("git", "diff"):
                return subprocess.CompletedProcess(argv, 1, "", "")
            if argv[:3] == ("gh", "pr", "list"):
                return subprocess.CompletedProcess(argv, 0, "[]", "")
            if argv[:3] == ("gh", "pr", "create"):
                return subprocess.CompletedProcess(argv, 0, "https://github.com/acme/project/pull/42\n", "")
            if fail_tests and argv[:2] == ("uv", "run"):
                return subprocess.CompletedProcess(argv, 1, "", "tests failed")
            return subprocess.CompletedProcess(argv, 0, "", "")

        return run, calls

    def test_missing_draft_only_returns_the_one_required_schema(self) -> None:
        result = run_public_release(self.root, run_id="public-1")

        self.assertEqual("input_required", result["outcome"])
        self.assertIn("description", result["prompt"])
        self.assertEqual('[framework]\nversion = "0.4.2.1"\n', (self.root / "version.toml").read_text())
        self.assertFalse((self.root / ".caprmedio_tmp").exists())

    def test_tests_bump_docs_pr_link_and_final_push_use_one_runner(self) -> None:
        runner, calls = self._runner()
        result = run_public_release(self.root, run_id="public-2", content_draft=self.draft, runner=runner)

        self.assertEqual("completed", result["outcome"])
        self.assertEqual("0.4.3", result["version"])
        self.assertEqual("https://github.com/acme/project/pull/42", result["pr_url"])
        self.assertIn('version = "0.4.3"', (self.root / "version.toml").read_text())
        self.assertIn("Latest public release: **0.4.3**", (self.root / "README.md").read_text())
        history = (self.root / "VERSION_HISTORY.md").read_text()
        self.assertIn("## 0.4.3 [PR](https://github.com/acme/project/pull/42)", history)
        self.assertIn("- Direct public release with one supplied PR description.", history)
        self.assertEqual(7, len([argv for argv in calls if argv[:2] == ("git", "add")]))
        self.assertEqual(7, len([argv for argv in calls if argv[:2] == ("git", "commit")]))
        self.assertEqual(2, len([argv for argv in calls if argv[:2] == ("git", "push")]))
        create = next(argv for argv in calls if argv[:3] == ("gh", "pr", "create"))
        self.assertEqual(self.draft["description"], create[create.index("--body") + 1])

    def test_failed_test_stops_before_version_or_document_changes_and_writes_issue(self) -> None:
        runner, calls = self._runner(fail_tests=True)
        result = run_public_release(self.root, run_id="public-3", content_draft=self.draft, runner=runner)

        self.assertEqual("failed", result["outcome"])
        self.assertEqual("tests", result["failed_step"])
        self.assertTrue((self.root / result["report_path"]).is_file())
        self.assertIn('version = "0.4.2.1"', (self.root / "version.toml").read_text())
        self.assertFalse(any(argv[:2] == ("git", "push") for argv in calls))

    def test_refuses_a_branch_other_than_amm_dev_before_staging(self) -> None:
        runner, calls = self._runner(branch="main")
        result = run_public_release(self.root, run_id="public-4", content_draft=self.draft, runner=runner)

        self.assertEqual("failed", result["outcome"])
        self.assertEqual("content_draft", result["failed_step"])
        self.assertFalse(any(argv[:2] == ("git", "add") for argv in calls))


if __name__ == "__main__":
    unittest.main()
