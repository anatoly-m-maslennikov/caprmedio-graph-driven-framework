"""Contract for the checked-in thin Project MCP bootstrap script."""

import importlib.util
from pathlib import Path
from types import SimpleNamespace
import tempfile
import unittest
from unittest.mock import patch


APP = Path(__file__).resolve().parents[1]
SCRIPT = APP / "docker" / "start_mcp.py"


class StartMcpScriptTests(unittest.TestCase):
    def _module(self, script: Path):
        specification = importlib.util.spec_from_file_location("start_mcp_fixture", script)
        self.assertIsNotNone(specification)
        module = importlib.util.module_from_spec(specification)
        self.assertIsNotNone(specification.loader)
        specification.loader.exec_module(module)
        return module

    def test_tracked_bootstrap_delegates_to_project_mcp_without_project_settings_parsing(self) -> None:
        source = SCRIPT.read_text(encoding="utf-8")

        self.assertIn("runtime.py", source)
        self.assertIn("project-mcp", source)
        self.assertNotIn("project_mcp_configuration", source)
        self.assertNotIn("caprmedio_project_settings.toml", source)

    def test_main_uses_locked_uv_project_mcp_url_handoff_only(self) -> None:
        module = self._module(SCRIPT)
        root = APP.parents[3]

        with patch.object(module.subprocess, "run", return_value=SimpleNamespace(returncode=0)) as run:
            self.assertEqual(0, module.main([
                "--project-root", str(root), "--source-root", str(root),
                "--port", "56317", "--no-build",
            ]))

        command = run.call_args.args[0]
        self.assertEqual("uv", command[0])
        self.assertIn("--locked", command)
        self.assertIn("project-mcp", command)
        self.assertEqual(["--output", "url"], command[command.index("--output"):command.index("--output") + 2])
        self.assertEqual(["--port", "56317"], command[command.index("--port"):command.index("--port") + 2])
        self.assertIn("--no-build", command)
        self.assertNotIn("docker", command)
        self.assertNotIn("worker", command)
        self.assertNotIn("workflow", command)

    def test_deployed_bootstrap_uses_the_selected_installed_package_without_a_checkout(self) -> None:
        with tempfile.TemporaryDirectory(prefix="caprmedio-start-mcp-", ignore_cleanup_errors=True) as temporary:
            root = Path(temporary).resolve()
            deployed = root / ".caprmedio_runtime" / "start_mcp.py"
            deployed.parent.mkdir(parents=True)
            deployed.write_bytes(SCRIPT.read_bytes())
            digest = "a" * 64
            package = root / ".caprmedio_install" / "releases" / digest
            launcher = package / "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/WORKFLOW_ORCHESTRATOR/docker/runtime.py"
            launcher.parent.mkdir(parents=True)
            launcher.write_text("# installed launcher fixture\n", encoding="utf-8")
            (root / ".caprmedio_install" / "current.toml").write_text(
                f'schema_version = 1\nrelease_relpath = "releases/{digest}"\n', encoding="utf-8"
            )
            module = self._module(deployed)

            with patch.object(module.subprocess, "run", return_value=SimpleNamespace(returncode=0)) as run:
                self.assertEqual(0, module.main(["--project-root", str(root)]))

        command = run.call_args.args[0]
        self.assertEqual(str(package.resolve()), command[command.index("--project") + 1])
        self.assertIn(str(launcher), command)
        self.assertEqual(["--source-root", str(package.resolve())],
                         command[command.index("--source-root"):command.index("--source-root") + 2])
        self.assertNotIn("worker", command)
        self.assertNotIn("workflow", command)

    def test_deployed_bootstrap_defaults_to_the_simple_local_package_and_target_runtime_paths(self) -> None:
        with tempfile.TemporaryDirectory(prefix="caprmedio-start-mcp-", ignore_cleanup_errors=True) as temporary:
            root = Path(temporary).resolve()
            deployed = root / ".caprmedio_runtime" / "start_mcp.py"
            deployed.parent.mkdir(parents=True)
            deployed.write_bytes(SCRIPT.read_bytes())
            package = root / ".caprmedio_runtime" / "simple_local_release" / "package"
            launcher = package / "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/WORKFLOW_ORCHESTRATOR/docker/runtime.py"
            launcher.parent.mkdir(parents=True)
            launcher.write_text("# simple local package launcher\n", encoding="utf-8")
            module = self._module(deployed)

            with patch.object(module.subprocess, "run", return_value=SimpleNamespace(returncode=0)) as run:
                self.assertEqual(0, module.main(["--project-root", str(root)]))

        command = run.call_args.args[0]
        environment = run.call_args.kwargs["env"]
        self.assertEqual(str(package.resolve()), command[command.index("--project") + 1])
        self.assertIn(str(launcher.resolve()), command)
        self.assertEqual(str(root / ".caprmedio_runtime" / "launcher-venv"),
                         environment["UV_PROJECT_ENVIRONMENT"])
        self.assertEqual(str(root / ".caprmedio_tmp" / "cache" / "uv"), environment["UV_CACHE_DIR"])

    def test_malformed_installed_selector_fails_closed_without_fallback(self) -> None:
        with tempfile.TemporaryDirectory(prefix="caprmedio-start-mcp-", ignore_cleanup_errors=True) as temporary:
            repository = Path(temporary).resolve() / "repository"
            root = repository / "project"
            deployed = root / ".caprmedio_runtime" / "start_mcp.py"
            deployed.parent.mkdir(parents=True)
            deployed.write_bytes(SCRIPT.read_bytes())
            enclosing_launcher = repository / "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/WORKFLOW_ORCHESTRATOR/docker/runtime.py"
            enclosing_launcher.parent.mkdir(parents=True)
            enclosing_launcher.write_text("# enclosing checkout launcher\n", encoding="utf-8")
            (root / ".caprmedio_install").mkdir()
            (root / ".caprmedio_install" / "current.toml").write_text(
                'release_relpath = "releases/not-a-digest"\n', encoding="utf-8"
            )
            module = self._module(deployed)
            with patch.object(module.subprocess, "run") as run:
                with self.assertRaises(SystemExit) as error:
                    module.main(["--project-root", str(root)])

        self.assertEqual(2, error.exception.code)
        run.assert_not_called()

    def test_nested_project_prefers_its_selected_package_over_enclosing_checkout(self) -> None:
        with tempfile.TemporaryDirectory(prefix="caprmedio-start-mcp-", ignore_cleanup_errors=True) as temporary:
            repository = Path(temporary).resolve() / "repository"
            root = repository / "project"
            deployed = root / ".caprmedio_runtime" / "start_mcp.py"
            deployed.parent.mkdir(parents=True)
            deployed.write_bytes(SCRIPT.read_bytes())
            enclosing_launcher = repository / "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/WORKFLOW_ORCHESTRATOR/docker/runtime.py"
            enclosing_launcher.parent.mkdir(parents=True)
            enclosing_launcher.write_text("# enclosing checkout launcher\n", encoding="utf-8")
            digest = "b" * 64
            package = root / ".caprmedio_install" / "releases" / digest
            launcher = package / "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/WORKFLOW_ORCHESTRATOR/docker/runtime.py"
            launcher.parent.mkdir(parents=True)
            launcher.write_text("# selected package launcher\n", encoding="utf-8")
            (root / ".caprmedio_install" / "current.toml").write_text(
                f'schema_version = 1\nrelease_relpath = "releases/{digest}"\n', encoding="utf-8"
            )
            module = self._module(deployed)
            with patch.object(module.subprocess, "run", return_value=SimpleNamespace(returncode=0)) as run:
                self.assertEqual(0, module.main([]))

        command = run.call_args.args[0]
        self.assertEqual(str(root.resolve()), command[command.index("--project-root") + 1])
        self.assertEqual(str(package.resolve()), command[command.index("--project") + 1])
        self.assertIn(str(launcher.resolve()), command)


if __name__ == "__main__":
    unittest.main()
