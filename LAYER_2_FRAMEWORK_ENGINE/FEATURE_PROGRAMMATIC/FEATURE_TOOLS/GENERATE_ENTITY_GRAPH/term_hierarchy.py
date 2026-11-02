"""Pure Terms-Graph hierarchy recognition and analysis.

This module deliberately has no carrier I/O, registry lookup, or publication
side effect.  Its recognition result is evidence for a later native-admission
gate; it is not evidence that either endpoint is an admitted runtime Term.
"""

from __future__ import annotations

import hashlib
import re
from collections import defaultdict
from collections.abc import Mapping, Sequence


TERMS_NARROWER_THAN = "terms/NARROWER_THAN"
_SHA256 = re.compile(r"^[0-9a-f]{64}$")
_PLAIN_CLAIM = re.compile(
    r"\Athe Term (?P<child>[^\n.][^\n]*?)(?<! must be)(?<! must not be) "
    r"NARROWER_THAN (?P<parent>[^\n.][^\n]*?)\.\Z"
)
_OBLIGATION_CLAIM = re.compile(
    r"\Athe Term (?P<child>[^\n.][^\n]*?) \*\*must\*\* be \*\*NARROWER_THAN\*\* "
    r"(?P<parent>[^\n.][^\n]*?)\.\Z"
)


