"""Bounded transport checks; initialization proves no Release execution."""

from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path

from starlette.testclient import TestClient

MCP_ROOT = Path(__file__).resolve().parents[1]
if str(MCP_ROOT) not in sys.path:
    sys.path.insert(0, str(MCP_ROOT))

from http_server import MAX_REQUEST_BODY_SIZE, create_app  # noqa: E402


# The current execute JSON-RPC envelope measured 7,266,044 mostly ASCII
# characters. Initialization metadata with that byte size tests transport
# admission independently of any Operator authorization or Release Action.
CURRENT_RELEASE_ENVELOPE_BYTES = 7_266_044


class HttpRequestBodyLimitTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory(ignore_cleanup_errors=True)
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name).resolve()
        implementation = self.root / "transport_fixture.py"
        implementation.write_text(
            'from mcp.server import MCPServer\n'
            'MCPServer("transport fixture").run(transport="stdio")\n', encoding="utf-8",
        )
        self.client = TestClient(create_app(self.root, implementation=implementation),
                                 base_url="http://127.0.0.1:8092")
        self.client.__enter__()
        self.addCleanup(self.client.__exit__, None, None, None)
        self.headers = {"host": "127.0.0.1:8092", "content-type": "application/json",
                        "accept": "application/json, text/event-stream"}

    @staticmethod
    def current_size_initialize() -> bytes:
        value = {"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {
            "protocolVersion": "2025-11-25", "capabilities": {},
            "clientInfo": {"name": "body-limit-fixture", "version": "1"},
            "_meta": {"padding": ""},
        }}
        base = json.dumps(value, separators=(",", ":")).encode()
        value["params"]["_meta"]["padding"] = "x" * (CURRENT_RELEASE_ENVELOPE_BYTES - len(base))
        return json.dumps(value, separators=(",", ":")).encode()

    def test_current_release_envelope_size_is_admitted_to_real_mcp_transport(self) -> None:
        self.assertEqual(MAX_REQUEST_BODY_SIZE, 16 * 1024 * 1024)
        body = self.current_size_initialize()
        self.assertEqual(len(body), CURRENT_RELEASE_ENVELOPE_BYTES)
        self.assertGreater(len(body), 4 * 1024 * 1024)
        self.assertLess(len(body), MAX_REQUEST_BODY_SIZE)
        response = self.client.post("/mcp", headers=self.headers, content=body)
        self.assertEqual(response.status_code, 200)
        self.assertIn("mcp-session-id", response.headers)
        self.assertIn("protocolVersion", response.text)
        self.assertNotIn("gate_evidence_refs", response.text)

    def test_over_bound_declared_and_streamed_bodies_are_rejected(self) -> None:
        oversized = b"x" * (MAX_REQUEST_BODY_SIZE + 1)
        for body in (oversized, iter((oversized[:4 * 1024 * 1024], oversized[4 * 1024 * 1024:]))):
            with self.subTest(streamed=not isinstance(body, bytes)):
                response = self.client.post("/mcp", headers=self.headers, content=body)
                self.assertEqual(response.status_code, 413)
                self.assertNotIn("mcp-session-id", response.headers)

    def test_larger_transport_policy_preserves_host_and_origin_admission(self) -> None:
        body = self.current_size_initialize()
        for extra, status in (({"host": "attacker.invalid"}, 421),
                              ({"origin": "https://attacker.invalid"}, 403)):
            with self.subTest(extra=extra):
                response = self.client.post("/mcp", headers={**self.headers, **extra}, content=body)
                self.assertEqual(response.status_code, status)
                self.assertNotIn("mcp-session-id", response.headers)


if __name__ == "__main__":
    unittest.main()
