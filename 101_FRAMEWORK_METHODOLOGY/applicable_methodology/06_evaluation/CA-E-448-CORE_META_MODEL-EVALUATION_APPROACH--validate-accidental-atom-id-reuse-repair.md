---
subjects:
  governs: "Entity/Node/Continuant/Atom.ID"
  depends_on:
    ["Entity/Node/Continuant/Atom.ID", "Atom/Content Role", "Entity/Node/Continuant/Atom.Substance", "Atom Scope", "Entity/Node/Continuant/Atom", "Entity/Node/Continuant/History/Revision/Type: Atom", "Entity/Carrier.Canonical Address", "Entity/Node/Continuant/Project", "Entity/Node/Continuant/Actor/Type: Operator", "Confidence Threshold", "Entity/Node/Continuant/History/Journal"]
version: 12
updated_at: "2026-10-19 15:55:01 +0400"
relations:
  evaluation_for:
    - CA-M-276
atom_id: "CA-E-448"
content_role: "Evaluation"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
type: "Evaluation Approach"
global_tier: 11
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/06_evaluation/CA-E-448-CORE_META_MODEL-EVALUATION_APPROACH--validate-accidental-atom-id-reuse-repair.md
  source_atom_id: CA-E-448
  source_atom_revision: 12
  source_sha256: 4f35cd0bac1fb9a558fc77a8f5d6c60d0b808966b50e2ded4baed90933689141
  original_relations_sha256: bac80633f7ceae4c33d069bb745b62b44460833c47bbcf9f7f698fad1015abce
---
# Summary

Validate accidental Atom ID reuse repair

## Scope

Atom ID collision repairs.

## Claim

the Evaluation **must** reject completion of an Atom ID collision repair under CA-M-276-CORE_META_MODEL-METHOD--repair-accidental-atom-id-reuse **if** **any** of:

- the original owner was selected **without** sufficient recorded assignment evidence **or** the required Operator decision, **or** its valid Atom ID changed.
- a later accidental reuse retains the colliding ID, receives a previously used number, **or** receives an ID outside its Project prefix **and** Content Role sequence.
- an affected Claim, Content Role, Atom Scope, Claim Target Scope Unit, **or** textual Claim Scope changes beyond the approved identity-reference correction, a distinct Claim is lost **or** merged, **or** an unrelated identity changes.
- a prior Revision **or** historical Record is rewritten, history becomes unreachable, **or** the Work Journal lacks the exact mapping between the historical Carrier **and** its corrected identity.
- an affected current reference resolves ambiguously, remains unresolved, **or** resolves **to** a different intended Claim; an uncertain reference is rebound **without** the required Operator decision.
- legitimate same-Atom Revisions **or** derived copies are renumbered as accidental reuse, **or** lookup **or** compilation silently selects an identity winner.

the Evaluation **must** distinguish a paused collision awaiting an Operator decision from a completed repair. its checks **must** cover the verified-original-owner case, reversed Carrier discovery order, an unknown original owner, an ambiguous incoming reference, **and** legitimate same-Atom Revisions **or** derived copies.

## Details
