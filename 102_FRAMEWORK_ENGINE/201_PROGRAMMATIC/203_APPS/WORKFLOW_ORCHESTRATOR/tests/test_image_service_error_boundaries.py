"""Focused process and Agent service failure-boundary checks."""

from contextlib import redirect_stderr, redirect_stdout
import asyncio
from concurrent.futures import CancelledError as FutureCancelledError
import io
import json
from pathlib import Path
import sys
import unittest
from unittest.mock import patch


APP = Path(__file__).resolve().parents[1]
DOCKER = APP / "docker"
for location in (APP, DOCKER):
    if str(location) not in sys.path:
        sys.path.insert(0, str(location))

import entrypoint  # noqa: E402
import agent_service  # noqa: E402
from operation_error_boundary import FailureRecord  # noqa: E402


class _Request:
    async def stream(self):
        yield b'{"context": {}, "phase": "check", "timeout": 1}'


class EntrypointFailureTests(unittest.TestCase):
    def run_mode(self, mode):
        stdout, stderr = io.StringIO(), io.StringIO()
        with (
            patch.object(sys, "argv", ["entrypoint.py", mode]),
            redirect_stdout(stdout),
            redirect_stderr(stderr),
        ):
            result = entrypoint.main()
        return result, stdout.getvalue(), stderr.getvalue()

    def stderr_records(self, stderr):
        records = [json.loads(line) for line in stderr.splitlines() if line]
        self.assertEqual(2, len(records), stderr)
        diagnostic, payload = records
        self.assertEqual("operation_failure", diagnostic["event"])
        self.assertEqual("DOCKER_ENTRYPOINT", diagnostic["component"])
        self.assertEqual(diagnostic["code"], payload["error"])
        return diagnostic, payload

    def test_invalid_mode_is_warning_and_keeps_protocol_stdout_clean(self):
        result, stdout, stderr = self.run_mode("unknown")
        diagnostic, payload = self.stderr_records(stderr)
        self.assertEqual(1, result)
        self.assertEqual("invalid_runtime_mode", payload["error"])
        self.assertEqual("WARNING", payload["severity"])
        self.assertEqual("WARNING", diagnostic["severity"])
        self.assertEqual("", stdout)

    def test_service_start_failure_is_explicit_runtime_error_on_stderr(self):
        with patch.object(entrypoint.os, "execv", side_effect=OSError("secret")):
            result, stdout, stderr = self.run_mode("mcp")
        diagnostic, payload = self.stderr_records(stderr)
        self.assertEqual(1, result)
        self.assertEqual("service_start_failed", payload["error"])
        self.assertEqual("ERROR", payload["severity"])
        self.assertEqual("ERROR", diagnostic["severity"])
        self.assertEqual("blocked", diagnostic["outcome"])
        self.assertEqual("", stdout)
        self.assertNotIn("secret", stderr)

    def test_health_process_has_no_project_prefix_fallback(self):
        with patch.object(entrypoint, "urlopen", side_effect=OSError("secret")):
            result, stdout, stderr = self.run_mode("agent-health")
        diagnostic, payload = self.stderr_records(stderr)
        self.assertEqual(1, result)
        self.assertEqual("agent_unavailable", payload["error"])
        self.assertNotIn("diagnostic_error", payload)
        self.assertEqual("ERROR", diagnostic["severity"])
        self.assertEqual("blocked", diagnostic["outcome"])
        self.assertEqual("", stdout)
        self.assertNotIn("secret", stderr)

    def test_missing_agent_auth_is_a_blocking_startup_failure(self):
        with (
            patch.dict("os.environ", {"CAPRMEDIO_AGENT_MODE": "codex"}),
            patch.object(entrypoint.Path, "is_file", return_value=False),
        ):
            result, stdout, stderr = self.run_mode("agent")
        diagnostic, payload = self.stderr_records(stderr)
        self.assertEqual(1, result)
        self.assertEqual("agent_auth_unavailable", payload["error"])
        self.assertEqual("ERROR", payload["severity"])
        self.assertEqual("ERROR", diagnostic["severity"])
        self.assertEqual("blocked", diagnostic["outcome"])
        self.assertEqual("", stdout)


class AgentServiceFailureTests(unittest.TestCase):
    def setUp(self):
        agent_service.busy = False
        agent_service.calls = 0

    def test_existing_request_error_contracts_emit_warning_without_payload_changes(self):
        from starlette.testclient import TestClient

        with TestClient(agent_service.app) as client:
            with patch.object(agent_service, "MAX_BYTES", 20):
                self.assertEqual(
                    {"error": "request_too_large"},
                    client.post("/execute", content=b"x" * 21).json(),
                )
            self.assertEqual(
                {"error": "invalid_dispatch"},
                client.post("/execute", json={"context": {}, "phase": "bad", "timeout": 1}).json(),
            )
            agent_service.busy = True
            self.assertEqual(
                {"error": "agent_busy"},
                client.post(
                    "/execute", json={"context": {}, "phase": "check", "timeout": 1}
                ).json(),
            )

    def test_malformed_context_is_502_and_busy_is_released(self):
        from starlette.testclient import TestClient

        with (
            TestClient(agent_service.app) as client,
            patch.object(agent_service, "execute", side_effect=KeyError("secret")),
        ):
            with redirect_stderr(io.StringIO()) as stderr:
                response = client.post(
                    "/execute", json={"context": {}, "phase": "check", "timeout": 1}
                )
        self.assertEqual(502, response.status_code)
        self.assertEqual({"error": "agent_execution_failed"}, response.json())
        self.assertFalse(agent_service.busy)
        self.assertNotIn("secret", stderr.getvalue())

    def test_future_cancellation_is_re_raised_after_busy_cleanup(self):
        async def run():
            with patch.object(
                agent_service.asyncio, "to_thread", side_effect=asyncio.CancelledError
            ):
                with self.assertRaises(asyncio.CancelledError):
                    await agent_service.submit(_Request())

        asyncio.run(run())
        self.assertFalse(agent_service.busy)

        async def future_run():
            with patch.object(agent_service.asyncio, "to_thread", side_effect=FutureCancelledError):
                with self.assertRaises(FutureCancelledError):
                    await agent_service.submit(_Request())

        asyncio.run(future_run())
        self.assertFalse(agent_service.busy)

    def test_report_failure_contract_accepts_structured_warning(self):
        with patch.object(
            agent_service,
            "report_failure",
            return_value=(FailureRecord("WARNING", "input_invalid", "request invalid"), None),
        ) as report:
            agent_service._request_error("input_invalid", "request invalid", "agent.execute")
        report.assert_called_once()
        self.assertIsNone(report.call_args.args[0])
        self.assertEqual("WARNING", report.call_args.args[1].severity)


if __name__ == "__main__":
    unittest.main()
