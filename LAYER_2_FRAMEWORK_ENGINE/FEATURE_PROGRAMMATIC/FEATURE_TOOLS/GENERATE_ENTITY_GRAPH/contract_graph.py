"""Source-bound formal-contract inventory; no CFEL execution or inference."""

from __future__ import annotations

import re
from collections import defaultdict
from collections.abc import Mapping
from dataclasses import replace
from typing import Any

import subject_notation as notation
from carrier_aliases import carrier_read_view
from cfel_claim_constraints import (
    claim_cfel_blocks,
    claim_fenced_blocks,
    claim_prose,
    extract_claim_constraints,
    has_prose_claim,
    section_text,
)
from current_subject_graph import (
    _model_target,
    _relation_definition_target,
    _target_kind,
    compose_narrowing_graph,
    namespace_local_expression,
)
from readable_entity_tree_data import primary_tree, read_edges, read_nodes


Record = dict[str, Any]
Candidate = tuple[Record, Mapping[str, Any], str | None, notation.Path | notation.RelationChain | None]
_RMED = {"Requirement", "Method", "Evaluation", "Delivery"}
_DECLARATION_FORMS = {"Declaration", "Relation Definition", "Entity Definition"}
_COMPONENT_ROOTS = {"CFEL", "Carrier", "Term"}
_MODEL_APPLICABILITY_SELECTORS = {
    "(Node,Node/**,.**)": "Node",
    "(Node,Node.**)": "Node",
}
_SCOPE_UNIT_DECLARATION_FORM = "Scope Unit Declaration"
_DECLARED_INSTANCE_KINDS = frozenset({"Scope Unit", "Project"})
_KNOWN_NAMED_CONTRACT_CONTEXTS = {
    "Projection//PROJECT_SCOPE_UNIT_GRAPH": "Projection",
    "NamedSelection//ExtensionSources": "Named Selection",
    "PROJECTSTRUCTURE//CAPRMEDIO": "PROJECT STRUCTURE",
}
_NAMESPACED_SELECTOR = re.compile(r"^\s*(?:CAPRMEDIO\s*<\+\s*(?:MODEL|STRUCTURE)|CAPRMEDIO_(?:MODEL|STRUCTURE))\s*<\+\s*(.+?)\s*$")
_METADATA = re.compile(
    r"^\s*\(\((?P<name>[A-Za-z][A-Za-z0-9_]*)\)\)\s*"
    r"(?:(?P<notation>==)\s*(?P<short>[^;\r\n]+)|>\|\s*Derivation\s*==\s*(?P<derivation>Direct|Derived))\s*;?\s*$",
    re.M,
)
_CLASSIFICATION = re.compile(r"^\s*Relation//(?P<name>[A-Za-z][A-Za-z0-9_]*)\s*\(\(HAS_CLASSIFICATION\)\)\s*Derivation\s*==\s*(?P<value>Direct|Derived)\s*;?\s*$", re.M)


def _source_ref(source: Mapping[str, Any]) -> str:
    return f"{source['atom_id']}@{source['version']}"


def _view(carrier: Mapping[str, Any]) -> Mapping[str, Any]:
    view = carrier.get("read_view")
    if isinstance(view, Mapping):
        return view
    metadata = carrier.get("metadata")
    return carrier_read_view(dict(metadata)) if isinstance(metadata, Mapping) else {}


def _active(carrier: Mapping[str, Any]) -> str | None:
    subjects = carrier.get("subjects")
    if not isinstance(subjects, Mapping):
        return None
    value = carrier_read_view({"subjects": dict(subjects)})["subjects"].get("governs")
    values = value if isinstance(value, list) else [value]
    return values[0] if len(values) == 1 and isinstance(values[0], str) and values[0].strip() else None


def _local_raw_selector(subject: str) -> str:
    namespaced = _NAMESPACED_SELECTOR.match(subject)
    return namespaced.group(1) if namespaced else subject


def _entry(carrier: Mapping[str, Any], subject: str, target: str, kind: str) -> Record:
    clauses, diagnostics = extract_claim_constraints(carrier)
    source = dict(carrier["source"])
    return {
        "source": source, "subject": subject, "target": target, "kind": kind,
        "blocks": claim_fenced_blocks(carrier), "cfel_blocks": claim_cfel_blocks(carrier),
        "clauses": clauses, "prose": claim_prose(carrier),
        "prose_claim": has_prose_claim(carrier),
        "claim_scope": section_text(carrier, "Claim Scope"),
        "semantics": section_text(carrier, "Semantics"),
        "details": section_text(carrier, "Details"),
        "diagnostics": [{**row, "source": row.get("source", source)} for row in diagnostics],
    }


def _gap(carrier: Mapping[str, Any], message: str, subject: str | None = None) -> Record:
    return {**_entry(carrier, subject or "", "", "unbound"), "message": message}


def _relation_name(value: str) -> str:
    return value.removeprefix("Relation//")


def _token(value: object) -> str | None:
    """Return a declared Relation name from an exact Relation reference only."""

    if not isinstance(value, str):
        return None
    text = value.strip()
    if text.startswith("@") and not text.startswith("@Relation//"):
        return None
    text = text.removeprefix("@Relation//").removeprefix("Relation//")
    match = re.fullmatch(r"\(\(([A-Za-z][A-Za-z0-9_]*)\)\)", text)
    if match:
        return match.group(1)
    return text if re.fullmatch(r"[A-Za-z][A-Za-z0-9_]*", text) else None


