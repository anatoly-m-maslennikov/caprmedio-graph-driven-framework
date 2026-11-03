"""Small, source-bound audits for selected Subject expressions."""

from __future__ import annotations

from collections import defaultdict
from collections.abc import Mapping
from dataclasses import replace
import re
from typing import Any

import subject_notation as notation
from carrier_aliases import carrier_read_view
from contract_graph import _conditional_target, _has_selection, _target as _contract_target
from current_subject_graph import _model_target, _target_kind, namespace_local_expression
from subject_projection_data import build_subject_projection_data


Record = dict[str, Any]
_ACTIVE = ("active", "governs")
_PASSIVE = ("passive", "depends_on")
_MODEL_DESCRIPTORS = {"Relation", "Operator", "Format", "Term"}


def _scope_subject(value: str) -> str:
    """Classify explicit MODEL Subjects without treating concrete instances as kinds."""
    try:
        expression = notation.parse_subject_expression(value, subject_profile="approved").expression
    except notation.SubjectNotationError:
        if re.match(r"^\s*(?:CAPRMEDIO_STRUCTURE|CAPRMEDIO\s*<\+\s*STRUCTURE)\s*<\+", value):
            return "structure"
        return "model" if re.match(r"^\s*(?:CAPRMEDIO_MODEL|CAPRMEDIO\s*<\+\s*MODEL)\s*<\+", value) else "unresolved"

    def root(expr: notation.Path | notation.RelationChain) -> str | None:
        if isinstance(expr, notation.RelationChain):
            first = expr.endpoints[0]
            if isinstance(first.head, notation.Name) and first.head.value in {"CAPRMEDIO_MODEL", "CAPRMEDIO_STRUCTURE"}:
                return first.head.value if notation.namespace_local_expression(expr) is not None else None
            if (isinstance(first.head, notation.Name) and first.head.value == "CAPRMEDIO"
                    and len(expr.endpoints) > 1 and isinstance(expr.endpoints[1].head, notation.Name)
                    and notation.namespace_local_expression(expr) is not None):
                return "CAPRMEDIO_" + expr.endpoints[1].head.value
            return None
        return root(expr.head) if isinstance(expr.head, (notation.Path, notation.RelationChain)) else None

    namespace = root(expression)
    if namespace == "CAPRMEDIO_STRUCTURE":
        return "structure"
    if namespace != "CAPRMEDIO_MODEL":
        if isinstance(expression, notation.Path) and isinstance(expression.head, notation.Name) and not expression.steps:
            if expression.head.value == "CAPRMEDIO_MODEL":
                return "model"
            if expression.head.value == "CAPRMEDIO_STRUCTURE":
                return "structure"
        return "unresolved"

    def has_concrete_instance(expr: object) -> bool:
        if isinstance(expr, notation.SelectionGroup):
            return any(has_concrete_instance(member) for member in expr.members)
        if isinstance(expr, notation.Qualification):
            return has_concrete_instance(expr.relative_path)
        if isinstance(expr, notation.RelationChain):
            return any(has_concrete_instance(endpoint) for endpoint in expr.endpoints)
        if not isinstance(expr, notation.Path):
            return False
        if has_concrete_instance(expr.head):
            return True
        prior = expr.head.value if isinstance(expr.head, notation.Name) else None
        for step in expr.steps:
            if step.operator == "//" and prior not in _MODEL_DESCRIPTORS:
                return True
            if has_concrete_instance(step.operand):
                return True
            if isinstance(step.operand, notation.Name):
                prior = step.operand.value
        return False

    return "instance" if has_concrete_instance(expression) else "model"


