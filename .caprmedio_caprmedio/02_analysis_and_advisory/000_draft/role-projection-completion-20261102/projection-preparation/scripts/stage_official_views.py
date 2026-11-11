#!/usr/bin/env python3
"""Stage CA-PROJ-014..019 from one pinned frontier; never publish them.

The output directory is deliberately confined to this preparation packet.
It verifies every selected Current carrier against the supplied frontier,
records the six live-projection predecessors, and leaves those projections
untouched.  Root performs any later official write, journal, commit, and push.
"""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[6]
PREP = Path(__file__).resolve().parents[1]
PROJECTIONS = ROOT / ".caprmedio_caprmedio/_projection"
TOOLS = ROOT / "LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_TOOLS"
if not (TOOLS / "subject_notation.py").is_file():
    TOOLS = ROOT / "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS"
sys.path[:0] = [str(TOOLS / "GENERATE_ENTITY_GRAPH"), str(TOOLS)]

from artifact_metadata import current_timestamp  # noqa: E402
from contract_graph import compose_contract_graph, render_contract_graph  # noqa: E402
from current_entity_sources import _read_atom, current_model_carriers  # noqa: E402
from current_subject_graph import compose_enhanced_current_graph, compose_narrowing_graph, subject_facts  # noqa: E402
from readable_entity_tree import render_inherency, render_model  # noqa: E402
from subject_inventory_views import (  # noqa: E402
    VIEW_SPECS, _frontmatter, _instances_document, _primary_document, _property_document,
)
from subject_notation import (  # noqa: E402
    Name, RelationChain, SubjectNotationError, namespace_local_expression, parse_subject_expression,
)

IDS = tuple(f"CA-PROJ-0{number}" for number in range(14, 20))
NAMES = {
    "CA-PROJ-014": "CA-PROJ-014-CAPRMEDIO--Subject-Graph-Primary-Subjects--Current-Methodology-and-Project-RMED.md",
    "CA-PROJ-015": "CA-PROJ-015-CAPRMEDIO--Subject-Graph-Properties--Current-Methodology-and-Project-RMED.md",
    "CA-PROJ-016": "CA-PROJ-016-CAPRMEDIO--Subject-Graph-Instances--Current-Methodology-and-Project-RMED.md",
    "CA-PROJ-017": "CA-PROJ-017-CAPRMEDIO--Model-Graph--Current-MODEL-Declarations.md",
    "CA-PROJ-018": "CA-PROJ-018-CAPRMEDIO--Entities-Graph--Current-Subject-Narrowing-Tree.md",
    "CA-PROJ-019": "CA-PROJ-019-CAPRMEDIO--MODEL-Formal-Contracts.md",
}


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def read_frontier(path: Path) -> tuple[list[dict], str]:
    raw = path.read_bytes()
    payload = json.loads(raw)
    operations = payload.get("operations")
    if not isinstance(operations, list) or not operations:
        raise ValueError("Frontier has no operations")
    seen = set()
    for row in operations:
        if not isinstance(row, dict):
            raise ValueError("Frontier operation is not an object")
        required = ("base_id", "version", "destination_path", "sha256", "status")
        if any(not row.get(key) for key in required):
            raise ValueError(f"Incomplete frontier row: {row!r}")
        if row["base_id"] in seen:
            raise ValueError(f"Duplicate frontier id: {row['base_id']}")
        seen.add(row["base_id"])
    return operations, digest(raw)


def relocated_index() -> dict[str, list[Path]]:
    """Index only the active CA #8 source tree by bytes for move-safe review."""
    root = ROOT / ".caprmedio_caprmedio/000_CAPRMEDIO_framework/sources"
    index: dict[str, list[Path]] = {}
    for path in root.rglob("*.md"):
        if "archive" not in path.parts:
            index.setdefault(digest(path.read_bytes()), []).append(path)
    return index