def _component_target(
    expression: notation.Path | notation.RelationChain,
) -> tuple[str, str] | None:
    """Admit an explicit CFEL component target without making a tree edge.

    ``CFEL <+`` declares a component family. Its right endpoint can itself be
    a component, a dependent Property of a component, or one named component
    instance. These are catalog records only: composition never becomes
    NARROWER_THAN evidence.
    """

    expression = namespace_local_expression(expression) or expression
    if isinstance(expression, notation.Path):
        return (
            ("component", notation.render_subject(expression))
            if isinstance(expression.head, notation.Name) and expression.head.value in _COMPONENT_ROOTS
            else None
        )
    first = expression.endpoints[0]
    if (
        isinstance(first.head, notation.Name)
        and first.head.value == "CFEL"
        and len(expression.endpoints) == 2 and len(expression.links) == 1
        and expression.links[0].operator == "<+" and expression.links[0].relation_type is None
        and isinstance(expression.endpoints[1], notation.Path)
    ):
        right = expression.endpoints[1]
        kind = _target_kind(right)
        if kind == "primary_node":
            return "component", notation.render_subject(right)
        if kind in {"property", "instance"}:
            return kind, _model_target(right)
    return None


def _target(expression: notation.Path | notation.RelationChain) -> tuple[str, str] | None:
    """Map an exact active Subject to one already-declarable target category."""

    expression = namespace_local_expression(expression) or expression
    relation = _relation_definition_target(expression)
    if relation is not None:
        target, _ = relation
        return "relation", _relation_name(target)
    component = _component_target(expression)
    if component is not None:
        return component
    if isinstance(expression, notation.Path):
        kind = _target_kind(expression)
        if kind in {"primary_node", "property", "instance"}:
            return kind, _model_target(expression)
        if kind == "relation":
            return "relation", _relation_name(_model_target(expression))
    return None


def _conditional_target(
    expression: notation.Path | notation.RelationChain, catalog: Mapping[tuple[str, str], list[Record]],
) -> tuple[tuple[str, str], str, Record] | None:
    """Bind only known value or qualifier conditions to an existing target.

    The condition remains on the source entry.  It neither admits a qualified
    Node nor expands a selector over possible model targets.
    """

    expression = namespace_local_expression(expression) or expression
    if isinstance(expression, notation.RelationChain):
        if len(expression.links) != 1 or expression.links[0].operator not in {">|", "|<"}:
            return None
        subject, axis = (
            (expression.endpoints[0], expression.endpoints[1])
            if expression.links[0].operator == ">|"
            else (expression.endpoints[1], expression.endpoints[0])
        )
        target = _target(subject)
        if target is not None and target in catalog:
            return target, "classification_context", {"axis": notation.render_subject(axis)}
        return None
    if not isinstance(expression, notation.Path):
        return None
    for index, step in enumerate(expression.steps):
        if step.operator not in {":", ":="}:
            continue
        base = replace(expression, steps=expression.steps[:index], value_format=None, value_cardinality=None)
        target = _target(base)
        if target is not None and target[0] == "property" and target in catalog:
            return target, "allowed_value_condition", {"condition": notation.render_subject(expression)}

    qualifiers = [(index, step.operand) for index, step in enumerate(expression.steps)
                  if step.operator == "/" and isinstance(step.operand, notation.Qualification)]
    if qualifiers and all(any(step.operator == ":" for step in qualifier.relative_path.steps) for _, qualifier in qualifiers):
        base = replace(expression, steps=tuple(step for step in expression.steps if not (
            step.operator == "/" and isinstance(step.operand, notation.Qualification))), value_format=None, value_cardinality=None)
        target = _target(base)
        properties = []
        for index, qualifier in qualifiers:
            relative = qualifier.relative_path
            marker = next((i for i, step in enumerate(relative.steps) if step.operator == ":"), None)
            anchor_steps = tuple(step for step in expression.steps[:index] if not (
                step.operator == "/" and isinstance(step.operand, notation.Qualification)))
            anchor = _target(replace(expression, steps=anchor_steps, value_format=None, value_cardinality=None))
            if marker is None or anchor is None or any(step.operator != ":" for step in relative.steps[marker:]):
                break
            path = replace(relative, steps=relative.steps[:marker], value_format=None, value_cardinality=None)
            properties.append(anchor[1] + "." + notation.render_subject(path))
        if target in catalog and len(properties) == len(qualifiers) and all(("property", prop) in catalog for prop in properties):
            return target, "property_qualification", {"properties": properties, "condition": notation.render_subject(expression)}
    if len(qualifiers) > 1 and [index for index, _ in qualifiers] == list(range(qualifiers[0][0], len(expression.steps))):
        base = replace(expression, steps=expression.steps[:qualifiers[0][0]], value_format=None, value_cardinality=None)
        target = _target(base)
        properties = []
        for _, qualifier in qualifiers:
            relative = qualifier.relative_path
            marker = next((i for i, step in enumerate(relative.steps) if step.operator == ":="), None)
            if marker is None or any(step.operator != ":=" for step in relative.steps[marker:]):
                break
            path = replace(relative, steps=relative.steps[:marker], value_format=None, value_cardinality=None)
            properties.append(target[1] + "." + notation.render_subject(path) if target else "")
        if (target in catalog and target[0] in {"primary_node", "instance", "component"}
                and len(properties) == len(qualifiers)
                and all(("property", property) in catalog for property in properties)):
            return target, "property_qualification", {"properties": properties, "condition": notation.render_subject(expression)}

    # A trailing grouped Property condition can qualify an already-declared
    # narrow Kind.  Its Property may be inherited from the root Kind, e.g.
    # Atom/(.Role:=Analysis)/(Form:=FPFReport) uses Atom.Form.
    for index in range(len(expression.steps) - 1, 0, -1):
        step = expression.steps[index]
        if step.operator != "/" or not isinstance(step.operand, (notation.Path, notation.Qualification)):
            continue
        condition = (step.operand.relative_path
                     if isinstance(step.operand, notation.Qualification) else step.operand)
        marker = next((position for position, item in enumerate(condition.steps) if item.operator == ":="), None)
        if marker is None or any(item.operator != ":=" for item in condition.steps[marker:]):
            continue
        base = replace(expression, steps=expression.steps[:index], value_format=None, value_cardinality=None)
        target = _target(base)
        if target is None or target not in catalog:
            continue
        root = replace(base, steps=(), value_format=None, value_cardinality=None)
        root_target = _target(root)
        property_path = replace(condition, steps=condition.steps[:marker], value_format=None, value_cardinality=None)
        if root_target is None:
            continue
        property_key = ("property", root_target[1] + "." + notation.render_subject(property_path))
        if property_key in catalog:
            return target, "inherited_property_qualification", {
                "property": property_key[1], "condition": notation.render_subject(condition),
            }
    qualifiers = [
        (index, step.operand) for index, step in enumerate(expression.steps)
        if step.operator == "/" and isinstance(step.operand, notation.Qualification)
    ]
    if len(qualifiers) != 1:
        return None
    index, qualifier = qualifiers[0]
    base = replace(expression, steps=expression.steps[:index], value_format=None, value_cardinality=None)
    target = _target(base)
    if target is None or target not in catalog or target[0] not in {"primary_node", "instance", "component"}:
        return None
    relative = qualifier.relative_path
    conditional = next((position for position, step in enumerate(relative.steps) if step.operator == ":="), None)
    if conditional is None or any(step.operator not in {":="} for step in relative.steps[conditional:]):
        return None
    property_path = replace(relative, steps=relative.steps[:conditional], value_format=None, value_cardinality=None)
    property_target = target[1] + "." + notation.render_subject(property_path)
    property_key = ("property", property_target)
    return ((target, "property_qualification", {
        "property": property_key[1], "condition": notation.render_subject(relative),
    }) if property_key in catalog else None)