def select_model_subjects(carriers: list[Record]) -> tuple[list[Record], list[Record]]:
    """Filter one projection's Subject occurrences while retaining source records."""
    selected, unresolved = [], []
    for carrier in carriers:
        subjects = _authored_subjects(carrier)
        if subjects is None:
            selected.append(carrier)
            continue
        kept = {}
        for role, keys in (("active", _ACTIVE), ("passive", _PASSIVE)):
            for key in keys:
                if key not in subjects:
                    continue
                original = subjects[key]
                values = original if isinstance(original, list) else [original]
                values_kept = []
                for value in values:
                    scope = _scope_subject(value) if isinstance(value, str) and value.strip() else "unresolved"
                    if scope == "model":
                        values_kept.append(value)
                    elif scope == "unresolved":
                        source = _source(carrier)
                        unresolved.append({"source": source, "pin": _pin(source), "role": role, "source_key": key,
                                           "raw_value": value if isinstance(value, str) else str(value),
                                           "message": "Subject lacks an explicit parseable MODEL namespace; review required."})
                if values_kept:
                    kept[key] = values_kept if isinstance(original, list) else values_kept[0]
        copy = dict(carrier)
        copy["subjects"] = kept
        if isinstance(carrier.get("metadata"), Mapping):
            copy["metadata"] = {**carrier["metadata"], "subjects": kept}
        selected.append(copy)
    return selected, unresolved


def _source(carrier: Mapping[str, Any]) -> Record:
    return dict(carrier.get("source", {}))


def _pin(source: Mapping[str, Any]) -> str:
    return f"{source.get('atom_id', 'unknown')}@{source.get('version', 'unknown')}"


def _view(carrier: Mapping[str, Any]) -> Mapping[str, Any]:
    value = carrier.get("read_view")
    if isinstance(value, Mapping):
        return value
    metadata = carrier.get("metadata")
    return carrier_read_view(dict(metadata)) if isinstance(metadata, Mapping) else {}


def _authored_subjects(carrier: Mapping[str, Any]) -> Mapping[str, Any] | None:
    """Read source keys before compatibility aliases add duplicate spellings."""

    metadata = carrier.get("metadata")
    if isinstance(metadata, Mapping) and isinstance(metadata.get("subjects"), Mapping):
        return metadata["subjects"]
    subjects = carrier.get("subjects")
    return subjects if isinstance(subjects, Mapping) else None


def _canonical(value: str) -> tuple[str | None, str | None]:
    """Render approved syntax, retaining names and qualification values exactly."""

    try:
        expression = notation.parse_subject_expression(value, subject_profile="approved").expression
    except notation.SubjectNotationError as error:
        return None, str(error)
    return notation.render_subject(expression), None


def _occurrences(carriers: list[Record]) -> tuple[list[Record], list[Record]]:
    rows, diagnostics = [], []
    for carrier in carriers:
        source = _source(carrier)
        subjects = _authored_subjects(carrier)
        if subjects is None:
            continue
        for role, keys in (("active", _ACTIVE), ("passive", _PASSIVE)):
            for key in keys:
                if key not in subjects:
                    continue
                values = subjects[key] if isinstance(subjects[key], list) else [subjects[key]]
                for value in values:
                    if not isinstance(value, str) or not value.strip():
                        diagnostics.append({"source": source, "pin": _pin(source), "role": role, "source_key": key,
                                            "raw_value": value, "message": "Subject must be non-empty text."})
                        continue
                    canonical, error = _canonical(value)
                    row = {"role": role, "source": source, "pin": _pin(source),
                           "source_key": key, "raw_value": value,
                           "subject": canonical}
                    if error is not None:
                        row["parse_error"] = error
                        diagnostics.append({**row, "message": f"Unsupported Subject: {error}"})
                    rows.append(row)
    return rows, diagnostics


def _local_target(subject: str) -> tuple[str, str] | None:
    """Return an existing declaration-shaped target; never expand selectors."""

    expression = notation.parse_subject_expression(subject, subject_profile="approved").expression
    expression = namespace_local_expression(expression) or expression
    if _has_selection(expression):
        return None
    if (isinstance(expression, notation.Path) and isinstance(expression.head, notation.Name)
            and expression.head.value in {"CAPRMEDIO_MODEL", "CAPRMEDIO_STRUCTURE"} and not expression.steps):
        return None
    target = _contract_target(expression)
    if target is not None:
        return target
    if not isinstance(expression, notation.Path):
        return None
    if isinstance(expression.head, notation.Name) and expression.head.value in {"CFEL", "Carrier", "Term"}:
        return "component", _model_target(expression)
    kind = _target_kind(expression)
    if kind in {"primary_node", "property", "instance", "relation"}:
        return kind, _model_target(expression)
    return None


