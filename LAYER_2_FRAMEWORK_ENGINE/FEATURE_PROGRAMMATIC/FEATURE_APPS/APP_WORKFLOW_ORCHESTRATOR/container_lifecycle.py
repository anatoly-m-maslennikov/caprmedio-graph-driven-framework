"""Pure planning for recursively contained lifecycle status changes."""

from __future__ import annotations

from contained_atom_targets import ContainedAtomInventory, ContainedAtomTarget


def plan_contained_status_changes(
    inventory: ContainedAtomInventory, requested_status: str,
) -> tuple[tuple[ContainedAtomTarget, str], ...]:
    """Return source-bound descendants deepest-first without applying changes.

    The depth walk is linear; deterministic ordering makes total work O(N log N).
    """
    if not isinstance(inventory, ContainedAtomInventory) or not isinstance(requested_status, str):
        raise TypeError("inventory and requested status have unsupported types")
    if not requested_status.strip():
        raise ValueError("requested status must be non-blank text")
    targets = tuple(inventory.targets)
    parent_id = inventory.parent.atom_id
    if (
        not isinstance(parent_id, str) or not parent_id.strip()
        or any(
            not isinstance(target, ContainedAtomTarget)
            or not isinstance(target.atom_id, str) or not target.atom_id.strip()
            or not isinstance(target.parent_atom_id, str) or not target.parent_atom_id.strip()
            for target in targets
        )
    ):
        raise ValueError("inventory contains malformed identity links")
    by_id = {target.atom_id: target for target in targets}
    if len(by_id) != len(targets) or parent_id in by_id:
        raise ValueError("inventory contains duplicate or included parent targets")
    known = set(by_id) | {parent_id}
    children: dict[str, list[ContainedAtomTarget]] = {}
    for target in targets:
        if target.parent_atom_id not in known:
            raise ValueError("inventory contains an unauthenticated parent link")
        children.setdefault(target.parent_atom_id, []).append(target)
    depth = {parent_id: 0}
    pending = [parent_id]
    while pending:
        owner = pending.pop()
        for target in children.get(owner, ()):
            depth[target.atom_id] = depth[owner] + 1
            pending.append(target.atom_id)
    if len(depth) != len(targets) + 1:
        raise ValueError("inventory contains a disconnected parent-link tree")
    return tuple(
        (
            target,
            "Canceled"
            if requested_status == "Done"
            and target.content_role == "Plan"
            and target.status != "Done"
            else requested_status,
        )
        for target in sorted(targets, key=lambda item: (-depth[item.atom_id], item.path, item.atom_id))
    )
