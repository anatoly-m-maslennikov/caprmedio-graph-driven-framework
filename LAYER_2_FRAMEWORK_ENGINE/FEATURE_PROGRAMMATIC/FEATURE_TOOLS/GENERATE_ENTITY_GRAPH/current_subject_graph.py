"""Compose a syntax graph from supplied current Atom Subjects, without history."""

import hashlib
import json
import re
from typing import Any

from dataclasses import replace

import subject_notation as notation
from carrier_aliases import carrier_read_view, matches_named_value

def namespace_local_expression(expression: notation.Path | notation.RelationChain | None) -> notation.Path | notation.RelationChain | None:
    local = notation.namespace_local_expression(expression) if expression is not None else None
    if local is not None:
        expression = local
    if isinstance(expression, notation.Path) and isinstance(expression.head, (notation.Path, notation.RelationChain)):
        head = namespace_local_expression(expression.head) or expression.head
        if isinstance(head, notation.Path) and head.value_format is None and head.value_cardinality is None:
            return replace(expression, head=head.head, steps=(*head.steps, *expression.steps))
    return local

Record = dict[str, Any]
_KINDS = {
    "//": "INSTANCE_OF",
    "/": "NARROWER_THAN",
    ".": "IS_PROPERTY_OF",
    ":": "IS_ALLOWED_VALUE_OF",
    ":=": "IS_ALLOWED_VALUE_OF",
}
_NAMESPACE_ROOTS = {"CAPRMEDIO_MODEL", "CAPRMEDIO_STRUCTURE"}


def _has_selection(node: object) -> bool:
    if isinstance(node, (notation.SelectionGroup, notation.SelectionSuffix)):
        return True
    if isinstance(node, notation.RelationChain):
        return any(_has_selection(endpoint) for endpoint in node.endpoints)
    if isinstance(node, notation.Path):
        return _has_selection(node.head) or any(_has_selection(step.operand) for step in node.steps)
    if isinstance(node, notation.Qualification):
        return _has_selection(node.relative_path)
    if isinstance(node, notation.DeclaredReference):
        return _has_selection(node.entity)
    return False


def _identifier(prefix: str, value: object) -> str:
    raw = json.dumps(value, ensure_ascii=False, separators=(",", ":")).encode("utf-8")
    return prefix + hashlib.sha256(raw).hexdigest()


def _cardinality(value: notation.Cardinality | None) -> Record | None:
    if value is None:
        return None
    return {"minimum": value.minimum, "maximum": value.maximum}


