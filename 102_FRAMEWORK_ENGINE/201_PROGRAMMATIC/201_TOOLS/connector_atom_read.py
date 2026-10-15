"""Effect-free Atom backend mechanics; callers must bind authority separately.

Every argument is receiver-bound private input, never a public physical selector.
These helpers do not admit a request, create a Run, or expose a new Tool.
"""

from __future__ import annotations

import hashlib
import re
from collections import Counter
from dataclasses import dataclass
from pathlib import Path

from atom_operations import ATOM_ID, _lifecycle, _role_directory
from atom_subject_lookup import _owner_for
from connector_atom_parse import IDENTITY, LIFECYCLES, matches, parse_atom, validate_filters
from subject_notation import SubjectNotationError
from VALIDATE_ATOMS.validate_atoms_workers.parsing import CarrierError
from VALIDATE_ATOMS.validate_atoms_workers.read_io import LimitReached, ReadContext
from VALIDATE_ATOMS.validate_atoms_workers.settings import CEILINGS


class AtomReadError(ValueError):
    def __init__(self, code: str, message: str, field: str | None = None):
        super().__init__(message)
        self.code, self.field = code, field


@dataclass(frozen=True)
class AtomSourceView:
    root: Path
    control: Path
    owners: dict[str, Path]
    scope_units: tuple[str, ...]
    lifecycles: tuple[str, ...]
    source_view: str
    subject_profile: str
    installed_roots: tuple[Path, ...]
    attribution: object


def _sources(view: AtomSourceView, bound_sources=None):
    if (view.source_view not in {"current", "history", "all"} or not view.scope_units
            or not set(view.scope_units) <= view.owners.keys() or not view.lifecycles
            or not set(view.lifecycles) <= LIFECYCLES
            or view.attribution is None):
        raise AtomReadError("input_invalid", "An explicit complete private source view is required.", "context")
    root, control = view.root, view.control
    if not root.is_absolute() or not control.is_relative_to(root):
        raise AtomReadError("input_invalid", "Source roots must be bound inside the Project.", "context")
    reader = ReadContext(roots=[str(root)], limits=dict(CEILINGS))
    observed, originals = [], []
    try:
        for path in reader.inventory(control):
            relative = path.relative_to(control)
            if path.is_symlink() and _owner_for(path, view.owners) in view.scope_units:
                raise AtomReadError("schema_invalid", "The supplied frontier contains a symlink source.", "context")
            if ("_projection" in relative.parts or _role_directory(path, control) is None
                    or any(path.is_relative_to(place) for place in view.installed_roots)):
                continue
            lifecycle = _lifecycle(path, control)
            owner = _owner_for(path, view.owners)
            selected = owner in view.scope_units and lifecycle in view.lifecycles
            if (lifecycle == "draft" or (view.source_view == "current" and lifecycle == "archived")
                    or (view.source_view == "history" and lifecycle != "archived")):
                continue
            raw = None
            try:
                raw = reader.read(path)
                parsed = parse_atom(raw)
            except (OSError, CarrierError) as error:
                # An identity claim cannot disappear as a plain Markdown note.
                if (raw is None and selected) or ATOM_ID.search(path.name) or (raw is not None and re.search(rb"(?m)^atom_id:", raw)):
                    raise AtomReadError("schema_invalid", "An Atom source is unreadable or malformed.", "context") from error
                continue
            properties = parsed.metadata
            if "projection" in properties:
                continue
            filename_id = ATOM_ID.search(path.name)
            if ((filename_id and filename_id.group(1) != properties["atom_id"])
                    or properties["current_scope_unit"] != owner):
                raise AtomReadError("schema_invalid", "Atom source identity or ownership is inconsistent.", "context")
            historical = lifecycle == "archived" or properties["status"].casefold() == "archived"
            if not historical:
                originals.append(properties["atom_id"])
            if (not selected or (view.source_view == "current" and historical)
                    or (view.source_view == "history" and not historical)):
                continue
            state = {"identity": properties["atom_id"], "version": properties["version"],
                     "source_token": hashlib.sha256(raw).hexdigest(), "source_view": view.attribution}
            observed.append((path, raw, parsed, state))
        if any(count > 1 for count in Counter(originals).values()):
            raise AtomReadError("target_ambiguous", "The source inventory has competing original identities.", "context")
        if bound_sources is not None:
            pins = {str(source.root / source.relative_path): source.sha256 for source in bound_sources}
            if pins != reader.fingerprints:
                raise AtomReadError("stale_state", "Observed source frontier differs from its exact admitted pins.", "context")
        if reader.currentness()["state"] != "unchanged":
            raise AtomReadError("stale_state", "The source inventory changed during observation.", "context")
    except (OSError, LimitReached) as error:
        raise AtomReadError("backend_failure", "The complete Atom source frontier is unavailable.", "context") from error
    return observed


