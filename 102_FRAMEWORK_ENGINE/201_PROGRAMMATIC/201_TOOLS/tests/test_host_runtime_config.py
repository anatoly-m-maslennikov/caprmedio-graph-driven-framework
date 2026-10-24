import hashlib
import os
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[4]
TOOLS = ROOT / "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS"
sys.path[:0] = [str(TOOLS), str(TOOLS / "VALIDATE_ATOMS")]

from host_runtime_config import (  # noqa: E402
    HostRuntimeConfig,
    HostRuntimeConfigError,
    load_host_runtime_config,
    resolve_host_project,
)


class HostRuntimeConfigTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.base = Path(self.temp.name).resolve()
        self.projects = self.base / "My_Repos"
        self.projects.mkdir()
        self.config = self.base / "config" / "runtime.toml"
        self._make_project("alpha")
        self._make_project("beta")

    def tearDown(self):
        self.temp.cleanup()

    def _make_project(self, name: str, prefix: str = "DUP") -> Path:
        root = self.projects / name
        control = root / f".caprmedio_{name}"
        control.mkdir(parents=True)
        (control / "caprmedio_project_settings.toml").write_text(
            f'[project]\nname = "{name}"\n[artifacts.identity]\nproject_prefix = "{prefix}"\n'
            f'[paths]\ncontrol_root = ".caprmedio_{name}"\n',
            encoding="utf-8",
        )
        (control / "project_structure.toml").write_text(
            "schema_version = 1\nscope_units = []\n", encoding="utf-8"
        )
        return root

    def _write_config(self, body: str | None = None, path: Path | None = None) -> Path:
        path = path or self.config
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(
            body
            or f'schema_version = 1\n[shared_mcp]\nprojects_root = "{self.projects}"\nhttp_port = 54321\n',
            encoding="utf-8",
        )
        return path

    def test_loads_valid_config_and_provenance(self):
        path = self._write_config()
        config = load_host_runtime_config(path)
        self.assertIsInstance(config, HostRuntimeConfig)
        self.assertEqual(path, config.source_path)
        self.assertEqual(self.projects, config.projects_root)
        self.assertEqual(2, config.max_loaded_projects)
        self.assertEqual(hashlib.sha256(path.read_bytes()).hexdigest(), config.raw_sha256)
        self.assertEqual(64, len(config.shared_runtime_id))
        self.assertTrue(config.shared_runtime_id == config.shared_runtime_id)

    def test_optional_capacity_and_default_xdg_path_do_not_write(self):
        path = self._write_config(
            f'schema_version = 1\n[shared_mcp]\nprojects_root = "{self.projects}"\n'
            "http_port = 1\nmax_loaded_projects = 64\n"
        )
        self.assertEqual(64, load_host_runtime_config(path).max_loaded_projects)
        xdg = self.base / "xdg"
        default = xdg / "caprmedio/runtime.toml"
        self._write_config(path=default)
        with patch.dict(os.environ, {"XDG_CONFIG_HOME": str(xdg)}):
            config = load_host_runtime_config()
        self.assertEqual(default, config.source_path)
        self.assertFalse((xdg / "caprmedio/runtime.toml.tmp").exists())
        with self.assertRaises(HostRuntimeConfigError):
            load_host_runtime_config(self.base / "missing.toml")

    def test_rejects_unknown_keys_and_non_exact_numbers(self):
        cases = (
            "schema_version = 1\nextra = true\n",
            'schema_version = 1\n[shared_mcp]\nprojects_root = "%s"\nhttp_port = 1\nextra = 1\n'
            % self.projects,
            "schema_version = true\n",
            f'schema_version = 1\n[shared_mcp]\nprojects_root = "{self.projects}"\nhttp_port = true\n',
            f'schema_version = 1\n[shared_mcp]\nprojects_root = "{self.projects}"\nhttp_port = 65536\n',
            f'schema_version = 1\n[shared_mcp]\nprojects_root = "{self.projects}"\nmax_loaded_projects = 65\n',
        )
        for body in cases:
            with self.subTest(body=body), self.assertRaises(HostRuntimeConfigError):
                load_host_runtime_config(self._write_config(body))

    def test_rejects_unsafe_roots_and_config_files(self):
        for root in (self.base / "missing", Path("/")):
            body = f'schema_version = 1\n[shared_mcp]\nprojects_root = "{root}"\nhttp_port = 1\n'
            with self.subTest(root=root), self.assertRaises(HostRuntimeConfigError):
                load_host_runtime_config(self._write_config(body))
        target = self.base / "real.toml"
        self._write_config(path=target)
        link = self.base / "link.toml"
        link.symlink_to(target)
        with self.assertRaises(HostRuntimeConfigError):
            load_host_runtime_config(link)
        oversized = self.base / "oversized.toml"
        self._write_config("x" * 4097, oversized)
        with self.assertRaises(HostRuntimeConfigError):
            load_host_runtime_config(oversized)

    def test_resolves_two_projects_without_prefix_identity_collision(self):
        config = load_host_runtime_config(self._write_config())
        alpha = resolve_host_project(config, self.projects / "alpha")
        beta = config.resolve_project(self.projects / "beta")
        self.assertNotEqual(alpha.instance_id, beta.instance_id)
        self.assertEqual("DUP", alpha.settings["artifacts"]["identity"]["project_prefix"])
        self.assertEqual("DUP", beta.settings["artifacts"]["identity"]["project_prefix"])

    def test_resolve_rejects_outside_parent_traversal_and_symlink_aliases(self):
        config = load_host_runtime_config(self._write_config())
        outside = self.base / "outside"
        outside.mkdir()
        link = self.projects / "alias"
        link.symlink_to(self.projects / "alpha", target_is_directory=True)
        for candidate in (
            self.projects,
            outside,
            self.projects / "missing",
            self.projects / "..",
            link,
        ):
            with self.subTest(candidate=candidate), self.assertRaises(ValueError):
                resolve_host_project(config, candidate)

    def test_resolve_requires_the_declared_prefix(self):
        config = load_host_runtime_config(self._write_config())
        root = self._make_project("missing-prefix", prefix="")
        with self.assertRaises(ValueError):
            resolve_host_project(config, root)


if __name__ == "__main__":
    unittest.main()
