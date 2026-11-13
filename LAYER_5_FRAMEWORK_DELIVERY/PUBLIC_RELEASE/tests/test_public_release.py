"""Direct public release fixtures and retained publication-boundary checks."""

from __future__ import annotations

import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from public_release import run_public_release


class PublicReleaseFixture(unittest.TestCase):
    def setUp(self) -> None:
        temp_root = (
            Path(__file__).resolve().parents[3] / ".caprmedio_tmp/verification/public-release-tests"
        )
        temp_root.mkdir(parents=True, exist_ok=True)
        self.temp = tempfile.TemporaryDirectory(dir=temp_root, ignore_cleanup_errors=True)
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        (self.root / "version.toml").write_text('[framework]\nversion = "0.4.2.1"\n')
        (self.root / "README.md").write_text("# Project\n")
        (self.root / "VERSION_HISTORY.md").write_text("# Version History\n")
        settings = self.root / ".caprmedio_caprmedio/caprmedio_project_settings.toml"
        settings.parent.mkdir()
        settings.write_text(
            '[project]\nkey="fixture"\nname="fixture"\nrepository_slug="project"\n[artifacts.identity]\nproject_prefix="FX"\n'
        )
        self.draft = {
            "description": "## New\n- Direct public release.\n\n## Fixed\n- Removed selector dependency.\n",
            "summary": ["Direct public release with one supplied PR description."],
        }
        self.snapshots: list[tuple[tuple[str, ...], dict[str, str]]] = []

    def _materials(self) -> dict[str, str]:
        return {
            name: (self.root / name).read_text()
            for name in ("version.toml", "README.md", "VERSION_HISTORY.md")
        }

    def _runner(
        self,
        *,
        fail_tests=False,
        branch="amm/dev",
        existing_pr=False,
        origin="git@githuba:acme/project.git",
        push_origin=None,
        discovery=None,
        created_url=None,
        change_after_tests=None,
        wrong_head=False,
        fail_push=False,
    ):
        calls: list[tuple[str, ...]] = []
        tracked = staged = self._materials()
        head = "a" * 40 + "\n"

        def run(argv: tuple[str, ...], cwd: Path) -> subprocess.CompletedProcess[str]:
            nonlocal tracked, staged, head
            self.assertEqual(self.root, cwd)
            calls.append(argv)
            self.snapshots.append((argv, self._materials()))
            if argv[:2] == ("git", "show"):
                return subprocess.CompletedProcess(argv, 0, tracked[argv[2].split(":", 1)[1]], "")
            if argv[:2] == ("git", "add"):
                staged = self._materials()
            if argv[:2] == ("git", "commit"):
                tracked = staged
            if fail_push and argv[:2] == ("git", "push"):
                return subprocess.CompletedProcess(argv, 1, "", "push uncertain")
            if fail_tests and argv[:2] == ("uv", "run"):
                return subprocess.CompletedProcess(argv, 1, "", "tests failed")
            if change_after_tests and argv[:2] == ("uv", "run"):
                if change_after_tests == "head":
                    head = "changed-head\n"
                else:
                    (self.root / "README.md").write_text("Changed after tested preparation.\n")
            match = {
                "url": "https://github.com/acme/project/pull/41",
                "state": "OPEN",
                "headRefName": "amm/dev",
                "baseRefName": "main",
            }
            responses = {
                ("git", "branch", "--show-current"): (0, branch + "\n"),
                ("git", "rev-parse", "HEAD"): (0, head),
                ("git", "status", "--porcelain"): (
                    0,
                    " M README.md\n" if self._materials() != tracked else "",
                ),
                ("git", "remote", "get-url"): (
                    0,
                    ((push_origin or origin) if "--push" in argv else origin) + "\n",
                ),
                ("git", "diff", "--cached"): (int(staged != tracked), ""),
                ("gh", "pr", "list"): (
                    0,
                    discovery
                    if discovery is not None
                    else json.dumps([match] if existing_pr else []),
                ),
                ("gh", "pr", "view"): (0, json.dumps(dict(match, url=("https://github.com/acme/project/pull/41" if existing_pr else "https://github.com/acme/project/pull/42"), isDraft=True, headRefOid=("b" * 40 if wrong_head else head.strip())))),
                ("gh", "pr", "create"): (
                    0,
                    created_url or "https://github.com/acme/project/pull/42\n",
                ),
            }
            code, output = responses.get(argv[:3], (0, ""))
            return subprocess.CompletedProcess(argv, code, output, "")

        return run, calls


