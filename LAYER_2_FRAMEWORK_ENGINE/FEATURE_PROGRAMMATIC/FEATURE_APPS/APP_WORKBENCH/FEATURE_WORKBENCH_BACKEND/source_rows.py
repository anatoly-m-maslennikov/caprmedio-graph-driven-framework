# CA-R-2723@5
# CA-R-2726@6
# CA-D-672@14
# CA-M-465@24
# CA-M-500@3
# CA-M-464@15

"""Map parsed Atom and Scope Unit sources to raw Workbench rows."""

from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass, field
from pathlib import Path
import re
from typing import Any

from .markdown_content import parse_content
from .relations import canonical


_NUMBERED_DRAFT_REFERENCE = re.compile(r"@\d+-draft$")


def atom(
    path: Path, root: Path, header: dict[str, Any], view: dict[str, Any],
    body: str | bytes, group: str,
) -> dict[str, Any]:
    cached_body = body.encode("utf-8") if isinstance(body, str) else body
    if not isinstance(cached_body, bytes):
        raise TypeError("Markdown body must be UTF-8 text or bytes")
    markdown = cached_body.decode("utf-8")
    atom_id, version = view.get("atom_id"), view.get("version")
    if group == "Current" and isinstance(atom_id, str):
        ref = atom_id
    elif group == "Draft" and isinstance(atom_id, str) and type(version) is int:
        if _NUMBERED_DRAFT_REFERENCE.search(atom_id):
            ref = atom_id
        elif atom_id.endswith(("-draft", "@draft")):
            ref = f"{atom_id}:{path.relative_to(root).as_posix()}"
        else:
            ref = f"{atom_id}@{version}-draft"
    else:
        ref = None
    return {
        "source_path": path.relative_to(root).as_posix(),
        "status_group": group,
        "id": atom_id if isinstance(atom_id, str) else None,
        "ref": ref,
        "version": bigint(version),
        "status": string(view.get("status")),
        "current_scope_unit": string(header.get("current_scope_unit")),
        "claim_target_scope_unit": string(header.get("claim_target_scope_unit")),
        "role": string(view.get("content_role")),
        "form": string(view.get("type")),
        "tier": bigint(view.get("tier")),
        "updated_at": view.get("updated_at"),
        "header_json": header,
        "_content_bytes": cached_body,
        "content_properties_json": parse_content(
            markdown, tolerate_duplicate_siblings=True, compact=True,
        ),
        "relation_edges_json": [],
        "hash": None,
    }


def scope(item: Any, root: Path) -> dict[str, Any]:
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


def string(value: Any) -> str | None:
    return value if isinstance(value, str) else None


def bigint(value: Any) -> int | None:
    return value if type(value) is int and -(2**63) <= value < 2**63 else None


def _same_types(before: Any, after: Any) -> bool:
    if type(before) is not type(after):
        return False
    if isinstance(before, dict):
        return before.keys() == after.keys() and all(_same_types(value, after[key]) for key, value in before.items())
    if isinstance(before, (list, tuple)):
        return len(before) == len(after) and all(_same_types(left, right) for left, right in zip(before, after))
    return True


def same_row(
    before: tuple[tuple[int, ...], dict[str, Any]] | None,
    after: tuple[tuple[int, ...], dict[str, Any]] | None,
) -> bool:
    if before is None or after is None:
        return before is after
    if before[1] is after[1]:
        return True
    return (
        _same_types(before[1], after[1])
        and before[1].get("_content_bytes") == after[1].get("_content_bytes")
        and canonical_row(before[1]) == canonical_row(after[1])
    )


def canonical_row(row: Mapping[str, Any]) -> str:
    """Validate a source row without decoding its private cached body."""
    payload = dict(row)
    if "_content_bytes" in payload:
        body = payload.pop("_content_bytes")
        if not isinstance(body, bytes):
            raise TypeError("cached Markdown body must be UTF-8 bytes")
    return canonical(payload)


@dataclass
class ReferenceIndex:
    """Track one selected carrier per reference and retain later copies for audits."""

    paths: dict[str, set[Path]] = field(default_factory=dict)
    accepted: set[Path] = field(default_factory=set)

    def rebuild(self, rows: Mapping[Path, Mapping[str, Any]]) -> None:
        self.paths = {}
        for path, row in rows.items():
            if (reference := _reference(row)) is not None:
                self.paths.setdefault(reference, set()).add(path)
        self.accepted = {
            path for path, row in rows.items()
            if (reference := _reference(row)) is None or path == min(self.paths[reference])
        }

    def update(
        self, before: Mapping[Path, Mapping[str, Any]], after: Mapping[Path, Mapping[str, Any]], affected: set[Path],
    ) -> set[Path]:
        impacted = set(affected)
        references = {
            reference
            for rows in (before, after) for path in affected
            if (row := rows.get(path)) is not None and (reference := _reference(row)) is not None
        }
        for reference in references:
            old = set(self.paths.get(reference, ()))
            for path in affected:
                if _reference(before.get(path)) == reference:
                    self.paths[reference].discard(path)
                if _reference(after.get(path)) == reference:
                    self.paths.setdefault(reference, set()).add(path)
            current = self.paths.get(reference, set())
            if not current:
                self.paths.pop(reference, None)
            impacted.update(old | current)
        for path in impacted:
            row = after.get(path)
            reference = _reference(row)
            if row is not None and (reference is None or path == min(self.paths[reference])):
                self.accepted.add(path)
            else:
                self.accepted.discard(path)
        return impacted


def _reference(row: Mapping[str, Any] | None) -> str | None:
    value = row.get("ref") if row is not None else None
    return value if isinstance(value, str) else None


def file_signature(path: Path) -> tuple[int, ...] | None:
    try:
        item = path.stat()
        return item.st_mode, item.st_ino, item.st_size, item.st_mtime_ns, item.st_ctime_ns
    except OSError:
        return None


def frontmatter_bounds(raw: bytes) -> tuple[int, int, int] | None:
    if raw.startswith(b"---\n"):
        opening_end = len(b"---\n")
    elif raw.startswith(b"---\r\n"):
        opening_end = len(b"---\r\n")
    else:
        return None
    closing = re.search(rb"\r?\n---\r?\n", raw, opening_end - 1)
    return None if closing is None else (opening_end, closing.start(), closing.end())


def source_body(raw: bytes, path: Path) -> bytes:
    bounds = frontmatter_bounds(raw)
    if bounds is None:
        raise ValueError(f"{path}: unsupported frontmatter delimiter")
    return raw[bounds[2]:]
