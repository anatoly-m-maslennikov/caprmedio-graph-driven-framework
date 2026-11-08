# CA-M-508@5
# CA-E-799@3
"""Required short resource guard in the ordinary Docker suite."""
import unittest
from workbench_resource_docker import run_resource_case


class WorkbenchResourceDockerTests(unittest.TestCase):
    def test_resource_guard(self):
        run_resource_case(self, 0)
