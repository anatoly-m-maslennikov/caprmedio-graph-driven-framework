"""Focused coverage for the direct Project-owned public release."""

from __future__ import annotations

import json
import unittest

from test_public_release import PublicReleaseFixture, run_public_release


class SimplePublicReleaseTests(PublicReleaseFixture):
    def test_missing_draft_only_returns_the_one_required_schema(self) -> None:
        result = run_public_release(self.root, run_id="public-1")

        self.assertEqual("input_required", result["outcome"])
        self.assertIn("description", result["prompt"])
        self.assertEqual(
            '[framework]\nversion = "0.4.2.1"\n', (self.root / "version.toml").read_text()
        )
        self.assertFalse((self.root / ".caprmedio_tmp").exists())

    def test_tests_bump_docs_pr_link_and_final_push_use_one_runner(self) -> None:
        runner, calls = self._runner()
        result = run_public_release(
            self.root, run_id="public-2", content_draft=self.draft, runner=runner
        )

        self.assertEqual("completed", result["outcome"])
        self.assertEqual("0.4.3", result["version"])
        self.assertEqual("https://github.com/acme/project/pull/42", result["pr_url"])
        self.assertIn('version = "0.4.3"', (self.root / "version.toml").read_text())
        self.assertIn("Latest public release: **0.4.3**", (self.root / "README.md").read_text())
        history = (self.root / "VERSION_HISTORY.md").read_text()
        self.assertIn("## 0.4.3 [PR](https://github.com/acme/project/pull/42)", history)
        self.assertIn("- Direct public release with one supplied PR description.", history)
        self.assertEqual(6, len([argv for argv in calls if argv[:2] == ("git", "add")]))
        self.assertEqual(2, len([argv for argv in calls if argv[:2] == ("git", "commit")]))
        self.assertEqual(2, len([argv for argv in calls if argv[:2] == ("git", "push")]))
        tests = next(argv for argv in calls if argv[:2] == ("uv", "run"))
        self.assertIn("--all-groups", tests)
        self.assertIn("3.14", tests)
        self.assertTrue(any(item.endswith("run_full_test_suite.py") for item in tests))
        self.assertNotIn("-m", tests)
        create = next(argv for argv in calls if argv[:3] == ("gh", "pr", "create"))
        self.assertIn("--draft", create)
        self.assertEqual(self.draft["description"], create[create.index("--body") + 1])
        discovery = next(argv for argv in calls if argv[:3] == ("gh", "pr", "list"))
        first_push = next(argv for argv in calls if argv[:2] == ("git", "push"))
        self.assertLess(calls.index(discovery), calls.index(tests))
        self.assertLess(calls.index(tests), calls.index(first_push))
        self.assertEqual("acme/project", discovery[discovery.index("--repo") + 1])

    def test_existing_open_pr_is_made_draft_before_editing(self) -> None:
        runner, calls = self._runner(existing_pr=True)
        result = run_public_release(
            self.root, run_id="public-open", content_draft=self.draft, runner=runner
        )

        self.assertEqual("completed", result["outcome"])
        ready = (
            "gh",
            "pr",
            "ready",
            "https://github.com/acme/project/pull/41",
            "--undo",
            "--repo",
            "acme/project",
        )
        edit = next(argv for argv in calls if argv[:3] == ("gh", "pr", "edit"))
        self.assertLess(calls.index(ready), calls.index(edit))
        self.assertFalse(any(argv[:3] == ("gh", "pr", "create") for argv in calls))

    def test_failed_test_retains_prepared_materials_and_writes_issue(self) -> None:
        runner, calls = self._runner(fail_tests=True)
        result = run_public_release(
            self.root, run_id="public-3", content_draft=self.draft, runner=runner
        )

        self.assertEqual("failed", result["outcome"])
        self.assertEqual("tests", result["failed_step"])
        self.assertTrue((self.root / result["report_path"]).is_file())
        self.assertIn("tests failed", (self.root / result["report_path"]).read_text())
        self.assertIn('version = "0.4.3"', (self.root / "version.toml").read_text())
        self.assertFalse(any(argv[:2] == ("git", "push") for argv in calls))

    def test_refuses_a_branch_other_than_amm_dev_before_staging(self) -> None:
        runner, calls = self._runner(branch="main")
        result = run_public_release(
            self.root, run_id="public-4", content_draft=self.draft, runner=runner
        )

        self.assertEqual("failed", result["outcome"])
        self.assertEqual("content_draft", result["failed_step"])
        self.assertFalse(any(argv[:2] == ("git", "add") for argv in calls))

    def test_remote_identity_is_bound_before_staging(self) -> None:
        for options in (
            {"origin": "git@githuba:acme/other.git"},
            {"push_origin": "git@githuba:other/project.git"},
            {"origin": "https://example.com/acme/project.git"},
        ):
            with self.subTest(options=options):
                runner, calls = self._runner(**options)
                result = run_public_release(
                    self.root, run_id="public-remote", content_draft=self.draft, runner=runner
                )
                self.assertEqual("failed", result["outcome"])
                self.assertFalse(any(argv[:2] == ("git", "add") for argv in calls))
                self.assertIn('version = "0.4.2.1"', (self.root / "version.toml").read_text())

    def test_nonmatching_pr_refuses_before_preparation(self) -> None:
        match = {
            "url": "https://github.com/acme/project/pull/41",
            "state": "OPEN",
            "headRefName": "amm/dev",
            "baseRefName": "main",
        }
        for output in (
            json.dumps([match, match]),
            json.dumps([dict(match, baseRefName="other")]),
            json.dumps([dict(match, headRefName="other")]),
            json.dumps([dict(match, state="CLOSED")]),
            json.dumps([dict(match, url="https://github.com/other/project/pull/41")]),
            "broken",
        ):
            with self.subTest(output=output):
                runner, calls = self._runner(discovery=output)
                result = run_public_release(
                    self.root, run_id="public-discovery", content_draft=self.draft, runner=runner
                )
                self.assertEqual("failed", result["outcome"])
                self.assertEqual("discover_pr", result["failed_step"])
                self.assertIn('version = "0.4.2.1"', (self.root / "version.toml").read_text())
                self.assertFalse(
                    any(argv[:2] in (("uv", "run"), ("git", "push")) for argv in calls)
                )

    def test_created_pr_url_must_match_the_bound_repository(self) -> None:
        runner, calls = self._runner(created_url="https://github.com/other/project/pull/42")
        result = run_public_release(
            self.root, run_id="public-created", content_draft=self.draft, runner=runner
        )
        self.assertEqual("failed", result["outcome"])
        self.assertEqual("upsert_pr", result["failed_step"])
        self.assertEqual(1, sum(argv[:2] == ("git", "push") for argv in calls))
        self.assertNotIn("[PR]", (self.root / "VERSION_HISTORY.md").read_text())

    def test_suite_source_drift_stops_before_publication(self) -> None:
        for change in ("tracked", "head"):
            with self.subTest(change=change):
                runner, calls = self._runner(change_after_tests=change)
                result = run_public_release(
                    self.root,
                    run_id="public-drift-" + change,
                    content_draft=self.draft,
                    runner=runner,
                )
                self.assertEqual("failed", result["outcome"])
                self.assertEqual("tests", result["failed_step"])
                self.assertIn("tested-source-changed", result["error"])
                self.assertFalse(
                    any(
                        argv[:2] == ("git", "push")
                        or argv[:3]
                        in (("gh", "pr", "create"), ("gh", "pr", "edit"), ("gh", "pr", "ready"))
                        for argv in calls
                    )
                )


if __name__ == "__main__":
    unittest.main()
