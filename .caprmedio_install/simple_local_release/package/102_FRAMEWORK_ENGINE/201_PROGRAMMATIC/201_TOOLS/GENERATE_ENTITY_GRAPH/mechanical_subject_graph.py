"""Step 1 only: declared syntax projection of existing Core '/' and ':'.

This thin snapshot wrapper preserves full literal target/prefix identities.
Slash is UNCLASSIFIED pending content classification; colon depicts a possible
allowed value, never assignment. No dot grammar, migration or native admission.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from collections.abc import Mapping, Sequence
from pathlib import Path

import generate_entity_graph as graph
import graph_fact_context as facts
import subject_model_sources as subjects
import subject_notation_snapshot as snapshot


_IMPLEMENTATION_PATH = Path(__file__).resolve()
_LOADED_IMPLEMENTATION_SHA256 = hashlib.sha256(_IMPLEMENTATION_PATH.read_bytes()).hexdigest()
_OUTPUT_DIRECTORY = ".caprmedio_caprmedio/_projection/core-subject-notation"
_OUTPUT_NAMES = ("step1.graph.json", "step1.entities.graph.dot", "step1.terms.graph.dot")


class MechanicalSubjectGraphError(ValueError):
    def __init__(self, code: str, *, created_paths: Sequence[str] = ()) -> None:
        self.code = code
        self.created_paths = tuple(created_paths)
        super().__init__(code)


def _digest(value: object) -> str:
    return hashlib.sha256(facts.canonical_bytes(value)).hexdigest()


def _check_code() -> None:
    snapshot._check_code()
    try:
        if hashlib.sha256(_IMPLEMENTATION_PATH.read_bytes()).hexdigest() != _LOADED_IMPLEMENTATION_SHA256:
            raise MechanicalSubjectGraphError("profile-stale")
    except OSError as error:
        raise MechanicalSubjectGraphError("profile-stale") from error


def _occurrence_key(row: Mapping) -> bytes:
    return facts.canonical_bytes({key: row[key] for key in ("subject_path", "role", "source_ref")})


def _fingerprint(module, digest: str) -> dict:
    return {"module": module.__name__, "loaded_path": Path(module.__file__).resolve().as_posix(), "sha256": digest}


def parse_subject_expression(path: str) -> dict:
    """Expose existing literal prefix syntax, without interpreting slash."""
    if not isinstance(path, str):
        raise MechanicalSubjectGraphError("subject-expression-invalid")
    graph._subject_parts(path)
    steps = snapshot._prefix_steps(path)
    prefixes = [steps[0][0], *[step[1] for step in steps]] if steps else [path]
    slash = [{"source": source, "target": target, "classification": "UNCLASSIFIED"}
             for source, target, separator, _, _ in steps if separator == "/"]
    values = [{"source": target, "target": source} for source, target, separator, _, _ in steps if separator == ":"]
    return {"source_expression": path, "literal_prefixes": prefixes, "separators": [step[2] for step in steps],
            "slash_steps": slash, "value_links": values, "value_link": values[-1] if values else None}


def build_mechanical_subject_graph(repository: Path) -> dict:
    """Read current registered Core through the existing trusted snapshot."""
    _check_code()
    repository = Path(repository).resolve()
    carriers, frontier, selection = snapshot.current_core_inputs(repository)
    before = snapshot.prepare_subject_notation_snapshot(repository, carriers, frontier, selection).as_dict()
    if before["coverage"]["disposition"] != "complete":
        raise MechanicalSubjectGraphError("mechanical-source-extraction-incomplete")
    occurrences = [{"occurrence_id": index, **row} for index, row in enumerate(before["occurrences"])]
    by_occurrence = {_occurrence_key(row): row["occurrence_id"] for row in occurrences}

    def occurrence_ids(lineages):
        return sorted({by_occurrence[_occurrence_key(row)] for row in lineages})

    entity_nodes = [{key: node[key] for key in ("identity", "is_full_target", "is_qualification_prefix_support")}
                    | {"occurrence_ids": occurrence_ids(node["lineages"])} for node in before["nodes"]]
    entity_edges = []
    for step in before["qualification_steps"]:
        separator = step["separator"]
        if separator == "/":
            kind, source, target = "UNCLASSIFIED", step["source_identity"], step["target_identity"]
        elif separator == ":":
            kind, source, target = "IS_ALLOWED_VALUE_OF", step["target_identity"], step["source_identity"]
        else:
            raise MechanicalSubjectGraphError("step1-separator-unsupported")
        edge = {"kind": kind, "source_identity": source, "target_identity": target,
                "source_separator": separator, "occurrence_ids": occurrence_ids(step["lineages"])}
        edge["edge_id"] = "syntax-edge:" + _digest({key: value for key, value in edge.items() if key != "occurrence_ids"})
        entity_edges.append(edge)
    entity_edges.sort(key=lambda edge: edge["edge_id"])
    component_occurrences = {}
    for row in occurrences:
        # Existing Subject parsing only; a dot remains part of a literal name.
        for component, _ in graph._subject_parts(row["subject_path"]):
            component_occurrences.setdefault(component, set()).add(row["occurrence_id"])
    terms = [{"identity": name, "occurrence_ids": sorted(ids)} for name, ids in sorted(component_occurrences.items())]
    source_links = [{"source_atom_id": link["source_atom_id"], "target_identity": link["target_identity"],
                     "occurrence_id": by_occurrence[_occurrence_key({"subject_path": link["target_identity"],
                                                                    "role": link["role"], "source_ref": link["source_ref"]})]}
                    for link in before["source_links"]]
    source_links.sort(key=lambda row: row["occurrence_id"])
    interpretation = {"/": "UNCLASSIFIED_pending_step2", ":": "possible_allowed_value_to_immediate_property_prefix_not_assignment"}
    profile = {"implementation": {"loaded_path": _IMPLEMENTATION_PATH.as_posix(), "sha256": _LOADED_IMPLEMENTATION_SHA256},
               "snapshot": _fingerprint(snapshot, snapshot._LOADED_IMPLEMENTATION_SHA256),
               "source_reader": _fingerprint(subjects, subjects._LOADED_IMPLEMENTATION_SHA256),
               "subject_parser": _fingerprint(graph, subjects._LOADED_PARSER_SHA256),
               "fact_context": _fingerprint(facts, facts._LOADED_IMPLEMENTATION_SHA256),
               "source_snapshot_provider": before["provider"], "operator_interpretation": interpretation}
    result = {"schema_version": 1, "projection_kind": "caprmedio.mechanical_subject_graph.step1",
              "diagnostic_only": True, "non_authoritative": True, "native_admission": "not_performed",
              "semantic_admission": "not_performed", "native_facts": [],
              "source_migration": "not_performed", "content_classification": "not_performed",
              "operator_interpretation": interpretation,
              "producer": {"id": "caprmedio.mechanical-subject-graph", "version": "1",
                           "profile_payload": profile, "profile_sha256": _digest(profile)},
              "registration": before["registration"], "selection": before["selection"],
              "source_frontier_evidence": {"source_frontier_sha256": frontier["source_frontier_sha256"],
                                            "selected_folder": frontier["selected_folder"], "project_structure": frontier["project_structure"]},
              "source_binding": before["source_binding"], "source_atoms": before["source_atoms"],
              "excluded_sources": before["excluded_sources"], "occurrences": occurrences, "source_links": source_links,
              "entities_graph": {"nodes": entity_nodes, "edges": entity_edges},
              "terms_graph": {"nodes": terms, "edges": []},
              "coverage": before["coverage"], "diagnostics": before["diagnostics"],
              "counts": {"frontier_sources": before["counts"]["frontier_sources"], "selected_sources": len(before["source_atoms"]),
                         "excluded_sources": len(before["excluded_sources"]), "occurrences": len(occurrences),
                         "entity_nodes": len(entity_nodes), "unclassified_slash_edges": sum(edge["kind"] == "UNCLASSIFIED" for edge in entity_edges),
                         "allowed_value_edges": sum(edge["kind"] == "IS_ALLOWED_VALUE_OF" for edge in entity_edges),
                         "term_nodes": len(terms), "term_edges": 0}}
    result["graph_sha256"] = _digest(result)
    _check_code()
    return result


def graph_dot(data: Mapping, graph_kind: str = "entities") -> str:
    """Render only model display nodes/edges; Source Atoms stay separate."""
    if graph_kind not in {"entities", "terms"}:
        raise MechanicalSubjectGraphError("graph-kind-invalid")
    model = data[graph_kind + "_graph"]
    quote = lambda value: json.dumps(value, ensure_ascii=False)
    node_id = lambda identity: "node_" + hashlib.sha256(identity.encode("utf-8")).hexdigest()
    lines = ["digraph mechanical_subject_" + graph_kind + " {", "  rankdir=LR;",
             "  graph [label=" + quote("Step 1 declared syntax — no native admission; source migration not performed") + ", labelloc=t];",
             "  // graph_sha256: " + data["graph_sha256"]]
    for node in model["nodes"]:
        lines.append(f"  {node_id(node['identity'])} [label={quote(node['identity'])}];")
    for edge in model["edges"]:
        style = "dashed" if edge["kind"] == "UNCLASSIFIED" else "solid"
        lines.append(f"  {node_id(edge['source_identity'])} -> {node_id(edge['target_identity'])} [label={quote(edge['kind'])}, style={style}];")
    return "\n".join([*lines, "}", ""])


def persist_mechanical_subject_graph(repository: Path, data: Mapping) -> dict:
    """Rebuild current evidence before create-only Step 1 publication."""
    current = build_mechanical_subject_graph(repository)
    if facts.canonical_bytes(data) != facts.canonical_bytes(current):
        raise MechanicalSubjectGraphError("mechanical-graph-stale")
    repository = Path(repository).resolve()
    paths = [facts._safe_path(repository, _OUTPUT_DIRECTORY + "/" + name) for name in _OUTPUT_NAMES]
    if any(path.exists() or path.is_symlink() for path in paths):
        raise MechanicalSubjectGraphError("mechanical-output-exists")
    payloads = [json.dumps(current, ensure_ascii=False, sort_keys=True, indent=2).encode("utf-8") + b"\n",
                graph_dot(current, "entities").encode("utf-8"), graph_dot(current, "terms").encode("utf-8")]
    paths[0].parent.mkdir(parents=True, exist_ok=True)
    for path in paths:
        facts._safe_path(repository, path.relative_to(repository).as_posix())
    created = []
    try:
        for path, payload in zip(paths, payloads):
            handle = path.open("xb")
            created.append(path.relative_to(repository).as_posix())
            with handle:
                handle.write(payload)
    except OSError as error:
        raise MechanicalSubjectGraphError("mechanical-publication-incomplete", created_paths=created) from error
    return {"outcome": "declared_syntax_projection_created", "graph_sha256": current["graph_sha256"],
            "outputs": [{"path": path.relative_to(repository).as_posix(), "sha256": hashlib.sha256(payload).hexdigest()}
                        for path, payload in zip(paths, payloads)], "run_recording": "not_performed"}


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repository", type=Path, default=Path.cwd())
    parser.add_argument("--persist", action="store_true", help="Create fixed Step 1 files only; never overwrite")
    args = parser.parse_args(argv)
    try:
        data = build_mechanical_subject_graph(args.repository)
        result = {"outcome": "dry_run", "graph_sha256": data["graph_sha256"], "counts": data["counts"],
                  "coverage": data["coverage"], "source_migration": "not_performed", "content_classification": "not_performed"}
        if args.persist:
            result.update(persist_mechanical_subject_graph(args.repository, data))
        print(json.dumps(result, ensure_ascii=False, sort_keys=True))
        return 0
    except (MechanicalSubjectGraphError, snapshot.SubjectNotationSnapshotError, subjects.SubjectModelSourceError,
            facts.FactContextError, graph.EntityGraphError) as error:
        print(json.dumps({"outcome": "mechanical_projection_unavailable", "code": error.code,
                          "created_paths": list(getattr(error, "created_paths", ()))}, sort_keys=True))
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
