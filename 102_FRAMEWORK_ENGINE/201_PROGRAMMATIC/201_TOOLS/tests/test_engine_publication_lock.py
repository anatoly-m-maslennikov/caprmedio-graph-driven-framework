"""Real process exclusion for the shared, reentrant Engine publication lock."""

from __future__ import annotations

import contextvars
import os
from pathlib import Path
import select
import signal
import subprocess
import sys
import tempfile
import threading
import time
import unittest

TOOLS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOLS))

from engine_publication_lock import EnginePublicationLockError, engine_publication_lock

LOCK_RELATIVE = Path(".caprmedio_runtime/framework/selector-publication.lock")
BUSY = "selector-publication-lock-busy"
UNSAFE = "selector-publication-lock-unsafe"

CONTENDER = r"""
import sys
sys.path.insert(0, sys.argv[1])
from engine_publication_lock import EnginePublicationLockError, engine_publication_lock
print('ready', flush=True)
for command in sys.stdin:
    try:
        with engine_publication_lock(sys.argv[2], timeout_seconds=0):
            print('acquired', flush=True)
    except EnginePublicationLockError as error:
        print(error.code, flush=True)
"""

HOLDER = r"""
import sys
sys.path.insert(0, sys.argv[1])
from engine_publication_lock import engine_publication_lock
with engine_publication_lock(sys.argv[2], timeout_seconds=0):
    print('owned', flush=True)
    sys.stdin.readline()
"""


def start_child(test, program, root, *arguments):
    child = subprocess.Popen(
        [sys.executable, "-B", "-c", program, str(TOOLS), str(root), *map(str, arguments)],
        stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
        env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1"}, bufsize=0,
    )
    test.addCleanup(stop_child, child)
    return child


def stop_child(child):
    if child.poll() is None:
        child.terminate()
    try:
        child.communicate(timeout=5)
    except subprocess.TimeoutExpired:
        child.kill()
        child.communicate(timeout=5)


def read_event(test, child):
    result = bytearray()
    deadline = time.monotonic() + 5
    while not result.endswith(b"\n"):
        remaining = deadline - time.monotonic()
        test.assertGreater(remaining, 0, "Child did not complete its handshake")
        ready, _, _ = select.select([child.stdout], [], [], remaining)
        test.assertTrue(ready, "Child did not complete its handshake")
        chunk = os.read(child.stdout.fileno(), 1)
        test.assertTrue(chunk, "Child exited before its handshake")
        result.extend(chunk)
    return result.decode().rstrip("\n")


def send_command(child):
    child.stdin.write(b"attempt\n")
    child.stdin.flush()


