"""Bounded, source-bound inventory of explicit proposed-carrier targets.

This module deliberately does not infer Atom identity from a filename.  It is a
small pre-write helper: callers supply only direct IDs mentioned by a proposed
carrier and the already-verified Project Structure mapping. For a nested Plan
it additionally resolves the one-way ``is_decomposition_of`` parent chain;
a typed Plan with blocks also retains its reachable prerequisite evidence.
It does *not* claim to inventory the project's complete graph.
"""

from __future__ import annotations

import os
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Iterable, Mapping

from .parsing import CarrierError, parse_carrier
from .read_io import LimitReached, ReadContext, ReadFailure, open_regular, protected
from .settings import CEILINGS


class ProposedReferenceError(ValueError):
    """An explicit target cannot be safely and completely inventoried."""


@dataclass(frozen=True)
class TargetCarrier:
    """Authenticated carrier facts retained for a direct reference or Plan parent."""

    atom_id: str
    status: str
    version: int
    path: str
    sha256: str
    metadata: dict[str, Any]


@dataclass(frozen=True)
class ProposedReferenceInventory:
    """Finite direct, parent-placement and reachable prerequisite evidence."""

    direct_targets: tuple[TargetCarrier, ...]
    plan_parent_closure: tuple[TargetCarrier, ...]
    plan_prerequisite_closure: tuple[TargetCarrier, ...] = ()
    _evidence: _ReferenceEvidence | None = field(default=None, repr=False, compare=False)

    def assert_current(self) -> None:
        """Recheck captured reference evidence at the caller's admission boundary."""
        if self._evidence is None:
            raise ProposedReferenceError("authoritative target currentness evidence is unavailable")
        self._evidence.assert_current()


@dataclass(frozen=True)
class _FrontierCarrier:
    metadata: dict[str, Any]
    role: str
    owner: str
    placement_matches: bool
    archived: bool


@dataclass(frozen=True)
class _ReferenceEvidence:
    reader: ReadContext
    roots: dict[Path, str]
    roles: dict[str, str]
    statuses: dict[str, dict[str, str]]
    paths: frozenset[Path]
    directories: tuple[str, ...]

    def assert_current(self) -> None:
        try:
            carriers, directories = _frontier(self.reader, self.roots, self.roles, self.statuses)
            current = self.reader.currentness()
        except (OSError, CarrierError, ReadFailure, LimitReached) as error:
            raise ProposedReferenceError("authoritative target frontier changed during admission") from error
        if frozenset(carriers) != self.paths or directories != self.directories or current.get("state") != "unchanged":
            raise ProposedReferenceError("authoritative target frontier changed during admission")


def _relative(root: Path, value: str | Path) -> Path:
    path = Path(value)
    if path.is_absolute() or any(part == ".." for part in path.parts):
        raise ProposedReferenceError("reference path is outside the project")
    absolute = root / path
    if not absolute.is_relative_to(root):
        raise ProposedReferenceError("reference path is outside the project")
    return absolute


def _authority_roots(
    root: Path, structure: Mapping[str, Any], project_authority_paths: Iterable[str | Path],
    project_name: str | None,
) -> dict[Path, str]:
    units = structure.get("scope_units")
    if not isinstance(units, list):
        raise ProposedReferenceError("Project Structure authority paths are unavailable")
    paths = [(path, project_name) for path in project_authority_paths]
    for unit in units:
        path = unit.get("authority_path") if isinstance(unit, Mapping) else None
        if not isinstance(path, str) or not path:
            raise ProposedReferenceError("Project Structure authority path is invalid")
        paths.append((path, unit.get("scope_unit_name")))
    roots: dict[Path, str] = {}
    for path, owner in paths:
        if not isinstance(path, (str, Path)) or not Path(path).parts:
            raise ProposedReferenceError("Project authority path is invalid")
        if not isinstance(owner, str) or not owner:
            raise ProposedReferenceError("Project authority owner is invalid")
        candidate = _relative(root, path)
        if candidate in roots and roots[candidate] != owner:
            raise ProposedReferenceError("Project authority owner is ambiguous")
        roots[candidate] = owner
    if not roots:
        raise ProposedReferenceError("Project Structure has no authoritative carrier frontier")
    return roots


