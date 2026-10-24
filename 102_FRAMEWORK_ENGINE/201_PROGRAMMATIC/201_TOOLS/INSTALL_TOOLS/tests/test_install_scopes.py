"""Functional CLI checks: host and Project installation never cross scopes."""

from contextlib import redirect_stderr
import io
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

INSTALL = Path(__file__).resolve().parents[1] / "install.py"
TOOLS = INSTALL.parents[1]
sys.path.insert(0, str(TOOLS))

from INSTALL_TOOLS.runtime_installation import install_runtime  # noqa: E402


class InstallScopesTests(unittest.TestCase):
    def setUp(self):
        directory = Path.cwd() / ".caprmedio_tmp/tests/install_scopes"
        directory.mkdir(parents=True, exist_ok=True)
        self.temporary = tempfile.TemporaryDirectory(dir=directory)
        self.addCleanup(self.temporary.cleanup)
        self.base = Path(self.temporary.name).resolve()
        self.repos = self.base / "repos"
        self.repos.mkdir()
        self.home = self.base / "codex"
        self.host = self.base / "host/runtime.toml"
        self.runtime = self.base / "runtime"
        self.environment = {**os.environ, "CODEX_HOME": str(self.home)}

    def run_cli(self, *arguments, ok=True):
        result = subprocess.run(
            [sys.executable, "-B", str(INSTALL), *map(str, arguments)],
            env=self.environment,
            text=True,
            capture_output=True,
            timeout=30,
        )
        self.assertEqual(result.returncode, 0 if ok else 2, result.stderr + result.stdout)
        return json.loads(result.stdout)

    def runtime_args(self):
        return (
            "runtime",
            "--projects-root",
            self.repos,
            "--host-settings",
            self.host,
            "--runtime-root",
            self.runtime,
            "--harness=codex",
        )

    def test_runtime_dry_run_is_pure_and_apply_is_idempotent(self):
        before = list(self.base.rglob("*"))
        preview = self.run_cli(*self.runtime_args())
        self.assertFalse(preview["result"]["applied"])
        self.assertEqual(before, list(self.base.rglob("*")))
        first = self.run_cli(*self.runtime_args(), "--http-port=18432", "--apply")
        self.assertEqual(first["result"]["container"]["outcome"], "not_requested")
        self.assertTrue(first["result"]["harness"]["applied"])
        self.assertEqual(first["result"]["harness"]["mode"], "apply")
        self.assertEqual(list(self.repos.iterdir()), [])
        saved = {
            path: path.read_bytes()
            for path in (self.host, self.home / "hooks.json", self.home / "config.toml")
        }
        second = self.run_cli(*self.runtime_args(), "--apply")
        self.assertEqual(second["result"]["settings"]["http_port"], 18432)
        self.assertEqual(saved, {path: path.read_bytes() for path in saved})

    def test_project_setup_never_changes_host_state(self):
        source = self.base / "framework"
        skill = source / "102_FRAMEWORK_ENGINE/202_AGENTIC/205_SKILLS/ca"
        (skill / "agents").mkdir(parents=True)
        (skill / "SKILL.md").write_text("---\nname: ca\ndescription: fixture\n---\n# CA\n")
        (skill / "agents/openai.yaml").write_text("interface:\n  display_name: CA\n")
        project = self.repos / "sample"
        project.mkdir()
        arguments = ("project", "--project-root", project, "--prefix=APP", "--source-root", source)
        before = list(project.iterdir())
        self.run_cli(*arguments)
        self.assertEqual(before, list(project.iterdir()))
        self.run_cli(*arguments, "--apply")
        self.run_cli(*arguments, "--apply")
        self.assertTrue((project / ".agents/skills/ca/SKILL.md").is_file())
        self.assertFalse(self.home.exists())
        self.assertFalse(self.host.exists())
        self.assertFalse(self.runtime.exists())

        self.environment["CODEX_HOME"] = str(self.repos / ".codex")
        self.run_cli(*self.runtime_args(), "--apply", ok=False)
        self.assertFalse((self.repos / ".codex").exists())
        self.assertFalse(self.host.exists())
        self.assertFalse((project / ".caprmedio_runtime/tools").exists())

    def test_invalid_runtime_and_conflicting_mcp_refuse_before_effects(self):
        self.run_cli(*self.runtime_args(), "--http-port=0", "--apply", ok=False)
        self.assertFalse(self.host.exists())
        self.home.mkdir()
        config = self.home / "config.toml"
        config.write_text('[mcp_servers.caprmedio]\ncommand = "existing-server"\n')
        before = config.read_bytes()
        self.run_cli(*self.runtime_args(), "--apply", ok=False)
        self.assertEqual(before, config.read_bytes())
        self.assertFalse(self.host.exists())
        self.assertFalse(self.runtime.exists())

    def test_docker_failure_keeps_configuration_and_returns_verified_partial_result(self):
        class Launcher:
            def apply(_self, settings, image):
                self.assertTrue(settings.is_file())
                return {"outcome": "started", "ready": False, "condition": "readiness_failed"}

        result = install_runtime(
            projects_root=self.repos,
            host_settings=self.host,
            runtime_root=self.runtime,
            image="sha256:" + "a" * 64,
            apply=True,
            launcher=Launcher(),
        )
        self.assertTrue(result["applied"])
        self.assertEqual(result["container"]["outcome"], "started")
        self.assertFalse(result["container"]["ready"])
        self.assertTrue(self.host.is_file())

    def test_unexpected_launch_error_preserves_installed_results_and_warns(self):
        class Launcher:
            def apply(_self, settings, image):
                raise OSError("private provider details")

        diagnostics = io.StringIO()
        with redirect_stderr(diagnostics):
            result = install_runtime(
                projects_root=self.repos,
                host_settings=self.host,
                runtime_root=self.runtime,
                image="sha256:" + "a" * 64,
                apply=True,
                launcher=Launcher(),
            )
        self.assertTrue(result["applied"])
        self.assertTrue(self.host.is_file())
        self.assertFalse(result["container"]["ready"])
        self.assertEqual(result["container"]["error"], "OSError")
        self.assertIn("WARNING", diagnostics.getvalue())
        self.assertNotIn("private provider details", diagnostics.getvalue() + json.dumps(result))


if __name__ == "__main__":
    unittest.main()
