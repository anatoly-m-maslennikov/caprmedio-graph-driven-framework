# CA-D-634@23

"""Render the existing typed Subject graph without admitting new model facts."""

import re
from collections import Counter

import yaml
from readable_entity_tree_data import (
    Children,
    Nodes,
    Record,
    name_key,
    primary_tree,
    read_edges,
    read_nodes,
    record,
    rows,
    text,
    tree,
)


def _sources(provenance: Record) -> list[str]:
    sources = set()
    for owner in rows(record(provenance).get("owners")):
        source = record(owner.get("source"))
        atom_id = text(source.get("atom_id"), "source Atom ID")
        version = source.get("version")
        if isinstance(version, bool) or not isinstance(version, int) or version < 1:
            raise ValueError("Invalid source Version")
        sources.add(f"{atom_id}@{version}")
    return sorted(sources)


def _fence(lines: list[str]) -> list[str]:
    width = max([3] + [len(match[0]) + 1 for line in lines for match in re.finditer(r"`+", line)])
    marker = "`" * width
    return [marker + "text", *lines, marker]


def named_selection_reference(value: object) -> str:
    """Render the carrier value as the declared Named Selection reference."""
    selection = text(value, "Projection.Source.Named Selection")
    return selection if selection.startswith("Named Selection//") else "Named Selection//" + selection


def _projection_frontmatter(
    provenance: Record,
    updated_at: str,
    projection_identity: Record | None,
    *,
    form: str,
) -> Record:
    """Build the admitted Projection carrier fields for a rendered view."""
    identity = record(projection_identity)
    return {
        "artifact_form": "Projection",
        "projection_id": text(identity.get("projection_id"), "projection_id"),
        "form": text(form, "Projection.Form"),
        "source": {
            "named_selection": named_selection_reference(identity.get("named_selection")),
            "atoms": _sources(provenance),
        },
        "updated_at": text(updated_at, "updated_at"),
    }


def _header(
    provenance: Record, updated_at: str, source_selection: str,
    projection_identity: Record | None = None,
) -> list[str]:
    frontmatter = yaml.safe_dump(
        _projection_frontmatter(provenance, updated_at, projection_identity, form="Map"),
        allow_unicode=True,
        sort_keys=False,
    ).rstrip()
    return [
        "---",
        frontmatter,
        "---",
        "",
        "## Inherency tree",
        "",
        "Source selection: " + text(source_selection, "source selection"),
        "",
        "Display selection: supplied graph nodes and Inherency relations; "
        "dependent entities appear in detail sections.",
        "",
        "Notation: / NARROWER_THAN; // INSTANCE_OF; . IS_PROPERTY_OF; "
        ": IS_ALLOWED_VALUE_OF; <+ CONTAINS (derived reverse of IS_CONTAINED_BY); >| HAS_CLASSIFICATION. Relations are traversed from broader to narrower, "
        "kind to named instance (the source INSTANCE_OF direction is instance to kind), "
        "bearer to dependent, Entity to allowed value, whole to part, and Entity to classification.",
        "",
        "This is a derived Projection, not independent model authority.",
        "",
        "### Primary entities",
        "",
    ]


def _details(
    appearances: list[str], nodes: Nodes, children: Children, dependents: set[str]
) -> tuple[list[str], set[str], set[str]]:
    body: list[str] = []
    shown: set[str] = set(appearances)
    cycles: set[str] = set()
    for primary in appearances:
        if any(edge["kind"] in {"IS_PROPERTY_OF", "IS_BORNE_BY"} for _, edge in children[primary]):
            lines, visited, found_cycles = tree(primary, dependents, nodes, children)
            body.extend(["### " + nodes[primary]["identity"], "", *_fence(lines), ""])
            shown.update(visited)
            cycles.update(found_cycles)
    return body, shown, cycles


def _limitations(
    graph: Record,
    nodes: Nodes,
    omitted: Counter[str],
    provisional: bool,
    orphaned: set[str],
    cycles: set[str],
) -> list[str]:
    notes = []
    if "native_admission" in graph and graph["native_admission"] != "performed":
        notes.append(
            "Native admission: "
            + str(graph.get("native_admission", "not evidenced by input"))
            + "."
        )
    if provisional:
        notes.append(
            "The input includes provisional notation; "
            "this rendering does not establish admitted model facts."
        )
    if omitted:
        notes.append(
            "Incomplete relation view: omitted unsupported or unclassified edges: "
            + ", ".join(f"{kind} ({count})" for kind, count in sorted(omitted.items()))
            + ". Their nodes remain visible without inventing a relation classification."
        )
    if orphaned:
        notes.append(
            "Incomplete dependent view: components have no displayed primary bearer: "
            + "; ".join(
                nodes[key]["identity"]
                for key in sorted(orphaned, key=lambda key: name_key(nodes, key))
            )
            + "."
        )
    if cycles:
        notes.append(
            "Cycles are marked [cycle] at the repeated placement and are not expanded further."
        )
    notes.append(
        "No inherited facts were synthesized; unavailable source facts remain unavailable."
    )
    notes.extend(str(item) for item in graph.get("diagnostics", []))
    return ["Source limitations:", "", *("- " + note for note in notes), ""]


