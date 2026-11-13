"""Pure Markdown views over ``build_subject_projection_data`` output."""

from __future__ import annotations

from collections.abc import Mapping, Sequence
import re
from typing import Any

from readable_entity_tree_data import primary_tree, read_edges, read_nodes


_NAMESPACE = re.compile(r"^(CAPRMEDIO_MODEL|CAPRMEDIO_STRUCTURE|CAPRMEDIO\s*<\+\s*(?:MODEL|STRUCTURE))(?:\s*<\+\s*(.+))?$")


def _source_ref(value: object) -> str | None:
    if isinstance(value, str):
        return value.strip() or None
    if not isinstance(value, Mapping):
        return None
    atom_id = value.get("atom_id")
    version = value.get("version")
    if atom_id is None:
        return None
    return f"{atom_id}@{version}" if version is not None else str(atom_id)


def _refs(value: object) -> list[str]:
    if isinstance(value, Mapping):
        for key in ("declaration_refs", "source_refs", "source"):
            if key in value:
                return _refs(value[key])
        ref = _source_ref(value)
        return [ref] if ref else []
    if isinstance(value, Sequence) and not isinstance(value, (str, bytes, bytearray)):
        return list(dict.fromkeys(ref for item in value for ref in _refs(item)))
    ref = _source_ref(value)
    return [ref] if ref else []


def _claims(value: object) -> list[tuple[str | None, str, str]]:
    if not isinstance(value, Sequence) or isinstance(value, (str, bytes, bytearray)):
        return []
    return [
        (_source_ref(row.get("source")), row["block"], row.get("label", "CFEL"))
        for row in value
        if isinstance(row, Mapping) and isinstance(row.get("block"), str)
    ]


def _fence(lines: Sequence[str], label: str = "text") -> list[str]:
    width = max([3] + [len(match.group(0)) + 1 for line in lines for match in re.finditer(r"`+", line)])
    marker = "`" * width
    return [f"{marker}{label}", *lines, marker]


def _cfel(block: str, label: str = "CFEL") -> str:
    width = max([3] + [len(match.group(0)) + 1 for match in re.finditer(r"`+", block)])
    marker = "`" * width
    content = block if block.endswith("\n") else block + "\n"
    return f"{marker}{label}\n{content}{marker}"


def _tree(data: Mapping[str, Any]) -> list[str]:
    graph = data["tree"]
    nodes = read_nodes(graph["nodes"])
    narrowing = [edge for edge in graph["edges"] if edge["kind"] == "NARROWER_THAN"]
    children, _, _, _ = read_edges(narrowing, nodes)
    lines, _, _ = primary_tree(nodes, children, set(nodes))
    return lines


def _namespace_path(value: object) -> tuple[str, ...] | None:
    if not isinstance(value, str):
        return None
    match = _NAMESPACE.fullmatch(" ".join(value.strip().split()))
    if not match:
        return None
    tail = [] if match.group(2) is None else [part.strip() for part in re.split(r"\s*<\+\s*", match.group(2))]
    root = tuple(part.strip() for part in re.split(r"\s*<\+\s*", match.group(1)))
    return (*root, *tail) if all(tail) else None


def _namespace_rows(data: Mapping[str, Any]) -> dict[tuple[str, ...], set[str]]:
    rows: dict[tuple[str, ...], set[str]] = {}

    def add(subject: object, source: object) -> None:
        path = _namespace_path(subject)
        refs = _refs(source)
        if path is not None and refs:
            rows.setdefault(path, set()).update(refs)

    for row in data.get("namespaces", []):
        if isinstance(row, Mapping):
            add(row.get("subject"), row.get("source"))
    for owner in data["tree_provenance"].get("owners", []):
        if isinstance(owner, Mapping):
            subjects = owner.get("subjects", owner.get("subject"))
            if isinstance(subjects, Mapping):
                subjects = subjects.get("active", subjects.get("governs"))
            if isinstance(subjects, Sequence) and not isinstance(subjects, (str, bytes, bytearray)):
                for subject in subjects:
                    add(subject, owner.get("source"))
            else:
                add(subjects, owner.get("source"))
    return rows


