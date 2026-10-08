---
atom_id: CA-P-1837
content_role: Plan
type: Plan
label: Task
work_sequence_number: 8
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
status: Active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-08 23:56:13 +0400"
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
    - CA-P-1840
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

the Plan is **not** Done **if** ((two selected Projects share mutable runtime state) **or** (the resulting mounts exceed the accepted Project boundary) **or** (the namespace/isolation tests fail)).
