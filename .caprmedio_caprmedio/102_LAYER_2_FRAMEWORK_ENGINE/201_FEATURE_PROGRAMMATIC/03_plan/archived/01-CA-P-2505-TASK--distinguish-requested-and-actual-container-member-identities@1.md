---
atom_id: CA-P-2505
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
  is_decomposition_of: [CA-P-2501]
version: 1
updated_at: "2026-10-20T21:52:10.009Z"
---
# Summary

Distinguish requested and actual container member identities

## Objective

Align technical coordinator aggregate observation with actual canonical Run evidence.

## Details

At most 15 minutes own work; split before extending. Own backend.py and its focused container status tests after initial freeze. Use failed mapping or null consistently with composition. Expose parent_requested_run_id separately from nullable actual parent_run_id, and requested member identities separately from evidence-backed actual_run_id. Completed identities require actual evidence; untouched entries are requested identities. No planned ID may be presented as a started Source Run. Validate marked aggregates and preserve truthful partial/uncertain status, ordinary behavior and direct-enqueue scope guard. Coordinate schema with P2503 before final freeze; no hidden currentness bypass or production traffic.

### Definition of Done

Focused synthetic-project checks and independent review verify the stated behavior without live MCP tests, deployment, migration, or held-batch replay. Review dependent next Task before acceptance execution.
