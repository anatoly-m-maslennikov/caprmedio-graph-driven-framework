# CA-E-682@1

"""Real HTTP/SSE coverage for the one-Project Workbench Codex bridge.

The app-server is an external executable fixture on ``PATH``.  The bridge,
HTTP server, JSON-RPC process boundary and runtime files are real.  No
Workbench business service is mocked here.
"""

from __future__ import annotations

import http.client
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import threading
import time
import unittest
from typing import Any
from urllib.parse import urlsplit


CODEX_ROOT = Path(__file__).resolve().parents[1]
REPOSITORY = CODEX_ROOT.parents[4]
FIXTURE = Path(__file__).with_name("fixtures") / "fake_codex.py"
ALLOWED_ORIGIN = "http://127.0.0.1:56317"
MCP_URL = f"{ALLOWED_ORIGIN}/caprmedio/mcp"
FORBIDDEN_OVERRIDE_KEYS = {
    "model",
    "modelProvider",
    "model_provider",
    "toolConfig",
    "tool_config",
    "allowedTools",
    "allowed_tools",
    "mcpServers",
    "mcp_servers",
    "approvalPolicy",
    "approval_policy",
    "sandbox",
    "auth",
    "credentials",
}


def _bridge_server() -> Path | None:
    configured = os.environ.get("CAPRMEDIO_CODEX_BRIDGE_SERVER")
    path = Path(configured) if configured else CODEX_ROOT / "bridge_server.py"
    return path if path.is_file() else None


def _write_codex_path_fixture(directory: Path) -> None:
    """Install a real executable named ``codex`` in the test PATH."""
    executable = directory / "codex"
    executable.write_text(
        "#!/bin/sh\n"
        f"exec {shutil.which('python3') or sys.executable} {FIXTURE} \"$@\"\n",
        encoding="utf-8",
    )
    executable.chmod(0o755)


