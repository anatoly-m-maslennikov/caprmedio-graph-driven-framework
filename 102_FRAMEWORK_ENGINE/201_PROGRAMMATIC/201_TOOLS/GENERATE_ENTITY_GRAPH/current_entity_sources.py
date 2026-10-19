"""Read current Atom carriers in one source folder for the readable graph."""

import hashlib
import os
import re
from collections.abc import Iterator
from pathlib import Path
from typing import Any

from artifact_metadata import atom_identifier
from current_subject_graph import compose_current_graph
from VALIDATE_ATOMS.validate_atoms_workers.parsing import (
    CarrierError,
    ParsedCarrier,
    parse_carrier,
)
from VALIDATE_ATOMS.validate_atoms_workers.settings import CEILINGS

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
_FRONTMATTER_OPEN = re.compile(r"\A---\r?\n")
_FRONTMATTER_CLOSE = re.compile(r"(?m)^---\r?\n")


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


def _parse_atom(raw: bytes, path: Path) -> ParsedCarrier | None:
    canonical_name = _ATOM_FILENAME.match(path.name) is not None
    try:
        parsed = parse_carrier(raw, path)
    except CarrierError:
        header = raw.split(b"\n---", 1)[0] if raw.startswith(b"---") else b""
        if canonical_name or _ATOM_FIELD.search(header):
            raise
        return None
    return parsed if canonical_name or "atom_id" in parsed.metadata else None


def _read_bounded(path: Path) -> bytes:
    maximum = CEILINGS["max_file_bytes"]
    if path.stat().st_size > maximum:
        raise ValueError(f"{path}: current source exceeds max_file_bytes ceiling")
    with path.open("rb") as source:
        raw = source.read(maximum + 1)
    if len(raw) > maximum:
        raise ValueError(f"{path}: current source exceeds max_file_bytes ceiling")
    return raw


def _raw_body(text: str, path: Path) -> str:
    """Return exact decoded body text using the carrier delimiter line offsets."""
    opening = _FRONTMATTER_OPEN.match(text)
    closing = _FRONTMATTER_CLOSE.search(text, opening.end()) if opening else None
    if closing is None:
        # parse_carrier already validates this boundary; keep failure explicit if its
        # splitting contract ever changes rather than silently losing source bytes.
        raise ValueError(f"{path}: parsed carrier has no exact body boundary")
    return text[closing.end() :]


def _read_atom(path: Path, repository: Path) -> dict[str, Any] | None:
    raw = _read_bounded(path)
    parsed = _parse_atom(raw, path)
    if parsed is None:
        return None
    metadata = parsed.metadata
    if str(metadata.get("artifact_form", "")).lower() in {"projection", "journal"}:
        return None
    if str(metadata.get("status", "")).strip().lower() in {"draft", "archived"}:
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
    return {
        "source": source,
        "subjects": metadata.get("subjects"),
        "metadata": metadata,
        "body": parsed.body,
        "raw_body": _raw_body(parsed.text, path),
        "raw": raw,
    }


def read_current_carriers(source_root: Path, repository: Path) -> list[dict[str, Any]]:
    """Read current Atom evidence once, retaining parsed fields and exact bytes."""
    source_root, repository = source_root.absolute(), repository.absolute()
    carriers = []
    for path in _source_paths(source_root, repository):
        carrier = _read_atom(path, repository)
        if carrier is not None:
            carriers.append(carrier)
    return carriers


def build_current_graph(
    source_root: Path, repository: Path
) -> tuple[dict[str, Any], dict[str, Any]]:
    """Discover current carriers afresh, then pass only their data to the pure core."""
    return compose_current_graph(read_current_carriers(source_root, repository))
