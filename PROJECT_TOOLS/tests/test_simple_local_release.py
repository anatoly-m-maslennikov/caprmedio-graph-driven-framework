"""The concrete Local release flow, without running Docker or installing packages."""

from __future__ import annotations

import subprocess
import stat
import sys
import tempfile
from types import ModuleType, SimpleNamespace
import unittest
from unittest.mock import patch
from pathlib import Path


sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "RELEASE_VERSION"))
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS"))
from local_release import run_local_release  # noqa: E402
from VALIDATE_ATOMS.validate_atoms_workers.proposed_carrier import ProposedCarrierError  # noqa: E402


class SimpleLocalReleaseTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory(ignore_cleanup_errors=True)
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name).resolve()
        self.control = self.root / ".caprmedio_caprmedio"
        self.sources = self.control / "101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES"
        rows = []
        for number, name in enumerate(("CORE_META_MODEL", "INSTALLED_EXTENSIONS", "PROJECT_CONFIGURATION"), 1):
            unit = self.sources / f"{number:03d}_{name}"
            unit.mkdir(parents=True)
            rows.extend(("[[scope_units]]", f'scope_unit_name = "{name}"',
                         f'authority_path = "{unit.relative_to(self.root).as_posix()}"', ""))
            for status in ("Active", "Draft", "Archived"):
                (unit / f"{status.lower()}.md").write_text(
                    f"---\natom_id: CA-R-{number}\nstatus: {status}\n---\n## Claim\n{status}\n", encoding="utf-8")
            historical = unit / "archive/active.md"
            historical.parent.mkdir()
            historical.write_text("---\nstatus: Active\n---\nold\n", encoding="utf-8")
        (self.control / "project_structure.toml").write_text("\n".join(rows), encoding="utf-8")
        self.product = self.root / "101_FRAMEWORK_METHODOLOGY"
        self.installed = self.control / "000_CAPRMEDIO_framework"
        self.runtime = self.root / ".caprmedio_runtime"
        for destination in (self.product, self.installed, self.runtime):
            destination.mkdir(parents=True)
            (destination / "old.txt").write_text("obsolete", encoding="utf-8")
            (destination / "config.toml").write_text("keep = true\n", encoding="utf-8")
        (self.installed / "project_structure.toml").write_text("preserved = true\n", encoding="utf-8")
        skill = self.root / "102_FRAMEWORK_ENGINE/202_AGENTIC/205_SKILLS/ca"
        skill.mkdir(parents=True)
        (skill / "SKILL.md").write_text("ca skill", encoding="utf-8")
        (self.root / "pyproject.toml").write_text("[project]\nname = 'fixture'\n", encoding="utf-8")
        (self.root / "uv.lock").write_text("version = 1\n", encoding="utf-8")
        (self.root / "version.toml").write_text('[framework]\nversion = "0.4.1"\n', encoding="utf-8")
        tools = self.root / "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS"
        tools.mkdir(parents=True)
        bootstrap_helper = (
            Path(__file__).resolve().parents[2]
            / "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/project_mcp_bootstrap.py"
        )
        (tools / "project_mcp_bootstrap.py").write_bytes(bootstrap_helper.read_bytes())
        (tools / "project_mcp_bootstrap.py").chmod(0o644)
        self.engine_bootstrap = (
            self.root / "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/"
            "WORKFLOW_ORCHESTRATOR/docker/start_mcp.py"
        )
        self.engine_bootstrap.parent.mkdir(parents=True)
        self.engine_bootstrap.write_bytes(b"#!/usr/bin/env python3\n# package bootstrap fixture\n")
        self.engine_bootstrap.chmod(0o755)
        # These transport/delivery fixtures deliberately omit full methodology authority.
        context = patch("VALIDATE_ATOMS.validate_atoms_workers.proposed_carrier.source_context_from_project",
                        autospec=True, return_value=SimpleNamespace(root=self.root))
        validation = patch("VALIDATE_ATOMS.validate_atoms_workers.proposed_carrier.validate_proposed_carrier",
                           autospec=True, return_value={})
        self.context = context.start()
        self.validation = validation.start()
        self.addCleanup(context.stop)
        self.addCleanup(validation.stop)

    def _runner(self):
        calls = []

        def run(argv, cwd):
            self.assertEqual(self.root, cwd)
            calls.append(argv)
            if argv == ("git", "diff", "--cached", "--quiet"):
                return subprocess.CompletedProcess(argv, 1, "", "")
            return subprocess.CompletedProcess(argv, 0, "", "")

        return run, calls

    def _compile(self, root):
        self.assertEqual(self.root, root)
        output = self.product / "applicable_methodology"
        output.mkdir(parents=True)
        (output / "compiled.md").write_text("compiled", encoding="utf-8")

    def _compiler(self, *, fail=False):
        module = ModuleType("COMPILE_APPLICABLE_METHODOLOGY.compile_applicable_methodology")
        module.CompileError = RuntimeError
        module.MethodologyPaths = SimpleNamespace
        module.compile_report = lambda root, paths: ({"can_apply": not fail}, (), {})
        module.stage_outputs = lambda *args: None
        module.replace_outputs_atomically = lambda root, staging, paths: self._compile(root)
        return patch.dict(sys.modules, {module.__name__: module})

    def test_active_sources_replace_product_and_installed_copy_preserves_config(self):
        archived = self.sources / "001_CORE_META_MODEL/archived/active@1.md"
        archived.parent.mkdir()
        archived.write_bytes((archived.parent.parent / "active.md").read_bytes())
        runner, calls = self._runner()
        with self._compiler():
            result = run_local_release(self.root, run_id="happy", runner=runner)
        self.assertEqual("completed", result["outcome"])
        for target in (self.product, self.installed):
            self.assertFalse((target / "old.txt").exists())
            self.assertEqual("keep = true\n", (target / "config.toml").read_text())
            self.assertTrue((target / "applicable_methodology/compiled.md").is_file())
            for unit in self.sources.iterdir():
                released = target / "sources" / unit.name
                self.assertEqual(["active.md"], sorted(path.name for path in released.rglob("*.md")))
        self.assertEqual("preserved = true\n", (self.installed / "project_structure.toml").read_text())
        self.assertEqual("keep = true\n", (self.runtime / "config.toml").read_text())
        bootstrap = self.runtime / "start_mcp.py"
        self.assertEqual(self.engine_bootstrap.read_bytes(), bootstrap.read_bytes())
        self.assertEqual(0o755, stat.S_IMODE(bootstrap.stat().st_mode))
        for package in (self.root / ".caprmedio_install/simple_local_release/package", self.runtime / "simple_local_release/package"):
            self.assertEqual("ca skill", (package / "SKILLS/ca/SKILL.md").read_text())
            self.assertTrue((package / "102_FRAMEWORK_ENGINE/202_AGENTIC/205_SKILLS/ca/SKILL.md").is_file())
        self.assertEqual("ca skill", (self.root / ".agents/skills/ca/SKILL.md").read_text())
        self.assertIn('version = "0.4.1.1"', (self.root / "version.toml").read_text())
        self.assertIn('version = "0.4.1.1"', (self.runtime / "simple_local_release/package/version.toml").read_text())
        self.assertEqual(1, sum(argv[-1:] == ("project-mcp",) for argv in calls))
        self.context.assert_called_once_with(self.root)
        self.assertEqual(3, self.validation.call_count)
        self.assertEqual(
            {path.relative_to(self.control) for path in self.sources.glob("*/active.md")},
            {call.args[3] for call in self.validation.call_args_list})
        for call in self.validation.call_args_list:
            self.assertEqual("Active", call.args[0]["status"])
            self.assertIs(self.context.return_value, call.args[2])

    def test_invalid_active_source_stops_before_tests_and_delivery(self):
        source = self.sources / "001_CORE_META_MODEL/active.md"
        source.write_text("---\natom_id: CA-R-1\nstatus: Active\nstatus: Active\n---\nInvalid\n", encoding="utf-8")
        runner, calls = self._runner()
        version = (self.root / "version.toml").read_bytes()

        result = run_local_release(self.root, run_id="invalid-source", runner=runner)

        self.assertEqual("failed", result["outcome"])
        self.assertEqual("validate_sources", result["failed_step"])
        self.validation.assert_not_called()
        self.assertFalse(any("unittest" in argv or argv[0] == "docker" for argv in calls))
        self.assertEqual(version, (self.root / "version.toml").read_bytes())
        for target in (self.product, self.installed):
            self.assertEqual("obsolete", (target / "old.txt").read_text())

    def test_unverified_complete_carrier_stops_before_tests_and_delivery(self):
        self.validation.side_effect = ProposedCarrierError("invalid complete carrier")
        runner, calls = self._runner()

        result = run_local_release(self.root, run_id="invalid-carrier", runner=runner)

        self.assertEqual("validate_sources", result["failed_step"])
        self.assertEqual("failed", result["outcome"])
        self.assertEqual(1, self.validation.call_count)
        self.assertFalse(any("unittest" in argv or argv[0] == "docker" for argv in calls))
        for target in (self.product, self.installed):
            self.assertEqual("obsolete", (target / "old.txt").read_text())

    def test_missing_or_duplicate_current_sources_stop_before_tests(self):
        core = self.sources / "001_CORE_META_MODEL/active.md"
        for case in ("missing", "duplicate"):
            with self.subTest(case=case):
                if case == "missing":
                    core.write_text("---\natom_id: CA-R-1\nstatus: Draft\n---\nInactive\n", encoding="utf-8")
                else:
                    core.write_bytes((self.sources / "002_INSTALLED_EXTENSIONS/active.md").read_bytes())
                runner, calls = self._runner()

                result = run_local_release(self.root, run_id=case + "-source", runner=runner)

                self.assertEqual("failed", result["outcome"])
                self.assertEqual("validate_sources", result["failed_step"])
                self.assertFalse(any("unittest" in argv for argv in calls))
                for target in (self.product, self.installed):
                    self.assertEqual("obsolete", (target / "old.txt").read_text())

    def test_installer_refreshes_bootstrap_without_touching_runtime_config_or_state(self):
        runner, calls = self._runner()
        with self._compiler():
            first = run_local_release(self.root, run_id="bootstrap-one", runner=runner)
        self.assertEqual("completed", first["outcome"])
        state = self.runtime / "project_mcp_state.json"
        state.write_text("retain this runtime state\n", encoding="utf-8")
        self.engine_bootstrap.write_bytes(b"#!/usr/bin/env python3\n# refreshed package bootstrap\n")
        self.engine_bootstrap.chmod(0o755)

        with self._compiler():
            second = run_local_release(self.root, run_id="bootstrap-two", runner=runner)

        self.assertEqual("completed", second["outcome"])
        bootstrap = self.runtime / "start_mcp.py"
        self.assertEqual(self.engine_bootstrap.read_bytes(), bootstrap.read_bytes())
        self.assertEqual(0o755, stat.S_IMODE(bootstrap.stat().st_mode))
        self.assertEqual("keep = true\n", (self.runtime / "config.toml").read_text())
        self.assertEqual("retain this runtime state\n", state.read_text())
        self.assertEqual(2, sum(argv[-1:] == ("project-mcp",) for argv in calls))

    def test_four_component_local_version_increments_without_rollover(self):
        (self.root / "version.toml").write_text('[framework]\nversion = "0.4.1.9"\n', encoding="utf-8")
        runner, _ = self._runner()
        with self._compiler():
            result = run_local_release(self.root, run_id="version", runner=runner)
        self.assertEqual("completed", result["outcome"])
        self.assertIn('version = "0.4.1.10"', (self.root / "version.toml").read_text())

    def test_preserved_ds_store_directories_do_not_block_replacement(self):
        retained = (
            self.product / "sources",
            self.product / "sources/001_CORE_META_MODEL",
            self.root / ".caprmedio_install/simple_local_release/package/102_FRAMEWORK_ENGINE",
        )
        for directory in retained:
            directory.mkdir(parents=True, exist_ok=True)
            (directory / ".DS_Store").write_bytes(b"ignored")
            (directory / "obsolete.txt").write_text("old", encoding="utf-8")
        runner, _ = self._runner()
        with self._compiler():
            result = run_local_release(self.root, run_id="ds-store", runner=runner)
        self.assertEqual("completed", result["outcome"])
        for directory in retained:
            self.assertEqual(b"ignored", (directory / ".DS_Store").read_bytes())
            self.assertFalse((directory / "obsolete.txt").exists())
        self.assertTrue((self.product / "sources/001_CORE_META_MODEL/active.md").is_file())

    def test_compiler_failure_stops_before_install_or_docker_and_reports(self):
        runner, calls = self._runner()
        with self._compiler(fail=True):
            result = run_local_release(self.root, run_id="compile-failed", runner=runner)
        self.assertEqual("failed", result["outcome"])
        self.assertIn("compile", result["failed_step"])
        self.assertEqual("obsolete", (self.installed / "old.txt").read_text())
        self.assertFalse(any(argv[0] == "docker" for argv in calls))
        report = self.root / result["report_path"]
        self.assertTrue(report.is_file())
        self.assertIn("compile_product", report.read_text())

    def test_test_failure_leaves_both_methodology_destinations_untouched(self):
        calls = []

        def runner(argv, cwd):
            calls.append(argv)
            if argv == ("git", "diff", "--cached", "--quiet"):
                return subprocess.CompletedProcess(argv, 1, "", "")
            if "unittest" in argv:
                self.assertEqual(3, self.validation.call_count)
                for target in (self.product, self.installed):
                    self.assertEqual("obsolete", (target / "old.txt").read_text())
            return subprocess.CompletedProcess(argv, 2 if "unittest" in argv else 0, "", "test failure")

        result = run_local_release(self.root, run_id="tests-failed", runner=runner)
        self.assertEqual("tests", result["failed_step"])
        self.assertEqual("failed", result["outcome"])
        for target in (self.product, self.installed):
            self.assertEqual("obsolete", (target / "old.txt").read_text())
        self.assertEqual(1, sum("unittest" in argv for argv in calls))
        self.assertEqual(2, sum(argv[:2] == ("git", "commit") for argv in calls))

    def test_git_stages_everything_and_commits_before_steps_and_at_end(self):
        runner, calls = self._runner()
        with self._compiler():
            result = run_local_release(self.root, run_id="git-order", runner=runner)
        self.assertEqual("completed", result["outcome"])
        adds = [index for index, argv in enumerate(calls) if argv[:3] == ("git", "add", "-A")]
        commits = [index for index, argv in enumerate(calls) if argv[:2] == ("git", "commit")]
        self.assertGreaterEqual(len(commits), 7)
        self.assertEqual(len(adds), len(commits))
        for add, commit in zip(adds, commits):
            self.assertEqual(add + 2, commit)
        self.assertEqual(len(calls) - 1, commits[-1])
        self.assertEqual([
            "validate sources", "tests", "copy active sources", "compile product", "copy product to installed framework",
            "build package", "install project runtime", "start mcp", "final",
        ], [calls[index][-1].removeprefix("chore(release): simple local ") for index in commits])

    def test_checkpoints_commit_actual_temporary_git_changes_including_final(self):
        def git(*args):
            return subprocess.run(("git", *args), cwd=self.root, capture_output=True, text=True, check=True)

        git("init", "--quiet")
        git("config", "user.name", "Release fixture")
        git("config", "user.email", "release-fixture@example.invalid")

        def runner(argv, cwd):
            self.assertEqual(self.root, cwd)
            if argv[0] == "git":
                return subprocess.run(argv, cwd=cwd, capture_output=True, text=True, check=False)
            return subprocess.CompletedProcess(argv, 0, "http://localhost:12345/mcp", "")

        with self._compiler():
            result = run_local_release(self.root, run_id="real-git", runner=runner)
        self.assertEqual("completed", result["outcome"])
        self.assertEqual("", git("status", "--porcelain").stdout)
        self.assertEqual("chore(release): simple local final", git("log", "-1", "--format=%s").stdout.strip())
        receipt = ".caprmedio_runtime/simple_local_release/reports/real-git.md"
        self.assertIn("http://localhost:12345/mcp", git("show", f"HEAD:{receipt}").stdout)
        self.assertEqual(7, int(git("rev-list", "--count", "HEAD").stdout))


if __name__ == "__main__":
    unittest.main()
