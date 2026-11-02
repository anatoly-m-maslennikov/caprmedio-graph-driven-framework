---
atom_id: CA-R-1616@14
content_role: Requirement
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: 'Subject/Graph Node/Domain/Continuant/Projection/Type: Realization Graph'
  depends_on:
  - Subject/Graph Node/Engineering/Execution Identity/Source Binding
  - Subject/Graph Node
  - Subject/Graph Node/Engineering/Graph Projection
  - Subject/Graph Node/Domain/Continuant/History/Journal
  - Subject/Graph Node/Domain/Continuant/Projection
  - Subject/Graph Relation
version: 14
updated_at: 2026-10-25 17:32:27 +0400
relations:
  relates_to:
  - CA-R-1470
  - CA-R-1493
  - CA-R-1494
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
