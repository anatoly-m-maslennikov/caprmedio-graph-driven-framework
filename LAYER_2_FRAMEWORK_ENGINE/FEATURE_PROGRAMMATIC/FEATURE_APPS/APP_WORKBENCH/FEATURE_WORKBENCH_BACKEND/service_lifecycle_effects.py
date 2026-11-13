"""Workbench lifecycle effects operations."""
from __future__ import annotations
from contextlib import contextmanager, nullcontext
import os
import stat
import sys
from pathlib import Path
from typing import Any


class ServiceLifecycleEffects:
    def lifecycle_changed(self, old: Path | None, new: Path | None) -> None:
        with self._refresh_lock:
            cached = self._lifecycle_reads.get()
            if cached is not None:
                for changed in (old, new):
                    if changed is not None:
                        cached.pop(Path(changed).absolute(), None)
            self._archive_layout()
            if old is not None:
                old_path = Path(old).absolute().relative_to(self._root).as_posix()
                self._lifecycle_pending.add(old_path)
                self._fresh_archive_paths.discard(old_path)
            if new is not None:
                new_path = Path(new).absolute().relative_to(self._root).as_posix()
                self._lifecycle_pending.add(new_path)
                if self._in_declared_archive(new_path):
                    self._fresh_archive_paths.add(new_path)

    def lifecycle_file_effect(self):
        return self._refresh_lock

    def lifecycle_publication(self):
        if getattr(self._lifecycle_group, "active", False):
            return nullcontext()
        return self.group_lifecycle_refresh()

    def project_consistency(self) -> dict[str, Any]:
        self._start()
        assert self._store is not None
        counts = self._store.project_consistency()
        return {**counts, **self._audit_status()}

    @contextmanager
    def lifecycle_read_scope(self):
        """Reuse a verified carrier read only within one lifecycle request."""
        if self._lifecycle_reads.get() is not None:
            yield
            return
        token = self._lifecycle_reads.set({})
        try:
            yield
        finally:
            self._lifecycle_reads.reset(token)

    def lifecycle_read(self, path: Path, *, descriptor: int | None = None) -> bytes:
        from VALIDATE_ATOMS.validate_atoms_workers.read_io import ReadContext, open_regular
        from VALIDATE_ATOMS.validate_atoms_workers.settings import CEILINGS

        self._start()
        path = Path(path).absolute()
        with self._refresh_lock:
            if not path.is_relative_to(self._reader.control_root):
                raise ValueError("Atom path is outside the lifecycle source boundary")
            assert self._store is not None
            reader = ReadContext(roots=[str(self._root)], limits=dict(CEILINGS))
            reader.allowed(path)
            # Bind the bytes and stability check to the same opened carrier.
            carrier_fd = open_regular(path) if descriptor is None else descriptor
            with os.fdopen(carrier_fd, "rb", closefd=descriptor is None) as carrier:
                def signature():
                    info = os.fstat(carrier.fileno())
                    if not stat.S_ISREG(info.st_mode):
                        raise ValueError("Atom carrier is not a regular file")
                    return (info.st_dev, info.st_ino, info.st_size, info.st_mtime_ns, info.st_ctime_ns)
                before = signature()
                reader.check_size(before[2])
                cached = self._lifecycle_reads.get()
                existing = cached.get(path) if cached is not None else None
                if existing is not None and existing[0] != before:
                    raise ValueError("Atom carrier changed during lifecycle request")
                raw = existing[1] if existing is not None else carrier.read(before[2])
                if signature() != before:
                    raise ValueError("Atom carrier changed during read")
                if cached is not None and existing is None:
                    cached[path] = (before, raw)
            return raw

    def lifecycle_declarations(self):
        self._start()
        with self._refresh_lock:
            return self._reader._declarations

    def _flush_lifecycle_changes(self) -> None:
        if getattr(self._lifecycle_group, "active", False):
            return
        self._start()
        with self._lifecycle_flush_lock, self._refresh_lock:
            self._publish_lifecycle_paths()

    def _publish_lifecycle_paths(self) -> None:
        pending, self._lifecycle_pending = self._lifecycle_pending, set()
        if pending:
            self._refresh([
                {"operation": "update", "old_path": path,
                 "new_path": path if (self._root / path).exists() else None}
                for path in sorted(pending)
            ])

    @contextmanager
    def group_lifecycle_refresh(self):
        self._start()
        publication = {}
        with self._lifecycle_flush_lock, self._refresh_lock:
            self._publish_lifecycle_paths()
            self._lifecycle_group.active = True
            try:
                yield publication
            finally:
                self._lifecycle_group.active = False
                try:
                    self._publish_lifecycle_paths()
                except (OSError, RuntimeError, ValueError) as error:
                    print(f"Workbench ERROR grouped_lifecycle_refresh {type(error).__name__}: {error}",
                          file=sys.stderr, flush=True)
                    publication["error"] = "Lifecycle file effects completed, but Workbench could not publish them."

    def lifecycle_descendants(self, references: tuple[str, ...], relation: str) -> set[str]:
        self._flush_lifecycle_changes()
        assert self._store is not None
        return self._store.lifecycle_descendants(references, relation)
