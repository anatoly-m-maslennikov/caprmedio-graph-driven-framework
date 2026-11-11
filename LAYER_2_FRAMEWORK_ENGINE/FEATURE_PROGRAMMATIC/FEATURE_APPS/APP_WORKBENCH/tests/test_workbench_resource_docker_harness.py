"""The resource guard mounts its test-only runner instead of baking it into the image."""

import subprocess
import unittest
from unittest.mock import patch

import workbench_resource_docker as harness


class WorkbenchResourceDockerHarnessTests(unittest.TestCase):
    def test_runner_tests_are_read_only_mounts(self):
        with patch.dict(harness.os.environ, {"CAPRMEDIO_IMAGE": "sha256:" + "a" * 64}), \
                patch.object(harness.subprocess, "run", return_value=subprocess.CompletedProcess([], 0, "WORKBENCH_RESOURCE {}\n", "")) as run:
            harness.run_resource_case(self, 0)
        command = run.call_args_list[0].args[0]
        for path in (harness.TESTS, *harness.SCOPE_FIXTURES):
            self.assertTrue((harness.ROOT / path).exists())
            self.assertIn(f"type=bind,src={harness.ROOT / path},dst=/workspace/{path},readonly", command)
        self.assertEqual(str(harness.RUNNER), command[-3])


if __name__ == "__main__":
    unittest.main()
