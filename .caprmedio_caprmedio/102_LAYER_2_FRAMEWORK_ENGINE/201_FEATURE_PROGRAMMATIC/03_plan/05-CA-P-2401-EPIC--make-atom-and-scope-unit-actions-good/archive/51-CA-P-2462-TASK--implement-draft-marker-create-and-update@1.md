---
atom_id: CA-P-2462
content_role: Plan
type: Plan
label: Task
work_sequence_number: 51
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
version: 1
updated_at: "2026-10-20T17:34:49.405Z"
---
# Summary

Implement Draft marker Create and Update

## Objective

Implement canonical parser/Create/Update compatibility without broadening canonical ID lookup or allocating numbers for Draft markers. Acceptance: focused parser and lifecycle functional checks, no history or Journal admission gate.

## Details

At most 15 minutes own work; split before extending. Follow the current PROGRAMMATIC M projection and Core07 D276@21, D288@21, D378@16, D446@16, D568@8, D570@12. Preserve unrelated work. Review dependent successors before execution.

### Definition of Done

Implement canonical parser/Create/Update compatibility without broadening canonical ID lookup or allocating numbers for Draft markers. Acceptance: focused parser and lifecycle functional checks, no history or Journal admission gate.

No deployment, live migration/staging, held-batch replay or Methodology map update. Use synthetic golden Projects and nonproduction test instances only.
