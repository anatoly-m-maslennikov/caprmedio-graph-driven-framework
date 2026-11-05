# CA-R-2791@1
# CA-M-475@1
# CA-D-680@1

"""Small JSON-RPC stdio client for the installed Codex app-server."""

from __future__ import annotations

from collections.abc import Callable
import json
from pathlib import Path
import shutil
import subprocess
import threading
from typing import Any


class AppServer:
    def __init__(self, project_root: Path, mcp_url: str, on_event: Callable[[dict[str, Any]], None]) -> None:
        codex = shutil.which("codex")
        if codex is None:
            raise RuntimeError("Codex CLI is unavailable")
        self._events, self._next_id = on_event, 1
        self._responses: dict[int | str, dict[str, Any]] = {}
        self._waiting = threading.Condition()
        override = f"mcp_servers.caprmedio.url={json.dumps(mcp_url)}"
        self.process = subprocess.Popen(
            [codex, "-c", override, "app-server"],
            cwd=project_root,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=None,
            text=True,
            bufsize=1,
        )
        self._reader = threading.Thread(target=self._read, daemon=True)
        self._reader.start()
        self.request("initialize", {"clientInfo": {"name": "caprmedio-workbench", "version": "1"}})
        self._write({"jsonrpc": "2.0", "method": "initialized", "params": {}})

    def _read(self) -> None:
        assert self.process.stdout is not None
        try:
            for line in self.process.stdout:
                try:
                    packet = json.loads(line)
                except ValueError:
                    continue
                if self._is_response(packet):
                    with self._waiting:
                        self._responses[packet["id"]] = packet
                        self._waiting.notify_all()
                elif isinstance(packet, dict):
                    self._events(packet)
        finally:
            with self._waiting:
                self._waiting.notify_all()
            self._events({"method": "bridge/failed", "params": {"message": "Codex app-server stopped"}})

    @staticmethod
    def _is_response(packet: object) -> bool:
        return (
            isinstance(packet, dict)
            and isinstance(packet.get("id"), (int, str))
            and ("result" in packet or "error" in packet)
        )

    def request(self, method: str, params: dict[str, Any]) -> dict[str, Any]:
        with self._waiting:
            identifier, self._next_id = self._next_id, self._next_id + 1
        self._write({"jsonrpc": "2.0", "id": identifier, "method": method, "params": params})
        with self._waiting:
            while identifier not in self._responses:
                if self.process.poll() is not None:
                    raise RuntimeError("Codex app-server stopped")
                self._waiting.wait(0.2)
            response = self._responses.pop(identifier)
        if "error" in response:
            raise RuntimeError(str(response["error"]))
        value = response.get("result")
        if not isinstance(value, dict):
            raise RuntimeError("Codex app-server returned an invalid result")
        return value

    def respond(self, identifier: int | str, result: Any) -> None:
        self._write({"jsonrpc": "2.0", "id": identifier, "result": result})

    def _write(self, packet: dict[str, Any]) -> None:
        if self.process.stdin is None or self.process.poll() is not None:
            raise RuntimeError("Codex app-server is unavailable")
        self.process.stdin.write(json.dumps(packet, separators=(",", ":")) + "\n")
        self.process.stdin.flush()

    def close(self) -> None:
        if self.process.poll() is None:
            self.process.terminate()
            self.process.wait(timeout=3)
