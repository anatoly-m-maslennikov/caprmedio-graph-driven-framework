# CA-D-672@24
# CA-M-1013@1
# CA-D-718@1
# CA-R-2728@8
# CA-R-2729@11
# CA-R-2950@4
# CA-R-2952@5
# CA-M-465@29
# CA-M-490@3
# CA-M-491@2
# CA-D-695@3
# CA-D-696@2
# CA-D-673@18
# CA-R-2786@5
# CA-M-474@2
# CA-R-2903@8
# CA-M-502@2
# CA-R-2723@7
# CA-R-2725@6
# CA-M-549@3
# CA-O-10025@1
# CA-M-551@2
# CA-D-715@3
# CA-M-463@10
"""One Project's direct file reader, background indexer, and SQL capability."""
from __future__ import annotations
from contextlib import contextmanager, nullcontext
from contextvars import ContextVar
import datetime as dt
import json
import os
import stat
from pathlib import Path
import shutil
import sys
import threading
import time
from typing import Any

from .errors import QueryExecutionError, WorkbenchUnavailableError
from .audit_worker import AuditSnapshot, AuditWorker
from .query_store import QueryStore
from .query_log import QueryLog
from .result_delivery import deliver, validate_delivery, result_metadata, failed_metadata
from .incremental_relations import RelationState, materialize_delta
from .generate_relation_registry import DEFAULT_REGISTRY_PATH
from .relation_registry import RelationRegistry
from .relation_registry_asset import load_registry_asset
from .runtime_settings import result_ttl_seconds, schema_mode
from .saved_queries import SavedQueryStore
from .source_reader import SourceReader
from .source_rows import file_signature
from .source_placement_audit import affected_descendants
from .source_roles import CANONICAL_ROLE_MARKERS
from .source_watcher import Change, SourceWatcher
from .statements import select_statement
from .watcher_change_log import WatcherChangeLog
from .header_columns import HeaderSchema, infer_header_schema
from .workbench_schema_asset import SchemaCompilation, load_image_schema
from .workspace import WorkspaceStore
TOOLS = Path(__file__).resolve().parents[3] / "FEATURE_TOOLS"
if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))

from work_journal import configured_journal_root  # noqa: E402
from carrier_aliases import canonical_role_name, named_value_token  # noqa: E402
from ATOM_LIFECYCLE.source import ArchiveNotLoadedError  # noqa: E402


def _load_audit_model():
    from ATOM_LIFECYCLE.candidate_schema import load_candidate_schema
    from ATOM_LIFECYCLE.status_model import load_status_model
    from .source_schema_audit import SourceSchemaAudit

    assets = TOOLS / "ATOM_LIFECYCLE"
    return SourceSchemaAudit(load_candidate_schema(assets / "candidate_schema.json"),
                             load_status_model(assets / "status_model.json"))


from .service_refresh import ServiceRefresh
from .service_lifecycle import ServiceLifecycle
from .service_lifecycle_effects import ServiceLifecycleEffects
from .service_indexing import ServiceIndexing
from .service_interface import ServiceInterface


