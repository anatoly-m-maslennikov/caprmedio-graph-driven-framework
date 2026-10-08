"""Public startup/output contract for the Project MCP launcher."""

from __future__ import annotations

import json
import fcntl
import os
from pathlib import Path
import sys
import tempfile
import threading
import unittest
from types import SimpleNamespace
from unittest.mock import patch


APP = Path(__file__).resolve().parents[1]
DOCKER = APP / "docker"
TOOLS = APP.parents[1] / "201_TOOLS"
sys.path[:0] = [str(DOCKER), str(TOOLS)]

from project_mcp_launcher import (  # noqa: E402
    ImageError,
    LaunchError,
    Launcher,
    ProjectSelectionError,
)


GOLDENS = Path(__file__).parent / "launcher_golden" / "startup_output_cases.json"
IMAGE_ID = "sha256:" + "a" * 64
FINGERPRINT = "b" * 64
INSTANCE_ID = "c" * 64


class Backend:
    """Small stateful fake exposing only the launcher's public backend seam."""

    def __init__(self) -> None:
        self.rows = []
        self.resolve_image_calls = 0
        self.start_calls = 0
        self.health_calls = []
        self.inspect_envs = []
        self.start_ports = []
        self.start_error = None
        self.health_result = True
        self.start_entered = threading.Event()
        self.release_start = None

    def resolve_image(self, source_root, explicit_id):
        self.resolve_image_calls += 1
        return IMAGE_ID, FINGERPRINT

    def inspect(self, selection):
        # Model the backend subprocess boundary: only its sanitized environment
        # is observable by Docker inspection, never the launcher credential.
        environment = dict(os.environ)
        environment.pop("CAPRMEDIO_MCP_HTTP_SECRET_TOKEN", None)
        self.inspect_envs.append(environment)
        return list(self.rows)

    def start(self, selection, image_id, fingerprint, token, timeout, port=None):
        self.start_calls += 1
        self.start_ports.append(port)
        self.start_entered.set()
        if self.release_start is not None:
            self.release_start.wait(timeout=2)
        if self.start_error is not None:
            raise self.start_error
        self.rows = [healthy_row(host_port=str(port) if port is not None else "8099")]

    def health(self, url, token, timeout):
        self.health_calls.append((url, token, timeout))
        return self.health_result


def healthy_row(*, project=INSTANCE_ID, image=IMAGE_ID, fingerprint=FINGERPRINT,
                host_ip="127.0.0.1", host_port="8099", ports=None):
    return {
        "Id": "container-a",
        "Image": image,
        "Config": {"Labels": {
            "org.caprmedio.project": project,
            "org.caprmedio.runtime.fingerprint": fingerprint,
            "org.caprmedio.service": "mcp-http",
        }},
        "State": {"Status": "running", "Health": {"Status": "healthy"}},
        "NetworkSettings": {"Ports": {
            "8092/tcp": ports if ports is not None else [
                {"HostIp": host_ip, "HostPort": host_port}
            ]
        }},
    }


