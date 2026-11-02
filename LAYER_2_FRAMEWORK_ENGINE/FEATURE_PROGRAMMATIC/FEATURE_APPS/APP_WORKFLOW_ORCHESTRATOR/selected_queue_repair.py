"""Run one untouched selected Workflow from a private, bounded DBOS queue."""

from __future__ import annotations

import argparse
from contextlib import contextmanager
import fcntl
import hashlib
import json
from pathlib import Path
import re
import sqlite3
import time
from typing import Any, Iterator

import backend
from contracts import Status
from engine import Coordinator
from runtime_config import control_directory
from selected_execution import RUN_ID, SelectedExecution, SelectedExecutionError
from selected_native_providers import SelectedNativeProviders


_SHA256 = re.compile(r"^[0-9a-f]{64}$")
_RUN_RECORD_TABLES = (
    ("operation_outputs", "workflow_uuid"),
    ("workflow_events", "workflow_uuid"),
    ("workflow_events_history", "workflow_uuid"),
    ("streams", "workflow_uuid"),
    ("notifications", "destination_uuid"),
)


class SelectedQueueRepairError(RuntimeError):
    """The selected Workflow cannot safely enter the repair worker."""


def _canonical_digest(value: object) -> str:
    payload = json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(payload).hexdigest()


def _validate_arguments(run_id: object, request_sha256: object, timeout_seconds: object) -> None:
    if not isinstance(run_id, str) or RUN_ID.fullmatch(run_id) is None:
        raise SelectedQueueRepairError("invalid selected Run ID")
    if not isinstance(request_sha256, str) or _SHA256.fullmatch(request_sha256) is None:
        raise SelectedQueueRepairError("expected request SHA-256 is invalid")
    if isinstance(timeout_seconds, bool) or not isinstance(timeout_seconds, int) or not 1 <= timeout_seconds <= 3600:
        raise SelectedQueueRepairError("timeout_seconds must be an integer from 1 through 3600")


def _load_frozen_request(root: Path, run_id: str, expected_sha256: str) -> None:
    selected = SelectedExecution(root)
    directory = selected.run_directory(run_id)
    request = directory / "selected_request.json"
    if not directory.is_dir() or request.is_symlink() or not request.is_file():
        raise SelectedQueueRepairError("selected request carrier is unavailable")
    if {path.name for path in directory.iterdir()} != {request.name}:
        raise SelectedQueueRepairError("selected Run already has execution evidence")
    if hashlib.sha256(request.read_bytes()).hexdigest() != expected_sha256:
        raise SelectedQueueRepairError("selected request SHA-256 differs from the admitted request")
    try:
        frozen = selected.load(run_id)
        frozen_request = frozen.get("request")
        if not isinstance(frozen_request, dict) or frozen_request.get("operation") != "enqueue_selected":
            raise SelectedQueueRepairError("frozen selected request is not an enqueue_selected request")
        if frozen_request.get("run_id") != run_id:
            raise SelectedQueueRepairError("frozen selected request has a different Run ID")
        selected._revalidate(frozen)
    except (FileNotFoundError, OSError, SelectedExecutionError) as error:
        raise SelectedQueueRepairError("selected Workflow graph is no longer current") from error


