"""Raw, candidate-only recognition of two explicit Core Term relation forms.

Neither a declarative spelling nor a normative obligation proves definition
implication, admitted endpoints or acyclicity. No native fact, inverse edge,
transitive edge, Subject incidence or Property fact is emitted here.
"""

from __future__ import annotations

import hashlib
import re
from collections.abc import Mapping, Sequence
from pathlib import Path

import core_relation_registry as registry
import generate_entity_graph as graph
import graph_fact_context as facts
import term_hierarchy


_IMPLEMENTATION_PATH = Path(__file__).resolve()
_LOADED_IMPLEMENTATION_SHA256 = hashlib.sha256(_IMPLEMENTATION_PATH.read_bytes()).hexdigest()
_HIERARCHY_PATH = Path(term_hierarchy.__file__).resolve()
_LOADED_HIERARCHY_SHA256 = hashlib.sha256(_HIERARCHY_PATH.read_bytes()).hexdigest()
_KIND = {"graph_kind": "terms", "canonical_name": "NARROWER_THAN"}
_PROVIDER_ID = "caprmedio.core-term-relation-candidates"
_VERSION = "1"
_MIXED_OBLIGATION = re.compile(
    r"\Athe Term (?P<child>[^\n.][^\n]*?) \*\*must\*\* be NARROWER_THAN "
    r"(?P<parent>[^\n.][^\n]*?)\.\Z"
)


class CoreRelationCandidateError(ValueError):
    def __init__(self, code: str) -> None:
        self.code = code
        super().__init__(code)


def _digest(value: object) -> str:
    return hashlib.sha256(facts.canonical_bytes(value)).hexdigest()


def _current_code() -> None:
    facts._check_loaded_profile()
    registry._current_code()
    try:
        if (hashlib.sha256(_IMPLEMENTATION_PATH.read_bytes()).hexdigest() != _LOADED_IMPLEMENTATION_SHA256 or
                hashlib.sha256(_HIERARCHY_PATH.read_bytes()).hexdigest() != _LOADED_HIERARCHY_SHA256):
            raise CoreRelationCandidateError("profile-stale")
    except OSError as error:
        raise CoreRelationCandidateError("profile-stale") from error


def _refs(*groups: Sequence[dict]) -> list[dict]:
    distinct = {facts.canonical_bytes(ref): ref for group in groups for ref in group}
    return sorted(distinct.values(), key=facts._source_key)


def _diagnostic(code: str, source_refs: Sequence[dict] = ()) -> dict:
    return {"code": code, "severity": "info", "source_refs": _refs(source_refs), "details": {}}


def _checked_registry(repository: Path, carriers: Sequence, selection: dict,
                      registry_records: object) -> tuple[dict, dict]:
    """Compare only to the existing current raw-checked registry profile.

    Root supplies internal, prevalidated records, not client flags. Rebuilding
    once here also rejects arbitrary record descriptors and stale evidence.
    """
    if not isinstance(registry_records, Sequence) or isinstance(registry_records, (str, bytes)):
        raise CoreRelationCandidateError("relation-registry-unverified")
    authority_path = registry._authority_path(repository)
    frontier = graph.source_frontier_for(repository, repository / authority_path)
    current = registry.prepare_core_relation_registry(repository, carriers, frontier, selection)
    expected = [record for record in current.records if record["kind"]["graph_kind"] == "terms"]
    if current.diagnostics or len(expected) != 1 or expected[0]["kind"] != _KIND:
        raise CoreRelationCandidateError("relation-registry-unavailable")
    if facts.canonical_bytes(list(registry_records)) != facts.canonical_bytes(expected):
        raise CoreRelationCandidateError("relation-registry-unverified")
    return expected[0], frontier


