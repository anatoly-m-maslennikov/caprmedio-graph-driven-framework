# CA-D-625@14

"""Private, read-only exact Atom source binding for lifecycle workflows."""
from __future__ import annotations

from dataclasses import dataclass
import hashlib
import os
from pathlib import Path
import re
from typing import Any

from carrier_aliases import carrier_read_view
from project_selection import ProjectSelection
from scope_unit_declarations import read_scope_unit_declarations
from VALIDATE_ATOMS.validate_atoms_workers.parsing import parse_carrier
from VALIDATE_ATOMS.validate_atoms_workers.read_io import ReadContext, open_regular
from VALIDATE_ATOMS.validate_atoms_workers.settings import CEILINGS
from .placement_model import active_placement


class SourceSelectionError(ValueError):
    """A logical Atom source cannot be bound unambiguously and safely."""


@dataclass(frozen=True)
class SourcePin:
    path: Path
    atom_id: str
    ref_id: str
    version: int
    status: str
    sha256: str
    raw: bytes
    metadata: dict[str, Any]


def _candidate_paths(reader: ReadContext, selection: ProjectSelection, atom_id: str) -> tuple[Path, ...]:
    """Discover just this identity in declared authoring roots, without following links."""
    prefix = re.compile(r"^(?:[1-9][0-9]*-)?" + re.escape(atom_id) + r"(?=@|-|\.)")
    return _matching_paths(reader, selection, prefix)


def _matching_paths(reader: ReadContext, selection: ProjectSelection, prefix: re.Pattern[str]) -> tuple[Path, ...]:
    return _inventory_paths(reader, selection, lambda name: True if prefix.match(name) else None).get(True, ())


def _inventory_paths(reader: ReadContext, selection: ProjectSelection, classify) -> dict[Any, tuple[Path, ...]]:
    recursive = {selection.root / unit["authority_path"] / role
                 for unit in selection.structure["scope_units"] for role in active_placement().role_folders.values()}
    direct = {selection.control_root}
    pending = [(directory, True) for directory in recursive] + [(directory, False) for directory in direct]
    found: dict[Any, set[Path]] = {}
    while pending:
        directory, descend = pending.pop()
        reader.checkpoint()
        try:
            reader.allowed(directory)
            descriptor = open_regular(directory, directory=True)
        except FileNotFoundError:
            continue
        try:
            with os.scandir(descriptor) as entries:
                for entry in entries:
                    reader.checkpoint()
                    path = directory / entry.name
                    identity = classify(entry.name)
                    if entry.is_symlink():
                        # A matching symlink is never read; a directory symlink
                        # could hide another source and cannot be traversed safely.
                        if identity is not None or descend:
                            raise SourceSelectionError("Symlink in Atom source boundary")
                    elif descend and entry.is_dir(follow_symlinks=False):
                        pending.append((path, True))
                    elif entry.name.endswith(".md") and identity is not None:
                        candidates = found.setdefault(identity, set())
                        candidates.add(path)
                        if len(candidates) > reader.limits["max_candidates"]:
                            raise SourceSelectionError("Atom source candidate limit exceeded")
        finally:
            os.close(descriptor)
    return {identity: tuple(sorted(paths)) for identity, paths in found.items()}


def _selector(selection: ProjectSelection, ref_id: str, expected_version: int | None) -> tuple[str, str | None, str | None]:
    if not isinstance(selection, ProjectSelection) or not isinstance(ref_id, str):
        raise SourceSelectionError("Invalid Project selection or Atom reference")
    try:
        prefix = selection.settings["artifacts"]["identity"]["project_prefix"]
        if not isinstance(prefix, str) or not prefix.strip() or prefix != prefix.upper():
            raise ValueError("Invalid Project identity prefix")
    except (KeyError, TypeError, ValueError) as error:
        raise SourceSelectionError("Selected Project identity prefix is unavailable or invalid") from error
    match = re.fullmatch(r"(" + re.escape(prefix) + r"-[A-Z]-[1-9][0-9]*)(?:@([1-9][0-9]*)(-draft)?)?", ref_id)
    if not match or (expected_version is not None and (type(expected_version) is not int or expected_version < 1)):
        raise SourceSelectionError("Invalid Atom reference or expected Version")
    atom_id, qualified, draft = match.groups()
    if qualified is not None and expected_version is not None and int(qualified) != expected_version:
        raise SourceSelectionError("Expected Version contradicts Atom reference")
    return atom_id, qualified, draft


def _matches_revision(path: Path, atom_id: str, qualified: str | None, draft: str | None) -> bool:
    marker = re.match(r"(?:[1-9][0-9]*-)?" + re.escape(atom_id) + r"(?:@([1-9][0-9]*)(-draft)?)?(?=-|\.)", path.name)
    if not marker:
        raise SourceSelectionError("Malformed candidate carrier identity")
    candidate_version, candidate_draft = marker.groups()
    # Retained archived carriers also use the historical suffix form.
    if not candidate_version:
        suffix = re.search(r"@([1-9][0-9]*)\.md$", path.name)
        if suffix:
            candidate_version = suffix.group(1)
    return (candidate_version, bool(candidate_draft)) == (qualified, bool(draft))


