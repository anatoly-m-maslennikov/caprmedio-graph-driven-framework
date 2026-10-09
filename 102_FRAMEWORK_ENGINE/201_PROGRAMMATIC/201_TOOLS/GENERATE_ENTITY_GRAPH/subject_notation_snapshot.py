"""Create-only, diagnostic pre-migration snapshot of declared Core Subjects.

Full targets and qualification prefixes are source-supported display objects,
not native admission. Legacy separator steps remain UNCLASSIFIED. This utility
does not migrate sources, record a Run/Journal, or claim a completed graph Action.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import tomllib
from collections.abc import Mapping, Sequence
from dataclasses import dataclass
from pathlib import Path

import generate_entity_graph as graph
import graph_fact_context as facts
import subject_model_sources as subjects


_TOKEN = object()
_IMPLEMENTATION_PATH = Path(__file__).resolve()
_LOADED_IMPLEMENTATION_SHA256 = hashlib.sha256(_IMPLEMENTATION_PATH.read_bytes()).hexdigest()
_OUTPUT_DIRECTORY = ".caprmedio_caprmedio/_projection/core-subject-notation"
_OUTPUT_NAMES = ("before.graph.json", "before.graph.dot")


class SubjectNotationSnapshotError(ValueError):
    def __init__(self, code: str, *, created_paths: Sequence[str] = ()) -> None:
        self.code = code
        self.created_paths = tuple(created_paths)
        super().__init__(code)


def _digest(value: object) -> str:
    return hashlib.sha256(facts.canonical_bytes(value)).hexdigest()


def _check_code() -> None:
    subjects._check_code()
    try:
        if hashlib.sha256(_IMPLEMENTATION_PATH.read_bytes()).hexdigest() != _LOADED_IMPLEMENTATION_SHA256:
            raise SubjectNotationSnapshotError("profile-stale")
    except OSError as error:
        raise SubjectNotationSnapshotError("profile-stale") from error


@dataclass(frozen=True, slots=True, init=False)
class SubjectNotationSnapshot:
    _bytes: bytes
    _repository: Path
    _carriers: tuple
    _frontier_bytes: bytes
    _selection_bytes: bytes
    _frontmatter: tuple
    _token: object

    def __init__(self, data: bytes, repository: Path, carriers: tuple, frontier: bytes,
                 selection: bytes, frontmatter: tuple, *, _token: object = None) -> None:
        if _token is not _TOKEN:
            raise SubjectNotationSnapshotError("snapshot-untrusted")
        for key, value in (("_bytes", data), ("_repository", repository), ("_carriers", carriers),
                           ("_frontier_bytes", frontier), ("_selection_bytes", selection),
                           ("_frontmatter", frontmatter), ("_token", _token)):
            object.__setattr__(self, key, value)

    def as_dict(self) -> dict:
        _trusted(self)
        return json.loads(self._bytes)

    @property
    def snapshot_sha256(self) -> str:
        return self.as_dict()["snapshot_sha256"]

    def raw_frontmatter(self, atom_id: str) -> bytes:
        """Return immutable original-EOL frontmatter for a selected source."""
        _trusted(self)
        for source_id, raw in self._frontmatter:
            if source_id == atom_id:
                return raw
        raise SubjectNotationSnapshotError("snapshot-source-unselected")


def _trusted(snapshot: object) -> None:
    if type(snapshot) is not SubjectNotationSnapshot or getattr(snapshot, "_token", None) is not _TOKEN:
        raise SubjectNotationSnapshotError("snapshot-untrusted")


def _registration(repository: Path, frontier: Mapping | None = None) -> dict:
    control = graph._configured_control_root(repository)
    path = control / "project_structure.toml"
    relative = path.relative_to(repository).as_posix()
    path = facts._safe_path(repository, relative)
    try:
        raw = path.read_bytes()
        records = tomllib.loads(raw.decode("utf-8")).get("scope_units")
    except (OSError, UnicodeDecodeError, tomllib.TOMLDecodeError) as error:
        raise SubjectNotationSnapshotError("snapshot-core-registration-unavailable") from error
    core = [record for record in records if isinstance(record, dict) and record.get("scope_unit_name") == "CORE_META_MODEL"] if isinstance(records, list) else []
    if len(core) != 1 or not isinstance(core[0].get("authority_path"), str):
        raise SubjectNotationSnapshotError("snapshot-core-registration-ambiguous")
    authority_path = core[0]["authority_path"]
    facts._safe_path(repository, authority_path, folder=True)
    evidence = {"carrier_path": relative, "carrier_sha256": hashlib.sha256(raw).hexdigest(), "schema_version": 1}
    if frontier is not None and (frontier.get("project_structure") != evidence or frontier.get("selected_folder") != authority_path):
        raise SubjectNotationSnapshotError("snapshot-core-frontier-foreign")
    return {"scope_unit_name": "CORE_META_MODEL", "authority_path": authority_path, "source": evidence}


def _owned_active_selection(pool: dict) -> dict:
    ids = [atom_id for atom_id, (carrier, _, raw) in pool.items()
           if carrier.status == "Active" and facts._raw_parts(raw)[3].get("current_scope_unit") == "CORE_META_MODEL"]
    return {"atom_ids": sorted(ids), "scope_unit_names": ["CORE_META_MODEL"]}


def current_core_inputs(repository: Path) -> tuple[list, dict, dict]:
    """Seal current registered Core inputs before preparing a snapshot."""
    _check_code()
    repository = Path(repository).resolve()
    registration = _registration(repository)
    folder = repository / registration["authority_path"]
    carriers, diagnostics = graph.discover_atoms(repository, folder)
    if any(row.get("severity") == "error" for row in diagnostics):
        raise SubjectNotationSnapshotError("snapshot-core-discovery-incomplete")
    frontier = graph.source_frontier_for(repository, folder)
    pool = facts._pool(repository, carriers)
    return carriers, frontier, _owned_active_selection(pool)


def _lineage(row: dict) -> dict:
    return {"source_atom_id": row["source_ref"]["atom_id"], "subject_path": row["subject_path"],
            "role": row["role"], "source_ref": row["source_ref"]}


def _lineages(rows: list[dict]) -> list[dict]:
    unique = {facts.canonical_bytes(row): row for row in rows}
    return sorted(unique.values(), key=lambda row: (row["subject_path"], row["role"], facts._source_key(row["source_ref"])))


def _prefix_steps(path: str) -> list[tuple[str, str, str, str, str]]:
    """Retain literal source prefixes; do not interpret old separators."""
    positions = list(re.finditer(r"[/:]", path))
    steps = []
    for index, marker in enumerate(positions):
        previous_end = positions[index - 1].end() if index else 0
        target_end = positions[index + 1].start() if index + 1 < len(positions) else len(path)
        steps.append((path[:marker.start()], path[:target_end], marker.group(),
                      path[previous_end:marker.start()].strip(), path[marker.end():target_end].strip()))
    return steps


def prepare_subject_notation_snapshot(repository: Path, carriers: Sequence, source_frontier: Mapping,
                                      selection: Mapping) -> SubjectNotationSnapshot:
    """Read-only diagnostic snapshot of every exact-Active owned Core source."""
    _check_code()
    repository = Path(repository).resolve()
    pool = facts._pool(repository, carriers)
    selected = facts._selection(selection, set(pool))
    frontier = facts._frontier(repository, source_frontier, pool, selected)
    registration = _registration(repository, frontier)
    if selected != _owned_active_selection(pool):
        raise SubjectNotationSnapshotError("snapshot-selection-not-owned-active-core")
    authority = repository / registration["authority_path"]
    if any(not (repository / pin["carrier_path"]).is_relative_to(authority) for _, pin, _ in pool.values()):
        raise SubjectNotationSnapshotError("snapshot-source-outside-core")
    selected_carriers = [pool[atom_id][0] for atom_id in selected["atom_ids"]]
    extracted = subjects.collect_subject_model_sources(repository, selected_carriers).as_dict()
    nodes, steps, pairs, links = {}, {}, {}, []
    for row in extracted["occurrences"]:
        path, lineage = row["subject_path"], _lineage(row)
        node = nodes.setdefault(path, {"identity": path, "is_full_target": False,
                                       "is_qualification_prefix_support": False, "lineages": []})
        node["is_full_target"] = True
        node["lineages"].append(lineage)
        link = {"source_atom_id": lineage["source_atom_id"], "target_identity": path,
                "role": row["role"], "source_ref": row["source_ref"], "representation": "source_incidence"}
        link["link_id"] = "source-link:" + _digest(link)
        links.append(link)
        for source, target, separator, left, right in _prefix_steps(path):
            for prefix in (source, target):
                support = nodes.setdefault(prefix, {"identity": prefix, "is_full_target": False,
                                                   "is_qualification_prefix_support": False, "lineages": []})
                support["is_qualification_prefix_support"] = True
                support["lineages"].append(lineage)
            step = steps.setdefault((source, target, separator), {"source_identity": source, "target_identity": target,
                                      "separator": separator, "classification": "UNCLASSIFIED", "lineages": []})
            step["lineages"].append(lineage)
            pair = pairs.setdefault((separator, left, right), {"separator": separator, "left_component": left,
                                   "right_component": right, "classification": "UNCLASSIFIED", "contexts": [], "lineages": []})
            pair["contexts"].append({"source_identity": source, "target_identity": target})
            pair["lineages"].append(lineage)
    for node in nodes.values():
        node["lineages"] = _lineages(node["lineages"])
    for step in steps.values():
        step["lineages"] = _lineages(step["lineages"])
        step["step_id"] = "unclassified-step:" + _digest({key: value for key, value in step.items() if key != "lineages"})
    for pair in pairs.values():
        pair["lineages"] = _lineages(pair["lineages"])
        pair["contexts"] = sorted({facts.canonical_bytes(context): context for context in pair["contexts"]}.values(),
                                   key=lambda context: (context["source_identity"], context["target_identity"]))
    source_atoms, excluded, raw_frontmatter = [], [], []
    for atom_id in sorted(pool):
        carrier, pin, raw = pool[atom_id]
        lines, _, boundary, fields = facts._raw_parts(raw)
        if atom_id in selected["atom_ids"]:
            source_atoms.append({**pin, "content_role": carrier.content_role, "status": carrier.status,
                                 "current_scope_unit": fields["current_scope_unit"]})
            raw_frontmatter.append((atom_id, b"".join(lines[1:boundary])))
        else:
            excluded.append({**pin, "reason": "status-not-exact-Active" if carrier.status != "Active" else "owner-not-CORE_META_MODEL"})
    result = {"schema_version": 1, "snapshot_kind": "caprmedio.subject_notation.before", "diagnostic_only": True,
              "non_authoritative": True, "semantic_admission": "not_performed", "native_facts": [],
              "registration": registration, "selection": selected,
              "source_binding": {"source_frontier_sha256": frontier["source_frontier_sha256"],
                                 "selection_sha256": _digest(selected), "source_collection_sha256": extracted["collection_sha256"]},
              "provider": {"id": "caprmedio.subject-notation-snapshot", "version": "1",
                           "profile_sha256": _digest({"implementation_sha256": _LOADED_IMPLEMENTATION_SHA256,
                                                     "source_reader": extracted["provider"], "steps": "legacy-separators-UNCLASSIFIED"})},
              "source_atoms": source_atoms, "excluded_sources": excluded, "occurrences": extracted["occurrences"],
              "nodes": sorted(nodes.values(), key=lambda node: node["identity"]),
              "source_links": sorted(links, key=lambda link: link["link_id"]),
              "qualification_steps": sorted(steps.values(), key=lambda step: step["step_id"]),
              "pair_inventory": sorted(pairs.values(), key=lambda pair: (pair["separator"], pair["left_component"], pair["right_component"])),
              "coverage": extracted["coverage"], "diagnostics": extracted["diagnostics"],
              "unperformed": sorted(set(extracted["unperformed"] + ["separator_classification", "run_recording", "graph_action_completion"]))}
    result["counts"] = {"frontier_sources": len(pool), "selected_sources": len(source_atoms), "excluded_sources": len(excluded),
                        "occurrences": len(extracted["occurrences"]), "full_target_nodes": sum(node["is_full_target"] for node in nodes.values()),
                        "support_only_nodes": sum(not node["is_full_target"] for node in nodes.values()), "nodes": len(nodes),
                        "source_links": len(links), "unclassified_steps": len(steps), "component_pairs": len(pairs)}
    result["snapshot_sha256"] = _digest(result)
    _check_code()
    return SubjectNotationSnapshot(facts.canonical_bytes(result), repository, tuple(carriers), facts.canonical_bytes(frontier),
                                    facts.canonical_bytes(selected), tuple(raw_frontmatter), _token=_TOKEN)


def snapshot_dot(snapshot: SubjectNotationSnapshot) -> str:
    _trusted(snapshot)
    data = snapshot.as_dict()
    quote = lambda value: json.dumps(value, ensure_ascii=False)
    object_id = lambda identity: "object_" + hashlib.sha256(identity.encode("utf-8")).hexdigest()
    source_id = lambda identity: "source_" + hashlib.sha256(identity.encode("utf-8")).hexdigest()
    lines = ["digraph core_subject_notation_before {", "  rankdir=LR;",
             '  graph [label="Diagnostic before snapshot — old separators UNCLASSIFIED; no native admission", labelloc=t];',
             "  // snapshot_sha256: " + data["snapshot_sha256"]]
    for node in data["nodes"]:
        shape = "ellipse" if node["is_full_target"] else "plaintext"
        lines.append(f"  {object_id(node['identity'])} [label={quote(node['identity'])}, shape={shape}];")
    for source in data["source_atoms"]:
        lines.append(f"  {source_id(source['atom_id'])} [label={quote(source['atom_id'] + ' @' + str(source['atom_revision']) + ' (source Atom)')}, shape=box, color=gray];")
    for link in data["source_links"]:
        lines.append(f"  {source_id(link['source_atom_id'])} -> {object_id(link['target_identity'])} [label={quote('ATOM INCIDENCE ' + link['role'])}, style=dotted, color=steelblue];")
    for step in data["qualification_steps"]:
        lines.append(f"  {object_id(step['source_identity'])} -> {object_id(step['target_identity'])} [label={quote('UNCLASSIFIED ' + step['separator'])}, style=dashed, color=gray, tooltip={quote(step['step_id'])}];")
    return "\n".join([*lines, "}", ""])


def _verify_current(snapshot: SubjectNotationSnapshot) -> None:
    _trusted(snapshot)
    current = prepare_subject_notation_snapshot(snapshot._repository, snapshot._carriers,
                                               json.loads(snapshot._frontier_bytes), json.loads(snapshot._selection_bytes))
    if current._bytes != snapshot._bytes or current._frontmatter != snapshot._frontmatter:
        raise SubjectNotationSnapshotError("snapshot-source-stale")


def persist_subject_notation_snapshot(snapshot: SubjectNotationSnapshot) -> dict:
    """Explicitly publish the two fixed, create-only diagnostic artifacts."""
    _verify_current(snapshot)
    paths = [facts._safe_path(snapshot._repository, _OUTPUT_DIRECTORY + "/" + name) for name in _OUTPUT_NAMES]
    if any(path.exists() or path.is_symlink() for path in paths):
        raise SubjectNotationSnapshotError("snapshot-output-exists")
    payloads = [json.dumps(snapshot.as_dict(), ensure_ascii=False, sort_keys=True, indent=2).encode("utf-8") + b"\n",
                snapshot_dot(snapshot).encode("utf-8")]
    paths[0].parent.mkdir(parents=True, exist_ok=True)
    # Revalidate canonical paths after directory creation, before exclusive opens.
    for path in paths:
        facts._safe_path(snapshot._repository, path.relative_to(snapshot._repository).as_posix())
    created = []
    try:
        for path, payload in zip(paths, payloads):
            handle = path.open("xb")
            created.append(path.relative_to(snapshot._repository).as_posix())
            with handle:
                handle.write(payload)
    except OSError as error:
        # Do not erase a produced artifact or conceal partial publication.
        raise SubjectNotationSnapshotError("snapshot-publication-incomplete", created_paths=created) from error
    return {"outcome": "diagnostic_snapshot_created", "snapshot_sha256": snapshot.snapshot_sha256,
            "outputs": [{"path": path.relative_to(snapshot._repository).as_posix(), "sha256": hashlib.sha256(payload).hexdigest()}
                        for path, payload in zip(paths, payloads)], "run_recording": "not_performed"}


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repository", type=Path, default=Path.cwd())
    parser.add_argument("--persist", action="store_true", help="Create the two diagnostic before.graph files; never overwrite")
    args = parser.parse_args(argv)
    try:
        carriers, frontier, selection = current_core_inputs(args.repository)
        snapshot = prepare_subject_notation_snapshot(args.repository, carriers, frontier, selection)
        result = {"outcome": "dry_run", "snapshot_sha256": snapshot.snapshot_sha256,
                  "counts": snapshot.as_dict()["counts"], "coverage": snapshot.as_dict()["coverage"],
                  "output_paths": [_OUTPUT_DIRECTORY + "/" + name for name in _OUTPUT_NAMES]}
        if args.persist:
            result.update(persist_subject_notation_snapshot(snapshot))
        print(json.dumps(result, ensure_ascii=False, sort_keys=True))
        return 0
    except (SubjectNotationSnapshotError, facts.FactContextError, subjects.SubjectModelSourceError, graph.EntityGraphError) as error:
        print(json.dumps({"outcome": "snapshot_unavailable", "code": error.code,
                          "created_paths": list(getattr(error, "created_paths", ())), "run_recording": "not_performed"}, sort_keys=True))
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
