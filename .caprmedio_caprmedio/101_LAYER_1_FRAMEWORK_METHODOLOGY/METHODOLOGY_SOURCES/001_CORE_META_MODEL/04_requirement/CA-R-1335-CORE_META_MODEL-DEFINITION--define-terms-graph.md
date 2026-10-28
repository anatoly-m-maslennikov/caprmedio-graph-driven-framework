---
subjects:
  governs: 'Subject/CAPRMEDIO/Graph/Node/Project Model/Projection/Type: Terms Graph'
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Projection
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Term
  - Subject/CAPRMEDIO/Graph/Relation/Type
  - Subject/CAPRMEDIO/Graph/Relation
version: 27
updated_at: 2026-10-27 19:59:53 +0400
relations: {}
atom_id: CA-R-1335
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
tier: 1
type: Definition
---
# Summary

Define Terms Graph

## Scope

Terms Graph projections **and** their represented graph facts.

## Claim

Terms Graph **means** the Type value under Projection whose instances are derived CAPRMEDIO Graphs with native Term nodes **and** edges representing Relations using shared project-unique Relation Types under that graph's applicable governing authority, with any applicable Graph Rule constraints preserved. their represented facts retain their appropriate source authority under CA-R-1746.

## Details

admitted external graph **or** source references under CA-R-1472 do **not** become native Term nodes merely by being referenced. those references retain their own endpoint classes, shared Relation Type identity, any graph-qualified reference **or** context, **and** source traceability.
