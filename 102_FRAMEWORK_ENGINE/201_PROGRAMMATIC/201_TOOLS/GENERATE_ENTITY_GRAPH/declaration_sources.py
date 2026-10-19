"""Compose a conservative catalogue from selected current source carriers."""

from __future__ import annotations

import hashlib
import re
from collections.abc import Mapping
from pathlib import Path
from typing import Any

from current_entity_sources import _raw_body
from subject_notation import SubjectNotationError, parse_subject
from VALIDATE_ATOMS.validate_atoms_workers.authority import AuthorityContext, Obligation
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
    subjects = carrier.get("subjects")
    if not isinstance(subjects, Mapping):
        return []
    value = subjects.get("governs")
    values = value if isinstance(value, list) else [value]
    return [item for item in values if isinstance(item, str) and item.strip()]


def _single_valid_governed_subject(carrier: Mapping[str, object]) -> str | None:
    subjects = carrier.get("subjects")
    if not isinstance(subjects, Mapping):
        return None
    value = subjects.get("governs")
    values = value if isinstance(value, list) else [value]
    if len(values) != 1 or not isinstance(values[0], str) or not values[0].strip():
        return None
    try:
        parse_subject(values[0], subject_profile="approved")
    except SubjectNotationError:
        return None
    return values[0]


def _candidate_name(subject: str) -> str | None:
    try:
        components = parse_subject(subject, subject_profile="approved")
    except SubjectNotationError:
        return None
    if len(components) == 4 and components[:3] == [
        ("Entity", None),
        ("Relation", "/"),
        ("Type", "/"),
    ] and components[3][1] == ":":
        return components[3][0]
    if len(components) == 1 and components[0][1] is None and _RELATION_LIKE.fullmatch(subject):
        return subject
    return None


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
        metadata = carrier.get("metadata")
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
    metadata = carrier["metadata"]
    if metadata.get("content_role") != "Requirement" or metadata.get("type") != "Graph Rule":
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
        metadata = carrier["metadata"]
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
