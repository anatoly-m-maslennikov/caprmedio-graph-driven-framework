#!/usr/bin/env python3
"""Create-only consolidated receipt for captured node-review batch 0.

This is intentionally a derivation tool: it reads the accepted disposition
ledger and captured Git bytes, emits no native/Core changes, and refuses to
replace an existing receipt with different bytes.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import pathlib
import sys


ROOT = pathlib.Path(__file__).resolve().parents[6]
REVIEW_ROOT = ROOT / ".caprmedio_caprmedio/_projection/core-entity-review"
INPUT = REVIEW_ROOT / "nodes/inputs/nodes.batch-0.input.json"
LEDGER = REVIEW_ROOT / "nodes/nodes.dispositions.json"
BASELINE = REVIEW_ROOT / "baseline.inventory.json"
CANDIDATE = REVIEW_ROOT / "presentation/operator.entity-graph.candidate.json"
OUTPUT = pathlib.Path(__file__).resolve().parents[1] / "batch-0.review.json"


def sha256_file(path: pathlib.Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_snapshot_sources():
    source_path = REVIEW_ROOT / "nodes/support/snapshot_sources.py"
    spec = importlib.util.spec_from_file_location("snapshot_sources", source_path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def concise_quote(quote: str) -> str:
    return " ".join(quote.split())


def checked_evidence(ledger: dict, mark: dict, snapshot) -> tuple[list[str], list[dict], list[str]]:
    """Return prior global keys and verify every cited span against captured Git bytes."""
    catalogue = ledger["evidence_catalogue"]
    global_refs = mark["scoped_refs"].get("global_evidence_refs", [])
    verified = []
    read_atoms = set(mark["review_row"].get("checked_source_atom_ids", []))

    for key in global_refs:
        evidence = catalogue[key]
        raw = snapshot.read_source(evidence["atom_id"])
        lines = raw.decode("utf-8").splitlines()
        start, end = evidence["start_line"], evidence["end_line"]
        extracted = "\n".join(lines[start - 1 : end])
        assert extracted == evidence["quote"], (key, "quoted lines changed")
        assert hashlib.sha256(extracted.encode("utf-8")).hexdigest() == evidence["text_sha256"], (
            key,
            "quoted-line digest changed",
        )
        read_atoms.add(evidence["atom_id"])
        verified.append(
            {
                "evidence_ref": key,
                "atom_id": evidence["atom_id"],
                "line_span": [start, end],
                "quote_sha256": evidence["text_sha256"],
                "quote": concise_quote(evidence["quote"]),
            }
        )

    # A no-evidence prior question still needs its stated captured source read.
    for atom_id in sorted(read_atoms):
        snapshot.read_source(atom_id)
    return global_refs, verified, sorted(read_atoms)


def base_operator_rules(identity: str) -> list[str]:
    if identity.startswith("Applicable Methodology"):
        return ["#/applicable_methodology", "#/projection_member_model"]
    if identity.startswith("Artifact/Revision") or identity.startswith("Atom/Revision"):
        return ["#/root_entities/4", "#/atom_versioning", "#/history_model"]
    if identity.startswith("Atom/Claim") or identity == "Claim":
        return ["#/content_direction", "#/dependent_entities"]
    if identity.startswith("Atom/Scope") or "Target Scope Unit" in identity:
        return ["#/content_direction/scope_omission", "#/entity_identity_model"]
    if identity == "Atom/Details":
        return ["#/content_direction", "#/dependent_entities"]
    if identity == "Journal/Revision":
        return ["#/history_model", "#/root_entities/4"]
    if identity.endswith("Revision Binding"):
        return ["#/root_entities/4", "#/carrier_delivery_model"]
    if identity == "Projection/Revision":
        return ["#/projection_member_model", "#/snapshot_and_history_rules"]
    return ["#/entity_vs_syntax_rules"]


def mapping(identity: str) -> dict:
    """Return only candidate-display classifications, never native admissions."""
    path = None
    result = {
        "action": "review_required",
        "candidate_root": None,
        "candidate_path": None,
        "content_view": "unclassified",
        "confidence_percent": 85,
        "operator_rules": base_operator_rules(identity),
        "mapping_note": "The candidate has no sufficiently specific display mapping; the captured meaning is retained for technical review.",
        "question": {
            "kind": "technical_followup",
            "text": "Keep the captured qualified meaning pending authoring review; the candidate does not formalize a separate native kind or display path for it.",
        },
    }

    # Applicable Methodology is a derived view with its own lifecycle, but not
    # an eighth root. Artifact is used as the proposed lifecycle display root.
    if identity == "Applicable Methodology":
        result.update(
            action="rebase",
            candidate_root="Artifact",
            candidate_path="Artifact/Projection: Applicable Methodology",
            content_view="P",
            confidence_percent=95,
            mapping_note=(
                "The latest Operator direction makes Applicable Methodology a whole-set, one-to-one Projection. "
                "It remains derived and non-authoritative; Project Configuration Atoms are original sources, not synthesized members. "
                "Git preserves Atom contents and versions, while the Journal registers by Atom ID which were projected Active, projected archived, or authored in Project Configuration; an archived older version is not a permanent Atom-ID exclusion."
            ),
            question=None,
        )
        return result
    if identity == "Applicable Methodology Revision":
        result["mapping_note"] = (
            "The captured Type rule is revision-qualified, while the latest candidate explicitly declines to formalize a separate "
            "Applicable Methodology Revision or Projection Revision kind."
        )
        result["question"] = None
        return result
    if identity == "Applicable Methodology Compilation":
        path = "Artifact/Atom.Substance"
    elif identity == "Applicable Methodology Compilation/Claim Transformation":
        path = "Artifact/Atom.Substance: Operation/Applicable Methodology Compilation/Claim Transformation"
    elif identity == "Applicable Methodology Compilation/Step":
        path = "Artifact/Atom.Substance: Operation/Applicable Methodology Compilation/Step"
    elif identity.startswith("Applicable Methodology Compilation/Step: "):
        path = "Artifact/Atom.Substance: Operation/Applicable Methodology Compilation/" + identity.rsplit("/", 1)[1]
    elif identity == "Applicable Methodology Retrieval":
        result.update(
            action="operation_or_method",
            candidate_root="Artifact",
            candidate_path="Artifact/Atom.Substance",
            content_view="M",
            confidence_percent=95,
            mapping_note="The retrieval definition is a Method view over an Atom specification; it is distinct from an actual Execution.",
            question=None,
        )
        return result
    if path is not None:
        result.update(
            action="operation_or_method",
            candidate_root="Artifact",
            candidate_path=path,
            content_view="O",
            confidence_percent=95,
            mapping_note="The candidate separates the Operation definition in an Atom from an actual Execution; the display path does not admit native edges.",
            question=None,
        )
        return result

    if identity in {
        "Applicable Methodology/Carrier",
        "Applicable Methodology/Carrier Set",
        "Applicable Methodology/Projected Atom Carrier",
    }:
        suffix = identity.removeprefix("Applicable Methodology/")
        result.update(
            action="delivery_policy",
            candidate_root="Carrier",
            candidate_path=f"Carrier: Applicable Methodology {suffix}",
            content_view="D",
            confidence_percent=95,
            operator_rules=["#/carrier_delivery_model", "#/applicable_methodology", "#/projection_member_model"],
            mapping_note="Carrier remains a separate root; this display preserves source-versus-projected carrier distinctions without creating per-Property Carrier relations.",
            question=None,
        )
        return result
    if identity == "Applicable Methodology/Subject Index Carrier":
        result.update(
            action="delivery_policy",
            candidate_root="Carrier",
            candidate_path="Carrier: Applicable Methodology transient subject index (not persistent)",
            content_view="D",
            confidence_percent=95,
            operator_rules=["#/carrier_delivery_model", "#/applicable_methodology"],
            mapping_note="The proposed Carrier display retains the captured prohibition on a persistent GOVERNS or DEPENDS_ON subject-index Carrier.",
            question=None,
        )
        return result
    if identity == "Applicable Methodology/Source Frontier Digest":
        result.update(
            action="operation_or_method",
            candidate_root="Artifact",
            candidate_path="Artifact/Atom.Substance: Operation/Applicable Methodology Compilation/Source Frontier Digest",
            content_view="O",
            confidence_percent=95,
            operator_rules=["#/applicable_methodology", "#/history_model/relation_version_binding"],
            mapping_note="The digest remains a bounded compilation-control value, including the complete conflict set and approval binding; it is not an independently admitted root.",
            question=None,
        )
        return result
    if identity == "Applicable Methodology/Conflict":
        path = "Artifact/Projection: Applicable Methodology/Conflict"
    elif identity == "Applicable Methodology/Member":
        path = "Artifact/Projection: Applicable Methodology/Derived Atom member"
    elif identity == "Applicable Methodology/Member Selection":
        path = "Artifact/Projection: Applicable Methodology/Source selection"
    elif identity == "Applicable Methodology/Sources":
        path = "Artifact/Projection: Applicable Methodology/Source set"
    elif identity == "Applicable Methodology/Sources/CORE_META_MODEL":
        path = "Artifact/Projection: Applicable Methodology/Source set/Core"
    elif identity == "Applicable Methodology/Sources/Installed Extensions":
        path = "Artifact/Projection: Applicable Methodology/Source set/Installed Extensions"
    elif identity == "Applicable Methodology/Sources/Installed Extensions/Catalog Entry":
        path = "Artifact/Projection: Applicable Methodology/Source set/Installed Extensions/Catalog Entry"
    if path is not None:
        note = (
            "The latest Operator direction defines a one-to-one Projection: each derived Atom retains the source Atom ID and Version Number, "
            "with a relative source link; the Projection has its own whole-set lifecycle."
        )
        if identity == "Applicable Methodology/Sources/Installed Extensions":
            note = (
                "The old captured source establishes a Catalog Entry rather than a collection. The latest candidate separately proposes Installed Extensions "
                "as an Applicable Methodology source category; that is a candidate direction, not retroactive captured-Core proof."
            )
        result.update(
            action="projection_view",
            candidate_root="Artifact",
            candidate_path=path,
            content_view="P",
            confidence_percent=95,
            operator_rules=["#/applicable_methodology", "#/projection_member_model", "#/atom_lookup"],
            mapping_note=note,
            question=None,
        )
        return result

    if identity == "Artifact/Revision":
        result.update(
            action="rebase",
            candidate_root="Revision",
            candidate_path="Revision",
            confidence_percent=95,
            mapping_note="Revision is a separate historical root, not an Artifact property or subtype. Atom-only Version Number and Updated At obligations are not lifted onto every Artifact Revision.",
            question=None,
        )
        return result
    if identity == "Artifact/Revision/Archive Carrier":
        result.update(
            action="delivery_policy",
            candidate_root="Carrier",
            candidate_path="Carrier: Revision archive",
            content_view="D",
            confidence_percent=95,
            operator_rules=["#/carrier_delivery_model", "#/atom_versioning"],
            mapping_note="Carrier is separate from Revision; archive placement is delivery policy and does not define Carrier identity.",
            question=None,
        )
        return result
    if identity in {"Artifact/Revision/Archive Carrier Basename", "Artifact/Revision/Version"}:
        result.update(
            action="syntax_context",
            candidate_root="Carrier",
            candidate_path="Carrier archive basename @Version Number (delivery convention)",
            content_view="D",
            confidence_percent=95,
            operator_rules=["#/carrier_delivery_model", "#/entity_identity_model/carrier_identity"],
            mapping_note="The captured @<version> suffix is a carrier filename convention, not a general Artifact Revision Version property or Carrier identity.",
            question=None,
        )
        return result
    if identity == "Artifact/Revision/Status":
        path = "Revision.Status"
    elif identity == "Artifact/Revision/Status: Archived":
        path = "Revision.Status: Archived"
    if path is not None:
        result.update(
            action="rebase",
            candidate_root="Revision",
            candidate_path=path,
            confidence_percent=95,
            mapping_note="The current version becomes Active on update while older archived versions remain history; archived status is not a permanent Atom-ID exclusion.",
            question=None,
        )
        return result

    if identity == "Atom/Claim":
        result.update(
            action="rebase",
            candidate_root="Artifact",
            candidate_path="Artifact/Atom.Substance",
            content_view="mixed",
            confidence_percent=95,
            operator_rules=["#/content_direction", "#/dependent_entities"],
            mapping_note="The candidate's Substance umbrella maps RMED to Claim as a proposed display/content direction only; captured Claim remains an Atom-owned independently replaceable statement.",
            question=None,
        )
        return result
    if identity == "Atom/Claim/Canonical Signature":
        result.update(
            action="projection_view",
            candidate_root="Artifact",
            candidate_path="Artifact/Atom.Substance: Claim/Canonical Signature (derived comparison value)",
            content_view="P",
            confidence_percent=95,
            operator_rules=["#/entity_representation_rules", "#/content_direction"],
            mapping_note="The captured signature remains a derived non-authoritative comparison value and does not establish Claim equivalence.",
            question=None,
        )
        return result
    if identity == "Atom/Claim/Canonical Signature/Projection":
        result.update(
            action="projection_view",
            candidate_root="Artifact",
            candidate_path="Artifact/Projection: Canonical Signature report",
            content_view="P",
            confidence_percent=95,
            operator_rules=["#/entity_representation_rules", "#/carrier_delivery_model"],
            mapping_note="A Projection is a distinct derived Entity instance and cannot become authority for its source facts or establish Claim equivalence.",
            question=None,
        )
        return result
    if identity == "Atom/Claim/Carrier":
        result.update(
            action="delivery_policy",
            candidate_root="Carrier",
            candidate_path="Carrier: Atom Claim body section",
            content_view="D",
            confidence_percent=95,
            operator_rules=["#/carrier_delivery_model", "#/content_direction"],
            mapping_note="This is a delivery placement for the Claim applicability body section, not a second Claim value or a per-Property Carrier relation.",
            question=None,
        )
        return result
    if identity == "Atom/Claim/Target Scope Unit":
        result.update(
            action="rebase",
            candidate_root="Scope Unit",
            candidate_path="Scope Unit: Claim target",
            content_view="mixed",
            confidence_percent=95,
            operator_rules=["#/content_direction/scope_omission", "#/entity_identity_model"],
            mapping_note="Claim target Scope Unit remains distinct from Substance Scope applicability; an omitted Substance Scope resolves only to the whole governed Subject and whole owning Scope Unit.",
            question=None,
        )
        return result
    if identity == "Atom/Claim/Target Scope Unit/Carrier":
        result.update(
            action="delivery_policy",
            candidate_root="Carrier",
            candidate_path="Carrier: Claim target Scope Unit field",
            content_view="D",
            confidence_percent=95,
            operator_rules=["#/carrier_delivery_model", "#/content_direction/scope_omission"],
            mapping_note="The carrier field records a resolved Claim target; it neither makes applicability ownership nor removes the explicit-Scope requirement for restricted coverage.",
            question=None,
        )
        return result
    if identity == "Atom/Content Role: Plan/Type: Plan/Claim":
        result.update(
            action="rebase",
            candidate_root="Artifact",
            candidate_path="Artifact/Atom.Substance",
            content_view="P",
            confidence_percent=95,
            operator_rules=["#/content_direction", "#/dependent_entities"],
            mapping_note="The candidate calls the Plan primary contribution Objective; this is a proposed terminology/display rebase, not a retroactive replacement of the captured Plan Claim rule.",
            question=None,
        )
        return result
    if identity == "Atom/Content Role: Plan/Type: Plan/Claim/Target Scope Unit":
        result.update(
            action="rebase",
            candidate_root="Scope Unit",
            candidate_path="Scope Unit: Plan target (owner default only when no separate target is selected)",
            content_view="P",
            confidence_percent=95,
            operator_rules=["#/content_direction/scope_omission", "#/entity_identity_model"],
            mapping_note="The captured Plan default keeps its owning Scope Unit only when no separate target is selected; it does not turn Substance Scope applicability into ownership.",
            question=None,
        )
        return result
    if identity == "Atom/Details":
        result.update(
            action="rebase",
            candidate_root="Artifact",
            candidate_path="Artifact/Atom.Details",
            content_view="mixed",
            confidence_percent=95,
            operator_rules=["#/content_direction", "#/dependent_entities"],
            mapping_note="General Details remain optional supporting information. The proposal does not remove required Plan Definition of Done or Analysis results.",
            question=None,
        )
        return result

    if identity == "Atom/Revision":
        result.update(
            action="rebase",
            candidate_root="Revision",
            candidate_path="Revision",
            confidence_percent=95,
            mapping_note="Revision is a separate historical root. Every Atom update increments Version Number; the older version is archived history and the new current version is Active.",
            question=None,
        )
        return result
    if identity == "Atom/Revision/Author":
        path = "Revision.Author"
    elif identity == "Atom/Revision/Content":
        path = "Revision.Content"
    elif identity == "Atom/Revision/History":
        path = "Revision.History"
    elif identity == "Atom/Revision/Identifier":
        path = "Revision.Identifier"
    elif identity == "Atom/Revision/Reference":
        path = "Revision.Reference"
    elif identity == "Atom/Revision/Status":
        path = "Revision.Status"
    elif identity == "Atom/Revision/Status: Draft":
        path = "Revision.Status: Draft"
    elif identity == "Atom/Revision/Updated At":
        path = "Revision.Updated At"
    elif identity == "Atom/Revision/Version":
        path = "Revision.Version Number"
    if path is not None:
        note = "This remains a dependent historical-state distinction under the separate Revision root."
        if identity == "Atom/Revision/Reference":
            note = (
                "The candidate proposes Atom ID + Version Number for an Atom historical reference. The captured exact-reference requirement including Updated At remains evidence for future authoring, not a retroactive candidate change to Core."
            )
        elif identity == "Atom/Revision/Status: Draft":
            note = "Drafts remain without assigned Atom IDs; no Draft semantic-deduplication rule is introduced."
        result.update(
            action="rebase",
            candidate_root="Revision",
            candidate_path=path,
            confidence_percent=95,
            mapping_note=note,
            question=None,
        )
        return result
    if identity == "Atom/Revision/Author/Frontmatter":
        path = "Carrier: Revision author field (delivery convention)"
    elif identity == "Atom/Revision/Authoritative Carrier Bundle":
        path = "Carrier: Atom Revision authoritative bundle"
    elif identity == "Atom/Revision/Frontmatter":
        path = "Carrier: Atom Revision frontmatter (delivery convention)"
    elif identity == "Atom/Revision/Status/Carrier":
        path = "Carrier: Revision status field (delivery convention)"
    elif identity == "Atom/Revision/Status: Draft/Filename":
        result.update(
            action="syntax_context",
            candidate_root=None,
            candidate_path=None,
            content_view="D",
            confidence_percent=95,
            operator_rules=["#/carrier_delivery_model", "#/entity_identity_model/carrier_identity", "#/snapshot_and_history_rules"],
            mapping_note="The Draft filename rule is delivery syntax. Drafts lack Atom IDs, and filename/path is not Carrier identity.",
            question=None,
        )
        return result
    if path is not None:
        result.update(
            action="delivery_policy",
            candidate_root="Carrier",
            candidate_path=path,
            content_view="D",
            confidence_percent=95,
            operator_rules=["#/carrier_delivery_model", "#/root_entities/4"],
            mapping_note="Carrier stays a separate root; the display records a delivery convention without admitting per-Property Carrier relations.",
            question=None,
        )
        return result
    if identity in {
        "Atom/Revision/Status: Draft/Identity Continuity Evidence",
        "Atom/Revision/Status: Draft/Revision Lineage",
    }:
        result.update(
            action="review_required",
            candidate_root=None,
            candidate_path=None,
            confidence_percent=85,
            operator_rules=["#/draft_duplicate_policy", "#/history_model"],
            mapping_note="The candidate retains ID-free Drafts and defers Draft semantic deduplication, but does not formalize the captured pre-addressable lineage/history-entry mechanism.",
            question=None,
        )
        return result

    if identity == "Atom/Scope":
        result.update(
            action="rebase",
            candidate_root="Artifact",
            candidate_path="Artifact/Atom.Substance Scope",
            content_view="mixed",
            confidence_percent=95,
            operator_rules=["#/content_direction/scope_omission", "#/content_direction"],
            mapping_note="Substance Scope is applicability rather than ownership. Omission resolves only to the whole governed Subject and whole owning Scope Unit; either restriction requires explicit Scope.",
            question=None,
        )
        return result
    if identity == "Claim":
        result.update(
            action="rebase",
            candidate_root="Artifact",
            candidate_path="Artifact/Atom.Substance",
            content_view="mixed",
            confidence_percent=95,
            operator_rules=["#/content_direction", "#/dependent_entities"],
            mapping_note="The Substance umbrella is a latest Operator candidate direction. It maps RMED to Claim while preserving role-specific headings, qualified Scope, and required Plan/Analysis content; it does not rename captured Core retroactively.",
            question=None,
        )
        return result
    if identity.endswith("Revision Binding"):
        prefix = identity.removesuffix("/Revision Binding")
        result.update(
            action="delivery_policy",
            candidate_root="Carrier",
            candidate_path=f"Carrier: {prefix} Revision binding",
            content_view="D",
            confidence_percent=95,
            operator_rules=["#/carrier_delivery_model", "#/history_model"],
            mapping_note="The binding is carrier/delivery evidence for a Revision; absent, ambiguous, or mismatched bindings remain unknown rather than being inferred from a carrier path.",
            question=None,
        )
        return result
    if identity == "Journal/Revision":
        result.update(
            action="rebase",
            candidate_root="Revision",
            candidate_path="Revision (Journal record state)",
            confidence_percent=95,
            operator_rules=["#/history_model", "#/root_entities/4"],
            mapping_note="Journal records what happened and its Revision has a derived timestamp; it is not an Atom Revision and does not inherit Atom Version Number requirements.",
            question=None,
        )
        return result
    if identity == "Projection/Revision":
        result.update(
            action="review_required",
            candidate_root=None,
            candidate_path=None,
            confidence_percent=85,
            operator_rules=["#/projection_member_model", "#/snapshot_and_history_rules"],
            mapping_note="The candidate tracks Projection rebuilds but explicitly does not formalize a separate Projection Revision kind; the captured latest-rebuild timestamp remains distinct.",
            question=None,
        )
        return result
    raise AssertionError(f"unmapped identity: {identity}")


def constrain_to_evidenced_display_path(identity: str, proposed: dict) -> dict:
    """Do not turn an inferred owner or old slash label into a candidate path.

    The candidate names only a few genuine subtype/property/allowed-value
    displays.  A confident semantic classification can still have a null
    display mapping when the candidate did not name the owner/path.
    """
    projection_context_only = {
        "Applicable Methodology",
        "Applicable Methodology/Conflict",
        "Applicable Methodology/Member",
        "Applicable Methodology/Member Selection",
        "Applicable Methodology/Sources",
        "Applicable Methodology/Sources/CORE_META_MODEL",
        "Applicable Methodology/Sources/Installed Extensions/Catalog Entry",
        "Atom/Claim/Canonical Signature",
        "Atom/Claim/Canonical Signature/Projection",
    }
    carrier_root_only = {
        "Applicable Methodology/Carrier",
        "Applicable Methodology/Carrier Set",
        "Applicable Methodology/Projected Atom Carrier",
        "Applicable Methodology/Subject Index Carrier",
        "Artifact/Revision/Archive Carrier",
        "Atom/Claim/Carrier",
        "Atom/Claim/Target Scope Unit/Carrier",
        "Atom/Revision/Author/Frontmatter",
        "Atom/Revision/Authoritative Carrier Bundle",
        "Atom/Revision/Frontmatter",
        "Atom/Revision/Status/Carrier",
        "Framework Instance Settings/Revision Binding",
        "Project Settings/Revision Binding",
    }
    revision_root_only = {
        "Atom/Revision/Author",
        "Atom/Revision/Content",
        "Atom/Revision/History",
        "Atom/Revision/Identifier",
        "Atom/Revision/Reference",
        "Journal/Revision",
    }
    needs_technical_path_review = {
        "Applicable Methodology Compilation/Step",
        "Applicable Methodology Compilation/Step: assess",
        "Applicable Methodology Compilation/Step: correct",
        "Applicable Methodology Compilation/Step: decide",
        "Applicable Methodology Compilation/Step: propose",
        "Applicable Methodology Compilation/Step: publish",
        "Applicable Methodology Compilation/Step: select",
        "Applicable Methodology/Source Frontier Digest",
    }
    if identity == "Applicable Methodology/Sources/Installed Extensions":
        proposed.update(
            action="review_required",
            candidate_root=None,
            candidate_path=None,
            confidence_percent=85,
            operator_rules=["#/applicable_methodology/sources"],
            mapping_note=(
                "The candidate lists Installed Extensions as a source category, but the checked captured evidence only defines an Installed Extensions "
                "Catalog Entry and the accepted ledger has no global evidence key for a collection identity."
            ),
            question={
                "kind": "source_gap",
                "text": "Source review must locate captured Main Content that defines an Installed Extensions collection, or keep this as an Operator-candidate source category without a captured-node mapping.",
            },
        )
    elif identity in projection_context_only:
        proposed["candidate_root"] = None
        proposed["candidate_path"] = None
        proposed["mapping_note"] += " The candidate confirms the Projection context but does not assign it to one of the seven root display paths."
    elif identity in carrier_root_only:
        proposed["candidate_path"] = None
        proposed["mapping_note"] += " The Carrier root is explicit, but the candidate does not name a narrower Carrier subtype/property path."
    elif identity in revision_root_only:
        proposed["candidate_path"] = None
        proposed["mapping_note"] += " The separate Revision root is explicit, but the candidate does not name this dependent display path."
    elif identity in {"Artifact/Revision/Archive Carrier Basename", "Artifact/Revision/Version"}:
        proposed["candidate_root"] = None
        proposed["candidate_path"] = None
        proposed["mapping_note"] += " The candidate confirms that filename/path is not Carrier identity but does not adopt this exact delivery syntax."
    elif identity in {"Atom/Claim/Target Scope Unit", "Atom/Content Role: Plan/Type: Plan/Claim/Target Scope Unit"}:
        proposed["candidate_path"] = None
        proposed["mapping_note"] += " Scope Unit is an explicit root, but the candidate does not admit a Claim-target display path."
    elif identity == "Atom/Scope":
        proposed["candidate_path"] = None
        proposed["mapping_note"] += " The candidate directs Substance Scope semantics but does not name a full owner/property display path."
    elif identity in needs_technical_path_review:
        proposed.update(
            action="review_required",
            candidate_root=None,
            candidate_path=None,
            confidence_percent=85,
            mapping_note=(
                "The captured workflow-specific distinction has meaningful Main Content evidence, but the candidate supplies no named subtype/property "
                "or relation path for it. It is retained for technical mapping review rather than nested under a convenient Artifact path."
            ),
            question=None,
        )
    elif identity == "Applicable Methodology Compilation/Claim Transformation":
        proposed.update(
            action="projection_view",
            candidate_root=None,
            candidate_path=None,
            content_view="P",
            confidence_percent=95,
            operator_rules=["#/applicable_methodology/mapping", "#/projection_member_model"],
            mapping_note="The one-to-one candidate Projection explicitly forbids combining multiple source Atoms into one projected Atom; the candidate supplies no root display path for the workflow-specific transformation label.",
            question=None,
        )
    return proposed


def preserved(old: dict, evidence: list[dict], mapping_note: str) -> list[str]:
    values = list((old.get("proposal") or {}).get("preserved_distinctions", []))
    if not values:
        values.append("The exact checked captured Main Content remains the evidence basis; this comparison makes no native change.")
    values.append(mapping_note)
    for item in evidence:
        values.append(f"Captured {item['atom_id']} lines {item['line_span'][0]}-{item['line_span'][1]}: {item['quote']}")
    return values


def build_receipt() -> dict:
    input_data = json.loads(INPUT.read_text())
    ledger = json.loads(LEDGER.read_text())
    candidate = json.loads(CANDIDATE.read_text())
    assert hashlib.sha256(CANDIDATE.read_bytes()).hexdigest() == "99e7710f5ef83df2b1f3ec1ef4142547655e63bef7415266c5521380da7fa99b"
    assert candidate["status"] == "Candidate"
    assert len(input_data["nodes"]) == 62
    snapshot = load_snapshot_sources()

    old_by_identity = {
        mark["identity"]: mark
        for mark in ledger["node_disposition_marks"]
        if mark["scoped_refs"].get("batch") == 0
    }
    assert set(old_by_identity) == {row["identity"] for row in input_data["nodes"]}
    rows = []
    all_checked_atoms = set()
    all_verified_refs = set()
    for input_row in input_data["nodes"]:
        identity = input_row["identity"]
        mark = old_by_identity[identity]
        old = mark["review_row"]
        global_refs, verified, read_atoms = checked_evidence(ledger, mark, snapshot)
        proposed = constrain_to_evidenced_display_path(identity, mapping(identity))
        assert proposed["action"] in {
            "retain", "rebase", "inherit", "delivery_policy", "operation_or_method",
            "projection_view", "syntax_context", "drop_candidate", "review_required", "concrete_conflict",
        }
        if proposed["confidence_percent"] < 90:
            assert proposed["action"] in {"review_required", "concrete_conflict"}
            assert proposed["candidate_path"] is None
        row = {
            "identity": identity,
            "prior_disposition": old["disposition"],
            "action": proposed["action"],
            "candidate_root": proposed["candidate_root"],
            "candidate_path": proposed["candidate_path"],
            "content_view": proposed["content_view"],
            "confidence_percent": proposed["confidence_percent"],
            "reason": f"{old['reason']} Latest-candidate comparison: {proposed['mapping_note']}",
            "operator_rules": proposed["operator_rules"],
            "evidence_refs": global_refs,
            "checked_source_atom_ids": read_atoms,
            "preserved_distinctions": preserved(old, verified, proposed["mapping_note"]),
            "question": proposed["question"],
            "input_governing_source_atom_ids": input_row["governing_source_atom_ids"],
            "input_source_atom_ids": input_row["source_atom_ids"],
            "input_occurrence_ids": input_row["occurrence_ids"],
            "verified_captured_evidence": verified,
        }
        rows.append(row)
        all_checked_atoms.update(read_atoms)
        all_verified_refs.update(global_refs)

    assert len(rows) == len(input_data["nodes"]) == len({row["identity"] for row in rows})
    return {
        "schema_version": 1,
        "batch": 0,
        "kind": "Captured nodes against Operator candidate",
        "non_authoritative": True,
        "native_admission": "not_performed",
        "source_migration": "not_performed",
        "captured_core_commit": "a971d0e00c33c779f485fc8cad63194894d440fb",
        "candidate_sha256": sha256_file(CANDIDATE),
        "input_sha256": sha256_file(INPUT),
        "baseline_sha256": sha256_file(BASELINE),
        "prior_review_sha256": sha256_file(LEDGER),
        "review_method": (
            "Derived comparison of accepted prior reviewed meanings against verified captured-snapshot Main Content and the latest Operator candidate. "
            "Quoted evidence spans were re-read from immutable Git commit a971d0e00c33c779f485fc8cad63194894d440fb via nodes/support/snapshot_sources.py; "
            "this is not a current-Core audit, native admission, source migration, or exhaustive re-audit of all 951 pins. "
            "Latest Operator directions are recorded as proposed candidate changes and do not retroactively alter captured Core facts."
        ),
        "evidence_verification": {
            "source_context": "captured_snapshot",
            "verification": "pass",
            "verified_evidence_ref_count": len(all_verified_refs),
            "checked_source_atom_count": len(all_checked_atoms),
            "snapshot_reader": "nodes/support/snapshot_sources.py:read_source",
        },
        "nodes": rows,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--persist", action="store_true", help="create the receipt only when absent; verify byte identity when present")
    args = parser.parse_args()
    rendered = json.dumps(build_receipt(), indent=2, ensure_ascii=False) + "\n"
    if not args.persist:
        print(rendered, end="")
        return
    if OUTPUT.exists():
        assert OUTPUT.read_text() == rendered, f"refusing to overwrite non-identical {OUTPUT}"
        print(json.dumps({"output": str(OUTPUT), "persistence": "verified_byte_identical"}))
        return
    OUTPUT.write_text(rendered)
    print(json.dumps({"output": str(OUTPUT), "persistence": "created"}))


if __name__ == "__main__":
    main()
