# CA-R-2723@3
# CA-R-2725@3
# CA-R-2726@5
# CA-M-464@8
# CA-M-465@23
# CA-M-500@2
# CA-D-672@12

"""Governed Workbench carrier reader; scheduling belongs to the service."""

from __future__ import annotations

import os
import re
import sys
from collections.abc import Iterator
from pathlib import Path
from typing import Any

from .content_schema import ContentSchema
from .source_content_schema import SourceContentSchema
from .source_rows import (
    ReferenceIndex, atom as source_atom, canonical_row, file_signature, frontmatter_bounds, same_row as _same_row,
    scope as source_scope, source_body,
)
TOOLS = Path(__file__).resolve().parents[3] / "FEATURE_TOOLS"
if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))

from atom_operations import control_root as configured_control_root  # noqa: E402
from carrier_aliases import carrier_read_view  # noqa: E402
from scope_unit_declarations import (  # noqa: E402
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
_ROLES = {
    "01_concern",
    "02_analysis",
    "03_plan",
    "04_requirement",
    "05_method",
    "06_evaluation",
    "07_delivery",
    "09_operations",
}
_ARCHIVE_PARTS = {"archive", "archived", "_projection"}
_FILENAME_MARKER = re.compile(
    rb"^(?:[0-9]+-)?[A-Za-z0-9-]+-(?P<role>[A-Za-z][A-Za-z0-9]*)-"
    rb"(?:[0-9]+|[Dd][Rr][Aa][Ff][Tt])(?:[-.@]|$)"
)
_HEADER_MARKER = re.compile(rb"^[ \t]*(?:['\"]?)(?:atom_id|role|content_role)(?:['\"]?):", re.MULTILINE)
_ROLE_MARKERS = {
    "01_concern": {"C", "CONC", "CONCERN"},
    "02_analysis": {"A", "ANAL", "ANALYSIS", "ANRP"},
    "03_plan": {"P", "PLAN", "EPIC", "TASK"},
    "04_requirement": {"R", "REQ", "REQU", "REQUIREMENT"},
    "05_method": {"M", "METH", "METHOD"},
    "06_evaluation": {"E", "EVAL", "EVALUATION"},
    "07_delivery": {"D", "DEL", "DELIVERY"},
    "09_operations": {"O", "OPER", "OPERATION", "OPERATIONS", "ACTION", "WORKFLOW", "STEP"},
}
class SourceReader:
    def __init__(self, root: Path, control_root: Path | None = None) -> None:
        self.root = Path(root).resolve()
        if control_root is None:
            self.control_root = configured_control_root(self.root)
        else:
            candidate = Path(control_root)
            self.control_root = (
                candidate if candidate.is_absolute() else self.root / candidate
            ).resolve()
        self._failed: dict[Path, tuple[int, ...]] = {}
        self._cached: dict[Path, tuple[tuple[int, ...], dict[str, Any]]] = {}
        self._declarations: Any | None = None
        self._declaration_paths: set[Path] = set()
        self._declaration_directories: set[Path] = set()
        self._role_directories: set[Path] = set()
        self._source_paths: set[Path] = set()
        self._references = ReferenceIndex()
        self._inventory_ready = False
        self._content_schema = SourceContentSchema()
        self._content_invalid: set[Path] = set()
        self.excluded_count = 0
        self.capture_changed = True
        self.capture_delta: dict[str, dict[str, Any] | None] | None = None

    @property
    def content_schema(self) -> ContentSchema | None:
        return self._content_schema.schema

    def release_cache(self) -> None:
        """Release parsed successful rows while retaining failed signatures."""
        self._cached.clear()
        self._references = ReferenceIndex()
        self._inventory_ready = False
        self._content_schema.reset()
        self._content_invalid.clear()
        self.capture_changed = True
        self.capture_delta = None

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
        current = self._cached_rows()
        content_paths = self._references.update(self._cached_rows(previous), current, affected)
        rows = {
            path.relative_to(self.root).as_posix(): (
                self._cached.get(path, (None, None))[1] if path in self._references.accepted else None
            )
            for path in content_paths
        }
        if self._content_schema.update(rows):
            return self._capture_full(reader, revalidate_content=True)
        invalid = self._exclude_invalid_content_sources(rows)
        if invalid:
            content_paths = self._references.update(current, self._cached_rows(), invalid)
            if self._content_schema.update({
                path.relative_to(self.root).as_posix(): (
                    self._cached.get(path, (None, None))[1] if path in self._references.accepted else None
                )
                for path in content_paths
            }):
                return self._capture_full(reader, revalidate_content=True)
        self.capture_delta = {
            path.relative_to(self.root).as_posix(): self._cached.get(path, (None, None))[1]
            for path in affected
        }
        self.excluded_count = len(self._failed)
        self.capture_changed = any(
            not _same_row(previous.get(path), self._cached.get(path))
            for path in affected
        )
        return self._rows(), self._scopes()

    def _capture_full(
        self, reader: ReadContext, *, revalidate_content: bool = False,
    ) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
        self.capture_changed = True
        self.capture_delta = None
        try:
            declarations = read_scope_unit_declarations(
                self.root, self.control_root, reader=reader
            )
        except ScopeDeclarationError as error:
            self._error(self.root, error)
            raise
        self._declarations = declarations
        self._declaration_paths = {Path(path).resolve() for path in declarations.paths}
        self._declaration_directories = {self.control_root}
        self._role_directories = set()
        for row in declarations.as_structure()["scope_units"]:
            authority = self.root / row["authority_path"]
            self._declaration_directories.add(authority / "04_requirement")
            self._role_directories.update(authority / role for role in _ROLES)
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
        self._cached = {
            path: cached
            for path, cached in self._cached.items()
            if path in self._source_paths
        }
        for path in sorted(self._source_paths):
            self._refresh_path(path, reader)
        self._references.rebuild(self._cached_rows())
        self._rebuild_content_schema(revalidated=revalidate_content)
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
            self._content_invalid.discard(source)
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
        if path.suffix != ".md":
            return False
        if path not in self._declaration_paths:
            role = self._role_directory(path)
            if role is None or _archived(path.relative_to(role).parts):
                return False
        return not self._has_symlink_ancestor(path)

    def _role_directory(self, path: Path) -> Path | None:
        return next((parent for parent in path.parents if parent in self._role_directories), None)

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
        self._exclude_content_errors(self._content_schema.rebuild(self._accepted_rows()))
        self._references.rebuild(self._cached_rows())

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
            self._content_invalid.discard(path)
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
            if path in self._cached
        ]

    def _cached_rows(
        self, cached: dict[Path, tuple[tuple[int, ...], dict[str, Any]]] | None = None,
    ) -> dict[Path, dict[str, Any]]:
        return {path: item[1] for path, item in (self._cached if cached is None else cached).items()}

    def _accepted_rows(self) -> list[dict[str, Any]]:
        return [self._cached[path][1] for path in sorted(self._references.accepted) if path in self._cached]

    def _scopes(self) -> list[dict[str, Any]]:
        assert self._declarations is not None
        return [
            source_scope(item, self.root)
            for item in (self._declarations.root, *self._declarations.units)
        ]

    def _read_source(
        self, path: Path, signature: tuple[int, ...], reader: ReadContext
    ) -> dict[str, Any] | None:
        try:
            raw = reader.read(path)
        except (OSError, RuntimeError) as error:
            self._cached.pop(path, None)
            if _canonical_filename_candidate(path):
                self._failed[path] = signature
                self.excluded_count += 1
                self._error(path, error)
            else:
                self._failed.pop(path, None)
            return None
        if not _candidate(path, raw):
            self._cached.pop(path, None)
            self._failed.pop(path, None)
            self._content_invalid.discard(path)
            return None
        try:
            parsed = parse_carrier(raw, path)
            view = carrier_read_view(parsed.metadata)
            group = _group(path.relative_to(self.root), view)
            if group is None:
                self._cached.pop(path, None)
                self._failed.pop(path, None)
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
            self.excluded_count += 1
            self._error(path, error)
            return None
        self._failed.pop(path, None)
        self._cached[path] = (signature, row)
        return row

    def _inventory_paths(self) -> set[Path]:
        paths = set(self._declaration_paths)
        for role in self._role_directories:
            if role.is_dir() and not role.is_symlink():
                paths.update(_markdown_paths(role))
        return paths

    @staticmethod
    def _error(path: Path, error: BaseException) -> None:
        print(f"source-reader: {path}: {error}", file=sys.stderr)