def _root_name(expression: notation.Path | notation.RelationChain) -> str | None:
    expression = namespace_local_expression(expression) or expression
    path = expression if isinstance(expression, notation.Path) else expression.endpoints[0]
    return path.head.value if isinstance(path.head, notation.Name) else None


def _catalog_roots(catalog: Mapping[tuple[str, str], list[Record]]) -> set[str]:
    roots = {"Relation" for (kind, _) in catalog if kind == "relation"}
    for kind, identity in catalog:
        if kind == "relation":
            continue
        try:
            expression = notation.parse_subject_expression(identity, subject_profile="approved").expression
        except notation.SubjectNotationError:
            continue
        root = _root_name(expression)
        if root is not None:
            roots.add(root)
    return roots


def _declared_instance_kind(
    expression: notation.Path | notation.RelationChain | None,
) -> str | None:
    """Return the generic Kind of one exact Scope Unit Declaration Subject."""

    if expression is not None:
        expression = namespace_local_expression(expression) or expression
    if not isinstance(expression, notation.Path) or not isinstance(expression.head, notation.Name):
        return None
    if (expression.head.value not in _DECLARED_INSTANCE_KINDS or len(expression.steps) != 1
            or expression.value_format is not None or expression.value_cardinality is not None):
        return None
    step = expression.steps[0]
    if step.operator != "//" or not isinstance(step.operand, notation.Name):
        return None
    return expression.head.value


def _scope_unit_declaration_contexts(
    candidates: list[Candidate],
) -> dict[str, Record]:
    """Index unambiguous Current Scope Unit Declaration instance evidence."""

    contexts: dict[str, list[Record]] = defaultdict(list)
    for carrier, view, _, expression in candidates:
        if (view.get("content_role") != "Requirement"
                or view.get("type") != _SCOPE_UNIT_DECLARATION_FORM):
            continue
        kind = _declared_instance_kind(expression)
        if kind is not None:
            contexts[notation.render_subject(expression)].append({
                "kind": kind, "source": dict(carrier["source"]),
            })
    return {selector: records[0] for selector, records in contexts.items() if len(records) == 1}


def _declared_instance_binding(
    expression: notation.Path | notation.RelationChain,
    catalog: Mapping[tuple[str, str], list[Record]],
    contexts: Mapping[str, Record],
) -> tuple[tuple[str, str], str, Record] | None:
    context = contexts.get(notation.render_subject(expression))
    if context is None:
        return None
    target = ("primary_node", context["kind"])
    if target not in catalog:
        target = ("component", context["kind"])
    if target not in catalog:
        return None
    return target, "scope_unit_declaration_context", {
        "instance_selector": notation.render_subject(expression),
        "instance_kind": context["kind"],
        "existence_provenance": "current_scope_unit_declaration",
        "declaration_source": context["source"],
    }