class BridgeHTTPTests(unittest.TestCase):
    """Exercise the public bridge wire, not its private Python classes."""

    @classmethod
    def setUpClass(cls) -> None:
        bridge = _bridge_server()
        if bridge is None:
            raise unittest.SkipTest("bridge_server.py is not available yet")
        temp_parent = REPOSITORY / ".caprmedio_tmp/workbench-codex-http"
        temp_parent.mkdir(parents=True, exist_ok=True)
        cls.temp = tempfile.TemporaryDirectory(dir=temp_parent)
        cls.root = Path(cls.temp.name) / "project"
        (cls.root / ".caprmedio_caprmedio").mkdir(parents=True)
        fake_bin = Path(cls.temp.name) / "bin"
        fake_bin.mkdir()
        _write_codex_path_fixture(fake_bin)
        cls.audit = Path(cls.temp.name) / "fake-codex.jsonl"
        environment = os.environ.copy()
        environment["PATH"] = f"{fake_bin}{os.pathsep}{environment.get('PATH', '')}"
        environment["FAKE_CODEX_AUDIT"] = str(cls.audit)
        cls.process = subprocess.Popen(
            [
                sys.executable,
                str(bridge),
                "--project-root",
                str(cls.root),
                "--mcp-url",
                MCP_URL,
            ],
            cwd=REPOSITORY,
            env=environment,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        cls.addClassCleanup(cls._stop_server)
        cls.base_url = cls._wait_for_bridge()

    @classmethod
    def _wait_for_bridge(cls) -> str:
        state = cls.root / ".caprmedio_runtime/workbench/codex/bridge.json"
        deadline = time.monotonic() + 15
        while time.monotonic() < deadline:
            if cls.process.poll() is not None:
                stdout = cls.process.stdout.read() if cls.process.stdout else ""
                stderr = cls.process.stderr.read() if cls.process.stderr else ""
                raise AssertionError(f"Codex bridge exited\nstdout:\n{stdout}\nstderr:\n{stderr}")
            try:
                value = json.loads(state.read_text(encoding="utf-8"))
                if value.get("ready") is True and isinstance(value.get("url"), str):
                    return value["url"].rstrip("/")
            except (OSError, ValueError):
                pass
            time.sleep(0.05)
        raise AssertionError("Codex bridge did not publish ready bridge.json")

    @classmethod
    def _stop_server(cls) -> None:
        process = getattr(cls, "process", None)
        if process is None:
            return
        if process.poll() is None:
            process.terminate()
            try:
                process.wait(timeout=5)
            except subprocess.TimeoutExpired:
                process.kill()
                process.wait(timeout=5)
        cls.temp.cleanup()

    @staticmethod
    def _endpoint(base_url: str, path: str) -> tuple[str, int, str]:
        parsed = urlsplit(base_url)
        return parsed.hostname or "127.0.0.1", parsed.port or 80, path

    def request(
        self,
        method: str,
        path: str,
        payload: dict[str, Any] | None = None,
        *,
        origin: str | None = ALLOWED_ORIGIN,
    ) -> tuple[int, dict[str, str], bytes]:
        host, port, request_path = self._endpoint(self.base_url, path)
        connection = http.client.HTTPConnection(host, port, timeout=10)
        body = json.dumps(payload).encode("utf-8") if payload is not None else None
        headers = {"Accept": "application/json"}
        if body is not None:
            headers["Content-Type"] = "application/json"
        if origin is not None:
            headers["Origin"] = origin
        connection.request(method, request_path, body=body, headers=headers)
        response = connection.getresponse()
        result = (response.status, dict(response.getheaders()), response.read())
        connection.close()
        return result

    def json_request(
        self,
        method: str,
        path: str,
        payload: dict[str, Any] | None = None,
        *,
        origin: str | None = ALLOWED_ORIGIN,
    ) -> tuple[int, dict[str, Any]]:
        status, _, body = self.request(method, path, payload, origin=origin)
        return status, json.loads(body or b"{}")

    def open_turn(self, message: str) -> tuple[http.client.HTTPConnection, http.client.HTTPResponse]:
        host, port, path = self._endpoint(self.base_url, "/turn")
        connection = http.client.HTTPConnection(host, port, timeout=20)
        connection.request(
            "POST",
            path,
            body=json.dumps({"message": message}).encode("utf-8"),
            headers={
                "Accept": "text/event-stream",
                "Content-Type": "application/json",
                "Origin": ALLOWED_ORIGIN,
            },
        )
        response = connection.getresponse()
        self.assertEqual(200, response.status)
        return connection, response

    @staticmethod
    def read_sse(response: http.client.HTTPResponse) -> list[dict[str, Any]]:
        events: list[dict[str, Any]] = []
        data: list[str] = []
        while True:
            raw = response.readline()
            if not raw:
                break
            line = raw.decode("utf-8").rstrip("\r\n")
            if line.startswith("data:"):
                data.append(line[5:].lstrip())
            elif not line and data:
                events.append(json.loads("\n".join(data)))
                data.clear()
        if data:
            events.append(json.loads("\n".join(data)))
        return events

    def wait_for_pending(self, request_id: str) -> dict[str, Any]:
        deadline = time.monotonic() + 5
        while time.monotonic() < deadline:
            status, value = self.json_request("GET", "/conversation")
            self.assertEqual(200, status)
            pending = value.get("pending_requests", [])
            if any(
                item == request_id
                or (isinstance(item, dict) and item.get("id") == request_id)
                for item in pending
            ):
                return value
            time.sleep(0.05)
        self.fail(f"native request {request_id!r} did not reach the bridge")

    def collect_turn(
        self,
        connection: http.client.HTTPConnection,
        response: http.client.HTTPResponse,
        output: dict[str, list[dict[str, Any]]],
    ) -> threading.Thread:
        def collect() -> None:
            try:
                output["events"] = self.read_sse(response)
            finally:
                connection.close()

        thread = threading.Thread(target=collect, daemon=True)
        thread.start()
        return thread

    def test_persistent_thread_streams_native_ids_and_interactions(self) -> None:
        status, first = self.json_request("GET", "/conversation")
        self.assertEqual(200, status)
        self.assertEqual("native-thread-1", first["thread_id"])
        self.assertIsInstance(first["thread"], dict)
        self.assertEqual([], first["pending_requests"])

        status, resumed = self.json_request("GET", "/conversation")
        self.assertEqual(200, status)
        self.assertEqual(first["thread_id"], resumed["thread_id"])

        connection, response = self.open_turn("hello")
        output: dict[str, list[dict[str, Any]]] = {"events": []}
        reader = self.collect_turn(connection, response, output)
        reader.join(timeout=5)
        self.assertFalse(reader.is_alive())
        events = output["events"]
        started = next(item for item in events if item.get("type") == "started")
        streamed = next(
            item for item in events
            if item.get("type") == "event" and item.get("event", {}).get("method") == "item/agentMessage"
        )
        completed_native = next(
            item for item in events
            if item.get("type") == "event" and item.get("event", {}).get("method") == "turn/completed"
        )["event"]
        finished = next(item for item in events if item.get("type") == "finished")
        self.assertEqual("native-thread-1", started["thread_id"])
        self.assertEqual(started["turn_id"], streamed["turn_id"])
        self.assertEqual("item/agentMessage", streamed["event"]["method"])
        self.assertEqual("native-thread-1", completed_native["params"]["threadId"])
        self.assertEqual("completed", finished["status"])

        connection, response = self.open_turn("approval")
        approval_output: dict[str, list[dict[str, Any]]] = {"events": []}
        approval_reader = self.collect_turn(connection, response, approval_output)
        self.wait_for_pending("native-approval-request")
        status, _ = self.json_request(
            "POST", "/respond", {"id": "native-approval-request", "result": {"approved": True}}
        )
        self.assertEqual(200, status)
        approval_reader.join(timeout=5)
        self.assertFalse(approval_reader.is_alive())
        approval_event = next(
            item for item in approval_output["events"]
            if item.get("type") == "event"
            and item.get("event", {}).get("method") == "item/commandExecution/requestApproval"
        )["event"]
        self.assertEqual(
            {"threadId", "turnId", "itemId", "reason"},
            set(approval_event["params"]),
        )
        self.assertEqual(
            "item/commandExecution/requestApproval",
            approval_event["method"],
        )
        self.assertEqual(
            "completed",
            next(item for item in approval_output["events"] if item.get("type") == "finished")["status"],
        )

        connection, response = self.open_turn("user-input")
        input_output: dict[str, list[dict[str, Any]]] = {"events": []}
        input_reader = self.collect_turn(connection, response, input_output)
        self.wait_for_pending("native-user-input-request")
        status, _ = self.json_request(
            "POST",
            "/respond",
            {"id": "native-user-input-request", "result": {"answer": "yes"}},
        )
        self.assertEqual(200, status)
        input_reader.join(timeout=5)
        self.assertFalse(input_reader.is_alive())
        input_event = next(
            item for item in input_output["events"]
            if item.get("type") == "event"
            and item.get("event", {}).get("method") == "item/tool/requestUserInput"
        )["event"]
        self.assertEqual(
            {"threadId", "turnId", "itemId", "questions"},
            set(input_event["params"]),
        )
        self.assertEqual(
            {"id", "header", "question", "options"},
            set(input_event["params"]["questions"][0]),
        )
        self.assertEqual(
            "item/tool/requestUserInput",
            input_event["method"],
        )
        self.assertEqual(
            "completed",
            next(item for item in input_output["events"] if item.get("type") == "finished")["status"],
        )

        connection, response = self.open_turn("elicitation")
        elicitation_output: dict[str, list[dict[str, Any]]] = {"events": []}
        elicitation_reader = self.collect_turn(connection, response, elicitation_output)
        self.wait_for_pending("native-elicitation-request")
        status, _ = self.json_request(
            "POST",
            "/respond",
            {
                "id": "native-elicitation-request",
                "result": {"action": "accept", "content": {"value": "yes"}},
            },
        )
        self.assertEqual(200, status)
        elicitation_reader.join(timeout=5)
        self.assertFalse(elicitation_reader.is_alive())
        elicitation_event = next(
            item for item in elicitation_output["events"]
            if item.get("type") == "event"
            and item.get("event", {}).get("method") == "mcpServer/elicitation/request"
        )["event"]
        self.assertEqual("mcpServer/elicitation/request", elicitation_event["method"])
        self.assertEqual(
            "completed",
            next(item for item in elicitation_output["events"] if item.get("type") == "finished")["status"],
        )

        connection, response = self.open_turn("interrupt")
        interrupt_output: dict[str, list[dict[str, Any]]] = {"events": []}
        interrupt_reader = self.collect_turn(connection, response, interrupt_output)
        deadline = time.monotonic() + 5
        turn_id = None
        while time.monotonic() < deadline and turn_id is None:
            _, conversation = self.json_request("GET", "/conversation")
            turn_id = conversation.get("active_turn_id")
            if turn_id is None:
                time.sleep(0.05)
        self.assertIsInstance(turn_id, str)
        status, _ = self.json_request("POST", "/interrupt", {"turn_id": "not-the-active-turn"})
        self.assertEqual(400, status)
        status, _ = self.json_request("POST", "/interrupt", {"turn_id": turn_id})
        self.assertEqual(200, status)
        interrupt_reader.join(timeout=5)
        self.assertFalse(interrupt_reader.is_alive())
        self.assertEqual(
            "interrupted",
            next(item for item in interrupt_output["events"] if item.get("type") == "finished")["status"],
        )

        status, final = self.json_request("GET", "/conversation")
        self.assertEqual(200, status)
        self.assertEqual("native-thread-1", final["thread_id"])
        self.assertIsNone(final["active_turn_id"])
        self.assertEqual([], final["pending_requests"])
        self.assertGreaterEqual(len(final["thread"].get("turns", [])), 1)

    def test_origin_guard_health_route_and_runtime_state(self) -> None:
        # Establish the persistent state independently of unittest method
        # ordering; the rejection itself must not create a thread.
        status, _ = self.json_request("GET", "/conversation")
        self.assertEqual(200, status)
        status, _, _ = self.request("GET", "/conversation", origin="http://attacker.invalid")
        self.assertEqual(403, status)
        status, health = self.json_request("GET", "/health", origin=None)
        self.assertEqual(200, status)
        self.assertTrue(health.get("ready"))

        state = json.loads(
            (self.root / ".caprmedio_runtime/workbench/codex/thread.json").read_text(encoding="utf-8")
        )
        self.assertEqual({"thread_id"}, set(state))
        self.assertEqual("native-thread-1", state["thread_id"])

        audit = [json.loads(line) for line in self.audit.read_text(encoding="utf-8").splitlines()]
        argv = next(item["argv"] for item in audit if "argv" in item)
        self.assertEqual("app-server", argv[-1])
        self.assertIn("-c", argv)
        self.assertTrue(any(item.startswith("mcp_servers.caprmedio.url=") for item in argv))
        forbidden_flags = ("--model", "--tool", "--tools", "--auth", "--sandbox", "--approval")
        self.assertFalse(any(item == flag or item.startswith(flag + "=") for item in argv for flag in forbidden_flags))
        thread_starts = [
            item for item in audit
            if item.get("in", {}).get("method") == "thread/start"
        ]
        self.assertEqual(1, len(thread_starts))
        for packet in audit:
            incoming = packet.get("in")
            if not isinstance(incoming, dict):
                continue
            params = incoming.get("params")
            if isinstance(params, dict):
                self.assertFalse(FORBIDDEN_OVERRIDE_KEYS & set(params))


if __name__ == "__main__":
    unittest.main()
