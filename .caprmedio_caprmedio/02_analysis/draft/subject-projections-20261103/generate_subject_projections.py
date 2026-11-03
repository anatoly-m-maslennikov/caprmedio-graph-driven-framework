#!/usr/bin/env python3
"""Stage seven source-pinned Subject Maps; publish only with --publish."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import sys

import yaml

ROOT = Path(__file__).resolve().parents[4]
PACKET = Path(__file__).resolve().parent
FRONTIER = ROOT / ".caprmedio_caprmedio/02_analysis/draft/role-projection-completion-20261102/current-source-frontier.json"
OUTPUT = ROOT / ".caprmedio_caprmedio/_projection"
TOOLS = ROOT / "LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_TOOLS"
sys.path[:0] = [str(TOOLS / "GENERATE_ENTITY_GRAPH"), str(TOOLS)]

from artifact_metadata import current_timestamp  # noqa: E402
from atom_operations import atom_identity_lock  # noqa: E402
from current_entity_sources import _read_atom  # noqa: E402
from generate_entity_graph import atomic_write  # noqa: E402
from subject_projection_audits import build_subject_audits, render_subject_audit  # noqa: E402
from subject_projection_data import build_subject_projection_data  # noqa: E402
from subject_projection_views import render_primary_projection  # noqa: E402

VIEWS = (
    (20, "Primary Entities Tree", 1),
    (21, "Primary Entities with Direct Properties", 2),
    (22, "Primary Entities with Inherited Property Contracts", 3),
    (23, "Primary Entities with Inherited Formal Claims", 4),
    (24, "Passive Only Subjects", "passive_only_subjects"),
    (25, "Subjects without Requirement Declarations", "subjects_without_declaration_coverage"),
    (26, "Entity Definition and Active Subject Coverage", "entity_definition_summary"),
)


def digest(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def read_sources(frontier: dict) -> list[dict]:
    carriers, seen = [], set()
    for row in frontier["operations"]:
        path = ROOT / row["destination_path"]
        if not path.resolve().is_relative_to(ROOT) or path.is_symlink():
            raise ValueError(f"Unsafe source path: {path}")
        if digest(path.read_bytes()) != row["sha256"]:
            raise ValueError(f"Source drift: {row['base_id']}")
        carrier = _read_atom(path, ROOT)
        if (carrier is None or carrier["source"]["atom_id"] != row["base_id"]
                or carrier["source"]["version"] != row["version"]
                or carrier["metadata"].get("status") != row["status"]):
            raise ValueError(f"Source identity or lifecycle mismatch: {path}")
        if row["base_id"] in seen:
            raise ValueError(f"Duplicate selected Atom: {row['base_id']}")
        seen.add(row["base_id"])
        carriers.append(carrier)
    return carriers


def check_declaration_authority(carriers: list[dict], data: dict) -> None:
    allowed = {
        (c["source"]["atom_id"], c["source"]["version"])
        for c in carriers
        if c["read_view"].get("content_role") == "Requirement"
        and c["read_view"].get("type") == "Declaration"
    }
    for entity in data["entities"]:
        records = [entity, *entity["direct_properties"], *entity["inherited_properties"]]
        for record in records:
            for evidence in [*record.get("formal_claims", []), *record.get("contracts", [])]:
                source = evidence["source"]
                if (source["atom_id"], source["version"]) not in allowed:
                    raise ValueError("Non-Declaration contract authority")


def output_predecessors(documents: list[dict]) -> dict[Path, bytes | None]:
    predecessors = {}
    for doc in documents:
        destination = ROOT / doc["path"]
        others = [p for p in OUTPUT.glob(f"{doc['projection_id']}-*.md") if p != destination]
        if others or destination.is_symlink():
            raise ValueError(f"Projection ID has a different carrier: {doc['projection_id']}")
        previous = destination.read_bytes() if destination.exists() else None
        if previous is not None:
            metadata = yaml.safe_load(previous.decode().split("---", 2)[1])
            if (metadata.get("projection_id") != doc["projection_id"] or metadata.get("form") != "Map"
                    or metadata.get("source", {}).get("named_selection") != f"Named Selection//Current {doc['name']}"):
                raise ValueError(f"Projection identity or selection mismatch: {destination}")
        predecessors[destination] = previous
    return predecessors


def publish(documents: list[dict], frontier_raw: bytes, frontier: dict, old: dict) -> dict:
    with atom_identity_lock(ROOT):
        if FRONTIER.read_bytes() != frontier_raw:
            raise ValueError("Frontier changed before publication")
        read_sources(frontier)
        predecessors = output_predecessors(documents)
        written = []
        try:
            for doc in documents:
                path = ROOT / doc["path"]
                atomic_write(path, (ROOT / doc["staged"]).read_text())
                written.append(path)
            if {p.name: digest(p.read_bytes()) for p in OUTPUT.glob("CA-PROJ-01[4-9]-*.md")} != old:
                raise ValueError("An existing projection changed during publication")
        except BaseException:
            for path in written:
                expected = next(d["sha256"] for d in documents if d["path"] == str(path.relative_to(ROOT)))
                if digest(path.read_bytes()) == expected:
                    previous = predecessors[path]
                    if previous is None:
                        path.unlink()
                    else:
                        atomic_write(path, previous.decode())
            raise
    return {str(path.relative_to(ROOT)): digest(raw) if raw is not None else None
            for path, raw in predecessors.items()}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--publish", action="store_true")
    args = parser.parse_args()
    frontier_raw = FRONTIER.read_bytes()
    frontier = json.loads(frontier_raw)
    carriers = read_sources(frontier)
    data = build_subject_projection_data(carriers)
    check_declaration_authority(carriers, data)
    audits = build_subject_audits(carriers, data)
    pins = sorted(f"{c['source']['atom_id']}@{c['source']['version']}" for c in carriers)
    now = current_timestamp(ROOT)
    old = {p.name: digest(p.read_bytes()) for p in OUTPUT.glob("CA-PROJ-01[4-9]-*.md")}
    stage = PACKET / "staged"
    stage.mkdir(exist_ok=True)
    documents = []
    scope = (
        f"Selected sources: {len(carriers)} Current Methodology and direct Project RMED Atoms. "
        "Coverage and absence are evaluated within this selection.\n\n"
        "Cardinalities, formats and Formal Claims come only from Current Requirement / Declaration Atoms. "
        "Unsupported CFEL remains visible with diagnostics.\n\n"
    )
    for number, name, mode in VIEWS:
        identifier = f"CA-PROJ-{number:03d}"
        filename = f"{identifier}-CAPRMEDIO--Map--{name.replace(' ', '-')}.md"
        body = render_primary_projection(data, mode) if isinstance(mode, int) else render_subject_audit(audits, mode)
        title, rest = body.split("\n", 1)
        header = {"artifact_form": "Projection", "projection_id": identifier, "form": "Map",
                  "source": {"named_selection": f"Named Selection//Current {name}", "atoms": pins},
                  "updated_at": now}
        text = "---\n" + yaml.safe_dump(header, allow_unicode=True, sort_keys=False) + "---\n\n" + title + "\n\n" + scope + rest.lstrip("\n")
        path = stage / filename
        path.write_text(text)
        documents.append({"projection_id": identifier, "name": name, "path": str((OUTPUT / filename).relative_to(ROOT)),
                          "staged": str(path.relative_to(ROOT)), "sha256": digest(text.encode())})
    manifest = {"status": "STAGED", "frontier": str(FRONTIER.relative_to(ROOT)), "frontier_sha256": digest(frontier_raw),
                "selected_sources": len(carriers), "declaration_coverage": data["coverage"],
                "audit_counts": {key: value.get("coverage", {}) for key, value in audits.items()},
                "prior_projections": old, "projections": documents}
    (PACKET / "audit-data.json").write_text(json.dumps(audits, indent=2, ensure_ascii=False) + "\n")
    (PACKET / "generation-manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")
    if args.publish:
        manifest["predecessors"] = publish(documents, frontier_raw, frontier, old)
        manifest["status"] = "PUBLISHED"
        (PACKET / "generation-manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")
    print(json.dumps({"status": manifest["status"], "views": len(documents), "sources": len(carriers), "audit_counts": manifest["audit_counts"]}))


if __name__ == "__main__":
    main()
