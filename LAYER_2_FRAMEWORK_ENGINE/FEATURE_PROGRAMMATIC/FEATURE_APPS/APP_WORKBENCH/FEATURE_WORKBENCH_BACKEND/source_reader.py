# CA-M-1013@1
# CA-R-2723@7
# CA-R-2726@9
# CA-R-3009@2
# CA-M-464@18
# CA-M-465@29
# CA-D-672@24
# CA-R-2725@6
"""Governed Workbench carrier reader; scheduling belongs to the service."""
from __future__ import annotations
import sys
import re
import os
from collections import Counter
from collections.abc import Callable, Iterable
from hashlib import sha256
from itertools import groupby
from pathlib import Path
from typing import Any
from .content_schema import ContentSchema, _is_declaration
from .header_columns import HeaderSchema
from .source_content_schema import SourceContentSchema
from .source_header_schema import SourceHeaderSchema
from .source_rows import (
    ReferenceIndex, atom as source_atom, canonical_row, file_signature, same_row as _same_row,
    scope as source_scope, source_body,
)
from .source_roles import ROLE_MARKERS, CANONICAL_ROLE_MARKERS
from .source_inventory import archived as _archived, group as _group, markdown_paths as _markdown_paths
TOOLS = Path(__file__).resolve().parents[3] / "FEATURE_TOOLS"
for path in (TOOLS.parent, TOOLS):
    if str(path) not in sys.path:
        sys.path.insert(0, str(path))