class PublicReleaseTests(PublicReleaseFixture):
    def test_legacy_history_entries_are_sorted_without_losing_details(self):
        history = self.root / "VERSION_HISTORY.md"
        older = "## Version 0.3\n\nOld details.\n\n"
        newer = "## Version 0.4.1\n\nNewer details.\n\n"
        history.write_text("# Version History\n\nIntroduction.\n\n" + older + newer)
        runner, _ = self._runner(existing_pr=True)
        result = run_public_release(self.root, run_id="legacy", content_draft=self.draft, runner=runner)
        self.assertEqual("completed", result["outcome"], result)
        text = history.read_text()
        self.assertLess(text.index("## 0.4.3"), text.index(newer))
        self.assertLess(text.index(newer), text.index(older))
        self.assertIn("Introduction.", text)

    def test_single_tested_push_for_existing_and_new_pr(self):
        for existing in (False, True):
            with self.subTest(existing=existing):
                runner, calls = self._runner(existing_pr=existing)
                result = run_public_release(self.root, run_id="public-" + str(existing), content_draft=self.draft, runner=runner)
                self.assertEqual("completed", result["outcome"], result)
                push = next(x for x in calls if x[:2] == ("git", "push"))
                self.assertEqual(1, sum(x[:2] == ("git", "push") for x in calls))
                self.assertEqual("a" * 40 + ":refs/heads/amm/dev", push[-1])
                tests = next(i for i, x in enumerate(calls) if x[:2] == ("uv", "run"))
                self.assertLess(tests, calls.index(push))
                self.assertLess(calls.index(push), next(i for i, x in enumerate(calls) if x[:3] == ("gh", "pr", "ready")))
                materials = next(snapshot for x, snapshot in self.snapshots if x[:2] == ("uv", "run"))
                self.assertIn("[PR](" + result["pr_url"] + ")", materials["VERSION_HISTORY.md"])
                self.assertTrue(materials["VERSION_HISTORY.md"].startswith("# Version History\n\n<!-- public-release:"))
                (self.root / "version.toml").write_text('[framework]\nversion = "0.4.2.1"\n')
                (self.root / "README.md").write_text("# Project\n")
                (self.root / "VERSION_HISTORY.md").write_text("# Version History\n")
                self.snapshots.clear()

    def test_failures_stop_without_push_or_retry(self):
        for options in ({"fail_tests": True}, {"change_after_tests": "head"}, {"change_after_tests": "tracked"}, {"created_url": "https://github.com/other/project/pull/42"}, {"fail_push": True}, {"wrong_head": True}):
            with self.subTest(options=options):
                runner, calls = self._runner(**options)
                result = run_public_release(self.root, run_id="failure", content_draft=self.draft, runner=runner)
                self.assertEqual("failed", result["outcome"], result)
                pushes = sum(x[:2] == ("git", "push") for x in calls)
                self.assertEqual(int(bool(options.get("fail_push") or options.get("wrong_head"))), pushes)
                self.assertFalse(any(x[:3] == ("gh", "pr", "ready") for x in calls))
                (self.root / "version.toml").write_text('[framework]\nversion = "0.4.2.1"\n')
                (self.root / "README.md").write_text("# Project\n")
                (self.root / "VERSION_HISTORY.md").write_text("# Version History\n")
                self.snapshots.clear()


if __name__ == "__main__":
    unittest.main()
