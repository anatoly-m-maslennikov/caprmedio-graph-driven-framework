---
atom_id: CA-P-1837
content_role: Plan
type: Plan
label: Task
work_sequence_number: 8
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
status: Done
author: Anatoly Maslennikov
version: 9
updated_at: 2026-10-25 17:32:27 +0400
subjects:
  governs: Subject/Graph Node/Engineering/Occurrent/Runtime/Docker Persistent-State Carrier
  depends_on:
  - Subject/Graph Node/Domain/Continuant/Project
  - Subject/Graph Node/Domain/Continuant/Project.Settings
  - Subject/Graph Node/Domain/Continuant/Project.Structure
  - Subject/Graph Node/Domain/Continuant/Project.Framework Settings
  - Subject/Graph Node/Engineering/Continuant/Tool
  - Subject/Graph Node/Engineering/Action
  - Subject/Graph Node/Domain/Occurrent/Execution/Workflow Run
  - Subject/Graph Node/Engineering/Continuant/Carrier
  - Subject/Graph Node/Engineering/Implementation Evaluation
  - 'Subject/Graph Node/Domain/Continuant/Actor/Type: AI Agent'
  - 'Subject/Graph Node/Domain/Continuant/Actor/Type: Operator'
relations:
  is_decomposition_of:
  - CA-P-1829
  blocks:
  - CA-P-1840
tier: 3
---
# Summary

Isolate runtime state by selected Project

## Objective

the AI Agent binds container naming, persistent state, **and** declared mounts **to** the selected Project identity.

## Details

- input: the shared selector **and** runtime state **and** Compose configuration under `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/WORKFLOW_ORCHESTRATOR`, plus MCP reload storage **in** `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/204_MCP/hot_reload.py`.
- output: per-Project Compose **and** state namespaces that separate locks, transport metadata, credentials, queues, MCP reload receipts/pending/cache storage, **and** declared authority bindings; use the accepted mount boundary.
- verification: compare two selected Projects **in** one repository **and** two repositories; writing one instance's state leaves the other instance's state unchanged.
- effort: **`<=15`** minutes for **`=1`** AI Agent; the Epic's decomposition rule applies **before** execution **if** the estimate no longer holds.

### Definition of Done

- completion evidence: shared selection-derived Compose, launcher **and** reload namespaces **and** the standalone endpoint-only mount declaration are implemented. 2 state/mount tests passed, including a left-only same-ID receipt leaving the other nested Project unchanged.

the Plan is **not** Done **if** ((two selected Projects share mutable runtime state) **or** (the resulting mounts exceed the accepted Project boundary) **or** (the namespace/isolation tests fail)).
