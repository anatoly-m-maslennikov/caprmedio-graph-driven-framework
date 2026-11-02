---
subjects:
  governs: "Entity/Node/Occurrent/Execution/Workflow Run"
  depends_on:
    ["Entity/Node/Continuant/Atom/Content Role: Operations/Type: Workflow", "Entity/Node/Occurrent/Execution/Step Run", "Entity/Node/Continuant/History/Journal.Record"]
version: 8
updated_at: "2026-10-19 15:53:19 +0400"
relations: {}
atom_id: CA-R-1510@8
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: Archived
author: "Anatoly Maslennikov"
global_tier: 9
---
# Summary

Define Workflow Run

## Scope

the Workflow Run entity.

## Claim

a Workflow Run **means** **`=1`** actual execution of **`=1`** Workflow against the inputs **and** parameters supplied for that run.

## Details

- the execution follows the Workflow's typed Relations **and** retains its actual Step Runs, outcomes, **and** applicable retry allowance.
- the run is distinct from the reusable Workflow **and** from the Journal Records that describe its execution. a reference **to** the definition does **not** prove that a run occurred.
