---
subjects:
  governs: 'Subject/CAPRMEDIO/Graph/Relation/Type: NARROWER_THAN'
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Term
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Projection/Type: Terms Graph'
  - Subject/CAPRMEDIO/Graph/Relation
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Term//Property
version: 21
updated_at: 2026-10-27 19:59:54 +0400
relations: {}
atom_id: CA-R-1435
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
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
