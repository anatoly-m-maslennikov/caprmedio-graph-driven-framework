"""The concrete Local release flow, without running Docker or installing packages."""

from __future__ import annotations

import subprocess
import json
import stat
import sys
import tempfile
from types import ModuleType, SimpleNamespace
import unittest
from unittest.mock import Mock, patch
from pathlib import Path


sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "RELEASE_VERSION"))
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS"))
from local_release import run_local_release, _launcher_image  # noqa: E402
from project_selection import resolve_project  # noqa: E402


class SimpleLocalReleaseTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory(ignore_cleanup_errors=True)
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name).resolve()
        self.control = self.root / ".caprmedio_caprmedio"
        self.sources = self.control / "101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES"
        rows = ["schema_version = 1", ""]
        for number, name in enumerate(("CORE_META_MODEL", "INSTALLED_EXTENSIONS", "PROJECT_CONFIGURATION"), 1):
            unit = self.sources / f"{number:03d}_{name}"
            unit.mkdir(parents=True)
            rows.extend(("[[scope_units]]", f'scope_unit_name = "{name}"',
                         f'authority_path = "{unit.relative_to(self.root).as_posix()}"',
                         f'delivery_path = "101_FRAMEWORK_METHODOLOGY/sources/{unit.name}"', ""))
            for status in ("Active", "Draft", "Archived"):
                (unit / f"{status.lower()}.md").write_text(
                    f"---\natom_id: CA-R-{number}\nstatus: {status}\n---\n## Claim\n{status}\n", encoding="utf-8")
            historical = unit / "archive/active.md"
            historical.parent.mkdir()
            historical.write_text("---\nstatus: Active\n---\nold\n", encoding="utf-8")
        (self.control / "project_structure.toml").write_text("\n".join(rows), encoding="utf-8")
        (self.control / "caprmedio_project_settings.toml").write_text(
            '[project]\nname = "caprmedio"\n[paths]\ncontrol_root = ".caprmedio_caprmedio"\n', encoding="utf-8")
        (self.root / ".gitignore").write_text(".caprmedio_tmp/\n", encoding="utf-8")
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
        (self.engine_bootstrap.parent / "runtime.py").write_text("# runtime entrypoint fixture\n", encoding="utf-8")
        self.image_id = "sha256:" + "a" * 64
        self.image = SimpleNamespace(resolve=Mock(return_value=self.image_id),
                                     identity=lambda: SimpleNamespace(fingerprint="b" * 64))
        image_factory = patch("local_release._image_manager", return_value=self.image)
        self.image_factory = image_factory.start()
        self.addCleanup(image_factory.stop)

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

    def test_launcher_image_reads_only_exact_selected_runtime_namespace(self):
        selection = resolve_project(self.root)
        old_image = "sha256:" + "c" * 64
        payload = {"project_root": str(self.root), "control_root": str(self.control),
                   "project_id": selection.instance_id, "image_id": old_image}
        legacy = self.root / ".caprmedio_install/project_mcp" / selection.instance_id / "last_launch.json"
        legacy.parent.mkdir(parents=True)
        legacy.write_text(json.dumps(payload), encoding="utf-8")
        retained = legacy.read_bytes()
        sibling = selection.launcher_state.parent / ("d" * 64) / "last_launch.json"
        sibling.parent.mkdir(parents=True)
        sibling.write_text(json.dumps(payload), encoding="utf-8")
        self.assertIsNone(_launcher_image(selection))
        current = selection.launcher_state / "last_launch.json"
        current.parent.mkdir(parents=True)
        current.write_text(json.dumps(payload), encoding="utf-8")
        self.assertEqual(old_image, _launcher_image(selection))
        payload["project_id"] = "d" * 64
        current.write_text(json.dumps(payload), encoding="utf-8")
        self.assertIsNone(_launcher_image(selection))
        current.unlink()
        current.symlink_to(legacy)
        self.assertIsNone(_launcher_image(selection))
        self.assertEqual(retained, legacy.read_bytes())

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
        for package in (self.runtime / "simple_local_release/package",):
            self.assertEqual("ca skill", (package / "SKILLS/ca/SKILL.md").read_text())
            self.assertTrue((package / "102_FRAMEWORK_ENGINE/202_AGENTIC/205_SKILLS/ca/SKILL.md").is_file())
        self.assertEqual("ca skill", (self.root / ".agents/skills/ca/SKILL.md").read_text())
        self.assertIn('version = "0.4.1.1"', (self.root / "version.toml").read_text())
        self.assertIn('version = "0.4.1.1"', (self.runtime / "simple_local_release/package/version.toml").read_text())
        self.assertEqual(1, sum(argv[-1:] == ("project-mcp",) for argv in calls))
        self.assertFalse((self.root / ".caprmedio_install").exists())
        self.assertEqual([], list((self.root / ".caprmedio_tmp/simple_local_release").iterdir()))

    def test_active_delivery_does_not_require_atom_metadata_or_relations(self):
        source = self.sources / "001_CORE_META_MODEL/active.md"
        source.write_text("---\natom_id: not-an-atom-id\nstatus: Active\n---\nNo Claim or relations.\n", encoding="utf-8")
        runner, calls = self._runner()
        with self._compiler():
            result = run_local_release(self.root, run_id="no-atom-gate", runner=runner)
        self.assertEqual("completed", result["outcome"])
        self.assertEqual(1, sum(any(item.endswith("run_full_test_suite.py") for item in argv) for argv in calls))
        for target in (self.product, self.installed):
            self.assertEqual(source.read_bytes(), (target / "sources/001_CORE_META_MODEL/active.md").read_bytes())

    def test_source_symlink_still_refuses_before_installed_replacement(self):
        outside = self.root / "outside.md"
        outside.write_bytes(b"untrusted payload")
        (self.sources / "001_CORE_META_MODEL/linked.md").symlink_to(outside)
        runner, calls = self._runner()
        result = run_local_release(self.root, run_id="unsafe-source", runner=runner)
        self.assertEqual("failed", result["outcome"])
        self.assertEqual("copy_active_sources", result["failed_step"])
        self.assertEqual("obsolete", (self.installed / "old.txt").read_text())
        self.image_factory.assert_not_called()
        self.assertFalse(any(argv[-1:] == ("project-mcp",) for argv in calls))
        self.assertEqual(b"untrusted payload", outside.read_bytes())

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
            self.runtime / "simple_local_release/package/102_FRAMEWORK_ENGINE",
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
            if any(item.endswith("run_full_test_suite.py") for item in argv):
                self.assertIn("--all-groups", argv)
                self.assertIn("--managed-python", argv)
                self.assertIn("3.14", argv)
                self.assertEqual(str(self.root), argv[argv.index("--project-root") + 1])
                for target in (self.product, self.installed):
                    self.assertEqual("obsolete", (target / "old.txt").read_text())
            return subprocess.CompletedProcess(argv, 2 if any(item.endswith("run_full_test_suite.py") for item in argv) else 0, "", "test failure")

        result = run_local_release(self.root, run_id="tests-failed", runner=runner)
        self.assertEqual("tests", result["failed_step"])
        self.assertEqual("failed", result["outcome"])
        for target in (self.product, self.installed):
            self.assertEqual("obsolete", (target / "old.txt").read_text())
        self.assertEqual(1, sum(any(item.endswith("run_full_test_suite.py") for item in argv) for argv in calls))
        self.assertEqual(1, sum(argv[:2] == ("git", "commit") for argv in calls))
        self.assertIn("test failure", (self.root / result["report_path"]).read_text())

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
            "tests", "copy active sources", "compile product", "build package", "prepare candidate image",
            "copy product to installed framework", "install project runtime", "start mcp", "final",
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
        self.assertEqual(6, int(git("rev-list", "--count", "HEAD").stdout))

    def test_package_inputs_fail_before_any_installed_replacement(self):
        runtime_package = self.runtime / "simple_local_release/package"
        skill = self.root / ".agents/skills/ca"
        for target in (runtime_package, skill):
            target.mkdir(parents=True)
            (target / "old.txt").write_text("prior payload", encoding="utf-8")
            (target / "old.txt").chmod(0o640)
        def inventory(target):
            return {path.relative_to(target).as_posix(): (path.read_bytes(), stat.S_IMODE(path.stat().st_mode))
                    for path in target.rglob("*") if path.is_file()}
        before = {target: inventory(target) for target in (self.installed, runtime_package, skill)}
        for relative in ("uv.lock", "102_FRAMEWORK_ENGINE/202_AGENTIC/205_SKILLS/ca/SKILL.md",
                         "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/WORKFLOW_ORCHESTRATOR/docker/runtime.py"):
            with self.subTest(relative=relative):
                missing = self.root / relative
                payload = missing.read_bytes()
                mode = stat.S_IMODE(missing.stat().st_mode)
                missing.unlink()
                runner, calls = self._runner()
                with self._compiler():
                    result = run_local_release(self.root, run_id="missing-input", runner=runner)
                missing.write_bytes(payload)
                missing.chmod(mode)
                self.assertEqual("failed", result["outcome"])
                self.assertEqual("build_package", result["failed_step"])
                self.assertFalse(any(argv[-1:] == ("project-mcp",) for argv in calls))
                for target, snapshot in before.items():
                    self.assertEqual(snapshot, inventory(target))
                self.assertEqual([], list((self.root / ".caprmedio_tmp/simple_local_release").iterdir()))

    def test_package_byte_or_mode_drift_refuses_before_installed_clear(self):
        import local_release
        prepare = local_release._prepare_package
        for field in ("bytes", "mode"):
            with self.subTest(field=field):
                def tamper(*args):
                    expected = prepare(*args)
                    path = args[2] / "uv.lock"
                    if field == "bytes":
                        path.write_bytes(path.read_bytes() + b"drift")
                    else:
                        path.chmod(0o600 if stat.S_IMODE(path.stat().st_mode) != 0o600 else 0o644)
                    return expected
                runner, _ = self._runner()
                with self._compiler(), patch.object(local_release, "_prepare_package", tamper):
                    result = run_local_release(self.root, run_id="tampered-package", runner=runner)
                self.assertEqual("failed", result["outcome"])
                self.assertEqual("prepare_candidate_image", result["failed_step"])
                self.image_factory.assert_not_called()
                self.assertEqual("obsolete", (self.installed / "old.txt").read_text())

    def test_unreadable_package_subtree_refuses_before_replacement(self):
        blocked = self.root / "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/blocked"
        blocked.mkdir()
        (blocked / "required.py").write_bytes(b"required payload")
        runtime_package = self.runtime / "simple_local_release/package"
        skill = self.root / ".agents/skills/ca"
        for target in (runtime_package, skill):
            target.mkdir(parents=True)
            (target / "old.txt").write_bytes(b"previous payload")
        runner, calls = self._runner()
        blocked.chmod(0)
        try:
            with self._compiler():
                result = run_local_release(self.root, run_id="unreadable-package", runner=runner)
        finally:
            blocked.chmod(0o700)
        self.assertEqual("failed", result["outcome"])
        self.assertEqual("build_package", result["failed_step"])
        self.image_factory.assert_not_called()
        self.assertEqual("obsolete", (self.installed / "old.txt").read_text())
        for target in (runtime_package, skill):
            self.assertEqual(b"previous payload", (target / "old.txt").read_bytes())
        self.assertFalse(any(argv[-1:] == ("project-mcp",) for argv in calls))

    def test_staging_is_run_private_and_verified_before_replacement(self):
        import local_release
        prepare = local_release._prepare_package
        stages = []
        def capture(root, product, package):
            self.assertTrue(package.is_relative_to(root / ".caprmedio_tmp/simple_local_release"))
            self.assertTrue(package.parent.name.startswith("private-"))
            self.assertEqual("obsolete", (self.installed / "old.txt").read_text())
            stages.append(package)
            return prepare(root, product, package)
        runner, _ = self._runner()
        with self._compiler(), patch.object(local_release, "_prepare_package", capture):
            result = run_local_release(self.root, run_id="private", runner=runner)
        self.assertEqual("completed", result["outcome"])
        self.assertEqual(1, len(stages))
        self.assertFalse(stages[0].exists())
        self.assertFalse((self.root / ".caprmedio_install").exists())

    def test_image_is_verified_before_replacement_and_installed_launch_cannot_build(self):
        def resolve(**kwargs):
            if not kwargs:
                self.assertEqual("obsolete", (self.installed / "old.txt").read_text())
                self.assertFalse((self.runtime / "simple_local_release/package").exists())
                self.assertFalse((self.root / ".agents/skills/ca").exists())
            else:
                self.assertEqual({"explicit_id": self.image_id, "build_if_missing": False}, kwargs)
            return self.image_id
        self.image.resolve.side_effect = resolve
        runner, calls = self._runner()
        with self._compiler():
            result = run_local_release(self.root, run_id="image-order", runner=runner)
        self.assertEqual("completed", result["outcome"])
        self.assertEqual(2, self.image_factory.call_count)
        source, temporary = self.image_factory.call_args_list[0].args
        self.assertTrue(source.is_relative_to(self.root / ".caprmedio_tmp/simple_local_release"))
        self.assertEqual(source.parent / "image_builds", temporary)
        self.assertEqual(self.runtime / "simple_local_release/package", self.image_factory.call_args_list[1].args[0])
        launch = next(argv for argv in calls if argv[-1:] == ("project-mcp",))
        self.assertEqual(self.image_id, launch[launch.index("--image") + 1])
        self.assertIn("--no-build", launch)

    def test_image_preparation_failure_preserves_previous_installation(self):
        runtime_package = self.runtime / "simple_local_release/package"
        skill = self.root / ".agents/skills/ca"
        for target in (runtime_package, skill):
            target.mkdir(parents=True)
            (target / "old.txt").write_bytes(b"previous payload")
        self.image.resolve.side_effect = RuntimeError("image unavailable")
        runner, calls = self._runner()
        with self._compiler():
            result = run_local_release(self.root, run_id="image-failed", runner=runner)
        self.assertEqual("failed", result["outcome"])
        self.assertEqual("prepare_candidate_image", result["failed_step"])
        self.assertEqual("obsolete", (self.installed / "old.txt").read_text())
        self.assertEqual(b"previous payload", (runtime_package / "old.txt").read_bytes())
        self.assertEqual(b"previous payload", (skill / "old.txt").read_bytes())
        self.assertFalse(any(argv[-1:] == ("project-mcp",) for argv in calls))


if __name__ == "__main__":
    unittest.main()
