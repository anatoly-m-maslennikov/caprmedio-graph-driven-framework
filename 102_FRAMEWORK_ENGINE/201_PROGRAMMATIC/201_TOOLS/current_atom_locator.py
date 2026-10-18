"""Resolve a missing Atom path hint within the selected Project's authority."""

from __future__ import annotations

import re
import os
from pathlib import Path
from collections.abc import Mapping
from typing import Any

import yaml

from atom_operations import ATOM_ID, ROLE_DIRECTORY, ToolError
from project_selection import ProjectSelection, ProjectSelectionError, active_selection
from VALIDATE_ATOMS.validate_atoms_workers.parsing import CarrierError, parse_carrier
from VALIDATE_ATOMS.validate_atoms_workers.read_io import LimitReached, ReadContext, open_regular
from VALIDATE_ATOMS.validate_atoms_workers.settings import CEILINGS

_ROLE_DIRECTORY_BY_ID_KIND = {
    "C": "01_concern", "A": "02_analysis", "P": "03_plan", "R": "04_requirement",
    "M": "05_method", "E": "06_evaluation", "D": "07_delivery", "O": "09_operations",
}
_IdentityRecord = tuple[Path, str | None, dict[str, Any] | None, bytes | None]
_IdentityRecords = tuple[_IdentityRecord, ...]


class CurrentAtomLocatorError(ToolError):
    """A safe current path could not be established for the requested identity."""


def _fail(code: str, message: str, details: dict[str, Any] | None = None) -> None:
    raise CurrentAtomLocatorError(code, message, details)


def _hint(root: Path, atom_id: str, reference: str | Path, reader: ReadContext) -> Path | None:
    raw = Path(reference)
    if raw.is_absolute():
        try:
            raw = raw.relative_to(root)
        except ValueError:
            _fail("atom-path-outside-project", "Atom path hint is outside the selected Project")
    if not raw.parts or ".." in raw.parts or "\x00" in str(raw):
        _fail("atom-path-invalid", "Atom path hint is not a safe Project-relative path")
    path = root / raw
    try:
        reader.allowed(path)
    except (OSError, RuntimeError, ValueError) as error:
        raise CurrentAtomLocatorError("atom-path-unavailable", "Atom path hint traverses an unsafe or unavailable path") from error
    if not path.exists() and not path.is_symlink():
        return None
    try:
        metadata = parse_carrier(reader.read(path), path).metadata
    except (OSError, RuntimeError, ValueError, CarrierError) as error:
        raise CurrentAtomLocatorError("atom-path-unavailable", "Atom path hint is present but cannot be safely read") from error
    if metadata.get("atom_id") != atom_id:
        _fail("atom-path-identity-mismatch", "Atom path hint identifies a different Atom")
    return path


def _possible_claim(raw: bytes, atom_id: str, filename_id: str | None) -> bool:
    if filename_id == atom_id:
        return True
    normalized = raw.replace(b"\r\n", b"\n")
    header = normalized.split(b"\n---\n", 1)[0] if normalized.startswith(b"---\n") else b""
    text = header.decode("utf-8", errors="replace")
    for claim in re.findall(r"(?m)^(?:atom_id|\"atom_id\"|'atom_id')\s*:\s*([^\n]*)$", text):
        try:
            if yaml.safe_load(claim) == atom_id:
                return True
        except yaml.YAMLError:
            pass
    return re.search(r"(?<![A-Za-z0-9_-])" + re.escape(atom_id) + r"(?![A-Za-z0-9_-])", text) is not None


def _excluded(path: Path, control: Path, delivery_roots: set[Path]) -> bool:
    relative = path.relative_to(control)
    if "_projection" in relative.parts:
        return True
    if any(path.is_relative_to(delivery) for delivery in delivery_roots):
        return True
    if any(part.casefold() in {"journal", "journals", "draft", "drafts", "archive", "archived"}
           for part in relative.parts[:-1]):
        return True
    # Do not enter another Project nested beneath a registered authority path.
    if any(part.startswith(".caprmedio_") for part in relative.parts[:-1]):
        return True
    return False


