"""Focused suite selection stays scoped, safe, and truthful."""

from __future__ import annotations

from contextlib import redirect_stderr, redirect_stdout
import io
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

TOOLS = Path(__file__).resolve().parents[1]

sys.path.insert(0, str(TOOLS))
import run_full_test_suite as full  # noqa: E402


PASSING = (
    "import unittest\n"
    "class Test(unittest.TestCase):\n"
    " def test_one(self): self.assertTrue(True)\n"
)


class FocusedReleaseTests(unittest.TestCase):
    def setUp(self) -> None:
        parent = TOOLS.parent / ".caprmedio_tmp/tests/focused-release"
        parent.mkdir(parents=True, exist_ok=True)
        directory = tempfile.TemporaryDirectory(dir=parent)
        self.addCleanup(directory.cleanup)
        self.root = Path(directory.name)
        for name in full.CODE_ROOTS:
            (self.root / name).mkdir()
        self.output, self.errors = io.StringIO(), io.StringIO()

    def file(self, relative: str, content: str = PASSING) -> Path:
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
        return path

    def run_suite(self, modules: tuple[str, ...] | None = None) -> int:
        with redirect_stdout(self.output), redirect_stderr(self.errors):
            if modules is None:
                return full.run_full_suite(self.root)
            return full.run_full_suite(self.root, test_modules=modules)

    def test_focused_selection_runs_only_requested_module_and_reports_scope(self) -> None:
        selected = self.file("PROJECT_TOOLS/tests/test_selected.py")
        unselected = self.file("PROJECT_TOOLS/tests/test_unselected.py")
        result = (True, 1, 0, "", "", 0.0, None)
        with patch.object(full, "run_module", return_value=result) as run:
            self.assertEqual(
                0,
                self.run_suite((selected.relative_to(self.root).as_posix(),)),
            )

        self.assertEqual([selected], [call.args[1] for call in run.call_args_list])
        report = self.output.getvalue()
        self.assertIn("focused", report.lower())
        self.assertIn(selected.relative_to(self.root).as_posix(), report)
        self.assertNotIn(unselected.name, report)

    def test_default_selection_remains_the_complete_discovered_suite(self) -> None:
        first = self.file("PROJECT_TOOLS/tests/test_first.py")
        second = self.file("PROJECT_TOOLS/tests/test_second.py")
        result = (True, 1, 0, "", "", 0.0, None)
        with patch.object(full, "run_module", return_value=result) as run:
            self.assertEqual(0, self.run_suite())

        self.assertEqual({first, second}, {call.args[1] for call in run.call_args_list})
        self.assertNotIn("focused", self.output.getvalue().lower())

    def assert_rejected(self, modules: tuple[str, ...]) -> None:
        with patch.object(full, "run_module") as run:
            try:
                status = self.run_suite(modules)
            except (OSError, ValueError) as error:
                status = 1
                self.errors.write(str(error))
        self.assertEqual(1, status)
        run.assert_not_called()

    def test_empty_duplicate_malformed_foreign_and_symlink_selection_is_rejected(self) -> None:
        selected = self.file("PROJECT_TOOLS/tests/test_selected.py")
        relative = selected.relative_to(self.root).as_posix()
        foreign = self.file("outside/test_foreign.py")

        cases = (
            ("empty", ()),
            ("duplicate", (relative, relative)),
            ("malformed", ("PROJECT_TOOLS/tests/test_selected",)),
            ("absolute", (str(selected),)),
            ("traversal", ("../outside/test_foreign.py",)),
            ("foreign", (foreign.relative_to(self.root).as_posix(),)),
        )
        for name, modules in cases:
            with self.subTest(name=name):
                self.output, self.errors = io.StringIO(), io.StringIO()
                self.assert_rejected(modules)

        linked_target = self.file("outside/test_link_target.py")
        link = self.root / "PROJECT_TOOLS/tests/test_link.py"
        link.symlink_to(linked_target)
        self.output, self.errors = io.StringIO(), io.StringIO()
        self.assert_rejected((link.relative_to(self.root).as_posix(),))

    def test_failing_and_required_skipped_focused_modules_fail_the_suite(self) -> None:
        failing = self.file(
            "PROJECT_TOOLS/tests/test_failing.py",
            PASSING.replace("assertTrue(True)", "assertTrue(False)"),
        )
        later = self.file("PROJECT_TOOLS/tests/test_later.py")
        self.assertEqual(
            1,
            self.run_suite((failing.relative_to(self.root).as_posix(), later.relative_to(self.root).as_posix())),
        )
        self.assertIn(later.name, self.output.getvalue())
        self.assertIn("failed modules: 1", self.output.getvalue())

        self.output, self.errors = io.StringIO(), io.StringIO()
        skipped = self.file(
            "PROJECT_TOOLS/tests/test_required_e2e.py",
            "import unittest\n"
            "@unittest.skip('required fixture unavailable')\n"
            "class Test(unittest.TestCase):\n"
            " def test_required(self): pass\n",
        )
        self.assertEqual(
            1,
            self.run_suite((skipped.relative_to(self.root).as_posix(),)),
        )
        self.assertIn("Required integration tests skipped", self.errors.getvalue())


if __name__ == "__main__":
    unittest.main()
