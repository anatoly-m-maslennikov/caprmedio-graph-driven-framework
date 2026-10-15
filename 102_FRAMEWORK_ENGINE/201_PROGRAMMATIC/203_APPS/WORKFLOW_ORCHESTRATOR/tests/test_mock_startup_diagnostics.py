"""Bounded mock startup evidence; no Docker daemon or live credentials."""

import asyncio
import io
from pathlib import Path
import subprocess
import unittest
from unittest.mock import AsyncMock, Mock, patch

import test_first_cut_http_docker_e2e as fixtures
from runtime import Runtime, _DIAGNOSTIC_LIMIT, _startup_diagnostic


class MockStartupDiagnosticsTests(unittest.TestCase):
    def test_failed_detached_mock_start_retains_exit_and_redacted_bounded_output(self):
        runtime = Runtime(Path.cwd(), mock=True)
        output = "Bearer bearer-canary\npassword=two word password\n" + "x" * 6000
        result = subprocess.CompletedProcess(
            [], 7, output, "network pool exhausted\nsecret=secret-canary"
        )
        with patch("runtime.subprocess.run", return_value=result) as execute:
            with self.assertRaises(RuntimeError) as caught:
                runtime.call("up", "-d", "--wait", "mcp-http", http=True)
        message = str(caught.exception)
        self.assertIn("exit 7", message)
        self.assertIn("network pool exhausted", message)
        self.assertNotIn("canary", message)
        self.assertNotIn("two word password", message)
        self.assertLessEqual(len(message), 2 * _DIAGNOSTIC_LIMIT + 100)
        self.assertEqual(1, execute.call_count)

    def test_production_auth_exec_logs_and_attached_start_failures_remain_generic(self):
        cases = (
            (False, None, ("up", "-d"), {}),
            (True, None, ("up", "-d"), {"authentication": True}),
            (True, "auth.json", ("up", "-d"), {}),
            (True, None, ("exec", "worker", "python"), {}),
            (True, None, ("logs",), {}),
            (True, None, ("up",), {}),
            (True, None, ("up", "-d"), {"capture": False}),
        )
        result = subprocess.CompletedProcess([], 1, "private-stdout", "private-stderr")
        for mock, auth_file, arguments, kwargs in cases:
            with self.subTest(mock=mock, arguments=arguments, kwargs=kwargs):
                runtime = Runtime(Path.cwd(), mock=mock, auth_file=auth_file)
                with patch("runtime.subprocess.run", return_value=result):
                    with self.assertRaises(RuntimeError) as caught:
                        runtime.call(*arguments, **kwargs)
                self.assertEqual(
                    "Docker operation failed; inspect service logs", str(caught.exception)
                )

    def test_successful_command_output_and_capture_false_are_unchanged(self):
        runtime = Runtime(Path.cwd(), mock=True)
        result = subprocess.CompletedProcess([], 0, "token=caller-output", "")
        with patch("runtime.subprocess.run", return_value=result):
            self.assertEqual("token=caller-output", runtime.call("up", "-d"))
            self.assertIsNone(runtime.call("up", "-d", capture=False))

    def test_recognizable_prefixed_credential_keys_are_redacted(self):
        for value in (
            "access_token=canary",
            "client_secret: canary",
            '"access_token":"canary"',
            "credential=canary",
            "credentials: canary",
            "api_token=canary",
        ):
            with self.subTest(value=value):
                output = _startup_diagnostic(value)
                self.assertNotIn("canary", output)
                self.assertIn("[redacted]", output)

    def test_redaction_precedes_truncation_and_removes_url_credentials(self):
        value = "token=" + "s" * 6000 + "\nhttps://user:url-password@registry.test/failure"
        output = _startup_diagnostic(value)
        self.assertNotIn("ssss", output)
        self.assertNotIn("url-password", output)
        self.assertIn("registry.test/failure", output)
        self.assertEqual("", _startup_diagnostic(None))


class MockHttpStartupDiagnosticsTests(unittest.IsolatedAsyncioTestCase):
    async def test_failed_start_logs_before_cleanup_and_preserves_original_failure(self):
        failure = RuntimeError("original startup failure")
        runtime = Mock(mock=True, auth_file=None)
        runtime.mcp_http_start.side_effect = failure
        runtime.call.return_value = "child initialize timed out\nBearer log-canary"
        temporary = Mock()
        harness = fixtures.FirstCutHttpDockerEndToEnd("runTest")
        harness._assertions = Mock()
        harness._assertions._stop = AsyncMock()
        runtime.mcp_http_stop.return_value = {"outcome": "stopped"}
        runtime.mcp_http_status.return_value = {
            "services": [{"Service": "mcp-http", "State": "exited"}]
        }
        stream = io.StringIO()
        with patch.object(fixtures.sys, "stderr", stream):
            startup = asyncio.create_task(fixtures._start_http(runtime))
            with self.assertRaises(RuntimeError) as caught:
                await startup
            self.assertIs(failure, caught.exception)
            runtime.call.assert_called_once_with(
                "logs", "--no-color", "--tail", "80", "mcp-http", http=True, timeout=10
            )
            temporary.cleanup.assert_not_called()
            result = await harness._cleanup_case(
                failure,
                runtime=runtime,
                temporary=temporary,
                startup_task=None,
                http_start_attempted=True,
                http_startup_task=startup,
                token=None,
            )
        self.assertIs(failure, result)
        self.assertIn("child initialize timed out", stream.getvalue())
        self.assertNotIn("log-canary", stream.getvalue())
        harness._assertions._stop.assert_awaited_once_with(runtime, http=True)
        temporary.cleanup.assert_called_once_with()

    async def test_log_read_failure_does_not_replace_start_failure(self):
        failure = RuntimeError("original startup failure")
        runtime = Mock(mock=True, auth_file=None)
        runtime.mcp_http_start.side_effect = failure
        runtime.call.side_effect = RuntimeError("private diagnostic error")
        stream = io.StringIO()
        with (
            patch.object(fixtures.sys, "stderr", stream),
            self.assertRaises(RuntimeError) as caught,
        ):
            await fixtures._start_http(runtime)
        self.assertIs(failure, caught.exception)
        self.assertEqual("", stream.getvalue())

    async def test_diagnostic_output_failure_does_not_replace_start_failure(self):
        failure = RuntimeError("original startup failure")
        runtime = Mock(mock=True, auth_file=None)
        runtime.mcp_http_start.side_effect = failure
        runtime.call.return_value = "child failed"
        stream = Mock()
        stream.write.side_effect = OSError("diagnostic output unavailable")
        with (
            patch.object(fixtures.sys, "stderr", stream),
            self.assertRaises(RuntimeError) as caught,
        ):
            await fixtures._start_http(runtime)
        self.assertIs(failure, caught.exception)

    async def test_success_and_nonmock_failure_do_not_read_logs(self):
        runtime = Mock(mock=True, auth_file=None)
        runtime.mcp_http_start.return_value = {"outcome": "ready"}
        self.assertEqual({"outcome": "ready"}, await fixtures._start_http(runtime))
        runtime.call.assert_not_called()
        runtime.mock = False
        runtime.mcp_http_start.side_effect = RuntimeError("startup failure")
        with self.assertRaisesRegex(RuntimeError, "startup failure"):
            await fixtures._start_http(runtime)
        runtime.call.assert_not_called()
        runtime.mock, runtime.auth_file = True, "auth.json"
        with self.assertRaisesRegex(RuntimeError, "startup failure"):
            await fixtures._start_http(runtime)
        runtime.call.assert_not_called()


if __name__ == "__main__":
    unittest.main()
