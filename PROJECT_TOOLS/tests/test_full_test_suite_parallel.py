"""Bounded parallel scheduling, coherent output and unchanged deadlines."""

from contextlib import nullcontext
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import subprocess
import threading
import unittest
from unittest.mock import patch

import test_full_test_suite as fixtures

full = fixtures.full


class FullTestSuiteParallelTests(unittest.TestCase):
    def setUp(self):
        self.case = fixtures.FullTestSuiteTests(methodName="runTest")
        self.case.setUp()
        self.addCleanup(self.case.doCleanups)

    def test_parallel_worker_bounds_and_serial_launcher_keep_one_image(self) -> None:
        modules = [
            self.case.file(f"PROJECT_TOOLS/tests/test_unit_{number}.py") for number in range(8)
        ]
        modules += [
            self.case.file(str(full.APP / f"tests/test_{number}_docker_e2e.py"))
            for number in range(3)
        ]
        selected = self.case.file(str(full.APP / "tests/test_selected_workflows_docker_e2e.py"))
        modules.append(selected)
        active = {"ordinary": 0, "docker": 0}
        peak = dict(active)
        docker_starts: list[Path] = []
        lock, ready, release = threading.Lock(), threading.Event(), threading.Event()

        def execute(root, module, environment):
            lane = "docker" if full._docker_module(root, module) else "ordinary"
            with lock:
                if lane == "docker":
                    docker_starts.append(module)
                active[lane] += 1
                peak[lane] = max(peak[lane], active[lane])
                if sum(active.values()) == 6:
                    ready.set()
            self.assertTrue(release.wait(5))
            with lock:
                active[lane] -= 1
            self.assertEqual("one-image", environment["CAPRMEDIO_IMAGE"])
            return True, 1, 0, f"output:{module.name}\n", f"errors:{module.name}\n", 0.25, None

        def launch(_root, _environment):
            self.assertEqual({"ordinary": 0, "docker": 0}, active)
            return True

        with (
            patch.object(full, "run_module", side_effect=execute),
            patch.object(
                full,
                "current_code_test_image",
                return_value=nullcontext({"CAPRMEDIO_IMAGE": "one-image"}),
            ) as image,
            patch.object(full, "run_launcher", side_effect=launch) as launcher,
            ThreadPoolExecutor(max_workers=1) as driver,
        ):
            future = driver.submit(self.case.run_suite)
            try:
                self.assertTrue(ready.wait(5))
                self.assertEqual({"ordinary": 4, "docker": 2}, peak)
                self.assertIn(selected, docker_starts[:2])
            finally:
                release.set()
            self.assertEqual(0, future.result(timeout=5))
        image.assert_called_once_with(self.case.root)
        launcher.assert_called_once()
        for module in modules:
            relative = module.relative_to(self.case.root)
            self.assertIn(
                f"Test module: {relative}\noutput:{module.name}\nModule time: {relative}: 0.250s\n",
                self.case.output.getvalue(),
            )
            self.assertIn(f"errors:{module.name}\n", self.case.errors.getvalue())
        self.assertIn(
            "Modules: 12; tests run: 12; skipped: 0; failed modules: 0", self.case.output.getvalue()
        )

    def test_all_module_deadlines_remain_1800_seconds(self):
        result = subprocess.CompletedProcess([], 0, fixtures.PASSED_COUNT, "")
        for relative in (
            full.APP / "tests/test_selected_workflows_docker_e2e.py",
            full.APP / "tests/test_selected_query_mcp_e2e.py",
            Path("PROJECT_TOOLS/tests/test_ordinary.py"),
        ):
            module = self.case.file(str(relative))
            with (
                self.subTest(module=relative),
                patch.object(full.subprocess, "run", return_value=result) as command,
            ):
                observed = full.run_module(self.case.root, module)
                self.assertEqual((True, 1, 0), observed[:3])
                self.assertEqual(1800, command.call_args.kwargs["timeout"])


if __name__ == "__main__":
    unittest.main()