def _raw_selector_binding(
    subject: str, catalog: Mapping[tuple[str, str], list[Record]],
) -> tuple[tuple[str, str], str, Record] | None:
    """Handle the few admitted non-Path selectors without expanding them."""

    compact = re.sub(r"\s+", "", _local_raw_selector(subject))
    base = _MODEL_APPLICABILITY_SELECTORS.get(compact)
    if base is not None:
        target = ("primary_node", base)
        if target in catalog:
            return target, "model_applicability_scope", {"applicability_scope": subject}
    kind = _KNOWN_NAMED_CONTRACT_CONTEXTS.get(compact)
    if kind is not None:
        target = ("primary_node", kind)
        if target not in catalog:
            target = ("component", kind)
        if target in catalog:
            return target, "known_instance_context", {
                "instance_selector": subject,
                "existence_provenance": "bounded_named_contract_context",
            }
    return None


def _lexical_term_binding(
    expression: notation.Path | notation.RelationChain,
    catalog: Mapping[tuple[str, str], list[Record]],
) -> tuple[tuple[str, str], str, Record] | None:
    """Keep a Term//Name as lexical evidence under Term, never as a Node."""

    expression = namespace_local_expression(expression) or expression
    if not isinstance(expression, notation.Path) or not isinstance(expression.head, notation.Name):
        return None
    if expression.head.value != "Term" or not any(step.operator == "//" for step in expression.steps):
        return None
    target = ("component", "Term")
    if target not in catalog:
        return None
    return target, "lexical_term_context", {"lexical_selector": notation.render_subject(expression)}


def _is_declaration(view: Mapping[str, Any]) -> bool:
    return view.get("content_role") == "Requirement" and view.get("type") in _DECLARATION_FORMS


def _metadata(entries: list[Record], relation: str) -> list[Record]:
    rows = []
    for entry in entries:
        for clause in entry["clauses"]:
            if clause.get("kind") == "relation_alias" and clause.get("relation") == relation:
                rows.append({"kind": "notation", "value": clause["glyph"], "source": clause["source"]})
        for block in entry["cfel_blocks"]:
            for match in _CLASSIFICATION.finditer(block["block"]):
                if match.group("name") == relation:
                    rows.append({"kind": "derivation", "value": match.group("value"), "source": block["source"]})
            for match in _METADATA.finditer(block["block"]):
                if match.group("name") == relation:
                    rows.append({
                        "kind": "notation" if match.group("notation") else "derivation",
                        "value": (match.group("short") or match.group("derivation")).strip(),
                        "source": block["source"],
                    })
    return rows


def _relation_parts(entries: list[Record], name: str) -> Record:
    host_target, inverses, derivation_links = [], [], []
    for entry in entries:
        for clause in entry["clauses"]:
            if clause.get("kind") != "relation_cardinality":
                continue
            relation = _token(clause.get("relation"))
            if relation == name:
                host_target.append(clause)
            source = _token(clause.get("source_selector"))
            target = _token(clause.get("target_selector"))
            if relation == "HAS_INVERSE" and source and target and name in {source, target}:
                inverses.append({"name": target if source == name else source, "source": clause["source"]})
            if relation == "IS_DERIVED_RELATION_OF" and source == name and target:
                derivation_links.append({"name": target, "source": clause["source"]})
    return {
        "host_target": host_target,
        "inverses": inverses,
        "derivation_links": derivation_links,
        "metadata": _metadata(entries, name),
    }


def _inverse_views(relations: list[Record]) -> None:
    """Expose only corroborated source-bound counterparts as derived views."""
    by_name = {row["target"]: row for row in relations if len(row["own"]) == 1}
    for derived in relations:
        if len(derived["own"]) != 1:
            continue
        own = derived["own"][0]
        reverse = [clause for clause in own["clauses"]
                   if clause.get("relation") == "HAS_INVERSE" and clause.get("written_direction") == "reverse"
                   and _token(clause.get("target_selector")) == derived["target"]]
        if len(reverse) != 1:
            continue
        direct_name = _token(reverse[0].get("source_selector"))
        direct = by_name.get(direct_name)
        if direct is None or direct is derived:
            continue
        direct_sources = {
            row["target"] for row in relations for entry in row["own"] for clause in entry["clauses"]
            if clause.get("relation") == "HAS_INVERSE" and clause.get("written_direction") == "forward"
            and _token(clause.get("source_selector")) == row["target"]
            and _token(clause.get("target_selector")) == derived["target"]
        }
        if direct_sources != {direct_name} or any(item["kind"] == "derivation" and item["value"] != "Derived"
                                                    for item in derived["metadata"]):
            continue
        direct_entry = direct["own"][0]
        matching = [clause for clause in direct_entry["clauses"]
                    if clause.get("relation") == "HAS_INVERSE" and clause.get("written_direction") == "forward"
                    and _token(clause.get("source_selector")) == direct_name
                    and _token(clause.get("target_selector")) == derived["target"]]
        classification = [item["value"] for item in direct["metadata"] if item["kind"] == "derivation"]
        meaning = direct_entry["semantics"] or (direct_entry["prose"] if direct_entry["prose_claim"] else "")
        if len(matching) != 1 or classification != ["Direct"] or not meaning.strip():
            continue
        derived["derived_view"] = {
            "classification": "Derived", "direct_relation": direct_name, "source": direct_entry["source"],
            "meaning": meaning,
            "endpoints": [{"host": clause.get("target_selector"), "target": clause.get("source_selector")}
                          for clause in direct["host_target"]],
        }


