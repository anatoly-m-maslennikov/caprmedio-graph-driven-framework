"""Direct public release fixtures and retained publication-boundary checks."""

from __future__ import annotations

import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "PUBLIC_RELEASE"))
from public_release import run_public_release


class PublicReleaseFixture(unittest.TestCase):
    def setUp(self) -> None:
        temp_root = (
            Path(__file__).resolve().parents[2] / ".caprmedio_tmp/verification/public-release-tests"
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
    ):
        calls: list[tuple[str, ...]] = []
        tracked = staged = self._materials()
        head = "fixture-head\n"

        def run(argv: tuple[str, ...], cwd: Path) -> subprocess.CompletedProcess[str]:
            nonlocal tracked, staged, head
            self.assertEqual(self.root, cwd)
            calls.append(argv)
            self.snapshots.append((argv, self._materials()))
            if argv[:2] == ("git", "add"):
                staged = self._materials()
            if argv[:2] == ("git", "commit"):
                tracked = staged
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
                ("gh", "pr", "create"): (
                    0,
                    created_url or "https://github.com/acme/project/pull/42\n",
                ),
            }
            code, output = responses.get(argv[:3], (0, ""))
            return subprocess.CompletedProcess(argv, code, output, "")

        return run, calls


class PublicReleaseTests(PublicReleaseFixture):
    def test_actual_mcp_loader_imports_companions_without_public_tool_path(self) -> None:
        project = Path(__file__).resolve().parents[2]
        script = (
            "import sys; from pathlib import Path; from unittest.mock import patch\n"
            "root = Path(sys.argv[1]); sys.path.insert(0, str(root / '102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/204_MCP'))\n"
            "from selected_routes import _direct_release_call\n"
            "with patch('subprocess.run', side_effect=AssertionError('Unexpected release effect')):\n"
            "    result = _direct_release_call(root, 'public.release', {'run_id': 'loader-test', 'content_draft': None})\n"
            "assert result['outcome'] == 'input_required', result\n"
        )
        checked = subprocess.run(
            (sys.executable, "-B", "-c", script, str(project)),
            cwd=project,
            text=True,
            capture_output=True,
            timeout=30,
            check=False,
        )
        self.assertEqual(0, checked.returncode, checked.stdout + checked.stderr)

    def test_one_draft_one_suite_then_url_only_followup(self) -> None:
        runner, calls = self._runner()
        result = run_public_release(
            self.root, run_id="public-123", content_draft=self.draft, runner=runner
        )
        self.assertEqual("completed", result["outcome"])
        self.assertEqual(1, sum(argv[:2] == ("uv", "run") for argv in calls))
        self.assertEqual(1, sum(argv[:3] == ("gh", "pr", "create") for argv in calls))
        tests = next(snapshot for argv, snapshot in self.snapshots if argv[:2] == ("uv", "run"))
        pushes = [snapshot for argv, snapshot in self.snapshots if argv[:2] == ("git", "push")]
        self.assertEqual(2, len(pushes))
        self.assertEqual(tests, pushes[0])
        self.assertEqual(tests["version.toml"], pushes[1]["version.toml"])
        self.assertEqual(tests["README.md"], pushes[1]["README.md"])
        self.assertEqual(
            tests["VERSION_HISTORY.md"].replace(
                "## 0.4.3\n", "## 0.4.3 [PR](https://github.com/acme/project/pull/42)\n"
            ),
            pushes[1]["VERSION_HISTORY.md"],
        )
        create = next(argv for argv in calls if argv[:3] == ("gh", "pr", "create"))
        self.assertEqual(self.draft["description"], create[create.index("--body") + 1])
        self.assertFalse(any(argv[:3] == ("gh", "pr", "merge") for argv in calls))

    def test_failed_suite_stops_before_remote_writes(self) -> None:
        runner, calls = self._runner(fail_tests=True)
        result = run_public_release(
            self.root, run_id="public-124", content_draft=self.draft, runner=runner
        )
        self.assertEqual("failed", result["outcome"])
        self.assertEqual("tests", result["failed_step"])
        self.assertEqual(1, sum(argv[:2] == ("uv", "run") for argv in calls))
        self.assertFalse(
            any(
                argv[:2] == ("git", "push")
                or argv[:3] in (("gh", "pr", "create"), ("gh", "pr", "edit"), ("gh", "pr", "ready"))
                for argv in calls
            )
        )

    def test_existing_actual_link_makes_finalization_a_no_op(self) -> None:
        runner, calls = self._runner(existing_pr=True)
        result = run_public_release(
            self.root, run_id="public-existing-pr", content_draft=self.draft, runner=runner
        )
        self.assertEqual("completed", result["outcome"])
        self.assertEqual(1, sum(argv[:2] == ("git", "commit") for argv in calls))
        self.assertEqual(1, sum(argv[:2] == ("git", "push") for argv in calls))
        tests = next(snapshot for argv, snapshot in self.snapshots if argv[:2] == ("uv", "run"))
        self.assertIn(
            "## 0.4.3 [PR](https://github.com/acme/project/pull/41)", tests["VERSION_HISTORY.md"]
        )
        self.assertEqual(tests, self._materials())


if __name__ == "__main__":
    unittest.main()
