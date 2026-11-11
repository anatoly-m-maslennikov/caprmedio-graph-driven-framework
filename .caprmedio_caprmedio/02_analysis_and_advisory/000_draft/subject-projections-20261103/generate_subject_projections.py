#!/usr/bin/env python3
"""Stage seven source-pinned Subject Maps; publish only with --publish."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path
import sys

import yaml

ROOT = Path(__file__).resolve().parents[4]
PACKET = Path(__file__).resolve().parent
FRONTIER = ROOT / ".caprmedio_caprmedio/02_analysis/draft/epic-completion-20261104/post-endpoint-frontier.json"
OUTPUT = ROOT / ".caprmedio_caprmedio/_projection"
TOOLS = ROOT / "LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_TOOLS"
sys.path[:0] = [str(TOOLS / "GENERATE_ENTITY_GRAPH"), str(TOOLS)]

from artifact_metadata import current_timestamp  # noqa: E402
from atom_operations import atom_identity_lock  # noqa: E402
from current_entity_sources import _read_atom  # noqa: E402
from generate_entity_graph import atomic_write  # noqa: E402
from scope_unit_declarations import read_scope_unit_declarations  # noqa: E402
from subject_projection_audits import build_subject_audits, render_subject_audit, select_model_subjects  # noqa: E402
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


def project_root_binding() -> tuple[str, str]:
    declarations = read_scope_unit_declarations(ROOT, ".caprmedio_caprmedio")
    root = declarations.root
    if not root.is_root or declarations.by_name.get(root.name) != root:
        raise ValueError("Project root Scope Unit is unresolved")
    return f"Project//{root.name}", declarations.digest


def validate_source(metadata: dict) -> None:
    source = metadata.get("source")
    if not isinstance(source, dict):
        raise ValueError("Projection source is missing")
    selection, atoms = source.get("named_selection"), source.get("atoms")
    if (not isinstance(selection, str) or not selection.startswith("Named Selection//")
            or not selection.removeprefix("Named Selection//").strip()
            or not isinstance(atoms, list)
            or any(not isinstance(atom, str) or not re.fullmatch(r"[^\s@]+@[0-9]+", atom) for atom in atoms)):
        raise ValueError("Projection source selection or versioned Atom references are invalid")


def output_predecessors(documents: list[dict]) -> dict[Path, bytes | None]:
    predecessors = {}
    expected_ids = {doc["projection_id"] for doc in documents}
    pairs = {(doc["form"], doc["scope_unit"]) for doc in documents}
    if len(expected_ids) != len(documents) or len(pairs) != len(documents):
        raise ValueError("Projection ID and Form/Scope Unit must be one-to-one")
    for path in OUTPUT.glob("CA-PROJ-*.md"):
        if path.is_symlink():
            raise ValueError(f"Unsafe Projection carrier: {path}")
        metadata = yaml.safe_load(path.read_text().split("---", 2)[1])
        if not isinstance(metadata, dict):
            raise ValueError(f"Invalid Projection metadata: {path}")
        identifier = metadata.get("projection_id")
        if identifier in expected_ids and path != ROOT / next(doc["path"] for doc in documents if doc["projection_id"] == identifier):
            raise ValueError(f"Projection ID has a different carrier: {path}")
        pair = (metadata.get("form"), metadata.get("scope_unit"))
        if pair in pairs and identifier not in expected_ids:
            raise ValueError(f"Projection Form/Scope Unit already has another ID: {path}")
    for doc in documents:
        destination = ROOT / doc["path"]
        others = [p for p in OUTPUT.glob(f"{doc['projection_id']}-*.md") if p != destination]
        if others or destination.is_symlink():
            raise ValueError(f"Projection ID has a different carrier: {doc['projection_id']}")
        previous = destination.read_bytes() if destination.exists() else None
        if previous is not None:
            metadata = yaml.safe_load(previous.decode().split("---", 2)[1])
            if (metadata.get("projection_id") != doc["projection_id"]
                    or metadata.get("form") != doc["form"]
                    or metadata.get("scope_unit") != doc["scope_unit"]):
                raise ValueError(f"Projection identity mismatch: {destination}")
            validate_source(metadata)
        predecessors[destination] = previous
    return predecessors


def check_model_authority(documents: list[dict]) -> None:
    directory = ROOT / ".caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement"
    declarations = []
    for path in directory.glob("CA-R-*.md"):
        if path.is_symlink():
            raise ValueError(f"Unsafe Declaration carrier: {path}")
        raw = path.read_text()
        metadata = yaml.safe_load(raw.split("---", 2)[1])
        if (metadata.get("status"), metadata.get("role"), metadata.get("form")) == ("Active", "Requirement", "Declaration"):
            declarations.append((metadata.get("subjects", {}).get("active"), raw))
    for doc in documents:
        active = f"CAPRMEDIO_MODEL <+ Projection/(.Form := {doc['form']})"
        matches = [text for subject, text in declarations if subject == active]
        if len(matches) != 1 or f"Projection.Form: {doc['form']};" not in matches[0]:
            raise ValueError(f"Projection Form Declaration unavailable: {doc['form']}")
    scope = [text for subject, text in declarations if subject == "CAPRMEDIO_MODEL <+ Projection.Scope Unit"]
    identity = [text for subject, text in declarations if subject == "CAPRMEDIO_MODEL <+ Projection.ID"]
    if (len(scope) != 1 or "Projection.Scope Unit{:1}: [Scope Unit//]{:1}" not in scope[0]
            or len(identity) != 1
            or "DETERMINES(Projection//$projection, (.Form, .Scope Unit), (.ID))" not in identity[0]
            or "DETERMINES(Projection//$projection_2, (.ID), (.Form, .Scope Unit))" not in identity[0]):
        raise ValueError("Projection identity Declarations are not adopted")


def publish(documents: list[dict], frontier_raw: bytes, frontier: dict, old: dict, root_binding: tuple[str, str]) -> dict:
    with atom_identity_lock(ROOT):
        if FRONTIER.read_bytes() != frontier_raw:
            raise ValueError("Frontier changed before publication")
        read_sources(frontier)
        if project_root_binding() != root_binding:
            raise ValueError("Project root declaration changed before publication")
        check_model_authority(documents)
        predecessors = output_predecessors(documents)
        for doc in documents:
            staged = ROOT / doc["staged"]
            if staged.is_symlink() or not staged.resolve().is_relative_to(ROOT) or digest(staged.read_bytes()) != doc["sha256"]:
                raise ValueError(f"Staged Projection changed: {staged}")
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
    root_binding = project_root_binding()
    scope_name = root_binding[0].removeprefix("Project//")
    if not scope_name or scope_name in {".", ".."} or any(c in scope_name for c in ("/", "\\", "\x00")):
        raise ValueError("Project root name is not a safe filename component")
    scoped, scope_diagnostics = select_model_subjects(carriers)
    model_carriers = [c for c in scoped if any(key in c.get("subjects", {}) for key in ("active", "governs"))]
    data = build_subject_projection_data(model_carriers)
    check_declaration_authority(carriers, data)
    audits = build_subject_audits(scoped, data, scope_diagnostics=scope_diagnostics)
    pins = sorted(f"{c['source']['atom_id']}@{c['source']['version']}" for c in carriers)
    now = current_timestamp(ROOT)
    old = {p.name: digest(p.read_bytes()) for p in OUTPUT.glob("CA-PROJ-01[4-9]-*.md")}
    stage = PACKET / "staged"
    stage.mkdir(exist_ok=True)
    documents = []
    scope = (
        f"Selected sources: {len(carriers)} Current Methodology and direct Project RMED Atoms. "
        "Subjects are limited to the explicit MODEL namespace; concrete Node instances are excluded. "
        "Unprefixed Subjects remain unresolved for review. Coverage and absence are evaluated within this selection.\n\n"
        "Cardinalities, formats and Formal Claims come only from Current Requirement / Declaration Atoms. "
        "Unsupported CFEL remains visible with diagnostics.\n\n"
    )
    for number, name, mode in VIEWS:
        identifier = f"CA-PROJ-{number:03d}"
        filename = f"{identifier}-{scope_name}--{name.replace(' ', '-')}--Current-{name.replace(' ', '-')}.md"
        body = render_primary_projection(data, mode) if isinstance(mode, int) else render_subject_audit(audits, mode)
        title, rest = body.split("\n", 1)
        header = {"artifact_form": "Projection", "projection_id": identifier, "form": name, "scope_unit": root_binding[0],
                  "source": {"named_selection": f"Named Selection//Current {name}", "atoms": pins},
                  "updated_at": now}
        validate_source(header)
        text = "---\n" + yaml.safe_dump(header, allow_unicode=True, sort_keys=False) + "---\n\n" + title + "\n\n" + scope + rest.lstrip("\n")
        path = stage / filename
        path.write_text(text)
        documents.append({"projection_id": identifier, "name": name, "form": name, "scope_unit": root_binding[0], "path": str((OUTPUT / filename).relative_to(ROOT)),
                          "staged": str(path.relative_to(ROOT)), "sha256": digest(text.encode())})
    manifest = {"status": "STAGED", "frontier": str(FRONTIER.relative_to(ROOT)), "frontier_sha256": digest(frontier_raw),
                "selected_sources": len(carriers), "declaration_coverage": data["coverage"],
                "audit_counts": {key: value.get("coverage", {}) for key, value in audits.items()},
                "prior_projections": old, "projections": documents}
    (PACKET / "audit-data.json").write_text(json.dumps(audits, indent=2, ensure_ascii=False) + "\n")
    (PACKET / "generation-manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")
    if args.publish:
        manifest["predecessors"] = publish(documents, frontier_raw, frontier, old, root_binding)
        manifest["status"] = "PUBLISHED"
        (PACKET / "generation-manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")
    print(json.dumps({"status": manifest["status"], "views": len(documents), "sources": len(carriers), "audit_counts": manifest["audit_counts"]}))


if __name__ == "__main__":
    main()
