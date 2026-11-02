---
subjects:
  governs: 'Entity/Object/Continuant/Projection/Type: Implementation Overview'
  depends_on:
  - Entity/Object/Continuant/Projection
  - Entity/Object/Continuant/Governing Objects/Atom
  - Entity/Object/Continuant/Term//Artifact
  - Entity/Aspect/Engineering/Traceability
  - Entity/Object/Continuant/History/Journal
  - Entity/Object/Continuant/Package/Project Implementation
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Evaluation'
  - Entity/Object/Continuant/Governing Objects/Atom/Content Role
version: 36
updated_at: 2026-10-29 10:13:49 +0400
relations: {}
atom_id: CA-R-1703
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
tier: 1
type: Rule
---
## Summary

Use Implementation Overview as a Projection

## Claim scope

Implementation Overview Projections.

## Claim

an Implementation Overview is a non-authoritative Projection of what the current normative Atom frontier, native project targets, available provenance, **and** **any** registered implementation lineage sources show as implemented. its Implementation Bindings derive from the shared Project Journal under CA-R-1695; the current view does **not** replace the historical implementation event records retained **in** that Journal. the Atom Content Role axis does **not** apply **to** this Projection.

it **may** report realization coverage, source-to-target bindings, relevant commits, **and** unresolved implementation gaps. it is regenerated mechanically **or** rebuilt through governed reasoning from its declared source frontier. it is never an Atom **and** cannot replace the Journal, normative Atoms, native implementation, Operations evidence, **or** Verification.

the presence of this Projection does **not** require an internal Implementation Atom. storage, retention, **and** whether the Projection is committed **or** generated at runtime remain governed separately.

## Primary claim

CAPRMEDIO represents the current view of project realization through an Implementation Overview Projection rather than an Implementation Atom.
