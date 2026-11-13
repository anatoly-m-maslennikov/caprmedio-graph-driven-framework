"""Workbench lifecycle operations."""
from __future__ import annotations
import json
import os
import stat
from pathlib import Path
from typing import Any
from .source_roles import CANONICAL_ROLE_MARKERS
from carrier_aliases import canonical_role_name, named_value_token
from ATOM_LIFECYCLE.source import ArchiveNotLoadedError


class ServiceLifecycle:
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
                    names = dict.fromkeys((*folders, "archive", "archived"))
                    self._archive_folders[name, role] = tuple((root / folder).as_posix() for folder in names)
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
        with self._refresh_lock:
            if requested:
                self._load_fresh_archive_matches(requested)
            rows = self._store.lifecycle_candidates(
                atom_ids=atom_ids, references=references, prefix=prefix, under=relative,
            )
            rows = [row for row in rows if self._reader.lifecycle_eligible(self._root / row[1] / row[2])]
            if requested:
                self._check_archive_lookup(requested, rows)
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
            rows = [row for row in rows if self._reader.lifecycle_eligible(self._root / row[1] / row[2])]
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
                if not self._reader.lifecycle_eligible(path):
                    continue
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

    def _lifecycle_eligible_parts(self, directory, filename):
        return self._reader.lifecycle_eligible(self._root / directory / filename)

    def lifecycle_last_id(self, selection, prefix: str, *, ceiling: int | None = None) -> str | None:
        self._check_lifecycle_project(selection)
        self._flush_lifecycle_changes()
        assert self._store is not None
        with self._refresh_lock:
            current = self._store.lifecycle_last_id(prefix, ceiling=ceiling, eligible=self._lifecycle_eligible_parts)
            reserved = self._reader.max_atom_number(prefix.rsplit("-", 2)[-2], ceiling=ceiling)
        number = max(reserved, int(current[len(prefix):]) if current is not None else 0)
        return f"{prefix}{number}" if number else None

    def lifecycle_latest_version(self, selection, atom_id: str) -> int | None:
        self._check_lifecycle_project(selection)
        self._flush_lifecycle_changes()
        assert self._store is not None
        with self._refresh_lock:
            self._archive_layout()
            unloaded, unknown = self._reader._catalog.unloaded_version_max(
                atom_id, self._reader._source_paths, self._archive_roots,
            )
            if unknown:
                raise ArchiveNotLoadedError(f"Load the Archive Scope Unit and Role for {atom_id} before allocating its next Version.")
            latest = self._store.lifecycle_latest_version(atom_id, eligible=self._lifecycle_eligible_parts)
            return max(latest or 0, unloaded or 0) or None