class _SubjectFacts:
    def __init__(self) -> None:
        self.nodes: dict[str, Record] = {}
        self.facts: list[Record] = []

    def node(self, identity: str, **metadata: Any) -> str:
        self.nodes.setdefault(identity, {"identity": identity}).update(metadata)
        return identity

    def fact(self, kind: str, source: str, target: str, **metadata: Any) -> None:
        self.facts.append({"kind": kind, "source": source, "target": target, **metadata})

    def reference(self, value: notation.DeclaredReference) -> str:
        identity = (value.entity.value if isinstance(value.entity, notation.Name)
                    else notation.render_subject(value.entity))
        return self.node(identity, declared_reference=True)

    def head(self, head: object) -> str:
        if isinstance(head, notation.Name):
            return self.node(head.value)
        if isinstance(head, notation.DeclaredReference):
            return self.reference(head)
        if isinstance(head, notation.Path):
            return self.path(head)
        if isinstance(head, notation.InitialAtomSelector):
            return self.node(head.literal, unresolved_selector=True)
        raise ValueError("A relation used as a path head has no supported Entity projection")

    def qualification(self, value: notation.Path, index: int,
                      relative: notation.Path, identity: str) -> str:
        if not isinstance(relative.head, notation.Name):
            raise ValueError("Qualification requires a relative Property name")
        base = replace(value, steps=value.steps[:index], value_format=None, value_cardinality=None)
        property_path = replace(
            base, steps=(*base.steps, notation.PathStep(".", relative.head, relative.head.span),
                         *relative.steps),
            value_format=relative.value_format, value_cardinality=relative.value_cardinality,
        )
        return self.node(identity, qualification=self.path(property_path))

    def operand(self, value: notation.Path, index: int, step: notation.PathStep) -> str:
        prefix = replace(value, steps=value.steps[:index + 1], value_format=None,
                         value_cardinality=None)
        identity = notation.render_subject(prefix)
        operand = step.operand
        if isinstance(operand, notation.Qualification):
            return self.qualification(value, index, operand.relative_path, identity)
        if isinstance(operand, notation.DeclaredReference):
            return self.reference(operand)
        if isinstance(operand, (notation.Name, notation.ValueLiteral)):
            return self.node(
                identity,
                **({"value": operand.value} if step.operator in {":", ":="} else {}),
            )
        if isinstance(operand, notation.Path):
            return self.path(operand)
        raise ValueError("Unsupported Subject path operand")

    def path(self, value: notation.Path) -> str:
        if isinstance(value.head, notation.RelationChain):
            local = namespace_local_expression(value.head)
            if isinstance(local, notation.Path):
                value = replace(value, head=local)
        while (isinstance(value.head, notation.Path) and value.head.value_format is None
               and value.head.value_cardinality is None):
            value = replace(value, head=value.head.head, steps=(*value.head.steps, *value.steps))
        current = self.head(value.head)
        for index, step in enumerate(value.steps):
            child = self.operand(value, index, step)
            if step.operator not in _KINDS:
                raise ValueError("Unsupported Subject path operator")
            self.fact(_KINDS[step.operator], child, current)
            current = child
        if value.value_format is not None:
            self.nodes[current]["value_format"] = value.value_format.value
        if value.value_cardinality is not None:
            self.nodes[current]["value_cardinality"] = _cardinality(value.value_cardinality)
        return current

    def relation(self, left: str, right: str, link: notation.RelationLink) -> None:
        reverse = link.operator in {"<+", "|<", "<(("}
        if link.operator in {"+>", "<+"}:
            kind = "IS_CONTAINED_BY"
        elif link.operator in {">|", "|<"}:
            kind = "HAS_CLASSIFICATION"
        elif link.operator == "<-->":
            kind = "HAS_INVERSE"
        elif link.relation_type is not None:
            kind = link.relation_type.value
        else:
            raise ValueError("Unsupported Subject relation operator")
        source, destination = (right, left) if reverse else (left, right)
        forward, backward = link.forward_cardinality, link.reverse_cardinality
        if reverse:
            forward, backward = backward, forward
        self.fact(kind, source, destination, forward_cardinality=_cardinality(forward),
                  reverse_cardinality=_cardinality(backward))


def subject_facts(subject: str) -> tuple[list[Record], list[Record], str]:
    """Project typed syntax to direct facts; never infer identities from role order."""
    expression = notation.parse_subject_expression(subject, subject_profile="approved").expression
    if _has_selection(expression):
        raise ValueError("Complex Subject selection cannot be projected as individual entities")
    projection = _SubjectFacts()
    if isinstance(expression, notation.Path):
        target = projection.path(expression)
    else:
        endpoints = [projection.path(endpoint) for endpoint in expression.endpoints]
        for left, right, link in zip(endpoints, endpoints[1:], expression.links):
            projection.relation(left, right, link)
        target = notation.render_subject(expression)
    return list(projection.nodes.values()), projection.facts, target


def path_steps(subject: str) -> list[tuple[str, str | None, str | None]]:
    """Compatibility view of path nodes; relation chains require subject_facts."""
    parsed = notation.parse_subject_expression(subject, subject_profile="approved")
    if not isinstance(parsed.expression, notation.Path):
        raise ValueError("Relation chains have direct facts rather than a single path")
    nodes, facts, _ = subject_facts(subject)
    by_child = {row["source"]: row for row in facts}
    return [(row["identity"], by_child[row["identity"]]["target"],
             by_child[row["identity"]]["kind"]) if row["identity"] in by_child
            else (row["identity"], None, None) for row in nodes]


def _occurrences(carrier: Record, diagnostics: list[str]) -> list[Record]:
    source, subjects = carrier["source"], carrier["subjects"]
    if not isinstance(subjects, dict):
        diagnostics.append(f"{source['path']}: Subjects mapping is unavailable.")
        return []
    try:
        subjects = carrier_read_view({"subjects": subjects})["subjects"]
    except ValueError as error:
        raise ValueError(f"{source['path']}: {error}") from error
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
        supplied_nodes, facts, target = subject_facts(subject)
    except (notation.SubjectNotationError, ValueError) as error:
        raise ValueError(f"{origin}: Subject projection failed: {error}") from error
    for supplied in supplied_nodes:
        identity = supplied["identity"]
        child_id = _identifier("subject:", identity)
        node = nodes.setdefault(child_id, {
            **supplied, "id": child_id, "occurrence_ids": set(), "is_full_target": False,
        })
        for key, value in supplied.items():
            if key in node and node[key] != value:
                raise ValueError(f"{origin}: conflicting Subject projection metadata for {identity}: {key}")
            node[key] = value
        node["occurrence_ids"].add(origin)
        node["is_full_target"] |= identity == target
    for supplied in facts:
        source_id = _identifier("subject:", supplied["source"])
        target_id = _identifier("subject:", supplied["target"])
        metadata = {key: value for key, value in supplied.items() if key not in {"source", "target"}}
        edge_id = _identifier("subject-edge:", [metadata, source_id, target_id])
        edge = edges.setdefault(edge_id, {
            **metadata, "id": edge_id, "relation_source": source_id,
            "relation_target": target_id, "occurrence_ids": set(),
        })
        edge["occurrence_ids"].add(origin)


