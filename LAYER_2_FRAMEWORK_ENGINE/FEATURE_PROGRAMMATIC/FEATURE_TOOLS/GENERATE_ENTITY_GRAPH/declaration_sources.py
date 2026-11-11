"""Compose a conservative catalogue from selected current source carriers."""

from __future__ import annotations

import hashlib
import re
from collections.abc import Mapping
from pathlib import Path
from typing import Any

from current_entity_sources import _raw_body
from carrier_aliases import carrier_read_view, matches_named_value
import subject_notation as notation
from subject_notation import SubjectNotationError, parse_subject_expression
from VALIDATE_ATOMS.validate_atoms_workers.authority import AuthorityContext, Obligation
from VALIDATE_ATOMS.validate_atoms_workers.parsing import CarrierError, parse_carrier
from VALIDATE_ATOMS.validate_atoms_workers.check_support import Check
from VALIDATE_ATOMS.validate_atoms_workers.check_sections import GRAPH_RULE_SOURCES
from VALIDATE_ATOMS.validate_atoms_workers.check_sections import _headings as body_headings
from VALIDATE_ATOMS.validate_atoms_workers.graph_rule_body import validated_graph_rule_payload
from VALIDATE_ATOMS.validate_atoms_workers.support_authority import require_sources


Record = dict[str, Any]
_METADATA_FIELDS = (
    "meaning",
    "direction",
    "inverse",
    "authority_effect",
    "transitivity",
    "applicability",
    "status",
    "exclusive_purpose",
)
_RELATION_LIKE = re.compile(r"[A-Z][A-Z0-9_]*\Z")
_OWNED_RELATION = re.compile(
    r"\b(?P<name>[A-Z][A-Z0-9_]*)\s+Relation"
    r"(?:\s+from\s+Entity\s+[A-Z][A-Za-z0-9_]*\s+to\s+Entity\s+[A-Z][A-Za-z0-9_]*)?"
    r"\s+(?:in|within)\s+the\s+"
    r"(?P<graph>[A-Z][A-Za-z0-9]*(?: [A-Z][A-Za-z0-9]*)* Graph)\b"
)
_GRAPH_MENTION = re.compile(
    r"\b(?:in|within)\s+the\s+(?P<graph>[A-Z][A-Za-z0-9]*(?: [A-Z][A-Za-z0-9]*)* Graph)\b"
)


def _view(carrier: Mapping[str, object]) -> Mapping[str, object]:
    """Use migrated Role/Form and Subject aliases without changing evidence."""

    value = carrier.get("read_view")
    if isinstance(value, Mapping):
        return value
    metadata = carrier.get("metadata")
    return carrier_read_view(dict(metadata)) if isinstance(metadata, Mapping) else {}


def _source(carrier: Mapping[str, object]) -> Record | None:
    value = carrier.get("source")
    if not isinstance(value, Mapping):
        return None
    atom_id, version = value.get("atom_id"), value.get("version")
    if not isinstance(atom_id, str) or not atom_id.strip() or type(version) is not int or version < 1:
        return None
    return {key: item for key, item in value.items()}


def _source_with_matching_bytes(
    source: Record | None, raw: object, raw_body: object
) -> Record | None:
    if source is None or not isinstance(raw, bytes) or not isinstance(raw_body, str):
        return None
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError:
        return None
    if hashlib.sha256(text.encode("utf-8")).hexdigest() != source.get("sha256"):
        return None
    try:
        exact_body = _raw_body(text, Path(str(source.get("path", "supplied.md"))))
    except ValueError:
        return None
    if raw_body != exact_body:
        return None
    return source


def _subjects(carrier: Mapping[str, object]) -> list[str]:
    subjects = _subjects_mapping(carrier)
    if not isinstance(subjects, Mapping):
        return []
    value = subjects.get("governs")
    values = value if isinstance(value, list) else [value]
    return [item for item in values if isinstance(item, str) and item.strip()]


def _single_valid_governed_subject(carrier: Mapping[str, object]) -> str | None:
    subjects = _subjects_mapping(carrier)
    if not isinstance(subjects, Mapping):
        return None
    value = subjects.get("governs")
    values = value if isinstance(value, list) else [value]
    if len(values) != 1 or not isinstance(values[0], str) or not values[0].strip():
        return None
    try:
        parse_subject_expression(values[0], subject_profile="approved")
    except SubjectNotationError:
        return None
    return values[0]


