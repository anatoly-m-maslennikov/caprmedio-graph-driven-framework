"""Bounded parallel scheduling, coherent output and unchanged deadlines."""

from contextlib import nullcontext
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import subprocess
import threading
import time
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
            self.case.file(f"PROJECT_TOOLS/tests/test_unit_{number}.py") for number in range(5)
        ]
        long_host = [
            self.case.file(str(full.APP / "tests/test_selected_subject_apply.py")),
            self.case.file(
                str(full.APP.parents[1] / "204_MCP/tests/test_subject_publication_confirmation.py")
            ),
            self.case.file(
                str(full.APP.parents[1] / "204_MCP/tests/test_subject_publication_gateway.py")
            ),
        ]
        modules += long_host
        modules += [
            self.case.file(str(full.APP / f"tests/test_{number}_docker_e2e.py"))
            for number in range(3)
        ]
        selected = self.case.file(str(full.APP / "tests/test_selected_workflows_docker_e2e.py"))
        modules.append(selected)
        active = {"ordinary": 0, "docker": 0}
        peak = dict(active)
        docker_starts: list[Path] = []
        ordinary_starts: list[Path] = []
        lock, ready, release = threading.Lock(), threading.Event(), threading.Event()

        def execute(root, module, environment):
            lane = "docker" if full._docker_module(root, module) else "ordinary"
            with lock:
                if lane == "docker":
                    docker_starts.append(module)
                else:
                    ordinary_starts.append(module)
                active[lane] += 1
                peak[lane] = max(peak[lane], active[lane])
                if sum(active.values()) == 4:
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
                self.assertEqual({"ordinary": 2, "docker": 2}, peak)
                self.assertIn(selected, docker_starts[:2])
                self.assertEqual(set(long_host[:2]), set(ordinary_starts[:2]))
            finally:
                release.set()
            self.assertEqual(0, future.result(timeout=5))
        image.assert_called_once_with(self.case.root)
        launcher.assert_called_once()
        for module in modules:
            relative = module.relative_to(self.case.root)
            self.assertIn(
                f"Test module FINISH: {relative}\noutput:{module.name}\nModule time: {relative}: 0.250s\n",
                self.case.output.getvalue(),
            )
            self.assertIn(f"errors:{module.name}\n", self.case.errors.getvalue())
        self.assertIn(
            "Modules: 12; tests run: 12; skipped: 0; failed modules: 0", self.case.output.getvalue()
        )

    def test_interrupt_cancels_queued_modules_in_both_worker_lanes(self):
        modules = [self.case.file(f"PROJECT_TOOLS/tests/test_unit_{number}.py") for number in range(4)]
        modules += [
            self.case.file(str(full.APP / f"tests/test_{number}_docker_e2e.py"))
            for number in range(4)
        ]
        started, watchers = [], []
        lock = threading.Lock()
        ready, release, canceled = threading.Event(), threading.Event(), threading.Event()

        def execute(_root, module, _environment):
            with lock:
                started.append(module)
                if len(started) == 4:
                    ready.set()
            self.assertTrue(release.wait(10))
            return True, 1, 0, "", "", 0.0, None

        def interrupted(pending):
            self.assertTrue(ready.wait(5))
            queued = [future for future in pending if not future.running()]
            self.assertEqual(4, len(queued))

            def release_after_cancellation():
                deadline = time.monotonic() + 3
                while not all(future.cancelled() for future in queued) and time.monotonic() < deadline:
                    time.sleep(0.01)
                if all(future.cancelled() for future in queued):
                    canceled.set()
                release.set()

            watcher = threading.Thread(target=release_after_cancellation)
            watchers.append(watcher)
            watcher.start()
            raise KeyboardInterrupt

        try:
            with (
                patch.object(full, "run_module", side_effect=execute),
                patch.object(full, "as_completed", side_effect=interrupted),
                patch.object(full, "current_code_test_image", return_value=nullcontext({})),
                patch.object(full, "run_launcher") as launcher,
            ):
                with self.assertRaises(KeyboardInterrupt):
                    self.case.run_suite()
            self.assertTrue(canceled.is_set(), "queued work must be canceled before waiting for active modules")
            self.assertEqual(4, len(started), "interruption must not start either lane's queued modules")
            launcher.assert_not_called()
        finally:
            release.set()
            for watcher in watchers:
                watcher.join(timeout=5)
                self.assertFalse(watcher.is_alive())

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
