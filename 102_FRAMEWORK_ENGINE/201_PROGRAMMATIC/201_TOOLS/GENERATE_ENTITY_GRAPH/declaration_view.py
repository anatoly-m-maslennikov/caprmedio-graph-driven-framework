"""Render the middle-level Entities Graph declaration view.

The caller supplies already-selected Relation Type and Graph Rule records. This
module only renders those records; it does not classify, admit, evaluate or
derive source facts.
"""

from __future__ import annotations

import json
from collections.abc import Mapping

import yaml

from readable_entity_tree import _fence as _text_fence
from readable_entity_tree import _sources


_METADATA_FIELDS = (
    ("meaning", "Meaning"),
    ("direction", "Declared direct direction"),
    ("inverse", "Inverse direction"),
    ("authority_effect", "Authority effect"),
    ("transitivity", "Transitivity"),
    ("applicability", "Applicability"),
    ("status", "Status"),
    ("exclusive_purpose", "Exclusive purpose"),
)
_UNAVAILABLE = "unavailable (not evidenced in selected authority)"


def _record(value: object, field: str) -> dict[str, object]:
    if not isinstance(value, dict):
        raise ValueError(f"{field} must be a plain mapping")
    return value


def _required_text(value: object, field: str) -> str:
    if not isinstance(value, str) or not value.strip() or any(char in value for char in "\r\n\t"):
        raise ValueError(f"Invalid {field}")
    return value


def _source_id(value: object) -> str | None:
    if value is None:
        return None
    source = _record(value, "source")
    atom_id = source.get("atom_id")
    version = source.get("version")
    if (
        not isinstance(atom_id, str)
        or not atom_id.strip()
        or isinstance(version, bool)
        or not isinstance(version, int)
        or version < 1
    ):
        raise ValueError("Invalid SourceRef")
    return f"{atom_id.strip()}@{version}"


def _source_ids(value: object) -> list[str]:
    if value is None:
        return []
    if not isinstance(value, list):
        raise ValueError("sources must be a list")
    return sorted({_source_id(item) for item in value if item is not None})


def _display(value: object, unavailable: str = _UNAVAILABLE) -> str:
    if value is None:
        return unavailable
    if isinstance(value, str):
        if not value:
            return unavailable
        return value.replace("\r", "\\r").replace("\n", "\\n")
    if isinstance(value, Mapping):
        normalized = {str(key): item for key, item in value.items()}
        return json.dumps(
            normalized, ensure_ascii=False, sort_keys=True, default=str, separators=(",", ":")
        )
    if isinstance(value, list):
        return json.dumps(
            value, ensure_ascii=False, sort_keys=True, default=str, separators=(",", ":")
        )
    return str(value)


def _metadata(row: dict[str, object]) -> dict[str, object]:
    value = row.get("metadata")
    if value is None:
        return {}
    return _record(value, "metadata")


def _relation_type_lines(row: dict[str, object]) -> list[str]:
    graph_kind = _display(row.get("graph_kind"))
    canonical_name = _display(row.get("canonical_name"))
    metadata = _metadata(row)
    lines = [f"Relation Type: {graph_kind} / {canonical_name}"]
    lines.extend((f"\tOwning graph kind: {graph_kind}", f"\tCanonical name: {canonical_name}"))
    for key, label in _METADATA_FIELDS:
        lines.append(f"\t{label}: {_display(metadata.get(key))}")
    source_ids = _source_ids(row.get("sources"))
    if source_ids:
        lines.append("\tSources:")
        lines.extend(f"\t\t{source_id}" for source_id in source_ids)
    else:
        lines.append(f"\tSources: {_UNAVAILABLE}")
    return lines


def _relation_type_key(row: object) -> tuple[str, str, str]:
    mapped = _record(row, "relation type")
    return (
        _display(mapped.get("graph_kind")),
        _display(mapped.get("canonical_name")),
        json.dumps(mapped.get("metadata", {}), ensure_ascii=False, sort_keys=True, default=str),
    )


def _raw_body_lines(value: object) -> list[str]:
    if value is None:
        return []
    text = str(value)
    return text.splitlines() or [""]


def _evidence_lines(evidence: object) -> list[object]:
    row = _record(evidence, "Relation Type evidence")
    source_id = _source_id(row.get("source")) or _UNAVAILABLE
    subject = _display(row.get("subject"))
    body = row.get("body")
    lines: list[object] = [
        f"#### Evidence: {source_id}",
        f"Source: {source_id}",
        f"Subject: {subject}",
        "Body:",
    ]
    if body is None:
        lines[-1] = f"Body: {_UNAVAILABLE}"
    else:
        lines.extend(_text_fence(_raw_body_lines(body)))
    return lines


def _relation_type_evidence(row: dict[str, object]) -> list[object]:
    evidence = row.get("evidence") or []
    if not isinstance(evidence, list):
        raise ValueError("evidence must be a list")
    evidence_rows = [_record(item, "Relation Type evidence") for item in evidence]
    evidence_rows.sort(
        key=lambda item: (_source_id(item.get("source")) or "~unavailable~", _display(item.get("subject")))
    )
    lines: list[object] = []
    for index, item in enumerate(evidence_rows):
        if index:
            lines.append("")
        lines.extend(_evidence_lines(item))
    return lines


def _graph_rule_key(row: object) -> tuple[str, str, str]:
    mapped = _record(row, "graph rule")
    return (
        _source_id(mapped.get("source")) or "~unavailable~",
        _display(mapped.get("subject")),
        _display(mapped.get("summary")),
    )


