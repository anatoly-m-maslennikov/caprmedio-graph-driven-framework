"""Installation preserves legacy state until separately authorized cleanup."""

import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "install_tools.py"
SPEC = importlib.util.spec_from_file_location("install_tools_retention", SCRIPT)
assert SPEC is not None and SPEC.loader is not None
installer = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = installer
SPEC.loader.exec_module(installer)


class LegacyRetentionTests(unittest.TestCase):
    def test_installation_cleanup_preserves_all_legacy_carriers(self):
        # Retained synthetic fixtures are intentional evidence, not live state.
        root = Path(tempfile.mkdtemp(prefix="caprmedio-retention-"))
        paths = (
            ".caprmedio_install/project_mcp/state.json",
            ".caprmedio_install/mcp_hot_reload/receipt.json",
            ".caprmedio_install/workflow_orchestrator/history.json",
            ".caprmedio_install/releases/old/manifest.toml",
            ".caprmedio_runtime/installed/manifest.toml",
            ".caprmedio_runtime/hooks/git/pre-commit",
        )
        for relative in paths:
            path = root / relative
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(b"synthetic retained evidence\n")
        before = {relative: (root / relative).read_bytes() for relative in paths}
        self.assertEqual([], installer._remove_legacy_installation(root))
        self.assertEqual(before, {relative: (root / relative).read_bytes() for relative in paths})


if __name__ == "__main__":
    unittest.main()
