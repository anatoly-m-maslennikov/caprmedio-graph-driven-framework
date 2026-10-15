---
subjects:
  governs: "Projection/Type: Process Log"
  depends_on:
    ["Execution/Step Run", "Execution/Workflow Run", "Projection", "Journal", "Journal.Record", "Action", "Workflow"]
version: 7
updated_at: "2026-10-15 12:12:29 +0000"
relations: {}
atom_id: "CA-R-1468@draft"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Draft"
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