class LauncherStartupContractTests(unittest.TestCase):
    """Fixtures are retained: sandbox cleanup is not test evidence."""

    def setUp(self) -> None:
        parent = APP.parents[3] / ".caprmedio_tmp" / "launcher-epic-1829" / "startup"
        parent.mkdir(parents=True, exist_ok=True)
        self.project_root = Path(tempfile.mkdtemp(dir=parent))
        self.control_root = self.project_root / ".caprmedio_local"
        self.control_root.mkdir()
        self.selection = SimpleNamespace(
            root=self.project_root,
            rootPath=self.project_root,
            control_root=self.control_root,
            control_rootPath=self.control_root,
            control_relative=Path(".caprmedio_local"),
            control_relativePath=Path(".caprmedio_local"),
            instance_id=INSTANCE_ID,
            settings={},
            structure={},
        )
        self.backend = Backend()
        self.launcher = Launcher(backend=self.backend)

    def launch(self, *, token="secret-token", **kwargs):
        kwargs.setdefault("source_root", APP.parents[3])
        with patch("project_mcp_launcher.resolve_project", return_value=self.selection):
            return self.launcher.launch(self.project_root, token, **kwargs)

    def assert_public_failure(self, result, disposition, condition):
        self.assertEqual(disposition, result["disposition"])
        self.assertEqual(condition, result["condition"])
        self.assertNotIn("url", result)
        self.assertNotIn("secret-token", json.dumps(result))

    def test_golden_corpus_is_complete_and_unique(self):
        cases = json.loads(GOLDENS.read_text(encoding="utf-8"))
        self.assertEqual(13, len(cases))
        self.assertEqual(13, len({case["condition"] for case in cases}))
        self.assertEqual({
            "READY_STARTED", "READY_REUSED", "PROJECT_SELECTION_REFUSED",
            "CREDENTIAL_SOURCE_REFUSED", "IMAGE_INPUT_UNAVAILABLE", "IMAGE_REFUSED",
            "PROJECT_LOCK_BUSY", "RUNTIME_MISMATCH", "RUNTIME_UNHEALTHY",
            "BUILD_FAILED", "DOCKER_START_FAILED", "DOCKER_PUBLICATION_FAILED",
            "READINESS_FAILED",
        }, {case["condition"] for case in cases})

    def test_started_result_is_authenticated_and_contains_only_ready_url(self):
        result = self.launch(source_root=APP.parents[3], timeout=7)
        self.assertEqual("started", result["disposition"])
        self.assertEqual("READY_STARTED", result["condition"])
        self.assertEqual(str(self.project_root), result["project_root"])
        self.assertEqual(str(self.control_root), result["control_root"])
        self.assertEqual(INSTANCE_ID, result["project_id"])
        self.assertEqual(IMAGE_ID, result["image_id"])
        self.assertEqual(FINGERPRINT, result["fingerprint"])
        self.assertEqual("container-a", result["container_id"])
        self.assertEqual("mcp-http", result["service"])
        self.assertEqual(8099, result["port"])
        self.assertTrue(result["readiness"])
        self.assertEqual("http://127.0.0.1:8099/mcp", result["url"])
        self.assertEqual(1, len(self.backend.health_calls))
        url, token, remaining_timeout = self.backend.health_calls[0]
        self.assertEqual("http://127.0.0.1:8099/mcp", url)
        self.assertEqual("secret-token", token)
        self.assertGreater(remaining_timeout, 0)
        self.assertLessEqual(remaining_timeout, 7)
        self.assertNotIn("secret-token", json.dumps(result))

    def test_omitted_port_leaves_dynamic_localhost_publication_to_the_backend(self):
        result = self.launch()
        self.assertEqual("started", result["disposition"])
        self.assertEqual([None], self.backend.start_ports)
        self.assertEqual(8099, result["port"])

    def test_invalid_port_values_refuse_before_selection_or_runtime_effects(self):
        for port in (True, False, "8099", 8099.0, 0, 65536):
            with self.subTest(port=port), patch("project_mcp_launcher.resolve_project") as resolve:
                result = self.launcher.launch(self.project_root, "secret-token", port=port)
            self.assert_public_failure(result, "failed", "DOCKER_START_FAILED")
            resolve.assert_not_called()
            self.assertEqual(0, self.backend.resolve_image_calls)
            self.assertEqual(0, self.backend.start_calls)

    def test_reuses_exact_healthy_runtime_without_starting(self):
        self.backend.rows = [healthy_row()]
        result = self.launch()
        self.assertEqual("reused", result["disposition"])
        self.assertEqual("READY_REUSED", result["condition"])
        self.assertEqual(0, self.backend.start_calls)
        self.assertEqual("http://127.0.0.1:8099/mcp", result["url"])

    def test_requested_port_reuses_only_the_exact_healthy_publication(self):
        self.backend.rows = [healthy_row(host_port="8123")]
        result = self.launch(port=8123)
        self.assertEqual("reused", result["disposition"])
        self.assertEqual("READY_REUSED", result["condition"])
        self.assertEqual(8123, result["port"])
        self.assertEqual(0, self.backend.start_calls)

        original_rows = self.backend.rows.copy()
        mismatch = self.launch(port=8124)
        self.assert_public_failure(mismatch, "refused", "RUNTIME_MISMATCH")
        self.assertEqual(0, self.backend.start_calls)
        self.assertEqual(original_rows, self.backend.rows)

    def test_requested_port_is_published_exactly_after_start(self):
        result = self.launch(port=8123)
        self.assertEqual("started", result["disposition"])
        self.assertEqual("READY_STARTED", result["condition"])
        self.assertEqual([8123], self.backend.start_ports)
        self.assertEqual(8123, result["port"])
        self.assertEqual("http://127.0.0.1:8123/mcp", result["url"])

    def test_selection_and_credential_refusals_precede_runtime_effects(self):
        with patch("project_mcp_launcher.resolve_project", side_effect=ProjectSelectionError("PROJECT_SELECTION_REFUSED")):
            result = self.launcher.launch(self.project_root, "secret-token")
        self.assert_public_failure(result, "refused", "PROJECT_SELECTION_REFUSED")
        self.assert_public_failure(self.launch(token=""), "refused", "CREDENTIAL_SOURCE_REFUSED")
        self.assertEqual(0, self.backend.resolve_image_calls)
        self.assertEqual(0, self.backend.start_calls)

    def test_omitted_source_root_is_truthful_image_input_refusal(self):
        with patch("project_mcp_launcher.resolve_project", return_value=self.selection):
            result = self.launcher.launch(self.project_root, "secret-token")
        self.assert_public_failure(result, "failed", "IMAGE_INPUT_UNAVAILABLE")
        self.assertEqual(0, self.backend.resolve_image_calls)
        self.assertEqual(0, self.backend.start_calls)
        self.assertEqual([], self.backend.inspect_envs)

    def test_runtime_inspection_environment_contains_no_http_secret(self):
        with patch.dict(os.environ, {"CAPRMEDIO_MCP_HTTP_SECRET_TOKEN": "secret-token"}):
            self.backend.rows = [healthy_row()]
            result = self.launch(source_root=APP.parents[3])
        self.assertEqual("reused", result["disposition"])
        self.assertTrue(self.backend.inspect_envs)
        self.assertNotIn("CAPRMEDIO_MCP_HTTP_SECRET_TOKEN", self.backend.inspect_envs[0])

    def test_image_and_build_boundary_failures_preserve_their_codes(self):
        for code, disposition in (("IMAGE_INPUT_UNAVAILABLE", "failed"),
                                  ("IMAGE_REFUSED", "refused"),
                                  ("BUILD_FAILED", "failed")):
            with self.subTest(code=code):
                self.backend.resolve_image = lambda *_args, code=code: (_ for _ in ()).throw(ImageError(code))
                self.assert_public_failure(self.launch(), disposition, code)

    def test_lock_and_start_failures_preserve_their_codes(self):
        self.backend.start_error = LaunchError("DOCKER_START_FAILED")
        self.assert_public_failure(self.launch(), "failed", "DOCKER_START_FAILED")
        self.backend.start_error = RuntimeError("secret-token must never escape")
        self.assert_public_failure(self.launch(), "failed", "DOCKER_START_FAILED")
        self.backend.start_error = None

    def test_occupied_requested_port_reports_failure_without_resource_destruction(self):
        self.backend.start_error = LaunchError("DOCKER_START_FAILED")
        result = self.launch(port=8123)
        self.assert_public_failure(result, "failed", "DOCKER_START_FAILED")
        self.assertEqual([8123], self.backend.start_ports)
        self.assertEqual([], self.backend.rows)

    def test_external_project_lock_contention_reports_busy_without_runtime_effects(self):
        lock_path = (self.project_root / ".caprmedio_install" / "project_mcp" /
                     INSTANCE_ID / "launch.lock")
        lock_path.parent.mkdir(parents=True)
        with lock_path.open("w", encoding="utf-8") as held:
            fcntl.flock(held.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
            try:
                result = self.launch(timeout=0.01)
            finally:
                fcntl.flock(held.fileno(), fcntl.LOCK_UN)
        self.assert_public_failure(result, "busy", "PROJECT_LOCK_BUSY")
        self.assertEqual(0, self.backend.resolve_image_calls)
        self.assertEqual(0, self.backend.start_calls)

    def test_mismatched_and_unhealthy_runtime_refuse_without_replacement(self):
        self.backend.rows = [healthy_row(project="d" * 64)]
        self.assert_public_failure(self.launch(), "refused", "RUNTIME_MISMATCH")
        self.assertEqual(0, self.backend.start_calls)
        self.backend.rows = [healthy_row(image="sha256:" + "d" * 64)]
        self.assert_public_failure(self.launch(), "refused", "RUNTIME_MISMATCH")
        self.assertEqual(0, self.backend.start_calls)
        self.backend.rows = [healthy_row(fingerprint="d" * 64)]
        self.assert_public_failure(self.launch(), "refused", "RUNTIME_MISMATCH")
        self.assertEqual(0, self.backend.start_calls)
        self.backend.rows = [healthy_row()]
        self.backend.rows[0]["State"]["Health"]["Status"] = "unhealthy"
        self.assert_public_failure(self.launch(), "refused", "RUNTIME_UNHEALTHY")
        self.assertEqual(0, self.backend.start_calls)

    def test_publisher_refuses_wildcard_wrong_target_and_multiple_ports(self):
        cases = (
            healthy_row(host_ip="0.0.0.0"),
            healthy_row(host_ip="192.0.2.10"),
            {**healthy_row(), "NetworkSettings": {"Ports": {
                "8093/tcp": [{"HostIp": "127.0.0.1", "HostPort": "8099"}]
            }}},
            healthy_row(ports=[
                {"HostIp": "127.0.0.1", "HostPort": "8099"},
                {"HostIp": "127.0.0.1", "HostPort": "8100"},
            ]),
        )
        for row in cases:
            with self.subTest(row=row):
                self.backend.rows = [row]
                self.assert_public_failure(self.launch(), "failed", "DOCKER_PUBLICATION_FAILED")

    def test_multiple_matching_containers_are_not_admitted(self):
        self.backend.rows = [healthy_row(), healthy_row()]
        self.assert_public_failure(self.launch(), "failed", "DOCKER_PUBLICATION_FAILED")

    def test_health_failure_has_no_url(self):
        self.backend.health_result = False
        self.assert_public_failure(self.launch(), "failed", "READINESS_FAILED")

    def test_concurrent_calls_share_the_project_lock_and_start_once(self):
        self.backend.release_start = threading.Event()
        results = []

        def call():
            results.append(self.launch())

        first = threading.Thread(target=call)
        second = threading.Thread(target=call)
        first.start()
        self.assertTrue(self.backend.start_entered.wait(timeout=2))
        second.start()
        self.backend.release_start.set()
        first.join(timeout=3)
        second.join(timeout=3)
        self.assertFalse(first.is_alive())
        self.assertFalse(second.is_alive())
        self.assertEqual(1, self.backend.start_calls)
        self.assertEqual({"READY_STARTED", "READY_REUSED"}, {result["condition"] for result in results})


if __name__ == "__main__":
    unittest.main()