def _sha256(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def _diagnostic(code: str, message: str, *, severity: str = "warning", **details: object) -> dict[str, object]:
    result: dict[str, object] = {"severity": severity, "code": code, "message": message}
    if details:
        result["details"] = details
    return result


def _string(value: object) -> str | None:
    return value if isinstance(value, str) and value else None


def _string_list(value: object) -> list[str]:
    if isinstance(value, str):
        return [value]
    if isinstance(value, Sequence) and not isinstance(value, (bytes, bytearray)):
        return [item for item in value if isinstance(item, str) and item]
    return []


def _contribution_text(contribution: Mapping[str, object]) -> tuple[str | None, str | None]:
    """Read the already-extracted primary Claim contribution.

    The surrounding builder owns Markdown section and fenced-code handling.  A
    contribution is therefore one Claim section, never a whole Carrier body.
    The two spelling pairs retain compatibility with its existing normalized
    records without introducing a new Carrier or frontmatter grammar.
    """

    section = _string(contribution.get("primary_section")) or _string(contribution.get("section"))
    claim = _string(contribution.get("primary_claim")) or _string(contribution.get("text"))
    return section, claim


def _carrier_evidence(carrier: Mapping[str, object], section: str, claim: str) -> tuple[dict[str, object] | None, list[dict[str, object]]]:
    atom_id = _string(carrier.get("atom_id"))
    revision = carrier.get("atom_revision", carrier.get("version"))
    carrier_path = _string(carrier.get("carrier_path"))
    carrier_sha256 = _string(carrier.get("carrier_sha256"))
    missing = [
        name
        for name, value in (
            ("atom_id", atom_id),
            ("atom_revision", revision if type(revision) is int and revision >= 1 else None),
            ("carrier_path", carrier_path),
            ("carrier_sha256", carrier_sha256 if carrier_sha256 and _SHA256.fullmatch(carrier_sha256) else None),
        )
        if value is None
    ]
    if missing:
        return None, [
            _diagnostic(
                "hierarchy-source-evidence-incomplete",
                "A hierarchy candidate lacks the immutable Carrier evidence required for a fact.",
                severity="error",
                missing=missing,
            )
        ]
    assert isinstance(revision, int)
    assert atom_id is not None and carrier_path is not None and carrier_sha256 is not None
    # The section hash covers the normalized source contribution (section label
    # and exact Claim string); claim_sha256 separately makes the parsed span
    # independently auditable.
    return {
        "atom_id": atom_id,
        "atom_revision": revision,
        "carrier_path": carrier_path,
        "carrier_sha256": carrier_sha256,
        "primary_section": section,
        "primary_section_sha256": _sha256(f"{section}\n{claim}"),
        "claim_sha256": _sha256(claim),
    }, []


def _subjects(governing_subjects: object) -> tuple[set[str], set[str], list[dict[str, object]]]:
    """Return exact governed and depended subject values supplied by the caller.

    No terminal-segment, spelling, or incidence inference happens here.  The
    accepted shapes are the existing ``governs``/``depends_on`` grouping and
    the existing relation-record sequence (``kind`` plus ``subject_path``).
    """

    governs: set[str] = set()
    depends_on: set[str] = set()
    diagnostics: list[dict[str, object]] = []
    if isinstance(governing_subjects, Mapping):
        governs.update(_string_list(governing_subjects.get("governs", governing_subjects.get("GOVERNS"))))
        depends_on.update(
            _string_list(governing_subjects.get("depends_on", governing_subjects.get("DEPENDS_ON")))
        )
        return governs, depends_on, diagnostics
    if isinstance(governing_subjects, Sequence) and not isinstance(governing_subjects, (str, bytes, bytearray)):
        for row in governing_subjects:
            if not isinstance(row, Mapping):
                diagnostics.append(
                    _diagnostic(
                        "hierarchy-subjects-invalid",
                        "A hierarchy subject record is not a mapping.",
                        severity="error",
                    )
                )
                continue
            kind = _string(row.get("kind"))
            subject = _string(row.get("subject_path"))
            if kind == "GOVERNS" and subject:
                governs.add(subject)
            elif kind == "DEPENDS_ON" and subject:
                depends_on.add(subject)
        return governs, depends_on, diagnostics
    diagnostics.append(
        _diagnostic(
            "hierarchy-subjects-invalid",
            "Hierarchy subjects must be existing subject groups or relation records.",
            severity="error",
        )
    )
    return governs, depends_on, diagnostics


def assess_hierarchy_claim(
    carrier: Mapping[str, object],
    governing_subjects: object,
    contribution: Mapping[str, object],
) -> dict[str, object]:
    """Recognize one current primary-Claim NARROWER_THAN assertion.

    Recognition is intentionally narrower than general prose parsing: only
    the two anchored current primary Claim forms are accepted.  The returned
    fact has a graph-qualified relation and child-to-parent direction, but has
    no native-admission verdict.
    """

    section, claim = _contribution_text(contribution)
    if section != "Claim" or claim is None:
        diagnostics = [
            _diagnostic(
                "hierarchy-primary-claim-unavailable",
                "Only an already-extracted primary Claim section may contribute a hierarchy fact.",
                section=section,
            )
        ]
        return {"state": "not_relation", "facts": [], "source_evidence": [], "diagnostics": diagnostics}

    # A primary Claim without this relation is simply irrelevant.  A Claim
    # trying to use NARROWER_THAN in another surface form is an unsupported
    # candidate rather than a relation inferred from near-matching prose.
    if "NARROWER_THAN" not in claim:
        return {"state": "not_relation", "facts": [], "source_evidence": [], "diagnostics": []}
    match = _PLAIN_CLAIM.fullmatch(claim) or _OBLIGATION_CLAIM.fullmatch(claim)
    if match is None:
        return {
            "state": "unsupported_candidate",
            "facts": [],
            "source_evidence": [],
            "diagnostics": [
                _diagnostic(
                    "hierarchy-claim-form-unsupported",
                    "NARROWER_THAN must use an exact current primary Claim form.",
                )
            ],
        }

    child = match.group("child")
    parent = match.group("parent")
    evidence, diagnostics = _carrier_evidence(carrier, section, claim)
    if evidence is None:
        return {
            "state": "unsupported_candidate",
            "facts": [],
            "source_evidence": [],
            "diagnostics": diagnostics,
        }
    governed, depended, subject_diagnostics = _subjects(governing_subjects)
    diagnostics.extend(subject_diagnostics)
    if subject_diagnostics or child not in governed or parent not in depended:
        diagnostics.append(
            _diagnostic(
                "hierarchy-claim-subject-mismatch",
                "The Claim child must be governed and its parent must be depended on exactly.",
                severity="error",
                child=child,
                parent=parent,
                governs=sorted(governed),
                depends_on=sorted(depended),
            )
        )
        return {
            "state": "target_mismatch",
            "facts": [],
            "source_evidence": [evidence],
            "diagnostics": diagnostics,
        }

    fact = {
        "kind": TERMS_NARROWER_THAN,
        "relation": TERMS_NARROWER_THAN,
        "child": child,
        "parent": parent,
        "direction": "child_to_parent",
        "source_evidence": evidence,
    }
    diagnostics.append(
        _diagnostic(
            "native-admission-unassessed",
            "Recognition is not native-Term admission; the caller must apply its registry and source-context gate.",
        )
    )
    return {"state": "recognized", "facts": [fact], "source_evidence": [evidence], "diagnostics": diagnostics}


def _fact_sort_key(fact: Mapping[str, object]) -> tuple[str, str, str, str]:
    evidence = fact.get("source_evidence")
    path = evidence.get("carrier_path", "") if isinstance(evidence, Mapping) else ""
    return (
        str(fact.get("child", "")), str(fact.get("parent", "")), str(path),
        str(fact.get("kind", fact.get("relation", ""))),
    )


def _cycles(parents_by_term: Mapping[str, Sequence[str]]) -> list[list[str]]:
    """Find canonical directed cycles in child-to-parent edges."""

    found: set[tuple[str, ...]] = set()
    active: list[str] = []
    active_index: dict[str, int] = {}
    seen: set[str] = set()

    def visit(term: str) -> None:
        seen.add(term)
        active_index[term] = len(active)
        active.append(term)
        for parent in parents_by_term.get(term, ()):
            if parent in active_index:
                cycle = active[active_index[parent] :]
                rotations = [tuple(cycle[index:] + cycle[:index]) for index in range(len(cycle))]
                found.add(min(rotations))
            elif parent not in seen:
                visit(parent)
        active.pop()
        del active_index[term]

    for term in sorted(parents_by_term):
        if term not in seen:
            visit(term)
    return [list(cycle) for cycle in sorted(found)]


def _ancestors(parents_by_term: Mapping[str, Sequence[str]]) -> dict[str, list[str]]:
    result: dict[str, list[str]] = {}
    for term in sorted(parents_by_term):
        found: set[str] = set()
        pending = list(parents_by_term[term])
        while pending:
            parent = pending.pop()
            if parent == term or parent in found:
                continue
            found.add(parent)
            pending.extend(parents_by_term.get(parent, ()))
        result[term] = sorted(found)
    return result


def analyze_hierarchy(terms: Sequence[str], facts: Sequence[Mapping[str, object]]) -> dict[str, object]:
    """Analyze only admitted native Terms and graph-qualified hierarchy facts.

    External endpoints remain evidence, never native nodes.  An external parent
    prevents a native child from being called an isolated root and records that
    root coverage is unresolved.
    """

    diagnostics: list[dict[str, object]] = []
    native_terms: set[str] = set()
    for term in terms:
        if not isinstance(term, str) or not term:
            diagnostics.append(
                _diagnostic(
                    "native-term-invalid",
                    "A native Terms-Graph term must be a nonempty string.",
                    severity="error",
                )
            )
            continue
        if term in native_terms:
            diagnostics.append(
                _diagnostic(
                    "native-term-duplicate",
                    "Duplicate native Term input was de-duplicated for analysis.",
                    term=term,
                )
            )
        native_terms.add(term)

    parents: dict[str, set[str]] = {term: set() for term in native_terms}
    external_references: list[dict[str, object]] = []
    native_edges: dict[tuple[str, str], dict[str, object]] = {}
    external_parent_terms: dict[str, set[str]] = defaultdict(set)
    for fact in facts:
        relation = fact.get("relation")
        kind = fact.get("kind", relation)
        child = fact.get("child")
        parent = fact.get("parent")
        if relation != kind:
            diagnostics.append(
                _diagnostic(
                    "hierarchy-kind-relation-mismatch",
                    "A hierarchy fact cannot name different kind and relation values.",
                    severity="error",
                    kind=kind,
                    relation=relation,
                )
            )
            continue
        if kind != TERMS_NARROWER_THAN:
            diagnostics.append(
                _diagnostic(
                    "hierarchy-kind-unsupported",
                    "Only terms/NARROWER_THAN fact kinds are accepted by this hierarchy analyzer.",
                    severity="error",
                    kind=kind,
                )
            )
            continue
        if not isinstance(child, str) or not child or not isinstance(parent, str) or not parent:
            diagnostics.append(
                _diagnostic(
                    "hierarchy-fact-invalid",
                    "A hierarchy fact requires nonempty child and parent Terms.",
                    severity="error",
                )
            )
            continue
        if fact.get("direction") != "child_to_parent":
            diagnostics.append(
                _diagnostic(
                    "hierarchy-direction-invalid",
                    "A hierarchy fact must explicitly point from child to parent.",
                    severity="error",
                    child=child,
                    parent=parent,
                )
            )
            continue
        if child in native_terms and parent in native_terms:
            key = (child, parent)
            prior = native_edges.get(key)
            if prior is None or _fact_sort_key(fact) < _fact_sort_key(prior):
                native_edges[key] = dict(fact)
            parents[child].add(parent)
            continue

        external = dict(fact)
        endpoints: list[dict[str, str]] = []
        if child not in native_terms:
            endpoints.append({"role": "child", "term": child})
        if parent not in native_terms:
            endpoints.append({"role": "parent", "term": parent})
            if child in native_terms:
                external_parent_terms[child].add(parent)
        external["external_endpoints"] = endpoints
        external_references.append(external)

    parents_by_term = {term: sorted(parents[term]) for term in sorted(native_terms)}
    edges = [native_edges[key] for key in sorted(native_edges)]
    external_references.sort(key=_fact_sort_key)
    for term in sorted(external_parent_terms):
        diagnostics.append(
            _diagnostic(
                "root-coverage-unresolved",
                "A native child has an external hierarchy parent, so it cannot be classified as an isolated root.",
                term=term,
                external_parents=sorted(external_parent_terms[term]),
            )
        )
    cycles = _cycles(parents_by_term)
    for cycle in cycles:
        diagnostics.append(
            _diagnostic(
                "terms-narrower-than-cycle",
                "NARROWER_THAN relations contain a directed cycle.",
                severity="error",
                cycle=cycle,
            )
        )
    roots = [
        term
        for term in sorted(native_terms)
        if not parents_by_term[term] and term not in external_parent_terms
    ]
    return {
        "edges": edges,
        "external_references": external_references,
        "parents_by_term": parents_by_term,
        "ancestors_by_term": _ancestors(parents_by_term),
        "roots": roots,
        "cycles": cycles,
        "diagnostics": diagnostics,
    }
