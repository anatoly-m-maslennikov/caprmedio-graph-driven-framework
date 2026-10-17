"""Isolated functional evidence for one selected queued-run repair."""
from __future__ import annotations

import json
from pathlib import Path
import subprocess
import sys
import textwrap
import unittest


APP = Path(__file__).resolve().parents[1]
TESTS = APP / "tests"
MCP = APP.parents[1] / "204_MCP"


_DRIVER = r'''
import hashlib
import json
from pathlib import Path
import sqlite3
import sys
import tempfile

app = Path(sys.argv[1])
tests = Path(sys.argv[2])
mcp = Path(sys.argv[3])
mode = sys.argv[4]
for location in (app, tests, mcp):
    sys.path.insert(0, str(location))

from dbos import DBOS
import backend
from backend import APP_VERSION, APPLICATION, database, enqueue_selected, status
from contracts import Status
from selected_execution import SelectedExecution
from selected_routes import SelectedRouteAdapter
from selected_workflows_docker_fixture import GoldenCase, GoldenProject
from selected_queue_repair import SelectedQueueRepairError, repair_selected_queue


def initialize(root):
    _, url = database(root)
    DBOS(config={
        "name": APPLICATION,
        "system_database_url": url,
        "run_admin_server": False,
        "enable_otlp": False,
        "application_version": APP_VERSION,
        "max_executor_threads": 2,
    })
    DBOS.launch()
    DBOS.destroy()


def execution(project, run_id):
    preview = SelectedRouteAdapter(project.root).invoke(
        "create_atom", project.request(request_id=run_id),
    )
    return project.request(
        request_id=run_id,
        mode="execute",
        receipt=preview["proposal_receipt"],
        receipt_digest=preview["proposal_receipt_digest"],
    )


def request(project, run_id):
    execution_request = execution(project, run_id)
    enqueue_selected(project.root, {
        "operation": "enqueue_selected", "run_id": run_id, "execution": execution_request,
    })


def non_target_rows(root, target):
    path, _ = database(root)
    with sqlite3.connect(path) as connection:
        return connection.execute(
            "SELECT * FROM workflow_status WHERE workflow_uuid != ? ORDER BY workflow_uuid", (target,),
        ).fetchall()


def all_rows(root):
    path, _ = database(root)
    with sqlite3.connect(path) as connection:
        return connection.execute("SELECT * FROM workflow_status ORDER BY workflow_uuid").fetchall()


fixture_parent = app.parents[3] / ".caprmedio_tmp" / "tests"
fixture_parent.mkdir(parents=True, exist_ok=True)
with tempfile.TemporaryDirectory(dir=fixture_parent) as temporary:
    root = Path(temporary)
    project = GoldenProject(app.parents[3], root, GoldenCase("W01", "create_atom"))
    project.prepare()
    initialize(root)
    target, sentinel = "repair-target", "repair-sentinel"
    if mode == "mismatched-input":
        target_execution = execution(project, target)
        SelectedExecution(root).freeze({
            "operation": "enqueue_selected", "run_id": target, "execution": target_execution,
        })
        transport = backend.client(root)
        try:
            transport.enqueue({
                "queue_name": backend.QUEUE,
                "workflow_name": backend.SELECTED_WORKFLOW,
                "workflow_id": target,
                "app_version": backend.APP_VERSION,
            }, sentinel)
        finally:
            transport.destroy()
        request(project, sentinel)
    else:
        request(project, target)
        request(project, sentinel)
    request_path = SelectedExecution(root).run_directory(target) / "selected_request.json"
    if mode == "mismatched-frozen-run":
        frozen = json.loads(request_path.read_text(encoding="utf-8"))
        frozen["request"]["run_id"] = sentinel
        request_path.write_text(json.dumps(frozen, sort_keys=True), encoding="utf-8")
    expected = hashlib.sha256(request_path.read_bytes()).hexdigest()
    carrier = project.native_parameters()["carrier"]["path"]
    before_authority = project.snapshot()
    before_sentinel = non_target_rows(root, target)
    before_rows = all_rows(root)

    if mode == "mismatched-frozen-run":
        try:
            repair_selected_queue(root, target, expected, timeout_seconds=10)
        except SelectedQueueRepairError:
            print("RESULT=" + json.dumps({
                "refused": True,
                "authority_unchanged": before_authority == project.snapshot(),
                "all_rows_unchanged": before_rows == all_rows(root),
                "target_status": status(root, Status(run_id=target))["scheduler_status"],
            }))
        else:
            raise AssertionError("mismatched frozen request Run identity was accepted")
    elif mode == "mismatched-input":
        try:
            repair_selected_queue(root, target, expected, timeout_seconds=10)
        except SelectedQueueRepairError:
            print("RESULT=" + json.dumps({
                "refused": True,
                "authority_unchanged": before_authority == project.snapshot(),
                "sentinel_unchanged": before_sentinel == non_target_rows(root, target),
                "target_status": status(root, Status(run_id=target))["scheduler_status"],
            }))
        else:
            raise AssertionError("mismatched persisted scheduler input was accepted")
    elif mode == "internal-queue":
        from dbos._queue import INTERNAL_QUEUE_NAME
        transport = __import__("backend").client(root)
        try:
            transport.register_queue(
                INTERNAL_QUEUE_NAME, global_concurrency=1, worker_concurrency=1,
                polling_interval_sec=0.2, on_conflict="never_update",
            )
            transport.resume_workflow(sentinel, queue_name=INTERNAL_QUEUE_NAME)
        finally:
            transport.destroy()
        before_refusal = non_target_rows(root, target)
        try:
            repair_selected_queue(root, target, expected, timeout_seconds=10)
        except SelectedQueueRepairError:
            print("RESULT=" + json.dumps({
                "refused": True,
                "authority_unchanged": before_authority == project.snapshot(),
                "sentinel_unchanged": before_refusal == non_target_rows(root, target),
                "target_status": status(root, Status(run_id=target))["scheduler_status"],
            }))
        else:
            raise AssertionError("internal queue work was accepted")
    elif mode == "dispatch-evidence":
        (SelectedExecution(root).run_directory(target) / "dispatch-intent.json").write_text(
            json.dumps({"run_id": target, "state": "dispatching"}), encoding="utf-8",
        )
        try:
            repair_selected_queue(root, target, expected, timeout_seconds=10)
        except SelectedQueueRepairError:
            print("RESULT=" + json.dumps({
                "refused": True,
                "authority_unchanged": before_authority == project.snapshot(),
                "sentinel_unchanged": before_sentinel == non_target_rows(root, target),
                "target_status": status(root, Status(run_id=target))["scheduler_status"],
            }))
        else:
            raise AssertionError("existing dispatch evidence was accepted")
    else:
        try:
            repair_selected_queue(root, target, "0" * 64, timeout_seconds=10)
        except SelectedQueueRepairError:
            bad_hash_refused = True
        else:
            bad_hash_refused = False
        after_bad_authority = project.snapshot()
        after_bad_sentinel = non_target_rows(root, target)
        repaired = repair_selected_queue(root, target, expected, timeout_seconds=30)
        try:
            repair_selected_queue(root, target, expected, timeout_seconds=10)
        except SelectedQueueRepairError:
            replay_refused = True
        else:
            replay_refused = False
        target_status = status(root, Status(run_id=target))
        print("RESULT=" + json.dumps({
            "bad_hash_refused": bad_hash_refused,
            "bad_hash_authority_unchanged": before_authority == after_bad_authority,
            "bad_hash_sentinel_unchanged": before_sentinel == after_bad_sentinel,
            "repaired": repaired,
            "target_status": target_status,
            "carrier_exists": (root / carrier).is_file(),
            "sentinel_unchanged": before_sentinel == non_target_rows(root, target),
            "replay_refused": replay_refused,
        }))
'''


