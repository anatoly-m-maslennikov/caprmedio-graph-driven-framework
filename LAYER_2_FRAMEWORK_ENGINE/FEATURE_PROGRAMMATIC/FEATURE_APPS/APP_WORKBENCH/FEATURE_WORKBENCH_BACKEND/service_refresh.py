"""Workbench refresh operations."""
from __future__ import annotations
import datetime as dt
import time
from typing import Any
from . import service as _service
from .audit_worker import AuditSnapshot, AuditWorker
from .header_columns import infer_header_schema
from .source_watcher import Change
from .spec_trace import SpecTraceStore


class ServiceRefresh:
    def _refresh(self, changes: list[Change] | None = None) -> None:
        self._begin_sync()
        succeeded = False
        try:
            with self._refresh_lock:
                assert self._store is not None
                if self._reader._catalog is None:
                    from .archive_catalog import ArchiveCatalog
                    self._reader._catalog = ArchiveCatalog(self._store._connection, self._store._lock, self._root)
                    from .reference_catalog import ReferenceCatalog
                    self._reader._references = ReferenceCatalog(self._store._connection, self._store._lock, self._root)
                started = time.monotonic()
                atoms, scopes = self._capture(changes)
                audit_paths = self._reader.audit_delta
                if audit_paths is None or audit_paths:
                    if self._audits is None:
                        self._audits = AuditWorker(self._store)
                    self._audits.invalidate()
                with self._store._lock:
                    self._reader._catalog.refresh_summaries({row["id"] for row in atoms if row.get("id") and row.get("status_group") in {"Current", "Draft"}})
                    captured_at = time.monotonic()
                    capture_seconds = captured_at - started
                    full = changed = False
                    materialize_seconds = write_seconds = 0.0
                    if changes is None or self._reader.capture_changed:
                        if self._header_schema is None:
                            self._header_schema = infer_header_schema(atoms)
                            self._reader.set_observed_header_schema(self._header_schema)
                        atoms, scopes, registered, _inverse, next_state, delta = _service.materialize_delta(
                            atoms, scopes, self._relation_state,
                            changes=self._reader.capture_delta, registry=self._registry,
                        )
                        materialize_seconds = time.monotonic() - captured_at
                        full = delta is None
                        writing_started = time.monotonic()
                        previous = self._relation_state
                        same_registry = previous is not None and (
                            previous.registered, previous.inverse, previous.aliases, previous.collisions
                        ) == (next_state.registered, next_state.inverse, next_state.aliases, next_state.collisions)
                        reuse_full = full and changes is not None and same_registry
                        if not full or reuse_full:
                            changed = self._store.apply(
                                atoms, scopes, relation_types=registered, content_schema=self._content_schema,
                                delta=delta, header_schema=self._header_schema,
                            )
                        if full and (not reuse_full or self._store.schema_changed):
                            self._store.replace(
                                atoms, scopes, relation_types=registered, content_schema=self._content_schema,
                                header_schema=self._header_schema,
                            )
                            changed = True
                        write_seconds += time.monotonic() - writing_started
                        self._relation_state = next_state
                        if self._reader.audit_delta is not None:
                            self._reader.audit_delta.update(_service.affected_descendants(previous, next_state, self._reader.audit_delta))
                if self._audits is not None and (audit_paths is None or audit_paths):
                    self._audits.submit(
                        AuditSnapshot.capture(self._reader, self._audits.capture_paths(audit_paths)), audit_paths
                    )
                if changes is None:
                    self._refresh_spec_traces()
                    self._lifecycle_pending.clear()
                else:
                    self._lifecycle_pending.difference_update(
                        path for change in changes for key in ("old_path", "new_path")
                        if (path := change.get(key)) is not None
                    )
                written_at = time.monotonic()
                paths = {row["source_path"] for row in atoms}
                removed = len(self._paths - paths)
                self._paths = paths
                succeeded = True
                print(
                    "Workbench INFO refresh "
                    f"mode={'full' if full else 'delta'} changed={str(changed).lower()} "
                    f"atoms={len(atoms)} scopes={len(scopes)} removed_atom_sources={removed} "
                    f"excluded_sources={self._reader.excluded_count} "
                    f"capture_ms={round(capture_seconds * 1000, 1)} "
                    f"materialize_ms={round(materialize_seconds * 1000, 1)} "
                    f"write_ms={round(write_seconds * 1000, 1)} "
                    f"elapsed_ms={round((written_at - started) * 1000, 1)}",
                    flush=True,
                )
        finally:
            self._finish_sync(succeeded)

    def _refresh_spec_traces(self, paths: list[str] | None = None) -> None:
        assert self._store is not None
        with self._store._lock:
            connection = self._store._connection
            traces = SpecTraceStore(connection, self._root)
            connection.execute("BEGIN TRANSACTION")
            try:
                if paths is None:
                    traces.initialize()
                traces.refresh(paths)
                connection.execute("COMMIT")
            except Exception:
                connection.execute("ROLLBACK")
                raise

    def _capture(self, changes: list[Change] | None):
        atoms, scopes = self._reader.capture(changes)
        if self._archive_layout():
            return self._reader.capture()
        return atoms, scopes
    def _begin_sync(self) -> None:
        with self._sync_status_lock:
            self._syncing += 1
    def _finish_sync(self, succeeded: bool) -> None:
        with self._sync_status_lock:
            if succeeded:
                self._last_synced_at = dt.datetime.now(dt.UTC).isoformat()
            self._syncing -= 1
    def sync_status(self) -> dict[str, Any]:
        """Return the owner-local indexing snapshot without starting Workbench."""
        audit = self._audit_status()
        with self._sync_status_lock:
            return {"syncing": self._syncing > 0, "last_synced_at": self._last_synced_at,
                    "loaded_archive_scopes": self._archive_coverage(), **audit}

    def _audit_status(self) -> dict[str, Any]:
        if self._audits is not None:
            return self._audits.status()
        return {"audits_pending": False, "last_audit_ms": None, "audit_error": None}

    def wait_for_audits(self, timeout: float | None = None) -> bool:
        return self._audits is None or self._audits.wait(timeout)