def _ancestor_rows(narrowing: Mapping[str, Any], declarations: Mapping[str, list[Record]]) -> dict[str, list[Record]]:
    """Return transitive declared ancestors with source refs; never copy claims."""

    nodes = {row["id"]: row for row in narrowing["nodes"]}
    immediate: dict[str, list[str]] = defaultdict(list)
    for edge in narrowing["edges"]:
        immediate[nodes[edge["relation_source"]]["identity"]].append(nodes[edge["relation_target"]]["identity"])

    def collect(target: str, seen: frozenset[str] = frozenset()) -> list[str]:
        result = []
        for parent in immediate.get(target, []):
            if parent not in seen:
                result.append(parent)
                result.extend(collect(parent, seen | {parent}))
        return list(dict.fromkeys(result))

    return {
        target: [
            {"target": parent, "declaration_refs": sorted(_source_ref(row["source"]) for row in declarations.get(parent, []))}
            for parent in collect(target)
        ]
        for target in set(immediate) | {row["identity"] for row in nodes.values()}
    }


def _property_parts(target: str) -> tuple[str, tuple[notation.PathStep, ...]] | None:
    try:
        expression = notation.parse_subject_expression(target, subject_profile="approved").expression
    except notation.SubjectNotationError:
        return None
    if not isinstance(expression, notation.Path):
        return None
    for index, step in enumerate(expression.steps):
        if step.operator == ".":
            bearer = replace(expression, steps=expression.steps[:index], value_format=None, value_cardinality=None)
            return notation.render_subject(bearer), expression.steps[index:]
    return None


def _inherited_property_rows(
    target: str, ancestors: Mapping[str, list[Record]], declarations: Mapping[str, list[Record]],
) -> list[Record]:
    parts = _property_parts(target)
    if parts is None:
        return []
    bearer, suffix = parts
    rows = []
    for ancestor in ancestors.get(bearer, []):
        try:
            parent = notation.parse_subject_expression(ancestor["target"], subject_profile="approved").expression
        except notation.SubjectNotationError:
            continue
        if not isinstance(parent, notation.Path):
            continue
        inherited = notation.render_subject(replace(parent, steps=parent.steps + suffix, value_format=None, value_cardinality=None))
        sources = declarations.get(inherited, [])
        if sources:
            rows.append({"target": inherited, "declaration_refs": sorted(_source_ref(row["source"]) for row in sources)})
    return rows


def _instance_kind(target: str) -> str | None:
    """Return the declared Kind path for one explicitly declared instance."""

    try:
        expression = notation.parse_subject_expression(target, subject_profile="approved").expression
    except notation.SubjectNotationError:
        return None
    if not isinstance(expression, notation.Path):
        return None
    for index, step in enumerate(expression.steps):
        if step.operator == "//":
            kind = replace(expression, steps=expression.steps[:index], value_format=None, value_cardinality=None)
            return notation.render_subject(kind)
    return None


def _ancestor_property_rows(
    target: str, ancestors: Mapping[str, list[Record]], declarations: Mapping[str, list[Record]],
) -> list[Record]:
    """Link Properties declared on ancestors without materializing child copies."""

    rows = []
    for ancestor in ancestors.get(target, []):
        for property_target, sources in declarations.items():
            parts = _property_parts(property_target)
            if parts is not None and parts[0] == ancestor["target"]:
                rows.append({
                    "target": property_target,
                    "declaration_refs": sorted(_source_ref(row["source"]) for row in sources),
                })
    return rows


def _tree_lines(narrowing: Mapping[str, Any]) -> list[str]:
    nodes = read_nodes(narrowing["nodes"])
    children, _, _, _ = read_edges(narrowing["edges"], nodes)
    lines, _, _ = primary_tree(nodes, children, set(nodes))
    return ["## Declared Narrowing Tree", "", "Each identity has its source-bound contract below.", "", "```text", *lines, "```", ""]


