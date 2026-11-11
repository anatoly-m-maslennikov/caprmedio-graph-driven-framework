# CA-R-2723@5
# CA-R-2726@6
# CA-R-3009@2
# CA-M-464@15
# CA-M-465@24
# CA-D-672@19
"""Governed Workbench carrier reader; scheduling belongs to the service."""
from __future__ import annotations
import sys
import re
from collections.abc import Callable, Iterable
from pathlib import Path
from typing import Any
from .content_schema import ContentSchema, _is_declaration
from .audit_tables import collect_issues
from .header_columns import HeaderSchema
from .source_content_schema import SourceContentSchema
from .source_header_schema import SourceHeaderSchema
from .source_rows import (
    ReferenceIndex, atom as source_atom, canonical_row, file_signature, same_row as _same_row,
    scope as source_scope, source_body,
)
from .source_inventory import (
    archived as _archived, group as _group, markdown_paths as _markdown_paths,
)
TOOLS = Path(__file__).resolve().parents[3] / "FEATURE_TOOLS"
if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))
from project_settings_values import control_root as configured_control_root, project_identity_prefix  # noqa: E402
from carrier_aliases import carrier_read_view  # noqa: E402
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
from VALIDATE_ATOMS.validate_atoms_workers.read_io import ReadContext  # noqa: E402
from VALIDATE_ATOMS.validate_atoms_workers.settings import CEILINGS  # noqa: E402
class SourceReader:
    def __init__(
        self, root: Path, control_root: Path | None = None, *, schema_mode: int = 2,
        compiled_schema: tuple[ContentSchema, HeaderSchema] | None = None,
        status_groups: tuple[tuple[str, str, str], ...] = (),
        role_folders: tuple[tuple[str, str], ...] | None = None,
    ) -> None:
        if type(schema_mode) is not int or schema_mode not in {1, 2}:
            raise ValueError("workbench.schema_mode must be 1 or 2")
        self.root = Path(root).resolve()
        self._schema_mode = schema_mode
        self._status_groups = status_groups
        self._role_folders = role_folders
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
        self._declaration_directories: set[Path] = set()
        self._source_paths: set[Path] = set()
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
    def set_observed_header_schema(self, schema: HeaderSchema) -> None:
        """Retain the Mode 2 Header shape observed during this owner's cold start."""
        self._observed_header_schema = schema
    def release_cache(self) -> None:
        """Release parsed successful rows while retaining failed signatures."""
        self._cached.clear()
        self._references = ReferenceIndex()
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
        previous = dict(self._cached)
        affected = self._apply_changes(changes)
        for path in sorted(affected):
            if path in self._source_paths:
                self._refresh_path(path, reader)
        affected.update(self._prune_missing_reference_aliases(affected))
        current = self._cached_rows()
        content_paths = self._references.update(self._cached_rows(previous), current, affected)
        rows = {
            path.relative_to(self.root).as_posix(): (
                self._cached.get(path, (None, None))[1] if path in self._references.accepted else None
            )
            for path in content_paths
        }
        if self._compiled_schema is None and self._content_schema.update(rows):
            return self._capture_full(reader, revalidate_content=True)
        invalid = self._exclude_invalid_content_sources(rows)
        if invalid:
            content_paths = self._references.update(current, self._cached_rows(), invalid)
            if self._compiled_schema is None and self._content_schema.update({
                path.relative_to(self.root).as_posix(): (
                    self._cached.get(path, (None, None))[1] if path in self._references.accepted else None
                )
                for path in content_paths
            }):
                return self._capture_full(reader, revalidate_content=True)
        header_rows = {
            path.relative_to(self.root).as_posix(): (
                self._cached.get(path, (None, None))[1] if path in self._references.accepted else None
            )
            for path in affected | content_paths
        }
        header_changed = self._compiled_schema is None and self._header_schema.update(
            header_rows, accept_shape=self._schema_mode == 2,
        )
        if header_changed and self._schema_mode == 1:
            return self._capture_full(reader)
        invalid = self._exclude_invalid_header_sources([row for row in header_rows.values() if row is not None])
        if invalid:
            content_paths = self._references.update(current, self._cached_rows(), invalid)
            rows = {
                path.relative_to(self.root).as_posix(): (
                    self._cached.get(path, (None, None))[1] if path in self._references.accepted else None
                )
                for path in content_paths
            }
            if self._compiled_schema is None and self._content_schema.update(rows):
                return self._capture_full(reader, revalidate_content=True)
        self.capture_delta = {
            path.relative_to(self.root).as_posix(): (
                self._cached.get(path, (None, None))[1] if path in self._references.accepted else None
            )
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
    def _prune_missing_reference_aliases(self, affected: set[Path]) -> set[Path]:
        """Drop a cached path that disappeared before its move event arrived."""
        references = {
            row["ref"]
            for path in affected
            if (row := self._cached.get(path, (None, None))[1]) is not None
            and isinstance(row.get("ref"), str)
        }
        removed: set[Path] = set()
        for reference in references:
            for path in self._references.paths.get(reference, ()):
                if path not in affected and file_signature(path) is None:
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
        prefix = project_identity_prefix(self.root)
        self._project_scope_id = f"{prefix.upper()}-SU-00"
        self._atom_filename = re.compile(rf"{re.escape(prefix)}-[A-Z]-.*\.md")
        self._declaration_paths = {Path(path).resolve() for path in declarations.paths}
        self._declaration_directories = {self.control_root}
        for row in declarations.as_structure()["scope_units"]:
            authority = self.root / row["authority_path"]
            self._declaration_directories.update(authority / role for role in DELEGATION_ROLE_FOLDERS)
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
        for path in sorted(self._source_paths):
            self._refresh_path(path, reader)
        self._references.rebuild(self._cached_rows())
        self._rebuild_content_schema(revalidated=revalidate_content)
        self._rebuild_header_schema()
        while self._exclude_invalid_header_sources():
            self._references.rebuild(self._cached_rows())
            self._rebuild_content_schema(revalidated=revalidate_content)
            self._rebuild_header_schema()
        self.excluded_count = len(self._failed)
        return self._rows(), self._scopes()
    def _declarations_changed(
        self, changes: list[dict[str, str | None]], reader: ReadContext,
    ) -> bool:
        for change in changes:
            old = self._change_path(change.get("old_path"))
            new = self._change_path(change.get("new_path"))
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
    def _apply_changes(self, changes: list[dict[str, str | None]]) -> set[Path]:
        affected: set[Path] = set()
        for change in changes:
            old = self._change_path(change.get("old_path"))
            new = self._change_path(change.get("new_path"))
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
            added = {path} if self._is_source_path(path) else set()
        elif path.is_dir():
            added = {
                candidate
                for candidate in _markdown_paths(path)
                if self._is_source_path(candidate)
            }
        else:
            added = set()
        self._source_paths.update(added)
        return added
    def _is_source_path(self, path: Path) -> bool:
        if self._atom_filename is None or not self._atom_filename.fullmatch(path.name) or not path.is_relative_to(self.control_root):
            return False
        return not _archived(path.relative_to(self.control_root).parts) and not self._has_symlink_ancestor(path)
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
        if revalidated:
            self._content_invalid.clear()
        else:
            self._content_invalid.intersection_update(self._source_paths)
        if self._compiled_schema is not None:
            while self._exclude_content_errors(
                self._content_schema.validation_errors(self._accepted_rows())
            ):
                self._references.rebuild(self._cached_rows())
            return
        self._exclude_content_errors(self._content_schema.rebuild(self._accepted_rows()))
        self._references.rebuild(self._cached_rows())
    def _rebuild_header_schema(self) -> None:
        if self._compiled_schema is None:
            self._header_schema.rebuild(self._accepted_rows())
    def _exclude_invalid_header_sources(self, rows: Iterable[dict[str, Any]] | None = None) -> set[Path]:
        schema = self.header_schema if self._schema_mode == 1 else self._observed_header_schema
        if schema is None:
            return set()
        candidates = self._accepted_rows() if rows is None else rows
        errors = self._header_schema.validation_errors(candidates, schema=schema)
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
        return self._exclude_content_errors(self._content_schema.validation_errors(
            row for row in rows.values() if row is not None
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
    def _refresh_path(self, path: Path, reader: ReadContext) -> None:
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
        self._read_source(path, signature, reader)
    def _rows(self) -> list[dict[str, Any]]:
        return [
            self._cached[path][1]
            for path in sorted(self._source_paths)
            if path in self._cached and path in self._references.accepted
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
            and any(path.is_relative_to(directory) for directory in authority)
        ]
        # Other Current rows suppress obsolete copies even when their form changed.
        errors = self._content_schema.validation_errors(row for row in rows if predicate(row))
        references = {row.get("ref") for row in rows if row.get("ref") is not None}
        return ([row for row in rows if row.get("source_path") not in errors]
                + [row for row in observed if row.get("ref") not in references])
    def _cached_rows(
        self, cached: dict[Path, tuple[tuple[int, ...], dict[str, Any]]] | None = None,
    ) -> dict[Path, dict[str, Any]]:
        return {path: item[1] for path, item in (self._cached if cached is None else cached).items()}
    def _accepted_rows(self) -> list[dict[str, Any]]:
        return [self._cached[path][1] for path in sorted(self._references.accepted) if path in self._cached]
    def _scopes(self) -> list[dict[str, Any]]:
        assert self._declarations is not None
        rows = [
            source_scope(item, self.root)
            for item in (self._declarations.root, *self._declarations.units)
        ]
        rows[0]["scope_unit_id"] = self._project_scope_id
        return rows
    def _read_source(
        self, path: Path, signature: tuple[int, ...], reader: ReadContext
    ) -> dict[str, Any] | None:
        try:
            raw = reader.read(path)
        except (OSError, RuntimeError) as error:
            self._cached.pop(path, None)
            self._failed[path] = signature
            self.excluded_count += 1
            self._error(path, error)
            return None
        try:
            parsed = parse_carrier(raw, path)
            view = carrier_read_view(parsed.metadata)
            group = _group(path.relative_to(self.root), view, self._status_groups)
            if group is None:
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
            canonical_row(row)
        except (OSError, RuntimeError, TypeError, ValueError, CarrierError) as error:
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
        return {path for path in _markdown_paths(self.control_root) if self._is_source_path(path)}
    def audit_issues(self, public_atoms: dict[tuple[str, str], dict[str, Any]]) -> dict[str, list[tuple[str | None, ...]]]:
        """Describe the same Current/Draft sources read during the latest capture."""
        assert self._declarations is not None
        return collect_issues(
            self.root, self.control_root, self._source_paths, self.audit_delta, self._cached,
            self._diagnostics, self._references.accepted,
            self._declarations.as_structure()["scope_units"], self._project_scope_id,
            self.content_schema, public_atoms, self._role_folders,
        )

    def _error(self, path: Path, error: BaseException) -> None:
        if path in self._source_paths:
            self._diagnostics[path] = str(error)
        print(f"source-reader: {path}: {error}", file=sys.stderr)
def capture_inventory(
    root: Path, control_root: Path | None = None
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    return SourceReader(root, control_root).capture()
