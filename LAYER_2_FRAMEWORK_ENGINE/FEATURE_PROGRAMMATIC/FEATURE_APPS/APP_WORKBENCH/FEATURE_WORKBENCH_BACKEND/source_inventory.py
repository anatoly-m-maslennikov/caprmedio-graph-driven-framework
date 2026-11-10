# CA-R-2723@5
"""Recognize selected Atom carriers and inventory Markdown paths."""

from __future__ import annotations

import os
from collections.abc import Iterator
from pathlib import Path
from typing import Any

from .source_roles import ARCHIVE_PARTS, FILENAME_MARKER, HEADER_MARKER, ROLE_MARKERS, ROLES
from .source_rows import frontmatter_bounds


def filename_candidate(path: Path) -> bool:
    return filename_marker(path) is not None


def canonical_filename_candidate(path: Path) -> bool:
    return filename_role_matches(path) and filename_candidate(path)


def filename_marker(path: Path) -> str | None:
    match = FILENAME_MARKER.search(path.name.encode("utf-8"))
    return match.group("role").decode("utf-8").upper() if match else None


def filename_role_matches(path: Path) -> bool:
    marker = filename_marker(path)
    if marker is None:
        return True
    role = next((part for part in reversed(path.parts[:-1]) if part in ROLES), None)
    return role is None or marker in ROLE_MARKERS[role]


def header_candidate(raw: bytes) -> bool:
    bounds = frontmatter_bounds(raw)
    if bounds is None:
        return False
    opening, boundary, _ = bounds
    return HEADER_MARKER.search(raw[opening:boundary]) is not None


def candidate(path: Path, raw: bytes) -> bool:
    return filename_role_matches(path) and (filename_candidate(path) or header_candidate(raw))


def group(path: Path, header: dict[str, Any]) -> str | None:
    parts = {item.casefold() for item in path.parts}
    status = header.get("status")
    status = status.casefold() if isinstance(status, str) else status
    if parts & {"archive", "archived"} or status == "archived":
        return None
    if parts & {"draft", "drafts"} or status == "draft":
        return "Draft"
    return "Current"


def archived(parts: tuple[str, ...]) -> bool:
    return bool({part.casefold() for part in parts} & ARCHIVE_PARTS)


def markdown_paths(root: Path) -> Iterator[Path]:
    for directory, names, files in os.walk(root, topdown=True, followlinks=False):
        base = Path(directory)
        for name in names:
            path = base / name
            if name.casefold() not in ARCHIVE_PARTS and path.suffix == ".md" and not path.is_symlink():
                yield path
        names[:] = [
            name for name in names
            if name.casefold() not in ARCHIVE_PARTS and not (base / name).is_symlink()
        ]
        for name in files:
            path = base / name
            if path.suffix == ".md" and not path.is_symlink():
                yield path


def rejected_diagnostic(path: Path, raw: bytes, root: Path, parse: Any, read_view: Any) -> str | None:
    """Report valid Atom carriers excluded by a mismatched role directory."""
    if filename_role_matches(path) or not filename_candidate(path) or not header_candidate(raw):
        return None
    try:
        view = read_view(parse(raw, path).metadata)
        if isinstance(view.get("atom_id"), str) and group(path.relative_to(root), view):
            return "Atom filename role conflicts with its role directory."
    except (OSError, RuntimeError, TypeError, ValueError):
        pass
    return None