def compose_current_graph(
    carriers: list[Record], *, unsupported_as_diagnostics: bool = False,
) -> tuple[Record, Record]:
    """Use only the passed current sources; Subject roles add no cross-path edges."""
    nodes: dict[str, Record] = {}
    edges: dict[str, Record] = {}
    diagnostics: list[str] = []
    occurrences = [row for carrier in carriers for row in _occurrences(carrier, diagnostics)]
    for occurrence in occurrences:
        try:
            _add_path(occurrence, nodes, edges, diagnostics)
        except ValueError as error:
            if not unsupported_as_diagnostics:
                raise
            diagnostics.append(str(error))
    for row in [*nodes.values(), *edges.values()]:
        row["occurrence_ids"] = sorted(row["occurrence_ids"])
    graph = {
        "kind": "current_atom_subjects",
        "source_basis": "current_atom_carriers",
        "native_admission": "not_performed",
        "nodes": sorted(nodes.values(), key=lambda row: (row["identity"], row["id"])),
        "edges": sorted(edges.values(), key=lambda row: row["id"]),
        "diagnostics": sorted(diagnostics),
    }
    provenance = {
        "owners": [{"source": carrier["source"]} for carrier in carriers],
        "occurrences": occurrences,
    }
    return graph, provenance


def _view(carrier: Record) -> Record:
    value = carrier.get("read_view")
    if isinstance(value, dict):
        return value
    metadata = carrier.get("metadata")
    if not isinstance(metadata, dict):
        return {}
    from carrier_aliases import carrier_read_view
    return carrier_read_view(metadata)


def _is_declaration(carrier: Record) -> bool:
    view = _view(carrier)
    return matches_named_value(view.get("content_role"), "Requirement") and matches_named_value(view.get("type"), "Declaration")


def _is_relation_definition(carrier: Record) -> bool:
    view = _view(carrier)
    return matches_named_value(view.get("content_role"), "Requirement") and any(
        matches_named_value(view.get("type"), form) for form in ("Relation Definition", "Relation Declaration")
    )


def _target_kind(expression: notation.Path | notation.RelationChain) -> str | None:
    """Classify one declared Path; qualifiers remain part of that declaration."""

    expression = namespace_local_expression(expression) or expression
    if _has_selection(expression):
        return None
    if not isinstance(expression, notation.Path) or not isinstance(expression.head, notation.Name):
        return None
    if expression.head.value in _NAMESPACE_ROOTS and not expression.steps:
        return None
    if any(
        step.operator in {":", ":="} or isinstance(step.operand, notation.DeclaredReference)
        for step in expression.steps
    ):
        return None
    operators = {step.operator for step in expression.steps}
    root = expression.head.value
    if root == "Relation" and "//" in operators and "." not in operators:
        return "relation"
    if "//" in operators and "." not in operators:
        return "instance"
    if "." in operators and "//" not in operators:
        return "property"
    if not operators or operators == {"/"}:
        return "primary_node"
    return None


