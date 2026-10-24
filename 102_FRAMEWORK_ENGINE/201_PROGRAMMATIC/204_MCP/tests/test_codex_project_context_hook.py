"""Functional checks for the documented Codex hook JSON protocol."""

import json
from pathlib import Path
import subprocess
import sys
import unittest

HOOK = Path(__file__).resolve().parents[2] / "201_TOOLS/INSTALL_TOOLS/codex_project_context_hook.py"


class CodexProjectContextHookTests(unittest.TestCase):
    def run_hook(self, event):
        raw = event if isinstance(event, bytes) else json.dumps(event).encode()
        result = subprocess.run(
            [sys.executable, "-B", str(HOOK)],
            input=raw,
            capture_output=True,
            check=True,
            timeout=5,
        )
        return json.loads(result.stdout), result.stderr.decode()

    def event(self, root="/repos/Project A", **changes):
        return {
            "hook_event_name": "PreToolUse",
            "tool_name": "mcp__caprmedio__workflow_orchestrator",
            "cwd": root,
            "tool_input": {"request": {"operation": "status", "run_id": "original"}},
            **changes,
        }

    def test_forwards_each_session_root_and_preserves_native_arguments(self):
        for root in ("/repos/Project A", "/repos/Project B", "/repos/nested/project"):
            for bound in (False, True):
                with self.subTest(root=root, already_bound=bound):
                    event = self.event(root)
                    if bound:
                        event["tool_input"]["project_root"] = root
                    output, warning = self.run_hook(event)
                    self.assertEqual(
                        output["hookSpecificOutput"],
                        {
                            "hookEventName": "PreToolUse",
                            "permissionDecision": "allow",
                            "updatedInput": {**event["tool_input"], "project_root": root},
                        },
                    )
                    self.assertEqual(warning, "")

    def test_unrelated_tools_and_events_are_untouched(self):
        for changes in (
            {"tool_name": "mcp__other__read"},
            {"tool_name": "Bash"},
            {"hook_event_name": "PostToolUse"},
            {"tool_name": None},
        ):
            with self.subTest(changes=changes):
                self.assertEqual(self.run_hook(self.event(**changes)), ({}, ""))

    def test_invalid_context_denies_without_exposing_payload(self):
        cases = [self.event(root=root) for root in (None, "", "relative", "/bad\0root")]
        cases += [self.event(tool_input=value) for value in (None, [], "secret")]
        cases += [self.event(tool_input={"project_root": "/repos/another", "secret": "hidden"})]
        cases += [b"not-json-secret", b"[]", b'{"cwd":"\xff"}']
        for event in cases:
            with self.subTest(event=event):
                output, warning = self.run_hook(event)
                decision = output["hookSpecificOutput"]
                self.assertEqual(decision["permissionDecision"], "deny")
                self.assertNotIn("updatedInput", decision)
                self.assertIn("WARNING", warning)
                self.assertNotIn("secret", warning + json.dumps(output))
                self.assertNotIn("hidden", warning + json.dumps(output))

    def test_oversized_event_is_denied(self):
        output, warning = self.run_hook(b" " * (32 * 1024 * 1024 + 1))
        self.assertEqual(output["hookSpecificOutput"]["permissionDecision"], "deny")
        self.assertIn("WARNING", warning)


if __name__ == "__main__":
    unittest.main()
