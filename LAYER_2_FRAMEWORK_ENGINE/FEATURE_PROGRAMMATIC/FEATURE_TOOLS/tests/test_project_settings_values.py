"""Read-only Project Settings values retain explicit selection semantics."""

from __future__ import annotations

from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch


TOOLS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOLS))

from project_settings_values import (  # noqa: E402
    ProjectSettingsValueError,
    control_root,
    project_identity_prefix,
)


class ProjectSettingsValuesTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name) / "project"
        self.root.mkdir()
        self.control = self.root / ".caprmedio_caprmedio"
        self.control.mkdir()
        self.settings = self.control / "caprmedio_project_settings.toml"
        self.settings.write_text(
            '[artifacts.identity]\nproject_prefix = "CA"\n[paths]\ncontrol_root = ".caprmedio_caprmedio"\n',
            encoding="utf-8",
        )

    def test_unbound_uses_only_the_canonical_settings_carrier(self) -> None:
        self.assertEqual(self.control.resolve(), control_root(self.root))
        self.assertEqual("CA", project_identity_prefix(self.root))

    def test_unbound_does_not_require_scope_declarations(self) -> None:
        self.assertEqual("CA", project_identity_prefix(self.root))

    def test_invalid_values_remain_attributable(self) -> None:
        self.settings.write_text('[paths]\ncontrol_root = ".caprmedio_other"\n', encoding="utf-8")
        with self.assertRaises(ProjectSettingsValueError) as control_error:
            control_root(self.root)
        self.assertEqual("project-settings-invalid", control_error.exception.code)
        with self.assertRaises(ProjectSettingsValueError) as prefix_error:
            project_identity_prefix(self.root)
        self.assertEqual("project-settings-invalid", prefix_error.exception.code)

    def test_bound_selection_is_used_without_opening_settings(self) -> None:
        selection = type("Selection", (), {
            "control_root": self.control.resolve(),
            "settings": {"artifacts": {"identity": {"project_prefix": "BOUND"}}},
        })()
        with patch("project_settings_values.bound_selection", return_value=selection):
            self.settings.unlink()
            self.assertEqual(self.control.resolve(), control_root(self.root))
            self.assertEqual("BOUND", project_identity_prefix(self.root))


if __name__ == "__main__":
    unittest.main()
