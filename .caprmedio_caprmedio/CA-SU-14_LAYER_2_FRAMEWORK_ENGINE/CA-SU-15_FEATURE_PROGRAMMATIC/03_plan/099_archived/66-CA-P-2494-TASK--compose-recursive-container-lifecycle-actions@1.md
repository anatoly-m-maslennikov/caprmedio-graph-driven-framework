---
atom_id: CA-P-2494
content_role: Plan
type: Plan
label: Task
work_sequence_number: 66
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
author: Anatoly Maslennikov
status: Backlog
subjects:
  governs: Entity/Node/Continuant/Atom
  depends_on: []
relations:
  is_decomposition_of: [CA-P-2401]
version: 1
updated_at: "2026-10-20T20:50:22.352Z"
---
# Summary

Compose recursive container lifecycle Actions

## Objective

Apply the latest always-recursive container lifecycle rule without adding an optional mode.

## Details

At most 15 minutes own work; split before extending. Depends on reconciled R1521/D461/E502 and the P2485 carrier-safety guard. Reuse the existing calling Workflow: resolve containment once from latest Atom revisions, compose independent guarded child Actions before a parent relocation would silently move a current child, and stop truthfully on first failure without cross-Atom rollback. Archive all contained latest Atoms, including Done Plans. For a requested parent Status Done, leave Done Plan descendants unchanged and request Canceled for other contained latest Plans. Preserve older history and external references; do not infer carried Status from paths. Inspect existing implementation boundaries first and split before exceeding the estimate. No per-child human confirmation or new generic orchestrator.

### Definition of Done

Focused synthetic-project checks and independent review verify the stated behavior without live MCP tests, deployment, migration, or held-batch replay. Review dependent next Task before acceptance execution.