def compose_contract_graph(carriers: list[Record]) -> Record:
    """Group complete selected RMED evidence by a prior declared exact target."""

    catalog: dict[tuple[str, str], list[Record]] = defaultdict(list)
    declaration_carriers: list[Record] = []
    candidates: list[Candidate] = []
    gaps: list[Record] = []
    outside_scope: list[Record] = []
    for carrier in carriers:
        try:
            view, subject = _view(carrier), _active(carrier)
        except ValueError as error:
            gaps.append(_gap(carrier, f"Carrier aliases conflict: {error}"))
            continue
        if view.get("content_role") not in _RMED:
            continue
        if subject is None:
            gaps.append(_gap(carrier, "Expected exactly one active Subject."))
            continue
        try:
            expression = notation.parse_subject_expression(subject, subject_profile="approved").expression
        except notation.SubjectNotationError as error:
            if re.sub(r"\s+", "", _local_raw_selector(subject)) not in _MODEL_APPLICABILITY_SELECTORS:
                gaps.append(_gap(carrier, str(error), subject))
                continue
            expression = None
        candidates.append((carrier, view, subject, expression))
        if not _is_declaration(view):
            continue
        if expression is None:
            gaps.append(_gap(carrier, "Declaration active Subject is a selector, not one declared target.", subject))
            continue
        target = _target(expression)
        if target is None:
            gaps.append(_gap(carrier, "Declaration active Subject is not a declared Node, Property, Relation, or component.", subject))
            continue
        kind, identity = target
        catalog[(kind, identity)].append(_entry(carrier, subject, identity, kind))
        # compose_narrowing_graph has its own bounded admission filter. Pass
        # only Node/retained-component Declaration carriers so CFEL, Carrier
        # and Term Definitions remain roots in the full Subject tree. Relation
        # Definitions belong to the relation catalog, never to a tree.
        if view.get("type") in {"Declaration", "Entity Definition"}:
            declaration_carriers.append(carrier)

    roots = _catalog_roots(catalog)
    instance_contexts = _scope_unit_declaration_contexts(candidates)
    shared: dict[tuple[str, str], list[Record]] = defaultdict(list)
    for carrier, view, subject, expression in candidates:
        if _is_declaration(view):
            continue
        assert subject is not None
        context: Record = {}
        if expression is None:
            selected = _raw_selector_binding(subject, catalog)
            target, binding, context = selected if selected is not None else (None, None, {})
        else:
            target = _target(expression)
            binding = "exact" if target is not None and target in catalog else None
            if binding is None:
                selected = _raw_selector_binding(subject, catalog)
                if selected is not None:
                    target, binding, context = selected
            if binding is None:
                selected = _declared_instance_binding(expression, catalog, instance_contexts)
                if selected is not None:
                    target, binding, context = selected
            if binding is None:
                conditional = _conditional_target(expression, catalog)
                if conditional is not None:
                    target, binding, context = conditional
            if binding is None:
                lexical = _lexical_term_binding(expression, catalog)
                if lexical is not None:
                    target, binding, context = lexical
        if target is None or binding is None:
            entry = _gap(carrier, "Active Subject has no declared target in this selection.", subject)
            root = _root_name(expression) if expression is not None else "Node"
            if root is not None and root not in roots:
                entry["message"] = "Selected source is outside the declared model scope."
                entry["selection_disposition"] = "outside_model_scope"
                outside_scope.append(entry)
            else:
                gaps.append(entry)
            continue
        kind, identity = target
        entry = _entry(carrier, subject, identity, kind)
        entry["binding"] = binding
        entry["binding_context"] = context
        shared[(kind, identity)].append(entry)

    narrowing, _ = compose_narrowing_graph(declaration_carriers)
    primary_declarations = {identity: rows for (kind, identity), rows in catalog.items() if kind == "primary_node"}
    ancestors = _ancestor_rows(narrowing, primary_declarations)
    entities, components, relations, conflicts, instance_kind_gaps = [], [], [], [], []
    for (kind, identity), own in sorted(catalog.items()):
        attached = shared[(kind, identity)]
        if len(own) > 1:
            conflicts.append({"target": identity, "kind": kind, "sources": sorted(_source_ref(row["source"]) for row in own)})
        row = {"target": identity, "kind": kind, "own": own, "shared": attached,
               "shared_sources": sorted(_source_ref(item["source"]) for item in attached)}
        if kind == "primary_node":
            row["transitive_ancestors"] = ancestors.get(identity, [])
            row["inherited_property_declarations"] = _ancestor_property_rows(
                identity, ancestors,
                {target: rows for (target_kind, target), rows in catalog.items() if target_kind == "property"},
            )
            entities.append(row)
        elif kind == "property":
            row["inherited_property_declarations"] = _inherited_property_rows(identity, ancestors, primary_declarations)
            entities.append(row)
        elif kind == "instance":
            declared_kind = _instance_kind(identity)
            kind_entries = ([] if declared_kind is None else (
                catalog.get(("primary_node", declared_kind), [])
                or catalog.get(("component", declared_kind), [])
            ))
            kind_shared = ([] if declared_kind is None else (
                shared.get(("primary_node", declared_kind), [])
                or shared.get(("component", declared_kind), [])
            ))
            row["instance_of"] = {
                "target": declared_kind,
                "declaration_refs": sorted(_source_ref(entry["source"]) for entry in kind_entries),
                "effective_source_refs": sorted(_source_ref(entry["source"]) for entry in [*kind_entries, *kind_shared]),
            }
            if declared_kind is None or not kind_entries:
                instance_kind_gaps.append({"instance": identity, "kind": declared_kind})
            entities.append(row)
        elif kind == "component":
            components.append(row)
        else:
            relations.append({**row, **_relation_parts([*own, *attached], identity)})

    _inverse_views(relations)
    for relation in relations:
        if relation["derivation_links"] and not relation.get("derived_view"):
            relation["derivation_scope"] = "Derivation qualification and endpoint transformation are not structurally interpreted."
    missing_relation_semantics = [
        {"relation": row["target"], "source": entry["source"]}
        for row in relations for entry in row["own"]
        if not (entry["semantics"].strip() or (entry["prose_claim"] and entry["prose"].strip()) or row.get("derived_view"))
    ]
    entries = [item for rows in catalog.values() for item in rows] + [item for rows in shared.values() for item in rows] + gaps + outside_scope
    diagnostics = [item for entry in entries for item in entry["diagnostics"]]
    inheritance_diagnostics = narrowing["diagnostics"]
    coverage = {
        "candidate_sources": len(entries), "bound_sources": len(entries) - len(gaps) - len(outside_scope),
        "declared_entity_targets": len(entities), "declared_component_targets": len(components),
        "declared_relation_targets": len(relations), "shared_sources": sum(len(rows) for rows in shared.values()),
        "fenced_claim_blocks": sum(len(entry["blocks"]) for entry in entries),
        "cfel_blocks": sum(len(entry["cfel_blocks"]) for entry in entries),
        "recognized_clauses": sum(len(entry["clauses"]) for entry in entries),
        "unsupported_clauses": len(diagnostics), "coverage_gaps": len(gaps),
        "outside_model_scope_sources": len(outside_scope),
        "duplicate_declarations": len(conflicts), "missing_relation_semantics": len(missing_relation_semantics),
        "instance_kind_gaps": len(instance_kind_gaps),
        "inheritance_diagnostics": len(inheritance_diagnostics),
    }
    display_incomplete = any((gaps, conflicts, missing_relation_semantics, instance_kind_gaps, inheritance_diagnostics))
    return {
        "kind": "source_bound_formal_contract_graph", "narrowing_tree": narrowing,
        "entities": entities, "components": components, "relations": relations,
        "coverage_gaps": gaps, "outside_model_scope": outside_scope, "unresolved": gaps, "conflicts": conflicts,
        "missing_relation_semantics": missing_relation_semantics, "instance_kind_gaps": instance_kind_gaps,
        "diagnostics": diagnostics, "inheritance_diagnostics": inheritance_diagnostics,
        "coverage": coverage,
        "display_coverage": "incomplete" if display_incomplete else "complete",
        "structured_cfel": "partial" if diagnostics else "complete",
        "outcome": "incomplete" if display_incomplete else "complete",
    }