def query_atoms(filters: dict, view: AtomSourceView, *, bound_sources=None) -> dict:
    """Observe all matches, without full reads, defaults or mutation effects."""
    try:
        validate_filters(filters)
    except (ValueError, TypeError) as error:
        raise AtomReadError("input_invalid", str(error), "query") from error
    if set(filters["scope_units"]) != set(view.scope_units) or set(filters["lifecycles"]) != set(view.lifecycles):
        raise AtomReadError("input_invalid", "Query frontier disagrees with its bound source view.", "query")
    data, states = [], []
    for _, _, parsed, state in _sources(view, bound_sources):
        try:
            selected = matches(parsed.metadata, filters, view.subject_profile)
        except (ValueError, SubjectNotationError) as error:
            raise AtomReadError("schema_invalid", "Source Subject syntax is unsupported by the supplied profile.", "context") from error
        if selected:
            row = {field: parsed.metadata.get(field) for field in filters["result_fields"]}
            row.update(atom_id=state["identity"], version=state["version"], current_scope_unit=parsed.metadata["current_scope_unit"])
            data.append(row)
            states.append(state)
    return {"data": {"matches": data, "complete": True, "source_view": view.attribution},
            "current_state": states, "effects": [], "errors": []}


def read_atom(identity: str, view: AtomSourceView, expected_state: dict | None = None, *, bound_sources=None) -> dict:
    """Read one exact identity independently; optional pins never choose a view."""
    if not isinstance(identity, str) or IDENTITY.fullmatch(identity) is None:
        raise AtomReadError("input_invalid", "Read requires one full logical Atom ID.", "target")
    if expected_state is not None and (not isinstance(expected_state, dict) or not expected_state
            or not expected_state.keys() <= {"identity", "version", "source_token", "source_view"}):
        raise AtomReadError("input_invalid", "Read pin must be exact observed state evidence.", "expected_state")
    if expected_state is not None and "version" in expected_state and (type(expected_state["version"]) is not int or expected_state["version"] < 1):
        raise AtomReadError("input_invalid", "Pinned Atom Version must be a positive integer.", "expected_state")
    found = [entry for entry in _sources(view, bound_sources) if entry[3]["identity"] == identity]
    if not found:
        raise AtomReadError("target_not_found", "The exact Atom is unavailable in the supplied source view.", "target")
    if expected_state is not None:
        found = [entry for entry in found if all(entry[3][field] == value for field, value in expected_state.items())]
        if not found:
            raise AtomReadError("stale_state", "Observed Atom state differs from the supplied exact pin.", "expected_state")
    if len(found) != 1:
        raise AtomReadError("target_ambiguous", "The supplied source view does not identify one Atom revision.", "target")
    _, _, parsed, state = found[0]
    data = {"atom_id": identity, "version": state["version"], "current_scope_unit": parsed.metadata["current_scope_unit"],
            "frontmatter": parsed.frontmatter, "content": parsed.body, "source": parsed.text}
    return {"data": data, "current_state": state, "effects": [], "errors": []}
