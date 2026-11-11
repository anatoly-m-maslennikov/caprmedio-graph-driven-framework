"""The concrete Local release flow, without running Docker or installing packages."""

from __future__ import annotations

import subprocess
from contextlib import AbstractContextManager
import io
import json
import shutil
import stat
import sys
import tempfile
from types import ModuleType, SimpleNamespace
import unittest
from unittest.mock import Mock, patch
from pathlib import Path


sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "RELEASE_VERSION"))
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_TOOLS"))
import local_release  # noqa: E402
from local_release import run_local_release, _launcher_image  # noqa: E402
from project_selection import resolve_project  # noqa: E402
from release_support import _release_sources  # noqa: E402
from scope_declaration_test_support import write_scope_unit_declarations  # noqa: E402
from release_registry_test_fixture import (  # noqa: E402
    write_relation_registry_generator,
    write_tool_registry_generator,
    write_workbench_schema_generator,
)


class SimpleLocalReleaseTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory(ignore_cleanup_errors=True)
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name).resolve()
        self.control = self.root / ".caprmedio_caprmedio"
        self.control.mkdir()
        (self.control / "caprmedio_project_settings.toml").write_text(
            '[project]\nname = "caprmedio"\n[paths]\ncontrol_root = ".caprmedio_caprmedio"\n', encoding="utf-8")
        declared = write_scope_unit_declarations(self.root, (
            {"scope_unit_name": "FRAMEWORK_METHODOLOGY", "scope_unit_type": "Unordered"},
            {"scope_unit_name": "METHODOLOGY_SOURCES", "parent": "FRAMEWORK_METHODOLOGY", "scope_unit_type": "Unordered"},
            {"scope_unit_name": "CORE_META_MODEL", "parent": "METHODOLOGY_SOURCES", "scope_unit_type": "Ordered", "scope_unit_label": "001", "local_order": 1},
            {"scope_unit_name": "INSTALLED_EXTENSIONS", "parent": "METHODOLOGY_SOURCES", "scope_unit_type": "Ordered", "scope_unit_label": "002", "local_order": 2},
            {"scope_unit_name": "PROJECT_CONFIGURATION", "parent": "METHODOLOGY_SOURCES", "scope_unit_type": "Ordered", "scope_unit_label": "003", "local_order": 3},
        ), control_root=self.control)
        self.sources = declared["METHODOLOGY_SOURCES"]["authority_path"]
        self.source_units = {name: declared[name]["authority_path"] for name in local_release._SOURCE_UNITS}
        for number, name in enumerate(local_release._SOURCE_UNITS, 1):
            unit = self.source_units[name]
            unit.mkdir(parents=True)
            for status in ("Active", "Draft", "Archived"):
                (unit / f"{status.lower()}.md").write_text(
                    f"---\natom_id: CA-R-{number}\nstatus: {status}\n---\n## Claim\n{status}\n", encoding="utf-8")
            for directory in ("archive", "draft", "_projection"):
                historical = unit / directory / "active.md"
                historical.parent.mkdir()
                historical.write_text("---\nstatus: Active\n---\nold\n", encoding="utf-8")
        (self.root / ".gitignore").write_text(".caprmedio_tmp/\n", encoding="utf-8")
        self.product = self.root / "LAYER_1_FRAMEWORK_METHODOLOGY"
        self.installed = self.control / "000_CAPRMEDIO_framework"
        self.runtime = self.root / ".caprmedio_runtime"
        delivery = self.root / "LAYER_5_FRAMEWORK_DELIVERY/PUBLIC_RELEASE"
        delivery.mkdir(parents=True)
        (delivery / "public_release.py").write_text("# release source\n", encoding="utf-8")
        (delivery / "tests").mkdir()
        (delivery / "tests/test_private.py").write_text("# excluded test\n", encoding="utf-8")
        for destination in (self.product, self.installed, self.runtime):
            destination.mkdir(parents=True)
            (destination / "old.txt").write_text("obsolete", encoding="utf-8")
            (destination / "config.toml").write_text("keep = true\n", encoding="utf-8")
        skill = self.root / "LAYER_2_FRAMEWORK_ENGINE/FEATURE_AGENTIC/FEATURE_SKILLS/ca"
        skill.mkdir(parents=True)
        (skill / "SKILL.md").write_text("ca skill", encoding="utf-8")
        (skill / "references").mkdir()
        (skill / "references/details.md").write_text("skill reference", encoding="utf-8")
        (self.root / "pyproject.toml").write_text("[project]\nname = 'fixture'\n", encoding="utf-8")
        (self.root / "uv.lock").write_text("version = 1\n", encoding="utf-8")
        (self.root / "version.toml").write_text('[framework]\nversion = "0.4.1"\n', encoding="utf-8")
        tools = self.root / "LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_TOOLS"
        tools.mkdir(parents=True)
        bootstrap_helper = (
            Path(__file__).resolve().parents[2]
            / "LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_TOOLS/project_mcp_bootstrap.py"
        )
        (tools / "project_mcp_bootstrap.py").write_bytes(bootstrap_helper.read_bytes())
        (tools / "project_mcp_bootstrap.py").chmod(0o644)
        (tools / "tests").mkdir()
        (tools / "tests/test_retired.py").write_text("# package-excluded test\n", encoding="utf-8")
        (tools / "fixtures").mkdir()
        (tools / "fixtures/input.json").write_text("{}\n", encoding="utf-8")
        (tools / "README.md").write_text("package-excluded prose\n", encoding="utf-8")
        (tools / "scope_declaration_test_support.py").write_text("# package-excluded test helper\n", encoding="utf-8")
        (tools / "scope_declaration_render.py").write_text("# package-excluded test renderer\n", encoding="utf-8")
        skill = tools / "retained/SKILL.md"
        skill.parent.mkdir()
        skill.write_text("retained implementation skill\n", encoding="utf-8")
        subject_builder = tools / "GENERATE_ENTITY_GRAPH/render_entity_tree.py"
        subject_builder.parent.mkdir()
        subject_builder.write_text("# retained subject builder\n", encoding="utf-8")
        prompt = self.root / "LAYER_2_FRAMEWORK_ENGINE/FEATURE_AGENTIC/FEATURE_PROMPTS/retired.py"
        prompt.parent.mkdir(parents=True)
        prompt.write_text("# source-only prompt\n", encoding="utf-8")
        self.engine_bootstrap = (
            self.root / "LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_MCP/"
            "docker/start_mcp.py"
        )
        self.engine_bootstrap.parent.mkdir(parents=True)
        self.engine_bootstrap.write_bytes(b"#!/usr/bin/env python3\n# package bootstrap fixture\n")
        self.engine_bootstrap.chmod(0o755)
        (self.engine_bootstrap.parent / "runtime.py").write_text("# runtime entrypoint fixture\n", encoding="utf-8")
        mcp = self.engine_bootstrap.parent.parent
        (mcp / "tool_providers.json").write_text(
            '{"mcp_blacklist":[],"providers":[]}\n', encoding="utf-8")
        write_tool_registry_generator(mcp)
        workbench_backend = (
            self.root / "LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_APPS/"
            "APP_WORKBENCH/FEATURE_WORKBENCH_BACKEND"
        )
        workbench_backend.mkdir(parents=True)
        write_relation_registry_generator(workbench_backend)
        write_workbench_schema_generator(workbench_backend)
        lifecycle = mcp.parent / "FEATURE_TOOLS/ATOM_LIFECYCLE"
        lifecycle.mkdir()
        (lifecycle / "status_model.py").write_text(
            "from pathlib import Path\n"
            "import sys\n"
            "sources = Path(sys.argv[sys.argv.index('--model-root') + 1])\n"
            "assert sources == Path.cwd() / 'METHODOLOGY/sources'\n"
            f"assert (sources / {self.source_units['CORE_META_MODEL'].name!r} / 'active.md').is_file()\n"
            "output = Path(sys.argv[sys.argv.index('--output') + 1])\n"
            "output.write_text('{\"schema\":1}\\n', encoding='utf-8')\n",
            encoding="utf-8",
        )
        shutil.copy2(lifecycle / "status_model.py", lifecycle / "candidate_schema.py")
        self.image_id = "sha256:" + "a" * 64
        self.image = SimpleNamespace(resolve=Mock(return_value=self.image_id),
                                     identity=Mock(return_value=SimpleNamespace(fingerprint="b" * 64)))
        original_launcher_image = local_release._launcher_image

        def scoped_launcher_image(selection):
            observed = original_launcher_image(selection)
            if observed is not None:
                return observed
            package = self.runtime / "simple_local_release/package"
            return self.image_id if package.is_dir() else None

        launcher = patch("local_release._launcher_image", side_effect=scoped_launcher_image)
        launcher.start()
        self.addCleanup(launcher.stop)
        image_factory = patch("local_release._image_manager", return_value=self.image)
        self.image_factory = image_factory.start()
        self.addCleanup(image_factory.stop)
        provenance = patch("local_release.release_image_provenance", return_value={
            "project_id": "c" * 64, "project_root": str(self.root),
            "control_root": ".caprmedio_caprmedio", "project_name": "Fixture",
            "head_commit": "d" * 40,
        })
        self.provenance = provenance.start()
        self.addCleanup(provenance.stop)

    def _runner(self):
        calls = []

        def run(argv, cwd):
            self.assertEqual(self.root, cwd)
            calls.append(argv)
            if argv == ("git", "diff", "--cached", "--quiet"):
                return subprocess.CompletedProcess(argv, 1, "", "")
            if self._is_mcp_bootstrap(argv):
                return self._mcp_bootstrap_success(argv)
            return subprocess.CompletedProcess(argv, 0, "", "")

        return run, calls

    def _is_mcp_bootstrap(self, argv: tuple[str, ...]) -> bool:
        return (
            len(argv) > 1
            and argv[0] == sys.executable
            and argv[1] == str(self.runtime / "start_mcp.py")
        )

    def _mcp_bootstrap_success(self, argv: tuple[str, ...]) -> subprocess.CompletedProcess[str]:
        launcher_python = self.runtime / "launcher-venv/bin/python"
        launcher_python.parent.mkdir(parents=True, exist_ok=True)
        launcher_python.write_text("#!/usr/bin/env python3\n", encoding="utf-8")
        launcher_python.chmod(0o755)
        return subprocess.CompletedProcess(argv, 0, "http://localhost:12345/mcp\n", "")

    def _compile(self, root):
        self.assertEqual(self.root, root)
        output = self.product / "applicable_methodology"
        output.mkdir(parents=True)
        (output / "compiled.md").write_text("compiled", encoding="utf-8")

    def _compiler(self, *, fail: bool = False) -> AbstractContextManager[object]:
        module = ModuleType("COMPILE_APPLICABLE_METHODOLOGY.compile_applicable_methodology")
        module.CompileError = RuntimeError
        module.MethodologyPaths = SimpleNamespace
        self.canonical_methodology_paths = SimpleNamespace(
            source=Path("relocated/methodology-sources"),
            output=Path("declared/applicable-methodology"),
            declaration_digest="canonical-declaration-digest",
            control_root=Path(".caprmedio_caprmedio"),
        )
        module.methodology_paths = Mock(return_value=self.canonical_methodology_paths)
        self.compile_report_paths = []

        def compile_report(root, paths):
            self.compile_report_paths.append(paths)
            return {"can_apply": not fail}, (), {}

        module.compile_report = compile_report
        module.stage_outputs = lambda *args: None
        module.replace_outputs_atomically = lambda root, staging, paths: self._compile(root)
        return patch.dict(sys.modules, {module.__name__: module})

    def test_compile_product_preserves_canonical_methodology_inputs(self):
        runner, _ = self._runner()
        with self._compiler():
            result = run_local_release(self.root, run_id="canonical-methodology-inputs", runner=runner)

        self.assertEqual("completed", result["outcome"])
        self.assertEqual(1, len(self.compile_report_paths))
        places = self.compile_report_paths[0]
        self.assertEqual(self.canonical_methodology_paths.source, places.source)
        self.assertEqual(self.canonical_methodology_paths.declaration_digest, places.declaration_digest)
        self.assertEqual(self.canonical_methodology_paths.control_root, places.control_root)
        self.assertEqual(Path("LAYER_1_FRAMEWORK_METHODOLOGY/applicable_methodology"), places.output)

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
        protected = ("settings.toml", "project_settings.toml", "caprmedio_framework_settings.toml",
                     "operators_registry.toml", "operator_registry/entry.txt")
        for target in (self.product, self.installed):
            for relative in protected:
                carrier = target / relative
                carrier.parent.mkdir(parents=True, exist_ok=True)
                carrier.write_text(f"preserve {relative}\n")
        core = self.source_units["CORE_META_MODEL"]
        (core / "active.md").chmod(0o640)
        archived = core / "archived/active@1.md"
        archived.parent.mkdir()
        archived.write_bytes((archived.parent.parent / "active.md").read_bytes())
        for directory in ("000_draft", "099_archived"):
            folder = core / "04_requirement" / directory
            folder.mkdir(parents=True)
            (folder / "active.md").write_bytes((core / "active.md").read_bytes())
            (folder / "data.json").write_text("{}\n", encoding="utf-8")
        terminal = core / "04_requirement" / "020_done"
        terminal.mkdir()
        (terminal / "active.md").write_bytes((core / "active.md").read_bytes())
        (terminal / "data.json").write_text("{}\n", encoding="utf-8")
        runner, calls = self._runner()
        with self._compiler():
            result = run_local_release(self.root, run_id="happy", runner=runner)
        self.assertEqual("completed", result["outcome"])
        for target in (self.product, self.installed):
            self.assertFalse((target / "old.txt").exists())
            self.assertEqual("keep = true\n", (target / "config.toml").read_text())
            self.assertTrue((target / "applicable_methodology/compiled.md").is_file())
            for relative in protected:
                self.assertEqual(f"preserve {relative}\n", (target / relative).read_text())
            self.assertEqual(0o640, stat.S_IMODE((target / "SUPERLAYER_1_METHODOLOGY_SOURCES" / core.name / "active.md").stat().st_mode))
            for unit in self.source_units.values():
                released = target / "SUPERLAYER_1_METHODOLOGY_SOURCES" / unit.name
                expected = ["active.md", "active.md"] if unit == core else ["active.md"]
                self.assertEqual(expected, sorted(path.name for path in released.rglob("*.md")))
            self.assertTrue((target / "SUPERLAYER_1_METHODOLOGY_SOURCES" / core.name / "04_requirement/020_done/data.json").is_file())
            for directory in ("000_draft", "099_archived"):
                self.assertFalse((target / "SUPERLAYER_1_METHODOLOGY_SOURCES" / core.name / "04_requirement" / directory).exists())
        self.assertEqual("keep = true\n", (self.runtime / "config.toml").read_text())
        bootstrap = self.runtime / "start_mcp.py"
        self.assertEqual(self.engine_bootstrap.read_bytes(), bootstrap.read_bytes())
        self.assertEqual(0o755, stat.S_IMODE(bootstrap.stat().st_mode))
        for package in (self.runtime / "simple_local_release/package",):
            source_skill = self.root / "LAYER_2_FRAMEWORK_ENGINE/FEATURE_AGENTIC/FEATURE_SKILLS/ca"
            expected_skill = {p.relative_to(source_skill): p.read_bytes() for p in source_skill.rglob("*") if p.is_file()}
            for relative in ("SKILLS/ca", "LAYER_2_FRAMEWORK_ENGINE/FEATURE_AGENTIC/FEATURE_SKILLS/ca"):
                packaged_skill = package / relative
                self.assertEqual(expected_skill, {p.relative_to(packaged_skill): p.read_bytes()
                                                  for p in packaged_skill.rglob("*") if p.is_file()})
            self.assertEqual("# release source\n", (package / "LAYER_5_FRAMEWORK_DELIVERY/PUBLIC_RELEASE/public_release.py").read_text())
            self.assertFalse((package / "LAYER_5_FRAMEWORK_DELIVERY/PUBLIC_RELEASE/tests").exists())
            self.assertTrue((package / "LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/"
                             "FEATURE_TOOLS/GENERATE_ENTITY_GRAPH/render_entity_tree.py").is_file())
            self.assertTrue((package / "LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_APPS/"
                             "APP_WORKBENCH/FEATURE_WORKBENCH_BACKEND/generate_workbench_schema.py").is_file())
            self.assertEqual(
                '{"schema_version":1,"providers":[]}\n',
                (package / "LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_MCP/"
                 "tool_registry.json").read_text(encoding="utf-8"),
            )
            self.assertFalse((package / "LAYER_2_FRAMEWORK_ENGINE/FEATURE_AGENTIC/FEATURE_PROMPTS").exists())
            packaged_tools = package / "LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_TOOLS"
            self.assertEqual(
                '{"schema":1}\n', (packaged_tools / "ATOM_LIFECYCLE/status_model.json").read_text(encoding="utf-8")
            )
            self.assertTrue((packaged_tools / "ATOM_LIFECYCLE/candidate_schema.json").is_file())
            self.assertFalse((packaged_tools / "tests").exists())
            self.assertFalse((packaged_tools / "fixtures").exists())
            self.assertFalse((packaged_tools / "README.md").exists())
            self.assertFalse((packaged_tools / "scope_declaration_test_support.py").exists())
            self.assertFalse((packaged_tools / "scope_declaration_render.py").exists())
            self.assertEqual("retained implementation skill\n", (packaged_tools / "retained/SKILL.md").read_text())
        self.assertEqual("ca skill", (self.root / ".agents/skills/ca/SKILL.md").read_text())
        self.assertIn('version = "0.4.1.1"', (self.root / "version.toml").read_text())
        self.assertIn('version = "0.4.1.1"', (self.runtime / "simple_local_release/package/version.toml").read_text())
        self.assertEqual(1, sum(self._is_mcp_bootstrap(argv) for argv in calls))
        self.assertFalse((self.root / ".caprmedio_install").exists())
        self.assertEqual([], list((self.root / ".caprmedio_tmp/simple_local_release").iterdir()))

    def test_release_sources_accept_nested_and_lowercase_active_status(self):
        core = self.source_units["CORE_META_MODEL"]
        samples = {
            "nested.md": "state:\n  status: Active",
            "lowercase.md": "status: active",
            "nested_lowercase.md": "state:\n  status: active",
            "inactive_nested.md": "state:\n  status: Draft",
            "unknown_case.md": "status: ACTIVE",
            "conflict.md": "status: Active\nstate:\n  status: Draft",
            "invalid.md": "status: Active\nstatus: Archived",
            "missing.md": "atom_id: CA-R-9",
        }
        for name, header in samples.items():
            (core / name).write_text(f"---\n{header}\n---\nbody\n", encoding="utf-8")
        (core / "archive" / "nested.md").write_text("---\nstate:\n  status: Active\n---\nold\n", encoding="utf-8")
        (core / "_projection" / "lowercase.md").write_text("---\nstatus: active\n---\nprojection\n", encoding="utf-8")

        selected = dict((name, files) for name, _, files in _release_sources(self.root))
        self.assertEqual(
            {core / name for name in ("active.md", "nested.md", "lowercase.md", "nested_lowercase.md")},
            set(selected["CORE_META_MODEL"]),
        )
        for name in ("INSTALLED_EXTENSIONS", "PROJECT_CONFIGURATION"):
            self.assertEqual([self.source_units[name] / "active.md"], selected[name])

    def test_active_delivery_does_not_require_atom_metadata_or_relations(self):
        source = self.source_units["CORE_META_MODEL"] / "active.md"
        source.write_text("---\natom_id: not-an-atom-id\nstatus: Active\n---\nNo Claim or relations.\n", encoding="utf-8")
        runner, calls = self._runner()
        with self._compiler():
            result = run_local_release(self.root, run_id="no-atom-gate", runner=runner)
        self.assertEqual("completed", result["outcome"])
        self.assertEqual(1, sum(any(item.endswith("run_full_test_suite.py") for item in argv) for argv in calls))
        for target in (self.product, self.installed):
            self.assertEqual(source.read_bytes(), (target / "SUPERLAYER_1_METHODOLOGY_SOURCES" / source.parent.name / "active.md").read_bytes())

    def test_focused_modules_are_forwarded_and_reported(self):
        modules = (
            "LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_PROJECT_TOOLS/tests/test_one.py",
            "LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_PROJECT_TOOLS/tests/test_two.py",
        )
        runner, calls = self._runner()
        with self._compiler():
            result = run_local_release(
                self.root,
                run_id="focused-forwarding",
                runner=runner,
                test_modules=modules,
            )

        self.assertEqual("completed", result["outcome"])
        self.assertEqual("focused", result["test_scope"])
        self.assertEqual(list(modules), result["test_modules"])
        test_command = next(argv for argv in calls if any(
            item.endswith("run_full_test_suite.py") for item in argv
        ))
        self.assertEqual(
            ("--test-module", modules[0], "--test-module", modules[1]),
            test_command[-4:],
        )
        receipt = (self.root / result["receipt_path"]).read_text(encoding="utf-8")
        self.assertIn("Test scope: `focused`", receipt)
        self.assertIn("Selected test modules: " + ", ".join(modules), receipt)

    def test_focused_test_failure_blocks_downstream_release(self):
        modules = ("LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_PROJECT_TOOLS/tests/test_failing.py",)
        base_runner, calls = self._runner()

        def failed_tests(argv, cwd):
            result = base_runner(argv, cwd)
            if any(item.endswith("run_full_test_suite.py") for item in argv):
                return subprocess.CompletedProcess(
                    argv, 1, "focused tests ran\n", "focused test failure\n"
                )
            return result

        result = run_local_release(
            self.root,
            run_id="focused-failed",
            runner=failed_tests,
            test_modules=modules,
        )

        self.assertEqual(("failed", "tests"), (result["outcome"], result["failed_step"]))
        self.assertEqual("focused", result["test_scope"])
        self.assertEqual(list(modules), result["test_modules"])
        self.assertFalse(any(self._is_mcp_bootstrap(argv) for argv in calls))
        report = (self.root / result["report_path"]).read_text(encoding="utf-8")
        self.assertIn("Test scope: `focused`", report)
        self.assertIn("Selected test modules: " + modules[0], report)
        self.assertIn("focused test failure", report)

    def _assert_input_refused(self, run_id):
        runner, calls = self._runner()
        result = run_local_release(self.root, run_id=run_id, runner=runner)
        self.assertEqual("failed", result["outcome"])
        self.assertEqual("validate_inputs", result["failed_step"])
        for target in (self.product, self.installed):
            self.assertEqual("obsolete", (target / "old.txt").read_text())
        self.assertFalse(any(any(item.endswith("run_full_test_suite.py") for item in argv) for argv in calls))
        self.assertFalse(any(self._is_mcp_bootstrap(argv) for argv in calls))
        self.image_factory.assert_not_called()

    def test_source_symlink_refuses_before_tests_version_or_product_replacement(self):
        outside = self.root / "outside.md"
        outside.write_bytes(b"untrusted payload")
        (self.source_units["CORE_META_MODEL"] / "linked.md").symlink_to(outside)
        self._assert_input_refused("unsafe-source")
        self.assertIn('version = "0.4.1"', (self.root / "version.toml").read_text())
        self.assertEqual(b"untrusted payload", outside.read_bytes())

    def test_missing_source_path_refuses_before_tests_or_replacement(self):
        self.source_units["CORE_META_MODEL"].rename(self.source_units["CORE_META_MODEL"].with_name("missing-core"))
        self._assert_input_refused("missing-source")

    def test_empty_selected_core_refuses_before_tests_version_or_replacement(self):
        (self.source_units["CORE_META_MODEL"] / "active.md").unlink()
        self._assert_input_refused("empty-core")
        self.assertIn('version = "0.4.1"', (self.root / "version.toml").read_text())

    def test_unsafe_product_descendant_refuses_before_any_clear(self):
        (self.product / "linked.txt").symlink_to(self.installed / "old.txt")
        self._assert_input_refused("unsafe-product")

    def test_invalid_version_refuses_before_tests_or_replacement(self):
        version = self.root / "version.toml"
        version.write_text('[framework]\nversion = "invalid"\n')
        self._assert_input_refused("invalid-version")
        self.assertIn('version = "invalid"', version.read_text())

    def test_unsafe_compiler_path_refuses_before_tests_or_replacement(self):
        tools = self.root / "LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_TOOLS"
        moved = tools.with_name("saved_tools")
        tools.rename(moved)
        tools.symlink_to(moved, target_is_directory=True)
        self._assert_input_refused("unsafe-compiler")

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
        self.assertEqual(2, sum(self._is_mcp_bootstrap(argv) for argv in calls))

    def test_four_component_local_version_increments_without_rollover(self):
        (self.root / "version.toml").write_text('[framework]\nversion = "0.4.1.9"\n', encoding="utf-8")
        runner, _ = self._runner()
        with self._compiler():
            result = run_local_release(self.root, run_id="version", runner=runner)
        self.assertEqual("completed", result["outcome"])
        self.assertIn('version = "0.4.1.10"', (self.root / "version.toml").read_text())

    def test_workbench_node_dependencies_are_not_packaged(self):
        frontend = self.root / "LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_APPS/APP_WORKBENCH/FEATURE_WORKBENCH_FRONTEND"
        dependencies = frontend / "node_modules/.bin"
        dependencies.mkdir(parents=True)
        (frontend / "package.json").write_text('{"name":"workbench"}')
        (dependencies / "vite").symlink_to("../vite/bin/vite.js")
        runner, _ = self._runner()
        with self._compiler():
            result = run_local_release(self.root, run_id="frontend-dependencies", runner=runner)
        self.assertEqual("completed", result["outcome"])
        packaged = self.runtime / "simple_local_release/package" / frontend.relative_to(self.root)
        self.assertTrue((packaged / "package.json").is_file())
        self.assertFalse((packaged / "node_modules").exists())

    def test_preserved_ds_store_directories_do_not_block_replacement(self):
        (self.source_units["INSTALLED_EXTENSIONS"] / "active.md").unlink()
        retained = (
            self.product / "SUPERLAYER_1_METHODOLOGY_SOURCES",
            self.product / "SUPERLAYER_1_METHODOLOGY_SOURCES" / self.source_units["CORE_META_MODEL"].name,
            self.installed / "obsolete",
            self.runtime / "simple_local_release/package/LAYER_2_FRAMEWORK_ENGINE",
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
        self.assertTrue((self.product / "SUPERLAYER_1_METHODOLOGY_SOURCES" / self.source_units["CORE_META_MODEL"].name / "active.md").is_file())
        for target in (self.product, self.installed):
            self.assertEqual([], list((target / "SUPERLAYER_1_METHODOLOGY_SOURCES" / self.source_units["INSTALLED_EXTENSIONS"].name).rglob("*.md")))

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
        stdout = "early stdout evidence\n" + "output tail\n" * 500
        stderr = "early failure traceback\n" + "error tail\n" * 500

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
            failed = any(item.endswith("run_full_test_suite.py") for item in argv)
            return subprocess.CompletedProcess(argv, 2 if failed else 0, stdout if failed else "", stderr if failed else "")

        with (
            patch("local_release.cleanup_stopped_containers") as stopped_cleanup,
            patch("local_release.cleanup_obsolete_images") as image_cleanup,
        ):
            result = run_local_release(self.root, run_id="tests-failed", runner=runner)
        self.assertEqual("tests", result["failed_step"])
        self.assertEqual("failed", result["outcome"])
        stopped_cleanup.assert_not_called()
        image_cleanup.assert_not_called()
        for target in (self.product, self.installed):
            self.assertEqual("obsolete", (target / "old.txt").read_text())
        self.assertEqual(1, sum(any(item.endswith("run_full_test_suite.py") for item in argv) for argv in calls))
        self.assertEqual(2, sum(argv[:2] == ("git", "commit") for argv in calls))
        report = (self.root / result["report_path"]).read_text()
        logs = list((self.root / ".caprmedio_tmp/simple_local_release").glob("tests-failed-tests-*.log"))
        self.assertEqual(1, len(logs))
        self.assertIn(f"Complete test output: `{logs[0].relative_to(self.root).as_posix()}`", report)
        self.assertEqual(f"stdout:\n{stdout}\nstderr:\n{stderr}", logs[0].read_text())
        self.assertNotIn("early failure traceback", report)
        with patch("local_release.tempfile.NamedTemporaryFile", side_effect=OSError("unavailable")):
            unsaved = run_local_release(self.root, run_id="tests-log-unavailable", runner=runner)
        self.assertEqual(("failed", "tests"), (unsaved["outcome"], unsaved["failed_step"]))
        self.assertIn("Complete test output could not be saved (OSError)",
                      (self.root / unsaved["report_path"]).read_text())

    def test_default_tests_log_is_retained_on_interrupt_with_actual_failed_step(self):
        runner, calls = self._runner()

        def interrupted(argv, cwd, log):
            self.assertIn("-u", argv)
            self.assertEqual(self.root, cwd)
            log.write(b"partial test evidence\n")
            log.flush()
            raise KeyboardInterrupt

        output = io.StringIO()
        with patch("local_release.subprocess.run", side_effect=lambda argv, **kwargs: runner(argv, kwargs["cwd"])), \
                patch("local_release.run_logged_test_process", side_effect=interrupted), \
                patch("local_release.sys.stderr", output):
            result = run_local_release(self.root, run_id="interrupted")

        self.assertEqual(("failed", "tests", "KeyboardInterrupt"),
                         (result["outcome"], result["failed_step"], result["error_type"]))
        self.assertEqual("partial test evidence\n", (self.root / result["test_log_path"]).read_text())
        report = (self.root / result["report_path"]).read_text()
        self.assertIn("Stopped at: `tests`", report)
        self.assertIn("Error class: `KeyboardInterrupt`", report)
        self.assertIn(result["test_log_path"], report)
        self.assertIn("Local release phase START: tests", output.getvalue())
        self.assertIn(result["test_log_path"], output.getvalue())
        for target in (self.product, self.installed):
            self.assertEqual("obsolete", (target / "old.txt").read_text())
        self.assertFalse(any(self._is_mcp_bootstrap(argv) for argv in calls))

    def test_default_test_log_survives_later_failure_without_whole_output_capture(self):
        runner, _ = self._runner()

        def passed(argv, cwd, log):
            log.write(b"complete test evidence\n")
            return subprocess.CompletedProcess(argv, 0, "bounded tail", "")

        with patch("local_release.subprocess.run", side_effect=lambda argv, **kwargs: runner(argv, kwargs["cwd"])), \
                patch("local_release.run_logged_test_process", side_effect=passed), self._compiler(fail=True):
            result = run_local_release(self.root, run_id="later-failed")

        self.assertEqual(("failed", "compile_product"), (result["outcome"], result["failed_step"]))
        self.assertEqual("complete test evidence\n", (self.root / result["test_log_path"]).read_text())
        self.assertIn(result["test_log_path"], (self.root / result["report_path"]).read_text())

    def test_interrupt_before_tests_reports_actual_git_step_without_claiming_log(self):
        def interrupted(argv, cwd):
            raise KeyboardInterrupt

        result = run_local_release(self.root, run_id="git-interrupted", runner=interrupted)
        self.assertEqual(("failed", "git_before_validate_inputs", "KeyboardInterrupt"),
                         (result["outcome"], result["failed_step"], result["error_type"]))
        self.assertIsNone(result["test_log_path"])
        self.assertIn("git_before_validate_inputs", (self.root / result["report_path"]).read_text())

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
        self.assertEqual(len(calls) - 2, commits[-1])
        self.assertEqual([
            "validate inputs", "tests", "copy active sources", "compile product", "build package", "prepare candidate image",
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
            if self._is_mcp_bootstrap(argv):
                return self._mcp_bootstrap_success(argv)
            if argv[0] == "docker":
                return subprocess.CompletedProcess(argv, 0, "", "")
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
        for relative in ("uv.lock", "LAYER_2_FRAMEWORK_ENGINE/FEATURE_AGENTIC/FEATURE_SKILLS/ca/SKILL.md",
                         "LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_MCP/docker/runtime.py"):
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
                self.assertFalse(any(self._is_mcp_bootstrap(argv) for argv in calls))
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
        blocked = self.root / "LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_TOOLS/blocked"
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
        self.assertFalse(any(self._is_mcp_bootstrap(argv) for argv in calls))

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
        events = []

        def resolve(**kwargs):
            events.append("candidate-resolve" if not kwargs else "installed-resolve")
            if not kwargs:
                self.assertEqual("obsolete", (self.installed / "old.txt").read_text())
                self.assertFalse((self.runtime / "simple_local_release/package").exists())
                self.assertFalse((self.root / ".agents/skills/ca").exists())
            else:
                self.assertEqual({"explicit_id": self.image_id, "build_if_missing": False}, kwargs)
            return self.image_id
        self.image.resolve.side_effect = resolve
        runner, calls = self._runner()

        def record(argv, cwd):
            result = runner(argv, cwd)
            if any(item.endswith("run_full_test_suite.py") for item in argv):
                events.append("full-suite-green")
            elif self._is_mcp_bootstrap(argv):
                events.append("launch")
            elif argv[:3] == ("docker", "image", "ls"):
                events.append("post-smoke-image-cleanup")
            return result

        with self._compiler():
            result = run_local_release(self.root, run_id="image-order", runner=record)
        self.assertEqual("completed", result["outcome"])
        self.assertEqual(2, self.image_factory.call_count)
        self.assertEqual([unittest.mock.call(), unittest.mock.call(use_packaged_assets=True),
                          unittest.mock.call(use_packaged_assets=True)], self.image.identity.call_args_list)
        source, temporary = self.image_factory.call_args_list[0].args
        self.assertTrue(source.is_relative_to(self.root / ".caprmedio_tmp/simple_local_release"))
        self.assertEqual(source.parent / "image_builds", temporary)
        self.assertEqual(self.runtime / "simple_local_release/package", self.image_factory.call_args_list[1].args[0])
        launch = next(argv for argv in calls if self._is_mcp_bootstrap(argv))
        self.assertEqual((sys.executable, str(self.runtime / "start_mcp.py")), launch[:2])
        self.assertEqual(str(self.runtime / "simple_local_release/package"), launch[launch.index("--source-root") + 1])
        self.assertNotIn("--image", launch)
        self.assertIn("--no-build", launch)
        self.assertLess(events.index("full-suite-green"), events.index("candidate-resolve"))
        self.assertLess(events.index("candidate-resolve"), events.index("installed-resolve"))
        self.assertLess(events.index("installed-resolve"), events.index("launch"))
        self.assertLess(events.index("launch"), events.index("post-smoke-image-cleanup"))

    def test_image_preparation_failure_preserves_previous_installation(self):
        runtime_package = self.runtime / "simple_local_release/package"
        skill = self.root / ".agents/skills/ca"
        for target in (runtime_package, skill):
            target.mkdir(parents=True)
            (target / "old.txt").write_bytes(b"previous payload")
        self.image.resolve.side_effect = RuntimeError("image unavailable")
        runner, calls = self._runner()
        with (
            self._compiler(),
            patch("local_release.cleanup_stopped_containers") as stopped_cleanup,
            patch("local_release.cleanup_obsolete_images") as image_cleanup,
        ):
            result = run_local_release(self.root, run_id="image-failed", runner=runner)
        self.assertEqual("failed", result["outcome"])
        self.assertEqual("prepare_candidate_image", result["failed_step"])
        stopped_cleanup.assert_not_called()
        image_cleanup.assert_not_called()
        self.assertEqual("obsolete", (self.installed / "old.txt").read_text())
        self.assertEqual(b"previous payload", (runtime_package / "old.txt").read_bytes())
        self.assertEqual(b"previous payload", (skill / "old.txt").read_bytes())
        self.assertFalse(any(self._is_mcp_bootstrap(argv) for argv in calls))

    def test_packaged_fingerprint_mismatch_preserves_previous_installation(self):
        runtime_package = self.runtime / "simple_local_release/package"
        runtime_package.mkdir(parents=True)
        (runtime_package / "old.txt").write_bytes(b"previous payload")
        self.image.identity.side_effect = [SimpleNamespace(fingerprint="b" * 64),
                                           SimpleNamespace(fingerprint="c" * 64)]
        runner, calls = self._runner()
        with self._compiler():
            result = run_local_release(self.root, run_id="package-mismatch", runner=runner)
        self.assertEqual("failed", result["outcome"])
        self.assertEqual("prepare_candidate_image", result["failed_step"])
        self.assertEqual("obsolete", (self.installed / "old.txt").read_text())
        self.assertEqual(b"previous payload", (runtime_package / "old.txt").read_bytes())
        self.assertFalse(any(self._is_mcp_bootstrap(argv) for argv in calls))


if __name__ == "__main__":
    unittest.main()
