# CA-R-2723@3
# CA-R-2725@2
# CA-R-2726@4
# CA-M-464@7
# CA-M-465@10
# CA-D-672@9

"""Governed Workbench carrier reader; scheduling belongs to the service."""

from __future__ import annotations

import sys
import re
from pathlib import Path
from typing import Any

from .markdown_content import parse_content
from .content_columns import content_columns
from .relations import canonical


TOOLS = Path(__file__).resolve().parents[3] / "FEATURE_TOOLS"
if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))

from atom_operations import control_root as configured_control_root  # noqa: E402
from carrier_aliases import carrier_read_view  # noqa: E402
from scope_unit_declarations import (  # noqa: E402
    ScopeDeclarationError,
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
_HEADER_MARKER = re.compile(rb"^(?:['\"]?)(?:atom_id|role|content_role)(?:['\"]?):", re.MULTILINE)
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
        self.excluded_count = 0

    def release_cache(self) -> None:
        """Release parsed successful rows while retaining failed signatures."""
        self._cached.clear()

    def capture(self) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
        self.excluded_count = 0
        reader = ReadContext(roots=[str(self.root)], limits=dict(CEILINGS))
        try:
            declarations = read_scope_unit_declarations(
                self.root, self.control_root, reader=reader
            )
        except ScopeDeclarationError as error:
            self._error(self.root, error)
            raise

        scopes = [
            _scope(item, self.root)
            for item in (declarations.root, *declarations.units)
        ]
        rows = []
        paths = self._paths(declarations)
        path_set = set(paths)
        self._failed = {
            path: signature
            for path, signature in self._failed.items()
            if path in path_set
        }
        self._cached = {
            path: cached
            for path, cached in self._cached.items()
            if path in path_set
        }
        for path in paths:
            signature = _signature(path)
            if signature is None:
                self._cached.pop(path, None)
                if _canonical_filename_candidate(path):
                    self.excluded_count += 1
                    self._error(path, OSError("source unavailable"))
                continue
            if self._failed.get(path) == signature:
                self._cached.pop(path, None)
                self.excluded_count += 1
                continue
            cached = self._cached.get(path)
            if cached is not None:
                if cached[0] == signature:
                    rows.append(cached[1])
                    continue
                self._cached.pop(path, None)
            row = self._read_source(path, signature, reader)
            if row is not None:
                rows.append(row)
        return rows, scopes

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
            return None
        try:
            parsed = parse_carrier(raw, path)
            view = carrier_read_view(parsed.metadata)
            group = _group(path.relative_to(self.root), view)
            if group is None:
                self._cached.pop(path, None)
                self._failed.pop(path, None)
                return None
            row = _atom(
                path,
                self.root,
                parsed.metadata,
                view,
                _body(raw, path),
                group,
            )
            canonical(row)
        except (OSError, RuntimeError, TypeError, ValueError, CarrierError) as error:
            self._cached.pop(path, None)
            self._failed[path] = signature
            self.excluded_count += 1
            self._error(path, error)
            return None
        self._failed.pop(path, None)
        self._cached[path] = (signature, row)
        return row

    def _paths(self, declarations: Any) -> list[Path]:
        paths = set(declarations.paths)
        for row in declarations.as_structure()["scope_units"]:
            authority = self.root / row["authority_path"]
            if not authority.exists():
                continue
            for role in authority.iterdir():
                if role.name not in _ROLES or not role.is_dir() or role.is_symlink():
                    continue
                for path in role.rglob("*.md"):
                    parts = {
                        part.casefold() for part in path.relative_to(role).parts
                    }
                    if not path.is_symlink() and not parts & _ARCHIVE_PARTS:
                        paths.add(path)
        return sorted(paths)

    @staticmethod
    def _error(path: Path, error: BaseException) -> None:
        print(f"source-reader: {path}: {error}", file=sys.stderr)


def capture_inventory(
    root: Path, control_root: Path | None = None
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    return SourceReader(root, control_root).capture()


def _signature(path: Path) -> tuple[int, ...] | None:
    try:
        item = path.stat()
        return (
            item.st_mode,
            item.st_ino,
            item.st_size,
            item.st_mtime_ns,
            item.st_ctime_ns,
        )
    except OSError:
        return None


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
    bounds = _frontmatter_bounds(raw)
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


def _string(value: Any) -> str | None:
    return value if isinstance(value, str) else None


def _bigint(value: Any) -> int | None:
    return value if type(value) is int and -(2**63) <= value < 2**63 else None


def _frontmatter_bounds(raw: bytes) -> tuple[int, int, int] | None:
    if raw.startswith(b"---\n"):
        opening_end = len(b"---\n")
    elif raw.startswith(b"---\r\n"):
        opening_end = len(b"---\r\n")
    else:
        return None
    closing = re.search(rb"\r?\n---\r?\n", raw, opening_end - 1)
    if closing is None:
        return None
    return opening_end, closing.start(), closing.end()


def _body(raw: bytes, path: Path) -> str:
    bounds = _frontmatter_bounds(raw)
    if bounds is not None:
        return raw[bounds[2] :].decode("utf-8")
    raise CarrierError("CARRIER_UNSUPPORTED", f"{path}: unsupported frontmatter delimiter")


def _atom(path, root, header, view, body, group):
    atom_id, version = header.get("atom_id"), header.get("version")
    if group == "Current" and isinstance(atom_id, str):
        ref = atom_id
    elif group == "Draft" and isinstance(atom_id, str) and type(version) is int:
        ref = (
            atom_id
            if atom_id.endswith(("-draft", "@draft"))
            else f"{atom_id}@{version}-draft"
        )
    else:
        ref = None
    row = {
        "source_path": path.relative_to(root).as_posix(),
        "status_group": group,
        "id": atom_id if isinstance(atom_id, str) else None,
        "ref": ref,
        "version": _bigint(version),
        "status": _string(header.get("status")),
        "current_scope_unit": _string(header.get("current_scope_unit")),
        "claim_target_scope_unit": _string(header.get("claim_target_scope_unit")),
        "role": _string(view.get("content_role")),
        "form": _string(view.get("type")),
        "tier": _bigint(header.get("tier")),
        "updated_at": header.get("updated_at"),
        "header_json": header,
        "content_markdown": body,
        "content_properties_json": parse_content(body, tolerate_duplicate_siblings=True),
        "relation_edges_json": [],
        "hash": None,
    }
    content_columns(row)
    return row


def _scope(item, root):
    return {
        "name": item.name,
        "scope_unit_id": item.scope_unit_id,
        "parent_name": item.parent,
        "declared_label": item.label,
        "ordered": item.ordered,
        "order_number": item.local_order,
        "declaration_source_path": item.source.relative_to(root).as_posix(),
        "declaration_version": item.version,
        "relation_edges_json": [],
        "hash": None,
    }
