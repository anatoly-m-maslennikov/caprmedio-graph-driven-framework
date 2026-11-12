# CA-M-465@29
"""Compute source diagnostics away from the query and lifecycle response path."""
from __future__ import annotations

from contextlib import contextmanager
from dataclasses import dataclass
from pathlib import Path
import sys
import threading
import time
from types import MappingProxyType
from typing import Any

from .audit_tables import TABLES, collect_issues
from .source_placement_audit import expected_carrier


@dataclass(frozen=True)
class AuditSnapshot:
    root: Path
    control_root: Path
    source_paths: frozenset[Path]
    cached: dict[Path, tuple[Any, dict[str, Any]]]
    diagnostics: dict[Path, str]
    accepted: frozenset[Path]
    references: dict[str, tuple[Path, ...]]
    units: tuple[dict[str, Any], ...]
    root_unit_name: str
    project_scope_id: str
    schema: Any
    role_folders: Any
    audit_model: Any
    invalid: frozenset[Path]

    @classmethod
    def capture(cls, reader: Any) -> AuditSnapshot:
        declarations = reader._declarations
        if declarations is None:
            raise ValueError("Scope Unit declarations are unavailable for Atom audits")
        return cls(
            reader.root, reader.control_root, frozenset(reader._source_paths), MappingProxyType(dict(reader._cached)),
            MappingProxyType(dict(reader._diagnostics)), frozenset(reader._references.accepted),
            MappingProxyType({ref: tuple(sorted(paths)) for ref, paths in reader._references.paths.items()}),
            tuple(declarations.as_structure()["scope_units"]), declarations.root.name,
            reader._project_scope_id, reader.content_schema, reader._role_folders, reader._audit_model,
            frozenset(reader._content_invalid | reader._header_invalid),
        )

    def current_row(self, reference: str) -> dict[str, Any] | None:
        for path in self.references.get(reference, ()):
            if path in self.accepted and (item := self.cached.get(path)) is not None:
                row = item[1]
                return row if row.get("status_group") not in {"Draft", "Archived"} else None
        return None

    def collect(self, public_atoms: dict[tuple[str, str], dict[str, Any]], paths: set[str]):
        schema_audit = placement_audit = None
        if self.audit_model is not None:
            schema_audit = self.audit_model.issues
            placement = self.audit_model.schema.placement
            if placement is not None:
                units = {unit[key]: unit for unit in self.units for key in ("scope_unit_name", "scope_unit_id")}
                if (root_unit := units.get(self.root_unit_name)) is not None:
                    units[self.project_scope_id] = root_unit

                def placement_audit(row):
                    return expected_carrier(row, units, self.current_row, placement)

        return collect_issues(
            self.root, self.control_root, self.source_paths, paths, self.cached, self.diagnostics,
            self.accepted, self.units, self.project_scope_id, self.schema, public_atoms,
            self.role_folders, schema_audit=schema_audit, placement_audit=placement_audit,
            schema_invalid=self.invalid,
        )


_EMPTY = object()


def _merge_paths(old, new):
    if old is _EMPTY:
        return None if new is None else set(new)
    if old is None or new is None:
        return None
    return old | set(new)


