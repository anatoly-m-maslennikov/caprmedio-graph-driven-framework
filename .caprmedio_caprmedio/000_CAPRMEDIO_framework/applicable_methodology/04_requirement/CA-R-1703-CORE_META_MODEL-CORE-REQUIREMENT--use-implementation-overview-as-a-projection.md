---
subjects:
  governs: "Entity/Continuant/Projection/Type: Implementation Overview"
  depends_on:
    ["Entity/Continuant/Projection", "Entity/Continuant/Object/Atom", "Artifact", "Implementation Binding", "Entity/Continuant/History/Journal", "Implementation", "Verification", "Atom/Content Role"]
version: 20
updated_at: "2026-10-15 18:45:28 +0000"
relations: {}
atom_id: "CA-R-1703"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/04_requirement/CA-R-1703-CORE_META_MODEL-CORE-REQUIREMENT--use-implementation-overview-as-a-projection.md
  source_atom_id: CA-R-1703
  source_atom_revision: 20
  source_sha256: 551ba6f64e4036650a7adc83b3f20cd4809f6d56a083a1a0e2c289a9f91ec0a4
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Use Implementation Overview as a Projection

## Scope

Implementation Overview Projections.

## Claim

an Implementation Overview is a non-authoritative Projection of what the current normative Atom frontier, native project targets, available provenance, **and** **any** registered implementation lineage sources show as implemented. its Implementation Bindings derive from the shared Project Journal under CA-R-1695; the current view does **not** replace the historical implementation event records retained **in** that Journal. the Atom Content Role axis does **not** apply **to** this Projection.

it **may** report realization coverage, source-to-target bindings, relevant commits, **and** unresolved implementation gaps. it is regenerated mechanically **or** rebuilt through governed reasoning from its declared source frontier. it is never an Atom **and** cannot replace the Journal, normative Atoms, native implementation, Operations evidence, **or** Verification.

the presence of this Projection does **not** require an internal Implementation Atom. storage, retention, **and** whether the Projection is committed **or** generated at runtime remain governed separately.

## Primary claim

CAPRMEDIO represents the current view of project realization through an Implementation Overview Projection rather than an Implementation Atom.

## Details