def compose_narrowing_graph(carriers: list[Record]) -> tuple[Record, Record]:
    """Compose a declared-only NARROWER_THAN tree from Current carriers."""

    from cfel_claim_constraints import extract_claim_constraints
    nodes: dict[str, Record] = {}
    edges: dict[str, Record] = {}
    diagnostics: list[str] = []
    pending: list[tuple[str, str, str, bool]] = []
    owners: list[Record] = []

    def source_name(carrier: Record) -> str:
        source = carrier["source"]
        return f"{source['atom_id']}@{source['version']}"

    def claim_constraints(carrier: Record) -> list[Record]:
        constraints, claim_diagnostics = extract_claim_constraints(carrier)
        for diagnostic in claim_diagnostics:
            if diagnostic["code"] == "python-formal-claim-invalid":
                raise ValueError(f"{source_name(carrier)}: {diagnostic['message']}")
        return constraints

    def active(carrier: Record) -> str | None:
        subjects = carrier.get("subjects")
        if not isinstance(subjects, dict):
            diagnostics.append(f"{source_name(carrier)}: active Subject is unavailable.")
            return None
        try:
            value = carrier_read_view({"subjects": subjects})["subjects"].get("governs")
        except ValueError as error:
            diagnostics.append(f"{source_name(carrier)}: {error}")
            return None
        values = value if isinstance(value, list) else [value]
        if len(values) != 1 or not isinstance(values[0], str) or not values[0].strip():
            diagnostics.append(f"{source_name(carrier)}: exactly one active Subject is required.")
            return None
        return values[0]

    def label(expression: notation.Path, canonical: str) -> str:
        if not expression.steps:
            return canonical
        operand = expression.steps[-1].operand
        if isinstance(operand, notation.Name):
            return operand.value
        if isinstance(operand, notation.Qualification):
            return "(." + notation.render_subject(operand.relative_path) + ")"
        return canonical

    def add_node(identity: str, display_name: str, carrier: Record) -> None:
        key = _identifier("narrowing:", identity)
        node = nodes.setdefault(key, {
            "id": key, "identity": identity, "display_name": display_name, "source_bindings": set(),
        })
        node["source_bindings"].add(source_name(carrier))

    def add_cfel_component_endpoint(carrier: Record, expression: notation.RelationChain) -> bool:
        """Admit the explicitly declared CFEL component, never its composition edge."""

        if len(expression.endpoints) != 2 or len(expression.links) != 1:
            return False
        left, right = expression.endpoints
        link = expression.links[0]
        if (
            link.operator != "<+" or link.relation_type is not None
            or not isinstance(left.head, notation.Name) or left.head.value != "CFEL"
        ):
            return False
        kind = _target_kind(right)
        if kind in {"property", "instance", "relation"}:
            # These are explicit component contracts, not Primary Nodes. The
            # contract catalog retains them; the narrowing tree has nothing to
            # render and must not manufacture a composition edge or diagnostic.
            return True
        if kind != "primary_node":
            return False
        try:
            _, facts, target = subject_facts(notation.render_subject(right))
        except (notation.SubjectNotationError, ValueError) as error:
            diagnostics.append(f"{source_name(carrier)}: CFEL component endpoint is unsupported: {error}.")
            return False
        add_node(target, label(right, target), carrier)
        for fact in facts:
            if fact["kind"] == "NARROWER_THAN":
                pending.append((fact["source"], fact["target"], source_name(carrier), False))
        return True

    def add_path(carrier: Record, subject: str, *, retained_relation_root: bool = False,
                 native_class: bool = False) -> bool:
        try:
            expression = notation.parse_subject_expression(subject, subject_profile="approved").expression
        except notation.SubjectNotationError as error:
            diagnostics.append(f"{source_name(carrier)}: unsupported Subject `{subject}`: {error}.")
            return False
        local_expression = namespace_local_expression(expression)
        if local_expression is not None:
            expression = local_expression
            subject = notation.render_subject(expression)
        if not isinstance(expression, notation.Path):
            first = expression.endpoints[0].head
            if (not retained_relation_root or not isinstance(first, notation.Name)
                    or first.value not in {"CFEL", "Carrier", "Term"}):
                diagnostics.append(f"{source_name(carrier)}: relation Subject `{subject}` is outside retained roots.")
                return False
            try:
                supplied, facts, _ = subject_facts(subject)
            except (notation.SubjectNotationError, ValueError) as error:
                diagnostics.append(f"{source_name(carrier)}: unsupported relation Subject `{subject}`: {error}.")
                return False
            references = {row["identity"] for row in supplied if row.get("declared_reference")}
            for fact in facts:
                if fact["kind"] == "NARROWER_THAN":
                    pending.append((fact["source"], fact["target"], source_name(carrier), fact["target"] in references))
            return True
        if isinstance(expression.head, notation.Name) and expression.head.value in _NAMESPACE_ROOTS and not expression.steps:
            return True
        if _target_kind(expression) in {"property", "instance"}:
            return True
        if _target_kind(expression) != "primary_node":
            diagnostics.append(f"{source_name(carrier)}: Subject `{subject}` does not declare one Primary Node.")
            return False
        try:
            _, facts, target = subject_facts(subject)
        except (notation.SubjectNotationError, ValueError) as error:
            diagnostics.append(f"{source_name(carrier)}: Subject facts unavailable: {error}.")
            return False
        add_node(target, label(expression, target), carrier)
        for fact in (() if native_class else facts):
            if fact["kind"] == "NARROWER_THAN":
                pending.append((fact["source"], fact["target"], source_name(carrier), False))
        return True

    declaration_targets: list[tuple[Record, str]] = []
    native_classes: list[tuple[Record, str, Record]] = []
    for carrier in carriers:
        view = _view(carrier)
        if not matches_named_value(view.get("content_role"), "Requirement"):
            continue
        form = view.get("type")
        if not any(matches_named_value(form, name) for name in {"Declaration", "Entity Definition"}):
            continue
        subject = active(carrier)
        if subject is None:
            continue
        if matches_named_value(form, "Declaration"):
            constraints = claim_constraints(carrier)
            native = [row for row in constraints if row.get("kind") == "native_class"]
            if len(native) > 1:
                diagnostics.append(f"{source_name(carrier)}: multiple native class declarations.")
                continue
            try:
                expression = notation.parse_subject_expression(subject, subject_profile="approved").expression
            except notation.SubjectNotationError:
                expression = None
            expression = namespace_local_expression(expression) or expression
            if isinstance(expression, notation.RelationChain) and add_cfel_component_endpoint(carrier, expression):
                owners.append(carrier)
                continue
            if add_path(carrier, subject, native_class=bool(native)):
                owners.append(carrier)
                try:
                    expression = notation.parse_subject_expression(subject, subject_profile="approved").expression
                    expression = namespace_local_expression(expression) or expression
                    if isinstance(expression, notation.Path) and _target_kind(expression) == "primary_node":
                        target = notation.render_subject(expression)
                        if native:
                            native_classes.append((carrier, target, native[0]))
                        else:
                            declaration_targets.append((carrier, target))
                except notation.SubjectNotationError:
                    pass
            continue
        if not matches_named_value(form, "Entity Definition"):
            continue
        try:
            expression = notation.parse_subject_expression(subject, subject_profile="approved").expression
        except notation.SubjectNotationError as error:
            diagnostics.append(f"{source_name(carrier)}: retained Entity Definition `{subject}` is unsupported: {error}.")
            continue
        expression = namespace_local_expression(expression) or expression
        if isinstance(expression, notation.RelationChain):
            if add_cfel_component_endpoint(carrier, expression):
                owners.append(carrier)
                continue
            if add_path(carrier, subject, retained_relation_root=True):
                owners.append(carrier)
            continue
        if not isinstance(expression.head, notation.Name) or expression.head.value not in {"CFEL", "Carrier", "Term"}:
            diagnostics.append(f"{source_name(carrier)}: Entity Definition `{subject}` is outside retained CFEL, Carrier, Term roots.")
            continue
        if add_path(carrier, subject):
            owners.append(carrier)

    def terminal_name(identity: str) -> str | None:
        try:
            parsed = notation.parse_subject_expression(identity, subject_profile="approved").expression
        except notation.SubjectNotationError:
            return None
        if not isinstance(parsed, notation.Path) or not isinstance(parsed.head, notation.Name):
            return None
        if not parsed.steps:
            return parsed.head.value
        operand = parsed.steps[-1].operand
        return operand.value if isinstance(operand, notation.Name) else None

    for carrier, target in declaration_targets:
        constraints = claim_constraints(carrier)
        for constraint in constraints:
            expression = constraint.get("expression")
            if (constraint.get("group") == "instances" or constraint.get("kind") != "relation_cardinality" or constraint.get("relation") != "NARROWER_THAN"
                    or not isinstance(expression, str)):
                continue
            selector = str(constraint.get("target_selector") or "").strip()
            if not selector.startswith("@"):
                try:
                    parsed_target = notation.parse_subject_expression(selector, subject_profile="approved").expression
                except notation.SubjectNotationError:
                    continue
                if not isinstance(parsed_target, notation.Path) or not isinstance(parsed_target.head, notation.Name) or parsed_target.steps:
                    continue
            if constraint.get("source_cardinality") is not None or constraint.get("target_cardinality") is not None:
                continue
            try:
                _, facts, _ = subject_facts(expression)
            except (notation.SubjectNotationError, ValueError) as error:
                diagnostics.append(f"{source_name(carrier)}: NARROWER_THAN Claim is unsupported: {error}.")
                continue
            source_names = {target, terminal_name(target)}
            direct = [fact for fact in facts if fact["kind"] == "NARROWER_THAN" and fact["source"] in source_names]
            if len(direct) != 1:
                diagnostics.append(f"{source_name(carrier)}: NARROWER_THAN Claim does not bind active Subject `{target}`.")
                continue
            pending.append((target, direct[0]["target"], source_name(carrier), True))

    by_identity = {node["identity"]: node for node in nodes.values()}
    def python_name(value: str) -> str:
        return re.sub(r"[^a-z0-9]", "", value.casefold())

    def subject_name(identity: str) -> str:
        try:
            path = notation.parse_subject_expression(identity, subject_profile="approved").expression
            if isinstance(path, notation.Path) and path.steps:
                operand = path.steps[-1].operand
                if isinstance(operand, notation.Qualification) and operand.relative_path.steps:
                    value = operand.relative_path.steps[-1].operand
                    if isinstance(value, notation.ValueLiteral):
                        return value.value
        except notation.SubjectNotationError:
            pass
        return terminal_name(identity) or identity

    symbols: dict[str, list[str]] = {}
    for identity in by_identity:
        symbols.setdefault(python_name(subject_name(identity)), []).append(identity)
    class_symbols: dict[str, list[str]] = {}
    for _, target, declaration in native_classes:
        class_symbols.setdefault(declaration["class_name"], []).append(target)
    for carrier, target, declaration in native_classes:
        if python_name(declaration["entity_name"]) != python_name(subject_name(target)):
            diagnostics.append(f"{source_name(carrier)}: native entity name disagrees with active Subject `{target}`.")
            continue
        for base in declaration["bases"]:
            matches = class_symbols.get(base)
            exact_class = matches is not None
            if not exact_class:
                matches = symbols.get(python_name(base), [])
            # The immediate qualified Topic parent disambiguates repeated Form names.
            try:
                parsed = notation.parse_subject_expression(target, subject_profile="approved").expression
                if isinstance(parsed, notation.Path) and parsed.steps:
                    parent = notation.render_subject(replace(parsed, steps=parsed.steps[:-1]))
                    if not exact_class and parent in matches:
                        matches = [parent]
            except notation.SubjectNotationError:
                pass
            if len(matches) != 1:
                diagnostics.append(f"{source_name(carrier)}: native base `{base}` is unresolved or ambiguous.")
                continue
            pending.append((target, matches[0], source_name(carrier), False))
    terminals: dict[str, list[Record]] = {}
    for node in nodes.values():
        terminal = terminal_name(node["identity"])
        if terminal is not None:
            terminals.setdefault(terminal, []).append(node)
    for child, parent, evidence, is_reference in pending:
        child_node = by_identity.get(child)
        matches = ([by_identity[parent]] if parent in by_identity else terminals.get(parent, [])) if is_reference else [by_identity[parent]] if parent in by_identity else []
        if child_node is None or not matches:
            diagnostics.append(f"{evidence}: NARROWER_THAN binding `{child}` -> `{parent}` has an undeclared endpoint.")
            continue
        if is_reference and (len(matches) != 1 or len(matches[0]["source_bindings"]) != 1):
            diagnostics.append(f"{evidence}: NARROWER_THAN reference `{parent}` is ambiguous.")
            continue
        parent_node = matches[0]
        edge_id = _identifier("narrowing-edge:", [child_node["id"], parent_node["id"]])
        edge = edges.setdefault(edge_id, {
            "id": edge_id, "kind": "NARROWER_THAN", "relation_source": child_node["id"],
            "relation_target": parent_node["id"], "source_bindings": set(),
        })
        edge["source_bindings"].add(evidence)
    if "Event Record" in by_identity and not any(edge["relation_source"] == by_identity["Event Record"]["id"] for edge in edges.values()):
        diagnostics.append("Event Record: no explicit NARROWER_THAN parent; rendered as a root.")
    for row in [*nodes.values(), *edges.values()]:
        row["source_bindings"] = sorted(row["source_bindings"])
    graph = {
        "kind": "current_declared_narrowing_tree", "source_basis": "current_declared_carriers",
        "native_admission": "not_performed", "nodes": sorted(nodes.values(), key=lambda row: row["identity"]),
        "edges": sorted(edges.values(), key=lambda row: row["id"]), "diagnostics": sorted(set(diagnostics)),
    }
    return graph, {"owners": [{"source": carrier["source"]} for carrier in owners]}


