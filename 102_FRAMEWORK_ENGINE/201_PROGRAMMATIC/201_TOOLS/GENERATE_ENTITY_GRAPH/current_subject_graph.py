"""Compose a syntax graph from supplied current Atom Subjects, without history."""

import hashlib
import json
from typing import Any

from subject_notation import SubjectNotationError, parse_subject

Record = dict[str, Any]
_KINDS = {"/": "NARROWER_THAN", ".": "IS_BORNE_BY", ":": "IS_ALLOWED_VALUE_OF"}


def _identifier(prefix: str, value: object) -> str:
    raw = json.dumps(value, ensure_ascii=False, separators=(",", ":")).encode("utf-8")
    return prefix + hashlib.sha256(raw).hexdigest()


def path_steps(subject: str) -> list[tuple[str, str | None, str | None]]:
    """Preserve each qualified prefix, including slash-plus-value classification."""
    parts = parse_subject(subject, subject_profile="approved")
    prefix, index = parts[0][0], 1
    steps: list[tuple[str, str | None, str | None]] = [(prefix, None, None)]
    while index < len(parts):
        segment, separator = parts[index]
        if separator == "/" and index + 1 < len(parts) and parts[index + 1][1] == ":":
            segment += ": " + parts[index + 1][0]
            index += 1
        if separator not in _KINDS:
            raise ValueError("Unsupported Subject separator")
        child = prefix + separator + (" " if separator == ":" else "") + segment
        steps.append((child, prefix, _KINDS[separator]))
        prefix, index = child, index + 1
    if prefix != subject:
        raise ValueError("Subject spelling would change during parsing")
    return steps


def _occurrences(carrier: Record, diagnostics: list[str]) -> list[Record]:
    source, subjects = carrier["source"], carrier["subjects"]
    if not isinstance(subjects, dict):
        diagnostics.append(f"{source['path']}: Subjects mapping is unavailable.")
        return []
    result = []
    for role in ("governs", "depends_on"):
        value = subjects.get(role, [])
        values = value if isinstance(value, list) else [value]
        for index, subject in enumerate(values):
            locator = f"{source['path']}#subjects.{role}[{index}]"
            if not isinstance(subject, str) or not subject:
                diagnostics.append(f"{locator}: Subject is not nonempty text; no identity guessed.")
                continue
            result.append({"id": locator, "subject": subject, "source": source, "role": role})
    return result


def _add_path(
    occurrence: Record, nodes: dict[str, Record], edges: dict[str, Record], diagnostics: list[str]
) -> None:
    subject, origin = occurrence["subject"], occurrence["id"]
    try:
        steps = path_steps(subject)
    except SubjectNotationError, ValueError:
        diagnostics.append(
            f"{origin}: unclear Subject retained literally without inferred edges: {subject}"
        )
        steps = [(subject, None, None)]
    for identity, parent, kind in steps:
        child_id = _identifier("subject:", identity)
        node = nodes.setdefault(
            child_id,
            {
                "id": child_id,
                "identity": identity,
                "occurrence_ids": set(),
                "is_full_target": False,
            },
        )
        node["occurrence_ids"].add(origin)
        node["is_full_target"] |= identity == subject
        if parent is not None:
            parent_id = _identifier("subject:", parent)
            edge_id = _identifier("subject-edge:", [kind, parent_id, child_id])
            edge = edges.setdefault(
                edge_id,
                {
                    "id": edge_id,
                    "kind": kind,
                    "relation_source": child_id,
                    "relation_target": parent_id,
                    "occurrence_ids": set(),
                },
            )
            edge["occurrence_ids"].add(origin)


def compose_current_graph(carriers: list[Record]) -> tuple[Record, Record]:
    """Use only the passed current sources; Subject roles add no cross-path edges."""
    nodes: dict[str, Record] = {}
    edges: dict[str, Record] = {}
    diagnostics: list[str] = []
    occurrences = [row for carrier in carriers for row in _occurrences(carrier, diagnostics)]
    for occurrence in occurrences:
        _add_path(occurrence, nodes, edges, diagnostics)
    for row in [*nodes.values(), *edges.values()]:
        row["occurrence_ids"] = sorted(row["occurrence_ids"])
    graph = {
        "kind": "current_atom_subjects",
        "source_basis": "current_atom_carriers",
        "nodes": sorted(nodes.values(), key=lambda row: (row["identity"], row["id"])),
        "edges": sorted(edges.values(), key=lambda row: row["id"]),
        "diagnostics": sorted(diagnostics),
    }
    provenance = {
        "owners": [{"source": carrier["source"]} for carrier in carriers],
        "occurrences": occurrences,
    }
    return graph, provenance