class SelectedQueueRepairTests(unittest.TestCase):
    """Each scenario has a separate interpreter and disposable DBOS database."""

    def _scenario(self, mode: str) -> dict[str, object]:
        completed = subprocess.run(
            [sys.executable, "-B", "-c", textwrap.dedent(_DRIVER), str(APP), str(TESTS), str(MCP), mode],
            check=False,
            capture_output=True,
            text=True,
            timeout=120,
        )
        self.assertEqual(0, completed.returncode, completed.stderr + completed.stdout)
        records = [line.removeprefix("RESULT=") for line in completed.stdout.splitlines()
                   if line.startswith("RESULT=")]
        self.assertEqual(1, len(records), completed.stdout)
        return json.loads(records[0])

    def test_repairs_only_the_bound_queued_run_once(self) -> None:
        result = self._scenario("repair")

        self.assertTrue(result["bad_hash_refused"])
        self.assertTrue(result["bad_hash_authority_unchanged"])
        self.assertTrue(result["bad_hash_sentinel_unchanged"])
        self.assertTrue(result["carrier_exists"])
        self.assertTrue(result["sentinel_unchanged"])
        self.assertTrue(result["replay_refused"])
        self.assertEqual("SUCCESS", result["target_status"]["scheduler_status"])
        repaired = result["repaired"]
        self.assertEqual("repair-target", repaired["run_id"])
        self.assertEqual("completed", repaired["outcome"])
        self.assertEqual("SUCCESS", repaired["scheduler_status"])

    def test_refuses_existing_dispatch_evidence_without_touching_the_queue(self) -> None:
        result = self._scenario("dispatch-evidence")

        self.assertTrue(result["refused"])
        self.assertTrue(result["authority_unchanged"])
        self.assertTrue(result["sentinel_unchanged"])
        self.assertEqual("ENQUEUED", result["target_status"])

    def test_refuses_when_another_queued_run_is_internal(self) -> None:
        result = self._scenario("internal-queue")

        self.assertTrue(result["refused"])
        self.assertTrue(result["authority_unchanged"])
        self.assertTrue(result["sentinel_unchanged"])
        self.assertEqual("ENQUEUED", result["target_status"])

    def test_refuses_mismatched_persisted_scheduler_input(self) -> None:
        result = self._scenario("mismatched-input")

        self.assertTrue(result["refused"])
        self.assertTrue(result["authority_unchanged"])
        self.assertTrue(result["sentinel_unchanged"])
        self.assertEqual("ENQUEUED", result["target_status"])

    def test_refuses_mismatched_frozen_request_run_identity(self) -> None:
        result = self._scenario("mismatched-frozen-run")

        self.assertTrue(result["refused"])
        self.assertTrue(result["authority_unchanged"])
        self.assertTrue(result["all_rows_unchanged"])
        self.assertEqual("ENQUEUED", result["target_status"])


if __name__ == "__main__":
    unittest.main()