def _subjects(pin: dict, raw: bytes) -> tuple[str, list[str], list[dict]] | None:
    """Use existing current Subject grammar, with evidence from current bytes."""
    lines, text, boundary, fields = facts._raw_parts(raw)
    governed = facts._governed_reference(pin, raw)
    if governed is None or fields.get("subjects") != "":
        return None
    frontmatter = "\n".join(text[1:boundary])
    # The outer pipeline has structurally validated the source against its
    # current raw pin. Recreate only this parser's internal Carrier from those
    # bytes; module-import class identity and caller frontmatter are irrelevant.
    parser_carrier = graph.AtomCarrier(
        atom_id=pin["atom_id"], version=pin["atom_revision"], cce_form=fields.get("cce_form", ""),
        content_role=fields.get("content_role", ""), atom_type=fields.get("type", ""),
        status=fields.get("status", ""), carrier_path=pin["carrier_path"], sha256=pin["carrier_sha256"],
        frontmatter=frontmatter, body="\n".join(text[boundary + 1:]),
    )
    try:
        relations, diagnostics = graph.parse_subject_relations(parser_carrier)
    except graph.EntityGraphError:
        return None
    if diagnostics:
        # In particular, never accept legacy subject-role aliases.
        return None
    child = [row.subject_path for row in relations if row.kind == "GOVERNS"]
    parents = [row.subject_path for row in relations if row.kind == "DEPENDS_ON"]
    if child != [governed[1]]:
        return None
    starts = [index for index in range(1, boundary) if re.fullmatch(r"  depends_on:[ \t]*.*", text[index])]
    if len(starts) != 1:
        return None
    start = starts[0]
    end = start + 1
    while end < boundary and (not text[end] or text[end].startswith("    ")):
        end += 1
    depended_ref = facts._source(pin, lines, start + 1, end,
                                 kind="canonical_atom_property", property_path="subjects.depends_on")
    return governed[1], parents, _refs([governed[0], depended_ref])


def _terminal(path: str) -> str | None:
    try:
        return graph.terminal_term(path)
    except graph.EntityGraphError:
        return None


def _recognize(claim: str, pin: dict, governed: str, parents: list[str]) -> tuple[str, str, str] | None:
    # Preserve the normative form as its own family; do not normalize must
    # away or pretend the declaration asserts an already-admitted relation.
    normative = _MIXED_OBLIGATION.fullmatch(claim)
    if normative is not None:
        child, parent = normative["child"], normative["parent"]
        family = "normative-obligation"
    else:
        # The preexisting assessor admits another fully-bold obligation form.
        # It is intentionally outside this lane's two reviewed source forms.
        if "**must**" in claim or "**NARROWER_THAN**" in claim:
            return None
        assessment = term_hierarchy.assess_hierarchy_claim(
            pin, {"governs": [_terminal(governed)], "depends_on": [_terminal(path) for path in parents]},
            {"section": "Claim", "text": claim},
        )
        if assessment["state"] != "recognized":
            return None
        child, parent = assessment["facts"][0]["child"], assessment["facts"][0]["parent"]
        family = "plain-assertion"
    if _terminal(governed) != child or sum(_terminal(path) == parent for path in parents) != 1:
        return None
    return child, parent, family


