"""Installed-package handoff for the Project-local loopback HTTP MCP."""

from __future__ import annotations

import hashlib
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch


APP = Path(__file__).resolve().parents[1]
DOCKER = APP / "docker"
TOOLS = APP.parents[1] / "201_TOOLS"
sys.path[:0] = [str(DOCKER), str(TOOLS)]

from installed_mcp_binding import InstalledMcpBinding, TargetProjectContext  # noqa: E402
from project_mcp_backend import ProjectMcpBackend  # noqa: E402
from project_mcp_launcher import Launcher  # noqa: E402
from project_selection import resolve_project  # noqa: E402


IMAGE_DIGEST = "a" * 64
RUNTIME_SELECTOR = "b" * 64
MANIFEST = "c" * 64
CATALOG = "d" * 64
PACKAGE_SELECTOR = "e" * 64


def _healthy_row(selection, *, image_id: str, fingerprint: str, host_port: str = "8192") -> dict:
    return {
        "Id": "installed-container",
        "Image": image_id,
        "Config": {"Labels": {
            "org.caprmedio.project": selection.instance_id,
            "org.caprmedio.runtime.fingerprint": fingerprint,
            "org.caprmedio.service": "mcp-http",
        }},
        "State": {"Status": "running", "Health": {"Status": "healthy"}},
        "NetworkSettings": {"Ports": {
            "8092/tcp": [{"HostIp": "127.0.0.1", "HostPort": host_port}],
        }},
    }


class _Backend:
    """No-Docker fake exposing the installed activation seam only."""

    def __init__(self) -> None:
        self.rows: list[dict] = []
        self.resolve_image_calls = 0
        self.start_calls: list[tuple] = []
        self.development_start_calls = 0
        self.health_calls: list[tuple] = []

    def resolve_image(self, *_args):
        self.resolve_image_calls += 1
        raise AssertionError("installed activation must not resolve or build an image")

    def inspect(self, _selection):
        return list(self.rows)

    def start(self, *_args):
        self.development_start_calls += 1
        raise AssertionError("installed activation must not use development startup")

    def start_installed(self, selection, image_id, fingerprint, compose_file, timeout, port=None):
        self.start_calls.append((selection, image_id, fingerprint, compose_file, timeout, port))
        self.rows = [_healthy_row(
            selection, image_id=image_id, fingerprint=fingerprint,
            host_port=str(port) if port is not None else "8192",
        )]

    def health(self, url, timeout):
        self.health_calls.append((url, timeout))
        return True


