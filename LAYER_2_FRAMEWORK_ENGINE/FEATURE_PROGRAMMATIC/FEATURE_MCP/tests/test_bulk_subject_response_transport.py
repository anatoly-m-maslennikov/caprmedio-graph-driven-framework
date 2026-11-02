"""Large complete SSE results preserve the existing connected approval channel."""

from pathlib import Path
import sys
import unittest
from unittest.mock import patch

import httpx2
from mcp.client.session import ClientSession
from mcp.client.streamable_http import streamable_http_client

MCP_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(MCP_ROOT))
import hot_reload  # noqa: E402
import test_hot_reload_http as http_fixture  # noqa: E402


class BulkSubjectResponseTransportTests(unittest.IsolatedAsyncioTestCase):
    setUp = http_fixture.HTTPProtocolTests.setUp
    write = http_fixture.HTTPProtocolTests.write

    async def test_large_response_retains_request_scoped_backchannel(self):
        # The full611 measured SDK event is 9,427,872 bytes including both views.
        payload = "x" * (5 * 1024 * 1024)
        backchannels = []

        async def child_call(gateway, context, params, generation):
            backchannels.append(context.session.can_send_request)
            return hot_reload.result({"payload": payload})

        async with self.app.starlette_app.router.lifespan_context(self.app.starlette_app):
            async with httpx2.AsyncClient(
                transport=httpx2.ASGITransport(app=self.app),
                base_url="http://127.0.0.1:8092",
            ) as http:
                async with streamable_http_client(
                    "http://127.0.0.1:8092/mcp",
                    http_client=http,
                    max_sse_event_size=16 * 1024 * 1024,
                ) as streams:
                    async with ClientSession(*streams) as client:
                        await client.initialize()
                        with patch.object(hot_reload.Gateway, "_implementation_call", child_call):
                            response = await client.call_tool("echo", {})
        self.assertFalse(response.is_error)
        self.assertEqual(payload, response.structured_content["payload"])
        self.assertEqual([True], backchannels)
        wire = response.model_dump_json(by_alias=True).encode()
        self.assertGreater(len(wire), 9_427_872)
        self.assertLess(len(wire), 16 * 1024 * 1024)


if __name__ == "__main__":
    unittest.main()
