"""Runtime boundary tests for retained Docker worker and MCP services."""

# CA-M-504@2
# CA-E-796@2
# CA-E-533@13

import json
import os
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

import yaml

APP = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(APP))
sys.path.insert(0, str(APP / "docker"))

from runtime_config import control_directory  # noqa: E402
from runtime import Runtime  # noqa: E402


class RuntimeTests(unittest.TestCase):
    image = "sha256:" + "a" * 64

    def setUp(self):
        self.temporary = APP.parents[3] / ".caprmedio_tmp/tests/docker-runtime"
        self.temporary.mkdir(parents=True, exist_ok=True)

    def test_native_and_docker_namespaces_do_not_share_a_queue(self):
        with patch.dict(os.environ, {"CAPRMEDIO_RUNTIME_NAMESPACE": ""}):
            self.assertEqual(control_directory(), ".caprmedio_install/workflow_orchestrator")
        with patch.dict(os.environ, {"CAPRMEDIO_RUNTIME_NAMESPACE": "docker"}):
            self.assertEqual(control_directory(), ".caprmedio_install/workflow_orchestrator/docker")
        with patch.dict(os.environ, {"CAPRMEDIO_RUNTIME_NAMESPACE": "../escape"}):
            with self.assertRaises(ValueError):
                control_directory()

    def test_compose_command_has_no_credential_input(self):
        with tempfile.TemporaryDirectory(
            dir=self.temporary, ignore_cleanup_errors=True
        ) as directory:
            runtime = Runtime(Path(directory))
            command = runtime.command("config")
            self.assertIn("--env-file", command)
            self.assertIn("/dev/null", command)
            self.assertNotIn("auth.compose.yaml", " ".join(command))
            self.assertNotIn("CAPRMEDIO_CODEX_AUTH_FILE", runtime.environment())

    def test_routing_does_not_fall_back_when_docker_stops(self):
        from docker_bridge import invoke

        with tempfile.TemporaryDirectory(
            dir=self.temporary, ignore_cleanup_errors=True
        ) as directory:
            root = Path(directory)
            path = root / ".caprmedio_install/workflow_orchestrator/docker/transport.json"
            path.parent.mkdir(parents=True)
            path.write_text(json.dumps({"transport": "docker", "project_name": "caprmedio-test"}))
            with patch("docker_bridge.subprocess.run", side_effect=OSError("unavailable")):
                with self.assertRaisesRegex(RuntimeError, "Docker runtime is unavailable"):
                    invoke(root, {"operation": "status", "run_id": "test"})

    def test_compose_inputs_enforce_service_boundaries_without_a_daemon(self):
        runtime = Runtime(APP.parents[3])
        arguments = ("--profile", "stdio", "config", "--format", "json")
        expected_command = runtime.command(*arguments)
        with patch("runtime.subprocess.run") as execute:
            execute.return_value.returncode = 0
            execute.return_value.stdout = ""
            self.assertEqual("", runtime.call(*arguments))
        execute.assert_called_once()
        actual_command = execute.call_args.args[0]
        self.assertEqual(expected_command, actual_command)
        self.assertEqual(runtime.environment(), execute.call_args.kwargs["env"])

        # Unit scope must not require an installed Docker daemon.  Parse the
        # exact Compose inputs here; Docker's fully resolved config is covered
        # by the opt-in container E2E harness.
        config = yaml.safe_load((APP / "docker/compose.yaml").read_text())
        services = config["services"]
        for service in services.values():
            self.assertTrue(service["read_only"])
            self.assertEqual(service["cap_drop"], ["ALL"])
            self.assertEqual(service["restart"], "no")
            self.assertFalse(service.get("ports"))
            self.assertFalse(service.get("privileged", False))
        for name in ("worker", "mcp"):
            mounts = services[name]["volumes"]
            project = next(volume for volume in mounts if volume["target"] == "/project")
            self.assertEqual(project["source"], "${CAPRMEDIO_PROJECT_ROOT}")
            self.assertFalse(project.get("read_only", False))
            self.assertEqual(
                {volume["target"] for volume in mounts if volume.get("read_only")},
                {"/project/.git"},
            )
            self.assertEqual(len(mounts), 2)
            self.assertFalse(any(volume["target"].startswith("/workspace") for volume in mounts))
        ignored = (APP / "docker/Dockerfile.dockerignore").read_text()
        for value in (
            "**/.env", "**/.env.*", "**/*.env", "**/auth.json",
            "**/.caprmedio_tmp", "**/.caprmedio_install",
            "**/.caprmedio_runtime", "**/tmp",
        ):
            self.assertIn(value, ignored)

    def test_mcp_services_default_hot_reload_to_disabled(self):
        expected = "${CAPRMEDIO_HOT_RELOAD:-0}"
        for compose_name, service in (
            ("compose.yaml", "mcp"),
            ("mcp-http.compose.yaml", "mcp-http"),
            ("project-mcp.compose.yaml", "mcp-http"),
            ("shared-mcp.compose.yaml", "shared-mcp"),
        ):
            with self.subTest(compose=compose_name, service=service):
                config = yaml.safe_load((APP / "docker" / compose_name).read_text())
                self.assertEqual(expected, config["services"][service]["environment"]["CAPRMEDIO_HOT_RELOAD"])

    def test_failed_start_does_not_select_docker_transport(self):
        with tempfile.TemporaryDirectory(
            dir=self.temporary, ignore_cleanup_errors=True
        ) as directory:
            root = Path(directory)
            (root / ".caprmedio_caprmedio").mkdir()
            (root / ".git").mkdir()
            runtime = Runtime(root, image=self.image)
            with patch.object(runtime, "call", side_effect=RuntimeError("not ready")):
                with self.assertRaises(RuntimeError):
                    runtime.start()
            self.assertFalse(
                (root / ".caprmedio_install/workflow_orchestrator/docker/transport.json").exists()
            )

    def test_start_only_creates_routing_after_services_are_ready(self):
        with tempfile.TemporaryDirectory(
            dir=self.temporary, ignore_cleanup_errors=True
        ) as directory:
            root = Path(directory)
            (root / ".caprmedio_caprmedio").mkdir()
            (root / ".git").mkdir()
            runtime = Runtime(root, image=self.image)
            with patch.object(runtime, "call", return_value="") as operation:
                self.assertEqual(runtime.start()["outcome"], "ready")
                self.assertEqual(runtime.start()["outcome"], "ready")
            self.assertEqual(operation.call_count, 2)
            marker = root / ".caprmedio_install/workflow_orchestrator/docker/transport.json"
            self.assertEqual(json.loads(marker.read_text())["project_name"], runtime.project)
            self.assertEqual(list(marker.parent.glob("transport-*.json")), [])
            self.assertFalse((marker.parent / "runs").exists())

    def test_mount_and_routing_symlinks_rejected_before_start(self):
        with tempfile.TemporaryDirectory(
            dir=self.temporary, ignore_cleanup_errors=True
        ) as directory:
            root = Path(directory)
            (root / ".git").mkdir()
            outside = root / "unmounted"
            outside.mkdir()
            authority = root / ".caprmedio_caprmedio"
            authority.symlink_to(outside, target_is_directory=True)
            runtime = Runtime(root)
            with patch.object(runtime, "call") as operation:
                with self.assertRaises(ValueError):
                    runtime.start()
                operation.assert_not_called()
            authority.unlink()
            authority.mkdir()
            install = root / ".caprmedio_install"
            install.mkdir()
            (install / "workflow_orchestrator").symlink_to(outside, target_is_directory=True)
            with patch.object(runtime, "call") as operation:
                with self.assertRaises(ValueError):
                    runtime.start()
                operation.assert_not_called()

if __name__ == "__main__":
    unittest.main()