def _subjects_mapping(carrier: Mapping[str, object]) -> Mapping[str, object] | None:
    subjects = carrier.get("subjects")
    if not isinstance(subjects, Mapping):
        subjects = _view(carrier).get("subjects")
    if not isinstance(subjects, Mapping):
        return None
    return carrier_read_view({"subjects": dict(subjects)}).get("subjects")


def _candidate_name(subject: str) -> str | None:
    try:
        expression = parse_subject_expression(subject, subject_profile="approved").expression
    except SubjectNotationError:
        return None
    if not isinstance(expression, notation.Path) or not isinstance(expression.head, notation.Name):
        return _defined_relation_name(subject)
    if expression.value_format is not None or expression.value_cardinality is not None:
        return None
    if expression.head.value == "Entity" and len(expression.steps) == 3:
        first, second, last = expression.steps
        if (first.operator == second.operator == "/" and last.operator == ":"
                and isinstance(first.operand, notation.Name) and first.operand.value == "Relation"
                and isinstance(second.operand, notation.Name) and second.operand.value == "Type"
                and isinstance(last.operand, notation.ValueLiteral)):
            return last.operand.value
    if not expression.steps and _RELATION_LIKE.fullmatch(expression.head.value):
        return expression.head.value
    return _defined_relation_name(subject)


def _defined_relation_name(subject: str) -> str | None:
    expression = parse_subject_expression(subject, subject_profile="approved").expression
    paths = expression.endpoints if isinstance(expression, notation.RelationChain) else (expression,)
    names = []
    for path in paths:
        if not path.steps:
            continue
        final = path.steps[-1]
        parent = path.steps[-2].operand if len(path.steps) > 1 else path.head
        if (final.operator == "//" and isinstance(final.operand, notation.Name)
                and isinstance(parent, notation.Name) and parent.value == "Relation"
                and _RELATION_LIKE.fullmatch(final.operand.value)):
            names.append(final.operand.value)
    return names[0] if len(names) == 1 else None


def _definition_metadata_matches(carrier: dict, source: Record, subject: str) -> bool:
    try:
        parsed = parse_carrier(carrier["raw"], Path(source["path"]))
    except CarrierError:
        return False
    parsed_view = carrier_read_view(parsed.metadata)
    view = _view(carrier)
    return (all(parsed_view.get(field) == view.get(field)
                for field in ("atom_id", "version", "status", "type"))
            and _single_valid_governed_subject({"subjects": parsed_view.get("subjects")}) == subject)


def resolve_relation_authorities(carriers: list[dict], names: list[str]) -> dict[str, Record]:
    """Bind canonical names to exact supplied Active Relation Definition sources.

    This is identity evidence only; unavailable relation metadata and admission
    constraints remain the responsibility of the existing admission pipeline.
    """
    candidates: dict[str, list[Record]] = {name: [] for name in names}
    for carrier in carriers:
        metadata = _view(carrier)
        if not matches_named_value(metadata.get("type"), "Relation Definition"):
            continue
        subject = _single_valid_governed_subject(carrier)
        if subject is None:
            continue
        name = _defined_relation_name(subject)
        if name not in candidates:
            continue
        source = _source_with_matching_bytes(_source(carrier), carrier.get("raw"), carrier.get("raw_body"))
        if not _active_source_matches_metadata(source, metadata):
            continue
        if not _definition_metadata_matches(carrier, source, subject):
            continue
        if source not in candidates[name]:
            candidates[name].append(source)
    result = {}
    for name, sources in candidates.items():
        if len(sources) != 1:
            raise ValueError(f"Relation authority {name} requires one exact Active Definition; found {len(sources)}")
        result[name] = sources[0]
    return result


def _scope(body: object) -> str | None:
    if not isinstance(body, str):
        return None
    lines = body.splitlines()
    scopes = [row for row in body_headings(body) if row[:2] == (2, "Scope")]
    if len(scopes) != 1:
        return None
    start = scopes[0][2]
    end = next((row[2] for row in body_headings(body) if row[2] > start and row[0] <= 2), len(lines))
    return "\n".join(lines[start + 1 : end])


