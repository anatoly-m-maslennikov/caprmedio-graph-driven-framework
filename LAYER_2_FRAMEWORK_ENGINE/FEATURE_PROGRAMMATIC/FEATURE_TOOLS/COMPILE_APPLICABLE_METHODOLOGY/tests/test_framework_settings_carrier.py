from __future__ import annotations

import importlib.util
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
        from scope_declaration_test_support import write_scope_unit_declarations

        temporary = Path.cwd() / ".caprmedio_tmp/framework-settings-carrier-tests"
        temporary.mkdir(parents=True, exist_ok=True)
        self.root = Path(tempfile.mkdtemp(prefix="case-", dir=temporary))
        self.addCleanup(shutil.rmtree, self.root, True)
        self.control = Path(".caprmedio_caprmedio")
        (self.root / compiler.SETTINGS_PATH).parent.mkdir(parents=True, exist_ok=True)
        (self.root / compiler.SETTINGS_PATH).write_text(
            "[project]\nname = \"caprmedio\"\n[paths]\ncontrol_root = \".caprmedio_caprmedio\"\n", encoding="utf-8"
        )
        self.declarations = write_scope_unit_declarations(
            self.root,
            (
                {"scope_unit_name": "METHODOLOGY_SOURCES", "parent": "PROJECT", "scope_unit_type": "Unordered"},
                {"scope_unit_name": "CORE_META_MODEL", "parent": "METHODOLOGY_SOURCES", "scope_unit_type": "Unordered"},
                {"scope_unit_name": "INSTALLED_EXTENSIONS", "parent": "METHODOLOGY_SOURCES", "scope_unit_type": "Unordered"},
                {"scope_unit_name": "PROJECT_CONFIGURATION", "parent": "METHODOLOGY_SOURCES", "scope_unit_type": "Unordered"},
            ),
        )
        self.source = Path(self.declarations["METHODOLOGY_SOURCES"]["authority_path"])
        self.layers = {
            name: Path(self.declarations[name]["authority_path"])
            for name, _, _ in compiler.LAYERS
        }
        for path in self.layers.values():
            path.mkdir(parents=True)

    def write(self, relative: Path, content: str) -> Path:
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
        return path

    def paths(self) -> compiler.MethodologyPaths:
        return compiler.methodology_paths(self.root)

    def test_nondefault_control_root_uses_canonical_instance_and_merges_default(self) -> None:
        self.write(
            self.layers["CORE_META_MODEL"] / compiler.DEFAULT_SETTINGS_NAME,
            "[defaults]\ncolour = \"blue\"\n[extensions.default]\nenabled = true\nrevision = \"v1\"\n",
        )
        canonical = self.write(
            self.control / compiler.INSTANCE_SETTINGS_RELATIVE,
            "[instance]\nlabel = \"custom-control\"\n[extensions.default]\nenabled = true\nrevision = \"v2\"\n",
        )
        legacy = self.write(
            self.layers["PROJECT_CONFIGURATION"] / "caprmedio_framework_settings.toml",
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
        default_dir = self.layers["CORE_META_MODEL"]
        default_dir.rmdir()
        external_dir = self.root / "external-defaults"
        external_dir.mkdir()
        (external_dir / "caprmedio_framework_default_settings.toml").write_text("[defaults]\nvalue = 1\n", encoding="utf-8")
        os.symlink(external_dir, default_dir)
        with self.assertRaises(compiler.CompileError) as symlinked_ancestor:
            compiler.framework_settings(self.root, self.paths())
        self.assertEqual("scope-declarations-invalid", symlinked_ancestor.exception.code)


if __name__ == "__main__":
    unittest.main()
