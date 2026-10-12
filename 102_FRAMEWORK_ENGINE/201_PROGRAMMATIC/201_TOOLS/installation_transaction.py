"""Per-Project publication exclusion and bounded retained-state orchestration.

The transaction is intentionally a library entry point, not an installer hook.
It never discovers or controls real processes: callers must provide immutable
process/release/command evidence and an already-observed shutdown response.
"""
from __future__ import annotations

from contextlib import contextmanager
from datetime import UTC, datetime
import fcntl
import math
import os
from pathlib import Path
import re
import stat
import time
import tomllib
from collections.abc import Iterator, Mapping, Sequence
import uuid

from installation_state import (
    INSTALLATION_ROOT,
    InstallationStateError,
    append_history,
    build_legacy_inventory,
    prove_quiescence,
    stage_legacy_copy,
    switch_runtime_selector,
    verify_staged_copy,
    write_inventory,
    write_quiescence,
    write_transaction_status,
)


SHA256 = re.compile(r"[0-9a-f]{64}\Z")
IDENTIFIER = re.compile(r"[A-Za-z0-9][A-Za-z0-9._:-]{0,127}\Z")
LOCK_NAME = "lock.toml"
TERMINAL_OUTCOMES = frozenset({"completed", "blocked", "partial", "recording-pending"})


class InstallationTransactionError(RuntimeError):
    """A per-Project installation transaction cannot safely continue."""

    def __init__(self, code: str, message: str) -> None:
        self.code = code
        self.message = message
        super().__init__(f"{code}: {message}")


def _quoted(value: str) -> str:
    import json

    return json.dumps(value, ensure_ascii=False)


def _lock_toml(record: Mapping[str, object]) -> str:
    return "\n".join(
        f"{key} = {_quoted(str(record[key]))}" if not isinstance(record[key], int) else f"{key} = {record[key]}"
        for key in (
            "schema_version",
            "target_project_context_sha256",
            "owner_run_id",
            "operation",
            "lock_generation",
            "acquired_at",
            "command_sha256",
            "lease_nonce",
        )
    ) + "\n"


