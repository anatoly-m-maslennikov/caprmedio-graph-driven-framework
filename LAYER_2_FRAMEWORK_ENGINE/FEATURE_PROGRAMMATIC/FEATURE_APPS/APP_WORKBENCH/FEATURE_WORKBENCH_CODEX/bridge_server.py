# CA-R-2791@1
# CA-M-475@1
# CA-D-680@1

"""Loopback HTTP/SSE server for the Workbench Codex bridge."""

from __future__ import annotations

import argparse
from collections.abc import Sequence
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from itertools import chain
import json
import os
from pathlib import Path
from typing import Any
from urllib.parse import urlsplit

from bridge import CodexBridge
from state import runtime_directory


def _origin(url: str) -> str:
    value = urlsplit(url)
    if value.scheme not in {"http", "https"} or not value.netloc:
        raise ValueError("mcp_url must have an HTTP origin")
    return f"{value.scheme}://{value.netloc}"


def _handler(bridge: CodexBridge, origin: str) -> type[BaseHTTPRequestHandler]:  # noqa: C901
    class Handler(BaseHTTPRequestHandler):
        def _allowed(self) -> bool:
            if self.headers.get("Origin") == origin:
                return True
            self.send_error(403, "Unexpected Origin")
            return False

        def _body(self) -> dict[str, Any]:
            value = json.loads(self.rfile.read(int(self.headers.get("Content-Length", "0"))))
            if not isinstance(value, dict):
                raise ValueError("JSON object required")
            return value

        def _json(self, value: Any, status: int = 200) -> None:
            self.send_response(status)
            self.send_header("Content-Type", "application/json")
            self.send_header("Access-Control-Allow-Origin", origin)
            self.end_headers()
            self.wfile.write(json.dumps(value).encode())

        def do_OPTIONS(self) -> None:  # noqa: N802
            if not self._allowed():
                return
            self.send_response(204)
            self.send_header("Access-Control-Allow-Origin", origin)
            self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
            self.send_header("Access-Control-Allow-Headers", "Content-Type")
            self.end_headers()

        def do_GET(self) -> None:  # noqa: N802
            if self.path == "/health":
                self.send_response(200 if bridge.ready else 503)
                self.end_headers()
                self.wfile.write(b'{"ready":true}')
                return
            if not self._allowed():
                return
            try:
                if self.path != "/conversation":
                    raise ValueError("Unknown endpoint")
                self._json(bridge.conversation())
            except Exception as error:
                self._json({"error": str(error)}, 400)

        def do_POST(self) -> None:  # noqa: N802
            if not self._allowed():
                return
            try:
                body = self._body()
                if self.path == "/turn":
                    self._turn(body)
                elif self.path == "/respond":
                    self._respond(body)
                elif self.path == "/interrupt":
                    self._interrupt(body)
                else:
                    raise ValueError("Unknown endpoint")
            except Exception as error:
                self._json({"error": str(error)}, 400)

        def _respond(self, body: dict[str, Any]) -> None:
            if set(body) != {"id", "result"} or not isinstance(body["id"], (int, str)):
                raise ValueError("Expected id and result")
            bridge.respond(body["id"], body["result"])
            self._json({"ok": True})

        def _interrupt(self, body: dict[str, Any]) -> None:
            if set(body) != {"turn_id"} or not isinstance(body["turn_id"], str):
                raise ValueError("Expected turn_id")
            bridge.interrupt(body["turn_id"])
            self._json({"ok": True})

        def _turn(self, body: dict[str, Any]) -> None:
            if set(body) != {"message"} or not isinstance(body["message"], str):
                raise ValueError("Expected message")
            turn_id, initial = bridge.start_turn(body["message"])
            self.send_response(200)
            self.send_header("Content-Type", "text/event-stream")
            self.send_header("Cache-Control", "no-cache")
            self.send_header("Access-Control-Allow-Origin", origin)
            self.end_headers()
            self._event({"type": "started", "thread_id": bridge.thread_id, "turn_id": turn_id})
            status = "completed"
            for packet in chain(initial, bridge.events()):
                self._event({"type": "event", "thread_id": bridge.thread_id, "turn_id": turn_id, "event": packet})
                status = self._status(packet, status)
            self._event({"type": "finished", "thread_id": bridge.thread_id, "turn_id": turn_id, "status": status})

        @staticmethod
        def _status(packet: dict[str, Any], default: str) -> str:
            if packet.get("method") == "bridge/failed":
                return "failed"
            if packet.get("method") != "turn/completed" or not isinstance(packet.get("params"), dict):
                return default
            turn = packet["params"].get("turn")
            return turn.get("status", default) if isinstance(turn, dict) else default

        def _event(self, value: dict[str, Any]) -> None:
            self.wfile.write(b"data: " + json.dumps(value).encode() + b"\n\n")
            self.wfile.flush()

        def log_message(self, _format: str, *_args: Any) -> None:
            pass

    return Handler


def serve(project_root: Path, mcp_url: str) -> ThreadingHTTPServer:
    root, origin = Path(project_root).resolve(strict=True), _origin(mcp_url)
    bridge = CodexBridge(root, mcp_url)
    server = ThreadingHTTPServer(("127.0.0.1", 0), _handler(bridge, origin))
    directory = runtime_directory(root)
    directory.mkdir(parents=True, exist_ok=True)
    url = f"http://127.0.0.1:{server.server_address[1]}"
    (directory / "bridge.json").write_text(
        json.dumps({"url": url, "ready": True, "pid": os.getpid(), "owned_pid": os.getpid(), "project_root": str(root)}) + "\n"
    )
    server.codex_bridge = bridge  # type: ignore[attr-defined]
    return server


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--project-root", required=True, type=Path)
    parser.add_argument("--mcp-url", required=True)
    args = parser.parse_args(argv)
    server = serve(args.project_root, args.mcp_url)
    print(f"http://127.0.0.1:{server.server_address[1]}", flush=True)
    try:
        server.serve_forever()
    finally:
        server.codex_bridge.close()  # type: ignore[attr-defined]
        server.server_close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
