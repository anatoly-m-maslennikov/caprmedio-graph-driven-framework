---
subjects:
  governs: Entity/Graph Syntax > Relation//NARROWER_THAN
  depends_on:
  - Entity/Object/Continuant/Term
  - 'Entity/Object/Continuant/Projection/Type: Terms Graph'
  - Entity/Graph Syntax > Relation
  - Entity/Object/Continuant/Term//Property
version: 23
updated_at: 2026-10-29 07:45:26 +0400
relations: {}
atom_id: CA-R-1435@23
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 1
type: Relation Definition
---
## Summary

Define NARROWER_THAN

## Claim scope

the NARROWER_THAN Relation **in** the Terms Graph.

## Claim

a NARROWER_THAN Relation from Term A **to** Term B **in** the Terms Graph **means** that, under their governing definitions, **if** Term A applies **to** a referent, **then** Term B applies **to** the same referent; this Relation does **not** express Property ownership **or** allowed-value membership.

## Semantics

Specialization and bearer dependence are distinct. A dependent kind can itself have narrower kinds. NARROWER_THAN does not establish that either endpoint is primary and does not substitute for IS_BORNE_BY.
