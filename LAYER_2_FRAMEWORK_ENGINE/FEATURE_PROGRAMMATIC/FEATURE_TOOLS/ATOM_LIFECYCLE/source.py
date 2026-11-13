# CA-M-1006@7
# CA-D-625@14

"""Private, read-only exact Atom source binding for lifecycle workflows."""
from __future__ import annotations

from .timing import trace

from dataclasses import dataclass
from contextlib import contextmanager
from contextvars import ContextVar
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


class ArchiveNotLoadedError(SourceSelectionError):
    """The requested historical carrier has not been loaded into Workbench."""


_QUERY_READER = ContextVar('lifecycle_query_reader', default=None)


@contextmanager
def bind_query_reader(reader):
    token = _QUERY_READER.set(reader)
    try:
        yield
    finally:
        _QUERY_READER.reset(token)


def query_reader():
    return _QUERY_READER.get()


def query_candidates(selection, **filters):
    """Select indexed carriers without walking the Project's Atom directories."""
    reader = query_reader()
    rows = reader.lifecycle_candidates(selection, **filters)
    found = {}
    for atom_id, path in rows:
        path = Path(path)
        if not path.is_absolute() or '..' in path.parts or not path.is_relative_to(selection.root):
            raise SourceSelectionError('Indexed Atom path is outside the selected Project')
        found.setdefault(atom_id, set()).add(path)
    return {atom_id: tuple(sorted(paths)) for atom_id, paths in found.items()}


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


@dataclass(frozen=True)
class SourceContext:
    path: Path
    atom_id: str
    ref_id: str
    version: int
    status: str
    metadata: dict[str, Any]
    summary: str | None


def _context_candidate(selection, ref_id, atom_id, row):
    if not isinstance(row, (list, tuple)) or len(row) != 3:
        raise SourceSelectionError('Indexed Atom context is invalid')
    path, metadata, summary = row
    if not isinstance(path, Path) or not isinstance(metadata, dict) or not isinstance(summary, (str, type(None))):
        raise SourceSelectionError('Indexed Atom context is invalid')
    if (not path.is_absolute() or '..' in path.parts or not path.is_relative_to(selection.control_root)
            or path.resolve(strict=False) != path or path.suffix != '.md'):
        raise SourceSelectionError('Indexed Atom path is outside the selected Project')
    if not _matches_revision(path, atom_id, None, None):
        return None
    view = carrier_read_view(metadata)
    version, status = view.get('version'), view.get('status')
    if ('projection' in view or view.get('atom_id') != atom_id or view.get('ref_id') not in (None, atom_id)
            or type(version) is not int or version < 1
            or not isinstance(status, str) or not status.strip()
            or status.casefold() in {'draft', 'archived'}):
        return None
    return SourceContext(path, atom_id, ref_id, version, status, metadata, summary)


@trace('source.context')
def select_context(selection: ProjectSelection, ref_id: str, *, expected_version: int | None = None) -> SourceContext:
    """Select Current Atom context from the bound Workbench index without reading its Carrier."""
    atom_id, qualified, _ = _selector(selection, ref_id, expected_version)
    reader = query_reader()
    if reader is None or qualified is not None:
        raise SourceSelectionError('Current indexed Atom context is required')
    try:
        rows = reader.lifecycle_contexts(selection, ref_id)
        if not isinstance(rows, (list, tuple)):
            raise SourceSelectionError('Indexed Atom context is invalid')
        candidates = {}
        for row in rows:
            candidate = _context_candidate(selection, ref_id, atom_id, row)
            if candidate is not None:
                if candidate.path in candidates and candidates[candidate.path] != candidate:
                    raise SourceSelectionError('Atom source context is ambiguous')
                candidates[candidate.path] = candidate
        if len(candidates) != 1:
            raise SourceSelectionError('Atom source context is missing or ambiguous')
        candidate = next(iter(candidates.values()))
        if expected_version is not None and candidate.version != expected_version:
            raise SourceSelectionError('Expected Version is stale')
        return candidate
    except SourceSelectionError:
        raise
    except (OSError, RuntimeError, KeyError, TypeError, ValueError) as error:
        raise SourceSelectionError('Project Atom context is unavailable or unsafe') from error