def carriers_from_frontier(rows: list[dict]) -> tuple[list[dict], list[dict]]:
    carriers = []
    relocations = []
    fallback = None
    for row in rows:
        path = ROOT / row["destination_path"]
        if not path.is_file():
            fallback = fallback or relocated_index()
            matches = fallback.get(row["sha256"], [])
            if len(matches) != 1:
                raise ValueError(f"Missing or ambiguous moved frontier carrier: {row['base_id']}")
            path = matches[0]
            relocations.append({"base_id": row["base_id"], "frontier_path": row["destination_path"],
                                "resolved_current_path": str(path.relative_to(ROOT))})
        raw = path.read_bytes()
        if digest(raw) != row["sha256"]:
            raise ValueError(f"Frontier hash drift: {row['base_id']}")
        carrier = _read_atom(path, ROOT)
        if carrier is None:
            raise ValueError(f"Unreadable Current carrier: {row['base_id']}")
        source = carrier["source"]
        if (source["atom_id"], source["version"], source["sha256"]) != (
            row["base_id"], row["version"], row["sha256"]
        ):
            raise ValueError(f"Carrier metadata drift: {row['base_id']}")
        if carrier["metadata"].get("status") != row["status"]:
            raise ValueError(f"Carrier status drift: {row['base_id']}")
        if carrier["read_view"].get("content_role") not in {"Requirement", "Method", "Evaluation", "Delivery"}:
            raise ValueError(f"Non-RMED frontier member: {row['base_id']}")
        carrier["source"] = {**carrier["source"], "path": str(path.relative_to(ROOT))}
        carriers.append(carrier)
    return carriers, relocations


def overlay_publication_candidates(carriers: list[dict], plan_path: Path) -> tuple[list[dict], dict]:
    """Replace ten DTOs in memory with plan-pinned Active candidate bytes."""
    raw = plan_path.read_bytes()
    plan = json.loads(raw)
    if plan.get("status") != "PASS":
        raise ValueError("Overlay publication plan is not PASS")
    operations = [row for row in plan.get("operations", []) if row.get("kind") == "publish"]
    if len(operations) != 10 or len({row.get("base_id") for row in operations}) != 10:
        raise ValueError("Expected exactly ten unique publish candidates")
    by_id = {carrier["source"]["atom_id"]: carrier for carrier in carriers}
    if len(by_id) != len(carriers):
        raise ValueError("Frontier has duplicate source IDs")
    overlay = []
    evidence = []
    for row in operations:
        base_id = row["base_id"]
        incumbent = by_id.get(base_id)
        if incumbent is None:
            raise ValueError(f"Overlay source absent from frontier: {base_id}")
        if incumbent["source"]["sha256"] != row["source_sha256"]:
            raise ValueError(f"Overlay predecessor drift: {base_id}")
        candidate_path = ROOT / row["candidate_path"]
        candidate = _read_atom(candidate_path, ROOT)
        if candidate is None or digest(candidate_path.read_bytes()) != row["candidate_sha256"]:
            raise ValueError(f"Overlay candidate is unreadable or hash-drifted: {base_id}")
        if candidate["metadata"].get("status") != "Active":
            raise ValueError(f"Overlay candidate is not Active: {base_id}")
        candidate = copy.deepcopy(candidate)
        candidate["source"] = {
            "atom_id": base_id,
            "version": row["version"],
            "path": row["destination_path"],
            "sha256": row["candidate_sha256"],
        }
        by_id[base_id] = candidate
        evidence.append({"base_id": base_id, "candidate_path": row["candidate_path"],
                         "destination_path": row["destination_path"], "version": row["version"],
                         "sha256": row["candidate_sha256"]})
    for carrier in carriers:
        overlay.append(by_id[carrier["source"]["atom_id"]])
    return overlay, {"path": str(plan_path.relative_to(ROOT)), "sha256": digest(raw), "candidates": evidence}


def existing_predecessors() -> dict[str, dict]:
    result = {}
    for identifier, name in NAMES.items():
        path = PROJECTIONS / name
        raw = path.read_bytes()
        header = yaml.safe_load(raw.decode("utf-8").split("---\n", 2)[1])
        if header.get("projection_id") != identifier or "version" in header:
            raise ValueError(f"Invalid live predecessor: {identifier}")
        result[identifier] = {"path": str(path.relative_to(ROOT)), "sha256": digest(raw)}
    return result


