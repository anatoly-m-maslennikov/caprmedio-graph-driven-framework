# CA-D-718@1
# CA-R-2728@7
# CA-R-2729@8
# CA-R-2950@2
# CA-R-2952@2
# CA-M-465@29
# CA-M-490@3
# CA-M-491@2
# CA-D-695@3
# CA-D-696@2
# CA-D-673@15
# CA-R-2786@2
# CA-M-474@2
# CA-R-2903@4
# CA-M-502@2
# CA-R-2723@6
# CA-R-2725@6
# CA-M-549@2
# CA-O-10025@1
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


class WorkbenchService:
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
    def _refresh(self, changes: list[Change] | None = None) -> None:
        self._begin_sync()
        succeeded = False
        try:
            with self._refresh_lock:
                assert self._store is not None
                started = time.monotonic()
                atoms, scopes = self._capture(changes)
                audit_paths = self._reader.audit_delta
                if audit_paths is None or audit_paths:
                    if self._audits is None:
                        self._audits = AuditWorker(self._store)
                    self._audits.invalidate()
                captured_at = time.monotonic()
                capture_seconds = captured_at - started
                full = changed = False
                materialize_seconds = write_seconds = 0.0
                if changes is None or self._reader.capture_changed:
                    if self._header_schema is None:
                        self._header_schema = infer_header_schema(atoms)
                        self._reader.set_observed_header_schema(self._header_schema)
                    atoms, scopes, registered, _inverse, next_state, delta = materialize_delta(
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
                        self._reader.audit_delta.update(affected_descendants(previous, next_state, self._reader.audit_delta))
                if self._audits is not None and (audit_paths is None or audit_paths):
                    self._audits.submit(AuditSnapshot.capture(self._reader), audit_paths)
                if changes is None:
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

    def _archive_coverage(self) -> list[dict[str, str]]:
        return [{"scope_unit": scope, "role": role} for scope, role in sorted(self._loaded_archives)]

    def _archive_layout(self) -> bool:
        declarations = self._reader._declarations
        if declarations is None or declarations.digest == self._archive_digest:
            return False
        self._archive_digest = declarations.digest
        self._archive_folders = {}
        self._archive_names = {}
        if self._archive_placement is not None:
            for row in declarations.as_structure()["scope_units"]:
                name = row["scope_unit_name"]
                identity = row["scope_unit_id"] or self._reader._project_scope_id
                self._archive_names.update({name: name, identity: name})
                for role in CANONICAL_ROLE_MARKERS:
                    try:
                        root = Path(row["authority_path"]) / self._archive_placement.role_folder(role)
                        folders = self._archive_placement.archive_folders(role)
                    except ValueError:
                        continue
                    self._archive_folders[name, role] = tuple((root / folder).as_posix() for folder in folders)
        self._archive_roots = {Path(folder) for folders in self._archive_folders.values() for folder in folders}
        with self._sync_status_lock:
            outdated = [key for key, paths in self._loaded_archives.items()
                        if self._archive_folders.get(key) != paths]
            for key in outdated:
                for path in self._loaded_archives.pop(key):
                    self._reader.unload_archive_folder(path)
        return bool(outdated)

    def load_archives(self, scopes: list[dict[str, str]]) -> dict[str, Any]:
        if not isinstance(scopes, list) or not scopes:
            raise ValueError("Provide at least one Scope Unit and Role.")
        self._start()
        with self._refresh_lock:
            self._archive_layout()
            selected = {}
            roles = {named_value_token(role): role for role in CANONICAL_ROLE_MARKERS}
            for pair in scopes:
                if (not isinstance(pair, dict) or pair.keys() != {"scope_unit", "role"}
                        or not all(isinstance(value, str) for value in pair.values())):
                    raise ValueError("Each Archive scope requires a Scope Unit and Role.")
                scope = self._archive_names.get(pair["scope_unit"])
                role = roles.get(named_value_token(canonical_role_name(pair["role"])))
                folders = self._archive_folders.get((scope, role))
                if folders is None:
                    raise ValueError("Unknown Scope Unit or Role, or no declared Archive placement.")
                selected[scope, role] = folders
            changes = self._reader.load_archive_folders(
                folder for folders in selected.values() for folder in folders
            )
            if changes:
                self._refresh(changes)
            with self._sync_status_lock:
                self._loaded_archives.update(selected)
                return {"loaded_archive_scopes": self._archive_coverage()}

    def _check_lifecycle_project(self, selection) -> None:
        if selection.root != self._root or selection.control_root != self._reader.control_root:
            raise ValueError("Lifecycle selection does not match Workbench Project")

    def lifecycle_candidates(self, selection, *, atom_ids=(), references=(), prefix=None, under=None):
        self._check_lifecycle_project(selection)
        self._flush_lifecycle_changes()
        assert self._store is not None
        relative = Path(under).relative_to(self._root).as_posix() if under is not None else None
        requested = (self._archive_lookup_versions(atom_ids, references)
                     if atom_ids and prefix is None and under is None else {})
        if requested:
            with self._refresh_lock:
                self._load_fresh_archive_matches(requested)
                rows = self._store.lifecycle_candidates(atom_ids=atom_ids, references=references)
                self._check_archive_lookup(requested, rows)
        else:
            rows = self._store.lifecycle_candidates(
                atom_ids=atom_ids, references=references, prefix=prefix, under=relative,
            )
        return [(reference.split("@", 1)[0], self._root / directory / filename)
                for reference, directory, filename in rows]

    def lifecycle_archive_candidates(self, selection, atom_id: str) -> list[tuple[str, Path]]:
        self._check_lifecycle_project(selection)
        self._flush_lifecycle_changes()
        assert self._store is not None
        requested = self._archive_lookup_versions((atom_id,), ())
        with self._refresh_lock:
            self._load_fresh_archive_matches(requested)
            rows = self._store.lifecycle_archive_candidates(atom_id)
            self._check_archive_lookup(requested, rows)
        return [(reference, self._root / directory / filename) for reference, directory, filename in rows]

    def lifecycle_contexts(self, selection, ref_id: str) -> list[tuple[Path, dict, str | None]]:
        """Read indexed context; watcher delivery bounds its freshness."""
        from VALIDATE_ATOMS.validate_atoms_workers.read_io import open_regular

        self._check_lifecycle_project(selection)
        self._flush_lifecycle_changes()
        assert self._store is not None

        result = []
        with self._refresh_lock:
            for row in self._store.lifecycle_contexts(ref_id):
                path = self._root / row["relative_path"] / row["filename"]
                if '..' in path.parts or not path.is_relative_to(self._reader.control_root):
                    raise ValueError("Atom path is outside the lifecycle source boundary")
                try:
                    descriptor = open_regular(path)
                    try:
                        if not stat.S_ISREG(os.fstat(descriptor).st_mode):
                            raise ValueError("Atom carrier is not a regular file")
                    finally:
                        os.close(descriptor)
                except OSError as error:
                    raise ValueError(f"Atom carrier index is stale: {path}") from error
                result.append((path, self._context_metadata(row), row.get("content.summary")))
        return result

    @staticmethod
    def _context_metadata(row: dict) -> dict:
        def first(*names):
            return next((row[name] for name in names if row.get(name) is not None), None)

        metadata = {}
        for key, names in {
            "atom_id": ("header.identity.atom_id", "header.identity.id", "header.atom_id"),
            "ref_id": ("header.identity.ref_id", "header.ref_id"),
            "version": ("header.state.version", "header.state.version_number", "header.version", "header.version_number"),
            "status": ("header.state.status", "header.status"),
            "role": ("header.context.role", "header.role", "header.content_role"),
            "form": ("header.context.form", "header.form", "header.type"),
        }.items():
            value = first(*names)
            if value is not None:
                metadata[key] = value
        container = first("header.context.container", "header.container")
        if isinstance(container, str):
            container = json.loads(container)
        container = dict(container) if isinstance(container, dict) else {}
        for kind in ("atom", "scope_unit"):
            value = first(f"header.context.container.{kind}", f"header.container.{kind}")
            if value is not None:
                container[kind] = value
        if container:
            metadata["container"] = container
        return metadata

    @staticmethod
    def _archive_lookup_versions(atom_ids, references):
        if not references:
            return {identity: None for identity in atom_ids}
        requested = {}
        for reference in references:
            identity, _, version = reference.partition("@")
            if version.isascii() and version.isdigit():
                requested.setdefault(identity, set()).add(int(version))
        return requested

    def _unloaded_archive_reservations(self, atom_id):
        self._archive_layout()
        return [(version, relative) for _, version, relative in self._reader.archive_reservations(
            atom_id, unloaded_only=True,
        ) if self._in_declared_archive(relative)]

    def _in_declared_archive(self, relative: str) -> bool:
        return any(parent in self._archive_roots for parent in Path(relative).parents)

    def _load_fresh_archive_matches(self, requested) -> None:
        changes = []
        for identity, versions in requested.items():
            for version, path in self._unloaded_archive_reservations(identity):
                if path in self._fresh_archive_paths and (versions is None or version in versions):
                    changes.extend(self._reader.load_archive_file(path))
        if changes:
            self._refresh(changes)

    def _check_archive_lookup(self, requested, rows) -> None:
        found = {reference for reference, _, _ in rows}
        for identity, versions in requested.items():
            missing = None if versions is None else versions - {
                version for version in versions if f"{identity}@{version}" in found
            }
            if missing is not None and not missing:
                continue
            if any(missing is None or version is None or version in missing
                   for version, _ in self._unloaded_archive_reservations(identity)):
                raise ArchiveNotLoadedError(f"Load the Archive Scope Unit and Role for {identity} before looking up its history.")

    def lifecycle_last_id(self, selection, prefix: str) -> str | None:
        self._check_lifecycle_project(selection)
        self._flush_lifecycle_changes()
        assert self._store is not None
        current = self._store.lifecycle_last_id(prefix)
        with self._refresh_lock:
            reserved = self._reader.max_atom_number(prefix.rsplit("-", 2)[-2])
        number = max(reserved, int(current[len(prefix):]) if current is not None else 0)
        return f"{prefix}{number}" if number else None

    def lifecycle_latest_version(self, selection, atom_id: str) -> int | None:
        self._check_lifecycle_project(selection)
        self._flush_lifecycle_changes()
        assert self._store is not None
        with self._refresh_lock:
            unloaded = self._unloaded_archive_reservations(atom_id)
            if any(version is None for version, _ in unloaded):
                raise ArchiveNotLoadedError(f"Load the Archive Scope Unit and Role for {atom_id} before allocating its next Version.")
            latest = self._store.lifecycle_latest_version(atom_id)
            return max(latest or 0, *(version for version, _ in unloaded), 0) or None

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
    def _index(self) -> None:
        try:
            self._watcher = SourceWatcher(self._reader.root, self._reader.control_root)
            self._watcher.start()
            self._watch_ready.set()
            while not self._stop.is_set():
                batch = self._watcher.changes(timeout=0.1)
                if batch:
                    self._record_watcher_changes(batch)
                if batch and not self._journal_only(batch):
                    with self._refresh_lock:
                        changed = [event for event in batch if self._watcher_needs_refresh(event)]
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
            signature = file_signature(path)
            if signature is None:
                if path in self._reader._source_paths or path in self._reader._archive_paths:
                    return True
                continue
            if (path in self._reader._archive_paths and path not in self._reader._source_paths):
                continue
            cached = self._reader._cached.get(path)
            if signature != (cached[0] if cached is not None else self._reader._failed.get(path)):
                return True
        return False

    def _watcher_projection_event(self, event: Change) -> Change:
        old = event["old_path"]
        if old is not None and event["new_path"] is None:
            path = self._root / old
            # An atomic replacement can recreate a file before its delete event arrives.
            if path.suffix == ".md" and file_signature(path) is not None:
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
        journal = (self._root / configured_journal_root(self._root)).resolve()
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
                self._store = QueryStore(
                    extension_directory=self._extension_directory,
                    database_path=self._database_path,
                    result_ttl_seconds=result_ttl_seconds(self._root),
                    schema_mode=self._schema_mode,
                )
                self._rehydrate_watcher_changes()
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
    def run(
        self, sql: str, page_size: int = 100, cursor_position: int | None = None,
        *, save: bool = False, preview: int | None = None, name: str | None = None,
        result_delivery: str = "file", result_format: str = "json_matrix",
    ) -> dict[str, Any]:
        validate_delivery(result_delivery, result_format)
        if type(save) is not bool:
            raise ValueError("save must be a boolean")
        if name is not None and not save:
            raise ValueError("name is only supported when save is true")
        page_size = QueryStore._page_size(page_size)
        preview = QueryStore._preview(preview)
        if save:
            name = SavedQueryStore._name(name)
        selected = select_statement(sql, cursor_position)
        try:
            result = self._run_store(selected, page_size=page_size, preview=preview, include_rows=True)
            if save:
                try:
                    result |= self._saved_queries.save_query(selected, name)
                except (ValueError, OSError) as error:
                    print(f"saved query failed: {error}", file=sys.stderr)
                    result |= {"outcome": "partial", "save_error": str(error)}
            self._log_attempt(selected, result_metadata(result))
            assert self._store is not None
            return deliver(self._store, self._root, result, result_delivery, result_format, full=True)
        except ValueError as error:
            self._log_attempt(selected, failed_metadata(error))
            raise
        except (QueryExecutionError, WorkbenchUnavailableError) as error:
            self._log_attempt(selected, failed_metadata(error))
            raise
    def _run_store(
        self, selected: str, *, page_size: int = 100, preview: int | None = None,
        include_rows: bool,
    ) -> dict[str, Any]:
        self._flush_lifecycle_changes()
        assert self._store is not None
        self._store.prune_results()
        return self._store.run(selected, page_size=page_size, preview=preview, include_rows=include_rows)
    def _log_attempt(self, sql: str, metadata: dict[str, Any]) -> None:
        try:
            self._query_log.append_async(sql, metadata)
        except Exception as error:
            print(f"query log failed: {error}", file=sys.stderr)
    def _drop_result(self, query_id: str | None) -> None:
        if query_id is not None and self._store is not None:
            self._store.drop(query_id)
    def _unpin_result(self, query_id: str | None) -> None:
        if query_id is not None and self._store is not None:
            self._store.unpin(query_id)
    @staticmethod
    def _arguments(name: str, arguments: object, allowed: set[str], required: set[str] = set()) -> dict[str, Any]:
        if not isinstance(arguments, dict) or set(arguments) - allowed or required - set(arguments):
            raise ValueError(f"invalid {name} arguments")
        return arguments
    @staticmethod
    def _limit(value: object, field: str = "limit") -> int:
        if isinstance(value, bool) or not isinstance(value, int) or not 1 <= value <= 1000:
            raise ValueError(f"{field} must be an integer from 1 to 1000")
        return value

    @staticmethod
    def _offset(value: object) -> int:
        if isinstance(value, bool) or not isinstance(value, int) or value < 0:
            raise ValueError("offset must be a non-negative integer")
        return value

    def interface_call(self, name: str, arguments: object) -> dict[str, Any]:  # noqa: C901
        """Perform one explicit Workspace/View action with strict backend validation."""
        with self._interface_lock:
            if name == "workspace_open":
                args = self._arguments(name, arguments, {"session_id"}, {"session_id"})
                return self._workspaces.open(args["session_id"])
            if name == "workspace_list":
                self._arguments(name, arguments, set())
                return self._workspaces.list()
            if name == "workspace_get":
                args = self._arguments(name, arguments, {"workspace_id"}, {"workspace_id"})
                return self._workspaces.get(args["workspace_id"])
            if name == "view_create":
                args = self._arguments(name, arguments, {"workspace_id", "position", "name"}, {"workspace_id"})
                return self._workspaces.create(args["workspace_id"], args.get("position", "last"), args.get("name"))
            if name == "view_duplicate":
                args = self._arguments(name, arguments, {"workspace_id", "view_id"}, {"workspace_id", "view_id"})
                return self._workspaces.duplicate(args["workspace_id"], args["view_id"])
            if name == "view_list":
                args = self._arguments(name, arguments, {"workspace_id"}, {"workspace_id"})
                return self._workspaces.list_views(args["workspace_id"])
            if name == "view_get":
                args = self._arguments(name, arguments, {"workspace_id", "view_id"}, {"workspace_id", "view_id"})
                return self._workspaces.get_view(args["workspace_id"], args["view_id"])
            if name == "view_update":
                args = self._arguments(name, arguments, {"workspace_id", "view_id", "sql", "cursor_position", "expected_revision"}, {"workspace_id", "view_id", "sql", "expected_revision"})
                if "cursor_position" in args:
                    WorkspaceStore.cursor(args["cursor_position"])
                return self._workspaces.update(
                    args["workspace_id"], args["view_id"], args["sql"],
                    args["expected_revision"], args.get("cursor_position"),
                )
            if name == "view_run":
                return self._view_run(arguments)
            if name == "view_check":
                args = self._arguments(name, arguments, {"workspace_id", "view_id", "cursor_position"}, {"workspace_id", "view_id"})
                view = self._workspaces.get_view(args["workspace_id"], args["view_id"])
                return {"workspace_id": view["workspace_id"], "view_id": view["view_id"]} | self.check(view["sql"], args.get("cursor_position"))
            if name == "view_fetch":
                return self._view_fetch(arguments)
            if name == "view_focus":
                args = self._arguments(name, arguments, {"workspace_id", "view_id"}, {"workspace_id", "view_id"})
                return self._workspaces.focus(args["workspace_id"], args["view_id"])
            if name == "view_rename":
                args = self._arguments(name, arguments, {"workspace_id", "view_id", "name"}, {"workspace_id", "view_id", "name"})
                return self._workspaces.rename(args["workspace_id"], args["view_id"], args["name"])
            if name == "view_remove":
                args = self._arguments(name, arguments, {"workspace_id", "view_id"}, {"workspace_id", "view_id"})
                response, query_id = self._workspaces.remove(args["workspace_id"], args["view_id"])
                self._unpin_result(query_id)
                return response
            if name == "view_save":
                args = self._arguments(name, arguments, {"workspace_id", "view_id"}, {"workspace_id", "view_id"})
                view = self._workspaces.get_view(args["workspace_id"], args["view_id"])
                return {"workspace_id": view["workspace_id"], "view_id": view["view_id"]} | self.save_view(view["sql"], view.get("name"))
            if name == "query_log_list":
                args = self._arguments(name, arguments, {"limit"})
                return self._query_log.list(args.get("limit", 20))
            if name == "query_log_get":
                args = self._arguments(name, arguments, {"log_id"}, {"log_id"})
                return self._query_log.get(args["log_id"])
            raise ValueError("unknown Workbench interface operation")

    def _view_run(self, arguments: object) -> dict[str, Any]:
        args = self._arguments("view_run", arguments, {"workspace_id", "view_id", "cursor_position", "preview", "save", "name"}, {"workspace_id", "view_id"})
        save = args.get("save", False)
        if type(save) is not bool:
            raise ValueError("save must be a boolean")
        if args.get("name") is not None and not save:
            raise ValueError("name is only supported when save is true")
        preview = QueryStore._preview(args.get("preview"))
        if save:
            SavedQueryStore._name(args.get("name"))
        current = self._workspaces.get_view(args["workspace_id"], args["view_id"])
        selected = select_statement(current["sql"], args.get("cursor_position"))
        view, prior = self._workspaces.clear_result(args["workspace_id"], args["view_id"])
        self._unpin_result(prior)
        self._drop_result(prior)
        try:
            result = self._run_store(selected, preview=preview, include_rows=False)
            metadata = result_metadata(result)
            assert self._store is not None
            self._store.pin(metadata["query_id"])
            saved: dict[str, Any] = {}
            if save:
                try:
                    saved = self._saved_queries.save_query(selected, args.get("name"))
                except ValueError as error:
                    print(f"saved query failed: {error}", file=sys.stderr)
                    saved = {"save_error": str(error)}
        except WorkbenchUnavailableError:
            raise
        except QueryExecutionError as error:
            metadata, saved = failed_metadata(error), {}
        except ValueError as error:
            metadata, saved = failed_metadata(error), {}
        self._log_attempt(selected, metadata)
        self._workspaces.set_result(args["workspace_id"], args["view_id"], metadata)
        return {"workspace_id": view["workspace_id"], "view_id": view["view_id"], "revision": view["revision"]} | metadata | saved

    def _view_fetch(self, arguments: object) -> dict[str, Any]:
        args = self._arguments("view_fetch", arguments, {"workspace_id", "view_id", "offset", "page_size", "preview", "grid", "result_delivery", "result_format"}, {"workspace_id", "view_id"})
        if "grid" in args and not isinstance(args["grid"], dict):
            raise ValueError("grid must be an object")
        validate_delivery(args.get("result_delivery", "file"), args.get("result_format", "json_matrix"))
        view = self._workspaces.get_view(args["workspace_id"], args["view_id"])
        result = view.get("result")
        if not isinstance(result, dict) or result.get("status") != "success" or not isinstance(result.get("query_id"), str):
            raise ValueError("view has no current result")
        page_size = self._limit(args.get("page_size", 100), "page_size")
        preview = QueryStore._preview(args.get("preview"))
        offset = self._offset(args.get("offset", 0))
        self._start()
        assert self._store is not None
        self._store.prune_results()
        page = self._store.page(
            result["query_id"], offset, page_size=page_size,
            preview=preview, grid=args.get("grid"),
        )
        page = deliver(self._store, self._root, page, args.get("result_delivery", "file"), args.get("result_format", "json_matrix"))
        return {"workspace_id": view["workspace_id"], "view_id": view["view_id"]} | page

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
        if self._store is not None:
            self._store.close()
        self._query_log.close()
