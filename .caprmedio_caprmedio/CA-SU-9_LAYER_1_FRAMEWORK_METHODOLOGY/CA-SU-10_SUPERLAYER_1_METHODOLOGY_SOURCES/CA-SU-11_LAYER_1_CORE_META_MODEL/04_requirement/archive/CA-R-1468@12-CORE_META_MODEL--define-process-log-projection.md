---
subjects:
  governs: 'Subject/Domain/Node/Continuant/Projection/Type: Process Log'
  depends_on:
  - Subject/Domain/Node/Occurrent/Execution/Step Run
  - Subject/Domain/Node/Occurrent/Execution/Workflow Run
  - Subject/Domain/Node/Continuant/Projection
  - Subject/Domain/Node/Continuant/History/Journal
  - Subject/Domain/Node/Continuant/History/Journal.Record
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Action'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Workflow'
version: 12
updated_at: 2026-10-23 03:14:50 +0400
relations: {}
atom_id: CA-R-1468@12
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Standard
status: Archived
author: Anatoly Maslennikov
global_tier: 11
---
# Summary

Define Process Log Projection

## Scope

the Process Log Projection Type.

## Claim

a Process Log **means** a non-authoritative Projection of the Project Journal that presents recorded Workflow Runs, Step Runs, **and** Action executions using their recorded execution associations, progress, **and** outcomes. it includes recorded executions **without** Artifact changes **and** does **not** infer an unrecorded execution association **or** successful outcome.

## Details