def aspect_containment_rows(provenance: dict) -> list[str]:
    """Render source-bound direct facts; never promote them to MODEL Nodes."""
    rows = set()
    for occurrence in provenance["occurrences"]:
        subject = occurrence["subject"]
        try:
            expression = parse_subject_expression(subject, subject_profile="approved").expression
        except SubjectNotationError:
            # compose_enhanced_current_graph already records this source diagnostic.
            continue
        local = namespace_local_expression(expression)
        path = local.endpoints[0] if isinstance(local, RelationChain) else local
        if not (local is not None and isinstance(path.head, Name) and path.head.value == "Aspects"):
            continue
        source = occurrence["source"]
        binding = f"{source['atom_id']}@{source['version']}"
        _, facts, _ = subject_facts(subject)
        for fact in facts:
            if fact["kind"] == "IS_CONTAINED_BY":
                rows.add(f"{fact['source']} IS_CONTAINED_BY {fact['target']} [{binding}]")
    if not rows:
        raise ValueError("No bare Aspect containment chains found; source migration is not ready")
    return sorted(rows, key=str.casefold)


def namespace_context(graph: dict) -> str:
    """Render only explicit direct containment branches rooted at CAPRMEDIO."""
    nodes = {row["id"]: row["identity"] for row in graph["nodes"]}
    branches = sorted(
        nodes[edge["relation_source"]]
        for edge in graph["edges"]
        if edge["kind"] == "IS_CONTAINED_BY"
        and nodes[edge["relation_target"]] == "CAPRMEDIO"
    )
    if not branches:
        return ""
    return "## Namespace context\n\n```text\nCAPRMEDIO\n" + "\n".join(f"  <+ {branch}" for branch in branches) + "\n```\n"


def insert_namespace_context(document: str, graph: dict) -> str:
    section = namespace_context(graph)
    if not section:
        return document
    marker = next(line for line in document.splitlines(keepends=True) if line.startswith("#"))
    return document.replace(marker, marker + "\n" + section + "\n", 1)


