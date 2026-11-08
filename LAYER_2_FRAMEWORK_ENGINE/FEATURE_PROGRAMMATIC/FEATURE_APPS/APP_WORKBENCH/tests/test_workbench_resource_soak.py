# CA-M-508@5
# CA-E-800@3
"""Optional long-running leak acceptance, separate from required Docker cases."""
import os
import unittest
from workbench_resource_docker import run_resource_case


@unittest.skipUnless(os.environ.get("CAPRMEDIO_WORKBENCH_SOAK_SECONDS"), "30-minute soak is opt-in")
class WorkbenchResourceSoakTests(unittest.TestCase):
    def test_leak_soak(self):
        seconds = int(os.environ["CAPRMEDIO_WORKBENCH_SOAK_SECONDS"])
        self.assertGreaterEqual(seconds, 1800, "acceptance needs 30 real minutes")
        run_resource_case(self, seconds)