class EnginePublicationLockTests(unittest.TestCase):
    def setUp(self):
        scratch = TOOLS.parents[2] / ".caprmedio_tmp" / "tests"
        scratch.mkdir(parents=True, exist_ok=True)
        self.fixture = tempfile.TemporaryDirectory(prefix="engine-lock-", dir=scratch)
        self.addCleanup(self.fixture.cleanup)
        self.root = Path(self.fixture.name) / "project"
        self.root.mkdir()

    def contender(self, root=None):
        child = start_child(self, CONTENDER, root or self.root)
        self.assertEqual(read_event(self, child), "ready")
        return child

    def attempt(self, child, expected):
        send_command(child)
        self.assertEqual(read_event(self, child), expected)

    def test_process_exclusion_reentrancy_and_body_error_preserve_outer_lock(self):
        with engine_publication_lock(self.root, timeout_seconds=0):
            inode = (self.root / LOCK_RELATIVE).stat().st_ino
            child = self.contender()
            with engine_publication_lock(str(self.root), timeout_seconds=0):
                self.attempt(child, BUSY)
            self.attempt(child, BUSY)
            with self.assertRaisesRegex(ValueError, "body failure"):
                with engine_publication_lock(self.root, timeout_seconds=0):
                    raise ValueError("body failure")
            self.attempt(child, BUSY)
        self.attempt(child, "acquired")
        self.assertEqual((self.root / LOCK_RELATIVE).stat().st_ino, inode)

    def test_roots_are_independent_in_one_thread_and_separate_processes(self):
        other = Path(self.fixture.name) / "other"
        other.mkdir()
        with engine_publication_lock(self.root, timeout_seconds=0):
            with engine_publication_lock(other, timeout_seconds=0):
                pass
            self.attempt(self.contender(other), "acquired")
            self.attempt(self.contender(), BUSY)

    def test_copied_context_in_other_thread_does_not_inherit_reentry(self):
        outcomes = []
        finished = threading.Event()
        def attempt():
            try:
                with engine_publication_lock(self.root, timeout_seconds=0):
                    outcomes.append("acquired")
            except EnginePublicationLockError as error:
                outcomes.append(error.code)
            finally:
                finished.set()
        with engine_publication_lock(self.root, timeout_seconds=0):
            inherited = contextvars.copy_context()
            thread = threading.Thread(target=lambda: inherited.run(attempt), daemon=True)
            thread.start()
            self.assertTrue(finished.wait(5), "Copied-context thread deadlocked")
            thread.join(timeout=5)
            self.assertFalse(thread.is_alive())
            self.assertEqual(outcomes, [BUSY])

    def test_expired_same_thread_context_cannot_bypass_new_process_owner(self):
        with engine_publication_lock(self.root, timeout_seconds=0):
            expired = contextvars.copy_context()
        child = start_child(self, HOLDER, self.root)
        self.assertEqual(read_event(self, child), "owned")
        def attempt():
            with engine_publication_lock(self.root, timeout_seconds=0):
                pass
        with self.assertRaises(EnginePublicationLockError) as busy:
            expired.run(attempt)
        self.assertEqual(busy.exception.code, BUSY)
        self.attempt(self.contender(), BUSY)
        send_command(child)
        child.communicate(timeout=5)
        self.assertEqual(child.returncode, 0)
        expired.run(attempt)

    def test_replaced_carrier_or_framework_cannot_split_cooperating_ownership(self):
        for replace_framework in (False, True):
            with self.subTest(replace_framework=replace_framework):
                with self.assertRaises(EnginePublicationLockError) as changed:
                    with engine_publication_lock(self.root, timeout_seconds=0):
                        child = self.contender()
                        carrier = self.root / LOCK_RELATIVE
                        if replace_framework:
                            carrier.parent.rename(carrier.parent.with_name("framework-held"))
                            carrier.parent.mkdir()
                        else:
                            replacement = carrier.with_name("replacement.lock")
                            replacement.touch()
                            os.replace(replacement, carrier)
                        self.attempt(child, BUSY)
                self.assertEqual(changed.exception.code, UNSAFE)
                self.attempt(child, "acquired")

    def test_changed_project_root_is_not_reported_as_successful_return(self):
        with self.assertRaises(EnginePublicationLockError) as changed:
            with engine_publication_lock(self.root, timeout_seconds=0):
                self.root.rename(self.root.with_name("project-held"))
                self.root.mkdir()
        self.assertEqual(changed.exception.code, UNSAFE)

    @unittest.skipUnless(hasattr(os, "fork"), "Requires an actual fork")
    def test_forked_context_cannot_reenter_or_release_parent_ownership(self):
        read_fd, write_fd = os.pipe()
        self.addCleanup(os.close, read_fd)
        with engine_publication_lock(self.root, timeout_seconds=0):
            child_pid = os.fork()
            if child_pid == 0:
                os.close(read_fd)
                try:
                    with engine_publication_lock(self.root, timeout_seconds=0):
                        outcome = "acquired"
                except EnginePublicationLockError as error:
                    outcome = error.code
                except BaseException as error:
                    outcome = type(error).__name__
                os.write(write_fd, outcome.encode())
                os._exit(0)
            os.close(write_fd)
            ready, _, _ = select.select([read_fd], [], [], 5)
            if not ready:
                os.kill(child_pid, signal.SIGKILL)
            _, status = os.waitpid(child_pid, 0)
            self.assertTrue(ready, "Forked contender did not respond")
            self.assertEqual(status, 0)
            self.assertEqual(os.read(read_fd, 4096).decode(), BUSY)
            self.attempt(self.contender(), BUSY)
        self.attempt(self.contender(), "acquired")

    def test_invalid_nested_timeout_is_not_granted_reentry(self):
        with engine_publication_lock(self.root, timeout_seconds=0):
            for timeout in (True, -1, 31, float("inf"), float("nan")):
                with self.subTest(timeout=timeout), self.assertRaises(EnginePublicationLockError):
                    with engine_publication_lock(self.root, timeout_seconds=timeout):
                        self.fail("Invalid nested timeout acquired ownership")

    def test_symlink_root_and_lock_carrier_are_not_admitted(self):
        alias = Path(self.fixture.name) / "alias"
        alias.symlink_to(self.root, target_is_directory=True)
        with engine_publication_lock(self.root, timeout_seconds=0):
            with self.assertRaises(EnginePublicationLockError):
                with engine_publication_lock(alias, timeout_seconds=0):
                    self.fail("Symlink root acquired ownership")
        carrier = self.root / LOCK_RELATIVE
        carrier.unlink()
        unrelated = Path(self.fixture.name) / "unrelated"
        unrelated.write_bytes(b"exact unrelated bytes")
        carrier.symlink_to(unrelated)
        with self.assertRaises(EnginePublicationLockError):
            with engine_publication_lock(self.root, timeout_seconds=0):
                self.fail("Symlink lock carrier acquired ownership")
        self.assertEqual(unrelated.read_bytes(), b"exact unrelated bytes")


if __name__ == "__main__":
    unittest.main()
