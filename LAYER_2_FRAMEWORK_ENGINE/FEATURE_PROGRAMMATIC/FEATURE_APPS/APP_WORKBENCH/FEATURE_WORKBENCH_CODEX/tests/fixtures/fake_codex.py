#!/usr/bin/env python3
"""External app-server fixture used by the Workbench Codex HTTP test.

This is deliberately a process boundary.  It speaks the small JSON-RPC
surface exercised by the bridge; it is not an in-process fake of bridge or
Workbench code.
"""

from __future__ import annotations

import json
import os
import sys
import time
from typing import Any


THREAD_ID = "native-thread-1"
THREAD_CWD = ""
turn_number = 0
turns: list[dict[str, Any]] = []


def audit(packet: dict[str, Any]) -> None:
    path = os.environ.get("FAKE_CODEX_AUDIT")
    if not path:
        return
    with open(path, "a", encoding="utf-8") as stream:
        stream.write(json.dumps(packet, separators=(",", ":")) + "\n")


def send(packet: dict[str, Any]) -> None:
    audit({"out": packet})
    sys.stdout.write(json.dumps(packet, separators=(",", ":")) + "\n")
    sys.stdout.flush()


def result(identifier: int | str, value: dict[str, Any]) -> None:
    send({"jsonrpc": "2.0", "id": identifier, "result": value})


def emit(method: str, params: dict[str, Any], identifier: int | str | None = None) -> None:
    packet: dict[str, Any] = {"jsonrpc": "2.0", "method": method, "params": params}
    if identifier is not None:
        packet["id"] = identifier
    send(packet)


def thread_value() -> dict[str, Any]:
    return {"thread": {"id": THREAD_ID, "cwd": THREAD_CWD, "turns": turns}}


def read_packet() -> dict[str, Any] | None:
    line = sys.stdin.readline()
    if not line:
        return None
    packet = json.loads(line)
    audit({"in": packet})
    return packet


def wait_for_native_request(identifier: int | str) -> dict[str, Any] | None:
    """Wait for the bridge's response to a server request, or an interrupt."""
    while True:
        packet = read_packet()
        if packet is None:
            return None
        if packet.get("id") == identifier and "result" in packet:
            return packet
        if packet.get("method") == "turn/interrupt":
            request_id = packet.get("id")
            if request_id is not None:
                result(request_id, {})
            return {"interrupted": True}
        if packet.get("method") == "thread/read":
            request_id = packet.get("id")
            if request_id is not None:
                result(request_id, thread_value())
            continue
        request_id = packet.get("id")
        if request_id is not None and "method" in packet:
            result(request_id, {})


def complete_turn(turn_id: str, status: str) -> None:
    turn = {"id": turn_id, "status": status}
    turns.append(turn)
    emit("turn/completed", {"threadId": THREAD_ID, "turn": turn})


def start_turn(identifier: int | str, params: dict[str, Any]) -> None:
    global turn_number
    turn_number += 1
    turn_id = f"native-turn-{turn_number}"
    result(identifier, {"turn": {"id": turn_id, "status": "inProgress"}})
    # Let the bridge publish active_turn_id after its turn/start response
    # before native notifications arrive.
    time.sleep(0.2)
    emit("turn/started", {"thread": {"id": THREAD_ID}, "turn": {"id": turn_id}})
    items = params.get("input")
    text = ""
    if isinstance(items, list) and items and isinstance(items[0], dict):
        text = str(items[0].get("text", ""))
    if text == "approval":
        request_id = "native-approval-request"
        emit("item/commandExecution/requestApproval", {
            "threadId": THREAD_ID,
            "turnId": turn_id,
            "itemId": "command-approval-item",
            "reason": "fixture approval",
        }, request_id)
        response = wait_for_native_request(request_id)
        if response and response.get("interrupted"):
            complete_turn(turn_id, "interrupted")
        else:
            emit("item/commandExecution/requestApproval/accepted", {
                "threadId": THREAD_ID,
                "turnId": turn_id,
                "itemId": "command-approval-item",
                "result": response.get("result") if response else None,
            })
            complete_turn(turn_id, "completed")
    elif text == "user-input":
        request_id = "native-user-input-request"
        emit("item/tool/requestUserInput", {
            "threadId": THREAD_ID,
            "turnId": turn_id,
            "itemId": "user-input-item",
            "questions": [{
                "id": "answer",
                "header": "Answer",
                "question": "fixture question",
                "options": [{"label": "Yes", "description": "accept fixture input"}],
            }],
        }, request_id)
        response = wait_for_native_request(request_id)
        if response and response.get("interrupted"):
            complete_turn(turn_id, "interrupted")
        else:
            emit("item/tool/requestUserInput/accepted", {
                "threadId": THREAD_ID,
                "turnId": turn_id,
                "itemId": "user-input-item",
                "result": response.get("result") if response else None,
            })
            complete_turn(turn_id, "completed")
    elif text == "elicitation":
        request_id = "native-elicitation-request"
        emit("mcpServer/elicitation/request", {
            "threadId": THREAD_ID,
            "turnId": turn_id,
            "serverName": "fixture-mcp",
            "message": "fixture elicitation",
            "requestedSchema": {
                "type": "object",
                "properties": {"value": {"type": "string"}},
                "required": ["value"],
            },
        }, request_id)
        response = wait_for_native_request(request_id)
        if response and response.get("interrupted"):
            complete_turn(turn_id, "interrupted")
        else:
            emit("mcpServer/elicitation/accepted", {
                "threadId": THREAD_ID,
                "turnId": turn_id,
                "result": response.get("result") if response else None,
            })
            complete_turn(turn_id, "completed")
    elif text == "interrupt":
        packet = wait_for_native_request("never-issued")
        complete_turn(turn_id, "interrupted" if packet and packet.get("interrupted") else "completed")
    else:
        emit("item/agentMessage", {"turn_id": turn_id, "text": "fixture response"})
        complete_turn(turn_id, "completed")


def main() -> int:
    global THREAD_CWD
    # The wrapper passes app-server exactly as the only argument.  Keep the
    # audit so the integration test can prove no model/tool/auth overrides
    # were injected into the external process.
    audit({"argv": sys.argv[1:]})
    for line in sys.stdin:
        packet = json.loads(line)
        audit({"in": packet})
        method = packet.get("method")
        identifier = packet.get("id")
        params = packet.get("params")
        if method == "initialize":
            result(identifier, {"serverInfo": {"name": "fake-codex", "version": "test"}})
        elif method == "initialized":
            continue
        elif method == "thread/start":
            if isinstance(params, dict) and isinstance(params.get("cwd"), str):
                THREAD_CWD = params["cwd"]
            result(identifier, thread_value())
        elif method == "thread/read":
            result(identifier, thread_value())
        elif method == "turn/start":
            start_turn(identifier, params if isinstance(params, dict) else {})
        elif method == "turn/interrupt":
            # The active turn's blocking loop handles this and emits the
            # terminal event.  This branch is for a bridge that interrupts
            # before the fixture enters that loop.
            result(identifier, {})
        else:
            if identifier is not None:
                result(identifier, {})
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
