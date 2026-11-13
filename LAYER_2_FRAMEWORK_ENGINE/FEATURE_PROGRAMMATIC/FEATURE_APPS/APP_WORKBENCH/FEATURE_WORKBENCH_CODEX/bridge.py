# CA-R-2791@1
# CA-R-2792@1
# CA-M-475@1
# CA-D-680@1

"""One native Codex thread and turn stream for one selected Project."""

from __future__ import annotations

import json
from pathlib import Path
import threading
from typing import Any

from app_server import AppServer
from state import runtime_directory


class CodexBridge:
    def __init__(self, project_root: Path, mcp_url: str) -> None:
        self.root, self.mcp_url = Path(project_root).resolve(strict=True), mcp_url
        self.runtime = runtime_directory(self.root)
        self.thread_id: str | None = self._thread_id()
        self.active_turn_id: str | None = None
        self.pending_requests: dict[int | str, dict[str, Any]] = {}
        self._events: list[dict[str, Any]] = []
        self._condition = threading.Condition()
        self._conversation_lock = threading.Lock()
        self._turn_lock = threading.Lock()
        self._failure_message: str | None = None
        self.client = AppServer(self.root, self.mcp_url, self._event)

    def _thread_id(self) -> str | None:
        path = runtime_directory(self.root) / "thread.json"
        if not path.exists():
            return None
        try:
            value = json.loads(path.read_text())
        except (OSError, ValueError, TypeError):
            raise RuntimeError("Persisted Codex thread state is invalid") from None
        if not isinstance(value, dict) or not isinstance(value.get("thread_id"), str):
            raise RuntimeError("Persisted Codex thread state is invalid")
        return value["thread_id"]

    def _persist_thread(self) -> None:
        assert self.thread_id is not None
        self.runtime.mkdir(parents=True, exist_ok=True)
        (self.runtime / "thread.json").write_text(json.dumps({"thread_id": self.thread_id}) + "\n")

    def _event(self, packet: dict[str, Any]) -> None:
        params = packet.get("params")
        with self._condition:
            if isinstance(packet.get("id"), (int, str)) and isinstance(packet.get("method"), str):
                self.pending_requests[packet["id"]] = packet
            if packet.get("method") == "turn/completed" and isinstance(params, dict):
                turn = params.get("turn")
                if isinstance(turn, dict) and turn.get("id") == self.active_turn_id:
                    self.active_turn_id = None
            if packet.get("method") == "bridge/failed":
                failure = packet.get("params")
                message = failure.get("message", "Codex app-server stopped") if isinstance(failure, dict) else "Codex app-server stopped"
                self._failure_message = str(message)
                self.active_turn_id = None
            self._events.append(packet)
            self._condition.notify_all()

    def conversation(self) -> dict[str, Any]:
        with self._conversation_lock:
            if self.thread_id is None:
                value = self.client.request(
                    "thread/start",
                    {"cwd": str(self.root), "developerInstructions": f"CAPRMEDIO project_root: {self.root}"},
                )
                thread = value.get("thread", value)
                self.thread_id = thread.get("id") if isinstance(thread, dict) else None
                if not self.thread_id:
                    raise RuntimeError("Codex app-server did not return a thread ID")
                self._persist_thread()
            value = self.client.request("thread/read", {"threadId": self.thread_id, "includeTurns": True})
            thread = value.get("thread", value)
            if not isinstance(thread, dict) or not isinstance(thread.get("cwd"), str):
                raise RuntimeError("Codex app-server did not return the thread workspace")
            if Path(thread["cwd"]).resolve(strict=True) != self.root:
                raise RuntimeError("Persisted Codex thread belongs to another Project")
            return {
                "thread_id": self.thread_id,
                "thread": thread,
                "active_turn_id": self.active_turn_id,
                "pending_requests": list(self.pending_requests.values()),
            }

    def start_turn(self, message: str) -> tuple[str, list[dict[str, Any]]]:
        if not isinstance(message, str) or not message.strip():
            raise ValueError("message must be a non-empty string")
        with self._turn_lock:
            if self.active_turn_id is not None:
                raise ValueError("A Codex turn is already active")
            self.conversation()
            value = self.client.request(
                "turn/start", {"threadId": self.thread_id, "input": [{"type": "text", "text": message}]}
            )
            turn = value.get("turn", value)
            turn_id = turn.get("id") if isinstance(turn, dict) else None
            if not isinstance(turn_id, str):
                raise RuntimeError("Codex app-server did not return a turn ID")
            self.active_turn_id = turn_id
            initial = self._drain_events()
            if any(self._completed_turn(packet) == turn_id for packet in initial):
                self.active_turn_id = None
            return turn_id, initial

    @staticmethod
    def _completed_turn(packet: dict[str, Any]) -> str | None:
        params = packet.get("params")
        if packet.get("method") != "turn/completed" or not isinstance(params, dict):
            return None
        turn = params.get("turn")
        return turn.get("id") if isinstance(turn, dict) and isinstance(turn.get("id"), str) else None

    def events(self):
        while True:
            with self._condition:
                if not self._events:
                    if self.active_turn_id is None:
                        return
                    self._condition.wait(0.2)
                packets = self._drain_events()
            yield from packets

    def _drain_events(self) -> list[dict[str, Any]]:
        with self._condition:
            packets, self._events = self._events, []
            return packets

    def respond(self, identifier: int | str, result: Any) -> None:
        with self._condition:
            if identifier not in self.pending_requests:
                raise ValueError("Unknown Codex interaction")
        self.client.respond(identifier, result)
        with self._condition:
            self.pending_requests.pop(identifier, None)

    def interrupt(self, turn_id: str) -> None:
        if turn_id != self.active_turn_id or self.thread_id is None:
            raise ValueError("Turn is not active")
        self.client.request("turn/interrupt", {"threadId": self.thread_id, "turnId": turn_id})

    @property
    def ready(self) -> bool:
        return self._failure_message is None and self.client.process.poll() is None

    def close(self) -> None:
        self.client.close()