class InstallationPublicationLock:
    """An anchored fcntl lock whose carrier proves one active publication owner.

    Unlike a release selector lock, this is the shared lock for every mutable
    installation surface.  It is created with O_EXCL and removed only by the
    same owner-generation after a terminal transaction result.  A left-behind
    record is deliberately stale/uncertain and cannot be automatically taken.
    """

    def __init__(
        self,
        project_root: Path | str,
        *,
        target_context_sha256: str,
        owner_run_id: str,
        operation: str,
        command_sha256: str,
        timeout_seconds: float = 30,
    ) -> None:
        if not isinstance(target_context_sha256, str) or SHA256.fullmatch(target_context_sha256) is None:
            raise InstallationTransactionError("installation-lock-invalid", "target context must be a SHA-256 digest")
        if not isinstance(command_sha256, str) or SHA256.fullmatch(command_sha256) is None:
            raise InstallationTransactionError("installation-lock-invalid", "command must be a SHA-256 digest")
        if not isinstance(owner_run_id, str) or IDENTIFIER.fullmatch(owner_run_id) is None:
            raise InstallationTransactionError("installation-lock-invalid", "owner run ID is unsafe")
        if not isinstance(operation, str) or IDENTIFIER.fullmatch(operation) is None:
            raise InstallationTransactionError("installation-lock-invalid", "operation is unsafe")
        if (
            isinstance(timeout_seconds, bool)
            or not isinstance(timeout_seconds, (int, float))
            or not math.isfinite(timeout_seconds)
            or not 0 <= timeout_seconds <= 30
        ):
            raise InstallationTransactionError("installation-lock-invalid", "timeout must be within [0, 30]")
        try:
            root = Path(project_root).absolute()
            observed = root.lstat()
        except (TypeError, ValueError, OSError) as error:
            raise InstallationTransactionError("installation-lock-invalid", "Project root is unavailable") from error
        if root.is_symlink() or not stat.S_ISDIR(observed.st_mode):
            raise InstallationTransactionError("installation-lock-unsafe", "Project root must be a real directory")
        self.project_root = root
        self.target_context_sha256 = target_context_sha256
        self.owner_run_id = owner_run_id
        self.operation = operation
        self.command_sha256 = command_sha256
        self.timeout_seconds = float(timeout_seconds)
        self.lock_generation = uuid.uuid4().hex
        self.lease_nonce = uuid.uuid4().hex
        self.acquired_at = datetime.now(UTC).isoformat(timespec="seconds")
        self._record: dict[str, object] = {
            "schema_version": 1,
            "target_project_context_sha256": target_context_sha256,
            "owner_run_id": owner_run_id,
            "operation": operation,
            "lock_generation": self.lock_generation,
            "acquired_at": self.acquired_at,
            "command_sha256": command_sha256,
            "lease_nonce": self.lease_nonce,
        }
        self._project_fd: int | None = None
        self._runtime_fd: int | None = None
        self._installation_fd: int | None = None
        self._lock_fd: int | None = None
        self._locked_fds: list[int] = []
        self._chain: list[tuple[Path, os.stat_result]] = []
        self._active = False
        self._released = False

    @property
    def lock_path(self) -> Path:
        return self.project_root / INSTALLATION_ROOT / LOCK_NAME

    @property
    def active(self) -> bool:
        return self._active and not self._released

    def _open_directory(self, parent_fd: int, name: str, display: Path) -> int:
        try:
            os.mkdir(name, mode=0o700, dir_fd=parent_fd)
        except FileExistsError:
            pass
        flags = os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW | os.O_CLOEXEC
        try:
            descriptor = os.open(name, flags, dir_fd=parent_fd)
        except OSError as error:
            raise InstallationTransactionError("installation-lock-unsafe", f"unsafe lock ancestor: {display}") from error
        observed = os.fstat(descriptor)
        if not stat.S_ISDIR(observed.st_mode):
            os.close(descriptor)
            raise InstallationTransactionError("installation-lock-unsafe", f"lock ancestor is not a directory: {display}")
        self._chain.append((display, observed))
        return descriptor

    def _recheck_chain(self) -> None:
        if self._installation_fd is None or self._lock_fd is None:
            raise InstallationTransactionError("installation-lock-unavailable", "lock is not open")
        for path, expected in self._chain:
            try:
                current = path.lstat()
            except OSError as error:
                raise InstallationTransactionError("installation-lock-unsafe", "lock ancestor disappeared") from error
            if path.is_symlink() or not stat.S_ISDIR(current.st_mode) or (current.st_dev, current.st_ino) != (
                expected.st_dev,
                expected.st_ino,
            ):
                raise InstallationTransactionError("installation-lock-unsafe", "lock ancestor changed")
        try:
            current = os.stat(LOCK_NAME, dir_fd=self._installation_fd, follow_symlinks=False)
        except OSError as error:
            raise InstallationTransactionError("installation-lock-unsafe", "lock carrier disappeared") from error
        opened = os.fstat(self._lock_fd)
        if not stat.S_ISREG(current.st_mode) or current.st_nlink != 1 or (current.st_dev, current.st_ino) != (
            opened.st_dev,
            opened.st_ino,
        ):
            raise InstallationTransactionError("installation-lock-unsafe", "lock carrier changed")

    @staticmethod
    def _flock(descriptor: int, deadline: float) -> None:
        while True:
            try:
                fcntl.flock(descriptor, fcntl.LOCK_EX | fcntl.LOCK_NB)
                return
            except BlockingIOError as error:
                if time.monotonic() >= deadline:
                    raise InstallationTransactionError(
                        "installation-lock-busy", "installation publication is exclusively owned for this Project"
                    ) from error
                time.sleep(min(0.05, max(0, deadline - time.monotonic())))

    def _write_record(self) -> None:
        if self._lock_fd is None:
            raise InstallationTransactionError("installation-lock-unavailable", "lock carrier is not open")
        encoded = _lock_toml(self._record).encode("utf-8")
        os.lseek(self._lock_fd, 0, os.SEEK_SET)
        os.ftruncate(self._lock_fd, 0)
        os.write(self._lock_fd, encoded)
        os.fsync(self._lock_fd)

    def _read_record(self) -> dict[str, object]:
        if self._lock_fd is None:
            raise InstallationTransactionError("installation-lock-unavailable", "lock carrier is not open")
        os.lseek(self._lock_fd, 0, os.SEEK_SET)
        raw = os.read(self._lock_fd, 65536)
        try:
            document = tomllib.loads(raw.decode("utf-8"))
        except (UnicodeDecodeError, tomllib.TOMLDecodeError) as error:
            raise InstallationTransactionError("installation-lock-unsafe", "lock carrier is not valid TOML") from error
        if not isinstance(document, dict):
            raise InstallationTransactionError("installation-lock-unsafe", "lock carrier is not a table")
        return document

    def acquire(self) -> "InstallationPublicationLock":
        if self._active or self._released:
            raise InstallationTransactionError("installation-lock-state", "lock instance cannot be acquired twice")
        descriptors: list[int] = []
        try:
            flags = os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW | os.O_CLOEXEC
            project_fd = os.open(self.project_root, flags)
            self._project_fd = project_fd
            descriptors.append(project_fd)
            self._chain.append((self.project_root, os.fstat(project_fd)))
            runtime_fd = self._open_directory(project_fd, INSTALLATION_ROOT.parts[0], self.project_root / INSTALLATION_ROOT.parts[0])
            self._runtime_fd = runtime_fd
            descriptors.append(runtime_fd)
            installation_fd = self._open_directory(runtime_fd, INSTALLATION_ROOT.parts[1], self.project_root / INSTALLATION_ROOT)
            self._installation_fd = installation_fd
            descriptors.append(installation_fd)
            deadline = time.monotonic() + self.timeout_seconds
            for descriptor in (project_fd, installation_fd):
                self._flock(descriptor, deadline)
                self._locked_fds.append(descriptor)
            try:
                lock_fd = os.open(
                    LOCK_NAME,
                    os.O_RDWR | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW | os.O_CLOEXEC,
                    0o600,
                    dir_fd=installation_fd,
                )
            except FileExistsError as error:
                raise InstallationTransactionError(
                    "installation-lock-stale", "a prior lock record requires explicit inspection/recovery"
                ) from error
            self._lock_fd = lock_fd
            descriptors.append(lock_fd)
            opened = os.fstat(lock_fd)
            if not stat.S_ISREG(opened.st_mode) or opened.st_nlink != 1:
                raise InstallationTransactionError("installation-lock-unsafe", "lock carrier must be an unaliased regular file")
            self._flock(lock_fd, deadline)
            self._locked_fds.append(lock_fd)
            self._recheck_chain()
            self._write_record()
            self._recheck_chain()
            self._active = True
            return self
        except BaseException:
            self._close(unlink=False)
            raise

    def revalidate(self) -> None:
        if not self.active:
            raise InstallationTransactionError("installation-lock-state", "lock is not active")
        self._recheck_chain()
        if self._read_record() != self._record:
            raise InstallationTransactionError("installation-lock-ownership", "lock record no longer names this owner generation")

    def _close(self, *, unlink: bool) -> None:
        if unlink and self._installation_fd is not None:
            try:
                os.unlink(LOCK_NAME, dir_fd=self._installation_fd)
                os.fsync(self._installation_fd)
            except FileNotFoundError:
                pass
        for descriptor in reversed(self._locked_fds):
            try:
                fcntl.flock(descriptor, fcntl.LOCK_UN)
            except OSError:
                pass
        self._locked_fds.clear()
        for descriptor in (self._lock_fd, self._installation_fd, self._runtime_fd, self._project_fd):
            if descriptor is not None:
                try:
                    os.close(descriptor)
                except OSError:
                    pass
        self._lock_fd = None
        self._installation_fd = None
        self._runtime_fd = None
        self._project_fd = None
        self._active = False

    def release(self, terminal_outcome: str) -> None:
        if terminal_outcome not in TERMINAL_OUTCOMES:
            raise InstallationTransactionError("installation-lock-terminal-invalid", "lock release needs a terminal outcome")
        self.revalidate()
        self._close(unlink=True)
        self._released = True

    def close_uncertain(self) -> None:
        """Release fcntl ownership but retain the record for explicit recovery."""

        self._close(unlink=False)


