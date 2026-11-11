---
atom_id: CA-P-1841
ref_id: CA-P-1841
container:
  atom: CA-P-1829
role: Plan
form: Plan
label: Task
topics:
  main_subject: Subject/Graph Node/Engineering/Occurrent/Runtime/Docker Runtime
  dependencies:
  - Subject/Graph Node/Domain/Continuant/Project
  - Subject/Graph Node/Domain/Continuant/Project.Settings
  - Subject/Graph Node/Domain/Continuant/Project.Structure
  - Subject/Graph Node/Domain/Continuant/Project.Framework Settings
  - Subject/Graph Node/Engineering/Continuant/Tool
  - Subject/Graph Node/Engineering/Action
  - Subject/Graph Node/Domain/Occurrent/Execution/Workflow Run
  - Subject/Graph Node/Engineering/Continuant/Carrier
  - Subject/Graph Node/Engineering/Evaluation
  - 'Subject/Graph Node/Domain/Continuant/Actor/Type: AI Agent'
  - 'Subject/Graph Node/Domain/Continuant/Actor/Type: Operator'
tier: 3
relations:
  is_decomposition_of:
  - CA-P-1829
  blocks:
  - CA-P-1842
status: Done
version: 8
updated_at: 2026-10-25 17:32:27 +0400
carrier_destination:
  file:
    name: 12-CA-P-1841-TASK--reuse-healthy-project-runtimes-safely.md
    path: .caprmedio_caprmedio/03_plan/020_done/16-CA-P-1829-EPIC--launch-isolated-project-mcp-runtimes/020_done
work_sequence_number: 12
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
author: Anatoly Maslennikov
---
# Summary

Reuse healthy Project runtimes safely

## Objective

the AI Agent implements serialized startup **and** idempotent healthy-runtime reuse.

## Details

- input: the selected-Project namespace, image **and** publication readers, **and** startup golden tests.
- output: one per-Project startup lock **and** reconciliation path that returns an existing matching healthy container **or** performs the admitted new startup; mismatches **and** unhealthy state follow the accepted unchanged/failure contract.
- verification: repeat **and** race the same Project request; preserve the healthy container ID **and** port. startup does **not** replay queued Workflow Runs **or** silently upgrade a running image.
- effort: **`<=15`** minutes for **`=1`** AI Agent; the Epic's decomposition rule applies **before** execution **if** the estimate no longer holds.

### Definition of Done

- completion evidence: real flock contention **and** concurrent startup tests passed; the same Project starts once, then reuses the healthy matching container without replacement.

the Plan is **not** Done **if** ((repeat startup force-recreates a healthy matching container) **or** (concurrent requests create duplicate runtimes) **or** (reuse/mismatch tests fail)).
