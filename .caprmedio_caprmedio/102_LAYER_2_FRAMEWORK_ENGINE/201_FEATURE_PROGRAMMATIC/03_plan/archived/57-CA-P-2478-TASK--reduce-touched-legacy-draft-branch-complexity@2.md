---
atom_id: CA-P-2478
content_role: Plan
type: Plan
label: Task
work_sequence_number: 57
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
  is_decomposition_of: [CA-P-2401]
version: 2
updated_at: "2026-10-20T19:48:03.722Z"
---
# Summary

Reduce touched legacy Draft branch complexity

## Objective

Reduce or explicitly justify the retained complexity increases in _run_create (13 to 14) and update_atom_action (61 to 71), without changing behavior or inflating abstractions.

## Details

At most 15 minutes own work; split before extending. P2477 removed all newly complex function findings and reduced configured total C901 from 17 to 12 versus HEAD 13. Two already-complex touched legacy functions still increased; do not call those values unchanged baseline. CA-C-546 retains this residual quality issue. This is follow-up source-quality work, not a correctness or deployment completion claim. Preserve all validated Draft behavior, pins, rollback and transport callers; at most 15 minutes own work, split before extending.

### Definition of Done

Focused synthetic-project checks and independent review verify the stated behavior without live MCP tests, deployment, migration, or held-batch replay. Review dependent next Task before acceptance execution.

### Dependency review

The revised Stage 1 Epic and deferred Stage 2 Epic are saved. Execute behavior-preserving cohesive extraction only, using the current PROGRAMMATIC M projection and frozen functional corpus. Preserve guards, error/result shapes, byte pins, currentness, history, no-op and recovery. No lint suppression or unrelated legacy refactor. Root owns records and Git; no runtime changes.
