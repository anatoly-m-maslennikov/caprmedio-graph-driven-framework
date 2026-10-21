"""Focused checks for bounded Docker stdout/stderr retention."""

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

    def test_overlays_only_extend_base_runtime_services(self):
        base_services = set(_compose("compose.yaml")["services"])
        for compose_name in ("auth.compose.yaml", "mock.compose.yaml"):
            services = _compose(compose_name)["services"]
            self.assertTrue(set(services) <= base_services, compose_name)

    def test_image_carries_framework_version_into_workspace(self):
        dockerfile = (DOCKER / "Dockerfile").read_text(encoding="utf-8")
        self.assertIn("COPY pyproject.toml uv.lock version.toml ./", dockerfile)


if __name__ == "__main__":
    unittest.main()