def _count(value: object) -> str:
    if not isinstance(value, Mapping):
        return "undefined"
    lower, upper = value.get("minimum"), value.get("maximum")
    return f"{lower}+" if upper is None else str(lower) if lower == upper else f"{lower}..{upper}"


def _clause(row: Mapping[str, Any]) -> str:
    if row.get("kind") == "relation_cardinality":
        relation = row.get("relation") or row.get("relation_notation") or "relation"
        written = row.get("written_direction", "forward")
        return f"`{row.get('source_selector')}` — {relation} → `{row.get('target_selector')}`; Host={_count(row.get('source_cardinality'))}; Target={_count(row.get('target_cardinality'))}; written direction={written}"
    if row.get("kind") == "property_constraint":
        return f"`{row.get('property_selector')}` {row.get('selection')}; names={row.get('name_format')}; names count={_count(row.get('occurrence_cardinality'))}; values={row.get('value_format')}; values count={_count(row.get('value_cardinality'))}"
    if row.get("kind") == "allowed_literal":
        return f"`{row.get('property_selector')}: {row.get('literal')}`"
    if row.get("kind") == "classification_condition":
        return f"`{row.get('subject_selector')} >| {row.get('axis')} {row.get('operator')} {row.get('value')}`"
    return f"`{row.get('expression')}`"


def _fence(block: Mapping[str, Any]) -> list[str]:
    content = str(block["block"]).rstrip()
    marker = "`" * max([3] + [len(value) + 1 for value in re.findall(r"`+", content)])
    label = str(block.get("label", ""))
    status = "" if block.get("closed", True) else " (unclosed in source)"
    return [marker + label, content, marker + status]


def _render_entry(lines: list[str], entry: Record, label: str) -> None:
    lines.append(f"- {label}: `{_source_ref(entry['source'])}`")
    if entry["claim_scope"]:
        lines.extend(["  - Claim Scope:", *["    " + row if row else "" for row in entry["claim_scope"].splitlines()]])
    if entry["prose"]:
        lines.extend(["  - Remaining Claim prose:", *["    " + row if row else "" for row in entry["prose"].splitlines()]])
    for block in entry["blocks"]:
        lines.extend(["  - Fenced Claim block:", *_fence(block)])
    groups: dict[str, list[str]] = {"Value contracts": [], "Nested Property contracts": [], "Allowed values": [], "Allowed Relations and other formal clauses": []}
    for clause in entry["clauses"]:
        title = ("Value contracts" if clause.get("kind") == "property_constraint" and clause.get("selection") == "values"
                 else "Nested Property contracts" if clause.get("kind") == "property_constraint"
                 else "Allowed values" if clause.get("kind") == "allowed_literal"
                 else "Allowed Relations and other formal clauses")
        groups[title].append(_clause(clause))
    for title, values in groups.items():
        if values:
            lines.extend([f"  - {title}:", *["    - " + value for value in values]])
    for diagnostic in entry["diagnostics"]:
        lines.append(f"  - Unresolved CFEL: `{diagnostic.get('expression', diagnostic.get('message'))}`")
    if entry["semantics"]:
        lines.extend(["  - Semantics:", *["    " + row if row else "" for row in entry["semantics"].splitlines()]])
    if entry["details"]:
        lines.extend(["  - Details (source-bound):", *["    " + row if row else "" for row in entry["details"].splitlines()]])


def _render_contract_rows(lines: list[str], row: Record) -> None:
    for own in row["own"]:
        _render_entry(lines, own, "Declaration source")
    for shared in row["shared"]:
        binding = shared.get("binding", "exact")
        _render_entry(lines, shared, f"Shared RMED source ({binding} binding)")
        if shared.get("binding_context"):
            lines.extend(["  - Binding context:", *[
                f"    - {key.replace('_', ' ')}: `{value}`"
                for key, value in shared["binding_context"].items()
            ]])