@contextmanager
def _worker_lock(root: Path) -> Iterator[None]:
    directory = Coordinator(root, None).store.path(control_directory())
    directory.mkdir(parents=True, exist_ok=True)
    with (directory / "worker.lock").open("a") as handle:
        try:
            fcntl.flock(handle, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except OSError as error:
            raise SelectedQueueRepairError("workflow worker lock is already held") from error
        try:
            yield
        finally:
            fcntl.flock(handle, fcntl.LOCK_UN)


def _read_scheduler(path: Path, run_id: str) -> dict[str, Any]:
    if not path.is_file():
        raise SelectedQueueRepairError("DBOS scheduler database is unavailable")
    with sqlite3.connect(path.resolve().as_uri() + "?mode=ro", uri=True) as connection:
        connection.row_factory = sqlite3.Row
        connection.execute("PRAGMA query_only = ON")
        tables = {row[0] for row in connection.execute("SELECT name FROM sqlite_master WHERE type='table'")}
        required = {"workflow_status", *[name for name, _ in _RUN_RECORD_TABLES]}
        if not required.issubset(tables):
            raise SelectedQueueRepairError("DBOS scheduler schema is incomplete")
        rows = [dict(row) for row in connection.execute(
            "SELECT * FROM workflow_status ORDER BY workflow_uuid"
        )]
        target = [row for row in rows if row["workflow_uuid"] == run_id]
        records = {
            table: connection.execute(f"SELECT COUNT(*) FROM {table} WHERE {column} = ?", (run_id,)).fetchone()[0]
            for table, column in _RUN_RECORD_TABLES
        }
    if len(target) != 1:
        raise SelectedQueueRepairError("selected scheduler row is missing or ambiguous")
    return {"target": target[0], "records": records, "other_rows": [row for row in rows if row["workflow_uuid"] != run_id]}


def _assert_scheduler_is_safe(state: dict[str, Any], run_id: str) -> None:
    from dbos._queue import INTERNAL_QUEUE_NAME

    target = state["target"]
    expected = {
        "status": "ENQUEUED",
        "name": backend.SELECTED_WORKFLOW,
        "application_version": backend.APP_VERSION,
        "application_name": backend.APPLICATION,
        "queue_name": backend.QUEUE,
        "executor_id": None,
        "started_at_epoch_ms": None,
        "completed_at": None,
        "output": None,
        "error": None,
        "recovery_attempts": 0,
        "parent_workflow_id": None,
    }
    if any(target.get(key) != value for key, value in expected.items()):
        raise SelectedQueueRepairError("selected scheduler row is not an untouched admitted queue entry")
    if any(state["records"].values()):
        raise SelectedQueueRepairError("selected scheduler row already has execution records")
    rows = [target, *state["other_rows"]]
    if any(row.get("status") == "PENDING" or row.get("queue_name") == INTERNAL_QUEUE_NAME for row in rows):
        raise SelectedQueueRepairError("scheduler has pending or internal work")
    if any(row.get("parent_workflow_id") == run_id for row in state["other_rows"]):
        raise SelectedQueueRepairError("selected scheduler row already has child workflow records")


def _private_queue(run_id: str, request_sha256: str) -> str:
    return "repair-" + hashlib.sha256(f"{run_id}\0{request_sha256}".encode()).hexdigest()[:32]


def _assert_workflow_input(handle: object, run_id: str) -> None:
    status = handle.get_status()
    try:
        matches = _canonical_digest(status.input) == _canonical_digest({"args": [run_id], "kwargs": {}})
    except (TypeError, ValueError):
        matches = False
    if status.workflow_id != run_id or not matches:
        raise SelectedQueueRepairError("scheduler input does not bind the selected Run ID")


def _start_private_worker(root: Path, queue_name: str):
    from dbos import DBOS

    _, url = backend.database(root)
    scheduler = backend._scheduler_identity()
    DBOS(config={"name": scheduler["application"], "system_database_url": url,
                 "run_admin_server": False, "enable_otlp": False,
                 "application_version": scheduler["app_version"],
                 "executor_id": "repair-" + queue_name.removeprefix("repair-"),
                 "max_executor_threads": 1})
    try:
        engine = Coordinator(root, None)
        backend.register_execution(DBOS, engine, selected_providers=SelectedNativeProviders(root))
        DBOS.listen_queues([queue_name])
        DBOS.launch()
    except Exception:
        DBOS.destroy(destroy_registry=True)
        raise
    return DBOS


def _terminal_status(handle: object, timeout_seconds: int) -> tuple[str, bool]:
    deadline = time.monotonic() + timeout_seconds
    last = "ENQUEUED"
    while time.monotonic() < deadline:
        current = handle.get_status().status
        last = str(current)
        if last in {"SUCCESS", "ERROR", "CANCELLED"}:
            return last, True
        time.sleep(0.1)
    return last, False


def repair_selected_queue(
    root: str | Path,
    run_id: str,
    expected_request_sha256: str,
    *,
    timeout_seconds: int = 60,
) -> dict[str, Any]:
    """Resume one untouched selected Run through one private DBOS queue."""
    _validate_arguments(run_id, expected_request_sha256, timeout_seconds)
    root_path = Path(root).resolve(strict=True)
    queue_name = _private_queue(run_id, expected_request_sha256)
    with _worker_lock(root_path):
        _load_frozen_request(root_path, run_id, expected_request_sha256)
        database_path, _ = backend.database(root_path)
        before = _read_scheduler(database_path, run_id)
        _assert_scheduler_is_safe(before, run_id)
        before_digest = _canonical_digest(before["other_rows"])
        if any(row.get("queue_name") == queue_name for row in before["other_rows"]):
            raise SelectedQueueRepairError("selected private queue already has a workflow row")
        transport = backend.client(root_path)
        try:
            _assert_workflow_input(transport.retrieve_workflow(run_id), run_id)
            transport.register_queue(queue_name, global_concurrency=1, worker_concurrency=1,
                                     polling_interval_sec=0.2, on_conflict="never_update")
            transport.resume_workflow(run_id, queue_name=queue_name)
        finally:
            transport.destroy()
        moved = _read_scheduler(database_path, run_id)
        if moved["target"].get("queue_name") != queue_name or moved["target"].get("status") != "ENQUEUED":
            raise SelectedQueueRepairError("DBOS did not move only the selected Run to the private queue")
        dbos = _start_private_worker(root_path, queue_name)
        observer = backend.client(root_path)
        try:
            scheduler_status, terminal = _terminal_status(
                observer.retrieve_workflow(run_id), timeout_seconds
            )
        finally:
            observer.destroy()
            dbos.destroy(destroy_registry=True)
        after = _read_scheduler(database_path, run_id)
        after_digest = _canonical_digest(after["other_rows"])
        if after_digest != before_digest:
            raise SelectedQueueRepairError("non-target scheduler rows changed during selected repair")
    result = {"run_id": run_id, "request_sha256": expected_request_sha256,
              "private_queue": queue_name, "scheduler_status": scheduler_status,
              "non_target_workflow_status_sha256": after_digest}
    if not terminal:
        return {**result, "outcome": "interrupted_pending", "disposition": "uncertain",
                "reason": "private repair worker timeout; shutdown was requested", "shutdown_requested": True}
    observed = backend.status(root_path, Status(run_id=run_id))
    return {**result, "status": observed, "outcome": observed.get("outcome"),
            "disposition": observed.get("disposition")}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project-root", required=True, type=Path, dest="root")
    parser.add_argument("--run-id", required=True)
    parser.add_argument("--expected-request-sha256", required=True)
    parser.add_argument("--timeout-seconds", type=int, default=60)
    print(json.dumps(repair_selected_queue(**vars(parser.parse_args())), default=str))


if __name__ == "__main__":
    main()
