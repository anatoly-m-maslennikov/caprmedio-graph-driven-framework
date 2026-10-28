---
subjects:
  governs: 'Subject/CAPRMEDIO/Graph/Node/Project Model/Projection/Type: Process Log'
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Execution/Step Run
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Execution/Workflow Run
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Projection
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal.Record
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Action'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Workflow'
version: 17
updated_at: 2026-10-27 19:59:55 +0400
relations: {}
atom_id: CA-R-1468
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
tier: 3
type: Definition
---
# Summary

Define Process Log Projection

## Scope

the Process Log Projection Type.

## Claim

a Process Log **means** a non-authoritative Projection of the Project Journal that presents recorded Workflow Runs, Step Runs, **and** Action executions using their recorded execution associations, progress, **and** outcomes. it includes recorded executions **without** Artifact changes **and** does **not** infer an unrecorded execution association **or** successful outcome.

## Details
