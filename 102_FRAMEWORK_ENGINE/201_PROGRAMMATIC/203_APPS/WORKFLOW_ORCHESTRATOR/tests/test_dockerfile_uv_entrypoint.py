"""Keep image startup inside the locked, pre-synced uv environment."""

import json
from pathlib import Path
import unittest


class DockerfileUVEntrypointTests(unittest.TestCase):
    def test_entrypoint_has_no_ambient_python_or_environment_file_fallback(self):
        dockerfile = Path(__file__).resolve().parents[1] / "docker/Dockerfile"
        rows = [line for line in dockerfile.read_text().splitlines() if line.startswith("ENTRYPOINT ")]
        self.assertEqual(len(rows), 1)
        command = json.loads(rows[0].removeprefix("ENTRYPOINT "))
        self.assertEqual(command[:6], ["uv", "run", "--locked", "--no-sync", "--no-env-file", "python"])
        self.assertEqual(command[6:], ["102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/WORKFLOW_ORCHESTRATOR/docker/entrypoint.py"])


if __name__ == "__main__":
    unittest.main()
