# CA-R-2723@3
# CA-R-2726@5
# CA-D-672@12

"""Map parsed Atom and Scope Unit sources to raw Workbench rows."""

from __future__ import annotations

from pathlib import Path
import re
from typing import Any

from .markdown_content import parse_content


_NUMBERED_DRAFT_REFERENCE = re.compile(r"@\d+-draft$")


def atom(
    path: Path, root: Path, header: dict[str, Any], view: dict[str, Any],
    body: str, group: str,
) -> dict[str, Any]:
    atom_id, version = view.get("atom_id"), view.get("version")
    if group == "Current" and isinstance(atom_id, str):
        ref = atom_id
    elif group == "Draft" and isinstance(atom_id, str) and type(version) is int:
        if _NUMBERED_DRAFT_REFERENCE.search(atom_id):
            ref = atom_id
        elif atom_id.endswith(("-draft", "@draft")):
            ref = f"{atom_id}:{path.relative_to(root).as_posix()}"
        else:
            ref = f"{atom_id}@{version}-draft"
    else:
        ref = None
    return {
        "source_path": path.relative_to(root).as_posix(),
        "status_group": group,
        "id": atom_id if isinstance(atom_id, str) else None,
        "ref": ref,
        "version": bigint(version),
        "status": string(view.get("status")),
        "current_scope_unit": string(header.get("current_scope_unit")),
        "claim_target_scope_unit": string(header.get("claim_target_scope_unit")),
        "role": string(view.get("content_role")),
        "form": string(view.get("type")),
        "tier": bigint(view.get("tier")),
        "updated_at": view.get("updated_at"),
        "header_json": header,
        "content_markdown": body,
        "content_properties_json": parse_content(body, tolerate_duplicate_siblings=True),
        "relation_edges_json": [],
        "hash": None,
    }


def scope(item: Any, root: Path) -> dict[str, Any]:
    return {
        "name": item.name,
        "scope_unit_id": item.scope_unit_id,
        "parent_name": item.parent,
        "declared_label": item.label,
        "ordered": item.ordered,
        "order_number": item.local_order,
        "declaration_source_path": item.source.relative_to(root).as_posix(),
        "declaration_version": item.version,
        "relation_edges_json": [],
        "hash": None,
    }


def string(value: Any) -> str | None:
    return value if isinstance(value, str) else None


def bigint(value: Any) -> int | None:
    return value if type(value) is int and -(2**63) <= value < 2**63 else None
