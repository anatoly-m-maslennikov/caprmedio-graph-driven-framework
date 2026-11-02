---
atom_id: CA-P-2473
content_role: Plan
type: Plan
label: Task
work_sequence_number: 2
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
author: Anatoly Maslennikov
status: Active
subjects:
  governs: Entity/Node/Continuant/Atom
  depends_on: []
relations:
  is_decomposition_of: [CA-P-2463]
version: 1
updated_at: "2026-10-20T18:33:14.454Z"
---
# Summary

Reject reviewed Draft YAML Version drift

## Objective

Close the independent finding that a qualified Draft marker could disagree with carried YAML Version yet be normalized to a valid candidate.

## Details

At most 15 minutes own work; split before extending. Require marker proposed Version to equal carried YAML Version before candidate normalization. Preserve the already reviewed ID-free/empty-number support and exact source/draft bindings. This is a separate bounded follow-up after P2471 ID-free compatibility.

### Definition of Done

Focused synthetic-project checks and independent review verify the stated behavior without live MCP tests, deployment, migration, or held-batch replay. Review dependent next Task before acceptance execution.