def _role_directories(authority: Path, reader: ReadContext, selected_role: str | None) -> tuple[Path, ...]:
    reader.allowed(authority)
    descriptor = open_regular(authority, directory=True)
    try:
        with os.scandir(descriptor) as entries:
            result = []
            for entry in entries:
                reader.checkpoint()
                if ROLE_DIRECTORY.fullmatch(entry.name) and (selected_role is None or entry.name == selected_role):
                    path = authority / entry.name
                    if entry.is_symlink():
                        _fail("atom-identity-source-unsafe", "A registered Atom role folder is symlinked")
                    if entry.is_dir(follow_symlinks=False):
                        result.append(path)
            return tuple(sorted(result))
    finally:
        os.close(descriptor)


def _registered_roots(selection: ProjectSelection, root: Path, control: Path) -> tuple[set[Path], set[Path]]:
    authorities: set[Path] = set()
    deliveries: set[Path] = set()
    for row in selection.structure.get("scope_units", ()):
        if not isinstance(row, Mapping):
            continue
        authority = row.get("authority_path")
        delivery = row.get("delivery_path")
        if isinstance(authority, str):
            path = root / authority
            if path.is_relative_to(control):
                authorities.add(path)
        if isinstance(delivery, str):
            path = root / delivery
            if path.is_relative_to(control):
                deliveries.add(path)
    return authorities, deliveries


def _read_records(candidates: set[Path], reader: ReadContext) -> _IdentityRecords:
    records: list[_IdentityRecord] = []
    for candidate in sorted(candidates):
        if candidate.suffix.lower() != ".md":
            continue
        filename = ATOM_ID.search(candidate.name)
        filename_id = filename.group(1) if filename else None
        if candidate.is_symlink():
            records.append((candidate, filename_id, None, None))
            continue
        try:
            raw = reader.read(candidate)
            records.append((candidate, filename_id, parse_carrier(raw, candidate).metadata, None))
        except CarrierError:
            records.append((candidate, filename_id, None, raw))
    return tuple(records)


def _selected_role(atom_id: str) -> str | None:
    kind = re.fullmatch(r"CA-([CAPRMEDO])-[0-9]+", atom_id)
    return _ROLE_DIRECTORY_BY_ID_KIND.get(kind.group(1)) if kind else None


def _matching_paths(records: _IdentityRecords, atom_id: str) -> list[Path]:
    found = []
    for candidate, filename_id, metadata, raw in records:
        if candidate.is_symlink():
            if filename_id == atom_id:
                _fail("atom-identity-source-unsafe", "The matching current Atom path is symlinked")
            continue
        if metadata is None:
            if raw is not None and _possible_claim(raw, atom_id, filename_id):
                _fail("atom-identity-source-ambiguous", "A malformed current carrier may claim this Atom identity")
            continue
        if "projection" in metadata or metadata.get("artifact_form") == "Projection":
            continue
        status = metadata.get("status")
        if isinstance(status, str) and status.casefold() in {"draft", "archived"}:
            continue
        identity = metadata.get("atom_id")
        if filename_id is not None and filename_id != identity and (filename_id == atom_id or identity == atom_id):
            _fail("atom-identity-source-ambiguous", "A current filename conflicts with its Atom identity")
        if identity == atom_id:
            found.append(candidate)
    return found