def _entity_target(subject: str) -> tuple[str, str] | None:
    """Keep a direct entity target or the last path in a plain context chain."""

    expression = notation.parse_subject_expression(subject, subject_profile="approved").expression
    if isinstance(expression, notation.RelationChain):
        if not expression.links or any(link.operator != "<+" or link.relation_type is not None for link in expression.links):
            return None
        expression = expression.endpoints[-1]
    if not isinstance(expression, notation.Path):
        return None
    if any(step.operator in {":", ":="} or isinstance(step.operand, notation.Qualification) for step in expression.steps):
        return None
    rendered = notation.render_subject(expression)
    return _local_target(rendered)


def _property_parts(target: str) -> tuple[str, str] | None:
    expression = notation.parse_subject_expression(target, subject_profile="approved").expression
    if not isinstance(expression, notation.Path):
        return None
    for index, step in enumerate(expression.steps):
        if step.operator == ".":
            origin = replace(expression, steps=expression.steps[:index], value_format=None, value_cardinality=None)
            suffix = replace(expression, head=step.operand, steps=expression.steps[index + 1:],
                             value_format=None, value_cardinality=None)
            return notation.render_subject(origin), notation.render_subject(suffix)
    return None


def _entity_definitions(carriers: list[Record]) -> dict[str, list[Record]]:
    rows: dict[str, list[Record]] = defaultdict(list)
    for carrier in carriers:
        view = _view(carrier)
        if view.get("content_role") != "Requirement" or view.get("type") != "Entity Definition":
            continue
        subjects = _authored_subjects(carrier)
        if subjects is None:
            continue
        values = subjects.get("active", subjects.get("governs"))
        values = values if isinstance(values, list) else [values]
        if len(values) != 1 or not isinstance(values[0], str):
            continue
        canonical, error = _canonical(values[0])
        if canonical is not None and error is None:
            rows[canonical].append(_source(carrier))
    return rows


def _term_identity(subject: str) -> str | None:
    expression = notation.parse_subject_expression(subject, subject_profile="approved").expression
    expression = namespace_local_expression(expression) or expression
    if (not isinstance(expression, notation.Path) or not isinstance(expression.head, notation.Name)
            or expression.head.value != "Term" or len(expression.steps) != 1
            or expression.steps[0].operator != "//" or not isinstance(expression.steps[0].operand, notation.Name)
            or expression.value_format is not None or expression.value_cardinality is not None):
        return None
    return notation.render_subject(expression)


def _term_definitions(carriers: list[Record]) -> dict[str, list[Record]]:
    rows: dict[str, list[Record]] = defaultdict(list)
    for carrier in carriers:
        view = _view(carrier)
        if (view.get("content_role") != "Method" or view.get("type") != "Term Definition"
                or not str(_source(carrier).get("atom_id", "")).startswith("CA-M-")):
            continue
        subjects = _authored_subjects(carrier)
        if subjects is None:
            continue
        values = subjects.get("active", subjects.get("governs"))
        values = values if isinstance(values, list) else [values]
        if len(values) != 1 or not isinstance(values[0], str):
            continue
        try:
            identity = _term_identity(values[0])
        except notation.SubjectNotationError:
            continue
        if identity is not None:
            rows[identity].append(_source(carrier))
    return rows


def _declaration_catalog(data: Mapping[str, Any]) -> dict[tuple[str, str], list[Record]]:
    declarations = data["declarations"]
    catalog = {("primary_node", identity): rows for identity, rows in declarations.get("primary_nodes", {}).items()}
    for kind_name, key in (("property", "properties"), ("instance", "instances"),
                           ("relation", "relations"), ("component", "components")):
        catalog.update({(kind_name, identity): rows for identity, rows in declarations.get(key, {}).items()})
    return catalog


def _conditional_coverage(subject: str, catalog: Mapping[tuple[str, str], list[Record]]) -> Record | None:
    expression = notation.parse_subject_expression(subject, subject_profile="approved").expression
    expression = namespace_local_expression(expression) or expression
    conditional = _conditional_target(expression, catalog)
    if conditional is None:
        return None
    bound, binding, _ = conditional
    return {"status": "covered", "base_target": bound[1], "binding": binding,
            "declaration_refs": [_pin(row["source"]) for row in catalog[bound]]}


