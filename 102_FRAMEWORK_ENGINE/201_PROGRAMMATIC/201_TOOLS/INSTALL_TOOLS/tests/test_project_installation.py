"""Functional checks for the bounded Project-only installer."""

from __future__ import annotations

import os
from pathlib import Path
import shutil
import sys
import tempfile
import tomllib
import unittest
from unittest.mock import patch

TOOLS_ROOT = Path(__file__).resolve().parents[2]
if str(TOOLS_ROOT) not in sys.path:
    sys.path.insert(0, str(TOOLS_ROOT))

from INSTALL_TOOLS.project_installation import (  # noqa: E402
    ProjectInstallationError,
    _apply,
    _plan,
    install_project,
)
from INSTALL_TOOLS.host_installation_io import FileUpdate, HostInstallationError  # noqa: E402
from project_selection import resolve_project  # noqa: E402
from technical_diagnostics import _project_prefix  # noqa: E402


TEST_TEMP_ROOT = Path.cwd() / ".caprmedio_tmp" / "tests" / Path(__file__).stem
TEST_TEMP_ROOT.mkdir(parents=True, exist_ok=True)
CANONICAL = Path(__file__).resolve().parents[5] / "102_FRAMEWORK_ENGINE/202_AGENTIC/205_SKILLS/ca"


class ProjectInstallationTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory(dir=TEST_TEMP_ROOT, delete=False)
        base = Path(self.temporary.name)
        self.project = base / "demo"
        self.project.mkdir()
        self.source = base / "source"
        skill = self.source / "102_FRAMEWORK_ENGINE/202_AGENTIC/205_SKILLS/ca"
        skill.mkdir(parents=True)
        shutil.copy2(CANONICAL / "SKILL.md", skill / "SKILL.md")
        (skill / "agents").mkdir()
        shutil.copy2(CANONICAL / "agents/openai.yaml", skill / "agents/openai.yaml")
        self.global_config = base / "codex-home/config.json"
        self.global_config.parent.mkdir()
        self.global_config.write_text('{"untouched": true}\n', encoding="utf-8")
        self.old_codex_home = os.environ.get("CODEX_HOME")
        os.environ["CODEX_HOME"] = str(self.global_config.parent)

    def tearDown(self) -> None:
        if self.old_codex_home is None:
            os.environ.pop("CODEX_HOME", None)
        else:
            os.environ["CODEX_HOME"] = self.old_codex_home
        self.temporary.cleanup()

    @staticmethod
    def _inventory(root: Path) -> dict[str, bytes | None]:
        result: dict[str, bytes | None] = {}
        for path in sorted(root.rglob("*")):
            relative = path.relative_to(root).as_posix()
            result[relative] = None if path.is_dir() else path.read_bytes()
        return result

    def test_fresh_seed_dry_run_apply_and_resolve_prefix(self) -> None:
        before = self._inventory(self.project)
        preview = install_project(self.project, prefix="APP", source_root=self.source)
        self.assertEqual("dry_run", preview["mode"])
        self.assertEqual(before, self._inventory(self.project))
        self.assertFalse((self.project / ".caprmedio_demo").exists())

        result = install_project(self.project, prefix="APP", apply=True, source_root=self.source)
        selection = resolve_project(self.project)
        self.assertEqual("APP", _project_prefix(selection.settings))
        self.assertFalse(result["no_op"])
        self.assertEqual(
            {"schema_version": 1, "scope_units": []},
            tomllib.loads((self.project / ".caprmedio_demo/project_structure.toml").read_text()),
        )
        self.assertTrue((self.project / ".caprmedio_demo/_journal").is_dir())
        self.assertTrue((self.project / ".caprmedio_demo/_projection").is_dir())
        self.assertEqual(
            (self.source / "102_FRAMEWORK_ENGINE/202_AGENTIC/205_SKILLS/ca/SKILL.md").read_bytes(),
            (self.project / ".agents/skills/ca/SKILL.md").read_bytes(),
        )

    def test_repeat_is_no_op_and_preserves_unrelated_files_and_global_config(self) -> None:
        install_project(self.project, prefix="APP", apply=True, source_root=self.source)
        unrelated = self.project / "README.md"
        unrelated.write_text("keep\n", encoding="utf-8")
        global_before = self.global_config.read_bytes()
        second = install_project(self.project, apply=True, source_root=self.source)
        self.assertTrue(second["no_op"])
        self.assertEqual([], second["changed"])
        self.assertEqual(b"keep\n", unrelated.read_bytes())
        self.assertEqual(global_before, self.global_config.read_bytes())

    def test_fresh_name_with_spaces_is_preserved(self) -> None:
        project = self.project.parent / "Friendly Demo"
        project.mkdir()
        install_project(project, prefix="APP", apply=True, source_root=self.source)
        settings = tomllib.loads(
            (project / ".caprmedio_Friendly Demo/caprmedio_project_settings.toml").read_text()
        )
        self.assertEqual("Friendly Demo", settings["project"]["name"])
        self.assertEqual("Friendly Demo", resolve_project(project).settings["project"]["name"])

    def test_existing_prefix_mismatch_refuses_before_mutation(self) -> None:
        install_project(self.project, prefix="APP", apply=True, source_root=self.source)
        before = self._inventory(self.project)
        with self.assertRaisesRegex(ProjectInstallationError, "requested prefix"):
            install_project(self.project, prefix="OTHER", apply=True, source_root=self.source)
        self.assertEqual(before, self._inventory(self.project))

    def test_custom_skill_conflict_happens_before_project_writes(self) -> None:
        carrier = self.project / ".agents/skills/ca/SKILL.md"
        carrier.parent.mkdir(parents=True)
        carrier.write_text("custom\n", encoding="utf-8")
        before = self._inventory(self.project)
        with self.assertRaisesRegex(ProjectInstallationError, "differs"):
            install_project(self.project, prefix="APP", apply=True, source_root=self.source)
        self.assertEqual(before, self._inventory(self.project))
        self.assertFalse((self.project / ".caprmedio_demo").exists())

    def test_apply_rejects_created_target_after_preflight_and_reports_retained_dirs(self) -> None:
        plan = _plan(self.project, "APP", self.source)
        carrier = self.project / ".agents/skills/ca/SKILL.md"
        original_apply = FileUpdate.apply

        def concurrent_apply(update: FileUpdate) -> None:
            if update.path == plan.control / "project_structure.toml":
                carrier.write_bytes(b"concurrent custom\n")
            original_apply(update)

        with self.assertRaises(ProjectInstallationError) as context:
            with patch.object(FileUpdate, "apply", concurrent_apply):
                _apply(plan)
        self.assertEqual("restore-conflict", context.exception.code)
        self.assertIn("retained_dirs=", str(context.exception))
        self.assertEqual(b"concurrent custom\n", carrier.read_bytes())

    def test_apply_rejects_edit_to_preexisting_skill_after_preflight(self) -> None:
        install_project(self.project, prefix="APP", apply=True, source_root=self.source)
        plan = _plan(self.project, None, self.source)
        carrier = self.project / ".agents/skills/ca/SKILL.md"
        carrier.write_bytes(b"concurrent edit\n")
        with self.assertRaises(HostInstallationError) as context:
            _apply(plan)
        self.assertEqual("concurrent-change", context.exception.code)
        self.assertEqual(b"concurrent edit\n", carrier.read_bytes())

    def test_symlink_and_ambiguous_control_refuse_without_writes(self) -> None:
        outside = self.project.parent / "outside"
        outside.mkdir()
        (self.project / ".agents").symlink_to(outside, target_is_directory=True)
        with self.assertRaisesRegex(ProjectInstallationError, "symlink"):
            install_project(self.project, prefix="APP", source_root=self.source)

        legacy = self.project.parent / "legacy"
        legacy.mkdir()
        (legacy / ".caprmedio").mkdir()
        before = self._inventory(legacy)
        with self.assertRaises(ProjectInstallationError) as context:
            install_project(legacy, prefix="APP", source_root=self.source)
        self.assertEqual("legacy-control-root", context.exception.code)
        self.assertEqual(before, self._inventory(legacy))

        other = self.project.parent / "other"
        other.mkdir()
        (other / ".caprmedio_one").mkdir()
        (other / ".caprmedio_two").mkdir()
        before = self._inventory(other)
        with self.assertRaises(ProjectInstallationError) as context:
            install_project(other, prefix="APP", source_root=self.source)
        self.assertEqual("project-selection-conflict", context.exception.code)
        self.assertEqual(before, self._inventory(other))


if __name__ == "__main__":
    unittest.main()
