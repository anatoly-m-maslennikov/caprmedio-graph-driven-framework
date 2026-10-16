"""Real, disposable child-process checks for the Local release log boundary."""

from __future__ import annotations

from contextlib import redirect_stderr
import io
import os
from pathlib import Path
import signal
import subprocess
import sys
import tempfile
import threading
import time
import unittest
from unittest.mock import Mock, patch

if os.name == "posix":
    import fcntl

REPOSITORY = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPOSITORY))
from PROJECT_TOOLS.local_release_test_process import run_logged_test_process  # noqa: E402


def _wait_for(path: Path, *, timeout: float = 10.0) -> None:
    deadline = time.monotonic() + timeout
    while not path.exists():
        if time.monotonic() >= deadline:
            raise AssertionError(f"Child fixture did not create {path.name}")
        time.sleep(0.02)


class LocalReleaseTestProcessTests(unittest.TestCase):
    def setUp(self) -> None:
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name).resolve()

    def test_output_is_logged_and_forwarded_before_child_exit_with_bounded_tail(self) -> None:
        ready = threading.Event()

        class ObservedOutput(io.StringIO):
            def write(self, text):
                result = super().write(text)
                if "early stderr" in self.getvalue():
                    ready.set()
                return result

        child = """
import pathlib, sys, time
gate = pathlib.Path(sys.argv[1])
print('early stdout', flush=True)
print('early stderr', file=sys.stderr, flush=True)
deadline = time.monotonic() + 10
while not gate.exists() and time.monotonic() < deadline:
    time.sleep(.02)
print('x' * 100_000)
print('final evidence')
"""
        results, errors = [], []
        log_path = self.root / "tests.log"
        gate = self.root / "continue"
        output = ObservedOutput()
        with log_path.open("w+b") as log, redirect_stderr(output):
            def run():
                try:
                    results.append(run_logged_test_process(
                        (sys.executable, "-B", "-u", "-c", child, str(gate)), self.root, log,
                    ))
                except BaseException as error:
                    errors.append(error)

            worker = threading.Thread(target=run)
            worker.start()
            try:
                self.assertTrue(ready.wait(5), "Output was not forwarded before the child waited")
                self.assertTrue(worker.is_alive())
                self.assertEqual("early stdout\nearly stderr\n", log_path.read_text())
            finally:
                gate.touch()
                worker.join(10)
        self.assertFalse(worker.is_alive())
        self.assertEqual([], errors)
        self.assertEqual(0, results[0].returncode)
        self.assertLessEqual(len(results[0].stdout), 8000)
        self.assertNotIn("early stdout", results[0].stdout)
        self.assertIn("final evidence", results[0].stdout)
        self.assertGreater(log_path.stat().st_size, 100_000)
        self.assertEqual(log_path.read_text(), output.getvalue())

    @unittest.skipUnless(os.name == "posix", "The owned process-group boundary is POSIX")
    def test_interrupt_stops_descendant_even_after_group_leader_exits(self) -> None:
        descendant = """
import fcntl, pathlib, signal, sys, time
root = pathlib.Path(sys.argv[1])
lock = (root / 'descendant.lock').open('w')
fcntl.flock(lock, fcntl.LOCK_EX)
signal.signal(signal.SIGINT, signal.SIG_IGN)
(root / 'descendant.ready').touch()
time.sleep(60)
"""
        child = """
import fcntl, os, pathlib, signal, subprocess, sys, time
root = pathlib.Path(sys.argv[1])
lock = (root / 'leader.lock').open('w')
fcntl.flock(lock, fcntl.LOCK_EX)
(root / 'leader.pid').write_text(str(os.getpid()))
def stop(*_):
    print('leader interrupted', flush=True)
    raise SystemExit(0)
signal.signal(signal.SIGINT, stop)
subprocess.Popen((sys.executable, '-B', '-u', '-c', sys.argv[2], str(root)))
while not (root / 'descendant.ready').exists():
    time.sleep(.02)
print('sleeping fixture ready', flush=True)
(root / 'leader.ready').touch()
time.sleep(60)
"""
        driver = """
from pathlib import Path
import sys
sys.path.insert(0, sys.argv[1])
from PROJECT_TOOLS.local_release_test_process import run_logged_test_process
root = Path(sys.argv[2])
with (root / 'tests.log').open('w+b') as log:
    try:
        run_logged_test_process((sys.executable, '-B', '-u', '-c', sys.argv[3], str(root), sys.argv[4]), root, log)
    except KeyboardInterrupt:
        print('interrupted')
        raise SystemExit(130)
"""
        process = subprocess.Popen(
            (sys.executable, "-B", "-u", "-c", driver, str(REPOSITORY), str(self.root), child, descendant),
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, start_new_session=True,
        )
        try:
            _wait_for(self.root / "leader.ready")
            _wait_for(self.root / "descendant.ready")
            process.send_signal(signal.SIGINT)
            stdout, stderr = process.communicate(timeout=10)
            self.assertEqual(130, process.returncode, stderr)
            self.assertEqual("interrupted\n", stdout)
            self.assertIn("sleeping fixture ready", stderr)
            self.assertIn("leader interrupted", (self.root / "tests.log").read_text())
            for name in ("leader", "descendant"):
                with (self.root / f"{name}.lock").open() as held:
                    fcntl.flock(held, fcntl.LOCK_EX | fcntl.LOCK_NB)
        finally:
            identity = self.root / "leader.pid"
            if identity.exists():
                try:
                    os.killpg(int(identity.read_text()), signal.SIGKILL)
                except ProcessLookupError:
                    pass
            if process.poll() is None:
                process.kill()
            process.communicate(timeout=5)

    @unittest.skipUnless(os.name == "posix", "The child-liveness fixture uses POSIX file locks")
    def test_forwarding_io_failure_stops_owned_child_and_retains_output(self) -> None:
        class BrokenOutput(io.StringIO):
            def write(self, text):
                if text:
                    raise OSError("fixture output unavailable")
                return 0

        child = """
import fcntl, pathlib, sys, time
root = pathlib.Path(sys.argv[1])
lock = (root / 'child.lock').open('w')
fcntl.flock(lock, fcntl.LOCK_EX)
print('retained evidence', flush=True)
time.sleep(60)
"""
        log_path = self.root / "tests.log"
        with log_path.open("w+b") as log, redirect_stderr(BrokenOutput()):
            with self.assertRaisesRegex(OSError, "fixture output unavailable"):
                run_logged_test_process(
                    (sys.executable, "-B", "-u", "-c", child, str(self.root)), self.root, log,
                )
        self.assertIn("retained evidence", log_path.read_text())
        with (self.root / "child.lock").open() as held:
            fcntl.flock(held, fcntl.LOCK_EX | fcntl.LOCK_NB)

    def test_bounded_reap_timeout_preserves_original_interrupt_and_partial_log(self) -> None:
        process = Mock()
        process.poll.side_effect = KeyboardInterrupt
        process.wait.side_effect = subprocess.TimeoutExpired(("fixture",), 2.0)
        log_path = self.root / "tests.log"
        with log_path.open("w+b") as log:
            log.write(b"partial evidence\n")
            with patch("PROJECT_TOOLS.local_release_test_process.subprocess.Popen", return_value=process), \
                    patch("PROJECT_TOOLS.local_release_test_process._signal_owned"), \
                    patch("PROJECT_TOOLS.local_release_test_process._owned_group_exists", return_value=False), \
                    redirect_stderr(io.StringIO()):
                with self.assertRaises(KeyboardInterrupt) as interrupted:
                    run_logged_test_process(("fixture",), self.root, log)

        process.wait.assert_called_once_with(timeout=2.0)
        self.assertIn("TimeoutExpired", "\n".join(interrupted.exception.__notes__))
        self.assertEqual("partial evidence\n", log_path.read_text())


if __name__ == "__main__":
    unittest.main()
