"""Reboot startup selects the completed local release, not an older selector."""

from pathlib import Path
from types import SimpleNamespace
import os
import tempfile
import unittest
from unittest.mock import patch

import test_start_mcp_script as fixture


class StartMcpPackagePriorityTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory(prefix="local-package-priority-")
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name).resolve()
        deployed = self.root / ".caprmedio_runtime/start_mcp.py"
        deployed.parent.mkdir()
        deployed.write_bytes(fixture.SCRIPT.read_bytes())
        self.module = fixture.StartMcpScriptTests()._module(deployed)
        self.local = self.root / ".caprmedio_runtime/simple_local_release/package"
        self.old = self.root / ".caprmedio_install/releases" / ("a" * 64)
        self.launcher(self.old)
        self.selector = self.root / ".caprmedio_install/current.toml"
        self.selector.write_text('release_relpath = "releases/' + "a" * 64 + '"\n')

    def launcher(self, package):
        launcher = package / self.module.LAUNCHER_PATH
        launcher.parent.mkdir(parents=True)
        launcher.write_text("# fixture launcher, never executed\n")
        return launcher

    def test_local_package_wins_without_changing_old_selector_or_runtime_config(self):
        launcher = self.launcher(self.local)
        config = self.root / ".caprmedio_runtime/config.toml"
        config.write_bytes(b"retained = true\n")
        before = self.selector.read_bytes()
        with patch.object(
            self.module.subprocess, "run", return_value=SimpleNamespace(returncode=0)
        ) as run:
            self.assertEqual(0, self.module.main([]))
        argv = run.call_args.args[0]
        self.assertEqual(str(self.local), argv[argv.index("--source-root") + 1])
        self.assertIn(str(launcher), argv)
        self.assertEqual(before, self.selector.read_bytes())
        self.assertEqual(b"retained = true\n", config.read_bytes())

    def test_absent_local_package_keeps_legacy_startup_fallback(self):
        self.assertFalse(self.local.exists())
        self.assertEqual(self.old, self.module._installed_source_root(self.root))

    def test_present_broken_local_package_refuses_instead_of_starting_old_package(self):
        self.local.mkdir(parents=True)
        with patch.object(self.module.subprocess, "run") as run:
            with self.assertRaises(SystemExit) as error:
                self.module.main([])
        self.assertEqual(2, error.exception.code)
        run.assert_not_called()

    def test_local_package_file_or_dangling_symlink_refuses(self):
        self.local.parent.mkdir(parents=True)
        self.local.write_bytes(b"not a package")
        with self.assertRaises(ValueError):
            self.module._installed_source_root(self.root)
        self.local.unlink()
        self.local.symlink_to(self.root / "absent")
        with self.assertRaises(ValueError):
            self.module._installed_source_root(self.root)

    def test_local_package_parent_symlink_refuses_even_if_legacy_selector_is_valid(self):
        self.local.parent.symlink_to(self.root / "absent", target_is_directory=True)
        with self.assertRaises(ValueError):
            self.module._installed_source_root(self.root)

    @unittest.skipUnless(
        os.name == "posix" and os.geteuid() != 0, "requires POSIX permission enforcement"
    )
    def test_unreadable_new_package_parent_refuses_without_legacy_startup(self):
        self.launcher(self.local)
        self.local.parent.chmod(0)
        try:
            with patch.object(self.module.subprocess, "run") as run:
                with self.assertRaises(SystemExit) as error:
                    self.module.main([])
            self.assertEqual(2, error.exception.code)
            run.assert_not_called()
        finally:
            self.local.parent.chmod(0o755)


if __name__ == "__main__":
    unittest.main()