class InstalledHttpHandoffTests(unittest.TestCase):
    def setUp(self) -> None:
        parent = APP.parents[3] / ".caprmedio_tmp" / "installed-http-handoff"
        parent.mkdir(parents=True, exist_ok=True)
        self.root = Path(tempfile.mkdtemp(dir=parent)).resolve()
        self.control = self.root / ".caprmedio_fixture"
        self.control.mkdir()
        (self.control / "caprmedio_project_settings.toml").write_text(
            '[paths]\ncontrol_root = ".caprmedio_fixture"\n\n[project]\nname = "fixture-project"\n',
            encoding="utf-8",
        )
        (self.control / "project_structure.toml").write_text(
            "schema_version = 1\nscope_units = []\n", encoding="utf-8",
        )
        self.config = self.root / ".caprmedio_runtime" / "config.toml"
        self.config.parent.mkdir()
        self.config.write_text(
            "schema_version = 1\n"
            "[project_mcp]\n"
            "startup_timeout_seconds = 7.0\n"
            "build_timeout_seconds = 600.0\n"
            "build_if_missing = true\n"
            "port = 8192\n",
            encoding="utf-8",
        )
        self.config_bytes = self.config.read_bytes()
        self.selection = resolve_project(self.root)
        self.binding = self._binding()
        self.backend = _Backend()
        self.launcher = Launcher(backend=self.backend)

    def _binding(self) -> InstalledMcpBinding:
        package = self.root / ".caprmedio_install" / "releases" / MANIFEST
        compose = package / "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/WORKFLOW_ORCHESTRATOR/docker/project-mcp.compose.yaml"
        compose.parent.mkdir(parents=True, exist_ok=True)
        compose.write_text("services: {}\n", encoding="utf-8")
        context_payload = b"installed target context\n"
        digest = hashlib.sha256(context_payload).hexdigest()
        context_path = self.root / ".caprmedio_runtime" / "installation" / "contexts" / f"{digest}.toml"
        context_path.parent.mkdir(parents=True, exist_ok=True)
        context_path.write_bytes(context_payload)
        return InstalledMcpBinding(
            package_manifest_sha256=MANIFEST,
            source_catalog_sha256=CATALOG,
            target_context=TargetProjectContext(
                digest, "bootstrap", "fixture-project", ".caprmedio_fixture", context_path,
            ),
            package_selector_sha256=PACKAGE_SELECTOR,
            runtime_selector_sha256=RUNTIME_SELECTOR,
            image_digest=IMAGE_DIGEST,
            package_root=package,
            mcp_server=package / "server.py",
            mcp_http_server=package / "http_server.py",
            dockerfile=package / "Dockerfile",
            compose_file=compose,
        )

    def _launch_installed(self, binding=None, **kwargs):
        with patch("project_mcp_launcher.resolve_project", return_value=self.selection):
            return self.launcher.launch_installed(self.root, self.binding if binding is None else binding, **kwargs)

    def _launch_admitted(self, **kwargs):
        with patch("project_mcp_launcher.resolve_project", return_value=self.selection):
            return self.launcher.launch_admitted(
                project_root=self.root,
                control_root=".caprmedio_fixture",
                binding=self.binding,
                image="sha256:" + IMAGE_DIGEST,
                **kwargs,
            )

    def test_installed_handoff_uses_only_selected_image_compose_and_runtime_state(self) -> None:
        result = self._launch_installed(timeout=7)

        self.assertEqual(("started", "READY_STARTED"), (result["disposition"], result["condition"]))
        self.assertEqual("sha256:" + IMAGE_DIGEST, result["image_id"])
        self.assertEqual(RUNTIME_SELECTOR, result["fingerprint"])
        self.assertEqual("http://127.0.0.1:8192/mcp", result["url"])
        self.assertEqual(0, self.backend.resolve_image_calls)
        self.assertEqual(0, self.backend.development_start_calls)
        self.assertEqual(1, len(self.backend.start_calls))
        _selection, image_id, fingerprint, compose_file, _timeout, port = self.backend.start_calls[0]
        self.assertEqual("sha256:" + IMAGE_DIGEST, image_id)
        self.assertEqual(RUNTIME_SELECTOR, fingerprint)
        self.assertEqual(self.binding.compose_file, compose_file)
        self.assertIsNone(port)

        state = self.root / ".caprmedio_runtime" / "runtime" / "project_mcp" / self.selection.instance_id
        self.assertTrue((state / "last_launch.json").is_file())
        self.assertTrue((state / "ready.json").is_file())
        self.assertFalse((self.root / ".caprmedio_install" / "project_mcp").exists())
        self.assertEqual(self.config_bytes, self.config.read_bytes())

    def test_installed_handoff_reuses_only_exact_healthy_runtime(self) -> None:
        self.backend.rows = [_healthy_row(
            self.selection, image_id="sha256:" + IMAGE_DIGEST, fingerprint=RUNTIME_SELECTOR,
        )]

        result = self._launch_installed()

        self.assertEqual(("reused", "READY_REUSED"), (result["disposition"], result["condition"]))
        self.assertEqual([], self.backend.start_calls)
        self.assertEqual(0, self.backend.resolve_image_calls)

    def test_admitted_handoff_reads_config_port_but_never_uses_its_build_setting(self) -> None:
        result = self._launch_admitted()

        self.assertEqual(("started", "READY_STARTED"), (result["disposition"], result["condition"]))
        self.assertEqual(8192, self.backend.start_calls[0][-1])
        self.assertEqual(0, self.backend.resolve_image_calls)
        self.assertEqual(self.config_bytes, self.config.read_bytes())

    def test_explicit_admitted_port_overrides_the_configured_port(self) -> None:
        result = self._launch_admitted(port=8123)

        self.assertEqual(("started", "READY_STARTED"), (result["disposition"], result["condition"]))
        self.assertEqual(8123, self.backend.start_calls[0][-1])
        self.assertEqual(0, self.backend.resolve_image_calls)

    def test_refuses_untyped_or_other_project_binding_without_docker_effects(self) -> None:
        result = self._launch_installed(object())
        self.assertEqual(("refused", "IMAGE_REFUSED"), (result["disposition"], result["condition"]))
        self.assertEqual([], self.backend.start_calls)

        foreign = self._binding()
        foreign = InstalledMcpBinding(
            **{**foreign.__dict__, "target_context": TargetProjectContext(
                foreign.target_context.sha256, "bootstrap", "other-project", ".caprmedio_fixture",
                foreign.target_context.path,
            )}
        )
        result = self._launch_installed(foreign)
        self.assertEqual(("refused", "PROJECT_SELECTION_REFUSED"),
                         (result["disposition"], result["condition"]))
        self.assertEqual([], self.backend.start_calls)
        self.assertEqual(0, self.backend.resolve_image_calls)

    def test_backend_uses_the_installed_compose_carrier_without_an_env_file(self) -> None:
        backend = ProjectMcpBackend()
        commands: list[tuple[tuple[str, ...], dict]] = []

        def capture(argv, **kwargs):
            commands.append((tuple(argv), kwargs))
            return ""

        with patch("project_mcp_backend._bounded_run", side_effect=capture):
            backend.start_installed(
                self.selection, "sha256:" + IMAGE_DIGEST, RUNTIME_SELECTOR,
                self.binding.compose_file, 7, 8123,
            )

        self.assertEqual(1, len(commands))
        argv, _kwargs = commands[0]
        self.assertEqual(str(self.binding.compose_file), argv[argv.index("-f") + 1])
        self.assertEqual("/dev/null", argv[argv.index("--env-file") + 1])


if __name__ == "__main__":
    unittest.main()
