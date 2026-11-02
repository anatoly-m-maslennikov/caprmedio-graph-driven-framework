"""Real native identity publication across threads and Project processes."""
from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor
import errno
import fcntl
import json
import os
from pathlib import Path
import signal
import stat
import subprocess
import sys
import threading
import time
import unittest
from unittest.mock import patch

TOOLS = Path(__file__).resolve().parents[1]
sys.path[:0] = [str(TOOLS), str(TOOLS / "tests")]

from atom_operations import ToolError, atom_from_path, atom_identity_lock, create_atom_revision, scan_atoms
import lifecycle_intents
import test_model_driven_status_lifecycle as fixture_module


class AtomIdentityConcurrencyTest(unittest.TestCase):
    def setUp(self) -> None:
        fixture_module.ModelDrivenStatusLifecycleTest.setUpClass()
        self.fixture = fixture_module.ModelDrivenStatusLifecycleTest("run")
        self.fixture.setUp()

    def tearDown(self) -> None:
        self.fixture.tearDown()

    def test_concurrent_lock_admission_serializes_secure_creation(self) -> None:
        together = threading.Barrier(2)
        opening = threading.Lock()
        overlap = threading.Event()
        contender_ready = threading.Event()
        parent_gates_ready = threading.Barrier(2, action=contender_ready.set)
        original_open = os.open
        original_flock = fcntl.flock

        def synchronized_directory_gate(descriptor, operation):
            if operation == fcntl.LOCK_EX and stat.S_ISDIR(os.fstat(descriptor).st_mode):
                parent_gates_ready.wait(timeout=5)
            return original_flock(descriptor, operation)

        def refuse_overlapping_open(path, *args, **kwargs):
            if path != "identity.lock":
                return original_open(path, *args, **kwargs)
            if not opening.acquire(blocking=False):
                overlap.set()
                contender_ready.set()
                raise FileNotFoundError(errno.ENOENT, "concurrent secure lock creation", path)
            try:
                # Reproduce the host's overlapping-open failure on every platform.
                self.assertTrue(contender_ready.wait(timeout=5), "second lock admission did not arrive")
                return original_open(path, *args, **kwargs)
            finally:
                opening.release()

        def acquire(_):
            together.wait(timeout=5)
            try:
                with atom_identity_lock(self.fixture.root):
                    return "acquired"
            except ToolError as error:
                return error.code

        with (
            patch("atom_operations.os.open", refuse_overlapping_open),
            patch("atom_operations.fcntl.flock", synchronized_directory_gate),
            ThreadPoolExecutor(max_workers=2) as pool,
        ):
            results = list(pool.map(acquire, range(2)))
        self.assertEqual(["acquired", "acquired"], results)
        self.assertFalse(overlap.is_set(), "secure lock opens overlapped before file locking")

    def test_concurrent_drafts_get_distinct_fresh_identities(self) -> None:
        drafts = [self.fixture.atom("Requirement", "Draft", draft=True, container=name)
                  for name in ("first", "second")]
        requests = [self.fixture.request(path, "Active") for path in drafts]
        together = threading.Barrier(2)
        allocator = lifecycle_intents._draft_promotion_identity

        def competing_allocation(root, target):
            identity = allocator(root, target)
            # Force the old unguarded allocation window to overlap. With the
            # lock the first writer waits briefly, then the second observes it.
            try:
                together.wait(timeout=0.2)
            except threading.BrokenBarrierError:
                pass
            return identity

        with patch.object(lifecycle_intents, "_draft_promotion_identity", competing_allocation):
            with ThreadPoolExecutor(max_workers=2) as pool:
                results = list(pool.map(self.fixture.execute, requests))
        identities = [result["observed"]["atom_id"] for result in results]
        self.assertEqual(["applied", "applied"], [result["outcome"] for result in results])
        self.assertEqual(2, len(set(identities)))
        self.assertTrue(all(not path.exists() for path in drafts))
        for identity in identities:
            self.assertEqual(1, sum(atom.atom_id == identity for atom in scan_atoms(self.fixture.root)))

    def test_concurrent_explicit_creates_cannot_publish_one_identity_twice(self) -> None:
        carriers = [self.fixture.create_carrier("Requirement", "Active", number=9000) for _ in range(2)]
        carriers[1]["path"] = carriers[1]["path"].replace("created-9000", "different-name")
        together = threading.Barrier(2)

        def create(carrier):
            together.wait(timeout=5)
            try:
                return create_atom_revision(self.fixture.root, carrier["path"], carrier["frontmatter"], carrier["content"]).atom_id
            except ToolError as error:
                return error.code

        with ThreadPoolExecutor(max_workers=2) as pool:
            results = list(pool.map(create, carriers))
        self.assertCountEqual(["CA-R-9000", "atom-id-collision"], results)
        self.assertEqual(1, sum(atom.atom_id == "CA-R-9000" for atom in scan_atoms(self.fixture.root)))

    def test_process_create_waits_for_same_project_identity_lock(self) -> None:
        carrier = self.fixture.create_carrier("Requirement", "Active", number=9000)
        ready = self.fixture.root / "child-ready"
        script = (
            "import json,sys; from pathlib import Path; sys.path.insert(0,sys.argv[1]); "
            "from atom_operations import create_atom_revision; "
            "root=Path(sys.argv[2]); carrier=json.loads(sys.argv[3]); "
            "Path(sys.argv[4]).write_text('ready'); "
            "create_atom_revision(root,carrier['path'],carrier['frontmatter'],carrier['content'])"
        )
        with atom_identity_lock(self.fixture.root):
            process = subprocess.Popen([sys.executable, "-c", script, str(TOOLS), str(self.fixture.root),
                                        json.dumps(carrier), str(ready)], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            try:
                deadline = time.monotonic() + 10
                while not ready.exists() and process.poll() is None and time.monotonic() < deadline:
                    time.sleep(0.01)
                self.assertTrue(ready.exists(), "child did not reach the native Create boundary")
                self.assertIsNone(process.poll())
                self.assertFalse((self.fixture.root / carrier["path"]).exists())
            except BaseException:
                process.kill()
                process.communicate()
                raise
        try:
            _stdout, stderr = process.communicate(timeout=20)
        except subprocess.TimeoutExpired:
            process.kill()
            process.communicate()
            raise
        self.assertEqual(0, process.returncode, stderr.decode())
        self.assertEqual("CA-R-9000", atom_from_path(self.fixture.root, self.fixture.root / carrier["path"]).atom_id)

    def test_interrupted_process_lock_wait_closes_its_descriptor(self) -> None:
        ready = self.fixture.root / "lock-holder-ready"
        script = (
            "import sys; from pathlib import Path; sys.path.insert(0,sys.argv[1]); "
            "from atom_operations import atom_identity_lock; "
            "root=Path(sys.argv[2]); lock=atom_identity_lock(root); lock.__enter__(); "
            "Path(sys.argv[3]).write_text('ready'); sys.stdin.buffer.read(1); lock.__exit__(None,None,None)"
        )
        process = subprocess.Popen([sys.executable, "-c", script, str(TOOLS), str(self.fixture.root), str(ready)],
                                   stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        opened = []
        original_open = os.open

        def track_open(path, *args, **kwargs):
            descriptor = original_open(path, *args, **kwargs)
            if path == "identity.lock":
                opened.append(descriptor)
            return descriptor

        def interrupt(_signum, _frame):
            raise RuntimeError("interrupted native identity lock wait")

        previous_handler = signal.getsignal(signal.SIGALRM)
        try:
            deadline = time.monotonic() + 10
            while not ready.exists() and process.poll() is None and time.monotonic() < deadline:
                time.sleep(0.01)
            self.assertTrue(ready.exists(), "child did not acquire the Project identity lock")
            signal.signal(signal.SIGALRM, interrupt)
            with patch("atom_operations.os.open", track_open):
                signal.setitimer(signal.ITIMER_REAL, 0.5)
                try:
                    with self.assertRaisesRegex(RuntimeError, "interrupted native identity lock wait"):
                        with atom_identity_lock(self.fixture.root):
                            self.fail("contending process lock unexpectedly entered")
                finally:
                    signal.setitimer(signal.ITIMER_REAL, 0)
            self.assertEqual(1, len(opened))
            with self.assertRaises(OSError):
                os.fstat(opened[0])
        finally:
            signal.setitimer(signal.ITIMER_REAL, 0)
            signal.signal(signal.SIGALRM, previous_handler)
            try:
                _stdout, stderr = process.communicate(input=b"release", timeout=10)
            except subprocess.TimeoutExpired:
                process.kill()
                process.communicate()
                raise
        self.assertEqual(0, process.returncode, stderr.decode())


if __name__ == "__main__":
    unittest.main()