def _render_namespace(rows: Mapping[tuple[str, ...], set[str]]) -> list[str]:
    if not rows:
        return []
    children: dict[tuple[str, ...], set[str]] = {}
    refs: dict[tuple[str, ...], set[str]] = {}
    for path, source_refs in rows.items():
        for index in range(1, len(path) + 1):
            prefix = path[:index]
            refs.setdefault(prefix, set()).update(source_refs)
            if index > 1:
                children.setdefault(path[: index - 1], set()).add(path[index - 1])

    def walk(prefix: tuple[str, ...], depth: int) -> list[str]:
        lines: list[str] = []
        for child in sorted(children.get(prefix, ())):
            current = prefix + (child,)
            suffix = f" [{', '.join(sorted(refs[current]))}]" if refs.get(current) else ""
            lines.append("  " * depth + f"<+ {child}{suffix}")
            lines.extend(walk(current, depth + 1))
        return lines

    lines = ["## Namespace context", "", "```text"]
    for root in sorted(path for path in refs if len(path) == 1):
        lines.extend([root[0], *walk(root, 1)])
    return [*lines, "```", ""]


def _entities(data: Mapping[str, Any]) -> list[Mapping[str, Any]]:
    return [row for row in data["entities"] if isinstance(row, Mapping)]


def _declaration_claims(data: Mapping[str, Any], identity: str) -> list[tuple[str | None, str, str]]:
    entries = data.get("declarations", {}).get("primary_nodes", {}).get(identity, [])
    return [claim for entry in entries for claim in _claims([*entry.get("cfel_blocks", []), *entry.get("python_blocks", [])])]


def _entity_claims(data: Mapping[str, Any], entity: Mapping[str, Any]) -> list[tuple[str | None, str, str]]:
    return _claims(entity.get("formal_claims")) or _declaration_claims(data, str(entity["identity"]))


def _properties(entity: Mapping[str, Any], level: int) -> list[Mapping[str, Any]]:
    direct = entity.get("direct_properties", [])
    if level == 2:
        return [row for row in direct if isinstance(row, Mapping)]
    inherited = entity.get("inherited_properties", [])
    return [row for row in (*direct, *inherited) if isinstance(row, Mapping)]


def _cardinality(value: object) -> str:
    if not isinstance(value, Mapping):
        return "missing"
    minimum, maximum = value.get("minimum"), value.get("maximum")
    return f"{minimum}+" if maximum is None else str(minimum) if maximum == minimum else f"{minimum}..{maximum}"


def _contract_channels(contract: Mapping[str, Any]) -> list[str]:
    if contract.get("kind") == "allowed_literal":
        return [f"    - allowed literal: `{contract.get('literal', '')}`"]
    if contract.get("kind") != "property_constraint":
        return []
    channels = []
    for key, label in (
        ("selection", "nesting"), ("name_format", "name format"),
        ("occurrence_cardinality", "occurrence cardinality"),
        ("effective_occurrence_cardinality", "effective occurrence cardinality"),
        ("value_format", "value format"), ("value_cardinality", "value cardinality"),
    ):
        if key in contract:
            value = ("omitted" if key == "occurrence_cardinality" and contract[key] is None
                     else "conflict" if key == "effective_occurrence_cardinality" and contract.get("occurrence_conflict")
                     else _cardinality(contract[key]) if key.endswith("cardinality") else contract[key])
            channels.append(f"    - {label}: `{value}`")
    return channels


def _render_contracts(lines: list[str], property: Mapping[str, Any], refs: list[str]) -> None:
    for contract in property.get("contracts", []):
        if not isinstance(contract, Mapping):
            continue
        expression = contract.get("expression", "[unwritten contract expression]")
        sources = _refs(contract.get("source")) or ["missing source"]
        for source in sources:
            lines.append(f"  - contract: `{expression}` — {source}")
            lines.extend(_contract_channels(contract))