def _graph_kind(scope: str | None, name: str) -> str | None:
    if scope is None:
        return None
    plain = scope.replace("**", "").replace("`", "")
    graphs = []
    for sentence in re.split(r"(?<=[.!?])\s+|\n+", plain):
        names = [match for match in _OWNED_RELATION.finditer(sentence) if match.group("name") == name]
        if len(names) != 1:
            continue
        mentions = {match.group("graph") for match in _GRAPH_MENTION.finditer(sentence)}
        if len(mentions) == 1 and names[0].group("graph") in mentions:
            graphs.append(names[0].group("graph"))
    graphs = sorted(set(graphs))
    return graphs[0] if len(graphs) == 1 else None


def _evidence(source: Record | None, subject: str, body: object, scope: str | None) -> Record:
    return {
        "source": source,
        "subject": subject,
        "scope": scope,
        "body": body if isinstance(body, str) else None,
    }


def _authority_rows(carriers: list[dict]) -> list[Record]:
    rows: list[Record] = []
    for carrier in carriers:
        if not isinstance(carrier, Mapping):
            continue
        binding = carrier.get("source")
        metadata = _view(carrier)
        raw = carrier.get("raw")
        if isinstance(binding, Mapping) and isinstance(metadata, Mapping) and isinstance(raw, bytes):
            try:
                text = raw.decode("utf-8")
            except UnicodeDecodeError:
                continue
            rows.append({"binding": dict(binding), "metadata": dict(metadata), "text": text})
    return rows


def _body_check(carriers: list[dict]) -> Check:
    # Check only the exact source bytes and metadata provided by the caller.
    # require_sources verifies them against the current support manifests.
    context = AuthorityContext([], 0, 0, 0, [], (), {}, True)
    obligation = Obligation(
        "declaration.graph_rule.body",
        [],
        True,
        "Validate the body under currently verified Graph Rule authority.",
    )
    return Check(obligation, context, {"sources": _authority_rows(carriers)})


def _active_source_matches_metadata(
    source: Record | None, metadata: Mapping[str, object]
) -> bool:
    return bool(
        source is not None
        and metadata.get("atom_id") == source.get("atom_id")
        and type(metadata.get("version")) is int
        and metadata.get("version") == source.get("version")
        and metadata.get("status") in {"Active", "active"}
    )


def _add_relation_candidate(
    carrier: dict,
    source: Record | None,
    metadata: Mapping[str, object],
    subject: str,
    relation_types: dict[tuple[str, str], Record],
    unresolved: list[Record],
) -> None:
    name = _candidate_name(subject)
    if name is None:
        return
    body = carrier.get("raw_body")
    scope = _scope(body)
    graph_kind = _graph_kind(scope, name)
    reason = None
    if source is None:
        reason = "Relation Type candidate lacks a matching exact source Atom ID, Version, and bytes."
    elif not _active_source_matches_metadata(source, metadata):
        reason = "Relation Type candidate is not established by an Active source Atom."
    elif graph_kind is None:
        reason = "The source Scope does not unambiguously establish this Relation name and owning graph kind."
    if reason:
        unresolved.append(
            {
                "source": source,
                "subject": subject,
                "reason": reason,
                "body": body if isinstance(body, str) else None,
            }
        )
        return

    assert source is not None and graph_kind is not None
    key = (graph_kind, name)
    row = relation_types.setdefault(
        key,
        {
            "graph_kind": graph_kind,
            "canonical_name": name,
            "metadata": {field: None for field in _METADATA_FIELDS},
            "sources": [],
            "evidence": [],
        },
    )
    if source not in row["sources"]:
        row["sources"].append(source)
        row["evidence"].append(_evidence(source, subject, body, scope))


