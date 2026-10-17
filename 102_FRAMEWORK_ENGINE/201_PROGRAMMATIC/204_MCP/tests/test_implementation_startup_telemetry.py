"""Fixed, opt-in child startup timings do not alter registration or failures."""

from contextlib import redirect_stderr
import io
import os
from pathlib import Path
import re
import subprocess
import sys
import tempfile
from types import SimpleNamespace
from typing import Callable, cast
import unittest
from unittest.mock import Mock, patch

MCP = Path(__file__).resolve().parents[1]
ROOT = MCP.parents[2]
sys.path.insert(0, str(MCP))
import implementation_server as implementation  # noqa: E402
from hot_reload import Gateway, GENERATION_READY_TIMEOUT_SECONDS  # noqa: E402
from test_rmed_workflow_mcp import _forward_startup_telemetry  # noqa: E402

LINE = re.compile(
    r"caprmedio_mcp_startup phase=([a-z_]+) "
    r"outcome=(completed|failed) elapsed_ms=[0-9]+"
)


class ImplementationStartupTelemetryTests(unittest.TestCase):
    def setUp(self) -> None:
        parent = ROOT / ".caprmedio_tmp/tests/implementation-startup-telemetry"
        parent.mkdir(parents=True, exist_ok=True)
        self.temporary = tempfile.TemporaryDirectory(dir=parent)
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)

    def _create(self, failure: str | None = None) -> tuple[str, list[str]]:
        calls: list[str] = []
        service = SimpleNamespace(
            exposed=set(),
            catalog=Mock(return_value=([], [], [])),
            tool_blacklist=Mock(return_value=frozenset()),
        )
        selected = SimpleNamespace(public_route_names=("fixture_route",))
        registry = SimpleNamespace(quarantined=[], withheld=[], registered_names=("helper",))
        stderr = io.StringIO()
        create = cast(Callable[[Path], object], implementation.create_server)
        with (
            patch.object(implementation, "Service", return_value=service),
            patch.object(implementation, "MCPServer"),
            patch.object(implementation, "register_orchestrator"),
            patch.object(implementation, "register_selected_routes", return_value=selected),
            patch.object(implementation, "register_catalog_tools", return_value=registry),
            redirect_stderr(stderr),
        ):
            if failure is not None:
                service.catalog.side_effect = RuntimeError(failure)
                with self.assertRaisesRegex(RuntimeError, failure):
                    create(self.root)
            else:
                create(self.root)
                self.assertEqual(service.exposed, {"fixture_route", "helper"})
            self.assertEqual(service.catalog.call_count, 1)
        for line in stderr.getvalue().splitlines():
            match = LINE.fullmatch(line)
            self.assertIsNotNone(match, line)
            if match is not None:
                calls.append(f"{match[1]}:{match[2]}")
        return stderr.getvalue(), calls

    def test_registration_milestones_are_fixed_and_silent_without_opt_in(self) -> None:
        with patch.dict(os.environ, {"CAPRMEDIO_STARTUP_TELEMETRY": "1"}):
            rendered, calls = self._create()
        self.assertEqual(
            calls,
            [
                "selected_registration:completed",
                "catalog:completed",
                "catalog_registration:completed",
            ],
        )
        self.assertNotIn(str(self.root), rendered)
        with patch.dict(os.environ, {"CAPRMEDIO_STARTUP_TELEMETRY": "0"}):
            self.assertEqual(self._create()[0], "")
        self.assertEqual(GENERATION_READY_TIMEOUT_SECONDS, 90)

    def test_catalog_failure_retains_exception_without_sensitive_telemetry(self) -> None:
        secret = "PRIVATE_CONTENT_MUST_NOT_ESCAPE"
        with patch.dict(os.environ, {"CAPRMEDIO_STARTUP_TELEMETRY": "1"}):
            rendered, calls = self._create(secret)
        self.assertEqual(calls, ["selected_registration:completed", "catalog:failed"])
        self.assertNotIn(secret, rendered)
        self.assertNotIn(str(self.root), rendered)

    def test_child_environment_only_adds_the_existing_telemetry_opt_in(self) -> None:
        values = {
            "PATH": "/fixture",
            "CAPRMEDIO_STARTUP_TELEMETRY": "1",
            "CAPRMEDIO_MCP_HTTP_SECRET_TOKEN": "private",
        }
        with patch.dict(os.environ, values, clear=True):
            self.assertEqual(
                Gateway.child_environment(),
                {
                    "PATH": "/fixture",
                    "CAPRMEDIO_STARTUP_TELEMETRY": "1",
                },
            )

    def test_new_child_markers_survive_only_the_safe_failure_capture_filter(self) -> None:
        valid = [
            f"caprmedio_mcp_startup phase={phase} outcome=completed elapsed_ms=1"
            for phase in (
                "implementation_import",
                "selected_registration",
                "catalog",
                "catalog_registration",
            )
        ]
        captured = io.StringIO(
            "\n".join(
                [
                    *valid,
                    "PRIVATE_CONTENT",
                    "caprmedio_mcp_startup phase=unknown outcome=failed elapsed_ms=1",
                ]
            )
        )
        forwarded = io.StringIO()
        with (
            patch.dict(os.environ, {"CAPRMEDIO_STARTUP_TELEMETRY": "1"}),
            redirect_stderr(forwarded),
        ):
            _forward_startup_telemetry(captured)
        self.assertEqual(forwarded.getvalue().splitlines(), valid)

    def test_real_import_emits_only_the_opt_in_completion_record(self) -> None:
        script = f"import sys; sys.path.insert(0, {str(MCP)!r}); import implementation_server"
        for enabled in ("0", "1"):
            result = subprocess.run(
                [sys.executable, "-I", "-B", "-c", script],
                env={**os.environ, "CAPRMEDIO_STARTUP_TELEMETRY": enabled},
                capture_output=True,
                text=True,
                timeout=30,
                check=True,
            )
            self.assertEqual(result.stdout, "")
            if enabled == "0":
                self.assertEqual(result.stderr, "")
            else:
                match = LINE.fullmatch(result.stderr.strip())
                self.assertIsNotNone(match, result.stderr)
                if match is not None:
                    self.assertEqual(match.groups(), ("implementation_import", "completed"))


if __name__ == "__main__":
    unittest.main()