def _render_property(lines: list[str], property: Mapping[str, Any], level: int) -> None:
    identity = str(property.get("identity", "[missing Property identity]"))
    relative = str(property.get("relative_name", identity))
    tags = " ".join(tag for tag in ("[inherited]" if property.get("inherited") else "",
                                    "[overridden]" if property.get("overridden") else "",
                                    "[multiple applicable declarations]" if property.get("multiple_applicable") else "") if tag)
    tags = f" {tags}" if tags else ""
    refs = _refs(property.get("declaration_refs"))
    for source in refs or ["missing Declaration data"]:
        lines.append(f"- property: `{identity}` (relative `{relative}`){tags} — {source}")
    if property.get("inherited") and property.get("origin_entity"):
        lines.append(f"  - origin: `{property['origin_entity']}`")
    if level >= 3:
        _render_contracts(lines, property, refs)
        if "effective_value_format" in property:
            sources = [ref for source in property.get("effective_value_format_sources", []) for ref in _refs(source)]
            lines.append(f"  - effective value format: `{property['effective_value_format']}` — {', '.join(sources) or 'missing source'}")
        for clause in property.get("instance_constraints", []):
            if isinstance(clause, Mapping):
                scope = {"per_bearer_each_schema": "each Property schema per bearer", "project": "project population"}.get(clause.get("scope"))
                lines.append(f"  - instance constraint: `{clause.get('expression', '')}` — {', '.join(_refs(clause.get('source'))) or 'missing source'}" + (f"; scope: {scope}" if scope else ""))
    if level == 4:
        claims = _claims(property.get("formal_claims"))
        if claims:
            lines.append("  - Property Declaration " + ("Formal Claim:" if any(label.casefold() != "cfel" for _, _, label in claims) else "CFEL:"))
            for source, block, label in claims:
                lines.append(f"    - source: `{source or 'missing source'}`")
                lines.extend(_cfel(block, label).splitlines())
        else:
            lines.append("  - Property Declaration CFEL: [missing CFEL block]")


def _render_properties(lines: list[str], data: Mapping[str, Any], level: int) -> None:
    heading = "Property declarations" if level == 4 else "Direct properties" if level == 2 else "Effective properties"
    lines.extend(["", f"## {heading}", ""])
    shown = False
    for entity in _entities(data):
        properties = _properties(entity, level)
        if not properties:
            continue
        shown = True
        lines.extend([f"### `{entity['identity']}`", ""])
        refs = _refs(entity.get("declaration_refs"))
        lines.append("- Declaration sources: " + (", ".join(refs) if refs else "[missing Current Requirement/Form Declaration]"))
        overridden = {old.get("identity")
                      for rules in entity.get("property_rule_origins", {}).values()
                      for rule in rules for old in rule.get("replaces", [])} if level == 4 else set()
        for property in properties:
            if property.get("identity") in overridden:
                property = {**property, "overridden": True}
            _render_property(lines, property, level)
        lines.append("")
    if not shown:
        lines.append("- None supplied.")


def _render_primary_claims(lines: list[str], data: Mapping[str, Any]) -> None:
    entities = _entities(data)
    by_identity = {str(entity["identity"]): entity for entity in entities}
    lines.extend(["", "## Primary Declaration CFEL", ""])
    for entity in entities:
        identity = str(entity["identity"])
        lines.extend([f"### `{identity}`", ""])
        declaration_refs = _refs(entity.get("declaration_refs"))
        own = _entity_claims(data, entity)
        if own:
            lines.append("- own Declaration:")
            for source, block, label in own:
                lines.append(f"  - source: `{source or 'missing source'}`")
                lines.extend(_cfel(block, label).splitlines())
        else:
            lines.append("- own Declaration: [missing CFEL block]" if declaration_refs else
                         "- own Declaration: [missing Current Requirement/Form Declaration]")
        for ancestor in entity.get("ancestors", []):
            ancestor = str(ancestor)
            parent = by_identity.get(ancestor)
            claims = _entity_claims(data, parent) if parent else _declaration_claims(data, ancestor)
            refs = _refs(parent.get("declaration_refs")) if parent else []
            lines.append(f"- ancestor Declaration `{ancestor}`:")
            if claims:
                for source, block, label in claims:
                    lines.append(f"  - source: `{source or 'missing source'}`")
                    lines.extend(_cfel(block, label).splitlines())
            else:
                lines.append("  - [missing CFEL block]" if refs else "  - [missing Current Requirement/Form Declaration]")
        lines.append("")