class WorkbenchService(ServiceRefresh, ServiceLifecycle, ServiceLifecycleEffects, ServiceIndexing, ServiceInterface):
    """Own only the Workbench lifecycle; QueryStore owns database serialization."""

    def __init__(
        self, root: Path, *, extension_directory: Path | None = None,
        compiled_schema: SchemaCompilation | None = None,
        relation_registry: RelationRegistry | None = None,
        archive_placement: Any | None = None,
    ) -> None:
        self._root = Path(root).resolve()
        self._schema_mode = schema_mode(self._root)
        try:
            compiled = compiled_schema if compiled_schema is not None else load_image_schema()
            self._registry = (
                relation_registry if relation_registry is not None else load_registry_asset(DEFAULT_REGISTRY_PATH)
            )
        except (OSError, ValueError) as error:
            print(f"Workbench image assets unavailable: {error}", file=sys.stderr)
            raise WorkbenchUnavailableError(f"Workbench image assets unavailable: {error}") from error
        audit_model = _load_audit_model() if compiled_schema is None else None
        self._archive_placement = audit_model.schema.placement if audit_model is not None else archive_placement
        self._reader = SourceReader(
            self._root, schema_mode=self._schema_mode, compiled_schema=(compiled.content, compiled.mode_one),
            status_groups=compiled.status_groups,
            role_folders=compiled.role_folders,
            audit_model=audit_model, include_archived=False,
            archive_placement=self._archive_placement,
        )
        self._content_schema = compiled.content
        self._header_schema: HeaderSchema | None = compiled.mode_one if self._schema_mode == 1 else None
        self._saved_queries = SavedQueryStore(self._root)
        self._workspaces = WorkspaceStore(self._root)
        self._workspaces.clear_transient_results()
        self._query_log = QueryLog(self._root)
        self._watcher_change_log = WatcherChangeLog(self._root)
        self._extension_directory = extension_directory
        self._database_path = (
            self._root / ".caprmedio_runtime" / "workbench" / "projection.duckdb"
        )
        self._start_lock = threading.Lock()
        self._refresh_lock = threading.RLock()
        self._interface_lock = threading.RLock()
        self._sync_status_lock = threading.Lock()
        self._watch_ready = threading.Event()
        self._stop = threading.Event()
        self._store: QueryStore | None = None
        self._audits: AuditWorker | None = None
        self._thread: threading.Thread | None = None
        self._watcher: SourceWatcher | None = None
        self._relation_state: RelationState | None = None
        self._failure: WorkbenchUnavailableError | None = None
        self._paths: set[str] = set()
        self._syncing = 0
        self._last_synced_at: str | None = None
        self._lifecycle_pending: set[str] = set()
        self._lifecycle_flush_lock = threading.Lock()
        self._lifecycle_group = threading.local()
        self._lifecycle_reads: ContextVar[dict[Path, tuple[tuple[int, ...], bytes]] | None] = ContextVar(
            "workbench_lifecycle_reads", default=None
        )
        self._archive_digest: str | None = None
        self._archive_folders: dict[tuple[str, str], tuple[str, ...]] = {}
        self._archive_names: dict[str, str] = {}
        self._archive_roots: set[Path] = set()
        self._loaded_archives: dict[tuple[str, str], tuple[str, ...]] = {}
        self._fresh_archive_paths: set[str] = set()
    def page(
        self, query_id: str, offset: int, page_size: int = 100, *, grid: object = None,
        preview: int | None = None, result_delivery: str = "file", result_format: str = "json_matrix",
    ) -> dict[str, Any]:
        validate_delivery(result_delivery, result_format)
        self._start()
        assert self._store is not None
        self._store.prune_results()
        page = self._store.page(query_id, offset, page_size=page_size, preview=preview, grid=grid)
        return deliver(self._store, self._root, page, result_delivery, result_format)

    def check(self, sql: str, cursor_position: int | None = None) -> dict[str, Any]:
        selected = select_statement(sql, cursor_position)
        self._start()
        assert self._store is not None
        result = self._store.check(selected)
        result.pop("sql", None)
        return result

    def save_view(self, sql: str, name: str | None = None) -> dict[str, Any]:
        return self._saved_queries.save_view(sql, name)

    def load(self, reference: str) -> dict[str, str]:
        return self._saved_queries.load(reference)

    def saved_list(self, limit: int = 20) -> dict[str, list[dict[str, str]]]:
        return self._saved_queries.list(limit)

    def schema(self) -> dict[str, dict[str, list[dict[str, str]]]]:
        self._start()
        assert self._store is not None
        return self._store.schema()

    def set_live_runs(self, rows: list[dict[str, str]]) -> None:
        self._start()
        assert self._store is not None
        self._store.set_live_runs(rows)

    def set_runtime_diagnostics(self, rows: list[dict[str, str]]) -> None:
        self._start()
        assert self._store is not None
        self._store.set_runtime_diagnostics(rows)

    def discard_derived_state(self) -> None:
        """Discard only this Workbench's rebuildable database before a full reread."""
        self.close()
        self._database_path.unlink(missing_ok=True)
        self._database_path.with_name(f"{self._database_path.name}.wal").unlink(missing_ok=True)
        temporary = self._database_path.parent / "duckdb-temp"
        if temporary.is_dir():
            shutil.rmtree(temporary)

    def close(self) -> None:
        self._stop.set()
        if self._thread is not None:
            self._thread.join()
        if self._audits is not None:
            self._audits.close()
        self._query_log.close()
        if self._store is not None:
            self._store.close()
