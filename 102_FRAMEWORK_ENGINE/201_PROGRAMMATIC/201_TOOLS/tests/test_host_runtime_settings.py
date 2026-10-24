from __future__ import annotations

from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch


TOOLS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOLS))

from INSTALL_TOOLS.host_runtime_settings import HostRuntimeSettings  # noqa: E402
from INSTALL_TOOLS import host_runtime_settings as settings_module  # noqa: E402
from host_runtime_config import load_host_runtime_config  # noqa: E402


TEST_TEMP_ROOT = Path.cwd() / ".caprmedio_tmp" / "tests" / Path(__file__).stem
TEST_TEMP_ROOT.mkdir(parents=True, exist_ok=True)


class HostRuntimeSettingsTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory(dir=TEST_TEMP_ROOT)
        self.base = Path(self.temporary.name)
        self.projects = self.base / "repos"
        self.projects.mkdir()
        self.settings = self.base / "config" / "runtime.toml"
        self.settings.parent.mkdir()

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def test_dry_run_has_no_file_side_effects(self) -> None:
        proposal = HostRuntimeSettings(
            projects_root=self.projects,
            host_settings=self.settings,
        )
        self.assertEqual(
            {
                "host_settings",
                "projects_root",
                "http_port",
                "max_loaded_projects",
                "changed",
            },
            set(proposal.preview),
        )
        self.assertTrue(proposal.preview["changed"])
        self.assertFalse(self.settings.exists())

    def test_create_and_restore(self) -> None:
        proposal = HostRuntimeSettings(
            projects_root=self.projects,
            host_settings=self.settings,
        )
        proposal.apply()
        loaded = load_host_runtime_config(self.settings)
        self.assertEqual(
            (self.projects, 8092, 2),
            (
                loaded.projects_root,
                loaded.http_port,
                loaded.max_loaded_projects,
            ),
        )
        self.assertEqual(0o600, self.settings.stat().st_mode & 0o777)
        proposal.restore()
        self.assertFalse(self.settings.exists())

    def test_update_preserves_omitted_values(self) -> None:
        original_root = self.base / "original-repos"
        original_root.mkdir()
        self.settings.write_text(
            f"schema_version = 1\n\n[shared_mcp]\nprojects_root = {str(original_root)!r}\n"
            "http_port = 18093\nmax_loaded_projects = 3\n",
            encoding="utf-8",
        )
        original = self.settings.read_bytes()
        proposal = HostRuntimeSettings(projects_root=self.projects, host_settings=self.settings)
        self.assertEqual(18093, proposal.preview["http_port"])
        self.assertEqual(3, proposal.preview["max_loaded_projects"])
        proposal.apply()
        loaded = load_host_runtime_config(self.settings)
        self.assertEqual(
            (self.projects, 18093, 3),
            (
                loaded.projects_root,
                loaded.http_port,
                loaded.max_loaded_projects,
            ),
        )
        proposal.restore()
        self.assertEqual(original, self.settings.read_bytes())

    def test_unchanged_values_preserve_original_bytes(self) -> None:
        original = (
            "# retain this comment\n"
            "schema_version = 1\n\n"
            "[shared_mcp]\n"
            f"projects_root = {str(self.projects)!r}\n"
            "http_port = 18094\n"
            "max_loaded_projects = 2\n"
        ).encode()
        self.settings.write_bytes(original)
        proposal = HostRuntimeSettings(projects_root=self.projects, host_settings=self.settings)
        self.assertFalse(proposal.preview["changed"])
        proposal.apply()
        self.assertEqual(original, self.settings.read_bytes())

    def test_invalid_root_fails_before_write(self) -> None:
        with self.assertRaises(ValueError):
            HostRuntimeSettings(
                projects_root=self.base / "missing",
                host_settings=self.settings,
            )
        self.assertFalse(self.settings.exists())
        with self.assertRaises(ValueError):
            HostRuntimeSettings(
                projects_root=self.projects,
                host_settings=self.projects / "runtime.toml",
            )
        self.assertFalse((self.projects / "runtime.toml").exists())

    def test_settings_symlink_is_rejected(self) -> None:
        target = self.base / "target.toml"
        target.write_text("", encoding="utf-8")
        self.settings.symlink_to(target)
        with self.assertRaises(ValueError):
            HostRuntimeSettings(projects_root=self.projects, host_settings=self.settings)
        self.assertTrue(self.settings.is_symlink())

    def test_concurrent_preflight_comment_edit_is_not_adopted_as_authorized_state(self):
        HostRuntimeSettings(projects_root=self.projects, host_settings=self.settings).apply()
        original = self.settings.read_bytes()
        concurrent = original + b"# operator edit\n"
        factory = settings_module.FileUpdate

        def changed_snapshot(path, content, mode):
            self.settings.write_bytes(concurrent)
            return factory(path, content, mode=mode)

        with patch.object(settings_module, "FileUpdate", side_effect=changed_snapshot):
            with self.assertRaisesRegex(ValueError, "changed during preflight"):
                HostRuntimeSettings(host_settings=self.settings)
        self.assertEqual(self.settings.read_bytes(), concurrent)


if __name__ == "__main__":
    unittest.main()
