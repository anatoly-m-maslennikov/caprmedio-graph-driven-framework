---
atom_id: CA-P-1841
content_role: Plan
type: Plan
label: Task
work_sequence_number: 12
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
status: Done
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-09 01:12:07 +0400"
subjects:
  governs: "CAPRMEDIO Framework Instance"
  depends_on:
    - "Project"
    - "Project Settings"
    - "Project Structure"
    - "Framework Instance Settings"
    - "Tool"
    - "Action"
    - "Workflow Run"
    - "Carrier"
    - "Evaluation"
    - "AI Agent"
    - "Operator"
relations:
  is_decomposition_of:
    - CA-P-1829
  blocks:
    - CA-P-1842
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