def _model_target(expression: notation.Path) -> str:
    """Keep top-level allowed literals as constraints rather than target identities."""

    cutoff = next(
        (index for index, step in enumerate(expression.steps) if step.operator in {":", ":="}),
        len(expression.steps),
    )
    if cutoff == len(expression.steps):
        return notation.render_subject(expression)
    return notation.render_subject(replace(expression, steps=expression.steps[:cutoff]))


def _relation_definition_target(
    expression: notation.Path | notation.RelationChain,
) -> tuple[str, str] | None:
    """Find the one direct Relation endpoint declared by a Relation Definition."""

    expression = namespace_local_expression(expression) or expression
    if isinstance(expression, notation.Path):
        legacy = re.fullmatch(r"(?:CAPRMEDIO_MODEL/)?CFEL/Relation//([A-Za-z_][A-Za-z_0-9]*)",
                              notation.render_subject(expression))
        if legacy is not None:
            return f"Relation//{legacy[1]}", "relation"
    paths = expression.endpoints if isinstance(expression, notation.RelationChain) else (expression,)
    candidates = [path for path in paths if _target_kind(path) == "relation"]
    if len(candidates) != 1:
        return None
    target = candidates[0]
    return _model_target(target), "relation"


def _declaration_row(
    target: str, occurrence: Record, kind: str,
) -> Record:
    return {
        "identity": target,
        "source": occurrence["source"],
        "subject": occurrence["subject"],
        "declaration_kind": kind,
    }