def _graph_rule_candidate(
    carrier: dict, carriers: list[dict], source: Record | None
) -> tuple[Record | None, Record | None, bool]:
    metadata = _view(carrier)
    if not matches_named_value(metadata.get("content_role"), "Requirement") or not matches_named_value(metadata.get("type"), "Graph Rule"):
        return None, None, False

    body = carrier.get("raw_body")
    subject = _single_valid_governed_subject(carrier)
    check = _body_check(carriers)
    authority_ok = require_sources(check, GRAPH_RULE_SOURCES)
    payload = validated_graph_rule_payload(body if isinstance(body, str) else "", check)
    diagnostics = [finding["reason"] for finding in check.findings]
    diagnostics.extend(gap["reason"] for gap in check.gaps)
    source_ok = _active_source_matches_metadata(source, metadata)
    authority_gap = not authority_ok

    reasons = []
    if not source_ok:
        reasons.append("Graph Rule source is not an exact Active source Atom identity/version/byte binding.")
    if subject is None:
        reasons.append("Graph Rule requires exactly one nonempty valid governed Subject.")
    if authority_gap:
        reasons.append("Current source-bound Graph Rule governing authority is missing or changed.")
    if not isinstance(body, str):
        reasons.append("Exact source raw_body is unavailable.")
    if diagnostics:
        reasons.append("Graph Rule body failed structural validation: " + " | ".join(diagnostics))
    elif payload is None:
        reasons.append("Graph Rule body validation returned no payload.")

    if (
        source_ok
        and isinstance(body, str)
        and subject is not None
        and authority_ok
        and payload is not None
        and not diagnostics
    ):
        return (
            {
                "source": source,
                "subject": subject,
                "summary": payload.summary.strip(),
                "yaml_block": payload.operative_block,
                "evidence": body if isinstance(body, str) else None,
                "authority": list(check.obligation.authority),
            },
            None,
            authority_gap,
        )

    return (
        None,
        {
            "source": source,
            "subject": subject or "unresolved governed Subject",
            "reason": "; ".join(reasons) or "Graph Rule candidate is unresolved.",
            "body": body if isinstance(body, str) else None,
            "summary": payload.summary.strip() if payload is not None else None,
            "yaml_block": payload.operative_block if payload is not None else None,
        },
        authority_gap,
    )


def _sort_catalog(
    relation_types: dict[tuple[str, str], Record],
    graph_rules: list[Record],
    unresolved: list[Record],
) -> tuple[list[Record], list[Record], list[Record]]:
    for row in relation_types.values():
        order = sorted(
            range(len(row["sources"])),
            key=lambda index: (row["sources"][index]["atom_id"], row["sources"][index]["version"]),
        )
        row["sources"] = [row["sources"][index] for index in order]
        row["evidence"] = [row["evidence"][index] for index in order]
    unresolved.sort(
        key=lambda row: (
            str((row.get("source") or {}).get("atom_id", "")),
            str((row.get("source") or {}).get("version", "")),
            str(row.get("subject", "")),
            str(row.get("reason", "")),
        )
    )
    return (
        [relation_types[key] for key in sorted(relation_types)],
        sorted(graph_rules, key=lambda row: (row["source"]["atom_id"], row["source"]["version"])),
        unresolved,
    )


def compose_declaration_catalog(carriers: list[dict]) -> Record:
    """Return source-backed declaration candidates without guessing authority.

    Relation metadata remains unavailable unless a future admitted explicit
    metadata carrier supplies it. Graph Rule bodies are admitted only when the
    supplied exact support-source bytes satisfy the current support manifests.
    """

    relation_types: dict[tuple[str, str], Record] = {}
    graph_rules: list[Record] = []
    unresolved: list[Record] = []
    limitations = [
        "CA-R-806 descriptive metadata is not decoded from prose; unavailable fields remain explicit gaps."
    ]
    rule_authority_gap = False

    for carrier in carriers:
        metadata = _view(carrier)
        source = _source(carrier)
        source = _source_with_matching_bytes(source, carrier.get("raw"), carrier.get("raw_body"))
        for subject in _subjects(carrier):
            _add_relation_candidate(carrier, source, metadata, subject, relation_types, unresolved)
        rule, gap, authority_gap = _graph_rule_candidate(carrier, carriers, source)
        if rule is not None:
            graph_rules.append(rule)
        if gap is not None:
            unresolved.append(gap)
        rule_authority_gap = rule_authority_gap or authority_gap

    relation_types, graph_rules, unresolved = _sort_catalog(relation_types, graph_rules, unresolved)
    if rule_authority_gap:
        limitations.append(
            "No Graph Rule is admitted unless all current source-bound support carriers are supplied and verified."
        )
    return {
        "relation_types": relation_types,
        "graph_rules": graph_rules,
        "unresolved": unresolved,
        "limitations": limitations,
    }
