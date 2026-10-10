"""Focused unit coverage for the project-local public release sequence."""

from __future__ import annotations

import importlib.util
from pathlib import Path
import sys
import tempfile
import unittest


MODULE_PATH = Path(__file__).parents[1] / "PUBLIC_RELEASE" / "public_release.py"
SPEC = importlib.util.spec_from_file_location("project_public_release", MODULE_PATH)
assert SPEC is not None and SPEC.loader is not None
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class Hooks:
    def __init__(self) -> None:
        self.calls: list[tuple[object, ...]] = []
        self.test_result: object = {"passed": True}

    def prompt(self, root: Path, version: str, changes: tuple[str, ...]) -> dict[str, object]:
        self.calls.append(("prompt", root, version, changes))
        return {
            "whats_new": ["Public release path."],
            "whats_fixed": ["Only metadata follows the PR URL."],
            "version_history_bullets": ["Public release workflow."],
        }

    def test(self, root: Path, candidate_root: Path) -> object:
        self.calls.append(("test", root, candidate_root))
        return self.test_result

    def commit(self, root: Path, paths: tuple[str, ...], message: str) -> dict[str, str]:
        self.calls.append(("commit", tuple(paths), message))
        return {"commit": "abc"}

    def push(self, root: Path, branch: str) -> dict[str, str]:
        self.calls.append(("push", branch))
        return {"branch": branch}

    def pr(self, root: Path, branch: str, base: str, body: str) -> dict[str, str]:
        self.calls.append(("pr", branch, base, body))
        return {"url": "https://github.com/acme/project/pull/42"}

    def journal(self, event: dict[str, object]) -> None:
        self.calls.append(("journal", event["phase"]))


class PublicReleaseTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory(dir="/private/tmp", ignore_cleanup_errors=True)
        self.root = Path(self.temp.name)
        (self.root / "version.toml").write_text('[framework]\nversion = "1.2.3"\n', encoding="utf-8")
        (self.root / "README.md").write_text("# Project\n", encoding="utf-8")
        (self.root / "VERSION_HISTORY.md").write_text("# Version History\n", encoding="utf-8")
        self.hooks = Hooks()
        self.config = {
            "branch": "amm/dev",
            "base": "main",
            "release_paths": ["README.md", "VERSION_HISTORY.md", "docs/public-release.md"],
            "readme_path": "README.md",
            "notes_path": "docs/public-release.md",
            "version_history_path": "VERSION_HISTORY.md",
            "candidate_root": ".",
            "changes": ["release workflow"],
        }

    def tearDown(self) -> None:
        self.temp.cleanup()

    def test_one_prompt_one_suite_then_url_only_followup(self) -> None:
        result = MODULE.run_public_release(self.root, run_id="public-123", hooks=self.hooks, config=self.config)

        self.assertEqual("published", result["status"])
        self.assertEqual("https://github.com/acme/project/pull/42", result["url"])
        self.assertEqual(1, len([call for call in self.hooks.calls if call[0] == "prompt"]))
        self.assertEqual(1, len([call for call in self.hooks.calls if call[0] == "test"]))
        call_names = [call[0] for call in self.hooks.calls]
        self.assertLess(call_names.index("test"), call_names.index("commit"))
        self.assertEqual(1, len([call for call in self.hooks.calls if call[0] == "pr"]))
        self.assertEqual(
            [
                ("commit", ("README.md", "VERSION_HISTORY.md", "docs/public-release.md"), "release: public v1.2.3"),
                ("commit", ("VERSION_HISTORY.md",), "docs: record public v1.2.3 PR URL"),
            ],
            [call for call in self.hooks.calls if call[0] == "commit"],
        )
        self.assertEqual([("push", "amm/dev"), ("push", "amm/dev")], [call for call in self.hooks.calls if call[0] == "push"])
        pr_call = next(call for call in self.hooks.calls if call[0] == "pr")
        self.assertEqual("main", pr_call[2])
        self.assertIn("## What's new", pr_call[3])
        self.assertIn("## What's fixed", pr_call[3])
        history = (self.root / "VERSION_HISTORY.md").read_text(encoding="utf-8")
        self.assertIn("<!-- public-release:public-123 -->", history)
        self.assertIn("## 1.2.3 [PR](https://github.com/acme/project/pull/42)", history)
        self.assertIn("- Public release workflow.", history)
        self.assertIn("Latest public release: **1.2.3**", (self.root / "README.md").read_text(encoding="utf-8"))
        self.assertIn("## What's new", (self.root / "docs/public-release.md").read_text(encoding="utf-8"))

    def test_failed_suite_stops_before_remote_effects(self) -> None:
        self.hooks.test_result = {"passed": False}

        with self.assertRaisesRegex(MODULE.PublicReleaseError, "full test suite"):
            MODULE.run_public_release(self.root, run_id="public-124", hooks=self.hooks, config=self.config)

        self.assertEqual(1, len([call for call in self.hooks.calls if call[0] == "prompt"]))
        self.assertEqual(1, len([call for call in self.hooks.calls if call[0] == "test"]))
        self.assertFalse(any(call[0] in {"commit", "push", "pr"} for call in self.hooks.calls))


if __name__ == "__main__":
    unittest.main()
