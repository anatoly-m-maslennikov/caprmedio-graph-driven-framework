"""Host-only checks for disposable launcher Settings ports; no Docker calls."""

from pathlib import Path
import subprocess
import tempfile
import time
import unittest
from unittest.mock import patch

import test_project_launcher_docker_e2e as launcher
from project_mcp_launcher import LaunchError, _configured_port


class FixturePortTests(unittest.TestCase):
    def test_distinct_settings_ports_drive_default_and_explicit_requests(self) -> None:
        parent = launcher.ROOT / ".caprmedio_tmp" / "launcher-fixture-port-checks"
        parent.mkdir(parents=True, exist_ok=True)
        for group in ("two-repositories", "same-repository"):
            with self.subTest(group=group), tempfile.TemporaryDirectory(dir=parent) as directory:
                with patch.object(
                    launcher, "_available_port", side_effect=(45121, 45122)
                ) as select:
                    fixtures = launcher._fixtures(Path(directory), group)
                select.assert_any_call(excluded=(45121,))
                selections = [
                    launcher.resolve_project(item.root, item.control) for item in fixtures
                ]
                self.assertEqual(
                    [45121, 45122], [_configured_port(item, None) for item in selections]
                )
                self.assertEqual(45122, _configured_port(selections[1], 45122))
                with self.assertRaises(LaunchError) as refused:
                    _configured_port(selections[1], 45121)
                self.assertEqual("PROJECT_SELECTION_REFUSED", refused.exception.code)
                response = subprocess.CompletedProcess([], 1, '{"readiness": false}', "")
                with patch.object(launcher.subprocess, "run", return_value=response) as run:
                    launcher._launch(
                        fixtures[0], None, launcher.ROOT, None, deadline=time.monotonic() + 900
                    )
                self.assertNotIn("--port", run.call_args.args[0])

    def test_available_port_skips_assigned_port(self) -> None:
        with patch.object(launcher.socket, "socket") as factory:
            probe = factory.return_value.__enter__.return_value
            probe.getsockname.side_effect = [("127.0.0.1", 45121), ("127.0.0.1", 45122)]
            self.assertEqual(45122, launcher._available_port(excluded=(45121,)))
            self.assertEqual(2, probe.bind.call_count)
            probe.bind.assert_called_with(("127.0.0.1", 0))

    def test_repeated_assigned_ports_refuse_with_bounded_attempts(self) -> None:
        with patch.object(launcher.socket, "socket") as factory:
            probe = factory.return_value.__enter__.return_value
            probe.getsockname.return_value = ("127.0.0.1", 45121)
            with self.assertRaisesRegex(AssertionError, "distinct ephemeral"):
                launcher._available_port(excluded=(45121,))
            self.assertEqual(8, probe.bind.call_count)

    def test_temporary_settings_port_restores_exact_bytes_on_error(self) -> None:
        parent = launcher.ROOT / ".caprmedio_tmp" / "launcher-fixture-port-checks"
        parent.mkdir(parents=True, exist_ok=True)
        with tempfile.TemporaryDirectory(dir=parent) as directory:
            fixture = launcher.ProjectFixture.create(
                Path(directory) / "project", "alpha", "fixture", 45121
            )
            settings = fixture.root / fixture.control / "caprmedio_project_settings.toml"
            before = settings.read_bytes()
            with self.assertRaisesRegex(RuntimeError, "fixture failure"):
                with launcher._fixture_settings_port(fixture, 45122):
                    selection = launcher.resolve_project(fixture.root, fixture.control)
                    self.assertEqual(45122, _configured_port(selection, 45122))
                    raise RuntimeError("fixture failure")
            self.assertEqual(before, settings.read_bytes())


if __name__ == "__main__":
    unittest.main()