def render_contract_graph(graph: Mapping[str, Any]) -> str:
    """Render complete source-bound Claims and bounded structured contract views."""

    lines = ["# Formal Contract Graph", "", "Bounded extraction only. CFEL blocks remain authoritative source text; this view does not execute CFEL.", "", "## Coverage", ""]
    lines.extend(f"- {key.replace('_', ' ')}: {value}" for key, value in graph["coverage"].items())
    lines.extend([f"- display coverage: {graph['display_coverage']}", f"- structured CFEL extraction: {graph['structured_cfel']}"])
    lines.extend([""] + _tree_lines(graph["narrowing_tree"]))
    lines.extend(["## Entity and Property Contracts", ""])
    for entity in graph["entities"]:
        lines.extend([f"### `{entity['target']}` — {entity['kind']}", ""])
        if entity["kind"] == "primary_node" and entity["transitive_ancestors"]:
            lines.append("- Transitive ancestor Declarations; their contracts are not copied:")
            lines.extend(f"  - `{row['target']}` — {', '.join(row['declaration_refs']) or 'no direct declaration source in selection'}" for row in entity["transitive_ancestors"])
        if entity["kind"] == "instance":
            instance_of = entity["instance_of"]
            lines.append(
                "- INSTANCE_OF declared Kind effective contracts; no instance contract is copied: "
                f"`{instance_of['target'] or 'unresolved'}` — "
                f"{', '.join(instance_of['effective_source_refs']) or 'no declared Kind source in selection'}"
            )
        if entity.get("inherited_property_declarations"):
            lines.append("- Inherited Property Declaration refs; no child Property Node is created:")
            lines.extend(f"  - `{row['target']}` — {', '.join(row['declaration_refs'])}" for row in entity["inherited_property_declarations"])
        _render_contract_rows(lines, entity)
        lines.append("")
    lines.extend(["## CFEL, Carrier, and Term Component Contracts", ""])
    for component in graph["components"]:
        lines.extend([f"### `{component['target']}` — declared component", ""])
        _render_contract_rows(lines, component)
        lines.append("")
    lines.extend(["## Relation Contracts", ""])
    for relation in graph["relations"]:
        lines.extend([f"### `(({relation['target']}))` — declared Relation", ""])
        _render_contract_rows(lines, relation)
        if relation["host_target"]:
            lines.extend(["- Host / Target contracts:", *["  - " + _clause(row) for row in relation["host_target"]]])
        if relation["metadata"]:
            lines.extend(["- Standalone metadata:", *[f"  - {row['kind']}: `{row['value']}` — {_source_ref(row['source'])}" for row in relation["metadata"]]])
        if relation.get("derived_view"):
            derived = relation["derived_view"]
            lines.append(f"- Derived view of `{derived['direct_relation']}` — {_source_ref(derived['source'])}; endpoints are a reversed source view, not new permissions.")
            lines.extend(f"  - `{endpoint['host']}` → `{endpoint['target']}`" for endpoint in derived["endpoints"])
            lines.extend(["  - Source meaning:", *["    " + line if line else "" for line in derived["meaning"].splitlines()]])
        if relation.get("derivation_scope"):
            lines.append(f"- Derivation interpretation gap: {relation['derivation_scope']}")
        if relation["inverses"]:
            lines.extend(["- HAS_INVERSE bindings; this does not certify an undeclared inverse Relation:", *[f"  - `(({row['name']}))` — {_source_ref(row['source'])}" for row in relation["inverses"]]])
        if relation["derivation_links"]:
            lines.extend(["- IS_DERIVED_RELATION_OF bindings:", *[f"  - `(({row['name']}))` — {_source_ref(row['source'])}" for row in relation["derivation_links"]]])
        lines.append("")
    lines.extend(["## Coverage Gaps and Conflicts", ""])
    for row in graph["coverage_gaps"]:
        lines.append(f"- `{_source_ref(row['source'])}`: {row['message']}")
        _render_entry(lines, row, "Unbound source evidence")
    for row in graph["outside_model_scope"]:
        lines.append(f"- `{_source_ref(row['source'])}`: {row['message']}")
        _render_entry(lines, row, "Selected evidence outside model scope")
    for row in graph["conflicts"]:
        lines.append(f"- Duplicate {row['kind']} Declaration `{row['target']}`: {', '.join(row['sources'])}")
    for row in graph["missing_relation_semantics"]:
        lines.append(f"- Relation `(({row['relation']}))` lacks Semantics: `{_source_ref(row['source'])}`")
    for row in graph["instance_kind_gaps"]:
        lines.append(f"- Instance `{row['instance']}` has no declared Kind target: `{row['kind'] or 'unresolved'}`")
    for row in graph["diagnostics"]:
        lines.append(f"- `{_source_ref(row['source'])}`: {row.get('expression', row.get('message'))}")
    for message in graph["inheritance_diagnostics"]:
        lines.append(f"- Narrowing evidence: {message}")
    if not (graph["coverage_gaps"] or graph["conflicts"] or graph["missing_relation_semantics"] or graph["instance_kind_gaps"] or graph["diagnostics"] or graph["inheritance_diagnostics"]):
        lines.append("- None.")
    return "\n".join(lines) + "\n"