def _candidate_paths(reader: ReadContext, selection: ProjectSelection, atom_id: str, *,
                     references: tuple[str, ...] = ()) -> tuple[Path, ...]:
    """Discover just this identity in declared authoring roots, without following links."""
    prefix = re.compile(r"^(?:[1-9][0-9]*-)?" + re.escape(atom_id) + r"(?=@|-|\.)")
    if query_reader() is not None:
        return tuple(path for path in query_candidates(selection, atom_ids=(atom_id,), references=references).get(atom_id, ())
                     if prefix.match(path.name))
    return _matching_paths(reader, selection, prefix)


def _matching_paths(reader: ReadContext, selection: ProjectSelection, prefix: re.Pattern[str]) -> tuple[Path, ...]:
    return _inventory_paths(reader, selection, lambda name: True if prefix.match(name) else None).get(True, ())


@trace('source.inventory')
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
    match = re.fullmatch(r"(" + re.escape(prefix) + r"-[A-Z]-[0-9]+)(?:@([1-9][0-9]*)(-draft)?)?", ref_id)
    if not match or (expected_version is not None and (type(expected_version) is not int or expected_version < 1)):
        raise SourceSelectionError("Invalid Atom reference or expected Version")
    atom_id, qualified, draft = match.groups()
    if qualified is not None and expected_version is not None and int(qualified) != expected_version:
        raise SourceSelectionError("Expected Version contradicts Atom reference")
    return atom_id, qualified, draft


def _carrier_revision(path: Path, atom_id: str) -> tuple[str | None, bool]:
    marker = re.match(r"(?:[1-9][0-9]*-)?" + re.escape(atom_id) + r"(?:@([1-9][0-9]*)(-draft)?)?(?=-|\.)", path.name)
    if not marker:
        raise SourceSelectionError("Malformed candidate carrier identity")
    candidate_version, candidate_draft = marker.groups()
    # Retained archived carriers also use the historical suffix form.
    if not candidate_version:
        suffix = re.search(r"@([1-9][0-9]*)\.md$", path.name)
        if suffix:
            candidate_version = suffix.group(1)
    return candidate_version, bool(candidate_draft)


def _matches_revision(path: Path, atom_id: str, qualified: str | None, draft: str | None) -> bool:
    return _carrier_revision(path, atom_id) == (qualified, bool(draft))


@trace('source.select_published_revisions')
def select_published_revisions(selection: ProjectSelection, atom_id: str) -> tuple[SourcePin, ...]:
    """Bind all Current, Backlog and Archived revisions of one Atom."""
    reader = ReadContext(roots=[str(selection.root)], limits=dict(CEILINGS))
    candidates = _candidate_paths(reader, selection, atom_id)
    references = set()
    for path in candidates:
        version, draft = _carrier_revision(path, atom_id)
        if not draft:
            references.add(f"{atom_id}@{version}" if version else atom_id)
    selected = tuple(select_sources(selection, sorted(references)).values())
    _check_currentness(reader, selection, atom_id, candidates)
    return selected


def _read_candidate(reader: ReadContext, path: Path, ref_id: str,
                    atom_id: str, qualified: str | None, draft: str | None, *,
                    retained_history: bool = False) -> SourcePin | None:
    source_reader = query_reader()
    raw = source_reader.lifecycle_read(path) if source_reader is not None else reader.read(path)
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


@trace('source.currentness')
def _check_currentness(reader: ReadContext, selection: ProjectSelection, atom_id: str,
                       candidates: tuple[Path, ...]) -> None:
    if query_reader() is not None:
        return
    if _candidate_paths(reader, selection, atom_id) != candidates:
        raise SourceSelectionError("Atom source candidates changed during selection")
    if reader.currentness()["state"] != "unchanged":
        raise SourceSelectionError("Atom source changed during selection")
    selection._revalidate_boundary(reader=reader)
    _check_declarations(reader, selection)


@trace('source.scope_declarations')
def _check_declarations(reader, selection):
    source_reader = query_reader()
    declarations = (source_reader.lifecycle_declarations() if source_reader is not None else
                    read_scope_unit_declarations(selection.root, selection.control_relative, reader=reader))
    if declarations.digest != selection.declaration_digest:
        raise SourceSelectionError("Retained Project declarations changed")


