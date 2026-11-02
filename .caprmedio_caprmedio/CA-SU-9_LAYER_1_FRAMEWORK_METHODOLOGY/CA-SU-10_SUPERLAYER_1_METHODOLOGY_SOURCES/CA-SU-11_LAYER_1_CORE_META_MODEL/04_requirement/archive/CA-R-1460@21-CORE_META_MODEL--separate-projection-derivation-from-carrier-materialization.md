---
subjects:
  governs: Entity/Object/Continuant/Projection
  depends_on:
  - Entity/Carrier
  - Entity/Object/Continuant/Projection/Type
  - Entity/Object/Continuant/Governing Objects/Atom.Content
version: 21
updated_at: 2026-10-29 10:13:48 +0400
relations: {}
atom_id: CA-R-1460@21
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 1
type: Rule
---
## Summary

Separate Projection derivation from Carrier materialization

## Claim scope

the derivation of a Projection and its Carrier materialization.

## Claim

the governing derivation logic of a Projection **must** remain distinct from its Carrier materialization strategy. whether **and** how its result is represented **or** persisted **in** Carriers does **not**, by itself, define the transformation **or** content-preservation behavior of that derivation, its semantic Type, **or** its refresh behavior; those remain determined by their applicable governing Claims. describing a derivation as direct **or** content-preserving does **not** select a persistence strategy.
