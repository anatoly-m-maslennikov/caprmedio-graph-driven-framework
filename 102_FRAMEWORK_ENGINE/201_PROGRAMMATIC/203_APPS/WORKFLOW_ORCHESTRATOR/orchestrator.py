"""Explicit local worker and short-lived queue client for independent Workflow Runs."""

# implementation of:
# Requirement: CA-R-2117
# Method: CA-M-431, CA-M-405

import argparse
import fcntl
import json
import os
from pathlib import Path
import subprocess
import sys
from typing import Annotated, Any

from pydantic import Field, TypeAdapter
from contracts import Enqueue, EnqueueSelected, Status, SubmitResult
from backend import enqueue, enqueue_selected, status, worker
from engine import Coordinator
from runtime_config import control_directory, docker_runtime

Request = Annotated[
    Enqueue | EnqueueSelected | Status | SubmitResult, Field(discriminator="operation")
]
ADAPTER: TypeAdapter[Request] = TypeAdapter(Request)


def _run_native(root: Path, request: Request) -> tuple[bool, Any | None]:
    from selected_integrated_entry import run as run_integrated

    return run_integrated(root, request)


def run(root, request):
    request = ADAPTER.validate_python(request)
    handled, result = _run_native(root, request)
    if handled:
        return result
    if not docker_runtime():
        from docker_bridge import MARKER, invoke

        if Coordinator(root, None).store.path(MARKER).exists():
            return invoke(root, request.model_dump())
    if isinstance(request, Enqueue):
        return enqueue(root, request)
    if isinstance(request, EnqueueSelected):
        return enqueue_selected(root, request)
    return status(root, request)


def _worker_paths(root):
    engine = Coordinator(root, None)
    directory = engine.store.path(control_directory())
    directory.mkdir(parents=True, exist_ok=True)
    return (
        engine,
        directory,
        engine.store.path(".caprmedio_install/workflow_orchestrator/worker.log"),
    )


def _start_worker(root):
    engine, _, log_path = _worker_paths(root)
    command = [
        sys.executable,
        str(Path(__file__).resolve()),
        "--project-root",
        str(engine.root),
        "worker",
    ]
    with log_path.open("ab") as log:
        child = subprocess.Popen(
            command, stdin=subprocess.DEVNULL, stdout=log, stderr=log, start_new_session=True
        )
    return {
        "worker_pid": child.pid,
        "outcome": "starting",
        "log_path": str(log_path.relative_to(engine.root)),
    }


def _foreground_worker(root):
    engine, directory, _ = _worker_paths(root)
    lock = directory / "worker.lock"
    with lock.open("a") as handle:
        fcntl.flock(handle, fcntl.LOCK_EX | fcntl.LOCK_NB)
        (directory / "worker.ready").unlink(missing_ok=True)
        identity = {"pid": os.getpid(), "state": "starting"}
        engine.save(directory / "worker.json", identity)
        completed = False
        try:
            result = worker(
                engine.root,
                ready_file=directory / "worker.ready",
                _process_boundary=True,
            )
            completed = True
            return result
        finally:
            if completed:
                (directory / "worker.ready").unlink(missing_ok=True)
                engine.save(directory / "worker.json", {**identity, "state": "stopped"})


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project-root", required=True, type=Path)
    parser.add_argument("--input", default="-")
    parser.add_argument(
        "operation",
        choices=[
            "worker",
            "start-worker",
            "enqueue",
            "enqueue_selected",
            "submit_result",
            "status",
        ],
    )
    args = parser.parse_args()
    if args.operation == "start-worker":
        print(json.dumps(_start_worker(args.project_root)))
    elif args.operation == "worker":
        return _foreground_worker(args.project_root) or 0
    else:
        raw = sys.stdin.read() if args.input == "-" else Path(args.input).read_text()
        request = json.loads(raw)
        if "operation" in request and request["operation"] != args.operation:
            parser.error("Operation conflicts with request")
        request["operation"] = args.operation
        print(json.dumps(run(args.project_root, request), default=str))
    return 0


def _main_process():
    """Keep CLI failures out of protocol stdout and report them once."""
    from runtime_process_boundary import run_process

    return run_process(main, operation="WORKFLOW_ORCHESTRATOR/orchestrator")


if __name__ == "__main__":
    raise SystemExit(_main_process())
