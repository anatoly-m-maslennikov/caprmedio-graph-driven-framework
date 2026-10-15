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


def _header(provenance: Record, updated_at: str, source_selection: str) -> list[str]:
    frontmatter = yaml.safe_dump(
        {
            "artifact_form": "Projection",
            "type": "Entities Graph",
            "updated_at": text(updated_at, "updated_at"),
            "sources": _sources(provenance),
        },
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
        "Notation: / NARROWER_THAN; . IS_BORNE_BY; : IS_ALLOWED_VALUE_OF. "
        "Relations are traversed from broader to narrower, bearer to dependent, "
        "and property to allowed value.",
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
        if any(edge["kind"] == "IS_BORNE_BY" for _, edge in children[primary]):
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
    graph: Record, provenance: Record, *, updated_at: str, source_selection: str
) -> str:
    """Return deterministic Markdown; only the supplied rebuild time may vary."""
    graph = record(graph)
    nodes = read_nodes(rows(graph.get("nodes")))
    children, dependents, omitted, provisional = read_edges(rows(graph.get("edges")), nodes)
    main, appearances, cycles = primary_tree(nodes, children, set(nodes) - dependents)
    details, shown, detail_cycles = _details(appearances, nodes, children, dependents)
    body = _header(provenance, updated_at, source_selection)
    body.extend([*_fence(main), "", *details])
    body.extend(
        _limitations(graph, nodes, omitted, provisional, dependents - shown, cycles | detail_cycles)
    )
    return "\n".join(body)