@contextmanager
def installation_publication_lock(
    project_root: Path | str,
    *,
    target_context_sha256: str,
    owner_run_id: str,
    operation: str,
    command_sha256: str,
    timeout_seconds: float = 30,
) -> Iterator[InstallationPublicationLock]:
    """Acquire the single hardened lock for mutable installation publication."""

    lock = InstallationPublicationLock(
        project_root,
        target_context_sha256=target_context_sha256,
        owner_run_id=owner_run_id,
        operation=operation,
        command_sha256=command_sha256,
        timeout_seconds=timeout_seconds,
    ).acquire()
    try:
        yield lock
    finally:
        if lock.active:
            lock.close_uncertain()


def _terminal(
    root: Path,
    inventory: Mapping[str, object],
    lock: InstallationPublicationLock,
    *,
    phase: str,
    status: str,
    selector_changed: bool,
) -> dict[str, object]:
    write_transaction_status(root, inventory, phase=phase, status=status, lock=lock)
    append_history(root, inventory, phase=phase, status=status, selector_changed=selector_changed, lock=lock)
    lock.release(status)
    return {
        "migration_id": inventory["migration_id"],
        "inventory_sha256": inventory["inventory_sha256"],
        "phase": phase,
        "status": status,
        "selector_changed": selector_changed,
        "selected": selector_changed,
    }


