"""CA-D-681@2
CA-R-2902@1
"""

import json
import subprocess
import sys
from pathlib import Path
import unittest


PLUGIN = Path(__file__).resolve().parents[1]
HOOK = PLUGIN / "hooks" / "session_start.py"
REPOSITORY = PLUGIN.parents[5]


class PluginPackageTests(unittest.TestCase):
    def test_plugin_manifest_and_hook_paths_exist(self) -> None:
        manifest = json.loads((PLUGIN / "plugin.json").read_text())
        hooks = json.loads((PLUGIN / "hooks" / "hooks.json").read_text())

        self.assertEqual("./hooks/hooks.json", manifest["extensions"]["com.openai"]["hooks"])
        session_start = hooks["hooks"]["SessionStart"][0]
        self.assertEqual('python3 "${PLUGIN_ROOT}/hooks/session_start.py"', session_start["command"])
        self.assertEqual(500, session_start["additionalContextLimit"])
        self.assertTrue((PLUGIN / "skills" / "workbench" / "SKILL.md").is_file())
        self.assertTrue(HOOK.is_file())

    def test_marketplace_entry_targets_this_plugin_package(self) -> None:
        marketplace = json.loads((REPOSITORY / ".agents" / "plugins" / "marketplace.json").read_text())
        manifest = json.loads((PLUGIN / "plugin.json").read_text())
        entries = marketplace["plugins"]
        names = [entry["name"] for entry in entries]
        entry = next(entry for entry in entries if entry["name"] == manifest["name"])
        package = (REPOSITORY / entry["source"]["path"]).resolve()

        self.assertEqual(len(names), len(set(names)))
        self.assertEqual("local", entry["source"]["source"])
        self.assertEqual(PLUGIN.resolve(), package)
        self.assertTrue((package / manifest["extensions"]["com.openai"]["hooks"]).is_file())

    def test_session_start_hook_emits_only_native_session_context(self) -> None:
        result = subprocess.run(
            [sys.executable, str(HOOK)],
            input=json.dumps({"session_id": "native-session-42", "cwd": "/trusted/project"}),
            text=True,
            capture_output=True,
            check=False,
        )

        self.assertEqual(0, result.returncode)
        self.assertEqual("", result.stderr)
        self.assertEqual({
            "hookSpecificOutput": {
                "hookEventName": "SessionStart",
                "additionalContext": "Native Codex session ID: native-session-42",
            }
        }, json.loads(result.stdout))

    def test_session_start_hook_rejects_malformed_input_without_context(self) -> None:
        result = subprocess.run(
            [sys.executable, str(HOOK)],
            input="not json",
            text=True,
            capture_output=True,
            check=False,
        )

        self.assertEqual(1, result.returncode)
        self.assertEqual("", result.stdout)


if __name__ == "__main__":
    unittest.main()
