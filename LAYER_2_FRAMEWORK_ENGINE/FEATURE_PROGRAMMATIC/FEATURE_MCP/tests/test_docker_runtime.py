"""Runtime boundary tests for retained Docker MCP services."""

# CA-M-504@2
# CA-E-796@4
# CA-E-533@13

import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

import yaml

APP = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(APP))
sys.path.insert(0, str(APP / "docker"))

from runtime import Runtime  # noqa: E402


class RuntimeTests(unittest.TestCase):
    image = "sha256:" + "a" * 64

    def test_build_passes_timeout_to_image_manager(self):
        runtime = Runtime(APP.parents[2])
        with patch.object(runtime, "_image_manager") as factory:
            factory.return_value.resolve.return_value = self.image
            self.assertEqual(self.image, runtime.build(timeout=17))
        factory.assert_called_once_with(create_temp=True, timeout=17)

    def setUp(self):
        self.temporary = APP.parents[2] / ".caprmedio_tmp/tests/docker-runtime"
        self.temporary.mkdir(parents=True, exist_ok=True)

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

    def test_compose_inputs_enforce_service_boundaries_without_a_daemon(self):
        runtime = Runtime(APP.parents[2])
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
        self.assertEqual({"mcp"}, set(services))
        mounts = services["mcp"]["volumes"]
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
            "**/.caprmedio_runtime", "**/tmp", "**/tests", "**/fixtures",
            "**/*.md", "!**/SKILL.md",
        ):
            self.assertIn(value, ignored)

    def test_mcp_services_have_no_reload_control(self):
        for compose_name, service in (
            ("compose.yaml", "mcp"),
            ("mcp-http.compose.yaml", "mcp-http"),
            ("project-mcp.compose.yaml", "mcp-http"),
            ("shared-mcp.compose.yaml", "shared-mcp"),
        ):
            with self.subTest(compose=compose_name, service=service):
                config = yaml.safe_load((APP / "docker" / compose_name).read_text())
                self.assertNotIn("CAPRMEDIO_HOT_RELOAD", config["services"][service]["environment"])

    def test_mount_symlinks_rejected_before_mcp_start(self):
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
                    runtime.mcp_http_start()
                operation.assert_not_called()

    def test_retired_worker_mode_returns_structured_warning(self):
        result = subprocess.run(
            [sys.executable, "-B", str(APP / "docker/entrypoint.py"), "worker"],
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(1, result.returncode)
        self.assertNotIn("NameError", result.stderr)
        self.assertEqual({"error": "invalid_runtime_mode", "severity": "WARNING"},
                         json.loads(result.stderr.splitlines()[-1]))

if __name__ == "__main__":
    unittest.main()
