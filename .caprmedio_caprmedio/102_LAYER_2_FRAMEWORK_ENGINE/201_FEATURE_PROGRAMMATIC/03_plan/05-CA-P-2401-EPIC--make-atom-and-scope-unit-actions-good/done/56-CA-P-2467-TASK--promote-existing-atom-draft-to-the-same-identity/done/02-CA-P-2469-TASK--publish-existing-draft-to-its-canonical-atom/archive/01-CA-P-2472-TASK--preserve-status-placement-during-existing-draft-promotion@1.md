---
atom_id: CA-P-2472
content_role: Plan
type: Plan
label: Task
work_sequence_number: 1
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
  is_decomposition_of: [CA-P-2469]
version: 1
updated_at: "2026-10-20T18:33:14.452Z"
---
# Summary

Preserve Status placement during existing Draft promotion

## Objective

Complete destination-aware canonical publication and verified rollback when a non-Active Current Plan is promoted to Active using a reviewed Draft.

## Details

At most 15 minutes own work; split before extending. P2469 partial checkpoint passed Active same-ID V4 publication/exact V3 archive, no-op preservation and injected Draft-cleanup recovery. Reuse the status/bundle owner, preserve children and source pins, do not copy Draft companion trees or invent relation policy.

### Definition of Done

Focused synthetic-project checks and independent review verify the stated behavior without live MCP tests, deployment, migration, or held-batch replay. Review dependent next Task before acceptance execution.