def capture_inventory(
    root: Path, control_root: Path | None = None
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    return SourceReader(root, control_root).capture()


def _filename_candidate(path: Path) -> bool:
    return _filename_marker(path) is not None


def _canonical_filename_candidate(path: Path) -> bool:
    return _filename_role_matches(path) and _filename_candidate(path)


def _filename_marker(path: Path) -> str | None:
    match = _FILENAME_MARKER.search(path.name.encode("utf-8"))
    return match.group("role").decode("utf-8").upper() if match else None


def _filename_role_matches(path: Path) -> bool:
    marker = _filename_marker(path)
    if marker is None:
        return True
    role = next((part for part in reversed(path.parts[:-1]) if part in _ROLES), None)
    return role is None or marker in _ROLE_MARKERS[role]


def _header_candidate(raw: bytes) -> bool:
    bounds = frontmatter_bounds(raw)
    if bounds is None:
        return False
    opening, boundary, _ = bounds
    return _HEADER_MARKER.search(raw[opening:boundary]) is not None


def _candidate(path: Path, raw: bytes) -> bool:
    return _filename_role_matches(path) and (_filename_candidate(path) or _header_candidate(raw))


def _group(path: Path, header: dict[str, Any]) -> str | None:
    parts = {item.casefold() for item in path.parts}
    status = header.get("status")
    status = status.casefold() if isinstance(status, str) else status
    if parts & {"archive", "archived"} or status == "archived":
        return None
    if parts & {"draft", "drafts"} or status == "draft":
        return "Draft"
    return "Current"


def _archived(parts: tuple[str, ...]) -> bool:
    return bool({part.casefold() for part in parts} & _ARCHIVE_PARTS)


def _markdown_paths(root: Path) -> Iterator[Path]:
    for directory, names, files in os.walk(root, topdown=True, followlinks=False):
        base = Path(directory)
        for name in names:
            path = base / name
            if name.casefold() not in _ARCHIVE_PARTS and path.suffix == ".md" and not path.is_symlink():
                yield path
        names[:] = [
            name for name in names
            if name.casefold() not in _ARCHIVE_PARTS and not (base / name).is_symlink()
        ]
        for name in files:
            path = base / name
            if path.suffix == ".md" and not path.is_symlink():
                yield path