def render_inherency(
    graph: Record, provenance: Record, *, updated_at: str, source_selection: str,
    projection_identity: Record | None = None,
) -> str:
    """Return deterministic Markdown; only the supplied rebuild time may vary."""
    graph = record(graph)
    nodes = read_nodes(rows(graph.get("nodes")))
    children, dependents, omitted, provisional = read_edges(rows(graph.get("edges")), nodes)
    main, appearances, cycles = primary_tree(nodes, children, set(nodes) - dependents)
    details, shown, detail_cycles = _details(appearances, nodes, children, dependents)
    body = _header(provenance, updated_at, source_selection, projection_identity)
    body.extend([*_fence(main), "", *details])
    body.extend(
        _limitations(graph, nodes, omitted, provisional, dependents - shown, cycles | detail_cycles)
    )
    return "\n".join(body)


def _model_header(
    provenance: Record, updated_at: str, source_selection: str,
    projection_identity: Record | None,
) -> list[str]:
    frontmatter = yaml.safe_dump(
        _projection_frontmatter(provenance, updated_at, projection_identity, form="Map"),
        allow_unicode=True,
        sort_keys=False,
    ).rstrip()
    return [
        "---", frontmatter, "---", "", "## Model graph", "",
        "Source selection: " + text(source_selection, "source selection"), "",
        "Display selection: direct Declaration targets, selected Subject expressions, "
        "Relations, classifications and constraint records. Literal values, Formats "
        "and cardinalities remain constraints, not graph Nodes.", "",
        "This is a derived Projection, not independent model authority.", "",
    ]


def _model_rows(title: str, rows_to_render: list[Record], formatter) -> list[str]:
    lines = ["## " + title, ""]
    if not rows_to_render:
        return [*lines, "- None supplied.", ""]
    lines.extend("- " + formatter(row) for row in rows_to_render)
    lines.append("")
    return lines


def _occurrences(row: Record) -> str:
    values = row.get("occurrence_ids")
    return "" if not values else " — " + ", ".join(str(value) for value in values)


def _cfel_diagnostic_text(row: Record) -> str:
    expression = row.get("expression")
    if isinstance(expression, str) and expression.strip():
        return expression
    return text(row.get("message"), "CFEL diagnostic message")


def render_model(
    graph: Record, provenance: Record, *, updated_at: str, source_selection: str,
    projection_identity: Record | None = None,
) -> str:
    """Render the bounded enhanced graph view without evaluating CFEL."""

    graph = record(graph)
    model = record(graph.get("model"))
    body = _model_header(provenance, updated_at, source_selection, projection_identity)
    body.extend(_model_rows(
        "Primary Nodes", rows(model.get("primary_nodes")),
        lambda row: "`" + text(row.get("identity"), "node identity") + "`" + _occurrences(row),
    ))
    body.extend(_model_rows(
        "Properties", rows(model.get("properties")),
        lambda row: "`" + text(row.get("identity"), "Property identity") + "`" + _occurrences(row),
    ))
    body.extend(_model_rows(
        "Instances", rows(model.get("instances")),
        lambda row: "`" + text(row.get("identity"), "instance identity") + "`" + _occurrences(row),
    ))
    def relation_text(row: Record) -> str:
        if "identity" in row:
            return "`" + text(row.get("identity"), "Relation identity") + "`"
        return "`" + text(row.get("kind"), "Relation") + "` `" + text(row.get("source"), "Relation source") + "` → `" + text(row.get("target"), "Relation target") + "`"

    def classification_text(row: Record) -> str:
        return "`" + text(row.get("source"), "classification subject") + "` >| `" + text(row.get("target"), "classification axis") + "`"

    body.extend(_model_rows(
        "Relations", rows(model.get("relations")),
        lambda row: relation_text(row) + _occurrences(row),
    ))
    body.extend(_model_rows(
        "Classifications", rows(model.get("classifications")),
        lambda row: classification_text(row) + _occurrences(row),
    ))
    body.extend(_model_rows(
        "Allowed literals", rows(model.get("allowed_literals")),
        lambda row: "`" + text(row.get("property"), "literal Property") + ": "
        + text(row.get("literal"), "literal value") + "`" + _occurrences(row),
    ))
    body.extend(_model_rows(
        "Selected Subject Expressions", rows(model.get("selected_subject_expressions")),
        lambda row: "`" + text(row.get("expression"), "Subject expression") + "`"
        + " — " + text(record(row.get("source")).get("atom_id"), "Subject source Atom"),
    ))
    body.extend(_model_rows(
        "Constraints", rows(graph.get("constraints")),
        lambda row: "`" + text(row.get("kind"), "constraint kind") + "`: `"
        + text(row.get("expression"), "constraint expression") + "`"
        + " — " + text(record(row.get("source")).get("atom_id"), "constraint source Atom"),
    ))
    body.extend(_model_rows(
        "Unsupported CFEL", rows(graph.get("cfel_diagnostics")),
        lambda row: "`" + text(row.get("code"), "CFEL diagnostic code") + "`: `"
        + _cfel_diagnostic_text(row) + "`"
        + (" — " + text(record(row.get("source")).get("atom_id"), "CFEL source Atom")
           if row.get("source") else ""),
    ))
    return "\n".join(body)
