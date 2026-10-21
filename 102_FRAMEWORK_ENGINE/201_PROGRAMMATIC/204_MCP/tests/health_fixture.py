"""Canonical disposable provider and ASGI fixture for MCP health tests."""
from pathlib import Path
import sys
import tempfile
import unittest

import httpx2
from mcp.client.session import ClientSession
from mcp.client.streamable_http import streamable_http_client


APP = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(APP))
from http_server import create_app  # noqa: E402


SECRET = "HEALTH_FIXTURE_SECRET"
PROVIDER_DIAGNOSTIC = "provider diagnostic /fixture/absolute/path"


class HealthHTTPFixture(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        directory = APP.parents[2] / ".caprmedio_tmp/tests/mcp-health"
        directory.mkdir(parents=True, exist_ok=True)
        self.temp = tempfile.TemporaryDirectory(dir=directory, ignore_cleanup_errors=True)
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.source = self.root / "provider.py"
        self.marker = self.root / "provider.calls"
        self._write_provider()
        self.app = create_app(self.root, implementation=self.source)

    def _write_provider(self):
        self.source.write_text(
            "import asyncio\n"
            "from pathlib import Path\n"
            "from mcp.server import MCPServer\n"
            f"MARKER = Path({str(self.marker)!r})\n"
            "server = MCPServer('health-fixture')\n"
            "def mark(value):\n"
            "    with MARKER.open('a', encoding='utf-8') as stream:\n"
            "        stream.write(value + '\\n')\n"
            "@server.tool(name='success', structured_output=True)\n"
            "def success(secret: str = '') -> dict[str, str]:\n"
            "    mark('success')\n"
            "    return {'outcome': 'completed', 'secret': secret, 'result': 'fixture-result'}\n"
            "@server.tool(name='partial', structured_output=True)\n"
            "def partial() -> dict[str, str]:\n"
            "    return {'outcome': 'partial', 'result': 'partial-result'}\n"
            "@server.tool(name='unsafe', structured_output=True)\n"
            f"def unsafe() -> dict[str, str]:\n    return {{'outcome': {SECRET!r}, 'disposition': {PROVIDER_DIAGNOSTIC!r}, 'error': {SECRET!r}}}\n"
            "@server.tool(name='raise_error', structured_output=True)\n"
            "def raise_error() -> dict[str, str]:\n"
            f"    raise RuntimeError({PROVIDER_DIAGNOSTIC!r})\n"
            "@server.tool(name='alpha', structured_output=True)\n"
            "async def alpha(delay: float = 0.02) -> dict[str, str]:\n"
            "    await asyncio.sleep(delay)\n"
            "    return {'outcome': 'completed', 'worker': 'alpha'}\n"
            "@server.tool(name='beta', structured_output=True)\n"
            "async def beta(delay: float = 0.02) -> dict[str, str]:\n"
            "    await asyncio.sleep(delay)\n"
            "    return {'outcome': 'completed', 'worker': 'beta'}\n"
            "@server.tool(name='slow', structured_output=True)\n"
            "async def slow(delay: float = 30.0) -> dict[str, str]:\n"
            "    mark('slow-started')\n"
            "    await asyncio.sleep(delay)\n"
            "    return {'outcome': 'completed', 'worker': 'slow'}\n"
            "server.run(transport='stdio')\n",
            encoding="utf-8",
        )

    def headers(self, **extra):
        return {"host": "127.0.0.1:18092", **extra}

    def lifespan(self):
        return self.app.starlette_app.router.lifespan_context(self.app.starlette_app)

    def new_app(self):
        return create_app(self.root, implementation=self.source)

    def raw_client(self):
        return httpx2.AsyncClient(
            transport=httpx2.ASGITransport(app=self.app),
            base_url="http://127.0.0.1:18092",
        )

    async def session(self):
        client = httpx2.AsyncClient(
            transport=httpx2.ASGITransport(app=self.app),
            base_url="http://127.0.0.1:18092",
        )
        transport = streamable_http_client(
            "http://127.0.0.1:18092/mcp", http_client=client
        )
        streams = await transport.__aenter__()
        session = ClientSession(*streams)
        await session.__aenter__()
        await session.initialize()
        return client, transport, session

    async def close_session(self, client, transport, session):
        await session.__aexit__(None, None, None)
        await transport.__aexit__(None, None, None)
        await client.aclose()

    @staticmethod
    def outcome(row):
        return row.get("outcome", row.get("actual_outcome"))

    @staticmethod
    def run_id(row):
        return row.get("run_id", row.get("workflow_run_id", row.get("actual_run_id")))


if __name__ == "__main__":
    unittest.main()
