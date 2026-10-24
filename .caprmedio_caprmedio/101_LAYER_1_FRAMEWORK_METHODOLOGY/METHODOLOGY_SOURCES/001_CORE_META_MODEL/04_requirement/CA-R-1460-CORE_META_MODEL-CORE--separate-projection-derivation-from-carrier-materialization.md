---
subjects:
  governs: Subject/Domain/Node/Continuant/Projection
  depends_on:
  - Subject/Engineering/Carrier
  - Subject/Domain/Node/Continuant/Projection/Type
  - Subject/Domain/Node/Continuant/Atom.Substance
version: 13
updated_at: 2026-10-24 01:37:42 +0400
relations: {}
atom_id: CA-R-1460
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
tier: 1
type: Rule
---
# Summary

Separate Projection derivation from Carrier materialization

## Scope

the derivation of a Projection and its Carrier materialization.

## Claim

the governing derivation logic of a Projection **must** remain distinct from its Carrier materialization strategy. whether **and** how its result is represented **or** persisted **in** Carriers does **not**, by itself, define the transformation **or** content-preservation behavior of that derivation, its semantic Type, **or** its refresh behavior; those remain determined by their applicable governing Claims. describing a derivation as direct **or** content-preserving does **not** select a persistence strategy.

## Details
