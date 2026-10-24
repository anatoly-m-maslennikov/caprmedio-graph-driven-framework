"""The installed installer retains its Skill and Docker launcher source closure."""

import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

TOOLS = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(TOOLS))

import framework_installation as publication  # noqa: E402


class InstallerDistributionTests(unittest.TestCase):
    def test_installed_commands_work_after_framework_source_is_taken_offline(self):
        directory = Path.cwd() / ".caprmedio_tmp/tests/installer_distribution"
        directory.mkdir(parents=True, exist_ok=True)
        with tempfile.TemporaryDirectory(dir=directory) as temporary:
            base = Path(temporary).resolve()
            framework = base / "framework"
            canonical = framework / publication.SOURCE_DIRECTORY
            shutil.copytree(
                TOOLS,
                canonical,
                ignore=shutil.ignore_patterns("tests", "__pycache__", "*.pyc", ".DS_Store"),
            )
            for relative, source in publication._distribution_sources(TOOLS).items():
                target = publication._distribution_sources(canonical)[relative]
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(source, target)
            with patch.object(publication, "resolve_repository", return_value=framework):
                installed = publication.install_release(framework, apply=True)
                self.assertTrue(publication.installation_status(framework)["verified"])
            (framework / "102_FRAMEWORK_ENGINE").rename(base / "offline-source")
            entrypoint = framework / installed["package_root"] / "INSTALL_TOOLS/install.py"
            repos = base / "repos"
            project = repos / "consumer"
            project.mkdir(parents=True)
            environment = {**os.environ, "CODEX_HOME": str(base / "codex")}
            result = subprocess.run(
                [
                    sys.executable,
                    "-I",
                    "-B",
                    str(entrypoint),
                    "project",
                    "--project-root",
                    str(project),
                    "--prefix=APP",
                    "--apply",
                ],
                env=environment,
                capture_output=True,
                text=True,
                timeout=30,
            )
            self.assertEqual(result.returncode, 0, result.stderr + result.stdout)
            self.assertTrue(json.loads(result.stdout)["ok"])
            self.assertTrue((project / ".agents/skills/ca/SKILL.md").is_file())
            preview = subprocess.run(
                [
                    sys.executable,
                    "-I",
                    "-B",
                    str(entrypoint),
                    "runtime",
                    "--projects-root",
                    str(repos),
                    "--host-settings",
                    str(base / "host/runtime.toml"),
                    "--runtime-root",
                    str(base / "runtime"),
                    "--image",
                    "sha256:" + "a" * 64,
                ],
                env=environment,
                capture_output=True,
                text=True,
                timeout=30,
            )
            self.assertEqual(preview.returncode, 0, preview.stderr + preview.stdout)
            self.assertEqual(
                json.loads(preview.stdout)["result"]["container"]["outcome"], "planned"
            )
            self.assertFalse((base / "host").exists())
            self.assertFalse((base / "codex").exists())


if __name__ == "__main__":
    unittest.main()
