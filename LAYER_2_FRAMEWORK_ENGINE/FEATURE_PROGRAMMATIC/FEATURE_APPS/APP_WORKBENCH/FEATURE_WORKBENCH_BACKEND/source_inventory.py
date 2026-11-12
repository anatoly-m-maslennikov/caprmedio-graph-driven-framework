# CA-R-2723@5
"""Recognize selected Atom carriers and inventory Markdown paths."""

from __future__ import annotations

import os
from collections.abc import Iterator
from pathlib import Path
from typing import Any

from .source_roles import ARCHIVE_PARTS, CANONICAL_ROLE_MARKERS, FILENAME_MARKER, HEADER_MARKER, ROLE_MARKERS
from .source_rows import frontmatter_bounds


def filename_candidate(path: Path) -> bool:
    return filename_marker(path) is not None


def canonical_filename_candidate(path: Path, role_folders=None) -> bool:
    return filename_role_matches(path, role_folders) and filename_candidate(path)


def filename_marker(path: Path) -> str | None:
    match = FILENAME_MARKER.search(path.name.encode("utf-8"))
    return match.group("role").decode("utf-8").upper() if match else None


def filename_role_matches(path: Path, role_folders=None) -> bool:
    marker = filename_marker(path)
    if marker is None:
        return True
    markers = ROLE_MARKERS if role_folders is None else {
        folder: CANONICAL_ROLE_MARKERS.get(role, {role[0].upper()}) for role, folder in role_folders
    }
    role = next((part for part in reversed(path.parts[:-1]) if part in markers), None)
    return role is None or marker in markers[role]


def header_candidate(raw: bytes) -> bool:
    bounds = frontmatter_bounds(raw)
    if bounds is None:
        return False
    opening, boundary, _ = bounds
    return HEADER_MARKER.search(raw[opening:boundary]) is not None


def candidate(path: Path, raw: bytes, role_folders=None) -> bool:
    return filename_role_matches(path, role_folders) and (filename_candidate(path) or header_candidate(raw))


def group(path: Path, header: dict[str, Any], status_groups=()) -> str | None:
    from carrier_aliases import carrier_status_folder, matches_named_value
    parts = {carrier_status_folder(item) for item in path.parts}
    status = header.get("status")
    status = status.casefold() if isinstance(status, str) else status
    if "archived" in parts or status == "archived":
        return "Archived"
    if "draft" in parts or status == "draft":
        return "Draft"
    for role, value, status_group in status_groups:
        if matches_named_value(header.get("role"), role) and matches_named_value(header.get("status"), value):
            return status_group
    return "Current"


def archived(parts: tuple[str, ...]) -> bool:
    from carrier_aliases import carrier_status_folder
    return any(part.casefold() in ARCHIVE_PARTS or carrier_status_folder(part) == "archived" for part in parts)


def markdown_paths(root: Path, *, include_archived: bool = True) -> Iterator[Path]:
    for directory, names, files in os.walk(root, topdown=True, followlinks=False):
        base = Path(directory)
        names[:] = [name for name in names if not (base / name).is_symlink()
                    and (include_archived or not archived((name,)))]
        for name in names:
            if (path := base / name).suffix == ".md":
                yield path
        for name in files:
            path = base / name
            if path.suffix == ".md" and not path.is_symlink():
                yield path


def rejected_diagnostic(path: Path, raw: bytes, root: Path, parse: Any, read_view: Any, role_folders=None) -> str | None:
    """Report valid Atom carriers excluded by a mismatched role directory."""
    if filename_role_matches(path, role_folders) or not filename_candidate(path) or not header_candidate(raw):
        return None
    try:
        view = read_view(parse(raw, path).metadata)
        if isinstance(view.get("atom_id"), str) and group(path.relative_to(root), view):
            return "Atom filename role conflicts with its role directory."
    except (OSError, RuntimeError, TypeError, ValueError):
        pass
    return None