def recognize_core_term_relations(repository: Path, carriers: Sequence, selection: Mapping,
                                  registry_records: Sequence[Mapping]) -> dict:
    """Return a closed D539 candidate bundle; native admission is unperformed."""
    _current_code()
    repository = Path(repository).resolve()
    pool = facts._pool(repository, carriers)
    selected = facts._selection(selection, set(pool))
    kind_record, frontier = _checked_registry(repository, carriers, selected, registry_records)
    binding = {"implementation_sha256": _LOADED_IMPLEMENTATION_SHA256,
               "hierarchy_implementation_sha256": _LOADED_HIERARCHY_SHA256,
               "fact_context_implementation_sha256": facts._LOADED_IMPLEMENTATION_SHA256,
               "registry_implementation_sha256": registry._LOADED_IMPLEMENTATION_SHA256,
               "registry_record_sha256": kind_record["registry_record_sha256"],
               "source_frontier_sha256": frontier["source_frontier_sha256"], "selection": selected}
    profile_sha256 = _digest(binding)
    provider = {"id": _PROVIDER_ID, "version": _VERSION, "profile_sha256": profile_sha256}
    candidates, decisions, diagnostics = [], [], []
    authority_refs = kind_record["authority_inputs"]
    for atom_id in selected["atom_ids"]:
        carrier, _, _ = pool[atom_id]
        # Source evidence is re-read at use, not accepted from earlier labels.
        pin, raw = facts._carrier_pin(repository, carrier)
        _, text, _, fields = facts._raw_parts(raw)
        if (carrier.content_role not in {"Requirement", "Method", "Evaluation", "Delivery"} or
                carrier.status != "Active" or fields.get("current_scope_unit") != "CORE_META_MODEL"):
            continue
        try:
            primary = facts._primary(pin, raw, carrier.content_role)
        except facts.FactContextError as error:
            if error.code != "context-primary-ambiguous":
                raise
            diagnostics.append(_diagnostic("core-term-relation-primary-unresolved"))
            continue
        if primary is None:
            continue
        location = primary["contribution"]
        claim = "\n".join(text[location["start_line"] - 1:location["end_line"]]).strip("\n")
        if "NARROWER_THAN" not in claim:
            continue
        try:
            subject_sources = _subjects(pin, raw)
        except facts.FactContextError as error:
            if error.code != "context-property-ambiguous":
                raise
            subject_sources = None
        found = _recognize(claim, pin, subject_sources[0], subject_sources[1]) if subject_sources else None
        if found is None:
            diagnostics.append(_diagnostic("core-term-relation-source-form-unresolved", [primary]))
            continue
        child, parent, family = found
        recognizer = {"id": _PROVIDER_ID + "." + family, "version": _VERSION, "profile_sha256": profile_sha256}
        payload = {"kind": dict(_KIND), "registry_record_sha256": kind_record["registry_record_sha256"],
                   "source": {"identity": child, "graph_kind": "terms", "node_class": "Term"},
                   "target": {"identity": parent, "graph_kind": "terms", "node_class": "Term"},
                   "representation": "external_reference"}
        candidate = {"fact_class": "relation", "payload": payload, "source_ref": primary, "recognizer": recognizer}
        candidate["candidate_id"] = "core-term-relation:" + _digest(candidate)
        checks = [
            {"code": "source-form-and-pin-current", "disposition": "pass", "source_refs": [primary]},
            {"code": "source-subject-terminal-matches", "disposition": "pass", "source_refs": subject_sources[2]},
            {"code": "registry-binding-current", "disposition": "pass", "source_refs": authority_refs},
            {"code": "semantic-definition-implication", "disposition": "unresolved", "source_refs": _refs([primary], authority_refs)},
            {"code": "endpoint-admission", "disposition": "unresolved", "source_refs": [primary]},
            {"code": "acyclicity", "disposition": "unresolved", "source_refs": [primary]},
        ]
        if family == "normative-obligation":
            checks.append({"code": "normative-declaration-implies-model-relation", "disposition": "unresolved", "source_refs": [primary]})
        checks.sort(key=lambda row: row["code"])
        decision = {"candidate_id": candidate["candidate_id"], "disposition": "unresolved",
                    "evaluator": provider, "authority_inputs": authority_refs, "checks": checks}
        decision["decision_sha256"] = _digest(decision)
        candidates.append(candidate)
        decisions.append(decision)
    candidates.sort(key=lambda row: row["candidate_id"])
    decisions.sort(key=lambda row: row["candidate_id"])
    diagnostics.append(_diagnostic("core-term-relation-semantic-admission-unperformed"))
    diagnostics.sort(key=lambda row: (row["code"], facts.canonical_bytes(row["source_refs"])))
    _current_code()
    return {"provider": provider, "candidates": candidates, "admission_decisions": decisions,
            "admitted_facts": [], "diagnostics": diagnostics}
