"""Actual SDK confirmation, disconnected enqueue and a fresh real DBOS worker."""

import asyncio
import json
from pathlib import Path
import subprocess
import sys
import time
import unittest

MCP = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(MCP / "tests"))

import test_subject_batch_confirmation as fixtures  # noqa: E402
import subject_batch_confirmation as host  # noqa: E402
from backend import status  # noqa: E402
from contracts import Status  # noqa: E402
from subject_batch_stage import stage_subject_batch  # noqa: E402

APP = MCP.parent / "203_APPS/WORKFLOW_ORCHESTRATOR"


class SubjectBatchQueueTests(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        self.fixture = fixtures.SubjectBatchConfirmationTests("runTest")
        self.fixture.setUp()
        for callback, arguments, keywords in self.fixture._cleanups:
            self.addCleanup(callback, *arguments, **keywords)
        self.fixture._cleanups.clear()
        self.root = self.fixture.project.root
        self.ready = self.root / ".caprmedio_tmp/batch-worker.ready"
        self.log = self.root / ".caprmedio_tmp/batch-worker.log"

    @staticmethod
    def stop_worker(process):
        if process.poll() is None:
            process.terminate()
            process.wait(timeout=15)

    async def start_worker(self):
        self.ready.unlink(missing_ok=True)
        with self.log.open("ab") as log:
            process = subprocess.Popen(
                [
                    sys.executable,
                    str(APP / "tests/mock_worker.py"),
                    str(self.root),
                    str(self.ready),
                ],
                stdout=subprocess.DEVNULL,
                stderr=log,
            )
        self.addCleanup(self.stop_worker, process)
        deadline = time.monotonic() + 25
        while not self.ready.exists() and process.poll() is None and time.monotonic() < deadline:
            await asyncio.sleep(0.1)
        self.assertTrue(self.ready.exists(), self.log.read_text())
        return process

    async def test_confirm_enqueue_disconnect_and_fresh_worker_publish_exact_batch(self):
        fixture, project = self.fixture, self.fixture.project
        archives = project.archives()
        staged = stage_subject_batch(self.root, project.parameters, limit=2)
        project.use_reviewed_packet(staged["reviewed_packet"])
        fixture.runner, fixture.frozen = project.execution("queued-draft-subject-batch")
        initialized = await self.start_worker()
        self.stop_worker(initialized)
        response = await fixture.connected_call(enqueue=host._enqueue)
        self.assertEqual("dispatched", response.structured_content["status"])
        self.assertTrue(fixture.receipt().is_file())
        self.assertEqual(1, len(fixture.forms))
        for path in project.paths:
            self.assertEqual(project.before[path], path.read_bytes())
        started = time.monotonic()
        worker = await self.start_worker()
        deadline = time.monotonic() + 30
        result = {}
        while time.monotonic() < deadline:
            result = status(self.root, Status(run_id="queued-draft-subject-batch"))
            if result.get("scheduler_status") in {"SUCCESS", "ERROR", "CANCELLED"}:
                break
            await asyncio.sleep(0.1)
        self.assertEqual("completed", result.get("outcome"), result)
        self.assertEqual("completed", result["subject_batch"]["state"])
        self.assertEqual(2, result["subject_batch"]["completed"])
        self.assertNotIn("atoms", result["subject_batch"])
        self.assertLess(len(json.dumps(result)), 5000)
        for path, archive in zip(project.paths, archives):
            self.assertNotEqual(project.before[path], path.read_bytes())
            self.assertEqual(project.before[path], archive.read_bytes())
        self.stop_worker(worker)
        print(f"subject_batch_queue: targets=2 execution_seconds={time.monotonic() - started:.3f}")


if __name__ == "__main__":
    unittest.main()
