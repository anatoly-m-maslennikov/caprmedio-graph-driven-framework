"""Different runtime roots must still serialize their shared Codex configuration."""

import os
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from INSTALL_TOOLS.codex_harness import CodexHarness  # noqa: E402
from INSTALL_TOOLS.host_installation_io import HostInstallationError  # noqa: E402
from INSTALL_TOOLS.host_installation_lock import installation_lock  # noqa: E402


@unittest.skipUnless(os.name == "posix", "Host installation locking requires POSIX")
class CodexHarnessLockScopesTests(unittest.TestCase):
    def test_shared_codex_home_refuses_other_runtime_roots_before_venv_or_writes(self):
        directory = Path.cwd() / ".caprmedio_tmp/tests/codex_harness_lock_scopes"
        directory.mkdir(parents=True, exist_ok=True)
        with tempfile.TemporaryDirectory(dir=directory) as temporary:
            base = Path(temporary).resolve()
            home, hook = base / "codex", base / "hook.py"
            hook.write_text("# fixture\n")
            with patch.dict(os.environ, {"CODEX_HOME": str(home)}):
                with installation_lock(home, ".caprmedio-codex-install.lock"):
                    for name in ("runtime-a", "runtime-b"):
                        runtime = base / name
                        harness = CodexHarness(
                            runtime_root=runtime,
                            endpoint="http://127.0.0.1:8092/mcp",
                            hook_source=hook,
                        )
                        with self.assertRaises(HostInstallationError) as caught:
                            harness.apply()
                        self.assertEqual(caught.exception.code, "installation-busy")
                        self.assertFalse(runtime.exists())
                self.assertFalse((home / "hooks.json").exists())
                self.assertFalse((home / "config.toml").exists())


if __name__ == "__main__":
    unittest.main()