class AuditWorker:
    """Complete a full audit once and coalesce newer work behind it.

    Full results can briefly precede newer deltas; status stays pending until
    all queued changes have published. Stale partial audits are discarded.

    Call invalidate() before changing the projection, then submit(captured_snapshot,
    audit_delta) after it is updated. A None delta requests a complete audit.
    close() stops the worker before closing or rebuilding the QueryStore.
    """

    def __init__(self, store: Any) -> None:
        self._store = store
        self._condition = threading.Condition()
        self._generation = 0
        self._pending_paths = _EMPTY
        self._pending_snapshot: AuditSnapshot | None = None
        self._active_paths = _EMPTY
        self._awaiting_submit = False
        self._stopped = False
        self._error: BaseException | None = None
        self._last_audit_ms: float | None = None
        self._thread = threading.Thread(target=self._run, name="workbench-audits", daemon=True)
        self._thread.start()

    def invalidate(self) -> None:
        with self._condition:
            if self._error is not None:
                return
            self._generation += 1
            self._awaiting_submit = True
            if self._active_paths is not _EMPTY and self._active_paths is not None:
                self._pending_paths = _merge_paths(self._pending_paths, self._active_paths)
            self._pending_snapshot = None

    def submit(self, snapshot: AuditSnapshot, paths: set[str] | None) -> None:
        with self._condition:
            if self._stopped:
                raise RuntimeError("Atom audit worker is stopped")
            if self._error is not None:
                return
            self._pending_paths = _merge_paths(self._pending_paths, paths)
            self._pending_snapshot = snapshot
            self._awaiting_submit = False
            self._condition.notify_all()

    def _current(self, generation: int, *, full: bool = False) -> bool:
        with self._condition:
            return not self._stopped and (full or generation == self._generation)

    @contextmanager
    def _publication(self, generation: int, *, full: bool = False):
        with self._condition:
            yield not self._stopped and (full or generation == self._generation)

    def _run(self) -> None:
        try:
            while True:
                with self._condition:
                    self._condition.wait_for(lambda: self._stopped or self._pending_snapshot is not None)
                    if self._stopped:
                        return
                    snapshot, paths, generation = self._pending_snapshot, self._pending_paths, self._generation
                    self._pending_snapshot = None
                    self._pending_paths = _EMPTY
                    self._active_paths = paths
                started = time.monotonic()
                read_seconds = compute_seconds = 0.0
                selected = (sorted(path.relative_to(snapshot.root).as_posix() for path in snapshot.source_paths)
                            if paths is None else sorted(paths))
                issues = {table: [] for table in TABLES}
                for offset in range(0, len(selected), 500):
                    if not self._current(generation, full=paths is None):
                        break
                    batch = set(selected[offset:offset + 500])
                    phase = time.monotonic()
                    rows = self._store.audit_content_rows(batch)
                    read_seconds += time.monotonic() - phase
                    phase = time.monotonic()
                    for table, records in snapshot.collect(rows, batch).items():
                        issues[table].extend(records)
                    compute_seconds += time.monotonic() - phase
                if self._current(generation, full=paths is None):
                    phase = time.monotonic()
                    published = self._store.publish_audit(
                        issues, paths, self._publication(generation, full=paths is None)
                    )
                    publish_seconds = time.monotonic() - phase
                    if published:
                        elapsed_ms = (time.monotonic() - started) * 1000
                        with self._condition:
                            self._last_audit_ms = elapsed_ms
                        print(f"Workbench INFO atom_audit paths={len(selected)} "
                              f"mode={'full' if paths is None else 'delta'} "
                              f"read_ms={read_seconds * 1000:.1f} compute_ms={compute_seconds * 1000:.1f} "
                              f"publish_wait_and_commit_ms={publish_seconds * 1000:.1f} "
                              f"elapsed_ms={elapsed_ms:.1f}", flush=True)
                with self._condition:
                    self._active_paths = _EMPTY
                    self._condition.notify_all()
        except Exception as error:
            with self._condition:
                self._error = error
                self._active_paths = _EMPTY
                self._pending_paths = _EMPTY
                self._pending_snapshot = None
                self._awaiting_submit = False
                self._condition.notify_all()
            print(f"Workbench ERROR atom_audit {type(error).__name__}: {error}", file=sys.stderr, flush=True)

    def wait(self, timeout: float | None = None) -> bool:
        with self._condition:
            done = self._condition.wait_for(
                lambda: self._error is not None or (not self._awaiting_submit and self._pending_snapshot is None
                                                    and self._active_paths is _EMPTY),
                timeout,
            )
            if self._error is not None:
                raise RuntimeError("Atom audit worker failed") from self._error
            return done

    def status(self) -> dict[str, Any]:
        """Expose pending work and terminal errors without affecting source refresh."""
        with self._condition:
            return {
                "audits_pending": (self._awaiting_submit or self._pending_snapshot is not None
                                   or self._active_paths is not _EMPTY),
                "last_audit_ms": self._last_audit_ms,
                "audit_error": None if self._error is None else f"{type(self._error).__name__}: {self._error}",
            }

    def close(self) -> None:
        with self._condition:
            self._stopped = True
            self._generation += 1
            self._pending_snapshot = None
            self._pending_paths = _EMPTY
            self._awaiting_submit = False
            self._condition.notify_all()
        self._thread.join()
