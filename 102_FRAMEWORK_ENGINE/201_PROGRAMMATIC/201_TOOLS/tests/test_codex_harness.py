"""Isolated acceptance checks for the global Codex adapter."""

from __future__ import annotations

import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

TOOLS_ROOT = Path(__file__).resolve().parents[1]
if str(TOOLS_ROOT) not in sys.path:
    sys.path.insert(0, str(TOOLS_ROOT))

from INSTALL_TOOLS.codex_harness import CodexHarness  # noqa: E402
from INSTALL_TOOLS.host_installation_io import HostInstallationError  # noqa: E402
from INSTALL_TOOLS.host_installation_lock import installation_lock  # noqa: E402


class CodexHarnessTests(unittest.TestCase):
    def setUp(self) -> None:
        temporary_root = Path.cwd() / ".caprmedio_tmp" / "tests" / Path(__file__).stem
        temporary_root.mkdir(parents=True, exist_ok=True)
        self.temporary = tempfile.TemporaryDirectory(dir=temporary_root)
        base = Path(self.temporary.name)
        self.home = base / "codex-home"
        self.home.mkdir(parents=True)
        self.runtime = base / "runtime"
        self.runtime.mkdir()
        self.hook = (
            Path(__file__).resolve().parents[1] / "INSTALL_TOOLS/codex_project_context_hook.py"
        )
        self.old_home = os.environ.get("CODEX_HOME")
        os.environ["CODEX_HOME"] = str(self.home)

    def tearDown(self) -> None:
        if self.old_home is None:
            os.environ.pop("CODEX_HOME", None)
        else:
            os.environ["CODEX_HOME"] = self.old_home
        self.temporary.cleanup()

    def harness(self, endpoint: str = "http://127.0.0.1:8092/mcp") -> CodexHarness:
        return CodexHarness(runtime_root=self.runtime, endpoint=endpoint, hook_source=self.hook)

    def test_preview_is_pure_and_apply_restore_keeps_venv(self) -> None:
        harness = self.harness()
        self.assertEqual([], list(self.home.iterdir()))
        self.assertEqual([], list(self.runtime.iterdir()))
        self.assertTrue(harness.previewJSONdict["changed"])

        harness.apply()
        self.assertTrue((self.home / "hooks.json").is_file())
        self.assertTrue((self.home / "config.toml").is_file())
        self.assertTrue((self.runtime / "codex_project_context.py").is_file())
        venv_root = self.runtime / "venv"
        self.assertTrue(
            (venv_root / ("Scripts/python.exe" if os.name == "nt" else "bin/python")).is_file()
        )

        harness.restore()
        self.assertFalse((self.home / "hooks.json").exists())
        self.assertFalse((self.home / "config.toml").exists())
        self.assertFalse((self.runtime / "codex_project_context.py").exists())
        self.assertTrue(venv_root.is_dir())

    def test_repeat_install_is_no_op_and_installed_hook_executes(self) -> None:
        self.harness().apply()
        before = {
            path: path.read_bytes()
            for path in (self.home / "hooks.json", self.home / "config.toml")
        }
        repeat = self.harness()
        self.assertFalse(repeat.previewJSONdict["changed"])
        repeat.apply()
        self.assertEqual(before, {path: path.read_bytes() for path in before})

        event = {
            "hook_event_name": "PreToolUse",
            "tool_name": "mcp__caprmedio__status",
            "cwd": str(self.runtime),
            "tool_input": {"request": {"operation": "status"}},
        }
        result = subprocess.run(
            [
                str(self.runtime / "venv/bin/python"),
                "-B",
                str(self.runtime / "codex_project_context.py"),
            ],
            input=json.dumps(event),
            text=True,
            capture_output=True,
            check=True,
        )
        output = json.loads(result.stdout)
        self.assertEqual(
            str(self.runtime), output["hookSpecificOutput"]["updatedInput"]["project_root"]
        )

    def test_hook_merge_uses_nested_schema_and_replaces_owned_basename_only(self) -> None:
        (self.home / "hooks.json").write_text(
            json.dumps(
                {
                    "description": "keep",
                    "hooks": {
                        "PreToolUse": [
                            {
                                "matcher": "^mcp__caprmedio__",
                                "hooks": [
                                    {
                                        "type": "command",
                                        "command": "python /old/caprmedio_project_context.py",
                                    },
                                    {"type": "command", "command": "keep-this"},
                                ],
                            },
                            {"matcher": "^Bash$", "hooks": []},
                        ]
                    },
                }
            )
        )
        self.harness().apply()
        document = json.loads((self.home / "hooks.json").read_text())
        groups = document["hooks"]["PreToolUse"]
        managed = [group for group in groups if group.get("matcher") == "^mcp__caprmedio__"]
        self.assertEqual(1, len(managed))
        commands = [hook["command"] for hook in managed[0]["hooks"]]
        self.assertIn("keep-this", commands)
        self.assertEqual(1, sum("codex_project_context.py" in command for command in commands))
        self.assertNotIn("/old/caprmedio_project_context.py", commands)

    def test_conflicting_config_fails_before_any_effect(self) -> None:
        config = self.home / "config.toml"
        config.write_text('[mcp_servers.caprmedio]\nurl = "http://127.0.0.1:9999/mcp"\n')
        original = config.read_bytes()
        with self.assertRaises(HostInstallationError) as context:
            self.harness()
        self.assertEqual("mcp-server-conflict", context.exception.code)
        self.assertEqual(original, config.read_bytes())
        self.assertEqual([], list(self.runtime.iterdir()))
        self.assertEqual([], [path for path in self.home.iterdir() if path.name == "hooks.json"])

    def test_stdio_config_conflict_is_rejected(self) -> None:
        (self.home / "config.toml").write_text('[mcp_servers.caprmedio]\ncommand = "python"\n')
        with self.assertRaises(HostInstallationError):
            self.harness()
        self.assertFalse((self.runtime / "venv").exists())

    @unittest.skipUnless(os.name == "posix", "Codex host locking is POSIX-only")
    def test_busy_lock_refuses_first_venv_admission_without_waiting(self) -> None:
        runtime = self.runtime / "concurrent"
        harness = CodexHarness(
            runtime_root=runtime, endpoint="http://127.0.0.1:8092/mcp", hook_source=self.hook
        )
        with installation_lock(runtime):
            with self.assertRaises(HostInstallationError) as context:
                harness.apply()
            self.assertEqual("installation-busy", context.exception.code)
            self.assertFalse((runtime / "venv").exists())
        self.assertTrue((runtime / ".caprmedio-install.lock").is_file())
        harness.apply()
        self.assertTrue((runtime / "venv").is_dir())

    def test_duplicate_owned_groups_preserve_metadata_and_reject_conflicts(self) -> None:
        (self.home / "hooks.json").write_text(
            """{
              "hooks": {"PreToolUse": [
                {"matcher": "^mcp__caprmedio__", "policy": "same", "hooks": [
                  {"type": "command", "command": "python /old/caprmedio_project_context.py", "custom": "same"},
                  {"type": "command", "command": "keep-one"}
                ]},
                {"matcher": "^mcp__caprmedio__", "policy": "same", "hooks": [
                  {"type": "command", "command": "python /old/caprmedio_project_context.py", "custom": "same"},
                  {"type": "command", "command": "keep-two"}
                ]}
              ]}
            }"""
        )
        self.harness().apply()
        document = json.loads((self.home / "hooks.json").read_text())
        groups = document["hooks"]["PreToolUse"]
        self.assertEqual(1, len(groups))
        self.assertEqual("same", groups[0]["policy"])
        commands = groups[0]["hooks"]
        self.assertEqual({"keep-one", "keep-two"}, {hook["command"] for hook in commands[:2]})
        owned = commands[-1]
        self.assertEqual((5, "same"), (owned["timeout"], owned["custom"]))
        (self.home / "hooks.json").write_text(
            """{"hooks":{"PreToolUse":[{"matcher":"^mcp__caprmedio__","policy":"a","hooks":[]},{"matcher":"^mcp__caprmedio__","policy":"b","hooks":[]}]}}"""
        )
        with self.assertRaises(HostInstallationError) as context:
            self.harness()
        self.assertEqual("hooks-conflict", context.exception.code)


if __name__ == "__main__":
    unittest.main()
