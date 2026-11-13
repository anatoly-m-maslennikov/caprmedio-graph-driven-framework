"""Workbench indexing operations."""
from __future__ import annotations
import sys
import threading
from pathlib import Path
from . import service as _service
from .errors import WorkbenchUnavailableError
from .runtime_settings import result_ttl_seconds
from .source_watcher import Change
from .spec_trace import PILOT


class ServiceIndexing:
    def _index(self) -> None:
        try:
            pilot = self._root / PILOT
            self._watcher = _service.SourceWatcher(
                self._reader.root, self._reader.control_root,
                implementation_root=pilot if pilot.is_dir() and pilot.resolve() == pilot else None,
            )
            self._watcher.start()
            self._watch_ready.set()
            while not self._stop.is_set():
                batch = self._watcher.changes(timeout=0.1)
                if batch:
                    self._record_watcher_changes(batch)
                if batch and not self._journal_only(batch):
                    with self._refresh_lock:
                        trace_paths = {
                            path for event in batch for path in (event["old_path"], event["new_path"])
                            if path is not None and Path(path).is_relative_to(PILOT)
                        }
                        if trace_paths:
                            self._refresh_spec_traces(sorted(trace_paths))
                        changed = [
                            event for event in batch if any(
                                path is not None and (self._root / path).is_relative_to(self._reader.control_root)
                                for path in (event["old_path"], event["new_path"])
                            ) and self._watcher_needs_refresh(event)
                        ]
                        if changed:
                            self._refresh([self._watcher_projection_event(event) for event in changed])
                self._prune_watcher_changes()
                assert self._store is not None
                self._store.prune_results()
        except Exception as error:
            self._failure = WorkbenchUnavailableError(f"Workbench indexing failed; restart required: {error}")
            self._watch_ready.set()
            if not self._stop.is_set():
                print(self._failure, file=sys.stderr)
        finally:
            if self._watcher is not None:
                self._watcher.close()
                self._watcher = None

    def _watcher_needs_refresh(self, event: Change) -> bool:
        for relative in (event["old_path"], event["new_path"]):
            if relative is None:
                continue
            path = self._root / relative
            if path.suffix != ".md" or path.is_symlink():
                return True
            signature = _service.file_signature(path)
            if signature is None:
                if path in self._reader._source_paths or (path.is_relative_to(self._reader.control_root) and self._reader._archive_path(path)):
                    return True
                continue
            if (path.is_relative_to(self._reader.control_root) and self._reader._archive_path(path) and path not in self._reader._source_paths):
                return True
            cached = self._reader._cached.get(path)
            if signature != (cached[0] if cached is not None else self._reader._failed.get(path)):
                return True
        return False

    def _watcher_projection_event(self, event: Change) -> Change:
        old = event["old_path"]
        if old is not None and event["new_path"] is None:
            path = self._root / old
            # A delayed delete can arrive after the carrier or directory reappears.
            exists = (_service.file_signature(path) is not None if path.suffix == ".md"
                      else path.is_dir(follow_symlinks=False))
            if exists:
                return {"operation": "update", "old_path": old, "new_path": old}
        return event

    def _rehydrate_watcher_changes(self) -> None:
        assert self._store is not None
        self._store.sync_change_log(self._watcher_change_log, initialize=True)
    def _record_watcher_changes(self, batch: list[Change]) -> None:
        assert self._store is not None
        self._store.sync_change_log(self._watcher_change_log, batch)
    def _prune_watcher_changes(self) -> None:
        assert self._store is not None
        self._store.sync_change_log(self._watcher_change_log)
    def _journal_only(self, batch: list[Change]) -> bool:
        journal = (self._root / _service.configured_journal_root(self._root)).resolve()
        paths = [
            path
            for change in batch
            for path in (change["old_path"], change["new_path"])
            if path is not None
        ]
        return bool(paths) and all(
            (self._root / path).resolve().is_relative_to(journal) for path in paths
        )
    def _start(self) -> None:
        with self._start_lock:
            if self._failure:
                raise self._failure
            if self._store is not None:
                return
            try:
                self._store = _service.QueryStore(
                    extension_directory=self._extension_directory,
                    database_path=self._database_path,
                    result_ttl_seconds=result_ttl_seconds(self._root),
                    schema_mode=self._schema_mode,
                )
                self._rehydrate_watcher_changes()
                try:
                    store = self._store
                    records = self._query_log.bind(lambda record: store.record_query_attempts([record]))
                    store.record_query_attempts(records)
                except (OSError, ValueError) as error:
                    print(f"query log failed: {error}", file=sys.stderr)
                with self._refresh_lock:
                    self._thread = threading.Thread(target=self._index, name="workbench-index", daemon=True)
                    self._thread.start()
                    self._watch_ready.wait()
                    if self._failure:
                        raise self._failure
                    self._refresh()
            except Exception as error:
                self._stop.set()
                if self._thread is not None:
                    self._thread.join()
                if self._audits is not None:
                    self._audits.close()
                self._failure = WorkbenchUnavailableError(
                    f"Workbench startup failed; restart required: {error}"
                )
                print(self._failure, file=sys.stderr)
                raise self._failure from error
