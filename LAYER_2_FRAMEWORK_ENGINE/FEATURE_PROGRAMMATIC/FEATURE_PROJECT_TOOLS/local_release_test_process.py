"""Stream one release-owned test process into its durable merged output log."""

from __future__ import annotations

import codecs
import os
from pathlib import Path
import signal
import subprocess
import sys
import time
from typing import BinaryIO


_CHUNK_BYTES = 64 * 1024
_TAIL_CHARACTERS = 8000
_CANCELLATION_GRACE_SECONDS = 2.0


def _signal_owned(process: subprocess.Popen[bytes], requested: signal.Signals) -> None:
    try:
        if os.name == "posix":
            os.killpg(process.pid, requested)
        elif requested == signal.SIGINT:
            process.terminate()
        else:
            process.kill()
    except ProcessLookupError:
        pass


def _owned_group_exists(process: subprocess.Popen[bytes]) -> bool:
    process.poll()
    if os.name != "posix":
        return process.returncode is None
    try:
        os.killpg(process.pid, 0)
    except ProcessLookupError:
        return False
    return True


def _stop_owned(process: subprocess.Popen[bytes]) -> None:
    """Reap the leader and stop its group even when the leader exits first."""
    _signal_owned(process, signal.SIGINT)
    deadline = time.monotonic() + _CANCELLATION_GRACE_SECONDS
    try:
        while _owned_group_exists(process) and time.monotonic() < deadline:
            time.sleep(0.05)
    finally:
        if _owned_group_exists(process):
            if os.name == "posix":
                _signal_owned(process, signal.SIGKILL)
            else:
                process.kill()
        process.wait(timeout=_CANCELLATION_GRACE_SECONDS)


def run_logged_test_process(
    argv: tuple[str, ...], cwd: Path, log: BinaryIO,
) -> subprocess.CompletedProcess[str]:
    """Keep complete output on disk, forwarding chunks and retaining only a tail.

    The caller owns the newly created log. Only this whole-suite process starts
    a new session; cancellation never targets the caller's process group.
    """
    tail = ""
    decoder = codecs.getincrementaldecoder("utf-8")(errors="replace")
    process: subprocess.Popen[bytes] | None = None
    log.flush()
    with Path(log.name).open("rb") as reader:
        def forward(*, final: bool = False) -> None:
            nonlocal tail
            while chunk := reader.read(_CHUNK_BYTES):
                text = decoder.decode(chunk)
                tail = (tail + text)[-_TAIL_CHARACTERS:]
                sys.stderr.write(text)
                sys.stderr.flush()
            if final:
                text = decoder.decode(b"", final=True)
                tail = (tail + text)[-_TAIL_CHARACTERS:]
                sys.stderr.write(text)
                sys.stderr.flush()

        try:
            process = subprocess.Popen(
                argv, cwd=cwd, stdout=log, stderr=subprocess.STDOUT,
                start_new_session=os.name == "posix",
            )
            while True:
                forward()
                if process.poll() is not None:
                    break
                time.sleep(0.05)
            forward(final=True)
        except BaseException as error:
            if process is not None:
                try:
                    _stop_owned(process)
                except (OSError, KeyboardInterrupt, subprocess.TimeoutExpired) as cleanup_error:
                    error.add_note(f"Test-process cancellation failed: {cleanup_error!r}")
                try:
                    forward(final=True)
                except (OSError, ValueError) as output_error:
                    error.add_note(f"Final test-output forwarding failed: {output_error!r}")
            raise
    return subprocess.CompletedProcess(argv, process.returncode, tail, "")
