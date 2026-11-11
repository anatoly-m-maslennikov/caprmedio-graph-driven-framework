"""Focused MCP image/process/gateway failure-boundary checks."""

from contextlib import redirect_stderr
import io
import json
import sys
from pathlib import Path
from types import SimpleNamespace
import unittest
from unittest.mock import AsyncMock, patch

from mcp import types

MCP = Path(__file__).resolve().parents[1]
TOOLS = MCP.parent / "FEATURE_TOOLS"
for directory in (MCP, TOOLS):
    if str(directory) not in sys.path:
        sys.path.insert(0, str(directory))

import direct_gateway  # noqa: E402
import http_server  # noqa: E402
import server  # noqa: E402
from operation_error_boundary import FailureRecord  # noqa: E402
import runtime_process_boundary  # noqa: E402

WARNING = FailureRecord("WARNING", "internal_failure", "operation failure")


class GatewayErrorBoundaryTests(unittest.IsolatedAsyncioTestCase):
    def _gateway(self):
        gateway = direct_gateway.DirectGateway(Path(self.tempdir.name))
        gateway.registry = SimpleNamespace(permits=lambda name: name == 'query_check')
        return gateway

    async def test_public_call_boundary_returns_safe_failure(self):
        gateway = self._gateway()
        params = types.CallToolRequestParams(name="query_check", arguments={})
        with (
            patch.object(gateway, "_call", new=AsyncMock(side_effect=ValueError("secret=private"))),
            patch.object(direct_gateway, "report_failure", return_value=(WARNING, None)) as reported,
        ):
            response = await gateway.call(None, params)
        self.assertTrue(response.is_error)
        self.assertEqual("failed", response.structured_content["outcome"])
        self.assertNotIn("private", json.dumps(response.structured_content))
        reported.assert_called_once()

    async def test_health_observer_record_failure_warns_without_replacing_result(self):
        gateway = self._gateway()
        response = direct_gateway.result({"outcome": "success"})
        with patch.object(gateway, "_call", new=AsyncMock(return_value=response)), patch.object(
            gateway.health_observations, "record", side_effect=ValueError("private")), patch.object(
            direct_gateway, "report_failure", return_value=(WARNING, None)) as reported:
            actual = await gateway.call(None, types.CallToolRequestParams(name="query_check", arguments={}))
        self.assertIs(response, actual)
        reported.assert_called_once()
        self.assertEqual(("WARNING", "health_observation_failed"),
                         (reported.call_args.args[1].severity, reported.call_args.args[1].code))

    async def asyncSetUp(self):
        self.tempdir = __import__("tempfile").TemporaryDirectory()
        self.addAsyncCleanup(self.tempdir.cleanup)


class HTTPBoundaryTests(unittest.IsolatedAsyncioTestCase):
    async def _guard(self, host, origin=None):
        messages = []

        async def app(_scope, _receive, _send):
            self.fail("refused request reached the MCP app")

        guard = http_server.LoopbackGuard(app)
        guard.gateway = SimpleNamespace(root=Path(self.tempdir.name))
        headers = [(b"host", host.encode())]
        if origin is not None:
            headers.append((b"origin", origin.encode()))
        scope = {"type": "http", "method": "GET", "path": "/health",
                 "headers": headers, "query_string": b"", "http_version": "1.1"}
        async def send(message):
            messages.append(message)

        with patch.object(http_server, "report_failure", return_value=(WARNING, None)) as reported:
            await guard._call(scope, lambda: None, send)
        return messages, reported

    async def test_host_and_origin_refusals_warn_without_crashing(self):
        host_messages, host_report = await self._guard("attacker.invalid")
        origin_messages, origin_report = await self._guard("127.0.0.1:8092", "https://attacker.invalid")
        self.assertEqual(421, host_messages[0]["status"])
        self.assertEqual(403, origin_messages[0]["status"])
        host_report.assert_called_once()
        origin_report.assert_called_once()

    async def test_health_observer_failure_is_visible_without_changing_readiness(self):
        class BrokenObserver:
            def snapshot(self):
                raise ValueError("secret=must-not-leak")

        gateway = SimpleNamespace(
            root=Path(self.tempdir.name),
            ready=True,
            health_observations=BrokenObserver(),
        )
        request = SimpleNamespace(headers={"accept": "application/json"})
        with patch.object(http_server, "report_failure", return_value=(WARNING, None)) as reported:
            response = await http_server.health(request, gateway)
        payload = json.loads(response.body)
        self.assertEqual(200, response.status_code)
        self.assertTrue(payload["ready"])
        self.assertEqual("health observations unavailable", payload["health_warning"])
        self.assertNotIn("must-not-leak", response.body.decode())
        reported.assert_called_once()

    async def asyncSetUp(self):
        self.tempdir = __import__("tempfile").TemporaryDirectory()
        self.addAsyncCleanup(self.tempdir.cleanup)


class ProcessBoundaryTests(unittest.TestCase):
    def test_process_boundary_emits_one_sanitized_fallback(self):
        root = Path(self.tempdir.name)
        with (
            patch.object(runtime_process_boundary, "report_failure",
                         return_value=(WARNING, "logger unavailable")) as reported,
            redirect_stderr(io.StringIO()) as stderr,
        ):
            code = runtime_process_boundary.run_process(
                lambda: (_ for _ in ()).throw(ValueError("token=private")),
                root=root, operation="mcp.startup",
            )
        self.assertEqual(2, code)
        self.assertNotIn("private", stderr.getvalue())
        reported.assert_called_once()

    def test_http_delegation_has_one_process_owner(self):
        with (
            patch.object(server, "run_process", side_effect=AssertionError("duplicate boundary")),
            patch("http_server.main", return_value=0) as delegated,
        ):
            result = server.main(["--project-root", self.tempdir.name, "--transport", "streamable-http"])
        self.assertEqual(0, result)
        delegated.assert_called_once_with(["--project-root", self.tempdir.name])

    def setUp(self):
        self.tempdir = __import__("tempfile").TemporaryDirectory()
        self.addCleanup(self.tempdir.cleanup)


if __name__ == "__main__":
    unittest.main()
