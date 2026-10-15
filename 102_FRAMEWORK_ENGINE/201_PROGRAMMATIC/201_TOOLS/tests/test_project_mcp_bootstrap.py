"""Package-owned Project MCP bootstrap deployment boundary."""

from pathlib import Path
import stat
import shutil
import sys
import tempfile
import unittest


TOOLS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOLS))

from project_mcp_bootstrap import (  # noqa: E402
    ProjectMcpBootstrapError,
    deploy_project_mcp_bootstrap,
)


RELATIVE = Path(
    "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/"
    "WORKFLOW_ORCHESTRATOR/docker/start_mcp.py"
)


class ProjectMcpBootstrapTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory(prefix="caprmedio-bootstrap-", ignore_cleanup_errors=True)
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name).resolve()
        self.target_root = self.root / "target"
        self.target_root.mkdir()
        self.package = self.target_root / ".caprmedio_install" / "releases" / ("a" * 64)
        self.source = self.package / RELATIVE
        self.source.parent.mkdir(parents=True)
        self.source.write_bytes(b"#!/usr/bin/env python3\n# package bootstrap\n")
        self.source.chmod(0o755)
        self.runtime = self.target_root / ".caprmedio_runtime"
        self.runtime.mkdir(parents=True)
        (self.runtime / "config.toml").write_text("keep = true\n", encoding="utf-8")
        (self.runtime / "state.json").write_text("retain state\n", encoding="utf-8")

    def test_clean_target_receives_only_the_package_bootstrap_and_refresh_preserves_state(self) -> None:
        target = self.runtime / "start_mcp.py"
        self.assertFalse((self.runtime.parent / "102_FRAMEWORK_ENGINE").exists())

        deploy_project_mcp_bootstrap(self.runtime.parent, self.package)
        self.assertEqual(self.source.read_bytes(), target.read_bytes())
        self.assertEqual(0o755, stat.S_IMODE(target.stat().st_mode))
        self.assertEqual("keep = true\n", (self.runtime / "config.toml").read_text())
        self.assertEqual("retain state\n", (self.runtime / "state.json").read_text())

        self.source.write_bytes(b"#!/usr/bin/env python3\n# refreshed package bootstrap\n")
        self.source.chmod(0o755)
        deploy_project_mcp_bootstrap(self.runtime.parent, self.package)
        self.assertEqual(self.source.read_bytes(), target.read_bytes())
        self.assertEqual(0o755, stat.S_IMODE(target.stat().st_mode))
        self.assertEqual("keep = true\n", (self.runtime / "config.toml").read_text())
        self.assertEqual("retain state\n", (self.runtime / "state.json").read_text())

        shutil.rmtree(self.runtime)
        deploy_project_mcp_bootstrap(self.runtime.parent, self.package)
        self.assertEqual(self.source.read_bytes(), target.read_bytes())
        self.assertEqual(0o755, stat.S_IMODE(target.stat().st_mode))

    def test_copy_does_not_execute_package_bootstrap(self) -> None:
        self.source.write_bytes(b"raise RuntimeError('bootstrap must not run during install')\n")

        deploy_project_mcp_bootstrap(self.runtime.parent, self.package)

        self.assertEqual(self.source.read_bytes(), (self.runtime / "start_mcp.py").read_bytes())

    def test_missing_or_symlinked_source_or_destination_refuses(self) -> None:
        self.source.unlink()
        with self.assertRaisesRegex(ProjectMcpBootstrapError, "source-unavailable"):
            deploy_project_mcp_bootstrap(self.runtime.parent, self.package)

        self.source.write_bytes(b"#!/usr/bin/env python3\n")
        self.source.chmod(0o644)
        with self.assertRaisesRegex(ProjectMcpBootstrapError, "source-unsafe"):
            deploy_project_mcp_bootstrap(self.runtime.parent, self.package)

        self.source.chmod(0o755)
        target = self.runtime / "start_mcp.py"
        outside = self.root / "outside.py"
        outside.write_text("outside\n", encoding="utf-8")
        target.symlink_to(outside)
        with self.assertRaisesRegex(ProjectMcpBootstrapError, "source-unsafe"):
            deploy_project_mcp_bootstrap(self.runtime.parent, self.package)

    def test_symlinked_package_source_ancestor_refuses(self) -> None:
        source_root = self.package / "102_FRAMEWORK_ENGINE"
        relocated = self.root / "relocated-engine"
        shutil.move(str(source_root), relocated)
        source_root.symlink_to(relocated, target_is_directory=True)

        with self.assertRaisesRegex(ProjectMcpBootstrapError, "source-unsafe"):
            deploy_project_mcp_bootstrap(self.runtime.parent, self.package)


if __name__ == "__main__":
    unittest.main()