def _read_candidate(reader: ReadContext, path: Path, ref_id: str,
                    atom_id: str, qualified: str | None, draft: str | None, *,
                    retained_history: bool = False) -> SourcePin | None:
    raw = reader.read(path)
    parsed = parse_carrier(raw, path)
    view = carrier_read_view(parsed.metadata)
    if "projection" in view:
        return None
    actual_version, status = view.get("version"), view.get("status")
    actual_id, actual_ref = view.get("atom_id"), view.get("ref_id")
    legacy_archive_id = retained_history and qualified is not None and not draft and actual_id == actual_ref == ref_id
    if ((actual_id != atom_id and not legacy_archive_id) or type(actual_version) is not int
            or actual_version < 1 or not isinstance(status, str)):
        raise SourceSelectionError("Candidate identity or Version is invalid")
    status_key = status.casefold()
    if (draft and status_key != "draft") or (qualified and not draft and status_key != "archived") or (not qualified and status_key in {"draft", "archived"}):
        raise SourceSelectionError("Candidate Status contradicts reference")
    if qualified is not None and actual_version != int(qualified):
        raise SourceSelectionError("Candidate Version contradicts reference")
    if actual_ref is not None and actual_ref not in (ref_id, atom_id if draft else ref_id):
        raise SourceSelectionError("Candidate Ref ID contradicts reference")
    return SourcePin(path, atom_id, ref_id, actual_version, status, hashlib.sha256(raw).hexdigest(), raw, parsed.metadata)


def _check_currentness(reader: ReadContext, selection: ProjectSelection, atom_id: str,
                       candidates: tuple[Path, ...]) -> None:
    if _candidate_paths(reader, selection, atom_id) != candidates:
        raise SourceSelectionError("Atom source candidates changed during selection")
    if reader.currentness()["state"] != "unchanged":
        raise SourceSelectionError("Atom source changed during selection")
    selection._revalidate_boundary(reader=reader)
    if read_scope_unit_declarations(selection.root, selection.control_relative, reader=reader).digest != selection.declaration_digest:
        raise SourceSelectionError("Retained Project declarations changed")


def _unique_candidate(reader, paths, ref_id, atom_id, qualified, draft):
    found = [pin for path in paths
             if _matches_revision(path, atom_id, qualified, draft)
             if (pin := _read_candidate(reader, path, ref_id, atom_id, qualified, draft)) is not None]
    if len(found) != 1:
        raise SourceSelectionError("Atom source is missing or ambiguous")
    return found[0]


def select_source(selection: ProjectSelection, ref_id: str, *, expected_version: int | None = None) -> SourcePin:
    """Bind one logical ID in the retained Project authoring tree, without mutation.

    An unqualified ID selects Current. A qualified ID selects Archived, or Draft
    with the ``-draft`` suffix. An optional expected version pins any read.
    """
    atom_id, qualified, draft = _selector(selection, ref_id, expected_version)
    reader = ReadContext(roots=[str(selection.root)], limits=dict(CEILINGS))
    try:
        selection._revalidate_boundary(reader=reader)
        # The retained declaration tree is the source authority, not delivery paths,
        # applicable-methodology projections, arbitrary Project files or caller paths.
        candidates = _candidate_paths(reader, selection, atom_id)
        selected = _unique_candidate(reader, candidates, ref_id, atom_id, qualified, draft)
        if expected_version is not None and selected.version != expected_version:
            raise SourceSelectionError("Expected Version is stale")
        _check_currentness(reader, selection, atom_id, candidates)
        return selected
    except SourceSelectionError:
        raise
    except (OSError, RuntimeError, KeyError, TypeError, ValueError) as error:
        raise SourceSelectionError("Project source selection is unavailable or unsafe") from error


def select_current_sources(selection: ProjectSelection, ref_ids: list[str]) -> dict[str, SourcePin]:
    """Bind Current sources together with one shared inventory and recheck."""
    selectors = [_selector(selection, ref_id, None) for ref_id in ref_ids]
    if any(qualified is not None for _, qualified, _ in selectors):
        raise SourceSelectionError("Invalid Atom reference or expected Version")
    return select_sources(selection, ref_ids)


def select_sources(selection: ProjectSelection, ref_ids: list[str]) -> dict[str, SourcePin]:
    """Bind several exact revisions with one source inventory and recheck."""
    selectors = [(ref_id, *_selector(selection, ref_id, None)) for ref_id in ref_ids]
    ids = {atom_id for _, atom_id, _, _ in selectors}
    if not ids:
        return {}
    prefix = selection.settings["artifacts"]["identity"]["project_prefix"]
    marker = re.compile(r"^(?:[1-9][0-9]*-)?(" + re.escape(prefix) + r"-[A-Z]-[1-9][0-9]*)(?=@|-|\.)")

    def classify(name: str) -> str | None:
        match = marker.match(name)
        return match.group(1) if match and match.group(1) in ids else None

    reader = ReadContext(roots=[str(selection.root)], limits=dict(CEILINGS))
    try:
        selection._revalidate_boundary(reader=reader)
        candidates = _inventory_paths(reader, selection, classify)
        selected = {ref_id: _unique_candidate(reader, candidates.get(atom_id, ()), ref_id, atom_id, qualified, draft)
                    for ref_id, atom_id, qualified, draft in selectors}
        if _inventory_paths(reader, selection, classify) != candidates:
            raise SourceSelectionError("Atom source candidates changed during selection")
        if reader.currentness()["state"] != "unchanged":
            raise SourceSelectionError("Atom source changed during selection")
        selection._revalidate_boundary(reader=reader)
        if read_scope_unit_declarations(selection.root, selection.control_relative, reader=reader).digest != selection.declaration_digest:
            raise SourceSelectionError("Retained Project declarations changed")
        return selected
    except SourceSelectionError:
        raise
    except (OSError, RuntimeError, KeyError, TypeError, ValueError) as error:
        raise SourceSelectionError("Project source selection is unavailable or unsafe") from error
