---
atom_id: CA-R-1616
content_role: Requirement
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
author: Anatoly Maslennikov
status: Active
subjects:
  governs: 'Subject/CAPRMEDIO/Graph/Node/Project Model/Projection/Type: Realization Graph'
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Traceability
  - Subject/CAPRMEDIO/Graph/Node
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Projection/Type: Realization Graph'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Projection
  - Subject/CAPRMEDIO/Graph/Relation
version: 17
updated_at: 2026-10-27 19:59:59 +0400
relations:
  depends_on:
  - CA-R-1493
  - CA-R-1568
  - CA-R-1746
tier: 3
type: Definition
---
# Summary

Define Realization Graph

## Scope

Realization Graphs derived from a declared selection of existing Implementation sources and available evidence.

## Claim

Realization Graph **means** a non-authoritative Projection of Entities **and** typed Relations derived from a declared selection of existing Implementation sources **and** available evidence, used **to** understand that Implementation **and** support reverse engineering into proposed RMED.

- the Projection **must** retain source traceability under CA-R-1746 **and** generation identity under CA-R-1493, using **only** the source kinds selected for the job; legacy Implementation need **not** have pre-existing RMED **or** Journal records.
- missing evidence **and** uncertain interpretations **must** be reported. observed structure **or** behavior does **not** establish intended Requirements, a passed Evaluation, **or** completeness outside the checked selection.
- the Artifact kind remains Projection, including **when** delivered as an Implementation output under CA-R-1568. views derive from its source-backed facts **without** creating another source of truth.

## Details
