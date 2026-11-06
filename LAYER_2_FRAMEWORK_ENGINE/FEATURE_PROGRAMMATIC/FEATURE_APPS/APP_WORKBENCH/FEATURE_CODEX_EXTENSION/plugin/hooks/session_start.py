#!/usr/bin/env python3
# CA-D-681@9
# CA-R-2902@4

import json
import sys
from typing import Any


def session_context(payload: object) -> dict[str, Any] | None:
    if not isinstance(payload, dict):
        return None
    session_id = payload.get("session_id")
    cwd = payload.get("cwd")
    if not isinstance(session_id, str) or not session_id.strip():
        return None
    if not isinstance(cwd, str) or not cwd:
        return None
    return {
        "hookSpecificOutput": {
            "hookEventName": "SessionStart",
            "additionalContext": f"Native Codex session ID: {session_id}",
        }
    }


def main() -> int:
    try:
        payload = json.load(sys.stdin)
    except json.JSONDecodeError:
        return 1
    output = session_context(payload)
    if output is None:
        return 1
    json.dump(output, sys.stdout)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