def _folder(value: object) -> str:
    if not isinstance(value, str) or not value or Path(value).parts != (value,) or value in {".", ".."}:
        raise ProposedReferenceError("carrier-directory authority is invalid")
    return value


def _container_id(metadata: Mapping[str, Any], role: str, owner: str, statuses: Mapping[str, str], local: str) -> str | None:
    atom_id = metadata.get("atom_id")
    kind = metadata.get("type")
    if (
        isinstance(atom_id, str) and atom_id
        and metadata.get("content_role") == role
        and metadata.get("current_scope_unit") == owner
        and isinstance(metadata.get("status"), str)
        and statuses.get(metadata["status"]) == local
        and type(metadata.get("version")) is int and metadata["version"] > 0
        and isinstance(kind, str)
        and ((role == "Plan" and kind == "Plan") or (role == "Operations" and kind in {"Workflow", "Step"}))
    ):
        return atom_id
    return None


def _frontier(
    reader: ReadContext, roots: Mapping[Path, str], roles: Mapping[str, str],
    statuses: Mapping[str, Mapping[str, str]],
) -> tuple[dict[Path, _FrontierCarrier], tuple[str, ...]]:
    """Read only exact role/status directories and authenticated sibling bundles."""
    if not roles or any(not isinstance(role, str) or not role for role in roles):
        raise ProposedReferenceError("role-directory authority is unavailable")
    for mapping in statuses.values():
        for status, folder in mapping.items():
            if not isinstance(status, str) or not status:
                raise ProposedReferenceError("status-directory authority is invalid")
            if folder != "":
                _folder(folder)
    pending: list[tuple[Path, str, str, str, str | None, bool, bool, Path]] = [
        (base / _folder(folder), role, owner, "", None, False, False, base)
        for base, owner in roots.items() for role, folder in roles.items()
    ]
    visited: set[Path] = set()
    directories: set[str] = set()
    found: dict[Path, _FrontierCarrier] = {}
    while pending:
        path, role, owner, local, parent_id, steps_only, archived, authority_root = pending.pop()
        # Each declared Scope Unit owns its subtree independently of ancestor bundles.
        if any(base != authority_root and base.is_relative_to(authority_root) and path.is_relative_to(base) for base in roots):
            continue
        if path in visited:
            continue
        visited.add(path)
        reader.allowed(path)
        try:
            descriptor = open_regular(path, directory=True)
        except FileNotFoundError:
            continue
        directories.add(str(path))
        files: list[Path] = []
        containers: set[str] = set()
        try:
            with os.scandir(descriptor) as entries:
                for count, entry in enumerate(entries, 1):
                    reader.checkpoint()
                    child = path / entry.name
                    is_directory = entry.is_dir(follow_symlinks=False)
                    if (not is_directory and child.suffix.lower() == ".md") or (
                        entry.is_file(follow_symlinks=False) and protected(child)
                    ):
                        files.append(child)
                    if is_directory or entry.is_symlink():
                        containers.add(entry.name)
                    if count > 1_000_000:
                        raise ReadFailure("Directory traversal exceeds host ceiling.")
        finally:
            os.close(descriptor)
        if len(found) + len(files) > reader.limits["max_candidates"]:
            raise LimitReached("max_candidates")
        role_statuses = statuses.get(role, {})
        if not local:
            pending.extend(
                (path / folder, role, owner, folder, parent_id, steps_only, archived or status.casefold() == "archived", authority_root)
                for status, folder in role_statuses.items() if folder
            )
        for child in sorted(files):
            raw = reader.read(child)
            metadata = parse_carrier(raw, child).metadata
            status = metadata.get("status")
            found[child] = _FrontierCarrier(
                metadata, role, owner,
                bool(role_statuses) and isinstance(status, str) and role_statuses.get(status) == local,
                archived,
            )
            if steps_only and (metadata.get("content_role"), metadata.get("type")) != ("Operations", "Step"):
                raise ProposedReferenceError("Workflow and Step containers admit only Step carriers")
            if role == "Plan" and parent_id is not None and metadata.get("content_role") == "Plan":
                if _parent_id(metadata) != parent_id:
                    raise ProposedReferenceError("nested Plan path does not use the authenticated Markdown parent carrier")
            if child.stem in containers:
                identity = _container_id(metadata, role, owner, role_statuses, local)
                if identity is not None:
                    pending.append((child.with_suffix(""), role, owner, "", identity, role == "Operations", archived, authority_root))
        if len(pending) + len(visited) > 1_000_000:
            raise ReadFailure("Directory traversal exceeds host ceiling.")
    return found, tuple(sorted(directories))


