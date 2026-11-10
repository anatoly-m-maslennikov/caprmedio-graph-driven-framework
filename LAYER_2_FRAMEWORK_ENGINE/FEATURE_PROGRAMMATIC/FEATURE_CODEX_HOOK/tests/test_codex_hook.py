# CA-E-814@1

"""Exercise the Codex command-hook boundary without an installed plugin."""

import json
from pathlib import Path
import subprocess
import sys
import unittest

HOOK = Path(__file__).resolve().parents[1] / "codex_hook.py"


def invoke(event):
    completed = subprocess.run(
        [sys.executable, str(HOOK)], input=event, text=True, capture_output=True, check=True
    )
    return json.loads(completed.stdout)


class CodexHookTests(unittest.TestCase):
    def setUp(self):
        self.event = {
            "hook_event_name": "PreToolUse",
            "tool_name": "mcp__caprmedio__query_run",
            "session_id": "codex-session-123",
            "tool_input": {
                "project_root": "/projects/example",
                "sql": "SELECT 1",
                "session_id": "native-argument",
            },
        }

    def decision(self, event):
        return invoke(json.dumps(event))["hookSpecificOutput"]

    def test_injects_session_and_preserves_native_arguments(self):
        result = self.decision(self.event)
        self.assertEqual("allow", result["permissionDecision"])
        self.assertEqual(
            {**self.event["tool_input"], "caller_context": {"session_id": "codex-session-123"}},
            result["updatedInput"],
        )

    def test_matching_existing_context_is_preserved(self):
        self.event["tool_input"]["caller_context"] = {"session_id": "codex-session-123", "other": 4}
        result = self.decision(self.event)
        self.assertEqual(self.event["tool_input"], result["updatedInput"])

    def test_conflicting_session_is_denied(self):
        self.event["tool_input"]["caller_context"] = {"session_id": "another-session"}
        self.assertEqual("deny", self.decision(self.event)["permissionDecision"])

    def test_missing_or_invalid_context_is_denied(self):
        for key, value in (("session_id", None), ("session_id", ""), ("tool_input", None)):
            with self.subTest(key=key, value=value):
                changed = {**self.event, key: value}
                self.assertEqual("deny", self.decision(changed)["permissionDecision"])
        for key, value in (("project_root", None), ("project_root", ""), ("caller_context", None)):
            with self.subTest(key=key, value=value):
                changed = {**self.event, "tool_input": {**self.event["tool_input"], key: value}}
                self.assertEqual("deny", self.decision(changed)["permissionDecision"])

    def test_other_servers_are_untouched(self):
        result = invoke(json.dumps({**self.event, "tool_name": "mcp__other__query_run"}))
        self.assertEqual({}, result)

    def test_invalid_json_is_denied(self):
        self.assertEqual("deny", invoke("{")["hookSpecificOutput"]["permissionDecision"])

    def test_large_deep_and_non_unicode_input_is_denied(self):
        for raw in (
            b" " * (32 * 1024 * 1024 + 1),
            b"[" * 1200 + b"]" * 1200,
            b'"\xff"',
            b"{" + b'"v":' + b"1" * 5000 + b"}",
        ):
            with self.subTest(size=len(raw)):
                result = subprocess.run(
                    [sys.executable, str(HOOK)], input=raw, capture_output=True, check=True
                )
                self.assertEqual(
                    "deny", json.loads(result.stdout)["hookSpecificOutput"]["permissionDecision"]
                )


if __name__ == "__main__":
    unittest.main()