def _enhanced_categories(
    carriers: list[Record], provenance: Record, diagnostics: list[str],
) -> Record:
    """Separate declared model targets from arbitrary Subject expressions.

    A Subject path can select, filter or constrain an existing Node. It becomes
    a model inventory entry only when it is the direct active target of a
    Requirement / Declaration Atom. This intentionally leaves raw syntax
    nodes in the legacy graph for lossless rendering without treating them as
    admitted model nodes.
    """

    carrier_by_path = {
        carrier["source"]["path"]: carrier
        for carrier in carriers
        if isinstance(carrier.get("source"), dict) and isinstance(carrier["source"].get("path"), str)
    }
    categories: dict[str, list[Record]] = {
        "primary_nodes": [], "properties": [], "instances": [], "relations": [],
        "classifications": [], "allowed_literals": [], "selected_subject_expressions": [],
    }
    active_count = {
        source_path: sum(
            occurrence["role"] == "governs" and occurrence["source"]["path"] == source_path
            for occurrence in provenance["occurrences"]
        )
        for source_path in carrier_by_path
    }
    for occurrence in provenance["occurrences"]:
        source = occurrence["source"]
        categories["selected_subject_expressions"].append({
            "expression": occurrence["subject"],
            "subject_role": occurrence["role"],
            "source": source,
        })
        carrier = carrier_by_path.get(source["path"])
        if (carrier is None or occurrence["role"] != "governs"
                or active_count[source["path"]] != 1):
            continue
        try:
            expression = notation.parse_subject_expression(
                occurrence["subject"], subject_profile="approved"
            ).expression
        except notation.SubjectNotationError as error:
            diagnostics.append(
                f"{occurrence['id']}: Model target unavailable: {error}"
            )
            continue
        if _is_relation_definition(carrier):
            admitted = _relation_definition_target(expression)
            if admitted is None:
                continue
            target, kind = admitted
        elif _is_declaration(carrier):
            local_expression = namespace_local_expression(expression)
            if local_expression is not None:
                expression = local_expression
            elif isinstance(expression, notation.RelationChain):
                continue
            kind = _target_kind(expression)
            if kind is None:
                # A Relation chain is not one Node declaration target.
                continue
            assert isinstance(expression, notation.Path)
            target = _model_target(expression)
        else:
            continue
        bucket = {
            "primary_node": "primary_nodes", "property": "properties",
            "instance": "instances", "relation": "relations",
        }[kind]
        categories[bucket].append(_declaration_row(target, occurrence, kind))
    return {
        key: sorted(values, key=lambda row: (str(row.get("identity", row.get("expression", row.get("source", "")))), str(row)))
        for key, values in categories.items()
    }