def render(carriers: list[dict], now: str) -> tuple[dict[str, str], dict]:
    expected = sorted(f"{c['source']['atom_id']}@{c['source']['version']}" for c in carriers)
    if len(expected) != len(set(expected)):
        raise ValueError("Source Atom bindings are not unique")
    observed, observed_provenance = compose_enhanced_current_graph(carriers)
    headers = {identifier: _frontmatter(identifier, selection, expected, now) for identifier, selection in VIEW_SPECS}
    docs = {
        "CA-PROJ-014": _primary_document(headers["CA-PROJ-014"], observed["model"], observed["diagnostics"]),
        "CA-PROJ-015": _property_document(headers["CA-PROJ-015"], observed["model"]),
        "CA-PROJ-016": _instances_document(headers["CA-PROJ-016"], observed["model"], observed["constraints"]),
    }
    direct_aspect_facts = aspect_containment_rows(observed_provenance)
    docs["CA-PROJ-014"] = docs["CA-PROJ-014"].rstrip() + "\n\n## Aspect containment facts\n\n```text\n" + "\n".join(direct_aspect_facts) + "\n```\n"
    docs["CA-PROJ-014"] = insert_namespace_context(docs["CA-PROJ-014"], observed)
    model_sources = current_model_carriers(carriers)
    model, model_provenance = compose_enhanced_current_graph(model_sources)
    docs["CA-PROJ-017"] = render_model(model, model_provenance, updated_at=now,
        source_selection="Current model Declarations, including canonical and derived Relations; source-bound extraction without executing CFEL.",
        projection_identity={"projection_id": "CA-PROJ-017", "named_selection": "Current Declared MODEL"})
    docs["CA-PROJ-017"] = insert_namespace_context(docs["CA-PROJ-017"], model)
    tree, tree_provenance = compose_narrowing_graph(carriers)
    if tree["diagnostics"] or any(edge["kind"] != "NARROWER_THAN" for edge in tree["edges"]):
        raise ValueError("Narrowing tree is not node-only")
    display = copy.deepcopy(tree)
    for node in display["nodes"]:
        node["display_name"] += " [" + ", ".join(node["source_bindings"]) + "]"
    docs["CA-PROJ-018"] = render_inherency(display, tree_provenance, updated_at=now,
        source_selection="Current model Declarations and retained CFEL/Carrier/Term Definitions. Only NARROWER_THAN forms this tree; CONTAINS is not rendered as narrowing.",
        projection_identity={"projection_id": "CA-PROJ-018", "named_selection": "Current Subject Narrowing Tree"})
    contract = compose_contract_graph(carriers)
    if (contract["display_coverage"] != "complete" or contract["outcome"] != "complete"
            or contract["coverage_gaps"] or contract["conflicts"] or contract["missing_relation_semantics"]):
        raise ValueError("Contract graph has coverage, conflict, or relation-semantics gaps")
    if not contract["relations"]:
        raise ValueError("Contract graph has no canonical or derived Relations")
    docs["CA-PROJ-019"] = "---\n" + yaml.safe_dump({"artifact_form": "Projection", "projection_id": "CA-PROJ-019", "form": "Map", "source": {"named_selection": "Named Selection//Current MODEL Formal Contracts", "atoms": expected}, "updated_at": now}, allow_unicode=True, sort_keys=False) + "---\n" + render_contract_graph(contract)
    docs["CA-PROJ-019"] = insert_namespace_context(docs["CA-PROJ-019"], observed)
    return docs, {"expected_source_atoms": expected, "observed_diagnostics": observed["diagnostics"], "aspect_containment_direct_facts": len(direct_aspect_facts), "contract_coverage": contract["coverage"], "relation_count": len(contract["relations"]), "tree_nodes": len(tree["nodes"]), "tree_edges": len(tree["edges"])}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--frontier", required=True, type=Path)
    parser.add_argument("--stage-dir", type=Path, default=PREP / "stageddocs")
    parser.add_argument("--overlay-publication-plan", type=Path)
    args = parser.parse_args()
    frontier = args.frontier if args.frontier.is_absolute() else ROOT / args.frontier
    stage = args.stage_dir.resolve()
    if not stage.is_relative_to(PREP):
        raise ValueError("Staging output must remain inside projection-preparation")
    rows, frontier_sha = read_frontier(frontier)
    predecessors = existing_predecessors()
    carriers, relocations = carriers_from_frontier(rows)
    overlay_evidence = None
    if args.overlay_publication_plan:
        plan_path = args.overlay_publication_plan
        plan_path = plan_path if plan_path.is_absolute() else ROOT / plan_path
        carriers, overlay_evidence = overlay_publication_candidates(carriers, plan_path)
    docs, evidence = render(carriers, current_timestamp(ROOT))
    stage.mkdir(parents=True, exist_ok=True)
    if any(stage.iterdir()):
        raise ValueError("Stage directory must be empty; preserve any prior packet")
    for identifier, document in docs.items():
        metadata = yaml.safe_load(document.split("---\n", 2)[1])
        if metadata.get("projection_id") != identifier or metadata.get("form") != "Map" or "version" in metadata:
            raise ValueError(f"Invalid staged frontmatter: {identifier}")
        if not metadata.get("source", {}).get("named_selection") or not metadata["source"].get("atoms"):
            raise ValueError(f"Missing staged source binding: {identifier}")
        (stage / NAMES[identifier]).write_text(document, encoding="utf-8")
    status = "COUNTERFACTUAL_NOT_PUBLISHED" if overlay_evidence else "STAGED_NOT_PUBLISHED"
    manifest = {"status": status, "frontier": {"path": str(frontier.relative_to(ROOT)), "sha256": frontier_sha, "selected_operations": len(rows), "relocated_current_carriers": relocations}, "predecessors": predecessors, "staged": [{"projection_id": i, "path": str((stage / NAMES[i]).relative_to(ROOT)), "sha256": digest((stage / NAMES[i]).read_bytes())} for i in IDS], "evidence": evidence, "publication_boundary": "No official projection, Current source, Journal, Git, or runtime state was written."}
    if overlay_evidence:
        manifest["counterfactual_overlay"] = overlay_evidence
        manifest["source_path_semantics"] = "Overlay DTO source.path is the intended canonical destination, not the candidate staging path."
    (stage / ("preview-manifest.json" if overlay_evidence else "staging-manifest.json")).write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": manifest["status"], "source_atoms": len(carriers), "relation_count": evidence["relation_count"]}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