def _inherited_property_coverage(identity: str, data: Mapping[str, Any]) -> Record | None:
    parts = _property_parts(identity)
    if parts is None:
        return None
    origin, relative = parts
    entity = next((row for row in data["entities"] if row["identity"] == origin), None)
    if entity is None:
        return None
    inherited = [row for row in entity["inherited_properties"] if row["relative_name"] == relative]
    if not inherited:
        return None
    return {"status": "covered", "target": identity, "inherited": True,
            "declaration_refs": sorted({ref for row in inherited for ref in row["declaration_refs"]})}


def _coverage(subject: str, data: Mapping[str, Any], definitions: Mapping[str, list[Record]],
              term_definitions: Mapping[str, list[Record]]) -> Record:
    declarations = data["declarations"]
    known = _declaration_catalog(data)
    target = _local_target(subject)
    if target is None:
        conditional = _conditional_coverage(subject, known)
        return ({**conditional, "target": conditional["base_target"]} if conditional is not None else
                {"status": "unresolved", "message": "Subject is not one direct known target; review required."})
    kind, identity = target
    catalog = {"primary_node": "primary_nodes", "property": "properties", "instance": "instances",
               "relation": "relations", "component": "components"}.get(kind)
    keys = [identity, identity.removeprefix("Relation//")] if kind == "relation" else [identity]
    direct = next((declarations.get(catalog, {}).get(key) for key in keys if declarations.get(catalog, {}).get(key)), None)
    if direct:
        return {"status": "covered", "target": identity, "declaration_refs": [
            _pin(row["source"]) for row in direct
        ]}
    if kind == "property":
        inherited = _inherited_property_coverage(identity, data)
        if inherited is not None:
            return inherited
    if kind == "instance":
        expression = notation.parse_subject_expression(identity, subject_profile="approved").expression
        assert isinstance(expression, notation.Path)
        index = next((i for i, step in enumerate(expression.steps) if step.operator == "//"), None)
        if index is not None:
            base = notation.render_subject(replace(expression, steps=expression.steps[:index], value_format=None, value_cardinality=None))
            declared = declarations["primary_nodes"].get(base)
            if declared:
                return {"status": "covered", "target": identity, "base_target": base,
                        "declaration_refs": [_pin(row["source"]) for row in declared]}
    conditional = _conditional_coverage(subject, known)
    if conditional is not None:
        return {**conditional, "target": identity}
    term_identity = _term_identity(subject)
    if term_identity is not None and term_identity in term_definitions:
        return {"status": "outside_required_scope", "target": identity,
                "message": "Term has a Method / Term Definition; outside Requirement Declaration scope",
                "term_definition_refs": [_pin(source) for source in term_definitions[term_identity]]}
    definition_refs = definitions.get(subject, [])
    if kind == "component" and definition_refs:
        return {"status": "outside_required_scope", "target": identity,
                "message": "no Requirement Declaration; existing Entity Definition; outside R2469 required scope",
                "entity_definition_refs": [_pin(source) for source in definition_refs]}
    return {"status": "missing", "target": identity,
            "message": "No effective Requirement / Declaration coverage in the selected sources."}


def _provenance(rows: list[Record]) -> Record:
    occurrences = sorted(rows, key=lambda row: (row["pin"], row["source_key"], row["raw_value"]))
    return {"raw_values": sorted({row["raw_value"] for row in rows}),
            "pins": sorted({row["pin"] for row in rows}), "occurrences": occurrences}


def _is_defining(carrier: Mapping[str, Any], target: tuple[str, str]) -> bool:
    source = _source(carrier)
    atom_id = str(source.get("atom_id", ""))
    form = str(_view(carrier).get("type", ""))
    if atom_id.startswith("CA-R-") and (form.endswith("Declaration") or form.endswith("Definition")):
        return True
    return (atom_id.startswith("CA-M-") and _view(carrier).get("content_role") == "Method"
            and form == "Term Definition" and target[0] == "component"
            and _term_identity(target[1]) is not None)