from carrier_aliases import canonical_role_name, carrier_read_view, named_value_token  # noqa: E402
from project_root_container import effective_root_container_header  # noqa: E402
from project_settings_values import control_root as configured_control_root, project_identity  # noqa: E402
from scope_unit_declarations import (  # noqa: E402
    DELEGATION_ROLE_FOLDERS,
    ScopeDeclarationError,
    _is_projection,
    _selects_declaration_form,
    read_scope_unit_declarations,
)
from VALIDATE_ATOMS.validate_atoms_workers.parsing import (  # noqa: E402
    CarrierError,
    parse_carrier,
)
from VALIDATE_ATOMS.validate_atoms_workers.read_io import ReadContext, open_regular  # noqa: E402
from VALIDATE_ATOMS.validate_atoms_workers.settings import CEILINGS  # noqa: E402
class SourceReader:
    def __init__(
        self, root: Path, control_root: Path | None = None, *, schema_mode: int = 2,
        compiled_schema: tuple[ContentSchema, HeaderSchema] | None = None,
        status_groups: tuple[tuple[str, str, str], ...] = (),
        role_folders: tuple[tuple[str, str], ...] | None = None,
        include_archived: bool = True,
        archive_placement: Any | None = None,
        audit_model: Any | None = None,
    ) -> None:
        if type(schema_mode) is not int or schema_mode not in {1, 2}:
            raise ValueError("workbench.schema_mode must be 1 or 2")
        self.root = Path(root).resolve()
        self._schema_mode = schema_mode
        self._status_groups = status_groups
        self._role_folders = role_folders
        self._lifecycle_role_markers = {
            folder: CANONICAL_ROLE_MARKERS.get(role, {role[0].upper()})
            for role, folder in role_folders or ()
        } or ROLE_MARKERS
        self._lifecycle_scopes: dict[Path, dict[str, Any]] = {}
        self._include_archived = include_archived
        self._archive_placement = archive_placement
        self._declared_archive_roots: set[Path] = set()
        self._retain_parsed = compiled_schema is not None
        self._audit_model = audit_model
        if control_root is None:
            self.control_root = configured_control_root(self.root)
        else:
            candidate = Path(control_root)
            self.control_root = (
                candidate if candidate.is_absolute() else self.root / candidate
            ).resolve()
        self._failed: dict[Path, tuple[int, ...]] = {}
        self._diagnostics: dict[Path, str] = {}
        self._cached: dict[Path, tuple[tuple[int, ...], dict[str, Any]]] = {}
        self._declarations: Any | None = None
        self._atom_filename: re.Pattern[str] | None = None
        self._declaration_paths: set[Path] = set()
        self._project_root_declaration: tuple[Path, str] | None = None
        self._declaration_directories: set[Path] = set()
        self._scope_authority_boundaries: set[Path] = set()
        self._source_paths: set[Path] = set()
        self._catalog = None
        self._archive_paths: set[Path] = set()
        self._archives_by_id: dict[str, set[Path]] = {}
        self._identity_prefix = ""
        self._filename_ids: dict[Path, tuple[str, str]] = {}
        self._role_ids: dict[str, Counter[int]] = {}
        self._role_max: dict[str, int] = {}
        self._identity_pattern: re.Pattern[str] | None = None
        self._loaded_archive_folders: set[Path] = set()
        self._loaded_archive_files: set[Path] = set()
        self._references = ReferenceIndex()
        self._inventory_ready = False
        self._compiled_schema = compiled_schema
        self._content_schema = SourceContentSchema(compiled_schema[0] if compiled_schema else None)
        self._header_schema = SourceHeaderSchema(compiled_schema[1] if compiled_schema else None)
        self._observed_header_schema: HeaderSchema | None = None
        self._content_invalid: set[Path] = set()
        self._header_invalid: set[Path] = set()
        self.excluded_count = 0
        self.capture_changed = True
        self.capture_delta: dict[str, dict[str, Any] | None] | None = None
        self.audit_delta: set[str] | None = None
    @property
    def content_schema(self) -> ContentSchema | None:
        return self._content_schema.schema
    @property
    def header_schema(self) -> HeaderSchema | None:
        return self._header_schema.schema
    def archive_catalog(self) -> tuple[str, ...]:
        """Return known Archive carrier paths without reading their content."""
        paths = self._catalog.paths(archived=True) if self._catalog else self._archive_paths
        return tuple(sorted(path.relative_to(self.root).as_posix() for path in paths))

    def archive_reservations(self, atom_id: str, *, unloaded_only: bool = False) -> tuple[tuple[str, int | None, str], ...]:
        """Find known Archive candidates for one Atom using filenames only."""
        result = []
        marker = re.compile(r"^(?:[1-9][0-9]*-)?" + re.escape(atom_id) + r"(?:@([1-9][0-9]*))?(?=[_.-]|$)")
        paths = self._catalog.paths(atom_id=atom_id, archived=True) if self._catalog else self._archives_by_id.get(atom_id, ())
        for path in paths:
            if self._lifecycle_owner(path, atom_id.rsplit("-", 2)[-2]) is None:
                continue
            if unloaded_only and path in self._source_paths:
                continue
            match = marker.match(path.name)
            if match is None:
                continue
            suffix = re.search(r"@([1-9][0-9]*)\.md$", path.name)
            version = match.group(1) or (suffix.group(1) if suffix else None)
            result.append((atom_id, int(version) if version else None, path.relative_to(self.root).as_posix()))
        return tuple(sorted(result, key=lambda item: item[2]))

    def _remember_archive(self, path: Path) -> None:
        if self._catalog:
            self._catalog_remember(path, True)
            return
        self._archive_paths.add(path)
        match = self._identity_pattern.match(path.name) if self._identity_pattern else None
        if match:
            atom_id = f"{self._identity_prefix}-{match.group(1)}-{match.group(2)}"
            self._archives_by_id.setdefault(atom_id, set()).add(path)

    def _forget_archive(self, path: Path) -> None:
        if self._catalog:
            return
        self._archive_paths.discard(path)
        identity = self._filename_ids.get(path)
        if identity is not None:
            atom_id = f"{self._identity_prefix}-{identity[0]}-{identity[1]}"
            paths = self._archives_by_id.get(atom_id)
            if paths is not None:
                paths.discard(path)
                if not paths:
                    del self._archives_by_id[atom_id]

    def _archive_path(self, path: Path) -> bool:
        parts = path.relative_to(self.control_root).parts
        return (_archived(tuple(part for part in parts if part.casefold() != "_projection"))
                or any(parent in self._declared_archive_roots for parent in path.parents))

    def max_atom_number(self, role_marker: str, *, ceiling: int | None = None) -> int:
        """Return the largest in-range filename number, including unloaded Archives."""
        role = role_marker.upper()
        if self._catalog:
            return self._catalog.max_number(role, ceiling)
        greatest = self._role_max.get(role, 0)
        if ceiling is None or greatest <= ceiling:
            return greatest
        return max((number for number in self._role_ids[role] if number <= ceiling), default=0)

    def _catalog_remember(self, path: Path, archived: bool) -> None:
        match = self._identity_pattern.match(path.name) if self._identity_pattern else None
        if not match or self._lifecycle_owner(path, match.group(1)) is None:
            return
        role, digits = match.groups()
        identity = f"{self._identity_prefix}-{role}-{digits}"
        marker = re.match(r"^(?:[1-9][0-9]*-)?" + re.escape(identity) + r"(?:@([1-9][0-9]*))?(?=[_.-]|$)", path.name)
        suffix = re.search(r"@([1-9][0-9]*)\.md$", path.name)
        version = (marker.group(1) if marker else None) or (suffix.group(1) if suffix else None)
        self._catalog.remember(path, (identity, role, str(int(digits))), version, archived)

    def _remember_filename(self, path: Path) -> None:
        if self._catalog:
            self._catalog_remember(path, self._archive_path(path))
            return
        if path in self._filename_ids or self._identity_pattern is None:
            return
        match = self._identity_pattern.match(path.name)
        if match is None:
            return
        role, digits = match.group(1), match.group(2)
        if self._lifecycle_owner(path, role) is None:
            return
        number = int(digits)
        self._filename_ids[path] = (role, digits)
        self._role_ids.setdefault(role, Counter())[number] += 1
        self._role_max[role] = max(number, self._role_max.get(role, 0))

    def _forget_filename(self, path: Path) -> None:
        if self._catalog:
            self._catalog.remove(path)
            return
        identity = self._filename_ids.pop(path, None)
        if identity is None:
            return
        role, digits = identity
        number = int(digits)
        counts = self._role_ids[role]
        counts[number] -= 1
        if not counts[number]:
            del counts[number]
        if self._role_max[role] == number and number not in counts:
            self._role_max[role] = max(counts, default=0)

    def load_archive_folder(self, relative: str) -> list[dict[str, str | None]]:
        """Register and inventory one Archive folder."""
        return self.load_archive_folders((relative,))

    def load_archive_folders(self, relatives: Iterable[str]) -> list[dict[str, str | None]]:
        """Validate all requested folders before registering or inventorying any of them."""
        folders = set()
        for relative in relatives:
            folder = self._change_path(relative)
            if folder is None or not folder.is_relative_to(self.control_root) or self._has_symlink_ancestor(folder):
                raise ValueError("Archive folder must be inside the Project authority folder")
            if folder.exists() and not folder.is_dir():
                raise ValueError("Archive folder is not a directory")
            folders.add(folder)
        candidates = {path for folder in folders for path in _markdown_paths(folder) if self._is_source_path(path)}
        self._loaded_archive_folders.update(folders)
        for path in candidates:
            if self._catalog:
                self._catalog_remember(path, True)
            else:
                self._remember_filename(path)
                self._remember_archive(path)
        return self._archive_load_changes(candidates)

    def unload_archive_folder(self, relative: str) -> None:
        """Forget an invalidated loaded root; the caller must perform a full capture."""
        folder = self._change_path(relative)
        if folder is None or not folder.is_relative_to(self.control_root):
            raise ValueError("Archive folder must be inside the Project authority folder")
        self._loaded_archive_folders = {root for root in self._loaded_archive_folders if not root.is_relative_to(folder)}
        self._loaded_archive_files = {path for path in self._loaded_archive_files if not path.is_relative_to(folder)}

    def load_archive_file(self, relative: str) -> list[dict[str, str | None]]:
        """Register one known Archive carrier for the next incremental capture."""
        path = self._change_path(relative)
        if path is None or not self._is_source_path(path):
            raise ValueError("Unknown Archive carrier")
        if not self._known_archive(path):
            if not self._archive_path(path) or not path.is_file():
                raise ValueError("Unknown Archive carrier")
            self._remember_filename(path)
            self._remember_archive(path)
        self._loaded_archive_files.add(path)
        return self._archive_load_changes((path,))

    def _archive_load_changes(self, paths: Iterable[Path]) -> list[dict[str, str | None]]:
        return [{"operation": "create", "new_path": path.relative_to(self.root).as_posix(), "old_path": None}
                for path in sorted(paths) if path not in self._source_paths]

    def _known_archive(self, path: Path) -> bool:
        return path in (self._catalog.paths(archived=True, under=path) if self._catalog else self._archive_paths)

    def _archive_selected(self, path: Path) -> bool:
        return (self._include_archived or path in self._loaded_archive_files
                or any(path.is_relative_to(folder) for folder in self._loaded_archive_folders))

    def set_observed_header_schema(self, schema: HeaderSchema) -> None:
        """Retain the Mode 2 Header shape observed during this owner's cold start."""
        self._observed_header_schema = schema
    def release_cache(self) -> None:
        """Release parsed successful rows while retaining failed signatures."""
        self._cached.clear()
        self._references.rebuild({})
        self._inventory_ready = False
        if self._compiled_schema is None:
            self._content_schema.reset()
            self._header_schema.reset()
        self._content_invalid.clear()
        self._header_invalid.clear()
        self.capture_changed = True
        self.capture_delta = None
        self.audit_delta = None
    def capture(
        self, changes: list[dict[str, str | None]] | None = None,
    ) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
        self.excluded_count = 0
        reader = ReadContext(roots=[str(self.root)], limits=dict(CEILINGS))
        if (
            changes is None
            or not self._inventory_ready
            or self._declarations is None
            or self._declarations_changed(changes, reader)
        ):
            return self._capture_full(reader)
        previous: dict[Path, tuple[tuple[int, ...], dict[str, Any]]] = {}
        affected = self._apply_changes(changes, previous)
        for path in sorted(affected):
            if path in self._source_paths:
                self._refresh_path(path, reader)
        affected.update(self._prune_missing_reference_aliases(affected, previous))
        content_paths = self._references.update(
            {path: item[1] for path, item in previous.items()}, self._cached_row, affected,
        )
        if self._compiled_schema is None and self._update_content_bindings(content_paths):
            return self._capture_full(reader, revalidate_content=True)
        before_validation = {path: self._cached_row(path) for path in content_paths}
        invalid = self._exclude_invalid_content_sources({
            path.relative_to(self.root).as_posix(): self._cached.get(path, (None, None))[1]
            for path in content_paths
        })
        if invalid:
            content_paths |= self._references.update(before_validation, self._cached_row, invalid)
            if self._compiled_schema is None and self._update_content_bindings(content_paths):
                return self._capture_full(reader, revalidate_content=True)
        if self._compiled_schema is None:
            header_rows = self._accepted_updates(affected | content_paths)
            header_changed = self._header_schema.update(
                {path: ({**row, "_model_class_bindings": self._content_schema._bindings} if row is not None else None)
                 for path, row in header_rows.items()}, accept_shape=self._schema_mode == 2,
            )
            if header_changed and self._schema_mode == 1:
                return self._capture_full(reader)
        before_validation = {path: self._cached_row(path) for path in affected | content_paths}
        invalid = self._exclude_invalid_header_sources([
            row for path in affected | content_paths
            if (row := self._cached.get(path, (None, None))[1]) is not None
        ])
        if invalid:
            content_paths |= self._references.update(before_validation, self._cached_row, invalid)
            if self._compiled_schema is None and self._content_schema.update(self._accepted_updates(content_paths)):
                return self._capture_full(reader, revalidate_content=True)
        self.capture_delta = {
            path.relative_to(self.root).as_posix(): self._cached.get(path, (None, None))[1]
            for path in affected | content_paths
        }
        self.audit_delta = {
            path.relative_to(self.root).as_posix() for path in affected | content_paths | invalid
        }
        self.excluded_count = len(self._failed)
        self.capture_changed = any(
            not _same_row(previous.get(path), self._cached.get(path))
            for path in affected
        )
        return self._rows(), self._scopes()
    def _accepted_updates(self, paths):
        accepted = self._references.accepted_paths(paths)
        return {path.relative_to(self.root).as_posix(): self._cached_row(path) if path in accepted else None
                for path in paths}

    def _update_content_bindings(self, paths):
        prior = dict(self._content_schema._bindings)
        return self._content_schema.update(self._accepted_updates(paths)) or prior != self._content_schema._bindings

    def _prune_missing_reference_aliases(
        self, affected: set[Path], previous: dict[Path, tuple[tuple[int, ...], dict[str, Any]]],
    ) -> set[Path]:
        """Drop a cached path that disappeared before its move event arrived."""
        references = {
            row["ref"]
            for path in affected
            if (row := self._cached.get(path, (None, None))[1]) is not None
            and isinstance(row.get("ref"), str)
        }
        removed: set[Path] = set()
        for paths in self._references.paths_by_reference(references).values():
            for path in paths:
                if path not in affected and file_signature(path) is None:
                    if path in self._cached:
                        previous.setdefault(path, self._cached[path])
                    removed.update(self._remove_paths(path))
        return removed
    def _capture_full(
        self, reader: ReadContext, *, revalidate_content: bool = False,
    ) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
        self.capture_changed = True
        self.capture_delta = None
        self.audit_delta = None
        try:
            declarations = read_scope_unit_declarations(
                self.root, self.control_root, reader=reader
            )
        except ScopeDeclarationError as error:
            self._error(self.root, error)
            raise
        self._declarations = declarations
        self._lifecycle_scopes = {self.root / row["authority_path"]: row
                                  for row in declarations.as_structure()["scope_units"]}
        prefix, project_name = project_identity(self.root, control_relative=self.control_root.relative_to(self.root))
        root_declaration = None
        if declarations.root.name == project_name:
            root_path = declarations.root.source
            root_pin = declarations.source_pins[root_path.relative_to(self.root).as_posix()]
            root_declaration = (root_path, root_pin["sha256"])
        if root_declaration != self._project_root_declaration:
            for identity in (self._project_root_declaration, root_declaration):
                if identity is not None:
                    self._cached.pop(identity[0], None)
            self._project_root_declaration = root_declaration
        self._project_scope_id = f"{prefix.upper()}-SU-00"
        self._atom_filename = re.compile(rf"(?:[1-9][0-9]*-)?{re.escape(prefix)}-[A-Z]-.*\.md")
        self._identity_prefix = prefix
        self._identity_pattern = re.compile(rf"^(?:[1-9][0-9]*-)?{re.escape(prefix)}-([A-Z])-([0-9]+)(?=[@_.-]|$)")
        self._declaration_paths = {Path(path).resolve() for path in declarations.paths}
        self._declaration_directories = {self.control_root}
        self._scope_authority_boundaries = set()
        self._declared_archive_roots = set()
        archive_folders = self._declared_archive_folders()
        for row in declarations.as_structure()["scope_units"]:
            authority = self.root / row["authority_path"]
            self._declared_archive_roots.update(authority / folder for folder in archive_folders)
            self._declaration_directories.update(authority / role for role in DELEGATION_ROLE_FOLDERS)
            while authority.is_relative_to(self.control_root):
                self._scope_authority_boundaries.add(authority)
                if authority == self.control_root:
                    break
                authority = authority.parent
        self._source_paths = set(self._inventory_paths())
        self._inventory_ready = True
        if revalidate_content:
            for path in self._content_invalid:
                self._failed.pop(path, None)
        self._failed = {
            path: signature
            for path, signature in self._failed.items()
            if path in self._source_paths
        }
        self._diagnostics = {
            path: message for path, message in self._diagnostics.items() if path in self._source_paths
        }
        self._cached = {
            path: cached
            for path, cached in self._cached.items()
            if path in self._source_paths
        }
        self._refresh_inventory(reader)
        self._references.rebuild(self._cached_rows())
        self._rebuild_content_schema(revalidated=revalidate_content)
        self._rebuild_header_schema()
        while self._exclude_invalid_header_sources():
            self._references.rebuild(self._cached_rows())
            self._rebuild_content_schema(revalidated=revalidate_content)
            self._rebuild_header_schema()
        self.excluded_count = len(self._failed)
        return self._rows(), self._scopes()

    def _declared_archive_folders(self) -> list[Path]:
        if self._archive_placement is None:
            return []
        folders = []
        for role in self._archive_placement.role_folders:
            try:
                role_folder = self._archive_placement.role_folder(role)
                archived = self._archive_placement.archive_folders(role)
            except ValueError:
                continue
            folders.extend(Path(role_folder) / name for name in archived)
        return folders
    def _refresh_inventory(self, reader: ReadContext) -> None:
        ordered = sorted(self._source_paths, key=lambda path: (path.parent, path.name))
        for directory, paths in groupby(ordered, key=lambda path: path.parent):
            try:
                descriptor = open_regular(directory, directory=True)
            except OSError:
                descriptor = None
            try:
                for path in paths:
                    self._refresh_path(path, reader, directory_fd=descriptor)
            finally:
                if descriptor is not None:
                    os.close(descriptor)
    def _declarations_changed(
        self, changes: list[dict[str, str | None]], reader: ReadContext,
    ) -> bool:
        for change in changes:
            old = self._change_path(change.get("old_path"))
            new = self._change_path(change.get("new_path"))
            if change.get("operation") in {"remove", "move", "rename"} and old in self._scope_authority_boundaries:
                return True
            if self._touches_declaration(old) or self._touches_declaration(new):
                return True
            if new is not None and self._is_declaration_candidate(new, reader):
                return True
        return False
    def _touches_declaration(self, path: Path | None) -> bool:
        return path is not None and any(
            declaration == path or declaration.is_relative_to(path)
            for declaration in self._declaration_paths
        )
    def _is_declaration_candidate(self, path: Path, reader: ReadContext) -> bool:
        if (
            path.suffix != ".md"
            or path.parent not in self._declaration_directories
            or (path.parent == self.control_root and not path.name.startswith("CA-R-"))
            or self._has_symlink_ancestor(path)
        ):
            return False
        try:
            raw = reader.read(path)
        except (OSError, RuntimeError):
            return False
        return _selects_declaration_form(raw) and not _is_projection(raw)
    def _apply_changes(
        self, changes: list[dict[str, str | None]],
        previous: dict[Path, tuple[tuple[int, ...], dict[str, Any]]],
    ) -> set[Path]:
        affected: set[Path] = set()
        for change in changes:
            old = self._change_path(change.get("old_path"))
            new = self._change_path(change.get("new_path"))
            for path in (old, new):
                if path is None:
                    continue
                candidates = (path,) if path.suffix == ".md" else (
                    source for source in self._source_paths if source.is_relative_to(path)
                )
                for source in candidates:
                    if source in self._cached:
                        previous.setdefault(source, self._cached[source])
            if old is not None:
                affected.update(self._remove_paths(old))
            if new is not None:
                if self._has_symlink_ancestor(new):
                    affected.update(self._remove_paths(new))
                else:
                    affected.update(self._add_paths(new))
        return affected
    def _change_path(self, value: str | None) -> Path | None:
        if value is None:
            return None
        relative = Path(value)
        if relative.is_absolute() or ".." in relative.parts:
            return None
        return self.root / relative
    def _remove_paths(self, path: Path) -> set[Path]:
        if path.suffix == ".md":
            removed = {path} if path in self._source_paths else set()
        else:
            removed = {
                source for source in self._source_paths if source.is_relative_to(path)
            }
        if path.suffix == ".md":
            self._forget_archive(path)
            self._forget_filename(path)
        elif self._catalog:
            self._catalog.remove(path)
        else:
            for source in tuple(self._filename_ids):
                if source.is_relative_to(path):
                    self._forget_archive(source)
                    self._forget_filename(source)
        for source in removed:
            self._source_paths.remove(source)
            self._cached.pop(source, None)
            self._failed.pop(source, None)
            self._diagnostics.pop(source, None)
            self._content_invalid.discard(source)
            self._header_invalid.discard(source)
        return removed
    def _add_paths(self, path: Path) -> set[Path]:
        if path.suffix == ".md":
            candidates = {path} if self._is_source_path(path) else set()
        elif path.is_dir():
            candidates = {candidate for candidate in _markdown_paths(path) if self._is_source_path(candidate)}
        else:
            candidates = set()
        added = set()
        for candidate in candidates:
            is_archive = self._archive_path(candidate) or (not self._catalog and self._known_archive(candidate)) or any(
                candidate.is_relative_to(folder) for folder in self._loaded_archive_folders
            )
            if self._catalog:
                self._catalog_remember(candidate, is_archive)
            else:
                self._remember_filename(candidate)
                if is_archive:
                    self._remember_archive(candidate)
            if not is_archive or self._archive_selected(candidate):
                added.add(candidate)
        self._source_paths.update(added)
        return added
    def _is_source_path(self, path: Path) -> bool:
        if self._atom_filename is None or not self._atom_filename.fullmatch(path.name) or not path.is_relative_to(self.control_root):
            return False
        return not self._has_symlink_ancestor(path)
    def _has_symlink_ancestor(self, path: Path) -> bool:
        if not path.is_relative_to(self.control_root):
            return True
        current = path
        while current != self.control_root:
            if current.is_symlink():
                return True
            current = current.parent
        return self.control_root.is_symlink()
    def _rebuild_content_schema(self, *, revalidated: bool = False) -> None:
        if self._retain_parsed:
            return
        if revalidated:
            self._content_invalid.clear()
        else:
            self._content_invalid.intersection_update(self._source_paths)
        if self._compiled_schema is not None:
            while self._exclude_content_errors(
                self._content_schema.validation_errors(
                    row for row in self._cached_rows().values() if row.get("status_group") != "Archived"
                )
            ):
                self._references.rebuild(self._cached_rows())
            return
        while True:
            errors = self._content_schema.rebuild(
                row for row in self._accepted_rows() if row.get("status_group") != "Archived"
            )
            errors.update(self._content_schema.validation_errors(
                row for row in self._cached_rows().values() if row.get("status_group") != "Archived"
            ))
            if not self._exclude_content_errors(errors):
                return
            self._references.rebuild(self._cached_rows())
    def _rebuild_header_schema(self) -> None:
        if self._compiled_schema is None:
            self._header_schema.rebuild({**row, "_model_class_bindings": self._content_schema._bindings} for row in self._accepted_rows())
    def _exclude_invalid_header_sources(self, rows: Iterable[dict[str, Any]] | None = None) -> set[Path]:
        if self._retain_parsed:
            return set()
        schema = self.header_schema if self._schema_mode == 1 else self._observed_header_schema
        if schema is None:
            return set()
        candidates = self._cached_rows().values() if rows is None else rows
        errors = self._header_schema.validation_errors(
            [row for row in candidates if row.get("status_group") != "Archived"], schema=schema
        )
        removed = set()
        for relative, error in errors.items():
            path = self.root / relative
            cached = self._cached.get(path)
            if self._compiled_schema is None and cached is not None and _is_declaration(cached[1]):
                raise ValueError(f"{relative}: {error}")
            if cached is not None:
                self._cached.pop(path)
                self._failed[path] = cached[0]
                self._header_invalid.add(path)
                self._error(path, error)
                removed.add(path)
        return removed
    def _exclude_invalid_content_sources(
        self, rows: dict[str, dict[str, Any] | None],
    ) -> set[Path]:
        if self._retain_parsed:
            return set()
        return self._exclude_content_errors(self._content_schema.validation_errors(
            row for row in rows.values() if row is not None and row.get("status_group") != "Archived"
        ))
    def _exclude_content_errors(self, errors: dict[str, ValueError]) -> set[Path]:
        removed = set()
        for relative, error in errors.items():
            path = self.root / relative
            cached = self._cached.pop(path, None)
            if cached is not None:
                removed.add(path)
                self._failed[path] = cached[0]
                self._content_invalid.add(path)
                self._error(path, error)
        return removed
    def _refresh_path(self, path: Path, reader: ReadContext, *, directory_fd: int | None = None) -> None:
        signature = file_signature(path)
        if signature is None:
            self._cached.pop(path, None)
            self._failed.pop(path, None)
            self._diagnostics.pop(path, None)
            self._content_invalid.discard(path)
            self._header_invalid.discard(path)
            self._source_paths.discard(path)
            return
        if self._failed.get(path) == signature:
            self._cached.pop(path, None)
            return
        cached = self._cached.get(path)
        if cached is not None and cached[0] == signature:
            return
        self._cached.pop(path, None)
        self._read_source(path, signature, reader, directory_fd=directory_fd)
    def _lifecycle_owner(self, path: Path, marker: str):
        if "_projection" in path.parts:
            return None
        for authority in path.parents:
            if (owner := self._lifecycle_scopes.get(authority)) is not None:
                parts = path.relative_to(authority).parts
                if len(parts) >= 2 and marker in self._lifecycle_role_markers.get(parts[0], ()):
                    return owner
                break
        return None

    def lifecycle_eligible(self, path: Path) -> bool:
        """Check an indexed carrier against its declared owning Scope Unit and role."""
        cached = self._cached.get(path)
        if cached is None or self._declarations is None:
            return False
        row = cached[1]
        view = carrier_read_view(row["header_json"])
        if view.get("projection"):
            return False
        role = named_value_token(canonical_role_name(row.get("role") or view.get("role")))
        if self._identity_pattern is None or (identity := self._identity_pattern.match(path.name)) is None:
            return False
        marker = identity[1]
        if not any(marker in markers and role == named_value_token(name)
                   for name, markers in CANONICAL_ROLE_MARKERS.items()):
            return False
        owner = self._lifecycle_owner(path, marker)
        if owner is None:
            return False
        container = view.get("container")
        if isinstance(container, dict):
            scope_id = container.get("scope_unit")
            if isinstance(scope_id, str):
                if scope_id not in {owner["scope_unit_name"], owner["scope_unit_id"] or self._project_scope_id}:
                    return False
            elif isinstance(parent := container.get("atom"), str):
                parents = self._references.paths_for(parent)
                if parents and not any(
                    self._lifecycle_owner(candidate, parent.rsplit("-", 2)[-2]) == owner
                    for candidate in parents if len(parent.rsplit("-", 2)) == 3
                ):
                    return False
        return True

    def _rows(self) -> list[dict[str, Any]]:
        return [
            self._cached[path][1]
            for path in sorted(self._source_paths)
            if path in self._cached
        ]
    def model_rows(self, observed, predicate: Callable[[dict[str, Any]], bool]) -> list[dict[str, Any]]:
        """Prefer Current Scope Unit sources over copies when building model assets."""
        assert self._declarations is not None
        authority = [
            self.root / row["authority_path"]
            for row in self._declarations.as_structure()["scope_units"]
            if self.root / row["authority_path"] != self.control_root
        ]
        rows = [
            row for path, (_, row) in sorted(self._cached.items())
            if row.get("status_group") == "Current"
            and "_projection" not in path.relative_to(self.control_root).parts
            and any(path.is_relative_to(directory) for directory in authority)
        ]
        # Other Current rows suppress obsolete copies even when their form changed.
        errors = self._content_schema.validation_errors(row for row in rows if predicate(row))
        references = {row.get("ref") for row in rows if row.get("ref") is not None}
        return ([row for row in rows if row.get("source_path") not in errors]
                + [row for row in observed if row.get("ref") not in references])
    def _cached_row(self, path: Path) -> dict[str, Any] | None:
        return self._cached.get(path, (None, None))[1]
    def _cached_rows(
        self, cached: dict[Path, tuple[tuple[int, ...], dict[str, Any]]] | None = None,
    ) -> dict[Path, dict[str, Any]]:
        return {path: item[1] for path, item in (self._cached if cached is None else cached).items()}
    def _accepted_rows(self) -> list[dict[str, Any]]:
        return [self._cached[path][1] for path in sorted(self._references.accepted_paths()) if path in self._cached]
    def _scopes(self) -> list[dict[str, Any]]:
        assert self._declarations is not None
        rows = [
            source_scope(item, self.root)
            for item in (self._declarations.root, *self._declarations.units)
        ]
        rows[0]["scope_unit_id"] = self._project_scope_id
        return rows
    def _read_source(
        self, path: Path, signature: tuple[int, ...], reader: ReadContext, *, directory_fd: int | None = None,
    ) -> dict[str, Any] | None:
        try:
            raw = reader.read(path, remember=False, directory_fd=directory_fd)
        except (OSError, RuntimeError) as error:
            self._cached.pop(path, None)
            self._failed[path] = signature
            self.excluded_count += 1
            self._error(path, error)
            return None
        parsed = None
        try:
            parsed = parse_carrier(raw, path)
            view = parsed._view
            assert view is not None
            group = _group(path.relative_to(self.root), view, self._status_groups)
            if (self._archive_path(path) or any(
                path.is_relative_to(folder) for folder in self._loaded_archive_folders
            )):
                group = "Archived"
            if group == "Archived":
                if not self._catalog or not self._archive_path(path):
                    self._remember_archive(path)
            else:
                self._forget_archive(path)
            if group is None or (group == "Archived" and not self._archive_selected(path)):
                self._source_paths.discard(path)
                self._cached.pop(path, None)
                self._failed.pop(path, None)
                self._diagnostics.pop(path, None)
                return None
            row = source_atom(
                path,
                self.root,
                parsed.metadata,
                view,
                source_body(raw, path),
                group,
            )
            root_identity = self._project_root_declaration
            if group == "Current" and root_identity is not None and path == root_identity[0]:
                assert self._declarations is not None
                pin = self._declarations.source_pins[row["source_path"]]
                if sha256(raw).hexdigest() == root_identity[1]:
                    row["_project_root_header"] = effective_root_container_header(
                        parsed.metadata, path=path, raw=raw,
                        root_declaration_path=root_identity[0], root_declaration_pin=pin,
                    )
            if self._retain_parsed:
                row["_retain_parsed"] = True
            canonical_row(row)
        except (OSError, RuntimeError, TypeError, ValueError, CarrierError) as error:
            if parsed is not None and self._retain_parsed:
                group = _group(path.relative_to(self.root), {}, self._status_groups)
                row = source_atom(path, self.root, {}, {}, b"", group)
                row["_source_schema_error"] = str(error)
                self._cached[path] = (signature, row)
                self._failed.pop(path, None)
                self._diagnostics.pop(path, None)
                return row
            self._cached.pop(path, None)
            self._failed[path] = signature
            self._content_invalid.discard(path)
            self._header_invalid.discard(path)
            self.excluded_count += 1
            self._error(path, error)
            return None
        self._failed.pop(path, None)
        self._diagnostics.pop(path, None)
        self._header_invalid.discard(path)
        self._cached[path] = (signature, row)
        return row
    def _inventory_paths(self) -> set[Path]:
        sources = set()
        archives = set()
        self._filename_ids.clear()
        self._archives_by_id.clear()
        self._role_ids.clear()
        self._role_max.clear()
        if self._catalog:
            self._catalog.begin()
        if self._atom_filename is None or self.control_root.is_symlink():
            return sources
        directory = None
        archived_directory = False
        for path in _markdown_paths(self.control_root):
            # The walk already excludes symlink files and directories.
            if not self._atom_filename.fullmatch(path.name):
                continue
            if path.parent != directory:
                directory = path.parent
                archived_directory = self._archive_path(path) or any(
                    directory.is_relative_to(folder) for folder in self._loaded_archive_folders
                )
            if self._catalog:
                self._catalog_remember(path, archived_directory)
            else:
                self._remember_filename(path)
                if archived_directory or path in self._archive_paths:
                    archives.add(path)
                    self._remember_archive(path)
            if not (archived_directory or path in archives) or self._archive_selected(path):
                sources.add(path)
        if self._catalog:
            self._catalog.finish()
        else:
            self._archive_paths = archives
        return sources
    def _error(self, path: Path, error: BaseException) -> None:
        if path in self._source_paths:
            self._diagnostics[path] = str(error)
        print(f"source-reader: {path}: {error}", file=sys.stderr)
def capture_inventory(
    root: Path, control_root: Path | None = None
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    return SourceReader(root, control_root).capture()
