---
subjects:
  governs: 'Entity/Object/Continuant/Projection/Type: Process Log'
  depends_on:
  - Entity/Object/Occurrent/Execution/Step Run
  - Entity/Object/Occurrent/Execution/Workflow Run
  - Entity/Object/Continuant/Projection
  - Entity/Object/Continuant/History/Journal
  - Entity/Object/Continuant/History/Journal > Event Record
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type: Action'
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type: Workflow'
version: 18
updated_at: 2026-10-29 07:17:17 +0400
relations: {}
atom_id: CA-R-1468@18
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
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
