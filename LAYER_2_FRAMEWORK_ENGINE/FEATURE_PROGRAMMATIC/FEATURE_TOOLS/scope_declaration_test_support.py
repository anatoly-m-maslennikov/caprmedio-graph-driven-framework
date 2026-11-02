"""Test-only materialization for Scope Unit Declaration fixture authority."""

from __future__ import annotations

import tomllib
from pathlib import Path
from typing import Any, Mapping

from scope_declaration_render import PROJECT, render_scope_declaration


def _settings(root: Path, control_root: Path | None) -> tuple[Path, str]:
    root = Path(root)
    supplied_control_root = control_root
    if control_root is None:
        control_root = root / ".caprmedio_caprmedio"
    control_root = Path(control_root)
    settings = tomllib.loads((control_root / "caprmedio_project_settings.toml").read_text("utf-8"))
    if supplied_control_root is None:
        configured = settings.get("paths", {}).get("control_root")
        if isinstance(configured, str) and configured:
            control_root = root / configured
    project_name = settings["project"]["name"]
    if not isinstance(project_name, str) or not project_name:
        raise ValueError("fixture project settings need project.name")
    return control_root, project_name


def _order(value: object) -> int | None:
    return value if isinstance(value, int) and not isinstance(value, bool) and value > 0 else None


def _slug(name: str) -> str:
    return name.lower().replace("_", "-")


def _component(row: Mapping[str, Any]) -> str:
    label = row.get("scope_unit_label")
    parts = [str(row["scope_id"])]
    if isinstance(label, str) and label:
        parts.append(label)
    if row["ordered"]:
        parts.append(str(row["local_order"]))
    parts.append(str(row["scope_unit_name"]))
    return "_".join(parts)


def _derived_rows(root: Path, rows: tuple[Mapping[str, Any], ...], control_root: Path, project_name: str) -> dict[str, dict[str, Any]]:
    result: dict[str, dict[str, Any]] = {
        project_name: {
            "scope_unit_name": project_name, "parent": None, "scope_unit_type": "Unordered",
            "scope_unit_label": None, "local_order": None, "ordered": False, "scope_id": None,
            "atom_id": "CA-R-990000", "authority_path": control_root,
            "delivery_path": root, "project": True,
        }
    }
    pending = list(rows)
    for index, row in enumerate(pending, start=1):
        name = row.get("scope_unit_name")
        parent = row.get("parent", PROJECT)
        if not isinstance(name, str) or not name:
            raise ValueError("fixture declaration needs scope_unit_name")
        if not isinstance(parent, str) or not parent:
            raise ValueError(f"fixture declaration {name} needs parent")
        ordered = row.get("scope_unit_type") == "Ordered"
        pending[index - 1] = {
            "scope_unit_name": name, "parent": parent, "scope_unit_type": "Ordered" if ordered else "Unordered",
            "scope_unit_label": row.get("scope_unit_label"),
            "local_order": _order(row.get("local_order")) if ordered else None,
            "ordered": ordered, "scope_id": f"TEST-SU-{index}", "atom_id": f"CA-R-{990000 + index}",
            "project": False,
        }
    while pending:
        remaining: list[dict[str, Any]] = []
        for row in pending:
            parent_name = project_name if row["parent"] == PROJECT else row["parent"]
            parent = result.get(parent_name)
            if parent is None:
                remaining.append(row)
                continue
            authority = Path(parent["authority_path"]) / _component(row)
            delivery = Path(parent["delivery_path"]) / "_".join(
                part for part in ([row["scope_unit_label"]] if row["scope_unit_label"] else [])
                + ([str(row["local_order"])] if row["ordered"] else []) + [row["scope_unit_name"]]
            )
            row["authority_path"] = authority
            row["delivery_path"] = delivery
            result[row["scope_unit_name"]] = row
        if len(remaining) == len(pending):
            raise ValueError("fixture declaration parents are missing or cyclic")
        pending = remaining
    return result


def write_scope_unit_declarations(root: Path, rows: tuple[Mapping[str, Any], ...] = (), *, control_root: Path | None = None, project_name: str | None = None) -> dict[str, dict[str, Any]]:
    """Materialize fixture declarations and return their derived structural rows."""
    resolved_control, settings_name = _settings(root, control_root)
    project_name = project_name or settings_name
    derived = _derived_rows(Path(root), tuple(rows), resolved_control, project_name)
    for row in derived.values():
        parent_authority = resolved_control if row["project"] else derived[
            project_name if row["parent"] == PROJECT else row["parent"]
        ]["authority_path"]
        filename = (
            f"{row['atom_id']}-{_slug(row['scope_unit_name'])}-SCOPE_UNIT_DECLARATION--"
            f"declare-{_slug(row['scope_unit_name'])}.md"
        )
        target = (resolved_control if row["project"] else Path(parent_authority) / "04_requirement") / filename
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(render_scope_declaration(
            name=row["scope_unit_name"], project_name=project_name, atom_id=row["atom_id"],
            updated_at="2026-11-02 00:00:00 +0000", scope_id=row["scope_id"],
            label=row["scope_unit_label"], ordered=row["ordered"], order_number=row["local_order"],
            parent=row["parent"], project=row["project"],
        ), encoding="utf-8")
        row["declaration_path"] = target
    return derived


def read_scope_unit_declarations(root: Path, control_root: Path, reader: Any = None) -> Any:
    """Delegate declaration discovery when a fixture supplies its reader."""
    if reader is None:
        raise ValueError("a declaration reader is required for fixture discovery")
    return reader(root, control_root)
