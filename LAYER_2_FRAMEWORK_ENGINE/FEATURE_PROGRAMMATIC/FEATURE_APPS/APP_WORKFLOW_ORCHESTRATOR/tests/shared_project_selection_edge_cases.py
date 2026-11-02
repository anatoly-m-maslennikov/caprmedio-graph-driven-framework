"""Regression checks for Structure authority paths and transported host roots."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
import sys
import tempfile
import unittest

APP = Path(__file__).resolve().parents[1]
TOOLS = APP.parents[1] / "FEATURE_TOOLS"
sys.path.insert(0, str(TOOLS))
from scope_declaration_test_support import write_scope_unit_declarations  # noqa: E402
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
        self.declarations = write_scope_unit_declarations(
            self.root,
            ({"scope_unit_name": "DECLARED", "parent": "PROJECT", "scope_unit_type": "Unordered"},),
            control_root=self.control,
            project_name="demo",
        )
        self.declaration = Path(self.declarations["DECLARED"]["declaration_path"])

    def declare_legacy_authority(self, value: str) -> None:
        """Ensure retired authored paths remain rejected as invalid source claims."""
        contents = self.declaration.read_text(encoding="utf-8")
        contents = contents.replace(
            "\n```\n",
            f'\nauthority_path == {json.dumps(value)};\n```\n',
            1,
        )
        self.declaration.write_text(contents, encoding="utf-8")

    def identity(self, host: str | Path) -> str:
        return hashlib.sha256(f"{host}\0.caprmedio_demo".encode()).hexdigest()

    def test_declaration_authority_refuses_authored_escape_and_symlink_but_allows_derived_paths(self) -> None:
        sibling = self.fixture / "sibling"
        sibling.mkdir()
        for value in ("../sibling", str(sibling), "alias/not-yet-materialized"):
            with self.subTest(authority_path=value):
                self.declare_legacy_authority(value)
                with self.assertRaises(ProjectSelectionError):
                    resolve_project(self.root)
                self.declarations = write_scope_unit_declarations(
                    self.root,
                    ({"scope_unit_name": "DECLARED", "parent": "PROJECT", "scope_unit_type": "Unordered"},),
                    control_root=self.control,
                    project_name="demo",
                )
                self.declaration = Path(self.declarations["DECLARED"]["declaration_path"])
        derived = Path(self.declarations["DECLARED"]["authority_path"])
        self.assertFalse(derived.exists())
        self.assertEqual(self.root, resolve_project(self.root).root)
        derived.symlink_to(sibling, target_is_directory=True)
        with self.assertRaises(ProjectSelectionError):
            resolve_project(self.root)

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
