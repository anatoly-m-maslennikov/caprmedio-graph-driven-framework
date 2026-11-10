# CA-E-600@21
# CA-M-504@2
# CA-E-796@2
"""Focused checks for bounded Docker stdout/stderr retention."""

import json
from pathlib import Path
import unittest

import yaml


APP = Path(__file__).resolve().parents[1]
DOCKER = APP / "docker"
EXPECTED_LOGGING = {
    "driver": "local",
    "options": {
        "max-size": "10m",
        "max-file": "3",
        "mode": "non-blocking",
        "max-buffer-size": "1m",
    },
}


def _compose(name: str) -> dict[str, object]:
    return yaml.safe_load((DOCKER / name).read_text(encoding="utf-8"))


class DockerLoggingTests(unittest.TestCase):
    def test_base_runtime_services_use_bounded_local_logging(self):
        config = _compose("compose.yaml")

        self.assertTrue(
            all(service["logging"] == EXPECTED_LOGGING for service in config["services"].values())
        )

    def test_standalone_runtime_services_use_bounded_local_logging(self):
        for compose_name in ("mcp-http.compose.yaml", "project-mcp.compose.yaml"):
            config = _compose(compose_name)
            self.assertTrue(
                all(
                    service["logging"] == EXPECTED_LOGGING
                    for service in config["services"].values()
                ),
                compose_name,
            )

    def test_base_runtime_has_no_agent_service_or_credential_volume(self):
        config = _compose("compose.yaml")
        self.assertEqual({"mcp"}, set(config["services"]))
        self.assertNotIn("volumes", config)

    def test_entrypoint_uses_built_python_without_retained_uv_supervisor(self):
        line = next(line for line in (DOCKER / "Dockerfile").read_text().splitlines()
                    if line.startswith("ENTRYPOINT "))
        self.assertEqual([
            "/opt/venv/bin/python",
            "LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_MCP/docker/entrypoint.py",
        ], json.loads(line.removeprefix("ENTRYPOINT ")))

    def test_image_carries_framework_version_into_workspace(self):
        dockerfile = (DOCKER / "Dockerfile").read_text(encoding="utf-8")
        self.assertIn("COPY version.toml ./", dockerfile)
        self.assertIn("COPY pyproject.toml uv.lock ./", dockerfile)
        self.assertIn("--mount=type=cache,id=caprmedio-uv,target=/tmp/uv-cache uv sync --locked", dockerfile)
        self.assertGreater(dockerfile.index("COPY version.toml ./"), dockerfile.index(" uv sync --locked"))


if __name__ == "__main__":
    unittest.main()
