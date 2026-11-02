"""Read compatibility for carrier field names; never mutate the source mapping."""

from typing import Any


def _equal(left: Any, right: Any) -> bool:
    if type(left) is not type(right):
        return False
    if isinstance(left, dict):
        return left.keys() == right.keys() and all(_equal(left[k], right[k]) for k in left)
    if isinstance(left, list):
        return len(left) == len(right) and all(_equal(a, b) for a, b in zip(left, right))
    return left == right


def _read_aliases(mapping: dict[str, Any], pairs: tuple[tuple[str, str], ...]) -> dict[str, Any]:
    view = dict(mapping)
    for old, new in pairs:
        if old in mapping and new in mapping and not _equal(mapping[old], mapping[new]):
            raise ValueError(f"Conflicting carrier aliases: {old} and {new}.")
        if old not in mapping and new in mapping:
            view[old] = mapping[new]
    return view


def carrier_read_view(metadata: dict[str, Any]) -> dict[str, Any]:
    """Expose legacy read keys alongside new names, rejecting unequal aliases."""
    view = _read_aliases(metadata, (("content_role", "role"), ("type", "form")))
    if isinstance(view.get("subjects"), dict):
        view["subjects"] = _read_aliases(view["subjects"], (("governs", "active"), ("depends_on", "passive")))
    return view
