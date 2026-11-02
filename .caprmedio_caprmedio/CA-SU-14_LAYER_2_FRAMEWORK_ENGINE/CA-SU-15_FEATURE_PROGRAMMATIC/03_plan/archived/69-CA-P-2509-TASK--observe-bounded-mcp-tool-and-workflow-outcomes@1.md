---
atom_id: CA-P-2509
content_role: Plan
type: Plan
label: Task
work_sequence_number: 69
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
author: Anatoly Maslennikov
status: Backlog
subjects:
  governs: Entity/Node/Continuant/Implementation
  depends_on: []
relations:
  is_decomposition_of: [CA-P-2401]
version: 1
updated_at: "2026-10-21 04:06:25 +0400"
---
# Summary

Observe bounded MCP Tool and Workflow outcomes

## Objective

Capture recent real calls and Workflow observations at the existing Gateway boundary.

## Details

At most 15 minutes own work; split before extending. Depends on reviewed P2508. Own only bounded process-local observations and narrow Gateway hooks. Keep no more than 32 Tool observations and 32 Workflow observations, with since-start coverage explicit. Preserve returned domain outcome, uncertain no-replay behavior and separate scheduler status from actual Workflow outcome. No raw arguments/results, paths, credentials or provider exception text. Acceptance: truthful success/rejection/error/uncertain and empty/eviction cases; no redispatch or DBOS/Docker query from health.
