"""Unit tests for execution-bound installed MCP transport adapters."""

from __future__ import annotations

from pathlib import Path
import hashlib
import sys
import tempfile
import unittest


TOOLS = Path(__file__).resolve().parents[1]
if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))
DOCKER = TOOLS.parent / "203_APPS" / "WORKFLOW_ORCHESTRATOR" / "docker"
if str(DOCKER) not in sys.path:
    sys.path.insert(0, str(DOCKER))

from framework_package import VerifiedFrameworkPackage  # noqa: E402
from installed_mcp_binding import (  # noqa: E402
    MCP_FILES,
    InstalledMcpBinding,
    TargetProjectContext,
)
from installed_mcp_runtime import (  # noqa: E402
    InstalledMcpRuntimeError,
    RUNTIME_METADATA_RELATIVE,
    launch_installed_mcp_http,
    reopen_installed_mcp_runtime,
    run_installed_mcp_stdio,
)
from project_mcp_launcher import Launcher  # noqa: E402


PACKAGE = "a" * 64
CATALOG = "b" * 64
CONTEXT = "c" * 64
PACKAGE_SELECTOR = "d" * 64
RUNTIME_SELECTOR = "e" * 64
IMAGE = "f" * 64


class _Admitter:
    def __init__(self, root: Path, binding: InstalledMcpBinding) -> None:
        self.root = root
        self.binding = binding
        self.calls: list[tuple[object, object, str]] = []

    def __call__(self, project_root, verified_package, *, target_context_sha256):
        self.calls.append((project_root, verified_package, target_context_sha256))
        if Path(project_root) != self.root:
            raise AssertionError("unexpected Project root")
        return self.binding


class _HttpLauncher:
    def __init__(self) -> None:
        self.calls: list[dict[str, object]] = []

    def launch_admitted(self, **kwargs):
        self.calls.append(kwargs)
        return {"condition": "delegated"}

    def launch(self, *args, **kwargs):  # pragma: no cover - assertion contract
        raise AssertionError("legacy checkout launcher must never be used")

    def launch_installed(self, *args, **kwargs):  # pragma: no cover - assertion contract
        raise AssertionError("adapter must use the public admitted launcher seam")


