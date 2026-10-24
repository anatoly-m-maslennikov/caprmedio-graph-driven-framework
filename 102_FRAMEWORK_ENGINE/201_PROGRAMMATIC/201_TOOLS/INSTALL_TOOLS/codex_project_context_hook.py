"""Pass Codex's session folder to CAPRMEDIO MCP without changing native inputs."""

from __future__ import annotations

import json
from pathlib import Path
import sys

MAX_EVENT_BYTES = 32 * 1024 * 1024


def bind_project(event: dict) -> dict:
    if event.get("hook_event_name") != "PreToolUse":
        return {}
    name = event.get("tool_name")
    if not isinstance(name, str) or not name.startswith("mcp__caprmedio__"):
        return {}
    root, arguments = event.get("cwd"), event.get("tool_input")
    if not isinstance(root, str) or "\0" in root or not Path(root).is_absolute():
        raise ValueError("CAPRMEDIO requires an absolute session folder.")
    if not isinstance(arguments, dict):
        raise ValueError("CAPRMEDIO tool arguments must be an object.")
    if "project_root" in arguments and arguments["project_root"] != root:
        raise ValueError("CAPRMEDIO Project binding differs from the session folder.")
    return {
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": "allow",
            "updatedInput": {**arguments, "project_root": root},
        }
    }


def main() -> None:
    try:
        raw = sys.stdin.buffer.read(MAX_EVENT_BYTES + 1)
        if len(raw) > MAX_EVENT_BYTES:
            raise ValueError("CAPRMEDIO hook input exceeds its size limit.")
        event = json.loads(raw)
        if not isinstance(event, dict):
            raise ValueError("CAPRMEDIO hook input must be an object.")
        response = bind_project(event)
    except ValueError, UnicodeError, RecursionError:
        reason = "CAPRMEDIO Project context is invalid; the request was not sent."
        print(
            json.dumps(
                {
                    "severity": "WARNING",
                    "component": "CAPRMEDIO_CODEX_HOOK",
                    "project_binding": "unbound",
                    "message": reason,
                }
            ),
            file=sys.stderr,
        )
        response = {
            "hookSpecificOutput": {
                "hookEventName": "PreToolUse",
                "permissionDecision": "deny",
                "permissionDecisionReason": reason,
            }
        }
    print(json.dumps(response))


if __name__ == "__main__":
    main()