def _carrier(
    reader: ReadContext, root: Path, path: Path, requested: set[str], carrier: _FrontierCarrier,
) -> TargetCarrier | None:
    metadata = carrier.metadata
    atom_id, status, version = metadata.get("atom_id"), metadata.get("status"), metadata.get("version")
    if not isinstance(atom_id, str) or atom_id not in requested:
        return None
    if (
        not isinstance(status, str)
        or type(version) is not int
        or version < 1
    ):
        raise ProposedReferenceError("authoritative target carrier lacks explicit identity, status, or version")
    if metadata.get("content_role") != carrier.role or metadata.get("current_scope_unit") != carrier.owner or not carrier.placement_matches:
        raise ProposedReferenceError("authoritative target carrier disagrees with its role, owner, or status placement")
    return TargetCarrier(
        atom_id=atom_id,
        status=status,
        version=version,
        path=str(path.relative_to(root)),
        sha256=reader.fingerprints[str(path)],
        metadata=dict(metadata),
    )


def _is_active_status(status: str) -> bool:
    """Accept the two source-admitted logical Active spellings without rewriting it."""
    return status in {"Active", "active"}


def _parent_id(metadata: Mapping[str, Any]) -> str | None:
    relations = metadata.get("relations", {})
    if not isinstance(relations, Mapping):
        raise ProposedReferenceError("Plan parent relation is malformed")
    parents = relations.get("is_decomposition_of", [])
    if parents is None:
        parents = []
    if not isinstance(parents, list) or len(parents) > 1 or any(not isinstance(item, str) or not item for item in parents):
        raise ProposedReferenceError("Plan parent relation is malformed")
    return parents[0] if parents else None


def _plan_container(
    parent_path: Path,
    child_status: object,
    admitted_plan_status_folders: Mapping[str, str] | None,
) -> Path:
    """Return the source-admitted local container for a child Plan status."""
    if not isinstance(child_status, str):
        raise ProposedReferenceError("nested Plan status is malformed")
    container = parent_path.with_suffix("")
    if child_status == "Active":
        return container
    if admitted_plan_status_folders is None:
        raise ProposedReferenceError("nested Plan status-folder authority is unavailable")
    folder = admitted_plan_status_folders.get(child_status)
    folder_path = Path(folder) if isinstance(folder, str) else None
    if (
        folder_path is None
        or not folder
        or folder_path.is_absolute()
        or len(folder_path.parts) != 1
        or folder_path.parts[0] in {".", ".."}
    ):
        raise ProposedReferenceError("nested Plan status-folder authority is invalid")
    return container / folder_path