class _AdmittedHttpBackend:
    """No-Docker backend for the real admitted-launcher adapter coverage."""

    def __init__(self) -> None:
        self.rows: list[dict[str, object]] = []
        self.start_calls: list[tuple[object, ...]] = []
        self.resolve_image_calls = 0

    def resolve_image(self, *_args):  # pragma: no cover - assertion contract
        self.resolve_image_calls += 1
        raise AssertionError("admitted startup must not resolve or build an image")

    def inspect(self, _selection):
        return list(self.rows)

    def start_installed(self, selection, image_id, fingerprint, compose_file, timeout, port=None):
        self.start_calls.append((selection, image_id, fingerprint, compose_file, timeout, port))
        self.rows = [{
            "Id": "runtime-fixture",
            "Image": image_id,
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


class InstalledMcpRuntimeTests(unittest.TestCase):
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
        self.config = self.root / ".caprmedio_runtime/config.toml"
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
        self.package_root = self.root / ".caprmedio_install/releases" / PACKAGE
        for relative in MCP_FILES:
            target = self.package_root / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text("# selected package carrier\n", encoding="utf-8")
        context_path = self.root / ".caprmedio_runtime/installation/contexts" / f"{CONTEXT}.toml"
        context_path.parent.mkdir(parents=True, exist_ok=True)
        context_path.write_text("schema_version = 1\n", encoding="utf-8")
        self.binding = InstalledMcpBinding(
            package_manifest_sha256=PACKAGE,
            source_catalog_sha256=CATALOG,
            target_context=TargetProjectContext(
                sha256=CONTEXT,
                mode="bootstrap",
                target_project_identity="fixture-project",
                control_child_relpath=".caprmedio_fixture",
                path=context_path,
            ),
            package_selector_sha256=PACKAGE_SELECTOR,
            runtime_selector_sha256=RUNTIME_SELECTOR,
            image_digest=IMAGE,
            package_root=self.package_root,
            mcp_server=self.package_root / MCP_FILES[1],
            mcp_http_server=self.package_root / MCP_FILES[0],
            dockerfile=self.package_root / MCP_FILES[3],
            compose_file=self.package_root / MCP_FILES[-1],
        )
        self.package = VerifiedFrameworkPackage(
            PACKAGE, self.package_root, (), "1.2.3", "1" * 64, CATALOG,
        )
        self.admitter = _Admitter(self.root, self.binding)

    def test_stdio_reopens_admission_and_yields_only_selected_project_container_access(self) -> None:
        requests = []

        result = run_installed_mcp_stdio(
            self.root,
            ".caprmedio_fixture",
            self.package,
            target_context_sha256=CONTEXT,
            package_selector_sha256=PACKAGE_SELECTOR,
            runtime_selector_sha256=RUNTIME_SELECTOR,
            compose_file=self.binding.compose_file,
            image="sha256:" + IMAGE,
            binding_admitter=self.admitter,
            runner=lambda request: requests.append(request) or "attached",
        )

        self.assertEqual("attached", result)
        self.assertEqual(1, len(self.admitter.calls))
        self.assertEqual(1, len(requests))
        request = requests[0]
        self.assertEqual("sha256:" + IMAGE, request.image)
        self.assertEqual(("mcp",), request.command)
        self.assertEqual(
            (
                "uv", "run", "--locked", "--no-sync", "--no-env-file",
                "--group", "rmed-workflow-mcp", "--group", "workflow-orchestrator",
                "python", "/workspace/" + MCP_FILES[4],
            ),
            request.entrypoint,
        )
        self.assertEqual(self.binding.mcp_server, request.server_file)
        self.assertTrue(request.stdin_attached)
        self.assertTrue(request.stdout_attached)
        self.assertEqual("none", request.network_mode)
        self.assertEqual((), request.published_ports)
        self.assertEqual(1, len(request.mounts))
        mount = request.mounts[0]
        self.assertEqual(self.root, mount.source)
        self.assertEqual("/project", mount.target)
        self.assertFalse(mount.read_only)
        self.assertNotIn(".git", str(mount.source))
        self.assertNotIn("auth", str(mount.source))
        self.assertNotIn("agent", str(mount.source))
        self.assertEqual(
            (
                ("CAPRMEDIO_CONTROL_ROOT", ".caprmedio_fixture"),
                ("CAPRMEDIO_PROJECT_INSTANCE_ID", hashlib.sha256(
                    f"{self.root}\0.caprmedio_fixture".encode("utf-8")
                ).hexdigest()),
                ("CAPRMEDIO_HOST_PROJECT_ROOT", str(self.root)),
            ),
            request.environment,
        )
        self.assertTrue(request.read_only)
        self.assertEqual(("ALL",), request.cap_drop)

    def test_http_reopens_admission_then_uses_only_admitted_launcher_seam(self) -> None:
        launcher = _HttpLauncher()

        result = launch_installed_mcp_http(
            self.root,
            ".caprmedio_fixture",
            self.package,
            target_context_sha256=CONTEXT,
            binding_admitter=self.admitter,
            launcher=launcher,
            port=8123,
        )

        self.assertEqual({"condition": "delegated"}, result)
        self.assertEqual(1, len(self.admitter.calls))
        self.assertEqual(1, len(launcher.calls))
        self.assertEqual(self.root, launcher.calls[0]["project_root"])
        self.assertIs(self.binding, launcher.calls[0]["binding"])
        self.assertEqual(".caprmedio_fixture", launcher.calls[0]["control_root"])
        self.assertEqual("sha256:" + IMAGE, launcher.calls[0]["image"])
        self.assertEqual(8123, launcher.calls[0]["port"])

    def test_http_adapter_uses_real_config_aware_admitted_seam_for_default_and_override_port(self) -> None:
        for requested, expected in ((None, 8192), (8123, 8123)):
            with self.subTest(port=requested):
                backend = _AdmittedHttpBackend()
                result = launch_installed_mcp_http(
                    self.root,
                    ".caprmedio_fixture",
                    self.package,
                    target_context_sha256=CONTEXT,
                    binding_admitter=self.admitter,
                    launcher=Launcher(backend=backend),
                    port=requested,
                )

                self.assertEqual(("started", "READY_STARTED"),
                                 (result["disposition"], result["condition"]))
                self.assertEqual(1, len(backend.start_calls))
                _selection, image, _fingerprint, compose, _timeout, port = backend.start_calls[0]
                self.assertEqual("sha256:" + IMAGE, image)
                self.assertEqual(self.binding.compose_file, compose)
                self.assertEqual(expected, port)
                self.assertEqual(0, backend.resolve_image_calls)
                self.assertEqual(self.config_bytes, self.config.read_bytes())

    def test_http_rejects_invalid_port_before_reopening_or_delegating(self) -> None:
        launcher = _HttpLauncher()
        for invalid in (True, 0, 65536, "8123"):
            with self.subTest(port=invalid), self.assertRaisesRegex(InstalledMcpRuntimeError, "HTTP port") as error:
                launch_installed_mcp_http(
                    self.root,
                    ".caprmedio_fixture",
                    self.package,
                    target_context_sha256=CONTEXT,
                    binding_admitter=self.admitter,
                    launcher=launcher,
                    port=invalid,
                )
            self.assertEqual("installed-mcp-port-invalid", error.exception.code)
        self.assertEqual([], self.admitter.calls)
        self.assertEqual([], launcher.calls)

    def test_rejects_override_paths_and_mismatched_admitted_values(self) -> None:
        with self.assertRaisesRegex(InstalledMcpRuntimeError, "source roots") as source_error:
            reopen_installed_mcp_runtime(
                self.root, ".caprmedio_fixture", self.package,
                target_context_sha256=CONTEXT, transport="http",
                source_root=self.root / "checkout", binding_admitter=self.admitter,
            )
        self.assertEqual("installed-mcp-source-override-forbidden", source_error.exception.code)
        self.assertEqual([], self.admitter.calls)

        with self.assertRaisesRegex(InstalledMcpRuntimeError, "checkout roots") as checkout_error:
            reopen_installed_mcp_runtime(
                self.root, ".caprmedio_fixture", self.package,
                target_context_sha256=CONTEXT, transport="http",
                checkout_root=self.root / "checkout", binding_admitter=self.admitter,
            )
        self.assertEqual("installed-mcp-checkout-override-forbidden", checkout_error.exception.code)
        self.assertEqual([], self.admitter.calls)

        with self.assertRaisesRegex(InstalledMcpRuntimeError, "selector differs") as selector_error:
            reopen_installed_mcp_runtime(
                self.root, ".caprmedio_fixture", self.package,
                target_context_sha256=CONTEXT, transport="http",
                package_selector_sha256="0" * 64, binding_admitter=self.admitter,
            )
        self.assertEqual("installed-mcp-selector-mismatch", selector_error.exception.code)
        self.assertEqual(1, len(self.admitter.calls))

        with self.assertRaisesRegex(InstalledMcpRuntimeError, "control root differs") as control_error:
            reopen_installed_mcp_runtime(
                self.root, ".caprmedio_other", self.package,
                target_context_sha256=CONTEXT, transport="stdio", binding_admitter=self.admitter,
            )
        self.assertEqual("installed-mcp-control-mismatch", control_error.exception.code)

    def test_metadata_location_is_only_a_descriptor_not_created_runtime_state(self) -> None:
        runtime = reopen_installed_mcp_runtime(
            self.root, ".caprmedio_fixture", self.package,
            target_context_sha256=CONTEXT, transport="stdio", binding_admitter=self.admitter,
        )

        self.assertEqual(self.root.joinpath(*RUNTIME_METADATA_RELATIVE.parts), runtime.metadata_root)
        self.assertFalse(runtime.metadata_root.exists())


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
