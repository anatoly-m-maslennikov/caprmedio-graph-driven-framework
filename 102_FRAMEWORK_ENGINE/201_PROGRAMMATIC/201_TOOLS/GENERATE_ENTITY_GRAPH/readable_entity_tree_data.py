"""Pure validation and traversal of supplied typed Subject graph records."""

import math
from collections import Counter
from typing import Any, cast

Record = dict[str, Any]
Nodes = dict[str, Record]
Children = dict[str, list[tuple[str, Record]]]
LABELS = {"NARROWER_THAN": "/", "IS_BORNE_BY": ".", "IS_ALLOWED_VALUE_OF": ":"}


def record(value: object) -> Record:
    if not isinstance(value, dict):
        raise ValueError("Expected a graph or provenance object")
    return cast(Record, value)


def rows(value: object) -> list[Record]:
    if not isinstance(value, list):
        raise ValueError("Expected graph or provenance rows")
    return [record(item) for item in value]


def text(value: object, field: str) -> str:
    if not isinstance(value, str) or not value.strip() or any(c in value for c in "\n\r\t"):
        raise ValueError(f"Invalid {field}")
    return value


def order(row: Record) -> tuple[int, float]:
    value = row.get("ordinal_position")
    if value is None:
        return (1, 0)
    if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value):
        raise ValueError("Invalid ordinal_position")
    return (0, value)


def name_key(nodes: Nodes, key: str) -> tuple[str, str, str]:
    node = nodes[key]
    return (cast(str, node.get("display_name", node["identity"])), node["identity"], key)


def read_nodes(rows: list[Record]) -> Nodes:
    nodes: Nodes = {}
    for node in rows:
        identity = text(node.get("identity"), "node identity")
        key = text(node.get("id"), "node ID")
        if key in nodes:
            raise ValueError("Duplicate node ID")
        order(node)
        if "display_name" in node:
            text(node["display_name"], "display name")
        nodes[key] = {**node, "identity": identity}
    return nodes


def _endpoints(edge: Record, nodes: Nodes) -> tuple[str, str]:
    child, parent = edge.get("relation_source"), edge.get("relation_target")
    if (
        not isinstance(child, str)
        or not isinstance(parent, str)
        or child not in nodes
        or parent not in nodes
    ):
        raise ValueError("Missing relation endpoint")
    return child, parent


def read_edges(rows: list[Record], nodes: Nodes) -> tuple[Children, set[str], Counter[str], bool]:
    children: Children = {key: [] for key in nodes}
    dependents: set[str] = set()
    omitted: Counter[str] = Counter()
    provisional = False
    for edge in rows:
        child, parent = _endpoints(edge, nodes)
        kind = text(edge.get("kind"), "relation kind")
        order(edge)
        provisional |= edge.get("disposition") == "provisional_notation"
        if kind not in LABELS:
            omitted[kind] += 1
            continue
        children[parent].append((child, edge))
        if kind == "IS_BORNE_BY":
            dependents.add(child)
    for edges in children.values():
        edges.sort(key=lambda pair: (*order(pair[1]), *name_key(nodes, pair[0]), pair[1]["kind"]))
    return children, _descendants(dependents, children), omitted, provisional


def _descendants(roots: set[str], children: Children) -> set[str]:
    found, pending = set(roots), list(roots)
    while pending:
        for child, _ in children[pending.pop()]:
            if child not in found:
                found.add(child)
                pending.append(child)
    return found


def tree(
    start: str, allowed: set[str], nodes: Nodes, children: Children
) -> tuple[list[str], list[str], set[str]]:
    lines: list[str] = []
    appearances: list[str] = []
    cycles: set[str] = set()
    stack: list[tuple[str, int, str, frozenset[str]]] = [(start, 0, "", frozenset())]
    while stack:
        key, depth, label, path = stack.pop()
        cyclic = key in path
        lines.append("\t" * depth + label + nodes[key]["identity"] + (" [cycle]" if cyclic else ""))
        if cyclic:
            cycles.add(key)
            continue
        appearances.append(key)
        next_path = path | {key}
        stack.extend(
            (child, depth + 1, LABELS[edge["kind"]] + " ", next_path)
            for child, edge in reversed(children[key])
            if child in allowed
        )
    return lines, appearances, cycles


def primary_tree(
    nodes: Nodes, children: Children, primaries: set[str]
) -> tuple[list[str], list[str], set[str]]:
    parents = {child for parent in primaries for child, _ in children[parent] if child in primaries}

    def root_key(key: str) -> tuple[int, float, str, str, str]:
        return (*order(nodes[key]), *name_key(nodes, key))

    roots = sorted(primaries - parents, key=root_key)
    main: list[str] = []
    appearances: dict[str, None] = {}
    cycles: set[str] = set()
    # Rootless cyclic components still need a visible traversal entry.
    for root in roots + sorted(primaries, key=root_key):
        if root not in appearances:
            lines, visited, found_cycles = tree(root, primaries, nodes, children)
            main.extend(lines)
            appearances.update(dict.fromkeys(visited))
            cycles.update(found_cycles)
    return main, list(appearances), cycles
