"""Fixture-only discovery and execution of the shared full-suite entry point."""

from __future__ import annotations

from contextlib import redirect_stderr, redirect_stdout
import io
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

TOOLS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOLS))
import run_full_test_suite as full  # noqa: E402

PASSING = (
    "import unittest\nclass Test(unittest.TestCase):\n def test_one(self): self.assertTrue(True)\n"
)


class FullTestSuiteTests(unittest.TestCase):
    def setUp(self) -> None:
        temporary = TOOLS.parent / ".caprmedio_tmp/tests/full-test-suite"
        temporary.mkdir(parents=True, exist_ok=True)
        directory = tempfile.TemporaryDirectory(dir=temporary)
        self.addCleanup(directory.cleanup)
        self.root = Path(directory.name)
        for name in full.CODE_ROOTS:
            (self.root / name).mkdir()
        self.output = io.StringIO()
        self.errors = io.StringIO()

    def file(self, relative: str, content: str = PASSING) -> Path:
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
        return path

    def run_suite(self) -> int:
        with redirect_stdout(self.output), redirect_stderr(self.errors):
            return full.run_full_suite(self.root)

    def test_discovery_covers_both_source_roots_and_excludes_inert_copies(self) -> None:
        selected = [
            self.file("102_FRAMEWORK_ENGINE/component/tests/test_engine.py"),
            self.file("102_FRAMEWORK_ENGINE/capability/test_service.py"),
            self.file("PROJECT_TOOLS/tests/test_project.py"),
        ]
        for relative in (
            "102_FRAMEWORK_ENGINE/.caprmedio_tmp/test_generated.py",
            "102_FRAMEWORK_ENGINE/component/tests/fixture/project/tests/test_copied.py",
            "102_FRAMEWORK_ENGINE/component/tests/golden/test_engine.v1.py",
            "PROJECT_TOOLS/__pycache__/test_cache.py",
            "other/tests/test_outside.py",
        ):
            self.file(relative, "raise AssertionError('inert fixture must not execute')\n")
        self.assertEqual(sorted(selected), full.discover_test_modules(self.root))

    def test_duplicate_names_and_sibling_imports_use_fresh_interpreters(self) -> None:
        for component, value in (("first", "alpha"), ("second", "beta")):
            folder = f"102_FRAMEWORK_ENGINE/{component}/tests"
            self.file(f"{folder}/helper.py", f"VALUE = {value!r}\n")
            self.file(
                f"{folder}/test_same.py",
                "import unittest\nfrom helper import VALUE\n"
                f"class Test(unittest.TestCase):\n def test_value(self): self.assertEqual({value!r}, VALUE)\n",
            )
        self.assertEqual(0, self.run_suite(), self.errors.getvalue())
        self.assertIn("tests run: 2; skipped: 0; failed modules: 0", self.output.getvalue())

    def test_test_and_import_errors_fail_but_later_modules_still_run(self) -> None:
        self.file(
            "PROJECT_TOOLS/tests/test_a_failure.py",
            PASSING.replace("assertTrue(True)", "assertTrue(False)"),
        )
        self.file("PROJECT_TOOLS/tests/test_b_import.py", "import missing_fixture_dependency\n")
        self.file("PROJECT_TOOLS/tests/test_c_good.py")
        self.assertEqual(1, self.run_suite())
        self.assertIn("test_c_good.py", self.output.getvalue())
        self.assertIn("failed modules: 2", self.output.getvalue())
        self.assertIn("missing_fixture_dependency", self.errors.getvalue())

    def test_platform_skip_is_reported_without_claiming_every_test_passed(self) -> None:
        self.file(
            "PROJECT_TOOLS/tests/test_skip.py",
            "import unittest\n@unittest.skip('platform fixture: symlinks unavailable')\n"
            "class Test(unittest.TestCase):\n def test_optional(self): pass\n",
        )
        self.assertEqual(0, self.run_suite())
        self.assertIn("skipped: 1", self.output.getvalue())
        self.assertIn("platform fixture: symlinks unavailable", self.errors.getvalue())

    def test_required_integration_skip_is_a_failure(self) -> None:
        self.file(
            "PROJECT_TOOLS/tests/test_fixture_e2e.py",
            "import unittest\n"
            "@unittest.skip('missing test environment')\n"
            "class Test(unittest.TestCase):\n def test_required(self): pass\n",
        )
        self.assertEqual(1, self.run_suite())
        self.assertIn("Required integration tests skipped", self.errors.getvalue())
        self.assertIn("skipped: 1; failed modules: 1", self.output.getvalue())

    def test_existing_optins_are_forwarded_without_inventing_image_inputs(self) -> None:
        module = self.file("PROJECT_TOOLS/tests/test_one.py")
        result = subprocess.CompletedProcess(
            [], 0, full.RESULT_MARKER + '{"tests":1,"skipped":0}\n', ""
        )
        with (
            patch.dict(full.os.environ, {"CAPRMEDIO_DOCKER_QUERY_IMAGE": "actual-image"}),
            patch.object(full.subprocess, "run", return_value=result) as command,
        ):
            with redirect_stdout(self.output), redirect_stderr(self.errors):
                self.assertEqual((True, 1, 0), full.run_module(self.root, module))
            environment = command.call_args.kwargs["env"]
            self.assertEqual("1", environment["CAPRMEDIO_DOCKER_E2E"])
            self.assertEqual("1", environment["CAPRMEDIO_DOCKER_QUERY_E2E"])
            self.assertEqual("actual-image", environment["CAPRMEDIO_DOCKER_QUERY_IMAGE"])

    def test_empty_suite_and_module_with_no_cases_are_failures(self) -> None:
        self.assertEqual(1, self.run_suite())
        self.file("PROJECT_TOOLS/tests/test_empty.py", "VALUE = 1\n")
        self.assertEqual(1, self.run_suite())
        self.assertIn("No test cases loaded", self.errors.getvalue())

    def test_module_timeout_and_command_errors_are_truthful_failures(self) -> None:
        module = self.file("PROJECT_TOOLS/tests/test_one.py")
        for error in (
            OSError("fixture command unavailable"),
            subprocess.TimeoutExpired("fixture", 600),
        ):
            with (
                self.subTest(error=error),
                patch.object(full.subprocess, "run", side_effect=error) as command,
            ):
                self.assertEqual(1, self.run_suite())
                self.assertEqual(full.MODULE_TIMEOUT_SECONDS, command.call_args.kwargs["timeout"])
                self.assertIn(module.name, self.errors.getvalue())

    def test_symlink_test_module_is_not_executed_outside_source_root(self) -> None:
        original = self.file("outside.py")
        link = self.root / "PROJECT_TOOLS/tests/test_link.py"
        link.parent.mkdir(parents=True)
        link.symlink_to(original)
        with self.assertRaises(OSError):
            full.discover_test_modules(self.root)

    def test_missing_source_root_cannot_silently_shrink_the_full_suite(self) -> None:
        (self.root / "102_FRAMEWORK_ENGINE").rmdir()
        self.file("PROJECT_TOOLS/tests/test_only_project.py")
        with self.assertRaises(OSError):
            full.discover_test_modules(self.root)

    def test_symlink_test_directory_cannot_silently_shrink_the_full_suite(self) -> None:
        outside = self.root / "outside"
        outside.mkdir()
        (self.root / "PROJECT_TOOLS/tests").symlink_to(outside, target_is_directory=True)
        with self.assertRaises(OSError):
            full.discover_test_modules(self.root)


if __name__ == "__main__":
    unittest.main()
