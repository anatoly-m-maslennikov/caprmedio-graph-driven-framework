---
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Project Model/Execution/Workflow Run
  depends_on:
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Workflow'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Execution/Step Run
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal.Record
version: 16
updated_at: 2026-10-27 19:59:56 +0400
relations: {}
atom_id: CA-R-1510
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
tier: 1
type: Definition
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
