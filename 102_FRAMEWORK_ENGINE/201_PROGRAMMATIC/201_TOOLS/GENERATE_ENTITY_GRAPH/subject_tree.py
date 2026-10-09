"""Plain-text tree view of the step-1 literal Subject graph; no inference."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import graph_fact_context as facts
import mechanical_subject_graph as mechanical


PROJECTION_DIRECTORY = ".caprmedio_caprmedio/_projection/core-subject-notation"


def entity_tree(data: dict, root: str | None = None) -> str:
    """Display literal prefixes, reversing value links for tree navigation only."""
    model = data["entities_graph"]
    identities = [node["identity"] for node in model["nodes"]]
    nodes = set(identities)
    if len(nodes) != len(identities) or any(not isinstance(name, str) or "\n" in name or "\r" in name for name in nodes):
        raise ValueError("tree-node-invalid")
    children = {name: set() for name in nodes}
    parents = {}
    for edge in model["edges"]:
        separator = edge["source_separator"]
        if separator == "/":
            parent, child = edge["source_identity"], edge["target_identity"]
        elif separator == ":":
            parent, child = edge["target_identity"], edge["source_identity"]
        else:
            raise ValueError("tree-separator-unsupported")
        if parent not in nodes or child not in nodes or not child.startswith(parent + separator) or len(child) <= len(parent) + 1:
            raise ValueError("tree-prefix-edge-invalid")
        if child in parents and parents[child] != parent:
            raise ValueError("tree-multiple-parents")
        parents[child] = parent
        children[parent].add(child)
    roots = sorted(nodes - parents.keys()) if root is None else [root]
    if root is not None and root not in nodes:
        raise ValueError("tree-root-unavailable")
    lines = []

    def walk(parent: str, indent: str) -> None:
        ordered = sorted(children[parent])
        for index, child in enumerate(ordered):
            last = index == len(ordered) - 1
            # Keep the literal separator visible; indentation is not taxonomy.
            lines.append(indent + ("└── " if last else "├── ") + child[len(parent):])
            walk(child, indent + ("    " if last else "│   "))

    for index, name in enumerate(roots):
        if index:
            lines.append("")
        lines.append(name)
        walk(name, "")
    return "\n".join(lines) + "\n"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repository", type=Path, default=Path.cwd())
    parser.add_argument("--root", help="Print one existing branch instead of the full forest")
    parser.add_argument("--persist", action="store_true", help="Create the fixed full tree file; never overwrite")
    args = parser.parse_args(argv)
    if args.persist and args.root is not None:
        parser.error("--persist publishes the full tree only")
    repository = args.repository.resolve()
    source = facts._safe_path(repository, PROJECTION_DIRECTORY + "/step1.graph.json")
    saved = json.loads(source.read_text(encoding="utf-8"))
    current = mechanical.build_mechanical_subject_graph(repository)
    if saved != current:
        raise ValueError("tree-source-graph-stale")
    tree = entity_tree(current, args.root)
    if args.persist:
        destination = facts._safe_path(repository, PROJECTION_DIRECTORY + "/step1.entities.tree.txt")
        header = ("Core Subjects — step 1, derived tree view\n"
                  "Source graph SHA-256: " + current["graph_sha256"] + "\n"
                  "Indentation follows literal prefixes. / remains unclassified; : marks allowed values.\n"
                  "Separate roots are not connected by invented relations.\n\n")
        with destination.open("x", encoding="utf-8", newline="\n") as handle:
            handle.write(header + tree)
        print(json.dumps({"outcome": "tree_created", "path": destination.relative_to(repository).as_posix(),
                          "entity_nodes": current["counts"]["entity_nodes"], "source_graph_sha256": current["graph_sha256"]}))
    else:
        print(tree, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