def _inherited_definition_refs(target: tuple[str, str], data: Mapping[str, Any]) -> list[str]:
    if target[0] != "property":
        return []
    parts = _property_parts(target[1])
    if parts is None:
        return []
    origin, relative = parts
    entity = next((row for row in data["entities"] if row["identity"] == origin), None)
    if entity is None:
        return []
    return sorted({ref for row in entity["inherited_properties"] if row["relative_name"] == relative
                   for ref in row["declaration_refs"]})


def _entity_summary(carriers: list[Record], occurrences: list[Record], data: Mapping[str, Any]) -> Record:
    """Separate defining-carrier coverage from active Subject coverage."""

    source_index = {(str(_source(carrier).get("path", "")), _pin(_source(carrier))): carrier for carrier in carriers}
    rows: dict[tuple[str, str], Record] = {}
    for occurrence in occurrences:
        if occurrence["subject"] is None:
            continue
        try:
            target = _entity_target(occurrence["subject"])
        except notation.SubjectNotationError:
            target = None
        if target is None:
            continue
        row = rows.setdefault(target, {"identity": target[1], "kind": target[0],
                                       "defining_refs": set(), "active_refs": set(), "subjects": []})
        row["subjects"].append({key: occurrence[key] for key in ("raw_value", "pin", "source_key", "role", "source")})
        row["defining_refs"].update(_inherited_definition_refs(target, data))
        carrier = source_index.get((str(occurrence["source"].get("path", "")), occurrence["pin"]))
        if occurrence["role"] == "active":
            row["active_refs"].add(occurrence["pin"])
            if carrier is not None and _is_defining(carrier, target):
                row["defining_refs"].add(occurrence["pin"])
    entities = []
    for row in rows.values():
        defining_refs, active_refs = sorted(row["defining_refs"]), sorted(row["active_refs"])
        entities.append({**row, "defining_refs": defining_refs, "active_refs": active_refs,
                         "missing_definition": not defining_refs, "missing_active": not active_refs,
                         "subjects": sorted(row["subjects"], key=lambda item: (item["pin"], item["source_key"], item["raw_value"]))})
    entities.sort(key=lambda row: (row["kind"], row["identity"]))
    return {"kind": "entity_definition_summary", "entities": entities,
            "display_entities": [row for row in entities if row["missing_definition"] or row["missing_active"]],
            "coverage": {"entities": len(entities), "entities_with_any_missing": sum(
                row["missing_definition"] or row["missing_active"] for row in entities)}}


