"""Ordinary startup namespaces remain explicit after Release-host retirement."""

import os
from pathlib import Path
import sys
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import runtime_config as config  # noqa: E402


class RuntimeNamespaceTests(unittest.TestCase):
    def test_native_and_docker_keep_their_exact_paths(self):
        base = ".caprmedio_install/workflow_orchestrator"
        for namespace, expected in (("", base), ("docker", base + "/docker")):
            with (
                self.subTest(namespace=namespace),
                patch.dict(os.environ, {"CAPRMEDIO_RUNTIME_NAMESPACE": namespace}),
            ):
                self.assertEqual(expected, config.control_directory())
                self.assertEqual(namespace == "docker", config.docker_runtime())

    def test_retired_release_host_never_falls_back_to_ordinary_startup(self):
        with patch.dict(os.environ, {"CAPRMEDIO_RUNTIME_NAMESPACE": "release-host"}):
            for selector in (
                config.control_directory,
                config.docker_runtime,
                config.implementation_mock_runtime,
            ):
                with (
                    self.subTest(selector=selector.__name__),
                    self.assertRaisesRegex(ValueError, "Unsupported runtime namespace"),
                ):
                    selector()

    def test_other_unknown_namespaces_are_still_rejected(self):
        with patch.dict(os.environ, {"CAPRMEDIO_RUNTIME_NAMESPACE": "unknown"}):
            with self.assertRaisesRegex(ValueError, "Unsupported runtime namespace"):
                config.control_directory()

    def test_mock_mode_still_requires_explicit_docker_startup(self):
        with patch.dict(
            os.environ, {"CAPRMEDIO_AGENT_MODE": "mock", "CAPRMEDIO_RUNTIME_NAMESPACE": ""}
        ):
            with self.assertRaisesRegex(ValueError, "requires explicit Docker startup"):
                config.implementation_mock_runtime()
        with patch.dict(
            os.environ, {"CAPRMEDIO_AGENT_MODE": "mock", "CAPRMEDIO_RUNTIME_NAMESPACE": "docker"}
        ):
            self.assertTrue(config.implementation_mock_runtime())

    def test_normal_agent_modes_and_invalid_mode_keep_their_meanings(self):
        for mode in ("", "codex"):
            with (
                self.subTest(mode=mode),
                patch.dict(
                    os.environ, {"CAPRMEDIO_AGENT_MODE": mode, "CAPRMEDIO_RUNTIME_NAMESPACE": ""}
                ),
            ):
                self.assertFalse(config.implementation_mock_runtime())
        with patch.dict(
            os.environ, {"CAPRMEDIO_AGENT_MODE": "invalid", "CAPRMEDIO_RUNTIME_NAMESPACE": "docker"}
        ):
            with self.assertRaisesRegex(ValueError, "Unsupported Agent runtime mode"):
                config.implementation_mock_runtime()


if __name__ == "__main__":
    unittest.main()
