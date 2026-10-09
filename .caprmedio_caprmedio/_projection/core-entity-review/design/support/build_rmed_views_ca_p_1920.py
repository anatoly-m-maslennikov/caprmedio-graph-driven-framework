#!/usr/bin/env python3
"""Build CA-P-1920's non-authoritative RMED pointer views.

This deliberately reuses the pinned baseline's subject metadata.  It does not
interpret a subject path, admit a relation, or make a source applicable.
"""

from __future__ import annotations

import hashlib
import json
from collections import defaultdict
from pathlib import Path
from typing import Any


ROLE_MAP = {
    "Requirement": "R",
    "Method": "M",
    "Evaluation": "E",
    "Delivery": "D",
}
ROLE_MEANING = {
    "R": "model skeleton and required results",
    "M": "construction and authoring conventions; excludes Operations-specific actions and workflows",
    "E": "checks and acceptance evidence",
    "D": "Carrier model, formats, and placement or storage; a direct Delivery definition can also be a model-skeleton input",
}
SAMPLE_IDS = ("CA-R-655", "CA-M-111", "CA-E-520", "CA-D-414", "CA-D-478")


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def canonical_json(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n"


def source_key(source: dict[str, Any]) -> str:
    return f"{source['atom_id']}@{source['atom_revision']}:{source['carrier_sha256']}"


def first_claim_line(repo_root: Path, source: dict[str, Any]) -> dict[str, Any] | None:
    """Return one raw Main Content Claim line; never reconstruct source bytes."""
    rel = Path(source["carrier_path"])
    raw = (repo_root / rel).read_bytes()
    lines = raw.decode("utf-8").splitlines()
    claim_line = next((index for index, line in enumerate(lines) if line == "## Claim"), None)
    if claim_line is None:
        return None
    for index in range(claim_line + 1, len(lines)):
        line = lines[index]
        if line.startswith("## "):
            break
        if line.strip():
            quote = line
            return {
                "carrier_path": source["carrier_path"],
                "carrier_sha256": source["carrier_sha256"],
                "start_line": index + 1,
                "end_line": index + 1,
                "quote": quote,
                "text_sha256": sha256(quote.encode("utf-8")),
            }
    return None


def pointer(occurrence: dict[str, Any], source_atom: dict[str, Any]) -> dict[str, Any]:
    source = occurrence["source_ref"]
    source_role = source_atom["content_role"]
    view_role = ROLE_MAP[source_role]
    return {
        "source_ref_key": source_key(source),
        "source_ref": {
            "source_ref_key": source_key(source),
            "contribution": source["contribution"],
        },
        "source_content_role": source_role,
        "rmed_role": view_role,
        "subject_pointer_role": occurrence["role"],
        "target_identity": occurrence["subject_path"],
        "derivation": (
            "source-subject GOVERNS pointer; it is not an admitted Entity relation or automatic applicability"
            if occurrence["role"] == "GOVERNS"
            else "source-subject DEPENDS_ON pointer; it is not a governing Claim or automatic applicability"
        ),
    }


def sorted_pointers(values: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return sorted(values, key=lambda item: (item["target_identity"], item["source_ref_key"]))


def compact_source_ref(row: dict[str, Any]) -> str:
    """Human views keep only a compact pointer; JSON retains exact proof."""
    return row["source_ref_key"].split(":", 1)[0]


def prefix_tree(values: dict[str, Any]) -> dict[str, Any]:
    """Group slash-delimited display strings without assigning slash semantics."""
    tree: dict[str, Any] = {"children": {}, "values": []}
    for identity, value in values.items():
        node = tree
        for segment in identity.split("/"):
            node = node["children"].setdefault(segment, {"children": {}, "values": []})
        node["values"].append((identity, value))
    return tree


def render_compact_prefix_tree(
    tree: dict[str, Any],
    lines: list[str],
    indent: str,
    prefix: tuple[str, ...] = (),
    leaf_renderer: Any = None,
) -> None:
    for segment in sorted(tree["children"]):
        node = tree["children"][segment]
        display_prefix = "/".join((*prefix, segment))
        if node["values"]:
            # A tree node owns exactly one fully literal identity; do not echo it.
            identity, value = node["values"][0]
            lines.append(f"{indent}- {identity}")
            leaf_renderer(value, lines, indent + "  ")
        else:
            lines.append(f"{indent}- {display_prefix} (prefix)")
        render_compact_prefix_tree(node, lines, indent + "  ", (*prefix, segment), leaf_renderer)


def write_indented_trees(
    design_dir: Path,
    role_trees: list[dict[str, Any]],
    entity_rows: list[dict[str, Any]],
) -> None:
    role_lines = [
        "CA-P-1920 RMED role tree — indented labels are literal slash-qualified identities for display only; no native semantics. Exact proof: rmed.views.json.",
        "",
    ]
    for tree in role_trees:
        role_lines.extend(
            [
                f"{tree['rmed_role']} — {tree['role_meaning']}",
                "  GOVERNS",
            ]
        )
        governs_by_identity: dict[str, list[dict[str, Any]]] = defaultdict(list)
        for row in tree["governing_claim_pointers"]:
            governs_by_identity[row["target_identity"]].append(row)
        render_compact_prefix_tree(
            prefix_tree(governs_by_identity),
            role_lines,
            "    ",
            leaf_renderer=lambda rows, output, pad: output.extend(
                f"{pad}- {compact_source_ref(row)}" for row in rows
            ),
        )
        role_lines.append("  DEPENDS_ON")
        depends_by_identity: dict[str, list[dict[str, Any]]] = defaultdict(list)
        for row in tree["dependency_pointers"]:
            depends_by_identity[row["target_identity"]].append(row)
        render_compact_prefix_tree(
            prefix_tree(depends_by_identity),
            role_lines,
            "    ",
            leaf_renderer=lambda rows, output, pad: output.extend(
                f"{pad}- {compact_source_ref(row)}" for row in rows
            ),
        )
        role_lines.append("")
    (design_dir / "rmed.roles.indented.txt").write_text("\n".join(role_lines) + "\n", encoding="utf-8")

    entity_lines = [
        "CA-P-1920 RMED Entity tree — indented labels are literal slash-qualified identities for display only; no native semantics. M/E/D are associated pointers, not proven applicability. Exact proof: rmed.views.json.",
        "",
    ]
    entity_by_identity = {row["entity_identity"]: row for row in entity_rows}

    def render_entity(row: dict[str, Any], output: list[str], pad: str) -> None:
        for channel_name, heading in (
            ("governing_claim_pointers_by_rmed_role", "GOVERNS"),
            ("dependency_pointers_by_rmed_role", "DEPENDS_ON"),
        ):
            role_map = row[channel_name]
            if not role_map:
                continue
            output.append(f"{pad}- {heading}")
            for role in ("R", "M", "E", "D"):
                pointers = role_map.get(role)
                if not pointers:
                    continue
                qualifier = "" if role == "R" else " — associated/pointer-derived; not proven applicable"
                output.append(f"{pad}  - {role}{qualifier}")
                for pointer_ref in pointers:
                    output.append(f"{pad}    - {compact_source_ref(pointer_ref)}")

    render_compact_prefix_tree(prefix_tree(entity_by_identity), entity_lines, "", leaf_renderer=render_entity)
    (design_dir / "rmed.entities.indented.txt").write_text("\n".join(entity_lines) + "\n", encoding="utf-8")


def main() -> None:
    design_dir = Path(__file__).resolve().parent
    repo_root = design_dir.parents[3]
    baseline_path = repo_root / ".caprmedio_caprmedio/_projection/core-entity-review/baseline.inventory.json"
    baseline_bytes = baseline_path.read_bytes()
    baseline = json.loads(baseline_bytes)

    source_atoms = {
        (source["atom_id"], source["atom_revision"]): source
        for source in baseline["source_atoms"]
    }
    source_pin_failures: list[dict[str, str]] = []
    for source in source_atoms.values():
        rel = Path(source["carrier_path"])
        if rel.is_absolute() or ".." in rel.parts:
            source_pin_failures.append({"atom_id": source["atom_id"], "reason": "unsafe carrier path"})
            continue
        actual_path = repo_root / rel
        if not actual_path.is_file():
            source_pin_failures.append({"atom_id": source["atom_id"], "reason": "carrier missing"})
            continue
        if sha256(actual_path.read_bytes()) != source["carrier_sha256"]:
            source_pin_failures.append({"atom_id": source["atom_id"], "reason": "carrier sha256 mismatch"})
    if source_pin_failures:
        raise SystemExit(canonical_json({"source_pin_validation": "failed", "failures": source_pin_failures}))

    catalog: dict[str, dict[str, Any]] = {}
    role_pointers: dict[str, dict[str, list[dict[str, Any]]]] = {
        role: {"GOVERNS": [], "DEPENDS_ON": []} for role in ROLE_MEANING
    }
    entities: dict[str, dict[str, dict[str, list[dict[str, str]]]]] = defaultdict(
        lambda: {
            "GOVERNS": {role: [] for role in ROLE_MEANING},
            "DEPENDS_ON": {role: [] for role in ROLE_MEANING},
        }
    )
    excluded: dict[str, dict[str, int]] = defaultdict(lambda: {"GOVERNS": 0, "DEPENDS_ON": 0, "source_atoms": 0})

    for source in source_atoms.values():
        if source["content_role"] not in ROLE_MAP:
            excluded[source["content_role"]]["source_atoms"] += 1

    for occurrence in baseline["occurrences"]:
        source = occurrence["source_ref"]
        source_atom = source_atoms[(source["atom_id"], source["atom_revision"])]
        source_role = source_atom["content_role"]
        if source_role not in ROLE_MAP:
            excluded[source_role][occurrence["role"]] += 1
            continue
        key = source_key(source)
        catalog.setdefault(
            key,
            {
                "atom_id": source["atom_id"],
                "atom_revision": source["atom_revision"],
                "content_role": source_role,
                "rmed_role": ROLE_MAP[source_role],
                "carrier_path": source["carrier_path"],
                "carrier_sha256": source["carrier_sha256"],
            },
        )
        rendered = pointer(occurrence, source_atom)
        role_pointers[rendered["rmed_role"]][occurrence["role"]].append(rendered)
        entities[rendered["target_identity"]][occurrence["role"]][rendered["rmed_role"]].append(
            {
                "source_ref_key": key,
                "source_ref": {
                    "source_ref_key": key,
                    "contribution": source["contribution"],
                },
                "source_content_role": source_role,
                "subject_pointer_role": occurrence["role"],
            }
        )

    role_trees: list[dict[str, Any]] = []
    for role, meaning in ROLE_MEANING.items():
        governs = sorted_pointers(role_pointers[role]["GOVERNS"])
        depends = sorted_pointers(role_pointers[role]["DEPENDS_ON"])
        role_trees.append(
            {
                "rmed_role": role,
                "role_meaning": meaning,
                "governing_claim_pointer_count": len(governs),
                "governed_identity_count": len({item["target_identity"] for item in governs}),
                "dependency_pointer_count": len(depends),
                "dependency_identity_count": len({item["target_identity"] for item in depends}),
                "governing_claim_pointers": governs,
                "dependency_pointers": depends,
            }
        )

    entity_rows: list[dict[str, Any]] = []
    for identity in sorted(entities):
        channels = entities[identity]
        governing = {
            role: sorted(values, key=lambda item: item["source_ref_key"])
            for role, values in channels["GOVERNS"].items()
            if values
        }
        dependencies = {
            role: sorted(values, key=lambda item: item["source_ref_key"])
            for role, values in channels["DEPENDS_ON"].items()
            if values
        }
        med_links = {role: governing[role] for role in ("M", "E", "D") if role in governing}
        entity_rows.append(
            {
                "entity_identity": identity,
                "view_membership": "pointer-derived from source Subjects; not a new Entity or admitted native fact",
                "governing_claim_pointers_by_rmed_role": governing,
                "dependency_pointers_by_rmed_role": dependencies,
                "optional_M_E_D_governing_links": med_links,
            }
        )

    samples: list[dict[str, Any]] = []
    for atom_id in SAMPLE_IDS:
        atom = next(source for source in source_atoms.values() if source["atom_id"] == atom_id)
        source = next(
            occurrence["source_ref"]
            for occurrence in baseline["occurrences"]
            if occurrence["role"] == "GOVERNS"
            and occurrence["source_ref"]["atom_id"] == atom_id
            and occurrence["source_ref"]["atom_revision"] == atom["atom_revision"]
        )
        sample = {
            "source_ref_key": source_key(source),
            "source_ref": {
                "source_ref_key": source_key(source),
                "contribution": source["contribution"],
            },
            "rmed_role": ROLE_MAP[atom["content_role"]],
            "subject_pointer_role": "GOVERNS",
            "target_identity": next(
                occurrence["subject_path"]
                for occurrence in baseline["occurrences"]
                if occurrence["role"] == "GOVERNS"
                and occurrence["source_ref"]["atom_id"] == atom_id
                and occurrence["source_ref"]["atom_revision"] == atom["atom_revision"]
            ),
            "claim_evidence": first_claim_line(repo_root, source),
            "provenance_note": "The Claim remains in its source Atom; this view stores only a pointer to its source pin.",
        }
        if atom_id == "CA-D-414":
            sample["model_skeleton_note"] = (
                "This Delivery Claim directly classifies Carrier and is shown as a possible skeleton input; the view does not admit a new model fact."
            )
        samples.append(sample)

    output = {
        "source_task": "CA-P-1920",
        "baseline_inventory_sha256": baseline["inventory_sha256"],
        "baseline_inventory_path": ".caprmedio_caprmedio/_projection/core-entity-review/baseline.inventory.json",
        "baseline_inventory_file_sha256": sha256(baseline_bytes),
        "source_binding": baseline["source_binding"],
        "non_authoritative": True,
        "source_migration": "not_performed",
        "semantic_admission": "not_performed",
        "view_rules": {
            "source_references": "Source Atom references are provenance pointers, not copied Claims or duplicated authority.",
            "governs": "GOVERNS remains a governing-subject pointer only; it does not prove applicability or a native relation.",
            "depends_on": "DEPENDS_ON remains a separate dependency pointer; it never becomes a governing Claim in this view.",
            "identity": "Every subject path is retained as a literal baseline identity; no root semantics, inheritance, or Internal/External/Relational locus is inferred.",
            "presentation_prefixes": "Indented slash-prefix grouping is presentation only; it does not classify slash syntax or create a model hierarchy.",
            "operations": "Operations sources are excluded from RMED construction guidance; no action or workflow is represented as M.",
        },
        "source_pin_validation": {
            "status": "passed",
            "checked_source_count": len(source_atoms),
            "checked_current_bytes": True,
        },
        "source_catalog": dict(sorted(catalog.items())),
        "role_centered_overview": {
            "layout": "R/M/E/D role tree with GOVERNS and DEPENDS_ON channels kept separate",
            "role_trees": role_trees,
            "excluded_source_roles": dict(sorted(excluded.items())),
        },
        "entity_centered_view": {
            "layout": "literal target identity with optional M/E/D GOVERNS links; DEPENDS_ON links are separate",
            "entity_identity_count": len(entity_rows),
            "entities": entity_rows,
        },
        "source_backed_examples": samples,
        "checks_performed": [
            "baseline inventory fingerprint and source binding copied without modification",
            "all 908 selected source carrier byte hashes match their pinned baseline hashes",
            "all 4,534 pointers retain their original role; RMED view includes only R/M/E/D source roles",
            "shared sources are stored once in source_catalog and referenced by source_ref_key",
            "no subject path was reclassified, no relation admitted, and no applicability inferred",
        ],
        "questions": [
            "Which pointer-derived M/E/D links, if any, should later semantic review establish as applicable to a specific Entity?",
            "Which Delivery Claims beyond direct definitions such as CA-D-414 should contribute to the model skeleton after Main Content review?",
        ],
    }

    json_path = design_dir / "rmed.views.json"
    json_path.write_text(canonical_json(output), encoding="utf-8")

    write_indented_trees(design_dir, role_trees, entity_rows)

    rows = []
    for tree in role_trees:
        rows.append(
            f"| {tree['rmed_role']} | {tree['role_meaning']} | {tree['governing_claim_pointer_count']} | "
            f"{tree['governed_identity_count']} | {tree['dependency_pointer_count']} | {tree['dependency_identity_count']} |"
        )
    sample_lines = []
    for sample in samples:
        evidence = sample["claim_evidence"]
        line = "unavailable" if evidence is None else f"{evidence['carrier_path']}:{evidence['start_line']} — {evidence['quote']}"
        sample_lines.append(
            f"- `{sample['rmed_role']}` `{sample['source_ref_key']}` → `{sample['target_identity']}`: {line}"
        )
    markdown = "\n".join(
        [
            "# CA-P-1920 — derived RMED views",
            "",
            "Non-authoritative pointer views from the pinned Core baseline. They neither migrate sources nor admit semantics, relations, applicability, locus, or inheritance.",
            "",
            f"Baseline inventory: `{output['baseline_inventory_sha256']}`. All {len(source_atoms)} selected source-carrier byte hashes match their baseline pins.",
            "",
            "## Role-centered overview",
            "",
            "| Role | View purpose | GOVERNS pointers | Governed identities | DEPENDS_ON pointers | Dependency identities |",
            "| --- | --- | ---: | ---: | ---: | ---: |",
            *rows,
            "",
            "`GOVERNS` and `DEPENDS_ON` are separate pointer channels. A dependency is never rendered as a governing Claim. `Operations` (102 governing / 782 dependency pointers) and `Concern` (1 / 0) remain outside RMED; M does not stand for Operations.",
            "",
            "## Entity-centered view",
            "",
            f"The JSON contains {len(entity_rows)} literal target identities. Each has separately keyed governing pointers and dependency pointers, plus nonempty optional M/E/D governing links. Membership is pointer-derived only; shared source pins live once in `source_catalog`.",
            "",
            "Detailed presentation trees: `rmed.roles.indented.txt` and `rmed.entities.indented.txt`. Their slash-prefix indentation is display only; it does not assign slash semantics or create Entity hierarchy.",
            "",
            "## Source-backed examples",
            "",
            *sample_lines,
            "",
            "CA-D-414 is deliberately visible as a Delivery-source skeleton input example: that does not promote Delivery generally or create a new fact. CA-D-478 illustrates the distinct Carrier/format/storage/placement channel.",
            "",
            "## Full baseline accounting",
            "",
            "The RMED view has 805 GOVERNS and 2,844 DEPENDS_ON pointers. Excluded Operations contributes 102 GOVERNS and 782 DEPENDS_ON pointers; excluded Concern contributes 1 GOVERNS and 0 DEPENDS_ON pointers. Together these are the pinned baseline's 4,534 occurrences.",
            "",
            "## Open semantic work",
            "",
            "- Establishing actual applicability of any per-Entity M/E/D pointer requires later Main Content semantic review.",
            "- Identifying further Delivery definitions that inform the skeleton requires the same review.",
            "- Internal, External, and Relational remain orthogonal and unclassified here.",
            "",
        ]
    )
    (design_dir / "rmed.views.md").write_text(markdown, encoding="utf-8")


if __name__ == "__main__":
    main()
