---
atom_id: CA-P-1850
content_role: Plan
type: Plan
label: Task
work_sequence_number: 2
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
status: Active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-09 15:41:25 +0400"
subjects:
  governs: "CAPRMEDIO Framework Instance"
  depends_on:
    - "Project"
    - "Plan"
    - "AI Agent"
    - "Operator"
    - "Framework Instance Settings"
    - "Journal"
    - "Workflow Run"
    - "Action"
    - "Workflow"
    - "Framework Package"
    - "Carrier"
relations:
  is_decomposition_of:
    - CA-P-1848
  blocks:
    - CA-P-1855
---
# Summary

Protect existing state during installation migration

## Objective

the AI Agent supplies a verified migration that preserves existing operational state while `.caprmedio_install` becomes the beta package boundary.

## Details

- scope: the installation/release contribution of the CAPRMEDIO Framework Instance delivered by the caprmedio Project.
- input: existing `.caprmedio_install/project_mcp`, `mcp_hot_reload`, `workflow_orchestrator` **and** related databases, locks, receipts, history **and** pending work.
- first repair `INSTALL_TOOLS/install_tools.py` whole-directory legacy deletion; installer execution **must not** remove live state, historical evidence, credentials **or** unrelated contents. use explicit owned-path admission rather than a directory sweep.
- implement **and** test quiescing, exact source/target inventories, migration into selected-Project `.caprmedio_runtime`, state-reader/selector updates, resumability **and** rollback. preserve Journal records **and** historical references; interrupted Runs remain honestly recorded, **not** passed **or** automatically replayed.
- stage the migration **and** exercise it **only** against disposable fixtures during preparation. actual Project state moves occur **in** the local release Workflow **after** its full-suite gate passes.
- unmapped **or** protected contents need an explicit retention/disposition decision. test initial failure, interrupted migration, repeated invocation, current-state recovery **and** preservation of another Project.
- effort: own work for **=1** AI Agent **must** fit **<=15** minutes. **if** this Plan needs larger own work, decompose it **before** execution **and** preserve its Objective **and** acceptance.
- control: use applicable Operator input **and** inherited Framework Instance Settings for permission, confidence **and** retry gates. creation is planned work **only**, **not** permission to execute the local/public cycle immediately.

### Definition of Done

the Plan is **not** Done **if** legacy installation can delete operational state, an existing record is lost **or** rewritten as successful, migration cannot resume/rollback, **or** live cutover occurs **before** the local release gate.
