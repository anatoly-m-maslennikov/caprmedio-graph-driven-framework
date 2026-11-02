"""Source-bound D547 Workflow edge readers."""

from __future__ import annotations

from collections.abc import Mapping
import hashlib
from pathlib import Path
import re
from typing import Any

from selected_execution_contracts import SelectedExecutionError
from selected_graph_sources import safe_definition_path, validate_definition


def _sha256(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def source_bound_d547_edges(
    root: Path, route: Mapping[str, Any], bound_steps: set[str]
) -> list[dict[str, str]] | None:
    """Read CA-O-016's canonical On Result table when the source supplies it."""
    binding = route.get("workflow")
    if not isinstance(binding, Mapping):
        raise SelectedExecutionError("D547 selected Workflow binding is invalid")
    workflow = validate_definition(root, binding, expected_kind="workflow")
    if workflow["atom_id"] != "CA-O-016":
        return None
    source = safe_definition_path(root, str(workflow["path"]))
    raw = source.read_bytes()
    if _sha256(raw) != workflow["sha256"]:
        raise SelectedExecutionError("Workflow definition changed while reading source graph")
    return _parse_source_edges(raw, bound_steps)


def _parse_source_edges(raw: bytes, bound_steps: set[str]) -> list[dict[str, str]]:
    try:
        lines = raw.decode("utf-8").splitlines()
    except UnicodeDecodeError as error:
        raise SelectedExecutionError("Workflow definition is not UTF-8") from error
    header = "| From Step | Result condition | Next Step **or** terminal result |"
    indexes = [index for index, line in enumerate(lines) if line.strip() == header]
    separator = re.compile(r"\|\s*:?-{3,}:?\s*\|\s*:?-{3,}:?\s*\|\s*:?-{3,}:?\s*\|")
    if (
        len(indexes) != 1
        or indexes[0] + 1 >= len(lines)
        or separator.fullmatch(lines[indexes[0] + 1].strip()) is None
    ):
        raise SelectedExecutionError("D547 source Workflow On Result table is invalid")
    edges: list[dict[str, str]] = []
    for line in lines[indexes[0] + 2 :]:
        stripped = line.strip()
        if not stripped.startswith("|"):
            break
        cells = [value.strip() for value in stripped.strip("|").split("|")]
        if len(cells) != 3 or not all(cells):
            raise SelectedExecutionError("D547 source Workflow On Result row is invalid")
        source_step, condition, target = cells
        if source_step not in bound_steps:
            raise SelectedExecutionError(
                "D547 source Workflow On Result source is not a bound Step"
            )
        edges.append({"from": source_step, "condition": condition, "to": target})
    if not edges:
        raise SelectedExecutionError("D547 source Workflow On Result table has no edges")
    return edges
