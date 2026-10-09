"""Synthetic replacement-policy tests for the legacy Tool installer."""

from __future__ import annotations

from pathlib import Path
import shutil
import sys
import tempfile
import unittest
from unittest.mock import patch


TOOLS = Path(__file__).resolve().parents[1]
TEST_TEMP_ROOT = Path.cwd() / ".caprmedio_tmp" / "tests" / Path(__file__).stem
TEST_TEMP_ROOT.mkdir(parents=True, exist_ok=True)
if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))

import framework_installation  # noqa: E402
from framework_installation import InstallationError, install_release, installation_status  # noqa: E402


class FrameworkInstallationReplacementTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory(dir=TEST_TEMP_ROOT, delete=False)
        self.root = Path(self.temporary.name) / "project"
        self.root.mkdir()
        self.source = self.root / "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS"
        for relative in framework_installation.REQUIRED_FILES:
            source = TOOLS / relative
            target = self.source / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, target)

    def _repository(self):
        return patch.object(framework_installation, "resolve_repository", side_effect=lambda value: Path(value).absolute())

    def _install(self, *, apply: bool = True):
        with self._repository():
            return install_release(self.root, apply=apply, source_root=self.source)

    @property
    def _tools(self) -> Path:
        return self.root / ".caprmedio_runtime/tools"

    def _upgrade_source(self) -> None:
        carrier = self.source / "background_services.toml"
        carrier.write_bytes(carrier.read_bytes() + b"\n# replacement fixture upgrade\n")

    @staticmethod
    def _has_version_bytes(path: Path) -> bool:
        return any(carrier.is_file() for carrier in path.rglob("*"))

    def test_dry_run_declares_replacement_without_creating_target_state(self) -> None:
        result = self._install(apply=False)

        self.assertFalse(result["installed"])
        self.assertEqual("replace-managed-installed-tool-version", result["planned_effect"])
        self.assertFalse((self.root / ".caprmedio_runtime").exists())

    def test_same_version_reinstall_repairs_drift_and_removes_obsolete_managed_bytes(self) -> None:
        first = self._install()
        release = self._tools / "releases" / str(first["release"])
        carrier = release / "TOOLS/background_services.toml"
        carrier.write_bytes(b"drift\n")
        obsolete = self._tools / "obsolete-tool-byte"
        obsolete.write_bytes(b"remove me\n")

        repaired = self._install()

        self.assertEqual(first["release"], repaired["release"])
        self.assertEqual((self.source / "background_services.toml").read_bytes(), carrier.read_bytes())
        self.assertFalse(obsolete.exists())

    def test_upgrade_replaces_prior_release_without_touching_config_journal_or_install_state(self) -> None:
        first = self._install()
        config = self.root / ".caprmedio_runtime/config.toml"
        journal = self.root / ".caprmedio_target/_journal/events.ndjson"
        installation_state = self.root / ".caprmedio_runtime/installation/migrations/prior/receipt.toml"
        for path, payload in (
            (config, b"# target config\n[project_mcp]\nport = 8123\n"),
            (journal, b"{\"event\": \"preserve\"}\n"),
            (installation_state, b"state = \"preserve\"\n"),
        ):
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(payload)
        preserved = {path: path.read_bytes() for path in (config, journal, installation_state)}
        self._upgrade_source()

        second = self._install()

        self.assertNotEqual(first["release"], second["release"])
        self.assertFalse(self._has_version_bytes(self._tools / "releases" / str(first["release"])))
        self.assertTrue(self._has_version_bytes(self._tools / "releases" / str(second["release"])))
        self.assertEqual(preserved, {path: path.read_bytes() for path in preserved})

    def test_stage_failure_preserves_the_selected_old_version(self) -> None:
        first = self._install()
        selector = self._tools / "current.toml"
        selector_before = selector.read_bytes()
        self._upgrade_source()

        with patch.object(
            framework_installation,
            "_verify_staged_release",
            side_effect=InstallationError("release-stage-invalid", "fixture rejects stage"),
        ), self.assertRaisesRegex(InstallationError, "fixture rejects stage"):
            self._install()

        self.assertEqual(selector_before, selector.read_bytes())
        self.assertTrue((self._tools / "releases" / str(first["release"])).is_dir())

    def test_unsafe_alias_or_protected_env_path_refuses_before_deletion(self) -> None:
        first = self._install()
        selector = self._tools / "current.toml"
        selector_before = selector.read_bytes()
        external = self.root.parent / "external-sentinel"
        external.write_bytes(b"outside managed surface\n")
        (self._tools / "external-alias").symlink_to(external)

        with self.assertRaisesRegex(InstallationError, "unsafe alias"):
            self._install()

        self.assertEqual(selector_before, selector.read_bytes())
        self.assertEqual(b"outside managed surface\n", external.read_bytes())
        (self._tools / "external-alias").unlink()

        with patch.object(
            framework_installation.os,
            "walk",
            return_value=iter(((str(self._tools), [], [".env-protected"]),)),
        ), self.assertRaisesRegex(InstallationError, "protected env path"):
            self._install()

        self.assertEqual(selector_before, selector.read_bytes())
        self.assertTrue((self._tools / "releases" / str(first["release"])).is_dir())

    def test_postwipe_promotion_failure_has_no_active_selector(self) -> None:
        first = self._install()
        self._upgrade_source()
        with self._repository():
            _rows, release = framework_installation.source_inventory(self.root, source_root=self.source)
        destination = self._tools / "releases" / release
        actual_copytree = framework_installation.shutil.copytree

        def fail_only_promotion(source: str | Path, target: str | Path, *args: object, **kwargs: object):
            if Path(target) == destination:
                raise OSError("fixture promotion failure")
            return actual_copytree(source, target, *args, **kwargs)

        with patch.object(framework_installation.shutil, "copytree", side_effect=fail_only_promotion), self.assertRaisesRegex(
            InstallationError, "cannot promote release"
        ):
            self._install()

        self.assertFalse((self._tools / "current.toml").exists())
        self.assertFalse(self._has_version_bytes(self._tools / "releases" / str(first["release"])))
        with self._repository():
            self.assertFalse(installation_status(self.root)["installed"])


if __name__ == "__main__":
    unittest.main()
