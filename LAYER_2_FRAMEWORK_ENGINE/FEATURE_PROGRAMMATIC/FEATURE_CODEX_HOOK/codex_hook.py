# CA-M-517@1
# CA-D-706@2

"""Attach the native Codex session to a bound CAPRMEDIO MCP call."""

from __future__ import annotations

import json
import sys
from typing import Any

MAX_EVENT_BYTES = 32 * 1024 * 1024


def deny(reason: str) -> dict[str, Any]:
    return {
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": "deny",
            "permissionDecisionReason": reason,
        }
    }


def pre_tool_use(event: object) -> dict[str, Any]:
    if not isinstance(event, dict):
        return deny("CAPRMEDIO hook event must be an object")
    tool_name = event.get("tool_name")
    if not isinstance(tool_name, str):
        return deny("CAPRMEDIO hook event requires a tool name")
    if not tool_name.startswith("mcp__caprmedio__"):
        return {}
    arguments = event.get("tool_input")
    session_id = event.get("session_id")
    if not isinstance(arguments, dict):
        return deny("CAPRMEDIO tool arguments must be an object")
    root = arguments.get("project_root")
    if not isinstance(root, str) or not root.strip():
        return deny("CAPRMEDIO tool call requires an existing Project binding")
    if not isinstance(session_id, str) or not session_id.strip():
        return deny("CAPRMEDIO hook event requires a session ID")
    context = arguments.get("caller_context", {})
    if not isinstance(context, dict):
        return deny("CAPRMEDIO caller context must be an object")
    if "session_id" in context and context["session_id"] != session_id:
        return deny("CAPRMEDIO caller session differs from the Codex session")
    updated = dict(arguments)
    updated["caller_context"] = {**context, "session_id": session_id}
    return {
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": "allow",
            "updatedInput": updated,
        }
    }


def main() -> int:
    try:
        raw = sys.stdin.buffer.read(MAX_EVENT_BYTES + 1)
        if len(raw) > MAX_EVENT_BYTES:
            raise ValueError("CAPRMEDIO hook input exceeds its size limit")
        event = json.loads(raw)
        result = pre_tool_use(event)
        output = json.dumps(result)
    except ValueError, UnicodeError, RecursionError:
        output = json.dumps(deny("CAPRMEDIO hook input is invalid or exceeds its size limit"))
    sys.stdout.write(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
