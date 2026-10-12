"""Regression checks for Structure authority paths and transported host roots."""

from __future__ import annotations

import hashlib
from pathlib import Path
import sys
import tempfile
import unittest

APP = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(APP.parents[1] / "201_TOOLS"))
from project_selection import ProjectSelectionError, rebind_selection, resolve_project  # noqa: E402


class ProjectSelectionEdgeCases(unittest.TestCase):
    def setUp(self) -> None:
        parent = APP.parents[3] / ".caprmedio_tmp" / "launcher-epic-1829" / "selection"
        parent.mkdir(parents=True, exist_ok=True)
        self.fixture = Path(tempfile.mkdtemp(dir=parent))
        self.root = self.fixture / "project"
        self.control = self.root / ".caprmedio_demo"
        self.control.mkdir(parents=True)
        (self.control / "caprmedio_project_settings.toml").write_text(
            '[paths]\ncontrol_root=".caprmedio_demo"\n[project]\nname="demo"\n', encoding="utf-8")
        self.structure = self.control / "project_structure.toml"
        self.structure.write_text("schema_version=1\n", encoding="utf-8")

    def declare_authority(self, value: str | None) -> None:
        declaration = f'authority_path="{value}"\n' if value is not None else ""
        self.structure.write_text(
            'schema_version=1\n[[scope_units]]\nscope_unit_name="DECLARED"\n' + declaration,
            encoding="utf-8")

    def identity(self, host: str | Path) -> str:
        return hashlib.sha256(f"{host}\0.caprmedio_demo".encode()).hexdigest()

    def test_structure_authority_refuses_escape_and_symlink_but_allows_unmaterialized_paths(self) -> None:
        sibling = self.fixture / "sibling"
        sibling.mkdir()
        (self.root / "alias").symlink_to(sibling, target_is_directory=True)
        for value in ("../sibling", str(sibling), "alias/not-yet-materialized"):
            with self.subTest(authority_path=value):
                self.declare_authority(value)
                with self.assertRaises(ProjectSelectionError):
                    resolve_project(self.root)
        for value in (".caprmedio_demo/not-yet-materialized", None):
            with self.subTest(authority_path=value):
                self.declare_authority(value)
                self.assertEqual(self.root, resolve_project(self.root).root)

    def test_transported_host_root_refuses_existing_alias_and_accepts_unmounted_canonical_path(self) -> None:
        selected = resolve_project(self.root)
        alias = self.fixture / "host-alias"
        alias.symlink_to(self.root, target_is_directory=True)
        with self.assertRaises(ProjectSelectionError):
            rebind_selection(selected, self.identity(alias), host_root=alias)
        for host in ("relative-host", str(self.fixture) + "/../host", str(self.fixture) + "/./host"):
            with self.subTest(host_root=host), self.assertRaises(ProjectSelectionError):
                rebind_selection(selected, self.identity(host), host_root=host)
        unmounted = self.fixture / "unmounted-host" / "project"
        self.assertFalse(unmounted.exists())
        transported = rebind_selection(selected, self.identity(unmounted), host_root=unmounted)
        self.assertEqual(unmounted, transported.host_root)
        self.assertEqual(self.identity(unmounted), transported.instance_id)
        self.assertEqual(self.root, transported.root)


if __name__ == "__main__":
    unittest.main()
