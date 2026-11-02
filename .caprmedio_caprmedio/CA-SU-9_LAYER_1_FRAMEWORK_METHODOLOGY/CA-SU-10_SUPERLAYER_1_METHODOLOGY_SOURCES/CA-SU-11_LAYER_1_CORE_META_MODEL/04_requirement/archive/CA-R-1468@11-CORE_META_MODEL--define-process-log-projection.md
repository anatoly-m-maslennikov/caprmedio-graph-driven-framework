---
subjects:
  governs: 'Entity/Node/Continuant/Projection/Type: Process Log'
  depends_on:
  - Entity/Node/Occurrent/Execution/Step Run
  - Entity/Node/Occurrent/Execution/Workflow Run
  - Entity/Node/Continuant/Projection
  - Entity/Node/Continuant/History/Journal
  - Entity/Node/Continuant/History/Journal.Record
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Action'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Workflow'
version: 11
updated_at: 2026-10-23 03:06:32 +0400
relations: {}
atom_id: CA-R-1468@11
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: Archived
author: "Anatoly Maslennikov"
global_tier: 11
---
# Summary

Define Process Log Projection

## Scope

the Process Log Projection Type.

## Claim

a Process Log **means** a non-authoritative Projection of the Project Journal that presents recorded Workflow Runs, Step Runs, **and** Action executions using their recorded execution associations, progress, **and** outcomes. it includes recorded executions **without** Artifact changes **and** does **not** infer an unrecorded execution association **or** successful outcome.

## Details