def _render_rule_origins(lines: list[str], data: Mapping[str, Any]) -> None:
    lines.extend(["", "## Entity rule origins", ""])
    for entity in _entities(data):
        properties = entity.get("property_rule_origins", {})
        relations = entity.get("relation_rule_origins", {})
        if not any(properties.values()) and not any(relations.values()):
            continue
        lines.extend([f"### `{entity['identity']}`", ""])
        for group, label in (("declared_here", "Declared here"), ("inherited", "Inherited"),
                             ("overridden_here", "Overridden here")):
            property_rows = properties.get(group, [])
            relation_rows = relations.get(group, [])
            if not property_rows and not relation_rows:
                continue
            lines.extend([f"#### {label}", ""])
            for row in property_rows:
                refs = ", ".join(_refs(row.get("declaration_refs"))) or "missing Declaration data"
                lines.append(f"- Property `{row['identity']}` — {refs}")
                for old in row.get("replaces", []):
                    old_refs = ", ".join(_refs(old.get("declaration_refs"))) or "missing Declaration data"
                    lines.append(f"  - Replaces rule from `{old['origin_entity']}` — {old_refs}")
                    _render_contracts(lines, old, _refs(old.get("declaration_refs")))
            for row in relation_rows:
                refs = ", ".join(_refs(row.get("declaration_refs"))) or "missing Declaration data"
                derivation = row.get("derivation") or "unclassified"
                lines.append(f"- Relation `{row['relation']}` ({derivation}, {row['level']}, {row['direction']}) — {refs}")
                if row.get("expression") and "\n" not in row["expression"]:
                    lines.append(f"  - Rule: `{row['expression']}`")
                elif row.get("contract"):
                    lines.append(f"  - Contract: `{row['contract']}`")
                if row["origin_entity"] != entity["identity"]:
                    lines.append(f"  - Origin: `{row['origin_entity']}`")
                for old in row.get("replaces", []):
                    old_refs = ", ".join(_refs(old.get("declaration_refs"))) or "missing Declaration data"
                    lines.append(f"  - Replaces rule from `{old['origin_entity']}` — {old_refs}")
                    contract = old.get("contract")
                    if isinstance(contract, Mapping):
                        expression = contract.get("expression")
                        if isinstance(expression, str) and "\n" not in expression:
                            lines.append(f"    - Rule: `{expression}`")
                        else:
                            lines.append(f"    - Contract: `{contract}`")
            lines.append("")


def _render_relation_declarations(lines: list[str], data: Mapping[str, Any]) -> None:
    relations = data.get("relation_declarations", [])
    if not relations:
        return
    lines.extend(["", "## Relation declarations", ""])
    for classification in ("Direct", "Derived", None):
        group = [row for row in relations if row.get("derivation") == classification]
        if not group:
            continue
        lines.extend([f"### {classification or 'Unclassified'}", ""])
        for row in group:
            refs = ", ".join(_refs(row.get("declaration_refs"))) or "missing Declaration data"
            direct = ", ".join(f"`{name}`" for name in row.get("direct_relations", []))
            lines.append(f"- `{row['name']}` — {refs}" + (f"; inverse of {direct}" if direct else ""))
        lines.append("")


def _render_diagnostics(lines: list[str], data: Mapping[str, Any]) -> None:
    values = [*data.get("diagnostics", []), *data["tree"].get("diagnostics", [])]
    if not values:
        return
    rendered = []
    for value in values:
        if isinstance(value, Mapping):
            message = value.get("expression", value.get("message", value.get("code")))
            source = _source_ref(value.get("source"))
            if message is not None:
                rendered.append(f"{message}" + (f" — {source}" if source else ""))
        else:
            rendered.append(str(value))
    if rendered:
        lines.extend(["", "## Diagnostics", "", *(f"- {item}" for item in rendered)])


def render_primary_projection(data: Mapping[str, Any], level: int) -> str:
    """Render one of the first four primary Subject views as Markdown body."""

    if type(level) is not int or level not in {1, 2, 3, 4}:
        raise ValueError("Primary projection level must be 1, 2, 3, or 4")
    tree_lines = _tree(data)
    lines = ["## Primary entities", "", "NARROWER_THAN: `/`", "", *_fence(tree_lines), ""]
    lines.extend(_render_namespace(_namespace_rows(data)))
    if level >= 2:
        _render_properties(lines, data, level)
    if level == 4:
        _render_primary_claims(lines, data)
        _render_rule_origins(lines, data)
        _render_relation_declarations(lines, data)
    _render_diagnostics(lines, data)
    return "\n".join(lines).rstrip() + "\n"


__all__ = ["render_primary_projection"]
