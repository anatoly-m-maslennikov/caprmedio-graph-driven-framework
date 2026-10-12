from __future__ import annotations

import importlib.util
import json
import os
import shutil
import sys
import tempfile
import unittest
from pathlib import Path


TOOL = Path(__file__).resolve().parents[1] / "compile_applicable_methodology.py"
SPEC = importlib.util.spec_from_file_location("compile_applicable_methodology_settings", TOOL)
assert SPEC and SPEC.loader
compiler = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = compiler
SPEC.loader.exec_module(compiler)


class FrameworkSettingsCarrierTest(unittest.TestCase):
    def setUp(self) -> None:
        temporary = Path.cwd() / ".caprmedio_tmp/framework-settings-carrier-tests"
        temporary.mkdir(parents=True, exist_ok=True)
        self.root = Path(tempfile.mkdtemp(prefix="case-", dir=temporary))
        self.addCleanup(shutil.rmtree, self.root, True)
        self.control = Path(".project-control")
        self.source = self.control / "000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources"
        (self.root / self.source).mkdir(parents=True)
        (self.root / compiler.SETTINGS_PATH).parent.mkdir(parents=True, exist_ok=True)
        (self.root / compiler.SETTINGS_PATH).write_text(
            "[paths]\ncontrol_root = \".project-control\"\n", encoding="utf-8"
        )
        (self.root / self.control / "project_structure.toml").write_text(
            "[[scope_units]]\n"
            "scope_unit_name = \"METHODOLOGY_SOURCES\"\n"
            f"authority_path = {json.dumps(self.source.as_posix())}\n"
            f"delivery_path = {json.dumps((self.control / '000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY').as_posix())}\n",
            encoding="utf-8",
        )

    def write(self, relative: Path, content: str) -> Path:
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
        return path

    def paths(self) -> compiler.MethodologyPaths:
        return compiler.methodology_paths(self.root)

    def test_nondefault_control_root_uses_canonical_instance_and_merges_default(self) -> None:
        self.write(
            self.source / compiler.DEFAULT_SETTINGS_RELATIVE,
            "[defaults]\ncolour = \"blue\"\n[extensions.default]\nenabled = true\nrevision = \"v1\"\n",
        )
        canonical = self.write(
            self.control / compiler.INSTANCE_SETTINGS_RELATIVE,
            "[instance]\nlabel = \"custom-control\"\n[extensions.default]\nenabled = true\nrevision = \"v2\"\n",
        )
        legacy = self.write(
            self.source / "003_PROJECT_CONFIGURATION/caprmedio_framework_settings.toml",
            "[extensions.default]\nenabled = true\nrevision = \"legacy\"\n",
        )

        settings, bindings = compiler.framework_settings(self.root, self.paths())

        self.assertEqual("blue", settings["defaults"]["colour"])
        self.assertEqual("custom-control", settings["instance"]["label"])
        self.assertEqual({"default": "v2"}, compiler.extension_selections(settings))
        self.assertIn(canonical.relative_to(self.root).as_posix(), bindings)
        self.assertNotIn(legacy.relative_to(self.root).as_posix(), bindings)

    def test_canonical_instance_addition_mutation_and_removal_change_source_snapshot(self) -> None:
        places = self.paths()
        absent = compiler.source_state_snapshot(self.root, places)
        canonical = self.write(self.control / compiler.INSTANCE_SETTINGS_RELATIVE, "[instance]\nvalue = 1\n")
        added = compiler.source_state_snapshot(self.root, places)
        self.assertNotEqual(absent, added)
        self.assertIn(canonical.relative_to(self.root).as_posix(), added)

        canonical.write_text("[instance]\nvalue = 2\n", encoding="utf-8")
        mutated = compiler.source_state_snapshot(self.root, places)
        self.assertNotEqual(added, mutated)

        canonical.unlink()
        self.assertEqual(absent, compiler.source_state_snapshot(self.root, places))

    def test_nondefault_control_project_settings_addition_mutation_and_removal_change_snapshot(self) -> None:
        places = self.paths()
        absent = compiler.source_state_snapshot(self.root, places)
        actual = self.root / self.control / "caprmedio_project_settings.toml"
        actual.write_text("[runtime]\nvalue = 1\n", encoding="utf-8")
        added = compiler.source_state_snapshot(self.root, places)
        self.assertNotEqual(absent, added)
        self.assertIn(actual.relative_to(self.root).as_posix(), added)

        actual.write_text("[runtime]\nvalue = 2\n", encoding="utf-8")
        self.assertNotEqual(added, compiler.source_state_snapshot(self.root, places))

        actual.unlink()
        self.assertEqual(absent, compiler.source_state_snapshot(self.root, places))

    def test_symlinked_canonical_carrier_or_ancestor_is_refused(self) -> None:
        canonical = self.root / self.control / compiler.INSTANCE_SETTINGS_RELATIVE
        canonical.parent.mkdir(parents=True, exist_ok=True)
        target = self.root / "settings-target.toml"
        target.write_text("[instance]\nvalue = 1\n", encoding="utf-8")
        os.symlink(target, canonical)
        with self.assertRaises(compiler.CompileError) as symlinked_file:
            compiler.framework_settings(self.root, self.paths())
        self.assertEqual("framework-settings-invalid", symlinked_file.exception.code)

        canonical.unlink()
        default_dir = self.root / self.source / "001_CORE_META_MODEL"
        external_dir = self.root / "external-defaults"
        external_dir.mkdir()
        (external_dir / "caprmedio_framework_default_settings.toml").write_text("[defaults]\nvalue = 1\n", encoding="utf-8")
        os.symlink(external_dir, default_dir)
        with self.assertRaises(compiler.CompileError) as symlinked_ancestor:
            compiler.framework_settings(self.root, self.paths())
        self.assertEqual("framework-settings-invalid", symlinked_ancestor.exception.code)


if __name__ == "__main__":
    unittest.main()
