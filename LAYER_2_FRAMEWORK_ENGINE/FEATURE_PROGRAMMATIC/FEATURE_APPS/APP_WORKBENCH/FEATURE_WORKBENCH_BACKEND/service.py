# CA-R-1603@15
# CA-R-2725@2
# CA-M-463@4
# CA-M-465@10
# CA-D-675@9

"""One Project's direct file reader, background indexer, and SQL capability."""

from __future__ import annotations

import hashlib
from pathlib import Path
import sys
import threading
from typing import Any

from watchfiles import watch

from .query_store import QueryStore
from .relations import canonical, materialize
from .source_reader import SourceReader


class WorkbenchService:
    """Own only the Workbench lifecycle; QueryStore owns database serialization."""

    def __init__(self, root: Path, *, extension_directory: Path | None = None) -> None:
        self._root = Path(root).resolve()
        self._reader = SourceReader(self._root)
        self._extension_directory = extension_directory
        self._database_path = (
            self._root / ".caprmedio_runtime" / "workbench" / "projection.duckdb"
        )
        self._start_lock = threading.Lock()
        self._refresh_lock = threading.Lock()
        self._watch_ready = threading.Event()
        self._stop = threading.Event()
        self._store: QueryStore | None = None
        self._thread: threading.Thread | None = None
        self._signature: str | None = None
        self._failure: str | None = None
        self._paths: set[str] = set()

    def _refresh(self) -> None:
        with self._refresh_lock:
            atoms, scopes = self._reader.capture()
            signature = hashlib.sha256(canonical([atoms, scopes]).encode("utf-8")).hexdigest()
            if signature == self._signature:
                self._reader.release_cache()
                return
            atoms, scopes = materialize(atoms, scopes)
            assert self._store is not None
            self._store.replace(atoms, scopes)
            self._reader.release_cache()
            self._signature = signature
            paths = {row["source_path"] for row in atoms}
            removed = len(self._paths - paths)
            self._paths = paths
            print(f"Workbench: indexed {len(atoms)} Atoms and {len(scopes)} Scope Units; "
                  f"removed_atom_sources={removed}; excluded_sources={self._reader.excluded_count}",
                  file=sys.stderr)

    def _index(self) -> None:
        try:
            watch_root = self._reader.control_root.resolve()
            if not watch_root.is_relative_to(self._reader.root):
                raise ValueError("Workbench sources must be inside the selected repository")
            changes = watch(
                str(watch_root),
                stop_event=self._stop,
                rust_timeout=100,
                yield_on_timeout=True,
            )
            try:
                first_batch = next(changes)
            except StopIteration:
                self._watch_ready.set()
                return
            self._watch_ready.set()
            if first_batch and not self._stop.is_set():
                self._refresh()
            for _batch in changes:
                if self._stop.is_set():
                    return
                if _batch:
                    self._refresh()
        except Exception as error:
            self._failure = f"Workbench indexing failed; restart required: {error}"
            self._watch_ready.set()
            if not self._stop.is_set():
                print(self._failure, file=sys.stderr)

    def _start(self) -> None:
        with self._start_lock:
            if self._failure:
                raise RuntimeError(self._failure)
            if self._store is not None:
                return
            try:
                self._store = QueryStore(
                    extension_directory=self._extension_directory,
                    database_path=self._database_path,
                )
                self._thread = threading.Thread(target=self._index, name="workbench-index", daemon=True)
                self._thread.start()
                self._watch_ready.wait()
                if self._failure:
                    raise RuntimeError(self._failure)
                self._refresh()
            except Exception as error:
                self._stop.set()
                if self._thread is not None:
                    self._thread.join()
                self._failure = f"Workbench startup failed; restart required: {error}"
                print(self._failure, file=sys.stderr)
                raise RuntimeError(self._failure) from error

    def run(self, sql: str, page_size: int = 100) -> dict[str, Any]:
        self._start()
        assert self._store is not None
        return self._store.run(sql, page_size=page_size)

    def page(self, query_id: str, offset: int, page_size: int = 100) -> dict[str, Any]:
        self._start()
        assert self._store is not None
        return self._store.page(query_id, offset, page_size=page_size)

    def check(self, sql: str) -> dict[str, Any]:
        self._start()
        assert self._store is not None
        return self._store.check(sql)

    def close(self) -> None:
        self._stop.set()
        if self._thread is not None:
            self._thread.join()
        if self._store is not None:
            self._store.close()
