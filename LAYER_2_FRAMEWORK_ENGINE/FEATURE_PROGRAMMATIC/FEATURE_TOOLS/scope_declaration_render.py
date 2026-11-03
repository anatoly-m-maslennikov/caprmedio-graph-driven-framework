"""Pure rendering for Scope Unit Declaration Atoms."""

from __future__ import annotations

import json


PROJECT = "PROJECT"
_STRUCTURE_PREFIX = "CAPRMEDIO_STRUCTURE <+ "


def _quoted(value: object) -> str:
    return json.dumps(value, ensure_ascii=False)


def _positive_int(value: object) -> bool:
    return isinstance(value, int) and not isinstance(value, bool) and value > 0


def render_scope_declaration(
    *,
    name: str,
    project_name: str,
    atom_id: str,
    updated_at: str,
    scope_id: str | None = None,
    label: str | None = None,
    ordered: bool = False,
    order_number: int | None = None,
    parent: str | None = None,
    project: bool = False,
    version: int = 1,
    status: str = "Active",
) -> str:
    """Render one declaration without reading files or resolving structure."""
    local_subject = f"Project//{name}" if project else f"Scope Unit//{name}"
    subject = (
        f"{_STRUCTURE_PREFIX}{local_subject}"
        if project_name.casefold() == "caprmedio"
        else local_subject
    )
    header = (
        "---\n"
        f"atom_id: {_quoted(atom_id)}\n"
        "role: Requirement\n"
        "form: Scope Unit Declaration\n"
        f"status: {_quoted(status)}\n"
        f"version: {version}\n"
        f"updated_at: {_quoted(updated_at)}\n"
        "subjects:\n"
        f"  active: {_quoted(subject)}\n"
        "  passive: []\n"
        "relations: {}\n"
        "---\n"
    )
    claims = [f"{local_subject}.Name == {_quoted(name)}"]
    if not project:
        if scope_id is not None:
            claims.insert(0, f"{local_subject}.ID == {_quoted(scope_id)}")
        if label is not None:
            claims.append(f"{local_subject}.Label == {_quoted(label)}")
        claims.append(f"{local_subject}.order.ordered == {str(bool(ordered)).lower()}")
        if ordered and _positive_int(order_number):
            claims.append(f"{local_subject}.order.number == {order_number}")
        if parent:
            parent_subject = (
                f"Project//{project_name}"
                if parent in {PROJECT, project_name}
                else f"Scope Unit//{parent}"
            )
            claims.append(f"{local_subject} ((IS_CONTAINED_BY)) {parent_subject}")
    return (
        header
        + f"## Summary\n\nDeclare {name}\n\n## Claim\n\n### Formal Claim\n\n```CFEL\n# instances\n"
        + ";\n".join(claims)
        + "\n```\n"
    )