def _graph_rule_lines(row: dict[str, object]) -> list[object]:
    source_id = _source_id(row.get("source")) or _UNAVAILABLE
    subject = _display(row.get("subject"))
    summary = _display(row.get("summary"))
    lines: list[object] = [
        f"### Graph Rule: {source_id}",
        f"Source: {source_id}",
        f"Governed Subject: {subject}",
        f"Summary: {summary}",
    ]
    yaml_block = row.get("yaml_block")
    if yaml_block is None:
        lines.append(f"Source YAML: {_UNAVAILABLE}")
    else:
        lines.extend(["Source YAML:", str(yaml_block)])
    return lines


def _unresolved_lines(row: dict[str, object]) -> list[object]:
    source_id = _source_id(row.get("source")) or _UNAVAILABLE
    subject = _display(row.get("subject"))
    reason = _display(row.get("reason"))
    lines: list[object] = [
        f"### Unresolved: {subject}",
        f"Source: {source_id}",
        f"Reason: {reason}",
    ]
    body = row.get("body")
    if body is not None:
        lines.extend(["Governing evidence:", *_text_fence(_raw_body_lines(body))])
    return lines


def _limitations(catalog: dict[str, object], graph_rule_count: int) -> list[object]:
    limitations = catalog.get("limitations", []) or []
    unresolved = catalog.get("unresolved", []) or []
    if not isinstance(limitations, list) or not isinstance(unresolved, list):
        raise ValueError("limitations and unresolved must be lists")
    lines: list[object] = ["## Source limitations", ""]
    if graph_rule_count == 0:
        lines.append("- Concrete Graph Rule catalogue: empty for the selected source set.")
    supplied = sorted({_display(item) for item in limitations if item is not None})
    if supplied:
        lines.extend(f"- {item}" for item in supplied)
    unresolved_rows = [_record(item, "unresolved item") for item in unresolved]
    unresolved_rows.sort(
        key=lambda item: (
            _source_id(item.get("source")) or "~unavailable~",
            _display(item.get("subject")),
            _display(item.get("reason")),
        )
    )
    if unresolved_rows:
        lines.extend(["", "### Unresolved source items", ""])
        for index, row in enumerate(unresolved_rows):
            if index:
                lines.append("")
            lines.extend(_unresolved_lines(row))
    if graph_rule_count and not supplied and not unresolved_rows:
        lines.append("- No source limitations supplied; this does not establish completeness outside the selection.")
    if not supplied and not unresolved_rows and not graph_rule_count:
        lines.append("- No additional limitations supplied; the empty Rule catalogue does not establish completeness outside the selection.")
    return lines


def _source_of_truth(value: object) -> str | list[str]:
    if isinstance(value, str):
        return _required_text(value, "source_of_truth")
    if isinstance(value, list) and value and all(
        isinstance(item, str) and item.strip() and not any(char in item for char in "\r\n\t")
        for item in value
    ):
        return value
    raise ValueError("Invalid source_of_truth")


def render_declarations(
    catalog: dict[str, object],
    provenance: dict[str, object],
    *,
    updated_at: str,
    source_selection: str,
    projection_identity: dict[str, object],
) -> str:
    """Return deterministic Markdown for supplied declaration records only."""

    catalog = _record(catalog, "catalog")
    projection_identity = _record(projection_identity, "projection_identity")
    identity = {
        "projection_id": _required_text(projection_identity.get("projection_id"), "projection_id"),
        "named_selection": _required_text(projection_identity.get("named_selection"), "named_selection"),
        "source_of_truth": _source_of_truth(projection_identity.get("source_of_truth")),
    }
    updated_at = _required_text(updated_at, "updated_at")
    source_selection = _required_text(source_selection, "source selection")
    relation_types_value = catalog.get("relation_types", []) or []
    graph_rules_value = catalog.get("graph_rules", []) or []
    if not isinstance(relation_types_value, list) or not isinstance(graph_rules_value, list):
        raise ValueError("relation_types and graph_rules must be lists")
    relation_types = [_record(row, "relation type") for row in relation_types_value]
    graph_rules = [_record(row, "graph rule") for row in graph_rules_value]
    relation_types.sort(key=_relation_type_key)
    graph_rules.sort(key=_graph_rule_key)

    frontmatter = yaml.safe_dump(
        {
            "artifact_form": "Projection",
            "projection_id": identity["projection_id"],
            "named_selection": identity["named_selection"],
            "source_of_truth": identity["source_of_truth"],
            "type": "Entities Graph",
            "updated_at": updated_at,
            "sources": _sources(provenance),
        },
        allow_unicode=True,
        sort_keys=False,
    ).rstrip()

    body: list[object] = [
        "---",
        frontmatter,
        "---",
        "",
        "Source selection: " + source_selection,
        "",
        "Display selection: named Relation Types and concrete Graph Rule declarations; actual Atom-to-Atom Relation tuples are excluded.",
        "",
        "This is a derived Projection, not independent model authority.",
        "",
        "## Relation Types",
        "",
    ]
    if relation_types:
        for index, row in enumerate(relation_types):
            if index:
                body.append("")
            body.extend(_text_fence(_relation_type_lines(row)))
            evidence = _relation_type_evidence(row)
            if evidence:
                body.extend(["", *evidence])
            body.append("")
    else:
        body.extend(["- No Relation Type declarations supplied for the selected source set.", ""])

    body.extend(["## Graph Rules", ""])
    if graph_rules:
        for index, row in enumerate(graph_rules):
            if index:
                body.append("")
            body.extend(_graph_rule_lines(row))
            body.append("")
    else:
        body.extend(["- Concrete Graph Rule catalogue: empty for the selected source set.", ""])

    body.extend(_limitations(catalog, len(graph_rules)))
    return "\n".join(str(item) for item in body)
