"""Consumer validation and byte-preserving runtime TOML reads."""

import sys
import tempfile
import tomllib
import unittest
from pathlib import Path

TOOLS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOLS))

from project_mcp_configuration import load_project_mcp_settings, parse_project_mcp_settings
from runtime_configuration import RuntimeConfigurationError


class ProjectMCPConfigurationTests(unittest.TestCase):
    def defaults(self):
        return tomllib.loads((TOOLS.parents[2] / "defaults/runtime-config.toml").read_text())

    def test_default_carrier_has_current_values_and_dynamic_port(self):
        settings = parse_project_mcp_settings(self.defaults())
        self.assertEqual((settings.startup_timeout_seconds, settings.build_timeout_seconds), (60.0, 600.0))
        self.assertTrue(settings.build_if_missing)
        self.assertIsNone(settings.port)

    def test_custom_values_and_unrelated_sections_are_preserved(self):
        root = Path(tempfile.mkdtemp(prefix="caprmedio-mcp-config-")).resolve()
        config = root / ".caprmedio_runtime/config.toml"
        config.parent.mkdir()
        payload = b"# personal comment\nschema_version=1\n[other]\nvalue='keep'\n[project_mcp]\nstartup_timeout_seconds=12\nbuild_timeout_seconds=90\nbuild_if_missing=false\nport=43210\n"
        config.write_bytes(payload)
        settings = load_project_mcp_settings(root)
        self.assertEqual((settings.port, settings.startup_timeout_seconds), (43210, 12.0))
        self.assertFalse(settings.build_if_missing)
        self.assertEqual(config.read_bytes(), payload)

    def test_absent_config_does_not_fall_back_or_create_file(self):
        root = Path(tempfile.mkdtemp(prefix="caprmedio-mcp-config-")).resolve()
        with self.assertRaises(RuntimeConfigurationError) as caught:
            load_project_mcp_settings(root)
        self.assertEqual(caught.exception.code, "runtime-config-missing")
        self.assertFalse((root / ".caprmedio_runtime").exists())

    def test_invalid_or_missing_values_require_migration(self):
        for key, value in (("port", True), ("port", 0), ("port", 65536),
                           ("startup_timeout_seconds", float("nan")),
                           ("startup_timeout_seconds", 61), ("build_timeout_seconds", -1),
                           ("build_if_missing", "true")):
            document = self.defaults()
            document["project_mcp"][key] = value
            with self.subTest(key=key, value=value), self.assertRaises(RuntimeConfigurationError):
                parse_project_mcp_settings(document)
        document = self.defaults()
        del document["project_mcp"]["startup_timeout_seconds"]
        with self.assertRaises(RuntimeConfigurationError):
            parse_project_mcp_settings(document)


if __name__ == "__main__":
    unittest.main()