def inventory_proposed_references(
    root: Path,
    project_structure: Mapping[str, Any],
    direct_atom_ids: Iterable[str],
    *,
    admitted_role_folders: Mapping[str, str],
    admitted_status_folders: Mapping[str, Mapping[str, str]],
    candidate_metadata: Mapping[str, Any] | None = None,
    candidate_path: str | Path | None = None,
    admitted_plan_status_folders: Mapping[str, str] | None = None,
    project_authority_paths: Iterable[str | Path] = (),
    project_name: str | None = None,
) -> ProposedReferenceInventory:
    """Return exact current facts for named targets and a nested Plan parent chain.

    ``direct_atom_ids`` is finite and explicit. Ordinary targets remain Active.
    A Plan's blocks-only endpoints instead resolve the current authenticated
    Plan Revision under the verified complete Plan status/history mapping.
    If ``candidate_metadata`` is a Plan with a parent,
    ``candidate_path`` is required and each child is checked to reside below the
    *actual authenticated parent carrier*.  A non-Active child Plan additionally
    requires its container folder from ``admitted_plan_status_folders``; callers
    must derive that finite mapping from validated CA-D-461 source evidence.
    ``project_authority_paths`` is an internal binding of exact Project roots
    from validated selected Project Settings and CA-D-324 source evidence.
    Atom IDs never come from filenames.  A changed frontier, unsafe file,
    duplicate, missing or inactive named target raises
    ``ProposedReferenceError``.
    """
    root = root.resolve()
    ids = tuple(direct_atom_ids)
    if not ids or any(not isinstance(item, str) or not item for item in ids) or len(set(ids)) != len(ids):
        raise ProposedReferenceError("direct target IDs must be a finite unique nonempty set")
    reader = ReadContext(roots=[str(root)], limits=dict(CEILINGS))
    try:
        roots = _authority_roots(root, project_structure, project_authority_paths, project_name)
        carriers, directories = _frontier(reader, roots, admitted_role_folders, admitted_status_folders)
    except (OSError, CarrierError, ReadFailure, LimitReached) as error:
        raise ProposedReferenceError("authoritative carrier frontier is unavailable") from error

    requested = set(ids)
    blocking: set[str] = set()
    typed_plan = candidate_metadata is not None and (candidate_metadata.get("content_role"), candidate_metadata.get("type")) == ("Plan", "Plan")
    if typed_plan:
        relations = candidate_metadata.get("relations", {})
        if isinstance(relations, Mapping) and isinstance(relations.get("blocks"), list):
            blocking = {value for value in relations["blocks"] if isinstance(value, str)}
            blocking.difference_update(
                value for kind, values in relations.items() if kind != "blocks" and isinstance(values, list)
                for value in values if isinstance(value, str)
            )
            blocking.intersection_update(requested)

    def current_plan(identity: str) -> TargetCarrier:
        # Keep prerequisite evidence on the same accepted current/history policy.
        from contained_atom_targets import ContainedAtomTargetsError, _latest_path

        if admitted_plan_status_folders is None or dict(admitted_plan_status_folders) != dict(admitted_status_folders.get("Plan", {})):
            raise ProposedReferenceError("Plan blocking status-directory authority is unavailable or inconsistent")
        for carrier in carriers.values():
            if carrier.metadata.get("atom_id") != identity:
                continue
            if carrier.role != "Plan" or (carrier.metadata.get("content_role"), carrier.metadata.get("type")) != ("Plan", "Plan"):
                raise ProposedReferenceError("Plan blocking target is not a Plan carrier")
            if not isinstance(carrier.metadata.get("status"), str):
                raise ProposedReferenceError("Plan blocking target lacks carried Status")
        plan_carriers = {path: carrier for path, carrier in carriers.items() if carrier.role == "Plan"}
        try:
            path = _latest_path(identity, plan_carriers, admitted_status_folders)
        except ContainedAtomTargetsError as error:
            raise ProposedReferenceError("Plan blocking target current Revision is unresolved") from error
        item = _carrier(reader, root, path, {identity}, carriers[path])
        if item is None:
            raise ProposedReferenceError("Plan blocking target is missing")
        return item

    active: dict[str, TargetCarrier] = {}
    inactive: set[str] = set()
    for path, carrier in carriers.items():
        identity = carrier.metadata.get("atom_id")
        if isinstance(identity, str) and identity in blocking:
            if carrier.role != "Plan" or (carrier.metadata.get("content_role"), carrier.metadata.get("type")) != ("Plan", "Plan"):
                raise ProposedReferenceError("Plan blocking target is not a Plan carrier")
            if not isinstance(carrier.metadata.get("status"), str):
                raise ProposedReferenceError("Plan blocking target lacks carried Status")
            continue
        if carrier.archived:
            atom_id = carrier.metadata.get("atom_id")
            if isinstance(atom_id, str) and atom_id in requested:
                inactive.add(atom_id)
            continue
        item = _carrier(reader, root, path, requested, carrier)
        if item is None:
            continue
        if not _is_active_status(item.status):
            inactive.add(item.atom_id)
            continue
        if item.atom_id in active:
            raise ProposedReferenceError("named authoritative target is ambiguous")
        active[item.atom_id] = item
    if blocking:
        for identity in blocking:
            active[identity] = current_plan(identity)
    missing = requested - set(active)
    if missing:
        if missing & inactive:
            raise ProposedReferenceError("named authoritative target is inactive or archived")
        raise ProposedReferenceError("named authoritative target is missing")

    closure: list[TargetCarrier] = []
    if candidate_metadata is not None:
        if candidate_metadata.get("content_role") == "Plan":
            parent = _parent_id(candidate_metadata)
            if parent is not None:
                if candidate_path is None:
                    raise ProposedReferenceError("nested Plan requires its actual carrier path")
                child_path = _relative(root, candidate_path)
                child_status = candidate_metadata.get("status")
                seen: set[str] = set()
                while parent is not None:
                    if parent in seen:
                        raise ProposedReferenceError("Plan parent closure contains a cycle")
                    seen.add(parent)
                    if parent not in active:
                        # Resolve only the newly named parent, retaining the same
                        # bounded frontier and then repeat the ordinary admission.
                        matches = []
                        for path, carrier in carriers.items():
                            if carrier.archived:
                                continue
                            item = _carrier(reader, root, path, {parent}, carrier)
                            if item is not None and item.atom_id == parent:
                                matches.append((path, item))
                        admitted = [
                            (path, item)
                            for path, item in matches
                            if _is_active_status(item.status)
                        ]
                        if len(admitted) != 1:
                            raise ProposedReferenceError("Plan parent is missing, inactive, or ambiguous")
                        active[parent] = admitted[0][1]
                    item = active[parent]
                    if not _is_active_status(item.status):
                        raise ProposedReferenceError("Plan parent is missing, inactive, or ambiguous")
                    if (item.metadata.get("content_role"), item.metadata.get("type")) != ("Plan", "Plan"):
                        raise ProposedReferenceError("Plan parent is not a Plan carrier")
                    closure.append(item)
                    parent = _parent_id(item.metadata)
                # Resolve the entire identity closure before physical checks, so
                # a genuine cycle cannot be hidden by an incidental bad layout.
                for item in closure:
                    parent_path = root / item.path
                    if child_path.parent != _plan_container(
                        parent_path, child_status, admitted_plan_status_folders,
                    ):
                        raise ProposedReferenceError("nested Plan path does not use the authenticated Markdown parent carrier")
                    child_path = parent_path
                    child_status = item.status
    prerequisites: dict[str, TargetCarrier] = {}
    candidate_relations = candidate_metadata.get("relations", {}) if typed_plan else {}
    if typed_plan and isinstance(candidate_relations, Mapping) and candidate_relations.get("blocks"):
        candidate_id = candidate_metadata.get("atom_id")
        if not isinstance(candidate_id, str) or not candidate_id:
            raise ProposedReferenceError("Plan prerequisite closure requires its carried identity")
        pending = [candidate_metadata]
        visited = {candidate_id}
        retained = requested | {item.atom_id for item in closure}
        try:
            while pending:
                reader.checkpoint()
                metadata = pending.pop()
                relations = metadata.get("relations", {})
                if not isinstance(relations, Mapping):
                    raise ProposedReferenceError("Plan prerequisite relations are malformed")
                parent = _parent_id(metadata)
                blocks = relations.get("blocks", [])
                if not isinstance(blocks, list) or any(not isinstance(value, str) or not value for value in blocks):
                    raise ProposedReferenceError("Plan prerequisite blocks relation is malformed")
                for identity in ([parent] if parent is not None else []) + blocks:
                    reader.checkpoint()
                    if identity in visited:
                        continue
                    visited.add(identity)
                    item = current_plan(identity)
                    if identity not in retained:
                        prerequisites[identity] = item
                    pending.append(item.metadata)
        except (OSError, CarrierError, ReadFailure, LimitReached) as error:
            raise ProposedReferenceError("Plan prerequisite closure exceeds its authenticated read boundary") from error
    evidence = _ReferenceEvidence(
        reader, dict(roots), dict(admitted_role_folders),
        {role: dict(mapping) for role, mapping in admitted_status_folders.items()},
        frozenset(carriers), directories,
    )
    evidence.assert_current()
    return ProposedReferenceInventory(
        tuple(active[item] for item in ids), tuple(closure), tuple(prerequisites.values()), evidence,
    )
