"""Private, read-only discovery of one source-bound P/O containment tree.

This is not a lifecycle receiver or an execution order. Each later single-Atom
action must rebind its source after any preceding placement change.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import os
import re

from VALIDATE_ATOMS.validate_atoms_workers.parsing import CarrierError
from VALIDATE_ATOMS.validate_atoms_workers.proposed_carrier import (
    ProposedCarrierError, VerifiedSourceContext, _current, _frontier_status_folders,
)
from VALIDATE_ATOMS.validate_atoms_workers.proposed_references import (
    ProposedReferenceError, TargetCarrier, _authority_roots, _carrier,
    _container_id, _frontier,
)
from VALIDATE_ATOMS.validate_atoms_workers.read_io import LimitReached, ReadContext, ReadFailure, open_regular
from VALIDATE_ATOMS.validate_atoms_workers.settings import CEILINGS


class ContainedAtomTargetsError(ValueError):
    """The requested current containment tree cannot be proved safely."""


@dataclass(frozen=True)
class ContainedAtomTarget:
    atom_id: str
    content_role: str
    atom_type: str
    status: str
    version: int
    path: str
    sha256: str
    parent_atom_id: str
    container_path: str
    directory_path: str | None


@dataclass(frozen=True)
class ContainedAtomInventory:
    parent: TargetCarrier
    targets: tuple[ContainedAtomTarget, ...]


def _bindings(context: VerifiedSourceContext):
    sources = {row["binding"]["atom_id"]: row for row in context.inputs["sources"]}
    roles = dict(re.findall(
        r"- ([A-Za-z]+): `([0-9]{2}_[a-z_]+)/`[;.]", sources["CA-D-324"]["text"],
    ))
    roles = {role: roles[role] for role in ("Plan", "Operations")}
    plans = {"Active": "", **dict(re.findall(
        r"- ([A-Za-z]+): .*?`([^`]+)`", sources["CA-D-461"]["text"],
    ))}
    statuses = _frontier_status_folders(context, plans)
    roots = _authority_roots(
        context.root, context.inputs["structure"],
        (context._selection.control_relative,),
        context.inputs["_project_identity"]["project"]["name"],
    )
    return roots, roles, {role: statuses[role] for role in roles}


def _under_old_bundle(path, carriers, statuses):
    bundles = {path.with_suffix(""): row for path, row in carriers.items()}
    for ancestor in reversed(path.parents):
        owner = bundles.get(ancestor)
        if owner is None or ancestor.parent.name != statuses[owner.role].get("Archived"):
            continue
        version = owner.metadata.get("version")
        suffix = re.search(r"@([1-9][0-9]*)$", ancestor.name)
        if type(version) is int and suffix and int(suffix[1]) == version:
            latest = _latest_path(owner.metadata["atom_id"], carriers, statuses, exclude_old=False)
            if carriers[latest].metadata["version"] > version:
                return True
    return False


def _latest_path(identity, carriers, statuses, *, exclude_old=True):
    revisions = {}
    current = []
    for path, row in carriers.items():
        if row.metadata.get("atom_id") != identity:
            continue
        if exclude_old and _under_old_bundle(path, carriers, statuses):
            continue
        version = row.metadata.get("version")
        if type(version) is not int or version < 1 or version in revisions:
            raise ContainedAtomTargetsError("invalid or competing same-Version carriers")
        revisions[version] = path
        # Archived ancestry is not this Revision's own archival placement.
        if path.parent.name == statuses[row.role].get("Archived"):
            suffix = re.search(r"@([1-9][0-9]*)$", path.stem)
            if suffix is None or int(suffix[1]) != version:
                raise ContainedAtomTargetsError("Archive Carrier suffix disagrees with its Version")
        else:
            current.append(path)
    if not revisions or len(current) > 1:
        raise ContainedAtomTargetsError("identity is missing or has duplicate current carriers")
    latest = revisions[max(revisions)]
    if current and current[0] != latest:
        raise ContainedAtomTargetsError("current carrier conflicts with later archived Revision")
    row = carriers[latest]
    local = statuses[row.role].get(row.metadata.get("status"))
    if not row.placement_matches or _container_id(
        row.metadata, row.role, row.owner, statuses[row.role], local,
    ) is None:
        raise ContainedAtomTargetsError("latest competing carrier is not admitted")
    return latest


def _check_tree_directories(reader, tree, directories):
    admitted = set(directories)
    for name in directories:
        path = Path(name)
        if not path.is_relative_to(tree):
            continue
        reader.allowed(path)
        descriptor = open_regular(path, directory=True)
        try:
            with os.scandir(descriptor) as entries:
                for entry in entries:
                    reader.checkpoint()
                    if entry.is_symlink():
                        raise ContainedAtomTargetsError("symlink in contained tree")
                    if not entry.is_dir(follow_symlinks=False) or entry.name == "archive":
                        continue  # explicitly deferred legacy history, never a target
                    if str(path / entry.name) not in admitted:
                        raise ContainedAtomTargetsError("unsupported contained directory lacks an admitted sibling carrier")
        finally:
            os.close(descriptor)


def discover_contained_atom_targets(
    context: VerifiedSourceContext, parent_atom_id: str, *,
    expected_version: int, expected_sha256: str,
) -> ContainedAtomInventory:
    """Return descendants, excluding the explicit parent, in stable tree order.

    Only the existing source-admitted P/O frontier is visited. Status is read
    from each carrier, including uniquely resolved current Archived carriers;
    legacy archive trees and references outside the matching directory are not
    descendants. Canonical history uses the unique greatest carried Version;
    competing current or same-Version carriers refuse. No effect is granted.
    """
    if (not isinstance(context, VerifiedSourceContext)
            or not isinstance(parent_atom_id, str) or not parent_atom_id
            or type(expected_version) is not int or expected_version < 1
            or not isinstance(expected_sha256, str)
            or re.fullmatch(r"[0-9a-f]{64}", expected_sha256) is None):
        raise ContainedAtomTargetsError("explicit parent identity and exact expected state are required")
    try:
        if context.root != context._selection.root:
            raise ContainedAtomTargetsError("selected Project does not match source context")
        _current(context._reader)
        roots, roles, statuses = _bindings(context)
        reader = ReadContext(roots=[str(context.root)], limits=dict(CEILINGS))
        carriers, directories = _frontier(reader, roots, roles, statuses)
        parent_path = _latest_path(parent_atom_id, carriers, statuses)
        parent_row = carriers[parent_path]
        parent = _carrier(reader, context.root, parent_path, {parent_atom_id}, parent_row)
        local = statuses[parent_row.role].get(parent_row.metadata.get("status"))
        if parent is None or _container_id(parent_row.metadata, parent_row.role, parent_row.owner,
                                            statuses[parent_row.role], local) is None:
            raise ContainedAtomTargetsError("parent is not an admitted Plan, Workflow or Step")
        if (parent.version, parent.sha256) != (expected_version, expected_sha256):
            raise ContainedAtomTargetsError("parent expected state is stale")
        tree = parent_path.with_suffix("")
        _check_tree_directories(reader, tree, directories)
        selected = {path: row for path, row in carriers.items()
                    if path.is_relative_to(tree) and not _under_old_bundle(path, carriers, statuses)}
        items = {}
        for path, row in selected.items():
            identity = row.metadata.get("atom_id")
            if not isinstance(identity, str) or not identity:
                raise ContainedAtomTargetsError("contained carrier lacks explicit identity")
            if identity == parent_atom_id:
                raise ContainedAtomTargetsError("parent identity recurs inside its own tree")
            if path != _latest_path(identity, carriers, statuses):
                continue
            item = _carrier(reader, context.root, path, {identity}, row)
            local = statuses[row.role].get(row.metadata.get("status"))
            if item is None or _container_id(row.metadata, row.role, row.owner, statuses[row.role], local) is None:
                raise ContainedAtomTargetsError("contained carrier has unsupported type or placement")
            items[path] = item
        containers = {path.with_suffix(""): item for path, item in {parent_path: parent, **items}.items()}
        children: dict[str, list[ContainedAtomTarget]] = {}
        for path, item in items.items():
            container = path.parent
            if container not in containers:
                container = container.parent  # one admitted local Status directory
            owner = containers.get(container)
            if owner is None:
                raise ContainedAtomTargetsError("contained carrier lacks an authenticated immediate container")
            own_directory = path.with_suffix("")
            children.setdefault(owner.atom_id, []).append(ContainedAtomTarget(
                item.atom_id, item.metadata["content_role"], item.metadata["type"],
                item.status, item.version, item.path, item.sha256, owner.atom_id,
                str(container.relative_to(context.root)),
                str(own_directory.relative_to(context.root)) if str(own_directory) in directories else None,
            ))
        ordered = []
        pending = list(reversed(sorted(children.get(parent_atom_id, []), key=lambda item: item.path)))
        while pending:
            item = pending.pop()
            ordered.append(item)
            pending.extend(reversed(sorted(children.get(item.atom_id, []), key=lambda child: child.path)))
        current_carriers, current_directories = _frontier(reader, roots, roles, statuses)
        _check_tree_directories(reader, tree, current_directories)
        if (current_carriers != carriers or current_directories != directories
                or reader.currentness()["state"] != "unchanged"):
            raise ContainedAtomTargetsError("contained source frontier changed during discovery")
        _current(context._reader)
        return ContainedAtomInventory(parent, tuple(ordered))
    except (OSError, RuntimeError, KeyError, TypeError, CarrierError, ProposedCarrierError,
            ProposedReferenceError, ReadFailure, LimitReached) as error:
        raise ContainedAtomTargetsError("contained target source context or frontier is unavailable") from error
