"""Selector-owned installed MCP CLI tests; Docker is always transport-injected."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
import shutil
import sys
import tempfile
import unittest


TOOLS = Path(__file__).resolve().parents[1]
if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))
DOCKER = TOOLS.parent / "203_APPS" / "WORKFLOW_ORCHESTRATOR" / "docker"
if str(DOCKER) not in sys.path:
    sys.path.insert(0, str(DOCKER))

from framework_package import assemble_framework_package, verify_framework_package  # noqa: E402
from installed_mcp_binding import MCP_FILES  # noqa: E402
from installed_mcp_cli import InstalledMcpCliError, run_installed_mcp_cli  # noqa: E402
from project_mcp_launcher import Launcher  # noqa: E402


IMAGE = "a" * 64
GATE = "b" * 64
SETTINGS = "c" * 64
STRUCTURE = "d" * 64
REGISTRY = "e" * 64
VERSION_PAYLOAD = b'[framework]\nversion = "1.2.3"\n'


def _digest(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def _compose() -> bytes:
    return b'''services:
  mcp-http:
    image: ${CAPRMEDIO_IMAGE:?An admitted immutable image is required}
    init: true
    read_only: true
    cap_drop: [ALL]
    security_opt: [no-new-privileges:true]
    restart: "no"
    stop_grace_period: 10s
    tmpfs: ["/tmp:size=128m,mode=1777"]
    pids_limit: 128
    mem_limit: 512m
    cpus: 1
    command: [mcp-http]
    environment:
      CAPRMEDIO_RUNTIME_NAMESPACE: docker
      CAPRMEDIO_CONTROL_ROOT: ${CAPRMEDIO_CONTROL_ROOT:?Selected control root is required}
      CAPRMEDIO_PROJECT_INSTANCE_ID: ${CAPRMEDIO_PROJECT_INSTANCE_ID:?Selected identity is required}
      CAPRMEDIO_HOST_PROJECT_ROOT: ${CAPRMEDIO_PROJECT_ROOT:?Selected Project root is required}
    labels:
      org.caprmedio.project: ${CAPRMEDIO_PROJECT_INSTANCE_ID}
      org.caprmedio.runtime.fingerprint: ${CAPRMEDIO_RUNTIME_FINGERPRINT:?Image fingerprint is required}
      org.caprmedio.service: mcp-http
      org.caprmedio.control_root: ${CAPRMEDIO_CONTROL_ROOT}
      org.caprmedio.host_project_root: ${CAPRMEDIO_PROJECT_ROOT}
    volumes:
      - type: bind
        source: ${CAPRMEDIO_PROJECT_ROOT}
        target: /project
    ports: ["127.0.0.1:${CAPRMEDIO_MCP_HTTP_PORT:-}:8092"]
    healthcheck:
      test: [CMD, python, -c, "import json,urllib.request; assert json.load(urllib.request.urlopen('http://127.0.0.1:8092/health',timeout=3))['ready'] is True"]
      interval: 2s
      timeout: 5s
      retries: 25
      start_period: 3s
'''


class _Backend:
    """No-Docker backend that models the narrow installed launcher seam."""

    def __init__(self) -> None:
        self.rows: list[dict[str, object]] = []
        self.start_calls: list[tuple[object, ...]] = []
        self.resolve_image_calls = 0

    def resolve_image(self, *_args):  # pragma: no cover - assertion contract
        self.resolve_image_calls += 1
        raise AssertionError("installed CLI must not resolve a development image")

    def inspect(self, _selection):
        return list(self.rows)

    def start_installed(self, selection, image, fingerprint, compose, timeout, port=None):
        self.start_calls.append((selection, image, fingerprint, compose, timeout, port))
        self.rows = [{
            "Id": "cli-fixture",
            "Image": image,
            "Config": {"Labels": {
                "org.caprmedio.project": selection.instance_id,
                "org.caprmedio.runtime.fingerprint": fingerprint,
                "org.caprmedio.service": "mcp-http",
            }},
            "State": {"Status": "running", "Health": {"Status": "healthy"}},
            "NetworkSettings": {"Ports": {
                "8092/tcp": [{"HostIp": "127.0.0.1", "HostPort": str(port)}],
            }},
        }]

    def health(self, _url, _timeout):
        return True


class InstalledMcpCliTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory(dir="/private/tmp", ignore_cleanup_errors=True)
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name).resolve()
        self.control = self.root / ".caprmedio_fixture"
        self.control.mkdir()
        (self.control / "caprmedio_project_settings.toml").write_text(
            '[paths]\ncontrol_root = ".caprmedio_fixture"\n\n[project]\nname = "fixture-project"\n',
            encoding="utf-8",
        )
        (self.control / "project_structure.toml").write_text(
            "schema_version = 1\nscope_units = []\n", encoding="utf-8",
        )
        self.package = self._package()
        self.context = self._write_context()
        self._write_selectors()
        self.config = self.root / ".caprmedio_runtime/config.toml"
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

    def _package(self):
        source = self.root / "package-source"
        payloads: dict[str, bytes] = {
            "pyproject.toml": b"[project]\nname = 'fixture'\n",
            "uv.lock": b"version = 1\n",
            "version.toml": VERSION_PAYLOAD,
            "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/tool.py": b"# package core\n",
            "methodology/active/CA-R-001--fixture.md": b"# active methodology\n",
            "methodology/support/CA-D-001--fixture.md": b"# declared support\n",
            "SKILLS/ca/SKILL.md": b"# ca\n",
            "defaults/framework.toml": b"[defaults]\nname = 'fixture'\n",
        }
        for relative in MCP_FILES:
            payloads[relative] = b"# exact package-owned carrier\n"
        payloads[MCP_FILES[-1]] = _compose()
        for relative, payload in payloads.items():
            target = source / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(payload)
            target.chmod(0o644)
        self._write_catalog(source)
        assembled = assemble_framework_package(source, self.root / ".caprmedio_install/releases")
        return verify_framework_package(assembled.root)

    def _write_catalog(self, source: Path) -> None:
        rows = (
            ("core", "core", "102_FRAMEWORK_ENGINE"),
            ("methodology", "methodology", "methodology/active"),
            ("support", "support", "methodology/support"),
        )
        lines = ["schema_version = 1", ""]
        for identity, kind, relative in rows:
            lines.extend((
                f"[source.{identity}]", f'kind = "{kind}"', f'revision = "{"a" * 40}"',
                f'sha256 = "{self._tree_digest(source / relative)}"',
                f'admission_receipt_sha256 = "{"b" * 64}"', 'visibility = "public"',
                "selection_default = false", f'path = "{relative}"', "",
            ))
        (source / "catalog.toml").write_text("\n".join(lines), encoding="utf-8")

    @staticmethod
    def _tree_digest(root: Path) -> str:
        rows = [
            {"path": path.relative_to(root).as_posix(), "sha256": _digest(path.read_bytes()),
             "mode": path.stat().st_mode & 0o777}
            for path in sorted(root.rglob("*"), key=lambda item: item.as_posix()) if path.is_file()
        ]
        return _digest(json.dumps(rows, sort_keys=True, separators=(",", ":")).encode("utf-8"))

    def _write_context(self) -> str:
        payload = (
            "schema_version = 1\nmode = \"bootstrap\"\n"
            "target_project_identity = \"fixture-project\"\n"
            "control_child_relpath = \".caprmedio_fixture\"\n"
            f"settings_sha256 = \"{SETTINGS}\"\nproject_structure_sha256 = \"{STRUCTURE}\"\n"
            f"registry_sha256 = \"{REGISTRY}\"\nrepository_identity = false\nroot_locator = \"fixture-project\"\n"
        ).encode("utf-8")
        digest = _digest(payload)
        path = self.root / ".caprmedio_runtime/installation/contexts" / f"{digest}.toml"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(payload)
        path.chmod(0o644)
        return digest

    def _write_selectors(self) -> None:
        selector = self.root / ".caprmedio_install/current.toml"
        selector.write_text(
            "schema_version = 1\n"
            f'package_manifest_sha256 = "{self.package.manifest_digest}"\n'
            f'release_relpath = "releases/{self.package.manifest_digest}"\n'
            'framework_version = "1.2.3"\n'
            f'version_toml_sha256 = "{_digest(VERSION_PAYLOAD)}"\n'
            f'source_catalog_sha256 = "{self.package.source_catalog_sha256}"\n'
            f'full_gate_receipt_sha256 = "{GATE}"\nimage_digest = "{IMAGE}"\n',
            encoding="utf-8",
        )
        runtime = self.root / ".caprmedio_runtime/installation/current.toml"
        runtime.parent.mkdir(parents=True, exist_ok=True)
        runtime.write_text(
            "schema_version = 1\n"
            f'package_manifest_sha256 = "{self.package.manifest_digest}"\n'
            f'target_project_context_sha256 = "{self.context}"\n'
            "state_generation = 1\ninstallation_lock_generation = 1\n"
            f'image_digest = "{IMAGE}"\n',
            encoding="utf-8",
        )

    def _arguments(self, *extra: str) -> list[str]:
        return ["--project-root", str(self.root), "--control-root", ".caprmedio_fixture", *extra]

    def test_http_cli_derives_canonical_package_and_reaches_real_admitted_adapter(self) -> None:
        for extra, expected_port in (((), 8192), (("--port", "8123"), 8123)):
            with self.subTest(extra=extra):
                backend = _Backend()
                result = run_installed_mcp_cli(
                    self._arguments(*extra),
                    launcher_factory=lambda: Launcher(backend=backend),
                    docker_transport=lambda _argv: self.fail("HTTP mode must not invoke Docker runner"),
                )
                self.assertEqual(("started", "READY_STARTED"),
                                 (result["disposition"], result["condition"]))
                self.assertEqual(1, len(backend.start_calls))
                _selection, image, _fingerprint, compose, _timeout, port = backend.start_calls[0]
                self.assertEqual("sha256:" + IMAGE, image)
                self.assertEqual(self.package.root / MCP_FILES[-1], compose)
                self.assertEqual(expected_port, port)
                self.assertEqual(0, backend.resolve_image_calls)
                self.assertEqual(self.config_bytes, self.config.read_bytes())

    def test_stdio_cli_translates_only_the_admitted_project_bind_and_uv_command(self) -> None:
        commands: list[tuple[str, ...]] = []
        result = run_installed_mcp_cli(
            self._arguments("--mode", "stdio"),
            launcher_factory=lambda: self.fail("stdio must not construct an HTTP launcher"),
            docker_transport=lambda argv: commands.append(argv) or 0,
        )

        self.assertEqual(0, result)
        self.assertEqual(1, len(commands))
        command = commands[0]
        self.assertEqual(("docker", "run", "--rm", "--interactive"), command[:4])
        self.assertIn("--read-only", command)
        self.assertEqual("none", command[command.index("--network") + 1])
        self.assertNotIn("--publish", command)
        self.assertNotIn("--env-file", command)
        self.assertEqual(1, command.count("--mount"))
        self.assertEqual(f"type=bind,src={self.root},dst=/project", command[command.index("--mount") + 1])
        self.assertEqual("uv", command[command.index("--entrypoint") + 1])
        image_index = command.index("sha256:" + IMAGE)
        self.assertEqual(
            ("run", "--locked", "--no-sync", "--no-env-file", "--group", "rmed-workflow-mcp",
             "--group", "workflow-orchestrator", "python", "/workspace/" + MCP_FILES[4], "mcp"),
            command[image_index + 1:],
        )
        self.assertEqual(self.config_bytes, self.config.read_bytes())

    def test_missing_selector_refuses_before_launcher_or_docker_effect(self) -> None:
        (self.root / ".caprmedio_install/current.toml").unlink()
        invoked = []
        with self.assertRaises(InstalledMcpCliError) as raised:
            run_installed_mcp_cli(
                self._arguments(),
                launcher_factory=lambda: invoked.append("launcher"),
                docker_transport=lambda _argv: invoked.append("docker"),
            )
        self.assertEqual("installed-cli-package-selector-missing", raised.exception.code)
        self.assertEqual([], invoked)

    def test_stdio_cli_refuses_canonical_project_root_with_comma_before_transport(self) -> None:
        with tempfile.TemporaryDirectory(
            prefix="caprmedio,cli-", dir="/private/tmp", ignore_cleanup_errors=True,
        ) as temporary:
            comma_root = Path(temporary).resolve()
            shutil.copytree(
                self.root, comma_root, dirs_exist_ok=True,
                ignore=shutil.ignore_patterns("package-source"),
            )
            invoked = []
            with self.assertRaises(InstalledMcpCliError) as raised:
                run_installed_mcp_cli(
                    ["--project-root", str(comma_root), "--control-root", ".caprmedio_fixture", "--mode", "stdio"],
                    launcher_factory=lambda: self.fail("stdio must not create an HTTP launcher"),
                    docker_transport=lambda _argv: invoked.append("docker") or 0,
                )
        self.assertEqual("installed-cli-stdio-invalid", raised.exception.code)
        self.assertEqual([], invoked)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
