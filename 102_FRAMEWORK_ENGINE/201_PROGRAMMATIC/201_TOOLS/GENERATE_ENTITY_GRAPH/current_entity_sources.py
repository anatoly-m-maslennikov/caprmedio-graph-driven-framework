"""Read current Atom carriers in one source folder for the readable graph."""

import hashlib
import os
import re
from collections.abc import Iterator
from pathlib import Path
from typing import Any

from artifact_metadata import atom_identifier
from current_subject_graph import compose_current_graph
from VALIDATE_ATOMS.validate_atoms_workers.parsing import CarrierError, parse_carrier

_EXCLUDED = {
    "draft",
    "drafts",
    "archive",
    "archived",
    "_projection",
    "_journal",
}
_ATOM_FILENAME = re.compile(r"(?:[0-9]+-)?CA-[A-Z]-[0-9]+(?:[-.@]|$)")
_ATOM_FIELD = re.compile(rb"(?m)^(?:atom_id|'atom_id'|\"atom_id\")[ \t]*:")


def _source_paths(source_root: Path, repository: Path) -> Iterator[Path]:
    relative = source_root.relative_to(repository)
    if any(part.lower() in _EXCLUDED for part in relative.parts):
        return
    if source_root.is_symlink() or any(parent.is_symlink() for parent in source_root.parents):
        raise ValueError("Source folder must not traverse a symlink")
    if not source_root.is_dir():
        raise ValueError("Source folder is unavailable")
    for folder, directories, files in os.walk(source_root, followlinks=False):
        base = Path(folder)
        directories[:] = sorted(
            name
            for name in directories
            if name.lower() not in _EXCLUDED and not (base / name).is_symlink()
        )
        for name in sorted(files):
            path = base / name
            if path.suffix == ".md" and not path.is_symlink():
                yield path


def _atom_metadata(raw: bytes, path: Path) -> dict[str, Any] | None:
    canonical_name = _ATOM_FILENAME.match(path.name) is not None
    try:
        metadata = parse_carrier(raw, path).metadata
    except CarrierError:
        header = raw.split(b"\n---", 1)[0] if raw.startswith(b"---") else b""
        if canonical_name or _ATOM_FIELD.search(header):
            raise
        return None
    return metadata if canonical_name or "atom_id" in metadata else None


def _read_atom(path: Path, repository: Path) -> dict[str, Any] | None:
    raw = path.read_bytes()
    metadata = _atom_metadata(raw, path)
    if metadata is None:
        return None
    if str(metadata.get("artifact_form", "")).lower() in {"projection", "journal"}:
        return None
    explicit = metadata.get("atom_id")
    if explicit is not None and not isinstance(explicit, str):
        raise ValueError(f"{path}: current Atom identity is not text")
    atom_id = atom_identifier(path.name, explicit)
    if not atom_id:
        raise ValueError(f"{path}: current Atom identity is unavailable")
    version = metadata.get("version")
    if isinstance(version, bool) or not isinstance(version, int) or version < 1:
        raise ValueError(f"{path}: current Atom has no valid Version")
    source = {
        "atom_id": atom_id,
        "version": version,
        "path": path.relative_to(repository).as_posix(),
        "sha256": hashlib.sha256(raw).hexdigest(),
    }
    return {"source": source, "subjects": metadata.get("subjects")}


def build_current_graph(
    source_root: Path, repository: Path
) -> tuple[dict[str, Any], dict[str, Any]]:
    """Discover current carriers afresh, then pass only their data to the pure core."""
    source_root, repository = source_root.absolute(), repository.absolute()
    carriers = []
    for path in _source_paths(source_root, repository):
        carrier = _read_atom(path, repository)
        if carrier is not None:
            carriers.append(carrier)
    return compose_current_graph(carriers)