class CurrentAtomLocator:
    """One admission's ephemeral, bounded index of requested role families."""

    def __init__(self, root: str | Path, *, reader: ReadContext | None = None) -> None:
        self.root = Path(root).resolve()
        self.reader = reader if reader is not None else ReadContext(roots=[str(self.root)], limits=dict(CEILINGS))
        self._selection: ProjectSelection | None = None
        self._records: dict[str | None, _IdentityRecords] = {}
        self._role_roots: dict[tuple[Path, str | None], tuple[Path, ...]] = {}

    def _index(self, selected_role: str | None) -> _IdentityRecords:
        if selected_role in self._records:
            return self._records[selected_role]
        try:
            selection = self._selection or active_selection(self.root)
            self._selection = selection
            control = selection.control_root
            authorities, deliveries = _registered_roots(selection, self.root, control)
            candidates: set[Path] = set()
            for authority in sorted(authorities):
                try:
                    role_roots = _role_directories(authority, self.reader, selected_role)
                except FileNotFoundError:
                    self._role_roots[(authority, selected_role)] = ()
                    continue
                self._role_roots[(authority, selected_role)] = role_roots
                for role_root in role_roots:
                    candidates.update(path for path in self.reader.inventory(role_root)
                                      if path.is_relative_to(control) and not _excluded(path, control, deliveries))
            self._records[selected_role] = _read_records(candidates, self.reader)
            return self._records[selected_role]
        except CurrentAtomLocatorError:
            raise
        except (OSError, RuntimeError, LimitReached, ProjectSelectionError) as error:
            raise CurrentAtomLocatorError("atom-identity-inventory-unavailable", "Current Project Atom identity inventory is unavailable") from error

    def locate(self, atom_id: str, reference: str | Path) -> str:
        """Return the hinted source or resolve a missing hint by stable ID."""
        path = _hint(self.root, atom_id, reference, self.reader)
        if path is not None:
            return path.relative_to(self.root).as_posix()
        found = _matching_paths(self._index(_selected_role(atom_id)), atom_id)
        if len(found) != 1:
            code = "atom-identity-duplicate" if found else "atom-identity-not-found"
            _fail(code, "Atom identity does not resolve to exactly one current carrier", {"atom_id": atom_id})
        return found[0].relative_to(self.root).as_posix()

    def assert_unique_current_claim(self, atom_id: str, expected_path: str | Path) -> None:
        """Require one current claim for this ID, at exactly the expected path."""
        expected = Path(expected_path)
        if expected.is_absolute():
            try:
                expected = expected.relative_to(self.root)
            except ValueError:
                _fail("atom-path-outside-project", "Expected Atom path is outside the selected Project")
        if not expected.parts or ".." in expected.parts or "\x00" in str(expected):
            _fail("atom-path-invalid", "Expected Atom path is not a safe Project-relative path")
        expected_absolute = self.root / expected
        try:
            self.reader.allowed(expected_absolute)
        except (OSError, RuntimeError, ValueError) as error:
            raise CurrentAtomLocatorError(
                "atom-path-unavailable", "Expected Atom path traverses an unsafe or unavailable path"
            ) from error

        found = _matching_paths(self._index(_selected_role(atom_id)), atom_id)
        if len(found) != 1:
            code = "atom-identity-duplicate" if found else "atom-identity-not-found"
            _fail(code, "Atom identity does not resolve to exactly one current carrier", {"atom_id": atom_id})
        if found[0] != expected_absolute:
            _fail(
                "atom-identity-path-mismatch",
                "Atom identity resolves to a different current carrier path",
                {"atom_id": atom_id},
            )
        self.revalidate()

    def revalidate(self) -> None:
        """Check one complete read snapshot after the admission has used it."""
        try:
            for (authority, role), before in self._role_roots.items():
                try:
                    after = _role_directories(authority, self.reader, role)
                except FileNotFoundError:
                    after = ()
                if after != before:
                    _fail("atom-identity-source-changed", "Registered Atom role folders changed during lookup")
            if self.reader.currentness()["state"] != "unchanged":
                _fail("atom-identity-source-changed", "Current Atom identity sources changed during lookup")
        except CurrentAtomLocatorError:
            raise
        except (OSError, RuntimeError, LimitReached) as error:
            raise CurrentAtomLocatorError("atom-identity-inventory-unavailable", "Current Atom identity revalidation is unavailable") from error


def locate_current_atom(root: str | Path, atom_id: str, reference: str | Path,
                        *, reader: ReadContext | None = None) -> str:
    """One-shot wrapper retaining the original lookup API and snapshot check."""
    locator = CurrentAtomLocator(root, reader=reader)
    resolved = locator.locate(atom_id, reference)
    locator.revalidate()
    return resolved