def build_subject_audits(carriers: list[Record], data: Record | None = None, *, scope_diagnostics: list[Record] | None = None) -> Record:
    """Build both selected-frontier Subject audits without admitting new Nodes."""

    data = build_subject_projection_data(carriers) if data is None else data
    occurrences, diagnostics = _occurrences(carriers)
    active = {row["subject"] for row in occurrences if row["role"] == "active" and row["subject"] is not None}
    active_raw = {row["raw_value"].strip() for row in occurrences if row["role"] == "active"}
    passive: dict[str, list[Record]] = defaultdict(list)
    for row in occurrences:
        if row["role"] != "passive":
            continue
        key = row["subject"] if row["subject"] is not None else "raw:" + row["raw_value"].strip()
        passive[key].append(row)
    passive_rows = [
        {"subject": rows[0]["subject"] or rows[0]["raw_value"],
         "unresolved": rows[0]["subject"] is None, **_provenance(rows)}
        for subject, rows in passive.items()
        if (subject not in active if rows[0]["subject"] is not None else rows[0]["raw_value"].strip() not in active_raw)
    ]
    definitions = _entity_definitions(carriers)
    term_definitions = _term_definitions(carriers)
    coverage_rows, unresolved = [], []
    unresolved_rows: dict[str, list[Record]] = defaultdict(list)
    for row in occurrences:
        if row["subject"] is None:
            unresolved_rows[row["raw_value"].strip()].append(row)
    for raw, rows in sorted(unresolved_rows.items()):
        unresolved.append({"subject": rows[0]["raw_value"], "status": "unresolved",
                           "message": f"Unsupported Subject: {rows[0]['parse_error']}", **_provenance(rows)})
    scope_groups: dict[str, list[Record]] = defaultdict(list)
    for diagnostic in scope_diagnostics or []:
        scope_groups[str(diagnostic["raw_value"])].append(diagnostic)
    for value, rows in sorted(scope_groups.items()):
        unresolved.append({"subject": value, "status": "unresolved", "message": rows[0]["message"],
                           **_provenance(rows)})
    diagnostics.extend(scope_diagnostics or [])
    for subject in sorted({row["subject"] for row in occurrences if row["subject"] is not None}):
        result = _coverage(subject, data, definitions, term_definitions)
        row = {"subject": subject, **result, **_provenance([row for row in occurrences if row["subject"] == subject])}
        (unresolved if result["status"] == "unresolved" else coverage_rows).append(row)
    return {
        "passive_only_subjects": {"kind": "passive_only_subjects", "subjects": sorted(passive_rows, key=lambda row: row["subject"]),
                                  "diagnostics": diagnostics,
                                  "coverage": {"subject_occurrences": len(occurrences),
                                               "parsed_subjects": len({row["subject"] for row in occurrences if row["subject"] is not None}),
                                               "unresolved_subjects": len(unresolved_rows) + len(scope_groups),
                                               "unresolved_occurrences": sum(row["subject"] is None for row in occurrences) + len(scope_diagnostics or []),
                                               "active_subjects": len(active), "passive_only_subjects": len(passive_rows)}},
        "subjects_without_declaration_coverage": {
            "kind": "subjects_without_declaration_coverage",
            "subjects": [row for row in coverage_rows if row["status"] == "missing"],
            "informational": [row for row in coverage_rows if row["status"] == "outside_required_scope"],
            "unresolved": unresolved, "diagnostics": diagnostics,
            "coverage": {"known_missing": sum(row["status"] == "missing" for row in coverage_rows),
                         "unresolved": len(unresolved)},
        },
        "entity_definition_summary": _entity_summary(carriers, occurrences, data),
    }


def render_subject_audit(audit: Mapping[str, Any], kind: str) -> str:
    """Render a body only; callers own projection frontmatter and wrapping."""

    report = audit[kind] if kind in audit else audit
    def evidence(row: Mapping[str, Any]) -> str:
        keys = sorted({item["source_key"] for item in row.get("occurrences", [])})
        return f"pins: {', '.join(row.get('pins', []))}; keys: {', '.join(keys)}"

    if report["kind"] == "passive_only_subjects":
        lines = ["# Subjects Used Only Passively", "", "## Subjects", ""]
        lines.extend(f"- `{row['subject']}` — {evidence(row)}"
                     + ("; unresolved syntax" if row["unresolved"] else "") for row in report["subjects"])
        lines.extend(["", f"## Diagnostics ({len(report['diagnostics'])})", ""])
        lines.extend(f"- `{row['raw_value']}` — {row['pin']}; {row['source_key']}; {row['message']}" for row in report["diagnostics"])
    elif report["kind"] == "subjects_without_declaration_coverage":
        lines = ["# Subjects Without Effective Requirement Declaration Coverage", "", "## Subjects", ""]
        lines.extend(f"- `{row['subject']}` — {row['message']}; {evidence(row)}" for row in report["subjects"])
        lines.extend(["", "## Informational outside required scope", ""])
        lines.extend(f"- `{row['subject']}` — {row['message']}; {evidence(row)}"
                     + (f"; Term Definition: {', '.join(row['term_definition_refs'])}" if row.get("term_definition_refs") else "")
                     for row in report["informational"])
        lines.extend(["", "## Unresolved coverage needing review", ""])
        lines.extend(f"- `{row['subject']}` — {row['message']}; {evidence(row)}" for row in report["unresolved"])
    else:
        lines = ["# Entity Definition Summary", "", "| Entity | Kind | Defining atom | Active Subject |", "| --- | --- | --- | --- |"]
        for row in report["display_entities"]:
            lines.append(f"| `{row['identity']}` | {row['kind']} | {'missing' if row['missing_definition'] else ', '.join(row['defining_refs'])} | {'missing' if row['missing_active'] else ', '.join(row['active_refs'])} |")
    if not any(line.startswith("- ") for line in lines):
        lines.append("- None.")
    return "\n".join(lines) + "\n"