def _unique_candidate(reader, paths, ref_id, atom_id, qualified, draft, *, retained_history=False):
    if query_reader() is not None:
        matching = {path for path in paths if _matches_revision(path, atom_id, qualified, draft)}
        if len(matching) != 1:
            raise SourceSelectionError("Atom source is missing or ambiguous")
        pin = _read_candidate(reader, next(iter(matching)), ref_id, atom_id, qualified, draft,
                              retained_history=retained_history)
        if pin is None:
            raise SourceSelectionError("Atom source has no valid matching carrier")
        return pin
    found = [pin for path in paths
             if _matches_revision(path, atom_id, qualified, draft)
             if (pin := _read_candidate(reader, path, ref_id, atom_id, qualified, draft,
                                        retained_history=retained_history)) is not None]
    if len(found) != 1:
        raise SourceSelectionError("Atom source is missing or ambiguous")
    return found[0]


@trace('source.select')
def select_source(selection: ProjectSelection, ref_id: str, *, expected_version: int | None = None) -> SourcePin:
    """Bind one logical ID in the retained Project authoring tree, without mutation.

    An unqualified ID selects Current. A qualified ID selects Archived, or Draft
    with the ``-draft`` suffix. An optional expected version pins any read.
    """
    atom_id, qualified, draft = _selector(selection, ref_id, expected_version)
    reader = ReadContext(roots=[str(selection.root)], limits=dict(CEILINGS))
    try:
        if query_reader() is None:
            selection._revalidate_boundary(reader=reader)
        # The retained declaration tree is the source authority, not delivery paths,
        # applicable-methodology projections, arbitrary Project files or caller paths.
        candidates = _candidate_paths(reader, selection, atom_id, references=(ref_id,))
        selected = _unique_candidate(reader, candidates, ref_id, atom_id, qualified, draft,
                                     retained_history=bool(qualified and not draft))
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


@trace('source.select_many')
def select_sources(selection: ProjectSelection, ref_ids: list[str]) -> dict[str, SourcePin]:
    """Bind several exact revisions with one source inventory and recheck."""
    selectors = [(ref_id, *_selector(selection, ref_id, None)) for ref_id in ref_ids]
    ids = {atom_id for _, atom_id, _, _ in selectors}
    if not ids:
        return {}
    prefix = selection.settings["artifacts"]["identity"]["project_prefix"]
    marker = re.compile(r"^(?:[1-9][0-9]*-)?(" + re.escape(prefix) + r"-[A-Z]-[0-9]+)(?=@|-|\.)")

    def classify(name: str) -> str | None:
        match = marker.match(name)
        return match.group(1) if match and match.group(1) in ids else None

    reader = ReadContext(roots=[str(selection.root)], limits=dict(CEILINGS))
    try:
        if query_reader() is not None:
            if len(ids) == len(selectors):
                indexed = query_candidates(selection, atom_ids=tuple(sorted(ids)), references=tuple(ref_ids))
                return {ref_id: _unique_candidate(reader, indexed.get(atom_id, ()), ref_id,
                                                   atom_id, qualified, draft,
                                                   retained_history=bool(qualified and not draft))
                        for ref_id, atom_id, qualified, draft in selectors}
            return {ref_id: _unique_candidate(
                        reader, query_candidates(selection, atom_ids=(atom_id,), references=(ref_id,)).get(atom_id, ()),
                        ref_id, atom_id, qualified, draft, retained_history=bool(qualified and not draft))
                    for ref_id, atom_id, qualified, draft in selectors}
        selection._revalidate_boundary(reader=reader)
        candidates = _inventory_paths(reader, selection, classify)
        selected = {ref_id: _unique_candidate(reader, candidates.get(atom_id, ()), ref_id, atom_id, qualified,
                                               draft, retained_history=bool(qualified and not draft))
                    for ref_id, atom_id, qualified, draft in selectors}
        if _inventory_paths(reader, selection, classify) != candidates:
            raise SourceSelectionError("Atom source candidates changed during selection")
        if reader.currentness()["state"] != "unchanged":
            raise SourceSelectionError("Atom source changed during selection")
        selection._revalidate_boundary(reader=reader)
        _check_declarations(reader, selection)
        return selected
    except SourceSelectionError:
        raise
    except (OSError, RuntimeError, KeyError, TypeError, ValueError) as error:
        raise SourceSelectionError("Project source selection is unavailable or unsafe") from error
