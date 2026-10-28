---
subjects:
  governs: 'Subject/Graph Relation/Type: NARROWER_THAN'
  depends_on:
  - Subject/Graph Node/Domain/Continuant/Term
  - 'Subject/Graph Node/Domain/Continuant/Projection/Type: Terms Graph'
  - Subject/Graph Relation
  - Subject/Graph Node/Domain/Continuant/Term//Property
version: 20
updated_at: 2026-10-26 17:20:40 +0400
relations: {}
atom_id: CA-R-1435@20
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 1
type: Definition
---
# Summary

Define NARROWER_THAN

## Scope

the NARROWER_THAN Relation **in** the Terms Graph.

## Claim

a NARROWER_THAN Relation from Term A **to** Term B **in** the Terms Graph **means** that, under their governing definitions, **if** Term A applies **to** a referent, **then** Term B applies **to** the same referent; this Relation does **not** express Property ownership **or** allowed-value membership.

## Semantics

Specialization and bearer dependence are distinct. A dependent kind can itself have narrower kinds. NARROWER_THAN does not establish that either endpoint is primary and does not substitute for IS_BORNE_BY.