def run_retained_legacy_migration(
    project_root: Path | str,
    *,
    migration_id: str,
    target_context_sha256: str,
    owner_run_id: str,
    command_sha256: str,
    state_generation: str,
    process_observations: Sequence[Mapping[str, object]],
    fail_after: str | None = None,
    timeout_seconds: float = 30,
) -> dict[str, object]:
    """Run only copy/verification/selector-state effects for synthetic callers.

    ``fail_after`` is deliberate fixture support.  It records partial reality;
    it never rolls back copied bytes or invokes a process action.
    """

    if fail_after not in {None, "planned", "staged", "published", "switched", "retained"}:
        raise InstallationTransactionError("migration-failure-phase-invalid", "unsupported injected phase")
    root = Path(project_root).absolute()
    with installation_publication_lock(
        root,
        target_context_sha256=target_context_sha256,
        owner_run_id=owner_run_id,
        operation="legacy-migration",
        command_sha256=command_sha256,
        timeout_seconds=timeout_seconds,
    ) as lock:
        inventory = build_legacy_inventory(
            root,
            migration_id=migration_id,
            target_context_sha256=target_context_sha256,
            process_observations=process_observations,
        )
        write_inventory(root, inventory, lock=lock)
        quiescence = prove_quiescence(inventory, process_observations)
        write_quiescence(root, inventory, quiescence, lock=lock)
        if not quiescence["safe"]:
            return _terminal(root, inventory, lock, phase="planned", status="blocked", selector_changed=False)
        if fail_after == "planned":
            return _terminal(root, inventory, lock, phase="planned", status="partial", selector_changed=False)
        staged = stage_legacy_copy(root, inventory, quiescence, lock=lock)
        if fail_after == "staged":
            return _terminal(root, inventory, lock, phase="staged", status="partial", selector_changed=False)
        verify_staged_copy(root, inventory, staged)
        write_transaction_status(root, inventory, phase="published", status="pending-switch", lock=lock)
        if fail_after == "published":
            return _terminal(root, inventory, lock, phase="published", status="partial", selector_changed=False)
        try:
            switch_runtime_selector(root, inventory, staged, state_generation=state_generation, lock=lock)
        except InstallationStateError as error:
            if error.code == "switch-recording-pending":
                return _terminal(root, inventory, lock, phase="switched", status="recording-pending", selector_changed=True)
            raise
        if fail_after == "switched":
            return _terminal(root, inventory, lock, phase="switched", status="recording-pending", selector_changed=True)
        if fail_after == "retained":
            return _terminal(root, inventory, lock, phase="retained", status="recording-pending", selector_changed=True)
        return _terminal(root, inventory, lock, phase="retained", status="completed", selector_changed=True)


__all__ = [
    "InstallationPublicationLock",
    "InstallationTransactionError",
    "installation_publication_lock",
    "run_retained_legacy_migration",
]