def compose_enhanced_current_graph(carriers: list[Record]) -> tuple[Record, Record]:
    """Add model/instance and CFEL inventories to the stable Subject graph.

    These records are source-bound observations.  They intentionally do not
    evaluate CFEL, synthesize inherited facts, or turn literals and constraint
    annotations into graph Nodes.
    """

    from cfel_claim_constraints import claim_cfel_blocks, claim_python_blocks, constraints_for

    graph, provenance = compose_current_graph(carriers, unsupported_as_diagnostics=True)
    constraints, unresolved = constraints_for(carriers)
    declaration_sources = {
        (carrier["source"].get("atom_id"), carrier["source"].get("version"), carrier["source"].get("path"))
        for carrier in carriers if isinstance(carrier.get("source"), dict) and _is_declaration(carrier)
    }
    identified_sources = {
        (carrier["source"].get("atom_id"), carrier["source"].get("version"), carrier["source"].get("path"))
        for carrier in carriers if isinstance(carrier.get("source"), dict) and _view(carrier).get("type")
    }
    def declared(row: Record) -> bool:
        source = row.get("source", {})
        return (source.get("atom_id"), source.get("version"), source.get("path")) in declaration_sources
    def non_declaration_property(row: Record) -> bool:
        source = row.get("source", {})
        key = (source.get("atom_id"), source.get("version"), source.get("path"))
        return (row.get("kind") in {"property_constraint", "allowed_literal"}
                and key in identified_sources and not declared(row))
    model_constraints = [row for row in constraints if row.get("group") != "instances" and not non_declaration_property(row)]
    model = _enhanced_categories(carriers, provenance, graph["diagnostics"])
    nodes = {row["id"]: row for row in graph["nodes"]}
    edges = {row["id"]: row for row in graph["edges"]}
    formal_relations: dict[str, Record] = {}
    for index, clause in enumerate(constraints):
        selector = clause.get("source_selector")
        if (not declared(clause) or clause.get("kind") != "relation_cardinality"
                or clause.get("relation") != "INSTANCE_OF"
                or not isinstance(selector, str) or not selector.startswith("(") or not selector.endswith(")")
                or clause.get("source_cardinality") is not None or clause.get("target_cardinality") is not None):
            continue
        try:
            parsed = notation.parse_subject_expression(selector[1:-1], subject_profile="approved").expression
            target = notation.parse_subject_expression(clause["target_selector"], subject_profile="approved").expression
        except (notation.SubjectNotationError, TypeError):
            continue
        if not isinstance(parsed, notation.RelationChain) or not isinstance(target, notation.Path):
            continue
        source_identity, target_identity = notation.render_subject(parsed), notation.render_subject(target)
        occurrence_id = f"{clause['source'].get('path', '')}#formal_claim[{index}]"
        provenance["occurrences"].append({"id": occurrence_id, "subject": clause["expression"],
                                          "source": clause["source"], "role": "formal_claim"})
        for identity in (source_identity, target_identity):
            node_id = _identifier("subject:", identity)
            node = nodes.setdefault(node_id, {"identity": identity, "id": node_id,
                                               "occurrence_ids": [], "is_full_target": False})
            node["occurrence_ids"] = sorted(set(node["occurrence_ids"]) | {occurrence_id})
        source_id, target_id = (_identifier("subject:", identity) for identity in (source_identity, target_identity))
        metadata = {"kind": "INSTANCE_OF", "forward_cardinality": None, "reverse_cardinality": None}
        edge_id = _identifier("subject-edge:", [metadata, source_id, target_id])
        edge = edges.setdefault(edge_id, {**metadata, "id": edge_id, "relation_source": source_id,
                                          "relation_target": target_id, "occurrence_ids": []})
        edge["occurrence_ids"] = sorted(set(edge["occurrence_ids"]) | {occurrence_id})
        relation = formal_relations.setdefault(edge_id, {"kind": "INSTANCE_OF", "source": source_identity,
                                                          "target": target_identity, "occurrence_ids": []})
        relation["occurrence_ids"] = sorted(set(relation["occurrence_ids"]) | {occurrence_id})
    model["relations"].extend(sorted(formal_relations.values(), key=lambda row: (row["source"], row["target"])))
    graph["nodes"] = sorted(nodes.values(), key=lambda row: (row["identity"], row["id"]))
    graph["edges"] = sorted(edges.values(), key=lambda row: row["id"])
    enhanced = {
        **graph,
        "kind": "current_atom_model_graph",
        "model": model,
        "constraints": model_constraints,
        "model_contracts": [row for row in model_constraints
                            if row.get("kind") in {"property_constraint", "allowed_literal"} and declared(row)],
        "source_constraints": [row for row in constraints if row.get("group") != "instances" and non_declaration_property(row)],
        "instance_constraints": [row for row in constraints if row.get("group") == "instances"],
        "formal_claim_blocks": [block for carrier in carriers for block in
                                [*claim_cfel_blocks(carrier), *claim_python_blocks(carrier)]],
        "cfel_diagnostics": unresolved,
    }
    return enhanced, provenance
